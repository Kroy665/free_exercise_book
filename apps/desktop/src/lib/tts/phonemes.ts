// Text -> phonemes for Kokoro, using espeak-ng (the `phonemizer` package, WebAssembly).
// Normalisation and post-processing follow kokoro-js (Apache-2.0, https://github.com/hexgrad/kokoro),
// so the model hears the phoneme strings it was trained on.

// WebKit (the macOS app's webview) cannot iterate a ReadableStream with `for await`,
// which phonemizer uses while unpacking its data. Add the missing iterator.
const RS = globalThis.ReadableStream?.prototype as unknown as Record<symbol, unknown> | undefined;
if (RS && !RS[Symbol.asyncIterator]) {
  RS[Symbol.asyncIterator] = async function* (this: ReadableStream) {
    const reader = this.getReader();
    try {
      for (;;) {
        const { done, value } = await reader.read();
        if (done) return;
        yield value;
      }
    } finally {
      reader.releaseLock();
    }
  };
}

let espeak: Promise<typeof import("phonemizer")> | null = null;

function splitNum(n: string): string {
  if (n.includes(".")) return n;
  if (n.includes(":")) {
    const [h, m] = n.split(":").map(Number);
    return m === 0 ? `${h} o'clock` : m < 10 ? `${h} oh ${m}` : `${h} ${m}`;
  }
  const year = parseInt(n.slice(0, 4), 10);
  if (year < 1100 || year % 1000 < 10) return n;
  const left = n.slice(0, 2), right = parseInt(n.slice(2, 4), 10), s = n.endsWith("s") ? "s" : "";
  if (year % 1000 >= 100 && year % 1000 <= 999) {
    if (right === 0) return `${left} hundred${s}`;
    if (right < 10) return `${left} oh ${right}${s}`;
  }
  return `${left} ${right}${s}`;
}

function pointNum(n: string): string {
  const [a, b] = n.split(".");
  return `${a} point ${b.split("").join(" ")}`;
}

function normalize(text: string): string {
  return text
    .replace(/[‘’]/g, "'")
    .replace(/[“”«»]/g, '"')
    .replace(/[^\S \n]/g, " ")
    .replace(/  +/g, " ")
    .replace(/\bD[Rr]\.(?= [A-Z])/g, "Doctor")
    .replace(/\b(?:Mr\.|MR\.(?= [A-Z]))/g, "Mister")
    .replace(/\b(?:Ms\.|MS\.(?= [A-Z]))/g, "Miss")
    .replace(/\b(?:Mrs\.|MRS\.(?= [A-Z]))/g, "Mrs")
    .replace(/\betc\.(?! [A-Z])/gi, "etc")
    .replace(/\d*\.\d+|\b\d{4}s?\b|(?<!:)\b(?:[1-9]|1[0-2]):[0-5]\d\b(?!:)/g, splitNum)
    .replace(/(?<=\d),(?=\d)/g, "")
    .replace(/\d*\.\d+/g, pointNum)
    .replace(/(?<=\d)-(?=\d)/g, " to ")
    .replace(/(?<=\d)S/g, " S")
    .replace(/(?<=[BCDFGHJ-NP-TV-Z])'?s\b/g, "'S")
    .replace(/(?<=X')S\b/g, "s")
    .replace(/(?:[A-Za-z]\.){2,} [a-z]/g, (m) => m.replace(/\./g, "-"))
    .replace(/(?<=[A-Z])\.(?=[A-Z])/gi, "-")
    .trim();
}

const PUNCT = /(\s*[;:,.!?¡¿—…"«»“”(){}[\]]+\s*)+/g;

/** Phonemes for one chunk of English text. `british` for the en-gb voices. */
export async function phonemize(text: string, british = false): Promise<string> {
  espeak ??= import("phonemizer");
  const { phonemize: ph } = await espeak;
  const s = normalize(text);
  const parts: { punct: boolean; text: string }[] = [];
  let last = 0;
  for (const m of s.matchAll(PUNCT)) {
    if (last < m.index!) parts.push({ punct: false, text: s.slice(last, m.index) });
    if (m[0].length) parts.push({ punct: true, text: m[0] });
    last = m.index! + m[0].length;
  }
  if (last < s.length) parts.push({ punct: false, text: s.slice(last) });
  const lang = british ? "en" : "en-us";
  const out = (await Promise.all(parts.map(async (p) => (p.punct ? p.text : (await ph(p.text, lang)).join(" "))))).join("");
  let r = out
    .replace(/ʲ/g, "j")
    .replace(/r/g, "ɹ")
    .replace(/x/g, "k")
    .replace(/ɬ/g, "l")
    .replace(/(?<=[a-zɹː])(?=hˈʌndɹɪd)/g, " ")
    .replace(/ z(?=[;:,.!?¡¿—…"«»“” ]|$)/g, "z");
  if (!british) r = r.replace(/(?<=nˈaɪn)ti(?!ː)/g, "di");
  return r.trim();
}
