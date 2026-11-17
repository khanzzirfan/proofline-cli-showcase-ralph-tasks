# Recommendation: run 8-claude-opus

Date: 2026-11-17. Ranking source: `ranking.md` / `ranking.json` (pick_score, max 40).
File paths below are relative to `session-recorder-chrome-extension/` and were checked against the source tree on 2026-11-17.

| Rank | Feature | Node(s) | pick_score | pain_score | Must not duplicate |
|---|---|---|---|---|---|
| 1 (top pick) | Copy for coding agent | P02 (+P03, P06) | 35 | 16 | #43 Copy as cURL |
| 2 | Acceptance check section | P07 (+P04) | 34 | 18 | #22 (closed) Playwright repro, #39 request and trace IDs |
| 3 | Video key frames in the report | P10 (+P12) | 32 | 14 | #21 screenshot shortcuts |

All three are small enough for one PR each. They also fit together: #1 is the hand-off, #2 tells the agent what "fixed" means, #3 makes the video readable. I would build #1 first because it has the best fit and is the smallest.

---

## 1. "Copy for coding agent" button (top pick)

**User and pain.** Developers and vibe coders who debug web apps with Cursor, Claude Code or Copilot spend their day copying console errors and request details from DevTools into the chat (P02: Cursor forum thread with 47 likes and 3,295 views, "I’m kind of tired of copy pasting stuff from my console window into the chat"; three more Cursor threads; an HN comment; a blog post titled "Copying and Pasting Console Logs to My AI All Day Long Sucks"). People who have already found the bug want to give the agent exactly what they saw (P03). Session Recorder already captures all of it, but the hand-off is still: export the ZIP, unzip it, open `report.md`, find the suggested prompt in `docs/report-format.md`, and paste both. The only clipboard action today is `copyIssue()` in `entrypoints/share/useShareReport.ts`, which copies the GitHub issue body (with a hosted-report link), not the report.

**Feature.** A "Copy for agent" button in the side panel export view. One click builds `report.md` at the chosen verbosity level (default Compact/L2, so it fits in context), wraps it in the suggested prompt from `docs/report-format.md`, and writes it to the clipboard. The prompt starts with a short "untrusted evidence" note (P06: text captured from the page, such as console messages and response bodies, is data, not instructions). Screenshots cannot go through a text clipboard, so the copied text lists their file names and says "export the ZIP if you need the images". The button shows the token estimate it already computes (`estimateForLevels`) and warns above the existing `TOKEN_WARN_LIMIT` (180,000).

**UX.** Side panel → open a session → Export panel → **Copy for agent** (next to "Download .zip"). One click after opening the session; the toast says "Copied ~12k tokens (Compact)". The same button can sit in the report tab (`entrypoints/report/main.ts`) next to its ZIP button. No new settings.

**Files likely touched.**
- `lib/export/agent-prompt.ts` (new): `buildAgentPrompt(report: string, opts: { level, tokenEstimate, screenshotPaths })` returns the prompt text. Pure function, easy to test.
- `lib/export/agent-prompt.test.ts` (new): unit tests.
- `lib/export/bundle.ts`: reuse `buildBundle` to get `report.md` text without zipping (maybe a small helper that returns only the report file).
- `entrypoints/sidepanel/components/ExportPanel.tsx`: the button, clipboard write, status text.
- `entrypoints/report/main.ts` (optional): the same button in the report tab.
- `docs/report-format.md`: replace "paste report.md and copy the prompt" with "click Copy for agent"; keep the prompt text in one place (the new module) and have the doc quote it.
- `e2e/record-export.spec.ts`: a new test.

**How to test.**
- Unit (Vitest): the prompt contains the untrusted-evidence note, the level, the report text verbatim, and the screenshot path list; it never contains raw asset bytes; output is stable (snapshot) for a fixture session built with `lib/fixtures/session-builder.ts`; the report text inside a fenced block cannot break the fence (a report line with ``` gets a longer fence).
- Playwright: extend `e2e/record-export.spec.ts`. Record a session on the test page that throws a console error and makes a failing request, open the Export panel, click "Copy for agent", read the clipboard (grant `clipboard-read` to the context), and check it holds the prompt, the error text and the failing URL.

**Risks.**
- Clipboard permission: the side panel needs focus for `navigator.clipboard.writeText`; it already works for `copyIssue()` in the share page, so reuse that pattern.
- Big reports: at L0/L1 the text can exceed what a chat box accepts. Default to L2 and show the token count.
- Secrets: copying puts captured data on the clipboard. Redaction is the job of the open redaction PRs (#31 #37 #38 #42 #44); this button must use the same trimmed and redacted `report.md` the ZIP uses, not raw events.
- Overlap with the hosted report link: the copy is local and offline, the issue flow is hosted. Say so in the docs.

**Must not duplicate.** #43 (Copy as cURL) copies one request; this copies the whole report as a prompt. Keep the button label and code separate from #43's per-request menu. Closed PR #22 is unrelated. Notes candidate B ("agent-ready GitHub issue") is about the filed issue, not the clipboard; do not touch the issue body here.

---

## 2. "Acceptance check" section in `report.md` and the issue

**User and pain.** Agent users whose agent says "fixed" without checking, and the bug is still there (P07, highest pain together with P01: claude-code #80950, "13 separate rounds of "fixes" (PRs #53 through #65) across 7 days"; #37818, "says "fixed," commits it — but never verifies the fix actually works"; #66054, "Repeatedly said "deployed" and "done" without ever producing a screenshot"; #42834; #319 with 11 reactions). Vague reports also lead to confident fixes for the wrong problem (P04). Users ask the agent to check the real output before it claims success, but nobody tells the agent what "the real output" should be.

**Feature.** A recording already knows the exact signals of the bug: the console errors and uncaught exceptions, the failing requests (method, path, status), and the page and step where they happened. At export, add an `## Acceptance check` section near the top of `report.md` (after the header, before `## Timeline`), and the same list at the end of the GitHub issue body. It is a checklist written for the agent: "After your fix, replay these steps and confirm: ☐ no `TypeError: cannot read 'id' of undefined` in the console at `/checkout` (first seen [01:12]); ☐ `POST /api/orders` no longer returns 500 (seen [01:13]); ☐ the user's note at [01:20] — 'button should show the receipt' — is true." Items come from deterministic rules (dedupe errors by message, keep the first failing request per method+path, include user annotations marked as expectations), so no model call is needed. The section is capped (for example 8 items) and appears at every verbosity level, because it is the shortest and most important part of the report.

**UX.** No new click: it appears in every export and in the issue preview on the share page, where the user can edit it like the rest of the body. One optional toggle in export settings ("Include acceptance check", on by default).

**Files likely touched.**
- `lib/export/acceptance.ts` (new): `buildAcceptanceChecks(events): AcceptanceItem[]` and `renderAcceptance(items): string[]`.
- `lib/export/acceptance.test.ts` (new).
- `lib/export/markdown.ts`: call it from `renderReport` between `renderHeader` and `## Timeline`.
- `lib/export/trimmer.ts`: make sure the section's source events (errors, failing requests) are kept at every level; they already are per "What we never trim" in `docs/report-format.md`, so only a test is needed.
- `lib/sharing/github.ts` (`issueBody`) or `entrypoints/share/useShareReport.ts`: append the checklist to the issue body.
- `lib/export/markdown.test.ts`, `lib/sharing/github.test.ts`: update expectations.
- `docs/report-format.md`: document the section and add "use the acceptance check before you say done" to the suggested prompt.

**How to test.**
- Unit: a fixture session with two identical errors, one 500 and one 404 to the same path, and one annotation gives exactly one error item, one item per method+path, and one note item, in time order; a session with no errors gives a "no errors captured: confirm the user's notes" fallback; the cap holds; page-controlled text (error messages) is put in inline code so it cannot inject Markdown or links.
- Playwright: in `e2e/record-export.spec.ts`, record a page that logs an error and gets a 500, export, unzip, and assert `report.md` contains `## Acceptance check` with both items. In `e2e/sharing.spec.ts`, assert the issue preview contains the same checklist.

**Risks.**
- Noisy pages: third-party errors (analytics, extensions) would become false checks. Reuse the trimmer's analytics filter (`lib/export/trimmer.analytics.test.ts` shows it exists) and drop errors from other origins by default.
- Expected 4xx (for example a 401 before login) are not bugs. Only list 5xx, network failures, and 4xx that the user annotated or that sit next to an error.
- It is a checklist, not a test: agents may still skip it. The value is that a human reviewer can now check the PR against a concrete list.

**Must not duplicate.** Closed PR #22 (Playwright repro test in the ZIP) was the large, executable version; this is a small, text-only list and must not generate test code. #39 adds request and trace IDs of failed requests; the acceptance check can reference those IDs if #39 lands but must not add its own ID extraction. #49 (group recordings of the same error) dedupes across sessions; this dedupes inside one session only. #48 (labels and assignees) touches the issue filing flow; keep changes to the issue body, not the filing form.

---

## 3. Video key frames in the report

**User and pain.** Developers and QA who record a bug as video, then find their coding agent cannot watch it (P10: claude-code #12676, 57 reactions, asks for video input for "Sharing quick recordings of bug reproduction steps"; #2614, "This tool cannot read binary files. The file appears to be a binary .mov file."; #14805, "Static screenshots miss flickering, jank, race conditions, and state changes"; several new tools that turn a video into key frames plus a timeline, such as Replay). Session Recorder records tab video, but the ZIP stores it as `video/*.webm`, which text agents cannot open, and at Compact/Minimal the video bytes are dropped. Event screenshots exist, but motion between them (a flicker, a spinner that never ends, a layout jump) is lost. P12 shows the other side: too many or too-large images break agent sessions, so frames must be few and small.

**Feature.** At export (Full and Standard, and optionally at Compact), extract a small set of JPEG frames from each video clip at the moments that matter: just before and just after each click, error and annotation, and at most one frame per N seconds of otherwise idle video. Write them to `frames/{seq}-{mmss}.jpg` (downscaled with the same 1400 px cap as screenshots), list them in `MANIFEST.md`, and add one line to the `report.md` timeline at each frame's time (`🎞 frame [01:12] frames/0003-0112.jpg — 300 ms after click on "Pay"`). Skip a frame if an event screenshot exists within 500 ms. Cap the total (for example 24 frames per report) so the report stays inside image budgets. Extraction uses a hidden `<video>` element, `currentTime` seeks and a canvas, in an extension page that already has the clip blob, so no new dependency (no ffmpeg).

**UX.** No new click. Export panel shows "includes N video frames" under the level, and one checkbox "Video frames" (on by default at Full/Standard). The report page shows frames inline like screenshots.

**Files likely touched.**
- `lib/export/video-frames.ts` (new): `pickFrameTimes(events, clips, opts): FramePlan[]` (pure, testable) and `extractFrames(blob, times): Promise<Blob[]>` (DOM: video + canvas).
- `lib/export/video-frames.test.ts` (new): tests for `pickFrameTimes`.
- `lib/export/bundle.ts`: add frame files to the bundle and to the asset path map (next to the `video/${seq}-${mmss}.webm` naming).
- `lib/export/markdown.ts`: render frame lines in the timeline and rows in `renderManifest`.
- `lib/export/trimmer.ts`: keep frames at L2 (they are small) while still dropping video bytes, if the owner agrees.
- `entrypoints/sidepanel/components/ExportPanel.tsx` and `entrypoints/report/main.ts`: run extraction before zipping (both build ZIPs today), show the count.
- `lib/export/bundle.video.test.ts`, `docs/report-format.md` (zip layout).

**How to test.**
- Unit: `pickFrameTimes` picks before/after times around a click, an error and an annotation; drops frames near existing screenshots; respects the cap and the clip bounds (no seek past the clip end, across a paused gap, or across tab-switch clips); is deterministic.
- Playwright: record a short session with video on a test page that changes colour after a click, export at Full, unzip, and assert `frames/*.jpg` exist, are valid JPEGs under the size cap, are listed in `MANIFEST.md` and referenced in `report.md`. One check that the frame after the click shows the new colour (sample a pixel) proves the seek lands at the right time.

**Risks.**
- WebM from `MediaRecorder` often has no duration or seek index, so `currentTime` seeks can be slow or wrong. Mitigation: fall back to playing the clip at high speed and grabbing frames with `requestVideoFrameCallback`, or fix the duration first; test this in Playwright, not only in unit tests.
- Export time grows with clip length; extraction must be cancellable and show progress (the export panel already has a `phase` text).
- Privacy: frames are new copies of what the video shows. They must pass through any screenshot redaction or blur that lands from the redaction PRs, and should be off when video is off.
- Smallness is 3, not 5: this is the largest of the three PRs (estimate 350 to 500 lines with tests).

**Must not duplicate.** #21 adds screenshot and pause keyboard shortcuts during recording; this works at export on recorded video and adds no shortcuts. #42 (secret protection across evidence) may add blurring of screenshots; reuse its hook for frames if it lands rather than writing a second blur path.

---

## What I would not build now

- **P05 secrets:** real and severe, but five open PRs cover it (#31 #37 #38 #42 #44).
- **P01 live browser access for agents:** the biggest pain, but it is a new product (an MCP server or live bridge), not one PR.
- **P08 visual proof in agent PRs:** real, but an "after" recording posted on the issue needs the filing flow (#48, #49) to settle first.
- **P06 untrusted-evidence preamble:** too small and too thinly evidenced (3 verified sources) to be a PR on its own; folded into feature 1 and worth adding to feature 2's issue text.
