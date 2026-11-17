# Recommendation — top 3 features for Session Recorder by Proofline

Run `6-minimax-m3` (agent `minimaxai/minimax-m3`), 2026-11-17.

Selected by `pick_score` from `ranking.json` (`2f + 2s + 2fit + sm + nov`, max 40). The full ranking and
its reasoning are in `ranking.md`; the evidence for every pain node is in `nodes/` and every URL is listed
with a status in `sources.md` (**51 verified, 0 unverified, 8 dropped**).

| # | Feature | Nodes | pick_score | pain_score |
|---|---|---|---|---|
| 1 | **Copy for agent** — one action that puts a clean prompt plus the trimmed report on the clipboard | P02, P17, P05 | 32 | 16 |
| 2 | **Evidence index** — a report section that tells the agent exactly which files to open | P05, P01, P02 | 31 | 18 |
| 3 | **Deterministic verdict** — a three-valued pass/fail/unverified per finding, plus a not-a-bug state | P16, P06, P13, P11 | 31 | 14 |

**One correction from US-004, which moved this list.** US-004 had P05 ("make the screenshots safe for
agents") as `top_pick`, on the claim that "no 2000 px dimension check exists anywhere" in the extension.
That claim was wrong. `lib/capture/screenshots.ts:38` reads `const MAX_SHOT_DIM = 1400;` and
`ScreenshotScheduler.capture()` (lines 160–190) already downscales any screenshot whose longest side
exceeds 1400 px and re-encodes it as JPEG. 1400 px is well under the 2000 px limit that poisons a Claude
Code session ([claude-code #13480](https://github.com/anthropics/claude-code/issues/13480)). The sizing and
format half of P05 is **already shipped**. P05 was re-scored (smallness 4→3, novelty 3→2, pick 33→29),
and the open remainder of the pain became feature 2 below: not making the image safe, but making the
agent able to *reach* it.

Everything below is written against the extension as it exists today. The file paths are real and were
checked against the source tree in this run.

---

## Feature 1 — Copy for agent

### The user and their pain

A developer or QA person has just reproduced a bug in a web app with Session Recorder. They want the
agent to look at it. Today the handoff is four manual steps: export the ZIP, unzip it, open `report.md`,
and copy the "Suggested prompt" out of `docs/report-format.md` by hand. The context notes call this gap
out explicitly: *"handing a report to a coding agent is manual (export ZIP, unzip, paste `report.md`, copy
the prompt from the docs)."*

Underneath that sits a sharper pain. The evidence for hand-pasting is not a preference, it is a failure:
console output copied out of a terminal arrives mangled, with visual padding turned into real characters
and URLs hard-wrapped at the terminal width — [claude-code #18170](https://github.com/anthropics/claude-code/issues/18170)
(👍 304, 140 comments) — and sometimes does not arrive at all ("Now Cursor simply says it doesn't see
anything", [Cursor topic 58803](https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803)).
The clipboard is the wrong container for machine-readable text, and the extension is the thing that
already holds the clean version.

- **Nodes:** P02 (pick 32, the mechanism), P17 (the cost/noise half), P05 (the images that ride along).
- **Evidence:** [claude-code #18170](https://github.com/anthropics/claude-code/issues/18170) (github-issue,
  2026-01, verified): "Copying a code block or paragraph from the terminal includes the visual padding as
  actual characters" (👍 304, 140 comments) ·
  [Cursor 58803](https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803)
  (forum, 2025-03-03, verified): "Now Cursor simply says it doesn't see anything. no matter what I do."
  (2 posts, 752 views) ·
  [HN 48795580](https://news.ycombinator.com/item?id=48795580) (hn, verified): "This is so helpful, thanks for
  open sourcing this, saves me having to copy paste from browser console to my coding agent." (6 points,
  2 comments) ·
  [claude-code #16592](https://github.com/anthropics/claude-code/issues/16592) (github-issue, 2026-01-07,
  verified): "a single session accumulated ~7MB of base64 image data across tool results" and "Screenshots:
  6,988 KB (86.3%)" of an 8 MB transcript (👍 14, 8 comments).

### The feature

A **Copy for agent** action that assembles one clipboard payload and copies it in a single click. The
payload is a short, fixed instruction block — the "Suggested prompt" that currently lives only in
`docs/report-format.md` — followed by the report body rendered at a level chosen for an agent, followed by
a short footer that names the evidence files that are *not* inlined (the screenshots), so the agent knows
to open them. The action defaults to **L2 (Compact)** rather than L1, because the evidence for the cost
half of the pain is that a full-fidelity session is 86 % screenshots and pastes into an agent's context
window with nothing the reader can remove. The prompt template lives in code, not in a docs file, so it
ships with the extension and can be improved without asking users to re-read a wiki.

The differentiator against the competitors is not the button — a dozen extensions ship one, which is why
P15 exists as a constraint node — it is *what is on the clipboard*: a report whose evidence was assembled
by a deterministic recorder, with the file list, the request bodies and the error links already joined on
one clock, at a token count the user was shown before copying.

### UX

It lives in **two** places, because the user is in two places when this pain hits:

1. **Side panel → Export panel** (`entrypoints/sidepanel/components/ExportPanel.tsx`), directly under the
   existing verbosity radio group and **above** the "Download .zip" button. The button reads
   **"Copy for agent"** and shows the token estimate next to it, e.g. `Copy for agent · ~12k tokens`. The
   token figure is not new — `estimateForLevels()` in `lib/export/bundle.ts:497` already computes it per
   level and the ExportPanel already renders it for the level radios — so the button reuses the same
   number the user is already looking at.
2. **The report viewer** (`entrypoints/report/main.ts`), in the sticky header next to the existing
   "Download" button, because that is where a user lands when a recording stops.

Clicks to value: **1 click** after the level is chosen (the level radio already exists, and the button
copies at the currently selected level). Nothing else is required — no dialog, no config, no file
dialog. On success the button swaps to a 2-second "Copied" state, mirroring the existing
"Downloaded" affordance in `ExportPanel.tsx`.

The payload is text only, so it pastes into any agent chat, any editor, any terminal.

### Files likely touched

| File | Change |
|---|---|
| `lib/export/agent-prompt.ts` | **New.** Pure module: the instruction template + a `buildAgentPayload()` that joins the prompt, the report body and the evidence-file footer. No chrome/DOM access, mirroring the contract of `lib/export/markdown.ts` and `lib/export/trimmer.ts`. |
| `lib/export/agent-prompt.test.ts` | **New.** Unit tests. |
| `entrypoints/sidepanel/components/ExportPanel.tsx` | Add the "Copy for agent" button, the token figure, and the copied/working states. |
| `entrypoints/report/main.ts` | Add the same button to the report-viewer header. |
| `lib/export/markdown.ts` | Read-only, but it is where `renderReport()` lives — the payload builder calls it rather than re-implementing it. No change expected. |
| `entrypoints/sidepanel/styles.css` | Button styling, reusing the existing `btn` / `btn--primary` classes. |
| `docs/report-format.md` | Update to say the prompt now ships with the extension and is included in the copy action. |

`lib/export/bundle.ts` needs no change: `buildBundle()` already returns `{ path: 'report.md', text }` and
`estimateForLevels()` already returns per-level token counts.

### How to test it

**Unit (vitest)** — `lib/export/agent-prompt.test.ts`:
- The payload contains the instruction block and the report body, in that order.
- The payload names every included screenshot file, using the same zip-relative path that
  `lib/export/bundle.ts:planAssetPaths()` assigns (`screenshots/001-0012.jpg`), so the agent's instruction
  and the file on disk agree.
- The payload's token estimate matches `estimateTokens()` on the same text — the number shown next to the
  button and the number in the payload are the same number.
- The default level is L2, and the payload changes when the level changes.
- The footer is omitted when the session has no screenshots (no dangling "see files" line).
- A session whose events were trimmed does not produce a footer naming a file that is not in the bundle.

**E2E (Playwright)** — extend `e2e/record-export.spec.ts`:
- Record a short session, open the report viewer, click "Copy for agent", and assert the clipboard
  contains the prompt and the report body. `e2e/support.ts` already sets up a session; the harness needs
  clipboard permission granted for the extension origin.
- Change the level radio and assert the copied payload changes accordingly.

**Not tested by E2E**: the token estimate's arithmetic (already covered by `lib/export/tokens.test.ts`).

### Risks

- **The clipboard is a plain-text channel; the screenshots do not travel with it.** This is the honest
  limit of this feature and it is exactly why feature 2 exists. Mitigation: the payload's footer names the
  files, so an agent with a filesystem can open them.
- **Copying a large payload is not free.** At L0 the report can be megabytes. Mitigation: default L2 and
  show the estimate; do not auto-downgrade below what the user selected.
- **`navigator.clipboard.writeText` requires a user gesture and a focused document.** The action is a real
  click on a real button, so the gesture requirement is satisfied; but the side panel can lose focus if the
  user clicks away. Mitigation: the copy runs synchronously inside the click handler, and the failure path
  shows the report in a selectable `<textarea>` so the user can copy manually.
- **The payload may contain secrets.** The extension already redacts, and the five open redaction PRs
  (#42, #44, #38, #37, #31) harden it further, but a "copy everything" action widens the blast radius of
  any redaction gap. Mitigation: the copy action copies the *already-trimmed* report, never raw events, and
  never the raw asset bytes.

### Open PRs this must not duplicate

**None directly.** The closest is **#43 (Copy as cURL)**, which copies a *request* as a cURL command, not
the report — different artifact, different action, and this feature must not absorb it. **#48 (labels and
assignees when filing)** touches the GitHub-issue path, not the clipboard. **#29 (browser, OS, viewport in
report)**, **#40 (redirect hops as requests)** and **#47 (per-repo transcription vocabulary)** change *what
is in* the report, so this feature must be written to render whatever the current report contains rather
than hard-coding sections. **#42 / #37 / #31** change redaction inside the report.

---

## Feature 2 — Evidence index: tell the agent which files to open

### The user and their pain

The extension captures the evidence; the agent cannot reach it. `report.md` renders a screenshot as a
markdown image link — `![ctx](screenshots/001-0012.jpg)` (`lib/export/markdown.ts:368-376`) — and a
network body as a fenced block or a path reference. When that report is pasted **as text** into an agent
chat, every screenshot becomes a dead reference: the agent is told a file exists but has no way to open
it, and no way to know that the visual state at the moment of failure is the one thing it needed.

That gap is the exact failure users report. On the agent side: "Claude can't visually verify frontend
work: no screenshots, no clicking through a flow, no reading console errors from a rendered page"
([claude-code #75632](https://github.com/anthropics/claude-code/issues/75632), 👍 8, 21 comments) and "I end
up reviewing the PR blind". On the harness side, the delivery route is broken in four different ways at
once: clipboard paste fails outright ([Cursor 176096](https://forum.cursor.com/t/ctrl-v-image-paste-always-fails-on-macos-execfile-missing-encodingbuffer/176096),
"Ctrl+V doesn't attach images from the clipboard right now, even though the screenshot is on the
clipboard"), the full-resolution bytes are silently dropped by a remote connector
([Cursor 177756](https://forum.cursor.com/t/grok-bot-drops-mcp-typeimage-bytes-from-remote-tool-results-full-res-screenshots-unsavable/177756),
"Only the text content part reaches the agent"), the image is replaced by a placeholder
([cline #9902](https://github.com/cline/cline/issues/9902), "url field must be a base64-encoded image"), and
oversized images poison the whole conversation
([claude-code #13480](https://github.com/anthropics/claude-code/issues/13480), 👍 90, 111 comments: "the
oversized image remains in the conversation history, causing all subsequent requests to fail with the same
error - even plain text messages with no images attached").

- **Nodes:** P05 (the images), P01 (the browser evidence the agent cannot see), P02 (the copy path).
- **Evidence:** [claude-code #13480](https://github.com/anthropics/claude-code/issues/13480) (github-issue,
  2025-12-09, verified) (👍 90, 111 comments) ·
  [copilot-cli #2675](https://github.com/github/copilot-cli/issues/2675) (github-issue, 2026-04-13, verified):
  "Currently, sharing visual context requires either taking a screenshot via Chrome DevTools integration
  (only works for browser pages) or saving an image to a file and referencing it with @" (👍 7, 3 comments,
  open) ·
  [Cursor 176096](https://forum.cursor.com/t/ctrl-v-image-paste-always-fails-on-macos-execfile-missing-encodingbuffer/176096)
  (forum, 2026-10-25, verified) (7 posts, 188 views) ·
  [Cursor 177756](https://forum.cursor.com/t/grok-bot-drops-mcp-typeimage-bytes-from-remote-tool-results-full-res-screenshots-unsavable/177756)
  (forum, 2026-11-08, verified) (2 posts, 44 views) ·
  [cline #9902](https://github.com/cline/cline/issues/9902) (github-issue, 2026-03-20, verified) (👍 4,
  5 comments) ·
  [copilot-cli #1241](https://github.com/github/copilot-cli/issues/1241) (github-issue, 2026-02-01, verified):
  "When I paste from a clipboard from things coming from SnagIt or Snipping Tool, nothing happens...no
  feedback, nada." (👍 7, closed 2026-04-07 as fixed).

### The feature

An **Evidence index**: a short section at the top of `report.md` — and in the copy-for-agent payload —
that enumerates the evidence the agent should look at, and says where it is. Not a file listing; a
*task list for the agent*. Three parts:

1. **A count and a kind breakdown** — "12 screenshots, 3 video clips, 14 network requests, 2 console
   errors" — so the agent knows the shape of the evidence before it reads anything.
2. **A "look here first" list** — the handful of frames that matter: the screenshot taken at the error, the
   annotation the human drew, the screenshot that immediately precedes the failing request. These are
   already identifiable in the event stream: `lib/export/trimmer.ts:thinScreenshots()` keeps
   `annotation` and `error` triggers, and the error event carries `linkedRequestId`, so the report can name
   the exact frame that sits next to the exact failure.
3. **A path list with a stated availability** — for each entry, the zip-relative path and whether the
   asset survived the current trim level. At L3 `thinScreenshots('manifest-only')` drops every screenshot
   event, so the index must say "screenshot at 00:12 not included at this level; re-export at L1 to see it"
   rather than naming a file that is not in the zip.

The last point is what makes this more than a manifest: `MANIFEST.md` already exists and lists every
included asset (`lib/export/markdown.ts:renderManifest()`), but it is a passive index in a separate file
that an agent may never open. This index is in the report, at the top, in agent-directed language.

### UX

It lives **inside the report**, so it needs no new surface. The user sees it:

- **In `report.md`** — a `## Evidence index` section between the header and `## Timeline`, above the
  existing content. The user reads it as a summary of what was captured; the agent reads it as a work
  list.
- **In the report viewer** (`entrypoints/report/main.ts`) — a small summary card above the timeline, so
  the human sees "what did we capture" without scrolling. This is a natural fit: the viewer already has
  the `shotBlock` / `annotationBlock` / `netGroup` builders.
- **In the copy-for-agent payload** (feature 1) — the index is the part that survives at every level, so
  the agent always knows there is evidence it has not seen.

Clicks to value: **0**. It is a rendering change to an existing artifact. The only user-visible choice is
whether to include it, which does not need one.

### Files likely touched

| File | Change |
|---|---|
| `lib/export/evidence-index.ts` | **New.** Pure module: `renderEvidenceIndex({ events, assets, level, assetPath })` returning the Markdown section. Sibling of `lib/export/markdown.ts`; no chrome/DOM access. |
| `lib/export/evidence-index.test.ts` | **New.** Unit tests. |
| `lib/export/markdown.ts` | Call the new renderer in `renderReport()` and insert the section after `renderHeader()`. |
| `lib/export/markdown.test.ts` | Extend for the new section. |
| `lib/export/bundle.ts` | No change expected — `renderReport()` is already called from `buildBundle()` and `estimateForLevels()`. |
| `entrypoints/report/main.ts` | Optional: a summary card above the timeline. |
| `lib/export/report-html.ts` | If the HTML viewer gets the card. |

### How to test it

**Unit (vitest)** — `lib/export/evidence-index.test.ts`:
- The index lists every included asset with its zip-relative path, and the paths match the ones
  `lib/export/bundle.ts:planAssetPaths()` assigns.
- The index names the screenshot at the error trigger and the annotation screenshot first.
- At L3 (`thinScreenshots('manifest-only')`) the index reports the screenshot as *not included* and says
  which level would include it — it never names a path that is absent from the bundle.
- The index never names an asset whose file is not in the zip (the "the report never points at a file that
  is not there" invariant the docs already state).
- An empty session renders a valid empty state rather than an empty heading.
- The index is stable under `applyLevel()` — running it on trimmed events gives the same result as running
  it on the untrimmed ones at the same level.

**E2E (Playwright)** — extend `e2e/record-export.spec.ts`:
- Record a session with a console error, export at L1, unzip the downloaded file and assert `report.md`
  contains an Evidence index section naming the error screenshot.
- Export at L3 and assert the same screenshot is reported as not included.

### Risks

- **This is a rendering change to the artifact every other feature depends on.** `report.md` is consumed by
  the hosted report, the GitHub issue body, the HTML viewer and the copy action. Mitigation: the new section
  is additive and comes first; every existing consumer that greps for `## Timeline` still finds it.
  `lib/export/markdown.test.ts` and `lib/export/bundle.integration.test.ts` are the regression net.
- **It is a "file list", which sounds like `MANIFEST.md`.** The risk of overlap is real; the justification
  is that `MANIFEST.md` is exhaustive and passive, while this is ranked and agent-directed, and it lives
  where the agent actually reads. If the maintainers prefer one index, the cheaper version is to put this
  content *at the top of `MANIFEST.md`* and drop the separate section.
- **Naming a file that is not in the bundle is the one failure that would actively mislead an agent.** This
  is the invariant the test suite must enforce hardest, and it is why the index takes the same
  `assetPath(assetId)` callback that `renderReport()` already uses — it cannot name a path the bundle does
  not contain.
- **It adds tokens.** The index is short (a bounded number of entries, never a full manifest) and the
  count/breakdown is already computed by `countByType()` in `lib/export/bundle.ts`. Mitigation: cap the
  "look here first" list at a fixed number of entries.

### Open PRs this must not duplicate

**None directly.** It must not re-implement **#32 (HAR export)**, which produces a HAR artifact for the
network evidence — this index *points at* the evidence, it does not produce a new format. **#39 (request
and trace IDs of failed requests)** adds identifiers that make the index's error↔request pairing more
precise, so this feature must read those IDs if present but must not add them. **#41 (storage snapshot)** and
**#49 (group recordings of the same error)** change what is in the bundle. **#29 (browser, OS, viewport in
report)** adds a header line the index can surface but must not duplicate.

---

## Feature 3 — Deterministic verdict: pass / fail / unverified, plus not-a-bug

### The user and their pain

The complaint from people who run QA agents is not "the agent missed bugs". It is that **the agent reports
bugs it cannot reproduce, and the report is not auditable**, so reviewers stop reading after the first noisy
finding. The community's converged answer is a third state — "I can't tell" — plus the expectation that
every finding carries its steps, its evidence and an honest confidence.

The same complaint shows up on the developer side, in a sharper form: the agent invents evidence. A vendor
agent attached screenshots that "look nothing like my app and give false impressions that this a fully
working and complete solution!"
([vscode-pull-request-github #7770](https://github.com/Microsoft/vscode-pull-request-github/issues/7770),
👍 1, 9 comments, closed as completed 2026-04-08). That is the same failure as a false completion claim
(P13) and as "nobody can prove the fix worked" (P06): a report that looks settled but shows no work.

Session Recorder is well placed here precisely because it has **no LLM in the loop**. Its verdict would be
computed from the recorded event stream — a failed request with `status >= 400` or `failed: true`, an
`error` event, a `linkedRequestId` joining them — so it is deterministic, reproducible and re-derivable.
A competitor with an LLM in the loop can only guess; the recorder can show its work.

- **Nodes:** P16 (pick 31, novelty 4 — the highest in the set), P06, P13, P11.
- **Evidence:** [HN 50339913](https://news.ycombinator.com/item?id=50339913) (hn, verified, 168 points,
  44 top-level comments): "outputs need to be auditable, not just accurate. Pass/fail/uncertain per check,
  evidence link, explicit confidence. Anything that can't show its work is asking the reader to accept
  vibes" · "The key missing details are (a) how they de-duplicate reports, (b) what evidence they attach
  (steps + screenshots/video + DOM/locator context), and (c) determinism/repro" ·
  [vscode-pull-request-github #7770](https://github.com/Microsoft/vscode-pull-request-github/issues/7770)
  (github-issue, 2025-09-07, verified): "The screenshots are fake, look nothing like my app and give false
  impressions that this a fully working and complete solution!" (👍 1, 9 comments) ·
  [clipy-mcp](https://github.com/clipy-recorder/clipy-mcp) (github-repo, verified): the closest shipped
  implementation — markers carry an explicit three-valued verdict, "Renders with a verdict glyph (✓ pass,
  ✗ failure that can abort via failMode, ⚠ unverified — never a silent pass)", and it keeps the two
  provenances apart: "Clipy vouches only that you said it — not that it verified it" (5 stars, 2 forks).

### The feature

A **deterministic verdict layer** in the report. Two pieces:

1. **A per-finding verdict.** Each *finding* is a concrete, recorded anomaly, not a guess. The extension
   already knows what those are, and the trimmer already knows which ones matter: `lib/export/trimmer.ts:isAnomalous()`
   treats `failed === true` or `status >= 400` as anomalous, `dedupErrors()` and `dedupConsole()` collapse
   repeats, and `dropBodiesExceptErrors()` keeps the body of any request linked to an error. So each
   finding can carry:
   - **verdict** — `fail` when the recording contains a hard signal (a failed request, an `error` event, a
     console error, an unhandled rejection); `pass` when the recording contains the events that the signal
     would have produced and does not (a request to the endpoint the user was working with returned 2xx);
     `unverified` when the recording does not contain enough to decide — the request was never captured, the
     body was trimmed at this level, or the failure happened outside the recorded tab.
   - **evidence** — the `[mm:ss]` timestamp, the request id and the path of the screenshot at that moment.
   - **confidence** — a fixed enum, not a float: `high` (a hard signal, reproducible from the event stream),
     `medium` (a soft signal such as a console warning), `low` (a heuristic). A deterministic rule, not a
     number an LLM produced.
2. **A not-a-bug state.** A reporter who knows the behaviour is intentional can mark a finding as
   *not a bug*, with a one-line reason. That state travels with the report into `session.json`, so the next
   agent run does not re-flag it. This is the "de-duplication" the HN thread asks for, and it is the thing
   the extension can do that a live-browser agent cannot: it knows what the user *said*.

The payload is deliberately small and machine-readable: one `verdict` object per finding in
`session.json`, and a compact `## Findings` table in `report.md` with the verdict glyph, the timestamp,
the one-line summary and the evidence links.

### UX

It lives in **two** places:

1. **In the report**, as a `## Findings` section directly after the Evidence index (feature 2) and before
   the timeline. The reporter reads it as a summary; the agent reads it as a work list with a verdict
   attached to each item.
2. **In the side panel**, as a small badge next to the session row in `SessionList`: the count of findings
   and the worst verdict among them (`3 findings · 1 unverified`). This is what makes "I can't tell"
   visible at triage time — the point where a reviewer decides whether to read the report at all.

**Not-a-bug** is set from the report viewer: clicking a finding's verdict cycles it
(`fail → pass → unverified → not-a-bug`), because the reporter is looking at the evidence when they make
that call. The change writes a `session-note` event with `kind: 'info'` carrying the finding's id and the
new verdict — `SessionNotePayload` (`lib/session/types.ts:455-458`) already has a `kind` field with
`'rehydrate' | 'detach' | 'info' | 'warning'`, and `session-note` events are protected from trimming, so
the note survives at every level.

Clicks to value: **1 click** to cycle a verdict, **0** to read the findings.

### Files likely touched

| File | Change |
|---|---|
| `lib/export/verdict.ts` | **New.** Pure module: `verdictFor(finding, events, level)` → `{ verdict, confidence, evidence }`, and `renderFindings()` for the Markdown table. No chrome/DOM access. |
| `lib/export/verdict.test.ts` | **New.** Unit tests. |
| `lib/session/types.ts` | Extend `SessionNotePayload` with an optional `findingId` and `verdict` so a not-a-bug note is machine-readable. |
| `lib/export/markdown.ts` | Render the `## Findings` section. |
| `entrypoints/report/main.ts` | Render each finding as a clickable verdict control; write the note via the existing event path. |
| `entrypoints/sidepanel/components/SessionList.tsx` | The findings badge. |
| `lib/storage/index.ts` | Only if the verdict cycle needs a dedicated write path. |
| `lib/export/trimmer.ts` | Read-only — `isAnomalous()` is the natural source of truth for what counts as a finding and should be **exported** rather than duplicated. |

### How to test it

**Unit (vitest)** — `lib/export/verdict.test.ts`:
- A session with a request that returned 500 produces a `fail` verdict with `high` confidence.
- A session with a 2xx request to the endpoint the user was working on produces `pass`.
- A session where the failing request was not captured produces `unverified` — **never** a silent `pass`.
  This is the invariant the whole feature exists to protect ("a guessed pass is worse than no test").
- A finding whose request body was trimmed at the current level is `unverified` with an explanation that
  names the level to re-export at.
- The verdict is deterministic: the same events at the same level always produce the same verdict.
- A not-a-bug note suppresses the finding in the next render, and the suppression survives at every trim
  level (the note is a protected event).
- The `## Findings` table contains an evidence link for every `fail` finding — a finding never appears
  without its evidence, which is the "anything that can't show its work is asking the reader to accept
  vibes" requirement.

**E2E (Playwright)** — new `e2e/verdicts.spec.ts`:
- Record a session against a page that returns a 500, stop, open the report viewer, and assert a finding
  appears with the `fail` glyph.
- Click the finding's verdict twice to reach not-a-bug, reload the report tab, and assert the finding is
  marked not-a-bug and the badge count in the side panel drops.

### Risks

- **This is the largest of the three features.** It is the smallest in novelty terms (novelty 4 means
  nothing covers it) but the biggest in surface area: a new pure module, a type change, two UI surfaces
  and a write path. If it must fit in "a few hundred lines", **ship the read-only half first** — the
  verdict computation and the `## Findings` table — and leave the interactive not-a-bug cycle for a
  follow-up PR. The read-only half alone still answers "is this a bug, and on what evidence".
- **A wrong verdict is worse than no verdict.** If the extension says `pass` for something that was
  broken, it has actively misled the agent. Mitigation: the default for insufficient evidence is
  `unverified`, never `pass`; and `unverified` is a distinct, prominent state, not a footnote.
- **"Finding" needs a definition, and the definition will be argued about.** The extension has many
  anomaly-shaped events. Mitigation: derive findings from the existing `isAnomalous()` notion plus `error`
  events, keep the rule in one place, and document it. A finding is "an event the extension can point at
  with evidence", not "something that looks wrong".
- **A not-a-bug note is a suppression, and suppressions are dangerous** — they can hide a real regression
  later. Mitigation: keep the note in the event stream as a first-class, protected, timestamped record
  (never a hidden flag), and render it in the report so the suppression is visible to anyone reading.
- **Competitors are close on this.** Clipy ships three-valued verdict glyphs. It is a 5-star project in a
  different product with a cloud account requirement, so the differentiator is the offline, deterministic,
  no-account path — but a feature that only claims "we also have three values" will not read as novel.

### Open PRs this must not duplicate

**None directly, but three are prerequisites-adjacent and must be read first:**

- **#39 (request and trace IDs of failed requests)** — adds the identifiers a finding's evidence line
  needs. This feature must *consume* those ids, not add them.
- **#41 (storage snapshot)** — changes the event payload shape; the verdict rules read event payloads and
  must be written to tolerate it.
- **#49 (group recordings of the same error)** — is itself a de-duplication mechanism and therefore
  overlaps conceptually with the "de-duplication" the HN thread asks for. This feature must not
  re-implement grouping; it should produce a verdict **per finding**, and let #49 group findings.

**Must not duplicate: #22 (Playwright repro test in ZIP)** — closed by its author, and it targeted the
related P11 "a recording is not a reproduction" pain. This feature produces a *verdict*, not a repro
script.

---

## What these three have in common

They are the three highest-`pick_score` nodes **after** removing P05's already-shipped half, and they
compose into one story: the extension records the evidence (it already does), it tells the agent what
evidence exists and where it is (feature 2), it hands that over in one click with the agent's own
instructions attached (feature 1), and it says honestly whether each item is a defect, a non-defect or
undetermined (feature 3).

None of them re-implements a live browser, none of them needs an LLM, and none of them touches the
crowded topics the context notes warn about — export paging, SARIF, wait-for-review, fail-on gates, new
`agent install` editors, or the five existing redaction PRs.

**Order of work:** feature 1 first (smallest, one button, unblocks the user immediately), feature 2 second
(it changes the report artifact and so must land after feature 1 has settled the payload shape), feature 3
third (largest surface, and the read-only half is the right first cut).
