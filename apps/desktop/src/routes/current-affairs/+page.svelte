<script lang="ts">
  import { api, errorMessage, type CaMonthSummary } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import ProgressBar from "$lib/components/ProgressBar.svelte";
  import { settings, t } from "$lib/stores/settings.svelte";
  import Newspaper from "@lucide/svelte/icons/newspaper";

  let months = $state<CaMonthSummary[] | null>(null);
  let error = $state<string | null>(null);

  async function load(lang: string) {
    error = null;
    try {
      months = await api.caMonths(lang);
    } catch (e) {
      error = errorMessage(e);
    }
  }

  $effect(() => {
    load(settings.lang);
  });
</script>

<div class="page">
  <h1>{t("ca.title")}</h1>
  <p class="muted">{t("ca.subtitle")}</p>

  {#if error}
    <ErrorBox message={error} onretry={() => load(settings.lang)} />
  {:else if !months}
    <p class="muted">{t("common.loading")}</p>
  {:else if months.length === 0}
    <div class="card empty">
      <p class="muted">{t("ca.empty")}</p>
      <a class="btn btn-primary" href="/downloads">{t("library.empty_action")}</a>
    </div>
  {:else}
    <div class="grid">
      {#each months as m (m.topic_id)}
        <a class="card month" href="/current-affairs/{m.topic_id}">
          <div class="mt"><Newspaper size={18} aria-hidden="true" /><strong lang={settings.lang}>{m.title}</strong></div>
          <span class="muted small">{t("ca.items", { n: m.items })} · {t("ca.quiz_meta", { n: m.questions })}</span>
          <div class="cats">
            {#each m.categories as c (c)}<span class="chip">{t(`ca.cat.${c}`)}</span>{/each}
          </div>
          <ProgressBar value={m.attempted} max={m.questions} label={t("library.progress", { done: m.attempted, total: m.questions })} />
          <span class="muted small">{t("library.progress", { done: m.attempted, total: m.questions })}</span>
        </a>
      {/each}
    </div>
  {/if}
</div>

<style>
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: var(--space-4);
    margin-top: var(--space-5);
  }
  .month {
    display: grid;
    gap: var(--space-2);
    color: inherit;
    text-decoration: none;
  }
  .month:hover {
    border-color: var(--accent);
  }
  .mt {
    display: flex;
    gap: var(--space-2);
    align-items: center;
  }
  .cats {
    display: flex;
    flex-wrap: wrap;
    gap: var(--space-1);
  }
  .chip {
    font-size: 0.75rem;
    padding: 0 var(--space-2);
    border-radius: 999px;
    background: var(--surface-2);
    color: var(--text-muted);
  }
  .empty {
    max-width: 480px;
    margin-top: var(--space-4);
  }
  .small {
    font-size: 0.8125rem;
  }
</style>
