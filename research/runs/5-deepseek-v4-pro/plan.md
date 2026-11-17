# US-001 — Search plan

Agent: deepseek/deepseek-v4-pro
Output dir: <mission>/research/runs/5-deepseek-v4-pro
Date: 2026-11-17

## Goal

Find real public evidence of the pains people have when they report, reproduce and fix
browser bugs with AI coding agents, rank those pains, and turn the best one into a small
feature for Session Recorder by Proofline.

## What I already know

From `00-context-notes.md` and the extension docs:

- Five candidate pains in the notes (section 5): (1) the agent can't see the browser;
  (2) copy-paste friction and lost/leaking logs; (3) handing a bug straight to an agent,
  often over MCP; (4) cloud agents that start from GitHub issues and want proof a fix
  worked; (5) redaction and secrets.
- Session Recorder already captures clicks, inputs, console, exceptions, network,
  screenshots, annotations, narration, transcripts, tab video and files, and exports a
  `report.md` ZIP at four trim levels. The known gap is that handing that report to a
  coding agent is manual (export ZIP, unzip, paste, copy the prompt from the docs).
- Open PRs not to duplicate (extension): #48, #47, #46, #45, #44, #43, #42, #41, #40,
  #39, #38, #37, #33, #32, #31, #30, #29, #25, #24, #23, #21.

## Hypotheses to test

- **H1 — Browser context gap.** Agents cannot see the browser's console, network, DOM or
  UI state, so they guess at frontend bugs or make the human paste logs. (notes pain 1)
- **H2 — Copy-paste friction.** Handing browser evidence to an agent is manual paste of
  console logs, cURL or HAR; pasted text sometimes never reaches the agent and can leak
  tokens. (notes pain 2)
- **H3 — Direct hand-off / MCP.** Users want to hand a bug report straight to an agent
  (Claude Code, Codex, Cursor, opencode), often over MCP or a one-link share. (notes pain 3)
- **H4 — Issue-driven agents and proof of fix.** Cloud agents start from GitHub issues and
  users want enough evidence in the issue plus reliable proof a fix worked (before/after
  screenshots in the PR). (notes pain 4)
- **H5 — Privacy and secrets.** Redaction and secret leakage into agent context or shared
  reports is a repeated, concrete worry. (notes pain 5)
- **H6 — Vision and video.** AI PR reviewers and CLI coding agents cannot see the UI a
  change produces or watch a screen recording; there is a gap around turning screenshots
  and video into something an agent can read (visual regression, screenshot diffs,
  before/after in PRs, key frames or a timeline from a bug video). (required area)

I will also watch for pains the notes missed: reproduction fidelity, issue quality, triage
and duplicates, verifying a fix worked, flaky fixes, auth/environment context, and cost.

## Search queries

Popularity signals: GitHub `reactions.total_count` and `+1` / `comments`; Reddit `score`
and `num_comments`; HN `points` and `num_comments`. Use a generic UA on every curl and
pause ~2s between calls to the same host. Save relied-on raw JSON under `raw/`.

### Source type 1 — GitHub issues, most-reacted (curl, sort=reactions)

1. `curl -sL -A "pain-research/1.0" "https://api.github.com/search/issues?q=repo:anthropics/claude-code+browser+console&sort=reactions&order=desc&per_page=20"`
2. `curl -sL -A "pain-research/1.0" "https://api.github.com/search/issues?q=repo:anthropics/claude-code+screenshot+image+vision&sort=reactions&order=desc&per_page=20"`
3. `curl -sL -A "pain-research/1.0" "https://api.github.com/search/issues?q=repo:anthropics/claude-code+bug+report&sort=reactions&order=desc&per_page=20"`
4. `curl -sL -A "pain-research/1.0" "https://api.github.com/search/issues?q=repo:getcursor/cursor+browser+console+network&sort=reactions&order=desc&per_page=20"`
5. `curl -sL -A "pain-research/1.0" "https://api.github.com/search/issues?q=repo:All-Hands-AI/OpenHands+screenshot+visual+regression&sort=reactions&order=desc&per_page=20"`
6. `curl -sL -A "pain-research/1.0" "https://api.github.com/search/issues?q=repo:RooCodeInc/Roo-Code+screenshot+image+vision&sort=reactions&order=desc&per_page=20"`
7. `curl -sL -A "pain-research/1.0" "https://api.github.com/search/issues?q=repo:sst/opencode+image+screenshot+vision&sort=reactions&order=desc&per_page=20"`
8. `curl -sL -A "pain-research/1.0" "https://api.github.com/search/issues?q=repo:cline/cline+screenshot+image&sort=reactions&order=desc&per_page=20"`
9. `curl -sL -A "pain-research/1.0" "https://api.github.com/search/issues?q=repo:ChromeDevTools/chrome-devtools-mcp+browser+console&sort=reactions&order=desc&per_page=20"`
10. `curl -sL -A "pain-research/1.0" "https://api.github.com/search/issues?q=repo:microsoft/playwright-mcp+browser+debug&sort=reactions&order=desc&per_page=20"`

### Source type 2 — GitHub issues, most-commented (curl, sort=comments)

11. `curl -sL -A "pain-research/1.0" "https://api.github.com/search/issues?q=repo:anthropics/claude-code+browser+console&sort=comments&order=desc&per_page=20"`
12. `curl -sL -A "pain-research/1.0" "https://api.github.com/search/issues?q=repo:anthropics/claude-code+bug+report+screenshot&sort=comments&order=desc&per_page=20"`

### Source type 3 — GitHub repo discovery (curl)

13. `curl -sL -A "pain-research/1.0" "https://api.github.com/search/repositories?q=bug+report+mcp+agent&sort=stars&order=desc"`

### Source type 4 — Reddit top posts (curl, search.json sort=top)

14. `curl -sL -A "pain-research/1.0" "https://www.reddit.com/r/ClaudeAI/search.json?q=browser+console&restrict_sr=1&sort=top&t=year&limit=25"`
15. `curl -sL -A "pain-research/1.0" "https://www.reddit.com/r/cursor/search.json?q=browser+bug&restrict_sr=1&sort=top&t=year&limit=25"`
16. `curl -sL -A "pain-research/1.0" "https://www.reddit.com/r/ChatGPTCoding/search.json?q=bug+report+screenshot&restrict_sr=1&sort=top&t=year&limit=25"`
17. `curl -sL -A "pain-research/1.0" "https://www.reddit.com/r/webdev/search.json?q=AI+coding+agent+bug&restrict_sr=1&sort=top&t=year&limit=25"`

### Source type 5 — Hacker News (Algolia API, points)

18. `curl -sL -A "pain-research/1.0" "https://hn.algolia.com/api/v1/search?query=coding+agent+browser+bug&tags=story"`
19. `curl -sL -A "pain-research/1.0" "https://hn.algolia.com/api/v1/search?query=AI+bug+report+screenshot&tags=comment"`
20. `curl -sL -A "pain-research/1.0" "https://hn.algolia.com/api/v1/search?query=visual+regression+AI+review&tags=story"`

### Source type 6 — Web search tool

21. `site:reddit.com Claude Code browser console network agent can't see`
22. `site:forum.cursor.com agent cannot access browser console network tab`
23. `site:news.ycombinator.com AI coding agent screenshot bug report`
24. `site:forum.cursor.com copy paste console agent no longer see it`
25. `site:github.com coding agent screenshot vision video bug report issue`

### Source type 7 — Web fetch tool (store reviews, forums, vendor docs)

26. Chrome Web Store reviews of Jam, Marker.io, BetterBugs, Darnly, FlowLens, Faylee —
    read the low-star reviews first.
27. `forum.cursor.com` threads from the notes (browser console access; copy-paste loss).
28. Product Hunt comments for FlowLens and Faylee; G2 pages for Jam / Marker.io.
29. Vendor docs/changelogs: GitHub Copilot "provide visual inputs", Devin Review,
    OpenHands resolver, Jam MCP, Darnly, Faylee.

## Coverage checklist (target >= 8)

anthropics/claude-code · getcursor/cursor + forum.cursor.com · openai/codex ·
github/copilot-cli + community discussions · All-Hands-AI/OpenHands · RooCodeInc/Roo-Code ·
sst/opencode · cline/cline · ChromeDevTools/chrome-devtools-mcp · microsoft/playwright-mcp ·
BrowserMCP / browser-use · r/ClaudeAI · r/cursor · r/ChatGPTCoding · r/webdev ·
r/QualityAssurance · r/ExperiencedDevs · Hacker News · Chrome Web Store reviews.

## What success looks like

At least 12 node files (aim 15-20), each with >= 2 evidence links, at least 3 nodes NOT in
notes section 5, and at least 2 vision/video nodes if evidence exists. Every URL recorded in
`sources.md` with a status, every cited page opened with web fetch, and no invented quotes.
