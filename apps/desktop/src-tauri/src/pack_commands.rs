//! IPC commands for the Downloads page. Long operations run on a blocking thread and
//! report progress through the `packs://progress` event.

use crate::pack_service::{self, PacksView};
use crate::state::AppState;
use feb_core::error::ErrorPayload;
use feb_core::packs as store;
use feb_packs::source::Source;
use feb_packs::version_newer;
use serde::Serialize;
use std::path::PathBuf;
use tauri::{AppHandle, Emitter, Manager, State};

type CmdResult<T> = Result<T, ErrorPayload>;

#[derive(Clone, Serialize)]
struct Progress<'a> {
    id: &'a str,
    /// "download" | "install" | "done" | "error"
    phase: &'a str,
    done: u64,
    total: u64,
    message: Option<String>,
}

#[derive(Serialize)]
pub struct InstallReport {
    pub view: PacksView,
    pub installed: Vec<String>,
    pub failed: Vec<(String, ErrorPayload)>,
}

fn join_err(e: impl std::fmt::Display) -> ErrorPayload {
    ErrorPayload {
        code: "INTERNAL",
        message: e.to_string(),
    }
}

fn dev_mode_err() -> ErrorPayload {
    ErrorPayload {
        code: "DEV_MODE",
        message: "Content packs are disabled while FEB_CONTENT_DIR is set (developer mode).".into(),
    }
}

fn install_all(
    app: &AppHandle,
    items: Vec<(feb_packs::PackEntry, Source)>,
    lang: &str,
) -> CmdResult<InstallReport> {
    let state = app.state::<AppState>();
    let (mut installed, mut failed) = (Vec::new(), Vec::new());
    for (entry, source) in items {
        let id = entry.id.clone();
        let result = state.packs.install(
            &state.content,
            &entry,
            &source,
            &mut |phase, done, total| {
                app.emit(
                    "packs://progress",
                    Progress {
                        id: &id,
                        phase,
                        done,
                        total,
                        message: None,
                    },
                )
                .ok();
            },
        );
        match result {
            Ok(_) => {
                app.emit(
                    "packs://progress",
                    Progress {
                        id: &id,
                        phase: "done",
                        done: 1,
                        total: 1,
                        message: None,
                    },
                )
                .ok();
                installed.push(id);
            }
            Err(e) => {
                app.emit(
                    "packs://progress",
                    Progress {
                        id: &id,
                        phase: "error",
                        done: 0,
                        total: 0,
                        message: Some(e.message.clone()),
                    },
                )
                .ok();
                failed.push((id, e));
            }
        }
    }
    let view = pack_service::view(&state.packs, &*state.content()?, lang, None)?;
    Ok(InstallReport {
        view,
        installed,
        failed,
    })
}

/// Pack list from local information only (installed, bundled, last server check).
#[tauri::command]
pub async fn packs_list(state: State<'_, AppState>, lang: String) -> CmdResult<PacksView> {
    pack_service::view(&state.packs, &*state.content()?, &lang, None)
}

/// Contact the content server for new and updated packs. Network problems are reported
/// in `remote.error`, not as a failure, so the page still shows local packs.
#[tauri::command]
pub async fn packs_check(app: AppHandle, lang: String) -> CmdResult<PacksView> {
    tauri::async_runtime::spawn_blocking(move || {
        let state = app.state::<AppState>();
        if state.packs.dev_mode {
            return Err(dev_mode_err());
        }
        let error = match state.packs.check_remote() {
            Ok(m) => {
                state.packs.store_exams(&state.content, &m);
                None
            }
            Err(e) => Some(e),
        };
        pack_service::view(&state.packs, &*state.content()?, &lang, error)
    })
    .await
    .map_err(join_err)?
}

/// Install or update the given packs from the best available source.
#[tauri::command]
pub async fn packs_install(
    app: AppHandle,
    ids: Vec<String>,
    lang: String,
) -> CmdResult<InstallReport> {
    tauri::async_runtime::spawn_blocking(move || {
        let state = app.state::<AppState>();
        if state.packs.dev_mode {
            return Err(dev_mode_err());
        }
        let mut items = Vec::new();
        let mut missing = Vec::new();
        for id in ids {
            match state.packs.best(&id) {
                Some(x) => items.push(x),
                None => missing.push((
                    id.clone(),
                    ErrorPayload {
                        code: "NOT_FOUND",
                        message: format!("pack {id} is not available"),
                    },
                )),
            }
        }
        let mut report = install_all(&app, items, &lang)?;
        report.failed.extend(missing);
        Ok(report)
    })
    .await
    .map_err(join_err)?
}

/// Remove a pack. The user's progress for its questions is kept.
#[tauri::command]
pub async fn packs_remove(
    state: State<'_, AppState>,
    id: String,
    lang: String,
) -> CmdResult<PacksView> {
    if state.packs.dev_mode {
        return Err(dev_mode_err());
    }
    {
        let _guard = state.packs.busy.lock().map_err(join_err)?;
        let mut conn = state.content()?;
        store::remove_pack(&mut conn, &id).map_err(pack_service::core_err)?;
    }
    pack_service::view(&state.packs, &*state.content()?, &lang, None)
}

/// Install packs from a folder (a copy of a pack directory, e.g. on a USB drive).
/// Only packs that are new or newer than the installed version are installed.
#[tauri::command]
pub async fn packs_import_folder(
    app: AppHandle,
    path: String,
    lang: String,
) -> CmdResult<InstallReport> {
    tauri::async_runtime::spawn_blocking(move || {
        let state = app.state::<AppState>();
        if state.packs.dev_mode {
            return Err(dev_mode_err());
        }
        let dir = PathBuf::from(path);
        let manifest = state.packs.folder_manifest(&dir)?;
        state.packs.store_exams(&state.content, &manifest);
        let installed =
            store::list_installed(&*state.content()?).map_err(pack_service::core_err)?;
        let items = manifest
            .packs
            .into_iter()
            .filter(|e| {
                installed
                    .iter()
                    .find(|p| p.id == e.id)
                    .is_none_or(|p| version_newer(&e.version, &p.version))
            })
            .map(|e| (e, Source::Folder(dir.clone())))
            .collect();
        install_all(&app, items, &lang)
    })
    .await
    .map_err(join_err)?
}
