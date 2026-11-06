//! Keyword search against the real sample content.

use feb_core::{db, import, search};
use std::path::PathBuf;

fn setup() -> rusqlite::Connection {
    let (mut c, _) = db::open_in_memory().unwrap();
    import::import_dir(
        &mut c,
        &PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../../content"),
    )
    .unwrap();
    c
}

fn kinds(hits: &[search::SearchHit]) -> Vec<(String, String)> {
    hits.iter()
        .map(|h| (h.kind.clone(), h.r#ref.clone()))
        .collect()
}

#[test]
fn finds_sections_questions_and_topics_in_english() {
    let c = setup();
    let hits = search::search(&c, "Meerut", "en", 20).unwrap();
    let k = kinds(&hits);
    assert!(k.contains(&("section".into(), "outbreak".into())), "{k:?}");
    assert!(
        k.contains(&("question".into(), "hist.modern.revolt-1857/q0001".into())),
        "{k:?}"
    );
    assert!(
        hits.iter()
            .all(|h| h.lang == "en" && h.topic_title == "The Revolt of 1857")
    );
    // Matches are marked for highlighting.
    assert!(
        hits.iter()
            .any(|h| h.snippet.contains('\u{2}') || h.title.contains("Meerut"))
    );
    let topic = search::search(&c, "revolt 1857", "en", 20).unwrap();
    assert_eq!(
        topic[0].kind,
        "topic",
        "title matches rank first: {:?}",
        kinds(&topic)
    );
}

#[test]
fn bengali_prefix_digits_and_english_terms() {
    let c = setup();
    // Bengali, with a suffix in the text ("মিরাটের").
    let hits = search::search(&c, "মিরাট", "bn", 20).unwrap();
    assert!(
        hits.iter()
            .any(|h| h.kind == "section" && h.r#ref == "outbreak" && h.lang == "bn")
    );
    // Prefix match handles inflection: "বিদ্রোহ" finds "বিদ্রোহের", "বিদ্রোহী"...
    assert!(!search::search(&c, "বিদ্রোহ", "bn", 20).unwrap().is_empty());
    // ASCII digits find Bengali digits and vice versa.
    let d1 = search::search(&c, "1858 ভারত শাসন", "bn", 20).unwrap();
    assert!(
        d1.iter().any(|h| h.lang == "bn"),
        "ASCII digits should match ১৮৫৮"
    );
    let d2 = search::search(&c, "১৮৫৮ Canning", "en", 20).unwrap();
    assert!(
        !d2.is_empty(),
        "Bengali digits should match 1858 in English text"
    );
    // English term while Bengali content is selected: found in the Bengali notes
    // (which carry the English term in brackets), shown in Bengali.
    let lapse = search::search(&c, "Doctrine of Lapse", "bn", 20).unwrap();
    assert!(
        lapse.iter().any(|h| h.r#ref == "causes" && h.lang == "bn"),
        "{:?}",
        kinds(&lapse)
    );
    // Items that exist in Bengali are titled in Bengali even when only English matched.
    assert!(lapse.iter().all(|h| h.lang == "bn"), "{lapse:?}");
    assert!(lapse.iter().any(|h| h.snippet_lang == "en"));
    // Each item appears once.
    let mut k = kinds(&lapse);
    let n = k.len();
    k.sort();
    k.dedup();
    assert_eq!(n, k.len());
}

#[test]
fn odd_input_is_safe() {
    let c = setup();
    for q in [
        "", "   ", "\"", "***", "a\"b", "NOT", "OR AND", "(", "Meerut\"",
    ] {
        search::search(&c, q, "en", 10).unwrap();
    }
    assert!(search::fts_query("  ").is_none());
    assert_eq!(
        search::fts_query("Mangal \"Pandey").unwrap(),
        "\"Mangal\"* \"Pandey\"*"
    );
    assert_eq!(search::normalize("১৮৫৭"), "1857");
}

#[test]
fn index_follows_pack_install_and_remove() {
    let c0 = setup();
    let dir = std::env::temp_dir().join(format!("feb-search-{}", std::process::id()));
    std::fs::create_dir_all(&dir).unwrap();
    let subjects =
        import::load_dir(&PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../../content")).unwrap();
    let (s, u) = (&subjects[0], &subjects[0].units[0]);
    let t = &u.topics[0];
    let pack = dir.join("p.db");
    feb_core::packs::build_pack_db(&pack, s, u, t).unwrap();
    drop(c0);

    let (mut c, _) = db::open_in_memory().unwrap();
    assert!(search::search(&c, "Meerut", "en", 5).unwrap().is_empty());
    feb_core::packs::install_pack_db(&mut c, &pack, &t.topic.id, &t.topic.version, "x", 1).unwrap();
    let n1 = search::search(&c, "Meerut", "en", 50).unwrap().len();
    assert!(n1 > 0);
    // Re-install doesn't duplicate index rows.
    feb_core::packs::install_pack_db(&mut c, &pack, &t.topic.id, &t.topic.version, "y", 1).unwrap();
    assert_eq!(search::search(&c, "Meerut", "en", 50).unwrap().len(), n1);
    feb_core::packs::remove_pack(&mut c, &t.topic.id).unwrap();
    assert!(search::search(&c, "Meerut", "en", 5).unwrap().is_empty());
    std::fs::remove_dir_all(&dir).ok();
}

#[test]
fn bengali_words_are_whole_tokens_not_fragments() {
    let c = setup();
    // The word index must hold whole Bengali words (vowel signs/virama inside the word).
    c.execute_batch("CREATE VIRTUAL TABLE temp.vocab USING fts5vocab(main, search_index, 'row');")
        .unwrap();
    let has = |w: &str| -> bool {
        c.query_row(
            "SELECT COUNT(*) FROM temp.vocab WHERE term = ?1",
            [w],
            |r| r.get::<_, i64>(0),
        )
        .unwrap()
            > 0
    };
    assert!(has("মিরাটের"), "whole inflected word indexed");
    assert!(has("মহাবিদ্রোহের"));
    assert!(!has("মহ"), "no consonant fragments");
}

#[test]
fn display_keeps_bengali_digits_and_substring_fallback_works() {
    let c = setup();
    let hits = search::search(&c, "মহাবিদ্রোহ", "bn", 20).unwrap();
    let topic = hits.iter().find(|h| h.kind == "topic").expect("topic hit");
    assert_eq!(
        topic.title, "১৮৫৭ সালের মহাবিদ্রোহ",
        "titles keep Bengali digits"
    );
    // "দ্রোহ" is inside words only (বিদ্রোহ, মহাবিদ্রোহের): found by the trigram fallback.
    let sub = search::search(&c, "দ্রোহ", "bn", 20).unwrap();
    assert!(!sub.is_empty(), "substring fallback");
    assert!(sub.iter().all(|h| h.lang == "bn"));
    // A word that appears nowhere finds nothing (no fragment false positives).
    assert!(search::search(&c, "কম্পিউটার", "bn", 20).unwrap().is_empty());
}
