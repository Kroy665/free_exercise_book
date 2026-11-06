use crate::{CoreError, Result, SUPPORTED_LANGS};
use rusqlite::{Connection, params};
use std::collections::BTreeMap;

/// Allowed keys and their defaults.
const DEFAULTS: &[(&str, &str)] = &[
    ("lang", "en"),      // content language (the UI is always English)
    ("theme", "system"), // system | light | dark
    ("font_size", "16"), // 14..=22 px
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
