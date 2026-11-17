# Ralph Progress Log

This file tracks progress across iterations. Agents update this file
after each iteration and it's included in prompts for context.

## Codebase Patterns (Study These First)

*Add reusable patterns discovered during development here.*

---


## 2026-11-17 - US-001
- Wrote plan.md: 28 queries, 6 source types, 11 hypotheses (incl. vision/video H6).
- Files changed: plan.md (created raw/ and nodes/ dirs)
- **Learnings:**
  - Open extension PRs already cover redaction, HAR, cURL, env info, duplicates; avoid them.
  - Gap per notes: hand-off to agent is manual (copyIssue only copies Markdown).
---

## 2026-11-17 - US-002
- Wrote 13 node files (P01-P13), sources.md, saved raw JSON in raw/.
- New pains not in notes section 5: P07 (CLI image paste), P08 (oversized image kills session), P09 (video), P10 (token cost), P11 (auth/session), P12 (agent browser tools unreliable).
- Vision/video nodes: P04, P06, P07, P08, P09.
- Files changed: nodes/P01..P13, sources.md, raw/*.json
- **Learnings:**
  - Reddit JSON and site:reddit.com searches are blocked/empty; no Reddit evidence. Say so in run-summary.
  - GitHub search without `in:title` returns usage-limit noise; use `in:title`. sst/opencode is now anomalyco/opencode; OpenHands is OpenHands/OpenHands.
  - Cursor forum Discourse `/t/<id>.json` gives views/likes; HN Algolia `/items/<id>` gives comment trees.
  - Top-engagement real pains: image paste (49 reactions), oversized image bricks session (90), browser connect to existing session (61), video input (57). Browser-hand-off pain evidence is mostly low-engagement; vendors (FlowLens, Heckle) confirm demand.
  - Reproduction-steps node (P13) and agent hand-off (P03) look like the best small PRs; US-004 to score.
---

## 2026-11-17 - US-003
- Re-fetched all 61 cited URLs (HTTP status) and grepped every quote in nodes/ against page/API text. All matched except 2 Product Hunt quotes (403 to curl) -> moved to unverified. Argos page now loads (verified, uncited).
- sources.md first line now: verified: 51, unverified: 9, dropped: 1. Node statuses: 11 verified, 2 partly-verified; no node depends on unverified sources.
- Files changed: sources.md, nodes/P03-*.md, nodes/P09-*.md
- **Learnings:**
  - GitHub issue bodies use markdown bold; strip `**` before quote matching (false MISS on #13480).
  - Product Hunt and G2 block curl; treat as unverified.
  - A quote-grep script (python -I, API + HTML strip) is a quick bulk verifier.
---

## 2026-11-17 - US-004
- Scored all 13 nodes by script from the Scores blocks; wrote ranking.md (two tables + reasons for top five) and ranking.json.
- Top pick: P03 (32), then P13 (31), P01 (30). Pain leader: P01 (18).
- Files changed: ranking.md, ranking.json
- **Learnings:**
  - Computing scores and verified_sources with a script from the node files avoids arithmetic slips.
  - verified_sources = distinct evidence URLs not listed in sources.md "Unverified".
---

## 2026-11-17 - US-005
- Wrote recommendation.md (3 specs: Copy for coding agent P03, Steps to reproduce block P13, agent-safe image cap P08) and run-summary.md (counts, tool status, weaknesses).
- Files changed: recommendation.md, run-summary.md
- **Learnings:**
  - P01 is mostly the P03 hand-off, so the third spec skips it for P08 (tied 30).
  - Real paths: entrypoints/share/useShareReport.ts (copyIssue ~L330), App.tsx (~L480), lib/export/markdown.ts, lib/capture/screenshots.ts (JPEG quality only, no dimension cap seen).
  - Image limits and PR #23 overlap still need checking before build.
---
