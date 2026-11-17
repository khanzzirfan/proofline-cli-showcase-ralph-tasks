# PRD: What hurts people who hand bugs to AI coding agents? (research run)

You are one of four independent research agents. Each agent runs the same brief and writes to its own folder.
The owner compares the four outputs afterwards, so **follow the formats below exactly**.

Your story description names your **OUTPUT_DIR** (an absolute path). Write only there.

## Goal

Find, from real public evidence, the pains that developers, QA and product people have when they report, reproduce
and fix bugs (especially web and browser bugs) with AI coding agents (Claude Code, Cursor, Codex, Copilot coding agent,
Jules, Devin, OpenHands, Roo Code, opencode, Windsurf and similar), and how they say they want it fixed.
Then rank the pains and turn the best into small feature ideas for **Session Recorder by Proofline**, a free, open-source Chrome
extension that records a browser bug (clicks, console, network, screenshots, annotations, narration) and files a
GitHub issue or exports a `report.md` ZIP for a coding agent.

The final pick must be buildable as **one clean pull request** (a few hundred lines, with tests) by one engineer.

## Read first (do not edit these)

1. `<mission>/research/00-context-notes.md`: everything known so far, including the open PRs that must not be duplicated.
2. `<mission>/session-recorder-chrome-extension/README.md`, `PRODUCT.md`, `docs/report-format.md`, `docs/PLAN.md`.
   The source code is in the same folder (`entrypoints/`, `lib/`) if you need to check what already exists.

## Guardrails (every story)

1. Write files only inside your OUTPUT_DIR. Never edit the extension repo, the notes, this PRD or any other folder.
2. **Independence:** never open, list or read anything under `<mission>/research/runs/` except your own OUTPUT_DIR.
3. No git commands that change anything (no commit, push, branch, clone). Do not open PRs, issues or comments anywhere. Do not sign in to anything.
4. Use web search and web fetch for evidence. Prefer: Reddit (r/ClaudeAI, r/cursor, r/ChatGPTCoding, r/webdev, r/QualityAssurance, r/programming, r/ExperiencedDevs), Hacker News, GitHub issues and discussions (anthropics/claude-code, getcursor/cursor, openai/codex, All-Hands-AI/OpenHands, RooCodeInc/Roo-Code, sst/opencode, ChromeDevTools/chrome-devtools-mcp, microsoft/playwright-mcp, github/copilot-cli and community discussions), Cursor forum, Chrome Web Store reviews of bug-report extensions (Jam, Marker.io, BetterBugs, Darnly, FlowLens), G2 and Product Hunt comments, vendor docs and changelogs.
   Use **every** search tool you have (see "Search toolkit" below): your web search tool, your web fetch tool, AND the public JSON APIs through `curl` in the shell. Popular pages matter most: sort by top, reactions or points.
5. **Never invent evidence.** Every claim cites a real URL you actually opened or saw in results. Quotes are verbatim and at most 30 words. If you could not open a page, mark it `unverified`. Vendor marketing counts as weak evidence; say so.
6. Keep personal data out: cite usernames only when they are part of a public URL; never copy emails.
7. Write plain, short English. Dates as `YYYY-MM-DD`.

## Search toolkit (use all of it)

Read-only public endpoints. Always send a generic user agent: `curl -sL -A "pain-research/1.0" "<url>"`. Never send
names, emails or tokens. Pause about 2 seconds between calls to the same host. Save raw JSON you rely on under
`OUTPUT_DIR/raw/` (small files only) so the owner can check it.

- **Web search tool** (`web_search` / `WebSearch`): broad queries, then `site:reddit.com`, `site:news.ycombinator.com`, `site:github.com`, `site:forum.cursor.com`.
- **Web fetch tool** (`web_fetch` / `WebFetch`): open every page you cite.
- **GitHub issues, most-reacted first** (no token needed, 10 calls a minute):
  `https://api.github.com/search/issues?q=repo:anthropics/claude-code+browser+console&sort=reactions&order=desc&per_page=20`
  Also try `sort=comments`, `is:issue`, and labels such as `label:enhancement`. Read reactions (`reactions.total_count`, `+1`) and `comments` as the popularity signal.
- **GitHub repo discovery:** `https://api.github.com/search/repositories?q=bug+report+mcp+agent&sort=stars&order=desc`
- **Reddit, top posts:** `https://www.reddit.com/r/ClaudeAI/search.json?q=browser+console&restrict_sr=1&sort=top&t=year&limit=25`
  and the comments of a post: `https://www.reddit.com/r/<sub>/comments/<id>.json?limit=50&sort=top`. Use `score` and `num_comments` as the signal. If Reddit blocks the request, use web search with `site:reddit.com` and say so in `run-summary.md`.
- **Hacker News (Algolia):** `https://hn.algolia.com/api/v1/search?query=coding+agent+browser+bug&tags=story` and `tags=comment`; use `points` and `num_comments`.
- **Chrome Web Store, Product Hunt, G2:** web fetch the listing or review pages of Jam, Marker.io, BetterBugs, Darnly, FlowLens, Faylee and similar; low-star reviews show the pain.

Popular places to cover (at least 8 of them):
anthropics/claude-code, getcursor/cursor and forum.cursor.com, openai/codex, github/copilot-cli and github community
discussions, All-Hands-AI/OpenHands, RooCodeInc/Roo-Code, sst/opencode, cline/cline, ChromeDevTools/chrome-devtools-mcp,
microsoft/playwright-mcp, BrowserMCP or browser-use, r/ClaudeAI, r/cursor, r/ChatGPTCoding, r/webdev,
r/QualityAssurance, r/ExperiencedDevs, Hacker News, Chrome Web Store reviews.

## Output layout (inside OUTPUT_DIR)

```
plan.md              US-001: search plan
nodes/P01-<slug>.md  US-002: one file per pain point ("node"), P01, P02, ...
sources.md           US-002/003: every URL with status verified | unverified | dropped
ranking.md           US-004: ranked tables and reasoning
ranking.json         US-004: machine-readable ranking (schema below)
recommendation.md    US-005: top 3 feature specs for Session Recorder
run-summary.md       US-005: what you did, counts, limits of your evidence
```

### Node file format (`nodes/P01-<slug>.md`)

```markdown
---
id: P01
title: <pain in the user's words, one line>
who: <developers | QA | product | agent users ...>
tools: [<agents or products involved>]
status: verified | partly-verified | unverified
---
## Pain
<2-4 sentences>
## Evidence
- <URL> (<source type: reddit | hn | github-issue | forum | review | blog | vendor-doc>, <date if known>, verified|unverified): "<quote ≤30 words>" <signal: upvotes, +1s, comments if visible>
## How users want it fixed
- <what they asked for, cite URL>
## Workarounds people use today
- <...>
## Session Recorder angle
<could the extension help? what already exists? which open PR overlaps (by number), if any?>
## Scores
frequency: <0-5>  severity: <0-5>  fit: <0-5>  smallness: <0-5>  novelty: <0-5>
```

### Scoring rubric (use exactly this)

- **frequency** 0-5: 0 = one weak mention, 3 = several independent sources, 5 = many sources with high engagement.
- **severity** 0-5: how much time, money or trust the pain costs.
- **fit** 0-5: how directly Session Recorder (a browser bug recorder that writes reports for agents) can address it.
- **smallness** 0-5: 5 = one clean PR of a few hundred lines with tests; 0 = a new product.
- **novelty** 0-5: 5 = nothing in the extension or its open PRs covers it; 0 = already done or an open PR does it.
- **pain_score** = 2*frequency + 2*severity (max 20): how much the world hurts.
- **pick_score** = 2*frequency + 2*severity + 2*fit + smallness + novelty (max 40): how good it is as our PR.

### `ranking.json` schema

```json
{
  "agent": "<agent/model as given in your OUTPUT_DIR name>",
  "generated": "YYYY-MM-DD",
  "nodes": [
    {"id": "P01", "title": "...", "frequency": 0, "severity": 0, "fit": 0, "smallness": 0, "novelty": 0,
     "pain_score": 0, "pick_score": 0, "verified_sources": 0, "overlapping_prs": [48],
     "feature_idea": "one line", "top_sources": ["https://..."]}
  ],
  "pain_rank": ["P03", "P01"],
  "pick_rank": ["P01", "P03"],
  "top_pick": {"node": "P01", "feature": "one line"}
}
```

## Stories

### US-001: Plan the search
Read the files in "Read first". Write `plan.md`: at least 15 concrete search queries across at least 6 source types,
and at least 6 hypotheses you will test (the five pains in section 5 of the notes, plus one on vision and video: PR
review and agents missing visual or video evidence), and look for pains the notes missed.

### US-002: Collect evidence into nodes
Run the searches. Write at least 12 node files (aim for 15-20), each with at least 2 evidence links, and at least 3
nodes that are NOT already listed in section 5 of the notes. Record every URL in `sources.md`.
Look for: pains about context the agent lacks (browser, console, network, UI state, auth, environment), reproduction,
hand-off friction, issue quality, privacy and secrets, cost, verifying that a fix worked, flaky fixes, triage and duplicates.

**Vision and video (required area, at least 2 nodes if evidence exists):** look for pains and missing tools around
(a) visual checks in PR review: AI reviewers and PR agents that cannot see the UI a change produces, visual regression
and screenshot diffs, before/after screenshots in PRs; (b) agents that cannot use screenshots or images in issues
(for example CLI agents without image paste); (c) video: agents that cannot watch a screen recording, the need to turn a bug
video into key frames, a timeline or text an agent can read, and video-analysis tools for bug reports (Jam, Loom, Marker.io AI
features and similar). Search GitHub issues for terms like `screenshot`, `image`, `vision`, `video`, `visual regression`
in the popular repos. Only propose a vision or video feature for Session Recorder if the evidence shows a real gap; say plainly
if it does not. Session Recorder already records tab video, screenshots and annotations, so check what an agent can use from them today.

### US-003: Verify and clean
Open every cited URL with web fetch. Set its status in `sources.md` and in each node. Merge duplicate nodes, drop
claims with no verified source, and set each node's `status`. Add a line at the top of `sources.md`:
`verified: N, unverified: N, dropped: N`.

### US-004: Score and rank
Score every node with the rubric. Write `ranking.md` with two tables (by `pain_score`, by `pick_score`), the scores,
and two or three sentences on why the top five are ordered that way. Write `ranking.json` that matches the schema and parses as JSON.

### US-005: Recommend and summarise
Write `recommendation.md`: the top 3 feature ideas for Session Recorder by pick_score. For each: the user and their pain
(cite nodes), the feature in one paragraph, the UX (where it lives, how many clicks), the files likely touched
(check the source tree under the extension folder), how to test it (unit and Playwright), risks, and which open PR it must not duplicate.
Then write `run-summary.md`: what you searched, counts (queries, sources, verified, nodes), and the weaknesses of your evidence.
