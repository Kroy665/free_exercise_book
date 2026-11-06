# Content Structure

How study content is organised, identified and formatted in `content/`. Editorial rules (accuracy, style, sources) are in [CONTENT_GUIDELINES.md](CONTENT_GUIDELINES.md).

## 1. Principles

- **Human-editable source.** Content is written in **Markdown** (notes) and **YAML** (metadata, questions). Contributors never touch SQLite or JSON.
- **Validated by schema.** YAML files are validated in CI against JSON Schemas in `content/schema/`.
- **Stable IDs.** Every subject, unit, topic, note section and question has a permanent ID. IDs are never reused or renamed. Deprecate instead.
- **One topic = one folder.** It holds notes and questions together, so reviewers see both.
- **Bilingual by design.** Launch languages are **English (`en`) and Bengali (`bn`)**. Notes have one file per language (`notes.en.md`, `notes.bn.md`) with **identical section anchors**. Questions keep all languages in one file, so translations cannot drift apart. CI fails if a topic is not complete in both `en` and `bn`. Other languages (`hi`, …) are optional extras.

## 2. Hierarchy

```
Subject   (history)               e.g. History, Polity, Geography, Economy, Science, Art & Culture,
  └── Unit (modern)                    Environment, Current Affairs, Reasoning*, Quant*, English*
        └── Topic (revolt-of-1857)     ← the unit of download, study and practice
              ├── Notes (sections)     ← the unit of reading and embedding
              └── Questions
```
\* Aptitude subjects come later. They need a different question generator (numeric, worked solutions).

**Topic size guideline:** one topic = 20–60 minutes of reading and **30–150 questions**. Split bigger topics.

## 3. Folder layout

```
content/
├── LICENSE.md                         # CC BY-SA 4.0
├── schema/
│   ├── subject.schema.json
│   ├── topic.schema.json
│   ├── question.schema.json
│   └── exam.schema.json
├── exams/
│   ├── upsc-cse-prelims.yaml          # exam patterns for mock tests
│   └── ssc-cgl-tier1.yaml
└── subjects/
    └── history/
        ├── subject.yaml
        └── modern/
            ├── unit.yaml
            └── revolt-of-1857/
                ├── topic.yaml
                ├── notes.en.md
                ├── notes.bn.md        # required (launch language)
                ├── notes.hi.md        # optional, later
                ├── questions.yaml
                └── assets/            # images (WebP/SVG, ≤ 200 KB each)
```

Current affairs live under `content/current-affairs/2026/11/` with `items.yaml` and `questions.yaml`.

## 4. IDs

| Thing | Format | Example |
|---|---|---|
| Subject | short slug | `hist` |
| Unit | `subject.unit` | `hist.modern` |
| Topic | `subject.unit.topic` | `hist.modern.revolt-1857` |
| Note section | `topic#anchor` | `hist.modern.revolt-1857#causes` |
| Question | `topic/q####` | `hist.modern.revolt-1857/q0007` |
| CA item | `ca.yyyy-mm/i###` | `ca.2026-11/i012` |

- Lowercase ASCII slugs, `a-z0-9-`, even for Bengali content.
- Question numbers are never reused. If a question is deleted, its ID is retired. List it in `topic.yaml → retired`.

## 5. `topic.yaml`

```yaml
id: hist.modern.revolt-1857
title:
  en: The Revolt of 1857
  bn: ১৮৫৭ সালের মহাবিদ্রোহ
summary:
  en: Causes, spread, leaders, suppression, nature and consequences of the Revolt of 1857.
  bn: ১৮৫৭ সালের মহাবিদ্রোহের কারণ, বিস্তার, নেতৃবৃন্দ, দমন, প্রকৃতি ও ফলাফল।
order: 3                     # position within unit
exams: [upsc-cse, wbcs, ssc-cgl, ssc-chsl, state-psc, rrb-ntpc]
prerequisites: [hist.modern.company-expansion]
estimated_minutes: 40
version: 1.0.0               # semver; bump on any change (see §9)
status: ai-generated         # ai-generated | reviewed | verified
reviewers: []                # GitHub handles of human reviewers
sources:
  - NCERT Class 8, Our Pasts III, Ch. 5 "When People Rebel"
  - NCERT Class 12, Themes in Indian History III, Ch. "Rebels and the Raj"
  - Bipan Chandra et al., India's Struggle for Independence, Ch. 1
retired: []
```

## 6. Notes (`notes.<lang>.md`)

Plain CommonMark plus a few custom blocks. **No raw HTML.**

### Rules
- Start with an `#` H1 title. Each `##` H2 is a **section** and must have an explicit anchor: `## Causes {#causes}`.
- Sections are the unit for search, embeddings, "Revise in notes" links and bookmarks. Keep each section **150–600 words**.
- `###` H3 for sub-sections. Do not go deeper than H4.
- Anchors are stable IDs. Do not rename them; questions reference them.

### Custom blocks
```markdown
:::keyfacts
- Began: **10 May 1857**, Meerut
:::

:::exam-tip
UPSC often asks about the *nature* of the revolt. Know the historians' views.
:::

:::mnemonic
...
:::

:::caution
Common confusion: Awadh was annexed on grounds of misgovernance, **not** the Doctrine of Lapse.
:::

:::timeline
- 1856 | Annexation of Awadh
- 29 Mar 1857 | Mangal Pandey at Barrackpore
:::

:::asof 2026-11-01 source="https://pib.gov.in/..."
Time-sensitive fact here.
:::
```

Tables use GitHub-flavoured Markdown. Images: `![Alt text required](assets/map-1857.webp)`. Alt text is mandatory.

## 7. Questions (`questions.yaml`)

All languages live in one file. **`en` and `bn` are required** on every localized field. Other languages are optional, and a language is used only when its item is complete.

### Common fields
| Field | Required | Notes |
|---|---|---|
| `id` | ✓ | `q0001`… (topic prefix added by packer) |
| `type` | ✓ | `single`, `statements`, `match`, `assertion-reason`, `chronology` |
| `difficulty` | ✓ | `1` easy · `2` medium · `3` hard |
| `exams` | ✓ | Exam tags this question style suits |
| `refs` | ✓ | Note section anchors that teach this fact |
| `stem` | ✓ | `{en: ..., bn: ...}` |
| `options` | ✓ | List of 4 `{en, hi}`, unless the type defines its own |
| `answer` | ✓ | 0-based index into `options` |
| `explanation` | ✓ | Why the answer is right **and** why key distractors are wrong |
| `status` | ✓ | `ai-generated` · `reviewed` · `verified` |
| `as_of` |   | ISO date for time-sensitive facts (**required** for current affairs) |
| `source` |   | URL or citation (**required** for current affairs) |
| `pyq` |   | `{exam: upsc-cse, year: 2019}` when a question is *inspired* by a past paper (never copied) |

### Type-specific fields
- `statements`: `stem` (intro line), `statements: [{en,hi}, ...]`, `question` (e.g. "Which of the statements given above is/are correct?") plus `options` like "1 and 2 only".
- `match`: `left: [...]`, `right: [...]` plus `options` as code strings like "A-2, B-1, C-4, D-3".
- `assertion-reason`: `assertion`, `reason`. **No `stem` and no `options`.** The app supplies the standard four options: (0) both true, R explains A · (1) both true, R does not explain A · (2) A true, R false · (3) A false, R true.
- `chronology`: `stem`, `items: [...]`, `options` as orders like "2-1-3-4".

### Exam tags vs exam patterns
`exams:` on topics and questions holds **exam family tags** (`upsc-cse`, `ssc-cgl`, `ssc-chsl`, `ibps-po`, `rrb-ntpc`, `state-psc`). Files in `exams/` define **test patterns** (`upsc-cse-prelims-gs1`, `ssc-cgl-tier1`) used only by the mock-test engine.

### YAML pitfalls (CI catches these)
- **Quote any text containing a comma inside `{ }` flow maps.** Write `{ en: "1, 2 and 3" }`. Unquoted, YAML splits it into extra keys.
- Quote text that starts with a number followed by `:` or contains `: ` or `#`.
- **Quote dates:** `as_of: "2026-11-06"`. Unquoted, YAML turns them into date objects.
- Prefer block style (`en: ...` on its own line) for long or tricky text.

### Example
```yaml
- id: q0001
  type: single
  difficulty: 1
  exams: [ssc-cgl, rrb-ntpc]
  refs: [outbreak]
  stem:
    en: Where did the Revolt of 1857 begin on 10 May 1857?
    bn: ১৮৫৭ সালের ১০ মে কোথায় মহাবিদ্রোহের সূচনা হয়েছিল?
  options:
    - { en: Meerut, bn: মিরাট }
    - { en: Delhi, bn: দিল্লি }
    - { en: Kanpur, bn: কানপুর }
    - { en: Lucknow, bn: লখনউ }
  answer: 0
  explanation:
    en: Sepoys at Meerut rose on 10 May 1857 and marched to Delhi the next day.
    bn: ১৮৫৭ সালের ১০ মে মিরাটের সিপাহিরা বিদ্রোহ করে এবং পরের দিন দিল্লির দিকে রওনা হয়।
  status: ai-generated
```

The full sample is in `content/subjects/history/modern/revolt-of-1857/`.

## 8. Exam patterns (`exams/*.yaml`)

Used by the mock test engine. **Always re-check against the latest official notification** and record it in `source` and `as_of`.

```yaml
id: ssc-cgl-tier1
name: { en: SSC CGL Tier I }
duration_minutes: 60
negative_marking: 0.5        # marks deducted per wrong answer
sections:
  - { id: gi,  name: { en: General Intelligence & Reasoning }, questions: 25, marks_each: 2, subjects: [reasoning] }
  - { id: ga,  name: { en: General Awareness }, questions: 25, marks_each: 2, subjects: [hist, polity, geo, econ, sci, ca] }
  - { id: qa,  name: { en: Quantitative Aptitude }, questions: 25, marks_each: 2, subjects: [quant] }
  - { id: eng, name: { en: English Comprehension }, questions: 25, marks_each: 2, subjects: [english] }
source: SSC CGL notification (official)
as_of: "2026-11-06"
```

If an exam has sections whose subjects are not yet available, the test builder offers a **GA-only** variant.

## 9. Versioning

- Each topic has its own **semver** `version`:
  - **patch**: typo or explanation wording fix
  - **minor**: questions or sections added
  - **major**: section anchors restructured (should be rare)
- Packs carry topic versions. The app shows "Updated: 3 questions corrected" from the changelog in `CHANGELOG.md` per subject.
- Changing a question's **answer** always requires a changelog line, because the app re-grades past attempts.

## 10. Current affairs items (`items.yaml`)

```yaml
- id: i001
  date: "2026-11-03"
  category: schemes          # schemes | appointments | awards | sports | economy | science | defence |
                             # environment | international | reports-indices | polity | states | obituaries
  title: { en: ... }
  body: { en: ... }          # 40–120 words
  key_points: [ { en: ... } ]
  related_topics: [econ.schemes.social-security]
  source: https://pib.gov.in/...
  as_of: "2026-11-03"
  status: ai-generated
```
