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

// ---------- Content packs (Downloads page) ----------

export type PackState = "installed" | "update" | "available";

export interface PackItem {
  id: string;
  title: string;
  summary: string | null;
  subject: string;
  subject_title: string;
  unit: string;
  unit_title: string;
  sort: [number, number, number];
  langs: string[];
  questions: number;
  sections: number;
  size: number;
  state: PackState;
  installed_version: string | null;
  available_version: string | null;
  source: "bundled" | "server" | null;
}

export interface PacksView {
  items: PackItem[];
  remote: { url: string; checked_at: number | null; error: ApiError | null };
  dev_mode: boolean;
  updates: number;
}

export interface InstallReport {
  view: PacksView;
  installed: string[];
  failed: [string, ApiError][];
}

export interface PackProgress {
  id: string;
  phase: "download" | "install" | "done" | "error";
  done: number;
  total: number;
  message: string | null;
}

export const packsApi = {
  list: (lang: string) => invoke<PacksView>("packs_list", { lang }),
  check: (lang: string) => invoke<PacksView>("packs_check", { lang }),
  install: (ids: string[], lang: string) => invoke<InstallReport>("packs_install", { ids, lang }),
  remove: (id: string, lang: string) => invoke<PacksView>("packs_remove", { id, lang }),
  importFolder: (path: string, lang: string) => invoke<InstallReport>("packs_import_folder", { path, lang }),
};

// ---------- Mock tests ----------

export interface PatternSectionView {
  id: string;
  name: string;
  required: number;
  available: number;
  marks_each: number;
}

export interface PatternView {
  id: string;
  name: string;
  duration_minutes: number;
  negative_marking: number;
  total_questions: number;
  total_marks: number;
  available: number;
  scaled_minutes: number;
  sections: PatternSectionView[];
  source: string | null;
  as_of: string | null;
}

export interface TestListItem {
  id: number;
  title: string;
  kind: "custom" | "pattern";
  status: "ready" | "in_progress" | "submitted";
  questions: number;
  duration_ms: number;
  remaining_ms: number;
  created_at: number;
  submitted_at: number | null;
  score: number | null;
  max_score: number | null;
  accuracy: number | null;
}

export interface AnswerState {
  choice: number | null;
  marked: boolean;
  visited: boolean;
  time_ms: number;
}

export interface TestState {
  answers: Record<string, AnswerState>;
  current: number;
}

export interface TestSession {
  id: number;
  title: string;
  kind: string;
  status: "ready" | "in_progress" | "submitted";
  duration_ms: number;
  remaining_ms: number;
  scaled_from: [number, number] | null;
  sections: { id: string; name: string; marks_each: number; negative: number; questions: QuestionView[] }[];
  state: TestState;
  total_questions: number;
  total_marks: number;
  missing: number;
}

export interface Tally {
  correct: number;
  wrong: number;
  unanswered: number;
  score: number;
  max_score: number;
}

export interface TestSummary extends Tally {
  accuracy: number;
  time_used_ms: number;
}

export interface ReviewItem {
  section: string;
  question: QuestionView;
  chosen: number | null;
  marked: boolean;
  time_ms: number;
  outcome: "correct" | "wrong" | "unanswered";
}

export interface TestResult {
  id: number;
  title: string;
  submitted_at: number | null;
  duration_ms: number;
  scaled_from: [number, number] | null;
  summary: TestSummary;
  sections: (Tally & { id: string; name: string })[];
  topics: (Tally & { id: string; name: string })[];
  review: ReviewItem[];
}

export interface CustomSpec {
  title: string | null;
  topic_ids: string[];
  count: number;
  duration_minutes: number;
  marks_each: number;
  negative: number;
}

export const testsApi = {
  overview: (lang: string) => invoke<{ patterns: PatternView[]; tests: TestListItem[] }>("tests_overview", { lang }),
  createCustom: (spec: CustomSpec) => invoke<number>("tests_create_custom", { spec }),
  createPattern: (patternId: string) => invoke<number>("tests_create_pattern", { patternId }),
  session: (id: number, lang: string) => invoke<TestSession>("test_session", { id, lang }),
  start: (id: number) => invoke<void>("test_start", { id }),
  save: (id: number, testState: TestState, remainingMs: number) =>
    invoke<void>("test_save", { id, testState, remainingMs }),
  submit: (id: number, testState: TestState, remainingMs: number) =>
    invoke<TestSummary>("test_submit", { id, testState, remainingMs }),
  result: (id: number, lang: string) => invoke<TestResult>("test_result", { id, lang }),
  remove: (id: number) => invoke<void>("test_delete", { id }),
};

// ---------- Search ----------

export interface SearchHit {
  kind: "topic" | "section" | "question";
  ref: string;
  topic_id: string;
  topic_title: string;
  title: string;
  /** Matches are wrapped in \u0002 … \u0003 */
  snippet: string;
  /** Language of `title`. */
  lang: string;
  /** Language of `snippet` (English when only English text matched). */
  snippet_lang: string;
}

export const searchApi = {
  search: (query: string, lang: string) => invoke<SearchHit[]>("search", { query, lang }),
};
