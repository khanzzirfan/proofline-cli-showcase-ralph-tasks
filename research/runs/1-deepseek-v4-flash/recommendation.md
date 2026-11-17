# Recommendation — top 3 feature ideas for Session Recorder

Run `1-deepseek-v4-flash`. Picks are the top three nodes by `pick_score` from `ranking.md`
(P02 = 35, P08 = 33, P09 = 31). Each spec is sized for **one clean PR**: a few hundred lines
plus tests. The open PRs listed are from `00-context-notes.md` §3 and must not be duplicated.

Selected: **#1 P02** (Copy for coding agent) · **#2 P08** (video key frames + timeline) ·
**#3 P09** (repro steps + required state).

---

## Feature 1 — "Copy for coding agent" (one clip: the prompt and a trimmed report)  ← top pick

**Node:** P02 "Copy-pasting logs and cURL into the agent by hand is slow, lossy and leaks tokens"
(`nodes/P02-copy-paste-friction.md`, pick_score 35). Supporting nodes: P01 (agent can't see the
browser — the evidence it needs is exactly what we hold), P13 (payload must fit a context window).

**Who and pain.** Developers debugging a web app with Claude Code/Cursor hand-copy console output,
cURL and response bodies into the chat. It breaks flow, loses formatting, sometimes never reaches
the agent, and risks pasting a token. The evidence is strong and popular: HN comment "saves me
having to copy paste from browser console to my coding agent" (HN 48795580); claude-code#18170
(305 reactions) is copy/paste formatting pain; claude-code#32005 describes the file-save dance as
breaking "the flow". Today the extension copies only the issue Markdown — `copyIssue()` in
`entrypoints/share/useShareReport.ts` — while the `report.md` prompt must be assembled by hand from
`docs/report-format.md` (the known gap, `00-context-notes.md` §3).

**The feature.** A single **"Copy for coding agent"** button that writes one clipboard payload: the
suggested-agent prompt from `docs/report-format.md` followed by `report.md` at the level the user
picked. It reuses the deterministic bundle that already exists, so no new capture, no LLM call, no
network. It is deliberately *not* an MCP server (too big, and P05 shows local MCP is a security
risk) — it is the small, safe handoff.

**UX (where it lives, how many clicks).** In the side-panel `ExportPanel` beside **Download .zip**
— same screen, same level radio, **one click**. On click: build the bundle for the selected level,
concatenate the prompt + `report.md`, `navigator.clipboard.writeText(...)`, then show the existing
busy/"Copied" phase text pattern already used there. Optional second surface (same PR, one extra
call site): a "Copy for coding agent" action in `AdvancedReport` in `entrypoints/share/App.tsx`,
reusing the `share` action plumbing.

**Files likely touched.** Real paths in `session-recorder-chrome-extension/`:
- `lib/export/agent-handoff.ts` **(new)** — pure: `buildAgentHandoff(input) -> string`, combining
  the prompt (a constant moved out of `docs/report-format.md`) with the rendered report.
- `lib/export/bundle.ts` — expose the already-built `report.md` text (or add a thin
  `renderReportText(input)` that calls `renderReport` from `lib/export/markdown.ts`).
- `entrypoints/sidepanel/components/ExportPanel.tsx` — the button + clipboard write + phase text.
- (optional) `entrypoints/share/useShareReport.ts` — a `copyForAgent()` action beside `copyIssue()`;
  `entrypoints/share/App.tsx` — the button in `AdvancedReport`.
- `lib/export/markdown.ts` — only if the prompt constant is exported from here.

**How to test.**
- Unit (`vitest`, node env, `pnpm test`): new `lib/export/agent-handoff.test.ts` — the payload
  starts with the prompt, contains a `# Session Report` block, uses the chosen level, and honours
  trimming (e.g. an L3 build omits a body that L0 keeps). Mirror the existing style of
  `lib/export/markdown.test.ts` / `lib/export/trimmer.test.ts`.
- Playwright (`pnpm test:e2e`): extend `e2e/record-export.spec.ts` (the crown-jewel spec). Grant
  clipboard permission, click "Copy for coding agent" at level L1, read `navigator.clipboard`, and
  assert it contains the prompt + `# Session Report` and **does not** contain `hunter2` (the
  redaction assertion the spec already makes for the zip). Reuse `dispatch` / `extUrl` /
  `tabIdForUrl` from `e2e/support.ts`.
- Quality gates: `pnpm compile` (`tsc --noEmit`), `pnpm compile:e2e`, `pnpm test`, `pnpm test:e2e`.

**Risks.** Low. Clipboard API needs a user gesture (the click is one) and works in an extension
page. Watch the payload size for L0 on long sessions — mitigate by defaulting to the user's selected
level and noting the token estimate the panel already shows. Keep the prompt in one place so it
cannot drift from `docs/report-format.md`.

**Open PRs it must not duplicate.** **#43 "Copy as cURL"** is adjacent (a clipboard copy) but a
different artifact; do not fold cURL copying into this PR. No open PR adds a report/agent clipboard
handoff — this is the P02 lane, still open.

---

## Feature 2 — Video → agent-readable key frames and a timestamped timeline

**Node:** P08 "An agent cannot watch a screen recording: users need frames and a text timeline"
(`nodes/P08-bug-video-agent-cannot-watch.md`, pick_score 33). Supporting nodes: P13 (frame cost),
P14 (narration/annotation as the hand-off).

**Who and pain.** QA, product and developers show a bug with a screen recording, but agents cannot
watch video — "MCP has no video content type, and Claude doesn't take video as input"
(bugdump.com). People narrate the video in prose (lossy) or run small tools that exist only to cut
frames: `s17labs/videobug` ("Your coding agent can't watch video"), `amagilabs/amagi-screen`. The
raw material already sits in the extension — `video-segment` events and the `video/*.webm` assets
(`entrypoints/offscreen/video.ts`, `lib/export/bundle.ts`) — but at L2+ the trimmer drops the video
bytes (`thinVideo()` in `lib/export/trimmer.ts`) and the report only prints a one-line
`🎬 VIDEO segment` marker (`lib/export/markdown.ts`). Nothing an agent can read comes out.

**The feature.** Turn a recording into (a) **N key frames as JPEGs** picked around the moments that
matter (markers, errors, annotations, navigations) and (b) a **timestamped text timeline** written
into `report.md`, so a text-only agent gets the motion in words and a vision agent gets a few
labelled images instead of a multi-MB video.

**UX (where it lives, how many clicks).** No new screen. Frame extraction runs as part of the
existing export when the session has video: a checkbox in `ExportPanel` — "Include key frames from
video" — default on for L0/L1. User flow stays **Download .zip** (1 click); frames appear under
`video/frames/` and the timeline under a `## Video timeline` block in `report.md`, joined to the
`[mm:ss]` clock.

**Files likely touched.**
- `lib/export/video-timeline.ts` **(new)** — pure: pick ≤N timestamps from events (protected
  signals first), emit the timeline text and a frame plan. Unit-testable with no DOM.
- `entrypoints/offscreen/frame-extract.ts` **(new)** — decode the stored WebM Blob, seek, draw to a
  canvas, encode JPEG. Runs in the offscreen document (the only place that already owns media APIs —
  see `entrypoints/offscreen/video.ts` / `main.ts`).
- `entrypoints/offscreen/main.ts` — handle a new message kind; `lib/messaging.ts` — the message type.
- `lib/storage/index.ts` — read the video asset(s) by id (`getAssets`, `putAsset` already exist).
- `lib/export/bundle.ts` — add `video/frames/NNN-mmss.jpg` files and pass them to the renderer.
- `lib/export/markdown.ts` — render the frame lines in the `video-segment` case.

**How to test.**
- Unit: `lib/export/video-timeline.test.ts` — given a fixture session (see
  `lib/fixtures/session-builder.ts`), assert the chosen frame timestamps, the count cap, and the
  timeline text; extend `lib/export/bundle.video.test.ts` (exists) to assert the frame paths are
  included and the report references them.
- Playwright: new `e2e/video-frames.spec.ts` (or extend `e2e/record-export.spec.ts`) — record a
  short tab video, export, unzip with `fflate`, assert `video/frames/*.jpg` exist and `report.md`
  contains the `## Video timeline` block. Follow the download-capture trick already in
  `e2e/record-export.spec.ts`.
- Gates: `pnpm compile`, `pnpm compile:e2e`, `pnpm test`, `pnpm test:e2e`.

**Risks.** Largest of the three. Decoding/seeking WebM in the offscreen doc is browser-version
sensitive and needs a real clip to test. Frame count must be capped (BugDump notes a 1280×720 frame
is ~1,230 tokens) and the whole extraction must stay deterministic and skip gracefully when there
is no video. Consider shipping the pure timeline text first and frames behind the checkbox if the
PR needs to shrink.

**Open PRs it must not duplicate.** None. `docs/PLAN.md` lists live streaming and rrweb DOM replay
as out of scope — both are different from "cut frames + write a timeline". #21 (screenshot/pause
keyboard shortcuts) is capture-side only. This lane is open.

---

## Feature 3 — An ordered "Reproduction" block with required state

**Node:** P09 "An agent can't reproduce the bug: missing steps, state, auth and data"
(`nodes/P09-repro-steps-state-auth.md`, pick_score 31). Supporting nodes: P12 (environment/flaky),
P11 (issue quality).

**Who and pain.** Even with a good report, agents fail when the reproduction needs state the report
does not carry: which user, whether logged in, the exact click order, the data. QA folklore is
blunt — "If they can't reproduce it, then their bug report is of no value" (r/QualityAssurance,
unverified snippet); the environment-manifest essay says without it "the agent cannot trigger the
original failure, so it patches symptoms instead of causes" (negiadventures, verified). Session
Recorder already captures clicks, inputs, navigations and tabs, so the recipe exists in the data
but is not assembled.

**The feature.** Emit a **`## Reproduction`** section near the top of `report.md`: an ordered,
numbered list of the user's steps (from `click`/`input`/`nav`/`spa-route` events, password values
staying `«redacted»`) plus a short **required-state** summary derived from the same stream (was the
user signed in, which route the repro starts on, any uploaded file). It is a rendering feature over
data already captured — no new capture.

**UX (where it lives, how many clicks).** No new UI. The block is part of every `report.md` at L0–L3
(it is cheap text and is exactly what the agent reads first). Optionally a "Reproduction steps"
preview in `ExportPanel` at zero extra clicks. The block is emitted before `## Timeline`.

**Files likely touched.**
- `lib/export/repro-steps.ts` **(new)** — pure: `buildReproSteps(events, session) -> string`
  (steps + required-state). Reads event types from `lib/session/types.ts`.
- `lib/export/markdown.ts` — call it from `renderReport()` and print the section after the header.
- `lib/export/bundle.ts` — only if the section needs `CaptureSettings` threaded through
  `RenderInput`; otherwise no change.
- `lib/export/trimmer.ts` — no change expected (the block is derived after trimming), but confirm it
  is present at L3 too.

**How to test.**
- Unit: `lib/export/repro-steps.test.ts` — a fixture session yields numbered steps in time order,
  a redacted password never appears, and required-state reflects a signed-in nav sequence; extend
  `lib/export/markdown.test.ts` to assert the `## Reproduction` heading renders at every level.
- Playwright: extend `e2e/record-export.spec.ts` — after the existing record→export step, assert the
  unzipped `report.md` contains `## Reproduction` and that the password it typed (`hunter2`) is
  absent while the click order it performed (`GET fetch`, etc.) is present.
- Gates: `pnpm compile`, `pnpm compile:e2e`, `pnpm test`, `pnpm test:e2e`.

**Risks.** Overlap discipline is the main risk (see below): environment fields are #29's job and a
storage snapshot is #41's. Keep this PR to *assembly of steps + required state from the event
stream* and build on those PRs rather than re-deriving browser/OS/viewport. Deriving "signed in" is
heuristic — keep it conservative and label it as inferred.

**Open PRs it must not duplicate.** **#29** ("browser, OS, viewport in report") already adds
environment; **#41** ("storage snapshot") touches state. This PR must build on those and add only
the ordered steps + required-state summary, not repeat their fields.

---

## Why these three

`pick_score` rewards fit, smallness and novelty, not just how much the world hurts. P02 wins on the
only perfect smallness (5): it is one clipboard write over a bundle the extension already builds,
and `00-context-notes.md` §3 names it as the unfilled gap. P08 is second because video is where the
extension already holds the raw material but produces nothing an agent can read (real, unpicked
gap; loses a point on smallness). P09 is third on the pick tie-break: it keeps fit 4 and smallness
4 and is genuinely distinct from the two above. P01, the fifth node, is the same clipboard move as
P02 and is deliberately not shipped twice; P05 hurts the world most (`pain_score` 18) but six open
PRs already own redaction, so it is context, not a target.
