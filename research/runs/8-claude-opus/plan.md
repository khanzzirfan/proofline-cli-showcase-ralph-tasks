# Search plan: run 8-claude-opus

Date: 2026-11-17. Agent: claude (opus). OUTPUT_DIR: `research/runs/8-claude-opus`.

## 1. What I read first

- `research/00-context-notes.md`: mission, open extension PRs (#21 to #49), the five pains in section 5, candidate features A to D.
- Extension `README.md`, `PRODUCT.md`, `docs/report-format.md`, `docs/PLAN.md`, and a look at `lib/export/`.

Facts that shape the plan:

- The ZIP already holds `report.md`, `session.json`, `MANIFEST.md`, screenshots (`{seq}-{mmss}.jpg`), network files, `video/*.webm` clips (Full and Standard only) and audio.
- At Compact and Minimal, video bytes are dropped and only clip times stay. Most text-only coding agents cannot read `.webm` at all, so the video is close to useless to an agent today. That is a lead for the vision and video hypothesis.
- Handing a report to an agent is manual: export ZIP, unzip, paste `report.md`, copy the prompt from the docs (`copyIssue` only copies issue Markdown).
- Crowded areas to avoid: redaction (5 PRs: #31 #37 #38 #42 #44), HAR (#32), cURL (#43), env info (#29), labels and assignees (#48), duplicate grouping (#49), Linear (#24), Playwright repro (#22, closed).

## 2. Hypotheses to test

Each hypothesis says what would confirm it and what would kill it.

| ID | Hypothesis | Confirm if | Reject if |
|---|---|---|---|
| H1 | **Agents can't see the browser.** Agents lack console, network, DOM and UI state, so they guess at front-end bugs. (notes 5.1) | Several high-reaction GitHub issues or forum threads ask for console/network/DOM access; MCP tools for this get many stars. | Users say chrome-devtools-mcp or Playwright MCP has solved it. |
| H2 | **Copy-paste hand-off is slow and lossy.** Users paste logs, HAR, cURL and screenshots by hand; pastes get truncated or lost; tokens leak. (notes 5.2) | Threads describing paste failures, truncated logs, context limits from huge logs. | Little evidence beyond the two known Cursor threads. |
| H3 | **People want bug reports delivered straight to the agent** (MCP, one link, or a prompt), not a ZIP. (notes 5.3) | Jam MCP / Faylee / FlowLens usage, issues asking for "send to agent", review comments asking for agent hand-off. | Only vendor marketing, no user voices. |
| H4 | **Cloud agents start from GitHub issues, and issue quality decides the result.** Vague issues without repro steps cause wrong fixes; users want an issue template agents can act on. (notes 5.4) | Posts saying Copilot/Jules/Codex/OpenHands failed on vague issues; requests for repro steps or acceptance criteria. | Agents are reported to work fine from thin issues. |
| H5 | **Secrets and privacy in shared evidence.** Logs, HAR and screenshots sent to agents leak tokens or PII. (notes 5.5) | Incidents or worries about agents reading `.env`, tokens in logs, HAR leaks. | Little user concern. Note: crowded in the extension already. |
| H6 | **Vision and video gap.** (a) AI PR reviewers and PR agents can't see the UI the change produces, and before/after screenshots in PRs are unreliable; (b) CLI agents can't take screenshots or images from issues (no image paste, images in issues ignored); (c) agents can't watch a screen recording, so users want a video turned into key frames, a timeline or text. | GitHub issues in claude-code / codex / opencode / copilot-cli asking for image paste, image in issue, video input; vendor features (Jam AI, Loom, Marker.io) that turn video into text; complaints that agents ignore screenshots. | Agents already read images in issues everywhere and nobody asks for video. |
| H7 | **Verifying that a fix worked.** Agents claim "fixed" without running the app; users must re-test by hand; no proof in the PR. (beyond notes) | Complaints about agents declaring success, requests for agents to self-verify in the browser. | Rare. |
| H8 | **Reproduction is the bottleneck.** Agents and devs can't reproduce user bugs (auth, environment, data, timing), "works on my machine". (beyond notes) | QA and dev threads on repro steps being missing or wrong. | — |
| H9 | **Token and cost blow-up from raw evidence.** Huge console or network dumps or screenshots eat context or credits; users want trimmed, relevant evidence. (beyond notes) | Issues about context overflow from logs, screenshot token cost, MCP tools returning too much. | — |
| H10 | **Flaky or regressing fixes and duplicate triage.** Agents fix one thing and break another; teams drown in duplicate bug reports. (beyond notes) | Threads about regressions after agent fixes; triage pain in QA subs. | — |
| H11 | **Auth and session state.** Agents' browsers can't log in or reuse the user's session, so they can't reach the bug. (beyond notes) | Issues on playwright-mcp / chrome-devtools-mcp about login, cookies, existing profile. | — |

## 3. Queries

At least two per source type. Every API call uses `curl -sL -A "pain-research/1.0"`, waits about 2 s between calls to the same host, and saves raw JSON I rely on to `raw/`.

### A. GitHub issues API, sorted by reactions (source type: github-issue)

| # | Query URL (abbreviated host `https://api.github.com/search/issues?`) | Tests |
|---|---|---|
| Q1 | `q=repo:anthropics/claude-code+browser+console&sort=reactions&order=desc&per_page=20` | H1 |
| Q2 | `q=repo:anthropics/claude-code+image+paste+is:issue&sort=reactions&order=desc&per_page=20` | H6b |
| Q3 | `q=repo:anthropics/claude-code+video+is:issue&sort=reactions&order=desc&per_page=20` | H6c |
| Q4 | `q=repo:openai/codex+screenshot+OR+image+is:issue&sort=reactions&order=desc&per_page=20` | H6b |
| Q5 | `q=repo:ChromeDevTools/chrome-devtools-mcp+is:issue&sort=reactions&order=desc&per_page=30` | H1, H9, H11 |
| Q6 | `q=repo:microsoft/playwright-mcp+is:issue&sort=reactions&order=desc&per_page=30` | H1, H9, H11 |
| Q7 | `q=repo:sst/opencode+image+OR+screenshot+is:issue&sort=reactions&order=desc&per_page=20` | H6b |
| Q8 | `q=repo:All-Hands-AI/OpenHands+browser+OR+screenshot+is:issue&sort=reactions&order=desc&per_page=20` | H1, H6 |
| Q9 | `q=repo:RooCodeInc/Roo-Code+browser+is:issue&sort=reactions&order=desc&per_page=20` | H1 |
| Q10 | `q=repo:cline/cline+browser+OR+console+is:issue&sort=reactions&order=desc&per_page=20` | H1 |
| Q11 | `q=repo:github/copilot-cli+image+OR+screenshot&sort=reactions&order=desc&per_page=20` | H6b |
| Q12 | `q=repo:anthropics/claude-code+"verify"+OR+"claims+fixed"+is:issue&sort=comments&order=desc&per_page=20` | H7 |
| Q13 | `q=repo:anthropics/claude-code+context+log+too+large+is:issue&sort=reactions&order=desc&per_page=20` | H9 |
| Q14 | `q=visual+regression+screenshot+pull+request+agent+is:issue&sort=reactions&order=desc&per_page=20` | H6a |

### B. GitHub repo discovery (source type: github-repo)

| # | Query | Tests |
|---|---|---|
| Q15 | `https://api.github.com/search/repositories?q=bug+report+mcp+agent&sort=stars&order=desc` | H3 |
| Q16 | `https://api.github.com/search/repositories?q=browser+console+logs+mcp&sort=stars&order=desc` | H1 |
| Q17 | `https://api.github.com/search/repositories?q=video+to+frames+llm+bug&sort=stars&order=desc` | H6c |

### C. Reddit JSON, top of the year (source type: reddit)

| # | Query URL | Tests |
|---|---|---|
| Q18 | `https://www.reddit.com/r/ClaudeAI/search.json?q=browser+console&restrict_sr=1&sort=top&t=year&limit=25` | H1 |
| Q19 | `https://www.reddit.com/r/cursor/search.json?q=screenshot+bug&restrict_sr=1&sort=top&t=year&limit=25` | H6 |
| Q20 | `https://www.reddit.com/r/ChatGPTCoding/search.json?q=frontend+bug+agent&restrict_sr=1&sort=top&t=year&limit=25` | H1, H8 |
| Q21 | `https://www.reddit.com/r/QualityAssurance/search.json?q=bug+report+AI&restrict_sr=1&sort=top&t=year&limit=25` | H4, H8, H10 |
| Q22 | `https://www.reddit.com/r/webdev/search.json?q=claude+code+says+fixed&restrict_sr=1&sort=top&t=year&limit=25` | H7 |
| Q23 | `https://www.reddit.com/r/ExperiencedDevs/search.json?q=AI+agent+bug+reproduce&restrict_sr=1&sort=top&t=year&limit=25` | H8 |

Comments of strong posts: `https://www.reddit.com/r/<sub>/comments/<id>.json?limit=50&sort=top`. If Reddit blocks `curl`, fall back to web search with `site:reddit.com` and record the block in `run-summary.md`.

### D. Hacker News Algolia (source type: hn)

| # | Query URL (host `https://hn.algolia.com/api/v1/search?`) | Tests |
|---|---|---|
| Q24 | `query=coding+agent+browser+bug&tags=story` | H1 |
| Q25 | `query=claude+code+screenshot&tags=comment` | H6 |
| Q26 | `query=chrome+devtools+mcp&tags=story` | H1, H9 |
| Q27 | `query=agent+said+it+fixed+the+bug&tags=comment` | H7 |
| Q28 | `query=bug+report+video+LLM&tags=story` | H6c |

Sort and quote by `points` and `num_comments`.

### E. Web search (source types: forum, blog, vendor-doc)

| # | Query | Tests |
|---|---|---|
| Q29 | `site:forum.cursor.com agent browser console network logs` | H1, H2 |
| Q30 | `site:forum.cursor.com paste image screenshot agent cannot see` | H6b |
| Q31 | `site:github.com/orgs/community/discussions copilot coding agent screenshot issue` | H4, H6 |
| Q32 | `AI code review cannot see UI visual regression screenshot pull request` | H6a |
| Q33 | `coding agent watch screen recording video bug report key frames` | H6c |
| Q34 | `Jam.dev AI video bug report agent MCP` and `Marker.io AI` | H3, H6c |
| Q35 | `Copilot coding agent vague issue wrong fix reproduction steps` | H4 |
| Q36 | `site:reddit.com claude code "says it's fixed" but not fixed` | H7 |
| Q37 | `playwright mcp login session cookies existing browser profile` | H11 |
| Q38 | `chrome devtools mcp token usage screenshot context window` | H9 |

### F. Reviews (source type: review)

| # | Target | Tests |
|---|---|---|
| Q39 | Chrome Web Store reviews: Jam, Marker.io, BetterBugs, Darnly (web fetch listing pages, read low-star reviews) | H2, H3, H5 |
| Q40 | Product Hunt: FlowLens, Jam MCP / Jam AI launches; G2: Jam and Marker.io cons | H3, H6c |

## 4. Source types covered

github-issue (A), github-repo (B), reddit (C), hn (D), forum (E: Cursor forum, GitHub community discussions), blog and vendor-doc (E), review (F: Chrome Web Store, Product Hunt, G2). That is 7+ source types.

Places targeted (need at least 8): anthropics/claude-code, openai/codex, sst/opencode, All-Hands-AI/OpenHands, RooCodeInc/Roo-Code, cline/cline, github/copilot-cli and community discussions, ChromeDevTools/chrome-devtools-mcp, microsoft/playwright-mcp, forum.cursor.com, r/ClaudeAI, r/cursor, r/ChatGPTCoding, r/webdev, r/QualityAssurance, r/ExperiencedDevs, Hacker News, Chrome Web Store.

## 5. Method

1. Run Q1 to Q28 through `curl` (rate-limited; GitHub search allows 10 calls a minute without a token). Save useful JSON to `raw/` with names like `gh-claude-code-browser-console.json`, trimmed with `jq` to the fields used (title, html_url, reactions, comments, created_at).
2. Run Q29 to Q40 with web search, then open each candidate page with web fetch.
3. Group findings into nodes `nodes/P01-<slug>.md` (aim 15 to 20). At least 3 nodes outside section 5 of the notes, at least 2 on vision and video if evidence exists.
4. Log every URL in `sources.md` with status; quotes verbatim, 30 words or fewer.
5. For the vision and video area, also check what an agent can use from the current ZIP (screenshots yes if the agent reads images; `.webm` almost certainly not) and say plainly if there is no real gap.

## 6. Guardrails I will keep

- Write only inside OUTPUT_DIR. Never read other folders under `research/runs/`.
- No changing git commands, no PRs, issues, comments or sign-ins.
- No invented evidence; mark unopened pages `unverified`; vendor pages are weak evidence.
- No personal data beyond usernames that are part of a public URL.
