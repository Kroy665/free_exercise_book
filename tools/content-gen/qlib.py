"""Question-file builder for maths topics (docs/CONTENT_STRUCTURE.md §7).

A topic script (tools/content-gen/math/<topic>.py) declares its questions with the
helpers below, listing the CORRECT option FIRST, plus a check() that recomputes the
answers with SymPy. Running the script:

    python3 tools/content-gen/math/<topic>.py

1. runs check() (aborts on any failure),
2. shuffles each question's correct option to a balanced, deterministic position,
3. writes content/subjects/math/<unit>/<topic>/questions.yaml.

Use raw strings (r"...") for LaTeX. Explanations are Markdown with worked steps.
"""
import pathlib, random, sys, yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
EXAMS = ["slst-0910", "slst-1112"]
STATEMENTS_Q = "Which of the statements given above is/are correct?"


class Topic:
    def __init__(self, topic_id: str, exams=None):
        self.id = topic_id
        _, unit, slug = topic_id.split(".")
        self.path = ROOT / "content/subjects/math" / unit / slug / "questions.yaml"
        self.exams = exams or EXAMS
        self.qs = []

    def single(self, d, refs, stem, opts, expl):
        assert len(opts) == 4 and len(set(opts)) == 4, stem
        self.qs.append(dict(type="single", difficulty=d, refs=refs, stem=stem, opts=opts, expl=expl))

    def statements(self, d, refs, stem, statements, opts, expl, question=STATEMENTS_Q):
        assert len(opts) == 4 and len(set(opts)) == 4, stem
        self.qs.append(dict(type="statements", difficulty=d, refs=refs, stem=stem, statements=statements,
                            question=question, opts=opts, expl=expl))

    def match(self, d, refs, stem, left, right, opts, expl):
        assert len(opts) == 4 and len(set(opts)) == 4, stem
        self.qs.append(dict(type="match", difficulty=d, refs=refs, stem=stem, left=left, right=right, opts=opts, expl=expl))

    def assertion_reason(self, d, refs, assertion, reason, answer, expl):
        """answer: 0 both true and R explains A · 1 both true, R does not explain A ·
        2 A true, R false · 3 A false, R true."""
        assert answer in (0, 1, 2, 3)
        self.qs.append(dict(type="assertion-reason", difficulty=d, refs=refs, assertion=assertion,
                            reason=reason, answer=answer, expl=expl))

    def write(self, check=None):
        if check:
            check()
            print(f"{self.id}: all checks passed")
        n = sum(q["type"] != "assertion-reason" for q in self.qs)
        # Balanced key positions: as even as possible, shuffled deterministically per topic.
        pos = [i % 4 for i in range(n)]
        random.Random(self.id).shuffle(pos)
        out, k = [], 0
        for i, q in enumerate(self.qs, 1):
            o = {"id": f"q{i:04d}", "type": q["type"], "difficulty": q["difficulty"], "exams": self.exams, "refs": q["refs"]}
            if q["type"] == "assertion-reason":
                o["assertion"] = {"en": q["assertion"]}
                o["reason"] = {"en": q["reason"]}
                o["answer"] = q["answer"]
            else:
                p = pos[k]; k += 1
                opts = q["opts"][1:]
                opts.insert(p, q["opts"][0])
                o["stem"] = {"en": q["stem"]}
                for key in ("statements", "left", "right"):
                    if key in q:
                        o[key] = [{"en": s} for s in q[key]]
                if "question" in q:
                    o["question"] = {"en": q["question"]}
                o["options"] = [{"en": x} for x in opts]
                o["answer"] = p
            o["explanation"] = {"en": q["expl"]}
            o["status"] = "ai-generated"
            out.append(o)
        self.path.write_text(yaml.dump(out, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=1000))
        types = {}
        for q in self.qs:
            types[q["type"]] = types.get(q["type"], 0) + 1
        print(f"{self.id}: wrote {len(out)} questions {types} -> {self.path.relative_to(ROOT)}")


class _Dumper(yaml.SafeDumper):
    pass


def _str(d, s):
    style = "|" if "\n" in s else ("'" if any(c in s for c in "\\$:#{}[],&*!|>'\"%@`") else None)
    return d.represent_scalar("tag:yaml.org,2002:str", s, style=style)


_Dumper.add_representer(str, _str)


def eq(got, want, label=""):
    """SymPy-aware equality check used inside check()."""
    import sympy as sp
    diff = sp.simplify(sp.sympify(got) - sp.sympify(want))
    if diff != 0:
        num = complex(sp.N(diff)) if not diff.free_symbols else None
        if num is None or abs(num) > 1e-10:
            sys.exit(f"CHECK FAILED {label}: got {got}, want {want}")
