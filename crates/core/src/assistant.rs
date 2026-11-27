//! Study assistant: the prompt and the course context sent to the language model.
//!
//! The model gets a catalogue of the installed notes so it can point the student at the
//! right section to read first. Links must use the app's own form `/topic/<id>#<anchor>`;
//! [`known_links`] lets the UI drop any link the model invents.

use crate::Result;
use crate::localize::{Localized, pick};
use rusqlite::{Connection, params};
use serde::{Deserialize, Serialize};
use std::collections::{BTreeSet, HashSet};

/// Where the student was when they asked.
#[derive(Debug, Clone, Default, Deserialize)]
pub struct AskContext {
    /// Text the student selected (notes, a question, an explanation, an earlier reply).
    #[serde(default)]
    pub selection: Option<String>,
    /// Topic open on screen, if any.
    #[serde(default)]
    pub topic_id: Option<String>,
    /// Question on screen, if any ("<topic_id>/q0001").
    #[serde(default)]
    pub question_id: Option<String>,
    /// The student has answered that question. Until then the model is not told the key
    /// or the worked solution, so it cannot give the answer away.
    #[serde(default)]
    pub answered: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct ChatMessage {
    /// "user" | "assistant"
    pub role: String,
    pub content: String,
}

const MAX_SELECTION: usize = 4000;
const MAX_MESSAGE: usize = 8000;
const MAX_TURNS: usize = 20;

pub const SYSTEM_RULES: &str = r#"You are the teacher inside Free Exercise Book, a revision app for the WBSSC SLST Mathematics exam (Assistant Teacher, Class IX–X and Class XI–XII). The student has an M.Sc. in mathematics but has been away from it for about six years, so explain at that level: precise, but recall the definitions and steps they may have forgotten.

How to answer:
- Answer the question directly first, then explain step by step. Keep it compact; use short paragraphs and lists.
- Write all mathematics in LaTeX: $...$ inline and $$...$$ for displayed lines. Do not use \( \) or \[ \].
- State theorem hypotheses exactly. If textbooks differ on a convention, say which one you use.
- If the student selected text, explain that text in the context of the page they are on.
- If you are not sure of something, say so rather than guess.
- End with a short "**Read first**" list (at most 3 items) naming the notes that build the background for this question, as Markdown links whose targets are copied character for character from the catalogue below. Only use links that appear in the catalogue; never invent one. Leave the list out if nothing in the catalogue fits."#;

/// For small local models: they copy example links instead of reading the catalogue, so the
/// app suggests the notes itself ([`suggest`]) and the model is told not to write links.
const NO_LINKS: &str = "- Do not write links or a reading list; the app shows the relevant notes under your answer.";

fn clip(s: &str, max: usize) -> String {
    if s.chars().count() <= max {
        s.to_string()
    } else {
        format!("{}…", s.chars().take(max).collect::<String>())
    }
}

struct TopicRow {
    id: String,
    title: String,
    unit: String,
}

fn topics(conn: &Connection, lang: &str) -> Result<Vec<TopicRow>> {
    let mut stmt = conn.prepare(
        "SELECT t.id, t.title, u.title FROM topics t JOIN units u ON u.id = t.unit_id
         JOIN subjects s ON s.id = t.subject_id ORDER BY s.ord, u.ord, t.ord",
    )?;
    let rows = stmt.query_map([], |r| {
        Ok((r.get::<_, String>(0)?, r.get::<_, String>(1)?, r.get::<_, String>(2)?))
    })?;
    let mut out = Vec::new();
    for row in rows {
        let (id, t, u) = row?;
        let title = serde_json::from_str::<Localized>(&t).map(|m| pick(&m, lang)).unwrap_or(t);
        let unit = serde_json::from_str::<Localized>(&u).map(|m| pick(&m, lang)).unwrap_or(u);
        out.push(TopicRow { id, title, unit });
    }
    Ok(out)
}

fn sections(conn: &Connection, topic_id: &str) -> Result<Vec<(String, String)>> {
    let mut stmt = conn.prepare(
        "SELECT anchor, heading FROM note_sections WHERE topic_id = ?1 AND lang = 'en' ORDER BY ord",
    )?;
    let rows = stmt.query_map([topic_id], |r| Ok((r.get(0)?, r.get(1)?)))?;
    Ok(rows.collect::<std::result::Result<_, _>>()?)
}

/// Topics whose notes best match `text` (word OR-query over the search index).
fn related_topics(conn: &Connection, text: &str, limit: usize) -> Result<Vec<String>> {
    let mut words: Vec<String> = Vec::new();
    let mut seen = HashSet::new();
    for w in text.split(|c: char| !c.is_alphanumeric()) {
        let w = w.to_lowercase();
        if w.chars().count() >= 4 && !w.chars().all(|c| c.is_ascii_digit()) && seen.insert(w.clone()) {
            words.push(format!("\"{w}\""));
        }
        if words.len() >= 24 {
            break;
        }
    }
    if words.is_empty() {
        return Ok(Vec::new());
    }
    let q = words.join(" OR ");
    let mut stmt = conn.prepare(
        "SELECT topic_id FROM search_index WHERE search_index MATCH ?1 AND lang = 'en'
         ORDER BY bm25(search_index, 4.0, 1.0, 0.8) LIMIT 60",
    )?;
    let rows = stmt.query_map(params![q], |r| r.get::<_, String>(0))?;
    let mut out = Vec::new();
    for t in rows {
        let t = t?;
        if !out.contains(&t) {
            out.push(t);
        }
        if out.len() >= limit {
            break;
        }
    }
    Ok(out)
}

fn question_text(conn: &Connection, question_id: &str, answered: bool) -> Result<Option<String>> {
    let data: Option<String> = conn
        .query_row("SELECT data FROM questions WHERE id = ?1", [question_id], |r| r.get(0))
        .ok();
    let Some(data) = data else { return Ok(None) };
    let v: serde_json::Value = serde_json::from_str(&data)?;
    let en = |k: &str| v.get(k).and_then(|x| x.get("en")).and_then(|x| x.as_str()).map(str::to_string);
    let list = |k: &str| -> Vec<String> {
        v.get(k)
            .and_then(|x| x.as_array())
            .map(|a| a.iter().filter_map(|x| x.get("en").and_then(|s| s.as_str()).map(str::to_string)).collect())
            .unwrap_or_default()
    };
    let mut s = String::new();
    for k in ["stem", "assertion", "reason", "question"] {
        if let Some(t) = en(k) {
            s.push_str(&format!("{k}: {t}\n"));
        }
    }
    for k in ["statements", "left", "right", "options"] {
        let l = list(k);
        if !l.is_empty() {
            s.push_str(&format!("{k}:\n"));
            for (i, t) in l.iter().enumerate() {
                s.push_str(&format!("  {}. {t}\n", i + 1));
            }
        }
    }
    if !answered {
        s.push_str("(not answered yet: give hints and explain the ideas, but do not reveal or confirm which option is correct)\n");
        return Ok(Some(s));
    }
    if let Some(a) = v.get("answer").and_then(|x| x.as_u64()) {
        s.push_str(&format!("correct option index (0-based): {a}\n"));
    }
    if let Some(t) = en("explanation") {
        s.push_str(&format!("worked solution: {}\n", clip(&t, 3000)));
    }
    Ok(Some(s))
}

/// The notes catalogue. `full`: every section of every topic (for large-context models);
/// otherwise every topic title plus the sections of the topics in `focus`.
pub fn catalogue(conn: &Connection, lang: &str, full: bool, focus: &[String]) -> Result<String> {
    let mut out = String::from("Catalogue of notes in the app (link: title › section):\n");
    let mut unit = String::new();
    for t in topics(conn, lang)? {
        if t.unit != unit {
            out.push_str(&format!("\n{}\n", t.unit));
            unit = t.unit.clone();
        }
        out.push_str(&format!("- /topic/{} — {}\n", t.id, t.title));
        if full || focus.contains(&t.id) {
            for (a, h) in sections(conn, &t.id)? {
                out.push_str(&format!("  - /topic/{}#{} — {} › {}\n", t.id, a, t.title, h));
            }
        }
    }
    Ok(out)
}

/// The system prompt. Stable across a conversation when `full` (so it can be cached).
pub fn system_prompt(conn: &Connection, lang: &str, full: bool, ctx: &AskContext, last_user: &str) -> Result<String> {
    let mut focus: Vec<String> = Vec::new();
    if !full {
        if let Some(t) = &ctx.topic_id {
            focus.push(t.clone());
        }
        let probe = format!("{} {}", ctx.selection.as_deref().unwrap_or_default(), last_user);
        for t in related_topics(conn, &probe, 4)? {
            if !focus.contains(&t) {
                focus.push(t);
            }
        }
    }
    if full {
        Ok(format!("{SYSTEM_RULES}\n\n{}", catalogue(conn, lang, true, &focus)?))
    } else {
        let rules = SYSTEM_RULES.split("\n- End with").next().unwrap_or(SYSTEM_RULES);
        let topics = catalogue(conn, lang, false, &focus)?;
        Ok(format!("{rules}\n{NO_LINKS}\n\nTopics in the app, for context:\n{topics}"))
    }
}

#[derive(Debug, Clone, Serialize)]
pub struct Suggestion {
    /// `/topic/<id>#<anchor>`
    pub href: String,
    pub topic: String,
    pub section: String,
}

/// Note sections that best match `text` (the question, the selection and the reply).
pub fn suggest(conn: &Connection, lang: &str, text: &str, limit: usize) -> Result<Vec<Suggestion>> {
    let mut words: Vec<String> = Vec::new();
    let mut seen = HashSet::new();
    for w in text.split(|c: char| !c.is_alphanumeric()) {
        let w = w.to_lowercase();
        if w.chars().count() >= 4 && !w.chars().all(|c| c.is_ascii_digit()) && !STOP.contains(&w.as_str()) && seen.insert(w.clone()) {
            words.push(format!("\"{w}\""));
        }
        if words.len() >= 40 {
            break;
        }
    }
    if words.is_empty() {
        return Ok(Vec::new());
    }
    let mut stmt = conn.prepare(
        "SELECT topic_id, ref, title FROM search_index
         WHERE search_index MATCH ?1 AND kind = 'section' AND lang = 'en'
         ORDER BY bm25(search_index, 4.0, 1.0, 0.8) LIMIT 40",
    )?;
    let rows = stmt.query_map(params![words.join(" OR ")], |r| {
        Ok((r.get::<_, String>(0)?, r.get::<_, String>(1)?, r.get::<_, String>(2)?))
    })?;
    let titles: std::collections::HashMap<String, String> = topics(conn, lang)?.into_iter().map(|t| (t.id, t.title)).collect();
    let mut out: Vec<Suggestion> = Vec::new();
    let mut per_topic: std::collections::HashMap<String, usize> = Default::default();
    for row in rows {
        let (tid, anchor, heading) = row?;
        if anchor == "exam-tips" {
            continue;
        }
        let n = per_topic.entry(tid.clone()).or_default();
        if *n >= 1 {
            continue; // one section per topic, so the list spans topics
        }
        *n += 1;
        out.push(Suggestion {
            href: format!("/topic/{tid}#{anchor}"),
            topic: titles.get(&tid).cloned().unwrap_or_else(|| tid.clone()),
            section: heading,
        });
        if out.len() >= limit {
            break;
        }
    }
    Ok(out)
}

/// Words too common in maths text to say anything about the topic.
const STOP: &[&str] = &[
    "that", "this", "with", "from", "then", "than", "have", "what", "when", "which", "where", "there", "their", "they",
    "does", "dont", "understand", "explain", "please", "step", "about", "into", "only", "also", "some", "such", "each",
    "every", "will", "would", "should", "could", "must", "been", "being", "here", "these", "those", "your", "frac",
    "mathbb", "text", "left", "right", "cdot", "quad", "question", "answer", "option", "correct", "solution", "true",
    "false", "given", "show", "find", "value", "values", "equal", "equals", "number", "numbers",
];

/// What the student is looking at, prepended to their latest message.
pub fn page_context(conn: &Connection, lang: &str, ctx: &AskContext) -> Result<String> {
    let mut s = String::new();
    if let Some(tid) = &ctx.topic_id
        && let Some(t) = topics(conn, lang)?.into_iter().find(|t| &t.id == tid)
    {
        s.push_str(&format!("[Page: topic {} — {}]\n", t.id, t.title));
    }
    if let Some(qid) = &ctx.question_id
        && let Some(q) = question_text(conn, qid, ctx.answered)?
    {
        s.push_str(&format!("[Question on screen]\n{q}"));
    }
    if let Some(sel) = ctx.selection.as_deref().map(str::trim).filter(|s| !s.is_empty()) {
        s.push_str(&format!("[Selected text]\n{}\n", clip(sel, MAX_SELECTION)));
    }
    Ok(s)
}

/// Validated, trimmed conversation with the page context attached to the last user turn.
pub fn prepare_messages(conn: &Connection, lang: &str, ctx: &AskContext, history: &[ChatMessage]) -> Result<Vec<ChatMessage>> {
    let mut msgs: Vec<ChatMessage> = history
        .iter()
        .filter(|m| (m.role == "user" || m.role == "assistant") && !m.content.trim().is_empty())
        .map(|m| ChatMessage { role: m.role.clone(), content: clip(&m.content, MAX_MESSAGE) })
        .collect();
    if msgs.len() > MAX_TURNS {
        msgs.drain(..msgs.len() - MAX_TURNS);
    }
    while msgs.first().is_some_and(|m| m.role != "user") {
        msgs.remove(0);
    }
    let Some(last) = msgs.last_mut().filter(|m| m.role == "user") else {
        return Err(crate::CoreError::Invalid("the conversation must end with a question".into()));
    };
    let page = page_context(conn, lang, ctx)?;
    if !page.is_empty() {
        last.content = format!("{page}\n[My question]\n{}", last.content);
    }
    Ok(msgs)
}

/// Every link target the model may use: `/topic/<id>` and `/topic/<id>#<anchor>`.
pub fn known_links(conn: &Connection) -> Result<BTreeSet<String>> {
    let mut out = BTreeSet::new();
    let mut stmt = conn.prepare("SELECT id FROM topics")?;
    for id in stmt.query_map([], |r| r.get::<_, String>(0))? {
        out.insert(format!("/topic/{}", id?));
    }
    let mut stmt = conn.prepare("SELECT DISTINCT topic_id, anchor FROM note_sections")?;
    for row in stmt.query_map([], |r| Ok((r.get::<_, String>(0)?, r.get::<_, String>(1)?)))? {
        let (t, a) = row?;
        out.insert(format!("/topic/{t}#{a}"));
    }
    Ok(out)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn page_context_goes_on_the_last_user_turn() {
        let (content, _user) = crate::db::open_in_memory().unwrap();
        let ctx = AskContext { selection: Some("Cauchy sequence".into()), ..Default::default() };
        let msgs = prepare_messages(
            &content,
            "en",
            &ctx,
            &[
                ChatMessage { role: "assistant".into(), content: "hello".into() },
                ChatMessage { role: "user".into(), content: "why?".into() },
            ],
        )
        .unwrap();
        assert_eq!(msgs.len(), 1);
        assert!(msgs[0].content.contains("[Selected text]\nCauchy sequence"));
        assert!(msgs[0].content.ends_with("[My question]\nwhy?"));
    }

    #[test]
    fn rejects_a_conversation_without_a_question() {
        let (content, _user) = crate::db::open_in_memory().unwrap();
        let r = prepare_messages(&content, "en", &AskContext::default(), &[]);
        assert!(r.is_err());
    }
}
