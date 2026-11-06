use crate::{CoreError, Result, SUPPORTED_LANGS};

/// Exam families the user can choose in first-run setup (docs/CONTENT_STRUCTURE.md §7).
pub const EXAM_TAGS: &[&str] = &[
    "upsc-cse",
    "wbcs",
    "state-psc",
    "ssc-cgl",
    "ssc-chsl",
    "ibps-po",
    "rrb-ntpc",
];
use rusqlite::{Connection, params};
use std::collections::BTreeMap;

/// Allowed keys and their defaults.
const DEFAULTS: &[(&str, &str)] = &[
    ("lang", "en"),       // content language (the UI is always English)
    ("theme", "system"),  // system | light | dark
    ("font_size", "16"),  // 14..=22 px
    ("daily_goal", "20"), // questions per day
    ("onboarded", "0"),   // first-run setup finished
    ("exams", ""),        // comma-separated exam tags the user prepares for
];

pub fn get_all(user: &Connection) -> Result<BTreeMap<String, String>> {
    let mut map: BTreeMap<String, String> = DEFAULTS
        .iter()
        .map(|(k, v)| (k.to_string(), v.to_string()))
        .collect();
    let mut stmt = user.prepare("SELECT key, value FROM settings")?;
    for row in stmt.query_map([], |r| Ok((r.get::<_, String>(0)?, r.get::<_, String>(1)?)))? {
        let (k, v) = row?;
        if map.contains_key(&k) {
            map.insert(k, v);
        }
    }
    Ok(map)
}

fn validate(key: &str, value: &str) -> Result<()> {
    let ok = match key {
        "lang" => SUPPORTED_LANGS.contains(&value),
        "theme" => matches!(value, "system" | "light" | "dark"),
        "font_size" => value.parse::<u8>().is_ok_and(|n| (14..=22).contains(&n)),
        "daily_goal" => value.parse::<u16>().is_ok_and(|n| (1..=500).contains(&n)),
        "onboarded" => matches!(value, "0" | "1"),
        "exams" => value.is_empty() || value.split(',').all(|e| EXAM_TAGS.contains(&e)),
        _ => return Err(CoreError::Invalid(format!("unknown setting '{key}'"))),
    };
    if ok {
        Ok(())
    } else {
        Err(CoreError::Invalid(format!(
            "bad value '{value}' for '{key}'"
        )))
    }
}

pub fn set(user: &Connection, key: &str, value: &str) -> Result<()> {
    validate(key, value)?;
    user.execute(
        "INSERT INTO settings (key, value) VALUES (?1, ?2) ON CONFLICT(key) DO UPDATE SET value = excluded.value",
        params![key, value],
    )?;
    Ok(())
}
