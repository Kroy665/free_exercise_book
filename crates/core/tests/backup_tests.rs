//! Progress export / import / reset, and the first-run settings.

use feb_core::{backup, db, import, practice, settings, srs};
use std::path::PathBuf;

const TOPIC: &str = "hist.modern.revolt-1857";

fn tmpdir(name: &str) -> PathBuf {
    let d = std::env::temp_dir().join(format!("feb-backup-{name}-{}", std::process::id()));
    let _ = std::fs::remove_dir_all(&d);
    std::fs::create_dir_all(&d).unwrap();
    d
}

#[test]
fn export_reset_import_round_trip() {
    let dir = tmpdir("rt");
    let (mut c, _) = db::open_in_memory().unwrap();
    import::import_dir(
        &mut c,
        &PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../../content"),
    )
    .unwrap();
    let mut u = db::open_user(&dir.join("user.db")).unwrap();
    let qs = practice::questions_for_topic(&c, TOPIC, "en").unwrap();
    for q in &qs[..4] {
        practice::record_attempt(&c, &u, &q.id, (q.answer + 1) % 4, 100, "practice").unwrap(); // wrong -> card
    }
    settings::set(&u, "daily_goal", "42").unwrap();

    let file = dir.join("progress.febackup");
    backup::export(&u, &file).unwrap();
    backup::reset(&mut u).unwrap();
    assert_eq!(practice::stats(&c, &u).unwrap().total_attempts, 0);
    assert_eq!(srs::due_count(&u, i64::MAX).unwrap(), 0);
    assert_eq!(
        settings::get_all(&u).unwrap()["daily_goal"],
        "42",
        "reset keeps settings"
    );

    settings::set(&u, "daily_goal", "7").unwrap();
    let s = backup::import(&mut u, &file, &dir.join("backups")).unwrap();
    assert_eq!((s.attempts, s.tests, s.cards), (4, 0, 4));
    assert_eq!(practice::stats(&c, &u).unwrap().total_attempts, 4);
    assert_eq!(
        settings::get_all(&u).unwrap()["daily_goal"],
        "42",
        "settings restored"
    );
    // The replaced progress was saved first (so an import can be undone).
    assert!(std::path::Path::new(&s.previous_backup).exists());
    std::fs::remove_dir_all(&dir).ok();
}

#[test]
fn rejects_bad_and_newer_backups() {
    let dir = tmpdir("bad");
    let mut u = db::open_user(&dir.join("user.db")).unwrap();
    let junk = dir.join("junk.febackup");
    std::fs::write(&junk, b"definitely not sqlite").unwrap();
    assert!(backup::import(&mut u, &junk, &dir.join("b")).is_err());

    // A backup written by a newer app (higher schema version) is refused.
    let newer = dir.join("newer.febackup");
    backup::export(&u, &newer).unwrap();
    rusqlite::Connection::open(&newer)
        .unwrap()
        .pragma_update(None, "user_version", 999)
        .unwrap();
    let err = backup::import(&mut u, &newer, &dir.join("b"))
        .unwrap_err()
        .to_string();
    assert!(err.contains("newer version"), "{err}");
    std::fs::remove_dir_all(&dir).ok();
}

#[test]
fn first_run_settings_are_validated() {
    let (_, u) = db::open_in_memory().unwrap();
    let s = settings::get_all(&u).unwrap();
    assert_eq!((s["onboarded"].as_str(), s["exams"].as_str()), ("0", ""));
    settings::set(&u, "exams", "upsc-cse,wbcs").unwrap();
    settings::set(&u, "onboarded", "1").unwrap();
    assert!(settings::set(&u, "exams", "upsc-cse,bogus").is_err());
    assert!(settings::set(&u, "onboarded", "yes").is_err());
}

#[test]
fn upgrading_an_old_progress_db_keeps_a_backup_first() {
    let dir = tmpdir("mig");
    let file = dir.join("user.db");
    {
        let u = db::open_user(&file).unwrap();
        u.execute(
            "INSERT INTO attempts (question_id, chosen, correct, time_ms, mode) VALUES ('x/q1', 0, 1, 1, 'practice')",
            [],
        )
        .unwrap();
        // Pretend it was written by an older app (schema version 1).
        u.pragma_update(None, "user_version", 1).unwrap();
    }
    // Re-applying migrations 2.. on a v1 file fails if tables exist, so only check the copy
    // was taken before migrating by observing the backups folder.
    let _ = db::open_user(&file);
    let backups: Vec<_> = std::fs::read_dir(dir.join("backups"))
        .unwrap()
        .flatten()
        .collect();
    assert_eq!(backups.len(), 1);
    let name = backups[0].file_name().into_string().unwrap();
    assert!(name.starts_with("user-before-v2-"), "{name}");
    let copy = rusqlite::Connection::open(backups[0].path()).unwrap();
    let n: i64 = copy
        .query_row("SELECT COUNT(*) FROM attempts", [], |r| r.get(0))
        .unwrap();
    assert_eq!(n, 1, "the backup holds the user's data");
    std::fs::remove_dir_all(&dir).ok();
}
