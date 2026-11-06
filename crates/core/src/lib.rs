//! Domain logic for Free Exercise Book.
//!
//! This crate has **no Tauri dependency** (see docs/APP_STRUCTURE.md). It owns:
//! - opening and migrating `content.db` and `user.db`
//! - importing source content (YAML + Markdown) into `content.db`
//! - library queries (subjects → units → topics → note sections)
//! - practice (questions resolved to a language, grading, mistakes)
//! - user settings

pub mod db;
pub mod error;
pub mod import;
pub mod library;
pub mod localize;
pub mod mock;
pub mod model;
pub mod packs;
pub mod practice;
pub mod progress;
pub mod search;
pub mod settings;
pub mod srs;

pub use error::{CoreError, Result};

/// Languages every topic must be complete in (docs/CONTENT_STRUCTURE.md §1).
pub const REQUIRED_LANGS: &[&str] = &["en", "bn"];
/// Languages the app can show content in.
pub const SUPPORTED_LANGS: &[&str] = &["en", "bn", "hi"];
