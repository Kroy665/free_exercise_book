// Small display helpers (UI is English; numbers use the Indian locale).

/** 1:05:09 or 5:09 */
export function clock(ms: number): string {
  const total = Math.max(0, Math.ceil(ms / 1000));
  const h = Math.floor(total / 3600);
  const m = Math.floor((total % 3600) / 60);
  const s = total % 60;
  const mm = h ? String(m).padStart(2, "0") : String(m);
  return `${h ? `${h}:` : ""}${mm}:${String(s).padStart(2, "0")}`;
}

/** "1 h 5 min" / "12 min" / "40 s" */
export function duration(ms: number): string {
  const s = Math.round(ms / 1000);
  if (s < 60) return `${s} s`;
  const m = Math.round(s / 60);
  if (m < 60) return `${m} min`;
  return `${Math.floor(m / 60)} h ${m % 60} min`;
}

/** Up to 2 decimals, no trailing zeros: 4.67, 24, -0.5 */
export function num(x: number): string {
  return new Intl.NumberFormat("en-IN", { maximumFractionDigits: 2 }).format(x);
}

export function date(secs: number): string {
  return new Intl.DateTimeFormat("en-IN", { dateStyle: "medium", timeStyle: "short" }).format(secs * 1000);
}

/** Negative marking as a readable fraction of the marks per question. */
export function negativeLabel(negative: number, marks: number): string {
  if (negative <= 0) return "No negative marking";
  const r = negative / marks;
  const fractions: [number, string][] = [[1 / 4, "¼"], [1 / 3, "⅓"], [1 / 2, "½"], [1, "full"]];
  const f = fractions.find(([v]) => Math.abs(v - r) < 0.01);
  return f ? `−${num(negative)} per wrong answer (${f[1]} of ${num(marks)})` : `−${num(negative)} per wrong answer`;
}
