//! Read source content (`content/` folder: YAML + Markdown) and write it into a content
//! database. Shared by:
//! - the packer (`tools/packer`), which writes one topic per pack database, and
//! - the developer path (`FEB_CONTENT_DIR`), which imports a whole folder directly.

use crate::localize::pick;
use crate::model::{CaItem, RawQuestion, SubjectFile, TopicFile, TopicMeta, UnitFile};
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

/// One `## Heading {#anchor}` section of a notes file.
#[derive(Debug, Clone)]
pub struct Section {
    pub anchor: String,
    pub heading: String,
    pub body: String,
}

#[derive(Debug, Clone)]
pub struct TopicSource {
    pub topic: TopicFile,
    /// (lang, sections) for every `notes.<lang>.md`, sorted by lang.
    pub notes: Vec<(String, Vec<Section>)>,
    pub questions: Vec<RawQuestion>,
    /// Current-affairs months only (`items.yaml`).
    pub ca_items: Vec<CaItem>,
}

#[derive(Debug, Clone)]
pub struct UnitSource {
    pub unit: UnitFile,
    pub topics: Vec<TopicSource>,
}

#[derive(Debug, Clone)]
pub struct SubjectSource {
    pub subject: SubjectFile,
    pub units: Vec<UnitSource>,
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

fn entries(dir: &Path) -> Result<Vec<PathBuf>> {
    let mut v: Vec<PathBuf> = fs::read_dir(dir)
        .map_err(|source| CoreError::Io {
            path: dir.display().to_string(),
            source,
        })?
        .filter_map(|e| e.ok().map(|e| e.path()))
        .collect();
    v.sort();
    Ok(v)
}

fn subdirs(dir: &Path) -> Result<Vec<PathBuf>> {
    Ok(entries(dir)?.into_iter().filter(|p| p.is_dir()).collect())
}

fn load_topic(dir: &Path) -> Result<TopicSource> {
    let topic: TopicFile = yaml(&dir.join("topic.yaml"))?;
    let mut notes = Vec::new();
    for path in entries(dir)? {
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
        let sections: Vec<Section> = parse_sections(&read(&path)?)
            .into_iter()
            .map(|(anchor, heading, body)| Section {
                anchor,
                heading,
                body,
            })
            .collect();
        notes.push((lang.to_string(), sections));
    }
    let qfile = dir.join("questions.yaml");
    let questions = if qfile.exists() {
        yaml(&qfile)?
    } else {
        Vec::new()
    };
    let ifile = dir.join("items.yaml");
    let ca_items: Vec<CaItem> = if ifile.exists() {
        yaml(&ifile)?
    } else {
        Vec::new()
    };
    // Current-affairs items also become note sections (one per item, after any intro
    // notes), so the notes reader, search and "Revise in notes" links work unchanged.
    if !ca_items.is_empty() {
        let mut langs: Vec<String> = ca_items
            .iter()
            .flat_map(|i| i.title.keys().cloned())
            .collect();
        langs.sort();
        langs.dedup();
        for lang in langs {
            let generated: Vec<Section> = ca_items
                .iter()
                .map(|i| Section {
                    anchor: i.id.clone(),
                    heading: pick(&i.title, &lang),
                    body: ca_markdown(i, &lang),
                })
                .collect();
            match notes.iter_mut().find(|(l, _)| *l == lang) {
                Some((_, list)) => list.extend(generated),
                None => notes.push((lang, generated)),
            }
        }
        notes.sort_by(|a, b| a.0.cmp(&b.0));
    }
    Ok(TopicSource {
        topic,
        notes,
        questions,
        ca_items,
    })
}

fn host(url: &str) -> &str {
    url.split("://")
        .nth(1)
        .unwrap_or(url)
        .split('/')
        .next()
        .unwrap_or(url)
        .trim_start_matches("www.")
}

/// Markdown for a current-affairs item shown as a note section.
fn ca_markdown(item: &CaItem, lang: &str) -> String {
    let mut s = pick(&item.body, lang);
    if !item.key_points.is_empty() {
        s.push_str("\n\n:::keyfacts\n");
        for p in &item.key_points {
            s.push_str(&format!("- {}\n", pick(p, lang)));
        }
        s.push_str(":::");
    }
    s.push_str(&format!(
        "\n\n:::asof {}\nSource: [{}]({})\n:::",
        item.as_of,
        host(&item.source),
        item.source
    ));
    s
}

/// Parse the whole `content/` folder (`content/subjects/<subject>/<unit>/<topic>/`).
pub fn load_dir(root: &Path) -> Result<Vec<SubjectSource>> {
    let mut subjects = Vec::new();
    // Subjects, then current affairs (a subject whose units are years and topics months).
    let mut subject_dirs = Vec::new();
    if root.join("subjects").is_dir() {
        subject_dirs.extend(subdirs(&root.join("subjects"))?);
    }
    if root.join("current-affairs/subject.yaml").exists() {
        subject_dirs.push(root.join("current-affairs"));
    }
    for sdir in subject_dirs {
        let sfile = sdir.join("subject.yaml");
        if !sfile.exists() {
            continue;
        }
        let subject: SubjectFile = yaml(&sfile)?;
        let mut units = Vec::new();
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
            let mut topics = Vec::new();
            for tdir in subdirs(&udir)? {
                if tdir.join("topic.yaml").exists() {
                    topics.push(load_topic(&tdir)?);
                }
            }
            units.push(UnitSource { unit, topics });
        }
        subjects.push(SubjectSource { subject, units });
    }
    Ok(subjects)
}

/// Parse `content/exams/*.yaml` (exam patterns for mock tests).
pub fn load_exams(root: &Path) -> Result<Vec<crate::mock::ExamPattern>> {
    let dir = root.join("exams");
    if !dir.exists() {
        return Ok(Vec::new());
    }
    let mut out = Vec::new();
    for path in entries(&dir)? {
        if path.extension().is_some_and(|e| e == "yaml" || e == "yml") {
            out.push(yaml(&path)?);
        }
    }
    Ok(out)
}

/// Insert or replace a subject row.
pub fn write_subject(conn: &Connection, s: &SubjectFile) -> Result<()> {
    conn.execute(
        "INSERT OR REPLACE INTO subjects (id, ord, title) VALUES (?1, ?2, ?3)",
        params![s.id, s.order, serde_json::to_string(&s.title)?],
    )?;
    Ok(())
}

/// Insert or replace a unit row.
pub fn write_unit(conn: &Connection, u: &UnitFile) -> Result<()> {
    conn.execute(
        "INSERT OR REPLACE INTO units (id, subject_id, ord, title) VALUES (?1, ?2, ?3, ?4)",
        params![u.id, u.subject, u.order, serde_json::to_string(&u.title)?],
    )?;
    Ok(())
}

/// Replace one topic (row, note sections, questions). Returns (sections, questions) written.
pub fn write_topic(conn: &Connection, unit: &UnitFile, t: &TopicSource) -> Result<(usize, usize)> {
    let topic = &t.topic;
    let id = &topic.id;
    conn.execute("DELETE FROM note_sections WHERE topic_id = ?1", [id])?;
    conn.execute("DELETE FROM questions WHERE topic_id = ?1", [id])?;
    let meta = TopicMeta {
        exams: topic.exams.clone(),
        estimated_minutes: topic.estimated_minutes,
        version: topic.version.clone(),
        status: topic.status.clone(),
        sources: topic.sources.clone(),
    };
    conn.execute(
        "INSERT OR REPLACE INTO topics (id, unit_id, subject_id, ord, title, summary, meta)
         VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7)",
        params![
            id,
            unit.id,
            unit.subject,
            topic.order,
            serde_json::to_string(&topic.title)?,
            topic
                .summary
                .as_ref()
                .map(serde_json::to_string)
                .transpose()?,
            serde_json::to_string(&meta)?,
        ],
    )?;
    let mut sections = 0;
    for (lang, list) in &t.notes {
        for (ord, s) in list.iter().enumerate() {
            conn.execute(
                "INSERT INTO note_sections (topic_id, lang, anchor, ord, heading, body_md)
                 VALUES (?1, ?2, ?3, ?4, ?5, ?6)",
                params![id, lang, s.anchor, ord as i64, s.heading, s.body],
            )?;
            sections += 1;
        }
    }
    conn.execute("DELETE FROM ca_items WHERE topic_id = ?1", [id])?;
    for (ord, i) in t.ca_items.iter().enumerate() {
        conn.execute(
            "INSERT INTO ca_items (id, topic_id, ord, date, category, title, body, key_points,
                                   related_topics, source, as_of, status)
             VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10, ?11, ?12)",
            params![
                format!("{id}/{}", i.id),
                id,
                ord as i64,
                i.date,
                i.category,
                serde_json::to_string(&i.title)?,
                serde_json::to_string(&i.body)?,
                serde_json::to_string(&i.key_points)?,
                serde_json::to_string(&i.related_topics)?,
                i.source,
                i.as_of,
                i.status
            ],
        )?;
    }
    for (ord, q) in t.questions.iter().enumerate() {
        conn.execute(
            "INSERT INTO questions (id, topic_id, ord, kind, difficulty, status, data)
             VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7)",
            params![
                format!("{id}/{}", q.id),
                id,
                ord as i64,
                q.kind,
                q.difficulty,
                q.status,
                serde_json::to_string(q)?
            ],
        )?;
    }
    Ok((sections, t.questions.len()))
}

/// Developer path: replace **all** content in `conn` with the folder at `root`
/// (no packs involved). Runs in one transaction; on error the old content stays.
pub fn import_dir(conn: &mut Connection, root: &Path) -> Result<ImportReport> {
    let subjects = load_dir(root)?;
    let exams = load_exams(root)?;
    let mut report = ImportReport::default();
    let tx = conn.transaction()?;
    tx.execute_batch(
        "DELETE FROM subjects; DELETE FROM units; DELETE FROM topics;
         DELETE FROM note_sections; DELETE FROM questions; DELETE FROM installed_packs;
         DELETE FROM ca_items;",
    )?;
    crate::mock::store_patterns(&tx, &exams)?;
    for s in &subjects {
        write_subject(&tx, &s.subject)?;
        report.subjects += 1;
        for u in &s.units {
            write_unit(&tx, &u.unit)?;
            report.units += 1;
            for t in &u.topics {
                let (sec, q) = write_topic(&tx, &u.unit, t)?;
                report.topics += 1;
                report.sections += sec;
                report.questions += q;
            }
        }
    }
    crate::search::rebuild(&tx)?;
    tx.commit()?;
    Ok(report)
}
