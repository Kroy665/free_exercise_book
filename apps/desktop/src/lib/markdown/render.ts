// Notes renderer: CommonMark + GFM tables + our custom blocks (docs/CONTENT_STRUCTURE.md §6).
// Raw HTML in content is disabled (docs/PRIVACY_AND_SECURITY.md §2).
import MarkdownIt from "markdown-it";
import container from "markdown-it-container";

const KINDS = ["keyfacts", "exam-tip", "mnemonic", "caution", "timeline", "asof"] as const;
const ANCHOR = /\s*\{#([a-z0-9-]+)\}\s*$/;

export interface RenderEnv {
  labels: Record<string, string>;
  [key: string]: unknown;
}

const md = new MarkdownIt({ html: false, linkify: false, typographer: false });

for (const kind of KINDS) {
  md.use(container, kind, {
    render(tokens: any[], idx: number, _opts: unknown, env: RenderEnv) {
      const tok = tokens[idx];
      if (tok.nesting !== 1) return "</aside>\n";
      let label = env?.labels?.[kind] ?? kind;
      if (kind === "asof") {
        const date = tok.info.trim().split(/\s+/)[1];
        if (date) label += ` ${date}`;
      }
      return `<aside class="callout callout-${kind}"><div class="callout-title">${md.utils.escapeHtml(label)}</div>\n`;
    },
  });
}

// `## Heading {#anchor}` → <h2 id="anchor">Heading</h2>
md.core.ruler.push("heading_anchor", (state) => {
  const toks = state.tokens;
  for (let i = 0; i < toks.length - 1; i++) {
    if (toks[i].type !== "heading_open") continue;
    const inline = toks[i + 1];
    const m = inline.content.match(ANCHOR);
    if (!m) continue;
    toks[i].attrSet("id", m[1]);
    inline.content = inline.content.replace(ANCHOR, "");
    const last = inline.children?.[inline.children.length - 1];
    if (last?.type === "text") last.content = last.content.replace(ANCHOR, "");
  }
});

// Inside :::timeline, "- date | event" → date and event spans for a two-column layout.
md.core.ruler.push("timeline", (state) => {
  let depth = 0;
  for (const tok of state.tokens) {
    if (tok.type === "container_timeline_open") depth++;
    else if (tok.type === "container_timeline_close") depth--;
    else if (depth > 0 && tok.type === "inline" && tok.children?.length) {
      const first = tok.children[0];
      const k = first.type === "text" ? first.content.indexOf(" | ") : -1;
      if (k < 0) continue;
      const open = new state.Token("html_inline", "", 0);
      open.content = `<span class="tl-date">${md.utils.escapeHtml(first.content.slice(0, k))}</span><span class="tl-text">`;
      first.content = first.content.slice(k + 3);
      const close = new state.Token("html_inline", "", 0);
      close.content = "</span>";
      tok.children = [open, ...tok.children, close];
    }
  }
});

export function renderMarkdown(src: string, env: RenderEnv): string {
  return md.render(src, { labels: env.labels });
}

/** Inline markdown only (bold/italic in question text), HTML-escaped. */
export function renderInline(src: string): string {
  return md.renderInline(src);
}
