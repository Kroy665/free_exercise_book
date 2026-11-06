<script lang="ts">
  import { api, errorMessage, type LibrarySubject, type Stats } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import ProgressBar from "$lib/components/ProgressBar.svelte";
  import { settings, t } from "$lib/stores/settings.svelte";

  let stats = $state<Stats | null>(null);
  let tree = $state<LibrarySubject[]>([]);
  let error = $state<string | null>(null);

  async function load(lang: string) {
    error = null;
    try {
      [stats, tree] = await Promise.all([api.statsGet(), api.libraryTree(lang)]);
    } catch (e) {
      error = errorMessage(e);
    }
  }

  $effect(() => {
    load(settings.lang);
  });

  const topics = $derived(tree.flatMap((s) => s.units.flatMap((u) => u.topics)));
  const accuracy = $derived(stats && stats.attempted > 0 ? Math.round((stats.correct / stats.attempted) * 100) : null);
</script>

<div class="page">
  <h1>{t("home.title")}</h1>
  <p class="muted">{t("home.subtitle")}</p>

  {#if error}
    <ErrorBox message={error} onretry={() => load(settings.lang)} />
  {:else if stats}
    <div class="tiles">
      <div class="card tile"><span class="num">{stats.topics}</span><span class="muted">{t("stat.topics")}</span></div>
      <div class="card tile"><span class="num">{stats.attempted}</span><span class="muted">{t("stat.practised")}</span></div>
      <div class="card tile">
        <span class="num">{accuracy === null ? "—" : `${accuracy}%`}</span><span class="muted">{t("stat.accuracy")}</span>
      </div>
      <a class="card tile link" href="/revise">
        <span class="num">{stats.mistakes}</span><span class="muted">{t("stat.mistakes")}</span>
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
        <p class="muted">{t("library.empty")}</p>
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
    color: inherit;
    text-decoration: none;
  }
  .tile.link:hover {
    border-color: var(--accent);
  }
  .num {
    font-size: 2rem;
    font-weight: 700;
    font-variant-numeric: tabular-nums;
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
