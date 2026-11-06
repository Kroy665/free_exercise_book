//! Thin IPC layer: validate input, call `feb_core`, map errors. No SQL, no rules here.

use crate::state::AppState;
use feb_core::error::ErrorPayload;
use feb_core::model::{AttemptResult, LibrarySubject, QuestionView, Stats, TopicView};
use feb_core::{CoreError, library, practice, settings};
use std::collections::BTreeMap;
use tauri::State;

type CmdResult<T> = Result<T, ErrorPayload>;

fn e(err: CoreError) -> ErrorPayload {
    ErrorPayload::from(&err)
}

#[tauri::command]
pub async fn library_tree(
    state: State<'_, AppState>,
    lang: String,
) -> CmdResult<Vec<LibrarySubject>> {
    library::tree(&*state.content()?, &*state.user()?, &lang).map_err(e)
}

#[tauri::command]
pub async fn topic_get(
    state: State<'_, AppState>,
    id: String,
    lang: String,
) -> CmdResult<TopicView> {
    library::topic(&*state.content()?, &id, &lang).map_err(e)
}

#[tauri::command]
pub async fn practice_questions(
    state: State<'_, AppState>,
    topic_id: String,
    lang: String,
) -> CmdResult<Vec<QuestionView>> {
    practice::questions_for_topic(&*state.content()?, &topic_id, &lang).map_err(e)
}

#[tauri::command]
pub async fn practice_record(
    state: State<'_, AppState>,
    question_id: String,
    chosen: u8,
    time_ms: u32,
    mode: String,
) -> CmdResult<AttemptResult> {
    if !matches!(mode.as_str(), "practice" | "revise") {
        return Err(e(CoreError::Invalid(format!("unknown mode '{mode}'"))));
    }
    practice::record_attempt(
        &*state.content()?,
        &*state.user()?,
        &question_id,
        chosen,
        time_ms,
        &mode,
    )
    .map_err(e)
}

#[tauri::command]
pub async fn mistakes_list(
    state: State<'_, AppState>,
    lang: String,
) -> CmdResult<Vec<QuestionView>> {
    practice::mistakes(&*state.content()?, &*state.user()?, &lang).map_err(e)
}

#[tauri::command]
pub async fn stats_get(state: State<'_, AppState>) -> CmdResult<Stats> {
    practice::stats(&*state.content()?, &*state.user()?).map_err(e)
}

#[tauri::command]
pub async fn settings_get(state: State<'_, AppState>) -> CmdResult<BTreeMap<String, String>> {
    settings::get_all(&*state.user()?).map_err(e)
}

#[tauri::command]
pub async fn settings_set(state: State<'_, AppState>, key: String, value: String) -> CmdResult<()> {
    settings::set(&*state.user()?, &key, &value).map_err(e)
}

#[tauri::command]
pub async fn search(
    state: State<'_, AppState>,
    query: String,
    lang: String,
) -> CmdResult<Vec<feb_core::search::SearchHit>> {
    if query.chars().count() > 200 {
        return Ok(Vec::new());
    }
    feb_core::search::search(&*state.content()?, &query, &lang, 30).map_err(e)
}
