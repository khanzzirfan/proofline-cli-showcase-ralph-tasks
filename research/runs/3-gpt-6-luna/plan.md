# US-001: Search plan

## Scope and constraints

- Research public reports by developers, QA and product people who hand browser bugs to AI coding agents. Prefer first-person accounts, issue discussions and concrete workarounds over vendor claims.
- Use the web search tool for discovery, web fetch to open every source eventually cited, and read-only public JSON APIs through `curl -sL -A "pain-research/1.0" "<url>"`. Save only small raw JSON responses relied on to `raw/` in this output directory. Pause about two seconds between calls to the same host.
- Track source URLs and status in `sources.md`; do not treat search snippets alone as verified evidence. Note visible engagement (votes, reactions, points, comments) and date. Keep quotes verbatim and at most 30 words; exclude personal emails and unnecessary personal data.
- Search across agent repos, community forums, developer/QA subreddits, Hacker News, browser automation tooling, bug-report products and vendor documentation/reviews. Seek evidence for pain beyond the existing notes before prioritizing candidate features.
- Session Recorder already captures browser interactions, console/network, screenshots, annotations, optional voice and tab video, and exports a structured `report.md` ZIP or files GitHub issues. Evaluate actual handoff and agent access to report assets, not merely capture availability. Avoid duplicating open extension PRs: #49, #48, #47, #46, #45, #44, #43, #42, #41, #40, #39, #38, #37, #33, #32, #31, #30, #29, #25, #24, #23 and #21. #22 is closed, not an open PR.

## Hypotheses to test

1. **Browser context is missing to agents.** Users cannot give an agent the live UI state, DOM, console, network activity or authenticated browser context it needs, so frontend debugging becomes guesswork. Test whether this repeats across Claude Code, Cursor and other agent communities, and distinguish existing browser/MCP integrations from unresolved gaps.
2. **Evidence handoff costs time and loses signal.** Users manually copy logs, cURL/HAR, screenshots or reproduction steps into prompts/issues; long or misplaced pasted output may be ignored, truncated or detached from its context.
3. **Routing a bug to an agent is fragmented.** Users want a report or browser session to reach the right local/cloud coding agent through a direct, portable handoff (including MCP or issue assignment) rather than a bespoke integration per agent.
4. **Fix verification lacks trustworthy visual/browser proof.** Users want agents to reproduce the failure, run the changed app, and attach evidence that the fix works; a passing test or textual PR summary may not establish the UI outcome.
5. **Evidence sharing creates privacy and safety concerns.** Captured logs, URLs, screenshots, request data or local tools may expose secrets or sensitive user data; users need clear, reliable redaction and safe boundaries for agent access.
6. **Agents and reviewers lack usable visual/video evidence.** Screenshots/images may not be consumable by some CLI agents or PR reviewers, and recordings may need keyframes, a timeline or text; verify whether this is a real gap despite Session Recorder's existing screenshot, annotation and video capture/export.
7. **Additional pain missed by prior notes.** Search for recurring problems around reproduction reliability, flaky fixes, environment/auth setup, duplicate triage, report quality, evidence size/context limits, cost and browser automation breakage. Promote only distinct, sourced pains.

## Search queries

Run broad discovery first, then targeted searches. Adjust wording to surface high-engagement first-person reports and sort by top, reactions or points where supported.

| # | Source type | Concrete query / endpoint | What it tests |
|---|---|---|---|
| 1 | Web search | `AI coding agent cannot see browser console network frontend bug debugging user complaint` | Browser context gap |
| 2 | Reddit search | `site:reddit.com/r/ClaudeAI Claude Code browser console inspect frontend bug agent` | Browser context in Claude workflows |
| 3 | Reddit search | `site:reddit.com/r/cursor Cursor agent browser console network tab copy paste logs` | Cursor context and handoff friction |
| 4 | Reddit search | `site:reddit.com/r/ChatGPTCoding coding agent reproduce bug screenshot browser visual` | Reproduction and visual evidence |
| 5 | Reddit search | `site:reddit.com/r/webdev AI agent debugging frontend bug reports reproduction steps` | Developer workflows and missed pains |
| 6 | Reddit search | `site:reddit.com/r/QualityAssurance AI coding agents QA flaky reproduction evidence screenshots` | QA-specific pains |
| 7 | Reddit search | `site:reddit.com/r/ExperiencedDevs AI coding agent verify fix browser tests trust` | Trust and verification |
| 8 | Reddit top-post JSON API | `https://www.reddit.com/r/ClaudeAI/search.json?q=browser+console&restrict_sr=1&sort=top&t=year&limit=25` | Top posts, score and comments for the required Reddit API sample; follow relevant post-comment JSON endpoints sorted by top |
| 9 | Hacker News search | `AI coding agents browser debugging bug reproduction screenshot evidence` | Independent discussion and workarounds |
| 10 | Hacker News Algolia JSON API | `https://hn.algolia.com/api/v1/search?query=coding+agent+browser+bug&tags=story` and `https://hn.algolia.com/api/v1/search?query=coding+agent+browser+bug&tags=comment` | Required HN story/comment API samples; record points and comment counts, prioritize high-engagement results |
| 11 | GitHub issue search | `site:github.com/anthropics/claude-code/issues browser console DOM screenshot image video` | Agent-repo feature requests and blockers |
| 12 | GitHub reactions JSON API | `https://api.github.com/search/issues?q=repo:anthropics/claude-code+browser+console&sort=reactions&order=desc&per_page=20` | Required GitHub reactions-first API sample; capture reactions and comments |
| 13 | GitHub comments JSON API | `https://api.github.com/search/issues?q=repo:anthropics/claude-code+browser+console&sort=comments&order=desc&per_page=20` | Popularity cross-check using comments |
| 14 | GitHub issue search | `site:github.com/getcursor/cursor/issues (screenshot OR image OR vision OR video OR browser OR console) bug` | Cursor agent visual/browser limitations and requests |
| 15 | Cursor forum | `site:forum.cursor.com agent cannot access browser console network tab copy paste terminal output` | Direct user reports, desired fixes and workarounds |
| 16 | GitHub issue search | `site:github.com/openai/codex/issues screenshot image paste browser visual bug reproduce` | CLI/image input and bug workflow limits |
| 17 | GitHub issues/discussions | `site:github.com/github/copilot-cli OR site:github.com/orgs/community/discussions coding agent screenshot visual input issue browser fix verification` | Copilot visual input and cloud-agent verification expectations |
| 18 | GitHub issue search | `site:github.com/All-Hands-AI/OpenHands/issues browser screenshot video console reproduction` | OpenHands browser/debug evidence needs |
| 19 | GitHub issue search | `site:github.com/RooCodeInc/Roo-Code/issues screenshot image vision browser console bug` | Roo Code image/browser workflows |
| 20 | GitHub issue search | `site:github.com/sst/opencode/issues image paste screenshot browser agent visual` | opencode CLI image evidence constraints |
| 21 | GitHub issue search | `site:github.com/cline/cline/issues screenshot image paste vision browser debug` | Cline image/vision constraints and requests |
| 22 | GitHub issue search | `site:github.com/ChromeDevTools/chrome-devtools-mcp/issues browser console network screenshot agent reproduce` | Browser tooling gaps, reliability and requested capabilities |
| 23 | GitHub issue search | `site:github.com/microsoft/playwright-mcp/issues screenshot video visual regression browser agent` | Playwright MCP evidence and verification limitations |
| 24 | GitHub repo discovery API | `https://api.github.com/search/repositories?q=bug+report+mcp+agent&sort=stars&order=desc` | Discover agent-ready bug-report tools; use stars as discovery signal, not proof of user pain |
| 25 | Browser tool / community | `site:github.com/browser-use OR site:github.com/BrowserMCP screenshot image video browser bug agent issue` | Browser-use/MCP workaround and coverage boundaries |
| 26 | GitHub issue search | `site:github.com/(anthropics/claude-code OR getcursor/cursor OR openai/codex OR github/copilot-cli OR All-Hands-AI/OpenHands OR RooCodeInc/Roo-Code OR sst/opencode OR cline/cline)/issues (screenshot OR image OR vision OR video OR "visual regression")` | Cross-agent visual and video evidence; refine into repo-specific searches if query syntax is unsupported |
| 27 | Web search / PR review | `AI code review agent cannot see rendered UI screenshot visual regression before after screenshot pull request` | Visual review proof and reviewer blind spots |
| 28 | Web search / issue reports | `"video" "bug report" AI coding agent watch screen recording key frames` | Whether agents can consume video or need timeline/keyframes |
| 29 | Product review | `Jam bug report Chrome extension review limitations screenshots console AI agent` | Low-star/critical user feedback and workarounds; vendor/product context is weak evidence |
| 30 | Product review | `Marker.io review bug reporting browser console screenshot issue agent` | Review pain around capture, collaboration and issue handoff |
| 31 | Chrome Web Store review | `site:chromewebstore.google.com/detail Darnly bug reports for AI reviews` and `site:chromewebstore.google.com FlowLens bug report reviews` | Review evidence for AI-oriented browser bug reports; fetch available listing/review pages |
| 32 | Product Hunt / G2 | `site:producthunt.com/products/flowlens-ai-native-bug-reports comments` and `site:g2.com Jam bug reporting reviews` | Adoption feedback and negative product reviews; treat promotional/platform data cautiously |
| 33 | Vendor documentation | `GitHub Copilot coding agent visual inputs screenshots issue documentation` | What cloud agents officially support and how users are expected to provide visual context |
| 34 | Vendor documentation | `Jules GitHub issue screenshot image coding agent documentation` and `OpenHands GitHub issue screenshot agent documentation` | Agent-trigger workflow and supported evidence formats |
| 35 | Vendor documentation / tool docs | `Jam MCP bug report agent handoff Darnly FlowLens Faylee MCP report` | Existing handoff products, formats, requirements and limitations; marketing claims are weak evidence |
| 36 | Web search / security | `AI bug report extension redact secrets screenshot logs MCP localhost security coding agent` | Redaction failures, safe sharing and local-agent tool boundaries |
| 37 | Web search / debugging | `AI coding agent flaky fix cannot reproduce bug environment auth browser state issue report` | Reproduction, auth and environment gaps beyond prior notes |
| 38 | Web search / triage | `AI coding agent duplicate GitHub bug issues triage poor bug report reproduction steps` | Duplicate triage and issue-quality pains |
| 39 | Web search / context limits | `coding agent pasted logs too long context window bug report evidence token limit` | Context-budget and report-size pains |
| 40 | Web search / cost and trust | `AI coding agent repeatedly retries browser debugging expensive verify fix users` | Cost, retries and trust impacts |

## Evidence and analysis sequence

1. Search broad web, Reddit, HN, GitHub and relevant forums for concrete user statements. Query popular agent and browser-tool repos separately; include at least eight of the required locations over the collection run.
2. Use GitHub reactions/comments, Reddit score/comments and HN points/comments to sort candidates. Save small raw API JSON in `raw/` only when it informs a cited claim or popularity assessment. If Reddit JSON is blocked, record that limitation and use `site:reddit.com` search results instead.
3. Inspect relevant issue threads, comments and linked product/review pages with web fetch. Separate direct user evidence from vendor docs, marketing and secondary commentary. Search results can discover a URL but do not by themselves establish a verified quote.
4. Cluster repeated, distinct pains into node files. Preserve a source URL for each claim; drop unsupported claims and merge duplicate descriptions. Include at least three pains not in the five baseline hypotheses if public evidence supports them.
5. Include a dedicated visual/video assessment. Check screenshots and image attachments in issues, CLI-agent paste support, AI PR reviewer UI visibility, visual regression artifacts, and video/keyframe support. Compare any claimed gap with Session Recorder’s current screenshots, annotations, video ZIP assets and report instructions. Do not recommend a new capture capability if an evidenced gap is only in transfer/consumption, or if the agent already consumes the exported asset.
6. For each retained pain, record current workarounds, what people explicitly ask for, source quality and engagement. Then score with the PRD rubric and check candidate work against the extension’s existing behavior and open PR list before recommending.
