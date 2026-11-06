// App-wide settings + UI strings. Settings live in user.db; this is the reactive mirror.
//
// Language model: the **UI is always English**. `settings.lang` is the *content* language
// (notes, questions, topic titles). Strings inside content use `tc()`.
import { api, type Settings } from "$lib/api";
import en from "$lib/i18n/en.json";
import { contentStrings } from "$lib/i18n/content";

export const settings = $state<Settings & { loaded: boolean }>({
  lang: "en",
  theme: "system",
  font_size: "16",
  loaded: false,
});

const darkQuery = typeof window !== "undefined" ? window.matchMedia("(prefers-color-scheme: dark)") : null;

function apply() {
  const root = document.documentElement;
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

/** Switch the content language between English and Bengali. */
export function toggleLang() {
  return setSetting("lang", settings.lang === "bn" ? "en" : "bn");
}

function fill(s: string, vars: Record<string, string | number>) {
  return s.replace(/\{(\w+)\}/g, (_, k) => (k in vars ? String(vars[k]) : `{${k}}`));
}

/** UI string (always English). */
export function t(key: string, vars: Record<string, string | number> = {}): string {
  return fill((en as Record<string, string>)[key] ?? key, vars);
}

/** String that appears inside study content, in the content's language. */
export function tc(key: string, lang: string): string {
  return contentStrings[lang]?.[key] ?? contentStrings.en[key] ?? key;
}

/** Option labels follow the question's language: A B C D, or ক খ গ ঘ for Bengali. */
export function optionLabel(i: number, lang: string): string {
  return (lang === "bn" ? ["ক", "খ", "গ", "ঘ"] : ["A", "B", "C", "D"])[i] ?? String(i + 1);
}
