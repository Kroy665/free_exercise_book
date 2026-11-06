<script lang="ts">
  import { goto } from "$app/navigation";
  import { EXAMS, dataApi, errorMessage } from "$lib/api";
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
    <p class="muted small">v0.1.0</p>
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
</style>
