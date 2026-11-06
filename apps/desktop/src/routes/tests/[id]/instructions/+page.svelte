<script lang="ts">
  import { goto } from "$app/navigation";
  import { page } from "$app/state";
  import { errorMessage, testsApi, type TestSession } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import { clock, negativeLabel, num } from "$lib/format";
  import { settings, t } from "$lib/stores/settings.svelte";

  let s = $state<TestSession | null>(null);
  let error = $state<string | null>(null);
  const id = $derived(Number(page.params.id));

  async function load(testId: number, lang: string) {
    error = null;
    try {
      s = await testsApi.session(testId, lang);
      if (s.status === "submitted") goto(`/tests/${testId}/result`, { replaceState: true });
    } catch (e) {
      error = errorMessage(e);
    }
  }

  $effect(() => {
    load(id, settings.lang);
  });

  async function start() {
    try {
      await testsApi.start(id);
      goto(`/tests/${id}/run`);
    } catch (e) {
      error = errorMessage(e);
    }
  }
</script>

<div class="page">
  <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/tests">{t("tests.title")}</a> › {t("ins.title")}</nav>
  {#if error}
    <ErrorBox message={error} onretry={() => load(id, settings.lang)} />
  {:else if !s}
    <p class="muted">{t("common.loading")}</p>
  {:else}
    <h1>{s.title}</h1>
    <div class="card facts">
      <div><span class="muted small">{t("ins.questions")}</span><strong>{s.total_questions}</strong></div>
      <div>
        <span class="muted small">{t("ins.time")}</span>
        <strong>{s.status === "in_progress" ? `${clock(s.remaining_ms)} left` : `${Math.round(s.duration_ms / 60000)} min`}</strong>
      </div>
      <div><span class="muted small">{t("ins.marks")}</span><strong>{num(s.total_marks)}</strong></div>
    </div>

    {#if s.scaled_from}
      <p class="card note">{t("ins.scaled", { q: s.scaled_from[0], min: s.scaled_from[1] })}</p>
    {/if}
    {#if s.missing}
      <p class="card note">{t("ins.missing", { n: s.missing })}</p>
    {/if}

    <h2>{t("ins.marking")}</h2>
    <ul>
      {#each s.sections as sec (sec.id)}
        <li>
          {#if s.sections.length > 1}<strong>{sec.name}</strong> ({sec.questions.length}): {/if}
          {t("ins.per_question", { m: num(sec.marks_each) })}; {negativeLabel(sec.negative, sec.marks_each)}
        </li>
      {/each}
    </ul>

    <h2>{t("ins.rules")}</h2>
    <ol class="rules">
      <li>{t("ins.rule1")}</li>
      <li>{t("ins.rule2")}</li>
      <li>{t("ins.rule3")}</li>
      <li>{t("ins.rule4")}</li>
    </ol>

    <button class="btn btn-primary big" onclick={start} disabled={s.total_questions === 0}>
      {s.status === "in_progress" ? t("ins.resume") : t("ins.start")}
    </button>
  {/if}
</div>

<style>
  .page {
    max-width: 760px;
  }
  .facts {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-4);
    margin: var(--space-4) 0;
  }
  .facts div {
    display: grid;
  }
  .facts strong {
    font-size: 1.5rem;
    font-variant-numeric: tabular-nums;
  }
  .note {
    border-color: var(--review);
    background: var(--review-bg);
    padding: var(--space-3) var(--space-4);
  }
  h2 {
    font-size: 1.125rem;
    margin-top: var(--space-5);
  }
  .rules li {
    margin-bottom: var(--space-2);
  }
  .big {
    margin-top: var(--space-5);
    min-height: 44px;
    padding: 0 var(--space-6);
  }
  .small {
    font-size: 0.8125rem;
  }
</style>
