//! Import source content (`content/` folder: YAML + Markdown) into `content.db`.
//!
//! This is the development path. Release builds will install signed packs
//! (docs/DATA_AND_PACKS.md); the packer reuses this same parsing code.

use crate::model::{RawQuestion, SubjectFile, TopicFile, TopicMeta, UnitFile};
use crate::{CoreError, Result};
use regex::Regex;
use rusqlite::{Connection, params};
use serde::Serialize;
use serde::de::DeserializeOwned;
use std::fs;
use std::path::{Path, PathBuf};
use std::sync::LazyLock;

#[derive(Debug, Default, Serialize)]
pub struct ImportReport {
    pub subjects: usize,
    pub units: usize,
    pub topics: usize,
    pub sections: usize,
    pub questions: usize,
}

static H2: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"^##\s+(.+?)\s*\{#([a-z0-9-]+)\}\s*$").unwrap());

/// Split a notes file into `## Heading {#anchor}` sections. Text before the first H2
/// (the `#` title) is ignored. Fenced code blocks are respected.
pub fn parse_sections(md: &str) -> Vec<(String, String, String)> {
    let mut out: Vec<(String, String, String)> = Vec::new();
    let mut in_fence = false;
    for line in md.lines() {
        if line.trim_start().starts_with("```") {
            in_fence = !in_fence;
        }
        if !in_fence && let Some(c) = H2.captures(line) {
            out.push((c[2].to_string(), c[1].to_string(), String::new()));
            continue;
        }
        if let Some(last) = out.last_mut() {
            last.2.push_str(line);
            last.2.push('\n');
        }
    }
    for s in &mut out {
        s.2 = s.2.trim().to_string();
    }
    out
}

fn read(path: &Path) -> Result<String> {
    fs::read_to_string(path).map_err(|source| CoreError::Io {
        path: path.display().to_string(),
        source,
    })
}

fn yaml<T: DeserializeOwned>(path: &Path) -> Result<T> {
    serde_yaml::from_str(&read(path)?).map_err(|e| CoreError::Content {
        path: path.display().to_string(),
        message: e.to_string(),
    })
}

fn subdirs(dir: &Path) -> Result<Vec<PathBuf>> {
    let mut v: Vec<PathBuf> = fs::read_dir(dir)
        .map_err(|source| CoreError::Io {
            path: dir.display().to_string(),
            source,
        })?
        .filter_map(|e| e.ok().map(|e| e.path()))
        .filter(|p| p.is_dir())
        .collect();
    v.sort();
    Ok(v)
}

/// Replace all content in `conn` with the content found under `root` (the `content/` dir).
/// Runs in one transaction: on any error the previous content stays intact.
pub fn import_dir(conn: &mut Connection, root: &Path) -> Result<ImportReport> {
    let mut report = ImportReport::default();
    let tx = conn.transaction()?;
    tx.execute_batch("DELETE FROM subjects; DELETE FROM units; DELETE FROM topics; DELETE FROM note_sections; DELETE FROM questions;")?;

    for sdir in subdirs(&root.join("subjects"))? {
        let sfile = sdir.join("subject.yaml");
        if !sfile.exists() {
            continue;
        }
        let subject: SubjectFile = yaml(&sfile)?;
        tx.execute(
            "INSERT INTO subjects (id, ord, title) VALUES (?1, ?2, ?3)",
            params![
                subject.id,
                subject.order,
                serde_json::to_string(&subject.title)?
            ],
        )?;
        report.subjects += 1;

        for udir in subdirs(&sdir)? {
            let ufile = udir.join("unit.yaml");
            if !ufile.exists() {
                continue;
            }
            let unit: UnitFile = yaml(&ufile)?;
            if unit.subject != subject.id {
                return Err(CoreError::Content {
                    path: ufile.display().to_string(),
                    message: format!(
                        "unit.subject '{}' != subject id '{}'",
                        unit.subject, subject.id
                    ),
                });
            }
            tx.execute(
                "INSERT INTO units (id, subject_id, ord, title) VALUES (?1, ?2, ?3, ?4)",
                params![
                    unit.id,
                    subject.id,
                    unit.order,
                    serde_json::to_string(&unit.title)?
                ],
            )?;
            report.units += 1;

            for tdir in subdirs(&udir)? {
                let tfile = tdir.join("topic.yaml");
                if !tfile.exists() {
                    continue;
                }
                let topic: TopicFile = yaml(&tfile)?;
                let meta = TopicMeta {
                    exams: topic.exams.clone(),
                    estimated_minutes: topic.estimated_minutes,
                    version: topic.version.clone(),
                    status: topic.status.clone(),
                    sources: topic.sources.clone(),
                };
                tx.execute(
                    "INSERT INTO topics (id, unit_id, subject_id, ord, title, summary, meta) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7)",
                    params![
                        topic.id,
                        unit.id,
                        subject.id,
                        topic.order,
                        serde_json::to_string(&topic.title)?,
                        topic.summary.as_ref().map(serde_json::to_string).transpose()?,
                        serde_json::to_string(&meta)?,
                    ],
                )?;
                report.topics += 1;

                // notes.<lang>.md
                let mut entries: Vec<PathBuf> = fs::read_dir(&tdir)
                    .map_err(|source| CoreError::Io {
                        path: tdir.display().to_string(),
                        source,
                    })?
                    .filter_map(|e| e.ok().map(|e| e.path()))
                    .collect();
                entries.sort();
                for path in entries {
                    let name = path
                        .file_name()
                        .and_then(|n| n.to_str())
                        .unwrap_or_default();
                    let Some(lang) = name
                        .strip_prefix("notes.")
                        .and_then(|r| r.strip_suffix(".md"))
                    else {
                        continue;
                    };
                    for (ord, (anchor, heading, body)) in
                        parse_sections(&read(&path)?).into_iter().enumerate()
                    {
                        tx.execute(
                            "INSERT INTO note_sections (topic_id, lang, anchor, ord, heading, body_md) VALUES (?1, ?2, ?3, ?4, ?5, ?6)",
                            params![topic.id, lang, anchor, ord as i64, heading, body],
                        )?;
                        report.sections += 1;
                    }
                }

                // questions.yaml
                let qfile = tdir.join("questions.yaml");
                if qfile.exists() {
                    let qs: Vec<RawQuestion> = yaml(&qfile)?;
                    for (ord, q) in qs.iter().enumerate() {
                        let full_id = format!("{}/{}", topic.id, q.id);
                        tx.execute(
                            "INSERT INTO questions (id, topic_id, ord, kind, difficulty, status, data) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7)",
                            params![full_id, topic.id, ord as i64, q.kind, q.difficulty, q.status, serde_json::to_string(q)?],
                        )?;
                        report.questions += 1;
                    }
                }
            }
        }
    }
    tx.commit()?;
    Ok(report)
}
