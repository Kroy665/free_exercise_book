#!/usr/bin/env python3
"""Bring clips made on Kaggle (or another machine) into dist/lecture-audio/clips.

  python3 tools/lecture-audio/import.py ~/Downloads/output.zip   # or an unpacked folder

Copies every <topic>/<clip-id>.mp3 whose text is still in the lecture, then reports how
much of each lecture has audio. tools/publish-packs.sh packs whatever is there.
"""
import os
import shutil
import sys
import tempfile
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate import jobs  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEST = os.path.join(ROOT, "dist", "lecture-audio", "clips")


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    tmp = None
    if src.endswith(".zip"):
        tmp = tempfile.mkdtemp()
        with zipfile.ZipFile(src) as z:
            for name in z.namelist():
                if name.endswith(".mp3") and ".." not in name and not name.startswith("/"):
                    z.extract(name, tmp)
        src = tmp
    found = {}
    for d, _, files in os.walk(src):
        for f in files:
            if f.endswith(".mp3") and not f.endswith(".part.mp3"):
                found[(os.path.basename(d), f[:-4])] = os.path.join(d, f)
    wanted = jobs(os.path.join(ROOT, "content"), None)
    per_topic, copied = {}, 0
    for topic, cid, _ in wanted:
        have = per_topic.setdefault(topic, [0, 0])
        have[1] += 1
        dst = os.path.join(DEST, topic, cid + ".mp3")
        if (topic, cid) in found:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(found[(topic, cid)], dst)
            copied += 1
        if os.path.exists(dst):
            have[0] += 1
    if tmp:
        shutil.rmtree(tmp)
    for topic, (h, n) in per_topic.items():
        print(f"  {topic:<42} {h:>3}/{n:<3}{'' if h == n else '  incomplete'}")
    done = sum(h for h, _ in per_topic.values())
    print(f"imported {copied} clips; {done} of {len(wanted)} lecture clips now in {DEST}")


if __name__ == "__main__":
    main()
