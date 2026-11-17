# Recommendation: top 3 features for Session Recorder (4-claude-sonnet, 2026-11-17)

Picked by `pick_score` from `ranking.json`: P03 (32), P13 (31), P01 (30). P01 is mostly the same hand-off as P03, so the third spec below uses P08 (30, tied) instead. It is a separate, small change.

Extension paths below were checked in the local clone.

---

## 1. "Copy for coding agent" (P03, also helps P01)

**User and pain.** A developer or QA person has just found a bug and wants the agent to start from the exact evidence (P03, P01). Today they export a ZIP, unzip it, paste `report.md`, and copy the "Suggested prompt" from `docs/report-format.md` by hand. HN 46047931 and 48795580 show small tools built only to remove this step. Evidence is vendor-heavy (weak).

**Feature.** A button on the share screen that puts one block on the clipboard: a short agent prompt (taken from the Suggested prompt, with project and page URL filled in) followed by the trimmed `report.md` text at the chosen verbosity level. A size guard cuts the report to a token budget and says what was cut, using the existing trimmer. No server, no MCP.

**UX.** Lives next to the existing "Copy issue" button on the share screen. One click, then a short "Copied" toast. Optional dropdown for the target agent (generic, Claude Code, Cursor); this only changes the wording of the prompt line.

**Files likely touched.**
- `entrypoints/share/useShareReport.ts` (new `copyForAgent`, next to `copyIssue` at about line 330)
- `entrypoints/share/App.tsx` (button, near line 480)
- new `lib/sharing/agent-prompt.ts` and `agent-prompt.test.ts` (pure prompt builder)
- `lib/export/markdown.ts`, `lib/export/trimmer.ts` (reuse only; no change expected)
- `docs/report-format.md` (point the Suggested prompt at the button)

**Tests.** Unit: prompt builder fills fields, is deterministic, respects the budget and states what was trimmed, handles empty console and network. Playwright: add a case in `e2e/sharing.spec.ts` that grants clipboard permission, clicks the button and checks the clipboard begins with the prompt and contains `report.md` headings.

**Risks.** Clipboard size limits on very long reports. Secrets in the copied text: it must go through the same redaction path as the export (open PRs #42, #37, #31, #38, #44 are changing redaction, so call the existing function and do not add rules). Prompt wording is a judgement call.

**Must not duplicate.** #48 (labels and assignees on filing), #49 (group same-error recordings), #43 (Copy as cURL, a different clipboard action; keep the button and code paths separate), #22 (closed Playwright repro test). No open PR copies a full agent prompt.

---

## 2. "Steps to reproduce" and "Expected vs actual" block at the top of `report.md` (P13)

**User and pain.** Developers whose agent "fixes" a flaky or wrong thing because nobody gave exact steps (P13, partly verified; BuildBetter blog is vendor). The report is chronological, not a steps list.

**Feature.** A deterministic summary block at the top of `report.md`: numbered steps built from recorded clicks, navigations and typed-input events (no LLM), then the first error with its `[mm:ss]` timestamp, then "Expected" and "Actual" lines taken from the user's marker notes if any, else left as a labelled placeholder. Steps are capped (for example 15) and collapse repeats.

**UX.** No new UI. The block appears in every export and in the issue body. A settings toggle is optional.

**Files likely touched.**
- `lib/export/markdown.ts` (new section in `renderReport`, line 56)
- new `lib/export/repro-steps.ts` and `repro-steps.test.ts`
- `lib/export/markdown.test.ts`, `bundle.integration.test.ts` (snapshot updates)
- `docs/report-format.md` (document the block)
- `lib/session/types.ts` only if event types need a field (check first)

**Tests.** Unit: fixtures with clicks, navigation, repeated clicks, no errors, no notes; stable output. Playwright: record a short session in `e2e/record-export.spec.ts` and check the exported `report.md` starts with the steps block.

**Risks.** Steps from raw clicks can be noisy (selectors, shadow DOM). Open PR #45 changes shadow DOM clicks and typing, so read events through the existing event types and expect small rebase work. Wrong "Expected" text would mislead the agent, so never guess it.

**Must not duplicate.** #23 (UJG docs bundle: unclear overlap, read it before starting), #25 (typed value before submit: consume its field if merged, do not re-capture), #29 (environment info; keep it in its own section), #22 (closed generated Playwright test; this feature is text only).

---

## 3. Agent-safe screenshot sizes in the export (P08)

**User and pain.** Developers whose Claude Code session dies after one oversized or corrupt image: `claude-code#13480` has 90 reactions and 111 comments, `#2939` has 63 reactions, `playwright-mcp#1211` has 6 reactions. After the error every later message fails (P08, verified).

**Feature.** When building the ZIP and the clipboard bundle, cap every screenshot to a safe longest side (about 1568 to 2000 px) and a byte ceiling, re-encoding as JPEG when needed. The report notes "downscaled from WxH" so an agent can ask for the original. Originals stay in IndexedDB.

**UX.** No new UI by default. A small line in export options: "Agent-safe images (recommended)", on by default.

**Files likely touched.**
- `lib/capture/screenshots.ts` (already has a `screenshotQuality` JPEG path near line 177; may need a resize helper)
- `lib/export/bundle.ts` (apply the cap at export time)
- `lib/export/markdown.ts` (the note)
- `lib/session/settings.ts` and `settings.test.ts` (new option, if kept)
- new `lib/export/image-cap.ts` and test

**Tests.** Unit: size calculation, aspect ratio kept, small images untouched, byte ceiling loops down quality. Playwright: export a session with a large screenshot and assert image dimensions in the ZIP are within the cap.

**Risks.** The exact image limits of each agent must be confirmed in vendor docs before choosing numbers (I did not verify them). Resizing in a service worker needs `OffscreenCanvas`; check the existing offscreen entrypoint. Detail loss for small text in screenshots, so keep the cap generous. Fit is medium: the evidence is about agent chat paste, and our ZIP may rarely hit the limit, so confirm real sizes first.

**Must not duplicate.** #21 (screenshot keyboard shortcut; unrelated, but touches screenshot code), #48 (filing), #32 (HAR export). No open PR resizes images.

---

## Why not the others

P01 (agent cannot see the browser) is the biggest pain but the recording already covers it; the open work is hand-off, which is feature 1. P05 (fixed without proof) is next, but the closed PR #22 shows the large version is risky. P12, P07 and P11 are agent-vendor problems with poor fit. Vision and video (P04, P06, P09): the gaps are real for cloud agents and PR review, but only P08 gives a small buildable feature; a video-to-key-frames feature (P09) would be large and rests on one 57-reaction request plus vendor pages.
