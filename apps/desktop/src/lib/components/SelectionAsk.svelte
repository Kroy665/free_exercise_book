<script lang="ts">
  // A small "Ask / Listen" bar that appears next to any text the user selects.
  import { askAbout } from "$lib/stores/assistant.svelte";
  import { speak } from "$lib/tts/tts.svelte";
  import MessageCircleQuestion from "@lucide/svelte/icons/message-circle-question";
  import Volume2 from "@lucide/svelte/icons/volume-2";

  let { root }: { root: HTMLElement | null } = $props();

  let pos = $state<{ x: number; y: number } | null>(null);
  let text = $state("");

  /** Selected text with rendered formulas turned back into $LaTeX$ (KaTeX keeps the source). */
  function selectedText(sel: Selection): string {
    const range = sel.getRangeAt(0);
    const frag = range.cloneContents();
    // A selection inside one formula: use the whole formula.
    const host = (range.commonAncestorContainer instanceof Element ? range.commonAncestorContainer : range.commonAncestorContainer.parentElement)?.closest(".katex");
    if (host) {
      const ann = host.querySelector('annotation[encoding="application/x-tex"]');
      if (ann?.textContent) return `$${ann.textContent.trim()}$`;
    }
    for (const k of Array.from(frag.querySelectorAll(".katex"))) {
      const ann = k.querySelector('annotation[encoding="application/x-tex"]');
      k.replaceWith(ann?.textContent ? `$${ann.textContent.trim()}$` : "");
    }
    // Orphan pieces of a formula cut by the selection edge.
    for (const k of Array.from(frag.querySelectorAll(".katex-html, .katex-mathml"))) k.remove();
    const div = document.createElement("div");
    div.append(frag);
    return (div.innerText || div.textContent || "").replace(/\n{3,}/g, "\n\n").trim();
  }

  function update() {
    const sel = window.getSelection();
    if (!root || !sel || sel.isCollapsed || !sel.rangeCount) { pos = null; return; }
    const range = sel.getRangeAt(0);
    if (!root.contains(range.commonAncestorContainer)) { pos = null; return; }
    const t = selectedText(sel);
    if (t.length < 2) { pos = null; return; }
    const rects = range.getClientRects();
    const r = rects[rects.length - 1] ?? range.getBoundingClientRect();
    text = t;
    pos = { x: Math.min(r.right, window.innerWidth - 200), y: r.bottom + 6 };
  }

  function onmouseup(e: MouseEvent) {
    if ((e.target as HTMLElement).closest(".askbar")) return;
    setTimeout(update, 0);
  }
  function onkeyup(e: KeyboardEvent) {
    if (e.shiftKey || e.key === "Escape") setTimeout(update, 0);
  }
  function onselectionchange() {
    const sel = window.getSelection();
    if (!sel || sel.isCollapsed) pos = null;
  }
  function onscroll() {
    pos = null;
  }

  function ask() {
    askAbout(text);
    pos = null;
    window.getSelection()?.removeAllRanges();
  }
  function listen() {
    speak(`sel:${text.slice(0, 40)}`, text);
    pos = null;
  }
</script>

<svelte:document {onmouseup} {onkeyup} {onselectionchange} />
<svelte:window onscrollcapture={onscroll} />

{#if pos}
  <div class="askbar" style="left:{pos.x}px; top:{pos.y}px" role="toolbar" aria-label="Selected text">
    <button class="btn btn-primary" onmousedown={(e) => e.preventDefault()} onclick={ask}>
      <MessageCircleQuestion size={16} aria-hidden="true" /> Ask
    </button>
    <button class="btn btn-ghost" onmousedown={(e) => e.preventDefault()} onclick={listen} title="Read aloud">
      <Volume2 size={16} aria-hidden="true" /> Listen
    </button>
  </div>
{/if}

<style>
  .askbar {
    position: fixed;
    z-index: 30;
    display: flex;
    gap: 2px;
    padding: 3px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    box-shadow: 0 6px 20px rgb(0 0 0 / 0.15);
    transform: translateX(-50%);
  }
  .askbar .btn {
    min-height: 30px;
    gap: var(--space-1);
    font-size: 0.875rem;
  }
</style>
