<script lang="ts">
  import { CONTENT_LANGS } from "$lib/i18n/content";
  import { setSetting, settings, t } from "$lib/stores/settings.svelte";
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
</style>
