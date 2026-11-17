# Recommendation — Session Recorder features

Agent: deepseek/deepseek-v4-pro · 2026-11-17

Top 3 feature ideas by `pick_score` from `ranking.json` (`pick_rank` = P08, P02, P01). Each is
buildable as one clean PR (a few hundred lines with tests) by one engineer. Full pain evidence is in
`nodes/P08-video-keyframes-for-agents.md`, `nodes/P02-copy-paste-friction.md`, and
`nodes/P01-agent-cannot-see-browser.md`.

---

## 1. Agent-readable visual timeline — keyframes, transcript and click targets (P08, 34)

**User and pain.** Developers and QA. Coding agents cannot take video input, and even the ones that
can burn tokens and lose the signal. Animation, race-condition and gesture bugs cannot be captured
in one frame; users want the recording turned into "select frames at the moments narration and
clicks line up, usually 4 to 8 for a 2 minute video" plus a transcript and click targets
(`nodes/P08`, [claude-code#12676](https://github.com/anthropics/claude-code/issues/12676), 57
reactions / 21 comments).

**Feature.** Emit a "Visual timeline" appendix into `report.md` and a `keyframes/` folder into the
ZIP. Deterministically pick a small number of keyframes per `video-segment` at the moments where
narration, clicks, annotations or errors line up, and render a compact table joining
`[mm:ss]` → keyframe image → transcript line → click/annotation target. This turns the recorded tab
video the extension already captures into the one artifact an agent can actually read.

**UX.** No new clicks — the timeline renders automatically at export, below the existing
`## Appendix` sections. It appears at L1/L2 (keyframes are thin JPEGs) and is skipped at L3 where
video is already metadata-only. Where no narration exists, the table still joins clicks/errors to
their nearest frame.

**Files likely touched.**

- `lib/export/keyframes.ts` (new) — pure frame-selection logic: given the trimmed event stream and
  screenshot assets, pick frames at click/narration/error/annotation moments, capped at ~8 per segment.
- `lib/export/markdown.ts` — render the `## Appendix: Visual timeline` table; reuses `formatClock`.
- `lib/export/bundle.ts` — assign `keyframes/*.jpg` paths, write the selected frames as assets, wire
  the new appendix into `renderReport`.
- `lib/export/trimmer.ts` — keep keyframes at L2, treat them like protected annotation screenshots.
- `lib/export/keyframes.test.ts` (new) + extend `lib/export/bundle.video.test.ts`.

**Test plan.**

- Unit: feed `keyframes.ts` a synthetic event stream (click at 00:04, narration at 00:04–00:09, error
  at 00:11) plus screenshots, assert it returns the frames nearest those timestamps and never more
  than the cap.
- Unit: `markdown.ts` renders the table with `[mm:ss]` anchors, image links and the transcript line.
- Playwright: record a short demo session with a click + narration, export L1, assert `report.md`
  contains `## Appendix: Visual timeline` and `keyframes/` holds ≤8 JPEGs.

**Risks.** Decoding webm to extract true frames needs `VideoDecoder`/offscreen plumbing — avoid it:
  reuse the screenshots the recorder already captures at "key moments" (`lib/capture/screenshots.ts`)
  and select from them, which is exactly what the issue's comment asks for. Keyframes can still be
  large on long sessions, so cap count and re-use near-duplicate suppression already in the capture
  layer.

**Must not duplicate.** No open PR touches this. `#32` (HAR export) and the closed `#22` (Playwright
repro) are adjacent only.

---

## 2. "Copy for coding agent" — one click to hand report.md + prompt to the agent (P02, 32)

**User and pain.** Developers. Handing browser evidence to a CLI agent today is manual: export the
ZIP, unzip, paste `report.md`, then re-paste when the agent drops it or indentation breaks it. The
codebase already only copies the issue Markdown (`copyIssue`); the report hand-off is manual
(`nodes/P02`, [claude-code#18170](https://github.com/anthropics/claude-code/issues/18170), 305
reactions / 140 comments).

**Feature.** A "Copy for coding agent" action that writes the trimmed `report.md` followed by the
suggested prompt (from `docs/report-format.md`) to the clipboard in one gesture. It reuses the
bundle already built in memory for the current verbosity level, so there is no extra export step.

**UX.** One button in the report/share view next to the existing copy action. On click it shows
"Copied report + prompt for <agent>." The level selector already in the UI controls what gets copied;
the estimate warns when the clipboard payload is very large.

**Files likely touched.**

- `entrypoints/share/useShareReport.ts` — add `copyForAgent` alongside `copyIssue`, reading the
  current-level `report.md` text from the prepared bundle.
- `lib/export/agent-prompt.ts` (new) — the suggested-prompt string, moved out of the docs so it is
  versioned and testable.
- `entrypoints/share/App.tsx` — the button (and a `clipboard` write handler).
- `lib/export/agent-prompt.test.ts` (new) + a share-hook test for the assembled payload.

**Test plan.**

- Unit: `agent-prompt.ts` returns the exact prompt text; `copyForAgent` concatenates `report.md` +
  prompt with a separator.
- Playwright: open a stopped session, click "Copy for coding agent", assert `navigator.clipboard`
  contains `You are a debugging assistant` and the `# Session Report:` heading.

**Risks.** MV3 clipboard writes need a user gesture (the button provides it); L0 reports can be very
large, so default to the selected level and warn above a size threshold. The prompt is static text —
no LLM call, so this stays deterministic and free.

**Must not duplicate.** `#43` (Copy as cURL) copies only a single request; no PR does the full
report + prompt hand-off.

---

## 3. Agent-consumable DOM context — the rendered element snapshot the agent is missing (P01, 31)

**User and pain.** Developers. Agents read source files but cannot see the rendered DOM the user
actually hit; they guess, change a line, and claim success. The recorder already captures console,
network, clicks and screenshots, but the one thing a browser-less agent still lacks is the rendered
markup around the interaction (`nodes/P01`, [claude-code#57034](https://github.com/anthropics/claude-code/issues/57034),
76 reactions).

**Feature.** Capture and emit a small, capped DOM context for the elements the user clicked, typed
into, or annotated — the element's existing `ElementDescriptor` plus its `outerHTML` and a short
ancestor chain — rendered as a fenced `html` block under the corresponding event in `report.md`. This
gives the agent the page structure without any browser, image, or full rrweb replay.

**UX.** Automatic at capture/export; no clicks. The snippet appears inline under `CLICK`, `INPUT` and
`Annotation` events so it reads in chronological order. Capture caps it at a few KB and routes it
through the existing redaction rules, so it never carries more than the current descriptor already does.

**Files likely touched.**

- `lib/dom/descriptor.ts` — add a capped `outerHtml` + ancestor context to the descriptor builder.
- `lib/session/types.ts` — extend `ElementDescriptor` with optional `outerHtml` / `contextHtml`.
- `entrypoints/interactions.content.ts` and `entrypoints/point-annotations.content.ts` — capture the
  snippet where the descriptor is built.
- `lib/export/markdown.ts` — render the fenced `html` block under the relevant events.
- `lib/dom/descriptor.test.ts` + `lib/export/markdown.test.ts`.

**Test plan.**

- Unit: `buildDescriptor` returns `outerHtml` capped at the limit and skips sensitive inputs; the
  markdown renderer emits a fenced `html` block.
- Playwright: click a demo element and export; assert the report contains the element's selector and
  a snippet of its outerHTML, and that a password input's value is never in the snippet.

**Risks.** `outerHTML` can be large or carry secrets — cap it (a few KB) and reuse `isSensitiveInput`
/ redaction before persisting; keep inner text of sensitive fields out. This is a capture-time
addition, so existing sessions simply lack the field (graceful degrade), no migration needed.

**Must not duplicate.** `#29` (browser/OS/viewport in the report) and `#32` (HAR export) are adjacent;
no PR captures rendered DOM context.
