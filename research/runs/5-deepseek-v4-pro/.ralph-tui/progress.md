# Ralph Progress Log

This file tracks progress across iterations. Agents update this file
after each iteration and it's included in prompts for context.

## Codebase Patterns (Study These First)

- **Popularity-signal evidence scraping:** run GitHub `search/issues` (`sort=reactions`) and HN Algolia (`tags=story|comment`) in parallel `curl` calls against different hosts, save raw JSON under `raw/`, then parse with one `python3` heredoc to pull `number/title/reactions.total_count/comments` (GitHub) or `points/num_comments` (HN). Reddit `search.json` returns an HTML block page — use `web_search` with `allowed_domains: ["reddit.com"]` instead. Several repos are renamed: `getcursor/cursor` and `sst/opencode` return HTTP 422, `All-Hands-AI/OpenHands` → `OpenHands/OpenHands`.
- **Node evidence rule:** every node needs >= 2 `- http` evidence lines with a verbatim quote <= 30 words and a popularity signal (reactions/comments/points); record each URL once in `sources.md` with a status.
- **US-003 verification fallbacks:** the GitHub unauthenticated core API is rate-limited (60/hr) and gets exhausted by US-002's `search/issues` calls, so re-verify GitHub issues by fetching the issue HTML page (`github.com/<owner>/<repo>/issues/<n>`) and reading `<title>` (no rate limit). Verify HN comment-level quotes with `hn.algolia.com/api/v1/items/{id}` — read the full `text` (not just the 500-char story preview) AND the `children` tree, because comment quotes live under children and long story quotes sit past the 500-char mark.
- **US-004 ranking scoring:** the node files already carry the five rubric sub-scores; US-004 only derives `pain_score = 2f+2s` and `pick_score = 2f+2s+2fit+smallness+novelty` and writes `ranking.md` (two tables) + `ranking.json`. Validate with a `python3 -c` script that asserts the formulas, 15 unique ids, `pain_rank[0]`/`pick_rank[0]` equal the max-score node, and every node has `verified_sources >= 1` — this catches arithmetic, ordering and schema mistakes in one shot.

---

## 2026-11-17 - US-001
- What was implemented: Wrote `plan.md` with the search plan for this research run — 29 concrete queries across 7 source types (GitHub reactions, GitHub comments, GitHub repo discovery, Reddit top, HN Algolia points, web search, web fetch) and 6 hypotheses (H1-H6), including the required H6 on vision/video. Reads the "Read first" files (00-context-notes.md, extension README/PRODUCT/report-format/PLAN).
- Files changed: `plan.md` (new); `.ralph-tui/progress.md` (this entry).
- **Learnings:**
  - Patterns discovered: The notes' five candidate pains map cleanly to five hypotheses (H1-H5); H6 (vision/video) is the required sixth. Every API query must carry `-A "pain-research/1.0"` and pause ~2s between same-host calls.
  - Gotchas encountered: No plan.md existed yet, so this story started fresh. The PRD's "plan.md" is a research deliverable (a data file in OUTPUT_DIR), not a coding-implementation plan, so no plan-mode review is needed.

---

## 2026-11-17 - US-002
- What was implemented: Ran the searches (GitHub `search/issues` by reactions, HN Algolia, web search, web fetch) and wrote 15 node files (`nodes/P01`–`P15`) plus `sources.md`. Covered 15 popular places. Collected verbatim, dated quotes with popularity signals (reactions, points, comments).
- Files changed: `nodes/P01..P15-*.md` (15 new), `sources.md` (new), `raw/*.json` (search API responses), `.ralph-tui/progress.md` (this entry).
- **Learnings:**
  - Patterns discovered: The strongest, most-defensible feature gap is turning the recorded tab video + narration + clicks into an agent-readable keyframe timeline (node P08, top pick_score 34) — high fit because the extension already records video/transcript/clicks, high novelty because no open PR touches it. Second/third picks: one-click "copy for coding agent" (P02) and emitting the annotated element's selector/text next to screenshots (P09).
  - Gotchas encountered: Reddit `search.json` is blocked (returns HTML, not JSON) — must fall back to `web_search` with `allowed_domains:["reddit.com"]`, which still returned only subreddit home pages. Three repos are renamed (`getcursor/cursor`, `sst/opencode`, `All-Hands-AI/OpenHands` → `OpenHands/OpenHands`) and return HTTP 422 on issue search. Cursor forum pages render only their title through `web_fetch` (Discourse body not extracted), so only the title is citable verbatim. Novel pains (not in notes section 5): P05 fabricated screenshots, P09 screenshot ambiguity, P10 token cost, P11 PR visual review, P12 vague reports, P13 auth/env gap, P14 state-dependent repro, P15 image context-poisoning.

---

## 2026-11-17 - US-003
- What was implemented: Independently re-verified all 25 cited sources. 9 web/blog/forum/docs URLs return HTTP 200; 12 GitHub issues confirmed via HTML pages (HTTP 200 + `<title>` matches, since the core API returned 403 rate-limit); 4 HN items confirmed via Algolia `items/{id}` with quotes verbatim. Cross-checked every node URL against `sources.md` (exact 1:1 match). Confirmed all 15 nodes carry `status: verified`, none leans on unverified/dropped sources, no fabricated quotes, and no duplicate nodes to merge. `sources.md` counts (verified: 25, unverified: 0, dropped: 3) are accurate — no deliverable files needed changing.
- Files changed: `.ralph-tui/progress.md` (this entry + a reusable US-003 pattern in Codebase Patterns). No node/sources deliverable changed (already correct).
- **Learnings:**
  - Patterns discovered: HN Algolia `items/{id}` returns the item plus its `children` tree — use it to verify comment-level quotes (strip `<p>` tags and read full `text`). GitHub HTML `<title>` is a rate-limit-free way to confirm an issue exists and its title matches.
  - Gotchas encountered: GitHub core API 403 "rate limit exceeded" during re-verification (US-002's search calls consumed it) — fell back to HTML pages. Two HN quotes looked absent until I read the FULL story text (P10 "token efficiency..." sits past the 500-char mark in the FlowLens story) and the children tree (P02 "saves me having to copy paste..." is a comment under the Heckle story, not the story text). The vibehacker URL has a trailing `-` (truncated slug) but still resolves 200 to the correct Faylee article.

---

## 2026-11-17 - US-004
- What was implemented: Scored all 15 nodes with the rubric and wrote `ranking.md` (pain_score table, pick_score table, top-five reasoning) and `ranking.json` (exact schema). Derived `pain_score = 2f+2s` and `pick_score = 2f+2s+2fit+smallness+novelty` from the sub-scores already recorded in each node file.
- Files changed: `ranking.md` (new), `ranking.json` (new), `.ralph-tui/progress.md` (this entry).
- **Learnings:**
  - Patterns discovered: The nodes already carried their five sub-scores from US-002, so US-004 was pure derivation + formatting. Top pick is P08 (pick_score 34, keyframes/timeline/transcript from recorded video), matching the US-002 learning; P02 (32) and P01 (31) round out the top three.
  - Gotchas encountered: `verified_sources` is distinct-URL count, so P08 (all evidence from one issue with 57 reactions + 21 comments) is `1` even though it lists three evidence lines. JSON titles with internal double quotes (P05 "proof", P07 "effectively blind") must be escaped.
---

## 2026-11-17 - US-005
- What was implemented: Wrote `recommendation.md` (top 3 feature specs by pick_score: P08 keyframe timeline, P02 copy-for-coding-agent, P01 agent-consumable DOM context) and `run-summary.md` (method, counts, tool outcomes, evidence weaknesses). Each spec has the user/pain (cited nodes), the feature, UX, real file paths under the extension, a unit + Playwright test plan, risks, and the open PRs it must not duplicate.
- Files changed: `recommendation.md` (new), `run-summary.md` (new), `.ralph-tui/progress.md` (this entry).
- **Learnings:**
  - Patterns discovered: The top-3 pick order (P08→P02→P01) is already fixed by `ranking.json`, so US-005 just expands each into a spec. Real file paths are verifiable from the extension source tree — keyframes/agent-prompt/descriptor changes land in `lib/export/{markdown,bundle,trimmer}.ts`, `lib/export/keyframes.ts` (new), `entrypoints/share/useShareReport.ts`, `lib/dom/descriptor.ts`, and `lib/session/types.ts`; tests mirror the existing `lib/export/*.test.ts` convention.
  - Gotchas encountered: P01 and P02 both touch "hand-off", so I separated them as *content* (P01 = the one missing piece, rendered DOM/outerHTML) vs *UX* (P02 = one-click clipboard hand-off). P08's keyframe feature should reuse existing "key moments" screenshots rather than decode webm (offscreen video decoding is the expensive path and the issue's own comment asks for exactly this selection). The suggested agent prompt lives only in `docs/report-format.md`, not in code — P02 moves it into a versioned, testable module.
---

