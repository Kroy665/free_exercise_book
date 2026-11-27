// Lecture player: plays a topic's teacher script step by step with the Kokoro voice,
// tells the notes which part to highlight, and pauses at questions.
import type { Lecture } from "$lib/api";
import { chunks } from "$lib/tts/speech";
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
});

let run = 0;
let sources: AudioBufferSourceNode[] = [];
// Synthesised audio per text, so the next step is ready before it is needed.
const cache = new Map<string, Promise<Float32Array>[]>();

function clip(text: string): Promise<Float32Array>[] {
  let c = cache.get(text);
  if (!c) {
    const parts = chunks(text, 220);
    // A short first part, so speech starts quickly.
    const first = parts[0] && parts[0].length > 110 ? chunks(parts[0], 110) : parts.slice(0, 1);
    c = [...first, ...parts.slice(1)].map((p) => synth(p));
    // A failed chunk must not stay cached, or every retry would replay the failure.
    for (const pr of c) pr.catch(() => cache.delete(text));
    cache.set(text, c);
    if (cache.size > 12) cache.delete(cache.keys().next().value!);
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

function halt() {
  run++;
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
  Object.assign(lecture, { topicId, data, index: 0, phase: "idle", answered: false, error: "" });
}

/** Play from step `i` onwards. */
export async function playFrom(i: number) {
  const data = lecture.data;
  if (!data) return;
  halt();
  stopTts();
  const mine = run;
  if (!(await voiceReady(() => playFrom(i)))) return;
  if (mine !== run) return;
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
      if (next) clip(next.say)[0]?.catch(() => {});
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
  halt();
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
  if (mine === run) playFrom(lecture.index + 1);
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
