//! Source-file shapes (deserialized from YAML) and view shapes (serialized to the UI).

use crate::localize::{Localized, pick, pick_opt, pick_vec};
use serde::{Deserialize, Serialize};

// ---------- Source files (content/) ----------

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SubjectFile {
    pub id: String,
    pub title: Localized,
    pub order: i64,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct UnitFile {
    pub id: String,
    pub subject: String,
    pub title: Localized,
    pub order: i64,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TopicFile {
    pub id: String,
    pub title: Localized,
    #[serde(default)]
    pub summary: Option<Localized>,
    pub order: i64,
    pub exams: Vec<String>,
    #[serde(default)]
    pub estimated_minutes: Option<i64>,
    pub version: String,
    pub status: String,
    #[serde(default)]
    pub sources: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TopicMeta {
    pub exams: Vec<String>,
    pub estimated_minutes: Option<i64>,
    pub version: String,
    pub status: String,
    pub sources: Vec<String>,
}

/// A question exactly as written in `questions.yaml` (all languages).
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RawQuestion {
    pub id: String,
    #[serde(rename = "type")]
    pub kind: String,
    pub difficulty: u8,
    pub exams: Vec<String>,
    pub refs: Vec<String>,
    #[serde(default)]
    pub stem: Option<Localized>,
    #[serde(default)]
    pub question: Option<Localized>,
    #[serde(default)]
    pub statements: Option<Vec<Localized>>,
    #[serde(default)]
    pub left: Option<Vec<Localized>>,
    #[serde(default)]
    pub right: Option<Vec<Localized>>,
    #[serde(default)]
    pub items: Option<Vec<Localized>>,
    #[serde(default)]
    pub assertion: Option<Localized>,
    #[serde(default)]
    pub reason: Option<Localized>,
    #[serde(default)]
    pub options: Option<Vec<Localized>>,
    pub answer: u8,
    pub explanation: Localized,
    pub status: String,
    #[serde(default)]
    pub as_of: Option<String>,
    #[serde(default)]
    pub source: Option<String>,
}

impl RawQuestion {
    fn localized_fields(&self) -> Vec<&Localized> {
        let mut v: Vec<&Localized> = vec![&self.explanation];
        for one in [&self.stem, &self.question, &self.assertion, &self.reason]
            .into_iter()
            .flatten()
        {
            v.push(one);
        }
        for list in [
            &self.statements,
            &self.left,
            &self.right,
            &self.items,
            &self.options,
        ]
        .into_iter()
        .flatten()
        {
            v.extend(list.iter());
        }
        v
    }

    /// True when every text field has `lang`. Partial translations are never shown
    /// (docs/CONTENT_GUIDELINES.md §7).
    pub fn is_complete_in(&self, lang: &str) -> bool {
        self.localized_fields()
            .iter()
            .all(|m| m.get(lang).is_some_and(|s| !s.trim().is_empty()))
    }

    /// Resolve to a single language, falling back to English for the whole question.
    pub fn resolve(&self, full_id: &str, topic_id: &str, lang: &str) -> QuestionView {
        let lang = if self.is_complete_in(lang) {
            lang
        } else {
            "en"
        };
        QuestionView {
            id: full_id.to_string(),
            topic_id: topic_id.to_string(),
            kind: self.kind.clone(),
            difficulty: self.difficulty,
            status: self.status.clone(),
            lang: lang.to_string(),
            refs: self.refs.clone(),
            stem: pick_opt(&self.stem, lang),
            question: pick_opt(&self.question, lang),
            statements: pick_vec(&self.statements, lang),
            left: pick_vec(&self.left, lang),
            right: pick_vec(&self.right, lang),
            items: pick_vec(&self.items, lang),
            assertion: pick_opt(&self.assertion, lang),
            reason: pick_opt(&self.reason, lang),
            options: pick_vec(&self.options, lang),
            answer: self.answer,
            explanation: pick(&self.explanation, lang),
            as_of: self.as_of.clone(),
            source: self.source.clone(),
        }
    }
}

// ---------- Views (sent to the UI) ----------

#[derive(Debug, Clone, Serialize)]
pub struct QuestionView {
    pub id: String,
    pub topic_id: String,
    pub kind: String,
    pub difficulty: u8,
    pub status: String,
    /// Language this question is actually shown in (may fall back to "en").
    pub lang: String,
    pub refs: Vec<String>,
    pub stem: Option<String>,
    pub question: Option<String>,
    pub statements: Option<Vec<String>>,
    pub left: Option<Vec<String>>,
    pub right: Option<Vec<String>>,
    pub items: Option<Vec<String>>,
    pub assertion: Option<String>,
    pub reason: Option<String>,
    /// `None` for assertion-reason: the UI supplies the four standard options.
    pub options: Option<Vec<String>>,
    pub answer: u8,
    pub explanation: String,
    pub as_of: Option<String>,
    pub source: Option<String>,
}

#[derive(Debug, Clone, Serialize)]
pub struct TopicSummary {
    pub id: String,
    pub title: String,
    pub summary: Option<String>,
    pub status: String,
    pub estimated_minutes: Option<i64>,
    pub question_count: i64,
    pub attempted: i64,
    pub correct: i64,
}

#[derive(Debug, Clone, Serialize)]
pub struct LibraryUnit {
    pub id: String,
    pub title: String,
    pub topics: Vec<TopicSummary>,
}

#[derive(Debug, Clone, Serialize)]
pub struct LibrarySubject {
    pub id: String,
    pub title: String,
    pub units: Vec<LibraryUnit>,
}

#[derive(Debug, Clone, Serialize)]
pub struct NoteSection {
    pub anchor: String,
    pub heading: String,
    pub body_md: String,
}

#[derive(Debug, Clone, Serialize)]
pub struct TopicView {
    pub id: String,
    pub title: String,
    pub summary: Option<String>,
    pub subject_id: String,
    pub subject_title: String,
    pub unit_id: String,
    pub unit_title: String,
    /// Language the notes are shown in (may fall back to "en").
    pub lang: String,
    pub available_langs: Vec<String>,
    pub sections: Vec<NoteSection>,
    pub meta: TopicMeta,
    pub question_count: i64,
}

#[derive(Debug, Clone, Serialize)]
pub struct AttemptResult {
    pub correct: bool,
    pub answer: u8,
    /// In revision, a correct answer asks the user to grade recall: next-review times
    /// (seconds) for each grade. None otherwise.
    pub srs: Option<crate::srs::Preview>,
}

#[derive(Debug, Clone, Default, Serialize)]
pub struct Stats {
    pub topics: i64,
    pub questions: i64,
    pub attempted: i64,
    pub correct: i64,
    pub mistakes: i64,
    pub total_attempts: i64,
    /// Spaced-repetition cards due now.
    pub due: i64,
}
