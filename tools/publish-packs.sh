#!/usr/bin/env bash
# Publish content packs from this machine (no GitHub Actions minutes).
#
#   tools/publish-packs.sh
#
# 1. Validates content/ (schemas, formulas, graphs).
# 2. Builds and signs every topic with the maintainer key
#    (~/.config/free-exercise-book/pack-signing.key, or FEB_PACK_SIGNING_KEY).
# 3. Commits the result on top of the `packs` branch and pushes it (a normal push,
#    never a force push). Installed apps pick the new topics up on their next start.
#
# Uses a separate clone in dist/packs-branch so the main checkout is never touched.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

key="${FEB_PACK_SIGNING_KEY_FILE:-$HOME/.config/free-exercise-book/pack-signing.key}"
if [[ -z "${FEB_PACK_SIGNING_KEY:-}" && ! -f "$key" ]]; then
  echo "error: no signing key ($key). See docs/DATA_AND_PACKS.md §4." >&2
  exit 1
fi

python3 -I tools/content-check/validate.py content | tail -2
python3 -I tools/content-check/validate.py content | grep -q '^VALID$' || { echo "error: content is not valid" >&2; exit 1; }

out="$root/dist/packs-publish"
rm -rf "$out"
SOURCE_DATE_EPOCH="$(git log -1 --format=%ct)" \
  cargo run --release -q -p feb-packer -- build content --out "$out" \
  $( [[ -z "${FEB_PACK_SIGNING_KEY:-}" ]] && echo --key "$key" )

remote="$(git remote get-url origin)"
branch_dir="$root/dist/packs-branch"
if [[ ! -d "$branch_dir/.git" ]]; then
  if git ls-remote --exit-code --heads origin packs >/dev/null 2>&1; then
    git clone -q --branch packs --single-branch "$remote" "$branch_dir"
  else
    mkdir -p "$branch_dir" && git -C "$branch_dir" init -q -b packs
    git -C "$branch_dir" remote add origin "$remote"
  fi
else
  git -C "$branch_dir" pull -q --ff-only origin packs 2>/dev/null || true
fi
git -C "$branch_dir" config user.name "$(git config user.name)"
git -C "$branch_dir" config user.email "$(git config user.email)"

# Replace the published files with the new build.
find "$branch_dir" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
cp -R "$out"/. "$branch_dir"/
cat > "$branch_dir/README.md" <<MD
Signed content packs for Free Exercise Book, built from $(git rev-parse --short HEAD)
by tools/publish-packs.sh. Do not edit by hand.
MD

git -C "$branch_dir" add -A
if git -C "$branch_dir" diff --cached --quiet; then
  echo "packs branch already up to date"
  exit 0
fi
git -C "$branch_dir" commit -q -m "Content packs from $(git rev-parse --short HEAD)"
git -C "$branch_dir" push -q origin packs
echo "published: $(ls "$out" | grep -c '\.pack$' || true) pack file(s) -> packs branch"
