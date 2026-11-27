# Lecture audio, made ahead of time

The lectures are fixed scripts, so their audio is made once, on a GPU, with the open
[Chatterbox](https://github.com/resemble-ai/chatterbox) voice model (MIT licence), and
published with the content packs. The app downloads a topic's audio when the topic is opened
(about 4–5 MB) and plays it; steps without a clip use the built-in Kokoro voice.

All 42 lectures are about 10 hours of speech (1,670 clips). Chatterbox needs a real GPU: it
is far too slow on an 8 GB Mac, so use Kaggle's free GPUs (30 hours a week; needs a verified phone number) or Google Colab's free T4.

## 1. Make the clips on Kaggle

1. kaggle.com → **Create → New Notebook → File → Import Notebook** → `kaggle.ipynb` (this folder).
2. Right-hand panel: **Accelerator: GPU T4 x2**, **Internet: on** (needs a phone-verified account).
3. Run all with `SAMPLE = True` (a few minutes) and listen to the clips at the end. Adjust
   `EXAGGERATION` / `CFG` if wanted.
4. Set `SAMPLE = False`, then **Save Version → Save & Run All (Commit)**. It runs in the
   background (about 10 hours or less on two T4s) and stops cleanly before Kaggle's 12-hour limit.
5. If not everything was made: **Add Input → Your Work →** this notebook's output, and commit
   again. Finished clips are skipped.

The notebook clones this repository, so the lecture texts it reads are those on `main`.

### Or on Google Colab (no phone verification)

colab.research.google.com → **File → Upload notebook** → `kaggle.ipynb`, then **Runtime →
Change runtime type → T4 GPU**, and run all. Clips are saved to Google Drive
(`MyDrive/lecture-audio/clips`); a free session lasts a few hours, so run again until all are
made (finished clips are skipped). Download that Drive folder for step 2.

## 2. Import and publish

```sh
# Download the notebook's output (Output → Download), then:
python3 tools/lecture-audio/import.py ~/Downloads/output.zip
tools/publish-packs.sh        # packs and signs audio/ along with the content packs
```

`import.py` keeps only clips whose text is still in the lectures and reports what is missing.
The clips live in `dist/lecture-audio/clips/` (not in git); keep a copy of the Kaggle output.

## How clips are matched

A clip's id is the SHA-256 of its text with whitespace collapsed (first 32 hex digits), one
clip per step `say` and per `answer`. When a lecture text is edited, its old clip no longer
matches; the app speaks that step with Kokoro until the clip is made again:

```sh
python3 tools/lecture-audio/generate.py content dist/lecture-audio/clips --list   # what is missing
```

On the server: `audio/manifest.json` (signed with the pack key) lists one
`<topic>@<hash>.audio` file per topic: `FEBAUD1\n`, a u32 index length, a JSON index
`{clip id: [offset, length]}`, then the MP3 clips (24 kHz mono, 48 kbit/s). See
`crates/packs/src/audio.rs`.
