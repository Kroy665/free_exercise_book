<script lang="ts">
  import { goto } from "$app/navigation";
  import { EXAMS, TTS_VOICES, assistantApi, dataApi, errorMessage, type AssistantStatus } from "$lib/api";
  import { speak, tts } from "$lib/tts/tts.svelte";
  import { onMount } from "svelte";
  import { CONTENT_LANGS } from "$lib/i18n/content";
  import { refreshDueBadge } from "$lib/stores/packs.svelte";
  import { setSetting, settings, t } from "$lib/stores/settings.svelte";
  import { ask, open, save } from "@tauri-apps/plugin-dialog";

  let message = $state<{ ok: boolean; text: string } | null>(null);
  const exams = $derived(new Set(settings.exams ? settings.exams.split(",") : []));
  const filters = [{ name: "Free Exercise Book backup", extensions: ["febackup"] }];

  function toggleExam(id: string) {
    const n = new Set(exams);
    if (n.has(id)) n.delete(id);
    else n.add(id);
    setSetting("exams", EXAMS.map((e) => e.id).filter((e) => n.has(e)).join(","));
  }

  async function exportData() {
    message = null;
    const day = new Date().toISOString().slice(0, 10);
    const path = await save({ defaultPath: `free-exercise-book-progress-${day}.febackup`, filters });
    if (!path) return;
    try {
      await dataApi.export(path);
      message = { ok: true, text: t("data.exported", { path }) };
    } catch (e) {
      message = { ok: false, text: errorMessage(e) };
    }
  }

  async function importData() {
    message = null;
    const path = await open({ multiple: false, directory: false, filters });
    if (typeof path !== "string") return;
    const ok = await ask(t("data.import_confirm"), { title: t("data.import"), kind: "warning", okLabel: t("data.import"), cancelLabel: t("common.cancel") });
    if (!ok) return;
    try {
      const r = await dataApi.import(path);
      refreshDueBadge();
      message = { ok: true, text: t("data.imported", { a: r.attempts, t: r.tests, c: r.cards, path: r.previous_backup }) };
      location.reload(); // settings may have changed
    } catch (e) {
      message = { ok: false, text: errorMessage(e) };
    }
  }

  async function resetData() {
    message = null;
    const ok = await ask(t("data.reset_confirm"), { title: t("data.reset"), kind: "warning", okLabel: t("data.reset"), cancelLabel: t("common.cancel") });
    if (!ok) return;
    try {
      await dataApi.reset();
      refreshDueBadge();
      message = { ok: true, text: t("data.reset_done") };
    } catch (e) {
      message = { ok: false, text: errorMessage(e) };
    }
  }

  // ---------- Study assistant ----------
  const OLLAMA_MODELS = [
    { id: "qwen2.5:3b", hint: "about 2 GB, good for 8 GB of memory" },
    { id: "qwen2.5:7b", hint: "about 4.7 GB, better maths, needs 16 GB" },
    { id: "llama3.2:3b", hint: "about 2 GB" },
  ];
  const CLAUDE_MODELS = [
    { id: "claude-opus-5-5", hint: "best explanations" },
    { id: "claude-sonnet-5-5", hint: "faster, cheaper" },
    { id: "claude-haiku-5-5", hint: "fastest, cheapest" },
  ];
  let aStatus = $state<AssistantStatus | null>(null);
  let keyInput = $state("");
  let keyMsg = $state("");
  let modelInput = $state(settings.ollama_model);
  let urlInput = $state(settings.ollama_url);

  async function refreshAssistant() {
    try { aStatus = await assistantApi.status(); } catch { aStatus = null; }
  }
  onMount(() => {
    refreshAssistant();
    if (location.hash) document.getElementById(location.hash.slice(1))?.scrollIntoView();
  });

  async function saveKey(remove = false) {
    keyMsg = "";
    try {
      await assistantApi.setKey(remove ? "" : keyInput);
      keyInput = "";
      keyMsg = remove ? "Key removed." : "Key saved on this computer.";
      await refreshAssistant();
    } catch (e) {
      keyMsg = errorMessage(e);
    }
  }
  async function saveOllama() {
    try {
      if (urlInput.trim() !== settings.ollama_url) await setSetting("ollama_url", urlInput.trim());
      if (modelInput.trim() !== settings.ollama_model) await setSetting("ollama_model", modelInput.trim());
      await refreshAssistant();
    } catch (e) {
      message = { ok: false, text: errorMessage(e) };
    }
  }
  async function removeVoice() {
    await assistantApi.ttsRemove();
    message = { ok: true, text: "Voice files removed. They download again the next time you press Listen." };
  }

  async function rerunSetup() {
    await setSetting("onboarded", "0");
    goto("/onboarding");
  }
</script>

<div class="page">
  <h1>{t("settings.title")}</h1>

  <section class="card group">
    <label for="lang"><strong>{t("settings.language")}</strong></label>
    <p class="muted">{t("settings.language_help")}</p>
    <select id="lang" value={settings.lang} onchange={(e) => setSetting("lang", e.currentTarget.value)}>
      {#each CONTENT_LANGS as l (l.code)}
        <option value={l.code}>{l.code === "en" ? l.label : `${l.native} (${l.label})`}</option>
      {/each}
    </select>
  </section>

  <section class="card group">
    <span id="theme-label"><strong>{t("settings.theme")}</strong></span>
    <div class="radios" role="radiogroup" aria-labelledby="theme-label">
      {#each ["system", "light", "dark"] as th (th)}
        <label>
          <input type="radio" name="theme" value={th} checked={settings.theme === th} onchange={() => setSetting("theme", th)} />
          {t(`theme.${th}`)}
        </label>
      {/each}
    </div>
  </section>

  <section class="card group">
    <label for="goal"><strong>{t("settings.goal")}</strong></label>
    <p class="muted">{t("settings.goal_help")}</p>
    <input id="goal" class="goal" type="number" min="1" max="500" value={settings.daily_goal}
      onchange={(e) => { const n = Math.round(Number(e.currentTarget.value)); if (n >= 1 && n <= 500) setSetting("daily_goal", String(n)); }} />
  </section>

  <section class="card group">
    <label class="row-check">
      <input type="checkbox" checked={settings.auto_update === "1"} onchange={(e) => setSetting("auto_update", e.currentTarget.checked ? "1" : "0")} />
      <strong>Download new topics automatically</strong>
    </label>
    <p class="muted">New and updated topics are published regularly. When this is on, the app checks once each time it starts and downloads them in the background.</p>
  </section>

  <section class="card group" id="assistant">
    <span id="ai-label"><strong>Study assistant</strong></span>
    <p class="muted">Ask about anything you select in the notes or questions (⌘J opens the chat). Ollama runs on this computer, free and offline. Claude gives stronger explanations; it needs internet and your own API key, and each question costs a little.</p>
    <div class="radios" role="radiogroup" aria-labelledby="ai-label">
      {#each [["ollama", "Ollama (offline)"], ["claude", "Claude API"], ["off", "Off"]] as [v, label] (v)}
        <label><input type="radio" name="assistant" value={v} checked={settings.assistant === v} onchange={() => setSetting("assistant", v).then(refreshAssistant)} /> {label}</label>
      {/each}
    </div>

    {#if settings.assistant === "ollama"}
      <label for="om"><strong>Model</strong></label>
      <div class="row">
        <input id="om" class="text" list="ollama-models" bind:value={modelInput} onchange={saveOllama} />
        <datalist id="ollama-models">
          {#each OLLAMA_MODELS as m (m.id)}<option value={m.id}>{m.hint}</option>{/each}
        </datalist>
      </div>
      <p class="muted small">Suggested: {#each OLLAMA_MODELS as m, i (m.id)}{i ? "; " : ""}<code>{m.id}</code> ({m.hint}){/each}.</p>
      <details>
        <summary class="small">Server address</summary>
        <input class="text" bind:value={urlInput} onchange={saveOllama} aria-label="Ollama server address" />
      </details>
      {#if aStatus}
        <p class="small" class:bad={!aStatus.ollama.reachable || !aStatus.ollama.has_model}>
          {#if !aStatus.ollama.reachable}
            Ollama is not running. Install it from ollama.com, open it, then <button class="btn btn-ghost small" onclick={refreshAssistant}>check again</button>.
          {:else if !aStatus.ollama.has_model}
            Ollama is running, but <code>{settings.ollama_model}</code> is not downloaded. Open the chat (⌘J) to download it.
          {:else}
            Ready: Ollama is running with <code>{settings.ollama_model}</code>.
          {/if}
        </p>
      {/if}
    {:else if settings.assistant === "claude"}
      <label for="cm"><strong>Model</strong></label>
      <select id="cm" value={settings.claude_model} onchange={(e) => setSetting("claude_model", e.currentTarget.value)}>
        {#each CLAUDE_MODELS as m (m.id)}<option value={m.id}>{m.id} ({m.hint})</option>{/each}
      </select>
      <label for="key"><strong>API key</strong></label>
      <p class="muted small">Create one at console.anthropic.com. It is stored only on this computer, in its own file (not in progress backups), and is sent only to api.anthropic.com.</p>
      <div class="row">
        <input id="key" class="text" type="password" autocomplete="off" placeholder={aStatus?.claude_has_key ? "A key is saved; paste a new one to replace it" : "sk-ant-…"} bind:value={keyInput} />
        <button class="btn btn-primary" onclick={() => saveKey()} disabled={!keyInput.trim()}>Save key</button>
        {#if aStatus?.claude_has_key}<button class="btn btn-ghost" onclick={() => saveKey(true)}>Remove</button>{/if}
      </div>
      {#if keyMsg}<p class="small">{keyMsg}</p>{/if}
    {/if}
  </section>

  <section class="card group" id="voice">
    <span><strong>Listen (Kokoro voice)</strong></span>
    <p class="muted">Reads explanations and selected text aloud, offline. The voice model (about 93 MB) downloads the first time you press Listen.</p>
    <label for="voice-sel" class="small">Voice</label>
    <select id="voice-sel" value={settings.tts_voice} onchange={(e) => setSetting("tts_voice", e.currentTarget.value)}>
      {#each TTS_VOICES as v (v.id)}<option value={v.id}>{v.label}</option>{/each}
    </select>
    <label for="speed" class="small">Speed · {Number(settings.tts_speed).toFixed(1)}×</label>
    <input id="speed" type="range" min="0.7" max="1.5" step="0.1" value={settings.tts_speed} onchange={(e) => setSetting("tts_speed", e.currentTarget.value)} />
    <div class="row">
      <button class="btn" onclick={() => speak("settings-test", "A sequence is Cauchy if, for every $\\varepsilon > 0$, there is an $N$ with $|a_m - a_n| < \\varepsilon$ for all $m, n \\ge N$.")}>
        {tts.key === "settings-test" && tts.phase === "speaking" ? "Stop" : "Test voice"}
      </button>
      <button class="btn btn-ghost" onclick={removeVoice}>Remove voice files</button>
    </div>
  </section>

  <section class="card group">
    <label for="fs"><strong>{t("settings.font_size")}</strong> · {settings.font_size}px</label>
    <input id="fs" type="range" min="14" max="22" step="1" value={settings.font_size} onchange={(e) => setSetting("font_size", e.currentTarget.value)} />
  </section>

  <section class="card group">
    <span id="exams-label"><strong>{t("settings.exams")}</strong></span>
    <p class="muted">{t("settings.exams_help")}</p>
    <div class="chips" role="group" aria-labelledby="exams-label">
      {#each EXAMS as ex (ex.id)}
        <button class="chip" role="checkbox" aria-checked={exams.has(ex.id)} class:on={exams.has(ex.id)} onclick={() => toggleExam(ex.id)}>{ex.label}</button>
      {/each}
    </div>
    <button class="btn btn-ghost start" onclick={rerunSetup}>{t("settings.rerun")}</button>
  </section>

  <section class="card group">
    <strong>{t("data.title")}</strong>
    <p class="muted">{t("data.help")}</p>
    <div class="row">
      <button class="btn" onclick={exportData}>{t("data.export")}</button>
      <button class="btn" onclick={importData}>{t("data.import")}</button>
      <button class="btn btn-ghost danger" onclick={resetData}>{t("data.reset")}</button>
    </div>
    {#if message}<p class="small {message.ok ? 'okmsg' : 'errmsg'}" role="status">{message.text}</p>{/if}
  </section>

    <section class="card group">
    <strong>{t("settings.about")}</strong>
    <p class="muted">{t("settings.about_text")}</p>
    <p class="muted small">v0.3.0</p>
  </section>
</div>

<style>
  .group {
    max-width: 560px;
    margin-bottom: var(--space-4);
    display: grid;
    gap: var(--space-2);
  }
  .group p {
    margin: 0;
  }
  .radios {
    display: flex;
    gap: var(--space-5);
    flex-wrap: wrap;
  }
  .goal {
    width: 120px;
    font: inherit;
    padding: var(--space-2);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    background: var(--surface);
    color: var(--text);
  }
  select,
  input[type="range"] {
    font: inherit;
    max-width: 320px;
  }
  select {
    padding: var(--space-2);
    border-radius: var(--radius-sm);
    border: 1px solid var(--border);
    background: var(--surface);
    color: var(--text);
  }
  .small {
    font-size: 0.8125rem;
  }
  .text {
    font: inherit;
    padding: var(--space-2);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    background: var(--surface);
    color: var(--text);
    min-width: 260px;
  }
  .bad {
    color: var(--wrong);
  }
  .chips,
  .row {
    display: flex;
    flex-wrap: wrap;
    gap: var(--space-2);
  }
  .chip {
    padding: var(--space-1) var(--space-3);
    border: 1px solid var(--border);
    border-radius: 999px;
    background: var(--surface);
    color: var(--text);
    font: inherit;
    font-size: 0.875rem;
    cursor: default;
  }
  .chip.on {
    border-color: var(--accent);
    background: var(--accent-soft);
    font-weight: 600;
  }
  .start {
    justify-self: start;
    padding-left: 0;
  }
  .danger {
    color: var(--wrong);
  }
  .okmsg {
    color: var(--correct);
    word-break: break-all;
  }
  .errmsg {
    color: var(--wrong);
  }
  .row-check { display: flex; align-items: center; gap: var(--space-2); }
</style>
