# Brief for writing a topic lecture

The app has a **Lecture** mode for every topic. A teacher's voice (Kokoro text-to-speech) explains the topic step by step. The notes on screen are the blackboard: for each step, the app highlights and scrolls to the part being explained. Some steps put a practice question beside the notes, wait for the student to answer, then speak the explanation.

You write `content/subjects/math/<unit>/<slug>/lecture.en.yaml` for the topics you are given. Create **only** those files: no other edits and no git commands.

## Read first
1. **The reference lecture, which sets the style and depth to match:**
   - `content/subjects/math/analysis/mean-value-theorems/lecture.en.yaml`
   - compare it with that topic's `notes.en.md` and `questions.yaml`
2. Your topic's `notes.en.md` and `questions.yaml`.

## Audience
- **Who:** an M.Sc. in mathematics returning after six years, preparing for the WBSSC SLST maths exam.
- **Depth:** speak to them as a good senior teacher would. Recall the definitions they have half-forgotten, explain *why* things are true, point out traps and shortcuts, and connect ideas.
- **No padding:** never talk down to them, and leave out filler.

## Format

```yaml
segments:
  - section: rolle                # anchor of a ## section in notes.en.md
    focus: 'exact text copied from that section'   # optional: what to highlight
    say: >
      What the teacher says, in plain spoken English.
  - section: rolle
    question: q0002               # a question id from questions.yaml
    say: >
      Introduce the question: "Try this one. Find c for ..."
    answer: >
      Spoken worked answer, said after the student answers.
```

### Field rules
- **`section`:** must be an anchor that exists in `notes.en.md`.
  - Teach the sections in the order the notes give them, and cover **every** section.
  - Cover `exam-tips` last, as a short recap.
- **`focus`:** must be an **exact substring** of that section's Markdown, copied character for character, LaTeX and `**` included.
  - Choose a distinctive sentence, formula line, list item or table row, ideally the key line for that step. The app highlights the block that contains it.
  - Use **single-quoted YAML** for `focus`: backslashes stay literal, and a `'` is written as `''`.
  - Leave `focus` out for an introduction step: the section heading is highlighted instead.
- **`say` and `answer`:** spoken text only.
  - **Forbidden characters:** `$ \ ^ _ { } | * #` and backticks. The validator rejects them.
  - **Avoid** `=`, `+`, `<`, `>` and `/` too: the voice reads symbols badly.
  - **Maths in words:**

    | Write | Not |
    |:---|:---|
    | "x squared", "e to the minus x", "x to the power two thirds" | powers as symbols |
    | "a over b", "one third", "nine by four" | fractions as symbols |
    | "the square root of x", "f dash of c", "the n-th derivative" | roots and derivatives as symbols |
    | "the integral from zero to one of x squared d x" | integral signs |
    | "the sum from n equals one to infinity of" | sigma notation |
    | "the limit as x tends to zero of" | limit notation |
    | "the modulus of z", "the determinant of A", "A inverse", "alpha", "lambda" | symbols and Greek letters |
    | "the closed interval from a to b", "the open interval" | brackets |
    | "minus one", "is less than or equal to", "is congruent to five mod seven" | operator symbols |

  - Digits are fine for plain numbers ("225", "30 percent"). Spell out small numbers when it reads better.
  - Write sentences of moderate length that sound natural aloud. Use "look at the highlighted line", "on the board" and "notice" to tie the speech to the highlight.
- **`question` and `answer`:**
  - Use 4–6 questions per lecture, spread through it, each placed right after the idea it tests. Mostly `single` questions; one `statements` or `match` is fine.
  - The `answer` must match the key. The correct option is `options[answer]`, with **0-based** `answer`, in `questions.yaml`; read the `explanation` too.
  - In the answer, say the correct result and the one-line reason, and name the tempting wrong option when there is one.
  - **Avoid assertion-reason questions:** the spoken answer needs their four-way key, which is easy to get wrong.

## Size and shape
- **Size:** 25–40 steps and about 1,800–2,800 words, which is a 12–18 minute lecture.
- **Steps:** each one is 40–110 words, so one step is one idea.
- **Opening step (no focus):** what the topic is and what the student will be able to do after it.
- **Main steps:** follow the notes' order.
  - For every key definition and theorem, say what it says, why it holds (the proof idea in one or two sentences, when it is examinable), and how it is used.
  - For worked examples, talk through the method; you don't need to recite every number.
  - Spend extra time on the `:::caution` traps and the `:::exam-tip` shortcuts.
  - Skim routine tables: say what they contain and the one or two rows worth memorising.
- **Closing step:** on `exam-tips`, a crisp recap ending with "now try the practice questions".

## Accuracy
- Say only what the notes and standard textbooks support, with exact hypotheses: closed vs open intervals, strict vs non-strict inequalities, and so on.
- If the notes state a convention, use the same one.
- Every number you say must match the notes or the question key. Recompute anything you derive aloud. You may use SymPy in a scratch script to check, but do not save it in the repo.

## Validate
```
python3 -I tools/content-check/validate.py content
```
- **Your topic's line** must end with `lecture: N steps, W words`.
- **ERR/WARN lines:** fix every ERR or WARN that names your lecture file, such as a focus text not found, forbidden characters, an unknown question, or uncovered sections.
- **Other topics:** ignore lines about them.

## Report back (short)
For each topic, give its steps, words and questions used, plus anything you were unsure about.

## After the lectures are written (maintainer)
Raise `version` in each topic's `topic.yaml` (for example 0.1.0 to 0.2.0) when it gains or changes a lecture. Installed apps download a topic again only when its version goes up.
