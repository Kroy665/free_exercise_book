<script lang="ts">
  let { value, max, label }: { value: number; max: number; label: string } = $props();
  const pct = $derived(max > 0 ? Math.round((value / max) * 100) : 0);
</script>

<div class="bar" role="progressbar" aria-valuemin={0} aria-valuemax={max} aria-valuenow={value} aria-label={label}>
  <div class="fill" style="width: {pct}%"></div>
</div>

<style>
  .bar {
    height: 6px;
    border-radius: 3px;
    background: var(--surface-2);
    overflow: hidden;
  }
  .fill {
    height: 100%;
    background: var(--accent);
    transition: width var(--dur-panel) var(--ease);
  }
</style>
