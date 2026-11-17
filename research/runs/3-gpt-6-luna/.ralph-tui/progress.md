# Ralph Progress Log

This file tracks progress across iterations. Agents update this file
after each iteration and it's included in prompts for context.

## Codebase Patterns (Study These First)

- Keep pure report/bundle behavior in `lib/export/` with Vitest coverage; test the side-panel user flow in `e2e/record-export.spec.ts`.

---

## 2026-11-16 - US-003
- Reopened all unique URLs cited in node Evidence sections and marked the four title-only Cursor forum pages unverified.
- Kept affected P05/P06 partly verified because their main claims have verified GitHub or vendor sources; changed P06’s fix request to cite verified structured-browser guidance.
- Files changed: `sources.md`, `nodes/P05-browser-tools-connection-fragile.md`, `nodes/P06-browser-network-output-hard-to-consume.md`, `nodes/P09-visual-input-coverage-is-not-universal.md`, `nodes/P10-secrets-in-copied-network-evidence.md`, `.ralph-tui/progress.md`.
- **Learnings:**
  - Cursor forum web fetch can return only the title; treat that as unverified rather than confirmation of the reported body.
  - A node may be partly verified when a verified source supports its main pain, but unverified-only recommendations should be rewritten or dropped.
---

## 2026-11-16 - US-004
- Scored all 13 nodes with the specified pain_score and pick_score formulas and ranked ties by node ID.
- Files changed: `ranking.md`, `ranking.json`, `.ralph-tui/progress.md`.
- **Learnings:**
  - A high pain score does not necessarily make a good small PR; novelty and smallness move privacy/MCP risks below feasible handoff ideas.
  - Keep source counts node-specific and do not count title-only forum pages as verified.
---

## 2026-11-16 - US-005
- Wrote the top-three Session Recorder feature specs and research method/counts summary, grounded in ranked nodes and verified extension paths.
- Files changed: `recommendation.md`, `run-summary.md`, `.ralph-tui/progress.md`.
- **Learnings:**
  - Export lives in `entrypoints/sidepanel/components/ExportPanel.tsx`; `lib/export/bundle.ts` and `lib/export/markdown.ts` build/render reports, with Vitest tests in `lib/export/` and Playwright coverage in `e2e/record-export.spec.ts`.
  - The ZIP already includes a manifest and visual assets; improve agent handoff and asset navigation instead of adding duplicate capture or video analysis.
  - Keep the open PR overlap list explicit; avoid adding duplicate issue-filing or network-export behavior.
---

