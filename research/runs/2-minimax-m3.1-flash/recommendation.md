# Recommendation — run `2-minimax-m3.1-flash`

Date: 2026-11-17 · Ranking source: [`ranking.json`](./ranking.json) / [`ranking.md`](./ranking.md)
Target: `session-recorder-chrome-extension` (WXT + React + TypeScript, `prooflinedev/session-recorder-chrome-extension`)

## The three features, in pick_score order

| # | Feature | Node | pick | pain | One line |
|---|---|---|---|---|---|
| 1 | **Copy for AI agent** | P03 | **37** | 18 | One click copies the agent instructions + the trimmed `report.md` to the clipboard. No ZIP, no unzip, no terminal paste. |
| 2 | **Screenshots a text-only agent can use** | P08 | 34 | 18 | Every screenshot gets a caption the agent can read, and the pack gets an `AGENT.md` telling the agent what is in the folder. |
| 3 | **Copy the failing call** | P01 | 34 | 16 | One click copies just the console errors and the failed requests — the two things the agent cannot see and never receives. |

*Source counts below are the `verified_sources` field from `ranking.json` — the verified, non-dropped URLs that
`sources.md` maps to the node. It can exceed the node's *Evidence* bullet count, because a node may also cite a
verified source in its "How users want it fixed" or "Workarounds" section (P08's twelfth is
`anthropics/claude-code#18170`, cited under Workarounds).*

**The recommendation: ship feature 1 as the one pull request.** Features 2 and 3 are the ranked runners-up and are
specified here so the owner can choose. Feature 3 is a 30-line section inside feature 1's bundle and is the obvious
follow-up; feature 2 is a separate, pack-side change and should be a second PR.

Why feature 1 wins on its own merits, beyond the number:

- The extension **already captures everything the agent lacks** — console, exceptions, network, screenshots,
  annotations (`lib/capture/console.ts`, `lib/capture/network.ts`, `lib/capture/screenshots.ts`). The gap is
  delivery, and delivery is cheap here.
- `lib/export/bundle.ts` already produces `report.md` at a chosen level, and `docs/report-format.md` already contains
  the exact prompt that makes it usable — the prompt lives only in a documentation file and never reaches a user.
- `navigator.clipboard.writeText` is already used (`entrypoints/share/useShareReport.ts:332`), so the mechanism is
  proven inside this codebase.
- The current path forces the user to leave the tool they are in, which is exactly what the evidence says people
  refuse to do (`https://github.com/anthropics/claude-code/issues/12644`, verified).

### Two facts about the current code that shape the design

1. **The existing copy action is unreachable without publishing.** In `entrypoints/share/App.tsx` the
   *Copy issue Markdown* button sits in the `else` branch of `{!state.publication ? … : …}` (lines 467–483), and
   `finalBody` is `''` unless `publicationReady(state.publication)` (`useShareReport.ts:295-297`). So today the only
   copy action in the product requires publishing the report to Cloudflare Pages or Proofline first. Feature 1 must
   **not** sit behind that branch: copying to the local clipboard is a local operation and publishing is an upload.
2. **`report.md` contains its own fenced code blocks.** Network bodies and console output are rendered inside
   triple-backtick fences (`lib/export/markdown.ts:348-361`, `:497-503`, `:544-546`, `:619-630`). A bundle that wraps
   the report in a ` ``` ` fence would break it. The builder must compute the longest backtick run inside the report
   and use a fence one longer. This is the single most likely thing to get wrong in the implementation, and it is
   exactly what a unit test must pin.

---

## Feature 1 — "Copy for AI agent" (node P03) · pick 37 · **the pick**

### The user and their pain

A developer or QA engineer has just reproduced a bug in a web app and wants a coding agent to fix it now. The agent
cannot see the browser, so the only way to help it is to hand over the recording. Today that means: export the ZIP,
unzip it, open `report.md`, copy it, paste it into the agent, then find the *Suggested prompt* in
`docs/report-format.md` and paste that too — and hope the agent can still find the screenshots.

Evidence (all verified, see `nodes/P03-hand-bug-straight-to-an-agent.md`):

- The Cursor forum's most-liked thread in this whole run (9 432 likes) asks for exactly this hand-off:
  `https://forum.cursor.com/t/integration-with-developer-tool/34824` — *"copying and pasting stuff from chrome
  developer tools (API requests, responses, browser console in particular) and into cursor to troubleshoot issues"*.
- A cloud session cannot even unzip a local file:
  `https://github.com/anthropics/claude-code/issues/101957` — *"I have to download, unzip, upgrade gh and run it
  locally, which defeats the point of a cloud session."*
- The demand is commercial, not theoretical: `https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/96`
  (77 reactions), `https://github.com/teunlao/vidin`, and
  `https://forum.cursor.com/t/i-m-building-annotatefix-to-bring-customer-bug-reports-and-browser-evidence-to-your-coding-agent/174630`.
- The paste itself is unreliable, which is why a *file-level* bundle matters:
  `https://github.com/anthropics/claude-code/issues/18170` (305 reactions, 140 comments) — *"it breaks every terminal
  copy-paste of code/config blocks"*.

### The feature, in one paragraph

Add one action, **Copy for AI agent**, that puts a complete, self-describing debugging hand-off on the clipboard: the
agent instructions that today exist only in `docs/report-format.md` (the "Suggested prompt" block), the trimmed
`report.md` at the level the user has selected, and a short list of the files that ship with the report so an agent
that can read files knows what else is on disk. The user clicks once in the Share report tab, switches to their
agent, and pastes. Nothing is uploaded, nothing is unzipped, and the report does not have to be published first.

### UX

- **Where it lives:** the Share report tab (`entrypoints/share/App.tsx`), in the *Report options* disclosure
  (`AdvancedReport`), immediately above the existing *Copy issue Markdown* button — but rendered **outside** the
  `state.publication` branch so it is available before any publishing.
- **How many clicks:** **one** — the button. The verbosity level is already a control on the same screen
  (`AdvancedReport` → *Report detail*), and the bundle uses the level currently selected there, so the user does not
  have to choose anything else.
- **Feedback:** the existing `progress()` channel in `useShareReport.ts` already renders a status line
  (`ShareStatus` in `App.tsx`, `aria-live="polite"`). Reuse it: *"Agent bundle copied (L2, ~14k tokens)."*
- **Secondary surface (optional, recommended):** the same action in the side panel next to *Download .zip*
  (`entrypoints/sidepanel/components/ExportPanel.tsx`) for the flow "record → stop → copy" without opening the
  Share tab. This is a second entry point onto the same action, not a second feature.
- **Not required for the user:** no dialog, no options, no new settings. The bundle format is fixed.

### What the clipboard contains

```
# Browser bug report — <session name>

<the Suggested prompt from docs/report-format.md, verbatim>

## Report

````md
<report.md rendered at the selected level>
````

## Files that ship with this report

- `report.md` — the report above
- `screenshots/001-0004.jpg` — screenshot at 00:04
- `network/001-api.example.com-todos.json` — response body
- …
```

The `## Files` list is derived from the bundle's own file list, so it can never drift from what was exported.

### Files likely touched (real paths in the extension)

| Path | Change | New lines (approx) |
| --- | --- | --- |
| `lib/export/agent-bundle.ts` | **new** — pure builder: `buildAgentBundle(files: ExportFile[], opts): string`. Renders the prompt, the fenced report and the file list. Owns the fence-length rule. | ~130 |
| `lib/export/agent-bundle.test.ts` | **new** — unit tests (below). | ~130 |
| `entrypoints/share/useShareReport.ts` | add `copyForAgent()` next to `copyIssue()` (line 330); writes via `navigator.clipboard.writeText` | ~12 |
| `entrypoints/share/reducer.ts` | add `'copy-agent'` to the `operation` union (line 20) | 1 |
| `entrypoints/share/App.tsx` | add the button in `AdvancedReport`, outside the `state.publication` branch | ~15 |
| `docs/report-format.md` | update §"Handing `report.md` to an LLM coding agent" (lines 70–101) to point at the button; keep the prompt text there as the source of truth and say the product now ships it | ~15 |

`lib/export/agent-bundle.ts` stays **pure** — no `chrome.*` access — so it is unit-testable in the existing vitest
setup and reusable from the side panel later. Total diff ≈ **330 lines**, most of it tests.

### How to test it

**Unit (`lib/export/agent-bundle.test.ts`, vitest — same style as `lib/export/markdown.test.ts`):**

1. The bundle contains the agent instructions and the full report text.
2. **The fence rule:** a report containing a ` ``` ` block (a network body, as `lib/export/markdown.ts` renders) comes
   back wrapped in a ` ```` ` fence, and the embedded block is byte-identical to the input.
3. The `## Files` list contains exactly the files in the bundle, and nothing else.
4. Determinism: the same input twice gives the same string; the builder does not mutate its input.
5. An empty/no-file bundle still produces valid output rather than throwing.
6. The report section is not duplicated: the report appears exactly once in the output.

**Playwright (`e2e/share-agent-copy.spec.ts`, new — same fixtures as `e2e/record-export.spec.ts`):**

1. Record a session against the demo page through the `__srTest` hook (`dispatch(background, { kind: 'session/start',
   tabId })`), stop it, open `share.html?session=<id>`.
2. Click *Copy for AI agent*.
3. Read the clipboard from the page context (`navigator.clipboard.readText()`) and assert it contains the prompt and
   the report heading.
4. Assert the button is **enabled before any publishing** — this is the regression test for the `state.publication`
   branch problem described above.
5. Assert the button is disabled while the bundle is preparing and while another operation is running.

`pnpm test` (vitest) and `pnpm exec playwright test e2e/share-agent-copy.spec.ts` are the two gates; `pnpm compile` and
`pnpm compile:e2e` cover the types.

### Risks

| Risk | Mitigation |
| --- | --- |
| The prompt drifts between `docs/report-format.md` and the shipped string. | Move the prompt into one exported constant and have the doc reference it; add a unit test that the doc still contains the same text (cheap string containment check). |
| The bundle is large and the clipboard silently truncates. | Report the size in the status line (`~14k tokens`) and let the existing level control decide; `estimateTokens` in `lib/export/tokens.ts` already computes it. |
| Secrets in the report reach the clipboard. | The clipboard is local — no upload. The existing redaction (`lib/capture/redaction.ts`) already runs at capture time. Do **not** add new redaction here (see the PR table below). |
| Someone expects the bundle to contain images. | State plainly in the status line and in `AGENT.md` (feature 2) that the bundle is text; images live in the export pack. |
| The action is mistaken for "file an issue". | Label it **Copy for AI agent**, never *Submit*, and keep it outside the issue-filing flow. |

### Open PRs it must not duplicate

| PR | Title | Why it is adjacent |
| --- | --- | --- |
| **#23** | `docs: add self-contained UJG bundle` (zavalit) | **Closest overlap.** It already ships "an agent-neutral prompt" and "shared repository instructions" — but as a **docs bundle** (`ujg/`) for journey-graph regeneration, not as a runtime clipboard action. Read it first. This PR must **not** add a competing prompt document under `docs/`; the prompt ships as product code in `lib/export/agent-bundle.ts` and the doc only links to it. |
| **#43** | `feat(report): add one-click Copy as cURL for HTTP network requests` (Ahdanrikzan) | Also a clipboard action in the report surface, and it adds `lib/export/curl.ts` + `e2e/report-curl.spec.ts`. Different target (one request vs. the whole report). Do not touch `lib/export/curl.ts`; keep the new files disjoint so the two PRs merge cleanly. |
| **#24** | File reports as Linear issues | A filing surface, not a clipboard surface. Do not add a Linear branch to this PR. |
| **#48** | Choose labels and assignees when filing a GitHub issue | Same. This PR does not change issue filing. |
| **#22** | Playwright repro test in the ZIP | Closed by its author; about a repro test, not a hand-off. Do not re-add it. |
| **#29**, **#41** | Browser/OS/viewport in the report; storage snapshot | Add metadata to the report. This PR adds no metadata; keep the sections separate so the two diffs do not collide. |
| **#31, #37, #38, #42, #44** | The redaction family | Already merged-by-others territory. This PR adds **no** redaction of its own; it reuses whatever `lib/capture/redaction.ts` already produced. |

---

## Feature 2 — "Screenshots a text-only agent can use" (node P08) · pick 34

### The user and their pain

A CLI coding agent cannot see an image. Claude Code's own issue says it plainly:
`https://github.com/anthropics/claude-code/issues/12644` — *"The Claude Code CLI has no way to accept images or
screenshots."* — and the thread lists four hand-built workarounds, including a `lastshot` script and a `clip2path`
daemon. Copilot CLI's issue lists the same three steps:
`https://github.com/github/copilot-cli/issues/1276` — *"Save the image to disk"*, *"Remember the file location"*,
*"Paste the file path into the CLI"*.

The extension already produces those images (`lib/capture/screenshots.ts`, `screenshots/001-0004.jpg` in the pack) and
already has the **human's own caption** for each one — the annotation text. At L3 the trimmer reduces the
screenshots to a filename manifest (`docs/report-format.md:53`), so the caption is dropped and a text-only agent gets
a name and a timestamp and nothing else. The bug stays a story.

Evidence: P08 — `nodes/P08-cli-agents-cannot-take-or-read-images.md` — has 12 verified sources, the largest evidence set
in this run, plus `https://github.com/github/copilot-cli/issues/476` (57 👍),
`https://github.com/openai/codex/issues/2221`, `https://forum.cursor.com/t/subject-image-copy-paste-in-cursor-chat-stopped-working/167990`
(171 likes), `https://forum.cursor.com/t/custom-api-models-cannot-read-local-image-file-paths-pasted-images-work/167497`
(127 likes).

### The feature, in one paragraph

Give every screenshot a caption that survives every verbosity level, and tell the agent what the pack contains. Add a
`## Screenshots` table to `report.md` at **all** levels — `time | file | what the reporter said` — where the third
column is the annotation text, or the nearest marker/note when there is no annotation, so a text-only agent reads
*"00:12 — screenshots/003-0012.jpg — the discount button does nothing"* instead of a bare filename. Add a root-level
`AGENT.md` to the export pack that names the entry point (`report.md`), the folders (`screenshots/`, `network/`) and
the three-step instruction, so an agent that can open files knows exactly what to open. This is the *pack-side*
counterpart to feature 1's *clipboard-side* bundle, and it is what turns the report into something an agent can act
on without a human narrating it.

### UX

- **Where it lives:** nowhere new in the UI. The table appears inside `report.md` (so it appears in the local report
  viewer, the ZIP and the hosted page), and `AGENT.md` appears in the ZIP root. The side panel's level picker and
  token estimate already reflect the added lines.
- **How many clicks:** **zero** — this is a change to what the existing export produces. The one place the user
  might act is the *Download .zip* button, whose result now contains one more file.
- **Feedback:** the side panel already shows `{state.files.length} files · N MiB` in the Share tab's *Report options*;
  `AGENT.md` is counted there automatically.

### Files likely touched

| Path | Change | New lines (approx) |
| --- | --- | --- |
| `lib/export/markdown.ts` | new `renderScreenshotTable()` called from `renderReport()`; the table replaces the bare filename manifest at L3 and is appended at L0–L2 | ~70 |
| `lib/export/markdown.test.ts` | unit tests for the table at L0…L3 | ~60 |
| `lib/export/bundle.ts` | add `{ path: 'AGENT.md', text: … }` to the file list in `buildBundle()` | ~25 |
| `lib/export/bundle.integration.test.ts` | assert `AGENT.md` is present and names `report.md` and `screenshots/` | ~20 |
| `lib/export/agent-bundle.ts` | **new in feature 1** — reuse the same table in the clipboard bundle | ~10 |
| `docs/report-format.md` | document the new section and the new file in the zip layout (lines 7–34) | ~15 |
| `e2e/record-export.spec.ts` | extend the existing zip assertions | ~20 |

### How to test it

**Unit:** `renderReport()` at L3 must still contain one row per screenshot **with its caption** (this is the
regression the feature exists to prevent); at L0–L2 the table is present and the image links are unchanged; a
screenshot with no annotation falls back to the nearest marker and then to an empty caption rather than dropping the
row. `buildBundle()` returns a file list containing `AGENT.md`.

**Playwright (`e2e/record-export.spec.ts`, extended):** record → *Download .zip* → unzip in-page with `unzipSync`
(the file already imports it) → assert `AGENT.md` exists and mentions `report.md` and `screenshots/` → assert
`report.md` contains the screenshots table with the annotation text.

### Risks

| Risk | Mitigation |
| --- | --- |
| L3 grows past its ~15k-token budget. | The table replaces the filename manifest rather than adding to it; one row per screenshot with a short caption is roughly the size of the manifest line it replaces. Measure with `estimateTokens` and assert the L3 estimate in a unit test. |
| Captions leak personal data. | Captions are user-authored text already present in the report body; no new surface is created. |
| It collides with #23's screenshot coverage. | #23 builds a journey graph with "exact screenshot coverage" and a "visual-review gallery" inside a `ujg/` bundle. This feature adds a flat table to `report.md` and one `AGENT.md`; it must not build a journey graph or a gallery. |
| It reads as a duplicate of feature 1. | It is not: feature 1 changes the clipboard, feature 2 changes the pack. Ship them as two PRs. |

### Open PRs it must not duplicate

| PR | Why |
| --- | --- |
| **#23** | Owns "screenshot coverage" and "visual-review gallery" inside the `ujg/` docs bundle. Do not add a gallery or a coverage graph. |
| **#29** | Adds browser/OS/viewport to the report. The new `## Screenshots` section must stay separate from that metadata block. |
| **#41** | Storage snapshot — adds files to the pack. Coordinate so the pack layout stays predictable. |
| **#43** | Adds `lib/export/curl.ts` and `e2e/report-curl.spec.ts`; the `e2e/record-export.spec.ts` edits must not conflict with its report-viewer changes. |

---

## Feature 3 — "Copy the failing call" (node P01) · pick 34

### The user and their pain

The agent has no console, no network panel and no DOM. The Cursor forum's most-liked thread in the run (908 likes,
staff-confirmed as a bug) is exactly this:
`https://forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console-which-opens-inside-the-cursor-as-a-separate-tab/152452`.
Claude Code's issue lists the workarounds — *"screenshots, paste, WebFetch (no auth, no JS), or driving headless
Playwright via Bash"* (`https://github.com/anthropics/claude-code/issues/57034`, 76 reactions).

The extension already captures it all. The gap is that the only hand-off the product offers is the **whole report**,
and a developer staring at a failing button does not want 150k tokens — they want the one request that 500'd and the
one line the console printed.

Evidence: `nodes/P01-agent-cannot-see-the-browser.md` — P01 has 5 verified sources, including a 908-like forum thread
and a 76-reaction issue. The wider `nodes/P07-report-arrives-as-words.md` covers the same gap from the QA side.

### The feature, in one paragraph

Add a second copy action, **Copy the failing call**, that copies only the evidence an agent needs to start: every
console error and uncaught exception with its `[mm:ss]` timestamp, and every network request that failed (status ≥ 400
or a transport failure) or that is linked to an error through `linkedRequestId`, with method, URL, status, a capped
response excerpt and the path of the full body file when one exists in the pack. It is the small, high-signal slice of
the report, for the case where the developer already knows what they are looking at.

### UX

- **Where it lives:** the Share report tab, in the same *Report options* disclosure, directly under *Copy for AI
  agent*.
- **How many clicks:** **one**. No options; the selection rule is fixed and stated in the copied text.
- **Feedback:** the same `progress()` status line: *"Failing call copied (1 error, 2 failed requests)."*

### Files likely touched

| Path | Change | New lines (approx) |
| --- | --- | --- |
| `lib/export/failing-call.ts` | **new** — pure selector: `collectFailingCall(events): FailingCallBlock` | ~110 |
| `lib/export/failing-call.test.ts` | **new** — unit tests | ~110 |
| `entrypoints/share/useShareReport.ts` | `copyFailingCall()` | ~10 |
| `entrypoints/share/reducer.ts` | `'copy-failing'` operation | 1 |
| `entrypoints/share/App.tsx` | the button | ~12 |
| `docs/report-format.md` | a short "if you only want the failing call" note | ~8 |

### How to test it

**Unit (`lib/export/failing-call.test.ts`):** a `net-request` with status 500 is selected; a 200 is not; a request
whose `requestId` matches an `error` event's `linkedRequestId` is selected even at status 200; a console `error` and
an `exception` are selected; a body is truncated at the cap with an explicit marker; the block is deterministic and
ordered by timestamp.

**Playwright:** extend `e2e/share-agent-copy.spec.ts` — click the action on a recorded session that produced a console
error, assert the clipboard contains the error text and the failing URL, and assert that a successful request is
**not** present.

### Risks

| Risk | Mitigation |
| --- | --- |
| The selection rule misses the real failure. | Select on two independent signals (status ≥ 400 **or** linked to an error), and say in the copied text what was selected and what was not. |
| Duplicates #39 and #43. | #39 adds request/trace IDs to failed requests in the report; this feature reads the same events but must not add the ID fields. #43 copies a request as cURL; this feature copies a *summary block*, not a runnable command. |
| Interaction with the redaction family. | The block must carry the already-redacted values from `lib/capture/redaction.ts` and add no redaction of its own. |

### Open PRs it must not duplicate

| PR | Why |
| --- | --- |
| **#43** | Copy as cURL — same source events, different output. Do not reuse its `lib/export/curl.ts` or its `shellQuote`; do not make this feature emit a runnable command. |
| **#39** | Request and trace IDs of failed requests. Do not re-add the ID fields; read them if present, ignore them otherwise. |
| **#31, #37, #38, #42, #44** | The redaction family. Reuse, do not re-implement. |
| **#32** | HAR export. A different artifact; do not emit HAR here. |
| **#40** | Redirect hops as separate requests. It changes the event stream; this feature must tolerate it, not reimplement it. |

---

## Which PR to open first

**Open feature 1 ("Copy for AI agent") as the single pull request.** It is the highest pick_score (37 against 34 and
34), the smallest coherent diff (~330 lines including tests), it needs no new permissions, no new dependency and no
new manifest entry, and it addresses the pain with the most independent evidence (P03 has 11 verified URLs, 8 of them
high-engagement). It is also the only one of the three that needs no change to the export format, so it can be
reviewed on its own without the owner first agreeing to a new pack layout.

Feature 3 is a natural second PR (a second button plus one pure module) and reuses feature 1's plumbing.
Feature 2 is a third PR and is the one that changes the pack layout, so it should go last and after #23 has been
merged or rejected.

### Plain answers to the two questions the PRD asks outright

- **Is there a real vision gap?** Yes. P08 has 12 verified URLs — the largest evidence set in the run — carrying 171
  likes, 127 likes, 57 👍, 35 👍, 21 reactions and 30 comments. P06 and P10 both sit in the top ten. A CLI agent
  literally cannot accept an image. Feature 2 is the tractable slice.
- **Is there a real video gap?** Yes, but it is **not** a good pull request. P09 is last on pick_score (23) because
  `smallness` is 1: turning the recorded `.webm` into key frames plus a timeline needs an ffmpeg-class pipeline, and
  the space is already occupied (`bradautomates/claude-video` at 21 021 stars, `teunlao/vidin`, Clipy, Loom). Do not
  build it.
