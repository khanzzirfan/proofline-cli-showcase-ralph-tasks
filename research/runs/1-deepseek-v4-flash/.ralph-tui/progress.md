# Ralph Progress Log

This file tracks progress across iterations. Agents update this file
after each iteration and it's included in prompts for context.

## Codebase Patterns (Study These First)

- The extension repo (`session-recorder-chrome-extension/`) is **outside the tool workspace root**; `read_file`
  refuses it. Read those PRD-mandated files with `shell_command cat` instead.
- Run folder layout: `plan.md`, `nodes/`, `raw/`, `sources.md`, `ranking.md`, `ranking.json`,
  `recommendation.md`, `run-summary.md`. Write only here; never touch `research/runs/<other>`.
- Tool API forms: Reddit `search.json?q=<q>&restrict_sr=1&sort=top&t=year`, HN
  `hn.algolia.com/api/v1/search?query=<q>&tags=story`, GitHub
  `api.github.com/search/issues?q=<q>&sort=reactions&order=desc`. Use `curl -sL -A "pain-research/1.0"`.
- **Reddit is blocked for this host** (JSON API and `web_fetch` both return an HTML "Prove your humanity" shell).
  Use `site:reddit.com` web search and mark Reddit sources `unverified`.
- **forum.cursor.com** thread pages are JS-rendered: `web_fetch` returns only the title. Cite the search snippet,
  mark `unverified`. GitHub issue pages/API and HN Algolia return full content (use those as primary evidence).
- Repo renames to watch: `All-Hands-AI/OpenHands` → `OpenHands/OpenHands`; `sst/opencode` → `anomalyco/opencode`.
- GitHub `search/issues` needs `sort=reactions|comments` to be useful; raw relevance is noisy (account/limit issues
  dominate). Confirm each hit with the single-issue API endpoint for exact reaction counts.
- **Use `web_fetch` on `github.com/<repo>/issues/<n>` for verification, not the REST API.** The unauthenticated
  core REST limit is 60 requests/hour and gets exhausted fast (we hit it); a GitHub issue *page* via `web_fetch`
  returns the body, all comments, the closed/open state and exact `👍 React with 👍 N` totals, with no rate limit.
  `gh` CLI is NOT installed on this host.
- `web_search`-less GitHub discovery: `api.github.com/search/repositories` has its own rate limit and still works
  after the core limit is gone.
- `docs.github.com` URLs can 301 to a renamed page — always note the redirect target ("provide-visual-inputs"
  now redirects to "research-plan-iterate") and cite what the landing page actually says.


---

## 2026-11-16 - US-001
- Wrote `plan.md` for the pain-research run: goal, condensed guardrails, 7 source types, 7 hypotheses
  (H1–H5 from notes section 5, H6 vision/video, H7 pains the notes missed), 30 concrete queries with
  exact API URL forms, coverage list of popular places, seed node plan P01–P14, Session Recorder
  PR-overlap watchlist, and the full output layout.
- Read all "Read first" files (context notes + README/PRODUCT/report-format/PLAN) via `cat`.
- Files changed: `plan.md` (new). Progress log updated.
- **Learnings:**
  - Acceptance needs ≥15 queries / ≥6 source types / ≥6 hypotheses (story text says 5, PRD says 6) — aim higher; delivered 30/7/7.
  - The extension source folder is outside the workspace root for the file tools; shell `cat` is the way in.
  - Seed nodes P09–P14 are the "not in section 5" pains required later in US-002; vision/video nodes are P06–P08.
---

## 2026-11-17 - US-002
- Ran the searches with every tool: GitHub search API (sort=reactions / sort=comments, ~15 queries across
  claude-code, codex, copilot-cli, vscode, chrome-devtools-mcp, playwright-mcp, Roo-Code, cline, OpenHands),
  GitHub repo-discovery API, Hacker News Algolia API (story+item), `web_search` + `web_fetch`, and Reddit
  `search.json` (blocked).
- Wrote 15 node files `nodes/P01..P15-*.md` (target was 12): P01 browser context, P02 copy-paste friction,
  P03 MCP hand-off, P04 cloud agents/unproven fixes, P05 secrets/redaction, P06 AI PR review has no eyes,
  P07 CLI agents can't take pasted screenshots, P08 agents can't watch video, P09 repro steps/state/auth,
  P10 verify-the-fix proof, P11 triage/duplicates/issue quality, P12 environment/flaky, P13 cost/context,
  P14 narration/annotation hand-off, P15 SaaS cost/privacy.
- Wrote `sources.md` (verified: 43, unverified: 30, dropped: 4) with a named "Popular places covered" list
  (14 places), per-URL status, and a "Vision and video — why the evidence is here" section.
- Files changed: `nodes/P01..P15-*.md` (15 new), `sources.md` (new), `raw/*.json` (saved API responses).
- **Learnings:**
  - Reddit is fully blocked for this host: `curl search.json` returns an HTML shell ("Prove your humanity") and
    `web_fetch` hits the same wall. Fall back to `site:reddit.com` web search and mark Reddit as unverified;
    quote from the search snippet, never invent the post body.
  - `forum.cursor.com` thread pages are JS-rendered: `web_fetch` returns only the thread title. Cite the search
    snippet and mark unverified. GitHub issue pages/API and HN Algolia both return full content.
  - `00-context-notes.md` had the old OpenHands repo name (`All-Hands-AI/OpenHands`) which now 404s in the search
    API — the repo is `OpenHands/OpenHands`. `sst/opencode` now redirects to `anomalyco/opencode`.
  - Strongest verified evidence clusters: (a) CLI/background agents still can't consume pasted images
    (codex#31685, copilot-cli#1276, vscode#256095/#280570, claude-code#32005); (b) agents can't watch video and
    several OSS tools exist to cut frames+timeline (videobug, amagi-screen, BugDump); (c) OpenHands#8372 asks for
    a screenshot as PR evidence — a direct "verify the fix" pain.
  - PR-overlap watch for US-004/005: redaction (P05) is crowded (#31/#37/#38/#42/#44) and #29 covers environment
    (P12) and #49 covers duplicates (P11) — keep novelty low there. The open lanes are P02 (copy for coding
    agent) and P08 (video → agent-readable frames/timeline).
---

## 2026-11-17 - US-003
- Re-opened every cited URL and set its status. GitHub issues/pages via `web_fetch` (exact state, reaction and
  comment counts), GitHub repos + repo-discovery search API + HN Algolia via `curl`, blogs/docs via `web_fetch`.
- Rewrote `sources.md`: now starts with `verified: 67, unverified: 12, dropped: 4` (counts verified with
  `grep -c`), adds a "Clean-up done in this pass" section, corrects a few reaction counts (e.g. cdtmcp#96 = 77,
  claude-code#13480 👍90) and records the two GitHub repo-search API results.
- Merged duplicate node **P10 into P04** (both = "a claimed fix needs proof"; same OpenHands#8372 evidence) and
  deleted `nodes/P10-verify-fix-proof.md`. Folded P10's evidence (thunkle.ai, TraceBug failing-test, apidog) into P04.
- Upgraded statuses to `verified`: P04, P06, P07, P12, P15. Kept `partly-verified`: P01, P02, P09, P11, P13, P14
  (each still has ≥1 verified source for its main claim; the unverified ones are Reddit / forum.cursor.com).
- Fixed non-verbatim quotes so they match the pages word-for-word: P06 (sitepoint, dev.to/jackm), P09
  (negiadventures, dev.to/yureki_lab), P11 (modem.ai), P12 (negiadventures), P13 (claude-code#13480), P14
  (videolens, HN 49119880). Upgraded opencode#1429 from unverified to verified (👍16).
- Files changed: `sources.md` (rewritten), nodes P01, P02, P04, P06, P07, P09, P11, P12, P13, P14, P15 edited,
  `nodes/P10-*.md` deleted, this log. No file written outside OUTPUT_DIR; no git commands.
- **Learnings:**
  - GitHub's unauthenticated REST core limit (60/hr) was exhausted by the US-002 API calls. `web_fetch` on the
    issue *page* gives body + comments + reactions with no limit — use it for verification. `gh` CLI not installed.
  - Reddit (HTML "Prove your humanity") and forum.cursor.com (JS-rendered, title only) are the only two
    unverifiable hosts; everything else cited — GitHub, HN, 20+ blogs/docs, Chrome Web Store, Toolradar — opened.
  - Two node quotes (negiadventures, modem.ai) and two blog quotes (sitepoint, dev.to/jackm) were paraphrases in
    quote marks; the plagiarism check was to re-open and copy the exact sentence.
---



## 2026-11-17 - US-004
- Scored all 14 nodes (P10 was merged into P04 in US-003) with the rubric and wrote `ranking.md`:
  pain_score table (sorted desc), pick_score table (sorted desc, with the open PRs to avoid), and
  a "why the top five" section. Wrote `ranking.json` matching the required schema exactly.
- Top pick = **P02** "Copy for coding agent" (pick_score 35; f5 s3 fit5 small5 nov4). Runners-up:
  P08 video key frames (33), P09 repro steps/state (31), P07 image manifest (31), P01 hand over
  captured console/network (31). Highest pain_score is P05 secrets (18) but novelty 0 (six open PRs).
- Files changed: `ranking.md` (new), `ranking.json` (new), this log. No file outside OUTPUT_DIR.
- **Learnings:**
  - pain_score and pick_score both re-derived and asserted in a throwaway python check (all 14 nodes
    pass `2f+2s` and `2f+2s+2fit+small+nov`), so the tables and JSON can never drift from the rubric.
  - Tie handling matters: P01/P07/P09 all pick_score 31 and P01/P04/P08/P09 all pain_score 16. Made
    the tiebreaks explicit in the doc (pain: severity→frequency→id; pick: demote duplicate-of-a-higher-pick
    → severity → verified sources → id) so the ordering is reproducible, not vibes.
  - P01 and P02 describe the SAME action (hand captured console/network → agent = the clipboard copy),
    so P01 is demoted below P02 in pick_rank; otherwise US-005 would ship two versions of one feature.
    watch out for this coupling in `recommendation.md`.
---

## 2026-11-17 - US-005
- Read all 14 node files, `ranking.md`/`ranking.json`, `sources.md`, `plan.md` and the relevant
  extension source (via `cat`, since the repo is outside the workspace root): `ExportPanel.tsx`,
  `useShareReport.ts`, `share/App.tsx`, `lib/export/{bundle,markdown,trimmer,tokens,zip}.ts`,
  `entrypoints/offscreen/video.ts`, `lib/sharing/{report,summary,draft}.ts`, `docs/report-format.md`,
  `docs/PLAN.md`, `e2e/record-export.spec.ts`, `lib/session/types.ts`.
- Wrote `recommendation.md`: the top 3 by `pick_score` — **P02 Copy for coding agent** (35),
  **P08 video key frames + timeline** (33), **P09 repro steps + required state** (31). Each spec has
  the user + pain with node citations, the feature, UX (where it lives / clicks), **real extension
  file paths**, unit + Playwright test plans with the actual commands (`pnpm compile`, `pnpm test`,
  `pnpm test:e2e`), risks, and the open PR(s) it must not duplicate (#43 for P02; none for P08;
  #29/#41 build-on for P09).
- Wrote `run-summary.md`: what I searched, counts (30 planned queries, 79 URL lines /
  `sources.md` header 67 verified-12 unverified-4 dropped, 14 nodes, 29 raw JSON files, 14 places),
  which tools worked (web_fetch issue pages, curl HN Algolia + GitHub search, web_search site:) vs
  blocked (Reddit, forum.cursor.com; GitHub core REST limit; no `gh`), and the evidence weaknesses
  (unverifiable Reddit/forum, vendor-heavy vision/video, uneven popularity signals, shallow reviews).
- Files changed: `recommendation.md` (new), `run-summary.md` (new), this log. No file outside
  OUTPUT_DIR; no git commands.
- **Learnings:**
  - Pick order comes straight from `ranking.json.pick_rank`; keep `recommendation.md` consistent with
    it. P01 (fifth) collapses into P02, so the spec for P02 notes P01 as supporting evidence instead
    of proposing a second clipboard feature.
  - "Files likely touched" must name paths that actually exist (checked with `find`/`cat`), plus one
    or two clearly-new paths; the cleanest P02 PR is `ExportPanel.tsx` + a new pure
    `lib/export/agent-handoff.ts` + `lib/export/bundle.ts`, reusing `renderReport`.
  - `sources.md`'s own header counts (67/12/4) and a naive `grep` of list items disagree by a couple
    because a few lines carry two URLs — state both numbers rather than silently pick one.
---
