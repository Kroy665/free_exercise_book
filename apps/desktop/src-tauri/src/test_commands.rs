//! IPC commands for mock tests (thin wrappers over `feb_core::mock`).

use crate::state::AppState;
use feb_core::error::ErrorPayload;
use feb_core::mock::{
    self, CustomSpec, PatternView, TestListItem, TestResult, TestSession, TestState, TestSummary,
};
use serde::Serialize;
use tauri::State;

type CmdResult<T> = Result<T, ErrorPayload>;

fn e(err: feb_core::CoreError) -> ErrorPayload {
    ErrorPayload::from(&err)
}

#[derive(Serialize)]
pub struct TestsOverview {
    pub patterns: Vec<PatternView>,
    pub tests: Vec<TestListItem>,
}

#[tauri::command]
pub async fn tests_overview(state: State<'_, AppState>, lang: String) -> CmdResult<TestsOverview> {
    Ok(TestsOverview {
        patterns: mock::pattern_views(&*state.content()?, &lang).map_err(e)?,
        tests: mock::list(&*state.user()?).map_err(e)?,
    })
}

#[tauri::command]
pub async fn tests_create_custom(state: State<'_, AppState>, spec: CustomSpec) -> CmdResult<i64> {
    mock::create_custom(&*state.content()?, &*state.user()?, &spec).map_err(e)
}

#[tauri::command]
pub async fn tests_create_pattern(
    state: State<'_, AppState>,
    pattern_id: String,
) -> CmdResult<i64> {
    mock::create_from_pattern(&*state.content()?, &*state.user()?, &pattern_id).map_err(e)
}

#[tauri::command]
pub async fn test_session(
    state: State<'_, AppState>,
    id: i64,
    lang: String,
) -> CmdResult<TestSession> {
    mock::session(&*state.content()?, &*state.user()?, id, &lang).map_err(e)
}

#[tauri::command]
pub async fn test_start(state: State<'_, AppState>, id: i64) -> CmdResult<()> {
    mock::start(&*state.user()?, id).map_err(e)
}

#[tauri::command]
pub async fn test_save(
    state: State<'_, AppState>,
    id: i64,
    test_state: TestState,
    remaining_ms: i64,
) -> CmdResult<()> {
    mock::save(&*state.user()?, id, &test_state, remaining_ms).map_err(e)
}

#[tauri::command]
pub async fn test_submit(
    state: State<'_, AppState>,
    id: i64,
    test_state: TestState,
    remaining_ms: i64,
) -> CmdResult<TestSummary> {
    let content = state.content()?;
    let mut user = state.user()?;
    mock::submit(&content, &mut user, id, &test_state, remaining_ms).map_err(e)
}

#[tauri::command]
pub async fn test_result(
    state: State<'_, AppState>,
    id: i64,
    lang: String,
) -> CmdResult<TestResult> {
    mock::result(&*state.content()?, &*state.user()?, id, &lang).map_err(e)
}

#[tauri::command]
pub async fn test_delete(state: State<'_, AppState>, id: i64) -> CmdResult<()> {
    mock::delete(&*state.user()?, id).map_err(e)
}
