//! Spaced repetition wiring and progress analytics against the sample content.

use feb_core::mock::{self, AnswerState, TestState};
use feb_core::srs::{self, Grade};
use feb_core::{db, import, practice, progress, settings};
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

#[test]
fn wrong_answers_enter_the_review_queue_and_revision_grades() {
    let (c, u) = setup();
    let qs = practice::questions_for_topic(&c, TOPIC, "en").unwrap();
    let (q0, q1) = (&qs[0], &qs[1]);

    // Practice: wrong -> card due in 10 minutes; right -> no card, no grading prompt.
    let r = practice::record_attempt(&c, &u, &q0.id, (q0.answer + 1) % 4, 500, "practice").unwrap();
    assert!(r.srs.is_none());
    let card = srs::card(&u, &q0.id).unwrap().expect("card created");
    assert_eq!(card.lapses, 1);
    assert!(
        practice::record_attempt(&c, &u, &q1.id, q1.answer, 500, "practice")
            .unwrap()
            .srs
            .is_none()
    );
    assert!(srs::card(&u, &q1.id).unwrap().is_none());
    assert_eq!(srs::due_count(&u, srs::now()).unwrap(), 0);
    assert_eq!(srs::due_count(&u, srs::now() + 601).unwrap(), 1);

    // Revision: a correct answer returns grade previews (Again < Hard < Good < Easy).
    let r = practice::record_attempt(&c, &u, &q0.id, q0.answer, 500, "revise").unwrap();
    let p = r.srs.expect("preview in revise mode");
    assert!(
        p.again < p.hard && p.hard < p.good && p.good < p.easy,
        "{p:?}"
    );
    let graded = practice::grade(&u, &q0.id, Grade::Good).unwrap();
    assert!(graded.due > srs::now() + 3600);
    assert_eq!(graded.reps, 2);

    // Tests: wrong answers create cards too.
    let id = mock::create_custom(
        &c,
        &u,
        &mock::CustomSpec {
            title: None,
            topic_ids: vec![TOPIC.into()],
            count: 12,
            duration_minutes: 5,
            marks_each: 1.0,
            negative: 0.0,
        },
    )
    .unwrap();
    mock::start(&u, id).unwrap();
    let q5 = &qs[5];
    let mut state = TestState::default();
    state.answers.insert(
        q5.id.clone(),
        AnswerState {
            choice: Some((q5.answer + 1) % 4),
            marked: false,
            visited: true,
            time_ms: 1,
        },
    );
    let mut u = u;
    mock::submit(&c, &mut u, id, &state, 0).unwrap();
    assert!(srs::card(&u, &q5.id).unwrap().is_some());
    assert_eq!(
        practice::stats(&c, &u).unwrap().due,
        0,
        "due 10 minutes later, not yet"
    );
}

#[test]
fn streaks_heatmap_weak_topics_and_goal() {
    let (c, u) = setup();
    let qs = practice::questions_for_topic(&c, TOPIC, "en").unwrap();
    // Activity today, yesterday, 2 days ago and 5 days ago (local days).
    for (days_ago, q) in [
        (0, &qs[0]),
        (1, &qs[1]),
        (2, &qs[2]),
        (5, &qs[3]),
        (5, &qs[4]),
    ] {
        u.execute(
            "INSERT INTO attempts (question_id, chosen, correct, time_ms, mode, created_at)
             VALUES (?1, ?2, 0, 100, 'practice', unixepoch('now', ?3))",
            rusqlite::params![q.id, (q.answer + 1) % 4, format!("-{days_ago} days")],
        )
        .unwrap();
    }
    let v = progress::view(&c, &u, "bn").unwrap();
    assert_eq!((v.streak, v.best_streak), (3, 3));
    assert_eq!(v.days.len() as i64, progress::HEATMAP_DAYS);
    assert_eq!(
        v.days.last().unwrap().attempts,
        1,
        "today is the last heatmap cell"
    );
    assert_eq!(v.today, 1);
    assert_eq!(v.total_attempts, 5);
    let t = &v.topics[0];
    assert_eq!(
        (t.title.as_str(), t.attempted, t.correct, t.accuracy),
        ("১৮৫৭ সালের মহাবিদ্রোহ", 5, 0, 0.0)
    );
    assert_eq!(
        v.weak,
        vec![TOPIC.to_string()],
        "5 tried, all wrong -> weak"
    );
    assert_eq!(v.daily_goal, 20);
    settings::set(&u, "daily_goal", "35").unwrap();
    assert!(settings::set(&u, "daily_goal", "0").is_err());
    assert_eq!(progress::view(&c, &u, "en").unwrap().daily_goal, 35);
}

#[test]
fn no_activity_today_keeps_yesterdays_streak_alive() {
    let (c, u) = setup();
    let q = &practice::questions_for_topic(&c, TOPIC, "en").unwrap()[0];
    for days_ago in [1, 2] {
        u.execute(
            "INSERT INTO attempts (question_id, chosen, correct, time_ms, mode, created_at)
             VALUES (?1, ?2, 1, 100, 'practice', unixepoch('now', ?3))",
            rusqlite::params![q.id, q.answer, format!("-{days_ago} days")],
        )
        .unwrap();
    }
    let v = progress::view(&c, &u, "en").unwrap();
    assert_eq!((v.streak, v.today), (2, 0));
    assert!(v.weak.is_empty());
}
