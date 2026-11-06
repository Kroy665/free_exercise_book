<script lang="ts">
  import { goto } from "$app/navigation";
  import { errorMessage, testsApi, type PatternView, type TestListItem } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import { clock, date, num } from "$lib/format";
  import { settings, t } from "$lib/stores/settings.svelte";
  import { ask } from "@tauri-apps/plugin-dialog";
  import Timer from "@lucide/svelte/icons/timer";
  import SlidersHorizontal from "@lucide/svelte/icons/sliders-horizontal";

  let patterns = $state<PatternView[] | null>(null);
  let tests = $state<TestListItem[]>([]);
  let error = $state<string | null>(null);
  let busy = $state<string | null>(null);

  const running = $derived(tests.filter((x) => x.status !== "submitted"));
  const done = $derived(tests.filter((x) => x.status === "submitted"));

  async function load(lang: string) {
    error = null;
    try {
      const o = await testsApi.overview(lang);
      patterns = o.patterns;
      tests = o.tests;
    } catch (e) {
      error = errorMessage(e);
    }
  }

  $effect(() => {
    load(settings.lang);
  });

  async function startPattern(p: PatternView) {
    busy = p.id;
    error = null;
    try {
      const id = await testsApi.createPattern(p.id);
      goto(`/tests/${id}/instructions`);
    } catch (e) {
      error = errorMessage(e);
    } finally {
      busy = null;
    }
  }

  async function discard(x: TestListItem) {
    const ok = await ask(t("tests.discard_confirm", { title: x.title }), {
      title: t("tests.discard"),
      kind: "warning",
      okLabel: t("tests.discard"),
      cancelLabel: t("common.cancel"),
    });
    if (!ok) return;
    await testsApi.remove(x.id);
    load(settings.lang);
  }
</script>

<div class="page">
  <h1>{t("tests.title")}</h1>
  <p class="muted">{t("tests.subtitle")}</p>

  {#if error}
    <ErrorBox message={error} onretry={() => load(settings.lang)} />
  {/if}

  {#if patterns === null && !error}
    <p class="muted">{t("common.loading")}</p>
  {:else if patterns}
    {#if running.length}
      <section>
        <h2>{t("tests.in_progress")}</h2>
        <ul class="card list">
          {#each running as x (x.id)}
            <li class="row">
              <div>
                <strong>{x.title}</strong>
                <span class="muted small">{x.questions} questions · {t("tests.left", { time: clock(x.remaining_ms) })}</span>
              </div>
              <div class="actions">
                <a class="btn btn-primary" href="/tests/{x.id}/instructions">{t("tests.resume")}</a>
                <button class="btn btn-ghost" onclick={() => discard(x)}>{t("tests.discard")}</button>
              </div>
            </li>
          {/each}
        </ul>
      </section>
    {/if}

    <section>
      <h2>{t("tests.patterns")}</h2>
      <p class="muted small">{t("tests.patterns_help")}</p>
      {#if patterns.length === 0}
        <p class="muted">{t("tests.no_patterns")}</p>
      {/if}
      <div class="grid">
        {#each patterns as p (p.id)}
          <div class="card pattern">
            <div class="ptitle"><Timer size={18} aria-hidden="true" /><strong>{p.name}</strong></div>
            <span class="muted small">
              {t("tests.pattern_meta", { q: p.total_questions, min: p.duration_minutes, marks: num(p.total_marks) })}
            </span>
            {#if p.available === 0}
              <span class="small warn">{t("tests.none_available")}</span>
            {:else}
              <span class="small">{t("tests.available", { a: p.available, q: p.total_questions })}</span>
              {#if p.available < p.total_questions}
                <span class="small muted">{t("tests.scaled", { a: p.available, min: p.scaled_minutes })}</span>
              {/if}
            {/if}
            <button class="btn btn-primary start" disabled={p.available === 0 || busy !== null} onclick={() => startPattern(p)}>
              {t("tests.start_pattern")}
            </button>
          </div>
        {/each}
        <div class="card pattern">
          <div class="ptitle"><SlidersHorizontal size={18} aria-hidden="true" /><strong>{t("tests.custom")}</strong></div>
          <span class="muted small">{t("tests.custom_help")}</span>
          <a class="btn start" href="/tests/new">{t("tests.create_custom")}</a>
        </div>
      </div>
    </section>

    <section>
      <h2>{t("tests.history")}</h2>
      {#if done.length === 0}
        <p class="muted">{t("tests.history_empty")}</p>
      {:else}
        <ul class="card list">
          {#each done as x (x.id)}
            <li class="row">
              <div>
                <strong>{x.title}</strong>
                <span class="muted small">{x.submitted_at ? date(x.submitted_at) : ""} · {x.questions} questions</span>
              </div>
              <div class="actions">
                <span class="score">{num(x.score ?? 0)} / {num(x.max_score ?? 0)}</span>
                <span class="muted small">{num(x.accuracy ?? 0)}%</span>
                <a class="btn" href="/tests/{x.id}/result">{t("tests.view_result")}</a>
              </div>
            </li>
          {/each}
        </ul>
      {/if}
    </section>
  {/if}
</div>

<style>
  section {
    margin-top: var(--space-6);
    max-width: 960px;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: var(--space-4);
    margin-top: var(--space-3);
  }
  .pattern {
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
  }
  .ptitle {
    display: flex;
    align-items: center;
    gap: var(--space-2);
  }
  .start {
    margin-top: auto;
    align-self: flex-start;
  }
  .warn {
    color: var(--review);
  }
  .list {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: var(--space-4);
    padding: var(--space-3) var(--space-4);
    border-top: 1px solid var(--border);
  }
  .row:first-child {
    border-top: 0;
  }
  .row > div:first-child {
    display: grid;
  }
  .actions {
    display: flex;
    align-items: center;
    gap: var(--space-3);
  }
  .score {
    font-weight: 700;
    font-variant-numeric: tabular-nums;
  }
  .small {
    font-size: 0.8125rem;
  }
</style>
