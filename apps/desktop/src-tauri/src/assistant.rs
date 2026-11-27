//! Study assistant chat: Ollama (local) or the Claude API (the user's own key).
//!
//! Replies stream to the UI as `assistant` events: `{id, kind: "delta"|"done"|"error", text}`.
//! The Claude API key is kept in its own file in the app data folder (not in the settings
//! table, so it never ends up in a progress backup).

use crate::state::AppState;
use feb_core::assistant::{self, AskContext, ChatMessage};
use feb_core::error::ErrorPayload;
use feb_core::settings;
use serde::Serialize;
use serde_json::{Value, json};
use std::collections::HashMap;
use std::io::{BufRead, BufReader};
use std::path::PathBuf;
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::{Arc, Mutex};
use std::time::Duration;
use tauri::{AppHandle, Emitter, State};

type CmdResult<T> = Result<T, ErrorPayload>;

const CLAUDE_URL: &str = "https://api.anthropic.com/v1/messages";
const CLAUDE_VERSION: &str = "2026-10-21";

#[derive(Default)]
pub struct AssistantState {
    running: Mutex<HashMap<String, Arc<AtomicBool>>>,
}

fn err(code: &'static str, message: impl Into<String>) -> ErrorPayload {
    ErrorPayload { code, message: message.into() }
}

fn core(e: feb_core::CoreError) -> ErrorPayload {
    ErrorPayload::from(&e)
}

fn key_path(state: &AppState) -> PathBuf {
    state.packs.data_dir.join("assistant").join("claude-key")
}

fn read_key(state: &AppState) -> Option<String> {
    std::fs::read_to_string(key_path(state)).ok().map(|s| s.trim().to_string()).filter(|s| !s.is_empty())
}

fn agent(timeout: Duration) -> ureq::Agent {
    ureq::AgentBuilder::new()
        .timeout_connect(Duration::from_secs(10))
        .timeout_read(timeout)
        .user_agent(concat!("FreeExerciseBook/", env!("CARGO_PKG_VERSION")))
        .build()
}

#[derive(Serialize)]
pub struct OllamaStatus {
    reachable: bool,
    models: Vec<String>,
    has_model: bool,
}

#[derive(Serialize)]
pub struct AssistantStatus {
    provider: String,
    ollama: OllamaStatus,
    claude_has_key: bool,
}

fn ollama_models(url: &str) -> Option<Vec<String>> {
    let resp = agent(Duration::from_secs(5)).get(&format!("{}/api/tags", url.trim_end_matches('/'))).call().ok()?;
    let v: Value = resp.into_json().ok()?;
    Some(
        v["models"]
            .as_array()?
            .iter()
            .filter_map(|m| m["name"].as_str().map(str::to_string))
            .collect(),
    )
}

/// Ollama names "qwen2.5:3b"; a bare "llama3.2" means "llama3.2:latest".
fn same_model(a: &str, b: &str) -> bool {
    let norm = |s: &str| if s.contains(':') { s.to_string() } else { format!("{s}:latest") };
    norm(a) == norm(b)
}

#[tauri::command]
pub async fn assistant_status(state: State<'_, AppState>) -> CmdResult<AssistantStatus> {
    let s = settings::get_all(&*state.user()?).map_err(core)?;
    let url = s["ollama_url"].clone();
    let model = s["ollama_model"].clone();
    let models = tauri::async_runtime::spawn_blocking(move || ollama_models(&url))
        .await
        .map_err(|e| err("INTERNAL", e.to_string()))?;
    let reachable = models.is_some();
    let models = models.unwrap_or_default();
    let has_model = models.iter().any(|m| same_model(m, &model));
    Ok(AssistantStatus {
        provider: s["assistant"].clone(),
        ollama: OllamaStatus { reachable, models, has_model },
        claude_has_key: read_key(&state).is_some(),
    })
}

/// Save (or, with an empty string, delete) the Claude API key.
#[tauri::command]
pub async fn assistant_set_key(state: State<'_, AppState>, key: String) -> CmdResult<()> {
    let path = key_path(&state);
    let key = key.trim();
    if key.is_empty() {
        let _ = std::fs::remove_file(&path);
        return Ok(());
    }
    if key.len() > 300 || !key.chars().all(|c| c.is_ascii_graphic()) {
        return Err(err("INVALID", "that does not look like an API key"));
    }
    let io = |e: std::io::Error| err("IO", e.to_string());
    std::fs::create_dir_all(path.parent().unwrap_or(&state.packs.data_dir)).map_err(io)?;
    // Created readable by this user only (never briefly world-readable).
    let mut opts = std::fs::OpenOptions::new();
    opts.write(true).create(true).truncate(true);
    #[cfg(unix)]
    {
        use std::os::unix::fs::{OpenOptionsExt, PermissionsExt};
        opts.mode(0o600);
        // An older key file may exist with wider permissions.
        if path.exists() {
            std::fs::set_permissions(&path, std::fs::Permissions::from_mode(0o600)).map_err(io)?;
        }
    }
    use std::io::Write;
    opts.open(&path).and_then(|mut f| f.write_all(key.as_bytes())).map_err(io)?;
    Ok(())
}

/// Every `/topic/...` link the assistant is allowed to show.
#[tauri::command]
pub async fn assistant_links(state: State<'_, AppState>) -> CmdResult<Vec<String>> {
    Ok(assistant::known_links(&*state.content()?).map_err(core)?.into_iter().collect())
}

/// Note sections related to `text` (question, selection and reply), for "Read first".
#[tauri::command]
pub async fn assistant_suggest(state: State<'_, AppState>, text: String) -> CmdResult<Vec<assistant::Suggestion>> {
    let text: String = text.chars().take(12_000).collect();
    let lang = settings::get_all(&*state.user()?).map_err(core)?["lang"].clone();
    assistant::suggest(&*state.content()?, &lang, &text, 3).map_err(core)
}

#[derive(Clone, Serialize)]
struct Event<'a> {
    id: &'a str,
    kind: &'a str,
    text: String,
}

struct Job {
    provider: String,
    url: String,
    model: String,
    key: Option<String>,
    system: String,
    messages: Vec<ChatMessage>,
}

#[tauri::command]
pub async fn assistant_chat(
    app: AppHandle,
    state: State<'_, AppState>,
    assist: State<'_, AssistantState>,
    id: String,
    messages: Vec<ChatMessage>,
    context: AskContext,
) -> CmdResult<()> {
    if id.is_empty() || id.len() > 64 {
        return Err(err("INVALID", "bad request id"));
    }
    let s = settings::get_all(&*state.user()?).map_err(core)?;
    let provider = s["assistant"].clone();
    let (url, model, key) = match provider.as_str() {
        "ollama" => (s["ollama_url"].clone(), s["ollama_model"].clone(), None),
        "claude" => {
            let Some(k) = read_key(&state) else {
                return Err(err("NO_KEY", "add your Claude API key in Settings › Study assistant"));
            };
            (CLAUDE_URL.to_string(), s["claude_model"].clone(), Some(k))
        }
        _ => return Err(err("OFF", "the study assistant is turned off in Settings")),
    };
    let lang = s["lang"].clone();
    let (system, messages) = {
        let content = state.content()?;
        let last = messages.iter().rev().find(|m| m.role == "user").map(|m| m.content.clone()).unwrap_or_default();
        // Claude has room (and caching) for the whole catalogue; small local models get a focused one.
        let system = assistant::system_prompt(&content, &lang, provider == "claude", &context, &last).map_err(core)?;
        let msgs = assistant::prepare_messages(&content, &lang, &context, &messages).map_err(core)?;
        (system, msgs)
    };

    let cancel = Arc::new(AtomicBool::new(false));
    if let Ok(mut r) = assist.running.lock() {
        r.insert(id.clone(), cancel.clone());
    }
    let job = Job { provider, url, model, key, system, messages };
    std::thread::spawn(move || {
        let emit = |kind: &str, text: String| {
            let _ = app.emit("assistant", Event { id: &id, kind, text });
        };
        let result = if job.provider == "claude" { run_claude(&job, &cancel, &emit) } else { run_ollama(&job, &cancel, &emit) };
        match result {
            Ok(()) => emit("done", String::new()),
            Err(m) => emit("error", m),
        }
        if let Some(st) = tauri::Manager::try_state::<AssistantState>(&app)
            && let Ok(mut r) = st.running.lock()
        {
            r.remove(&id);
        }
    });
    Ok(())
}

#[tauri::command]
pub async fn assistant_cancel(assist: State<'_, AssistantState>, id: String) -> CmdResult<()> {
    if let Ok(r) = assist.running.lock()
        && let Some(c) = r.get(&id)
    {
        c.store(true, Ordering::Relaxed);
    }
    Ok(())
}

fn http_error(e: ureq::Error, what: &str) -> String {
    match e {
        ureq::Error::Status(code, resp) => {
            let body = resp.into_string().unwrap_or_default();
            let msg = serde_json::from_str::<Value>(&body)
                .ok()
                .and_then(|v| v["error"]["message"].as_str().or(v["error"].as_str()).map(str::to_string))
                .unwrap_or(body);
            format!("{what} returned {code}: {}", msg.chars().take(300).collect::<String>())
        }
        ureq::Error::Transport(t) => format!("could not reach {what}: {t}"),
    }
}

fn run_ollama(job: &Job, cancel: &AtomicBool, emit: &dyn Fn(&str, String)) -> Result<(), String> {
    let mut msgs = vec![json!({"role": "system", "content": job.system})];
    msgs.extend(job.messages.iter().map(|m| json!({"role": m.role, "content": m.content})));
    let body = json!({
        "model": job.model,
        "stream": true,
        "messages": msgs,
        "options": {"num_ctx": 8192, "temperature": 0.3},
    });
    let resp = agent(Duration::from_secs(300))
        .post(&format!("{}/api/chat", job.url.trim_end_matches('/')))
        .send_json(body)
        .map_err(|e| {
            let m = http_error(e, "Ollama");
            if m.contains("could not reach") {
                format!("{m}. Start Ollama (open the Ollama app, or run `ollama serve`) and try again.")
            } else {
                m
            }
        })?;
    for line in BufReader::new(resp.into_reader()).lines() {
        if cancel.load(Ordering::Relaxed) {
            return Ok(());
        }
        let line = line.map_err(|e| e.to_string())?;
        if line.trim().is_empty() {
            continue;
        }
        let v: Value = serde_json::from_str(&line).map_err(|e| e.to_string())?;
        if let Some(e) = v["error"].as_str() {
            return Err(format!("Ollama: {e}"));
        }
        if let Some(t) = v["message"]["content"].as_str()
            && !t.is_empty()
        {
            emit("delta", t.to_string());
        }
        if v["done"].as_bool() == Some(true) {
            break;
        }
    }
    Ok(())
}

fn run_claude(job: &Job, cancel: &AtomicBool, emit: &dyn Fn(&str, String)) -> Result<(), String> {
    let body = json!({
        "model": job.model,
        "max_tokens": 16000,
        "stream": true,
        // The rules and catalogue are identical on every turn, so cache them.
        "system": [{"type": "text", "text": job.system, "cache_control": {"type": "ephemeral"}}],
        "messages": job.messages.iter().map(|m| json!({"role": m.role, "content": m.content})).collect::<Vec<_>>(),
        "output_config": {"effort": "medium"},
        // On a policy decline, the API re-runs the request on a suitable fallback model.
        "fallbacks": "default",
    });
    let resp = agent(Duration::from_secs(600))
        .post(CLAUDE_URL)
        .set("x-api-key", job.key.as_deref().unwrap_or_default())
        .set("anthropic-version", CLAUDE_VERSION)
        .set("anthropic-beta", "server-side-fallback-2026-07-01")
        .send_json(body)
        .map_err(|e| http_error(e, "the Claude API"))?;
    for line in BufReader::new(resp.into_reader()).lines() {
        if cancel.load(Ordering::Relaxed) {
            return Ok(());
        }
        let line = line.map_err(|e| e.to_string())?;
        let Some(data) = line.strip_prefix("data:") else { continue };
        let Ok(v) = serde_json::from_str::<Value>(data.trim()) else { continue };
        match v["type"].as_str() {
            Some("content_block_delta") if v["delta"]["type"] == "text_delta" => {
                if let Some(t) = v["delta"]["text"].as_str() {
                    emit("delta", t.to_string());
                }
            }
            Some("message_delta") => match v["delta"]["stop_reason"].as_str() {
                Some("refusal") => return Err("Claude declined to answer this request.".into()),
                Some("max_tokens") => emit("delta", "\n\n*(The reply hit its length limit.)*".into()),
                _ => {}
            },
            Some("error") => {
                return Err(format!(
                    "Claude API: {}",
                    v["error"]["message"].as_str().unwrap_or("unknown error")
                ));
            }
            Some("message_stop") => break,
            _ => {}
        }
    }
    Ok(())
}

#[derive(Clone, Serialize)]
struct PullEvent {
    status: String,
    completed: u64,
    total: u64,
}

/// Download an Ollama model (`ollama pull`), reporting progress as `assistant-pull` events.
#[tauri::command]
pub async fn assistant_ollama_pull(app: AppHandle, state: State<'_, AppState>, model: String) -> CmdResult<()> {
    if model.is_empty() || model.len() > 100 || !model.chars().all(|c| c.is_ascii_alphanumeric() || "._:/-".contains(c)) {
        return Err(err("INVALID", "bad model name"));
    }
    let url = settings::get_all(&*state.user()?).map_err(core)?["ollama_url"].clone();
    tauri::async_runtime::spawn_blocking(move || -> Result<(), String> {
        let resp = agent(Duration::from_secs(600))
            .post(&format!("{}/api/pull", url.trim_end_matches('/')))
            .send_json(json!({"model": model, "stream": true}))
            .map_err(|e| http_error(e, "Ollama"))?;
        for line in BufReader::new(resp.into_reader()).lines() {
            let line = line.map_err(|e| e.to_string())?;
            let Ok(v) = serde_json::from_str::<Value>(&line) else { continue };
            if let Some(e) = v["error"].as_str() {
                return Err(format!("Ollama: {e}"));
            }
            let _ = app.emit(
                "assistant-pull",
                PullEvent {
                    status: v["status"].as_str().unwrap_or_default().to_string(),
                    completed: v["completed"].as_u64().unwrap_or(0),
                    total: v["total"].as_u64().unwrap_or(0),
                },
            );
        }
        Ok(())
    })
    .await
    .map_err(|e| err("INTERNAL", e.to_string()))?
    .map_err(|m| err("NETWORK", m))
}

#[cfg(test)]
mod tests {
    use super::*;

    /// Needs a running Ollama with the model: FEB_TEST_OLLAMA_MODEL=qwen2.5:3b.
    #[test]
    #[ignore]
    fn streams_from_ollama() {
        let model = std::env::var("FEB_TEST_OLLAMA_MODEL").expect("FEB_TEST_OLLAMA_MODEL");
        let job = Job {
            provider: "ollama".into(),
            url: "http://127.0.0.1:11434".into(),
            model,
            key: None,
            system: format!(
                "{}\n\nCatalogue of notes in the app (link: title › section):\n- /topic/math.analysis.mean-value-theorems#rolle — Mean Value Theorems › Rolle's theorem\n",
                feb_core::assistant::SYSTEM_RULES
            ),
            messages: vec![ChatMessage {
                role: "user".into(),
                content: "[Selected text]\n$f'(c)=0$ for some $c\\in(a,b)$\n[My question]\nWhy does Rolle's theorem need f(a)=f(b)? One short paragraph.".into(),
            }],
        };
        let out = Mutex::new(String::new());
        let deltas = std::sync::atomic::AtomicUsize::new(0);
        let t0 = std::time::Instant::now();
        run_ollama(&job, &AtomicBool::new(false), &|kind, text| {
            assert_eq!(kind, "delta");
            deltas.fetch_add(1, Ordering::Relaxed);
            out.lock().unwrap().push_str(&text);
        })
        .unwrap();
        let out = out.into_inner().unwrap();
        eprintln!("{} deltas in {:?}:\n{out}", deltas.load(Ordering::Relaxed), t0.elapsed());
        assert!(deltas.load(Ordering::Relaxed) > 5 && out.len() > 50);
    }

    #[test]
    fn reports_a_missing_ollama_model() {
        let job = Job {
            provider: "ollama".into(),
            url: "http://127.0.0.1:9".into(),
            model: "none".into(),
            key: None,
            system: String::new(),
            messages: vec![ChatMessage { role: "user".into(), content: "hi".into() }],
        };
        let e = run_ollama(&job, &AtomicBool::new(false), &|_, _| {}).unwrap_err();
        assert!(e.contains("Start Ollama"), "{e}");
    }
}
