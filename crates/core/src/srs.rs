//! Spaced repetition with FSRS-5 (Free Spaced Repetition Scheduler, as used by Anki).
//!
//! Cards are created when a question is answered wrongly anywhere (practice, test,
//! revision) and are then reviewed in Revise, where the user grades their recall.
//! Formulas: https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-Algorithm
//! (FSRS-5, default parameters, 90% desired retention).

use crate::Result;
use rusqlite::{Connection, OptionalExtension, params};
use serde::{Deserialize, Serialize};

/// FSRS-5 default parameters.
const W: [f64; 19] = [
    0.40255, 1.18385, 3.173, 15.69105, 7.1949, 0.5345, 1.4604, 0.0046, 1.54575, 0.1192, 1.01925,
    1.9395, 0.11, 0.29605, 2.2698, 0.2315, 2.9898, 0.51655, 0.6621,
];
const DECAY: f64 = -0.5;
const FACTOR: f64 = 19.0 / 81.0;
const DESIRED_RETENTION: f64 = 0.9;
const DAY: f64 = 86_400.0;
/// "Again" brings a card back after this many seconds (same session / later today).
const RELEARN_SECS: i64 = 10 * 60;
const MAX_INTERVAL_DAYS: f64 = 365.0;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "lowercase")]
pub enum Grade {
    Again = 1,
    Hard = 2,
    Good = 3,
    Easy = 4,
}

#[derive(Debug, Clone, Copy, PartialEq, Serialize)]
pub struct Card {
    pub stability: f64,
    pub difficulty: f64,
    pub due: i64,
    pub last_review: i64,
    pub reps: i64,
    pub lapses: i64,
}

fn g(grade: Grade) -> f64 {
    grade as i32 as f64
}

fn init_difficulty(grade: Grade) -> f64 {
    (W[4] - (W[5] * (g(grade) - 1.0)).exp() + 1.0).clamp(1.0, 10.0)
}

/// Probability of recall after `days` with stability `s`.
pub fn retrievability(days: f64, s: f64) -> f64 {
    (1.0 + FACTOR * days / s).powf(DECAY)
}

fn interval_days(s: f64) -> f64 {
    (s / FACTOR * (DESIRED_RETENTION.powf(1.0 / DECAY) - 1.0)).clamp(1.0, MAX_INTERVAL_DAYS)
}

fn next_difficulty(d: f64, grade: Grade) -> f64 {
    let delta = -W[6] * (g(grade) - 3.0);
    let d1 = d + delta * (10.0 - d) / 9.0; // linear damping
    (W[7] * init_difficulty(Grade::Easy) + (1.0 - W[7]) * d1).clamp(1.0, 10.0) // mean reversion
}

fn recall_stability(d: f64, s: f64, r: f64, grade: Grade) -> f64 {
    let hard = if grade == Grade::Hard { W[15] } else { 1.0 };
    let easy = if grade == Grade::Easy { W[16] } else { 1.0 };
    s * (W[8].exp() * (11.0 - d) * s.powf(-W[9]) * ((W[10] * (1.0 - r)).exp() - 1.0) * hard * easy
        + 1.0)
}

fn forget_stability(d: f64, s: f64, r: f64) -> f64 {
    let sf = W[11] * d.powf(-W[12]) * ((s + 1.0).powf(W[13]) - 1.0) * (W[14] * (1.0 - r)).exp();
    sf.min(s)
}

fn short_term_stability(s: f64, grade: Grade) -> f64 {
    s * (W[17] * (g(grade) - 3.0 + W[18])).exp()
}

/// Stability, difficulty, reps and lapses after reviewing with `grade`.
fn next_state(card: Option<&Card>, grade: Grade, now: i64) -> (f64, f64, i64, i64) {
    match card {
        None => (
            W[grade as usize - 1],
            init_difficulty(grade),
            1,
            i64::from(grade == Grade::Again),
        ),
        Some(c) => {
            let elapsed = ((now - c.last_review).max(0) as f64) / DAY;
            let s = if elapsed < 1.0 {
                short_term_stability(c.stability, grade)
            } else {
                let r = retrievability(elapsed, c.stability);
                if grade == Grade::Again {
                    forget_stability(c.difficulty, c.stability, r)
                } else {
                    recall_stability(c.difficulty, c.stability, r, grade)
                }
            };
            (
                s.max(0.01),
                next_difficulty(c.difficulty, grade),
                c.reps + 1,
                c.lapses + i64::from(grade == Grade::Again),
            )
        }
    }
}

/// Whole-day intervals for Hard / Good / Easy, kept apart like Anki does
/// (hard ≤ good, good ≥ hard + 1, easy ≥ good + 1) so the three buttons always differ.
fn intervals(card: Option<&Card>, now: i64) -> [f64; 3] {
    let days = |g| interval_days(next_state(card, g, now).0).round();
    let (mut hard, mut good, mut easy) = (days(Grade::Hard), days(Grade::Good), days(Grade::Easy));
    hard = hard.min(good);
    good = good.max(hard + 1.0);
    easy = easy.max(good + 1.0);
    [
        hard,
        good.min(MAX_INTERVAL_DAYS),
        easy.min(MAX_INTERVAL_DAYS),
    ]
}

/// Schedule a review. `card` is None for a new card.
pub fn schedule(card: Option<&Card>, grade: Grade, now: i64) -> Card {
    let (stability, difficulty, reps, lapses) = next_state(card, grade, now);
    let due = match grade {
        Grade::Again => now + RELEARN_SECS,
        g => now + (intervals(card, now)[g as usize - 2] * DAY) as i64,
    };
    Card {
        stability,
        difficulty,
        due,
        last_review: now,
        reps,
        lapses,
    }
}

/// Seconds until the next review for each grade (for the grade buttons).
#[derive(Debug, Clone, Copy, Serialize)]
pub struct Preview {
    pub again: i64,
    pub hard: i64,
    pub good: i64,
    pub easy: i64,
}

pub fn preview(card: Option<&Card>, now: i64) -> Preview {
    let after = |gr| schedule(card, gr, now).due - now;
    Preview {
        again: after(Grade::Again),
        hard: after(Grade::Hard),
        good: after(Grade::Good),
        easy: after(Grade::Easy),
    }
}

// ------------------------------------------------------------------ storage

pub fn now() -> i64 {
    std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .map(|d| d.as_secs() as i64)
        .unwrap_or(0)
}

pub fn card(user: &Connection, question_id: &str) -> Result<Option<Card>> {
    Ok(user
        .query_row(
            "SELECT stability, difficulty, due, last_review, reps, lapses FROM srs_cards WHERE question_id = ?1",
            [question_id],
            |r| {
                Ok(Card {
                    stability: r.get(0)?,
                    difficulty: r.get(1)?,
                    due: r.get(2)?,
                    last_review: r.get(3)?,
                    reps: r.get(4)?,
                    lapses: r.get(5)?,
                })
            },
        )
        .optional()?)
}

/// Apply a review and store the card.
pub fn review(user: &Connection, question_id: &str, grade: Grade, now: i64) -> Result<Card> {
    let next = schedule(card(user, question_id)?.as_ref(), grade, now);
    user.execute(
        "INSERT OR REPLACE INTO srs_cards (question_id, stability, difficulty, due, last_review, reps, lapses)
         VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7)",
        params![question_id, next.stability, next.difficulty, next.due, next.last_review, next.reps, next.lapses],
    )?;
    Ok(next)
}

/// Question ids due for review (oldest due first).
pub fn due_ids(user: &Connection, now: i64, limit: usize) -> Result<Vec<String>> {
    let mut stmt =
        user.prepare("SELECT question_id FROM srs_cards WHERE due <= ?1 ORDER BY due LIMIT ?2")?;
    Ok(stmt
        .query_map(params![now, limit as i64], |r| r.get(0))?
        .collect::<Result<_, _>>()?)
}

pub fn due_count(user: &Connection, now: i64) -> Result<i64> {
    Ok(user.query_row(
        "SELECT COUNT(*) FROM srs_cards WHERE due <= ?1",
        [now],
        |r| r.get(0),
    )?)
}

#[cfg(test)]
mod tests {
    use super::*;

    const T0: i64 = 1_800_000_000;
    fn days(secs: i64) -> f64 {
        secs as f64 / DAY
    }

    #[test]
    fn new_card_intervals_follow_grade() {
        let p = preview(None, T0);
        assert_eq!(p.again, RELEARN_SECS);
        assert!(p.hard < p.good && p.good < p.easy, "{p:?}");
        // Right after a lapse stabilities are tiny, but the buttons still differ.
        let lapsed = schedule(
            Some(&schedule(None, Grade::Good, T0)),
            Grade::Again,
            T0 + 3 * 86_400,
        );
        let q = preview(Some(&lapsed), lapsed.last_review + 600);
        assert!(q.hard < q.good && q.good < q.easy, "{q:?}");
        // FSRS-5 defaults: first Good ≈ 3 days, first Easy ≈ 16 days.
        assert_eq!(days(p.good).round(), 3.0);
        assert_eq!(days(p.easy).round(), 16.0);
    }

    #[test]
    fn successful_reviews_grow_and_lapses_shrink() {
        let mut c = schedule(None, Grade::Good, T0);
        let mut prev = c.due - T0;
        for _ in 0..4 {
            let now = c.due; // review exactly when due
            c = schedule(Some(&c), Grade::Good, now);
            let interval = c.due - now;
            assert!(
                interval > prev,
                "intervals grow: {} -> {}",
                days(prev),
                days(interval)
            );
            prev = interval;
        }
        let before = c.stability;
        let lapsed = schedule(Some(&c), Grade::Again, c.due);
        assert!(lapsed.stability < before);
        assert_eq!(lapsed.lapses, 1);
        assert_eq!(lapsed.due - c.due, RELEARN_SECS);
        assert!(
            lapsed.difficulty > c.difficulty,
            "Again makes the card harder"
        );
        assert!((1.0..=10.0).contains(&lapsed.difficulty));
    }

    #[test]
    fn storage_and_due_queue() {
        let (_, u) = crate::db::open_in_memory().unwrap();
        review(&u, "a", Grade::Again, T0).unwrap();
        review(&u, "b", Grade::Good, T0).unwrap();
        assert_eq!(due_count(&u, T0).unwrap(), 0);
        assert_eq!(
            due_ids(&u, T0 + RELEARN_SECS, 10).unwrap(),
            vec!["a".to_string()]
        );
        assert_eq!(due_count(&u, T0 + 4 * 86_400).unwrap(), 2);
        let c = review(&u, "a", Grade::Good, T0 + RELEARN_SECS).unwrap();
        assert_eq!(c.reps, 2);
    }
}
