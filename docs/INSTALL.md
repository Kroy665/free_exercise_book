# Install Free Exercise Book

Free Exercise Book is free and works **offline** after installation. Pick the file for your operating system from the [latest release](https://github.com/Kroy665/free_exercise_book/releases).

> **Pre-alpha (v0.1.0).** Installers are **not code-signed yet** (signing certificates cost money; see [SPEC §7](SPEC.md#7-open-questions)). Your operating system will show a warning the first time. The steps below explain how to open the app safely. Every release also lists the files' SHA-256 checksums.

## Which file do I need?

| Operating system | File | Notes |
|---|---|---|
| **Windows 10 / 11** (64-bit) | `…_x64-setup.exe` | Recommended. Installs for the current user. |
| | `…_x64_en-US.msi` | For IT admins / installing for all users. |
| **macOS 11+** (Apple Silicon and Intel) | `…_universal.dmg` | One file works on both M-series and Intel Macs. |
| **Linux** (Ubuntu, Debian, Mint) | `…_amd64.deb` | |
| **Linux** (Fedora, RHEL, openSUSE) | `…x86_64.rpm` | |
| **Linux** (any distribution) | `…_amd64.AppImage` | Portable: no install needed. |

## Windows

1. Download the **`setup.exe`** file and double-click it.
2. If you see **"Windows protected your PC"** (SmartScreen), click **More info → Run anyway**. This appears because the installer is not code-signed yet.
3. Follow the installer. Open **Free Exercise Book** from the Start menu.

The app needs **Microsoft Edge WebView2**, which is already installed on Windows 10 (updated) and Windows 11. If it is missing, the installer downloads it automatically (internet needed once).

## macOS

1. Download the **`.dmg`** file, open it, and drag **Free Exercise Book** into **Applications**.
2. The first time you open it, macOS says it **can't verify the developer**. To open it anyway:
   - Open **System Settings → Privacy & Security**, scroll down, and click **Open Anyway** next to *"Free Exercise Book" was blocked*. Then confirm with **Open**.
   - On macOS 14 and older you can also **right-click (Control-click) the app → Open → Open**.
3. If macOS says the app **"is damaged and can't be opened"**, run this once in Terminal, then open the app again:
   ```sh
   xattr -dr com.apple.quarantine "/Applications/Free Exercise Book.app"
   ```
   This removes the download quarantine flag. The app is not damaged; macOS shows this message for unsigned apps downloaded from the internet.

## Linux

**Debian / Ubuntu / Mint (`.deb`)**
```sh
sudo apt install ./Free.Exercise.Book_*_amd64.deb
```

**Fedora / RHEL / openSUSE (`.rpm`)**
```sh
sudo dnf install ./Free.Exercise.Book-*.x86_64.rpm      # openSUSE: sudo zypper install ./…rpm
```

**AppImage (any distribution)**
```sh
chmod +x Free.Exercise.Book_*_amd64.AppImage
./Free.Exercise.Book_*_amd64.AppImage
```
On Ubuntu 22.04+ AppImages need FUSE 2: `sudo apt install libfuse2t64` (Ubuntu 24.04) or `sudo apt install libfuse2` (22.04).

Requires WebKitGTK 4.1 (installed automatically by the `.deb`/`.rpm`; present on most desktops for the AppImage).

## Verify your download (optional)

Compare the file's checksum with `SHA256SUMS.txt` on the release page:

| OS | Command |
|---|---|
| Windows (PowerShell) | `Get-FileHash .\file.exe -Algorithm SHA256` |
| macOS | `shasum -a 256 file.dmg` |
| Linux | `sha256sum file.deb` |

## Your data

Everything stays on your computer. Progress and settings are stored in the app's data folder:

| OS | Location |
|---|---|
| Windows | `%APPDATA%\io.github.kroy665.freeexercisebook\` |
| macOS | `~/Library/Application Support/io.github.kroy665.freeexercisebook/` |
| Linux | `~/.local/share/io.github.kroy665.freeexercisebook/` |

Uninstalling the app does not delete this folder. Delete it yourself to remove all progress.

## Problems?

[Open an issue](https://github.com/Kroy665/free_exercise_book/issues/new) with your OS version and what happened.
