// Graphs and charts for notes, drawn as inline SVG from a small text spec in a fenced block
// (docs/CONTENT_STRUCTURE.md §6.1). Everything is computed here, offline; colours come from
// CSS classes so light and dark themes both work.
//
// ```plot                              ```chart
// title: $y = x^2 - 2$                 type: bar          # bar | line | histogram | pie | scatter
// x: -3, 3                             title: Marks of 40 students
// f: x^2 - 2 | $y = x^2-2$             labels: 0-10, 10-20, 20-30
// point: sqrt(2), 0 | $\sqrt2$         data: 5, 12, 9 | Section A
// ```                                  ```
import { compile, num, ExprError } from "./expr.ts";

export class FigureError extends Error {}

export interface LegendItem {
  cls: string;
  label: string;
  kind: "line" | "box";
}

export interface Figure {
  svg: string;
  title: string | null;
  /** Shown under the graph as HTML, so labels can contain $maths$. */
  legend: LegendItem[];
}

type Spec = { key: string; value: string; label: string | null }[];

const W = 600, H = 380;
const M = { l: 44, r: 16, t: 14, b: 34 };
const PW = W - M.l - M.r, PH = H - M.t - M.b;
let clipSeq = 0;

function esc(s: string): string {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

/** Plain-text version of a label for SVG (strip $…$ and simple LaTeX). */
function plain(s: string): string {
  return s
    .replace(/\$+/g, "")
    .replace(/\\frac\{([^}]*)\}\{([^}]*)\}/g, "($1)/($2)")
    .replace(/\\sqrt\{([^}]*)\}/g, "√($1)")
    .replace(/\\sqrt/g, "√")
    .replace(/\\(pi)\b/g, "π").replace(/\\theta\b/g, "θ").replace(/\\alpha\b/g, "α").replace(/\\beta\b/g, "β")
    .replace(/\\(le|leq)\b/g, "≤").replace(/\\(ge|geq)\b/g, "≥").replace(/\\infty\b/g, "∞").replace(/\\cdot\b/g, "·")
    .replace(/\^\{([^}]*)\}/g, "^$1").replace(/_\{([^}]*)\}/g, "_$1")
    .replace(/\\([a-zA-Z]+)/g, "$1")
    .replace(/[{}]/g, "")
    .replace(/\^2\b/g, "²").replace(/\^3\b/g, "³");
}

function parseSpec(src: string): Spec {
  const out: Spec = [];
  for (const raw of src.split("\n")) {
    const line = raw.replace(/\s+#.*$/, "").trim();
    if (!line || line.startsWith("#")) continue;
    const m = /^([a-z][a-z0-9-]*)\s*:\s*(.*)$/.exec(line);
    if (!m) throw new FigureError(`cannot read line "${line}" (expected "key: value")`);
    const bar = m[2].lastIndexOf(" | ");
    const value = bar >= 0 ? m[2].slice(0, bar).trim() : m[2].trim();
    const label = bar >= 0 ? m[2].slice(bar + 3).trim() : null;
    out.push({ key: m[1], value, label });
  }
  return out;
}

/** Split on top-level commas (not inside parentheses). */
function splitTop(s: string, sep = ","): string[] {
  const out: string[] = [];
  let depth = 0, cur = "";
  for (const c of s) {
    if (c === "(") depth++;
    if (c === ")") depth--;
    if (c === sep && depth === 0) { out.push(cur.trim()); cur = ""; } else cur += c;
  }
  if (cur.trim()) out.push(cur.trim());
  return out;
}

function pair(v: string, what: string): [number, number] {
  const parts = splitTop(v);
  if (parts.length !== 2) throw new FigureError(`${what} needs two values, like "-3, 3"`);
  const [a, b] = parts.map(num);
  if (!(a < b)) throw new FigureError(`${what}: the first value must be smaller`);
  return [a, b];
}

function fmt(v: number): string {
  if (Math.abs(v) < 1e-10) return "0";
  const s = Math.abs(v) >= 1e4 || Math.abs(v) < 1e-3 ? v.toExponential(1) : String(+v.toFixed(4));
  return s.replace("-", "−");
}

function niceStep(span: number, target = 8): number {
  const raw = span / target, p = Math.pow(10, Math.floor(Math.log10(raw))), f = raw / p;
  return (f < 1.5 ? 1 : f < 3 ? 2 : f < 7 ? 5 : 10) * p;
}

function ticks(a: number, b: number, step: number): number[] {
  const out: number[] = [];
  for (let v = Math.ceil(a / step - 1e-9) * step; v <= b + step * 1e-9; v += step) out.push(Math.abs(v) < step * 1e-9 ? 0 : v);
  return out;
}

function piLabel(v: number): string {
  const k = Math.round((v / Math.PI) * 2); // multiples of π/2
  if (k === 0) return "0";
  const sign = k < 0 ? "−" : "";
  const n = Math.abs(k);
  if (n % 2 === 0) return `${sign}${n / 2 === 1 ? "" : n / 2}π`;
  return `${sign}${n === 1 ? "" : n}π/2`;
}

interface Frame {
  x0: number; x1: number; y0: number; y1: number;
  sx: (x: number) => number; sy: (y: number) => number;
}

function frame(x0: number, x1: number, y0: number, y1: number): Frame {
  return {
    x0, x1, y0, y1,
    sx: (x) => M.l + ((x - x0) / (x1 - x0)) * PW,
    sy: (y) => M.t + PH - ((y - y0) / (y1 - y0)) * PH,
  };
}

const r2 = (v: number) => Math.round(v * 100) / 100;

function axes(f: Frame, opts: { xpi?: boolean; xlabel?: string; ylabel?: string; xAtZero?: boolean }): string {
  const parts: string[] = [];
  const xs = opts.xpi ? ticks(f.x0, f.x1, Math.PI / 2) : ticks(f.x0, f.x1, niceStep(f.x1 - f.x0, 8));
  const ys = ticks(f.y0, f.y1, niceStep(f.y1 - f.y0, 7));
  for (const x of xs) parts.push(`<line class="fig-grid" x1="${r2(f.sx(x))}" y1="${M.t}" x2="${r2(f.sx(x))}" y2="${M.t + PH}"/>`);
  for (const y of ys) parts.push(`<line class="fig-grid" x1="${M.l}" y1="${r2(f.sy(y))}" x2="${M.l + PW}" y2="${r2(f.sy(y))}"/>`);
  // Axes through the origin when it is in view, else along the frame edge.
  const ax = opts.xAtZero !== false && f.y0 <= 0 && f.y1 >= 0 ? f.sy(0) : M.t + PH;
  const ay = f.x0 <= 0 && f.x1 >= 0 ? f.sx(0) : M.l;
  parts.push(`<line class="fig-axis" x1="${M.l}" y1="${r2(ax)}" x2="${M.l + PW}" y2="${r2(ax)}"/>`);
  parts.push(`<line class="fig-axis" x1="${r2(ay)}" y1="${M.t}" x2="${r2(ay)}" y2="${M.t + PH}"/>`);
  for (const x of xs) {
    if (Math.abs(x) < 1e-12 && ay > M.l) continue;
    parts.push(`<text class="fig-tick" x="${r2(f.sx(x))}" y="${r2(Math.min(ax + 15, H - 4))}" text-anchor="middle">${opts.xpi ? piLabel(x) : fmt(x)}</text>`);
  }
  for (const y of ys) {
    if (Math.abs(y) < 1e-12 && ax < M.t + PH) continue;
    parts.push(`<text class="fig-tick" x="${r2(Math.max(ay - 5, 30))}" y="${r2(f.sy(y) + 4)}" text-anchor="end">${fmt(y)}</text>`);
  }
  if (Math.abs(ax - (M.t + PH)) > 1 && ay > M.l + 1) {
    parts.push(`<text class="fig-tick" x="${r2(ay - 5)}" y="${r2(ax + 14)}" text-anchor="end">0</text>`);
  }
  if (opts.xlabel) parts.push(`<text class="fig-label" x="${M.l + PW}" y="${H - 2}" text-anchor="end">${esc(plain(opts.xlabel))}</text>`);
  if (opts.ylabel) parts.push(`<text class="fig-label" x="${M.l + 4}" y="${M.t + 12}">${esc(plain(opts.ylabel))}</text>`);
  return parts.join("");
}

/** Path through sampled points, broken at gaps and at jumps (asymptotes, jump discontinuities).
 *  A jump is a step that is large on screen and much larger than both neighbouring steps;
 *  a steep but continuous curve has neighbouring steps of similar size, so it is not broken. */
function pathFrom(input: ([number, number] | null)[], f: Frame): string {
  const span = f.y1 - f.y0, limit = span * 3;
  // Drop isolated one-sample spikes (e.g. floating-point tan(pi/2) at a removable jump).
  const pts = input.map((p, i) => {
    const a = input[i - 1], b = input[i + 1];
    if (!p || !a || !b) return p;
    const da = Math.abs(p[1] - a[1]), db = Math.abs(p[1] - b[1]), ab = Math.abs(b[1] - a[1]);
    return da > span * 0.08 && db > span * 0.08 && ab < 0.25 * Math.min(da, db) ? null : p;
  });
  const ok = (p: [number, number] | null): p is [number, number] =>
    !!p && Number.isFinite(p[0]) && Number.isFinite(p[1]) && p[1] <= f.y1 + limit && p[1] >= f.y0 - limit;
  const dy = (i: number) => (i > 0 && i < pts.length && ok(pts[i]) && ok(pts[i - 1]) ? Math.abs(pts[i]![1] - pts[i - 1]![1]) : 0);
  let d = "", pen = false;
  for (let i = 0; i < pts.length; i++) {
    const p = pts[i];
    if (!ok(p)) { pen = false; continue; }
    if (pen) {
      const step = dy(i);
      const around = Math.max(dy(i - 1), dy(i + 1));
      if (step > span * 1.5 || (step > span * 0.08 && step > 8 * around)) pen = false;
    }
    d += `${pen ? "L" : "M"}${r2(f.sx(p[0]))},${r2(f.sy(p[1]))}`;
    pen = true;
  }
  return d;
}

/** Marching squares for F(x, y) = 0. */
function implicitPath(F: (x: number, y: number) => number, f: Frame): string {
  const nx = 180, ny = 120;
  const dx = (f.x1 - f.x0) / nx, dy = (f.y1 - f.y0) / ny;
  const v: number[][] = [];
  for (let j = 0; j <= ny; j++) {
    v.push([]);
    for (let i = 0; i <= nx; i++) v[j].push(F(f.x0 + i * dx, f.y0 + j * dy));
  }
  let d = "";
  const lerp = (a: number, b: number) => (Math.abs(a - b) < 1e-15 ? 0.5 : a / (a - b));
  for (let j = 0; j < ny; j++) {
    for (let i = 0; i < nx; i++) {
      const a = v[j][i], b = v[j][i + 1], c = v[j + 1][i + 1], e = v[j + 1][i];
      if (![a, b, c, e].every(Number.isFinite)) continue;
      const x = f.x0 + i * dx, y = f.y0 + j * dy;
      const pts: [number, number][] = [];
      if (a * b < 0 || (a === 0) !== (b === 0)) pts.push([x + lerp(a, b) * dx, y]);
      if (b * c < 0) pts.push([x + dx, y + lerp(b, c) * dy]);
      if (e * c < 0) pts.push([x + lerp(e, c) * dx, y + dy]);
      if (a * e < 0) pts.push([x, y + lerp(a, e) * dy]);
      // Ignore sign changes across poles (huge values), e.g. 1/x.
      const big = Math.max(Math.abs(a), Math.abs(b), Math.abs(c), Math.abs(e));
      if (big > 1e6) continue;
      for (let k = 0; k + 1 < pts.length; k += 2) {
        d += `M${r2(f.sx(pts[k][0]))},${r2(f.sy(pts[k][1]))}L${r2(f.sx(pts[k + 1][0]))},${r2(f.sy(pts[k + 1][1]))}`;
      }
    }
  }
  return d;
}

function wrap(body: string, title: string | null, kind: string): string {
  const label = esc(title ? plain(title) : kind);
  return `<svg class="fig-svg" viewBox="0 0 ${W} ${H}" role="img" aria-label="${label}" xmlns="http://www.w3.org/2000/svg">${body}</svg>`;
}

function expr2(src: string, vars: string[]) {
  try {
    return compile(src, vars);
  } catch (e) {
    throw new FigureError(`"${src}": ${e instanceof ExprError ? e.message : String(e)}`);
  }
}

// ---------------------------------------------------------------- plot

export function renderPlot(src: string): Figure {
  const spec = parseSpec(src);
  let title: string | null = null, xr: [number, number] = [-5, 5], yr: [number, number] | null = null;
  let tr: [number, number] = [0, 2 * Math.PI], equal = false, xpi = false;
  let xlabel: string | undefined, ylabel: string | undefined;
  for (const s of spec) {
    if (s.key === "title") title = s.value;
    else if (s.key === "x") xr = pair(s.value, "x");
    else if (s.key === "y") yr = pair(s.value, "y");
    else if (s.key === "t" || s.key === "theta") tr = pair(s.value, s.key);
    else if (s.key === "equal") equal = s.value === "true" || s.value === "yes";
    else if (s.key === "xticks") xpi = s.value === "pi";
    else if (s.key === "xlabel") xlabel = s.value;
    else if (s.key === "ylabel") ylabel = s.value;
  }
  const N = 720;
  type Curve = { pts: ([number, number] | null)[]; label: string | null; dashed?: boolean };
  const curves: Curve[] = [];
  const implicits: { F: (x: number, y: number) => number; label: string | null }[] = [];
  const shades: { f: (x: number) => number; g: (x: number) => number; a: number; b: number }[] = [];
  const points: { x: number; y: number; label: string | null }[] = [];
  const vlines: { x: number; label: string | null }[] = [];
  const hlines: { y: number; label: string | null }[] = [];
  const known = new Set(["title", "x", "y", "t", "theta", "equal", "xticks", "xlabel", "ylabel"]);

  for (const s of spec) {
    const sample = (fx: (t: number) => [number, number], [a, b]: [number, number]) => {
      const pts: [number, number][] = [];
      for (let i = 0; i <= N; i++) pts.push(fx(a + ((b - a) * i) / N));
      return pts;
    };
    switch (s.key) {
      case "f": {
        const fn = expr2(s.value, ["x"]);
        curves.push({ pts: sample((x) => [x, fn(x)], xr), label: s.label });
        break;
      }
      case "param": {
        const parts = splitTop(s.value);
        if (parts.length !== 2) throw new FigureError(`param needs "x(t), y(t)"`);
        const [fx, fy] = parts.map((p) => expr2(p.replace(/θ/g, "t"), ["t"]));
        curves.push({ pts: sample((t) => [fx(t), fy(t)], tr), label: s.label });
        break;
      }
      case "polar": {
        const fr = expr2(s.value.replace(/θ/g, "t").replace(/\btheta\b/g, "t"), ["t"]);
        curves.push({ pts: sample((t) => [fr(t) * Math.cos(t), fr(t) * Math.sin(t)], tr), label: s.label });
        break;
      }
      case "implicit": {
        const sides = s.value.split("=");
        if (sides.length > 2) throw new FigureError(`implicit: use at most one "="`);
        const L = expr2(sides[0], ["x", "y"]), R = sides[1] ? expr2(sides[1], ["x", "y"]) : () => 0;
        implicits.push({ F: (x, y) => L(x, y) - R(x, y), label: s.label });
        break;
      }
      case "shade": {
        const parts = splitTop(s.value);
        if (parts.length < 3 || parts.length > 4) throw new FigureError(`shade needs "f(x), a, b" or "f(x), a, b, g(x)"`);
        const fn = expr2(parts[0], ["x"]), g = parts[3] ? expr2(parts[3], ["x"]) : () => 0;
        const [a, b] = [num(parts[1]), num(parts[2])];
        shades.push({ f: fn, g, a, b });
        break;
      }
      case "point": {
        const parts = splitTop(s.value);
        if (parts.length !== 2) throw new FigureError(`point needs "x, y"`);
        points.push({ x: num(parts[0]), y: num(parts[1]), label: s.label });
        break;
      }
      case "vline": vlines.push({ x: num(s.value), label: s.label }); break;
      case "hline": hlines.push({ y: num(s.value), label: s.label }); break;
      default:
        if (!known.has(s.key)) throw new FigureError(`unknown key "${s.key}"`);
    }
  }
  if (!curves.length && !implicits.length && !points.length) throw new FigureError("nothing to draw: add f:, param:, polar:, implicit: or point:");

  // x range for parametric/polar-only plots comes from the curve unless given.
  const hasX = spec.some((s) => s.key === "x");
  const ptsAll = curves.flatMap((c) => c.pts).filter((p): p is [number, number] => !!p && Number.isFinite(p[0]) && Number.isFinite(p[1]));
  if (!hasX && !spec.some((s) => s.key === "f" || s.key === "shade")) {
    const xsv = [...ptsAll.map((p) => p[0]), ...points.map((p) => p.x)];
    if (xsv.length) {
      const [lo, hi] = [Math.min(...xsv), Math.max(...xsv)], pad = (hi - lo || 2) * 0.1;
      xr = [lo - pad, hi + pad];
    }
  }
  if (!yr) {
    const ys = [...ptsAll.filter((p) => p[0] >= xr[0] && p[0] <= xr[1]).map((p) => p[1]), ...points.map((p) => p.y)];
    if (ys.length) {
      ys.sort((a, b) => a - b);
      // Ignore the extreme 2% so asymptotes do not flatten the picture.
      const q = (k: number) => ys[Math.min(ys.length - 1, Math.max(0, Math.round(k * (ys.length - 1))))];
      let [lo, hi] = curves.length ? [q(0.02), q(0.98)] : [ys[0], ys[ys.length - 1]];
      lo = Math.min(lo, ...points.map((p) => p.y)); hi = Math.max(hi, ...points.map((p) => p.y));
      if (hi - lo < 1e-9) { lo -= 1; hi += 1; }
      const pad = (hi - lo) * 0.08;
      yr = [lo - pad, hi + pad];
    } else {
      const half = (xr[1] - xr[0]) * (PH / PW) / 2;
      yr = [-half, half];
    }
  }
  if (equal) {
    // Same scale on both axes (circles look round): grow the smaller span.
    const ux = (xr[1] - xr[0]) / PW, uy = (yr[1] - yr[0]) / PH;
    if (ux > uy) { const c = (yr[0] + yr[1]) / 2, h = (ux * PH) / 2; yr = [c - h, c + h]; }
    else { const c = (xr[0] + xr[1]) / 2, h = (uy * PW) / 2; xr = [c - h, c + h]; }
  }
  const fr = frame(xr[0], xr[1], yr[0], yr[1]);
  const clip = `fig-clip-${++clipSeq}`;
  const body: string[] = [
    `<defs><clipPath id="${clip}"><rect x="${M.l}" y="${M.t}" width="${PW}" height="${PH}"/></clipPath></defs>`,
    axes(fr, { xpi, xlabel, ylabel }),
    `<g clip-path="url(#${clip})">`,
  ];
  for (const sh of shades) {
    const top: string[] = [], bot: string[] = [];
    const n = 200;
    for (let i = 0; i <= n; i++) {
      const x = sh.a + ((sh.b - sh.a) * i) / n;
      top.push(`${r2(fr.sx(x))},${r2(fr.sy(sh.f(x)))}`);
      bot.unshift(`${r2(fr.sx(x))},${r2(fr.sy(sh.g(x)))}`);
    }
    body.push(`<polygon class="fig-shade" points="${[...top, ...bot].join(" ")}"/>`);
  }
  const leg: LegendItem[] = [];
  let si = 0;
  for (const c of curves) {
    const cls = `fig-curve fig-s${(si++ % 5) + 1}`;
    body.push(`<path class="${cls}" d="${pathFrom(c.pts, fr)}"/>`);
    if (c.label) leg.push({ cls, label: c.label, kind: "line" });
  }
  for (const im of implicits) {
    const cls = `fig-curve fig-s${(si++ % 5) + 1}`;
    body.push(`<path class="${cls}" d="${implicitPath(im.F, fr)}"/>`);
    if (im.label) leg.push({ cls, label: im.label, kind: "line" });
  }
  for (const v of vlines) {
    body.push(`<line class="fig-guide" x1="${r2(fr.sx(v.x))}" y1="${M.t}" x2="${r2(fr.sx(v.x))}" y2="${M.t + PH}"/>`);
    if (v.label) body.push(`<text class="fig-note" x="${r2(fr.sx(v.x) + 4)}" y="${M.t + 14}">${esc(plain(v.label))}</text>`);
  }
  for (const h of hlines) {
    body.push(`<line class="fig-guide" x1="${M.l}" y1="${r2(fr.sy(h.y))}" x2="${M.l + PW}" y2="${r2(fr.sy(h.y))}"/>`);
    if (h.label) body.push(`<text class="fig-note" x="${M.l + 6}" y="${r2(fr.sy(h.y) - 5)}">${esc(plain(h.label))}</text>`);
  }
  body.push("</g>");
  for (const p of points) {
    if (p.x < xr[0] || p.x > xr[1] || p.y < yr[0] || p.y > yr[1]) continue;
    body.push(`<circle class="fig-point" cx="${r2(fr.sx(p.x))}" cy="${r2(fr.sy(p.y))}" r="4"/>`);
    if (p.label) body.push(`<text class="fig-note" x="${r2(fr.sx(p.x) + 7)}" y="${r2(fr.sy(p.y) - 7)}">${esc(plain(p.label))}</text>`);
  }
  return { svg: wrap(body.join(""), title, "Graph"), title, legend: leg };
}

// ---------------------------------------------------------------- chart

export function renderChart(src: string): Figure {
  const spec = parseSpec(src);
  let type = "", title: string | null = null, labels: string[] = [];
  let xlabel: string | undefined, ylabel: string | undefined;
  const series: { values: number[]; name: string | null }[] = [];
  const points: [number, number][] = [];
  const fits: { f: (x: number) => number; label: string | null }[] = [];
  for (const s of spec) {
    switch (s.key) {
      case "type": type = s.value; break;
      case "title": title = s.value; break;
      case "labels": labels = splitTop(s.value); break;
      case "xlabel": xlabel = s.value; break;
      case "ylabel": ylabel = s.value; break;
      case "data": series.push({ values: splitTop(s.value).map(num), name: s.label }); break;
      case "points":
        for (const p of s.value.split(";")) {
          const xy = splitTop(p);
          if (xy.length !== 2) throw new FigureError(`points: write "x, y; x, y; …"`);
          points.push([num(xy[0]), num(xy[1])]);
        }
        break;
      case "fit": fits.push({ f: expr2(s.value, ["x"]), label: s.label }); break;
      default: throw new FigureError(`unknown key "${s.key}"`);
    }
  }
  const types = ["bar", "line", "histogram", "pie", "scatter"];
  if (!types.includes(type)) throw new FigureError(`type must be one of ${types.join(", ")}`);

  if (type === "scatter") {
    if (!points.length) throw new FigureError("scatter needs points:");
    const xs = points.map((p) => p[0]), ys = points.map((p) => p[1]);
    const px = (Math.max(...xs) - Math.min(...xs) || 2) * 0.08, py = (Math.max(...ys) - Math.min(...ys) || 2) * 0.1;
    const fr = frame(Math.min(...xs) - px, Math.max(...xs) + px, Math.min(...ys) - py, Math.max(...ys) + py);
    const axesSvg = axes(fr, { xlabel, ylabel });
    const body: string[] = [];
    const leg: LegendItem[] = [];
    fits.forEach((ft, i) => {
      const cls = `fig-curve fig-s${i + 2}`;
      body.push(`<line class="${cls}" x1="${r2(fr.sx(fr.x0))}" y1="${r2(fr.sy(ft.f(fr.x0)))}" x2="${r2(fr.sx(fr.x1))}" y2="${r2(fr.sy(ft.f(fr.x1)))}"/>`);
      if (ft.label) leg.push({ cls, label: ft.label, kind: "line" });
    });
    for (const [x, y] of points) body.push(`<circle class="fig-dot fig-s1" cx="${r2(fr.sx(x))}" cy="${r2(fr.sy(y))}" r="4"/>`);
    const clip = `fig-clip-${++clipSeq}`;
    return {
      svg: wrap(`<defs><clipPath id="${clip}"><rect x="${M.l}" y="${M.t}" width="${PW}" height="${PH}"/></clipPath></defs>${axesSvg}<g clip-path="url(#${clip})">${body.join("")}</g>`, title, "Scatter diagram"),
      title,
      legend: leg,
    };
  }

  if (!series.length) throw new FigureError("add at least one data: line");
  if (type === "pie") {
    const vals = series[0].values;
    if (labels.length !== vals.length) throw new FigureError(`labels (${labels.length}) and data (${vals.length}) differ in length`);
    if (vals.some((v) => v < 0)) throw new FigureError("pie values must be non-negative");
    const total = vals.reduce((a, b) => a + b, 0);
    const cx = W / 2, cy = H / 2, R = 160;
    let ang = -Math.PI / 2;
    const parts: string[] = [];
    vals.forEach((v, i) => {
      const a2 = ang + (v / total) * 2 * Math.PI;
      const large = a2 - ang > Math.PI ? 1 : 0;
      const [x1, y1, x2, y2] = [cx + R * Math.cos(ang), cy + R * Math.sin(ang), cx + R * Math.cos(a2), cy + R * Math.sin(a2)];
      parts.push(vals.length === 1
        ? `<circle class="fig-fill fig-s1" cx="${cx}" cy="${cy}" r="${R}"/>`
        : `<path class="fig-fill fig-bar fig-s${(i % 5) + 1}" d="M${cx},${cy}L${r2(x1)},${r2(y1)}A${R},${R} 0 ${large} 1 ${r2(x2)},${r2(y2)}Z"/>`);
      ang = a2;
    });
    const leg: LegendItem[] = labels.map((l, i) => ({
      cls: `fig-fill fig-s${(i % 5) + 1}`,
      label: `${l} (${fmt(Math.round((vals[i] / total) * 1000) / 10)}%)`,
      kind: "box",
    }));
    return { svg: wrap(parts.join(""), title, "Pie chart"), title, legend: leg };
  }

  const n = type === "histogram" ? labels.length - 1 : labels.length;
  if (type === "histogram" && labels.length < 2) throw new FigureError("histogram labels are the class boundaries, e.g. 0, 10, 20, 30");
  for (const s of series) {
    if (s.values.length !== n) {
      throw new FigureError(type === "histogram"
        ? `histogram needs ${n} frequencies for ${labels.length} boundaries, got ${s.values.length}`
        : `labels (${labels.length}) and data (${s.values.length}) differ in length`);
    }
  }
  const all = series.flatMap((s) => s.values);
  const lo = Math.min(0, ...all), hiRaw = Math.max(0, ...all);
  const step = niceStep(hiRaw - lo || 1, 6);
  const hi = Math.ceil(hiRaw / step) * step || step;
  const fr = frame(0, n, lo, hi);
  const body: string[] = [];
  // Horizontal grid and y ticks.
  for (const y of ticks(lo, hi, step)) {
    body.push(`<line class="fig-grid" x1="${M.l}" y1="${r2(fr.sy(y))}" x2="${M.l + PW}" y2="${r2(fr.sy(y))}"/>`);
    body.push(`<text class="fig-tick" x="${M.l - 6}" y="${r2(fr.sy(y) + 4)}" text-anchor="end">${fmt(y)}</text>`);
  }
  body.push(`<line class="fig-axis" x1="${M.l}" y1="${r2(fr.sy(0))}" x2="${M.l + PW}" y2="${r2(fr.sy(0))}"/>`);
  body.push(`<line class="fig-axis" x1="${M.l}" y1="${M.t}" x2="${M.l}" y2="${M.t + PH}"/>`);
  const leg: LegendItem[] = [];
  if (type === "histogram") {
    series[0].values.forEach((v, i) => {
      body.push(`<rect class="fig-fill fig-bar fig-s1" x="${r2(fr.sx(i))}" y="${r2(fr.sy(Math.max(v, 0)))}" width="${r2(fr.sx(i + 1) - fr.sx(i))}" height="${r2(Math.abs(fr.sy(v) - fr.sy(0)))}"/>`);
    });
    labels.forEach((l, i) => body.push(`<text class="fig-tick" x="${r2(fr.sx(i))}" y="${M.t + PH + 16}" text-anchor="middle">${esc(plain(l))}</text>`));
  } else {
    const k = series.length;
    labels.forEach((l, i) => body.push(`<text class="fig-tick" x="${r2(fr.sx(i + 0.5))}" y="${M.t + PH + 16}" text-anchor="middle">${esc(plain(l))}</text>`));
    series.forEach((s, j) => {
      const cls = `fig-s${(j % 5) + 1}`;
      if (type === "bar") {
        const bw = 0.7 / k;
        s.values.forEach((v, i) => {
          const x = i + 0.15 + j * bw;
          body.push(`<rect class="fig-fill fig-bar ${cls}" x="${r2(fr.sx(x))}" y="${r2(fr.sy(Math.max(v, 0)))}" width="${r2(fr.sx(x + bw) - fr.sx(x) - 1)}" height="${r2(Math.abs(fr.sy(v) - fr.sy(0)))}"/>`);
        });
      } else {
        const pts = s.values.map((v, i) => `${r2(fr.sx(i + 0.5))},${r2(fr.sy(v))}`);
        body.push(`<polyline class="fig-curve ${cls}" points="${pts.join(" ")}"/>`);
        s.values.forEach((v, i) => body.push(`<circle class="fig-dot ${cls}" cx="${r2(fr.sx(i + 0.5))}" cy="${r2(fr.sy(v))}" r="3.5"/>`));
      }
      if (s.name) leg.push({ cls: type === "bar" ? `fig-fill ${cls}` : `fig-curve ${cls}`, label: s.name, kind: type === "bar" ? "box" : "line" });
    });
  }
  if (xlabel) body.push(`<text class="fig-label" x="${M.l + PW}" y="${H - 2}" text-anchor="end">${esc(plain(xlabel))}</text>`);
  if (ylabel) body.push(`<text class="fig-label" x="${M.l + 4}" y="${M.t + 12}">${esc(plain(ylabel))}</text>`);
  return { svg: wrap(body.join(""), title, "Chart"), title, legend: leg };
}
