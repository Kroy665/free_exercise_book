<script lang="ts">
  import { page } from "$app/state";
  import { errorMessage, testsApi, type TestResult } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import ProgressBar from "$lib/components/ProgressBar.svelte";
  import { date, duration, num } from "$lib/format";
  import { settings, t } from "$lib/stores/settings.svelte";

  let r = $state<TestResult | null>(null);
  let error = $state<string | null>(null);
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

  const s = $derived(r?.summary);
  const pct = $derived(s && s.max_score > 0 ? Math.max(0, Math.round((s.score / s.max_score) * 100)) : 0);
  // Marks lost to negative marking = (marks for correct answers) - score.
  const negCost = $derived.by(() => {
    if (!r || !s) return 0;
    let gained = 0;
    for (const sec of r.sections) gained += sec.correct * (sec.max_score / Math.max(1, sec.correct + sec.wrong + sec.unanswered));
    return Math.round((gained - s.score) * 100) / 100;
  });
</script>

<div class="page">
  <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/tests">{t("tests.title")}</a> › {t("res.title")}</nav>
  {#if error}
    <ErrorBox message={error} onretry={() => load(id, settings.lang)} />
  {:else if !r || !s}
    <p class="muted">{t("common.loading")}</p>
  {:else}
    <h1>{r.title}</h1>
    {#if r.submitted_at}<p class="muted">{date(r.submitted_at)}</p>{/if}

    <div class="card hero">
      <div class="score">
        <span class="muted small">{t("res.score")}</span>
        <span class="big">{num(s.score)} <span class="of">/ {num(s.max_score)}</span></span>
        <ProgressBar value={pct} max={100} label={t("res.score")} />
      </div>
      <div class="tiles">
        <div><span class="n ok">{s.correct}</span><span class="muted small">{t("res.correct")}</span></div>
        <div><span class="n bad">{s.wrong}</span><span class="muted small">{t("res.wrong")}</span></div>
        <div><span class="n">{s.unanswered}</span><span class="muted small">{t("res.unanswered")}</span></div>
        <div><span class="n">{num(s.accuracy)}%</span><span class="muted small">{t("res.accuracy")}</span></div>
        <div><span class="n">{duration(s.time_used_ms)}</span><span class="muted small">{t("res.time")} / {duration(r.duration_ms)}</span></div>
      </div>
    </div>
    {#if negCost > 0}
      <p class="muted">{t("res.negative_cost", { n: num(negCost) })}</p>
    {/if}

    <div class="actions">
      <a class="btn btn-primary" href="/tests/{r.id}/review">{t("res.review")}</a>
      <a class="btn" href="/tests">{t("res.back")}</a>
    </div>

    {#if r.sections.length > 1}
      <h2>{t("res.sections")}</h2>
      {@render table(r.sections, false)}
    {/if}
    <h2>{t("res.topics")}</h2>
    {@render table(r.topics, true)}
  {/if}
</div>

{#snippet table(rows: TestResult["topics"], link: boolean)}
  <table class="card tbl">
    <thead>
      <tr>
        <th>{t("res.col.name")}</th><th>{t("res.correct")}</th><th>{t("res.wrong")}</th><th>{t("res.unanswered")}</th><th>{t("res.score")}</th>
      </tr>
    </thead>
    <tbody>
      {#each rows as row (row.id)}
        <tr>
          <td lang={settings.lang}>{#if link}<a href="/topic/{row.id}">{row.name}</a>{:else}{row.name}{/if}</td>
          <td>{row.correct}</td><td>{row.wrong}</td><td>{row.unanswered}</td>
          <td class="num">{num(row.score)} / {num(row.max_score)}</td>
        </tr>
      {/each}
    </tbody>
  </table>
{/snippet}

<style>
  .page {
    max-width: 960px;
  }
  .hero {
    display: grid;
    grid-template-columns: minmax(220px, 1fr) 2fr;
    gap: var(--space-6);
    align-items: center;
    margin: var(--space-4) 0;
  }
  .score {
    display: grid;
    gap: var(--space-2);
  }
  .big {
    font-size: 2.5rem;
    font-weight: 700;
    font-variant-numeric: tabular-nums;
  }
  .of {
    font-size: 1.25rem;
    color: var(--text-muted);
  }
  .tiles {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: var(--space-3);
  }
  .tiles div {
    display: grid;
  }
  .n {
    font-size: 1.375rem;
    font-weight: 700;
    font-variant-numeric: tabular-nums;
  }
  .ok {
    color: var(--correct);
  }
  .bad {
    color: var(--wrong);
  }
  .actions {
    display: flex;
    gap: var(--space-2);
    margin: var(--space-4) 0;
  }
  h2 {
    font-size: 1.125rem;
    margin-top: var(--space-6);
  }
  .tbl {
    width: 100%;
    border-collapse: collapse;
    padding: 0;
  }
  .tbl th,
  .tbl td {
    padding: var(--space-2) var(--space-3);
    border-bottom: 1px solid var(--border);
    text-align: left;
  }
  .tbl th {
    font-size: 0.8125rem;
    color: var(--text-muted);
    font-weight: 600;
  }
  .tbl tr:last-child td {
    border-bottom: 0;
  }
  .num {
    font-variant-numeric: tabular-nums;
    white-space: nowrap;
  }
  .small {
    font-size: 0.8125rem;
  }
</style>
