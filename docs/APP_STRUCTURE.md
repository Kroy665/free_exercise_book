# App Structure

How the codebase is organised and how data flows through it.

## 1. Architecture overview

```
┌──────────────────────────────────────────────────────────┐
│ Svelte 5 UI (SvelteKit, adapter-static, SPA)             │
│  routes/ · components/ · stores/ · lib/api.ts (typed)    │
└───────────────▲──────────────────────────────────────────┘
                │ Tauri IPC (invoke / events), typed via specta
┌───────────────┴──────────────────────────────────────────┐
│ apps/desktop/src-tauri  (thin shell)                     │
│  commands/*.rs  → validate input, call core, map errors  │
└───────────────▲──────────────────────────────────────────┘
                │ plain Rust calls
┌───────────────┴──────────────────────────────────────────┐
│ crates/core   library · practice · tests · srs · search  │
│               progress · settings  (no Tauri dependency) │
├──────────────────────────┬───────────────────────────────┤
│ crates/packs             │ crates/embed (optional)       │
│ manifest, download,      │ ONNX query embedding          │
│ verify, install          │ (fastembed / ort)             │
└──────────┬───────────────┴───────────────┬───────────────┘
           ▼                               ▼
   content.db (read-mostly)        user.db (user data)
   SQLite + FTS5 + sqlite-vec      SQLite
```

**Rules**
1. **The UI has no business logic.** It renders state and calls commands.
2. **Commands are thin.** They contain no SQL and no rules, only `core` calls.
3. **`crates/core` must not depend on Tauri.** That keeps it testable and reusable for a future mobile app or CLI.
4. **Content and user data live in separate databases.** Installing, updating or deleting packs never touches `user.db`.
5. **Everything works without a network.** Network access exists only in `crates/packs` (and the app updater).

## 2. Repository layout

```
.
├── Cargo.toml                    # Rust workspace
├── apps/
│   └── desktop/
│       ├── package.json          # Svelte/Vite/SvelteKit
│       ├── svelte.config.js      # adapter-static, fallback: index.html
│       ├── src/
│       │   ├── routes/           # one folder per screen (see NAVIGATION.md)
│       │   ├── lib/
│       │   │   ├── api/          # generated TS bindings + thin wrappers
│       │   │   ├── components/   # reusable UI (see UI_GUIDELINES.md)
│       │   │   ├── stores/       # Svelte 5 runes-based state ($state classes)
│       │   │   ├── i18n/         # en.json (UI, English only) + content.ts (strings inside content, per content language)
│       │   │   ├── markdown/     # note renderer + custom blocks
│       │   │   └── styles/       # tokens.css, base.css
│       │   └── app.html
│       ├── static/fonts/         # bundled Noto fonts (no CDN)
│       └── src-tauri/
│           ├── Cargo.toml
│           ├── tauri.conf.json
│           ├── capabilities/     # least-privilege permission sets
│           └── src/
│               ├── main.rs
│               ├── state.rs      # AppState: db pools, paths, settings
│               ├── error.rs      # AppError → serialisable IPC error
│               └── commands/     # library.rs, practice.rs, tests.rs, ...
├── crates/
│   ├── core/
│   │   └── src/
│   │       ├── db/               # connection setup, migrations (refinery)
│   │       ├── library/          # subjects, topics, notes
│   │       ├── practice/         # question selection, attempts, grading
│   │       ├── tests/            # mock test engine, scoring, resume
│   │       ├── srs/              # FSRS scheduling (fsrs crate)
│   │       ├── search/           # FTS5 + vector + hybrid ranking
│   │       ├── progress/         # analytics queries
│   │       └── model/            # shared types (serde + specta)
│   ├── packs/
│   │   └── src/                  # manifest, http (ureq/reqwest), verify (minisign), install
│   └── embed/
│       └── src/                  # model load, tokenise, embed(query) -> [f32; 384]
├── tools/
│   └── packer/                   # `packer build content/ --out dist/` → .pack + manifest
├── content/                      # source content (see CONTENT_STRUCTURE.md)
└── docs/
```

## 3. Key crates and libraries

| Concern | Choice |
|---|---|
| Desktop shell | `tauri` 2.x |
| SQLite | `rusqlite` (bundled feature) + `r2d2` pool; WAL mode |
| Full-text search | SQLite FTS5 (`unicode61 remove_diacritics 2`; trigram table for Indic scripts) |
| Vectors | `sqlite-vec` extension, statically linked |
| Embeddings | `fastembed` / `ort`, model `multilingual-e5-small` (384-dim) |
| Spaced repetition | `fsrs` |
| Migrations | `refinery` (or `rusqlite_migration`) |
| Serialization | `serde`, `serde_json`, `serde_yaml` (packer only) |
| IPC typing | `specta` + `tauri-specta` to generate TypeScript bindings |
| Errors | `thiserror` in libraries, `anyhow` only in tools |
| Logging | `tracing` → rolling local log file (never uploaded). *v0.1 status: startup messages use `eprintln!`; move to `tracing`.* |
| Signatures | `minisign-verify` (app) / `minisign` (packer) |
| Compression | `zstd` |

## 4. Data locations

Resolved with Tauri's path API, so they follow each OS's conventions:

| Data | Location |
|---|---|
| `content.db` | `<app_data>/content.db` |
| `user.db` | `<app_data>/user.db` |
| Downloaded packs (cache) | `<app_cache>/packs/` |
| Embedding model | `<app_data>/models/` |
| Logs | `<app_log>/` |

Users can move the data folder in Settings (useful for portable or USB installs).

## 5. IPC contract

- Commands are grouped by domain: `library_*`, `practice_*`, `test_*`, `search_*`, `progress_*`, `packs_*`, `settings_*`.
- Every command returns `Result<T, AppError>`. `AppError` has a stable `code` (e.g. `PACK_SIGNATURE_INVALID`) and a user-safe `message`.
- Long operations (downloads, installs, embedding) emit **events** (`packs://progress`) instead of blocking.
- TS bindings should be **generated** with `tauri-specta` and committed. *v0.1 status:* `src/lib/api/index.ts` is still hand-written and mirrors `crates/core/src/model.rs`; switch to generated bindings once `tauri-specta` 2.x is stable.

Example:

```rust
#[tauri::command]
#[specta::specta]
pub async fn practice_next(
    state: State<'_, AppState>,
    req: NextQuestionRequest,
) -> Result<QuestionView, AppError> {
    Ok(state.core.practice().next(req)?)
}
```

## 6. Frontend structure

- **Routing:** SvelteKit file routes, SPA mode (`ssr = false`, `prerender = false` at root).
- **State:** small domain stores as Svelte 5 rune classes (`settings.svelte.ts`, `session.svelte.ts`). Server data is fetched per page in `+page.ts` `load` via the api layer.
- **No network calls from the UI.** All I/O goes through Rust commands.
- **Markdown** is rendered by a sanitising pipeline (markdown-it + our custom block plugins). Raw HTML in content is disabled.
- **i18n:** UI strings live in `lib/i18n/*.json`, accessed via a `t('key')` helper. No hard-coded user-facing strings.

## 7. Startup sequence

1. Resolve paths and open both DBs (create and migrate if needed).
1a. If `FEB_CONTENT_DIR` is set (developer mode), import that folder directly. Otherwise install bundled packs on first run / update installed packs from a newer bundle (docs/DATA_AND_PACKS.md §10).
2. Load settings. Apply theme and font size before first paint (avoids a flash).
3. If no packs are installed, go to **Onboarding**. Otherwise go to **Home**.
4. In the background (only if network is allowed): check the manifest for pack and app updates.
5. In the background: load the embedding model lazily on first meaning-based search.

## 8. Testing layers

| Layer | Tool |
|---|---|
| `crates/core` | Rust unit + integration tests against temp SQLite DBs |
| `crates/packs` | Tests with fixture packs, including tampered ones that must fail |
| `tools/packer` | Snapshot tests on `content/` sample → deterministic pack |
| UI components | Vitest + @testing-library/svelte |
| End-to-end | WebdriverIO with `tauri-driver` (Windows/Linux) |
