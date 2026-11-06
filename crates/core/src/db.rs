//! Connection setup and migrations. Migrations are append-only (docs/CODING_GUIDELINES.md §2).

use crate::Result;
use rusqlite::Connection;
use std::path::Path;

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

pub fn open_user(path: &Path) -> Result<Connection> {
    let mut conn = Connection::open(path)?;
    configure(&conn)?;
    migrate(&mut conn, USER_MIGRATIONS)?;
    Ok(conn)
}

/// In-memory databases, for tests.
pub fn open_in_memory() -> Result<(Connection, Connection)> {
    let mut content = Connection::open_in_memory()?;
    migrate(&mut content, CONTENT_MIGRATIONS)?;
    let mut user = Connection::open_in_memory()?;
    migrate(&mut user, USER_MIGRATIONS)?;
    Ok((content, user))
}
