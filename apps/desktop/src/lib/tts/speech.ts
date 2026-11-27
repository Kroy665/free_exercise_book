// Turn Markdown with LaTeX into plain English a speech model can read aloud.
// "$\frac{a}{b}$" -> "a over b", "$x^2$" -> "x squared", "$\sqrt{x}$" -> "the square root of x".

const SYMBOLS: Record<string, string> = {
  alpha: "alpha", beta: "beta", gamma: "gamma", delta: "delta", epsilon: "epsilon", varepsilon: "epsilon",
  zeta: "zeta", eta: "eta", theta: "theta", vartheta: "theta", iota: "iota", kappa: "kappa", lambda: "lambda",
  mu: "mu", nu: "nu", xi: "xi", pi: "pi", rho: "rho", sigma: "sigma", tau: "tau", phi: "phi", varphi: "phi",
  chi: "chi", psi: "psi", omega: "omega", Gamma: "capital gamma", Delta: "capital delta", Theta: "capital theta",
  Lambda: "capital lambda", Sigma: "capital sigma", Phi: "capital phi", Psi: "capital psi", Omega: "capital omega",
  infty: "infinity", cdot: "times", times: "times", div: "divided by", pm: "plus or minus", mp: "minus or plus",
  le: "is less than or equal to", leq: "is less than or equal to", ge: "is greater than or equal to",
  geq: "is greater than or equal to", ne: "is not equal to", neq: "is not equal to", approx: "is approximately",
  equiv: "is equivalent to", sim: "is similar to", cong: "is congruent to", to: "tends to", rightarrow: "tends to",
  mapsto: "maps to", implies: "implies", Rightarrow: "implies", iff: "if and only if", Leftrightarrow: "if and only if",
  in: "in", notin: "not in", subset: "subset of", subseteq: "subset of", cup: "union", cap: "intersection",
  emptyset: "the empty set", varnothing: "the empty set", forall: "for all", exists: "there exists",
  partial: "partial", nabla: "del", sum: "the sum", prod: "the product", int: "the integral of",
  iint: "the double integral of", oint: "the contour integral of", lim: "the limit", sin: "sine", cos: "cos",
  tan: "tan", cot: "cot", sec: "sec", csc: "cosec", cosec: "cosec", log: "log", ln: "log", exp: "exp",
  sinh: "sinh", cosh: "cosh", tanh: "tanh", arcsin: "arc sine", arccos: "arc cos", arctan: "arc tan",
  det: "determinant", max: "max", min: "min", sup: "supremum", inf: "infimum", gcd: "g c d", deg: "degree",
  dots: "and so on", ldots: "and so on", cdots: "and so on", angle: "angle", perp: "perpendicular to",
  parallel: "parallel to", circ: "degrees", prime: "prime", R: "R", N: "N", Z: "Z", Q: "Q", C: "C",
};

const POWER_WORDS: Record<string, string> = { "2": "squared", "3": "cubed" };

/** Read one {group} starting at s[i] === "{"; returns [content, next index]. */
function group(s: string, i: number): [string, number] {
  if (s[i] !== "{") {
    // A single token: \command or one character.
    if (s[i] === "\\") {
      const m = /^\\[A-Za-z]+/.exec(s.slice(i));
      if (m) return [m[0], i + m[0].length];
    }
    return [s[i] ?? "", i + 1];
  }
  let depth = 0;
  for (let j = i; j < s.length; j++) {
    if (s[j] === "{") depth++;
    else if (s[j] === "}" && --depth === 0) return [s.slice(i + 1, j), j + 1];
  }
  return [s.slice(i + 1), s.length];
}

function short(spoken: string): boolean {
  return spoken.trim().split(/\s+/).length <= 1;
}

/** LaTeX maths -> words. */
export function speakTex(src: string): string {
  // Intervals first, so closed and open ends are not lost: [a,b], (a,b], [a,b).
  src = src
    .replace(/\[\s*([^\[\](),]+?)\s*,\s*([^\[\](),]+?)\s*\]/g, " the closed interval from {$1} to {$2} ")
    .replace(/\(\s*([^\[\](),]+?)\s*,\s*([^\[\](),]+?)\s*\]/g, " the interval from {$1}, open, to {$2}, closed ")
    .replace(/\[\s*([^\[\](),]+?)\s*,\s*([^\[\](),]+?)\s*\)/g, " the interval from {$1}, closed, to {$2}, open ");
  let s = src.replace(/\\(left|right|big|Big|bigg|Bigg)\b/g, "").replace(/\\[,;:! ]/g, " ").replace(/&/g, " ");
  s = s.replace(/\\\\/g, ", ");
  let out = "";
  let i = 0;
  while (i < s.length) {
    const c = s[i];
    if (c === "\\") {
      const m = /^\\([A-Za-z]+)/.exec(s.slice(i));
      if (!m) { i += 2; continue; }
      const name = m[1];
      i += m[0].length;
      while (s[i] === " ") i++;
      if (name === "frac" || name === "dfrac" || name === "tfrac") {
        const [a, j] = group(s, i);
        const [b, k] = group(s, j);
        i = k;
        const A = speakTex(a), B = speakTex(b);
        out += short(A) && short(B) ? ` ${A} over ${B} ` : ` the fraction ${A}, over ${B}, `;
      } else if (name === "sqrt") {
        let root = "";
        if (s[i] === "[") {
          const end = s.indexOf("]", i);
          root = s.slice(i + 1, end);
          i = end + 1;
        }
        const [a, j] = group(s, i);
        i = j;
        out += root === "3" ? ` the cube root of ${speakTex(a)} ` : root ? ` the ${speakTex(root)}th root of ${speakTex(a)} ` : ` the square root of ${speakTex(a)} `;
      } else if (["text", "mathrm", "textbf", "mathbf", "operatorname", "mathit", "boldsymbol"].includes(name)) {
        const [a, j] = group(s, i);
        i = j;
        out += ` ${name === "text" ? a : speakTex(a)} `;
      } else if (name === "mathbb") {
        const [a, j] = group(s, i);
        i = j;
        out += ` ${a} `;
      } else if (["vec", "overrightarrow"].includes(name)) {
        const [a, j] = group(s, i);
        i = j;
        out += ` vector ${speakTex(a)} `;
      } else if (["bar", "overline"].includes(name)) {
        const [a, j] = group(s, i);
        i = j;
        out += ` ${speakTex(a)} bar `;
      } else if (name === "hat") {
        const [a, j] = group(s, i);
        i = j;
        out += ` ${speakTex(a)} hat `;
      } else if (name === "binom") {
        const [a, j] = group(s, i);
        const [b, k] = group(s, j);
        i = k;
        out += ` ${speakTex(a)} choose ${speakTex(b)} `;
      } else if (name === "lvert" || name === "rvert" || name === "vert" || name === "mid") {
        out += name === "mid" ? " such that " : " modulus ";
      } else if (name === "begin" || name === "end") {
        const [, j] = group(s, i);
        i = j;
        out += name === "begin" ? " the matrix " : " ";
      } else if (["int", "iint", "oint", "sum", "prod", "lim", "limsup", "liminf", "max", "min", "sup", "inf", "bigcup", "bigcap"].includes(name)) {
        // Limits of a big operator: \int_a^b, \sum_{i=1}^{n}, \lim_{x \to a}.
        let lo = "", hi = "";
        for (let k = 0; k < 2; k++) {
          while (s[i] === " ") i++;
          if (s[i] === "_") { const [a, j] = group(s, i + 1); lo = speakTex(a); i = j; }
          else if (s[i] === "^") { const [a, j] = group(s, i + 1); hi = speakTex(a); i = j; }
        }
        const word = { int: "the integral", iint: "the double integral", oint: "the contour integral", sum: "the sum", prod: "the product", lim: "the limit", limsup: "the limit superior", liminf: "the limit inferior", max: "the maximum", min: "the minimum", sup: "the supremum", inf: "the infimum", bigcup: "the union", bigcap: "the intersection" }[name];
        if (name.startsWith("lim") && lo) out += ` ${word} as ${lo}, of `;
        else if (lo && hi) out += ` ${word} from ${lo} to ${hi}, of `;
        else if (lo) out += ` ${word} over ${lo}, of `;
        else out += ` ${word} of `;
      } else {
        out += ` ${SYMBOLS[name] ?? name} `;
      }
    } else if (c === "^") {
      const [a, j] = group(s, i + 1);
      i = j;
      const t = a.trim();
      if (POWER_WORDS[t]) out += ` ${POWER_WORDS[t]} `;
      else if (t === "{-1}" || t === "-1") out += " inverse ";
      else if (t === "\\prime" || t === "'") out += " prime ";
      else if (t === "\\circ") out += " degrees ";
      else out += ` to the power ${speakTex(a)}, `;
    } else if (c === "_") {
      const [a, j] = group(s, i + 1);
      i = j;
      out += ` sub ${speakTex(a)} `;
    } else if (c === "{" || c === "}") {
      i++;
    } else if (c === "=") { out += " equals "; i++; }
    else if (c === "+") { out += " plus "; i++; }
    else if (c === "-") { out += " minus "; i++; }
    else if (c === "<") { out += " is less than "; i++; }
    else if (c === ">") { out += " is greater than "; i++; }
    else if (c === "|") { out += " modulus "; i++; }
    else if (c === "'") { out += " prime "; i++; }
    else if (c === "!") { out += " factorial "; i++; }
    else if (c === "/") { out += " over "; i++; }
    else if (c === "(" || c === "[") { out += " ("; i++; }
    else if (c === ")" || c === "]") { out += ") "; i++; }
    else { out += c; i++; }
  }
  return out.replace(/\s+/g, " ").trim();
}

/** Markdown with $maths$ -> text for speech. */
export function toSpeech(md: string): string {
  let s = md
    .replace(/```[\s\S]*?```/g, " ") // graphs, charts, code
    .replace(/^:::.*$/gm, "")
    .replace(/\$\$([\s\S]+?)\$\$/g, (_, m) => ` ${speakTex(m)}. `)
    .replace(/\$([^$\n]+?)\$/g, (_, m) => ` ${speakTex(m)} `)
    .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1") // links -> their text
    .replace(/^\s*\|?[-:| ]+\|[-:| ]*$/gm, "") // table rules
    .replace(/\|/g, ", ")
    .replace(/^#+\s*/gm, "")
    .replace(/\{#[a-z0-9-]+\}/g, "")
    .replace(/[*_`>]/g, "")
    .replace(/^\s*[-•]\s+/gm, "")
    .replace(/›/g, ", ");
  s = s.replace(/[ \t]+/g, " ").replace(/\n{2,}/g, "\n").trim();
  return s;
}

/** Split into chunks of whole sentences, each short enough for one Kokoro call. */
export function chunks(text: string, max = 300): string[] {
  const parts = text.split(/(?<=[.!?:;])\s+|\n+/).map((p) => p.trim()).filter(Boolean);
  const out: string[] = [];
  let cur = "";
  for (const p of parts) {
    if (cur && (cur + " " + p).length > max) {
      out.push(cur);
      cur = "";
    }
    if (p.length > max) {
      // A very long sentence: break at commas.
      for (const q of p.split(/(?<=,)\s+/)) {
        if (cur && (cur + " " + q).length > max) { out.push(cur); cur = ""; }
        cur = cur ? `${cur} ${q}` : q;
      }
    } else {
      cur = cur ? `${cur} ${p}` : p;
    }
  }
  if (cur) out.push(cur);
  return out;
}
