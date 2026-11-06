<script lang="ts">
  import { page } from "$app/state";
  import { api, errorMessage, type QuestionView, type TopicView } from "$lib/api";
  import ErrorBox from "$lib/components/ErrorBox.svelte";
  import PracticeSession from "$lib/components/PracticeSession.svelte";
  import { settings, t } from "$lib/stores/settings.svelte";

  let topic = $state<TopicView | null>(null);
  let questions = $state<QuestionView[] | null>(null);
  let error = $state<string | null>(null);
  const id = $derived(page.params.id ?? "");

  async function load(topicId: string, lang: string) {
    error = null;
    try {
      const [tp, qs] = await Promise.all([api.topicGet(topicId, lang), api.practiceQuestions(topicId, lang)]);
      // ?q=<question id> (from search): start with that question.
      const first = page.url.searchParams.get("q");
      const i = first ? qs.findIndex((q) => q.id === first) : -1;
      topic = tp;
      questions = i > 0 ? [qs[i], ...qs.slice(0, i), ...qs.slice(i + 1)] : qs;
    } catch (e) {
      error = errorMessage(e);
    }
  }

  $effect(() => {
    load(id, settings.lang);
  });
</script>

<div class="page">
  {#if error}
    <ErrorBox message={error} onretry={() => load(id, settings.lang)} />
  {:else if !topic || !questions}
    <p class="muted">{t("common.loading")}</p>
  {:else}
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/library">{t("nav.library")}</a> › <a href="/topic/{topic.id}">{topic.title}</a> › {t("topic.practice")}
    </nav>
    <h1 lang={topic.lang}>{topic.title}</h1>
    {#key questions}
      <PracticeSession {questions} mode="practice" backHref="/topic/{topic.id}" />
    {/key}
  {/if}
</div>
