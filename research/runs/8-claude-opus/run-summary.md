# Run summary: 8-claude-opus

Date: 2026-11-17. Agent: claude (opus). All files are in this folder; nothing was written elsewhere, no git commands that change anything, no sign-ins, no posts.

## What I did

1. **US-001 plan** (`plan.md`): read the context notes and the extension docs; wrote 11 hypotheses (H1-H5 from section 5 of the notes, H6 vision and video, H7-H11 new) and 40 planned queries across 7 source types (GitHub issues, GitHub repos, Reddit, HN, Cursor forum, blogs/vendor docs, reviews).
2. **US-002 collect**: ran the searches, wrote 15 nodes (`nodes/P01`-`P15`), recorded every URL in `sources.md`, saved raw JSON in `raw/`.
3. **US-003 verify**: re-opened every cited non-Reddit URL and checked every quote word for word (83 of 84 matched; the miss was replaced with a verbatim quote). Results in `raw/us003-quote-check.tsv`.
4. **US-004 rank**: scored all nodes with the PRD rubric; `ranking.md` and `ranking.json` (parses, formulas checked).
5. **US-005 recommend**: `recommendation.md` with three feature specs, file paths checked against the extension source tree.

## Counts

| Item | Count |
|---|---|
| Hypotheses | 11 |
| Planned queries (`plan.md`) | 40 |
| Queries run (approx.) | ~80: ~45 GitHub issue searches (35 saved in `raw/gh-*.json`), 3 GitHub repo searches, 7 HN Algolia searches (`raw/hn-*.json`) plus item lookups, 8 Cursor forum threads, 13 built-in web searches, 7 SerpAPI (Google) searches for Reddit, Reddit JSON attempts (all blocked) |
| Sources recorded in `sources.md` | 101 |
| Verified | 78 |
| Unverified | 9 (all Reddit, search snippets only) |
| Dropped | 14 (403/404, JS-only pages, low signal, mirrors) |
| Evidence lines checked in US-003 | 84 (83 quotes matched verbatim) |
| Nodes | 15 (4 partly-verified: P02, P07, P10, P14; 11 verified) |
| Nodes not in section 5 of the notes | 7 (P06, P07, P11, P12, P13, P14, P15) |
| Vision and video nodes | 3 (P08, P09, P10) plus P12 related |
| Popular places covered | 12 of the PRD list |

## Tools: what worked

| Tool | Worked? | Notes |
|---|---|---|
| Web search (built-in WebSearch) | Yes, partly | Good for blogs, vendor docs and forum posts. Refuses `reddit.com`. |
| Web fetch | Partly | Most pages were opened with `curl -sL -A "pain-research/1.0"` instead; the web-fetch agent was refused for Reddit. G2 and Product Hunt returned 403. Chrome Web Store reviews load by script, so only listing text was readable. |
| GitHub API (`search/issues`, `search/repositories`, issue bodies) | Yes | Main source. No token: 10 search calls/min, 60 core calls/hour (used 32). `in:title` gave far better results than body matches. Repos moved: `sst/opencode` → `anomalyco/opencode`, `All-Hands-AI/OpenHands` → `OpenHands/OpenHands`. |
| Reddit JSON API | No | `search.json` and `api.reddit.com` return 403 or an HTML block page; `old.reddit.com` returns a login wall. Fallback: SerpAPI Google search with `site:reddit.com`; posts kept as `unverified`. |
| HN Algolia API | Yes | Stories, comments and item lookups; used for verification too. |
| Cursor forum (Discourse JSON) | Yes | `/t/<id>.json` gives likes, views and post text. |
| SerpAPI (Google) | Yes | Only route to Reddit content (snippets). |

## Top results

- **Pain rank (pain_score):** P07 agent says "fixed" without checking (18), P01 agent can't see the browser (18), P02 copy-paste console logs (16), P04 vague reports → wrong fixes (16), P14 can't reproduce (16).
- **Pick rank (pick_score):** P02 Copy for coding agent (35), P07 Acceptance check (34), P10 Video key frames (32).
- **Top pick:** a "Copy for agent" button that puts a ready prompt plus the trimmed `report.md` on the clipboard.
- **Vision and video:** one real gap for Session Recorder (P10: agents cannot read the `video/*.webm` the ZIP contains). PR review blind to UI (P08) and CLI agents without image input (P09) are real but mostly outside what a recorder can fix in one PR.

## Weaknesses of the evidence

1. **Reddit is missing as a verified source.** All 9 Reddit posts are search snippets that I could not open. Users' own voices on Reddit (the PRD's first-named source) are therefore thin, and P10 and P14 lean on them for frequency.
2. **GitHub issue bias.** Most verified evidence is from GitHub issues, mainly anthropics/claude-code. That over-represents Claude Code users and people who file bugs, and under-represents QA and product people, who rarely post there.
3. **Low engagement on many sources.** Apart from a few strong signals (claude-code #57034 with 76 reactions, #12676 with 57, the 604-point HN Chrome DevTools MCP story, the Cursor thread with 3,295 views), many cited issues have 0 to 6 reactions. Frequency scores of 4 often rest on several small sources, not one big one.
4. **Review sites failed.** G2 and Product Hunt returned 403 and Chrome Web Store reviews did not load, so complaints about competing bug-report tools (Jam, Marker.io, BetterBugs) are barely covered.
5. **Vendor and blog bias.** Some nodes (P04, P06, P10) cite vendor docs or security blogs, which the PRD counts as weak evidence. P06 has only 3 verified sources.
6. **Scores are one agent's judgement.** fit, smallness and novelty were scored by me against the extension code and the open-PR list in the notes as of 2026-11-17; open PRs may change. Query counts in this summary are approximate because many GitHub and HN calls ran in shell loops.
7. **Survivor bias of "agent can't see X" posts.** Tools such as Chrome DevTools MCP and Playwright MCP now cover part of P01 and P02; some older complaints may already be solved for users who installed them.
