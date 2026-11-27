<script lang="ts">
  // The teacher: plays the topic's lecture, shows what is being said, and puts the
  // lecture's questions beside the notes.
  import { tick } from "svelte";
  import { api, errorMessage, type AttemptResult, type QuestionView } from "$lib/api";
  import { renderRich } from "$lib/markdown/render";
  import { settings } from "$lib/stores/settings.svelte";
  import { askAbout } from "$lib/stores/assistant.svelte";
  import { lecture, playFrom, pause, resume, stopLecture, go, answerGiven } from "$lib/lecture/lecture.svelte";
  import QuestionCard from "./QuestionCard.svelte";
  import VoiceStatus from "./VoiceStatus.svelte";
  import Play from "@lucide/svelte/icons/play";
  import Pause from "@lucide/svelte/icons/pause";
  import SkipBack from "@lucide/svelte/icons/skip-back";
  import SkipForward from "@lucide/svelte/icons/skip-forward";
  import X from "@lucide/svelte/icons/x";
  import LoaderCircle from "@lucide/svelte/icons/loader-circle";
  import MessageCircleQuestion from "@lucide/svelte/icons/message-circle-question";
  import GraduationCap from "@lucide/svelte/icons/graduation-cap";

  let { topicId, onclose }: { topicId: string; onclose: () => void } = $props();

  const segs = $derived(lecture.data?.segments ?? []);
  const seg = $derived(segs[lecture.index]);
  const total = $derived(segs.length);

  // Questions of this topic, for the steps that ask one.
  let questions = $state<QuestionView[]>([]);
  $effect(() => {
    const id = topicId;
    api.practiceQuestions(id, settings.lang).then((q) => (questions = q)).catch(() => {});
  });
  const question = $derived(seg?.question ? questions.find((q) => q.id === `${topicId}/${seg.question}`) : undefined);

  let selected = $state<number | null>(null);
  let result = $state<AttemptResult | null>(null);
  let qError = $state("");
  let showSolution = $state(false);
  let askedAt = 0;
  // New step: clear the question state.
  $effect(() => {
    void lecture.index;
    askedAt = performance.now();
    selected = null;
    result = null;
    qError = "";
    showSolution = false;
  });

  async function check() {
    if (!question || selected === null || result) return;
    try {
      const ms = Math.min(Math.round(performance.now() - askedAt), 3_600_000);
      result = await api.practiceRecord(question.id, selected, ms, "practice");
      answerGiven();
    } catch (e) {
      qError = errorMessage(e);
    }
  }
  function reveal() {
    if (!question) return;
    result = { correct: false, answer: question.answer, srs: null };
    answerGiven();
  }

  function askTeacher() {
    pause();
    const text = seg?.focus ?? seg?.say ?? "";
    askAbout(text, "I didn't understand this part of the lecture. Please explain it another way, with a small example.");
  }

  // Keep the current step in view in the transcript.
  let list = $state<HTMLElement | null>(null);
  $effect(() => {
    void lecture.index;
    tick().then(() => list?.querySelector(".step.now")?.scrollIntoView({ block: "nearest", behavior: "smooth" }));
  });

  const playing = $derived(lecture.phase === "playing" || lecture.phase === "preparing" || lecture.phase === "answer");

  function toggle() {
    if (playing) pause();
    else if (lecture.phase === "paused") resume();
    else if (lecture.phase === "question") answerGiven();
    else playFrom(lecture.phase === "done" ? 0 : lecture.index);
  }

  function onkeydown(e: KeyboardEvent) {
    if ((e.target as HTMLElement).closest("input, textarea, select") || e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key === " " && lecture.phase !== "question") { e.preventDefault(); toggle(); }
    else if (e.key === "ArrowRight" && e.shiftKey) { e.preventDefault(); go(lecture.index + 1); }
    else if (e.key === "ArrowLeft" && e.shiftKey) { e.preventDefault(); go(lecture.index - 1); }
  }
</script>

<svelte:window {onkeydown} />

<aside class="lecture" aria-label="Lecture">
  <header>
    <GraduationCap size={18} aria-hidden="true" />
    <strong>Lecture</strong>
    <span class="muted small">{total ? `Step ${lecture.index + 1} of ${total}` : ""}</span>
    <span class="spacer"></span>
    <button class="btn btn-ghost icon" aria-label="Close lecture" title="Close lecture" onclick={() => { stopLecture(); onclose(); }}>
      <X size={18} aria-hidden="true" />
    </button>
  </header>

  <div class="controls">
    <button class="btn btn-ghost icon" aria-label="Previous step" title="Previous step (Shift+←)" onclick={() => go(lecture.index - 1)} disabled={lecture.index === 0}>
      <SkipBack size={18} aria-hidden="true" />
    </button>
    <button class="btn btn-primary play" onclick={toggle} aria-label={playing ? "Pause" : "Play"} title="Play / pause (Space)">
      {#if lecture.phase === "preparing"}
        <LoaderCircle size={18} class="spin" aria-hidden="true" /> Preparing…
      {:else if playing}
        <Pause size={18} aria-hidden="true" /> Pause
      {:else if lecture.phase === "idle"}
        <Play size={18} aria-hidden="true" /> {lecture.index ? "Continue" : "Start lecture"}
      {:else if lecture.phase === "done"}
        <Play size={18} aria-hidden="true" /> Play again
      {:else if lecture.phase === "question"}
        <Play size={18} aria-hidden="true" /> Skip question
      {:else}
        <Play size={18} aria-hidden="true" /> Resume
      {/if}
    </button>
    <button class="btn btn-ghost icon" aria-label="Next step" title="Next step (Shift+→)" onclick={() => go(lecture.index + 1)} disabled={lecture.index >= total - 1}>
      <SkipForward size={18} aria-hidden="true" />
    </button>
    <button class="btn btn-ghost ask" onclick={askTeacher} title="Pause and ask about this step">
      <MessageCircleQuestion size={16} aria-hidden="true" /> Ask
    </button>
  </div>
  <progress max={Math.max(1, total)} value={lecture.index + (lecture.phase === "done" ? 1 : 0)}></progress>

  <VoiceStatus />
  {#if lecture.error}<p class="err">Voice: {lecture.error}</p>{/if}

  {#if seg?.question}
    <div class="qbox">
      <p class="qhead"><strong>Your turn</strong> <span class="muted small">Answer, then the teacher explains.</span></p>
      {#if question}
        <QuestionCard q={question} {selected} {result} onselect={(i) => { if (!result) selected = i; }} />
        {#if qError}<p class="err">{qError}</p>{/if}
        {#if !result}
          <div class="row">
            <button class="btn btn-primary" onclick={check} disabled={selected === null}>Check</button>
            <button class="btn btn-ghost" onclick={reveal}>Show me</button>
          </div>
        {:else}
          <p class="verdict" class:ok={result.correct}>{result.correct ? "Correct." : `The answer is option ${"ABCD"[result.answer]}.`}</p>
          <button class="btn btn-ghost small" onclick={() => (showSolution = !showSolution)}>{showSolution ? "Hide" : "Show"} worked solution</button>
          {#if showSolution}<div class="prose solution">{@html renderRich(question.explanation)}</div>{/if}
        {/if}
      {:else}
        <p class="muted small">Loading the question…</p>
      {/if}
    </div>
  {/if}

  <ol class="transcript" bind:this={list}>
    {#each segs as s, i (i)}
      <li class="step" class:now={i === lecture.index} class:past={i < lecture.index}>
        <button class="steptext" onclick={() => go(i)} title="Play from here">
          {s.say}
          {#if s.question}<span class="tag">Question</span>{/if}
        </button>
        {#if i === lecture.index && s.answer && lecture.answered}
          <p class="answertext">{s.answer}</p>
        {/if}
      </li>
    {/each}
  </ol>
</aside>

<style>
  .lecture {
    position: sticky;
    top: var(--space-4);
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
    max-height: calc(100vh - 110px);
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-md, 10px);
    padding: var(--space-3);
    min-width: 0;
  }
  header {
    display: flex;
    align-items: center;
    gap: var(--space-2);
  }
  .spacer {
    flex: 1;
  }
  .icon {
    padding: 0 var(--space-2);
  }
  .controls {
    display: flex;
    align-items: center;
    gap: var(--space-1);
  }
  .play {
    gap: var(--space-1);
    flex: 1;
    justify-content: center;
  }
  .ask {
    gap: var(--space-1);
  }
  progress {
    width: 100%;
    height: 4px;
  }
  .qbox {
    border: 1px solid var(--accent);
    border-radius: var(--radius-sm);
    padding: var(--space-3);
    display: grid;
    gap: var(--space-2);
    overflow-y: auto;
    max-height: 55vh;
    flex: none;
  }
  .qhead {
    margin: 0;
  }
  .row {
    display: flex;
    gap: var(--space-2);
  }
  .verdict {
    margin: 0;
    font-weight: 600;
    color: var(--wrong);
  }
  .verdict.ok {
    color: var(--correct);
  }
  .transcript {
    list-style: none;
    margin: 0;
    padding: 0;
    overflow-y: auto;
    min-height: 120px;
    flex: 1;
    display: grid;
    gap: 2px;
    align-content: start;
  }
  .steptext {
    display: block;
    width: 100%;
    text-align: left;
    background: none;
    border: 0;
    border-left: 3px solid transparent;
    padding: var(--space-2);
    font: inherit;
    font-size: 0.875rem;
    color: var(--text-muted);
    cursor: pointer;
    border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  }
  .steptext:hover {
    background: var(--surface-2);
  }
  .now .steptext {
    color: var(--text);
    font-size: 0.9375rem;
    border-left-color: var(--accent);
    background: var(--accent-soft);
  }
  .past .steptext {
    opacity: 0.7;
  }
  .answertext {
    margin: var(--space-1) 0 0 var(--space-3);
    font-size: 0.875rem;
  }
  .tag {
    display: inline-block;
    margin-left: var(--space-1);
    padding: 0 6px;
    border-radius: 999px;
    font-size: 0.6875rem;
    background: var(--accent);
    color: var(--accent-fg);
  }
  .err {
    color: var(--wrong);
    font-size: 0.875rem;
    margin: 0;
  }
  .small {
    font-size: 0.8125rem;
  }
</style>
