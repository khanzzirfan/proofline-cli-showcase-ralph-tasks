> Draft only, not submitted: seven open PRs already page through exports (see the README).

Title: Add iterExportReviews to page through review exports

## Who this helps

Engineers who pull organization review analytics into a warehouse, notebook or CI job with `exportReviews`. An export can span many pages, but `exportReviews` returns one page and the README asked callers to write the cursor loop themselves. `iterReviews` already pages the review list safely. Exports had nothing equivalent, and a plain `while (cursor)` loop never ends if the server repeats a cursor.

## What changed

`client.iterExportReviews(parameters, { maxPages })` is an async generator that yields each `ExportPage` in order and follows `nextCursor` until it is null.

```typescript
for await (const page of client.iterExportReviews({
  path: { org_id: organizationId, dataset: "reviews" },
  query: { from: "2026-10-01T00:00:00Z", to: "2026-10-25T00:00:00Z", format: "csv" },
})) {
  process.stdout.write(page.text);
}
```

- **Only the cursor changes.** Dataset, window, format and grouping are copied from the first call. An initial `query.cursor` is respected, and opaque cursors are sent back unchanged.
- **No infinite loops.** It throws the existing `invalid-response` protocol error when a cursor is repeated, seen earlier, or empty. `maxPages` defaults to 100 and is checked with `integerLimit`. Going over it throws the existing `pagination-limit` error.
- **Errors pass through.** Refusals and authorization failures from `exportReviews` propagate unchanged, and the token stays redacted.

## Decisions

- **It yields pages, not rows.** CSV pages each carry their own header, and callers often stream `page.text` straight to a file. Yielding rows would lose that and hide `datasetVersion` and `settledUntil`. Callers who want rows can use `page.rows`.
- **No `maxItems`.** Unlike `iterReviews`, page size is decided by the server and a page's rows are already decoded, so a page limit is the meaningful bound.
- **It reuses `iterReviews`' guards.** It uses the same error helpers and loop detection so both paginators fail the same way.
- **Scope is hand-written code only.** Only `src/index.ts`, `tests/http.test.mjs` and `README.md` changed. Nothing generated was touched, and `pnpm generate` produces no diff.

## Verification

- `pnpm generate && git diff --exit-code`, `pnpm lint`, `pnpm typecheck`, `node check-claims.mjs`, `pnpm build`, `pnpm test`: 66/66 pass. That is the 60 existing tests plus 6 new ones.
- The new tests run against the existing local mock server and cover:
  - CSV and NDJSON across several pages
  - an initial cursor and opaque cursors (`start/+=`, `opaque/+cursor=`) checked byte for byte in the request URL
  - a cursor repeated immediately, one repeated after an A→B→A cycle, and an empty continuation header
  - going over `maxPages` (and `maxPages: 0` rejected)
  - a 403 on page 2 that surfaces after page 1 was yielded, with no token in the message, stack or JSON
- Mutation check: removing the seen-cursor guard makes `iterExportReviews rejects a repeated cursor` fail (65/66). With the guard restored, 66/66 pass.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
