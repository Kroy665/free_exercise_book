# Product Specification

Status: Draft v0.1 · Last updated: 2026-11-06

## 1. Vision

The best free study companion for Indian government exams. It works fully offline, runs on a low-end PC and is maintained by the community.

## 2. Goals and non-goals

**Goals**
- Topic-wise **notes** and **MCQ practice** are the core of the app.
- Work **offline**. Once a topic is downloaded, no internet is needed.
- Run well on **4 GB RAM / dual-core** machines.
- Give **accurate**, source-backed content with a visible verification status.
- Make it easy for non-programmers to contribute content.
- Support **bilingual** content: **English and Bengali (বাংলা) at launch**, then Hindi and more Indian languages.

**Non-goals (for v1)**
- User accounts, cloud servers or a backend we must run.
- Video lectures.
- Social features (leaderboards, chat).
- Paid tiers, ads or upsells, ever.

## 3. Users

| Persona | Needs |
|---|---|
| Rural aspirant, patchy internet, shared PC | Download once, small downloads, Bengali-medium content, low resource use |
| Bengali-medium WBCS / WBPSC / WBSSC aspirant | Full Bengali notes and MCQs, with English terms for key concepts |
| Working professional | Short daily sessions, spaced revision, mobile later |
| Serious UPSC aspirant | Depth, statement-type questions, full mock tests, weak-area analytics |
| Coaching centre or library | Sideload packs to many PCs from USB without internet |
| Contributor or teacher | Simple Markdown/YAML editing, clear review process |

## 4. Feature list

Priorities: **P0** = MVP, **P1** = v1.0, **P2** = later.

### 4.1 Library and notes
| ID | Feature | Pri |
|---|---|---|
| L1 | Browse Subject → Unit → Topic tree, showing which items are downloaded | P0 |
| L2 | Notes reader: Markdown, tables, timelines, callouts, images | P0 |
| L3 | Table of contents per note, with scroll position remembered | P0 |
| L4 | Bookmarks on topics and note sections | P0 |
| L5 | Content language button (English/Bengali) in the top bar; UI stays English | P0 |
| L6 | Highlights and personal notes on note text | P1 |
| L7 | "Related notes" (vector similarity) | P1 |
| L8 | Source and "as of" date shown on time-sensitive facts | P0 |
| L9 | Export a topic as a printable PDF exercise book | P2 |

### 4.2 Practice (MCQ)
| ID | Feature | Pri |
|---|---|---|
| P1 | Topic practice with instant feedback and explanation | P0 |
| P2 | Question types: single choice, statement-based, match-the-following, assertion–reason, chronology | P0 |
| P3 | Filter by difficulty, exam tag and unseen/wrong questions | P1 |
| P4 | "Revise this" links from a question to the note section it tests | P1 |
| P5 | Mistake notebook (automatic) | P0 |
| P6 | ✅ Spaced revision queue (FSRS-5; wrong answers anywhere enter the queue) | P1 |
| P7 | Daily quiz (10 questions from downloaded topics) | P1 |
| P8 | Report an error on any question | P0 |

### 4.3 Mock tests
| ID | Feature | Pri |
|---|---|---|
| T1 | Exam-pattern tests: timer, sections, negative marking, from exam definitions | P1 |
| T2 | Custom tests (topics, count, time, negative marking) | P0 |
| T3 | Question palette: answered, not answered, marked for review | P1 |
| T4 | Result with score, accuracy, time per question and topic breakdown | P1 |
| T5 | Resume an interrupted test after a crash or close | P1 |

### 4.4 Current affairs
| ID | Feature | Pri |
|---|---|---|
| C1 | Monthly packs: news items, each with category, date, source link and "as of" | P1 |
| C2 | Monthly MCQ sets | P1 |
| C3 | Current-affairs items tagged to static topics (shown inside those topics) | P2 |

### 4.5 Search
| ID | Feature | Pri |
|---|---|---|
| S1 | ✅ Keyword search across notes and questions (FTS5; Bengali-aware words, digits, substring fallback) | P0 |
| S2 | Meaning-based search (vectors), with fallback to keyword | P1 |
| S3 | ✅ Command palette (Ctrl/Cmd+K) with search and quick actions | P1 |

### 4.6 Progress
| ID | Feature | Pri |
|---|---|---|
| A1 | ✅ Accuracy and attempt counts per topic | P0 |
| A2 | ✅ Weak topics and an activity heatmap | P1 |
| A3 | ✅ Streaks and a daily goal | P1 |
| A4 | Export/import of progress (single file) | P1 |

### 4.7 Downloads and updates
| ID | Feature | Pri |
|---|---|---|
| D1 | Pick exams and topics, download packs, show sizes | P0 |
| D2 | Signature and hash verification of every pack | P0 |
| D3 | Update notices for packs; delta updates | P1 |
| D4 | Sideload `.pack` files from disk or USB | P1 |
| D5 | Optional download of the embedding model for meaning-based search | P1 |
| D6 | App self-update (Tauri updater, signed) | P1 |

### 4.8 Settings
Language, theme (system/light/dark), font size, reading width, daily goal, network (allow/deny, mirror choice), data folder location, export/reset data.

### 4.9 Later (P2+)
- Offline AI tutor ("explain this answer") via a small local model (llama.cpp). Opt-in, separate download.
- Mobile app sharing `crates/core` (Tauri mobile).
- More languages: Hindi (next), then Marathi, Tamil, Telugu, Gujarati, Kannada, Malayalam, Odia, Punjabi, Assamese.
- Peer-to-peer pack sharing on a local network.

## 5. Non-functional requirements

| Area | Target |
|---|---|
| Installer size | ≤ 15 MB (without the embedding model) |
| Cold start | ≤ 2 s on a 4 GB RAM / HDD machine |
| Memory | ≤ 250 MB during normal use |
| Search latency | Keyword ≤ 50 ms; vector ≤ 300 ms for 100k items |
| Pack size | A typical topic pack is ≤ 2 MB (compressed) |
| Min OS | Windows 10, macOS 11, Ubuntu 22.04 (or equivalent with WebKitGTK 4.1) |
| Min window | 960 × 600 |
| Accessibility | WCAG 2.2 AA |
| Privacy | Zero telemetry by default. See [PRIVACY_AND_SECURITY.md](PRIVACY_AND_SECURITY.md) |

## 6. Roadmap

| Version | Scope |
|---|---|
| **v0.1** | Shell, onboarding, sample content **in English and Bengali** (content language switch; English UI), library, notes reader, topic practice, keyword search, mistake notebook, error reporting |
| **v0.2** | ✅ Content packs: Downloads page, signed packs, bundled/offline install, updates, folder import. ✅ Mock tests: custom and exam-pattern tests (scaled to installed content), timer, palette, mark for review, resume, negative marking, results by section/topic, review. ✅ Spaced repetition (FSRS-5) and Progress page (goal, streaks, heatmap, weak topics, test trend). |
| **v0.3** | Vector search, related notes/questions, FSRS revision, monthly current-affairs packs |
| **v0.4** | Hindi content, WBCS exam pattern, delta updates, sideloading, app auto-update |
| **v1.0** | Stable pack format, broad syllabus coverage, accessibility audit, signed installers |

## 7. Open questions
- Code signing: Windows via SignPath Foundation (free for OSS); macOS needs an Apple Developer account ($99/yr). Funding source?
- Primary hosting for packs: GitHub Releases plus which mirror?
- Final product name.
