<script lang="ts">
  import { api, errorMessage, type ProgressView } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import ProgressBar from "$lib/components/ProgressBar.svelte";
  import { date, num } from "$lib/format";
  import { settings, t } from "$lib/stores/settings.svelte";
  import Flame from "@lucide/svelte/icons/flame";
  import Target from "@lucide/svelte/icons/target";

  let v = $state<ProgressView | null>(null);
  let error = $state<string | null>(null);

  async function load(lang: string) {
    error = null;
    try {
      v = await api.progress(lang);
    } catch (e) {
      error = errorMessage(e);
    }
  }

  $effect(() => {
    load(settings.lang);
  });

  // Heatmap: weeks as columns (Mon..Sun rows), like a contribution graph.
  const weeks = $derived.by(() => {
    if (!v) return [];
    const days = v.days.map((d) => ({ ...d, dow: (new Date(d.date + "T00:00:00").getDay() + 6) % 7 }));
    const cols: ((typeof days)[number] | null)[][] = [];
    let col: ((typeof days)[number] | null)[] = Array(7).fill(null);
    for (const d of days) {
      col[d.dow] = d;
      if (d.dow === 6) {
        cols.push(col);
        col = Array(7).fill(null);
      }
    }
    if (col.some(Boolean)) cols.push(col);
    return cols;
  });
  const maxDay = $derived(Math.max(1, ...(v?.days.map((d) => d.attempts) ?? [1])));
  const level = (n: number) => (n === 0 ? 0 : Math.min(4, Math.ceil((n / maxDay) * 4)));
  const weakTopics = $derived(v ? v.weak.map((id) => v!.topics.find((x) => x.topic_id === id)!).filter(Boolean) : []);
  const fmtDay = (d: string) => new Intl.DateTimeFormat("en-IN", { dateStyle: "medium" }).format(new Date(d + "T00:00:00"));
</script>

<div class="page">
  <h1>{t("progress.title")}</h1>
  <p class="muted">{t("progress.subtitle")}</p>

  {#if error}
    <ErrorBox message={error} onretry={() => load(settings.lang)} />
  {:else if !v}
    <p class="muted">{t("common.loading")}</p>
  {:else}
    <div class="tiles">
      <div class="card tile">
        <span class="muted small"><Target size={14} aria-hidden="true" /> {t("progress.today")}</span>
        <span class="num">{v.today} <span class="of">/ {v.daily_goal}</span></span>
        <ProgressBar value={Math.min(v.today, v.daily_goal)} max={v.daily_goal} label={t("home.goal")} />
      </div>
      <div class="card tile">
        <span class="muted small"><Flame size={14} aria-hidden="true" /> {t("progress.streak")}</span>
        <span class="num">{t("progress.days", { n: v.streak })}</span>
        <span class="muted small">{t("progress.best")}: {t("progress.days", { n: v.best_streak })}</span>
      </div>
      <div class="card tile">
        <span class="muted small" title={t("progress.accuracy_help")}>{t("progress.accuracy")}</span>
        <span class="num">{v.attempted ? `${num(v.accuracy)}%` : "—"}</span>
        <span class="muted small">{t("progress.accuracy_help")}</span>
      </div>
      <div class="card tile">
        <span class="muted small">{t("progress.practised")}</span>
        <span class="num">{v.attempted}</span>
        <span class="muted small">{t("progress.answers", { n: v.total_attempts })}</span>
      </div>
    </div>

    <section>
      <h2>{t("progress.activity")}</h2>
      <div class="card heat">
        <div class="grid" role="img" aria-label={t("progress.activity")}>
          {#each weeks as col, ci (ci)}
            <div class="col">
              {#each col as d, ri (ri)}
                {#if d}
                  <span class="cell l{level(d.attempts)}" title={t("progress.activity_cell", { date: fmtDay(d.date), n: d.attempts })}></span>
                {:else}
                  <span class="cell empty"></span>
                {/if}
              {/each}
            </div>
          {/each}
        </div>
        <div class="legend muted small">
          {t("progress.less")}
          {#each [0, 1, 2, 3, 4] as l (l)}<span class="cell l{l}"></span>{/each}
          {t("progress.more")}
        </div>
      </div>
    </section>

    {#if v.total_attempts === 0}
      <p class="card muted">{t("progress.empty")}</p>
    {/if}

    <div class="two">
      <section>
        <h2>{t("progress.weak")}</h2>
        <p class="muted small">{t("progress.weak_help")}</p>
        {#if weakTopics.length === 0}
          <p class="muted">{t("progress.weak_none")}</p>
        {:else}
          <ul class="card list">
            {#each weakTopics as w (w.topic_id)}
              <li class="row">
                <div>
                  <strong lang={settings.lang}>{w.title}</strong>
                  <span class="muted small">{num(w.accuracy)}% · {w.correct}/{w.attempted}</span>
                </div>
                <a class="btn btn-primary" href="/topic/{w.topic_id}/practice">{t("progress.practise")}</a>
              </li>
            {/each}
          </ul>
        {/if}
      </section>

      <section>
        <h2>{t("progress.tests")}</h2>
        {#if v.tests.length === 0}
          <p class="muted">{t("progress.tests_none")}</p>
        {:else}
          <div class="card bars">
            {#each v.tests as tp (tp.id)}
              <a class="bar" href="/tests/{tp.id}/result" title="{tp.title} · {date(tp.submitted_at)} · {num(tp.pct)}%" aria-label="{tp.title}, {date(tp.submitted_at)}: {num(tp.pct)}%">
                <span class="fill" style="height: {Math.max(2, tp.pct)}%"></span>
                <span class="pct small">{Math.round(tp.pct)}%</span>
              </a>
            {/each}
          </div>
        {/if}
      </section>
    </div>

    <section>
      <h2>{t("progress.topics")}</h2>
      <table class="card tbl">
        <thead>
          <tr><th>{t("progress.col.topic")}</th><th>{t("progress.col.done")}</th><th>{t("progress.col.accuracy")}</th><th>{t("progress.col.last")}</th></tr>
        </thead>
        <tbody>
          {#each v.topics as tp (tp.topic_id)}
            <tr>
              <td><a href="/topic/{tp.topic_id}" lang={settings.lang}>{tp.title}</a><br /><span class="muted small" lang={settings.lang}>{tp.subject_title}</span></td>
              <td class="num">
                {tp.attempted} / {tp.questions}
                <ProgressBar value={tp.attempted} max={tp.questions} label={tp.title} />
              </td>
              <td class="num">{tp.attempted ? `${num(tp.accuracy)}%` : "—"}</td>
              <td class="muted small">{tp.last_at ? date(tp.last_at) : t("progress.never")}</td>
            </tr>
          {/each}
        </tbody>
      </table>
    </section>
  {/if}
</div>

<style>
  .page {
    max-width: 1100px;
  }
  .tiles {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: var(--space-4);
    margin: var(--space-5) 0;
  }
  .tile {
    display: grid;
    gap: var(--space-1);
    align-content: start;
  }
  .tile :global(svg) {
    vertical-align: -2px;
  }
  .num {
    font-size: 1.75rem;
    font-weight: 700;
    font-variant-numeric: tabular-nums;
  }
  .of {
    font-size: 1rem;
    color: var(--text-muted);
  }
  section {
    margin-top: var(--space-6);
  }
  h2 {
    font-size: 1.125rem;
  }
  .heat {
    display: grid;
    gap: var(--space-3);
    overflow-x: auto;
  }
  .grid {
    display: flex;
    gap: 3px;
  }
  .col {
    display: grid;
    grid-template-rows: repeat(7, 12px);
    gap: 3px;
  }
  .cell {
    display: inline-block;
    width: 12px;
    height: 12px;
    border-radius: 2px;
    background: var(--surface-2);
  }
  .cell.empty {
    background: transparent;
  }
  .cell.l1 {
    background: color-mix(in srgb, var(--correct) 30%, var(--surface-2));
  }
  .cell.l2 {
    background: color-mix(in srgb, var(--correct) 55%, var(--surface-2));
  }
  .cell.l3 {
    background: color-mix(in srgb, var(--correct) 78%, var(--surface-2));
  }
  .cell.l4 {
    background: var(--correct);
  }
  .legend {
    display: flex;
    align-items: center;
    gap: 3px;
  }
  .two {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--space-6);
  }
  .list {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: var(--space-3);
    padding: var(--space-3) var(--space-4);
    border-top: 1px solid var(--border);
  }
  .row:first-child {
    border-top: 0;
  }
  .row > div {
    display: grid;
  }
  .bars {
    display: flex;
    align-items: flex-end;
    gap: var(--space-2);
    height: 160px;
  }
  .bar {
    flex: 1;
    max-width: 40px;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: center;
    text-decoration: none;
    position: relative;
  }
  .fill {
    width: 100%;
    background: var(--accent);
    border-radius: 3px 3px 0 0;
  }
  .pct {
    color: var(--text-muted);
    margin-top: 2px;
  }
  .tbl {
    width: 100%;
    border-collapse: collapse;
    padding: 0;
  }
  .tbl th,
  .tbl td {
    padding: var(--space-2) var(--space-3);
    border-bottom: 1px solid var(--border);
    text-align: left;
    vertical-align: top;
  }
  .tbl th {
    font-size: 0.8125rem;
    color: var(--text-muted);
    font-weight: 600;
  }
  .tbl tr:last-child td {
    border-bottom: 0;
  }
  .tbl td.num {
    font-variant-numeric: tabular-nums;
    min-width: 140px;
  }
  .small {
    font-size: 0.8125rem;
  }
</style>
