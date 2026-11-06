//! Mock tests: custom tests and exam-pattern tests with timer, negative marking,
//! resume and results (docs/SPEC.md T1–T5, docs/NAVIGATION.md §4.4).
//!
//! A test's question set and marking scheme are frozen in `user.db` when it is created,
//! so a pack update or removal never changes a running or finished test.

use crate::localize::{Localized, pick};
use crate::model::{QuestionView, RawQuestion};
use crate::{CoreError, Result};
use rusqlite::{Connection, OptionalExtension, params};
use serde::{Deserialize, Serialize};
use std::collections::{BTreeMap, HashMap, HashSet};
use std::time::{SystemTime, UNIX_EPOCH};

// ------------------------------------------------------------------ exam patterns

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PatternSection {
    pub id: String,
    pub name: Localized,
    pub questions: u32,
    pub marks_each: f64,
    pub subjects: Vec<String>,
}

/// `content/exams/*.yaml` (docs/CONTENT_STRUCTURE.md §8).
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ExamPattern {
    pub id: String,
    pub name: Localized,
    pub duration_minutes: u32,
    /// Marks deducted per wrong answer.
    pub negative_marking: f64,
    pub sections: Vec<PatternSection>,
    #[serde(default)]
    pub status: Option<String>,
    #[serde(default)]
    pub source: Option<String>,
    #[serde(default)]
    pub as_of: Option<String>,
}

/// Insert or replace exam patterns (from a verified manifest or a developer import).
pub fn store_patterns(content: &Connection, patterns: &[ExamPattern]) -> Result<()> {
    for p in patterns {
        content.execute(
            "INSERT OR REPLACE INTO exam_patterns (id, data) VALUES (?1, ?2)",
            params![p.id, serde_json::to_string(p)?],
        )?;
    }
    Ok(())
}

pub fn patterns(content: &Connection) -> Result<Vec<ExamPattern>> {
    let mut stmt = content.prepare("SELECT data FROM exam_patterns ORDER BY id")?;
    let rows: Vec<String> = stmt
        .query_map([], |r| r.get(0))?
        .collect::<Result<_, _>>()?;
    rows.iter().map(|d| Ok(serde_json::from_str(d)?)).collect()
}

fn pattern(content: &Connection, id: &str) -> Result<ExamPattern> {
    let data: Option<String> = content
        .query_row("SELECT data FROM exam_patterns WHERE id = ?1", [id], |r| {
            r.get(0)
        })
        .optional()?;
    let data = data.ok_or_else(|| CoreError::NotFound(format!("exam pattern {id}")))?;
    Ok(serde_json::from_str(&data)?)
}

#[derive(Debug, Clone, Serialize)]
pub struct PatternSectionView {
    pub id: String,
    pub name: String,
    pub required: u32,
    pub available: u32,
    pub marks_each: f64,
}

#[derive(Debug, Clone, Serialize)]
pub struct PatternView {
    pub id: String,
    pub name: String,
    pub duration_minutes: u32,
    pub negative_marking: f64,
    pub total_questions: u32,
    pub total_marks: f64,
    /// Questions that can be included with the installed content.
    pub available: u32,
    /// Duration if the test is scaled down to the available questions.
    pub scaled_minutes: u32,
    pub sections: Vec<PatternSectionView>,
    pub source: Option<String>,
    pub as_of: Option<String>,
}

fn subject_question_ids(
    content: &Connection,
    subjects: &[String],
) -> Result<Vec<(String, String)>> {
    // (question id, topic id), in a stable order.
    let mut out = Vec::new();
    let mut stmt = content.prepare(
        "SELECT q.id, q.topic_id FROM questions q JOIN topics t ON t.id = q.topic_id
         WHERE t.subject_id = ?1 ORDER BY q.id",
    )?;
    for s in subjects {
        for row in stmt.query_map([s], |r| Ok((r.get(0)?, r.get(1)?)))? {
            out.push(row?);
        }
    }
    Ok(out)
}

fn scaled_minutes(duration: u32, total: u32, included: u32) -> u32 {
    if total == 0 || included >= total {
        return duration;
    }
    ((duration as f64 * included as f64 / total as f64).ceil() as u32).max(1)
}

/// Exam patterns with how many of their questions the installed content can supply.
pub fn pattern_views(content: &Connection, lang: &str) -> Result<Vec<PatternView>> {
    let mut out = Vec::new();
    for p in patterns(content)? {
        let mut used: HashSet<String> = HashSet::new();
        let mut sections = Vec::new();
        for s in &p.sections {
            let pool: Vec<_> = subject_question_ids(content, &s.subjects)?
                .into_iter()
                .filter(|(q, _)| !used.contains(q))
                .collect();
            let available = (pool.len() as u32).min(s.questions);
            used.extend(pool.into_iter().take(available as usize).map(|(q, _)| q));
            sections.push(PatternSectionView {
                id: s.id.clone(),
                name: pick(&s.name, lang),
                required: s.questions,
                available,
                marks_each: s.marks_each,
            });
        }
        let total: u32 = p.sections.iter().map(|s| s.questions).sum();
        let available: u32 = sections.iter().map(|s| s.available).sum();
        out.push(PatternView {
            name: pick(&p.name, lang),
            total_marks: p
                .sections
                .iter()
                .map(|s| s.questions as f64 * s.marks_each)
                .sum(),
            scaled_minutes: scaled_minutes(p.duration_minutes, total, available),
            duration_minutes: p.duration_minutes,
            negative_marking: p.negative_marking,
            total_questions: total,
            available,
            sections,
            source: p.source.clone(),
            as_of: p.as_of.clone(),
            id: p.id,
        });
    }
    Ok(out)
}

// ------------------------------------------------------------------ test records

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SectionConfig {
    pub id: String,
    pub name: Localized,
    pub marks_each: f64,
    /// Marks deducted per wrong answer.
    pub negative: f64,
    pub question_ids: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TestConfig {
    pub duration_ms: u64,
    pub sections: Vec<SectionConfig>,
    /// Set when an exam-pattern test was scaled down: (full question count, full minutes).
    #[serde(default)]
    pub scaled_from: Option<(u32, u32)>,
}

#[derive(Debug, Clone, Default, Serialize, Deserialize)]
pub struct AnswerState {
    pub choice: Option<u8>,
    #[serde(default)]
    pub marked: bool,
    #[serde(default)]
    pub visited: bool,
    #[serde(default)]
    pub time_ms: u64,
}

#[derive(Debug, Clone, Default, Serialize, Deserialize)]
pub struct TestState {
    pub answers: BTreeMap<String, AnswerState>,
    /// Index of the question the user was on (for resume).
    #[serde(default)]
    pub current: usize,
}

/// Options for a custom test.
#[derive(Debug, Clone, Deserialize)]
pub struct CustomSpec {
    pub title: Option<String>,
    pub topic_ids: Vec<String>,
    pub count: u32,
    pub duration_minutes: u32,
    pub marks_each: f64,
    pub negative: f64,
}

fn now() -> i64 {
    SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .map(|d| d.as_secs() as i64)
        .unwrap_or(0)
}

/// Small deterministic PRNG (xorshift64*); no external dependency needed.
struct Rng(u64);
impl Rng {
    fn new() -> Self {
        let seed = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .map(|d| d.as_nanos() as u64)
            .unwrap_or(1);
        Rng(seed | 1)
    }
    fn next(&mut self) -> u64 {
        self.0 ^= self.0 >> 12;
        self.0 ^= self.0 << 25;
        self.0 ^= self.0 >> 27;
        self.0.wrapping_mul(0x2545_F491_4F6C_DD1D)
    }
    fn shuffle<T>(&mut self, v: &mut [T]) {
        for i in (1..v.len()).rev() {
            let j = (self.next() % (i as u64 + 1)) as usize;
            v.swap(i, j);
        }
    }
}

/// Pick `count` questions from `pool`, preferring ones the user has never attempted,
/// then ones they got wrong last time, then the rest. Random within each group.
fn choose(
    user: &Connection,
    pool: Vec<String>,
    count: usize,
    rng: &mut Rng,
) -> Result<Vec<String>> {
    let mut latest: HashMap<String, bool> = HashMap::new();
    let mut stmt = user.prepare(
        "SELECT a.question_id, a.correct FROM attempts a
         JOIN (SELECT question_id, MAX(id) AS mid FROM attempts GROUP BY question_id) l ON a.id = l.mid",
    )?;
    for row in stmt.query_map([], |r| Ok((r.get::<_, String>(0)?, r.get::<_, bool>(1)?)))? {
        let (q, c) = row?;
        latest.insert(q, c);
    }
    let (mut unseen, mut wrong, mut right) = (Vec::new(), Vec::new(), Vec::new());
    for q in pool {
        match latest.get(&q) {
            None => unseen.push(q),
            Some(false) => wrong.push(q),
            Some(true) => right.push(q),
        }
    }
    rng.shuffle(&mut unseen);
    rng.shuffle(&mut wrong);
    rng.shuffle(&mut right);
    Ok(unseen
        .into_iter()
        .chain(wrong)
        .chain(right)
        .take(count)
        .collect())
}

fn insert_test(
    user: &Connection,
    kind: &str,
    pattern_id: Option<&str>,
    title: &str,
    config: &TestConfig,
) -> Result<i64> {
    user.execute(
        "INSERT INTO tests (kind, pattern_id, title, config, state, remaining_ms, status)
         VALUES (?1, ?2, ?3, ?4, ?5, ?6, 'ready')",
        params![
            kind,
            pattern_id,
            title,
            serde_json::to_string(config)?,
            serde_json::to_string(&TestState::default())?,
            config.duration_ms as i64
        ],
    )?;
    Ok(user.last_insert_rowid())
}

pub fn create_custom(content: &Connection, user: &Connection, spec: &CustomSpec) -> Result<i64> {
    if spec.topic_ids.is_empty() {
        return Err(CoreError::Invalid("choose at least one topic".into()));
    }
    if spec.count == 0 || spec.count > 500 {
        return Err(CoreError::Invalid(
            "number of questions must be 1–500".into(),
        ));
    }
    if spec.duration_minutes == 0 || spec.duration_minutes > 600 {
        return Err(CoreError::Invalid("time must be 1–600 minutes".into()));
    }
    let valid = spec.marks_each.is_finite()
        && spec.marks_each > 0.0
        && spec.negative.is_finite()
        && (0.0..=spec.marks_each).contains(&spec.negative);
    if !valid {
        return Err(CoreError::Invalid("invalid marking scheme".into()));
    }
    let mut pool = Vec::new();
    let mut stmt = content.prepare("SELECT id FROM questions WHERE topic_id = ?1 ORDER BY id")?;
    for t in &spec.topic_ids {
        for row in stmt.query_map([t], |r| r.get::<_, String>(0))? {
            pool.push(row?);
        }
    }
    if pool.is_empty() {
        return Err(CoreError::Invalid(
            "the selected topics have no questions".into(),
        ));
    }
    let ids = choose(user, pool, spec.count as usize, &mut Rng::new())?;
    let config = TestConfig {
        duration_ms: spec.duration_minutes as u64 * 60_000,
        sections: vec![SectionConfig {
            id: "all".into(),
            name: [("en".to_string(), "Questions".to_string())].into(),
            marks_each: spec.marks_each,
            negative: spec.negative,
            question_ids: ids,
        }],
        scaled_from: None,
    };
    let title = spec
        .title
        .clone()
        .filter(|t| !t.trim().is_empty())
        .unwrap_or_else(|| "Custom test".into());
    insert_test(user, "custom", None, &title, &config)
}

pub fn create_from_pattern(
    content: &Connection,
    user: &Connection,
    pattern_id: &str,
) -> Result<i64> {
    let p = pattern(content, pattern_id)?;
    let mut rng = Rng::new();
    let mut used: HashSet<String> = HashSet::new();
    let mut sections = Vec::new();
    for s in &p.sections {
        let pool: Vec<String> = subject_question_ids(content, &s.subjects)?
            .into_iter()
            .map(|(q, _)| q)
            .filter(|q| !used.contains(q))
            .collect();
        let ids = choose(user, pool, s.questions as usize, &mut rng)?;
        used.extend(ids.iter().cloned());
        if !ids.is_empty() {
            sections.push(SectionConfig {
                id: s.id.clone(),
                name: s.name.clone(),
                marks_each: s.marks_each,
                negative: p.negative_marking,
                question_ids: ids,
            });
        }
    }
    let total: u32 = p.sections.iter().map(|s| s.questions).sum();
    let included: u32 = sections.iter().map(|s| s.question_ids.len() as u32).sum();
    if included == 0 {
        return Err(CoreError::Invalid(
            "no installed questions match this exam yet; download topics for its subjects first"
                .into(),
        ));
    }
    let minutes = scaled_minutes(p.duration_minutes, total, included);
    let config = TestConfig {
        duration_ms: minutes as u64 * 60_000,
        sections,
        scaled_from: (included < total).then_some((total, p.duration_minutes)),
    };
    insert_test(user, "pattern", Some(&p.id), &pick(&p.name, "en"), &config)
}

struct Row {
    title: String,
    kind: String,
    config: TestConfig,
    state: TestState,
    remaining_ms: i64,
    status: String,
    created_at: i64,
    submitted_at: Option<i64>,
    result: Option<TestSummary>,
}

fn load(user: &Connection, id: i64) -> Result<Row> {
    let row = user
        .query_row(
            "SELECT title, kind, config, state, remaining_ms, status, created_at, submitted_at, result
             FROM tests WHERE id = ?1",
            [id],
            |r| {
                Ok((
                    r.get::<_, String>(0)?,
                    r.get::<_, String>(1)?,
                    r.get::<_, String>(2)?,
                    r.get::<_, String>(3)?,
                    r.get::<_, i64>(4)?,
                    r.get::<_, String>(5)?,
                    r.get::<_, i64>(6)?,
                    r.get::<_, Option<i64>>(7)?,
                    r.get::<_, Option<String>>(8)?,
                ))
            },
        )
        .optional()?
        .ok_or_else(|| CoreError::NotFound(format!("test {id}")))?;
    Ok(Row {
        title: row.0,
        kind: row.1,
        config: serde_json::from_str(&row.2)?,
        state: serde_json::from_str(&row.3)?,
        remaining_ms: row.4,
        status: row.5,
        created_at: row.6,
        submitted_at: row.7,
        result: row.8.map(|r| serde_json::from_str(&r)).transpose()?,
    })
}

fn questions_by_id(
    content: &Connection,
    ids: &[String],
    lang: &str,
) -> Result<HashMap<String, QuestionView>> {
    let mut out = HashMap::new();
    let mut stmt = content.prepare("SELECT topic_id, data FROM questions WHERE id = ?1")?;
    for id in ids {
        let row: Option<(String, String)> = stmt
            .query_row([id], |r| Ok((r.get(0)?, r.get(1)?)))
            .optional()?;
        if let Some((topic, data)) = row {
            let raw: RawQuestion = serde_json::from_str(&data)?;
            out.insert(id.clone(), raw.resolve(id, &topic, lang));
        }
    }
    Ok(out)
}

// ------------------------------------------------------------------ session (exam view)

#[derive(Debug, Clone, Serialize)]
pub struct SessionSection {
    pub id: String,
    pub name: String,
    pub marks_each: f64,
    pub negative: f64,
    pub questions: Vec<QuestionView>,
}

#[derive(Debug, Clone, Serialize)]
pub struct TestSession {
    pub id: i64,
    pub title: String,
    pub kind: String,
    pub status: String,
    pub duration_ms: u64,
    pub remaining_ms: i64,
    pub scaled_from: Option<(u32, u32)>,
    pub sections: Vec<SessionSection>,
    pub state: TestState,
    pub total_questions: usize,
    pub total_marks: f64,
    /// Questions removed from content since the test was created (they are skipped).
    pub missing: usize,
}

/// The exam view. Answers and explanations are withheld until the test is submitted.
pub fn session(
    content: &Connection,
    user: &Connection,
    id: i64,
    lang: &str,
) -> Result<TestSession> {
    let row = load(user, id)?;
    let all: Vec<String> = row
        .config
        .sections
        .iter()
        .flat_map(|s| s.question_ids.clone())
        .collect();
    let qs = questions_by_id(content, &all, lang)?;
    let submitted = row.status == "submitted";
    let mut missing = 0;
    let sections = row
        .config
        .sections
        .iter()
        .map(|s| SessionSection {
            id: s.id.clone(),
            name: pick(&s.name, lang),
            marks_each: s.marks_each,
            negative: s.negative,
            questions: s
                .question_ids
                .iter()
                .filter_map(|q| {
                    let v = qs.get(q).cloned();
                    if v.is_none() {
                        missing += 1;
                    }
                    v
                })
                .map(|mut v| {
                    if !submitted {
                        v.answer = u8::MAX;
                        v.explanation = String::new();
                    }
                    v
                })
                .collect(),
        })
        .collect::<Vec<_>>();
    let total_questions = sections.iter().map(|s| s.questions.len()).sum();
    let total_marks = sections
        .iter()
        .map(|s| s.questions.len() as f64 * s.marks_each)
        .sum();
    Ok(TestSession {
        id,
        title: row.title,
        kind: row.kind,
        status: row.status,
        duration_ms: row.config.duration_ms,
        remaining_ms: row.remaining_ms,
        scaled_from: row.config.scaled_from,
        sections,
        state: row.state,
        total_questions,
        total_marks,
        missing,
    })
}

pub fn start(user: &Connection, id: i64) -> Result<()> {
    let n = user.execute(
        "UPDATE tests SET status = 'in_progress', started_at = COALESCE(started_at, ?2)
         WHERE id = ?1 AND status IN ('ready', 'in_progress')",
        params![id, now()],
    )?;
    if n == 0 {
        return Err(CoreError::Invalid(format!("test {id} cannot be started")));
    }
    Ok(())
}

/// Save progress (called after every answer and periodically for the timer).
pub fn save(user: &Connection, id: i64, state: &TestState, remaining_ms: i64) -> Result<()> {
    let n = user.execute(
        "UPDATE tests SET state = ?2, remaining_ms = ?3 WHERE id = ?1 AND status = 'in_progress'",
        params![id, serde_json::to_string(state)?, remaining_ms.max(0)],
    )?;
    if n == 0 {
        return Err(CoreError::Invalid(format!("test {id} is not in progress")));
    }
    Ok(())
}

pub fn delete(user: &Connection, id: i64) -> Result<()> {
    user.execute("DELETE FROM tests WHERE id = ?1", [id])?;
    Ok(())
}

// ------------------------------------------------------------------ grading

#[derive(Debug, Clone, Default, Serialize, Deserialize)]
pub struct Tally {
    pub correct: u32,
    pub wrong: u32,
    pub unanswered: u32,
    pub score: f64,
    pub max_score: f64,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SectionTally {
    pub id: String,
    pub name: Localized,
    #[serde(flatten)]
    pub tally: Tally,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TopicTally {
    pub topic_id: String,
    #[serde(flatten)]
    pub tally: Tally,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TestSummary {
    #[serde(flatten)]
    pub total: Tally,
    /// correct / attempted (0 when nothing was attempted).
    pub accuracy: f64,
    pub time_used_ms: u64,
    pub sections: Vec<SectionTally>,
    pub topics: Vec<TopicTally>,
}

fn round2(x: f64) -> f64 {
    (x * 100.0).round() / 100.0
}

fn add(t: &mut Tally, marks: f64, negative: f64, outcome: Option<bool>) {
    t.max_score += marks;
    match outcome {
        Some(true) => {
            t.correct += 1;
            t.score += marks;
        }
        Some(false) => {
            t.wrong += 1;
            t.score -= negative;
        }
        None => t.unanswered += 1,
    }
}

/// Submit (or auto-submit) a test: grade it, store the result and record every answered
/// question as an attempt (so wrong answers reach the mistake notebook).
pub fn submit(
    content: &Connection,
    user: &mut Connection,
    id: i64,
    state: &TestState,
    remaining_ms: i64,
) -> Result<TestSummary> {
    let row = load(user, id)?;
    if row.status == "submitted" {
        return row
            .result
            .ok_or_else(|| CoreError::Invalid("submitted test has no result".into()));
    }
    let mut answers: HashMap<String, u8> = HashMap::new();
    let mut topic_of: HashMap<String, String> = HashMap::new();
    {
        let mut stmt = content.prepare("SELECT topic_id, data FROM questions WHERE id = ?1")?;
        for s in &row.config.sections {
            for q in &s.question_ids {
                if let Some((topic, data)) = stmt
                    .query_row([q], |r| {
                        Ok((r.get::<_, String>(0)?, r.get::<_, String>(1)?))
                    })
                    .optional()?
                {
                    let raw: RawQuestion = serde_json::from_str(&data)?;
                    answers.insert(q.clone(), raw.answer);
                    topic_of.insert(q.clone(), topic);
                }
            }
        }
    }

    let mut total = Tally::default();
    let mut sections = Vec::new();
    let mut topics: BTreeMap<String, Tally> = BTreeMap::new();
    let tx = user.transaction()?;
    for s in &row.config.sections {
        let mut st = Tally::default();
        for q in &s.question_ids {
            let Some(&answer) = answers.get(q) else {
                continue;
            }; // removed from content
            let a = state.answers.get(q).cloned().unwrap_or_default();
            let outcome = a.choice.map(|c| c == answer);
            add(&mut st, s.marks_each, s.negative, outcome);
            add(&mut total, s.marks_each, s.negative, outcome);
            add(
                topics.entry(topic_of[q].clone()).or_default(),
                s.marks_each,
                s.negative,
                outcome,
            );
            if let Some(c) = a.choice {
                tx.execute(
                    "INSERT INTO attempts (question_id, chosen, correct, time_ms, mode) VALUES (?1, ?2, ?3, ?4, 'test')",
                    params![q, c, c == answer, a.time_ms as i64],
                )?;
                if c != answer {
                    crate::srs::review(&tx, q, crate::srs::Grade::Again, now())?;
                }
            }
        }
        st.score = round2(st.score);
        sections.push(SectionTally {
            id: s.id.clone(),
            name: s.name.clone(),
            tally: st,
        });
    }
    total.score = round2(total.score);
    let attempted = total.correct + total.wrong;
    let summary = TestSummary {
        accuracy: if attempted == 0 {
            0.0
        } else {
            round2(total.correct as f64 / attempted as f64 * 100.0)
        },
        time_used_ms: row
            .config
            .duration_ms
            .saturating_sub(remaining_ms.max(0) as u64),
        total,
        sections,
        topics: topics
            .into_iter()
            .map(|(topic_id, mut tally)| {
                tally.score = round2(tally.score);
                TopicTally { topic_id, tally }
            })
            .collect(),
    };
    tx.execute(
        "UPDATE tests SET status = 'submitted', submitted_at = ?2, state = ?3, remaining_ms = ?4, result = ?5
         WHERE id = ?1",
        params![id, now(), serde_json::to_string(state)?, remaining_ms.max(0), serde_json::to_string(&summary)?],
    )?;
    tx.commit()?;
    Ok(summary)
}

// ------------------------------------------------------------------ results and history

#[derive(Debug, Clone, Serialize)]
pub struct ReviewItem {
    pub section: String,
    pub question: QuestionView,
    pub chosen: Option<u8>,
    pub marked: bool,
    pub time_ms: u64,
    /// "correct" | "wrong" | "unanswered"
    pub outcome: &'static str,
}

#[derive(Debug, Clone, Serialize)]
pub struct NamedTally {
    pub id: String,
    pub name: String,
    #[serde(flatten)]
    pub tally: Tally,
}

#[derive(Debug, Clone, Serialize)]
pub struct TestResult {
    pub id: i64,
    pub title: String,
    pub submitted_at: Option<i64>,
    pub duration_ms: u64,
    pub scaled_from: Option<(u32, u32)>,
    pub summary: TestSummary,
    pub sections: Vec<NamedTally>,
    pub topics: Vec<NamedTally>,
    pub review: Vec<ReviewItem>,
}

pub fn result(content: &Connection, user: &Connection, id: i64, lang: &str) -> Result<TestResult> {
    let row = load(user, id)?;
    let summary = row
        .result
        .clone()
        .ok_or_else(|| CoreError::Invalid(format!("test {id} is not submitted yet")))?;
    let all: Vec<String> = row
        .config
        .sections
        .iter()
        .flat_map(|s| s.question_ids.clone())
        .collect();
    let qs = questions_by_id(content, &all, lang)?;
    let mut review = Vec::new();
    for s in &row.config.sections {
        for q in &s.question_ids {
            let Some(v) = qs.get(q) else { continue };
            let a = row.state.answers.get(q).cloned().unwrap_or_default();
            review.push(ReviewItem {
                section: pick(&s.name, lang),
                outcome: match a.choice {
                    None => "unanswered",
                    Some(c) if c == v.answer => "correct",
                    Some(_) => "wrong",
                },
                chosen: a.choice,
                marked: a.marked,
                time_ms: a.time_ms,
                question: v.clone(),
            });
        }
    }
    let topic_title = |t: &str| -> String {
        content
            .query_row("SELECT title FROM topics WHERE id = ?1", [t], |r| {
                r.get::<_, String>(0)
            })
            .ok()
            .and_then(|j| serde_json::from_str::<Localized>(&j).ok())
            .map(|m| pick(&m, lang))
            .unwrap_or_else(|| t.to_string())
    };
    Ok(TestResult {
        id,
        title: row.title,
        submitted_at: row.submitted_at,
        duration_ms: row.config.duration_ms,
        scaled_from: row.config.scaled_from,
        sections: summary
            .sections
            .iter()
            .map(|s| NamedTally {
                id: s.id.clone(),
                name: pick(&s.name, lang),
                tally: s.tally.clone(),
            })
            .collect(),
        topics: summary
            .topics
            .iter()
            .map(|t| NamedTally {
                id: t.topic_id.clone(),
                name: topic_title(&t.topic_id),
                tally: t.tally.clone(),
            })
            .collect(),
        summary,
        review,
    })
}

#[derive(Debug, Clone, Serialize)]
pub struct TestListItem {
    pub id: i64,
    pub title: String,
    pub kind: String,
    pub status: String,
    pub questions: usize,
    pub duration_ms: u64,
    pub remaining_ms: i64,
    pub created_at: i64,
    pub submitted_at: Option<i64>,
    pub score: Option<f64>,
    pub max_score: Option<f64>,
    pub accuracy: Option<f64>,
}

pub fn list(user: &Connection) -> Result<Vec<TestListItem>> {
    let mut stmt = user.prepare("SELECT id FROM tests ORDER BY id DESC LIMIT 200")?;
    let ids: Vec<i64> = stmt
        .query_map([], |r| r.get(0))?
        .collect::<Result<_, _>>()?;
    ids.into_iter()
        .map(|id| {
            let r = load(user, id)?;
            Ok(TestListItem {
                id,
                questions: r.config.sections.iter().map(|s| s.question_ids.len()).sum(),
                duration_ms: r.config.duration_ms,
                remaining_ms: r.remaining_ms,
                created_at: r.created_at,
                submitted_at: r.submitted_at,
                score: r.result.as_ref().map(|s| s.total.score),
                max_score: r.result.as_ref().map(|s| s.total.max_score),
                accuracy: r.result.as_ref().map(|s| s.accuracy),
                title: r.title,
                kind: r.kind,
                status: r.status,
            })
        })
        .collect()
}
