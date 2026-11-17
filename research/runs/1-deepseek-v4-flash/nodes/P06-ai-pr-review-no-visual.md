---
id: P06
title: "AI PR review has no eyes: a code diff cannot show the UI the change produces"
who: developers, QA
tools: [GitHub Copilot code review, Bugbot-style bots, Cursor, Storybook/Chromatic]
status: verified
---
## Pain
AI reviewers read a diff, but the bug being fixed is often visual. A bot can say a null check is
missing; it cannot see that the layout shifted, the button is covered, or the theme broke. Teams
must bolt on a separate visual-regression pipeline or review the UI by hand.

## Evidence
- https://safeguard.sh/resources/blog/what-an-ai-code-review-bot-cannot-see (blog, 2026-10-18, verified): "A pull request shows what changed. It rarely shows why." and bots rarely judge "whether now is the right time".
- https://www.sitepoint.com/review-ai-generated-ui-changes/ (blog, 2026-10-19, verified): "Reviewing AI-generated UI changes in a traditional diff viewer is not just slow; it is structurally inadequate", proposing Storybook + Chromatic.
- https://dev.to/stendya/your-ai-assistant-ships-ui-10x-faster-add-visual-regression-to-github-actions-in-5-minutes-1chn (blog, verified): "every UI change your agent ships carries the same five visual bugs: layout shifts, truncated text, overlapping elements, broken responsive breakpoints, theme regressions".
- https://github.com/lintlab/visual-regression-action (repo/vendor, verified): a GitHub Action that "screenshots your pull request's preview deployment, compares it pixel by pixel with production, and fails the check" (0★, vendor).
- https://dev.to/jackm-singularity/visual-qa-agents-catch-ui-regressions-before-ai-written-code-ships-28pg (blog, verified): "A visual QA agent closes that gap by driving the app like a user, comparing screenshots, checking flows".

## How users want it fixed
- A before/after visual artifact attached to the PR that a human (or bot) can glance at.
- Visual diff as a CI gate instead of manual eyeballing.

## Workarounds people use today
- Storybook + Chromatic/Percy/Lost Pixel; hand screenshots in the PR; preview deployments.

## Session Recorder angle
The extension records screenshots and annotations and can produce a "before" report from the
reporter's side. It cannot see the CI preview or run the diff. A modest feature: include labelled
before/after screenshots and their annotations in the report so a PR reviewer/agent has the visual
truth next to the diff. Real gap, but the extension is not a CI visual-diff tool — fit is partial.

## Scores
frequency: 4  severity: 3  fit: 3  smallness: 3  novelty: 3
