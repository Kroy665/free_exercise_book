<script lang="ts">
  import { goto } from "$app/navigation";
  import { searchApi, type SearchHit } from "$lib/api";
  import { setSetting, settings, t, toggleLang } from "$lib/stores/settings.svelte";
  import { tick } from "svelte";
  import Search from "@lucide/svelte/icons/search";
  import BookOpen from "@lucide/svelte/icons/book-open";
  import FileText from "@lucide/svelte/icons/file-text";
  import CircleHelp from "@lucide/svelte/icons/circle-help";
  import CornerDownLeft from "@lucide/svelte/icons/corner-down-left";
  import ArrowRight from "@lucide/svelte/icons/arrow-right";

  let { open = $bindable(false) }: { open: boolean } = $props();

  type Item =
    | { type: "command"; id: string; label: string; run: () => void }
    | { type: "hit"; id: string; hit: SearchHit };

  let query = $state("");
  let hits = $state<SearchHit[]>([]);
  let active = $state(0);
  let input = $state<HTMLInputElement | null>(null);
  let list = $state<HTMLElement | null>(null);
  let seq = 0;

  const isDark = () =>
    settings.theme === "dark" ||
    (settings.theme === "system" && window.matchMedia("(prefers-color-scheme: dark)").matches);

  const commands: { id: string; key: string; run: () => void }[] = [
    { id: "home", key: "search.cmd.home", run: () => goto("/") },
    { id: "library", key: "search.cmd.library", run: () => goto("/library") },
    { id: "tests", key: "search.cmd.tests", run: () => goto("/tests") },
    { id: "new-test", key: "search.cmd.new_test", run: () => goto("/tests/new") },
    { id: "revise", key: "search.cmd.revise", run: () => goto("/revise") },
    { id: "downloads", key: "search.cmd.downloads", run: () => goto("/downloads") },
    { id: "settings", key: "search.cmd.settings", run: () => goto("/settings") },
    { id: "lang", key: "search.cmd.lang", run: () => toggleLang() },
    { id: "theme", key: "search.cmd.theme", run: () => setSetting("theme", isDark() ? "light" : "dark") },
  ];

  const matchedCommands = $derived.by(() => {
    const q = query.trim().toLowerCase();
    const all = commands.map((c) => ({ ...c, label: t(c.key) }));
    if (!q) return all;
    return all.filter((c) => c.label.toLowerCase().includes(q)).slice(0, 4);
  });

  const items = $derived<Item[]>([
    ...matchedCommands.map((c) => ({ type: "command" as const, id: `cmd:${c.id}`, label: c.label, run: c.run })),
    ...hits.map((h) => ({ type: "hit" as const, id: `${h.kind}:${h.ref}`, hit: h })),
  ]);

  const groups = $derived.by(() => {
    const g: { key: string; items: { item: Item; index: number }[] }[] = [];
    items.forEach((item, index) => {
      const key = item.type === "command" ? "search.commands" : `search.${item.hit.kind}s`;
      let grp = g.find((x) => x.key === key);
      if (!grp) g.push((grp = { key, items: [] }));
      grp.items.push({ item, index });
    });
    return g;
  });

  // Search as you type (debounced); ignore out-of-order responses.
  $effect(() => {
    const q = query;
    const lang = settings.lang;
    const mine = ++seq;
    if (!q.trim()) {
      hits = [];
      return;
    }
    const timer = setTimeout(async () => {
      try {
        const res = await searchApi.search(q, lang);
        if (mine === seq) hits = res;
      } catch {
        if (mine === seq) hits = [];
      }
    }, 120);
    return () => clearTimeout(timer);
  });

  $effect(() => {
    void items.length;
    active = 0;
  });

  $effect(() => {
    if (open) {
      query = "";
      hits = [];
      tick().then(() => input?.focus());
    }
  });

  function close() {
    open = false;
  }

  function choose(item: Item) {
    close();
    if (item.type === "command") return item.run();
    const h = item.hit;
    const ca = h.topic_id.startsWith("ca.");
    if (h.kind === "topic") goto(ca ? `/current-affairs/${h.topic_id}` : `/topic/${h.topic_id}`);
    else if (h.kind === "section") goto(ca ? `/current-affairs/${h.topic_id}#${h.ref}` : `/topic/${h.topic_id}#${h.ref}`);
    else goto(`/topic/${h.topic_id}/practice?q=${encodeURIComponent(h.ref)}`);
  }

  function onkeydown(e: KeyboardEvent) {
    if (e.key === "Escape") {
      e.preventDefault();
      close();
    } else if (e.key === "ArrowDown") {
      e.preventDefault();
      active = Math.min(active + 1, items.length - 1);
      scrollActive();
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      active = Math.max(active - 1, 0);
      scrollActive();
    } else if (e.key === "Enter" && items[active]) {
      e.preventDefault();
      choose(items[active]);
    }
  }

  function scrollActive() {
    tick().then(() => list?.querySelector('[aria-selected="true"]')?.scrollIntoView({ block: "nearest" }));
  }

  /**
   * Split a snippet into plain/highlighted parts (rendered as text, never as HTML).
   * Highlights are widened to whole words: cutting a Bengali word between a consonant
   * and its vowel sign breaks how the word is drawn (e.g. a dotted-circle "◌ে").
   */
  function parts(snippet: string): { text: string; mark: boolean }[] {
    const raw: { text: string; mark: boolean }[] = [];
    for (const chunk of snippet.split("\u0002")) {
      const [marked, rest] = chunk.includes("\u0003") ? chunk.split("\u0003", 2) : [null, chunk];
      if (marked !== null) raw.push({ text: marked, mark: true });
      if (rest) raw.push({ text: rest, mark: false });
    }
    const boundary = /[\s\p{P}।]/u;
    for (let i = 0; i < raw.length; i++) {
      if (!raw[i].mark) continue;
      const prev = raw[i - 1];
      if (prev && !prev.mark) {
        let k = prev.text.length;
        while (k > 0 && !boundary.test(prev.text[k - 1])) k--;
        raw[i].text = prev.text.slice(k) + raw[i].text;
        prev.text = prev.text.slice(0, k);
      }
      const next = raw[i + 1];
      if (next && !next.mark) {
        let k = 0;
        while (k < next.text.length && !boundary.test(next.text[k])) k++;
        raw[i].text += next.text.slice(0, k);
        next.text = next.text.slice(k);
      }
    }
    // Snippet edges ("…") can cut a word in half; drop the partial word at each edge.
    const first = raw[0];
    if (first && !first.mark && first.text.startsWith("…")) {
      let k = 1;
      while (k < first.text.length && !boundary.test(first.text[k])) k++;
      first.text = "…" + first.text.slice(k);
    }
    const last = raw[raw.length - 1];
    if (last && !last.mark && last.text.endsWith("…")) {
      let k = last.text.length - 1;
      while (k > 0 && !boundary.test(last.text[k - 1])) k--;
      last.text = last.text.slice(0, k).trimEnd() + "…";
    }
    return raw.filter((p) => p.text && p.text !== "…");
  }
</script>

{#if open}
  <!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_static_element_interactions -->
  <div class="backdrop" onclick={close}></div>
  <div class="palette" role="dialog" aria-modal="true" aria-label={t("search.label")}>
    <div class="field">
      <Search size={18} aria-hidden="true" />
      <input
        bind:this={input}
        bind:value={query}
        {onkeydown}
        type="text"
        placeholder={t("search.placeholder")}
        aria-label={t("search.label")}
        role="combobox"
        aria-expanded="true"
        aria-controls="palette-list"
        aria-activedescendant={items[active] ? `pi-${active}` : undefined}
        autocomplete="off"
        spellcheck="false"
      />
      <kbd>Esc</kbd>
    </div>

    <div class="results" id="palette-list" role="listbox" bind:this={list}>
      {#each groups as g (g.key)}
        <p class="group">{t(g.key)}</p>
        {#each g.items as { item, index } (item.id)}
          <!-- svelte-ignore a11y_click_events_have_key_events -->
          <div
            id="pi-{index}"
            class="item"
            role="option"
            tabindex="-1"
            aria-selected={index === active}
            onmousemove={() => (active = index)}
            onclick={() => choose(item)}
          >
            {#if item.type === "command"}
              <ArrowRight size={16} aria-hidden="true" />
              <span class="label">{item.label}</span>
            {:else}
              {@const h = item.hit}
              {#if h.kind === "topic"}<BookOpen size={16} aria-hidden="true" />{:else if h.kind === "section"}<FileText size={16} aria-hidden="true" />{:else}<CircleHelp size={16} aria-hidden="true" />{/if}
              <span class="text">
                <span class="label" lang={h.lang}>{h.title}</span>
                {#if h.kind !== "topic"}<span class="sub" lang={h.lang}>{h.topic_title}</span>{/if}
                {#if h.snippet}
                  <span class="snippet" lang={h.snippet_lang}>{#each parts(h.snippet) as p, i (i)}{#if p.mark}<mark>{p.text}</mark>{:else}{p.text}{/if}{/each}</span>
                {/if}
              </span>
            {/if}
            {#if index === active}<CornerDownLeft size={14} aria-hidden="true" class="enter" />{/if}
          </div>
        {/each}
      {/each}
      {#if query.trim() && hits.length === 0 && matchedCommands.length === 0}
        <p class="empty">{t("search.none", { q: query.trim() })}</p>
      {/if}
    </div>
    <footer class="foot">
      <span>{t("search.keys")}</span>
      {#if !query.trim()}<span class="hint">{t("search.hint")}</span>{/if}
    </footer>
  </div>
{/if}

<style>
  .backdrop {
    position: fixed;
    inset: 0;
    background: rgb(0 0 0 / 0.35);
    z-index: 40;
  }
  .palette {
    position: fixed;
    top: 12vh;
    left: 50%;
    transform: translateX(-50%);
    width: min(680px, calc(100vw - 32px));
    max-height: 70vh;
    display: flex;
    flex-direction: column;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    box-shadow: 0 24px 64px rgb(0 0 0 / 0.3);
    z-index: 41;
    overflow: hidden;
  }
  .field {
    display: flex;
    align-items: center;
    gap: var(--space-3);
    padding: var(--space-3) var(--space-4);
    border-bottom: 1px solid var(--border);
    color: var(--text-muted);
  }
  .field input {
    flex: 1;
    border: 0;
    outline: 0;
    background: transparent;
    color: var(--text);
    font: inherit;
    font-size: 1.0625rem;
  }
  kbd {
    font-family: var(--font-mono);
    font-size: 0.75rem;
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 0 6px;
  }
  .results {
    overflow-y: auto;
    overscroll-behavior: contain;
    padding: var(--space-2);
  }
  .group {
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-muted);
    margin: var(--space-2) var(--space-2) var(--space-1);
  }
  .item {
    display: flex;
    align-items: flex-start;
    gap: var(--space-3);
    padding: var(--space-2) var(--space-3);
    border-radius: var(--radius-sm);
    cursor: default;
  }
  .item :global(svg) {
    flex: none;
    margin-top: 3px;
    color: var(--text-muted);
  }
  .item[aria-selected="true"] {
    background: var(--accent-soft);
  }
  .text {
    display: grid;
    min-width: 0;
    flex: 1;
  }
  .label {
    font-weight: 500;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .sub {
    font-size: 0.75rem;
    color: var(--text-muted);
  }
  .snippet {
    font-size: 0.8125rem;
    color: var(--text-muted);
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  mark {
    background: var(--review-bg);
    color: var(--text);
    border-radius: 2px;
    padding: 0 1px;
  }
  .item :global(.enter) {
    margin-left: auto;
  }
  .empty {
    padding: var(--space-4);
    color: var(--text-muted);
    margin: 0;
  }
  .foot {
    display: flex;
    justify-content: space-between;
    gap: var(--space-3);
    padding: var(--space-2) var(--space-4);
    border-top: 1px solid var(--border);
    font-size: 0.75rem;
    color: var(--text-muted);
  }
  .hint {
    text-align: right;
  }
</style>
