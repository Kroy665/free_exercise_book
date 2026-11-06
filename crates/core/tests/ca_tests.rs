//! Current-affairs months against the real October 2026 content.

use feb_core::{ca, db, import, library, practice, search};
use std::path::PathBuf;

const MONTH: &str = "ca.2026.10";

fn content_dir() -> PathBuf {
    PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../../content")
}

#[test]
fn months_items_sections_and_quiz() {
    let (mut c, u) = db::open_in_memory().unwrap();
    import::import_dir(&mut c, &content_dir()).unwrap();

    let months = ca::months(&c, &u, "en").unwrap();
    assert_eq!(months.len(), 1);
    let m = &months[0];
    assert_eq!(
        (m.topic_id.as_str(), m.title.as_str(), m.items, m.questions),
        (MONTH, "October 2026", 5, 8)
    );
    assert!(m.categories.contains(&"awards".to_string()));

    // Items newest first, in Bengali, with sources.
    let v = ca::month(&c, MONTH, "bn").unwrap();
    assert_eq!(v.title, "অক্টোবর ২০২৬");
    assert_eq!(v.items.first().unwrap().date, "2026-10-30");
    assert!(v.items.windows(2).all(|w| w[0].date >= w[1].date));
    assert!(
        v.items
            .iter()
            .all(|i| i.lang == "bn" && i.source.starts_with("https://"))
    );
    assert!(v.items.iter().any(|i| i.title.contains("রেপো")));

    // Items also exist as note sections (notes reader, "Revise in notes" links).
    let notes = library::topic(&c, MONTH, "en").unwrap();
    assert_eq!(notes.sections.len(), 5);
    let rbi = notes.sections.iter().find(|s| s.anchor == "i001").unwrap();
    assert!(rbi.body_md.contains(":::keyfacts") && rbi.body_md.contains(":::asof 2026-10-07"));
    assert!(rbi.body_md.contains("(https://rbi.org.in/"));

    // The quiz is ordinary practice; every CA question cites a source.
    let qs = practice::questions_for_topic(&c, MONTH, "bn").unwrap();
    assert_eq!(qs.len(), 8);
    assert!(
        qs.iter()
            .all(|q| q.source.is_some() && q.as_of.is_some() && q.lang == "bn")
    );

    // Searchable, and not shown as a Library subject's unit/topic mix-up.
    let hits = search::search(&c, "repo rate", "en", 10).unwrap();
    assert!(hits.iter().any(|h| h.topic_id == MONTH));
    let tree = library::tree(&c, &u, "en").unwrap();
    assert!(
        tree.iter().any(|s| s.id == "ca"),
        "CA is a subject (the UI hides it from Library)"
    );
}

#[test]
fn month_pack_round_trip_keeps_items() {
    let subjects = import::load_dir(&content_dir()).unwrap();
    let s = subjects.iter().find(|s| s.subject.id == "ca").unwrap();
    let u = &s.units[0];
    let t = &u.topics[0];
    assert_eq!(t.ca_items.len(), 5);
    let dir = std::env::temp_dir().join(format!("feb-ca-{}", std::process::id()));
    std::fs::create_dir_all(&dir).unwrap();
    let pack = dir.join("ca.db");
    feb_core::packs::build_pack_db(&pack, s, u, t).unwrap();

    let (mut c, user) = db::open_in_memory().unwrap();
    feb_core::packs::install_pack_db(&mut c, &pack, MONTH, &t.topic.version, "x", 1).unwrap();
    assert_eq!(ca::month(&c, MONTH, "en").unwrap().items.len(), 5);
    assert_eq!(ca::months(&c, &user, "en").unwrap()[0].questions, 8);
    // Re-install doesn't duplicate; remove clears items.
    feb_core::packs::install_pack_db(&mut c, &pack, MONTH, &t.topic.version, "y", 1).unwrap();
    assert_eq!(ca::month(&c, MONTH, "en").unwrap().items.len(), 5);
    feb_core::packs::remove_pack(&mut c, MONTH).unwrap();
    assert!(ca::months(&c, &user, "en").unwrap().is_empty());
    let n: i64 = c
        .query_row("SELECT COUNT(*) FROM ca_items", [], |r| r.get(0))
        .unwrap();
    assert_eq!(n, 0);
    std::fs::remove_dir_all(&dir).ok();
}
