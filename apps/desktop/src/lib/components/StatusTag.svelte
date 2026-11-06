<script lang="ts">
  import type { ContentStatus } from "$lib/api";
  import { t } from "$lib/stores/settings.svelte";

  let { status }: { status: ContentStatus } = $props();
</script>

<span class="tag tag-{status}" title={status === "ai-generated" ? t("status.ai_note") : undefined}>
  {t(`status.${status}`)}
</span>

<style>
  .tag {
    display: inline-block;
    font-size: 0.75rem;
    line-height: 1.6;
    padding: 0 var(--space-2);
    border-radius: 999px;
    border: 1px solid var(--border);
    color: var(--text-muted);
    white-space: nowrap;
  }
  .tag-ai-generated {
    color: var(--review);
    background: var(--review-bg);
    border-color: transparent;
  }
  .tag-reviewed,
  .tag-verified {
    color: var(--correct);
    background: var(--correct-bg);
    border-color: transparent;
  }
</style>
