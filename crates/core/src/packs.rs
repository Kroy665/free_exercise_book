//! Content packs inside the databases (docs/DATA_AND_PACKS.md §2, §5).
//!
//! A pack holds exactly one topic (plus its subject and unit rows). This module only
//! deals with SQLite: building a pack database and installing/removing one in
//! `content.db`. Downloading, signatures and compression live in the `feb-packs` crate.

use crate::db::{self, PACK_FORMAT};
use crate::import::{
    SubjectSource, TopicSource, UnitSource, write_subject, write_topic, write_unit,
};
use crate::{CoreError, Result};
use rusqlite::{Connection, OptionalExtension, params};
use serde::Serialize;
use std::path::Path;

#[derive(Debug, Clone, Serialize)]
pub struct InstalledPack {
    pub id: String,
    pub version: String,
    pub sha256: String,
    pub size: i64,
    pub installed_at: i64,
}

#[derive(Debug, Clone, Copy, Default, Serialize)]
pub struct PackCounts {
    pub sections: usize,
    pub questions: usize,
}

/// Write a pack database for one topic at `path`. Deterministic for the same input.
pub fn build_pack_db(
    path: &Path,
    subject: &SubjectSource,
    unit: &UnitSource,
    topic: &TopicSource,
) -> Result<PackCounts> {
    let mut conn = db::create_pack(path)?;
    let tx = conn.transaction()?;
    for (k, v) in [
        ("format", PACK_FORMAT.to_string()),
        ("id", topic.topic.id.clone()),
        ("version", topic.topic.version.clone()),
    ] {
        tx.execute(
            "INSERT INTO pack_meta (key, value) VALUES (?1, ?2)",
            params![k, v],
        )?;
    }
    write_subject(&tx, &subject.subject)?;
    write_unit(&tx, &unit.unit)?;
    let (sections, questions) = write_topic(&tx, &unit.unit, topic)?;
    tx.commit()?;
    conn.execute_batch("VACUUM;")?;
    Ok(PackCounts {
        sections,
        questions,
    })
}

fn meta(conn: &Connection, key: &str) -> Result<String> {
    conn.query_row(
        "SELECT value FROM pack.pack_meta WHERE key = ?1",
        [key],
        |r| r.get(0),
    )
    .optional()?
    .ok_or_else(|| CoreError::Invalid(format!("pack is missing pack_meta.{key}")))
}

/// Install (or update) a pack from an uncompressed pack database file.
///
/// `expected_id` / `expected_version` come from the signed manifest and must match the
/// pack's own metadata. Everything happens in one transaction: on error, the previously
/// installed version stays intact. User data (`user.db`) is never touched.
pub fn install_pack_db(
    conn: &mut Connection,
    pack_path: &Path,
    expected_id: &str,
    expected_version: &str,
    sha256: &str,
    size: i64,
) -> Result<InstalledPack> {
    conn.execute("ATTACH DATABASE ?1 AS pack", [pack_path.to_string_lossy()])?;
    let result = (|| -> Result<InstalledPack> {
        let format: u32 = meta(conn, "format")?
            .parse()
            .map_err(|_| CoreError::Invalid("bad pack format".into()))?;
        if format != PACK_FORMAT {
            return Err(CoreError::Invalid(format!(
                "pack format {format} is not supported by this app (expects {PACK_FORMAT}); please update the app"
            )));
        }
        let id = meta(conn, "id")?;
        let version = meta(conn, "version")?;
        if id != expected_id || version != expected_version {
            return Err(CoreError::Invalid(format!(
                "pack contents ({id}@{version}) do not match the manifest ({expected_id}@{expected_version})"
            )));
        }
        let topic_count: i64 = conn.query_row(
            "SELECT COUNT(*) FROM pack.topics WHERE id = ?1",
            [&id],
            |r| r.get(0),
        )?;
        if topic_count != 1 {
            return Err(CoreError::Invalid(format!(
                "pack {id} does not contain its topic"
            )));
        }

        let tx = conn.transaction()?;
        tx.execute("DELETE FROM note_sections WHERE topic_id = ?1", [&id])?;
        tx.execute("DELETE FROM questions WHERE topic_id = ?1", [&id])?;
        tx.execute("DELETE FROM ca_items WHERE topic_id = ?1", [&id])?;
        tx.execute_batch(
            "INSERT OR REPLACE INTO subjects SELECT * FROM pack.subjects;
             INSERT OR REPLACE INTO units SELECT * FROM pack.units;
             INSERT OR REPLACE INTO topics SELECT * FROM pack.topics;
             INSERT INTO note_sections SELECT * FROM pack.note_sections;
             INSERT INTO questions SELECT * FROM pack.questions;",
        )?;
        let has_ca: bool = tx.query_row(
            "SELECT EXISTS (SELECT 1 FROM pack.sqlite_master WHERE type = 'table' AND name = 'ca_items')",
            [],
            |r| r.get(0),
        )?;
        if has_ca {
            tx.execute_batch("INSERT INTO ca_items SELECT * FROM pack.ca_items;")?;
        }
        tx.execute(
            "INSERT OR REPLACE INTO installed_packs (id, version, sha256, size) VALUES (?1, ?2, ?3, ?4)",
            params![id, version, sha256, size],
        )?;
        crate::search::index_topic(&tx, &id)?;
        tx.commit()?;
        Ok(installed(conn, &id)?.expect("just installed"))
    })();
    conn.execute("DETACH DATABASE pack", [])?;
    result
}

/// Remove a pack's topic. Subjects/units left without topics are removed too.
/// The user's attempts and progress for its questions are kept in `user.db`.
pub fn remove_pack(conn: &mut Connection, id: &str) -> Result<()> {
    let tx = conn.transaction()?;
    tx.execute("DELETE FROM note_sections WHERE topic_id = ?1", [id])?;
    tx.execute("DELETE FROM questions WHERE topic_id = ?1", [id])?;
    tx.execute("DELETE FROM ca_items WHERE topic_id = ?1", [id])?;
    tx.execute("DELETE FROM topics WHERE id = ?1", [id])?;
    tx.execute("DELETE FROM installed_packs WHERE id = ?1", [id])?;
    crate::search::remove_topic(&tx, id)?;
    tx.execute_batch(
        "DELETE FROM units WHERE id NOT IN (SELECT DISTINCT unit_id FROM topics);
         DELETE FROM subjects WHERE id NOT IN (SELECT DISTINCT subject_id FROM topics);",
    )?;
    tx.commit()?;
    Ok(())
}

pub fn installed(conn: &Connection, id: &str) -> Result<Option<InstalledPack>> {
    Ok(conn
        .query_row(
            "SELECT id, version, sha256, size, installed_at FROM installed_packs WHERE id = ?1",
            [id],
            row,
        )
        .optional()?)
}

pub fn list_installed(conn: &Connection) -> Result<Vec<InstalledPack>> {
    let mut stmt = conn.prepare(
        "SELECT id, version, sha256, size, installed_at FROM installed_packs ORDER BY id",
    )?;
    Ok(stmt.query_map([], row)?.collect::<Result<_, _>>()?)
}

/// True when the content database has topics that did not come from packs
/// (developer import via `FEB_CONTENT_DIR`).
pub fn has_dev_content(conn: &Connection) -> Result<bool> {
    Ok(conn.query_row(
        "SELECT EXISTS (SELECT 1 FROM topics WHERE id NOT IN (SELECT id FROM installed_packs))",
        [],
        |r| r.get(0),
    )?)
}

/// Remove content that did not come from a pack (left over from a developer import or
/// from v0.1.0, which bundled raw content). Returns the number of topics removed.
pub fn purge_unmanaged(conn: &mut Connection) -> Result<usize> {
    let tx = conn.transaction()?;
    let ids: Vec<String> = {
        let mut stmt =
            tx.prepare("SELECT id FROM topics WHERE id NOT IN (SELECT id FROM installed_packs)")?;
        stmt.query_map([], |r| r.get(0))?
            .collect::<Result<_, _>>()?
    };
    for id in &ids {
        tx.execute("DELETE FROM note_sections WHERE topic_id = ?1", [id])?;
        tx.execute("DELETE FROM questions WHERE topic_id = ?1", [id])?;
        tx.execute("DELETE FROM ca_items WHERE topic_id = ?1", [id])?;
        tx.execute("DELETE FROM topics WHERE id = ?1", [id])?;
        crate::search::remove_topic(&tx, id)?;
    }
    tx.execute_batch(
        "DELETE FROM units WHERE id NOT IN (SELECT DISTINCT unit_id FROM topics);
         DELETE FROM subjects WHERE id NOT IN (SELECT DISTINCT subject_id FROM topics);",
    )?;
    tx.commit()?;
    Ok(ids.len())
}

fn row(r: &rusqlite::Row<'_>) -> rusqlite::Result<InstalledPack> {
    Ok(InstalledPack {
        id: r.get(0)?,
        version: r.get(1)?,
        sha256: r.get(2)?,
        size: r.get(3)?,
        installed_at: r.get(4)?,
    })
}
