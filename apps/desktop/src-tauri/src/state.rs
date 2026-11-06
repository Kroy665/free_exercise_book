use crate::pack_service::PackConfig;
use feb_core::error::ErrorPayload;
use rusqlite::Connection;
use std::sync::{Mutex, MutexGuard};

pub struct AppState {
    pub content: Mutex<Connection>,
    pub user: Mutex<Connection>,
    pub packs: PackConfig,
}

fn lock(m: &Mutex<Connection>) -> Result<MutexGuard<'_, Connection>, ErrorPayload> {
    m.lock().map_err(|_| ErrorPayload {
        code: "STATE_POISONED",
        message: "internal state lock poisoned".into(),
    })
}

impl AppState {
    pub fn content(&self) -> Result<MutexGuard<'_, Connection>, ErrorPayload> {
        lock(&self.content)
    }
    pub fn user(&self) -> Result<MutexGuard<'_, Connection>, ErrorPayload> {
        lock(&self.user)
    }
}
