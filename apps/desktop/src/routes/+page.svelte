<script lang="ts">
  import { api, errorMessage, type LibrarySubject, type ProgressView } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import ProgressBar from "$lib/components/ProgressBar.svelte";
  import { num } from "$lib/format";
  import { settings, t } from "$lib/stores/settings.svelte";
  import Target from "@lucide/svelte/icons/target";
  import RotateCcw from "@lucide/svelte/icons/rotate-ccw";
  import Flame from "@lucide/svelte/icons/flame";

  let p = $state<ProgressView | null>(null);
  let tree = $state<LibrarySubject[]>([]);
  let error = $state<string | null>(null);

  async function load(lang: string) {
    error = null;
    try {
      [p, tree] = await Promise.all([api.progress(lang), api.libraryTree(lang)]);
    } catch (e) {
      error = errorMessage(e);
    }
  }

  $effect(() => {
    load(settings.lang);
  });

  // Current-affairs months have their own page.
  const topics = $derived(tree.filter((s) => s.id !== "ca").flatMap((s) => s.units.flatMap((u) => u.topics)));
  const goalDone = $derived(!!p && p.today >= p.daily_goal);
</script>

<div class="page">
  <h1>{t("home.title")}</h1>
  <p class="muted">{t("home.subtitle")}</p>

  {#if error}
    <ErrorBox message={error} onretry={() => load(settings.lang)} />
  {:else if p}
    <div class="tiles">
      <div class="card tile goal" class:done={goalDone}>
        <span class="muted small"><Target size={14} aria-hidden="true" /> {t("home.goal")}</span>
        <span class="num">{p.today} <span class="of">/ {p.daily_goal}</span></span>
        <ProgressBar value={Math.min(p.today, p.daily_goal)} max={p.daily_goal} label={t("home.goal_of", { n: p.today, goal: p.daily_goal })} />
        <span class="muted small">{goalDone ? t("home.goal_done") : t("home.goal_of", { n: p.today, goal: p.daily_goal })}</span>
      </div>
      <a class="card tile link" href="/revise">
        <span class="muted small"><RotateCcw size={14} aria-hidden="true" /> {t("home.due")}</span>
        <span class="num">{p.due}</span>
        <span class="small {p.due ? 'cta' : 'muted'}">{p.due ? t("home.due_action") + " →" : t("revise.due_empty").split(".")[0] + "."}</span>
      </a>
      <a class="card tile link" href="/progress">
        <span class="muted small"><Flame size={14} aria-hidden="true" /> {t("progress.streak")}</span>
        <span class="num">{t("progress.days", { n: p.streak })}</span>
        <span class="muted small">{t("progress.best")}: {t("progress.days", { n: p.best_streak })}</span>
      </a>
      <a class="card tile link" href="/progress">
        <span class="muted small">{t("progress.accuracy")}</span>
        <span class="num">{p.attempted ? `${num(p.accuracy)}%` : "—"}</span>
        <span class="muted small">{t("progress.answers", { n: p.total_attempts })}</span>
      </a>
    </div>

    <h2>{t("home.topics")}</h2>
    <div class="grid">
      {#each topics as topic (topic.id)}
        <a class="card topic" href="/topic/{topic.id}">
          <strong lang={settings.lang}>{topic.title}</strong>
          <ProgressBar value={topic.attempted} max={topic.question_count} label={t("library.progress", { done: topic.attempted, total: topic.question_count })} />
          <span class="muted small">{t("library.progress", { done: topic.attempted, total: topic.question_count })}</span>
        </a>
      {:else}
        <div class="card">
          <p class="muted">{t("library.empty")}</p>
          <a class="btn btn-primary" href="/downloads">{t("library.empty_action")}</a>
        </div>
      {/each}
    </div>
  {:else}
    <p class="muted">{t("common.loading")}</p>
  {/if}
</div>

<style>
  .tiles {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: var(--space-4);
    margin: var(--space-5) 0 var(--space-6);
  }
  .tile {
    display: grid;
    gap: var(--space-1);
    align-content: start;
    color: inherit;
    text-decoration: none;
  }
  .tile :global(svg) {
    vertical-align: -2px;
  }
  .tile.link:hover {
    border-color: var(--accent);
  }
  .goal.done {
    border-color: var(--correct);
    background: var(--correct-bg);
  }
  .num {
    font-size: 2rem;
    font-weight: 700;
    font-variant-numeric: tabular-nums;
  }
  .of {
    font-size: 1rem;
    color: var(--text-muted);
  }
  .cta {
    color: var(--accent);
    font-weight: 600;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: var(--space-4);
  }
  .topic {
    display: grid;
    gap: var(--space-2);
    color: inherit;
    text-decoration: none;
  }
  .topic:hover {
    border-color: var(--accent);
  }
  .small {
    font-size: 0.8125rem;
  }
</style>
