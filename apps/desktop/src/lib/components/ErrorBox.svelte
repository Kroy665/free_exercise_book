<script lang="ts">
  import { t } from "$lib/stores/settings.svelte";

  let { message, onretry }: { message: string; onretry?: () => void } = $props();
</script>

<div class="card error" role="alert">
  <strong>{t("common.error")}</strong>
  <p class="muted">{message}</p>
  {#if onretry}
    <button class="btn" onclick={onretry}>{t("common.retry")}</button>
  {/if}
</div>

<style>
  .error {
    border-color: var(--wrong);
  }
</style>
