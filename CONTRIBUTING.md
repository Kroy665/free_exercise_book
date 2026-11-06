# Contributing

Thank you for helping build a free study tool for millions of aspirants. You can contribute in four ways, and **none of them except code requires programming**.

| Contribution | Skills | Start here |
|---|---|---|
| **Review content** | Subject knowledge | Pick a topic with `status: ai-generated`, check facts against sources, open a PR changing it to `reviewed` |
| **Write content** | Subject knowledge, Markdown | [docs/CONTENT_STRUCTURE.md](docs/CONTENT_STRUCTURE.md), [docs/CONTENT_GUIDELINES.md](docs/CONTENT_GUIDELINES.md) |
| **Translate** | Fluent Bengali (or Hindi / another Indian language) | [CONTENT_GUIDELINES §7](docs/CONTENT_GUIDELINES.md#7-translation-guidelines), plus `apps/desktop/src/lib/i18n/` for UI strings |
| **Code** | Rust and/or Svelte | [docs/APP_STRUCTURE.md](docs/APP_STRUCTURE.md), [docs/CODING_GUIDELINES.md](docs/CODING_GUIDELINES.md) |

You can also **report errors** with the in-app button or by opening an issue with the question ID.

## Reviewing a topic (most needed)

1. Open the topic folder, e.g. `content/subjects/history/modern/revolt-of-1857/`.
2. For every question, check the answer, the explanation and each distractor against a source from [CONTENT_GUIDELINES §4](docs/CONTENT_GUIDELINES.md#4-sources).
3. Fix any errors. Set `status: reviewed` on the questions you checked and add your GitHub handle to `reviewers` in `topic.yaml`.
4. Open a PR titled `content(history): review revolt-of-1857`, with a note on what you changed and which sources you used.

## Pull request checklist

- [ ] Follows the relevant guideline document
- [ ] CI passes (lint, tests, content validation)
- [ ] Original wording (no copied text or questions)
- [ ] Version bumped in `topic.yaml` (content PRs)
- [ ] Screenshots for UI changes (light and dark)

## Licensing

- Code contributions are licensed under **GPL-3.0-or-later**.
- Content contributions are licensed under **CC BY-SA 4.0**.

By opening a PR you confirm you have the right to contribute the work under these licenses.

## Code of conduct

Be respectful and helpful. Assume good intent. No harassment, discrimination or political campaigning in project spaces. Maintainers may remove content or contributors who break this.
