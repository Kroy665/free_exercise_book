<script lang="ts">
  import { goto } from "$app/navigation";
  import { page } from "$app/state";
  import { api, errorMessage, testsApi, type CaMonthView } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import StatusTag from "$lib/components/StatusTag.svelte";
  import { settings, t } from "$lib/stores/settings.svelte";
  import { openUrl } from "@tauri-apps/plugin-opener";
  import { tick } from "svelte";
  import ExternalLink from "@lucide/svelte/icons/external-link";
  import ListChecks from "@lucide/svelte/icons/list-checks";
  import Timer from "@lucide/svelte/icons/timer";

  let v = $state<CaMonthView | null>(null);
  let error = $state<string | null>(null);
  let category = $state("all");
  const id = $derived(page.params.id ?? "");

  async function load(monthId: string, lang: string) {
    error = null;
    try {
      v = await api.caMonth(monthId, lang);
      await tick();
      const hash = decodeURIComponent(location.hash.slice(1));
      if (hash) document.getElementById(hash)?.scrollIntoView();
    } catch (e) {
      error = errorMessage(e);
    }
  }

  $effect(() => {
    load(id, settings.lang);
  });

  const categories = $derived(v ? [...new Set(v.items.map((i) => i.category))].sort() : []);
  const shown = $derived(v ? v.items.filter((i) => category === "all" || i.category === category) : []);
  const fmtDate = (d: string) => new Intl.DateTimeFormat("en-IN", { dateStyle: "medium" }).format(new Date(d + "T00:00:00"));
  const host = (u: string) => u.replace(/^https?:\/\//, "").split("/")[0].replace(/^www\./, "");

  async function timedTest() {
    if (!v) return;
    try {
      const testId = await testsApi.createCustom({
        title: `${v.title} — current affairs`,
        topic_ids: [v.topic_id],
        count: v.questions,
        duration_minutes: Math.max(5, Math.ceil(v.questions * 0.75)),
        marks_each: 2,
        negative: 0.5,
      });
      goto(`/tests/${testId}/instructions`);
    } catch (e) {
      error = errorMessage(e);
    }
  }
</script>

<div class="page">
  <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/current-affairs">{t("ca.title")}</a> › {v?.title ?? ""}</nav>
  {#if error}
    <ErrorBox message={error} onretry={() => load(id, settings.lang)} />
  {:else if !v}
    <p class="muted">{t("common.loading")}</p>
  {:else}
    <header class="head">
      <h1 lang={settings.lang}>{v.title}</h1>
      <div class="actions">
        <a class="btn btn-primary" href="/topic/{v.topic_id}/practice"><ListChecks size={16} aria-hidden="true" />{t("ca.quiz")} ({v.questions})</a>
        <button class="btn" onclick={timedTest}><Timer size={16} aria-hidden="true" />{t("ca.test")}</button>
      </div>
    </header>
    <p class="muted small">{t("ca.verify_note")}</p>

    <div class="filters chrome" role="tablist">
      <button role="tab" aria-selected={category === "all"} class="btn {category === 'all' ? 'btn-primary' : ''}" onclick={() => (category = "all")}>
        {t("ca.all")} ({v.items.length})
      </button>
      {#each categories as c (c)}
        <button role="tab" aria-selected={category === c} class="btn {category === c ? 'btn-primary' : ''}" onclick={() => (category = c)}>
          {t(`ca.cat.${c}`)} ({v.items.filter((i) => i.category === c).length})
        </button>
      {/each}
    </div>

    {#each shown as item (item.id)}
      <article class="card item" id={item.anchor} lang={item.lang}>
        <header class="ih">
          <span class="date">{fmtDate(item.date)}</span>
          <span class="chip">{t(`ca.cat.${item.category}`)}</span>
          <StatusTag status={item.status} />
        </header>
        <h2>{item.title}</h2>
        <p>{item.body}</p>
        {#if item.key_points.length}
          <ul class="points">
            {#each item.key_points as p, i (i)}<li>{p}</li>{/each}
          </ul>
        {/if}
        <footer class="if" lang="en">
          <button class="btn btn-ghost src" onclick={() => openUrl(item.source)} title={item.source}>
            <ExternalLink size={14} aria-hidden="true" />{t("ca.source")}: {host(item.source)}
          </button>
          <span class="muted small">{t("ca.as_of", { d: fmtDate(item.as_of) })}</span>
          {#if item.related.length}
            <span class="muted small">
              {t("ca.related")}:
              {#each item.related as r, i (r.id)}{#if i > 0}, {/if}{#if r.title}<a href="/topic/{r.id}" lang={settings.lang}>{r.title}</a>{:else}{r.id} {t("ca.not_installed")}{/if}{/each}
            </span>
          {/if}
        </footer>
      </article>
    {/each}
  {/if}
</div>

<style>
  .page {
    max-width: 860px;
  }
  .head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: var(--space-4);
    flex-wrap: wrap;
  }
  .actions {
    display: flex;
    gap: var(--space-2);
  }
  .filters {
    display: flex;
    flex-wrap: wrap;
    gap: var(--space-2);
    margin: var(--space-4) 0;
  }
  .item {
    margin-bottom: var(--space-4);
    scroll-margin-top: var(--space-5);
  }
  .item h2 {
    font-size: 1.25rem;
    margin: var(--space-2) 0;
  }
  .ih {
    display: flex;
    align-items: center;
    gap: var(--space-2);
  }
  .date {
    font-weight: 600;
    font-size: 0.875rem;
    font-variant-numeric: tabular-nums;
  }
  .chip {
    font-size: 0.75rem;
    padding: 0 var(--space-2);
    border-radius: 999px;
    background: var(--accent-soft);
    color: var(--accent);
  }
  .points {
    padding-left: var(--space-5);
    margin: 0 0 var(--space-3);
  }
  .if {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: var(--space-3);
    border-top: 1px solid var(--border);
    padding-top: var(--space-2);
  }
  .src {
    padding-left: 0;
    color: var(--accent);
  }
  .small {
    font-size: 0.8125rem;
  }
</style>
