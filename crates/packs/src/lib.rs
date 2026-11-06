//! Content packs: signed manifest, integrity checks, compression and transport
//! (docs/DATA_AND_PACKS.md §2–§5).
//!
//! Trust model: the **manifest** is signed with the project's minisign (Ed25519) key and
//! lists the SHA-256 of every pack. A pack is accepted only if its hash matches a
//! manifest whose signature verifies against a key compiled into the app.

use serde::{Deserialize, Serialize};
use sha2::{Digest, Sha256};
use std::collections::BTreeMap;
use std::io::Read;

#[cfg(feature = "sign")]
pub mod sign;
#[cfg(feature = "fetch")]
pub mod source;

/// Manifest file names inside a pack directory / on the server.
pub const MANIFEST_FILE: &str = "manifest.json";
pub const MANIFEST_SIG_FILE: &str = "manifest.json.minisig";
/// Manifest schema understood by this version of the app.
pub const MANIFEST_SCHEMA: u32 = 1;
/// Safety limits (a pack is normally < 2 MB compressed).
pub const MAX_MANIFEST_BYTES: u64 = 8 * 1024 * 1024;
pub const MAX_PACK_BYTES: u64 = 100 * 1024 * 1024;
pub const MAX_UNPACKED_BYTES: u64 = 500 * 1024 * 1024;

pub type Localized = BTreeMap<String, String>;

#[derive(Debug, thiserror::Error)]
pub enum PackError {
    #[error("network error: {0}")]
    Network(String),
    #[error("file error: {0}")]
    Io(#[from] std::io::Error),
    #[error("signature check failed: {0}")]
    Signature(String),
    #[error("{name}: checksum mismatch (the file is corrupted or was tampered with)")]
    Hash { name: String },
    #[error("invalid manifest: {0}")]
    Manifest(String),
    #[error("{0} is larger than allowed")]
    TooLarge(String),
}

impl PackError {
    pub fn code(&self) -> &'static str {
        match self {
            PackError::Network(_) => "NETWORK",
            PackError::Io(_) => "IO_ERROR",
            PackError::Signature(_) => "PACK_SIGNATURE_INVALID",
            PackError::Hash { .. } => "PACK_HASH_MISMATCH",
            PackError::Manifest(_) => "MANIFEST_INVALID",
            PackError::TooLarge(_) => "TOO_LARGE",
        }
    }
}

pub type Result<T, E = PackError> = std::result::Result<T, E>;

#[derive(Debug, Clone, Copy, Default, Serialize, Deserialize)]
pub struct Counts {
    pub sections: usize,
    pub questions: usize,
}

/// One downloadable pack (= one topic).
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PackEntry {
    pub id: String,
    pub version: String,
    pub title: Localized,
    #[serde(default)]
    pub summary: Option<Localized>,
    pub subject: String,
    pub subject_title: Localized,
    pub subject_order: i64,
    pub unit: String,
    pub unit_title: Localized,
    pub unit_order: i64,
    pub order: i64,
    pub langs: Vec<String>,
    pub exams: Vec<String>,
    pub status: String,
    #[serde(default)]
    pub estimated_minutes: Option<i64>,
    pub counts: Counts,
    /// File name relative to the manifest location.
    pub file: String,
    /// Size of the compressed file in bytes.
    pub size: u64,
    /// SHA-256 (hex) of the compressed file.
    pub sha256: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Manifest {
    pub schema: u32,
    /// Unix seconds.
    pub generated_at: u64,
    pub min_app_version: String,
    pub packs: Vec<PackEntry>,
}

impl Manifest {
    pub fn get(&self, id: &str) -> Option<&PackEntry> {
        self.packs.iter().find(|p| p.id == id)
    }
}

pub fn sha256_hex(bytes: &[u8]) -> String {
    hex::encode(Sha256::digest(bytes))
}

pub fn compress(bytes: &[u8]) -> Result<Vec<u8>> {
    Ok(zstd::encode_all(bytes, 19)?)
}

/// Decompress with an upper bound on the output size (protects against zip bombs).
pub fn decompress(bytes: &[u8]) -> Result<Vec<u8>> {
    let mut out = Vec::new();
    zstd::stream::Decoder::new(bytes)?
        .take(MAX_UNPACKED_BYTES + 1)
        .read_to_end(&mut out)?;
    if out.len() as u64 > MAX_UNPACKED_BYTES {
        return Err(PackError::TooLarge("unpacked pack".into()));
    }
    Ok(out)
}

/// Verify `manifest_bytes` against its minisign signature with any of the trusted
/// public keys (minisign `.pub` file contents), then parse it.
pub fn verify_manifest(
    manifest_bytes: &[u8],
    signature: &str,
    trusted_keys: &[String],
) -> Result<Manifest> {
    let sig = minisign_verify::Signature::decode(signature)
        .map_err(|e| PackError::Signature(format!("unreadable signature: {e}")))?;
    let mut last_err = String::from("no trusted keys configured");
    let mut ok = false;
    for key in trusted_keys {
        match minisign_verify::PublicKey::decode(key) {
            Ok(pk) => match pk.verify(manifest_bytes, &sig, false) {
                Ok(()) => {
                    ok = true;
                    break;
                }
                Err(e) => last_err = e.to_string(),
            },
            Err(e) => last_err = format!("bad trusted key: {e}"),
        }
    }
    if !ok {
        return Err(PackError::Signature(last_err));
    }
    let manifest: Manifest =
        serde_json::from_slice(manifest_bytes).map_err(|e| PackError::Manifest(e.to_string()))?;
    if manifest.schema != MANIFEST_SCHEMA {
        return Err(PackError::Manifest(format!(
            "manifest schema {} is not supported (expected {MANIFEST_SCHEMA}); please update the app",
            manifest.schema
        )));
    }
    for p in &manifest.packs {
        // File names come from a signed manifest, but never allow path traversal anyway.
        if p.file.contains('/') || p.file.contains('\\') || p.file.starts_with('.') {
            return Err(PackError::Manifest(format!("bad file name for {}", p.id)));
        }
    }
    Ok(manifest)
}

/// Check a downloaded pack against its manifest entry.
pub fn check_pack(entry: &PackEntry, bytes: &[u8]) -> Result<()> {
    if bytes.len() as u64 != entry.size || sha256_hex(bytes) != entry.sha256 {
        return Err(PackError::Hash {
            name: entry.id.clone(),
        });
    }
    Ok(())
}

/// Compare dotted numeric versions ("0.10.2" > "0.9.9"). Non-numeric parts compare as 0.
pub fn version_newer(candidate: &str, current: &str) -> bool {
    let parse = |v: &str| {
        v.split('.')
            .map(|p| p.parse::<u64>().unwrap_or(0))
            .collect::<Vec<_>>()
    };
    parse(candidate) > parse(current)
}
