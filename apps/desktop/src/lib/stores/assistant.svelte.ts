// Study assistant chat state. Replies stream in as `assistant` events from the Rust side.
import { listen } from "@tauri-apps/api/event";
import { assistantApi, errorMessage, type AssistantEvent, type ChatMessage, type Suggestion } from "$lib/api";

export interface Turn extends ChatMessage {
  id: string;
  /** Text the user selected when asking (shown as a quote above the question). */
  quote?: string;
  error?: string;
  streaming?: boolean;
  /** Notes to read first, found by the app (not the model). */
  suggestions?: Suggestion[];
  /** The question this reply answers (used to find suggestions). */
  ask?: string;
  /** The same answer rewritten for listening (maths in words), made on first "Listen". */
  spoken?: string;
}

export const chat = $state({
  open: false,
  turns: [] as Turn[],
  busy: false,
  /** Selection waiting to be sent with the next question. */
  quote: "",
  /** What is on screen, set by pages. */
  topicId: null as string | null,
  questionId: null as string | null,
  /** Whether that question has been answered (only then may the model see its key). */
  questionAnswered: false,
  /** Draft in the input box (so "Ask" can prefill it). */
  draft: "",
  links: new Set<string>(),
});

let current = "";
let seq = 0;
// Hidden requests (spoken versions): id -> collected text and how to finish.
const hidden = new Map<string, { text: string; resolve: (t: string) => void; reject: (e: Error) => void }>();

listen<AssistantEvent>("assistant", (e) => {
  const { id, kind, text } = e.payload;
  const h = hidden.get(id);
  if (h) {
    if (kind === "delta") h.text += text;
    else {
      hidden.delete(id);
      if (kind === "error") h.reject(new Error(text));
      else h.resolve(h.text);
    }
    return;
  }
  const turn = chat.turns.find((t) => t.id === id);
  if (!turn) return;
  if (kind === "delta") turn.content += text;
  else {
    turn.streaming = false;
    if (kind === "error") turn.error = text;
    if (id === current) { chat.busy = false; current = ""; }
    if (kind === "done") {
      assistantApi.suggest(`${turn.ask ?? ""}\n${turn.content}`).then((s) => (turn.suggestions = s)).catch(() => {});
    }
  }
}).catch(() => {});

export async function loadLinks() {
  try {
    chat.links = new Set(await assistantApi.links());
  } catch {
    /* outside Tauri */
  }
}

/** Open the panel with selected text attached, ready for a question. */
export function askAbout(selection: string, question = "") {
  chat.open = true;
  chat.quote = selection.trim();
  chat.draft = question;
}

export async function send(text: string) {
  const q = text.trim();
  if (!q || chat.busy) return;
  if (!chat.links.size) loadLinks();
  const quote = chat.quote;
  chat.quote = "";
  chat.draft = "";
  chat.turns.push({ id: `u${++seq}`, role: "user", content: q, quote: quote || undefined });
  const id = `a${Date.now()}-${++seq}`;
  chat.turns.push({ id, role: "assistant", content: "", streaming: true, ask: `${quote}\n${q}` });
  const reply = chat.turns[chat.turns.length - 1];
  chat.busy = true;
  current = id;
  // Earlier quotes go into the history inline; the newest one is sent as the selection.
  const history: ChatMessage[] = chat.turns
    .slice(0, -1)
    .filter((t) => !t.error && t.content)
    .map((t, i, all) => ({
      role: t.role,
      content: t.quote && i !== all.length - 1 ? `[Selected text]\n${t.quote}\n[My question]\n${t.content}` : t.content,
    }));
  try {
    await assistantApi.chat(id, history, { selection: quote || null, topic_id: chat.topicId, question_id: chat.questionId, answered: chat.questionAnswered });
  } catch (e) {
    reply.streaming = false;
    reply.error = errorMessage(e);
    chat.busy = false;
    current = "";
  }
}

const SPOKEN = "Now give that same explanation as you would say it aloud to the student in class: " +
  "plain spoken English only, as a teacher talking. Say all mathematics in words (x squared, a over b, " +
  "the square root of x, f dash of c, the integral from zero to one of). Use no symbols, LaTeX, Markdown, " +
  "lists or links. Keep it under 220 words.";

/** The reply as a teacher would say it (maths in words), for "Listen". Cached on the turn. */
export async function spokenVersion(turnId: string): Promise<string> {
  const i = chat.turns.findIndex((t) => t.id === turnId);
  const turn = chat.turns[i];
  if (!turn) throw new Error("message not found");
  if (turn.spoken) return turn.spoken;
  const history: ChatMessage[] = chat.turns
    .slice(0, i + 1)
    .filter((t) => !t.error && t.content)
    .map((t) => ({ role: t.role, content: t.quote ? `[Selected text]\n${t.quote}\n[My question]\n${t.content}` : t.content }));
  history.push({ role: "user", content: SPOKEN });
  const id = `s${Date.now()}-${++seq}`;
  const text = await new Promise<string>((resolve, reject) => {
    hidden.set(id, { text: "", resolve, reject });
    assistantApi.chat(id, history, { topic_id: chat.topicId }).catch((e) => {
      hidden.delete(id);
      reject(new Error(errorMessage(e)));
    });
  });
  turn.spoken = text.trim();
  return turn.spoken;
}

export function cancel() {
  if (current) assistantApi.cancel(current).catch(() => {});
  const t = chat.turns.find((x) => x.id === current);
  if (t) t.streaming = false;
  chat.busy = false;
  current = "";
}

export function clearChat() {
  cancel();
  chat.turns = [];
  chat.quote = "";
}
