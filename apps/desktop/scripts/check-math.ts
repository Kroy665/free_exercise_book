// Checks that every formula ($…$, $$…$$) and every ```plot / ```chart block in the content
// renders without errors. Run by tools/content-check/validate.py, which sends the parsed
// texts as JSON on stdin: [{ "where": "path#field", "text": "..." }, ...].
// Exit code 1 if anything fails. Needs Node 23.6+ (runs TypeScript directly).
import katex from "katex";
import { renderChart, renderPlot } from "../src/lib/markdown/figures.ts";

const MACROS = { "\\R": "\\mathbb{R}", "\\N": "\\mathbb{N}", "\\Z": "\\mathbb{Z}", "\\Q": "\\mathbb{Q}", "\\C": "\\mathbb{C}" };

let input = "";
for await (const chunk of process.stdin) input += chunk;
const items: { where: string; text: string }[] = JSON.parse(input);

let errors = 0, formulas = 0, figures = 0;
const fail = (where: string, msg: string) => {
  errors++;
  console.log(`ERR ${where}: ${msg}`);
};

for (const { where, text } of items) {
  // Figures first; then remove fenced blocks so their contents are not read as maths.
  let rest = text.replace(/^```(plot|chart)[^\n]*\n([\s\S]*?)^```\s*$/gm, (_m, kind: string, body: string) => {
    figures++;
    try {
      kind === "plot" ? renderPlot(body) : renderChart(body);
    } catch (e) {
      fail(where, `${kind}: ${(e as Error).message}`);
    }
    return "";
  });
  rest = rest.replace(/^```[\s\S]*?^```\s*$/gm, "").replace(/`[^`\n]*`/g, "");
  const tex = (src: string, display: boolean) => {
    formulas++;
    try {
      katex.renderToString(src, { displayMode: display, throwOnError: true, strict: "error", macros: { ...MACROS } });
    } catch (e) {
      fail(where, `formula "${src.slice(0, 60)}": ${(e as Error).message.replace(/^KaTeX parse error: /, "")}`);
    }
  };
  rest = rest.replace(/\$\$([\s\S]+?)\$\$/g, (_m, body: string) => (tex(body.trim(), true), " "));
  // Inline $…$: no space after the opening or before the closing $ (same rule as the app).
  rest = rest.replace(/(^|[^\\$])\$(?=\S)((?:\\\$|[^$\n])*?\S)\$/g, (_m, pre: string, body: string) => (tex(body, false), pre));
  const stray = rest.match(/(^|[^\\])\$\S/);
  if (stray) fail(where, `unmatched "$" near "${rest.slice(Math.max(0, (stray.index ?? 0) - 20), (stray.index ?? 0) + 30).replace(/\n/g, " ")}"`);
}
console.log(`maths check: ${formulas} formulas, ${figures} figures, ${errors} error(s)`);
process.exit(errors ? 1 : 0);
