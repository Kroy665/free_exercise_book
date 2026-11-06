<script lang="ts">
  import { page } from "$app/state";
  import { errorMessage, testsApi, type ReviewItem, type TestResult } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import QuestionCard from "$lib/components/QuestionCard.svelte";
  import { duration } from "$lib/format";
  import { renderInline } from "$lib/markdown/render";
  import { settings, t } from "$lib/stores/settings.svelte";
  import BookOpen from "@lucide/svelte/icons/book-open";

  type Filter = "all" | "wrong" | "unanswered" | "marked" | "correct";
  let r = $state<TestResult | null>(null);
  let error = $state<string | null>(null);
  let filter = $state<Filter>("all");
  const id = $derived(Number(page.params.id));

  async function load(testId: number, lang: string) {
    error = null;
    try {
      r = await testsApi.result(testId, lang);
    } catch (e) {
      error = errorMessage(e);
    }
  }

  $effect(() => {
    load(id, settings.lang);
  });

  const numbered = $derived(r?.review.map((item, i) => ({ item, n: i + 1 })) ?? []);
  const shown = $derived(
    numbered.filter(({ item }) =>
      filter === "all" ? true : filter === "marked" ? item.marked : item.outcome === filter,
    ),
  );
  const count = (f: Filter) =>
    numbered.filter(({ item }) => (f === "all" ? true : f === "marked" ? item.marked : item.outcome === f)).length;

  const result = (item: ReviewItem) => ({ correct: item.outcome === "correct", answer: item.question.answer });
</script>

<div class="page">
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <a href="/tests">{t("tests.title")}</a> › <a href="/tests/{id}/result">{t("res.title")}</a> › {t("rev.title")}
  </nav>
  {#if error}
    <ErrorBox message={error} onretry={() => load(id, settings.lang)} />
  {:else if !r}
    <p class="muted">{t("common.loading")}</p>
  {:else}
    <h1>{r.title}</h1>
    <div class="filters chrome" role="tablist">
      {#each ["all", "wrong", "unanswered", "marked", "correct"] as const as f (f)}
        <button role="tab" aria-selected={filter === f} class="btn {filter === f ? 'btn-primary' : ''}" onclick={() => (filter = f)}>
          {t(`rev.filter.${f}`)} ({count(f)})
        </button>
      {/each}
    </div>

    {#each shown as { item, n } (item.question.id)}
      <article class="card item">
        <header class="ihead">
          <strong>Q{n}</strong>
          {#if r.sections.length > 1}<span class="muted small">{item.section}</span>{/if}
          <span class="tag {item.outcome}">{t(`res.${item.outcome}`)}</span>
          {#if item.marked}<span class="tag marked">{t("rev.filter.marked")}</span>{/if}
          <span class="muted small time">{t("rev.time", { t: duration(item.time_ms) })}</span>
        </header>
        <QuestionCard q={item.question} selected={item.chosen} result={result(item)} onselect={() => {}} />
        <div class="expl">
          <h3>{t("q.explanation")}</h3>
          <p lang={item.question.lang}>{@html renderInline(item.question.explanation)}</p>
          {#if item.question.refs[0]}
            <a class="btn btn-ghost" href="/topic/{item.question.topic_id}#{item.question.refs[0]}">
              <BookOpen size={16} aria-hidden="true" />{t("q.revise_notes")}
            </a>
          {/if}
        </div>
      </article>
    {:else}
      <p class="muted">{t("rev.empty")}</p>
    {/each}
  {/if}
</div>

<style>
  .page {
    max-width: 860px;
  }
  .filters {
    display: flex;
    gap: var(--space-2);
    flex-wrap: wrap;
    margin: var(--space-4) 0;
  }
  .item {
    margin-bottom: var(--space-4);
  }
  .ihead {
    display: flex;
    align-items: center;
    gap: var(--space-2);
    margin-bottom: var(--space-3);
  }
  .time {
    margin-left: auto;
  }
  .tag {
    font-size: 0.75rem;
    padding: 0 var(--space-2);
    border-radius: 999px;
    background: var(--surface-2);
  }
  .tag.correct {
    color: var(--correct);
    background: var(--correct-bg);
  }
  .tag.wrong {
    color: var(--wrong);
    background: var(--wrong-bg);
  }
  .tag.marked {
    color: var(--review);
    background: var(--review-bg);
  }
  .expl {
    margin-top: var(--space-4);
    border-top: 1px solid var(--border);
    padding-top: var(--space-3);
  }
  .expl h3 {
    font-size: 1rem;
  }
  .small {
    font-size: 0.8125rem;
  }
</style>
