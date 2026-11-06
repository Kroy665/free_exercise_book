//! Content pack management for the app: trusted keys, sources (bundled / server /
//! folder), the merged pack list for the Downloads page, and install/update/remove.
//! (docs/DATA_AND_PACKS.md)

use feb_core::error::ErrorPayload;
use feb_core::localize::pick;
use feb_core::packs as store;
use feb_packs::source::Source;
use feb_packs::{Manifest, PackEntry, PackError, verify_manifest, version_newer};
use rusqlite::Connection;
use serde::Serialize;
use std::collections::BTreeMap;
use std::path::{Path, PathBuf};
use std::sync::Mutex;
use std::time::{SystemTime, UNIX_EPOCH};

/// Default content server: the `packs` branch of the project repository.
/// Override with the `FEB_PACKS_URL` environment variable (must end with `/`).
pub const DEFAULT_PACKS_URL: &str =
    "https://raw.githubusercontent.com/Kroy665/free_exercise_book/packs/";

pub struct PackConfig {
    pub data_dir: PathBuf,
    pub cache_dir: PathBuf,
    /// Packs shipped inside the installer (or `dist/packs` in debug builds).
    pub bundled_dir: Option<PathBuf>,
    pub remote_url: String,
    pub trusted_keys: Vec<String>,
    /// `FEB_CONTENT_DIR` developer mode: content is imported directly, packs are disabled.
    pub dev_mode: bool,
    /// Serialises installs/removals.
    pub busy: Mutex<()>,
}

pub fn pack_err(e: PackError) -> ErrorPayload {
    ErrorPayload {
        code: e.code(),
        message: e.to_string(),
    }
}

pub fn core_err(e: feb_core::CoreError) -> ErrorPayload {
    ErrorPayload::from(&e)
}

fn io_err(e: std::io::Error) -> ErrorPayload {
    ErrorPayload {
        code: "IO_ERROR",
        message: e.to_string(),
    }
}

/// Public keys whose signatures the app accepts. Release builds trust only the project key.
pub fn trusted_keys() -> Vec<String> {
    #[allow(unused_mut)]
    let mut keys = vec![include_str!("../keys/packs.pub").to_string()];
    #[cfg(debug_assertions)]
    {
        let dev =
            PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../../../dist/dev-key/minisign.pub");
        if let Ok(k) = std::fs::read_to_string(dev) {
            keys.push(k);
        }
    }
    keys
}

fn now() -> u64 {
    SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .map(|d| d.as_secs())
        .unwrap_or(0)
}

impl PackConfig {
    fn remote_dir(&self) -> PathBuf {
        self.data_dir.join("remote-manifest")
    }

    pub fn folder_manifest(&self, dir: &Path) -> Result<Manifest, ErrorPayload> {
        let (bytes, sig) = Source::Folder(dir.to_path_buf())
            .fetch_manifest()
            .map_err(pack_err)?;
        verify_manifest(&bytes, &sig, &self.trusted_keys).map_err(pack_err)
    }

    pub fn bundled_manifest(&self) -> Option<Manifest> {
        let dir = self.bundled_dir.as_ref()?;
        match self.folder_manifest(dir) {
            Ok(m) => Some(m),
            Err(e) => {
                eprintln!("[packs] bundled packs rejected: {}", e.message);
                None
            }
        }
    }

    /// Last verified server manifest (works offline) and when it was fetched.
    pub fn cached_remote(&self) -> Option<(Manifest, u64)> {
        let dir = self.remote_dir();
        let m = self.folder_manifest(&dir).ok()?;
        let at = std::fs::read_to_string(dir.join("checked_at"))
            .ok()?
            .trim()
            .parse()
            .ok()?;
        Some((m, at))
    }

    /// Fetch, verify and cache the server manifest.
    pub fn check_remote(&self) -> Result<Manifest, ErrorPayload> {
        let (bytes, sig) = Source::Remote(self.remote_url.clone())
            .fetch_manifest()
            .map_err(pack_err)?;
        let manifest = verify_manifest(&bytes, &sig, &self.trusted_keys).map_err(pack_err)?;
        let dir = self.remote_dir();
        std::fs::create_dir_all(&dir).map_err(io_err)?;
        std::fs::write(dir.join(feb_packs::MANIFEST_FILE), &bytes).map_err(io_err)?;
        std::fs::write(dir.join(feb_packs::MANIFEST_SIG_FILE), sig).map_err(io_err)?;
        std::fs::write(dir.join("checked_at"), now().to_string()).map_err(io_err)?;
        Ok(manifest)
    }

    /// Best available version of a pack: the newest of bundled and server; bundled wins
    /// a tie (no download needed).
    pub fn best(&self, id: &str) -> Option<(PackEntry, Source)> {
        let bundled = self
            .bundled_manifest()
            .and_then(|m| m.get(id).cloned())
            .zip(self.bundled_dir.clone().map(Source::Folder));
        let remote = self
            .cached_remote()
            .and_then(|(m, _)| m.get(id).cloned())
            .map(|e| (e, Source::Remote(self.remote_url.clone())));
        match (bundled, remote) {
            (Some(b), Some(r)) => Some(if version_newer(&r.0.version, &b.0.version) {
                r
            } else {
                b
            }),
            (b, r) => b.or(r),
        }
    }

    /// Download (or read), verify, decompress and install one pack.
    pub fn install(
        &self,
        content: &Mutex<Connection>,
        entry: &PackEntry,
        source: &Source,
        progress: &mut dyn FnMut(&str, u64, u64),
    ) -> Result<store::InstalledPack, ErrorPayload> {
        let bytes = source
            .fetch_pack(entry, &mut |done, total| progress("download", done, total))
            .map_err(pack_err)?;
        progress("install", entry.size, entry.size);
        let raw = feb_packs::decompress(&bytes).map_err(pack_err)?;
        std::fs::create_dir_all(&self.cache_dir).map_err(io_err)?;
        let tmp = self.cache_dir.join(format!("installing-{}.db", entry.id));
        std::fs::write(&tmp, raw).map_err(io_err)?;
        let _guard = self.busy.lock().map_err(|_| ErrorPayload {
            code: "STATE_POISONED",
            message: "busy lock".into(),
        })?;
        let result = {
            let mut conn = content.lock().map_err(|_| ErrorPayload {
                code: "STATE_POISONED",
                message: "db lock".into(),
            })?;
            store::install_pack_db(
                &mut conn,
                &tmp,
                &entry.id,
                &entry.version,
                &entry.sha256,
                entry.size as i64,
            )
            .map_err(core_err)
        };
        std::fs::remove_file(&tmp).ok();
        result
    }

    /// First run: install every bundled pack. Later runs: update installed packs whose
    /// bundled version is newer (the app was updated). Never re-installs a removed pack.
    pub fn sync_bundled(&self, content: &Mutex<Connection>) {
        if self.dev_mode {
            return;
        }
        let Some(manifest) = self.bundled_manifest() else {
            return;
        };
        let Some(dir) = self.bundled_dir.clone() else {
            return;
        };
        let marker = self.data_dir.join("packs-initialized");
        let first_run = !marker.exists();
        if let Ok(mut c) = content.lock() {
            match store::purge_unmanaged(&mut c) {
                Ok(n) if n > 0 => {
                    eprintln!("[packs] removed {n} topic(s) not installed from packs")
                }
                Err(e) => eprintln!("[packs] cleanup failed: {e}"),
                _ => {}
            }
        }
        let installed: BTreeMap<String, String> = content
            .lock()
            .ok()
            .and_then(|c| store::list_installed(&c).ok())
            .unwrap_or_default()
            .into_iter()
            .map(|p| (p.id, p.version))
            .collect();
        let source = Source::Folder(dir);
        for entry in &manifest.packs {
            let wanted = match installed.get(&entry.id) {
                None => first_run,
                Some(v) => version_newer(&entry.version, v),
            };
            if wanted {
                match self.install(content, entry, &source, &mut |_, _, _| {}) {
                    Ok(p) => eprintln!("[packs] installed bundled {}@{}", p.id, p.version),
                    Err(e) => eprintln!("[packs] bundled {} failed: {}", entry.id, e.message),
                }
            }
        }
        std::fs::write(marker, "1").ok();
    }
}

// ---------------------------------------------------------------- view for the UI

#[derive(Debug, Clone, Serialize)]
pub struct PackItem {
    pub id: String,
    pub title: String,
    pub summary: Option<String>,
    pub subject: String,
    pub subject_title: String,
    pub unit: String,
    pub unit_title: String,
    pub sort: (i64, i64, i64),
    pub langs: Vec<String>,
    pub questions: usize,
    pub sections: usize,
    pub size: u64,
    /// "installed" | "update" | "available"
    pub state: &'static str,
    pub installed_version: Option<String>,
    pub available_version: Option<String>,
    /// "bundled" (no download needed) | "server" | null
    pub source: Option<&'static str>,
}

#[derive(Debug, Clone, Serialize)]
pub struct RemoteStatus {
    pub url: String,
    pub checked_at: Option<u64>,
    pub error: Option<ErrorPayload>,
}

#[derive(Debug, Clone, Serialize)]
pub struct PacksView {
    pub items: Vec<PackItem>,
    pub remote: RemoteStatus,
    pub dev_mode: bool,
    pub updates: usize,
}

fn item_from_entry(e: &PackEntry, lang: &str) -> PackItem {
    PackItem {
        id: e.id.clone(),
        title: pick(&e.title, lang),
        summary: e.summary.as_ref().map(|s| pick(s, lang)),
        subject: e.subject.clone(),
        subject_title: pick(&e.subject_title, lang),
        unit: e.unit.clone(),
        unit_title: pick(&e.unit_title, lang),
        sort: (e.subject_order, e.unit_order, e.order),
        langs: e.langs.clone(),
        questions: e.counts.questions,
        sections: e.counts.sections,
        size: e.size,
        state: "available",
        installed_version: None,
        available_version: Some(e.version.clone()),
        source: None,
    }
}

pub fn view(
    cfg: &PackConfig,
    content: &Connection,
    lang: &str,
    remote_error: Option<ErrorPayload>,
) -> Result<PacksView, ErrorPayload> {
    let installed = store::list_installed(content).map_err(core_err)?;
    let bundled = cfg.bundled_manifest();
    let remote = cfg.cached_remote();

    let mut items: BTreeMap<String, PackItem> = BTreeMap::new();
    for (m, origin) in [
        (bundled.as_ref(), "bundled"),
        (remote.as_ref().map(|(m, _)| m), "server"),
    ] {
        let Some(m) = m else { continue };
        for e in &m.packs {
            let newer = items
                .get(&e.id)
                .and_then(|i| i.available_version.as_deref())
                .is_none_or(|v| version_newer(&e.version, v));
            if newer {
                let mut it = item_from_entry(e, lang);
                it.source = Some(origin);
                items.insert(e.id.clone(), it);
            }
        }
    }
    for p in &installed {
        let it = match items.get_mut(&p.id) {
            Some(it) => it,
            None => {
                // Installed, but no longer listed anywhere: describe it from content.db.
                let t = feb_core::library::topic(content, &p.id, lang).map_err(core_err)?;
                items.insert(
                    p.id.clone(),
                    PackItem {
                        id: p.id.clone(),
                        title: t.title,
                        summary: t.summary,
                        subject: t.subject_id,
                        subject_title: t.subject_title,
                        unit: t.unit_id,
                        unit_title: t.unit_title,
                        sort: (i64::MAX, i64::MAX, i64::MAX),
                        langs: t.available_langs,
                        questions: t.question_count as usize,
                        sections: t.sections.len(),
                        size: p.size as u64,
                        state: "installed",
                        installed_version: None,
                        available_version: None,
                        source: None,
                    },
                );
                items.get_mut(&p.id).unwrap()
            }
        };
        it.installed_version = Some(p.version.clone());
        it.state = match &it.available_version {
            Some(v) if version_newer(v, &p.version) => "update",
            _ => "installed",
        };
    }
    let mut items: Vec<PackItem> = items.into_values().collect();
    items.sort_by(|a, b| a.sort.cmp(&b.sort).then(a.id.cmp(&b.id)));
    let updates = items.iter().filter(|i| i.state == "update").count();
    Ok(PacksView {
        items,
        remote: RemoteStatus {
            url: cfg.remote_url.clone(),
            checked_at: remote.map(|(_, at)| at),
            error: remote_error,
        },
        dev_mode: cfg.dev_mode,
        updates,
    })
}

#[cfg(test)]
mod tests {
    //! Full pack lifecycle against a local HTTP "content server".
    use super::*;
    use feb_core::import::load_dir;
    use feb_packs::{Counts, Manifest, PackEntry, sign};
    use std::io::{Read, Write};
    use std::net::TcpListener;

    const TOPIC: &str = "hist.modern.revolt-1857";

    /// Build a signed pack directory from the sample content, forcing `version`.
    fn make_packs(dir: &Path, version: &str, secret: &str) {
        std::fs::create_dir_all(dir).unwrap();
        let root = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../../../content");
        let mut packs = Vec::new();
        for s in load_dir(&root).unwrap() {
            for u in &s.units {
                for t in &u.topics {
                    let mut t = t.clone();
                    t.topic.version = version.to_string();
                    let tmp = dir.join("tmp.db");
                    let c = feb_core::packs::build_pack_db(&tmp, &s, u, &t).unwrap();
                    let packed = feb_packs::compress(&std::fs::read(&tmp).unwrap()).unwrap();
                    std::fs::remove_file(&tmp).unwrap();
                    let file = format!("{}@{version}.pack", t.topic.id);
                    std::fs::write(dir.join(&file), &packed).unwrap();
                    packs.push(PackEntry {
                        id: t.topic.id.clone(),
                        version: version.into(),
                        title: t.topic.title.clone(),
                        summary: None,
                        subject: s.subject.id.clone(),
                        subject_title: s.subject.title.clone(),
                        subject_order: 1,
                        unit: u.unit.id.clone(),
                        unit_title: u.unit.title.clone(),
                        unit_order: 1,
                        order: 1,
                        langs: vec!["en".into(), "bn".into()],
                        exams: vec![],
                        status: "ai-generated".into(),
                        estimated_minutes: None,
                        counts: Counts {
                            sections: c.sections,
                            questions: c.questions,
                        },
                        size: packed.len() as u64,
                        sha256: feb_packs::sha256_hex(&packed),
                        file,
                    });
                }
            }
        }
        let m = Manifest {
            schema: 1,
            generated_at: 0,
            min_app_version: "0.1.0".into(),
            packs,
        };
        let bytes = serde_json::to_vec(&m).unwrap();
        std::fs::write(dir.join(feb_packs::MANIFEST_FILE), &bytes).unwrap();
        std::fs::write(
            dir.join(feb_packs::MANIFEST_SIG_FILE),
            sign::sign(secret, &bytes, "t").unwrap(),
        )
        .unwrap();
    }

    /// Minimal static file server (one request per connection). Returns the base URL.
    fn serve(dir: PathBuf) -> String {
        let listener = TcpListener::bind("127.0.0.1:0").unwrap();
        let addr = listener.local_addr().unwrap();
        std::thread::spawn(move || {
            for stream in listener.incoming() {
                let Ok(mut s) = stream else { continue };
                let mut buf = [0u8; 4096];
                let n = s.read(&mut buf).unwrap_or(0);
                let req = String::from_utf8_lossy(&buf[..n]);
                let path = req
                    .split_whitespace()
                    .nth(1)
                    .unwrap_or("/")
                    .trim_start_matches('/')
                    .to_string();
                match std::fs::read(dir.join(&path)) {
                    Ok(body) => {
                        let _ = write!(
                            s,
                            "HTTP/1.1 200 OK\r\nContent-Length: {}\r\nConnection: close\r\n\r\n",
                            body.len()
                        );
                        let _ = s.write_all(&body);
                    }
                    Err(_) => {
                        let _ = s.write_all(b"HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\nConnection: close\r\n\r\n");
                    }
                }
            }
        });
        format!("http://{addr}/")
    }

    fn installed_version(c: &Mutex<Connection>) -> Option<String> {
        store::installed(&c.lock().unwrap(), TOPIC)
            .unwrap()
            .map(|p| p.version)
    }

    #[test]
    fn lifecycle_bundled_update_tamper_remove() {
        let tmp = std::env::temp_dir().join(format!("feb-app-packs-{}", std::process::id()));
        let _ = std::fs::remove_dir_all(&tmp);
        let key = sign::generate_keypair("test").unwrap();
        let rogue = sign::generate_keypair("rogue").unwrap();
        make_packs(&tmp.join("bundled"), "1.0.0", &key.secret);
        make_packs(&tmp.join("server"), "1.1.0", &key.secret);
        make_packs(&tmp.join("rogue"), "9.0.0", &rogue.secret);

        let cfg = |remote: String| PackConfig {
            data_dir: tmp.join("data"),
            cache_dir: tmp.join("cache"),
            bundled_dir: Some(tmp.join("bundled")),
            remote_url: remote,
            trusted_keys: vec![key.public.clone()],
            dev_mode: false,
            busy: Mutex::new(()),
        };
        std::fs::create_dir_all(tmp.join("data")).unwrap();
        let (content, _user) = feb_core::db::open_in_memory().unwrap();
        let content = Mutex::new(content);
        let packs = cfg(serve(tmp.join("server")));

        // First run installs the bundled pack, offline.
        packs.sync_bundled(&content);
        assert_eq!(installed_version(&content).as_deref(), Some("1.0.0"));
        let v = view(&packs, &content.lock().unwrap(), "bn", None).unwrap();
        assert_eq!(
            (v.items[0].state, v.items[0].title.as_str()),
            ("installed", "১৮৫৭ সালের মহাবিদ্রোহ")
        );

        // The server has 1.1.0 → shown as an update and installed from the server.
        packs.check_remote().unwrap();
        let v = view(&packs, &content.lock().unwrap(), "en", None).unwrap();
        assert_eq!((v.items[0].state, v.updates), ("update", 1));
        let (entry, source) = packs.best(TOPIC).unwrap();
        assert!(matches!(source, Source::Remote(_)));
        let mut phases = Vec::new();
        packs
            .install(&content, &entry, &source, &mut |p, _, _| {
                phases.push(p.to_string())
            })
            .unwrap();
        assert_eq!(installed_version(&content).as_deref(), Some("1.1.0"));
        assert!(
            phases.contains(&"download".to_string()) && phases.contains(&"install".to_string())
        );

        // A corrupted download is rejected and the installed version stays.
        let file = tmp.join("server").join(&entry.file);
        let mut bytes = std::fs::read(&file).unwrap();
        *bytes.last_mut().unwrap() ^= 0xff;
        std::fs::write(&file, bytes).unwrap();
        let err = packs
            .install(&content, &entry, &source, &mut |_, _, _| {})
            .unwrap_err();
        assert_eq!(err.code, "PACK_HASH_MISMATCH");
        assert_eq!(installed_version(&content).as_deref(), Some("1.1.0"));

        // Removing works, and a later start does not silently re-install it.
        store::remove_pack(&mut content.lock().unwrap(), TOPIC).unwrap();
        packs.sync_bundled(&content);
        assert_eq!(installed_version(&content), None);
        let v = view(&packs, &content.lock().unwrap(), "en", None).unwrap();
        assert_eq!(v.items[0].state, "available");

        // A server signed by an unknown key is refused.
        let rogue_cfg = cfg(serve(tmp.join("rogue")));
        assert_eq!(
            rogue_cfg.check_remote().unwrap_err().code,
            "PACK_SIGNATURE_INVALID"
        );
        // An unreachable server is a NETWORK error (shown as "offline" in the UI).
        assert_eq!(
            cfg("http://127.0.0.1:9/".into())
                .check_remote()
                .unwrap_err()
                .code,
            "NETWORK"
        );

        std::fs::remove_dir_all(&tmp).ok();
    }
}
