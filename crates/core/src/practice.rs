use crate::model::{AttemptResult, QuestionView, RawQuestion, Stats};
use crate::{CoreError, Result, srs};
use rusqlite::{Connection, OptionalExtension, params};
use std::collections::HashMap;

const LATEST: &str = "SELECT a.question_id, a.correct FROM attempts a
     JOIN (SELECT question_id, MAX(id) AS mid FROM attempts GROUP BY question_id) l ON a.id = l.mid";

fn load(
    content: &Connection,
    sql: &str,
    p: impl rusqlite::Params,
    lang: &str,
) -> Result<Vec<QuestionView>> {
    let mut stmt = content.prepare(sql)?;
    let rows: Vec<(String, String, String)> = stmt
        .query_map(p, |r| Ok((r.get(0)?, r.get(1)?, r.get(2)?)))?
        .collect::<Result<_, _>>()?;
    rows.into_iter()
        .map(|(id, topic_id, data)| {
            let raw: RawQuestion = serde_json::from_str(&data)?;
            Ok(raw.resolve(&id, &topic_id, lang))
        })
        .collect()
}

pub fn questions_for_topic(
    content: &Connection,
    topic_id: &str,
    lang: &str,
) -> Result<Vec<QuestionView>> {
    load(
        content,
        "SELECT id, topic_id, data FROM questions WHERE topic_id = ?1 ORDER BY ord",
        [topic_id],
        lang,
    )
}

/// Grade on the Rust side (the source of truth), then store the attempt.
pub fn record_attempt(
    content: &Connection,
    user: &Connection,
    question_id: &str,
    chosen: u8,
    time_ms: u32,
    mode: &str,
) -> Result<AttemptResult> {
    if chosen > 3 {
        return Err(CoreError::Invalid(format!(
            "chosen option {chosen} out of range"
        )));
    }
    let data: Option<String> = content
        .query_row(
            "SELECT data FROM questions WHERE id = ?1",
            [question_id],
            |r| r.get(0),
        )
        .optional()?;
    let Some(data) = data else {
        return Err(CoreError::NotFound(format!("question {question_id}")));
    };
    let raw: RawQuestion = serde_json::from_str(&data)?;
    let correct = raw.answer == chosen;
    user.execute(
        "INSERT INTO attempts (question_id, chosen, correct, time_ms, mode) VALUES (?1, ?2, ?3, ?4, ?5)",
        params![question_id, chosen, correct, time_ms, mode],
    )?;
    let now = srs::now();
    let srs = if !correct {
        // A wrong answer anywhere puts the question into the review queue.
        srs::review(user, question_id, srs::Grade::Again, now)?;
        None
    } else if mode == "revise" {
        Some(srs::preview(srs::card(user, question_id)?.as_ref(), now))
    } else {
        None
    };
    Ok(AttemptResult {
        correct,
        answer: raw.answer,
        srs,
    })
}

/// The user's recall grade for a correctly answered revision question.
pub fn grade(user: &Connection, question_id: &str, grade: srs::Grade) -> Result<srs::Card> {
    srs::review(user, question_id, grade, srs::now())
}

/// Questions due for spaced-repetition review now (questions removed from content are skipped).
pub fn due(
    content: &Connection,
    user: &Connection,
    lang: &str,
    limit: usize,
) -> Result<Vec<QuestionView>> {
    let mut out = Vec::new();
    for id in srs::due_ids(user, srs::now(), limit)? {
        out.extend(load(
            content,
            "SELECT id, topic_id, data FROM questions WHERE id = ?1",
            [&id],
            lang,
        )?);
    }
    Ok(out)
}

/// Latest result per question → (attempted, correct) per topic.
pub fn latest_results_by_topic(user: &Connection) -> Result<HashMap<String, (i64, i64)>> {
    let mut stmt = user.prepare(LATEST)?;
    let mut map: HashMap<String, (i64, i64)> = HashMap::new();
    let rows = stmt.query_map([], |r| Ok((r.get::<_, String>(0)?, r.get::<_, bool>(1)?)))?;
    for row in rows {
        let (qid, correct) = row?;
        let topic = qid.split('/').next().unwrap_or_default().to_string();
        let e = map.entry(topic).or_default();
        e.0 += 1;
        if correct {
            e.1 += 1;
        }
    }
    Ok(map)
}

/// Questions whose most recent attempt was wrong (the mistake notebook).
pub fn mistakes(content: &Connection, user: &Connection, lang: &str) -> Result<Vec<QuestionView>> {
    let mut stmt = user.prepare(&format!("{LATEST} WHERE a.correct = 0 ORDER BY a.id DESC"))?;
    let ids: Vec<String> = stmt
        .query_map([], |r| r.get(0))?
        .collect::<Result<_, _>>()?;
    let mut out = Vec::new();
    for id in ids {
        // A question may have been removed from content; skip it silently.
        out.extend(load(
            content,
            "SELECT id, topic_id, data FROM questions WHERE id = ?1",
            [&id],
            lang,
        )?);
    }
    Ok(out)
}

pub fn stats(content: &Connection, user: &Connection) -> Result<Stats> {
    let mut s = Stats {
        topics: content.query_row("SELECT COUNT(*) FROM topics", [], |r| r.get(0))?,
        questions: content.query_row("SELECT COUNT(*) FROM questions", [], |r| r.get(0))?,
        total_attempts: user.query_row("SELECT COUNT(*) FROM attempts", [], |r| r.get(0))?,
        ..Default::default()
    };
    for (attempted, correct) in latest_results_by_topic(user)?.values() {
        s.attempted += attempted;
        s.correct += correct;
    }
    s.mistakes = s.attempted - s.correct;
    s.due = srs::due_count(user, srs::now())?;
    Ok(s)
}
