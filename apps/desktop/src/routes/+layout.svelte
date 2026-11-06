<script lang="ts">
  import "@fontsource-variable/noto-sans";
  import "@fontsource-variable/noto-sans-bengali";
  import "$lib/styles/tokens.css";
  import "$lib/styles/base.css";
  import { page } from "$app/state";
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
  import Languages from "@lucide/svelte/icons/languages";

  let { children } = $props();

  loadSettings();

  const main = [
    { href: "/", key: "nav.home", icon: House },
    { href: "/library", key: "nav.library", icon: BookOpen },
    { href: "/tests", key: "nav.tests", icon: Timer },
    { href: "/revise", key: "nav.revise", icon: RotateCcw },
    { href: "/current-affairs", key: "nav.current_affairs", icon: Newspaper },
    { href: "/progress", key: "nav.progress", icon: ChartColumn },
  ];
  const bottom = [
    { href: "/downloads", key: "nav.downloads", icon: Download },
    { href: "/settings", key: "nav.settings", icon: Settings },
  ];

  function active(href: string) {
    const p = page.url.pathname;
    if (href === "/") return p === "/";
    return p === href || p.startsWith(href + "/") || (href === "/library" && p.startsWith("/topic/"));
  }

  const isDark = $derived(
    settings.theme === "dark" ||
    (settings.theme === "system" && window.matchMedia("(prefers-color-scheme: dark)").matches),
  );

  function onkeydown(e: KeyboardEvent) {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "l") {
      e.preventDefault();
      toggleLang();
    }
  }
</script>

<svelte:window {onkeydown} />

{#if settings.loaded}
  <div class="shell">
    <nav class="sidebar" aria-label={t("nav.main")}>
      <div class="brand">{t("app.name")}</div>
      <ul>
        {#each main as item (item.href)}
          <li>
            <a href={item.href} title={t(item.key)} class:active={active(item.href)} aria-current={active(item.href) ? "page" : undefined}>
              <item.icon size={20} aria-hidden="true" /><span>{t(item.key)}</span>
            </a>
          </li>
        {/each}
      </ul>
      <ul class="bottom">
        {#each bottom as item (item.href)}
          <li>
            <a href={item.href} title={t(item.key)} class:active={active(item.href)} aria-current={active(item.href) ? "page" : undefined}>
              <item.icon size={20} aria-hidden="true" /><span>{t(item.key)}</span>
            </a>
          </li>
        {/each}
      </ul>
    </nav>

    <div class="main-col">
      <header class="topbar">
        <button class="btn btn-ghost" onclick={toggleLang} title={t("lang.toggle")} aria-label={t("lang.toggle")}>
          <Languages size={18} aria-hidden="true" />
          <span class:on={settings.lang === "en"}>EN</span>/<span class:on={settings.lang === "bn"}>বাং</span>
        </button>
        <button
          class="btn btn-ghost"
          onclick={() => setSetting("theme", isDark ? "light" : "dark")}
          title={t("theme.toggle")}
          aria-label={t("theme.toggle")}
        >
          {#if isDark}<Sun size={18} aria-hidden="true" />{:else}<Moon size={18} aria-hidden="true" />{/if}
        </button>
      </header>
      <main>
        {@render children()}
      </main>
    </div>
  </div>
{/if}

<style>
  .shell {
    display: grid;
    grid-template-columns: 220px 1fr;
    min-height: 100vh;
  }
  .sidebar {
    position: sticky;
    top: 0;
    height: 100vh;
    display: flex;
    flex-direction: column;
    background: var(--surface);
    border-right: 1px solid var(--border);
    padding: var(--space-4) var(--space-2);
  }
  .brand {
    font-weight: 700;
    padding: 0 var(--space-3) var(--space-4);
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
  nav a {
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
    min-width: 0;
  }
  .topbar {
    display: flex;
    justify-content: flex-end;
    gap: var(--space-1);
    padding: var(--space-2) var(--space-4);
    border-bottom: 1px solid var(--border);
    background: var(--bg);
    position: sticky;
    top: 0;
    z-index: 5;
  }
  .topbar span {
    color: var(--text-muted);
  }
  .topbar span.on {
    color: var(--text);
    font-weight: 700;
  }
  @media (max-width: 1100px) {
    .shell {
      grid-template-columns: 64px 1fr;
    }
    .brand,
    nav a span {
      display: none;
    }
    nav a {
      justify-content: center;
      padding: 0;
    }
  }
</style>
