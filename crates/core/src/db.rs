//! Connection setup and migrations. Migrations are append-only (docs/CODING_GUIDELINES.md §2).

use crate::Result;
use rusqlite::Connection;
use std::path::Path;

/// Current-affairs items (structured); also created in every pack database (may be empty).
const CA_ITEMS_DDL: &str = r#"
    CREATE TABLE ca_items (
        id             TEXT PRIMARY KEY,  -- "<topic_id>/<item id>"
        topic_id       TEXT NOT NULL,     -- the month, e.g. ca.2026.10
        ord            INTEGER NOT NULL,
        date           TEXT NOT NULL,
        category       TEXT NOT NULL,
        title          TEXT NOT NULL,     -- JSON {lang: text}
        body           TEXT NOT NULL,     -- JSON {lang: text}
        key_points     TEXT NOT NULL,     -- JSON [{lang: text}]
        related_topics TEXT NOT NULL,     -- JSON [topic id]
        source         TEXT NOT NULL,
        as_of          TEXT NOT NULL,
        status         TEXT NOT NULL
    );
    CREATE INDEX ca_items_topic ON ca_items(topic_id, ord);
"#;

const CONTENT_MIGRATIONS: &[&str] = &[
    // 1: initial content schema
    r#"
    CREATE TABLE subjects (
        id    TEXT PRIMARY KEY,
        ord   INTEGER NOT NULL,
        title TEXT NOT NULL            -- JSON {lang: text}
    );
    CREATE TABLE units (
        id         TEXT PRIMARY KEY,
        subject_id TEXT NOT NULL,
        ord        INTEGER NOT NULL,
        title      TEXT NOT NULL
    );
    CREATE TABLE topics (
        id         TEXT PRIMARY KEY,
        unit_id    TEXT NOT NULL,
        subject_id TEXT NOT NULL,
        ord        INTEGER NOT NULL,
        title      TEXT NOT NULL,
        summary    TEXT,
        meta       TEXT NOT NULL       -- JSON: exams, version, status, sources, estimated_minutes
    );
    CREATE TABLE note_sections (
        topic_id TEXT NOT NULL,
        lang     TEXT NOT NULL,
        anchor   TEXT NOT NULL,
        ord      INTEGER NOT NULL,
        heading  TEXT NOT NULL,
        body_md  TEXT NOT NULL,
        PRIMARY KEY (topic_id, lang, anchor)
    );
    CREATE TABLE questions (
        id         TEXT PRIMARY KEY,   -- "<topic_id>/q0001"
        topic_id   TEXT NOT NULL,
        ord        INTEGER NOT NULL,
        kind       TEXT NOT NULL,
        difficulty INTEGER NOT NULL,
        status     TEXT NOT NULL,
        data       TEXT NOT NULL       -- JSON of the source question, all languages
    );
    CREATE INDEX questions_topic ON questions(topic_id, ord);
    "#,
    // 2: installed content packs (docs/DATA_AND_PACKS.md §6)
    r#"
    CREATE TABLE installed_packs (
        id           TEXT PRIMARY KEY,  -- = topic id
        version      TEXT NOT NULL,
        sha256       TEXT NOT NULL,     -- of the compressed .pack file
        size         INTEGER NOT NULL,  -- compressed bytes
        installed_at INTEGER NOT NULL DEFAULT (unixepoch())
    );
    "#,
    // 3: exam patterns for mock tests (from content/exams/, shipped in the signed manifest)
    r#"
    CREATE TABLE exam_patterns (
        id   TEXT PRIMARY KEY,
        data TEXT NOT NULL              -- JSON ExamPattern
    );
    "#,
    // 4: full-text search (docs/DATA_AND_PACKS.md §8, crates/core/src/search.rs).
    // `search_index`: word index. `tokenchars` keeps Bengali/Devanagari vowel signs, virama and
    // ZWJ/ZWNJ inside words (by default unicode61 splits words at them). `alt` holds the
    // digit-normalised text (০-৯ -> 0-9) so "1857" finds "১৮৫৭"; title/body stay original
    // for display. `search_trigram`: substring fallback (Bengali compounds, partial words).
    r#"
    CREATE VIRTUAL TABLE search_index USING fts5(
        title,
        body,
        alt,
        kind     UNINDEXED,   -- topic | section | question
        ref      UNINDEXED,   -- topic id | section anchor | question id
        topic_id UNINDEXED,
        lang     UNINDEXED,
        tokenize = 'unicode61 remove_diacritics 2 tokenchars ''ঁংঃ়ািীুূৃৄেৈোৌ্ৗৢৣऀँंःऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏ॒॑॓॔ॕॖॗॢॣ‌‍'''
    );
    CREATE VIRTUAL TABLE search_trigram USING fts5(
        text,
        kind     UNINDEXED,
        ref      UNINDEXED,
        topic_id UNINDEXED,
        lang     UNINDEXED,
        tokenize = 'trigram'
    );
    "#,
    // 5: current-affairs items
    CA_ITEMS_DDL,
];

/// Pack file format version (docs/DATA_AND_PACKS.md §2). A pack is a SQLite database with
/// the content tables of content migration 1 plus a `pack_meta` key/value table.
pub const PACK_FORMAT: u32 = 1;

/// Create an empty pack database at `path` (overwritten if it exists).
pub fn create_pack(path: &Path) -> Result<Connection> {
    if path.exists() {
        std::fs::remove_file(path).map_err(|source| crate::CoreError::Io {
            path: path.display().to_string(),
            source,
        })?;
    }
    let conn = Connection::open(path)?;
    conn.execute_batch(CONTENT_MIGRATIONS[0])?;
    conn.execute_batch("CREATE TABLE pack_meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);")?;
    conn.execute_batch(CA_ITEMS_DDL)?;
    Ok(conn)
}

const USER_MIGRATIONS: &[&str] = &[
    // 1: attempts + settings
    r#"
    CREATE TABLE attempts (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        question_id TEXT NOT NULL,
        chosen      INTEGER NOT NULL,
        correct     INTEGER NOT NULL,
        time_ms     INTEGER NOT NULL,
        mode        TEXT NOT NULL,
        created_at  INTEGER NOT NULL DEFAULT (unixepoch())
    );
    CREATE INDEX attempts_question ON attempts(question_id, id);
    CREATE TABLE settings (
        key   TEXT PRIMARY KEY,
        value TEXT NOT NULL
    );
    "#,
    // 2: mock tests (docs/NAVIGATION.md §4.4)
    r#"
    CREATE TABLE tests (
        id           INTEGER PRIMARY KEY AUTOINCREMENT,
        kind         TEXT NOT NULL,      -- custom | pattern
        pattern_id   TEXT,
        title        TEXT NOT NULL,
        config       TEXT NOT NULL,      -- JSON TestConfig (sections, question ids, marking, duration)
        state        TEXT NOT NULL,      -- JSON TestState (answers, marks, time per question)
        remaining_ms INTEGER NOT NULL,
        status       TEXT NOT NULL,      -- ready | in_progress | submitted
        created_at   INTEGER NOT NULL DEFAULT (unixepoch()),
        started_at   INTEGER,
        submitted_at INTEGER,
        result       TEXT                -- JSON TestSummary
    );
    "#,
    // 3: spaced repetition cards (FSRS-5, crates/core/src/srs.rs)
    r#"
    CREATE TABLE srs_cards (
        question_id TEXT PRIMARY KEY,
        stability   REAL NOT NULL,     -- days until recall probability falls to 90%
        difficulty  REAL NOT NULL,     -- 1 (easy) .. 10 (hard)
        due         INTEGER NOT NULL,  -- unix seconds
        last_review INTEGER NOT NULL,  -- unix seconds
        reps        INTEGER NOT NULL,
        lapses      INTEGER NOT NULL
    );
    CREATE INDEX srs_due ON srs_cards(due);
    "#,
];

fn configure(conn: &Connection) -> Result<()> {
    conn.pragma_update(None, "journal_mode", "WAL")?;
    conn.pragma_update(None, "foreign_keys", "ON")?;
    conn.pragma_update(None, "synchronous", "NORMAL")?;
    Ok(())
}

fn migrate(conn: &mut Connection, migrations: &[&str]) -> Result<()> {
    let current: usize = conn.pragma_query_value(None, "user_version", |r| r.get(0))?;
    for (i, sql) in migrations.iter().enumerate().skip(current) {
        let tx = conn.transaction()?;
        tx.execute_batch(sql)?;
        tx.pragma_update(None, "user_version", i + 1)?;
        tx.commit()?;
    }
    Ok(())
}

pub fn open_content(path: &Path) -> Result<Connection> {
    let mut conn = Connection::open(path)?;
    configure(&conn)?;
    migrate(&mut conn, CONTENT_MIGRATIONS)?;
    Ok(conn)
}

/// Schema version of `user.db` written by this app version.
pub fn user_schema_version() -> usize {
    USER_MIGRATIONS.len()
}

/// Backups of `user.db` taken before a schema upgrade are kept (newest N).
const KEEP_MIGRATION_BACKUPS: usize = 3;

pub fn open_user(path: &Path) -> Result<Connection> {
    let mut conn = Connection::open(path)?;
    configure(&conn)?;
    // Before upgrading an existing progress database, keep a copy
    // (docs/PRIVACY_AND_SECURITY.md §4): `<dir>/backups/user-before-v<N>-<time>.db`.
    let current: usize = conn.pragma_query_value(None, "user_version", |r| r.get(0))?;
    if current > 0 && current < USER_MIGRATIONS.len() {
        backup_before_migration(&conn, path, current)?;
    }
    migrate(&mut conn, USER_MIGRATIONS)?;
    Ok(conn)
}

fn backup_before_migration(conn: &Connection, path: &Path, from: usize) -> Result<()> {
    let dir = path.parent().unwrap_or(Path::new(".")).join("backups");
    std::fs::create_dir_all(&dir).map_err(|source| crate::CoreError::Io {
        path: dir.display().to_string(),
        source,
    })?;
    let file = dir.join(format!(
        "user-before-v{}-{}.db",
        from + 1,
        crate::srs::now()
    ));
    conn.execute("VACUUM INTO ?1", [file.to_string_lossy()])?;
    // Keep only the newest few.
    let mut old: Vec<_> = std::fs::read_dir(&dir)
        .map(|it| {
            it.filter_map(|e| e.ok().map(|e| e.path()))
                .filter(|p| {
                    p.file_name()
                        .and_then(|n| n.to_str())
                        .is_some_and(|n| n.starts_with("user-before-v"))
                })
                .collect()
        })
        .unwrap_or_default();
    old.sort_by_key(|p| std::fs::metadata(p).and_then(|m| m.modified()).ok());
    while old.len() > KEEP_MIGRATION_BACKUPS {
        std::fs::remove_file(old.remove(0)).ok();
    }
    Ok(())
}

/// In-memory databases, for tests.
pub fn open_in_memory() -> Result<(Connection, Connection)> {
    let mut content = Connection::open_in_memory()?;
    migrate(&mut content, CONTENT_MIGRATIONS)?;
    let mut user = Connection::open_in_memory()?;
    migrate(&mut user, USER_MIGRATIONS)?;
    Ok((content, user))
}
