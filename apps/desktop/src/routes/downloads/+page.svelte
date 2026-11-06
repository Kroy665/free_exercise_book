<script lang="ts">
  import { errorMessage, packsApi, type PackItem, type PackProgress, type PacksView } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import ProgressBar from "$lib/components/ProgressBar.svelte";
  import { refreshPackBadge } from "$lib/stores/packs.svelte";
  import { settings, t } from "$lib/stores/settings.svelte";
  import { listen } from "@tauri-apps/api/event";
  import { ask, open } from "@tauri-apps/plugin-dialog";
  import RefreshCw from "@lucide/svelte/icons/refresh-cw";
  import FolderInput from "@lucide/svelte/icons/folder-input";
  import Download from "@lucide/svelte/icons/download";
  import CircleCheck from "@lucide/svelte/icons/circle-check";
  import WifiOff from "@lucide/svelte/icons/wifi-off";

  let view = $state<PacksView | null>(null);
  let error = $state<string | null>(null);
  let notice = $state<{ kind: "ok" | "bad"; text: string } | null>(null);
  let checking = $state(false);
  let busy = $state<Set<string>>(new Set());
  let progress = $state<Record<string, PackProgress>>({});

  const installed = $derived(view?.items.filter((i) => i.state !== "available") ?? []);
  const available = $derived(view?.items.filter((i) => i.state === "available") ?? []);
  const updates = $derived(installed.filter((i) => i.state === "update"));

  // Group available packs by subject → unit for browsing.
  const groups = $derived.by(() => {
    const out: { key: string; subject: string; unit: string; items: PackItem[] }[] = [];
    for (const it of available) {
      const key = `${it.subject}/${it.unit}`;
      let g = out.find((x) => x.key === key);
      if (!g) out.push((g = { key, subject: it.subject_title, unit: it.unit_title, items: [] }));
      g.items.push(it);
    }
    return out;
  });

  function size(bytes: number) {
    if (bytes < 1024) return `${bytes} B`;
    if (bytes < 1024 * 1024) return `${Math.round(bytes / 1024)} KB`;
    return `${(bytes / 1024 / 1024).toFixed(1)} MB`;
  }

  function when(secs: number) {
    return new Intl.DateTimeFormat("en-IN", { dateStyle: "medium", timeStyle: "short" }).format(secs * 1000);
  }

  async function load(lang: string) {
    error = null;
    try {
      view = await packsApi.list(lang);
    } catch (e) {
      error = errorMessage(e);
    }
  }

  async function check() {
    checking = true;
    notice = null;
    try {
      view = await packsApi.check(settings.lang);
      refreshPackBadge(view);
    } catch (e) {
      notice = { kind: "bad", text: errorMessage(e) };
    } finally {
      checking = false;
    }
  }

  function report(r: { view: PacksView; installed: string[]; failed: [string, { message: string }][] }) {
    view = r.view;
    refreshPackBadge(r.view);
    if (r.failed.length) {
      notice = { kind: "bad", text: t("downloads.failed", { n: r.failed.length, message: r.failed[0][1].message }) };
    } else if (r.installed.length) {
      notice = { kind: "ok", text: t("downloads.done", { n: r.installed.length }) };
    } else {
      notice = { kind: "ok", text: t("downloads.nothing_new") };
    }
  }

  async function install(ids: string[]) {
    if (!ids.length) return;
    notice = null;
    busy = new Set([...busy, ...ids]);
    try {
      report(await packsApi.install(ids, settings.lang));
    } catch (e) {
      notice = { kind: "bad", text: errorMessage(e) };
    } finally {
      busy = new Set([...busy].filter((id) => !ids.includes(id)));
      for (const id of ids) delete progress[id];
    }
  }

  async function remove(item: PackItem) {
    const ok = await ask(t("downloads.remove_confirm", { title: item.title }), {
      title: t("downloads.remove"),
      kind: "warning",
      okLabel: t("downloads.remove"),
      cancelLabel: t("common.cancel"),
    });
    if (!ok) return;
    try {
      view = await packsApi.remove(item.id, settings.lang);
      refreshPackBadge(view);
    } catch (e) {
      notice = { kind: "bad", text: errorMessage(e) };
    }
  }

  async function importFolder() {
    const path = await open({ directory: true, title: t("downloads.import_title") });
    if (typeof path !== "string") return;
    notice = null;
    try {
      report(await packsApi.importFolder(path, settings.lang));
    } catch (e) {
      notice = { kind: "bad", text: errorMessage(e) };
    }
  }

  function pct(p: PackProgress | undefined) {
    return p && p.total > 0 ? Math.min(100, Math.round((p.done / p.total) * 100)) : 0;
  }

  $effect(() => {
    load(settings.lang);
  });

  $effect(() => {
    const un = listen<PackProgress>("packs://progress", (e) => {
      progress[e.payload.id] = e.payload;
    });
    return () => {
      un.then((f) => f());
    };
  });
</script>

{#snippet packRow(item: PackItem)}
  {@const p = progress[item.id]}
  {@const working = busy.has(item.id)}
  <li class="row">
    <div class="info">
      <strong lang={settings.lang}>{item.title}</strong>
      <span class="muted small">
        {t("downloads.meta", { q: item.questions, s: item.sections, size: size(item.size) })}
        ·
        {#if item.state === "update"}
          {t("downloads.update_to", { from: item.installed_version ?? "?", to: item.available_version ?? "?" })}
        {:else}
          {t("downloads.version", { v: item.installed_version ?? item.available_version ?? "?" })}
        {/if}
        {#if item.state === "available" && item.source === "bundled"}· {t("downloads.bundled")}{/if}
      </span>
      {#if working}
        <div class="progress" aria-live="polite">
          <ProgressBar value={pct(p)} max={100} label={item.title} />
          <span class="muted small">
            {p?.phase === "install" ? t("downloads.phase.install") : t("downloads.phase.download", { pct: pct(p) })}
          </span>
        </div>
      {/if}
    </div>
    <div class="actions">
      {#if item.state === "available"}
        <button class="btn btn-primary" disabled={working} onclick={() => install([item.id])}>
          <Download size={16} aria-hidden="true" />{t("downloads.download")}
        </button>
      {:else}
        {#if item.state === "update"}
          <button class="btn btn-primary" disabled={working} onclick={() => install([item.id])}>{t("downloads.update")}</button>
        {:else}
          <span class="ok" title={t("downloads.installed")}><CircleCheck size={18} aria-hidden="true" /><span class="sr-only">{t("downloads.installed")}</span></span>
        {/if}
        <button class="btn btn-ghost" disabled={working} onclick={() => remove(item)}>{t("downloads.remove")}</button>
      {/if}
    </div>
  </li>
{/snippet}

<div class="page">
  <header class="head">
    <div>
      <h1>{t("downloads.title")}</h1>
      <p class="muted">{t("downloads.subtitle")}</p>
    </div>
    <div class="toolbar">
      <button class="btn" onclick={importFolder} disabled={view?.dev_mode}>
        <FolderInput size={16} aria-hidden="true" />{t("downloads.import")}
      </button>
      <button class="btn btn-primary" onclick={check} disabled={checking || view?.dev_mode}>
        <RefreshCw size={16} aria-hidden="true" class={checking ? "spin" : ""} />
        {checking ? t("downloads.checking") : t("downloads.check")}
      </button>
    </div>
  </header>

  {#if error}
    <ErrorBox message={error} onretry={() => load(settings.lang)} />
  {:else if !view}
    <p class="muted">{t("common.loading")}</p>
  {:else}
    {#if view.dev_mode}
      <p class="card banner">{t("downloads.dev_mode")}</p>
    {/if}

    {#if view.remote.error}
      <div class="card banner warn" role="status">
        <WifiOff size={18} aria-hidden="true" />
        <div>
          <p>{t("downloads.offline")}</p>
          <p class="muted small">{t("downloads.error_detail", { message: view.remote.error.message })}</p>
        </div>
      </div>
    {:else}
      <p class="muted small">
        {view.remote.checked_at ? t("downloads.last_checked", { when: when(view.remote.checked_at) }) : t("downloads.never_checked")}
      </p>
    {/if}

    {#if notice}
      <p class="card banner {notice.kind === 'ok' ? 'good' : 'warn'}" role="status">{notice.text}</p>
    {/if}

    <section>
      <div class="section-head">
        <h2>{t("downloads.installed")}</h2>
        {#if updates.length}
          <button class="btn" onclick={() => install(updates.map((u) => u.id))}>{t("downloads.update_all", { n: updates.length })}</button>
        {/if}
      </div>
      {#if installed.length}
        <ul class="list card">
          {#each installed as item (item.id)}{@render packRow(item)}{/each}
        </ul>
      {:else}
        <p class="muted">{t("downloads.empty_installed")}</p>
      {/if}
    </section>

    <section>
      <div class="section-head">
        <h2>{t("downloads.available")}</h2>
        {#if available.length > 1}
          <button class="btn" onclick={() => install(available.map((a) => a.id))}>{t("downloads.download_all", { n: available.length })}</button>
        {/if}
      </div>
      {#if groups.length}
        {#each groups as g (g.key)}
          <h3 class="muted group" lang={settings.lang}>{g.subject} › {g.unit}</h3>
          <ul class="list card">
            {#each g.items as item (item.id)}{@render packRow(item)}{/each}
          </ul>
        {/each}
      {:else}
        <p class="muted">{t("downloads.empty_available")}</p>
      {/if}
    </section>
  {/if}
</div>

<style>
  .head {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: var(--space-4);
    margin-bottom: var(--space-3);
  }
  .toolbar {
    display: flex;
    gap: var(--space-2);
    flex: none;
  }
  section {
    margin-top: var(--space-6);
    max-width: 880px;
  }
  .section-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .group {
    font-size: 0.9375rem;
    margin: var(--space-4) 0 var(--space-2);
  }
  .list {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: var(--space-4);
    padding: var(--space-3) var(--space-4);
    border-top: 1px solid var(--border);
  }
  .row:first-child {
    border-top: 0;
  }
  .info {
    display: grid;
    gap: 2px;
    min-width: 0;
    flex: 1;
  }
  .progress {
    display: grid;
    gap: var(--space-1);
    margin-top: var(--space-2);
    max-width: 360px;
  }
  .actions {
    display: flex;
    align-items: center;
    gap: var(--space-2);
    flex: none;
  }
  .ok {
    color: var(--correct);
    display: inline-flex;
    padding: 0 var(--space-2);
  }
  .banner {
    display: flex;
    gap: var(--space-3);
    align-items: flex-start;
    padding: var(--space-3) var(--space-4);
    margin: var(--space-3) 0;
  }
  .banner p {
    margin: 0;
  }
  .warn {
    border-color: var(--review);
    background: var(--review-bg);
  }
  .good {
    border-color: var(--correct);
    background: var(--correct-bg);
  }
  .small {
    font-size: 0.8125rem;
  }
  :global(.spin) {
    animation: spin 1s linear infinite;
  }
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
</style>
