//! Lecture audio made ahead of time (tools/lecture-audio): one signed audio pack per topic on
//! the content server (`audio/` on the packs branch), downloaded when the topic is opened and
//! kept in `<app data>/lecture-audio/`. Steps without a clip use the built-in voice (tts.rs).

use crate::state::AppState;
use feb_core::error::ErrorPayload;
use feb_packs::audio::{AUDIO_DIR, AudioManifest, AudioPack, check_audio, clip_id, verify_audio_manifest};
use feb_packs::source::Source;
use feb_packs::{MANIFEST_FILE, MANIFEST_SIG_FILE, MAX_MANIFEST_BYTES, MAX_PACK_BYTES};
use std::path::{Path, PathBuf};
use std::sync::{Arc, Mutex};
use tauri::State;

type CmdResult<T> = Result<T, ErrorPayload>;

fn err(code: &'static str, message: impl Into<String>) -> ErrorPayload {
    ErrorPayload { code, message: message.into() }
}

#[derive(Default)]
pub struct LectureAudioState {
    /// The audio manifest, fetched once per run (`None` inside: none could be had).
    manifest: Mutex<Option<Option<AudioManifest>>>,
    /// The open topic's pack.
    open: Mutex<Option<(String, Arc<AudioPack>)>>,
}

fn dir(state: &AppState) -> PathBuf {
    state.packs.data_dir.join("lecture-audio")
}

/// The server's audio manifest, saved for offline use; the saved one when offline.
fn manifest(state: &AppState, la: &LectureAudioState) -> Option<AudioManifest> {
    let mut m = la.manifest.lock().ok()?;
    if let Some(cached) = m.as_ref() {
        return cached.clone();
    }
    let root = dir(state);
    let keys = &state.packs.trusted_keys;
    let src = Source::Remote(state.packs.remote_url.clone());
    let fetched = (|| {
        let bytes = src.fetch_file(&format!("{AUDIO_DIR}/{MANIFEST_FILE}"), MAX_MANIFEST_BYTES, &mut |_, _| {}).ok()?;
        let sig = src.fetch_file(&format!("{AUDIO_DIR}/{MANIFEST_SIG_FILE}"), 64 * 1024, &mut |_, _| {}).ok()?;
        let sig = String::from_utf8(sig).ok()?;
        let parsed = verify_audio_manifest(&bytes, &sig, keys).ok()?;
        std::fs::create_dir_all(&root).ok()?;
        std::fs::write(root.join(MANIFEST_FILE), &bytes).ok()?;
        std::fs::write(root.join(MANIFEST_SIG_FILE), &sig).ok()?;
        Some(parsed)
    })();
    let found = fetched.or_else(|| {
        let bytes = std::fs::read(root.join(MANIFEST_FILE)).ok()?;
        let sig = std::fs::read_to_string(root.join(MANIFEST_SIG_FILE)).ok()?;
        verify_audio_manifest(&bytes, &sig, keys).ok()
    });
    // Offline: try again on the next topic rather than never.
    if found.is_some() {
        *m = Some(found.clone());
    }
    found
}

/// Files of this topic's packs already on disk.
fn local_files(root: &Path, topic: &str) -> Vec<PathBuf> {
    let prefix = format!("{topic}@");
    std::fs::read_dir(root)
        .map(|rd| {
            rd.flatten()
                .map(|e| e.path())
                .filter(|p| {
                    p.file_name().and_then(|n| n.to_str()).is_some_and(|n| n.starts_with(&prefix) && n.ends_with(".audio"))
                })
                .collect()
        })
        .unwrap_or_default()
}

/// Make sure the topic's newest audio pack is on disk and open; `None` if there is none.
fn open(state: &AppState, la: &LectureAudioState, topic: &str) -> Result<Option<Arc<AudioPack>>, String> {
    if let Some((t, p)) = la.open.lock().map_err(|e| e.to_string())?.as_ref()
        && t == topic
    {
        return Ok(Some(p.clone()));
    }
    let root = dir(state);
    let path = match manifest(state, la).as_ref().and_then(|m| m.get(topic)).cloned() {
        Some(entry) => {
            let path = root.join(&entry.file);
            if !path.is_file() {
                let bytes = Source::Remote(state.packs.remote_url.clone())
                    .fetch_file(&format!("{AUDIO_DIR}/{}", entry.file), MAX_PACK_BYTES, &mut |_, _| {})
                    .map_err(|e| e.to_string())?;
                check_audio(&entry, &bytes).map_err(|e| e.to_string())?;
                std::fs::create_dir_all(&root).map_err(|e| e.to_string())?;
                let tmp = path.with_extension("part");
                std::fs::write(&tmp, &bytes).map_err(|e| e.to_string())?;
                std::fs::rename(&tmp, &path).map_err(|e| e.to_string())?;
            }
            // Older versions of this topic's audio are no longer needed.
            for old in local_files(&root, topic) {
                if old != path {
                    let _ = std::fs::remove_file(old);
                }
            }
            path
        }
        // Not on the server (or offline): use what was downloaded before, if anything.
        None => match local_files(&root, topic).into_iter().next() {
            Some(p) => p,
            None => return Ok(None),
        },
    };
    let pack = Arc::new(AudioPack::parse(std::fs::read(&path).map_err(|e| e.to_string())?).map_err(|e| e.to_string())?);
    *la.open.lock().map_err(|e| e.to_string())? = Some((topic.to_string(), pack.clone()));
    Ok(Some(pack))
}

/// Download (if needed) the topic's lecture audio; returns which of `texts` have a clip.
#[tauri::command]
pub async fn lecture_audio_prepare(app: tauri::AppHandle, topic: String, texts: Vec<String>) -> CmdResult<Vec<bool>> {
    tauri::async_runtime::spawn_blocking(move || {
        let state = tauri::Manager::state::<AppState>(&app);
        let la = tauri::Manager::state::<LectureAudioState>(&app);
        if state.packs.dev_mode && std::env::var_os("FEB_PACKS_URL").is_none() {
            return Ok(vec![false; texts.len()]);
        }
        let pack = open(&state, &la, &topic).map_err(|m| err("LECTURE_AUDIO", m))?;
        Ok(texts.iter().map(|t| pack.as_ref().is_some_and(|p| p.has(&clip_id(t)))).collect())
    })
    .await
    .map_err(|e| err("INTERNAL", e.to_string()))?
}

/// The clip for one spoken text of the open topic, as 24 kHz mono little-endian f32
/// samples; empty when there is no clip.
#[tauri::command]
pub async fn lecture_audio_clip(
    la: State<'_, LectureAudioState>,
    topic: String,
    text: String,
) -> CmdResult<tauri::ipc::Response> {
    let pack = match la.open.lock().map_err(|e| err("INTERNAL", e.to_string()))?.as_ref() {
        Some((t, p)) if *t == topic => p.clone(),
        _ => return Ok(tauri::ipc::Response::new(Vec::new())),
    };
    let bytes = tauri::async_runtime::spawn_blocking(move || -> Result<Vec<u8>, String> {
        let Some(mp3) = pack.clip(&clip_id(&text)) else { return Ok(Vec::new()) };
        let samples = decode_mp3(mp3)?;
        Ok(samples.iter().flat_map(|s| s.to_le_bytes()).collect())
    })
    .await
    .map_err(|e| err("INTERNAL", e.to_string()))?
    .map_err(|m| err("LECTURE_AUDIO", m))?;
    Ok(tauri::ipc::Response::new(bytes))
}

/// MP3 -> 24 kHz mono f32 (the clips are made at that rate).
fn decode_mp3(mp3: &[u8]) -> Result<Vec<f32>, String> {
    use symphonia::core::audio::SampleBuffer;
    use symphonia::core::codecs::DecoderOptions;
    use symphonia::core::errors::Error;
    use symphonia::core::formats::FormatOptions;
    use symphonia::core::io::MediaSourceStream;
    use symphonia::core::meta::MetadataOptions;
    use symphonia::core::probe::Hint;

    let mss = MediaSourceStream::new(Box::new(std::io::Cursor::new(mp3.to_vec())), Default::default());
    let mut hint = Hint::new();
    hint.with_extension("mp3");
    let mut format = symphonia::default::get_probe()
        .format(&hint, mss, &FormatOptions { enable_gapless: true, ..Default::default() }, &MetadataOptions::default())
        .map_err(|e| e.to_string())?
        .format;
    let track = format.default_track().ok_or("clip has no audio")?;
    if track.codec_params.sample_rate.is_some_and(|r| r != 24_000) {
        return Err("clip is not 24 kHz".into());
    }
    let id = track.id;
    let mut dec = symphonia::default::get_codecs()
        .make(&track.codec_params, &DecoderOptions::default())
        .map_err(|e| e.to_string())?;
    let mut out = Vec::new();
    loop {
        let packet = match format.next_packet() {
            Ok(p) => p,
            Err(Error::IoError(e)) if e.kind() == std::io::ErrorKind::UnexpectedEof => break,
            Err(e) => return Err(e.to_string()),
        };
        if packet.track_id() != id {
            continue;
        }
        match dec.decode(&packet) {
            Ok(buf) => {
                let spec = *buf.spec();
                let mut sb = SampleBuffer::<f32>::new(buf.capacity() as u64, spec);
                sb.copy_interleaved_ref(buf);
                let ch = spec.channels.count().max(1);
                out.extend(sb.samples().chunks(ch).map(|c| c[0]));
            }
            Err(Error::DecodeError(_)) => continue,
            Err(e) => return Err(e.to_string()),
        }
    }
    Ok(out)
}

#[cfg(test)]
mod tests {
    #[test]
    fn decodes_mp3() {
        // 0.5 s of a 440 Hz tone, made with ffmpeg the way generate.py makes clips.
        let dir = std::env::temp_dir().join("feb-lecture-audio-test");
        std::fs::create_dir_all(&dir).unwrap();
        let f = dir.join("tone.mp3");
        let ok = std::process::Command::new("ffmpeg")
            .args(["-y", "-loglevel", "error", "-f", "lavfi", "-i", "sine=f=440:d=0.5", "-ar", "24000", "-ac", "1", "-c:a", "libmp3lame", "-b:a", "48k"])
            .arg(&f)
            .status()
            .is_ok_and(|s| s.success());
        if !ok {
            eprintln!("ffmpeg not available; skipping");
            return;
        }
        let s = super::decode_mp3(&std::fs::read(&f).unwrap()).unwrap();
        let secs = s.len() as f32 / 24_000.0;
        assert!((0.45..0.6).contains(&secs), "{secs}");
        assert!(s.iter().fold(0f32, |m, x| m.max(x.abs())) > 0.08);
    }
}
