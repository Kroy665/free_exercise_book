<script lang="ts">
  import { api, errorMessage, type AttemptResult, type Grade, type QuestionView } from "$lib/api";
  import { refreshDueBadge } from "$lib/stores/packs.svelte";
  import { renderInline } from "$lib/markdown/render";
  import { optionLabel, settings, t } from "$lib/stores/settings.svelte";
  import { openUrl } from "@tauri-apps/plugin-opener";
  import { untrack } from "svelte";
  import QuestionCard from "./QuestionCard.svelte";
  import ProgressBar from "./ProgressBar.svelte";
  import StatusTag from "./StatusTag.svelte";
  import ErrorBox from "./ErrorBox.svelte";
  import Flag from "@lucide/svelte/icons/flag";
  import BookOpen from "@lucide/svelte/icons/book-open";

  interface Props {
    questions: QuestionView[];
    mode: "practice" | "revise";
    backHref: string;
  }
  let { questions, mode, backHref }: Props = $props();

  const REPO = "https://github.com/Kroy665/free_exercise_book";

  // Parent re-mounts this component (via {#key}) when the question set changes.
  let queue = $state<QuestionView[]>(untrack(() => [...questions]));
  let index = $state(0);
  let selected = $state<number | null>(null);
  let result = $state<AttemptResult | null>(null);
  let results = $state<{ q: QuestionView; correct: boolean }[]>([]);
  let finished = $state(false);
  let busy = $state(false);
  let error = $state<string | null>(null);
  let startedAt = performance.now();

  const q = $derived(queue[index]);
  const isLast = $derived(index === queue.length - 1);
  const score = $derived(results.filter((r) => r.correct).length);
  const wrong = $derived(results.filter((r) => !r.correct).map((r) => r.q));

  function start(list: QuestionView[]) {
    queue = list;
    index = 0;
    selected = null;
    result = null;
    results = [];
    finished = false;
    startedAt = performance.now();
  }

  async function check() {
    if (selected === null || result || busy) return;
    busy = true;
    error = null;
    try {
      const ms = Math.round(performance.now() - startedAt);
      result = await api.practiceRecord(q.id, selected, ms, mode);
      results.push({ q, correct: result.correct });
    } catch (e) {
      error = errorMessage(e);
    } finally {
      busy = false;
    }
  }

  // Revision: after a correct answer the user grades recall; that schedules the next review.
  const grading = $derived(mode === "revise" && !!result?.correct && !!result?.srs);

  async function gradeAndNext(g: Grade) {
    if (busy) return;
    busy = true;
    try {
      await api.grade(q.id, g);
      refreshDueBadge();
      next();
    } catch (e) {
      error = errorMessage(e);
    } finally {
      busy = false;
    }
  }

  function interval(secs: number): string {
    if (secs < 3600) return `${Math.max(1, Math.round(secs / 60))} min`;
    if (secs < 86400) return `${Math.round(secs / 3600)} h`;
    const d = Math.round(secs / 86400);
    if (d < 31) return `${d} d`;
    if (d < 365) return `${Math.round(d / 30)} mo`;
    return `${(d / 365).toFixed(1)} y`;
  }

  function next() {
    if (!result) return;
    if (mode === "revise" && !result.correct) refreshDueBadge();
    if (isLast) {
      finished = true;
      return;
    }
    index += 1;
    selected = null;
    result = null;
    startedAt = performance.now();
  }

  function report(question: QuestionView) {
    const title = `Content error: ${question.id}`;
    const body = `**Question:** \`${question.id}\` (language: ${question.lang})\n\n**What is wrong?**\n\n<!-- Describe the error and, if possible, a source. -->\n`;
    const url = `${REPO}/issues/new?labels=content-error&title=${encodeURIComponent(title)}&body=${encodeURIComponent(body)}`;
    openUrl(url).catch(() => window.open(url, "_blank"));
  }

  function onkeydown(e: KeyboardEvent) {
    if (finished || e.metaKey || e.ctrlKey || e.altKey) return;
    const el = e.target as HTMLElement;
    if (el.closest("input, textarea, select")) return;
    const k = e.key.toLowerCase();
    const idx = "1234".indexOf(k) >= 0 ? Number(k) - 1 : "abcd".indexOf(k);
    if (grading && "1234".includes(k)) {
      e.preventDefault();
      gradeAndNext((["again", "hard", "good", "easy"] as const)[Number(k) - 1]);
    } else if (idx >= 0 && !result) {
      selected = idx;
      e.preventDefault();
    } else if (e.key === "Enter") {
      e.preventDefault();
      if (grading) gradeAndNext("good");
      else if (result) next();
      else check();
    }
  }
</script>

<svelte:window {onkeydown} />

{#if finished}
  <section class="card summary" aria-live="polite">
    <h2>{t("summary.title")}</h2>
    <p class="score">{t("summary.score", { c: score, n: results.length })}</p>
    {#if wrong.length}
      <h3>{t("summary.review")}</h3>
      <ul>
        {#each wrong as w (w.id)}
          <li>{@html renderInline(w.stem ?? w.assertion ?? w.id)}</li>
        {/each}
      </ul>
    {/if}
    <div class="actions">
      {#if wrong.length}
        <button class="btn btn-primary" onclick={() => start([...wrong])}>{t("summary.retry_wrong")}</button>
      {/if}
      <button class="btn" onclick={() => start([...questions])}>{t("summary.again")}</button>
      <a class="btn btn-ghost" href={backHref}>{t("summary.back")}</a>
    </div>
  </section>
{:else if q}
  <section class="session">
    <header class="head">
      <span class="muted">{t("q.progress", { i: index + 1, n: queue.length })}</span>
      <StatusTag status={q.status} />
    </header>
    <ProgressBar value={index + (result ? 1 : 0)} max={queue.length} label={t("q.progress", { i: index + 1, n: queue.length })} />

    {#if q.lang !== settings.lang}
      <p class="fallback muted">{t("q.fallback")}</p>
    {/if}

    <div class="body">
      <QuestionCard {q} {selected} {result} onselect={(i) => (selected = i)} />
    </div>

    {#if error}
      <ErrorBox message={error} onretry={check} />
    {/if}

    {#if result}
      <div class="feedback {result.correct ? 'ok' : 'bad'}" aria-live="polite">
        <strong>
          {result.correct ? t("q.correct") : t("q.wrong", { label: optionLabel(result.answer, q.lang) })}
        </strong>
        {#if mode === "revise" && !result.correct}
          <p class="muted small">{t("srs.wrong_note", { t: "10 min" })}</p>
        {/if}
        <h3>{t("q.explanation")}</h3>
        <p lang={q.lang}>{@html renderInline(q.explanation)}</p>
        <div class="links">
          {#if q.refs[0]}
            <a class="btn btn-ghost" href="/topic/{q.topic_id}#{q.refs[0]}">
              <BookOpen size={18} aria-hidden="true" />{t("q.revise_notes")}
            </a>
          {/if}
          <button class="btn btn-ghost" onclick={() => report(q)}>
            <Flag size={18} aria-hidden="true" />{t("q.report")}
          </button>
        </div>
      </div>
    {/if}

    <footer class="foot">
      <span class="muted hint">{grading ? t("srs.keys") : t("q.keys")}</span>
      {#if grading && result?.srs}
        <div class="grades" role="group" aria-label={t("srs.how")}>
          <span class="muted small">{t("srs.how")}</span>
          {#each [["again", result.srs.again], ["hard", result.srs.hard], ["good", result.srs.good], ["easy", result.srs.easy]] as const as [g, secs], i (g)}
            <button class="btn grade {g === 'good' ? 'btn-primary' : ''}" disabled={busy} onclick={() => gradeAndNext(g)}>
              <span>{i + 1}. {t(`srs.${g}`)}</span><span class="when">{interval(secs)}</span>
            </button>
          {/each}
        </div>
      {:else if result}
        <button class="btn btn-primary" onclick={next}>{isLast ? t("q.finish") : t("q.next")}</button>
      {:else}
        <button class="btn btn-primary" disabled={selected === null || busy} onclick={check}>{t("q.check")}</button>
      {/if}
    </footer>
  </section>
{/if}

<style>
  .session {
    max-width: var(--read-width);
  }
  .head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: var(--space-2);
  }
  .body {
    margin-top: var(--space-5);
  }
  .fallback {
    margin-top: var(--space-3);
    font-size: 0.875rem;
  }
  .feedback {
    margin-top: var(--space-5);
    padding: var(--space-4);
    border-radius: var(--radius-md);
    border: 1px solid;
  }
  .feedback h3 {
    font-size: 1rem;
    margin-top: var(--space-3);
  }
  .ok {
    background: var(--correct-bg);
    border-color: var(--correct);
  }
  .ok strong {
    color: var(--correct);
  }
  .bad {
    background: var(--wrong-bg);
    border-color: var(--wrong);
  }
  .bad strong {
    color: var(--wrong);
  }
  .links {
    display: flex;
    gap: var(--space-2);
    flex-wrap: wrap;
  }
  .foot {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: var(--space-4);
    margin-top: var(--space-5);
  }
  .foot {
    flex-wrap: wrap;
  }
  .grades {
    order: -1;
    flex: 1 1 100%;
    display: flex;
    align-items: center;
    gap: var(--space-2);
    justify-content: flex-end;
  }
  .grades > span {
    margin-right: auto;
  }
  .grade {
    flex-direction: column;
    gap: 0;
    min-height: 44px;
    line-height: 1.2;
  }
  .when {
    font-size: 0.75rem;
    opacity: 0.8;
  }
  .small {
    font-size: 0.8125rem;
  }
  .hint {
    font-size: 0.8125rem;
  }
  .summary {
    max-width: var(--read-width);
  }
  .score {
    font-size: 1.5rem;
    font-weight: 600;
  }
  .actions {
    display: flex;
    gap: var(--space-2);
    flex-wrap: wrap;
    margin-top: var(--space-4);
  }
</style>
