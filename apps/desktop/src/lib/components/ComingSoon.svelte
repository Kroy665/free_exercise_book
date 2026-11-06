<script lang="ts">
  import { t } from "$lib/stores/settings.svelte";

  let { titleKey, version }: { titleKey: string; version: string } = $props();
</script>

<div class="page">
  <h1>{t(titleKey)}</h1>
  <div class="card">
    <p><strong>{t("common.soon")}</strong></p>
    <p class="muted">{t("soon.text", { version })}</p>
  </div>
</div>
