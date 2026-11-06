# Data and Content Packs

How content gets from `content/` to a user's offline database, and how search (keyword + vector) works.

## 1. Pipeline

```
content/ (YAML + MD)
   │  tools/packer validate   → schema, IDs, refs, duplicates, answer spread
   │  tools/packer build      → per-topic SQLite + embeddings
   │  tools/packer sign       → minisign (Ed25519)
   ▼
dist/
  manifest.json + manifest.json.minisig
  packs/hist.modern.revolt-1857@1.0.0.pack
   │  GitHub Release (primary) + mirrors
   ▼
App: download → verify hash + signature → import into content.db → index
```

The packer runs in CI on every merge to `main` in the content repo. Builds are **deterministic**: the same input gives a byte-identical pack.

## 2. Pack format

A `.pack` is a **zstd-compressed SQLite database** with this schema (subset of `content.db`):

| Table | Purpose |
|---|---|
| `pack_meta` | id, version, content schema version, embedding model id, created_at |
| `topics` | id, unit_id, subject_id, titles (JSON by lang), metadata JSON |
| `note_sections` | id (`topic#anchor`), topic_id, lang, ord, heading, body_md |
| `questions` | id, topic_id, type, difficulty, exams JSON, refs JSON, data JSON (all langs), status, as_of, source |
| `assets` | path, mime, bytes (images) |
| `embeddings` | item_id, item_kind (`section`/`question`), lang, vector BLOB (f32 × 384, little-endian) |

Granularity: **one pack per topic**, plus **one pack per current-affairs month**. A "subject bundle" is just a list of topic packs in the manifest.

## 3. Manifest

```json
{
  "schema": 1,
  "generated_at": "2026-11-06T00:00:00Z",
  "embedding_model": "intfloat/multilingual-e5-small@v1",
  "min_app_version": "0.1.0",
  "packs": [
    {
      "id": "hist.modern.revolt-1857",
      "version": "1.0.0",
      "title": {"en": "The Revolt of 1857", "bn": "১৮৫৭ সালের মহাবিদ্রোহ"},
      "subject": "hist", "unit": "hist.modern",
      "langs": ["en", "bn"],
      "exams": ["upsc-cse", "ssc-cgl"],
      "size": 412345,
      "sha256": "…",
      "url": "packs/hist.modern.revolt-1857@1.0.0.pack",
      "delta_from": {"0.9.0": {"url": "…", "sha256": "…", "size": 20480}},
      "counts": {"sections": 7, "questions": 12},
      "status_summary": {"ai-generated": 12, "reviewed": 0, "verified": 0},
      "changelog": "Initial release"
    }
  ],
  "mirrors": ["https://github.com/<org>/<content-repo>/releases/download/latest/", "https://…"]
}
```

## 4. Integrity and trust

- The manifest is signed with the project's **minisign** key. The public key is **compiled into the app**.
- The app verifies: manifest signature → each pack's `sha256` → pack's `pack_meta.id/version` match the manifest.
- Sideloaded packs must come with their `.minisig`, or be inside a signed bundle. Unsigned packs are rejected unless the user enables **Developer mode** (shown with a warning banner).
- Key rotation: the manifest can carry a new key signed by the old one. The app accepts it once and stores it.

## 5. Install process (transactional)

1. Download to `<cache>/packs/*.part` with resume support (HTTP Range).
2. Verify the hash and signature.
3. Decompress to a temp file and `ATTACH` it to `content.db`.
4. In **one transaction**: delete existing rows for that pack ID, insert new rows, update FTS and vector indexes, record it in `installed_packs`.
5. Detach and delete the temp file. Optionally keep the compressed pack for sharing or sideloading.
6. If the update changed any answer, re-grade the affected attempts in `user.db` and queue a notice.

Any failure rolls back, so the old version stays intact.

## 6. `content.db` (on device)

Same tables as the pack, plus:

```sql
CREATE TABLE installed_packs (id TEXT PRIMARY KEY, version TEXT, installed_at INTEGER, size INTEGER);

-- Keyword search
CREATE VIRTUAL TABLE fts_sections  USING fts5(heading, body, content='note_sections', tokenize='unicode61 remove_diacritics 2');
CREATE VIRTUAL TABLE fts_questions USING fts5(stem, options, explanation, tokenize='unicode61 remove_diacritics 2');
CREATE VIRTUAL TABLE fts_trigram   USING fts5(text, tokenize='trigram');  -- robust for Indic scripts & typos

-- Vector search (sqlite-vec)
CREATE VIRTUAL TABLE vec_items USING vec0(item_rowid INTEGER PRIMARY KEY, embedding float[384]);
```

## 7. `user.db` (on device, never overwritten by packs)

```sql
attempts(id, question_id, question_version, chosen, correct, time_ms, mode, session_id, created_at)
sessions(id, kind /*practice|test|daily|revise*/, source JSON, started_at, ended_at, score JSON)
test_state(test_id, pattern JSON, question_ids JSON, answers JSON, marked JSON, remaining_ms, updated_at)
srs_cards(question_id PRIMARY KEY, stability, difficulty, due, last_review, reps, lapses, state)
bookmarks(item_id, item_kind, created_at, note)
highlights(section_id, lang, start, end, color, note, created_at)
reading_progress(topic_id, lang, section_id, scroll, updated_at)
settings(key PRIMARY KEY, value JSON)
```

User data references content **by stable ID only**, so it survives pack removal and reinstall.
**Export** = `user.db` copied via the SQLite backup API → `progress-YYYY-MM-DD.febackup` (zstd).

## 8. Search

### Keyword (always available)
FTS5 with BM25, with prefix matching for search-as-you-type. Uses the trigram index for Indic text and typos.

**Bengali search notes**
- Normalise text (NFC) at both pack-build and query time, so composed and decomposed forms of characters like `য়` and `ড়` match.
- Index Bengali digits (০–৯) and ASCII digits as the same value, so "1857" finds "১৮৫৭" and vice versa.
- Keep the English terms that appear in brackets in Bengali notes in the index, so typing "Doctrine of Lapse" in the Bengali UI still finds স্বত্ববিলোপ নীতি.
- `multilingual-e5-small` covers Bengali, so meaning-based search works across languages (an English query can find a Bengali note).

### Vector (optional)
- Content vectors are **precomputed by the packer** with `multilingual-e5-small` (`"passage: "` prefix).
- On device, only the **query** is embedded (`"query: "` prefix) by `crates/embed`. The model (~120 MB, quantised ONNX) is downloaded only if the user turns on "Smart search".
- `vec_items` KNN (cosine) returns the top 50 items.

### Hybrid ranking
`score = 0.5 · rrf(bm25_rank) + 0.5 · rrf(vector_rank)` (Reciprocal Rank Fusion, k = 60). If the model is absent, only keyword search is used. The UI never shows an error for this.

### Other vector uses
- **Related notes/questions:** KNN over precomputed vectors. This **needs no model on the device**.
- **"Revise this" after a wrong answer:** `refs` first, then nearest note sections.
- **Duplicate detection (packer, CI):** cosine > 0.92 between questions in the same subject → CI warning.

### Model compatibility
`embedding_model` in the manifest must match the installed model. If the project changes models, the app keeps keyword search, re-downloads the model, and packs are rebuilt. Vectors from different models are never mixed.

## 9. Hosting and bandwidth

- Primary: GitHub Releases on the content repo (free, reliable).
- Mirrors: jsDelivr (GitHub-backed CDN) and any community mirror listed in the manifest. The app tries mirrors in order.
- Downloads are resumable, delta updates cut repeat downloads, and the app never downloads in the background on a metered connection without asking (Windows exposes this; elsewhere there is a user setting).
