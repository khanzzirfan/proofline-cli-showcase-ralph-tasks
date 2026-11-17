# Ralph Progress Log

This file tracks progress across iterations. Agents update this file
after each iteration and it's included in prompts for context.

## Codebase Patterns (Study These First)

*Add reusable patterns discovered during development here.*

---


## 2026-11-17 - US-001
- Implemented `ProoflineClient.iterExportReviews(parameters, { maxPages })` in `src/index.ts`, right after `exportReviews`. Yields each `ExportPage`, follows `nextCursor` until null; only `query.cursor` changes; starts from `parameters.query.cursor`; repeated/seen cursor -> `protocol(...)`; exceeding maxPages (default 100, `integerLimit`) -> `paginationLimit(...)`; `exportReviews` errors propagate unchanged.
- Files changed: `src/index.ts`
- Quality gate: `pnpm lint && pnpm typecheck && pnpm build && pnpm test` pass (60/60 tests).
- **Learnings:**
  - Mirrors `iterReviews` loop shape (seen-set + `cursor` var); `parameters.query` is required for export (unlike list), so no optional chaining.
  - Tests import `dist/`, so run `pnpm build` before `pnpm test`.
---

## 2026-11-17 - US-002
- Added 6 tests (CSV + NDJSON multi-page, initial/opaque cursor byte-for-byte, repeated cursor (just-used and earlier), maxPages (exceeded + invalid 0), 403 on page 2 propagates as ProoflineError with no token in message/stack/JSON) plus an `exportPager` helper in `tests/http.test.mjs` after the existing export test.
- Files changed: `tests/http.test.mjs`
- Quality gate: lint, typecheck, build, test all pass (66/66, up from 60).
- **Mutation check:** removed the `seen.has(page.nextCursor)` condition in `iterExportReviews`, rebuilt, ran tests -> `not ok 25 - iterExportReviews rejects a repeated cursor` (65 pass / 1 fail). Restored `src/index.ts` and rebuilt; 66/66 pass.
- **Learnings:**
  - `page.nextCursor === cursor` alone catches an immediate repeat; only an A->B->A cycle exercises `seen`, so the test needs a 3-step chain.
  - macOS `sed -i` needs `-i ''`; a failed sed silently left the baseline 60/60 passing, so check the test count.
---

## 2026-11-17 - US-003
- Replaced the manual "repeat the call with the returned cursor" guidance and the trailing "Continue with query.cursor" comment in README "Review exports" with a `for await (const page of client.iterExportReviews(...))` example. Kept the single-page `exportReviews` paragraph. Notes `maxPages` (default 100, pagination limit error), the repeated-cursor protocol error, `query.cursor` as start point, and unchanged error propagation.
- Files changed: `README.md` (Review exports section only)
- Quality gate: lint, typecheck, build, test all pass (66/66).
- **Learnings:**
  - The README edit was a scripted slice between "To read subsequent pages" and "## MCP organization selection", so no other section could be touched; confirm with `git diff --stat README.md`.
---
