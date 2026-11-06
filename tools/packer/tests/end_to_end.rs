//! packer build -> verify manifest -> check + decompress + install every pack.

use std::path::PathBuf;
use std::process::Command;

#[test]
fn build_verify_install() {
    let root = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../..");
    let tmp = std::env::temp_dir().join(format!("feb-packer-e2e-{}", std::process::id()));
    let out = tmp.join("out");
    let status = Command::new(env!("CARGO_BIN_EXE_feb-packer"))
        .args([
            "build",
            root.join("content").to_str().unwrap(),
            "--out",
            out.to_str().unwrap(),
        ])
        .args(["--dev-key", tmp.join("key").to_str().unwrap()])
        .env_remove("FEB_PACK_SIGNING_KEY")
        .status()
        .unwrap();
    assert!(status.success());

    let public = std::fs::read_to_string(tmp.join("key/minisign.pub")).unwrap();
    let bytes = std::fs::read(out.join("manifest.json")).unwrap();
    let sig = std::fs::read_to_string(out.join("manifest.json.minisig")).unwrap();
    let manifest = feb_packs::verify_manifest(&bytes, &sig, &[public]).unwrap();
    assert!(!manifest.packs.is_empty());

    let (mut content, user) = feb_core::db::open_in_memory().unwrap();
    for p in &manifest.packs {
        let packed = std::fs::read(out.join(&p.file)).unwrap();
        feb_packs::check_pack(p, &packed).unwrap();
        let db = tmp.join(format!("{}.db", p.id));
        std::fs::write(&db, feb_packs::decompress(&packed).unwrap()).unwrap();
        feb_core::packs::install_pack_db(
            &mut content,
            &db,
            &p.id,
            &p.version,
            &p.sha256,
            p.size as i64,
        )
        .unwrap();
        let q = feb_core::practice::questions_for_topic(&content, &p.id, "en").unwrap();
        assert_eq!(q.len(), p.counts.questions);
    }
    assert_eq!(
        feb_core::library::tree(&content, &user, "bn").unwrap()[0].title,
        "ইতিহাস"
    );

    // Rebuilding with the same input and timestamp gives byte-identical packs.
    let first = std::fs::read(out.join(&manifest.packs[0].file)).unwrap();
    assert!(
        Command::new(env!("CARGO_BIN_EXE_feb-packer"))
            .args([
                "build",
                root.join("content").to_str().unwrap(),
                "--out",
                out.to_str().unwrap()
            ])
            .args(["--dev-key", tmp.join("key").to_str().unwrap()])
            .status()
            .unwrap()
            .success()
    );
    assert_eq!(
        first,
        std::fs::read(out.join(&manifest.packs[0].file)).unwrap()
    );
    std::fs::remove_dir_all(&tmp).ok();
}
