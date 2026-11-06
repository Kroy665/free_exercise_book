// Typed wrappers over Tauri commands. Components never call invoke() directly.
// Mirrors crates/core/src/model.rs. TODO: generate with tauri-specta (docs/APP_STRUCTURE.md §5).
import { invoke } from "@tauri-apps/api/core";

export type Lang = "en" | "bn" | "hi";
export type QuestionKind = "single" | "statements" | "match" | "assertion-reason" | "chronology";
export type ContentStatus = "ai-generated" | "reviewed" | "verified";

export interface QuestionView {
  id: string;
  topic_id: string;
  kind: QuestionKind;
  difficulty: 1 | 2 | 3;
  status: ContentStatus;
  lang: string;
  refs: string[];
  stem: string | null;
  question: string | null;
  statements: string[] | null;
  left: string[] | null;
  right: string[] | null;
  items: string[] | null;
  assertion: string | null;
  reason: string | null;
  options: string[] | null;
  answer: number;
  explanation: string;
  as_of: string | null;
  source: string | null;
}

export interface TopicSummary {
  id: string;
  title: string;
  summary: string | null;
  status: ContentStatus;
  estimated_minutes: number | null;
  question_count: number;
  attempted: number;
  correct: number;
}

export interface LibraryUnit {
  id: string;
  title: string;
  topics: TopicSummary[];
}

export interface LibrarySubject {
  id: string;
  title: string;
  units: LibraryUnit[];
}

export interface NoteSection {
  anchor: string;
  heading: string;
  body_md: string;
}

export interface TopicView {
  id: string;
  title: string;
  summary: string | null;
  subject_id: string;
  subject_title: string;
  unit_id: string;
  unit_title: string;
  lang: string;
  available_langs: string[];
  sections: NoteSection[];
  meta: {
    exams: string[];
    estimated_minutes: number | null;
    version: string;
    status: ContentStatus;
    sources: string[];
  };
  question_count: number;
}

export interface AttemptResult {
  correct: boolean;
  answer: number;
}

export interface Stats {
  topics: number;
  questions: number;
  attempted: number;
  correct: number;
  mistakes: number;
  total_attempts: number;
}

// `lang` is the content language; the UI is always English.
export type Settings = Record<"lang" | "theme" | "font_size", string>;

export interface ApiError {
  code: string;
  message: string;
}

export function errorMessage(e: unknown): string {
  if (e && typeof e === "object" && "message" in e) return String((e as ApiError).message);
  return String(e);
}

export const api = {
  libraryTree: (lang: string) => invoke<LibrarySubject[]>("library_tree", { lang }),
  topicGet: (id: string, lang: string) => invoke<TopicView>("topic_get", { id, lang }),
  practiceQuestions: (topicId: string, lang: string) =>
    invoke<QuestionView[]>("practice_questions", { topicId, lang }),
  practiceRecord: (questionId: string, chosen: number, timeMs: number, mode: "practice" | "revise") =>
    invoke<AttemptResult>("practice_record", { questionId, chosen, timeMs, mode }),
  mistakesList: (lang: string) => invoke<QuestionView[]>("mistakes_list", { lang }),
  statsGet: () => invoke<Stats>("stats_get"),
  settingsGet: () => invoke<Settings>("settings_get"),
  settingsSet: (key: keyof Settings, value: string) => invoke<void>("settings_set", { key, value }),
};
