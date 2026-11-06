//! Key generation and signing (packer only). The app never holds a secret key.

use crate::{PackError, Result};

pub struct KeyPairStrings {
    /// minisign `.pub` file contents (safe to publish / compile into the app).
    pub public: String,
    /// minisign secret key file contents (unencrypted; keep private).
    pub secret: String,
}

fn err(e: impl std::fmt::Display) -> PackError {
    PackError::Signature(e.to_string())
}

pub fn generate_keypair(comment: &str) -> Result<KeyPairStrings> {
    let kp = minisign::KeyPair::generate_unencrypted_keypair().map_err(err)?;
    Ok(KeyPairStrings {
        public: kp.pk.to_box().map_err(err)?.into_string(),
        secret: kp.sk.to_box(Some(comment)).map_err(err)?.into_string(),
    })
}

/// Public key (`.pub` contents) belonging to a secret key.
pub fn public_from_secret(secret: &str) -> Result<String> {
    let sk = minisign::SecretKeyBox::from_string(secret.trim())
        .map_err(err)?
        .into_unencrypted_secret_key()
        .map_err(err)?;
    Ok(minisign::PublicKey::from_secret_key(&sk)
        .map_err(err)?
        .to_box()
        .map_err(err)?
        .into_string())
}

/// Sign `data`, returning minisign signature file contents.
pub fn sign(secret: &str, data: &[u8], trusted_comment: &str) -> Result<String> {
    let sk = minisign::SecretKeyBox::from_string(secret.trim())
        .map_err(err)?
        .into_unencrypted_secret_key()
        .map_err(err)?;
    let sig = minisign::sign(
        None,
        &sk,
        data,
        Some(trusted_comment),
        Some("Free Exercise Book content manifest"),
    )
    .map_err(err)?;
    Ok(sig.into_string())
}
