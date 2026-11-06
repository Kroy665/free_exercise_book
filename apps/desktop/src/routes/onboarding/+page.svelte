<script lang="ts">
  import { goto } from "$app/navigation";
  import { EXAMS, errorMessage, packsApi, type PackItem } from "$lib/api";
  import { CONTENT_LANGS } from "$lib/i18n/content";
  import { refreshPackBadge } from "$lib/stores/packs.svelte";
  import { setSetting, settings, t } from "$lib/stores/settings.svelte";
  import CircleCheck from "@lucide/svelte/icons/circle-check";
  import WifiOff from "@lucide/svelte/icons/wifi-off";

  const STEPS = ["welcome", "lang", "exams", "goal", "topics", "done"] as const;
  let step = $state(0);
  let exams = $state<Set<string>>(new Set(settings.exams ? settings.exams.split(",") : []));
  let goal = $state(Number(settings.daily_goal) || 20);
  let items = $state<PackItem[]>([]);
  let selected = $state<Set<string>>(new Set());
  let checking = $state(false);
  let installing = $state(false);
  let offline = $state<string | null>(null);
  let note = $state<string | null>(null);

  const current = $derived(STEPS[step]);
  const installed = $derived(items.filter((i) => i.state !== "available" && !i.id.startsWith("ca.")));
  const available = $derived(items.filter((i) => i.state === "available"));

  function suggest(list: PackItem[]) {
    // Pre-select available topics that match the chosen exams (or all, if none chosen).
    const want = list.filter((i) => i.state === "available" && (exams.size === 0 || i.exams.some((e) => exams.has(e))));
    selected = new Set(want.map((i) => i.id));
  }

  async function loadPacks() {
    try {
      items = (await packsApi.list(settings.lang)).items;
      suggest(items);
    } catch (e) {
      offline = errorMessage(e);
    }
  }

  async function checkOnline() {
    checking = true;
    offline = null;
    try {
      const v = await packsApi.check(settings.lang);
      items = v.items;
      if (v.remote.error) offline = v.remote.error.message;
      suggest(items);
    } catch (e) {
      offline = errorMessage(e);
    } finally {
      checking = false;
    }
  }

  async function installSelected() {
    installing = true;
    note = null;
    try {
      const r = await packsApi.install([...selected], settings.lang);
      items = r.view.items;
      refreshPackBadge(r.view);
      selected = new Set();
      note = r.failed.length ? t("downloads.failed", { n: r.failed.length, message: r.failed[0][1].message }) : t("downloads.done", { n: r.installed.length });
    } catch (e) {
      note = errorMessage(e);
    } finally {
      installing = false;
    }
  }

  async function next() {
    if (current === "exams") await setSetting("exams", [...exams].join(","));
    if (current === "goal") await setSetting("daily_goal", String(Math.min(500, Math.max(1, Math.round(goal)))));
    step = Math.min(step + 1, STEPS.length - 1);
    if (STEPS[step] === "topics") loadPacks();
  }

  async function finish() {
    await setSetting("onboarded", "1");
    goto("/", { replaceState: true });
  }

  function toggleExam(id: string) {
    const n = new Set(exams);
    if (n.has(id)) n.delete(id);
    else n.add(id);
    exams = n;
  }

  function togglePack(id: string) {
    const n = new Set(selected);
    if (n.has(id)) n.delete(id);
    else n.add(id);
    selected = n;
  }
</script>

<div class="ob">
  <header class="top chrome">
    <div class="brand"><img src="/favicon.png" alt="" width="24" height="24" /> {t("app.name")}</div>
    {#if current !== "welcome" && current !== "done"}
      <span class="muted small">{t("ob.step", { i: step, n: STEPS.length - 2 })}</span>
    {/if}
    {#if current !== "done"}
      <button class="btn btn-ghost" onclick={finish}>{t("ob.skip")}</button>
    {:else}
      <span></span>
    {/if}
  </header>

  <main class="body">
    <section class="panel">
      {#if current === "welcome"}
        <img class="logo" src="/favicon.png" alt="" width="72" height="72" />
        <h1>{t("ob.welcome.title")}</h1>
        <p class="lead muted">{t("ob.welcome.text")}</p>
        <ul class="points">
          <li><CircleCheck size={18} aria-hidden="true" />{t("ob.welcome.p1")}</li>
          <li><CircleCheck size={18} aria-hidden="true" />{t("ob.welcome.p2")}</li>
          <li><CircleCheck size={18} aria-hidden="true" />{t("ob.welcome.p3")}</li>
        </ul>
      {:else if current === "lang"}
        <h1>{t("ob.lang.title")}</h1>
        <p class="muted">{t("ob.lang.text")}</p>
        <div class="choices two" role="radiogroup" aria-label={t("ob.lang.title")}>
          {#each CONTENT_LANGS as l (l.code)}
            <button
              class="choice"
              role="radio"
              aria-checked={settings.lang === l.code}
              class:on={settings.lang === l.code}
              onclick={() => setSetting("lang", l.code)}
            >
              <span class="big" lang={l.code}>{l.native}</span>
              <span class="muted small">{l.label}</span>
            </button>
          {/each}
        </div>
      {:else if current === "exams"}
        <h1>{t("ob.exams.title")}</h1>
        <p class="muted">{t("ob.exams.text")}</p>
        <div class="choices" role="group" aria-label={t("ob.exams.title")}>
          {#each EXAMS as ex (ex.id)}
            <button class="choice" role="checkbox" aria-checked={exams.has(ex.id)} class:on={exams.has(ex.id)} onclick={() => toggleExam(ex.id)}>
              <strong>{ex.label}</strong>
              <span class="muted small">{ex.hint}</span>
            </button>
          {/each}
        </div>
      {:else if current === "goal"}
        <h1>{t("ob.goal.title")}</h1>
        <p class="muted">{t("ob.goal.text")}</p>
        <div class="choices three" role="radiogroup" aria-label={t("ob.goal.title")}>
          {#each [[10, "ob.goal.light"], [20, "ob.goal.steady"], [40, "ob.goal.serious"]] as const as [n, k] (n)}
            <button class="choice" role="radio" aria-checked={goal === n} class:on={goal === n} onclick={() => (goal = n)}>
              <span class="big">{n}</span>
              <span class="muted small">{t(k)} · {t("ob.goal.per_day", { n })}</span>
            </button>
          {/each}
        </div>
        <label class="custom">
          {t("ob.goal.custom")}:
          <input type="number" min="1" max="500" bind:value={goal} />
        </label>
      {:else if current === "topics"}
        <h1>{t("ob.topics.title")}</h1>
        <p class="muted">{t("ob.topics.text")}</p>
        {#if installed.length}
          <h2>{t("ob.topics.installed")}</h2>
          <ul class="list">
            {#each installed as i (i.id)}
              <li><CircleCheck size={16} aria-hidden="true" class="ok" /><span lang={settings.lang}>{i.title}</span><span class="muted small">{i.subject_title}</span></li>
            {/each}
          </ul>
        {/if}
        {#if available.length}
          <h2>{t("ob.topics.suggested")}</h2>
          <ul class="list">
            {#each available as i (i.id)}
              <li>
                <label>
                  <input type="checkbox" checked={selected.has(i.id)} onchange={() => togglePack(i.id)} />
                  <span lang={settings.lang}>{i.title}</span>
                  <span class="muted small">{i.subject_title} · {Math.round(i.size / 1024)} KB</span>
                </label>
              </li>
            {/each}
          </ul>
          <button class="btn btn-primary" disabled={installing || selected.size === 0} onclick={installSelected}>
            {installing ? t("ob.topics.installing") : t("ob.topics.install", { n: selected.size })}
          </button>
        {:else if !checking && !offline}
          <p class="muted small">{t("ob.topics.none")}</p>
        {/if}
        {#if note}<p class="muted small" role="status">{note}</p>{/if}
        {#if offline}
          <p class="warn small" role="status"><WifiOff size={16} aria-hidden="true" /> {t("ob.topics.offline")}</p>
        {/if}
        <button class="btn btn-ghost" onclick={checkOnline} disabled={checking}>
          {checking ? t("ob.topics.checking") : t("ob.topics.check")}
        </button>
      {:else}
        <img class="logo" src="/favicon.png" alt="" width="72" height="72" />
        <h1>{t("ob.done.title")}</h1>
        <p class="lead muted">{t("ob.done.text")}</p>
      {/if}
    </section>
  </main>

  <footer class="foot chrome">
    {#if step > 0 && current !== "done"}
      <button class="btn" onclick={() => (step -= 1)}>{t("ob.back")}</button>
    {:else}
      <span></span>
    {/if}
    {#if current === "welcome"}
      <button class="btn btn-primary big-btn" onclick={next}>{t("ob.welcome.start")}</button>
    {:else if current === "done"}
      <button class="btn btn-primary big-btn" onclick={finish}>{t("ob.done.start")}</button>
    {:else}
      <button class="btn btn-primary big-btn" onclick={next} disabled={installing}>{t("ob.next")}</button>
    {/if}
  </footer>
</div>

<style>
  .ob {
    height: 100vh;
    display: flex;
    flex-direction: column;
    background: var(--bg);
  }
  .top,
  .foot {
    flex: none;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: var(--space-3) var(--space-6);
  }
  .top {
    border-bottom: 1px solid var(--border);
  }
  .foot {
    border-top: 1px solid var(--border);
  }
  .brand {
    display: flex;
    align-items: center;
    gap: var(--space-2);
    font-weight: 700;
  }
  .brand img,
  .logo {
    border-radius: 8px;
  }
  .body {
    flex: 1;
    overflow-y: auto;
    overscroll-behavior: none;
    display: flex;
    justify-content: center;
    padding: var(--space-7) var(--space-6);
  }
  .panel {
    width: min(720px, 100%);
  }
  .lead {
    font-size: 1.125rem;
  }
  .points {
    list-style: none;
    padding: 0;
    display: grid;
    gap: var(--space-3);
    margin-top: var(--space-5);
  }
  .points li {
    display: flex;
    gap: var(--space-3);
    align-items: center;
  }
  .points :global(svg),
  :global(.ok) {
    color: var(--correct);
    flex: none;
  }
  .choices {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: var(--space-3);
    margin-top: var(--space-5);
  }
  .choices.three {
    grid-template-columns: repeat(3, 1fr);
  }
  .choice {
    display: grid;
    gap: var(--space-1);
    text-align: left;
    padding: var(--space-4);
    border: 2px solid var(--border);
    border-radius: var(--radius-md);
    background: var(--surface);
    color: var(--text);
    font: inherit;
    cursor: default;
  }
  .choice:hover {
    border-color: var(--accent);
  }
  .choice.on {
    border-color: var(--accent);
    background: var(--accent-soft);
  }
  .big {
    font-size: 1.75rem;
    font-weight: 700;
  }
  .custom {
    display: flex;
    align-items: center;
    gap: var(--space-2);
    margin-top: var(--space-4);
  }
  .custom input {
    width: 100px;
    font: inherit;
    padding: var(--space-2);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    background: var(--surface);
    color: var(--text);
  }
  h2 {
    font-size: 1rem;
    margin-top: var(--space-5);
  }
  .list {
    list-style: none;
    padding: 0;
    margin: 0 0 var(--space-4);
    display: grid;
    gap: var(--space-2);
  }
  .list li,
  .list label {
    display: flex;
    align-items: center;
    gap: var(--space-2);
  }
  .list .small {
    margin-left: auto;
  }
  .warn {
    display: flex;
    gap: var(--space-2);
    align-items: center;
    color: var(--review);
  }
  .big-btn {
    min-height: 42px;
    padding: 0 var(--space-6);
  }
  .small {
    font-size: 0.8125rem;
  }
</style>
