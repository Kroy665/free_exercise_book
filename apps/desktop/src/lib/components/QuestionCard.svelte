<script lang="ts">
  import type { AttemptResult, QuestionView } from "$lib/api";
  import { renderInline } from "$lib/markdown/render";
  import { optionLabel, t } from "$lib/stores/settings.svelte";
  import CircleCheck from "@lucide/svelte/icons/circle-check";
  import CircleX from "@lucide/svelte/icons/circle-x";

  interface Props {
    q: QuestionView;
    selected: number | null;
    result: AttemptResult | null;
    onselect: (i: number) => void;
  }
  let { q, selected, result, onselect }: Props = $props();

  // Assertion-reason questions use the four standard options supplied by the app.
  const options = $derived(q.options ?? [0, 1, 2, 3].map((i) => t(`ar.${i}`)));
  const label = (i: number) => optionLabel(i, q.lang);

  function state(i: number): string {
    if (!result) return i === selected ? "selected" : "";
    if (i === result.answer) return "correct";
    if (i === selected) return "wrong";
    return "dim";
  }
</script>

<article class="qcard" lang={q.lang}>
  {#if q.stem}
    <p class="stem">{@html renderInline(q.stem)}</p>
  {/if}

  {#if q.kind === "assertion-reason"}
    <div class="ar">
      <p><strong>{t("q.assertion")}:</strong> {@html renderInline(q.assertion ?? "")}</p>
      <p><strong>{t("q.reason")}:</strong> {@html renderInline(q.reason ?? "")}</p>
    </div>
  {:else if q.kind === "match" && q.left && q.right}
    <table class="match">
      <thead><tr><th>{t("q.list1")}</th><th>{t("q.list2")}</th></tr></thead>
      <tbody>
        {#each q.left as l, i (i)}
          <tr><td>{l}</td><td>{q.right[i] ?? ""}</td></tr>
        {/each}
      </tbody>
    </table>
  {:else if q.statements || q.items}
    <div class="list">
      {#each q.statements ?? q.items ?? [] as s, i (i)}
        <p>{@html renderInline(s)}</p>
      {/each}
    </div>
  {/if}

  {#if q.question}
    <p class="stem">{@html renderInline(q.question)}</p>
  {/if}

  <div class="options" role="radiogroup" aria-label={t("q.options")}>
    {#each options as opt, i (i)}
      {@const s = state(i)}
      <button
        class="opt {s}"
        role="radio"
        aria-checked={i === selected}
        disabled={!!result}
        onclick={() => onselect(i)}
      >
        <span class="label">{label(i)}</span>
        <span class="text">{@html renderInline(opt)}</span>
        {#if s === "correct"}
          <CircleCheck size={20} aria-hidden="true" />
          <span class="sr-only">{t("q.correct_answer")}</span>
        {:else if s === "wrong"}
          <CircleX size={20} aria-hidden="true" />
          <span class="sr-only">{t("q.your_answer")}</span>
        {/if}
      </button>
    {/each}
  </div>
</article>

<style>
  .qcard {
    max-width: var(--read-width);
  }
  .stem {
    font-size: 1.125rem;
    font-weight: 500;
  }
  .ar,
  .list {
    background: var(--surface-2);
    border-radius: var(--radius-sm);
    padding: var(--space-3) var(--space-4);
    margin-bottom: var(--space-4);
  }
  .ar p:last-child,
  .list p:last-child {
    margin-bottom: 0;
  }
  .match {
    border-collapse: collapse;
    margin-bottom: var(--space-4);
    min-width: 60%;
  }
  .match th,
  .match td {
    border: 1px solid var(--border);
    padding: var(--space-2) var(--space-3);
    text-align: left;
  }
  .match th {
    background: var(--surface-2);
  }
  .options {
    display: grid;
    gap: var(--space-2);
  }
  .opt {
    display: flex;
    align-items: center;
    gap: var(--space-3);
    width: 100%;
    min-height: 48px;
    padding: var(--space-2) var(--space-3);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    background: var(--surface);
    color: var(--text);
    font: inherit;
    text-align: left;
    cursor: pointer;
    transition: border-color var(--dur-fast) var(--ease), background var(--dur-fast) var(--ease);
  }
  .opt:hover:not(:disabled) {
    border-color: var(--accent);
  }
  .opt:disabled {
    cursor: default;
  }
  .label {
    flex: none;
    display: grid;
    place-items: center;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    border: 1px solid var(--border);
    font-weight: 600;
    font-size: 0.875rem;
  }
  .text {
    flex: 1;
  }
  .selected {
    border: 2px solid var(--accent);
  }
  .selected .label {
    background: var(--accent);
    border-color: var(--accent);
    color: var(--accent-fg);
  }
  .correct {
    background: var(--correct-bg);
    border-color: var(--correct);
    color: var(--text);
  }
  .correct .label,
  .correct :global(svg) {
    border-color: var(--correct);
    color: var(--correct);
  }
  .wrong {
    background: var(--wrong-bg);
    border-color: var(--wrong);
  }
  .wrong .label,
  .wrong :global(svg) {
    border-color: var(--wrong);
    color: var(--wrong);
  }
  .dim {
    opacity: 0.7;
  }
</style>
