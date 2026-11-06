//! Current affairs: monthly packs (`ca.<yyyy>.<mm>`) with structured news items.
//! Months are ordinary topics of the subject `ca`, so practice, tests, search, revision
//! and progress work for them unchanged; this module adds the month list and item view.

use crate::Result;
use crate::localize::{Localized, pick};
use crate::practice::latest_results_by_topic;
use rusqlite::{Connection, params};
use serde::Serialize;

pub const SUBJECT: &str = "ca";

#[derive(Debug, Clone, Serialize)]
pub struct MonthSummary {
    pub topic_id: String,
    pub title: String,
    pub items: i64,
    pub questions: i64,
    pub attempted: i64,
    pub correct: i64,
    /// Categories present this month (sorted).
    pub categories: Vec<String>,
}

#[derive(Debug, Clone, Serialize)]
pub struct RelatedTopic {
    pub id: String,
    /// None when the topic isn't installed.
    pub title: Option<String>,
}

#[derive(Debug, Clone, Serialize)]
pub struct ItemView {
    pub id: String,
    /// Note section anchor (the item id within the month).
    pub anchor: String,
    pub date: String,
    pub category: String,
    pub title: String,
    pub body: String,
    pub key_points: Vec<String>,
    pub related: Vec<RelatedTopic>,
    pub source: String,
    pub as_of: String,
    pub status: String,
    /// Language the item is shown in (falls back to English per field).
    pub lang: String,
}

#[derive(Debug, Clone, Serialize)]
pub struct MonthView {
    pub topic_id: String,
    pub title: String,
    pub items: Vec<ItemView>,
    pub questions: i64,
}

fn title_of(content: &Connection, topic_id: &str, lang: &str) -> Option<String> {
    content
        .query_row("SELECT title FROM topics WHERE id = ?1", [topic_id], |r| {
            r.get::<_, String>(0)
        })
        .ok()
        .and_then(|j| serde_json::from_str::<Localized>(&j).ok())
        .map(|m| pick(&m, lang))
}

/// Installed months, newest first.
pub fn months(content: &Connection, user: &Connection, lang: &str) -> Result<Vec<MonthSummary>> {
    let progress = latest_results_by_topic(user)?;
    let mut stmt = content.prepare(
        "SELECT t.id, t.title,
                (SELECT COUNT(*) FROM ca_items c WHERE c.topic_id = t.id),
                (SELECT COUNT(*) FROM questions q WHERE q.topic_id = t.id),
                (SELECT group_concat(DISTINCT category) FROM ca_items c WHERE c.topic_id = t.id)
         FROM topics t WHERE t.subject_id = ?1 ORDER BY t.id DESC",
    )?;
    let rows: Vec<(String, String, i64, i64, Option<String>)> = stmt
        .query_map([SUBJECT], |r| {
            Ok((r.get(0)?, r.get(1)?, r.get(2)?, r.get(3)?, r.get(4)?))
        })?
        .collect::<Result<_, _>>()?;
    let mut out = Vec::new();
    for (id, title, items, questions, cats) in rows {
        let (attempted, correct) = progress.get(&id).copied().unwrap_or((0, 0));
        let mut categories: Vec<String> = cats
            .unwrap_or_default()
            .split(',')
            .filter(|c| !c.is_empty())
            .map(String::from)
            .collect();
        categories.sort();
        out.push(MonthSummary {
            title: pick(&serde_json::from_str::<Localized>(&title)?, lang),
            topic_id: id,
            items,
            questions,
            attempted,
            correct,
            categories,
        });
    }
    Ok(out)
}

/// One month's items, newest first.
pub fn month(content: &Connection, topic_id: &str, lang: &str) -> Result<MonthView> {
    let title = title_of(content, topic_id, lang)
        .ok_or_else(|| crate::CoreError::NotFound(format!("current-affairs month {topic_id}")))?;
    let mut stmt = content.prepare(
        "SELECT id, date, category, title, body, key_points, related_topics, source, as_of, status
         FROM ca_items WHERE topic_id = ?1 ORDER BY date DESC, ord",
    )?;
    type Row = (
        String,
        String,
        String,
        String,
        String,
        String,
        String,
        String,
        String,
        String,
    );
    let rows: Vec<Row> = stmt
        .query_map(params![topic_id], |r| {
            Ok((
                r.get(0)?,
                r.get(1)?,
                r.get(2)?,
                r.get(3)?,
                r.get(4)?,
                r.get(5)?,
                r.get(6)?,
                r.get(7)?,
                r.get(8)?,
                r.get(9)?,
            ))
        })?
        .collect::<Result<_, _>>()?;
    let mut items = Vec::new();
    for (id, date, category, t, b, kp, rel, source, as_of, status) in rows {
        let t: Localized = serde_json::from_str(&t)?;
        let b: Localized = serde_json::from_str(&b)?;
        let kp: Vec<Localized> = serde_json::from_str(&kp)?;
        let rel: Vec<String> = serde_json::from_str(&rel)?;
        let shown = if t.contains_key(lang) && b.contains_key(lang) {
            lang
        } else {
            "en"
        };
        items.push(ItemView {
            anchor: id.rsplit('/').next().unwrap_or(&id).to_string(),
            id,
            date,
            category,
            title: pick(&t, shown),
            body: pick(&b, shown),
            key_points: kp.iter().map(|p| pick(p, shown)).collect(),
            related: rel
                .into_iter()
                .map(|r| RelatedTopic {
                    title: title_of(content, &r, lang),
                    id: r,
                })
                .collect(),
            source,
            as_of,
            status,
            lang: shown.to_string(),
        });
    }
    let questions: i64 = content.query_row(
        "SELECT COUNT(*) FROM questions WHERE topic_id = ?1",
        [topic_id],
        |r| r.get(0),
    )?;
    Ok(MonthView {
        topic_id: topic_id.to_string(),
        title,
        items,
        questions,
    })
}
