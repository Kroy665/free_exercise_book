//! feb-packer: build signed content packs from `content/` (docs/DATA_AND_PACKS.md §1).
//!
//!   feb-packer build <content-dir> --out <dir> [--key <file> | --dev-key <dir> | --auto-key <dir>]
//!   feb-packer keygen --secret <file> --public <file>
//!
//! Signing key, in order: `--key <file>`, env `FEB_PACK_SIGNING_KEY` (key file contents,
//! used in CI), the maintainer key `~/.config/free-exercise-book/pack-signing.key` (only
//! with `--auto-key`), or a development key in `--dev-key`/`--auto-key <dir>` (created on
//! first use; untrusted: only debug builds of the app accept it).

use feb_core::import::{load_dir, load_exams};
use feb_core::packs::build_pack_db;
use feb_packs::sign;
use feb_packs::{Counts, MANIFEST_FILE, MANIFEST_SCHEMA, MANIFEST_SIG_FILE, Manifest, PackEntry};
use std::path::{Path, PathBuf};
use std::process::ExitCode;
use std::time::{SystemTime, UNIX_EPOCH};

type Res<T> = Result<T, String>;

fn usage() -> ExitCode {
    eprintln!(
        "usage:\n  feb-packer build <content-dir> --out <dir> [--key <file> | --dev-key <dir> | --auto-key <dir>]\n  feb-packer keygen --secret <file> --public <file>"
    );
    ExitCode::from(2)
}

fn flag(args: &[String], name: &str) -> Option<String> {
    args.iter()
        .position(|a| a == name)
        .and_then(|i| args.get(i + 1).cloned())
}

fn write(path: &Path, data: impl AsRef<[u8]>) -> Res<()> {
    if let Some(dir) = path.parent() {
        std::fs::create_dir_all(dir).map_err(|e| format!("{}: {e}", dir.display()))?;
    }
    std::fs::write(path, data).map_err(|e| format!("{}: {e}", path.display()))
}

fn read(path: &Path) -> Res<String> {
    std::fs::read_to_string(path).map_err(|e| format!("{}: {e}", path.display()))
}

fn keygen(args: &[String]) -> Res<()> {
    let (Some(secret), Some(public)) = (flag(args, "--secret"), flag(args, "--public")) else {
        return Err("keygen needs --secret and --public".into());
    };
    let secret = PathBuf::from(secret);
    if secret.exists() {
        return Err(format!(
            "{} already exists; refusing to overwrite a signing key",
            secret.display()
        ));
    }
    let kp = sign::generate_keypair("Free Exercise Book content signing key")
        .map_err(|e| e.to_string())?;
    write(&secret, &kp.secret)?;
    #[cfg(unix)]
    {
        use std::os::unix::fs::PermissionsExt;
        std::fs::set_permissions(&secret, std::fs::Permissions::from_mode(0o600)).ok();
    }
    write(Path::new(&public), &kp.public)?;
    println!(
        "secret key: {} (keep private, back it up)\npublic key: {public}",
        secret.display()
    );
    Ok(())
}

/// Returns the secret key contents and a label for messages.
fn signing_key(args: &[String]) -> Res<(String, String)> {
    if let Some(path) = flag(args, "--key") {
        return Ok((read(Path::new(&path))?, format!("key file {path}")));
    }
    if let Ok(k) = std::env::var("FEB_PACK_SIGNING_KEY")
        && !k.trim().is_empty()
    {
        return Ok((k, "FEB_PACK_SIGNING_KEY".into()));
    }
    let auto = flag(args, "--auto-key");
    if auto.is_some() {
        let home = std::env::var_os("HOME").or_else(|| std::env::var_os("USERPROFILE"));
        if let Some(home) = home {
            let k = PathBuf::from(home).join(".config/free-exercise-book/pack-signing.key");
            if k.exists() {
                return Ok((read(&k)?, format!("maintainer key {}", k.display())));
            }
        }
    }
    if let Some(dir) = flag(args, "--dev-key").or(auto) {
        let dir = PathBuf::from(dir);
        let (sk, pk) = (dir.join("minisign.key"), dir.join("minisign.pub"));
        if !sk.exists() {
            let kp = sign::generate_keypair("Free Exercise Book DEVELOPMENT key (untrusted)")
                .map_err(|e| e.to_string())?;
            write(&sk, &kp.secret)?;
            write(&pk, &kp.public)?;
        }
        return Ok((
            read(&sk)?,
            format!("DEVELOPMENT key in {} (debug builds only)", dir.display()),
        ));
    }
    Err(
        "no signing key: pass --key <file>, set FEB_PACK_SIGNING_KEY, or use --dev-key <dir>"
            .into(),
    )
}

fn build(args: &[String]) -> Res<()> {
    let content = args
        .get(1)
        .filter(|a| !a.starts_with("--"))
        .ok_or("build needs <content-dir>")?;
    let out = PathBuf::from(flag(args, "--out").ok_or("build needs --out <dir>")?);
    let (secret, key_label) = signing_key(args)?;

    let subjects = load_dir(Path::new(content)).map_err(|e| e.to_string())?;
    std::fs::create_dir_all(&out).map_err(|e| format!("{}: {e}", out.display()))?;
    // Remove outputs of previous builds so removed topics disappear.
    for entry in std::fs::read_dir(&out)
        .map_err(|e| e.to_string())?
        .flatten()
    {
        let p = entry.path();
        let name = p.file_name().and_then(|n| n.to_str()).unwrap_or_default();
        if name.ends_with(".pack") || name == MANIFEST_FILE || name == MANIFEST_SIG_FILE {
            std::fs::remove_file(&p).map_err(|e| format!("{}: {e}", p.display()))?;
        }
    }

    let mut packs = Vec::new();
    for s in &subjects {
        for u in &s.units {
            for t in &u.topics {
                let topic = &t.topic;
                let tmp = out.join(format!(".tmp-{}.db", topic.id));
                let counts =
                    build_pack_db(&tmp, s, u, t).map_err(|e| format!("{}: {e}", topic.id))?;
                let raw = std::fs::read(&tmp).map_err(|e| e.to_string())?;
                std::fs::remove_file(&tmp).ok();
                let packed = feb_packs::compress(&raw).map_err(|e| e.to_string())?;
                let file = format!("{}@{}.pack", topic.id, topic.version);
                write(&out.join(&file), &packed)?;
                packs.push(PackEntry {
                    id: topic.id.clone(),
                    version: topic.version.clone(),
                    title: topic.title.clone(),
                    summary: topic.summary.clone(),
                    subject: s.subject.id.clone(),
                    subject_title: s.subject.title.clone(),
                    subject_order: s.subject.order,
                    unit: u.unit.id.clone(),
                    unit_title: u.unit.title.clone(),
                    unit_order: u.unit.order,
                    order: topic.order,
                    langs: t.notes.iter().map(|(l, _)| l.clone()).collect(),
                    exams: topic.exams.clone(),
                    status: topic.status.clone(),
                    estimated_minutes: topic.estimated_minutes,
                    counts: Counts {
                        sections: counts.sections,
                        questions: counts.questions,
                    },
                    size: packed.len() as u64,
                    sha256: feb_packs::sha256_hex(&packed),
                    file,
                });
                println!(
                    "  {:<40} {:>8} bytes  {:>3} sections  {:>3} questions",
                    topic.id,
                    packed.len(),
                    counts.sections,
                    counts.questions
                );
            }
        }
    }
    packs.sort_by(|a, b| {
        (a.subject_order, a.unit_order, a.order).cmp(&(b.subject_order, b.unit_order, b.order))
    });

    let generated_at = std::env::var("SOURCE_DATE_EPOCH")
        .ok()
        .and_then(|v| v.parse().ok())
        .unwrap_or_else(|| {
            SystemTime::now()
                .duration_since(UNIX_EPOCH)
                .map(|d| d.as_secs())
                .unwrap_or(0)
        });
    let exams = load_exams(Path::new(content))
        .map_err(|e| e.to_string())?
        .iter()
        .map(serde_json::to_value)
        .collect::<Result<Vec<_>, _>>()
        .map_err(|e| e.to_string())?;
    println!("  {} exam pattern(s)", exams.len());
    let manifest = Manifest {
        schema: MANIFEST_SCHEMA,
        generated_at,
        min_app_version: "0.1.0".into(),
        packs,
        exams,
    };
    let bytes = serde_json::to_vec_pretty(&manifest).map_err(|e| e.to_string())?;
    let sig = sign::sign(
        &secret,
        &bytes,
        &format!("timestamp:{generated_at}\tfile:{MANIFEST_FILE}"),
    )
    .map_err(|e| e.to_string())?;
    write(&out.join(MANIFEST_FILE), &bytes)?;
    write(&out.join(MANIFEST_SIG_FILE), sig)?;
    println!(
        "{} packs -> {} (signed with {key_label})",
        manifest.packs.len(),
        out.display()
    );
    Ok(())
}

fn main() -> ExitCode {
    let args: Vec<String> = std::env::args().skip(1).collect();
    let result = match args.first().map(String::as_str) {
        Some("build") => build(&args),
        Some("keygen") => keygen(&args),
        _ => return usage(),
    };
    match result {
        Ok(()) => ExitCode::SUCCESS,
        Err(e) => {
            eprintln!("error: {e}");
            ExitCode::FAILURE
        }
    }
}
