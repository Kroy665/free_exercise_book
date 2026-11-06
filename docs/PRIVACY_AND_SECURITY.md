# Privacy and Security

## 1. Privacy promises (user-facing, keep these true)

1. **No account.** Ever required.
2. **No telemetry or analytics** by default. If an opt-in crash reporter is ever added, it must be off by default, show exactly what is sent, and never include study data.
3. **Your study data stays on your device.** Progress, notes, highlights and bookmarks are never uploaded.
4. **Network use is limited to:** fetching the content manifest and packs, the embedding model (if enabled), and app updates. All of these can be turned off in Settings → Network.
5. **No ads, no trackers, no third-party SDKs** in the app.
6. "Report error" opens the user's browser with a **pre-filled** issue. Nothing is sent unless the user submits it themselves.

## 2. Threat model

| Threat | Mitigation |
|---|---|
| Malicious or tampered content pack (mirror compromise, MITM) | Ed25519 signed manifest, SHA-256 per pack, public key compiled into app |
| Script injection via content (XSS in webview) | No raw HTML in Markdown; sanitiser on render; strict CSP; content never evaluated as code |
| Malicious app update | Tauri updater signature verification; HTTPS only |
| Abuse of Tauri IPC from compromised webview | Least-privilege capabilities; no shell, no arbitrary fs, no HTTP from the frontend |
| Corrupted DB after crash or power loss | SQLite WAL, transactional installs, automatic backup of `user.db` before migrations |
| Supply chain (crates/npm) | `cargo deny`, `npm audit` in CI, lockfiles committed, Dependabot, minimal deps |
| Signing key leak | Keys in CI secrets plus offline backup; key rotation procedure (see DATA_AND_PACKS §4) |

## 3. Webview hardening

- **CSP** (in `tauri.conf.json`):
  `default-src 'self'; img-src 'self' asset: data:; style-src 'self' 'unsafe-inline'; script-src 'self'; connect-src ipc: http://ipc.localhost; object-src 'none'; frame-src 'none'`
- No remote URLs are loaded in the webview. External links open in the system browser via the `opener` plugin, and only for `https:` URLs.
- Tauri **capabilities** grant only the commands the UI needs. No `fs`, `shell` or `http` plugins are exposed to the frontend.
- Disable devtools in release builds.

## 4. Data handling

- `user.db` is backed up automatically before each migration (keeps the last 3).
- Export files contain only study data; the format is documented so users own their data. *Implemented:* Settings → Your data → Export / Import / Reset. A backup (`.febackup`) is a SQLite copy of `user.db` (answers, tests, revision cards, settings). Import refuses non-backups and backups from newer app versions, upgrades older ones, and first saves the current progress to `<app data>/backups/` so an import can be undone. Reset deletes answers, tests and revision cards; settings and content stay.
- "Reset all data" asks for confirmation and deletes both DBs, the caches and the model.

## 5. Reporting vulnerabilities

Report privately via GitHub Security Advisories on the repository. Please do not open public issues for security problems. We aim to respond within 7 days.
