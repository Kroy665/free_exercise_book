use crate::{CoreError, Result, SUPPORTED_LANGS};

/// Exam families the user can choose in first-run setup (docs/CONTENT_STRUCTURE.md §7).
pub const EXAM_TAGS: &[&str] = &[
    "slst-0910",
    "slst-1112",
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
    ("auto_update", "1"), // download new and updated topics when the app starts
    ("assistant", "ollama"),                     // off | ollama | claude
    ("ollama_url", "http://127.0.0.1:11434"),    // local Ollama server
    ("ollama_model", "qwen2.5:3b"),              // any model the user has pulled
    ("claude_model", "claude-opus-5-5"),         // Claude API model id
    ("tts_voice", "af_heart"),                   // Kokoro voice
    ("tts_speed", "1"),                          // 0.7..=1.5
];

/// Kokoro voices the app offers (files are downloaded on first use).
pub const TTS_VOICES: &[&str] = &["af_heart", "af_bella", "bf_emma", "am_michael", "bm_george"];

fn model_name(v: &str) -> bool {
    !v.is_empty() && v.len() <= 100 && v.chars().all(|c| c.is_ascii_alphanumeric() || "._:/-".contains(c))
}

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
        "onboarded" | "auto_update" => matches!(value, "0" | "1"),
        "assistant" => matches!(value, "off" | "ollama" | "claude"),
        "ollama_url" => {
            value.len() <= 200
                && (value.starts_with("http://") || value.starts_with("https://"))
                && !value.contains(char::is_whitespace)
        }
        "ollama_model" | "claude_model" => model_name(value),
        "tts_voice" => TTS_VOICES.contains(&value),
        "tts_speed" => value.parse::<f32>().is_ok_and(|n| (0.7..=1.5).contains(&n)),
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
