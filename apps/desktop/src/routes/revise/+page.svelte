<script lang="ts">
  import { api, errorMessage, type QuestionView } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import PracticeSession from "$lib/components/PracticeSession.svelte";
  import { renderInline } from "$lib/markdown/render";
  import { refreshDueBadge } from "$lib/stores/packs.svelte";
  import { settings, t } from "$lib/stores/settings.svelte";

  type Tab = "due" | "mistakes";
  let tab = $state<Tab>("due");
  let due = $state<QuestionView[] | null>(null);
  let mistakes = $state<QuestionView[] | null>(null);
  let running = $state<Tab | null>(null);
  let error = $state<string | null>(null);

  async function load(lang: string) {
    error = null;
    try {
      [due, mistakes] = await Promise.all([api.reviseDue(lang), api.mistakesList(lang)]);
      refreshDueBadge();
      if (due.length === 0 && mistakes.length > 0 && running === null) tab = "mistakes";
    } catch (e) {
      error = errorMessage(e);
    }
  }

  $effect(() => {
    load(settings.lang);
  });

  const list = $derived(tab === "due" ? due : mistakes);
</script>

<div class="page">
  <h1>{t("revise.title")}</h1>

  {#if error}
    <ErrorBox message={error} onretry={() => load(settings.lang)} />
  {:else if !due || !mistakes}
    <p class="muted">{t("common.loading")}</p>
  {:else if running}
    {#key running}
      <PracticeSession
        questions={running === "due" ? due : mistakes}
        mode="revise"
        backHref="/revise"
      />
    {/key}
  {:else}
    <div class="tabs chrome" role="tablist">
      <button role="tab" aria-selected={tab === "due"} class="tab" class:on={tab === "due"} onclick={() => (tab = "due")}>
        {t("revise.due")} ({due.length})
      </button>
      <button role="tab" aria-selected={tab === "mistakes"} class="tab" class:on={tab === "mistakes"} onclick={() => (tab = "mistakes")}>
        {t("revise.mistakes")} ({mistakes.length})
      </button>
    </div>

    <p class="muted small help">{tab === "due" ? t("revise.due_help") : t("revise.mistakes_help")}</p>

    {#if !list || list.length === 0}
      <p class="card muted">{tab === "due" ? t("revise.due_empty") : t("revise.empty")}</p>
    {:else}
      <button class="btn btn-primary" onclick={() => (running = tab)}>
        {tab === "due" ? t("revise.start_due", { n: list.length }) : t("revise.start", { n: list.length })}
      </button>
      <ul class="list">
        {#each list as q (q.id)}
          <li class="card" lang={q.lang}>{@html renderInline(q.stem ?? q.assertion ?? q.id)}</li>
        {/each}
      </ul>
    {/if}
  {/if}
</div>

<style>
  .tabs {
    display: flex;
    gap: var(--space-1);
    border-bottom: 1px solid var(--border);
    margin: var(--space-4) 0 var(--space-3);
  }
  .tab {
    padding: var(--space-2) var(--space-4);
    border: 0;
    border-bottom: 2px solid transparent;
    margin-bottom: -1px;
    background: none;
    color: var(--text-muted);
    font: inherit;
    cursor: default;
  }
  .tab.on {
    color: var(--text);
    border-bottom-color: var(--accent);
    font-weight: 600;
  }
  .help {
    max-width: var(--read-width);
  }
  .list {
    list-style: none;
    padding: 0;
    display: grid;
    gap: var(--space-2);
    margin-top: var(--space-5);
    max-width: var(--read-width);
  }
  .list li {
    padding: var(--space-3) var(--space-4);
  }
  .small {
    font-size: 0.8125rem;
  }
</style>
