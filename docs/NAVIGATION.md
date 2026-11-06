# Navigation Guidelines

## 1. Information architecture

```
App
├── Home                    Today: continue, daily quiz, revision due, goal
├── Library                 Subjects → Units → Topics
│   └── Topic               Tabs: Notes · Practice · Related
├── Practice                Quick practice, by topic, by exam, daily quiz
├── Tests                   Exam-pattern mocks, custom tests, history
│   └── Test session        Full-screen exam view (sidebar hidden)
│       └── Result → Review
├── Revise                  Due today (SRS) · Mistakes · Bookmarks
├── Current Affairs         Month list → Month → Items / Quiz
├── Progress                Overview, by subject/topic, test history
├── Downloads               Installed, available, updates, sideload
└── Settings                General, reading, study, data, network, about
```

Search (⌘K / Ctrl+K) is global and opens as an overlay, not a page.

## 2. Sidebar

Order (top to bottom): **Home, Library, Practice, Tests, Revise, Current Affairs, Progress**. At the bottom: **Downloads, Settings**.

- Show a badge on **Revise** with the number of cards due, capped at "99+".
- Show a dot on **Downloads** when updates are available.
- Mark the active item with an accent bar and `aria-current="page"`.

## 3. Routes

| Route | Screen |
|---|---|
| `/` | Home |
| `/onboarding` | First-run flow (steps as query `?step=`) |
| `/library` | Subjects grid |
| `/library/[subject]` | Units and topics of a subject |
| `/topic/[topicId]` | Topic, Notes tab (default) |
| `/topic/[topicId]/practice` | Topic practice session |
| `/topic/[topicId]/related` | Related notes and questions |
| `/practice` | Practice hub |
| `/practice/session/[sessionId]` | Running practice session (any source) |
| `/tests` | Tests hub |
| `/tests/new` | Custom test builder |
| `/tests/[testId]/instructions` | Instructions screen |
| `/tests/[testId]/run` | Exam view |
| `/tests/[testId]/result` | Result summary |
| `/tests/[testId]/review` | Question-by-question review |
| `/revise` | Due / Mistakes / Bookmarks tabs |
| `/current-affairs` | Month list |
| `/current-affairs/[yyyy-mm]` | Month items and quiz |
| `/progress` | Analytics |
| `/downloads` | Pack manager |
| `/settings/[section]` | Settings |

IDs in routes are **stable content IDs** (e.g. `hist.modern.revolt-1857`), so links survive pack updates.

**Deep links:** Register the `freeexbook://` scheme, e.g. `freeexbook://topic/hist.modern.revolt-1857#causes`. This is used by shared links and "Report error" round-trips.

## 4. Key user flows

### 4.1 First run (onboarding)
1. **Welcome:** one sentence about the app and "Start".
2. **Content language:** English / বাংলা (notes and questions; Hindi is added later). Menus and buttons are always English. A second option, "Show English terms in Bengali content", is on by default.
3. **Exams:** multi-select (UPSC CSE, SSC CGL, IBPS PO, RRB NTPC, state PSCs...). This only pre-selects topics.
4. **Topics:** pre-selected from the chosen exams, with the total download size shown and the option to adjust.
5. **Download:** progress per pack. The user can **start studying as soon as the first pack is installed**.
6. **Offline / sideload option:** "Have a pack file? Import from disk."

The user can skip any step. Onboarding never blocks access to installed content.

### 4.2 Study a topic
Library → Subject → Topic (Notes) → read → "Practice this section" or the **Practice** tab → session → result → "Revise mistakes" or "Back to notes".

### 4.3 Practice session
```
Question ─(select)→ Check ─→ Feedback + explanation ─→ Next
    │                                     └─ "Revise in notes" (opens note section in side panel)
    └─ Skip / Bookmark / Report error
End of set → Summary (score, time, wrong list) → Retry wrong · Next set · Back to topic
```
- Leaving mid-session saves progress automatically. No confirmation is needed.

### 4.4 Mock test
```
Tests hub → Instructions (pattern, marks, negative marking, time) → Start
→ Exam view (palette, timer, mark for review, save & next)
→ Submit (confirm dialog showing answered/unanswered/marked counts)
→ Result → Review (filter: wrong / unanswered / marked / all)
```
- **Leaving a running test requires confirmation** ("Pause and exit? The timer will stop and you can resume later.").
- Auto-submit when the timer reaches 0.
- **Exam-pattern tests** use the exam's sections, marks and negative marking (from `content/exams/`, shipped in the signed manifest). If the installed topics can't supply every question, the test is **shortened and its time scaled in proportion**, and the Tests page and instructions say so.
- Question selection prefers questions never attempted, then ones answered wrongly last time.
- Answers given in tests count as attempts (mode `test`), so wrong ones appear in **Revise → Mistakes**.
- The exam view (`/tests/[id]/run`) hides the sidebar and top bar. Leaving it asks "Pause and exit?"; progress and remaining time are saved every few seconds and after every answer.
- State is saved after every answer so a crash or close can **resume**.

### 4.5 Revise
Due cards (FSRS) first, then Mistakes, then Bookmarks. Each review uses the same QuestionCard UI with "Again / Hard / Good / Easy" grading after the answer is revealed. Grading is auto-suggested from correctness and time.

### 4.6 Downloads
Installed packs (with update badge) → Available packs by subject → Pack detail (size, version, changelog, question/note counts) → Download / Update / Remove. Removing a pack keeps the user's progress history.

## 5. Back and history behaviour

- The app uses normal history. **Back** (Alt+← / ⌘[ / mouse back button) works everywhere except inside a running test.
- The topic page remembers its last tab and scroll position.
- Breadcrumbs appear on Library and Topic pages: `Library › History › Modern India › Revolt of 1857`.
- Opening a note from a question opens a **side panel**, not a navigation, so the user does not lose their place.

## 6. Keyboard shortcuts

Shown in Settings → Keyboard and in a `?` overlay.

| Context | Key | Action |
|---|---|---|
| Global | `Ctrl/⌘ + K` | Search / command palette |
| Global | `Ctrl/⌘ + ,` | Settings |
| Global | `G` then `H` / `L` / `P` / `T` / `R` | Go to Home / Library / Practice / Tests / Revise |
| Global | `?` | Shortcut help |
| Global | `Ctrl/⌘ + =` / `-` / `0` | Font size up / down / reset |
| Global | `Ctrl/⌘ + L` | Toggle content language (English ⇄ বাংলা) on the current page |
| Question | `1`–`4` or `A`–`D` | Select option |
| Question | `Enter` | Check answer → Next |
| Question | `S` | Skip |
| Question | `B` | Bookmark |
| Question | `E` | Toggle explanation |
| Question | `N` | Open related note in side panel |
| Test | `M` | Mark for review |
| Test | `→` / `←` | Next / previous question |
| Test | `Ctrl/⌘ + Enter` | Submit test (opens confirm) |
| Revise | `1`–`4` (after reveal) | Again / Hard / Good / Easy |
| Any panel | `Esc` | Close overlay / side panel / dialog |

Single-letter shortcuts are disabled while a text input has focus.

In Bengali questions, options are labelled **ক খ গ ঘ**, but the keys stay `1–4` / `A–D` (they map to the same positions). The `?` overlay shows both labels.

## 7. Top bar

- **Content language button** (globe icon + current language, e.g. "বাংলা ▾"): opens a menu to pick the content language. Same as `Ctrl/⌘ + L` and Settings → Content language. Changing it re-renders the current page in place.
- **Theme toggle** (sun/moon).

## 8. Global status indicators (top bar)

- **Offline**: a small muted "Offline" chip. Informational only, never a blocker.
- **Downloading**: a progress chip that opens Downloads.
- **Update available**: a dot on Downloads; app updates appear as a dismissible banner, at most once per day.
