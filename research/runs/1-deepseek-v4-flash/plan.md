# US-001: Search plan — pains when handing bugs to AI coding agents

**Agent:** `1-deepseek-v4-flash` (command-code-research, deepseek/deepseek-v4-flash)
**OUTPUT_DIR:** `<mission>/research/runs/1-deepseek-v4-flash`
**Date:** 2026-11-16

## Goal

Collect real public evidence of the pains developers, QA and product people feel when they report,
reproduce and fix bugs (especially web/browser bugs) with AI coding agents. Rank the pains and turn
the best into small feature ideas for **Session Recorder by Proofline** — one clean PR, a few hundred
lines with tests.

**Target for our PR:** Session Recorder already records clicks, inputs, navigation, tabs, console,
exceptions, network, screenshots, annotations, narration, transcripts, video, files and an inferred
OpenAPI description; it exports a `report.md` ZIP and files GitHub issues. The known gap (from
`00-context-notes.md` section 3): handing a report to a coding agent is manual — export ZIP, unzip,
paste `report.md`, copy the prompt from the docs. Only the issue Markdown is copied in code
(`copyIssue` in `entrypoints/share/useShareReport.ts`). Open PRs #21–#49 must not be duplicated.

## Guardrails (restated, applied to every query)

1. Write only inside OUTPUT_DIR. Never edit the extension repo, the notes, the PRD, or any other folder.
2. Independence: never open/list/read anything under `research/runs/` except this OUTPUT_DIR.
3. No state-changing git. No PRs, issues, comments, sign-ins anywhere.
4. Every claim cites a real URL I actually opened or saw in results; quotes ≤30 words, verbatim; mark
   anything I could not open `unverified`. Vendor marketing = weak evidence.
5. No personal data; usernames only if part of a public URL.
6. Plain short English; dates `YYYY-MM-DD`.
7. All `curl` calls: `curl -sL -A "pain-research/1.0"`, ~2s between calls to the same host. Save the
   small raw JSON I rely on under `raw/`.

## Source types to cover (7)

1. **Reddit JSON API** (`search.json`, `sort=top`) — score + `num_comments` as the signal.
2. **Hacker News Algolia API** — `points` + `num_comments`.
3. **GitHub issues search API** (`sort=reactions`, `sort=comments`) — `reactions.total_count`, comments.
4. **GitHub repo discovery API** — stars for the tool landscape.
5. **Web search tool** — broad queries plus `site:` filters (reddit, news.ycombinator.com, github.com, forum.cursor.com).
6. **Chrome Web Store / Product Hunt / G2 review pages** (web fetch) — low-star reviews show the pain.
7. **Vendor docs / changelogs / blogs** (web fetch) — weak evidence, but shows what shipped and what is missing.

## Hypotheses to test

From `00-context-notes.md` section 5 (H1–H5) plus vision/video (H6) and one for pains the notes may
have missed (H7).

- **H1 — "My agent can't see the browser."** Agents cannot read the live browser: console, network
  tab, DOM/UI state; they guess at frontend bugs. (notes: claude-code #75632, #52907; Cursor forum.)
- **H2 — Copy-paste friction and secret leakage.** Users paste console logs / cURL / HAR by hand;
  tokens leak; pasted logs sometimes never reach the agent. (notes: Cursor forum thread.)
- **H3 — Hand a bug straight to an agent, often over MCP.** Jam MCP, Darnly, FlowLens, Faylee exist;
  is the gap in what they hand over (evidence fidelity, redaction)? (notes: jam.dev, producthunt FlowLens.)
- **H4 — Cloud agents start from GitHub issues; users want proof a fix works.** Copilot/Jules/Codex/
  OpenHands trigger from issues; before/after screenshots in the PR are unreliable. (notes: GitHub docs,
  community discussion 169913, sinatra.dev.)
- **H5 — Redaction and safety.** Users fear secrets in screenshots/network/URLs; a local MCP server was
  found reachable by any local process. (notes: infosecurity-magazine.)
- **H6 — Vision and video (required area).** (a) AI reviewers / PR agents cannot see the UI a change
  produces; visual regression and screenshot diffs; before/after screenshots in PRs. (b) Agents that
  cannot use images in issues (e.g. CLI agents without image paste). (c) Agents cannot watch a screen
  recording; the need to turn a bug video into key frames, a timeline or text an agent can read; video
  analysis in Jam/Loom/Marker.io. Only propose a feature here if evidence shows a real gap — say so
  plainly if it does not.
- **H7 — Pains the notes missed.** Candidate areas to probe: verifying a fix / re-recording proof,
  flaky agent fixes, triage and duplicates, issue quality (too little or too much detail), environment
  and auth/state the agent lacks, cost of long context, reproducibility of race conditions.

## Concrete queries (30)

### A. Reddit top posts (source type 1)

1. `https://www.reddit.com/r/ClaudeAI/search.json?q=browser+console&restrict_sr=1&sort=top&t=year&limit=25`
2. `https://www.reddit.com/r/cursor/search.json?q=agent+console+network&restrict_sr=1&sort=top&t=year&limit=25`
3. `https://www.reddit.com/r/ChatGPTCoding/search.json?q=debug+frontend+agent&restrict_sr=1&sort=top&t=year&limit=25`
4. `https://www.reddit.com/r/webdev/search.json?q=AI+bug+report+screenshot&restrict_sr=1&sort=top&t=year&limit=25`
5. `https://www.reddit.com/r/QualityAssurance/search.json?q=bug+report+AI&restrict_sr=1&sort=top&t=year&limit=25`
6. `https://www.reddit.com/r/ExperiencedDevs/search.json?q=AI+coding+agent+review&restrict_sr=1&sort=top&t=year&limit=25`
7. Open the top 2–3 posts' comments, e.g. `https://www.reddit.com/r/<sub>/comments/<id>.json?limit=50&sort=top`.
   If Reddit blocks the request, fall back to web search `site:reddit.com` and say so in `run-summary.md`.

### B. Hacker News — Algolia by points (source type 2)

8. `https://hn.algolia.com/api/v1/search?query=coding+agent+browser+bug&tags=story&numericFilters=points>20`
9. `https://hn.algolia.com/api/v1/search?query=browser+console+ai+agent&tags=comment`
10. `https://hn.algolia.com/api/v1/search?query=AI+code+review+screenshots&tags=story`
11. `https://hn.algolia.com/api/v1/search?query=bug+report+screen+recording&tags=story`
12. `https://hn.algolia.com/api/v1/search?query=visual+regression+testing&tags=story&numericFilters=points>50`

### C. GitHub issues, most-reacted first (source type 3)

Pattern: `https://api.github.com/search/issues?q=<query>&sort=reactions&order=desc&per_page=20`
(repeat with `sort=comments`, and with `is:issue`). Read reactions and comment counts.

13. `repo:anthropics/claude-code browser console`
14. `repo:anthropics/claude-code screenshot image vision`
15. `repo:getcursor/cursor screenshot image`
16. `repo:ChromeDevTools/chrome-devtools-mcp console network screenshot`
17. `repo:microsoft/playwright-mcp screenshot image video`
18. `repo:All-Hands-AI/OpenHands browser screenshot`
19. `repo:RooCodeInc/Roo-Code screenshot vision image`
20. `repo:openai/codex screenshot image attach`
21. `repo:github/copilot-cli screenshot image`

### D. GitHub repo discovery (source type 4)

22. `https://api.github.com/search/repositories?q=bug+report+mcp+agent&sort=stars&order=desc`
23. `https://api.github.com/search/repositories?q=bug+report+chrome+extension&sort=stars&order=desc`

### E. Web search — broad and `site:` (source type 5)

24. `site:forum.cursor.com agent console network tab`
25. `"visual regression" OR "screenshot diff" AI code review pull request`
26. `site:github.com copilot coding agent screenshot issue visual`
27. `turn bug screen recording into frames OR timeline for an AI agent`
28. `site:reddit.com claude code cannot see browser console`
29. `site:news.ycombinator.com coding agent frontend bug console`
30. `AI agent cannot read screenshot image in github issue`

### F. Reviews and listings (source type 6, web fetch)

- Chrome Web Store reviews: Jam, Marker.io, BetterBugs, Darnly, FlowLens (low-star reviews for pain).
- Product Hunt: FlowLens AI-native bug reports (comments).
- G2: Jam reviews (low-star).

### G. Vendor docs / changelogs / blogs (source type 7, web fetch)

- `https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs`
- Jam docs / Marker.io AI features; Jam MCP `mcp.jam.dev`; Loom + AI.
- Proofline extension docs already read: `README.md`, `PRODUCT.md`, `docs/report-format.md`, `docs/PLAN.md`.

## Coverage: popular places (aim ≥8)

- anthropics/claude-code · getcursor/cursor · forum.cursor.com · openai/codex · github/copilot-cli +
  GitHub community discussions · All-Hands-AI/OpenHands · RooCodeInc/Roo-Code · sst/opencode ·
  cline/cline · ChromeDevTools/chrome-devtools-mcp · microsoft/playwright-mcp · browser-use/BrowserMCP ·
  r/ClaudeAI · r/cursor · r/ChatGPTCoding · r/webdev · r/QualityAssurance · r/ExperiencedDevs ·
  Hacker News · Chrome Web Store reviews.

## Node plan (US-002 target: 15–20 nodes, ≥12 required)

Seed nodes from section 5, to be confirmed/merged with evidence:
- P01 Agent can't see the browser (console/network/DOM) — H1
- P02 Hand-pasting logs/cURL/HAR and token leakage — H2
- P03 Handing a bug to an agent over MCP — H3
- P04 Issue-driven cloud agents and unproven fixes — H4
- P05 Redaction / secrets in evidence and MCP exposure — H5
- P06 AI PR review with no visual evidence (vision) — H6a
- P07 Agents can't use images in issues (CLI agents) — H6b
- P08 Bug video an agent can't watch; needs frames/timeline — H6c
- P09 Reproducing a bug for the agent (steps, state, auth) — H7
- P10 Verifying the fix / re-recording proof — H7
- P11 Triage and duplicate issues / issue quality — H7
- P12 Environment and flaky/race-condition bugs — H7
- P13 Cost / long context of pasted evidence — H7
- P14 Annotation and narration as the de-facto handoff — H7

At least 3 nodes must be pains **not** in section 5 of the notes (target: P09–P14). Each node needs
≥2 evidence links and the node-format frontmatter. Aim for ≥2 nodes in the vision/video area (P06–P08),
or a `sources.md` section explaining why the evidence was not found.

## Session Recorder overlap to watch (for `## Session Recorder angle`)

- **#21** screenshot/pause keyboard shortcuts · **#29** browser/OS/viewport in report · **#32** HAR export ·
  **#43** Copy as cURL · **#42** secret protection across evidence · **#31/#37/#38/#44** redaction ·
  **#41** storage snapshot · **#49** group recordings into existing issues · **#48** labels/assignees on filing ·
  **#22** Playwright repro test (closed by author). Already-done ⇒ novelty 0.

## Outputs (rest of the run)

```
plan.md              this file (US-001)
nodes/P01-<slug>.md  one file per pain (US-002), P01, P02, ...
sources.md           every URL with status verified | unverified | dropped (US-002/003)
ranking.md           ranked tables + reasoning (US-004)
ranking.json         machine-readable ranking (US-004)
recommendation.md    top 3 feature specs (US-005)
run-summary.md       method, counts, evidence weaknesses (US-005)
raw/                 small raw JSON I rely on (Reddit / HN / GitHub API)
```

## Method note

Every query above is read-only and public. I will record popularity signals (upvotes, `score`,
`points`, reactions, comments) wherever the source shows them, and I will set each node's `status`
to `verified | partly-verified | unverified` after opening each cited URL in US-003.
