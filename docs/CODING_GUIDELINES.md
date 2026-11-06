# Coding Guidelines

## 1. General

- **Simple over clever.** This project will be maintained by volunteers with varied experience.
- Small PRs (≤ 400 lines changed where possible), one concern per PR.
- Every feature needs tests at the right layer (see [APP_STRUCTURE.md §8](APP_STRUCTURE.md#8-testing-layers)).
- No new dependency without a short justification in the PR (size, maintenance, license). Licenses must be GPL-3.0-compatible (`cargo deny` enforces this).

## 2. Rust

- Toolchain: stable (≥ 1.88). **Edition 2024** for all crates (set once in the workspace `Cargo.toml`).
- `cargo fmt` and `cargo clippy --all-targets -- -D warnings` must pass.
- Errors: `thiserror` enums in libraries; no `unwrap()`/`expect()` outside tests and `main` startup (use `?`).
- No `unsafe` unless reviewed and commented with a `// SAFETY:` note.
- SQL: use parameterised queries only, kept next to the domain module (`library/queries.rs`). Never use string-formatted SQL with user input.
- Migrations are append-only and numbered. Never edit a released migration.
- Blocking work (DB, file I/O, embeddings) runs on `tauri::async_runtime::spawn_blocking` or a dedicated thread. Never on the main thread.
- Public types crossing IPC derive `Serialize, Deserialize, specta::Type`.
- Log with `tracing`, never `println!`. Never log user notes or personal data.

## 3. Svelte / TypeScript

- Svelte 5 with **runes** (`$state`, `$derived`, `$effect`). No legacy stores in new code.
- TypeScript `strict: true`. No `any` without a comment.
- Prettier + ESLint (`eslint-plugin-svelte`) must pass. `svelte-check` must pass.
- Components: `PascalCase.svelte`, one component per file, props typed with `interface Props`.
- Styling: scoped `<style>` using tokens from `tokens.css`. No CSS framework, so there is no runtime styling cost and the look stays consistent.
- No direct `invoke()` in components. Call through `lib/api/`.
- Every user-visible string goes through `t()`.
- Accessibility lint (`svelte-check` a11y warnings) is treated as an error.

## 4. Git and commits

- Branch from `main`: `feat/…`, `fix/…`, `content/…`, `docs/…`.
- **Conventional Commits:** `feat(practice): add assertion-reason type`, `fix(packs): resume partial download`, `content(history): add revolt of 1857`.
- PRs need one approving review. Content PRs need a content reviewer (see [CONTENT_GUIDELINES.md](CONTENT_GUIDELINES.md)).
- Squash merge. The PR title becomes the commit message.

## 5. CI (GitHub Actions)

| Job | Runs on |
|---|---|
| Rust fmt, clippy, test | Linux, Windows, macOS |
| `cargo deny` (licenses, advisories) | Linux |
| Frontend lint, `svelte-check`, Vitest | Linux |
| Content validate (schema, refs, duplicates, answer spread) | Linux, only on `content/**` changes |
| Build installers (tauri-action) | All 3 OS on tags |
| E2E smoke (tauri-driver) | Linux + Windows, nightly |

## 6. Releases

- App versions: semver, tags `v0.1.0`. Changelog generated from Conventional Commits.
- Installers: `.msi` / `.exe` (NSIS) for Windows, `.dmg` (universal) for macOS, `.AppImage` + `.deb` + `.rpm` for Linux. Flatpak later.
- Updater artifacts are signed with the Tauri updater key (kept in CI secrets, with offline backup held by two maintainers).
- Code signing: Windows via SignPath Foundation (free for OSS). macOS notarisation needs an Apple Developer account.
- Builds are reproducible where possible. Checksums (`SHA256SUMS`) are published with every release.

## 7. Performance budgets (checked in PR review)

- Installer ≤ 15 MB, JS bundle ≤ 400 KB gzipped.
- No query > 50 ms on the sample 100k-question benchmark DB (`cargo bench -p core`).
- First paint ≤ 1 s after window creation on a reference low-end machine.
