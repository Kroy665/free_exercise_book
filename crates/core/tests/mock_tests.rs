//! Mock test engine against the real sample content: 12 History questions plus 8
//! current-affairs questions (exam patterns include the `ca` subject).

use feb_core::mock::{self, AnswerState, CustomSpec, TestState};
use feb_core::{db, import, practice};
use std::path::PathBuf;

const TOPIC: &str = "hist.modern.revolt-1857";

fn setup() -> (rusqlite::Connection, rusqlite::Connection) {
    let (mut c, u) = db::open_in_memory().unwrap();
    import::import_dir(
        &mut c,
        &PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../../content"),
    )
    .unwrap();
    (c, u)
}

/// Questions available to the UPSC GS pattern (subjects hist + ca), however much
/// sample content exists.
fn pool(c: &rusqlite::Connection) -> u32 {
    c.query_row(
        "SELECT COUNT(*) FROM questions q JOIN topics t ON t.id = q.topic_id WHERE t.subject_id IN ('hist','ca')",
        [],
        |r| r.get(0),
    )
    .unwrap()
}

/// What the engine should do for a 100-question / 120-minute pattern with `n` available.
fn expected(n: u32) -> (u32, u32) {
    let used = n.min(100);
    (
        used,
        if used == 100 {
            120
        } else {
            (120 * used).div_ceil(100)
        },
    )
}

fn answer_key(c: &rusqlite::Connection) -> std::collections::HashMap<String, u8> {
    // Full question id ("<topic>/q0001") -> keyed answer, for every installed question.
    let mut stmt = c.prepare("SELECT id, data FROM questions").unwrap();
    stmt.query_map([], |r| Ok((r.get::<_, String>(0)?, r.get::<_, String>(1)?)))
        .unwrap()
        .map(|row| {
            let (id, d) = row.unwrap();
            let v: serde_json::Value = serde_json::from_str(&d).unwrap();
            (id, v["answer"].as_u64().unwrap() as u8)
        })
        .collect()
}

#[test]
fn exam_patterns_are_scaled_to_installed_content() {
    let (c, _) = setup();
    let views = mock::pattern_views(&c, "en").unwrap();
    let upsc = views
        .iter()
        .find(|p| p.id == "upsc-cse-prelims-gs1")
        .unwrap();
    let (used, minutes) = expected(pool(&c));
    assert_eq!((upsc.total_questions, upsc.available), (100, used));
    assert_eq!(upsc.scaled_minutes, minutes);
    let ssc = views.iter().find(|p| p.id == "ssc-cgl-tier1").unwrap();
    let ga = ssc.sections.iter().find(|s| s.id == "ga").unwrap();
    assert_eq!((ga.required, ga.available), (25, pool(&c).min(25)));
    assert!(
        ssc.sections
            .iter()
            .filter(|s| s.id != "ga")
            .all(|s| s.available == 0)
    );
}

#[test]
fn pattern_test_full_cycle_with_negative_marking() {
    let (c, mut u) = setup();
    let id = mock::create_from_pattern(&c, &u, "upsc-cse-prelims-gs1").unwrap();
    let s = mock::session(&c, &u, id, "bn").unwrap();
    let (used, minutes) = expected(pool(&c));
    assert_eq!(
        (s.status.as_str(), s.total_questions as u32, s.duration_ms),
        ("ready", used, minutes as u64 * 60_000)
    );
    assert_eq!(s.scaled_from, (used < 100).then_some((100, 120)));
    // Answers and explanations are hidden during the test.
    let qs = &s.sections[0].questions;
    assert!(
        qs.iter()
            .all(|q| q.answer == u8::MAX && q.explanation.is_empty())
    );
    assert_eq!(qs[0].lang, "bn");
    assert!(
        mock::save(&u, id, &TestState::default(), 1).is_err(),
        "cannot save before start"
    );

    mock::start(&u, id).unwrap();
    let key = answer_key(&c);
    let mut state = TestState::default();
    for (i, q) in qs.iter().enumerate() {
        let right = key[&q.id];
        let choice = match i {
            0..=2 => Some(right),           // 3 correct
            3..=4 => Some((right + 1) % 4), // 2 wrong
            _ => None,                      // the rest unanswered
        };
        state.answers.insert(
            q.id.clone(),
            AnswerState {
                choice,
                marked: i == 5,
                visited: true,
                time_ms: 1000,
            },
        );
    }
    state.current = 6;
    mock::save(&u, id, &state, 600_000).unwrap();
    // Resume: progress survives a reload.
    let resumed = mock::session(&c, &u, id, "en").unwrap();
    assert_eq!(
        (
            resumed.status.as_str(),
            resumed.state.current,
            resumed.remaining_ms
        ),
        ("in_progress", 6, 600_000)
    );

    let r = mock::submit(&c, &mut u, id, &state, 300_000).unwrap();
    assert_eq!(
        (r.total.correct, r.total.wrong, r.total.unanswered),
        (3, 2, used - 5)
    );
    assert_eq!(r.total.max_score, 2.0 * used as f64);
    assert_eq!(r.total.score, 4.67); // 3*2 - 2*0.6667
    assert_eq!(r.accuracy, 60.0);
    assert_eq!(r.time_used_ms, minutes as u64 * 60_000 - 300_000);
    // Submitting again returns the same result; saving is no longer allowed.
    assert_eq!(
        mock::submit(&c, &mut u, id, &TestState::default(), 0)
            .unwrap()
            .total
            .score,
        4.67
    );
    assert!(mock::save(&u, id, &state, 1).is_err());

    // Wrong answers reach the mistake notebook; only answered questions are attempts.
    assert_eq!(practice::mistakes(&c, &u, "en").unwrap().len(), 2);
    assert_eq!(practice::stats(&c, &u).unwrap().total_attempts, 5);

    let res = mock::result(&c, &u, id, "en").unwrap();
    assert_eq!(res.review.len() as u32, used);
    assert_eq!(
        res.review.iter().filter(|x| x.outcome == "wrong").count(),
        2
    );
    assert!(
        res.review
            .iter()
            .all(|x| x.question.answer < 4 && !x.question.explanation.is_empty())
    );
    assert!(!res.topics.is_empty());
    let list = mock::list(&u).unwrap();
    assert_eq!(
        (list[0].status.as_str(), list[0].score),
        ("submitted", Some(4.67))
    );
}

#[test]
fn custom_tests_validate_and_prefer_unseen_questions() {
    let (c, u) = setup();
    let spec = |count, topics: Vec<&str>| CustomSpec {
        title: Some("Revision".into()),
        topic_ids: topics.into_iter().map(String::from).collect(),
        count,
        duration_minutes: 10,
        marks_each: 1.0,
        negative: 0.25,
    };
    assert!(mock::create_custom(&c, &u, &spec(5, vec![])).is_err());
    assert!(mock::create_custom(&c, &u, &spec(0, vec![TOPIC])).is_err());
    assert!(mock::create_custom(&c, &u, &spec(5, vec!["no.such.topic"])).is_err());

    // Attempt 5 questions in practice; a 7-question test must pick the 7 unseen ones.
    let qs = practice::questions_for_topic(&c, TOPIC, "en").unwrap();
    for q in &qs[..5] {
        practice::record_attempt(&c, &u, &q.id, q.answer, 500, "practice").unwrap();
    }
    let id = mock::create_custom(&c, &u, &spec(7, vec![TOPIC])).unwrap();
    let s = mock::session(&c, &u, id, "en").unwrap();
    assert_eq!(s.title, "Revision");
    let seen: Vec<_> = qs[..5].iter().map(|q| q.id.clone()).collect();
    assert!(
        s.sections[0]
            .questions
            .iter()
            .all(|q| !seen.contains(&q.id))
    );
    // Asking for more than exist gives all of them.
    let all = mock::create_custom(&c, &u, &spec(50, vec![TOPIC])).unwrap();
    assert_eq!(
        mock::session(&c, &u, all, "en").unwrap().total_questions,
        12
    );
    mock::delete(&u, all).unwrap();
    assert!(mock::session(&c, &u, all, "en").is_err());
}
