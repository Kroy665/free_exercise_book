<script lang="ts">
  import { api, errorMessage, type LibrarySubject } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import ProgressBar from "$lib/components/ProgressBar.svelte";
  import StatusTag from "$lib/components/StatusTag.svelte";
  import { settings, t } from "$lib/stores/settings.svelte";

  let tree = $state<LibrarySubject[] | null>(null);
  let error = $state<string | null>(null);

  async function load(lang: string) {
    error = null;
    try {
      tree = await api.libraryTree(lang);
    } catch (e) {
      error = errorMessage(e);
    }
  }

  $effect(() => {
    load(settings.lang);
  });
</script>

<div class="page">
  <h1>{t("library.title")}</h1>

  {#if error}
    <ErrorBox message={error} onretry={() => load(settings.lang)} />
  {:else if !tree}
    <p class="muted">{t("common.loading")}</p>
  {:else if tree.length === 0}
    <p class="muted">{t("library.empty")}</p>
  {:else}
    {#each tree as subject (subject.id)}
      <section class="subject">
        <h2>{subject.title}</h2>
        {#each subject.units as unit (unit.id)}
          <h3 class="muted">{unit.title}</h3>
          <div class="grid">
            {#each unit.topics as topic (topic.id)}
              <a class="card topic" href="/topic/{topic.id}">
                <div class="row">
                  <strong>{topic.title}</strong>
                  <StatusTag status={topic.status} />
                </div>
                {#if topic.summary}<p class="muted small">{topic.summary}</p>{/if}
                <ProgressBar value={topic.attempted} max={topic.question_count} label={t("library.progress", { done: topic.attempted, total: topic.question_count })} />
                <span class="muted small">
                  {t("library.questions", { n: topic.question_count })}
                  {#if topic.estimated_minutes}· {t("library.minutes", { n: topic.estimated_minutes })}{/if}
                  · {t("library.progress", { done: topic.attempted, total: topic.question_count })}
                </span>
              </a>
            {/each}
          </div>
        {/each}
      </section>
    {/each}
  {/if}
</div>

<style>
  .subject {
    margin-top: var(--space-5);
  }
  h3 {
    font-size: 1rem;
    font-weight: 600;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: var(--space-4);
    margin-bottom: var(--space-5);
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
  .topic p {
    margin: 0;
  }
  .row {
    display: flex;
    justify-content: space-between;
    align-items: start;
    gap: var(--space-2);
  }
  .small {
    font-size: 0.8125rem;
  }
</style>
