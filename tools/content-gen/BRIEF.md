# Brief for writing one maths topic

You are writing **one topic** of the Free Exercise Book maths course for the **WBSSC SLST (Assistant Teacher) Mathematics** exam. It covers both Class IX–X (graduation-level syllabus) and Class XI–XII (post-graduation-level syllabus). The reader holds an M.Sc. in mathematics, but has had about 6 years away from it and studies 1–2 hours a day. Write **compact revision at PG depth**, not a beginner course. English only.

## Read first
1. `docs/syllabus/wbssc-slst-mathematics.md`: the official syllabus. Cover everything it lists for your topic, at both levels.
2. `docs/SYLLABUS.md`: your topic's row ("Covers") and the neighbouring topics. Do not cover what belongs to another topic; mention it in one line at most.
3. **The reference topic.** Match its style, depth and structure:
   - `content/subjects/math/algebra/complex-numbers/` (`topic.yaml`, `notes.en.md`, `questions.yaml`)
4. `docs/CONTENT_STRUCTURE.md` §5–§7, especially **§6.1** (maths, tables, ```plot / ```chart blocks).
5. `tools/content-gen/qlib.py`: the question builder you must use.

## Files you create (only these)
- `content/subjects/math/<unit>/<slug>/topic.yaml`:
  - copy the shape of the reference
  - `id` = your topic id; `order` = position within its unit (given in your task)
  - `exams: [slst-0910, slst-1112]`
  - `version: 0.1.0`, `status: ai-generated`, `prerequisites` (earlier topic ids if relevant)
  - `estimated_minutes`: 45–75
  - `sources`: 3–4 standard texts by author and title, plus the WBSSC syllabus item; no URLs
  - `retired: []`
- `content/subjects/math/<unit>/<slug>/notes.en.md`:
  - `#` title, then **6–8 `##` sections**, each with an explicit anchor `{#kebab-case}`; each section 150–600 words
  - definitions, theorem statements (with hypotheses exactly right), standard results and formulas, **solved examples**, `:::exam-tip` and `:::caution` blocks for shortcuts and traps
  - proof ideas only where the idea itself is examinable
  - use a table where it helps
  - use a ```plot or ```chart only where a picture genuinely helps; most algebra topics need none or one
  - last section: `## Quick checks and traps {#exam-tips}`
- `tools/content-gen/math/<slug>.py`: the question script (see below). Run it to produce `questions.yaml`.

**Do not touch** any other file: no `unit.yaml`, `subject.yaml`, `docs/` or other topics, and **no git commands**. Other agents are writing other topics in parallel.

## Questions: exactly 30, through `tools/content-gen/qlib.py`
Pattern (see the module docstring):

```python
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from qlib import Topic, eq
T = Topic("math.<unit>.<slug>")
T.single(2, ["anchor"], r"stem with $LaTeX$", [r"correct", r"wrong", r"wrong", r"wrong"], r"""worked solution""")
...
def check():
    import sympy as sp
    eq(<sympy computation>, <the key you put first>, "q3")   # one per computable question
    ...
T.write(check)
```

- **Mix:**
  - about 20–22 `single`
  - 2–3 `statements` (3 numbered statements; options like "1 and 2 only")
  - 2 `match` (4×4, options as "A-3, B-2, C-4, D-1")
  - 4–5 `assertion_reason`, using a mix of answers 0, 1, 2 and 3
- **Difficulty:** about 8 easy (1), 14 medium (2), 8 hard (3). The questions should look like a real SLST paper: mostly short computations and standard-result recall, which a prepared candidate solves in about 1 minute.
- The **correct option comes first** in your list. qlib moves it to a balanced position.
- **Exactly one option is correct.** Distractors should be the results of plausible mistakes: sign slips, a wrong formula, off-by-one errors, a principal-value slip, swapped conditions. Never write a distractor that is also true.
- **Every explanation is a worked solution:** the steps, the result, and a short reason the tempting distractor is wrong. Use display maths `$$…$$` for key lines. Add a fast "check" trick where one exists.
- `refs` = anchors from your notes that teach the fact.
- **Use raw strings for all LaTeX.**
- In option and stem text, `$...$` must have no space just inside the dollars.
- In table cells use `\lvert x\rvert`, not `|x|`.

### Verification is mandatory
- `check()` must recompute with SymPy **every question whose key can be computed**: numbers, expressions, roots, determinants, counts, matched pairs.
- For conceptual questions (statements, assertion-reason, definitions), also prove or disprove each statement in `check()` with a concrete SymPy example or counterexample where possible. Then reread each one against the standard theorem statement.
- If a check fails, **fix the question**. Never fix the check to fit.

## Validate before you finish
```
python3 tools/content-gen/math/<slug>.py
python3 -I tools/content-check/validate.py content
```
- The validator checks schemas and anchors, renders every formula and graph, and catches LaTeX in double-quoted YAML.
- Fix **every ERR line that mentions your topic folder**. Ignore errors in other topic folders: those belong to agents still working.
- Your topic's line must show 30 questions and an answer spread close to even.

## Accuracy rules
- **Only standard, textbook-verifiable mathematics.** Theorem statements must have the right hypotheses (continuity on a closed interval, monic polynomials, field vs ring, and so on).
- Where books differ in convention, state the convention and keep questions convention-safe. Examples: whether a principal argument range is $(-\pi,\pi]$; whether log means ln; whether "rank" is defined via minors.
- No copied textbook text; write your own explanations and examples.

## Report back (short)
Give the topic id, section anchors, the question type and difficulty counts, the number of SymPy checks, and the validator result for your topic. List anything you were unsure about.
