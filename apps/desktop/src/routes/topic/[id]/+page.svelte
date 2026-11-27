<script lang="ts">
  import { page } from "$app/state";
  import { api, errorMessage, type Lecture, type TopicView } from "$lib/api";
  import LecturePanel from "$lib/components/LecturePanel.svelte";
  import { lecture, load as loadLecture, playFrom, stopLecture } from "$lib/lecture/lecture.svelte";
  import GraduationCap from "@lucide/svelte/icons/graduation-cap";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import StatusTag from "$lib/components/StatusTag.svelte";
  import { renderMarkdown } from "$lib/markdown/render";
  import { settings, t, tc } from "$lib/stores/settings.svelte";
  import { openUrl } from "@tauri-apps/plugin-opener";
  import { tick } from "svelte";

  const CALLOUTS = ["keyfacts", "exam-tip", "mnemonic", "caution", "timeline", "asof"];

  let topic = $state<TopicView | null>(null);
  let lectureData = $state<Lecture | null>(null);
  let lectureOpen = $state(false);
  let error = $state<string | null>(null);
  const id = $derived(page.params.id ?? "");

  async function load(topicId: string, lang: string) {
    error = null;
    try {
      if (topic?.id !== topicId) lectureOpen = false;
      topic = await api.topicGet(topicId, lang);
      lectureData = await api.lectureGet(topicId, lang).catch(() => null);
      loadLecture(topicId, lectureData);
      await tick();
      const hash = decodeURIComponent(location.hash.slice(1));
      if (hash) document.getElementById(hash)?.scrollIntoView();
    } catch (e) {
      error = errorMessage(e);
    }
  }

  $effect(() => {
    load(id, settings.lang);
  });

  const labels = $derived(Object.fromEntries(CALLOUTS.map((k) => [k, tc(`callout.${k}`, topic?.lang ?? "en")])));
  const sections = $derived(
    topic?.sections.map((s) => ({ ...s, html: renderMarkdown(s.body_md, { labels }) })) ?? [],
  );

  // External links in notes open in the system browser (PRIVACY_AND_SECURITY §3).
  // Delegated listener: Enter on a focused link also fires "click".
  let article = $state<HTMLElement | null>(null);
  $effect(() => {
    article?.addEventListener("click", onLinkClick);
    return () => article?.removeEventListener("click", onLinkClick);
  });

  function startLecture() {
    lectureOpen = true;
    playFrom(lecture.index);
  }

  // Leaving the page ends the lecture.
  $effect(() => () => stopLecture());

  // The blackboard: highlight and scroll to the part of the notes the teacher is explaining.
  $effect(() => {
    const seg = lectureOpen && lecture.data ? lecture.data.segments[lecture.index] : undefined;
    void lecture.phase;
    article?.querySelectorAll(".lecture-focus, .lecture-section").forEach((el) => el.classList.remove("lecture-focus", "lecture-section"));
    if (!seg || !topic || !article) return;
    const sec = topic.sections.find((s) => s.anchor === seg.section);
    const heading = article.querySelector(`h2[id="${CSS.escape(seg.section)}"]`);
    const box = heading?.closest("section");
    if (!sec || !box) return;
    box.classList.add("lecture-section");
    let target: Element | null = heading;
    const at = seg.focus ? sec.body_md.indexOf(seg.focus) : -1;
    if (at >= 0) {
      const line = sec.body_md.slice(0, at).split("\n").length - 1;
      let best: Element | null = null;
      let span = Infinity;
      for (const el of Array.from(box.querySelectorAll("[data-line]"))) {
        const a = Number(el.getAttribute("data-line")), b = Number(el.getAttribute("data-line-end"));
        if (a <= line && line < b && b - a <= span) {
          best = el;
          span = b - a;
        }
      }
      if (best) target = best;
    }
    target?.classList.add("lecture-focus");
    target?.scrollIntoView({ behavior: "smooth", block: "center" });
  });

  function onLinkClick(e: MouseEvent) {
    const a = (e.target as HTMLElement).closest("a");
    if (a && /^https:\/\//.test(a.getAttribute("href") ?? "")) {
      e.preventDefault();
      openUrl(a.href);
    }
  }
</script>

<div class="page">
  {#if error}
    <ErrorBox message={error} onretry={() => load(id, settings.lang)} />
  {:else if !topic}
    <p class="muted">{t("common.loading")}</p>
  {:else}
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/library">{t("nav.library")}</a> › {topic.subject_title} › {topic.unit_title}
    </nav>
    <header class="head">
      <h1 lang={topic.lang}>{topic.title}</h1>
      <div class="meta">
        <StatusTag status={topic.meta.status} />
        <span class="muted">{t("library.questions", { n: topic.question_count })}</span>
        {#if topic.meta.estimated_minutes}
          <span class="muted">· {t("library.minutes", { n: topic.meta.estimated_minutes })}</span>
        {/if}
      </div>
      {#if lectureData && !lectureOpen}
        <button class="btn btn-primary lecture-btn" onclick={startLecture}>
          <GraduationCap size={18} aria-hidden="true" /> Start lecture
          <span class="muted-on-accent">· the teacher explains this topic, with questions</span>
        </button>
      {/if}
      <div class="tabs" role="tablist">
        <a role="tab" aria-selected="true" class="tab on" href="/topic/{topic.id}">{t("topic.notes")}</a>
        <a role="tab" aria-selected="false" class="tab" href="/topic/{topic.id}/practice">{t("topic.practice")}</a>
      </div>
    </header>

    {#if topic.lang !== settings.lang}
      <p class="card notice">{t("topic.fallback")}</p>
    {/if}

    <div class="layout" class:teaching={lectureOpen}>
      <article class="prose" lang={topic.lang} bind:this={article}>
        {#each sections as s (s.anchor)}
          <section>
            <h2 id={s.anchor}>{s.heading}</h2>
            {@html s.html}
          </section>
        {/each}

        <div class="end card">
          <a class="btn btn-primary" href="/topic/{topic.id}/practice">{t("topic.start_practice")}</a>
          {#if topic.meta.sources.length}
            <h3>{t("topic.sources")}</h3>
            <ul class="muted small">
              {#each topic.meta.sources as src (src)}<li>{src}</li>{/each}
            </ul>
          {/if}
        </div>
      </article>

      {#if lectureOpen}
        <LecturePanel topicId={topic.id} onclose={() => (lectureOpen = false)} />
      {:else}
      <aside class="toc" aria-label={t("topic.contents")}>
        <div class="toc-inner">
          <strong class="muted small">{t("topic.contents")}</strong>
          <ul>
            {#each sections as s (s.anchor)}
              <li><a href="#{s.anchor}">{s.heading}</a></li>
            {/each}
          </ul>
        </div>
      </aside>
      {/if}
    </div>
  {/if}
</div>

<style>
  .head {
    margin-bottom: var(--space-5);
  }
  .meta {
    display: flex;
    gap: var(--space-2);
    align-items: center;
    margin-bottom: var(--space-4);
  }
  .tabs {
    display: flex;
    gap: var(--space-1);
    border-bottom: 1px solid var(--border);
  }
  .tab {
    padding: var(--space-2) var(--space-4);
    color: var(--text-muted);
    text-decoration: none;
    border-bottom: 2px solid transparent;
    margin-bottom: -1px;
  }
  .tab.on {
    color: var(--text);
    border-bottom-color: var(--accent);
    font-weight: 600;
  }
  .notice {
    border-color: var(--review);
    background: var(--review-bg);
    padding: var(--space-3) var(--space-4);
  }
  .layout {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 220px;
    gap: var(--space-6);
  }
  .layout.teaching {
    grid-template-columns: minmax(0, 1fr) minmax(320px, 400px);
    gap: var(--space-5);
  }
  .lecture-btn {
    gap: var(--space-2);
    margin-bottom: var(--space-4);
  }
  .muted-on-accent {
    opacity: 0.85;
    font-weight: 400;
  }
  /* Blackboard: the section being taught is marked, and the exact part glows. */
  article :global(section.lecture-section) {
    border-left: 3px solid var(--accent-soft);
    padding-left: var(--space-4);
    margin-left: calc(-1 * var(--space-4) - 3px);
  }
  article :global(.lecture-focus) {
    background: var(--accent-soft);
    outline: 2px solid var(--accent);
    outline-offset: 4px;
    border-radius: 4px;
    transition: background 0.3s;
  }
  .prose section:first-child h2 {
    margin-top: 0;
  }
  .toc-inner {
    position: sticky;
    top: var(--space-5);
  }
  .toc ul {
    list-style: none;
    padding: 0;
    margin: var(--space-2) 0 0;
    border-left: 1px solid var(--border);
  }
  .toc a {
    display: block;
    padding: var(--space-1) var(--space-3);
    color: var(--text-muted);
    text-decoration: none;
    font-size: 0.875rem;
  }
  .toc a:hover {
    color: var(--accent);
  }
  .end {
    margin-top: var(--space-7);
  }
  .end h3 {
    margin-top: var(--space-5);
    font-size: 1rem;
  }
  .small {
    font-size: 0.8125rem;
  }
  @media (max-width: 1280px) {
    .layout:not(.teaching) {
      grid-template-columns: minmax(0, 1fr);
    }
    .toc {
      display: none;
    }
  }
</style>
