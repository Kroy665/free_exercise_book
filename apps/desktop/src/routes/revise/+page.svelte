<script lang="ts">
  import { api, errorMessage, type QuestionView } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import PracticeSession from "$lib/components/PracticeSession.svelte";
  import { renderInline } from "$lib/markdown/render";
  import { settings, t } from "$lib/stores/settings.svelte";

  let mistakes = $state<QuestionView[] | null>(null);
  let running = $state(false);
  let error = $state<string | null>(null);

  async function load(lang: string) {
    error = null;
    try {
      mistakes = await api.mistakesList(lang);
    } catch (e) {
      error = errorMessage(e);
    }
  }

  $effect(() => {
    load(settings.lang);
  });
</script>

<div class="page">
  <h1>{t("revise.title")}</h1>

  {#if error}
    <ErrorBox message={error} onretry={() => load(settings.lang)} />
  {:else if !mistakes}
    <p class="muted">{t("common.loading")}</p>
  {:else if running}
    {#key mistakes}
      <PracticeSession questions={mistakes} mode="revise" backHref="/revise" />
    {/key}
  {:else}
    <h2>{t("revise.mistakes")}</h2>
    {#if mistakes.length === 0}
      <p class="card muted">{t("revise.empty")}</p>
    {:else}
      <button class="btn btn-primary" onclick={() => (running = true)}>{t("revise.start", { n: mistakes.length })}</button>
      <ul class="list">
        {#each mistakes as q (q.id)}
          <li class="card" lang={q.lang}>{@html renderInline(q.stem ?? q.assertion ?? q.id)}</li>
        {/each}
      </ul>
    {/if}
  {/if}
</div>

<style>
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
</style>
