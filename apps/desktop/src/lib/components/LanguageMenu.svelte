<script lang="ts">
  import { CONTENT_LANGS } from "$lib/i18n/content";
  import { setSetting, settings, t } from "$lib/stores/settings.svelte";
  import Languages from "@lucide/svelte/icons/languages";
  import ChevronDown from "@lucide/svelte/icons/chevron-down";
  import Check from "@lucide/svelte/icons/check";

  let open = $state(false);
  let root = $state<HTMLElement | null>(null);
  const current = $derived(CONTENT_LANGS.find((l) => l.code === settings.lang) ?? CONTENT_LANGS[0]);

  function choose(code: string) {
    open = false;
    if (code !== settings.lang) setSetting("lang", code);
  }

  function onwindowclick(e: MouseEvent) {
    if (open && root && !root.contains(e.target as Node)) open = false;
  }
  function onkeydown(e: KeyboardEvent) {
    if (open && e.key === "Escape") open = false;
  }
</script>

<svelte:window onclick={onwindowclick} {onkeydown} />

<div class="langmenu" bind:this={root}>
  <button
    class="btn btn-ghost trigger"
    aria-haspopup="listbox"
    aria-expanded={open}
    title={t("lang.toggle_hint")}
    onclick={() => (open = !open)}
  >
    <Languages size={18} aria-hidden="true" />
    <span class="sr-only">{t("lang.content")}:</span>
    <span lang={current.code}>{current.native}</span>
    <ChevronDown size={16} aria-hidden="true" />
  </button>
  {#if open}
    <ul class="menu" role="listbox" aria-label={t("lang.content")}>
      <li class="heading">{t("lang.content")}</li>
      {#each CONTENT_LANGS as l (l.code)}
        <li>
          <button role="option" aria-selected={l.code === settings.lang} onclick={() => choose(l.code)}>
            <span class="tick">{#if l.code === settings.lang}<Check size={16} aria-hidden="true" />{/if}</span>
            <span lang={l.code}>{l.native}</span>
            {#if l.code !== "en"}<span class="muted">{l.label}</span>{/if}
          </button>
        </li>
      {/each}
    </ul>
  {/if}
</div>

<style>
  .langmenu {
    position: relative;
  }
  .trigger {
    gap: var(--space-2);
  }
  .menu {
    position: absolute;
    right: 0;
    top: calc(100% + 4px);
    min-width: 200px;
    margin: 0;
    padding: var(--space-1);
    list-style: none;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    box-shadow: 0 8px 24px rgb(0 0 0 / 0.14);
    z-index: 20;
  }
  .heading {
    font-size: 0.75rem;
    color: var(--text-muted);
    padding: var(--space-1) var(--space-3);
  }
  .menu button {
    display: flex;
    align-items: center;
    gap: var(--space-2);
    width: 100%;
    padding: var(--space-2) var(--space-3);
    border: 0;
    border-radius: var(--radius-sm);
    background: none;
    color: var(--text);
    font: inherit;
    text-align: left;
    cursor: default;
  }
  .menu button:hover,
  .menu button:focus-visible {
    background: var(--accent-soft);
  }
  .tick {
    width: 16px;
    display: inline-grid;
    color: var(--accent);
  }
  .muted {
    margin-left: auto;
    font-size: 0.8125rem;
  }
</style>
