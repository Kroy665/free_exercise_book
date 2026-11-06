mod commands;
mod state;

use feb_core::{db, import};
use state::AppState;
use std::path::PathBuf;
use std::sync::Mutex;
use tauri::{AppHandle, Manager};

/// Where to import content from (until signed packs exist, docs/DATA_AND_PACKS.md):
/// 1. `FEB_CONTENT_DIR` env var
/// 2. the repo's `content/` folder (debug builds)
/// 3. the bundled `content/` resource (release builds)
fn content_dir(app: &AppHandle) -> Option<PathBuf> {
    if let Ok(p) = std::env::var("FEB_CONTENT_DIR") {
        return Some(PathBuf::from(p));
    }
    #[cfg(debug_assertions)]
    {
        let p = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../../../content");
        if p.join("subjects").exists() {
            return Some(p);
        }
    }
    app.path()
        .resource_dir()
        .ok()
        .map(|d| d.join("content"))
        .filter(|p| p.join("subjects").exists())
}

fn init_state(app: &AppHandle) -> Result<AppState, Box<dyn std::error::Error>> {
    let data_dir = app.path().app_data_dir()?;
    std::fs::create_dir_all(&data_dir)?;
    let mut content = db::open_content(&data_dir.join("content.db"))?;
    let user = db::open_user(&data_dir.join("user.db"))?;

    match content_dir(app) {
        Some(dir) => match import::import_dir(&mut content, &dir) {
            Ok(r) => eprintln!("[content] imported from {}: {r:?}", dir.display()),
            // Keep the previous content (the import is transactional) and keep running.
            Err(err) => eprintln!("[content] import failed: {err}"),
        },
        None => eprintln!("[content] no content directory found"),
    }

    Ok(AppState {
        content: Mutex::new(content),
        user: Mutex::new(user),
    })
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .setup(|app| {
            let state = init_state(app.handle())?;
            app.manage(state);
            Ok(())
        })
        .invoke_handler(tauri::generate_handler![
            commands::library_tree,
            commands::topic_get,
            commands::practice_questions,
            commands::practice_record,
            commands::mistakes_list,
            commands::stats_get,
            commands::settings_get,
            commands::settings_set,
        ])
        .run(tauri::generate_context!())
        .expect("error while running Free Exercise Book");
}
