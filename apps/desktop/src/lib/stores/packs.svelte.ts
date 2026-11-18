// Sidebar badges: pack updates (Downloads dot) and cards due for review (Revise count),
// plus the start-up auto-download of new and updated topics.
import { api, packsApi, type PacksView } from "$lib/api";

export const packBadge = $state({ updates: 0, due: 0 });

/** Shown once after the start-up download: titles of topics that were added or updated. */
export const packNotice = $state({ added: [] as string[], updated: [] as string[], hasCa: false });

export function refreshDueBadge() {
  api
    .statsGet()
    .then((s) => (packBadge.due = s.due))
    .catch(() => {});
}

export function refreshPackBadge(view?: PacksView) {
  if (view) {
    packBadge.updates = view.updates;
    return;
  }
  packsApi
    .list("en")
    .then((v) => (packBadge.updates = v.updates))
    .catch(() => {});
}

export function refreshCaNav() {
  api
    .caMonths("en")
    .then((m) => (packNotice.hasCa = m.length > 0))
    .catch(() => {});
}

let started = false;

/**
 * Once per app start: ask the content server for new and updated topics and install them
 * in the background. Network problems are ignored (the Downloads page shows them).
 */
export async function autoUpdate(lang: string) {
  if (started) return;
  started = true;
  try {
    const view = await packsApi.check(lang);
    const todo = view.items.filter((i) => i.state === "update" || (i.state === "available" && i.source === "server"));
    if (!todo.length) return refreshPackBadge(view);
    const report = await packsApi.install(todo.map((i) => i.id), lang);
    const done = new Set(report.installed);
    packNotice.added = todo.filter((i) => done.has(i.id) && i.state === "available").map((i) => i.title);
    packNotice.updated = todo.filter((i) => done.has(i.id) && i.state === "update").map((i) => i.title);
    refreshPackBadge(report.view);
    refreshCaNav();
  } catch {
    // Offline, developer mode or server trouble: nothing to do now.
  }
}
