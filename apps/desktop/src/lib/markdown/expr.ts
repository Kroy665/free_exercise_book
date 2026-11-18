// A small, safe maths expression compiler for graphs (no eval; the CSP forbids it anyway).
//
//   compile("2x^2 - 3sin(x) + e^(-x/2)", ["x"])  →  (x) => number
//
// Grammar (usual precedence; ^ is right-associative and binds tighter than unary minus,
// so -x^2 = -(x^2)). Implicit multiplication: 2x, 3(x+1), (x+1)(x-1), 2pi, x y.
//   expr   := term (('+' | '-') term)*
//   term   := unary (('*' | '/' | implicit) unary)*
//   unary  := ('-' | '+') unary | power
//   power  := atom ('^' unary)?
//   atom   := number | name | name '(' args ')' | '(' expr ')' | '|' expr '|'
// Names: the given variables, constants pi, e, and the functions in FUNCS.
// log and ln are both the natural logarithm (Indian university convention); use log10.

type Fn = (env: number[]) => number;

const FUNCS: Record<string, (...a: number[]) => number> = {
  sin: Math.sin, cos: Math.cos, tan: Math.tan,
  sec: (x) => 1 / Math.cos(x), cosec: (x) => 1 / Math.sin(x), csc: (x) => 1 / Math.sin(x),
  cot: (x) => 1 / Math.tan(x),
  asin: Math.asin, acos: Math.acos, atan: Math.atan, atan2: Math.atan2,
  sinh: Math.sinh, cosh: Math.cosh, tanh: Math.tanh,
  asinh: Math.asinh, acosh: Math.acosh, atanh: Math.atanh,
  exp: Math.exp, ln: Math.log, log: Math.log, log10: Math.log10, log2: Math.log2,
  sqrt: Math.sqrt, cbrt: Math.cbrt, abs: Math.abs, sign: Math.sign,
  floor: Math.floor, ceil: Math.ceil, round: Math.round,
  min: Math.min, max: Math.max,
};
const CONSTS: Record<string, number> = { pi: Math.PI, e: Math.E };

export class ExprError extends Error {}

type Tok = { k: "num"; v: number } | { k: "name"; v: string } | { k: "op"; v: string };

function lex(src: string): Tok[] {
  const out: Tok[] = [];
  const s = src.replace(/π/g, "pi").replace(/[−–]/g, "-").replace(/[×·]/g, "*").replace(/÷/g, "/");
  let i = 0;
  while (i < s.length) {
    const c = s[i];
    if (/\s/.test(c)) { i++; continue; }
    const num = /^(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?/.exec(s.slice(i));
    if (num) { out.push({ k: "num", v: parseFloat(num[0]) }); i += num[0].length; continue; }
    const name = /^[a-zA-Z][a-zA-Z0-9]*/.exec(s.slice(i));
    if (name) { out.push(...splitName(name[0])); i += name[0].length; continue; }
    if ("+-*/^(),|".includes(c)) { out.push({ k: "op", v: c }); i++; continue; }
    throw new ExprError(`unexpected "${c}"`);
  }
  return out;
}

// Known names stay whole ("sin", "pi", "log10"); unknown runs split into letters so
// "xy" means x*y. Digits stay attached to a preceding known name only (log10, log2).
let VARS: string[] = [];
function splitName(n: string): Tok[] {
  if (n in FUNCS || n in CONSTS || VARS.includes(n)) return [{ k: "name", v: n }];
  // Greedy: longest known prefix first.
  for (let j = n.length - 1; j > 0; j--) {
    const head = n.slice(0, j);
    if (head in FUNCS || head in CONSTS || VARS.includes(head)) return [{ k: "name", v: head }, ...splitName(n.slice(j))];
  }
  if (n.length === 1) return [{ k: "name", v: n }];
  if (/^[a-zA-Z]\d+$/.test(n)) return [{ k: "name", v: n[0] }, { k: "num", v: Number(n.slice(1)) }];
  return [{ k: "name", v: n[0] }, ...splitName(n.slice(1))];
}

export function compile(src: string, vars: string[]): (...args: number[]) => number {
  VARS = vars;
  const t = lex(src);
  let p = 0;
  const peek = () => t[p];
  const isOp = (v: string) => t[p]?.k === "op" && t[p].v === v;
  const expect = (v: string) => {
    if (!isOp(v)) throw new ExprError(`expected "${v}"`);
    p++;
  };

  function expr(): Fn {
    let a = term();
    while (isOp("+") || isOp("-")) {
      const op = t[p++].v, l = a, r = term();
      a = op === "+" ? (e) => l(e) + r(e) : (e) => l(e) - r(e);
    }
    return a;
  }
  function startsAtom(): boolean {
    const k = peek();
    return !!k && (k.k === "num" || k.k === "name" || (k.k === "op" && k.v === "("));
  }
  function term(): Fn {
    let a = unary();
    for (;;) {
      if (isOp("*") || isOp("/")) {
        const op = t[p++].v, l = a, r = unary();
        a = op === "*" ? (e) => l(e) * r(e) : (e) => l(e) / r(e);
      } else if (startsAtom()) {
        const l = a, r = power();
        a = (e) => l(e) * r(e);
      } else return a;
    }
  }
  function unary(): Fn {
    if (isOp("-")) { p++; const a = unary(); return (e) => -a(e); }
    if (isOp("+")) { p++; return unary(); }
    return power();
  }
  function power(): Fn {
    const b = atom();
    if (isOp("^")) {
      p++;
      const x = unary();
      return (e) => Math.pow(b(e), x(e));
    }
    return b;
  }
  function atom(): Fn {
    const k = t[p++];
    if (!k) throw new ExprError("unexpected end");
    if (k.k === "num") { const v = k.v; return () => v; }
    if (k.k === "op" && k.v === "(") { const a = expr(); expect(")"); return a; }
    if (k.k === "op" && k.v === "|") { const a = expr(); expect("|"); return (e) => Math.abs(a(e)); }
    if (k.k === "name") {
      const vi = vars.indexOf(k.v);
      if (vi >= 0) return (e) => e[vi];
      if (k.v in CONSTS) { const v = CONSTS[k.v]; return () => v; }
      if (k.v in FUNCS) {
        const f = FUNCS[k.v];
        const args: Fn[] = [];
        if (isOp("(")) {
          p++;
          args.push(expr());
          while (isOp(",")) { p++; args.push(expr()); }
          expect(")");
        } else if (isOp("^")) {
          // sin^2(x) = (sin x)^2
          p++;
          const pw = unary();
          const a = power();
          return (e) => Math.pow(f(a(e)), pw(e));
        } else {
          args.push(power()); // sin x, sin 2x is sin(2)*x: write sin(2x)
        }
        return (e) => f(...args.map((a) => a(e)));
      }
      throw new ExprError(`unknown name "${k.v}"`);
    }
    throw new ExprError(`unexpected "${k.v}"`);
  }

  const f = expr();
  if (p < t.length) throw new ExprError(`unexpected "${(t[p] as Tok).v}"`);
  return (...args: number[]) => f(args);
}

/** A constant expression such as "2pi" or "-3/2". */
export function num(src: string): number {
  const v = compile(src, [])();
  if (!Number.isFinite(v)) throw new ExprError(`"${src}" is not a finite number`);
  return v;
}
