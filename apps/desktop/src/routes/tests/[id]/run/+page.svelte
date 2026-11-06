<script lang="ts">
  import { beforeNavigate, goto } from "$app/navigation";
  import { page } from "$app/state";
  import { errorMessage, testsApi, type AnswerState, type QuestionView, type TestSession, type TestState } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import QuestionCard from "$lib/components/QuestionCard.svelte";
  import { clock, num } from "$lib/format";
  import { settings, t } from "$lib/stores/settings.svelte";
  import { ask } from "@tauri-apps/plugin-dialog";
  import Flag from "@lucide/svelte/icons/flag";
  import Pause from "@lucide/svelte/icons/pause";

  const SAVE_EVERY_MS = 5000;
  const id = $derived(Number(page.params.id));

  let s = $state<TestSession | null>(null);
  let error = $state<string | null>(null);
  let answers = $state<Record<string, AnswerState>>({});
  let current = $state(0);
  let remaining = $state(0);
  let submitting = $state(false);
  let leaving = false;
  let announce = $state("");

  // Flat list of questions with their section, for numbering and the palette.
  const flat = $derived(
    s ? s.sections.flatMap((sec, si) => sec.questions.map((q) => ({ q, si, section: sec.name }))) : [],
  );
  const cur = $derived(flat[current]);
  const counts = $derived.by(() => {
    let a = 0, m = 0;
    for (const { q } of flat) {
      const st = answers[q.id];
      if (st?.choice != null) a++;
      if (st?.marked) m++;
    }
    return { answered: a, unanswered: flat.length - a, marked: m };
  });

  function stateOf(q: QuestionView): string {
    const st = answers[q.id];
    if (!st?.visited) return "not-visited";
    if (st.choice != null && st.marked) return "answered-marked";
    if (st.marked) return "marked";
    if (st.choice != null) return "answered";
    return "not-answered";
  }

  function testState(): TestState {
    return { answers: $state.snapshot(answers), current };
  }

  let saveTimer: ReturnType<typeof setTimeout> | null = null;
  async function save() {
    if (!s || s.status !== "in_progress" || submitting) return;
    try {
      await testsApi.save(id, testState(), Math.round(remaining));
    } catch (e) {
      error = errorMessage(e);
    }
  }
  function saveSoon() {
    if (saveTimer) clearTimeout(saveTimer);
    saveTimer = setTimeout(save, 300);
  }

  function visit(i: number) {
    if (!flat[i]) return;
    current = i;
    const qid = flat[i].q.id;
    answers[qid] = { ...(answers[qid] ?? { choice: null, marked: false, visited: false, time_ms: 0 }), visited: true };
    saveSoon();
  }

  function choose(i: number) {
    const qid = cur.q.id;
    answers[qid] = { ...answers[qid], choice: i, visited: true };
    saveSoon();
  }

  function clear() {
    const qid = cur.q.id;
    answers[qid] = { ...answers[qid], choice: null };
    saveSoon();
  }

  function markAndNext() {
    const qid = cur.q.id;
    answers[qid] = { ...answers[qid], marked: !answers[qid]?.marked };
    if (answers[qid].marked) visit(Math.min(current + 1, flat.length - 1));
    else saveSoon();
  }

  async function load(testId: number, lang: string) {
    try {
      const sess = await testsApi.session(testId, lang);
      if (sess.status === "submitted") return goto(`/tests/${testId}/result`, { replaceState: true });
      if (sess.status === "ready") await testsApi.start(testId);
      sess.status = "in_progress";
      s = sess;
      answers = sess.state.answers ?? {};
      remaining = sess.remaining_ms;
      visit(Math.min(sess.state.current ?? 0, Math.max(0, flat.length - 1)));
      if (remaining <= 0) submit(true);
    } catch (e) {
      error = errorMessage(e);
    }
  }

  $effect(() => {
    load(id, settings.lang);
  });

  // Timer: counts down, adds time to the current question, saves every few seconds.
  $effect(() => {
    if (!s) return;
    let last = performance.now();
    let sinceSave = 0;
    const tick = setInterval(() => {
      const now = performance.now();
      const dt = now - last;
      last = now;
      if (submitting) return;
      const before = remaining;
      remaining = Math.max(0, remaining - dt);
      if (before > 300_000 && remaining <= 300_000) announce = t("run.five_min");
      if (before > 60_000 && remaining <= 60_000) announce = t("run.one_min");
      const qid = flat[current]?.q.id;
      if (qid && answers[qid]) answers[qid].time_ms = Math.round((answers[qid].time_ms ?? 0) + dt);
      sinceSave += dt;
      if (sinceSave >= SAVE_EVERY_MS) {
        sinceSave = 0;
        save();
      }
      if (remaining <= 0) {
        announce = t("run.time_up");
        submit(true);
      }
    }, 250);
    return () => clearInterval(tick);
  });

  async function submit(auto = false) {
    if (submitting || !s) return;
    if (!auto) {
      const ok = await ask(
        t("run.submit_confirm", { a: counts.answered, u: counts.unanswered, m: counts.marked }),
        { title: t("run.submit"), kind: "warning", okLabel: t("run.submit"), cancelLabel: t("common.cancel") },
      );
      if (!ok) return;
    }
    submitting = true;
    try {
      await testsApi.submit(id, testState(), Math.round(remaining));
      leaving = true;
      goto(`/tests/${id}/result`, { replaceState: true });
    } catch (e) {
      error = errorMessage(e);
      submitting = false;
    }
  }

  async function pauseAndExit() {
    leaving = true;
    await save();
    goto(`/tests`);
  }

  // Leaving the exam view (sidebar is hidden, but Back / shortcuts still navigate).
  beforeNavigate((nav) => {
    if (leaving || submitting || !s) return;
    nav.cancel();
    const target = nav.to?.url;
    ask(t("run.pause_confirm"), {
      title: t("run.pause"),
      kind: "warning",
      okLabel: t("run.pause"),
      cancelLabel: t("common.cancel"),
    }).then(async (ok) => {
      if (!ok) return;
      leaving = true;
      await save();
      goto(target ? target.pathname : "/tests");
    });
  });

  function onkeydown(e: KeyboardEvent) {
    if (!cur || submitting) return;
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
      e.preventDefault();
      submit();
      return;
    }
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    if ((e.target as HTMLElement).closest("input, textarea, select")) return;
    const k = e.key.toLowerCase();
    const idx = "1234".indexOf(k) >= 0 ? Number(k) - 1 : "abcd".indexOf(k);
    if (idx >= 0 && idx < (cur.q.options?.length ?? 4)) {
      e.preventDefault();
      choose(idx);
    } else if (e.key === "ArrowRight") {
      e.preventDefault();
      visit(Math.min(current + 1, flat.length - 1));
    } else if (e.key === "ArrowLeft") {
      e.preventDefault();
      visit(Math.max(current - 1, 0));
    } else if (k === "m") {
      e.preventDefault();
      markAndNext();
    }
  }

  const marking = $derived.by(() => {
    if (!s || !cur) return "";
    const sec = s.sections[cur.si];
    return sec.negative > 0 ? `+${num(sec.marks_each)} / −${num(sec.negative)}` : `+${num(sec.marks_each)}`;
  });
  const warn = $derived(remaining <= 60_000 ? "critical" : remaining <= 300_000 ? "low" : "");
</script>

<svelte:window {onkeydown} />

<div class="exam">
  {#if error}
    <div class="pad"><ErrorBox message={error} onretry={() => { error = null; load(id, settings.lang); }} /></div>
  {:else if !s || !cur}
    <p class="pad muted">{t("common.loading")}</p>
  {:else}
    <header class="bar chrome">
      <strong class="title">{s.title}</strong>
      <div class="timer {warn}" role="timer" aria-label={t("run.time_left")}>
        <span class="muted small">{t("run.time_left")}</span>
        <span class="clock">{clock(remaining)}</span>
      </div>
      <div class="baractions">
        <button class="btn btn-ghost" onclick={pauseAndExit}><Pause size={16} aria-hidden="true" />{t("run.pause")}</button>
        <button class="btn btn-primary" onclick={() => submit()} disabled={submitting}>{t("run.submit")}</button>
      </div>
    </header>
    <p class="sr-only" aria-live="assertive">{announce}</p>

    <div class="body">
      <main class="qpane">
        <div class="qhead">
          <span class="muted">
            {#if s.sections.length > 1}{cur.section} · {/if}{t("run.question", { i: current + 1, n: flat.length })}
          </span>
          <span class="muted small">{marking}</span>
        </div>
        {#key cur.q.id}
          <QuestionCard q={cur.q} selected={answers[cur.q.id]?.choice ?? null} result={null} onselect={choose} />
        {/key}

        <div class="nav chrome">
          <button class="btn" onclick={() => visit(current - 1)} disabled={current === 0}>{t("run.prev")}</button>
          <button class="btn btn-ghost" onclick={clear} disabled={answers[cur.q.id]?.choice == null}>{t("run.clear")}</button>
          <button class="btn" onclick={markAndNext}>
            <Flag size={16} aria-hidden="true" />{answers[cur.q.id]?.marked ? t("run.unmark") : t("run.mark_next")}
          </button>
          <button class="btn btn-primary" onclick={() => visit(Math.min(current + 1, flat.length - 1))} disabled={current === flat.length - 1}>
            {t("run.save_next")}
          </button>
        </div>
        <p class="muted small keys">{t("run.keys")}</p>
      </main>

      <aside class="palette chrome" aria-label={t("run.palette")}>
        {#each s.sections as sec, si (sec.id)}
          {#if s.sections.length > 1}<p class="small muted secname">{sec.name}</p>{/if}
          <div class="cells">
            {#each flat as f, i (f.q.id)}
              {#if f.si === si}
                <button
                  class="cell {stateOf(f.q)}"
                  class:current={i === current}
                  aria-current={i === current ? "true" : undefined}
                  aria-label="{t('run.question', { i: i + 1, n: flat.length })}, {stateOf(f.q).replace('-', ' ')}"
                  onclick={() => visit(i)}>{i + 1}</button>
              {/if}
            {/each}
          </div>
        {/each}
        <ul class="legend small">
          <li><span class="cell answered"></span>{t("run.legend.answered")} ({counts.answered})</li>
          <li><span class="cell not-answered"></span>{t("run.legend.not_answered")}</li>
          <li><span class="cell not-visited"></span>{t("run.legend.not_visited")}</li>
          <li><span class="cell marked"></span>{t("run.legend.marked")} ({counts.marked})</li>
          <li><span class="cell answered-marked"></span>{t("run.legend.answered_marked")}</li>
        </ul>
      </aside>
    </div>
  {/if}
</div>

<style>
  .exam {
    height: 100vh;
    display: flex;
    flex-direction: column;
    background: var(--bg);
  }
  .pad {
    padding: var(--space-6);
  }
  .bar {
    flex: none;
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    align-items: center;
    gap: var(--space-4);
    padding: var(--space-2) var(--space-5);
    border-bottom: 1px solid var(--border);
    background: var(--surface);
  }
  .title {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .timer {
    display: grid;
    justify-items: center;
    line-height: 1.2;
  }
  .clock {
    font-size: 1.5rem;
    font-weight: 700;
    font-variant-numeric: tabular-nums;
  }
  .timer.low .clock {
    color: var(--review);
  }
  .timer.critical .clock {
    color: var(--wrong);
  }
  .baractions {
    justify-self: end;
    display: flex;
    gap: var(--space-2);
  }
  .body {
    flex: 1;
    min-height: 0;
    display: grid;
    grid-template-columns: minmax(0, 1fr) 280px;
  }
  .qpane {
    overflow-y: auto;
    overscroll-behavior: none;
    padding: var(--space-5) var(--space-6) var(--space-7);
  }
  .qhead {
    display: flex;
    justify-content: space-between;
    max-width: var(--read-width);
    margin-bottom: var(--space-4);
  }
  .nav {
    display: flex;
    gap: var(--space-2);
    flex-wrap: wrap;
    margin-top: var(--space-5);
    max-width: var(--read-width);
  }
  .nav .btn-primary {
    margin-left: auto;
  }
  .keys {
    margin-top: var(--space-3);
  }
  .palette {
    overflow-y: auto;
    border-left: 1px solid var(--border);
    background: var(--surface);
    padding: var(--space-4);
  }
  .secname {
    margin: var(--space-3) 0 var(--space-1);
  }
  .cells {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: var(--space-2);
  }
  .cell {
    display: inline-grid;
    place-items: center;
    height: 36px;
    min-width: 36px;
    border-radius: var(--radius-sm);
    border: 1px solid var(--border);
    background: var(--surface);
    color: var(--text);
    font: inherit;
    font-size: 0.875rem;
    font-variant-numeric: tabular-nums;
    cursor: default;
  }
  .cell.not-answered {
    border: 2px solid var(--wrong);
  }
  .cell.answered {
    background: var(--correct);
    border-color: var(--correct);
    color: var(--accent-fg);
  }
  .cell.marked {
    background: var(--review);
    border-color: var(--review);
    color: var(--accent-fg);
  }
  .cell.answered-marked {
    background: var(--review);
    border-color: var(--correct);
    color: var(--accent-fg);
    box-shadow: inset 0 0 0 2px var(--correct);
  }
  .cell.current {
    outline: 2px solid var(--accent);
    outline-offset: 2px;
  }
  .legend {
    list-style: none;
    padding: 0;
    margin: var(--space-5) 0 0;
    display: grid;
    gap: var(--space-2);
  }
  .legend li {
    display: flex;
    align-items: center;
    gap: var(--space-2);
  }
  .legend .cell {
    height: 16px;
    min-width: 16px;
    width: 16px;
  }
  .small {
    font-size: 0.8125rem;
  }
</style>
