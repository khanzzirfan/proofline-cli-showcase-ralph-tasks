# Search plan (US-001), run 4-claude-sonnet

Date: 2026-11-17. Tools I will use: WebSearch, WebFetch, and `curl -sL -A "pain-research/1.0"` against the GitHub, Reddit and HN Algolia JSON APIs. About 2 seconds between calls to the same host. Small raw JSON goes in `raw/`.

## What I read first

- Notes: Session Recorder is a Chrome extension (WXT, React, TS). It already captures clicks, console, network, screenshots, annotations, narration, tab video, files and an inferred OpenAPI. It exports a ZIP with `report.md` at four trim levels and files GitHub issues.
- Known gap: handing a report to an agent is manual (`copyIssue` only copies issue Markdown).
- Out of scope in `docs/PLAN.md`: live streaming to an agent, rrweb DOM replay, Firefox, Safari.
- 21 open PRs already cover: redaction (5), grouping duplicates (#49), labels (#48), cURL (#43), HAR (#32), storage snapshot (#41), env info (#29), shadow DOM (#45), Linear (#24), request IDs (#39), screenshot shortcuts (#21). Avoid all of these.

## Queries (28), grouped by source type

### 1. GitHub issues API, most reacted (`sort=reactions&order=desc`, then `sort=comments`)
1. `repo:anthropics/claude-code browser console` (sort reactions)
2. `repo:anthropics/claude-code screenshot image paste` (sort reactions)
3. `repo:anthropics/claude-code video OR recording` (sort comments)
4. `repo:openai/codex image OR screenshot` (sort reactions)
5. `repo:RooCodeInc/Roo-Code browser console OR network` (sort reactions)
6. `repo:sst/opencode image OR screenshot OR vision` (sort reactions)
7. `repo:ChromeDevTools/chrome-devtools-mcp` network OR console OR auth OR login (sort reactions)
8. `repo:microsoft/playwright-mcp` screenshot OR token OR snapshot (sort reactions)
9. `repo:cline/cline` and `repo:All-Hands-AI/OpenHands` with `visual OR screenshot OR reproduce`
10. GitHub repo discovery: `bug report mcp agent`, `browser console mcp`, `screen recording bug ai` (sort stars)

### 2. Reddit top (JSON API, `sort=top&t=year`; fall back to `site:reddit.com` web search if blocked)
11. r/ClaudeAI: `browser console`, `screenshot`, `debug frontend`
12. r/cursor: `browser console`, `agent can't see`, `screenshot`
13. r/ChatGPTCoding: `bug report agent`, `UI bug`, `video`
14. r/webdev and r/ExperiencedDevs: `AI agent fix bug`, `AI PR review UI`
15. r/QualityAssurance: `AI bug report`, `reproduce steps AI`, `Jam OR Marker.io`

### 3. Hacker News (Algolia: `search?query=...&tags=story` and `tags=comment`; points and comments)
16. `coding agent browser bug`
17. `bug report AI agent reproduce`
18. `screen recording AI agent video`
19. `AI code review visual regression screenshot`
20. Show HN: `bug report extension MCP`

### 4. Forums
21. `site:forum.cursor.com browser console network agent`
22. `site:forum.cursor.com screenshot image agent` and `video`
23. `site:github.com/orgs/community copilot coding agent screenshot` (discussions)

### 5. Chrome Web Store, Product Hunt, G2 reviews (WebFetch listing pages)
24. Jam, Marker.io, BetterBugs, Darnly, FlowLens, Faylee: low-star reviews and "missing" wishes
25. Product Hunt comments on FlowLens, Jam, Faylee

### 6. Blogs and vendor docs (weak evidence, marked as such)
26. Copilot coding agent visual inputs; Jules; Codex cloud docs on screenshots
27. Jam MCP docs, Marker.io AI features, Loom AI bug features (video to text)
28. Blogs: `agent can't reproduce bug`, `AI agent flaky fix`, `verify fix agent screenshot`

## Hypotheses to test

- H1 Agent can't see the browser (console, network, DOM, UI state, auth). Notes pain 1.
- H2 Copy-paste friction: manual pasting of logs, cURL, HAR; leaks; pastes that don't reach the agent. Notes pain 2.
- H3 Users want one-step hand-off from a bug tool to an agent (MCP or issue). Notes pain 3.
- H4 Cloud agents start from GitHub issues, and issue quality (missing steps, env, expected result) makes them guess or fail. Notes pain 4, extended.
- H5 Redaction and safety: secrets leak into prompts and reports; local MCP servers are open. Notes pain 5.
- H6 **Vision and video:** (a) AI reviewers and PR agents can't see the UI a change makes; no before/after screenshots. (b) CLI agents can't take images from issues or paste. (c) Agents can't watch a screen recording; users want key frames, a timeline or text. Test whether the gap is real, and what an agent can use from today's ZIP (screenshots, video file, `report.md`).
- H7 Verifying a fix: agents say "fixed" without proof; the human re-runs the repro by hand. Look for demand for a repro script or checklist the agent can run.
- H8 Token and context cost: raw HAR, console or DOM dumps blow the context window; users want trimmed, ranked evidence.
- H9 Reproduction gaps: bugs depend on auth, data, environment, flags or timing, so the agent can't reproduce. Missing from the notes.
- H10 Duplicates and triage: agent-opened or user-filed issues duplicate each other. (Open PR #49 overlaps, so I check it only to avoid it.)
- H11 Non-developers (QA, product) can't write the prompt an agent needs. Missing from the notes.

## Pains the notes may have missed (to look for on purpose)

Auth and session state for the agent; environment and version info (open PR #29 overlaps); privacy of video and audio; cost and tokens; flaky or wrong fixes; agents that "fix" the symptom; issue templates for agents; mobile or responsive bugs; narration quality.

## Coverage target

At least 8 popular places from the PRD list, 12+ nodes, at least 3 not in notes section 5, at least 2 vision/video nodes. I will not propose a vision or video feature unless evidence shows a real gap.
