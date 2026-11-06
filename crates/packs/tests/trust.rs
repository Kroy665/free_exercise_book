//! Signature and integrity checks must reject anything not produced by a trusted key.

#![cfg(feature = "sign")]

use feb_packs::{
    Counts, Manifest, PackEntry, check_pack, compress, decompress, sha256_hex, sign,
    verify_manifest,
};

fn manifest_with(pack: &[u8]) -> Manifest {
    Manifest {
        schema: 1,
        generated_at: 0,
        min_app_version: "0.1.0".into(),
        exams: vec![],
        packs: vec![PackEntry {
            id: "a.b.c".into(),
            version: "1.0.0".into(),
            title: [("en".to_string(), "T".to_string())].into(),
            summary: None,
            subject: "a".into(),
            subject_title: Default::default(),
            subject_order: 1,
            unit: "a.b".into(),
            unit_title: Default::default(),
            unit_order: 1,
            order: 1,
            langs: vec!["en".into()],
            exams: vec![],
            status: "ai-generated".into(),
            estimated_minutes: None,
            counts: Counts::default(),
            file: "a.b.c@1.0.0.pack".into(),
            size: pack.len() as u64,
            sha256: sha256_hex(pack),
        }],
    }
}

#[test]
fn sign_verify_and_tamper() {
    let kp = sign::generate_keypair("test").unwrap();
    let other = sign::generate_keypair("other").unwrap();
    assert_eq!(
        sign::public_from_secret(&kp.secret).unwrap().trim(),
        kp.public.trim()
    );

    let pack = compress(b"hello pack").unwrap();
    let m = manifest_with(&pack);
    let bytes = serde_json::to_vec(&m).unwrap();
    let sig = sign::sign(&kp.secret, &bytes, "t").unwrap();

    // Good signature with the right key (also when other keys are trusted too).
    let ok = verify_manifest(&bytes, &sig, &[other.public.clone(), kp.public.clone()]).unwrap();
    assert_eq!(ok.packs[0].id, "a.b.c");
    // Wrong key.
    assert!(verify_manifest(&bytes, &sig, std::slice::from_ref(&other.public)).is_err());
    // No keys.
    assert!(verify_manifest(&bytes, &sig, &[]).is_err());
    // Tampered manifest (one byte changed).
    let mut bad = bytes.clone();
    let i = bad.iter().position(|&b| b == b'T').unwrap();
    bad[i] = b'X';
    assert!(verify_manifest(&bad, &sig, std::slice::from_ref(&kp.public)).is_err());

    // Pack integrity.
    check_pack(&ok.packs[0], &pack).unwrap();
    let mut corrupt = pack.clone();
    *corrupt.last_mut().unwrap() ^= 1;
    assert_eq!(
        check_pack(&ok.packs[0], &corrupt).unwrap_err().code(),
        "PACK_HASH_MISMATCH"
    );
    assert_eq!(decompress(&pack).unwrap(), b"hello pack");
}

#[test]
fn rejects_path_traversal_even_if_signed() {
    let kp = sign::generate_keypair("test").unwrap();
    let mut m = manifest_with(b"x");
    m.packs[0].file = "../../etc/passwd".into();
    let bytes = serde_json::to_vec(&m).unwrap();
    let sig = sign::sign(&kp.secret, &bytes, "t").unwrap();
    assert!(verify_manifest(&bytes, &sig, &[kp.public]).is_err());
}

#[test]
fn versions() {
    assert!(feb_packs::version_newer("0.10.0", "0.9.9"));
    assert!(feb_packs::version_newer("1.0.1", "1.0.0"));
    assert!(!feb_packs::version_newer("1.0.0", "1.0.0"));
}
