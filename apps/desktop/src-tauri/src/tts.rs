//! Kokoro text-to-speech ("Listen").
//!
//! The webview turns text into phonemes (espeak-ng, `src/lib/tts/phonemes.ts`); this module
//! runs the Kokoro-82M model natively with ONNX Runtime and returns the audio samples.
//! The model and voices are downloaded on first use into `<app data>/tts` and checked
//! against pinned SHA-256 hashes.

use crate::state::AppState;
use feb_core::error::ErrorPayload;
use serde::Serialize;
use sha2::{Digest, Sha256};
use std::io::{Read, Write};
use std::path::{Path, PathBuf};
use std::sync::{Mutex, OnceLock};
use std::time::Duration;
use tauri::{AppHandle, Emitter, State};

type CmdResult<T> = Result<T, ErrorPayload>;

const MODEL_BASE: &str = "https://huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX/resolve/1939ad2a8e416c0acfeecc08a694d14ef25f2231/";

struct File {
    /// Path under `<app data>/tts/` (and, for model files, under the model repo).
    path: &'static str,
    base: &'static str,
    size: u64,
    sha256: &'static str,
}

const CORE: &[File] = &[
    File { path: "config.json", base: MODEL_BASE, size: 44, sha256: "df34b4f930b23447cd4dc410fabfb42eb3f24e803e6c3f97d618fb359380a36f" },
    File { path: "tokenizer.json", base: MODEL_BASE, size: 3497, sha256: "77a02c8e164413299b4b4c403b14f8e0e1c1b727db4d46a09d6327b861060a34" },
    File { path: "tokenizer_config.json", base: MODEL_BASE, size: 113, sha256: "be1cb066d6ef6b074b3f15e6a6dd21ac88ff3cdaedf325f0aaed686c70f75d20" },
    File { path: "onnx/model_quantized.onnx", base: MODEL_BASE, size: 92_361_116, sha256: "fbae9257e1e05ffc727e951ef9b9c98418e6d79f1c9b6b13bd59f5c9028a1478" },
];

const VOICES: &[File] = &[
    File { path: "voices/af_heart.bin", base: MODEL_BASE, size: 522_240, sha256: "d583ccff3cdca2f7fae535cb998ac07e9fcb90f09737b9a41fa2734ec44a8f0b" },
    File { path: "voices/af_bella.bin", base: MODEL_BASE, size: 522_240, sha256: "f69d836209b78eb8c66e75e3cda491e26ea838a3674257e9d4e5703cbaf55c8b" },
    File { path: "voices/bf_emma.bin", base: MODEL_BASE, size: 522_240, sha256: "669fe0647f9dd04fcab92f1439a40eeb4c8b4ab1f82e4996fe3d918ce4a63b73" },
    File { path: "voices/am_michael.bin", base: MODEL_BASE, size: 522_240, sha256: "1d1f21dd8da39c30705cd4c75d039d265e9bc4a2a93ed09bc9e1b1225eb95ba1" },
    File { path: "voices/bm_george.bin", base: MODEL_BASE, size: 522_240, sha256: "c4b235a4c1f2cd3b939fed08b899ce9385638b763f7b73a59616c4fc9bd6c9bc" },
];

fn err(code: &'static str, message: impl Into<String>) -> ErrorPayload {
    ErrorPayload { code, message: message.into() }
}

fn dir(state: &AppState) -> PathBuf {
    state.packs.data_dir.join("tts")
}

fn needed(voice: &str) -> CmdResult<Vec<&'static File>> {
    let v = VOICES
        .iter()
        .find(|f| f.path == format!("voices/{voice}.bin"))
        .ok_or_else(|| err("INVALID", format!("unknown voice '{voice}'")))?;
    Ok(CORE.iter().chain(std::iter::once(v)).collect())
}

/// Present with the right size (hashes are checked when the file is downloaded).
fn present(root: &Path, f: &File) -> bool {
    std::fs::metadata(root.join(f.path)).is_ok_and(|m| m.len() == f.size)
}

#[derive(Serialize)]
pub struct TtsStatus {
    ready: bool,
    /// Bytes still to download for this voice.
    missing_bytes: u64,
}

#[tauri::command]
pub async fn tts_status(state: State<'_, AppState>, voice: String) -> CmdResult<TtsStatus> {
    let root = dir(&state);
    let missing: u64 = needed(&voice)?.iter().filter(|f| !present(&root, f)).map(|f| f.size).sum();
    Ok(TtsStatus { ready: missing == 0, missing_bytes: missing })
}

#[derive(Clone, Serialize)]
struct Progress {
    done: u64,
    total: u64,
}

fn download(root: &Path, f: &File, done: &mut u64, total: u64, app: &AppHandle) -> Result<(), String> {
    let dest = root.join(f.path);
    if let Some(p) = dest.parent() {
        std::fs::create_dir_all(p).map_err(|e| e.to_string())?;
    }
    let agent = ureq::AgentBuilder::new()
        .timeout_connect(Duration::from_secs(15))
        .timeout_read(Duration::from_secs(60))
        .user_agent(concat!("FreeExerciseBook/", env!("CARGO_PKG_VERSION")))
        .build();
    let resp = agent
        .get(&format!("{}{}", f.base, f.path))
        .call()
        .map_err(|e| format!("download of {} failed: {e}", f.path))?;
    let tmp = dest.with_extension("part");
    let mut out = std::fs::File::create(&tmp).map_err(|e| e.to_string())?;
    let mut hasher = Sha256::new();
    let mut reader = resp.into_reader().take(f.size + 1);
    let mut buf = vec![0u8; 256 * 1024];
    let mut got = 0u64;
    let mut last_emit = 0u64;
    loop {
        let n = reader.read(&mut buf).map_err(|e| e.to_string())?;
        if n == 0 {
            break;
        }
        hasher.update(&buf[..n]);
        out.write_all(&buf[..n]).map_err(|e| e.to_string())?;
        got += n as u64;
        *done += n as u64;
        if *done - last_emit > 1_000_000 {
            last_emit = *done;
            let _ = app.emit("tts-progress", Progress { done: *done, total });
        }
    }
    drop(out);
    let hash = hex::encode(hasher.finalize());
    if got != f.size || hash != f.sha256 {
        let _ = std::fs::remove_file(&tmp);
        return Err(format!("{} did not match its expected checksum; try again", f.path));
    }
    std::fs::rename(&tmp, &dest).map_err(|e| e.to_string())
}

/// Download whatever is missing for `voice`, reporting `tts-progress` events.
#[tauri::command]
pub async fn tts_download(app: AppHandle, state: State<'_, AppState>, voice: String) -> CmdResult<()> {
    let root = dir(&state);
    let files: Vec<&'static File> = needed(&voice)?.into_iter().filter(|f| !present(&root, f)).collect();
    let total: u64 = files.iter().map(|f| f.size).sum();
    tauri::async_runtime::spawn_blocking(move || -> Result<(), String> {
        let mut done = 0u64;
        for f in files {
            download(&root, f, &mut done, total, &app)?;
        }
        let _ = app.emit("tts-progress", Progress { done: total, total });
        Ok(())
    })
    .await
    .map_err(|e| err("INTERNAL", e.to_string()))?
    .map_err(|m| err("NETWORK", m))
}

/// Delete the downloaded speech files.
#[tauri::command]
pub async fn tts_remove(state: State<'_, AppState>, tts: State<'_, TtsState>) -> CmdResult<()> {
    if let Ok(mut e) = tts.engine.lock() {
        *e = None;
    }
    let root = dir(&state);
    if root.exists() {
        std::fs::remove_dir_all(&root).map_err(|e| err("IO", e.to_string()))?;
    }
    Ok(())
}

// ---------- Synthesis ----------

/// Kokoro takes at most 510 phoneme tokens per call (plus the two boundary tokens).
const MAX_TOKENS: usize = 510;
const STYLE_DIM: usize = 256;

struct Engine {
    session: ort::session::Session,
    vocab: std::collections::HashMap<char, i64>,
    voices: std::collections::HashMap<String, Vec<f32>>,
}

#[derive(Default)]
pub struct TtsState {
    engine: Mutex<Option<Engine>>,
}

fn init_runtime() {
    static INIT: OnceLock<()> = OnceLock::new();
    INIT.get_or_init(|| {
        ort::init().with_name("feb-tts").commit();
    });
}

fn load_engine(root: &Path) -> Result<Engine, String> {
    let threads = std::thread::available_parallelism().map(|n| n.get()).unwrap_or(4).clamp(1, 8) / 2;
    init_runtime();
    let session = ort::session::Session::builder()
        .map_err(|e| e.to_string())?
        .with_intra_threads(threads.max(1))
        .map_err(|e| e.to_string())?
        .commit_from_file(root.join("onnx/model_quantized.onnx"))
        .map_err(|e| format!("could not load the voice model: {e}"))?;
    let tok: serde_json::Value = serde_json::from_slice(&std::fs::read(root.join("tokenizer.json")).map_err(|e| e.to_string())?)
        .map_err(|e| e.to_string())?;
    let vocab = tok["model"]["vocab"]
        .as_object()
        .ok_or("tokenizer.json has no vocabulary")?
        .iter()
        .filter_map(|(k, v)| {
            let mut cs = k.chars();
            match (cs.next(), cs.next(), v.as_i64()) {
                (Some(c), None, Some(id)) => Some((c, id)),
                _ => None,
            }
        })
        .collect();
    Ok(Engine { session, vocab, voices: Default::default() })
}

fn voice<'e>(engine: &'e mut Engine, root: &Path, name: &str) -> Result<&'e [f32], String> {
    if !engine.voices.contains_key(name) {
        let bytes = std::fs::read(root.join(format!("voices/{name}.bin"))).map_err(|e| e.to_string())?;
        let v: Vec<f32> = bytes.chunks_exact(4).map(|b| f32::from_le_bytes([b[0], b[1], b[2], b[3]])).collect();
        if v.len() < STYLE_DIM {
            return Err("voice file is too small".into());
        }
        engine.voices.insert(name.to_string(), v);
    }
    Ok(&engine.voices[name])
}

fn synthesize(engine: &mut Engine, root: &Path, voice_name: &str, phonemes: &str, speed: f32) -> Result<Vec<f32>, String> {
    let mut ids: Vec<i64> = vec![0];
    ids.extend(phonemes.chars().filter_map(|c| engine.vocab.get(&c).copied()).take(MAX_TOKENS));
    ids.push(0);
    if ids.len() <= 2 {
        return Ok(Vec::new());
    }
    // The voice file holds one style vector per input length.
    let rows = {
        let v = voice(engine, root, voice_name)?;
        v.len() / STYLE_DIM
    };
    let row = (ids.len() - 2).min(rows - 1);
    let style: Vec<f32> = voice(engine, root, voice_name)?[row * STYLE_DIM..(row + 1) * STYLE_DIM].to_vec();
    let n = ids.len();
    let inputs = ort::inputs![
        "input_ids" => ort::value::Tensor::from_array(([1usize, n], ids)).map_err(|e| e.to_string())?,
        "style" => ort::value::Tensor::from_array(([1usize, STYLE_DIM], style)).map_err(|e| e.to_string())?,
        "speed" => ort::value::Tensor::from_array(([1usize], vec![speed])).map_err(|e| e.to_string())?,
    ];
    let outputs = engine.session.run(inputs).map_err(|e| e.to_string())?;
    let (_, audio) = outputs["waveform"].try_extract_tensor::<f32>().map_err(|e| e.to_string())?;
    Ok(audio.to_vec())
}

/// Speak one chunk of phonemes; returns 24 kHz mono samples as little-endian f32 bytes.
#[tauri::command]
pub async fn tts_synth(
    app: AppHandle,
    state: State<'_, AppState>,
    voice: String,
    phonemes: String,
    speed: f32,
) -> CmdResult<tauri::ipc::Response> {
    if !feb_core::settings::TTS_VOICES.contains(&voice.as_str()) {
        return Err(err("INVALID", format!("unknown voice '{voice}'")));
    }
    if phonemes.chars().count() > 4 * MAX_TOKENS {
        return Err(err("INVALID", "text chunk is too long"));
    }
    let speed = if speed.is_finite() { speed.clamp(0.5, 2.0) } else { 1.0 };
    let root = dir(&state);
    let bytes = tauri::async_runtime::spawn_blocking(move || -> Result<Vec<u8>, String> {
        let tts = tauri::Manager::state::<TtsState>(&app);
        let mut guard = tts.engine.lock().map_err(|_| "speech engine lock poisoned".to_string())?;
        if guard.is_none() {
            *guard = Some(load_engine(&root)?);
        }
        let engine = guard.as_mut().ok_or("speech engine missing")?;
        let samples = synthesize(engine, &root, &voice, &phonemes, speed)?;
        Ok(samples.iter().flat_map(|s| s.to_le_bytes()).collect())
    })
    .await
    .map_err(|e| err("INTERNAL", e.to_string()))?
    .map_err(|m| err("TTS", m))?;
    Ok(tauri::ipc::Response::new(bytes))
}

#[cfg(test)]
mod tests {
    use super::*;

    /// Needs the downloaded files: FEB_TTS_DIR=<folder with onnx/, voices/, tokenizer.json>.
    #[test]
    #[ignore]
    fn speaks_phonemes() {
        let root = PathBuf::from(std::env::var("FEB_TTS_DIR").expect("FEB_TTS_DIR"));
        let t0 = std::time::Instant::now();
        let mut e = load_engine(&root).unwrap();
        let load = t0.elapsed();
        let ph = "ðɪ ˈɪntᵻɡɹəl ʌv ˈɛks skwˈɛɹd fɹʌm zˈiəɹoʊ tə wˈʌn ˈiːkwəlz wˈʌn θˈɜːd.";
        for _ in 0..2 {
            let t1 = std::time::Instant::now();
            let a = synthesize(&mut e, &root, "af_heart", ph, 1.0).unwrap();
            let secs = a.len() as f32 / 24_000.0;
            let peak = a.iter().fold(0f32, |m, x| m.max(x.abs()));
            eprintln!("load {load:?}; {secs:.2}s of audio in {:?}; peak {peak:.2}", t1.elapsed());
            assert!(secs > 2.0 && secs < 10.0 && peak > 0.05);
        }
    }
}
