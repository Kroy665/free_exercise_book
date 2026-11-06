use serde::Serialize;

pub type Result<T, E = CoreError> = std::result::Result<T, E>;

#[derive(Debug, thiserror::Error)]
pub enum CoreError {
    #[error("database error: {0}")]
    Db(#[from] rusqlite::Error),
    #[error("cannot read {path}: {source}")]
    Io {
        path: String,
        #[source]
        source: std::io::Error,
    },
    #[error("invalid content in {path}: {message}")]
    Content { path: String, message: String },
    #[error("not found: {0}")]
    NotFound(String),
    #[error("invalid input: {0}")]
    Invalid(String),
    #[error("json error: {0}")]
    Json(#[from] serde_json::Error),
}

impl CoreError {
    /// Stable machine-readable code, sent to the UI (docs/APP_STRUCTURE.md §5).
    pub fn code(&self) -> &'static str {
        match self {
            CoreError::Db(_) => "DB_ERROR",
            CoreError::Io { .. } => "IO_ERROR",
            CoreError::Content { .. } => "CONTENT_INVALID",
            CoreError::NotFound(_) => "NOT_FOUND",
            CoreError::Invalid(_) => "INVALID_INPUT",
            CoreError::Json(_) => "JSON_ERROR",
        }
    }
}

/// Serializable error shape for the IPC boundary.
#[derive(Debug, Clone, Serialize)]
pub struct ErrorPayload {
    pub code: &'static str,
    pub message: String,
}

impl From<&CoreError> for ErrorPayload {
    fn from(e: &CoreError) -> Self {
        ErrorPayload {
            code: e.code(),
            message: e.to_string(),
        }
    }
}
