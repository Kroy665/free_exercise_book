# Free Exercise Book

> Working name. A free, open-source, **offline-first** desktop app for Indian government exam preparation: topic-wise notes, MCQ practice, mock tests and current affairs.

- **Platforms:** Windows, macOS, Linux
- **Stack:** Rust, Tauri 2, Svelte 5 (SvelteKit SPA), SQLite with FTS5 and sqlite-vec
- **License:** App code is [GPL-3.0](LICENSE). Content is [CC BY-SA 4.0](content/LICENSE.md).
- **Cost:** Free forever. No accounts, ads or tracking.
- **Languages:** English and **Bengali (বাংলা)** at launch, for both the UI and the content. Hindi and other Indian languages come later.

## Who it is for

Aspirants preparing for UPSC, State PSCs, SSC, Banking (IBPS/SBI), Railways (RRB) and similar exams, especially those with **limited or unreliable internet**. Users download the topics they need once and study offline.

## Status

Pre-alpha (v0.1 in progress). Working now: library, notes reader, topic practice (all 5 question types), mistake notebook and settings, in **English and Bengali**, with one sample topic (*The Revolt of 1857*).

## Development

Prerequisites: [Rust](https://rustup.rs) (stable ≥ 1.88), Node.js ≥ 20, and the [Tauri prerequisites](https://v2.tauri.app/start/prerequisites/) for your OS (WebView2 on Windows, WebKitGTK 4.1 on Linux).

```sh
cd apps/desktop
npm install
npm run tauri dev        # run the app (imports ../../content on start)
npm run tauri build      # build installers
```

Checks:

```sh
cargo test --workspace                       # core tests (uses the sample content)
cargo clippy --workspace --all-targets -- -D warnings
cd apps/desktop && npm run check             # svelte-check / TypeScript
python3 tools/content-check/validate.py content   # needs: pip install pyyaml jsonschema
```

Set `FEB_CONTENT_DIR=/path/to/content` to load content from another folder.

## Documentation

| Document | What it covers |
|---|---|
| [docs/SPEC.md](docs/SPEC.md) | Product specification: features, scope, roadmap |
| [docs/APP_STRUCTURE.md](docs/APP_STRUCTURE.md) | Architecture, repository layout, modules, data flow |
| [docs/UI_GUIDELINES.md](docs/UI_GUIDELINES.md) | Design principles, tokens, typography, components, accessibility |
| [docs/NAVIGATION.md](docs/NAVIGATION.md) | Screens, routes, user flows, keyboard shortcuts |
| [docs/CONTENT_STRUCTURE.md](docs/CONTENT_STRUCTURE.md) | How notes, MCQs, topics and exams are organised and formatted |
| [docs/CONTENT_GUIDELINES.md](docs/CONTENT_GUIDELINES.md) | Editorial rules: accuracy, sourcing, verification, language, copyright |
| [docs/DATA_AND_PACKS.md](docs/DATA_AND_PACKS.md) | Database schema, vector search, offline content packs, updates |
| [docs/CODING_GUIDELINES.md](docs/CODING_GUIDELINES.md) | Code style, testing, CI, commits, releases |
| [docs/PRIVACY_AND_SECURITY.md](docs/PRIVACY_AND_SECURITY.md) | Privacy promises, threat model, security rules |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute code, content and translations |

## Repository layout (planned)

```
apps/desktop/        Tauri app (Svelte UI + src-tauri Rust shell)
crates/core/         Domain logic: library, practice, tests, SRS, search
crates/packs/        Pack format, download, signature verification, install
crates/embed/        Optional on-device query embeddings
tools/packer/        CLI that turns content/ into signed .pack files
content/             Source content (YAML + Markdown), CC BY-SA 4.0
docs/                Guidelines and specifications
```
