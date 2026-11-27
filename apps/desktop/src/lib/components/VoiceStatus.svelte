<script lang="ts">
  // Download prompt, progress and errors for the Kokoro voice ("Listen").
  import { tts, stop, downloadVoice, cancelDownloadPrompt } from "$lib/tts/tts.svelte";

  let { floating = false }: { floating?: boolean } = $props();
  const mb = (n: number) => `${Math.round(n / 1_000_000)} MB`;
</script>

{#if tts.phase === "need-download" || tts.phase === "downloading" || tts.phase === "error"}
  <div class="voice" class:floating role="status">
    {#if tts.phase === "need-download"}
      <p>Listening needs a one-time download of the Kokoro voice ({mb(tts.missingBytes)}). After that it works offline.</p>
      <div class="row">
        <button class="btn btn-primary" onclick={downloadVoice}>Download voice</button>
        <button class="btn btn-ghost" onclick={cancelDownloadPrompt}>Not now</button>
      </div>
    {:else if tts.phase === "downloading"}
      <p>Downloading voice… {tts.total ? Math.floor((100 * tts.done) / tts.total) : 0}%</p>
      <progress max={tts.total || 1} value={tts.done}></progress>
    {:else}
      <p class="err">Voice: {tts.error}</p>
      <div class="row"><button class="btn btn-ghost" onclick={stop}>Dismiss</button></div>
    {/if}
  </div>
{/if}

<style>
  .voice {
    margin: var(--space-3);
    padding: var(--space-3);
    border: 1px solid var(--border);
    border-left: 4px solid var(--accent);
    border-radius: var(--radius-sm);
    background: var(--surface);
    font-size: 0.875rem;
    display: grid;
    gap: var(--space-2);
  }
  .floating {
    position: fixed;
    left: 50%;
    bottom: var(--space-5);
    transform: translateX(-50%);
    margin: 0;
    width: min(440px, calc(100vw - 2 * var(--space-5)));
    box-shadow: 0 6px 24px rgb(0 0 0 / 0.15);
    z-index: 25;
  }
  p {
    margin: 0;
  }
  progress {
    width: 100%;
  }
  .row {
    display: flex;
    gap: var(--space-2);
  }
  .err {
    color: var(--wrong);
  }
</style>
