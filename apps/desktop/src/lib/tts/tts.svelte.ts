// "Listen": read text aloud with Kokoro. Phonemes are made here (espeak-ng in WebAssembly);
// the Rust side runs the speech model natively and returns the audio.
import { invoke } from "@tauri-apps/api/core";
import { listen } from "@tauri-apps/api/event";
import { assistantApi, errorMessage } from "$lib/api";
import { settings } from "$lib/stores/settings.svelte";
import { chunks, toSpeech } from "./speech";
import { phonemize } from "./phonemes";

type Phase = "idle" | "need-download" | "downloading" | "loading" | "speaking" | "error";

export const tts = $state({
  phase: "idle" as Phase,
  /** Which text is being read (a message id or any key the caller chose). */
  key: "",
  missingBytes: 0,
  done: 0,
  total: 0,
  error: "",
});

let ctx: AudioContext | null = null;
// Other players on the same AudioContext (the lecture) register here, so "Listen"
// silences them first instead of talking over them.
const interrupters = new Set<() => void>();
export function onSpeak(fn: () => void) {
  interrupters.add(fn);
}
let run = 0; // bumps on every speak/stop, so stale audio is dropped
let pendingText = "";
/** Called after the voice download finishes (instead of speaking `pendingText`). */
let onReady: (() => void) | null = null;

export function audioContext(): AudioContext {
  ctx ??= new AudioContext();
  return ctx;
}

/** True when the voice files are present; otherwise shows the download prompt. */
export async function voiceReady(then?: () => void): Promise<boolean> {
  const st = await assistantApi.ttsStatus(settings.tts_voice);
  if (st.ready) return true;
  stop();
  tts.phase = "need-download";
  tts.missingBytes = st.missing_bytes;
  pendingText = "";
  onReady = then ?? null;
  return false;
}
let sources: AudioBufferSourceNode[] = [];

listen<{ done: number; total: number }>("tts-progress", (e) => {
  tts.done = e.payload.done;
  tts.total = e.payload.total;
}).catch(() => {});

const RATE = 24_000;

/** 24 kHz mono samples for one short chunk of plain text (Rust runs the model). */
export async function synth(text: string): Promise<Float32Array> {
  const voice = settings.tts_voice;
  const phonemes = await phonemize(text, voice.startsWith("b"));
  if (!phonemes) return new Float32Array();
  const bytes = await invoke<ArrayBuffer>("tts_synth", { voice, phonemes, speed: Number(settings.tts_speed) || 1 });
  return new Float32Array(bytes);
}

/** Read `markdown` aloud. Speaking the same key again stops it. */
export async function speak(key: string, markdown: string) {
  if (tts.key === key && (tts.phase === "speaking" || tts.phase === "loading")) return stop();
  stop();
  for (const fn of interrupters) fn();
  const mine = ++run;
  tts.key = key;
  tts.error = "";
  try {
    const st = await assistantApi.ttsStatus(settings.tts_voice);
    if (mine !== run) return;
    if (!st.ready) {
      tts.phase = "need-download";
      tts.missingBytes = st.missing_bytes;
      pendingText = markdown;
      return;
    }
    // A short first chunk, so speech starts quickly; longer ones after.
    const all = chunks(toSpeech(markdown), 260);
    const parts = all.length && all[0].length > 120 ? [...chunks(all[0], 120), ...all.slice(1)] : all;
    if (!parts.length) { tts.phase = "idle"; tts.key = ""; return; }
    tts.phase = "loading";
    ctx = audioContext();
    if (ctx.state === "suspended") await ctx.resume();
    let when = 0;
    let next = synth(parts[0]);
    for (let i = 0; i < parts.length; i++) {
      const samples = await next;
      if (mine !== run) return;
      // Synthesise the next chunk while this one plays.
      if (i + 1 < parts.length) next = synth(parts[i + 1]);
      if (!samples.length) continue;
      const buf = ctx.createBuffer(1, samples.length, RATE);
      buf.copyToChannel(new Float32Array(samples), 0);
      const src = ctx.createBufferSource();
      src.buffer = buf;
      src.connect(ctx.destination);
      when = Math.max(when, ctx.currentTime + 0.03);
      src.start(when);
      when += buf.duration + 0.15;
      sources.push(src);
      tts.phase = "speaking";
    }
    const left = Math.max(0, when - ctx.currentTime);
    setTimeout(() => {
      if (mine === run) { tts.phase = "idle"; tts.key = ""; sources = []; }
    }, left * 1000);
  } catch (e) {
    if (mine !== run) return;
    tts.phase = "error";
    tts.error = errorMessage(e);
  }
}

export function stop() {
  run++;
  for (const s of sources) {
    try { s.stop(); } catch { /* already stopped */ }
  }
  sources = [];
  if (tts.phase !== "downloading") {
    tts.phase = "idle";
    tts.key = "";
  }
}

/** Download the speech files (asked for after `speak` found them missing), then speak. */
export async function downloadVoice() {
  const key = tts.key, text = pendingText;
  tts.phase = "downloading";
  tts.done = 0;
  tts.total = tts.missingBytes;
  try {
    await assistantApi.ttsDownload(settings.tts_voice);
    tts.phase = "idle";
    tts.key = "";
    const then = onReady;
    onReady = null;
    if (then) then();
    else if (text) await speak(key, text);
  } catch (e) {
    tts.phase = "error";
    tts.error = errorMessage(e);
  }
}

export function cancelDownloadPrompt() {
  onReady = null;
  tts.phase = "idle";
  tts.key = "";
  pendingText = "";
}
