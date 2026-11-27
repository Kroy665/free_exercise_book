//! Lecture audio packs: clips made ahead of time (tools/lecture-audio), one pack per topic,
//! listed in a separately signed `audio/manifest.json` on the content server.
//!
//! A clip is found by its id: the first 32 hex digits of the SHA-256 of the spoken text with
//! its whitespace collapsed ([`clip_id`]), so text changed after the audio was made simply
//! has no clip (the app then uses its built-in voice).
//!
//! Pack file: `FEBAUD1\n`, a little-endian u32 length, a JSON index
//! `{ clip id: [offset, length] }` (offsets from the end of the index), then the MP3 clips.

use crate::{PackError, Result, sha256_hex};
use serde::{Deserialize, Serialize};
use std::collections::BTreeMap;

pub const AUDIO_DIR: &str = "audio";
pub const AUDIO_SCHEMA: u32 = 1;
const MAGIC: &[u8] = b"FEBAUD1\n";

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AudioEntry {
    /// Topic id.
    pub id: String,
    /// File name relative to the audio manifest.
    pub file: String,
    pub size: u64,
    pub sha256: String,
    pub clips: usize,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AudioManifest {
    pub schema: u32,
    pub generated_at: u64,
    /// The voice the clips were made with (shown in the app).
    pub voice: String,
    pub topics: Vec<AudioEntry>,
}

impl AudioManifest {
    pub fn get(&self, id: &str) -> Option<&AudioEntry> {
        self.topics.iter().find(|t| t.id == id)
    }
}

/// Clip id of a spoken text.
pub fn clip_id(text: &str) -> String {
    let norm = text.split_whitespace().collect::<Vec<_>>().join(" ");
    sha256_hex(norm.as_bytes())[..32].to_string()
}

/// Check the signature (see [`crate::verify_signature`]) and parse an audio manifest.
pub fn verify_audio_manifest(bytes: &[u8], signature: &str, trusted_keys: &[String]) -> Result<AudioManifest> {
    crate::verify_signature(bytes, signature, trusted_keys)?;
    let m: AudioManifest = serde_json::from_slice(bytes).map_err(|e| PackError::Manifest(e.to_string()))?;
    if m.schema != AUDIO_SCHEMA {
        return Err(PackError::Manifest(format!("audio manifest schema {} is not supported; please update the app", m.schema)));
    }
    for t in &m.topics {
        if t.file.contains('/') || t.file.contains('\\') || t.file.starts_with('.') {
            return Err(PackError::Manifest(format!("bad audio file name for {}", t.id)));
        }
    }
    Ok(m)
}

/// Check a downloaded audio pack against its manifest entry.
pub fn check_audio(entry: &AudioEntry, bytes: &[u8]) -> Result<()> {
    if bytes.len() as u64 != entry.size || sha256_hex(bytes) != entry.sha256 {
        return Err(PackError::Hash { name: format!("audio for {}", entry.id) });
    }
    Ok(())
}

/// Build a pack from (clip id, MP3 bytes).
pub fn write_pack(clips: &BTreeMap<String, Vec<u8>>) -> Vec<u8> {
    let mut index = BTreeMap::new();
    let mut at = 0u64;
    for (id, b) in clips {
        index.insert(id.clone(), [at, b.len() as u64]);
        at += b.len() as u64;
    }
    let json = serde_json::to_vec(&index).expect("index serialises");
    let mut out = Vec::with_capacity(MAGIC.len() + 4 + json.len() + at as usize);
    out.extend_from_slice(MAGIC);
    out.extend_from_slice(&(json.len() as u32).to_le_bytes());
    out.extend_from_slice(&json);
    for b in clips.values() {
        out.extend_from_slice(b);
    }
    out
}

/// An opened audio pack.
pub struct AudioPack {
    index: BTreeMap<String, [u64; 2]>,
    data: Vec<u8>,
    base: usize,
}

impl AudioPack {
    pub fn parse(data: Vec<u8>) -> Result<Self> {
        let bad = || PackError::Manifest("not a lecture audio pack".into());
        if data.len() < MAGIC.len() + 4 || &data[..MAGIC.len()] != MAGIC {
            return Err(bad());
        }
        let n = u32::from_le_bytes(data[MAGIC.len()..MAGIC.len() + 4].try_into().unwrap()) as usize;
        let base = MAGIC.len() + 4 + n;
        if base > data.len() {
            return Err(bad());
        }
        let index: BTreeMap<String, [u64; 2]> = serde_json::from_slice(&data[MAGIC.len() + 4..base]).map_err(|_| bad())?;
        let body = (data.len() - base) as u64;
        if index.values().any(|[o, l]| o.checked_add(*l).is_none_or(|end| end > body)) {
            return Err(bad());
        }
        Ok(Self { index, data, base })
    }

    pub fn has(&self, id: &str) -> bool {
        self.index.contains_key(id)
    }

    pub fn clip(&self, id: &str) -> Option<&[u8]> {
        let [o, l] = *self.index.get(id)?;
        Some(&self.data[self.base + o as usize..self.base + (o + l) as usize])
    }

    pub fn len(&self) -> usize {
        self.index.len()
    }

    pub fn is_empty(&self) -> bool {
        self.index.is_empty()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn round_trip() {
        let mut clips = BTreeMap::new();
        clips.insert(clip_id("Hello  there.\n"), b"abc".to_vec());
        clips.insert(clip_id("Second"), b"defgh".to_vec());
        let p = AudioPack::parse(write_pack(&clips)).unwrap();
        assert_eq!(p.clip(&clip_id("Hello there.")), Some(&b"abc"[..]));
        assert_eq!(p.clip(&clip_id("Second")), Some(&b"defgh"[..]));
        assert!(p.clip("nope").is_none());
        assert!(AudioPack::parse(b"FEBAUD1\n\x02\x00\x00\x00{}".to_vec()).is_ok());
        assert!(AudioPack::parse(b"junk".to_vec()).is_err());
    }

    #[test]
    fn clip_id_matches_python() {
        // tools/lecture-audio/generate.py: sha256(" ".join(text.split()))[:32]
        assert_eq!(clip_id(" a\n b "), sha256_hex(b"a b")[..32]);
    }
}
