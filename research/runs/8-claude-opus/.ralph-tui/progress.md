# Ralph Progress Log

This file tracks progress across iterations. Agents update this file
after each iteration and it's included in prompts for context.

## Codebase Patterns (Study These First)

*Add reusable patterns discovered during development here.*

- Reddit is blocked (curl and WebSearch); use SerpAPI `site:reddit.com` and mark posts `unverified`.
- Use `in:title` in GitHub issue search; repo names: anomalyco/opencode, OpenHands/OpenHands.
- Evidence raw data: raw/gh-*.json, raw/gh-issue-bodies.json, raw/hn-*.json, raw/cursor-forum.jsonl.
- Quote verification: normalize text (unescape, lowercase alphanumerics) and substring-match; see raw/us003-quote-check.tsv.

---


## 2026-11-17 - US-001
- Wrote plan.md: 11 hypotheses (H6 = vision and video), 40 queries across github-issue, github-repo, reddit, hn, forum, blog/vendor-doc, review.
- Files changed: plan.md, .ralph-tui/progress.md
- **Learnings:**
  - Extension ZIP has video/*.webm only at Full/Standard; Compact/Minimal drop video bytes. Text agents can't read webm, so video-to-keyframes/timeline is a candidate gap to test.
  - Crowded extension areas: redaction (#31 #37 #38 #42 #44), HAR #32, cURL #43, env info #29.
---

## 2026-11-17 - US-002
- Ran GitHub issue search API (sort=reactions, ~45 queries across claude-code, codex, copilot-cli, opencode, OpenHands, Roo-Code, cline, chrome-devtools-mcp, playwright-mcp), GitHub repo search, HN Algolia (stories, comments, item threads), Cursor forum Discourse JSON, WebSearch, SerpAPI (Google) for Reddit, curl page fetches for blogs/vendor docs.
- Wrote 15 nodes (P01-P15), sources.md (verified 78, unverified 9, dropped 14), raw JSON under raw/.
- New pains beyond notes section 5: P06 prompt injection via bug reports, P07 claims fixed without verifying, P11 token blow-up, P12 images break sessions, P13 agent browser not logged in, P14 can't reproduce, P15 replay human repro. Vision/video: P08, P09, P10 (+P12).
- Files changed: nodes/*.md, sources.md, raw/*, .ralph-tui/progress.md
- **Learnings:**
  - Reddit is fully blocked here: search.json returns an HTML wall for generic UA, WebSearch refuses reddit.com. SerpAPI google_light with `site:reddit.com` finds posts (snippets only) -> mark unverified.
  - Repos moved: sst/opencode -> anomalyco/opencode, All-Hands-AI/OpenHands -> OpenHands/OpenHands (search API returns 0 for old names, no redirect).
  - GitHub `q=...+browser+console` matches body text loosely and returns generic top issues; use `in:title` for useful results. Core API is 60/hour unauthenticated; search API includes issue bodies, so use it to save core calls.
  - zsh: `echo "$json"` mangles backslashes, and function names like `gh`, `g`, `rd`, `gb` collide with aliases; use printf/curl -o and unique names (ghb, redq, gq).
  - Extension already: downscales screenshots to 1400px (lib/capture/screenshots.ts MAX_SHOT_DIM), marks evidence untrusted only in AI summary prompt (lib/sharing/summary.ts), not in report.md.
  - Candidate small PRs: video key frames into report (P10), untrusted-evidence preamble in report.md/issue (P06), acceptance-check section (P07), copy-for-agent (P02/P03).
---

## 2026-11-17 - US-003
- Re-fetched every cited non-Reddit URL (84 evidence lines; GitHub/blog by curl, HN by Algolia item API, Cursor by Discourse JSON) and checked each quote word for word: 83/84 matched. Replaced the P04 alphaxiv quote with a verbatim abstract sentence and reformatted the P03 Heckle line.
- Reddit (9) still blocked (curl 403 or login wall, web-fetch agent refused), so they stay unverified. Statuses: P02, P07, P10, P14 partly-verified; the rest verified. No merges (P03 and P15 cross-referenced). Fixed 3 mislabelled source types.
- sources.md: verified 78, unverified 9, dropped 14; added a US-003 section. Quote check saved to raw/us003-quote-check.tsv.
- Files changed: sources.md, nodes/P02,P03,P04,P07,P15, raw/us003-quote-check.tsv, .ralph-tui/progress.md
- **Learnings:**
  - Quote check: normalize to lowercase alphanumerics after html.unescape. HN Algolia JSON keeps ’ escapes, so decode them or the match comes back partial.
  - alphaxiv /abs pages only show the abstract (in a JSON-LD "abstract" field); quotes from the full paper won't match.
  - Reddit: old.reddit.com returns 200, but it is a "Welcome to Reddit" login wall, not content.
---

## 2026-11-17 - US-004
- Scored all 15 nodes (scores taken from each node's `## Scores` line), computed pain_score and pick_score with a script, wrote ranking.json (schema checked: formulas asserted, parses) and ranking.md (pain table, pick table, feature idea per node, reasons for top five).
- Pick rank top 5: P02 Copy for coding agent (35), P07 Acceptance check (34), P10 video key frames (32), P04 agent brief block (31), P01/P03/P06 tie (30). Pain rank top: P07 and P01 (18).
- Files changed: ranking.md, ranking.json, .ralph-tui/progress.md (script kept in session scratchpad, not in OUTPUT_DIR)
- **Learnings:**
  - verified_sources = distinct URLs on Evidence lines whose first parenthesis says verified (not unverified); "Same page" lines carry no URL, so they are not double-counted.
  - overlapping_prs lists nearby PRs (including closed #22) so US-005 can say what not to duplicate.
  - Ties broken by the other score, then by verified sources.
---

## 2026-11-17 - US-005
- Wrote recommendation.md: top 3 by pick_score (P02 Copy for agent 35, P07 Acceptance check 34, P10 Video key frames 32), each with user/pain (nodes cited), feature, UX, files likely touched (checked in the extension tree), unit + Playwright test plan, risks, and open PRs not to duplicate (#43; #22/#39/#49/#48; #21/#42). Plus a "not now" list.
- Wrote run-summary.md: method, counts (11 hypotheses, 40 planned / ~80 run queries, 101 sources: 78 verified, 9 unverified, 14 dropped, 15 nodes), tools that worked (GitHub API, HN Algolia, Discourse JSON, WebSearch, SerpAPI; Reddit JSON blocked), evidence weaknesses.
- Files changed: recommendation.md, run-summary.md, .ralph-tui/progress.md
- **Learnings:**
  - Extension facts for specs: the only clipboard action is copyIssue() in entrypoints/share/useShareReport.ts; ZIPs are built in both entrypoints/sidepanel/components/ExportPanel.tsx and entrypoints/report/main.ts; renderReport in lib/export/markdown.ts goes header -> ## Timeline -> appendices; the suggested agent prompt lives only in docs/report-format.md.
  - Query counts are not in the iteration logs when calls ran in shell loops; count raw/*.json files and say "approx.".
---
