# PRD: iterExportReviews paginator for @proofline/sdk

You are working in a git worktree of github.com/prooflinedev/sdk-typescript (TypeScript, Node >=22, pnpm, Biome).

## Problem
`client.exportReviews()` in `src/index.ts` returns ONE page (`ExportPage` from `src/exports.ts`, with `nextCursor`).
The README tells users to hand-roll a cursor loop. `client.iterReviews()` already paginates the review list safely
(maxPages limit, seen-cursor loop detection, typed `protocol(...)` / `paginationLimit(...)` errors). Export consumers
get none of that, and a naive `while (cursor)` loop can spin forever if the server repeats a cursor.

Who it helps: engineers pulling organization review analytics (CSV/NDJSON) into a warehouse, notebook or CI job.

## Feature
`client.iterExportReviews(parameters: ExportParameters, options: { maxPages?: number } = {}): AsyncGenerator<ExportPage>`
yields each page in order, following `nextCursor` until it is null. Mirrors `iterReviews`:
- `maxPages` default 100, validated with `integerLimit`; exceeding it throws `paginationLimit(...)`.
- A `nextCursor` equal to the cursor just used, or already seen, throws `protocol(...)`.
- Starts from `parameters.query.cursor` when given. Dataset, window, format and grouping stay constant; only `cursor` changes.
- Opaque cursors are passed back byte-for-byte.
- Errors from `exportReviews` (refusals, tenant authorization failures) propagate unchanged.

## Guardrails (apply to every story)
1. Read `AGENTS.md` and `README.md` first.
2. Never commit, push, tag, publish, fork or open PRs. Never run `git push` or `gh`. The owner does that.
3. Edit only: `src/index.ts`, `src/exports.ts` (only if needed), `tests/http.test.mjs`, `README.md`.
   Never edit generated files: `src/operations.ts`, `src/schema.d.ts`, `openapi.public.json`, `generate.mjs`, `pnpm-lock.yaml`, `package.json`.
4. No new dependencies. Work offline; tests use the existing local mock-server helpers in `tests/http.test.mjs`.
5. Match the style of `iterReviews` and Biome formatting (`pnpm exec biome format --write src tests` is allowed).
6. Never log or expose the token; keep the existing redaction behaviour.
7. Tests import `dist/`, so ALWAYS run `pnpm build` before `pnpm test`. Baseline: 60/60 tests pass after a build.
8. Quality gate for every story: `pnpm lint && pnpm typecheck && pnpm build && pnpm test` all pass.
9. Record only real results in notes. Never invent test output.

## Stories

### US-001: Implement iterExportReviews
Steps:
1. Read `iterReviews`, `exportReviews` in `src/index.ts` and `decodeExport` / `ExportPage` in `src/exports.ts`.
2. Add `async *iterExportReviews(...)` directly after `exportReviews` in `ProoflineClient`.
3. Implement the behaviour listed under Feature.

### US-002: Tests for iterExportReviews
Steps:
1. Add tests in `tests/http.test.mjs` next to the existing export tests ("exports preserve CSV cells, opaque cursors and tenant authorization failures"), reusing their mock server helpers.
2. Cover: CSV two pages then end; NDJSON two pages then end; initial cursor respected and opaque cursor passed back exactly; repeated cursor throws; maxPages exceeded throws; a 403 on page 2 propagates as `ProoflineError` and its text does not contain the token.
3. Mutation check: temporarily remove the seen-cursor check, confirm a test fails, restore it, and record this in notes.

### US-003: README update
Steps:
1. In README "Review exports", keep the single-page `exportReviews` explanation.
2. Replace the "Continue with query.cursor" guidance with a short `for await (const page of client.iterExportReviews(...))` example, and note `maxPages` (default 100) and the repeated-cursor error.
3. Change no other README section.
