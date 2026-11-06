mod commands;
mod pack_commands;
mod pack_service;
mod state;
mod test_commands;

use feb_core::{db, import};
use pack_service::PackConfig;
use state::AppState;
use std::path::PathBuf;
use std::sync::Mutex;
use tauri::{AppHandle, Manager};

/// Packs that ship with the app: `dist/packs` from the repo in debug builds (built by
/// `npm run packs`), otherwise the bundled `packs/` resource.
fn bundled_dir(app: &AppHandle) -> Option<PathBuf> {
    #[cfg(debug_assertions)]
    {
        let p = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../../../dist/packs");
        if p.join(feb_packs::MANIFEST_FILE).exists() {
            return Some(p);
        }
    }
    app.path()
        .resource_dir()
        .ok()
        .map(|d| d.join("packs"))
        .filter(|p| p.join(feb_packs::MANIFEST_FILE).exists())
}

fn init_state(app: &AppHandle) -> Result<AppState, Box<dyn std::error::Error>> {
    let data_dir = app.path().app_data_dir()?;
    let cache_dir = app.path().app_cache_dir()?;
    std::fs::create_dir_all(&data_dir)?;
    let mut content = db::open_content(&data_dir.join("content.db"))?;
    let user = db::open_user(&data_dir.join("user.db"))?;

    // Developer mode: import a content folder directly, no packs (docs/APP_STRUCTURE.md §7).
    let dev_dir = std::env::var("FEB_CONTENT_DIR").ok().map(PathBuf::from);
    if let Some(dir) = &dev_dir {
        match import::import_dir(&mut content, dir) {
            Ok(r) => eprintln!("[content] developer import from {}: {r:?}", dir.display()),
            Err(err) => eprintln!("[content] developer import failed: {err}"),
        }
    }

    let mut remote_url =
        std::env::var("FEB_PACKS_URL").unwrap_or_else(|_| pack_service::DEFAULT_PACKS_URL.into());
    if !remote_url.ends_with('/') {
        remote_url.push('/');
    }
    let packs = PackConfig {
        data_dir,
        cache_dir,
        bundled_dir: bundled_dir(app),
        remote_url,
        trusted_keys: pack_service::trusted_keys(),
        dev_mode: dev_dir.is_some(),
        busy: Mutex::new(()),
    };
    let content = Mutex::new(content);
    packs.sync_bundled(&content);

    Ok(AppState {
        content,
        user: Mutex::new(user),
        packs,
    })
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .plugin(tauri_plugin_dialog::init())
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
            pack_commands::packs_list,
            pack_commands::packs_check,
            pack_commands::packs_install,
            pack_commands::packs_remove,
            pack_commands::packs_import_folder,
            test_commands::tests_overview,
            test_commands::tests_create_custom,
            test_commands::tests_create_pattern,
            test_commands::test_session,
            test_commands::test_start,
            test_commands::test_save,
            test_commands::test_submit,
            test_commands::test_result,
            test_commands::test_delete,
        ])
        .run(tauri::generate_context!())
        .expect("error while running Free Exercise Book");
}
