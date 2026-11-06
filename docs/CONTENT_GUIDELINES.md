# Content Guidelines

Editorial rules for notes, questions and current affairs. **Accuracy is the product.** One wrong answer key costs more trust than ten missing topics.

## 1. Accuracy and verification

### Status levels (shown to users)
| Status | Meaning | Who sets it |
|---|---|---|
| `ai-generated` | Drafted by AI, passed automated checks, **not yet human-reviewed** | Generator |
| `reviewed` | One human checked every fact against a listed source | Reviewer |
| `verified` | Two independent humans reviewed, or one subject expert | Maintainer |

The topic page and each question show a small status tag. Library cards do **not** show it (product decision, keeps the library clean).

### Mandatory checks before merge
1. Every fact in a question's **answer and explanation** appears in the topic's notes or a listed source.
2. Dates, numbers, article/schedule numbers, names and spellings are checked against a **standard source** (see §4).
3. Exactly **one** option is correct (for `single`). No "trick" ambiguity.
4. Distractors are plausible but **unambiguously wrong**.
5. Time-sensitive facts carry `as_of` (and `source` for current affairs).
6. CI passes: schema, duplicate detection, anchor references, language completeness.

### AI-generated content workflow
1. **Generate** notes from the syllabus outline, citing sources.
2. **Generate** questions only from the notes (not from the model's general memory).
3. **Verify** with a second, independent pass that re-checks each claim and flags uncertain ones.
4. Flagged items are fixed or removed. **Never ship a fact marked uncertain.**
5. Open a PR with `status: ai-generated` and a checklist for human reviewers.

## 2. Writing notes

- **Exam-oriented and concise.** Prefer bullets, tables and timelines over long paragraphs.
- Each section opens with 1–2 lines of context, then the facts.
- Put **high-frequency exam facts** in `:::keyfacts`.
- Use `:::caution` for commonly confused facts (these make great distractors too).
- Give both views on contested historical interpretations and attribute them ("According to R.C. Majumdar…").
- Neutral, factual tone. No political opinion, no glorification or vilification of communities, parties or individuals.
- Spell names consistently with **NCERT** usage. Mention the common alternative once if needed (e.g. "Tantia (Tatya) Tope").
- Dates: `10 May 1857`. Centuries: "19th century". Numbers: Indian system in prose (₹1.5 lakh crore).

## 3. Writing MCQs

**Good stems**
- Test one fact or concept.
- Are complete questions. The user should be able to answer without reading the options.
- Use positive phrasing. If you must use NOT/INCORRECT, write it in **bold caps**: "Which of the following is **NOT** correct?"

**Good options**
- Four options, similar length and grammar.
- No "All of the above" in `single` type (use the `statements` type instead).
- Avoid "None of the above" unless it reflects real exam style for that exam tag.
- Shuffle positions. Across a topic, correct answers should spread evenly over A–D (CI warns if any letter is > 35%).

**Explanations**
- 1–4 sentences. State why the correct answer is correct.
- Add one line about the most tempting wrong option.
- Link to the note section via `refs`.

**Mix per topic (target)**
| Difficulty | Share | Type mix |
|---|---|---|
| Easy (1) | 30% | mostly `single` |
| Medium (2) | 45% | `single`, `match`, `chronology` |
| Hard (3) | 25% | `statements`, `assertion-reason` (UPSC style) |

## 4. Sources

**Preferred (in order)**
1. Official: Constitution of India, Gazette, PIB, ministry and department sites, RBI, NITI Aayog, Census, Economic Survey, Union Budget, India Year Book.
2. NCERT textbooks (old and new).
3. Standard references: Laxmikanth (Polity), Bipan Chandra / Spectrum (Modern History), R.S. Sharma / Satish Chandra (Ancient/Medieval), G.C. Leong / Majid Husain (Geography), Ramesh Singh (Economy).
4. Reputed newspapers (The Hindu, Indian Express) for current affairs, cross-checked with an official source.

**Not acceptable as sole source:** Wikipedia, blogs, coaching notes, social media, YouTube, AI output.

Cite as a short text reference in `topic.yaml → sources`, or a URL for current affairs.

## 5. Copyright and originality

- **Write everything in your own words.** Never copy text, tables, diagrams or questions from books, coaching material or websites.
- Facts are not copyrightable; expression is. Restructure and rewrite.
- **Past exam questions (PYQs):** You may write *original* questions on the same fact and tag them `pyq: {exam, year}`. Do not reproduce the original wording.
- Images: create your own (SVG preferred) or use public-domain / CC-licensed images with attribution in `assets/ATTRIBUTION.md`.
- By contributing, you agree to license content under **CC BY-SA 4.0**.

## 6. Current affairs rules

- Every item needs an **official or reputed source URL** and `as_of`.
- **Only include facts an official source states and other sources don't contradict.** Leave out details that sources disagree on (and note them in a YAML comment) until a reviewer confirms them. AI search summaries are leads, not sources.
- Cover facts likely to be asked: what, who, where, when, which ministry, key numbers. Skip opinion and speculation.
- Neutral wording, especially for political, judicial and international events.
- Link each item to static topics through `related_topics` when relevant.
- Monthly packs are frozen after the month closes plus 15 days. Later corrections are patch releases.
- Facts that go stale ("current Chief Justice of India") must be phrased with a date: "as of November 2026".

## 7. Translation guidelines

**Launch languages: English (`en`) and Bengali (`bn`).** Every topic must be complete in both before release. Hindi (`hi`) and other languages follow the same rules.

### General rules (all languages)
- Translate meaning, not word by word. Notes and questions must say **exactly the same facts** in every language: same dates, same numbers, same answer.
- A question's translation is complete only when the stem, all options, statements/lists and the explanation are translated. **Partial translations are never shown**; the app falls back to English for that item.
- Do not translate IDs, section anchors (`{#causes}`), scheme acronyms or Article numbers' meaning. Translate only the surrounding words.
- Translator PRs need review by a second fluent speaker.

### Bengali (বাংলা) style guide
| Rule | Example |
|---|---|
| Write in standard colloquial Bengali (**চলিত ভাষা**), never the literary style (সাধু ভাষা) | হয়েছিল, not হইয়াছিল |
| Spelling follows the **Paschimbanga Bangla Akademi** rules | সরকারি, জানুয়ারি, শ্রেণি |
| Terminology follows **WBBSE/WBCHSE textbooks** and the WBCS exam's Bengali papers | স্বত্ববিলোপ নীতি, অধীনতামূলক মিত্রতা, ভারত শাসন আইন |
| On first use in a note section, put the **English term in brackets** after key administrative, constitutional and technical terms | ভারত-সচিব (Secretary of State for India) |
| **Bengali digits** (০–৯) in all Bengali prose, dates, statement numbers and option codes | ১০ মে ১৮৫৭; "কেবল ১ ও ২"; "ক-৩, খ-১" |
| List labels for match questions: **ক, খ, গ, ঘ** (List I) and **১, ২, ৩, ৪** (List II) | ক. লখনউ … ১. কুনওয়ার সিং |
| Proper nouns use the spelling common in West Bengal textbooks | মিরাট, লখনউ, ঝাঁসি, রানি লক্ষ্মীবাঈ, তাঁতিয়া টোপি, মঙ্গল পাণ্ডে |
| Notes use neutral, impersonal sentences; exam tips address the reader as **আপনি** | মনে রাখুন… |
| End sentences with the দাঁড়ি (।) | |
| Book and document titles: give the original English title, transliterated, then a Bengali gloss if helpful | "দ্য ইন্ডিয়ান ওয়ার অব ইন্ডিপেনডেন্স" |
| When a person is better known by a full name in Bengali, use it | R.C. Majumdar → রমেশচন্দ্র মজুমদার |

Standard question phrases (use these exactly, for consistency):

| English | Bengali |
|---|---|
| Consider the following statements | নিম্নলিখিত বিবৃতিগুলি বিবেচনা করুন। |
| Which of the statements given above is/are correct? | উপরের কোন বিবৃতিটি/বিবৃতিগুলি সঠিক? |
| Match List I with List II | তালিকা I-এর সঙ্গে তালিকা II মেলান। |
| Arrange in chronological order | কালানুক্রমিকভাবে সাজান। |
| 1 and 2 only | কেবল ১ ও ২ |
| 1, 2 and 3 | ১, ২ ও ৩ |
| Which one of the following is **NOT** … | নিম্নলিখিত কোনটি … **নয়**? |
| Assertion (A) / Reason (R) | বিবৃতি (A) / কারণ (R) |

### Hindi (हिन्दी), later
- Use standard exam terminology from **Hindi-medium NCERT** and official CSTT glossaries.
- Proper nouns use the standard Hindi spelling (मंगल पांडे, लॉर्ड कैनिंग).

## 8. Sensitive topics

For religion, caste, communal history, border disputes, maps and ongoing court cases:
- Follow the official Government of India position and terminology for maps and boundaries (Survey of India).
- Use neutral, factual phrasing. Attribute claims.
- Maintainers have final say on wording. Escalate disagreements in an issue, not in content.

## 9. Error reports

- In-app "Report error" opens a GitHub issue template prefilled with the question ID, version and the user's note.
- **Triage SLA:** confirmed answer-key errors get a patch release within 7 days.
- When an answer key changes, the app re-grades affected past attempts and tells the user.
