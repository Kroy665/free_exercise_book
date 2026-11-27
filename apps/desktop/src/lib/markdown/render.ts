// Notes renderer: CommonMark + GFM tables + our custom blocks (docs/CONTENT_STRUCTURE.md §6).
// Raw HTML in content is disabled (docs/PRIVACY_AND_SECURITY.md §2).
import MarkdownIt from "markdown-it";
import container from "markdown-it-container";
import katex from "katex";
import "katex/dist/katex.min.css";
import { renderChart, renderPlot, FigureError } from "./figures";

const KINDS = ["keyfacts", "exam-tip", "mnemonic", "caution", "timeline", "asof"] as const;
const ANCHOR = /\s*\{#([a-z0-9-]+)\}\s*$/;

export interface RenderEnv {
  labels: Record<string, string>;
  [key: string]: unknown;
}

const md = new MarkdownIt({ html: false, linkify: false, typographer: false });

// ---------- Maths: $inline$, $$display$$ (inline or as its own block), rendered by KaTeX ----------
const MACROS = { "\\R": "\\mathbb{R}", "\\N": "\\mathbb{N}", "\\Z": "\\mathbb{Z}", "\\Q": "\\mathbb{Q}", "\\C": "\\mathbb{C}" };

export function tex(src: string, display: boolean): string {
  return katex.renderToString(src, { displayMode: display, throwOnError: false, strict: false, trust: false, macros: { ...MACROS } });
}

md.inline.ruler.after("escape", "math_inline", (state, silent) => {
  const s = state.src, start = state.pos;
  if (s[start] !== "$") return false;
  const display = s[start + 1] === "$";
  const open = display ? 2 : 1;
  // Inline: no space right after the opening $ (so "$5 and $10" stays text).
  if (!display && (s[start + 1] === undefined || /\s/.test(s[start + 1]))) return false;
  let end = start + open;
  for (;;) {
    end = s.indexOf(display ? "$$" : "$", end);
    if (end < 0) return false;
    if (s[end - 1] === "\\") { end++; continue; }
    if (!display && /\s/.test(s[end - 1])) { end++; continue; }
    break;
  }
  const body = s.slice(start + open, end);
  if (!body.trim()) return false;
  if (!silent) {
    const tok = state.push(display ? "math_display_inline" : "math_inline", "", 0);
    tok.content = body;
  }
  state.pos = end + open;
  return true;
});

md.block.ruler.before("fence", "math_block", (state, startLine, endLine, silent) => {
  const first = state.src.slice(state.bMarks[startLine] + state.tShift[startLine], state.eMarks[startLine]);
  if (!first.startsWith("$$")) return false;
  let body = first.slice(2), line = startLine, closed = false;
  // "$$a$$ and more text" is a paragraph with inline display maths, not a block.
  if (body.includes("$$") && !body.trimEnd().endsWith("$$")) return false;
  if (body.trimEnd().endsWith("$$") && body.trim().length > 2) {
    body = body.trimEnd().slice(0, -2);
    closed = true;
  }
  while (!closed && ++line < endLine) {
    const text = state.src.slice(state.bMarks[line] + state.tShift[line], state.eMarks[line]);
    if (text.trimEnd().endsWith("$$")) {
      body += "\n" + text.trimEnd().slice(0, -2);
      closed = true;
    } else body += "\n" + text;
  }
  if (!closed) return false;
  if (silent) return true;
  const tok = state.push("math_block", "", 0);
  tok.content = body.trim();
  tok.map = [startLine, line + 1];
  state.line = line + 1;
  return true;
});

md.renderer.rules.math_inline = (t, i) => tex(t[i].content, false);
md.renderer.rules.math_display_inline = (t, i) => `<span class="math-display">${tex(t[i].content, true)}</span>`;
md.renderer.rules.math_block = (t, i) => `<div class="math-display"${lines(t[i])}>${tex(t[i].content, true)}</div>\n`;

// Source line range of a block (data-line / data-line-end), so the lecture can highlight
// the block that holds a given piece of the notes.
function lines(tok: { map: [number, number] | null }): string {
  return tok.map ? ` data-line="${tok.map[0]}" data-line-end="${tok.map[1]}"` : "";
}
md.core.ruler.push("source_lines", (state) => {
  for (const tok of state.tokens) {
    if (tok.map && tok.nesting === 1 && tok.block) {
      tok.attrSet("data-line", String(tok.map[0]));
      tok.attrSet("data-line-end", String(tok.map[1]));
    }
  }
});

// ---------- Graphs and charts: ```plot / ```chart fenced blocks (figures.ts) ----------
const defaultFence = md.renderer.rules.fence!;
md.renderer.rules.fence = (tokens, idx, opts, env, self) => {
  const tok = tokens[idx];
  const kind = tok.info.trim().split(/\s+/)[0];
  if (kind !== "plot" && kind !== "chart") return defaultFence(tokens, idx, opts, env, self);
  try {
    const fig = kind === "plot" ? renderPlot(tok.content) : renderChart(tok.content);
    const keys = fig.legend
      .map((k) => {
        const mark = k.kind === "line"
          ? `<line class="${k.cls}" x1="1" y1="6" x2="21" y2="6"/>`
          : `<rect class="${k.cls}" x="5" y="0" width="12" height="12" rx="2"/>`;
        return `<span class="fig-key"><svg width="22" height="12" aria-hidden="true">${mark}</svg>${md.renderInline(k.label)}</span>`;
      })
      .join("");
    const legend = keys ? `<div class="fig-legend">${keys}</div>` : "";
    const cap = fig.title ? `<figcaption>${md.renderInline(fig.title)}</figcaption>` : "";
    return `<figure class="fig"${lines(tok)}>${fig.svg}${legend}${cap}</figure>\n`;
  } catch (e) {
    const msg = e instanceof FigureError ? e.message : String(e);
    return `<div class="fig-error" role="note">Could not draw this ${kind}: ${md.utils.escapeHtml(msg)}</div>\n`;
  }
};

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
      return `<aside class="callout callout-${kind}"${lines(tok)}><div class="callout-title">${md.utils.escapeHtml(label)}</div>\n`;
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

/** Full markdown (maths, lists, tables, graphs) for worked solutions and explanations. */
export function renderRich(src: string): string {
  return md.render(src, { labels: {} });
}

/** Inline markdown only (bold/italic and maths in question text), HTML-escaped. */
export function renderInline(src: string): string {
  return md.renderInline(src);
}
