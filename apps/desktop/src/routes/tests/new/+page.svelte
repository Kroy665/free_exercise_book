<script lang="ts">
  import { goto } from "$app/navigation";
  import { api, errorMessage, testsApi, type LibrarySubject } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import { settings, t } from "$lib/stores/settings.svelte";

  let tree = $state<LibrarySubject[] | null>(null);
  let error = $state<string | null>(null);
  let creating = $state(false);

  let name = $state("");
  let selected = $state<Set<string>>(new Set());
  let count = $state(10);
  let minutes = $state(10);
  let marks = $state(2);
  let negFraction = $state(0); // 0, 1/4, 1/3, 1/2

  const topics = $derived(tree?.flatMap((s) => s.units.flatMap((u) => u.topics)) ?? []);
  const available = $derived(topics.filter((x) => selected.has(x.id)).reduce((n, x) => n + x.question_count, 0));
  const negative = $derived(Math.round(marks * negFraction * 10000) / 10000);

  async function load(lang: string) {
    try {
      tree = await api.libraryTree(lang);
      if (selected.size === 0) selected = new Set(topics.map((x) => x.id));
    } catch (e) {
      error = errorMessage(e);
    }
  }

  $effect(() => {
    load(settings.lang);
  });

  // Keep the question count within what is available, and suggest ~1 minute per question.
  $effect(() => {
    if (available > 0 && count > available) count = available;
  });

  function toggle(id: string) {
    const next = new Set(selected);
    if (next.has(id)) next.delete(id);
    else next.add(id);
    selected = next;
  }

  async function create() {
    creating = true;
    error = null;
    try {
      const id = await testsApi.createCustom({
        title: name.trim() || null,
        topic_ids: [...selected],
        count,
        duration_minutes: minutes,
        marks_each: marks,
        negative,
      });
      goto(`/tests/${id}/instructions`);
    } catch (e) {
      error = errorMessage(e);
    } finally {
      creating = false;
    }
  }
</script>

<div class="page">
  <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/tests">{t("tests.title")}</a> › {t("new.title")}</nav>
  <h1>{t("new.title")}</h1>

  {#if error}
    <ErrorBox message={error} />
  {/if}

  {#if !tree}
    <p class="muted">{t("common.loading")}</p>
  {:else if topics.length === 0}
    <div class="card"><p class="muted">{t("new.no_topics")}</p><a class="btn btn-primary" href="/downloads">{t("library.empty_action")}</a></div>
  {:else}
    <form class="form" onsubmit={(e) => { e.preventDefault(); create(); }}>
      <label class="field">
        <span>{t("new.name")}</span>
        <input type="text" bind:value={name} maxlength="80" placeholder="Custom test" />
      </label>

      <fieldset class="card">
        <legend>{t("new.topics")}</legend>
        <div class="quick">
          <button type="button" class="btn btn-ghost" onclick={() => (selected = new Set(topics.map((x) => x.id)))}>{t("new.select_all")}</button>
          <button type="button" class="btn btn-ghost" onclick={() => (selected = new Set())}>{t("new.select_none")}</button>
        </div>
        {#each tree as s (s.id)}
          {#each s.units as u (u.id)}
            <p class="group muted small" lang={settings.lang}>{s.title} › {u.title}</p>
            {#each u.topics as topic (topic.id)}
              <label class="check">
                <input type="checkbox" checked={selected.has(topic.id)} onchange={() => toggle(topic.id)} />
                <span lang={settings.lang}>{topic.title}</span>
                <span class="muted small">{t("library.questions", { n: topic.question_count })}</span>
              </label>
            {/each}
          {/each}
        {/each}
      </fieldset>

      <div class="row3">
        <label class="field">
          <span>{t("new.count")}</span>
          <input type="number" min="1" max={Math.max(1, available)} bind:value={count} required />
        </label>
        <label class="field">
          <span>{t("new.duration")}</span>
          <input type="number" min="1" max="600" bind:value={minutes} required />
        </label>
        <label class="field">
          <span>{t("new.marks")}</span>
          <input type="number" min="0.25" max="10" step="0.25" bind:value={marks} required />
        </label>
      </div>
      <p class="muted small">{t("new.count_help", { n: available })}</p>

      <label class="field">
        <span>{t("new.negative")}</span>
        <select bind:value={negFraction}>
          <option value={0}>{t("new.neg.none")}</option>
          <option value={0.25}>{t("new.neg.quarter")}</option>
          <option value={1 / 3}>{t("new.neg.third")}</option>
          <option value={0.5}>{t("new.neg.half")}</option>
        </select>
      </label>

      <button class="btn btn-primary" type="submit" disabled={creating || selected.size === 0 || available === 0}>
        {t("new.create")}
      </button>
    </form>
  {/if}
</div>

<style>
  .form {
    display: grid;
    gap: var(--space-4);
    max-width: 640px;
  }
  .field {
    display: grid;
    gap: var(--space-1);
  }
  .field span {
    font-weight: 600;
    font-size: 0.9375rem;
  }
  input[type="text"],
  input[type="number"],
  select {
    font: inherit;
    padding: var(--space-2);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    background: var(--surface);
    color: var(--text);
  }
  fieldset {
    margin: 0;
    display: grid;
    gap: var(--space-1);
  }
  legend {
    font-weight: 600;
    padding: 0 var(--space-1);
  }
  .quick {
    display: flex;
    gap: var(--space-1);
  }
  .group {
    margin: var(--space-2) 0 0;
  }
  .check {
    display: flex;
    align-items: center;
    gap: var(--space-2);
    padding: var(--space-1) 0;
  }
  .check .small {
    margin-left: auto;
  }
  .row3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-3);
  }
  .small {
    font-size: 0.8125rem;
  }
  .form > .btn {
    justify-self: start;
  }
</style>
