//! Export, import (restore) and reset of the user's progress (`user.db`):
//! answers, tests, review cards and settings (docs/PRIVACY_AND_SECURITY.md §4).
//! Content is not included; it comes from packs.

use crate::{CoreError, Result, db};
use rusqlite::{Connection, OpenFlags};
use serde::Serialize;
use std::path::Path;

/// Tables copied by export/import, in dependency-free order.
const TABLES: &[&str] = &["settings", "attempts", "tests", "srs_cards"];

fn path_str(p: &Path) -> Result<String> {
    p.to_str()
        .map(str::to_string)
        .ok_or_else(|| CoreError::Invalid(format!("unsupported path: {}", p.display())))
}

fn io(path: &Path, source: std::io::Error) -> CoreError {
    CoreError::Io {
        path: path.display().to_string(),
        source,
    }
}

/// Write a consistent copy of the progress database to `path` (overwrites).
pub fn export(user: &Connection, path: &Path) -> Result<()> {
    if path.exists() {
        std::fs::remove_file(path).map_err(|e| io(path, e))?;
    }
    user.execute("VACUUM INTO ?1", [path_str(path)?])?;
    Ok(())
}

#[derive(Debug, Clone, Serialize)]
pub struct ImportSummary {
    pub attempts: i64,
    pub tests: i64,
    pub cards: i64,
    /// Copy of the progress that was replaced (to undo by importing it again).
    pub previous_backup: String,
}

/// Replace the current progress with a backup file. The current progress is saved to
/// `backup_dir` first. Older backups are upgraded; backups from newer app versions are
/// refused.
pub fn import(user: &mut Connection, path: &Path, backup_dir: &Path) -> Result<ImportSummary> {
    // 1. Check it is a progress backup this version understands.
    {
        let src =
            Connection::open_with_flags(path, OpenFlags::SQLITE_OPEN_READ_ONLY).map_err(|_| {
                CoreError::Invalid("this file is not a Free Exercise Book backup".into())
            })?;
        let version: usize = src
            .pragma_query_value(None, "user_version", |r| r.get(0))
            .map_err(|_| {
                CoreError::Invalid("this file is not a Free Exercise Book backup".into())
            })?;
        let has_attempts: bool = src
            .query_row(
                "SELECT EXISTS (SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'attempts')",
                [],
                |r| r.get(0),
            )
            .unwrap_or(false);
        if version == 0 || !has_attempts {
            return Err(CoreError::Invalid(
                "this file is not a Free Exercise Book backup".into(),
            ));
        }
        if version > db::user_schema_version() {
            return Err(CoreError::Invalid(
                "this backup was made by a newer version of the app; please update the app first"
                    .into(),
            ));
        }
    }

    // 2. Upgrade a copy to the current schema, and save the current progress.
    std::fs::create_dir_all(backup_dir).map_err(|e| io(backup_dir, e))?;
    let stamp = crate::srs::now();
    let upgraded = backup_dir.join(format!("import-{stamp}.tmp.db"));
    std::fs::copy(path, &upgraded).map_err(|e| io(path, e))?;
    drop(db::open_user(&upgraded)?);
    let previous = backup_dir.join(format!("progress-before-import-{stamp}.db"));
    export(user, &previous)?;

    // 3. Replace all progress tables in one transaction.
    user.execute("ATTACH DATABASE ?1 AS imp", [path_str(&upgraded)?])?;
    let result = (|| -> Result<ImportSummary> {
        let tx = user.transaction()?;
        for t in TABLES {
            tx.execute_batch(&format!(
                "DELETE FROM main.{t}; INSERT INTO main.{t} SELECT * FROM imp.{t};"
            ))?;
        }
        let count = |t: &str| {
            tx.query_row(&format!("SELECT COUNT(*) FROM main.{t}"), [], |r| {
                r.get::<_, i64>(0)
            })
        };
        let summary = ImportSummary {
            attempts: count("attempts")?,
            tests: count("tests")?,
            cards: count("srs_cards")?,
            previous_backup: previous.display().to_string(),
        };
        tx.commit()?;
        Ok(summary)
    })();
    user.execute("DETACH DATABASE imp", [])?;
    std::fs::remove_file(&upgraded).ok();
    result
}

/// Delete answers, tests and review cards. Settings are kept.
pub fn reset(user: &mut Connection) -> Result<()> {
    let tx = user.transaction()?;
    tx.execute_batch("DELETE FROM attempts; DELETE FROM tests; DELETE FROM srs_cards;")?;
    tx.commit()?;
    Ok(())
}
