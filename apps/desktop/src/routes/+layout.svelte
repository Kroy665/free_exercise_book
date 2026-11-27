<script lang="ts">
  import "@fontsource-variable/noto-sans";
  import "@fontsource-variable/noto-sans-bengali";
  import "$lib/styles/tokens.css";
  import "$lib/styles/base.css";
  import { afterNavigate, goto } from "$app/navigation";
  import { page } from "$app/state";
  import LanguageMenu from "$lib/components/LanguageMenu.svelte";
  import CommandPalette from "$lib/components/CommandPalette.svelte";
  import AssistantPanel from "$lib/components/AssistantPanel.svelte";
  import SelectionAsk from "$lib/components/SelectionAsk.svelte";
  import VoiceStatus from "$lib/components/VoiceStatus.svelte";
  import { chat } from "$lib/stores/assistant.svelte";
  import MessageCircleQuestion from "@lucide/svelte/icons/message-circle-question";
  import Search from "@lucide/svelte/icons/search";
  import { autoUpdate, packBadge, packNotice, refreshCaNav, refreshDueBadge, refreshPackBadge } from "$lib/stores/packs.svelte";
  import { loadSettings, setSetting, settings, t, toggleLang } from "$lib/stores/settings.svelte";
  import House from "@lucide/svelte/icons/house";
  import BookOpen from "@lucide/svelte/icons/book-open";
  import Timer from "@lucide/svelte/icons/timer";
  import RotateCcw from "@lucide/svelte/icons/rotate-ccw";
  import Newspaper from "@lucide/svelte/icons/newspaper";
  import ChartColumn from "@lucide/svelte/icons/chart-column";
  import Download from "@lucide/svelte/icons/download";
  import Settings from "@lucide/svelte/icons/settings";
  import Sun from "@lucide/svelte/icons/sun";
  import Moon from "@lucide/svelte/icons/moon";

  let { children } = $props();

  loadSettings();
  refreshPackBadge();
  refreshDueBadge();
  refreshCaNav();

  const allMain = [
    { href: "/", key: "nav.home", icon: House },
    { href: "/library", key: "nav.library", icon: BookOpen },
    { href: "/tests", key: "nav.tests", icon: Timer },
    { href: "/revise", key: "nav.revise", icon: RotateCcw },
    { href: "/current-affairs", key: "nav.current_affairs", icon: Newspaper },
    { href: "/progress", key: "nav.progress", icon: ChartColumn },
  ];
  // Current Affairs only appears when a current-affairs month is installed.
  const main = $derived(allMain.filter((i) => i.href !== "/current-affairs" || packNotice.hasCa));
  const bottom = [
    { href: "/downloads", key: "nav.downloads", icon: Download },
    { href: "/settings", key: "nav.settings", icon: Settings },
  ];

  const examMode = $derived(/^\/tests\/\d+\/run\/?$/.test(page.url.pathname));
  const setupMode = $derived(page.url.pathname.startsWith("/onboarding"));

  // First start: run the setup before anything else.
  $effect(() => {
    if (settings.loaded && settings.onboarded === "0" && !setupMode) goto("/onboarding", { replaceState: true });
  });

  // New topics are published regularly: fetch them in the background once per start.
  $effect(() => {
    if (settings.loaded && settings.onboarded === "1" && settings.auto_update === "1") autoUpdate(settings.lang);
  });
  const noticeText = $derived.by(() => {
    const { added, updated } = packNotice;
    if (added.length === 1 && !updated.length) return `New topic downloaded: ${added[0]}`;
    const parts = [];
    if (added.length) parts.push(`${added.length} new topic${added.length > 1 ? "s" : ""}`);
    if (updated.length) parts.push(`${updated.length} updated`);
    return parts.length ? `Downloaded ${parts.join(", ")}.` : "";
  });

  function active(href: string) {
    const p = page.url.pathname;
    if (href === "/") return p === "/";
    if (p.startsWith("/topic/ca.")) return href === "/current-affairs";
    return p === href || p.startsWith(href + "/") || (href === "/library" && p.startsWith("/topic/"));
  }

  const isDark = $derived(
    settings.theme === "dark" ||
      (settings.theme === "system" && window.matchMedia("(prefers-color-scheme: dark)").matches),
  );

  // Only the content pane scrolls (desktop layout). Reset it on every page change,
  // unless the URL targets a section (#anchor), which the page scrolls to itself.
  let scroller = $state<HTMLElement | null>(null);
  afterNavigate(({ to }) => {
    if (scroller && !to?.url.hash) scroller.scrollTop = 0;
    refreshDueBadge();
  });

  let paletteOpen = $state(false);
  let shell = $state<HTMLElement | null>(null);

  // The assistant knows which topic is open.
  $effect(() => {
    const m = /^\/topic\/([^/]+)/.exec(page.url.pathname);
    chat.topicId = m ? decodeURIComponent(m[1]) : null;
  });

  function onkeydown(e: KeyboardEvent) {
    if (!examMode && (e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      paletteOpen = !paletteOpen;
      return;
    }
    if (!examMode && (e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "j") {
      e.preventDefault();
      chat.open = !chat.open;
      return;
    }
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "l") {
      e.preventDefault();
      toggleLang();
    }
  }

  // Desktop app, not a web page: no browser context menu (Reload / Inspect) in release builds.
  function oncontextmenu(e: MouseEvent) {
    if (!import.meta.env.PROD) return;
    if ((e.target as HTMLElement).closest("input, textarea, [contenteditable='true']")) return;
    e.preventDefault();
  }
</script>

<svelte:window {onkeydown} {oncontextmenu} />

{#if settings.loaded && (examMode || setupMode)}
  <!-- Exam view: full window, no sidebar or top bar (like the real computer-based test). -->
  {@render children()}
{:else if settings.loaded}
  <div class="shell" class:with-chat={chat.open} bind:this={shell}>
    <nav class="sidebar chrome" aria-label={t("nav.main")}>
      <div class="brand">
        <img src="/favicon.png" alt="" width="24" height="24" />
        <span>{t("app.name")}</span>
      </div>
      <ul>
        {#each main as item (item.href)}
          {@const due = item.href === "/revise" ? packBadge.due : 0}
          <li>
            <a href={item.href} title={due ? t("nav.due", { n: due }) : t(item.key)} class:active={active(item.href)} aria-current={active(item.href) ? "page" : undefined}>
              <item.icon size={20} aria-hidden="true" /><span>{t(item.key)}</span>
              {#if due}<span class="count" aria-label={t("nav.due", { n: due })}>{due > 99 ? "99+" : due}</span>{/if}
            </a>
          </li>
        {/each}
      </ul>
      <ul class="bottom">
        {#each bottom as item (item.href)}
          {@const dot = item.href === "/downloads" && packBadge.updates > 0}
          <li>
            <a href={item.href} title={dot ? t("nav.updates", { n: packBadge.updates }) : t(item.key)} class:active={active(item.href)} aria-current={active(item.href) ? "page" : undefined}>
              <span class="icon"><item.icon size={20} aria-hidden="true" />{#if dot}<span class="dot" aria-hidden="true"></span>{/if}</span><span>{t(item.key)}</span>
              {#if dot}<span class="sr-only">{t("nav.updates", { n: packBadge.updates })}</span>{/if}
            </a>
          </li>
        {/each}
      </ul>
    </nav>

    <div class="main-col">
      <header class="topbar chrome">
        <button class="searchbtn" onclick={() => (paletteOpen = true)} aria-keyshortcuts="Control+K Meta+K">
          <Search size={16} aria-hidden="true" />
          <span>{t("search.open")}…</span>
          <kbd>{navigator.platform.startsWith("Mac") ? "⌘K" : "Ctrl K"}</kbd>
        </button>
        <span class="spacer"></span>
        <button
          class="btn btn-ghost askbtn"
          class:on={chat.open}
          onclick={() => (chat.open = !chat.open)}
          title="Teacher (⌘J)"
          aria-pressed={chat.open}
          aria-keyshortcuts="Control+J Meta+J"
        >
          <MessageCircleQuestion size={18} aria-hidden="true" /><span>Ask</span>
        </button>
        <LanguageMenu />
        <button
          class="btn btn-ghost"
          onclick={() => setSetting("theme", isDark ? "light" : "dark")}
          title={t("theme.toggle")}
          aria-label={t("theme.toggle")}
        >
          {#if isDark}<Sun size={18} aria-hidden="true" />{:else}<Moon size={18} aria-hidden="true" />{/if}
        </button>
      </header>
      <main class="content" bind:this={scroller}>
        {@render children()}
      </main>
      {#if noticeText}
        <div class="notice" role="status">
          <span>{noticeText}</span>
          <a class="btn btn-ghost" href="/library" onclick={() => { packNotice.added = []; packNotice.updated = []; }}>Open Library</a>
          <button class="btn btn-ghost" aria-label="Dismiss" onclick={() => { packNotice.added = []; packNotice.updated = []; }}>✕</button>
        </div>
      {/if}
    </div>
    {#if chat.open}<AssistantPanel />{/if}
  </div>
  <CommandPalette bind:open={paletteOpen} />
  <SelectionAsk root={shell} />
  {#if !chat.open}<VoiceStatus floating />{/if}
{/if}

<style>
  .notice {
    position: fixed;
    right: var(--space-5);
    bottom: var(--space-5);
    display: flex;
    align-items: center;
    gap: var(--space-2);
    padding: var(--space-2) var(--space-2) var(--space-2) var(--space-4);
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 4px solid var(--correct);
    border-radius: var(--radius-sm);
    box-shadow: 0 6px 24px rgb(0 0 0 / 0.12);
    font-size: 0.9375rem;
    z-index: 20;
    max-width: min(560px, calc(100vw - 2 * var(--space-5)));
  }
  .shell {
    display: grid;
    grid-template-columns: 220px minmax(0, 1fr);
    height: 100vh;
    overflow: hidden;
  }
  .shell.with-chat {
    grid-template-columns: 220px minmax(0, 1fr) minmax(320px, 400px);
  }
  .askbtn {
    gap: var(--space-1);
  }
  .askbtn.on {
    background: var(--accent-soft);
  }
  .sidebar {
    display: flex;
    flex-direction: column;
    min-height: 0;
    overflow-y: auto;
    background: var(--surface);
    border-right: 1px solid var(--border);
    padding: var(--space-4) var(--space-2);
  }
  .brand {
    display: flex;
    align-items: center;
    gap: var(--space-2);
    font-weight: 700;
    font-size: 0.9375rem;
    white-space: nowrap;
    padding: 0 var(--space-3) var(--space-4);
  }
  .brand img {
    border-radius: 6px;
  }
  ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: grid;
    gap: 2px;
  }
  .bottom {
    margin-top: auto;
  }
  .count {
    margin-left: auto;
    min-width: 20px;
    padding: 0 6px;
    border-radius: 999px;
    background: var(--accent);
    color: var(--accent-fg);
    font-size: 0.75rem;
    font-weight: 600;
    text-align: center;
    line-height: 18px;
  }
  .icon {
    position: relative;
    display: inline-flex;
  }
  .dot {
    position: absolute;
    top: -2px;
    right: -3px;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--accent);
    border: 2px solid var(--surface);
  }
  nav a {
    position: relative;
    display: flex;
    align-items: center;
    gap: var(--space-3);
    min-height: 36px;
    padding: 0 var(--space-3);
    border-radius: var(--radius-sm);
    color: var(--text);
    text-decoration: none;
    border-left: 3px solid transparent;
  }
  nav a:hover {
    background: var(--surface-2);
  }
  nav a.active {
    background: var(--accent-soft);
    border-left-color: var(--accent);
    font-weight: 600;
  }
  .main-col {
    display: flex;
    flex-direction: column;
    min-width: 0;
    min-height: 0;
  }
  .topbar {
    flex: none;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: var(--space-1);
    padding: var(--space-2) var(--space-4);
    border-bottom: 1px solid var(--border);
    background: var(--bg);
  }
  .searchbtn {
    display: flex;
    align-items: center;
    gap: var(--space-2);
    width: min(360px, 40vw);
    height: 34px;
    padding: 0 var(--space-3);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    background: var(--surface);
    color: var(--text-muted);
    font: inherit;
    font-size: 0.875rem;
    cursor: default;
  }
  .searchbtn:hover {
    border-color: var(--accent);
  }
  .searchbtn kbd {
    margin-left: auto;
    font-family: var(--font-mono);
    font-size: 0.75rem;
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 0 6px;
  }
  .spacer {
    flex: 1;
  }
  .content {
    flex: 1;
    min-height: 0;
    overflow-y: auto;
    overscroll-behavior: none;
  }
  @media (max-width: 1100px) {
    .shell {
      grid-template-columns: 64px minmax(0, 1fr);
    }
    .shell.with-chat {
      grid-template-columns: 64px minmax(0, 1fr) minmax(300px, 360px);
    }
    .brand span,
    nav a span:not(.icon):not(.count) {
      display: none;
    }
    .count {
      position: absolute;
      transform: translate(10px, -10px);
      min-width: 16px;
      padding: 0 4px;
      line-height: 16px;
      font-size: 0.6875rem;
    }
    .brand {
      justify-content: center;
      padding: 0 0 var(--space-4);
    }
    nav a {
      justify-content: center;
      padding: 0;
    }
  }
</style>
