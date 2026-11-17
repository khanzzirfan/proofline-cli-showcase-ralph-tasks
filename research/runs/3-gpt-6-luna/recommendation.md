# Recommendation: top 3 small feature specs

Ranked by `pick_score` in `ranking.json`. These are three small, independent handoff improvements, not a proposal to add live browser control. Session Recorder already captures screenshots, annotations, narration, video, console/network evidence and creates a ZIP with `report.md`, `session.json` and `MANIFEST.md`. Its current docs tell people to unzip and hand the report to an agent, but its export UI has no agent-specific action.

## 1. Copy an agent handoff prompt

**Pain and user:** Developers, QA and agent users lose time moving browser evidence to a coding agent and explaining how to use it (P01, P02). See [P01](nodes/P01-agent-cant-see-live-browser.md) and [P02](nodes/P02-browser-evidence-copy-paste.md); evidence includes the 76-reaction browser-sharing request and the HN report of console copy/paste friction.

**Feature:** Add a `Copy agent prompt` action beside the ZIP download. It copies a concise, static prompt telling the agent that the adjacent downloaded ZIP contains `report.md`, `MANIFEST.md`, screenshots and machine-readable events; instruct it to inspect the report and referenced assets, use annotations/narration as reporter intent, and not assume live browser access. Do not copy recorded data, network bodies or secrets to the clipboard. This is a small explicit handoff, not an agent integration.

**UX:** In the side-panel Export panel, choose the verbosity level, download the ZIP, then click `Copy agent prompt` (two actions after choosing the level). Show a brief copied status and retain the existing Download and Share actions. Clearly state that the prompt does not contain the report or attachments; the user still supplies the downloaded folder to their agent.

**Likely files:** `entrypoints/sidepanel/components/ExportPanel.tsx`, `entrypoints/sidepanel/styles.css`, `docs/report-format.md`; tests in a focused `ExportPanel` test if a component-test pattern exists, otherwise a pure helper under `lib/export/` with a Vitest test. `e2e/record-export.spec.ts` is the likely Playwright coverage point.

**Test plan:** Unit-test exact prompt contents, clipboard text, and the success state; assert that no session events, report content, URLs or credentials are interpolated. Playwright: open a recorded session’s Export panel, click the action, verify clipboard prompt and status, and confirm the existing ZIP download still works.

**Risks:** Clipboard permission or API failure; a prompt that promises files not actually present; users may think the prompt itself contains evidence. Keep the prompt generic, include a clear “attach/unzip the ZIP” instruction, and test that the mentioned archive layout matches `lib/export/bundle.ts`.

**Open PRs not to duplicate:** No direct overlap identified. Keep this separate from #48 (issue labels/assignees), #32 (HAR export), #43 (Copy as cURL), #21 (keyboard shortcuts), and the redaction PRs #31, #37, #38, #42. Do not add issue filing or new network-export behavior.

## 2. Put a short agent-use guide inside `report.md`

**Pain and user:** Developers using CLI/cloud agents and reviewers can receive the recording but may not know which assets to inspect or what the report can and cannot prove (P01, P02, P09). See [P01](nodes/P01-agent-cant-see-live-browser.md), [P02](nodes/P02-browser-evidence-copy-paste.md), and [P09](nodes/P09-visual-input-coverage-is-not-universal.md). The report format already has a manifest and screenshot references, but visual inputs are not supported uniformly across agents; video-specific consumption pain was not verified.

**Feature:** Add a compact, deterministic `Using this evidence` section to the generated Markdown report. Explain that the report timeline is primary, screenshot paths and timestamps point to visual evidence, `MANIFEST.md` lists included assets, and `session.json` is available for structured event data. Tell the agent to inspect only included assets and to ask for missing context rather than infer live state. Do not add video conversion, new capture or agent-specific formats.

**UX:** No additional click: the guide appears near the top of `report.md` in the existing ZIP. An agent or person sees it when opening the file already referenced in the extension’s README. Keep it short so it does not bury the captured timeline.

**Likely files:** `lib/export/markdown.ts`, `lib/export/markdown.test.ts`, `docs/report-format.md`, and possibly `lib/export/bundle.integration.test.ts` to verify the section survives all verbosity levels.

**Test plan:** Vitest assertions for the exact guidance and for no broken asset-path promises; integration-test that the section exists at Full, Standard, Compact and Minimal and that the referenced manifest and assets are included when applicable. Playwright: export a recording at multiple levels and inspect the opened/downloaded report for the guide and valid local links.

**Risks:** Duplicating or contradicting current `docs/report-format.md`; overstating screenshot/video availability at trimmed levels; verbosity increase. Keep wording aligned with the manifest and current trimming rules. The research did not verify a separate agent video-consumption problem, so this proposal improves navigation only.

**Open PRs not to duplicate:** No direct overlap identified. Avoid #32 and #43 (network-export formats), #29 (browser/OS/viewport metadata), #23 (docs bundle), #21 (keyboard shortcuts), and #41 (storage snapshot). Do not add image/video recording features already present.

## 3. Add a post-fix verification checklist to the agent prompt

**Pain and user:** Developers, QA and product reviewers cannot infer that a UI fix worked from a code change or passing test alone; the agent needs the reporter’s observed failure and intended behavior as a validation target (P07, supported by P12). See [P07](nodes/P07-fix-needs-visual-verification.md) and [P12](nodes/P12-automated-repro-needs-intended-behavior.md). The strongest source requests actual rendered-page verification; a separate HN comment notes that automated exploration needs explicit assertions and acceptance criteria.

**Feature:** Extend the copied prompt from feature 1 with a short, fixed verification checklist: identify the recorded failing workflow and expected/observed behavior in annotations, notes or narration; reproduce it in the project when possible; make the change; rerun the same flow; report what was checked and any unverified steps; attach before/after screenshots only if the agent’s environment supports it. This does not create a Playwright script or claim that the extension can verify a later fix.

**UX:** Included in the same `Copy agent prompt` action, with no additional click. The prompt must distinguish recorded evidence from the agent’s post-change results and avoid inventing expected behavior if none was recorded.

**Likely files:** `entrypoints/sidepanel/components/ExportPanel.tsx`, the shared prompt helper/test proposed in feature 1, and `e2e/record-export.spec.ts`. If feature 1 is not selected, this can be a small independent `Verify the fix` prompt action, but combining the two keeps UI surface and tests smaller.

**Test plan:** Unit-test checklist text and ensure it requires explicit reporting of failed/unavailable checks without claiming success. Include fixture cases with and without annotations/notes. Playwright: copy the prompt from a sample recording and verify the checklist includes the captured-intent instruction and the caveat about unavailable browser access.

**Risks:** The prompt cannot make a cloud agent run a browser; vague notes cannot become reliable acceptance criteria; this may duplicate feature 1 if implemented separately. Keep it as prompt text only and bundle with feature 1 if the team chooses that PR.

**Open PRs not to duplicate:** No direct overlap identified. Do not add an executable reproduction test or ZIP Playwright script, which would approach closed-by-author #22. Avoid #29 (environment metadata), #33 (E2E navigation race fix), and #48 (issue filing labels/assignees). The verification checklist should not create a new browser automation integration.

## Scope and selection

All three recommendations target transfer and interpretation of evidence already captured. The highest-confidence single PR is feature 1 combined with feature 3’s verification checklist: one prompt helper, one export-panel action, focused unit tests and a Playwright check. Feature 2 is a separate alternative if product prefers guidance embedded in the artifact over clipboard UX. Do not pursue a new local MCP bridge or video-analysis feature based on this evidence set.
