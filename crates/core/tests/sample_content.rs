//! Integration tests against the real sample content in `content/`.

use feb_core::{db, import, library, practice, settings};
use std::path::PathBuf;

fn content_dir() -> PathBuf {
    PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../../content")
}

fn setup() -> (rusqlite::Connection, rusqlite::Connection) {
    let (mut c, u) = db::open_in_memory().unwrap();
    let report = import::import_dir(&mut c, &content_dir()).unwrap();
    assert!(report.topics >= 1 && report.questions >= 12, "{report:?}");
    (c, u)
}

const TOPIC: &str = "hist.modern.revolt-1857";

#[test]
fn library_tree_in_bengali() {
    let (c, u) = setup();
    let tree = library::tree(&c, &u, "bn").unwrap();
    let hist = tree.iter().find(|s| s.id == "hist").unwrap();
    assert_eq!(hist.title, "ইতিহাস");
    let topic = &hist.units[0].topics[0];
    assert_eq!(topic.title, "১৮৫৭ সালের মহাবিদ্রোহ");
    assert_eq!(topic.question_count, 12);
}

#[test]
fn notes_have_same_anchors_in_both_languages() {
    let (c, _) = setup();
    let en = library::topic(&c, TOPIC, "en").unwrap();
    let bn = library::topic(&c, TOPIC, "bn").unwrap();
    assert_eq!(bn.lang, "bn");
    let a = |t: &feb_core::model::TopicView| {
        t.sections
            .iter()
            .map(|s| s.anchor.clone())
            .collect::<Vec<_>>()
    };
    assert_eq!(a(&en), a(&bn));
    assert_eq!(en.sections.len(), 7);
    assert!(bn.sections[0].heading.contains("পটভূমি"));
}

#[test]
fn missing_language_falls_back_to_english() {
    let (c, _) = setup();
    // No Tamil notes or questions exist.
    let t = library::topic(&c, TOPIC, "ta").unwrap();
    assert_eq!(t.lang, "en");
    // Hindi is only complete for q0001; the rest must fall back to English as a whole.
    let qs = practice::questions_for_topic(&c, TOPIC, "hi").unwrap();
    assert_eq!(qs[0].lang, "hi");
    assert!(qs[1..].iter().all(|q| q.lang == "en"));
}

#[test]
fn grading_progress_and_mistakes() {
    let (c, u) = setup();
    let qs = practice::questions_for_topic(&c, TOPIC, "bn").unwrap();
    let q0 = &qs[0];
    assert_eq!(q0.options.as_ref().unwrap()[0], "মিরাট");

    let wrong = (q0.answer + 1) % 4;
    let r = practice::record_attempt(&c, &u, &q0.id, wrong, 1200, "practice").unwrap();
    assert!(!r.correct);
    assert_eq!(practice::mistakes(&c, &u, "en").unwrap().len(), 1);

    // Answer correctly later → leaves the mistake notebook.
    assert!(
        practice::record_attempt(&c, &u, &q0.id, q0.answer, 900, "practice")
            .unwrap()
            .correct
    );
    assert!(practice::mistakes(&c, &u, "en").unwrap().is_empty());

    let s = practice::stats(&c, &u).unwrap();
    assert_eq!((s.attempted, s.correct, s.total_attempts), (1, 1, 2));
    assert!(practice::record_attempt(&c, &u, &q0.id, 9, 1, "practice").is_err());
}

#[test]
fn settings_are_validated() {
    let (_, u) = setup();
    assert_eq!(settings::get_all(&u).unwrap()["lang"], "en");
    settings::set(&u, "lang", "bn").unwrap();
    assert_eq!(settings::get_all(&u).unwrap()["lang"], "bn");
    assert!(settings::set(&u, "lang", "xx").is_err());
    assert!(settings::set(&u, "nope", "1").is_err());
}

#[test]
fn sections_parser_ignores_fenced_headings() {
    let md = "# T\n\n## A {#a}\ntext\n```\n## not {#x}\n```\n## B {#b}\nmore\n";
    let s = import::parse_sections(md);
    assert_eq!(
        s.iter().map(|x| x.0.as_str()).collect::<Vec<_>>(),
        ["a", "b"]
    );
}
