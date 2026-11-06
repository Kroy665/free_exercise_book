//! Keyword search (SQLite FTS5) over topics, note sections and questions
//! (docs/SPEC.md S1, docs/DATA_AND_PACKS.md §8).
//!
//! Two indexes (content migration 4):
//! - `search_index`: whole-word index. Bengali/Devanagari vowel signs and virama count as
//!   part of a word (`tokenchars`), so "মহাবিদ্রোহের" is one word, not consonant fragments.
//!   Every query word is a prefix match, which suits Bengali inflection
//!   ("বিদ্রোহ" finds "বিদ্রোহের"). `title`/`body` keep the original text for display;
//!   `alt` holds the digit-normalised text so "1857" finds "১৮৫৭" and vice versa.
//! - `search_trigram`: substring fallback when few whole-word matches exist (Bengali
//!   compounds such as "মহাবিদ্রোহ", or partial words).
//!
//! Both are kept in sync per topic when packs are installed, updated or removed.

use crate::Result;
use crate::localize::{Localized, pick};
use crate::model::RawQuestion;
use rusqlite::{Connection, OptionalExtension, params};
use serde::Serialize;
use std::collections::{HashMap, HashSet};
use unicode_normalization::UnicodeNormalization;

/// Fewer whole-word hits than this triggers the substring (trigram) fallback.
const TRIGRAM_THRESHOLD: usize = 8;

pub fn nfc(s: &str) -> String {
    s.nfc().collect()
}

/// NFC + Bengali and Devanagari digits -> ASCII digits.
pub fn normalize(s: &str) -> String {
    s.nfc()
        .map(|c| match c {
            '০'..='৯' => char::from(b'0' + (c as u32 - '০' as u32) as u8),
            '०'..='९' => char::from(b'0' + (c as u32 - '०' as u32) as u8),
            _ => c,
        })
        .collect()
}

/// Remove Markdown and our block syntax so it doesn't pollute the index or snippets.
fn plain(md: &str) -> String {
    let mut out = String::with_capacity(md.len());
    for line in md.lines() {
        let l = line.trim_start();
        if l.starts_with(":::") || l.starts_with("|---") || l.starts_with("|:--") {
            continue;
        }
        let l = l.trim_start_matches(['#', '>', '-', '*', ' ']);
        let cleaned: String = l
            .chars()
            .map(|c| {
                if matches!(c, '*' | '_' | '`' | '|' | '[' | ']') {
                    ' '
                } else {
                    c
                }
            })
            .collect();
        out.push_str(cleaned.trim());
        out.push('\n');
    }
    out
}

fn first_line(s: &str, max: usize) -> String {
    let line = s.lines().next().unwrap_or_default().trim();
    if line.chars().count() <= max {
        line.to_string()
    } else {
        format!("{}…", line.chars().take(max).collect::<String>())
    }
}

struct Writer<'c> {
    words: rusqlite::Statement<'c>,
    trigram: rusqlite::Statement<'c>,
}

impl Writer<'_> {
    fn add(
        &mut self,
        title: &str,
        body: &str,
        kind: &str,
        r: &str,
        topic: &str,
        lang: &str,
    ) -> Result<()> {
        let (title, body) = (nfc(title), nfc(body));
        let both = format!("{title}\n{body}");
        let normalized = normalize(&both);
        // Only store `alt` when it differs (text with Bengali/Devanagari digits).
        let alt = if normalized == both {
            String::new()
        } else {
            normalized.clone()
        };
        self.words
            .execute(params![title, body, alt, kind, r, topic, lang])?;
        self.trigram
            .execute(params![normalized, kind, r, topic, lang])?;
        Ok(())
    }
}

/// (Re)build the index rows of one topic. Call inside the install/remove transaction.
pub fn index_topic(conn: &Connection, topic_id: &str) -> Result<()> {
    remove_topic(conn, topic_id)?;
    let topic: Option<(String, Option<String>)> = conn
        .query_row(
            "SELECT title, summary FROM topics WHERE id = ?1",
            [topic_id],
            |r| Ok((r.get(0)?, r.get(1)?)),
        )
        .optional()?;
    let Some((title, summary)) = topic else {
        return Ok(());
    };
    let title: Localized = serde_json::from_str(&title)?;
    let summary: Option<Localized> = summary.map(|s| serde_json::from_str(&s)).transpose()?;

    let mut w = Writer {
        words: conn.prepare(
            "INSERT INTO search_index (title, body, alt, kind, ref, topic_id, lang)
             VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7)",
        )?,
        trigram: conn.prepare(
            "INSERT INTO search_trigram (text, kind, ref, topic_id, lang) VALUES (?1, ?2, ?3, ?4, ?5)",
        )?,
    };

    for (lang, t) in &title {
        let body = summary
            .as_ref()
            .and_then(|s| s.get(lang))
            .cloned()
            .unwrap_or_default();
        w.add(t, &body, "topic", topic_id, topic_id, lang)?;
    }

    let mut sections = conn
        .prepare("SELECT lang, anchor, heading, body_md FROM note_sections WHERE topic_id = ?1")?;
    let rows: Vec<(String, String, String, String)> = sections
        .query_map([topic_id], |r| {
            Ok((r.get(0)?, r.get(1)?, r.get(2)?, r.get(3)?))
        })?
        .collect::<Result<_, _>>()?;
    for (lang, anchor, heading, body) in rows {
        w.add(&heading, &plain(&body), "section", &anchor, topic_id, &lang)?;
    }

    let mut questions = conn.prepare("SELECT id, data FROM questions WHERE topic_id = ?1")?;
    let rows: Vec<(String, String)> = questions
        .query_map([topic_id], |r| Ok((r.get(0)?, r.get(1)?)))?
        .collect::<Result<_, _>>()?;
    for (id, data) in rows {
        let raw: RawQuestion = serde_json::from_str(&data)?;
        let mut langs: Vec<String> = raw.explanation.keys().cloned().collect();
        langs.retain(|l| raw.is_complete_in(l));
        for lang in langs {
            let v = raw.resolve(&id, topic_id, &lang);
            let stem = v.stem.clone().or(v.assertion.clone()).unwrap_or_default();
            let mut body = Vec::new();
            for part in [&v.question, &v.assertion, &v.reason].into_iter().flatten() {
                body.push(part.clone());
            }
            for list in [&v.statements, &v.left, &v.right, &v.items, &v.options]
                .into_iter()
                .flatten()
            {
                body.extend(list.iter().cloned());
            }
            body.push(v.explanation.clone());
            w.add(
                &plain(&stem),
                &plain(&body.join("\n")),
                "question",
                &id,
                topic_id,
                &lang,
            )?;
        }
    }
    Ok(())
}

/// Remove a topic from both indexes.
pub fn remove_topic(conn: &Connection, topic_id: &str) -> Result<()> {
    conn.execute("DELETE FROM search_index WHERE topic_id = ?1", [topic_id])?;
    conn.execute("DELETE FROM search_trigram WHERE topic_id = ?1", [topic_id])?;
    Ok(())
}

/// Rebuild both indexes (after a developer import, or once after upgrading).
pub fn rebuild(conn: &Connection) -> Result<()> {
    conn.execute("DELETE FROM search_index", [])?;
    conn.execute("DELETE FROM search_trigram", [])?;
    let mut stmt = conn.prepare("SELECT id FROM topics")?;
    let ids: Vec<String> = stmt
        .query_map([], |r| r.get(0))?
        .collect::<Result<_, _>>()?;
    for id in ids {
        index_topic(conn, &id)?;
    }
    Ok(())
}

/// Build the index if content exists but the index is empty (first start after upgrade).
pub fn ensure_index(conn: &Connection) -> Result<()> {
    let indexed: i64 = conn.query_row("SELECT COUNT(*) FROM search_index", [], |r| r.get(0))?;
    let topics: i64 = conn.query_row("SELECT COUNT(*) FROM topics", [], |r| r.get(0))?;
    if indexed == 0 && topics > 0 {
        rebuild(conn)?;
    }
    Ok(())
}

fn words(input: &str) -> Vec<String> {
    normalize(input)
        .split(|c: char| c.is_whitespace() || (c.is_ascii_punctuation() && c != '-') || c == '।')
        .map(|w| w.trim_matches('-').replace('"', ""))
        .filter(|w| !w.is_empty())
        .take(8)
        .collect()
}

/// Whole-word query: every word must match, as a prefix. None if nothing searchable.
pub fn fts_query(input: &str) -> Option<String> {
    let w: Vec<String> = words(input)
        .into_iter()
        .map(|w| format!("\"{w}\"*"))
        .collect();
    if w.is_empty() {
        None
    } else {
        Some(w.join(" "))
    }
}

/// Substring query for the trigram index (words of 3+ characters).
pub fn trigram_query(input: &str) -> Option<String> {
    let w: Vec<String> = words(input)
        .into_iter()
        .filter(|w| w.chars().count() >= 3)
        .map(|w| format!("\"{w}\""))
        .collect();
    if w.is_empty() {
        None
    } else {
        Some(w.join(" "))
    }
}

#[derive(Debug, Clone, Serialize)]
pub struct SearchHit {
    /// "topic" | "section" | "question"
    pub kind: String,
    /// Topic id, section anchor or question id.
    pub r#ref: String,
    pub topic_id: String,
    pub topic_title: String,
    pub title: String,
    /// Matching text with matches wrapped in \u{2} … \u{3} (the UI highlights them).
    pub snippet: String,
    /// Language of `title` (the selected language whenever the item exists in it).
    pub lang: String,
    /// Language of `snippet` (English when only the English text matched).
    pub snippet_lang: String,
}

struct Candidate {
    kind: String,
    r: String,
    topic_id: String,
    lang: String,
    title: Option<String>,
    snippet: String,
}

/// Search in `lang`, also matching English text (so English terms work while Bengali
/// content is selected). Each item appears once, titled in `lang` when it exists there.
pub fn search(conn: &Connection, input: &str, lang: &str, limit: usize) -> Result<Vec<SearchHit>> {
    let Some(q) = fts_query(input) else {
        return Ok(Vec::new());
    };
    let mut cands: Vec<Candidate> = Vec::new();
    {
        let mut stmt = conn.prepare(
            "SELECT kind, ref, topic_id, lang, title,
                    snippet(search_index, 1, char(2), char(3), '…', 14)
             FROM search_index
             WHERE search_index MATCH ?1 AND lang IN (?2, 'en')
             ORDER BY bm25(search_index, 4.0, 1.0, 0.8) LIMIT ?3",
        )?;
        let rows = stmt.query_map(params![q, lang, (limit * 3) as i64], |r| {
            Ok(Candidate {
                kind: r.get(0)?,
                r: r.get(1)?,
                topic_id: r.get(2)?,
                lang: r.get(3)?,
                title: Some(r.get(4)?),
                snippet: r.get(5)?,
            })
        })?;
        for c in rows {
            cands.push(c?);
        }
    }
    let distinct: HashSet<(String, String)> = cands
        .iter()
        .map(|c| (c.kind.clone(), c.r.clone()))
        .collect();
    if distinct.len() < TRIGRAM_THRESHOLD
        && let Some(tq) = trigram_query(input)
    {
        let mut stmt = conn.prepare(
            "SELECT kind, ref, topic_id, lang, snippet(search_trigram, 0, char(2), char(3), '…', 48)
             FROM search_trigram
             WHERE search_trigram MATCH ?1 AND lang IN (?2, 'en')
             ORDER BY rank LIMIT ?3",
        )?;
        let rows = stmt.query_map(params![tq, lang, (limit * 2) as i64], |r| {
            Ok(Candidate {
                kind: r.get(0)?,
                r: r.get(1)?,
                topic_id: r.get(2)?,
                lang: r.get(3)?,
                title: None,
                snippet: r.get(4)?,
            })
        })?;
        for c in rows {
            cands.push(c?);
        }
    }

    // Prefer the selected language when an item matched in both.
    let preferred: HashSet<(String, String)> = cands
        .iter()
        .filter(|c| c.lang == lang)
        .map(|c| (c.kind.clone(), c.r.clone()))
        .collect();
    let mut title_in = conn.prepare(
        "SELECT title FROM search_index WHERE kind = ?1 AND ref = ?2 AND topic_id = ?3 AND lang = ?4 LIMIT 1",
    )?;
    let mut topic_titles: HashMap<String, String> = HashMap::new();
    let mut seen: HashSet<(String, String)> = HashSet::new();
    let mut out = Vec::new();
    for c in cands {
        let key = (c.kind.clone(), c.r.clone());
        if (c.lang != lang && preferred.contains(&key)) || !seen.insert(key) {
            continue;
        }
        // Title in the selected language if the item exists in it; else in the match's language.
        let lookup = |l: &str, st: &mut rusqlite::Statement<'_>| {
            st.query_row(params![c.kind, c.r, c.topic_id, l], |row| {
                row.get::<_, String>(0)
            })
            .optional()
        };
        let (title, title_lang) = if c.lang == lang && c.title.is_some() {
            (c.title.clone().unwrap_or_default(), c.lang.clone())
        } else if let Some(t) = lookup(lang, &mut title_in)? {
            (t, lang.to_string())
        } else if let Some(t) = c.title.clone() {
            (t, c.lang.clone())
        } else if let Some(t) = lookup(&c.lang, &mut title_in)? {
            (t, c.lang.clone())
        } else {
            continue;
        };
        let topic_title = match topic_titles.get(&c.topic_id) {
            Some(t) => t.clone(),
            None => {
                let t: String = conn
                    .query_row(
                        "SELECT title FROM topics WHERE id = ?1",
                        [&c.topic_id],
                        |r| r.get::<_, String>(0),
                    )
                    .ok()
                    .and_then(|j| serde_json::from_str::<Localized>(&j).ok())
                    .map(|m| pick(&m, lang))
                    .unwrap_or_else(|| c.topic_id.clone());
                topic_titles.insert(c.topic_id.clone(), t.clone());
                t
            }
        };
        out.push(SearchHit {
            title: if c.kind == "question" {
                first_line(&title, 140)
            } else {
                title
            },
            snippet: c.snippet,
            kind: c.kind,
            r#ref: c.r,
            topic_id: c.topic_id,
            topic_title,
            lang: title_lang,
            snippet_lang: c.lang,
        });
        if out.len() >= limit {
            break;
        }
    }
    Ok(out)
}
