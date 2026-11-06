# Interim content validator (until tools/packer exists).
# Usage: pip install pyyaml jsonschema && python3 tools/content-check/validate.py content

import sys, json, re, pathlib, collections, yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
import unicodedata
REQUIRED_LANGS = ["en", "bn"]
def walk(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items(): yield from walk(v, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from walk(v, f"{path}[{i}]")
    elif isinstance(o, str): yield path, o
root = pathlib.Path(sys.argv[1])
schemas = {p.name: json.loads(p.read_text()) for p in (root/"schema").glob("*.json")}
reg = Registry().with_resources([(n, Resource.from_contents(s)) for n, s in schemas.items()])
def check(schema, path):
    data = yaml.safe_load(path.read_text())
    errs = list(Draft202012Validator(schemas[schema], registry=reg).iter_errors(data))
    for e in errs: print(f"ERR {path}: {list(e.path)} {e.message[:150]}")
    return data, not errs
ok = True
for p in root.glob("subjects/*/subject.yaml"): ok &= check("subject.schema.json", p)[1]
for p in root.glob("subjects/*/*/unit.yaml"): ok &= check("subject.schema.json", p)[1]
for p in root.glob("exams/*.yaml"): ok &= check("exam.schema.json", p)[1]
for t in root.glob("subjects/*/*/*/topic.yaml"):
    ok &= check("topic.schema.json", t)[1]
    qs, good = check("question.schema.json", t.parent/"questions.yaml"); ok &= good
    anchors = None
    for lang in REQUIRED_LANGS:
        note = t.parent/f"notes.{lang}.md"
        if not note.exists(): print(f"ERR missing {note}"); ok = False; continue
        text = note.read_text()
        if unicodedata.normalize("NFC", text) != text: print(f"ERR {note} is not NFC-normalised"); ok = False
        a = re.findall(r"\{#([a-z0-9-]+)\}", text)
        if anchors is None: anchors = a
        elif a != anchors: print(f"ERR {note} anchors {a} != en anchors {anchors}"); ok = False
    anchors = set(anchors or [])
    ids = [q["id"] for q in qs]
    if len(ids) != len(set(ids)): print("ERR duplicate ids"); ok = False
    for q in qs:
        for r in q["refs"]:
            if r not in anchors: print(f"ERR {q['id']} bad ref {r}"); ok = False
    for q in qs:
        for path, val in walk(q):
            if path.endswith(".bn"):
                if re.search(r"[0-9]", val): print(f"ERR {q['id']} {path}: ASCII digits in Bengali text (use ০-৯)"); ok = False
                if unicodedata.normalize("NFC", val) != val: print(f"ERR {q['id']} {path}: not NFC"); ok = False
    dist = collections.Counter(q["answer"] for q in qs if q["type"] != "assertion-reason")
    print(t.parent.name, "questions:", len(qs), "answer spread:", dict(sorted(dist.items())), "anchors:", sorted(anchors))
print("VALID" if ok else "INVALID")
