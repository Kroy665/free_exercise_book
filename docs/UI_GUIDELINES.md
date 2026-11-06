# UI Guidelines

## 1. Design principles

1. **Focus first.** A student studying for hours needs calm screens. One primary action per screen. No decorative noise.
2. **Readable for long sessions.** Comfortable line length, generous line height, real dark mode.
3. **Fast on weak hardware.** No heavy animations, blur effects or huge images. Every interaction should feel instant (< 100 ms).
4. **Offline is normal, not an error.** Never show a scary error because there is no internet. Show what is available.
5. **Every script renders correctly.** Bengali (launch language), Devanagari and other Indic scripts are first-class, not an afterthought.
6. **Keyboard friendly.** Everything in practice and tests can be done without a mouse.
7. **Honest feedback.** Show correctness, verification status and sources clearly. Never hide a wrong answer.

## 2. Layout

```
┌────────┬─────────────────────────────────────────────┐
│        │ Top bar: breadcrumb · search (⌘K) · status  │
│ Side   ├─────────────────────────────────────────────┤
│ bar    │                                             │
│ (nav)  │   Content area                              │
│ 220px  │   - reading pages: max 72ch, centred        │
│ / 64px │   - dashboards: 12-col grid, max 1200px     │
│ coll.  │                                             │
└────────┴─────────────────────────────────────────────┘
```

- **Min window:** 960 × 600. Below 1100 px width the sidebar collapses to icons (64 px).
- **Desktop behaviour, not a web page:** the window itself never scrolls. The sidebar and top bar are fixed; **only the content pane scrolls**, with no rubber-band overscroll. App chrome (sidebar, top bar, buttons, cards) is not text-selectable and uses the arrow cursor; study content stays selectable. The browser context menu (Reload / Inspect) is disabled in release builds.
- **Test mode** hides the sidebar entirely (full-screen exam view, like the real CBT).
- **Spacing scale (px):** 4, 8, 12, 16, 24, 32, 48, 64. Use tokens, never arbitrary values.
- **Radius:** 6 px (controls), 10 px (cards). No pill-shaped buttons except tags.

## 3. Design tokens

All colours, spacing and type sizes are CSS custom properties in `lib/styles/tokens.css`. **Components must use tokens only. No hex values in components.**

```css
:root {
  /* Surfaces */
  --bg:            #FAFAF7;   /* warm paper */
  --surface:       #FFFFFF;
  --surface-2:     #F2F1EC;
  --border:        #E2E0D8;
  /* Text */
  --text:          #1F2328;
  --text-muted:    #5B616B;
  /* Brand */
  --accent:        #1F5FAD;   /* calm blue */
  --accent-fg:     #FFFFFF;
  /* Semantic */
  --correct:       #1E7A46;
  --correct-bg:    #E6F4EC;
  --wrong:         #B42318;
  --wrong-bg:      #FDECEA;
  --review:        #8A5A00;   /* marked for review */
  --review-bg:     #FFF4DB;
  --focus-ring:    #1F5FAD;
}
:root[data-theme="dark"] {
  --bg:            #14161A;
  --surface:       #1B1E23;
  --surface-2:     #23272E;
  --border:        #33383F;
  --text:          #E6E8EB;
  --text-muted:    #A0A6AF;
  --accent:        #6EA8FE;
  --accent-fg:     #0B1220;
  --correct:       #4CC38A;
  --correct-bg:    #12291E;
  --wrong:         #F97066;
  --wrong-bg:      #2E1513;
  --review:        #F5B83D;
  --review-bg:     #2C2210;
  --focus-ring:    #6EA8FE;
}
```

- Theme options: **System** (default), Light, Dark. Applied before first paint.
- All text/background pairs must meet **WCAG AA** (4.5:1 body, 3:1 large text and UI). Check new tokens with a contrast checker in the PR.

## 4. Typography

- **Fonts are bundled** in `static/fonts/` (WOFF2). Never load fonts from a CDN; the app must work offline.
- Font stack:
  ```css
  --font-ui:   "Noto Sans", "Noto Sans Bengali", system-ui, sans-serif;
  --font-read: "Noto Serif", "Noto Serif Bengali", Georgia, serif; /* optional reading mode */
  --font-mono: "JetBrains Mono", ui-monospace, monospace;
  ```
- **Bundled at launch:** Noto Sans/Serif (Latin) and **Noto Sans/Serif Bengali** (variable WOFF2). Add other script fonts (Devanagari etc.) lazily, only when that language is enabled, to keep the installer small.
- **Do not rely on system Bengali fonts.** Older Windows fonts (Vrinda) and some Linux setups render conjuncts (যুক্তাক্ষর) such as ক্ষ, ন্ত্র and স্ব badly. Always use the bundled font.
- **Type scale (rem, base 16 px, user-adjustable 14–22 px):** 0.875 · 1 · 1.125 · 1.25 · 1.5 · 2.
- **Line height:** 1.6 for Latin reading text, **1.75 for Bengali** (tall vowel signs above and below: ি ী ু ূ ৃ, and the headline মাত্রা), 1.3 for headings (1.45 for Bengali headings).
- Bengali glyphs look smaller than Latin ones at the same size. In Bengali mode, scale body text by **1.06×** (`--bn-scale`) so both scripts feel equally readable.

### Bengali number and label conventions
- **UI vs content language:** the UI (menus, buttons, messages) is **always English**. Only study content (topic titles, notes, questions and the labels inside them, such as callout titles, "List I/II", assertion–reason options) follows the selected content language.
- **Digits:** Bengali content is authored with Bengali digits (০–৯); UI numbers (counts, progress) use 0–9.
- **Option labels:** follow the question's language: ক খ গ ঘ for Bengali questions, A B C D for English.
- **Dates:** `১০ মে ১৮৫৭` (day, Bengali month name, year), via `Intl.DateTimeFormat('bn-IN')`.
- **Punctuation:** Bengali sentences end with the দাঁড়ি (।). Never replace it with a full stop in Bengali strings.
- **Reading width:** max 72ch (user setting: narrow 60ch / normal 72ch / wide 90ch).
- Do not use letter-spacing or all-caps on Indic text. It breaks shaping.
- Do not truncate Indic text mid-cluster. Use CSS `text-overflow` only on whole lines.

## 5. Components

Build a small, consistent set in `lib/components/`. Each component has a story or example page and supports both themes.

| Component | Notes |
|---|---|
| `Button` | Variants: `primary`, `secondary`, `ghost`, `danger`. Sizes: sm/md. Always a visible focus ring. |
| `IconButton` | Must have `aria-label` and a tooltip. |
| `Card` | Topic and test cards; whole card is clickable via a real `<a>`/`<button>`. |
| `ProgressBar` / `ProgressRing` | Shows topic completion; includes a text label for screen readers. |
| `Tag` | Exam tags, difficulty, status (`ai-generated` / `reviewed` / `verified`). Status is shown on the topic page and questions, **not on library cards**. |
| `Callout` | Note blocks: `keyfacts`, `exam-tip`, `mnemonic`, `caution`, `as-of`. |
| `QuestionCard` | Stem, statements/table, options, actions. Handles every question type. |
| `OptionButton` | States: default, hover, selected, correct, wrong, disabled. See §6. |
| `QuestionPalette` | Grid of numbers in test mode with legend. |
| `Timer` | `mm:ss`, turns `--review` colour at 5 min, `--wrong` at 1 min; announces at 5 and 1 min via `aria-live`. |
| `EmptyState` | Illustration-free: icon + one sentence + one action. |
| `Toast` | Non-blocking messages, auto-dismiss 4 s, never used for errors that need action. |
| `Dialog` | Confirmations only (submit test, delete pack). Traps focus. Esc closes. |
| `DownloadRow` | Pack name, size, state (available / downloading % / installed / update). |

**Icons:** Lucide (`lucide-svelte`), bundled, 20 px default, stroke 1.75. Icons always come with a text label, except in the collapsed sidebar, where they have a tooltip and `aria-label`.

## 6. Question and answer states

Correctness must **never rely on colour alone**. Always pair it with an icon and text.

| State | Visual |
|---|---|
| Default | `--surface`, `--border` |
| Selected (before submit) | `--accent` 2 px border, filled radio |
| Correct | `--correct-bg`, `--correct` border, ✓ icon, "Correct answer" (sr-only) |
| Wrong (user's choice) | `--wrong-bg`, `--wrong` border, ✗ icon, "Your answer" label |
| Not chosen | Dimmed to 70% opacity after submission |

- **Practice mode:** The answer is revealed after the user clicks **Check** (or presses Enter), then the explanation panel expands below.
- **Test mode:** Nothing is revealed until the test is submitted.
- Option labels are **A B C D** (or (a) (b) (c) (d) when matching an exam style). Keys `1–4` and `A–D` both select.

### Test palette legend
| State | Style |
|---|---|
| Not visited | outline |
| Not answered | `--wrong` outline |
| Answered | `--correct` fill |
| Marked for review | `--review` fill |
| Answered + marked | `--review` fill with a ✓ dot |

## 7. Notes reader

- Sticky table of contents on the right (≥ 1280 px) or a dropdown (smaller).
- Callout blocks use a left border plus icon, not a full background flood.
- Tables: zebra rows, sticky header, horizontal scroll inside the table (never the page).
- Timelines render as a vertical list with dates in a fixed-width column.
- Every section heading has a "Practice this section" link when questions reference it.
- "As of" and source badges appear inline after time-sensitive facts, in muted text.

## 8. Motion

- Durations: 120 ms (hover/press), 200 ms (panels). Easing: `cubic-bezier(.2,.0,.0,1)`.
- No motion that conveys essential information.
- Respect `prefers-reduced-motion`: disable all transitions except opacity.

## 9. Accessibility (WCAG 2.2 AA)

- Semantic HTML first (`button`, `a`, `nav`, `main`, headings in order).
- Visible focus ring (2 px `--focus-ring`, 2 px offset) on every interactive element.
- All flows are keyboard-only operable. See shortcuts in [NAVIGATION.md](NAVIGATION.md).
- Screen-reader text for answer states, timer warnings and download progress (`aria-live="polite"`).
- Hit targets ≥ 32 × 32 px.
- Set `lang` attributes on content (`lang="bn"` for Bengali, `lang="en"` for English terms inside Bengali text) so screen readers switch voice and the right font features apply.
- Test with NVDA (Windows), VoiceOver (macOS) and Orca (Linux) before each release.
- Automated check: an axe-core scan (WCAG 2.0/2.1/2.2 A and AA rules) of every screen in light and dark mode found **0 violations** (v0.2). Automated tools catch only part of the issues; the manual screen-reader and keyboard checks above still apply.

## 10. Writing style for UI text

- Plain, friendly and short. Use the second person ("Your progress"), never jargon.
- Buttons are verbs: "Download", "Start test", "Check answer". Never "OK" alone.
- Errors say **what happened and what to do**: "Couldn't download Polity (no internet). It will retry when you're online."
- Numbers use the Indian format where relevant (1,00,000), via `Intl.NumberFormat('en-IN')`.
- Dates use `6 Nov 2026` style. Do not use ambiguous `06/11/26`.
- Every UI string goes through `t()` (en.json). Content can be ~40% longer in Bengali; never fix widths to English text.
- UI copy is English only. Bengali text appears only inside study content (see CONTENT_GUIDELINES §7).

## 11. States every screen must design for

Loading (skeletons, not spinners, for > 300 ms), empty (nothing downloaded yet), offline, partial (some packs outdated), error (with retry), and success.
