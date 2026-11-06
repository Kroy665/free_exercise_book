// Number of pack updates, for the dot on the Downloads item in the sidebar.
import { packsApi, type PacksView } from "$lib/api";

export const packBadge = $state({ updates: 0 });

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
