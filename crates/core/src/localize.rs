use std::collections::BTreeMap;

/// Text in several languages: `{ "en": "...", "bn": "..." }`.
pub type Localized = BTreeMap<String, String>;

/// Pick `lang`, falling back to English, then to any available language.
pub fn pick(map: &Localized, lang: &str) -> String {
    map.get(lang)
        .or_else(|| map.get("en"))
        .or_else(|| map.values().next())
        .cloned()
        .unwrap_or_default()
}

pub fn pick_opt(map: &Option<Localized>, lang: &str) -> Option<String> {
    map.as_ref().map(|m| pick(m, lang))
}

pub fn pick_vec(list: &Option<Vec<Localized>>, lang: &str) -> Option<Vec<String>> {
    list.as_ref()
        .map(|l| l.iter().map(|m| pick(m, lang)).collect())
}
