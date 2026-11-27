<script lang="ts">
  import { tick } from "svelte";
  import { listen } from "@tauri-apps/api/event";
  import { assistantApi, errorMessage, type AssistantStatus } from "$lib/api";
  import { renderInline, renderRich } from "$lib/markdown/render";
  import { chat, send, cancel, clearChat, loadLinks, spokenVersion } from "$lib/stores/assistant.svelte";
  import { settings } from "$lib/stores/settings.svelte";
  import { tts, speak } from "$lib/tts/tts.svelte";
  import VoiceStatus from "./VoiceStatus.svelte";
  import X from "@lucide/svelte/icons/x";
  import Trash2 from "@lucide/svelte/icons/trash-2";
  import Send from "@lucide/svelte/icons/send";
  import Square from "@lucide/svelte/icons/square";
  import Volume2 from "@lucide/svelte/icons/volume-2";
  import LoaderCircle from "@lucide/svelte/icons/loader-circle";
  import Sparkles from "@lucide/svelte/icons/sparkles";
  import BookOpen from "@lucide/svelte/icons/book-open";

  let status = $state<AssistantStatus | null>(null);
  let statusError = $state("");
  let pulling = $state<{ status: string; completed: number; total: number } | null>(null);
  let input = $state<HTMLTextAreaElement | null>(null);
  let list = $state<HTMLElement | null>(null);

  async function refresh() {
    statusError = "";
    try {
      status = await assistantApi.status();
    } catch (e) {
      statusError = errorMessage(e);
    }
  }

  $effect(() => {
    if (chat.open) {
      refresh();
      loadLinks();
      tick().then(() => input?.focus());
    }
  });
  // Re-check when the provider or model changes in Settings.
  $effect(() => {
    void settings.assistant;
    void settings.ollama_model;
    if (chat.open) refresh();
  });

  // Keep the newest message in view while it streams.
  $effect(() => {
    const last = chat.turns[chat.turns.length - 1];
    void last?.content.length;
    void chat.turns.length;
    tick().then(() => list?.scrollTo({ top: list.scrollHeight }));
  });

  // Focus the box when "Ask" attaches a selection.
  $effect(() => {
    if (chat.quote) tick().then(() => input?.focus());
  });

  const warning = $derived.by(() => {
    if (!status) return "";
    if (status.provider === "off") return "off";
    if (status.provider === "claude" && !status.claude_has_key) return "nokey";
    if (status.provider === "ollama" && !status.ollama.reachable) return "noollama";
    if (status.provider === "ollama" && !status.ollama.has_model) return "nomodel";
    return "";
  });

  async function pull() {
    pulling = { status: "starting", completed: 0, total: 0 };
    const un = await listen<{ status: string; completed: number; total: number }>("assistant-pull", (e) => (pulling = e.payload));
    try {
      await assistantApi.pull(settings.ollama_model);
      await refresh();
    } catch (e) {
      statusError = errorMessage(e);
    } finally {
      un();
      pulling = null;
    }
  }

  // "Listen" speaks a version written for listening, not the written reply with its formulas.
  let preparing = $state("");
  let listenError = $state("");
  async function listenTo(id: string) {
    if (tts.key === id && (tts.phase === "speaking" || tts.phase === "loading")) return speak(id, "");
    listenError = "";
    preparing = id;
    try {
      const text = await spokenVersion(id);
      if (preparing === id) speak(id, text);
    } catch (e) {
      listenError = errorMessage(e);
    } finally {
      if (preparing === id) preparing = "";
    }
  }

  /** Rendered reply with only the app's own topic links kept clickable. */
  function rendered(md: string): string {
    // Models sometimes write \( \) and \[ \]; the renderer reads $ and $$.
    md = md
      .replace(/\\\[([\s\S]+?)\\\]/g, (_, m) => `$$${m}$$`)
      .replace(/\\\(([\s\S]+?)\\\)/g, (_, m) => `$${m.trim()}$`);
    const html = renderRich(md);
    if (!html.includes("<a")) return html;
    const doc = new DOMParser().parseFromString(`<div>${html}</div>`, "text/html");
    for (const a of Array.from(doc.querySelectorAll("a"))) {
      const href = a.getAttribute("href") ?? "";
      if (chat.links.has(href)) {
        a.classList.add("topic-link");
      } else {
        a.replaceWith(...Array.from(a.childNodes));
      }
    }
    return doc.body.firstElementChild?.innerHTML ?? html;
  }

  function onkeydown(e: KeyboardEvent) {
    if (e.key === "Enter" && !e.shiftKey && !e.isComposing) {
      e.preventDefault();
      send(chat.draft);
    }
  }

  const provider = $derived(settings.assistant === "claude" ? `Claude (${settings.claude_model})` : settings.assistant === "ollama" ? `Ollama (${settings.ollama_model})` : "Off");
</script>

<aside class="panel" aria-label="Teacher">
  <header>
    <Sparkles size={18} aria-hidden="true" />
    <div class="title">
      <strong>Teacher</strong>
      <a class="muted small" href="/settings#assistant">{provider}</a>
    </div>
    <button class="btn btn-ghost icon" title="Clear chat" aria-label="Clear chat" onclick={clearChat} disabled={!chat.turns.length}>
      <Trash2 size={16} aria-hidden="true" />
    </button>
    <button class="btn btn-ghost icon" title="Close (⌘J)" aria-label="Close" onclick={() => (chat.open = false)}>
      <X size={18} aria-hidden="true" />
    </button>
  </header>

  {#if warning || statusError}
    <div class="setup" role="status">
      {#if statusError}
        <p>{statusError}</p>
      {:else if warning === "off"}
        <p>The assistant is turned off. Choose Ollama or Claude in <a href="/settings#assistant">Settings</a>.</p>
      {:else if warning === "nokey"}
        <p>Add your Claude API key in <a href="/settings#assistant">Settings</a> to use Claude.</p>
      {:else if warning === "noollama"}
        <p>Ollama is not running. Open the Ollama app (or run <code>ollama serve</code>), then <button class="linkbtn" onclick={refresh}>check again</button>.</p>
      {:else if warning === "nomodel"}
        {#if pulling}
          <p>Downloading <strong>{settings.ollama_model}</strong>: {pulling.status}{pulling.total ? ` — ${Math.floor((100 * pulling.completed) / pulling.total)}%` : ""}</p>
        {:else}
          <p>The model <strong>{settings.ollama_model}</strong> is not downloaded in Ollama yet (about 2 GB).</p>
          <button class="btn btn-primary" onclick={pull}>Download model</button>
        {/if}
      {/if}
    </div>
  {/if}

  <div class="messages" bind:this={list}>
    {#if !chat.turns.length}
      <div class="empty muted">
        <p>I'm your teacher. Ask anything you don't understand.</p>
        <p class="small">Tip: select text anywhere in the notes or a question, then press <strong>Ask</strong>. The assistant sees the page you are on and suggests which notes to read first.</p>
      </div>
    {/if}
    {#each chat.turns as turn (turn.id)}
      {#if turn.role === "user"}
        <div class="msg user">
          {#if turn.quote}<blockquote class="quote">{@html renderInline(turn.quote)}</blockquote>{/if}
          <p>{turn.content}</p>
        </div>
      {:else}
        <div class="msg bot">
          {#if turn.content}
            <div class="prose">{@html rendered(turn.content)}</div>
          {:else if turn.streaming}
            <p class="muted thinking"><LoaderCircle size={16} class="spin" aria-hidden="true" /> Thinking…</p>
          {/if}
          {#if turn.error}<p class="err">{turn.error}</p>{/if}
          {#if turn.suggestions?.length && !turn.streaming}
            <div class="readfirst">
              <span class="muted small">Read first</span>
              {#each turn.suggestions as sg (sg.href)}
                <a href={sg.href}><BookOpen size={14} aria-hidden="true" /> {sg.topic} › {sg.section}</a>
              {/each}
            </div>
          {/if}
          {#if listenError && preparing === "" && turn === chat.turns[chat.turns.length - 1]}<p class="err">{listenError}</p>{/if}
          {#if turn.content && !turn.streaming}
            <div class="tools">
              <button class="btn btn-ghost small" onclick={() => listenTo(turn.id)} aria-pressed={tts.key === turn.id}>
                {#if preparing === turn.id}
                  <LoaderCircle size={15} class="spin" aria-hidden="true" /> Teacher is preparing…
                {:else if tts.key === turn.id && tts.phase === "loading"}
                  <LoaderCircle size={15} class="spin" aria-hidden="true" /> Preparing voice…
                {:else if tts.key === turn.id && tts.phase === "speaking"}
                  <Square size={14} aria-hidden="true" /> Stop
                {:else}
                  <Volume2 size={15} aria-hidden="true" /> Listen
                {/if}
              </button>
            </div>
          {/if}
        </div>
      {/if}
    {/each}
  </div>

  <VoiceStatus />

  <form class="composer" onsubmit={(e) => { e.preventDefault(); send(chat.draft); }}>
    {#if chat.quote}
      <div class="chip">
        <span class="chip-text">{chat.quote}</span>
        <button type="button" class="btn btn-ghost icon" aria-label="Remove selected text" onclick={() => (chat.quote = "")}><X size={14} aria-hidden="true" /></button>
      </div>
    {/if}
    <div class="row">
      <textarea
        bind:this={input}
        bind:value={chat.draft}
        {onkeydown}
        rows="2"
        placeholder={chat.quote ? "What don't you understand about this?" : "Ask a question…"}
        aria-label="Your question"
      ></textarea>
      {#if chat.busy}
        <button type="button" class="btn btn-ghost icon" title="Stop" aria-label="Stop" onclick={cancel}><Square size={16} aria-hidden="true" /></button>
      {:else}
        <button type="submit" class="btn btn-primary icon" title="Send (Enter)" aria-label="Send" disabled={!chat.draft.trim()}><Send size={16} aria-hidden="true" /></button>
      {/if}
    </div>
  </form>
</aside>

<style>
  .panel {
    display: flex;
    flex-direction: column;
    min-height: 0;
    height: 100%;
    background: var(--surface);
    border-left: 1px solid var(--border);
  }
  header {
    display: flex;
    align-items: center;
    gap: var(--space-2);
    padding: var(--space-2) var(--space-2) var(--space-2) var(--space-4);
    border-bottom: 1px solid var(--border);
  }
  .title {
    display: flex;
    flex-direction: column;
    flex: 1;
    min-width: 0;
    line-height: 1.2;
  }
  .title a {
    color: var(--text-muted);
    text-decoration: none;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .icon {
    padding: 0 var(--space-2);
  }
  .setup {
    margin: var(--space-3);
    padding: var(--space-3);
    border: 1px solid var(--border);
    border-left: 4px solid var(--accent);
    border-radius: var(--radius-sm);
    font-size: 0.875rem;
    display: grid;
    gap: var(--space-2);
  }
  .setup p {
    margin: 0;
  }
  .linkbtn {
    background: none;
    border: 0;
    padding: 0;
    color: var(--accent);
    text-decoration: underline;
    font: inherit;
    cursor: pointer;
  }
  .messages {
    flex: 1;
    min-height: 0;
    overflow-y: auto;
    padding: var(--space-3) var(--space-4);
    display: flex;
    flex-direction: column;
    gap: var(--space-3);
  }
  .empty p {
    margin: 0 0 var(--space-2);
  }
  .msg {
    font-size: 0.9375rem;
    min-width: 0;
  }
  .msg.user {
    align-self: flex-end;
    max-width: 90%;
    background: var(--accent-soft);
    border-radius: var(--radius-sm);
    padding: var(--space-2) var(--space-3);
  }
  .msg.user p {
    margin: 0;
    white-space: pre-wrap;
  }
  .quote {
    margin: 0 0 var(--space-2);
    padding-left: var(--space-2);
    border-left: 3px solid var(--accent);
    color: var(--text-muted);
    font-size: 0.875rem;
    max-height: 8em;
    overflow: hidden;
  }
  .msg.bot .prose {
    overflow-x: auto;
  }
  .msg.bot :global(.prose > :first-child) {
    margin-top: 0;
  }
  .msg.bot :global(a.topic-link) {
    font-weight: 600;
  }
  .thinking {
    display: flex;
    align-items: center;
    gap: var(--space-2);
    margin: 0;
  }
  .err {
    color: var(--wrong);
    margin: var(--space-1) 0 0;
    font-size: 0.875rem;
  }
  .readfirst {
    display: grid;
    gap: 2px;
    margin-top: var(--space-2);
    padding: var(--space-2);
    border-radius: var(--radius-sm);
    background: var(--surface-2);
    font-size: 0.875rem;
  }
  .readfirst a {
    display: flex;
    align-items: center;
    gap: var(--space-1);
    text-decoration: none;
  }
  .readfirst a:hover {
    text-decoration: underline;
  }
  .tools {
    display: flex;
    gap: var(--space-1);
    margin-top: var(--space-1);
  }
  .tools .btn {
    min-height: 28px;
    gap: var(--space-1);
  }
  .composer {
    border-top: 1px solid var(--border);
    padding: var(--space-2) var(--space-3) var(--space-3);
    display: grid;
    gap: var(--space-2);
  }
  .row {
    display: flex;
    gap: var(--space-2);
    align-items: flex-end;
  }
  textarea {
    flex: 1;
    resize: none;
    font: inherit;
    font-size: 0.9375rem;
    padding: var(--space-2);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    background: var(--bg);
    color: var(--text);
    max-height: 10em;
  }
  textarea:focus {
    outline: 2px solid var(--accent);
    outline-offset: -1px;
  }
  .chip {
    display: flex;
    align-items: center;
    gap: var(--space-1);
    background: var(--surface-2);
    border-radius: var(--radius-sm);
    padding: var(--space-1) var(--space-1) var(--space-1) var(--space-2);
    font-size: 0.8125rem;
  }
  .chip-text {
    flex: 1;
    min-width: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    color: var(--text-muted);
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
