use crate::localize::{Localized, pick};
use crate::model::{LibrarySubject, LibraryUnit, NoteSection, TopicMeta, TopicSummary, TopicView};
use crate::practice::latest_results_by_topic;
use crate::{CoreError, Result};
use rusqlite::{Connection, OptionalExtension, params};

fn loc(json: &str, lang: &str) -> Result<String> {
    let m: Localized = serde_json::from_str(json)?;
    Ok(pick(&m, lang))
}

/// Subjects → units → topics, with per-topic progress.
pub fn tree(content: &Connection, user: &Connection, lang: &str) -> Result<Vec<LibrarySubject>> {
    let progress = latest_results_by_topic(user)?;

    let mut subjects: Vec<LibrarySubject> = Vec::new();
    let mut stmt = content.prepare("SELECT id, title FROM subjects ORDER BY ord")?;
    let rows: Vec<(String, String)> = stmt
        .query_map([], |r| Ok((r.get(0)?, r.get(1)?)))?
        .collect::<Result<_, _>>()?;
    for (sid, stitle) in rows {
        let mut units = Vec::new();
        let mut ustmt =
            content.prepare("SELECT id, title FROM units WHERE subject_id = ?1 ORDER BY ord")?;
        let urows: Vec<(String, String)> = ustmt
            .query_map([&sid], |r| Ok((r.get(0)?, r.get(1)?)))?
            .collect::<Result<_, _>>()?;
        for (uid, utitle) in urows {
            let mut tstmt = content.prepare(
                "SELECT t.id, t.title, t.summary, t.meta, (SELECT COUNT(*) FROM questions q WHERE q.topic_id = t.id)
                 FROM topics t WHERE t.unit_id = ?1 ORDER BY t.ord",
            )?;
            let trows: Vec<(String, String, Option<String>, String, i64)> = tstmt
                .query_map([&uid], |r| {
                    Ok((r.get(0)?, r.get(1)?, r.get(2)?, r.get(3)?, r.get(4)?))
                })?
                .collect::<Result<_, _>>()?;
            let mut topics = Vec::new();
            for (tid, ttitle, tsummary, tmeta, qcount) in trows {
                let meta: TopicMeta = serde_json::from_str(&tmeta)?;
                let (attempted, correct) = progress.get(&tid).copied().unwrap_or((0, 0));
                topics.push(TopicSummary {
                    title: loc(&ttitle, lang)?,
                    summary: tsummary.map(|s| loc(&s, lang)).transpose()?,
                    status: meta.status,
                    estimated_minutes: meta.estimated_minutes,
                    question_count: qcount,
                    attempted,
                    correct,
                    id: tid,
                });
            }
            units.push(LibraryUnit {
                id: uid,
                title: loc(&utitle, lang)?,
                topics,
            });
        }
        subjects.push(LibrarySubject {
            id: sid,
            title: loc(&stitle, lang)?,
            units,
        });
    }
    Ok(subjects)
}

/// A topic with its notes in `lang` (falls back to English when the notes are missing).
pub fn topic(content: &Connection, id: &str, lang: &str) -> Result<TopicView> {
    struct Row {
        title: String,
        summary: Option<String>,
        meta: String,
        sid: String,
        stitle: String,
        uid: String,
        utitle: String,
    }
    let row = content
        .query_row(
            "SELECT t.title, t.summary, t.meta, s.id, s.title, u.id, u.title
             FROM topics t JOIN subjects s ON s.id = t.subject_id JOIN units u ON u.id = t.unit_id
             WHERE t.id = ?1",
            [id],
            |r| {
                Ok(Row {
                    title: r.get(0)?,
                    summary: r.get(1)?,
                    meta: r.get(2)?,
                    sid: r.get(3)?,
                    stitle: r.get(4)?,
                    uid: r.get(5)?,
                    utitle: r.get(6)?,
                })
            },
        )
        .optional()?;
    let Some(Row {
        title,
        summary,
        meta,
        sid,
        stitle,
        uid,
        utitle,
    }) = row
    else {
        return Err(CoreError::NotFound(format!("topic {id}")));
    };

    let mut lstmt = content
        .prepare("SELECT DISTINCT lang FROM note_sections WHERE topic_id = ?1 ORDER BY lang")?;
    let available_langs: Vec<String> = lstmt
        .query_map([id], |r| r.get(0))?
        .collect::<Result<_, _>>()?;
    let notes_lang = if available_langs.iter().any(|l| l == lang) {
        lang
    } else {
        "en"
    };

    let mut sstmt = content
        .prepare("SELECT anchor, heading, body_md FROM note_sections WHERE topic_id = ?1 AND lang = ?2 ORDER BY ord")?;
    let sections = sstmt
        .query_map(params![id, notes_lang], |r| {
            Ok(NoteSection {
                anchor: r.get(0)?,
                heading: r.get(1)?,
                body_md: r.get(2)?,
            })
        })?
        .collect::<Result<Vec<_>, _>>()?;

    let question_count: i64 = content.query_row(
        "SELECT COUNT(*) FROM questions WHERE topic_id = ?1",
        [id],
        |r| r.get(0),
    )?;

    Ok(TopicView {
        id: id.to_string(),
        title: loc(&title, lang)?,
        summary: summary.map(|s| loc(&s, lang)).transpose()?,
        subject_id: sid,
        subject_title: loc(&stitle, lang)?,
        unit_id: uid,
        unit_title: loc(&utitle, lang)?,
        lang: notes_lang.to_string(),
        available_langs,
        sections,
        meta: serde_json::from_str(&meta)?,
        question_count,
    })
}
