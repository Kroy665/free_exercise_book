// Sidebar badges: pack updates (Downloads dot) and cards due for review (Revise count).
import { api, packsApi, type PacksView } from "$lib/api";

export const packBadge = $state({ updates: 0, due: 0 });

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
