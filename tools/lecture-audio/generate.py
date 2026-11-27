#!/usr/bin/env python3
"""Make the lectures' audio ahead of time with Chatterbox (Resemble AI, MIT licence).

Every spoken text of every lecture (each step's `say` and, after a question, its `answer`)
becomes one MP3 clip: <out>/<topic-id>/<clip-id>.mp3, where clip-id is the SHA-256 of the
text with its whitespace collapsed (first 32 hex digits). The app looks clips up by that id,
so a step whose text changed later simply falls back to the built-in voice until its clip
is made again.

Needs a GPU (CUDA, or Apple silicon with plenty of memory), ffmpeg, PyYAML and
`pip install chatterbox-tts`. Clips already in <out> are skipped, so a run can be resumed,
and `--shard i/n` splits the work between GPUs (see kaggle.ipynb).

  python3 tools/lecture-audio/generate.py content dist/lecture-audio/clips [--topics id,...]
  python3 tools/lecture-audio/generate.py content OUT --list   # what would be made
"""
import argparse
import glob
import hashlib
import os
import re
import subprocess
import sys
import time

import yaml

SR = 24_000


def norm(text: str) -> str:
    return " ".join(text.split())


def clip_id(text: str) -> str:
    return hashlib.sha256(norm(text).encode()).hexdigest()[:32]


def jobs(content: str, topics: set[str] | None):
    """(topic id, clip id, text) for every spoken text, in lecture order."""
    out = []
    for f in sorted(glob.glob(os.path.join(content, "subjects", "*", "*", "*", "lecture.en.yaml"))):
        with open(os.path.join(os.path.dirname(f), "topic.yaml")) as t:
            topic = yaml.safe_load(t)["id"]
        if topics and topic not in topics:
            continue
        with open(f) as fh:
            segs = yaml.safe_load(fh)["segments"]
        seen = set()
        for s in segs:
            for text in (s.get("say"), s.get("answer")):
                if text and norm(text):
                    cid = clip_id(text)
                    if cid not in seen:
                        seen.add(cid)
                        out.append((topic, cid, norm(text)))
    return out


def pieces(text: str, limit: int = 240):
    """Sentences (long ones split at commas): Chatterbox is most reliable on short inputs.
    Yields (piece, pause after it in seconds)."""
    for sent in re.split(r"(?<=[.!?])\s+", text):
        if len(sent) <= limit:
            yield sent, 0.32
            continue
        parts, cur = [], ""
        for p in re.split(r"(?<=[,;:])\s+", sent):
            if cur and len(cur) + 1 + len(p) > limit:
                parts.append(cur)
                cur = ""
            cur = f"{cur} {p}".strip()
        if cur:
            parts.append(cur)
        for k, p in enumerate(parts):
            yield p, 0.32 if k == len(parts) - 1 else 0.16


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("content")
    ap.add_argument("out")
    ap.add_argument("--topics", help="comma-separated topic ids (default: all)")
    ap.add_argument("--shard", default="0/1", help="i/n: make every n-th clip starting at i")
    ap.add_argument("--limit", type=int, default=0, help="stop after this many clips (for a sample)")
    ap.add_argument("--max-minutes", type=float, default=0, help="stop cleanly after this long (Kaggle: 12 h limit)")
    ap.add_argument("--list", action="store_true", help="only print the clips and total length")
    ap.add_argument("--exaggeration", type=float, default=0.45, help="Chatterbox expressiveness (0.25-1)")
    ap.add_argument("--cfg", type=float, default=0.5, help="Chatterbox cfg_weight (lower: slower, calmer)")
    ap.add_argument("--tempo", type=float, default=1.0, help="speed of the clip (better: set it later with import.py --tempo)")
    ap.add_argument("--bitrate", default="96k", help="MP3 bitrate (import.py makes the 48k copies the app gets)")
    ap.add_argument("--voice", help="optional reference clip (a few seconds of a voice to imitate)")
    a = ap.parse_args()

    todo = jobs(a.content, set(a.topics.split(",")) if a.topics else None)
    i, n = map(int, a.shard.split("/"))
    todo = [j for k, j in enumerate(todo) if k % n == i]
    todo = [j for j in todo if not os.path.exists(os.path.join(a.out, j[0], j[1] + ".mp3"))]
    if a.limit:
        todo = todo[: a.limit]
    chars = sum(len(t) for _, _, t in todo)
    print(f"{len(todo)} clips to make, {chars} characters (about {chars / 15 / 60:.0f} minutes of speech)", flush=True)
    if a.list or not todo:
        return

    import numpy as np
    import torch
    from chatterbox.tts import ChatterboxTTS

    dev = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
    model = ChatterboxTTS.from_pretrained(device=dev)
    if a.voice:
        model.prepare_conditionals(a.voice, exaggeration=a.exaggeration)
    print(f"model on {dev}", flush=True)

    def say(piece: str) -> np.ndarray:
        # Chatterbox now and then mumbles, stops early or runs on; judge by length and retry.
        best = None
        for attempt in range(3):
            torch.manual_seed(1234 + attempt)
            wav = model.generate(piece, exaggeration=a.exaggeration, cfg_weight=a.cfg)
            w = wav.squeeze(0).detach().cpu().numpy().astype(np.float32)
            per_char = len(w) / SR / max(len(piece), 1)
            if 0.035 <= per_char <= 0.13:
                return w
            if best is None or abs(per_char - 0.065) < abs(len(best) / SR / len(piece) - 0.065):
                best = w
        print(f"  warning: odd length after retries: {piece[:60]!r}", flush=True)
        return best

    t0, done_chars = time.time(), 0
    for k, (topic, cid, text) in enumerate(todo, 1):
        if a.max_minutes and time.time() - t0 > a.max_minutes * 60:
            print("time budget used up; run again to continue", flush=True)
            break
        audio = []
        for piece, pause in pieces(text):
            audio.append(say(piece))
            audio.append(np.zeros(int(SR * pause), np.float32))
        pcm = np.concatenate(audio[:-1]) if len(audio) > 1 else audio[0]
        os.makedirs(os.path.join(a.out, topic), exist_ok=True)
        dst = os.path.join(a.out, topic, cid + ".mp3")
        tmp = dst + ".part.mp3"
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
             "-af", (f"atempo={a.tempo}," if a.tempo != 1 else "") + "loudnorm=I=-18:TP=-1.5:LRA=11", "-ar", str(SR), "-ac", "1",
             "-c:a", "libmp3lame", "-b:a", a.bitrate, tmp],
            input=pcm.tobytes(), check=True,
        )
        os.replace(tmp, dst)
        done_chars += len(text)
        el = time.time() - t0
        left = el / done_chars * (chars - done_chars)
        print(f"[{k}/{len(todo)}] {topic} {cid[:8]} {len(pcm) / SR:.0f}s audio; "
              f"{el / 60:.0f} min so far, about {left / 60:.0f} min left", flush=True)


if __name__ == "__main__":
    sys.exit(main())
