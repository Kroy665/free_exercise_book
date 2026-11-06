# Free Exercise Book

> Working name. A free, open-source, **offline-first** desktop app for Indian government exam preparation: topic-wise notes, MCQ practice, mock tests and current affairs.

- **Platforms:** Windows, macOS, Linux
- **Stack:** Rust, Tauri 2, Svelte 5 (SvelteKit SPA), SQLite with FTS5 and sqlite-vec
- **License:** App code is [GPL-3.0](LICENSE). Content is [CC BY-SA 4.0](content/LICENSE.md).
- **Cost:** Free forever. No accounts, ads or tracking.
- **Languages:** English and **Bengali (বাংলা)** for study content (notes and questions), chosen with the language button. Menus are in English. Hindi and other Indian languages come later.

## Download

Latest: **v0.1.0 (pre-alpha)**. [All releases](https://github.com/Kroy665/free_exercise_book/releases)

| Operating system | Download |
|---|---|
| **Windows 10 / 11** (64-bit) | [Installer (.exe)](https://github.com/Kroy665/free_exercise_book/releases/download/v0.1.0/Free.Exercise.Book_0.1.0_x64-setup.exe) · [MSI](https://github.com/Kroy665/free_exercise_book/releases/download/v0.1.0/Free.Exercise.Book_0.1.0_x64_en-US.msi) |
| **macOS 11+** (Apple Silicon and Intel) | [Disk image (.dmg)](https://github.com/Kroy665/free_exercise_book/releases/download/v0.1.0/Free.Exercise.Book_0.1.0_universal.dmg) |
| **Linux**: Ubuntu / Debian / Mint | [.deb](https://github.com/Kroy665/free_exercise_book/releases/download/v0.1.0/Free.Exercise.Book_0.1.0_amd64.deb) |
| **Linux**: Fedora / RHEL / openSUSE | [.rpm](https://github.com/Kroy665/free_exercise_book/releases/download/v0.1.0/Free.Exercise.Book-0.1.0-1.x86_64.rpm) |
| **Linux**: any distribution | [AppImage](https://github.com/Kroy665/free_exercise_book/releases/download/v0.1.0/Free.Exercise.Book_0.1.0_amd64.AppImage) |

The installers are **not code-signed yet**, so Windows and macOS show a warning the first time. See **[docs/INSTALL.md](docs/INSTALL.md)** for how to open the app, verify downloads and find your data.

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

Content is installed from signed **content packs** (see [docs/DATA_AND_PACKS.md](docs/DATA_AND_PACKS.md#10-implementation-notes)):

```sh
cd apps/desktop
npm run packs                                   # build + sign packs into dist/packs (dev key if you have no signing key)
FEB_CONTENT_DIR=../../content npm run tauri dev # author mode: load content/ directly, no packs
FEB_PACKS_URL=http://localhost:8000/ npm run tauri dev   # test against a local pack server
```

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
| [docs/INSTALL.md](docs/INSTALL.md) | Download, install and first-run help for each OS |
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
