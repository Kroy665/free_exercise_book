// App-wide settings + i18n. Settings live in user.db; this is the reactive mirror.
import { api, type Settings } from "$lib/api";
import en from "$lib/i18n/en.json";
import bn from "$lib/i18n/bn.json";

const dicts: Record<string, Record<string, string>> = { en, bn };

export const settings = $state<Settings & { loaded: boolean }>({
  lang: "en",
  theme: "system",
  font_size: "16",
  digits: "native",
  loaded: false,
});

const darkQuery = typeof window !== "undefined" ? window.matchMedia("(prefers-color-scheme: dark)") : null;

function apply() {
  const root = document.documentElement;
  root.lang = settings.lang;
  const dark = settings.theme === "dark" || (settings.theme === "system" && !!darkQuery?.matches);
  root.dataset.theme = dark ? "dark" : "light";
  root.style.setProperty("--font-size", `${settings.font_size}px`);
}

darkQuery?.addEventListener("change", apply);

export async function loadSettings() {
  try {
    Object.assign(settings, await api.settingsGet());
  } catch {
    // Running outside Tauri (plain browser): keep defaults.
  }
  settings.loaded = true;
  apply();
}

export async function setSetting(key: keyof Settings, value: string) {
  settings[key] = value;
  apply();
  await api.settingsSet(key, value);
}

export function toggleLang() {
  return setSetting("lang", settings.lang === "bn" ? "en" : "bn");
}

const BN_DIGITS = "০১২৩৪৫৬৭৮৯";

/** Localize ASCII digits in a string (Bengali digits unless the user prefers 0-9). */
export function digits(s: string | number): string {
  const str = String(s);
  if (settings.lang !== "bn" || settings.digits === "latin") return str;
  return str.replace(/[0-9]/g, (d) => BN_DIGITS[Number(d)]);
}

/** Translate a UI string key, with {placeholders}. Numbers are digit-localized. */
export function t(key: string, vars: Record<string, string | number> = {}): string {
  const s = dicts[settings.lang]?.[key] ?? en[key as keyof typeof en] ?? key;
  return s.replace(/\{(\w+)\}/g, (_, k) => (k in vars ? digits(vars[k]) : `{${k}}`));
}

/** Option labels: A B C D in English, ক খ গ ঘ in Bengali (UI_GUIDELINES §4). */
export function optionLabel(i: number, lang = settings.lang): string {
  return (lang === "bn" ? ["ক", "খ", "গ", "ঘ"] : ["A", "B", "C", "D"])[i] ?? String(i + 1);
}
