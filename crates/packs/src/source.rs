//! Where packs come from: the content server (HTTPS) or a local folder
//! (bundled with the installer, or a USB copy of a pack directory).

use crate::{
    MANIFEST_FILE, MANIFEST_SIG_FILE, MAX_MANIFEST_BYTES, MAX_PACK_BYTES, PackEntry, PackError,
    Result,
};
use std::io::Read;
use std::path::PathBuf;
use std::time::Duration;

#[derive(Debug, Clone)]
pub enum Source {
    /// Base URL ending with `/`; files are fetched as `<base><name>`.
    Remote(String),
    /// Directory containing `manifest.json`, its signature and the `.pack` files.
    Folder(PathBuf),
}

fn agent() -> ureq::Agent {
    ureq::AgentBuilder::new()
        .timeout_connect(Duration::from_secs(15))
        .timeout_read(Duration::from_secs(60))
        .user_agent(concat!("FreeExerciseBook/", env!("CARGO_PKG_VERSION")))
        .build()
}

fn read_limited(
    mut r: impl Read,
    max: u64,
    what: &str,
    total: u64,
    progress: &mut dyn FnMut(u64, u64),
) -> Result<Vec<u8>> {
    let mut out = Vec::with_capacity(total.min(max) as usize);
    let mut buf = [0u8; 64 * 1024];
    loop {
        let n = r.read(&mut buf)?;
        if n == 0 {
            break;
        }
        out.extend_from_slice(&buf[..n]);
        if out.len() as u64 > max {
            return Err(PackError::TooLarge(what.to_string()));
        }
        progress(out.len() as u64, total);
    }
    Ok(out)
}

impl Source {
    pub fn describe(&self) -> String {
        match self {
            Source::Remote(u) => u.clone(),
            Source::Folder(p) => p.display().to_string(),
        }
    }

    fn get(&self, name: &str, max: u64, progress: &mut dyn FnMut(u64, u64)) -> Result<Vec<u8>> {
        match self {
            Source::Remote(base) => {
                let url = format!("{base}{name}");
                let resp = agent().get(&url).call().map_err(|e| match e {
                    ureq::Error::Status(code, _) => {
                        PackError::Network(format!("{url}: HTTP {code}"))
                    }
                    ureq::Error::Transport(t) => PackError::Network(t.to_string()),
                })?;
                let total = resp
                    .header("Content-Length")
                    .and_then(|v| v.parse().ok())
                    .unwrap_or(0);
                read_limited(resp.into_reader(), max, name, total, progress)
            }
            Source::Folder(dir) => {
                let f = std::fs::File::open(dir.join(name))?;
                let total = f.metadata()?.len();
                read_limited(f, max, name, total, progress)
            }
        }
    }

    /// Returns (manifest bytes, signature text). Verify with [`crate::verify_manifest`].
    pub fn fetch_manifest(&self) -> Result<(Vec<u8>, String)> {
        let bytes = self.get(MANIFEST_FILE, MAX_MANIFEST_BYTES, &mut |_, _| {})?;
        let sig = self.get(MANIFEST_SIG_FILE, 64 * 1024, &mut |_, _| {})?;
        let sig = String::from_utf8(sig)
            .map_err(|_| PackError::Signature("signature is not text".into()))?;
        Ok((bytes, sig))
    }

    /// Download a pack and check it against its (signed) manifest entry.
    pub fn fetch_pack(
        &self,
        entry: &PackEntry,
        progress: &mut dyn FnMut(u64, u64),
    ) -> Result<Vec<u8>> {
        let bytes = self.get(&entry.file, MAX_PACK_BYTES, &mut |done, total| {
            progress(done, if total == 0 { entry.size } else { total })
        })?;
        crate::check_pack(entry, &bytes)?;
        Ok(bytes)
    }
}
