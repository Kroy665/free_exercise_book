//! Progress analytics: daily activity, streaks, goal, per-topic accuracy, weak areas and
//! test trend (docs/SPEC.md A1–A3). Days are local calendar days.

use crate::localize::{Localized, pick};
use crate::{Result, settings, srs};
use rusqlite::Connection;
use serde::Serialize;
use std::collections::HashMap;

/// Days shown in the activity heatmap (12 weeks).
pub const HEATMAP_DAYS: i64 = 84;
/// A topic is "weak" when at least this many of its questions were tried…
const WEAK_MIN_ATTEMPTED: i64 = 3;
/// …and the latest answers are right less often than this (%).
const WEAK_BELOW_PCT: f64 = 60.0;

#[derive(Debug, Clone, Serialize)]
pub struct DayCount {
    pub date: String,
    pub attempts: i64,
    pub correct: i64,
}

#[derive(Debug, Clone, Serialize)]
pub struct TopicProgress {
    pub topic_id: String,
    pub title: String,
    pub subject_title: String,
    pub questions: i64,
    /// Distinct questions tried.
    pub attempted: i64,
    /// Of those, answered correctly the last time.
    pub correct: i64,
    /// correct / attempted × 100 (0 when nothing attempted).
    pub accuracy: f64,
    pub last_at: Option<i64>,
}

#[derive(Debug, Clone, Serialize)]
pub struct TestPoint {
    pub id: i64,
    pub title: String,
    pub pct: f64,
    pub submitted_at: i64,
}

#[derive(Debug, Clone, Serialize)]
pub struct ProgressView {
    pub total_attempts: i64,
    pub attempted: i64,
    pub correct: i64,
    pub accuracy: f64,
    pub today: i64,
    pub daily_goal: i64,
    pub streak: i64,
    pub best_streak: i64,
    pub due: i64,
    pub days: Vec<DayCount>,
    pub topics: Vec<TopicProgress>,
    pub weak: Vec<String>,
    pub tests: Vec<TestPoint>,
}

fn pct(a: i64, b: i64) -> f64 {
    if b == 0 {
        0.0
    } else {
        (a as f64 / b as f64 * 1000.0).round() / 10.0
    }
}

/// (current streak, best streak) from local days with at least one attempt.
fn streaks(user: &Connection) -> Result<(i64, i64)> {
    let today: i64 = user.query_row(
        "SELECT CAST(julianday(date('now','localtime')) AS INTEGER)",
        [],
        |r| r.get(0),
    )?;
    let mut stmt = user.prepare(
        "SELECT DISTINCT CAST(julianday(date(created_at,'unixepoch','localtime')) AS INTEGER) AS d
         FROM attempts ORDER BY d DESC",
    )?;
    let days: Vec<i64> = stmt
        .query_map([], |r| r.get(0))?
        .collect::<Result<_, _>>()?;
    let (mut best, mut run, mut prev) = (0, 0, None::<i64>);
    for &d in days.iter().rev() {
        run = if prev == Some(d - 1) { run + 1 } else { 1 };
        best = best.max(run);
        prev = Some(d);
    }
    // Current streak: consecutive days ending today, or yesterday (today not done yet).
    let mut current = 0;
    let mut expect = match days.first() {
        Some(&d) if d == today || d == today - 1 => d,
        _ => return Ok((0, best)),
    };
    for &d in &days {
        if d == expect {
            current += 1;
            expect -= 1;
        } else {
            break;
        }
    }
    Ok((current, best))
}

pub fn view(content: &Connection, user: &Connection, lang: &str) -> Result<ProgressView> {
    let total_attempts: i64 = user.query_row("SELECT COUNT(*) FROM attempts", [], |r| r.get(0))?;
    let today: i64 = user.query_row(
        "SELECT COUNT(*) FROM attempts WHERE date(created_at,'unixepoch','localtime') = date('now','localtime')",
        [],
        |r| r.get(0),
    )?;

    // Activity for the last HEATMAP_DAYS days, oldest first, including empty days.
    let mut stmt = user.prepare(
        "WITH RECURSIVE days(d) AS (
             SELECT date('now','localtime', ?1)
             UNION ALL SELECT date(d, '+1 day') FROM days WHERE d < date('now','localtime')
         )
         SELECT days.d, COUNT(a.id), COALESCE(SUM(a.correct), 0)
         FROM days LEFT JOIN attempts a ON date(a.created_at,'unixepoch','localtime') = days.d
         GROUP BY days.d ORDER BY days.d",
    )?;
    let days: Vec<DayCount> = stmt
        .query_map([format!("-{} days", HEATMAP_DAYS - 1)], |r| {
            Ok(DayCount {
                date: r.get(0)?,
                attempts: r.get(1)?,
                correct: r.get(2)?,
            })
        })?
        .collect::<Result<_, _>>()?;

    // Latest result per question and last activity, grouped by topic.
    let mut per_topic: HashMap<String, (i64, i64, i64)> = HashMap::new(); // attempted, correct, last_at
    let mut stmt = user.prepare(
        "SELECT a.question_id, a.correct, l.last_at FROM attempts a
         JOIN (SELECT question_id, MAX(id) AS mid, MAX(created_at) AS last_at FROM attempts GROUP BY question_id) l
           ON a.id = l.mid",
    )?;
    for row in stmt.query_map([], |r| {
        Ok((
            r.get::<_, String>(0)?,
            r.get::<_, bool>(1)?,
            r.get::<_, i64>(2)?,
        ))
    })? {
        let (qid, correct, at) = row?;
        let topic = qid.split('/').next().unwrap_or_default().to_string();
        let e = per_topic.entry(topic).or_default();
        e.0 += 1;
        e.1 += i64::from(correct);
        e.2 = e.2.max(at);
    }

    let mut stmt = content.prepare(
        "SELECT t.id, t.title, s.title, (SELECT COUNT(*) FROM questions q WHERE q.topic_id = t.id)
         FROM topics t JOIN subjects s ON s.id = t.subject_id ORDER BY s.ord, t.unit_id, t.ord",
    )?;
    let rows: Vec<(String, String, String, i64)> = stmt
        .query_map([], |r| Ok((r.get(0)?, r.get(1)?, r.get(2)?, r.get(3)?)))?
        .collect::<Result<_, _>>()?;
    let mut topics = Vec::new();
    for (id, title, subject, questions) in rows {
        let (attempted, correct, last) = per_topic.get(&id).copied().unwrap_or((0, 0, 0));
        topics.push(TopicProgress {
            title: pick(&serde_json::from_str::<Localized>(&title)?, lang),
            subject_title: pick(&serde_json::from_str::<Localized>(&subject)?, lang),
            questions,
            attempted,
            correct,
            accuracy: pct(correct, attempted),
            last_at: (last > 0).then_some(last),
            topic_id: id,
        });
    }
    let mut weak: Vec<&TopicProgress> = topics
        .iter()
        .filter(|t| t.attempted >= WEAK_MIN_ATTEMPTED && t.accuracy < WEAK_BELOW_PCT)
        .collect();
    weak.sort_by(|a, b| a.accuracy.total_cmp(&b.accuracy));
    let weak = weak
        .into_iter()
        .take(5)
        .map(|t| t.topic_id.clone())
        .collect();

    let (attempted, correct) = per_topic
        .values()
        .fold((0, 0), |acc, v| (acc.0 + v.0, acc.1 + v.1));
    let tests = crate::mock::list(user)?
        .into_iter()
        .filter(|t| t.status == "submitted")
        .take(12)
        .filter_map(|t| {
            let (score, max) = (t.score?, t.max_score?);
            Some(TestPoint {
                pct: if max > 0.0 {
                    ((score / max * 1000.0).round() / 10.0).max(0.0)
                } else {
                    0.0
                },
                id: t.id,
                title: t.title,
                submitted_at: t.submitted_at?,
            })
        })
        .collect::<Vec<_>>()
        .into_iter()
        .rev()
        .collect();
    let (streak, best_streak) = streaks(user)?;
    let daily_goal = settings::get_all(user)?
        .get("daily_goal")
        .and_then(|v| v.parse().ok())
        .unwrap_or(20);

    Ok(ProgressView {
        total_attempts,
        attempted,
        correct,
        accuracy: pct(correct, attempted),
        today,
        daily_goal,
        streak,
        best_streak,
        due: srs::due_count(user, srs::now())?,
        days,
        topics,
        weak,
        tests,
    })
}
