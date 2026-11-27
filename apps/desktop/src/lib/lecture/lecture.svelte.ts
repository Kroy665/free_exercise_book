// Lecture player: plays a topic's teacher script step by step, tells the notes which part
// to highlight, and pauses at questions. Steps use the audio made ahead of time for the
// topic (downloaded when it opens); steps without it are spoken by the built-in Kokoro voice.
import { api, assistantApi, type Lecture } from "$lib/api";
import { chunks } from "$lib/tts/speech";
import { settings } from "$lib/stores/settings.svelte";
import { audioContext, onSpeak, stop as stopTts, synth, voiceReady } from "$lib/tts/tts.svelte";

export type LecturePhase = "idle" | "preparing" | "playing" | "paused" | "question" | "answer" | "done";

export const lecture = $state({
  topicId: "",
  data: null as Lecture | null,
  index: 0,
  phase: "idle" as LecturePhase,
  /** Set when the student has answered the step's question (its spoken answer follows). */
  answered: false,
  error: "",
  /** Background preparation of the whole lecture's audio: chunks done / all chunks. */
  prepared: 0,
  toPrepare: 0,
});

let run = 0;
// Jumping to another step drops synthesis queued for the old one.
let gen = 0;
function queued(text: string): Promise<Float32Array> {
  const mine = gen;
  return synth(text, { live: () => mine === gen });
}
let sources: AudioBufferSourceNode[] = [];
// Synthesised audio per text, so the next step is ready before it is needed.
const cache = new Map<string, Promise<Float32Array>[]>();
const ready = new Set<string>();

/** How a step's text is split for the voice (the same for playing and preparing). */
function parts(text: string): string[] {
  const all = chunks(text, 220);
  // A short first part, so speech starts quickly.
  const first = all[0] && all[0].length > 80 ? chunks(all[0], 80) : all.slice(0, 1);
  return [...first, ...all.slice(1)];
}

// Texts of the open lecture that have a ready-made clip, and the download that finds them.
let covered = new Set<string>();
let audioReady: Promise<void> = Promise.resolve();

function texts(data: Lecture): string[] {
  return data.segments.flatMap((s) => (s.answer ? [s.say, s.answer] : [s.say]));
}

// Steps without a ready-made clip are made by Kokoro, which takes minutes for a lecture, so
// that starts in the background when the topic opens, into the voice's disk cache.
// Playback goes ahead of it.
let prep = 0;
export function stopPreparing() {
  prep++;
  lecture.prepared = lecture.toPrepare = 0;
}

async function prepare(data: Lecture, topicId: string) {
  const mine = ++prep;
  lecture.prepared = lecture.toPrepare = 0;
  const all = texts(data);
  audioReady = api
    .lectureAudioPrepare(topicId, all)
    .then((have) => {
      if (mine === prep) covered = new Set(all.filter((_, k) => have[k]));
    })
    .catch(() => {});
  await audioReady;
  if (mine !== prep) return;
  const rest = all.filter((t) => !covered.has(t)).flatMap(parts);
  if (!rest.length) {
    lecture.toPrepare = lecture.prepared = 1; // "voice ready"
    return;
  }
  lecture.toPrepare = rest.length;
  try {
    // Only when the voice is downloaded; never ask for the download from here.
    if (!(await assistantApi.ttsStatus(settings.tts_voice)).ready || mine !== prep) {
      lecture.toPrepare = 0;
      return;
    }
  } catch {
    lecture.toPrepare = 0;
    return;
  }
  const live = () => mine === prep;
  for (const p of rest) {
    synth(p, { background: true, live }).then(
      () => { if (live()) lecture.prepared++; },
      () => {},
    );
  }
}

function clip(text: string): Promise<Float32Array>[] {
  let c = cache.get(text);
  if (!c) {
    if (covered.has(text)) {
      const topic = lecture.topicId;
      // The ready-made clip; Kokoro if it cannot be read after all.
      c = [api.lectureAudioClip(topic, text).then(async (s) => {
        if (s.length) return s;
        const own = await Promise.all(parts(text).map((p) => queued(p)));
        const out = new Float32Array(own.reduce((n, a) => n + a.length, 0));
        let at = 0;
        for (const a of own) { out.set(a, at); at += a.length; }
        return out;
      })];
    } else {
      c = parts(text).map((p) => queued(p));
    }
    // A failed chunk must not stay cached, or every retry would replay the failure.
    for (const pr of c) pr.catch(() => { if (cache.get(text) === c) cache.delete(text); });
    // Remember when every chunk is ready, so a jump keeps finished audio.
    Promise.all(c).then(() => ready.add(text), () => {});
    cache.set(text, c);
    if (cache.size > 12) {
      const old = cache.keys().next().value!;
      cache.delete(old);
      ready.delete(old);
    }
  }
  return c;
}

/** Play `text` to the end (resolves early if the lecture is stopped or moved). */
async function say(text: string, mine: number): Promise<boolean> {
  const ctx = audioContext();
  if (ctx.state === "suspended" && lecture.phase !== "paused") await ctx.resume();
  for (const part of clip(text)) {
    const samples = await part;
    if (mine !== run) return false;
    if (!samples.length) continue;
    const buf = ctx.createBuffer(1, samples.length, 24_000);
    buf.copyToChannel(new Float32Array(samples), 0);
    const src = ctx.createBufferSource();
    src.buffer = buf;
    src.connect(ctx.destination);
    sources.push(src);
    if (lecture.phase === "preparing") lecture.phase = "playing";
    await new Promise<void>((resolve) => {
      src.onended = () => resolve();
      src.start();
    });
    sources = sources.filter((s) => s !== src);
    if (mine !== run) return false;
  }
  // A breath between steps.
  await new Promise((r) => setTimeout(r, 350));
  return mine === run;
}

/** Stop playback. `drop`: also discard queued synthesis (when jumping elsewhere). */
function halt(drop = true) {
  run++;
  if (drop) {
    gen++;
    // Queued chunks are now cancelled: forget texts that were not finished.
    for (const t of [...cache.keys()]) if (!ready.has(t)) cache.delete(t);
  }
  for (const s of sources) {
    try { s.stop(); } catch { /* already stopped */ }
  }
  sources = [];
}

// "Listen" elsewhere in the app: stop the lecture's audio (paused, not suspended on the
// shared AudioContext, which "Listen" resumes) so the two voices never overlap.
onSpeak(() => {
  if (["preparing", "playing", "answer", "paused"].includes(lecture.phase)) {
    halt();
    lecture.phase = "paused";
  }
});

export function load(topicId: string, data: Lecture | null) {
  if (lecture.topicId === topicId && lecture.data === data) return;
  halt();
  cache.clear();
  ready.clear();
  Object.assign(lecture, { topicId, data, index: 0, phase: "idle", answered: false, error: "" });
  covered = new Set();
  audioReady = Promise.resolve();
  if (data) prepare(data, topicId);
  else stopPreparing();
}

/** After the voice is downloaded: prepare the open lecture's audio. */
export function prepareAgain() {
  if (lecture.data && !lecture.toPrepare) prepare(lecture.data, lecture.topicId);
}

/** Play from step `i` onwards. */
export async function playFrom(i: number, drop = true) {
  const data = lecture.data;
  if (!data) return;
  halt(drop);
  stopTts();
  const mine = run;
  lecture.phase = "preparing";
  // Wait (briefly) for the topic's ready-made audio, so it is used from the first step.
  await Promise.race([audioReady, new Promise((r) => setTimeout(r, 10_000))]);
  if (mine !== run) return;
  // Kokoro is needed only for steps without a ready-made clip.
  if (texts(data).some((t) => !covered.has(t))) {
    if (!(await voiceReady(() => playFrom(i)))) {
      if (mine === run) lecture.phase = "idle";
      return;
    }
    if (mine !== run) return;
    prepareAgain();
  }
  const ctx = audioContext();
  if (ctx.state === "suspended") await ctx.resume();
  for (let k = Math.max(0, i); k < data.segments.length; k++) {
    const seg = data.segments[k];
    lecture.index = k;
    lecture.answered = false;
    lecture.phase = "preparing";
    lecture.error = "";
    // Start making the next step's audio while this one plays.
    const next = data.segments[k + 1];
    try {
      const done = say(seg.say, mine);
      if (next) clip(next.say);
      if (!(await done)) return;
      if (seg.question) {
        lecture.phase = "question";
        return; // resumes from answerGiven()
      }
    } catch (e) {
      if (mine !== run) return;
      lecture.error = String((e as Error)?.message ?? e);
      lecture.phase = "paused";
      return;
    }
  }
  if (mine === run) lecture.phase = "done";
}

/** The student answered (or skipped) the question: speak the answer, then carry on. */
export async function answerGiven() {
  const data = lecture.data;
  const seg = data?.segments[lecture.index];
  if (!data || !seg?.answer) return;
  halt(false);
  const mine = run;
  lecture.answered = true;
  lecture.phase = "answer";
  try {
    if (!(await say(seg.answer, mine))) return;
  } catch (e) {
    lecture.error = String((e as Error)?.message ?? e);
    lecture.phase = "paused";
    return;
  }
  if (mine === run) playFrom(lecture.index + 1, false);
}

export async function pause() {
  if (lecture.phase !== "playing" && lecture.phase !== "preparing" && lecture.phase !== "answer") return;
  await audioContext().suspend();
  lecture.phase = "paused";
}

export async function resume() {
  if (lecture.phase !== "paused") return;
  if (sources.length) {
    lecture.phase = lecture.answered ? "answer" : "playing";
    await audioContext().resume();
  } else {
    playFrom(lecture.index);
  }
}

export function stopLecture() {
  halt();
  audioContext().resume().catch(() => {});
  lecture.phase = "idle";
}

export function go(i: number) {
  if (!lecture.data) return;
  const k = Math.min(Math.max(0, i), lecture.data.segments.length - 1);
  playFrom(k);
}
