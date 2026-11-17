verified: 25, unverified: 0, dropped: 3

# Sources

Every URL cited in the nodes, with its status. "verified" = opened via `web_fetch` (HTTP 200 and content read) or read verbatim from the GitHub search API (title + reactions). "unverified" = could not open. "dropped" = attempted but unusable (blocked or renamed). Dates are `YYYY-MM-DD` where the source shows one.

## Popular places covered (>= 8 required)

anthropics/claude-code · openai/codex · github/copilot-cli · All-Hands-AI/OpenHands · RooCodeInc/Roo-Code · cline/cline · ChromeDevTools/chrome-devtools-mcp · microsoft/playwright-mcp · microsoft/vscode-pull-request-github · forum.cursor.com · Hacker News · Chrome Web Store review ecosystem (via a QA comparison of Jam / BetterBugs / Marker.io / Loom). Reddit (`r/ClaudeAI`, `r/cursor`, `r/ChatGPTCoding`, `r/QualityAssurance`) was attempted but blocked (see dropped).

## Verified sources (cited in nodes)

| URL | Type | Date | Used in |
|---|---|---|---|
| https://github.com/anthropics/claude-code/issues/57034 | github-issue | 2026-05-07 | P01 |
| https://github.com/anthropics/claude-code/issues/52907 | github-issue | 2026-04-24 | P01, P13 |
| https://reposquare.com/claude-code-browser-access/ | blog | 2026-10-31 | P01 |
| https://dev.to/dedupedai/let-claude-code-or-cursor-debug-your-page-in-a-real-chrome-browser-ldc | blog | — | P01 |
| https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803 | forum | — | P02 (title only) |
| https://news.ycombinator.com/item?id=48795580 | hn | — | P02, P03 |
| https://github.com/anthropics/claude-code/issues/18170 | github-issue | 2026-01-14 | P02 (title via search API) |
| https://news.ycombinator.com/item?id=46047931 | hn | — | P03, P10, P12 |
| https://vibehacker.com/news/faylee-turns-a-bug-report-into-one-link-your-coding-agent-can-open-over-mcp-and- | news | 2026-10-31 | P03, P06 |
| https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs | vendor-doc | — | P04 |
| https://github.com/anthropics/claude-code/issues/75632 | github-issue | 2026-07-08 | P04 |
| https://www.browseract.com/blog/github-copilot-browser-automation | blog | — | P04, P06, P13, P14 |
| https://github.com/microsoft/vscode-pull-request-github/issues/7770 | github-issue | 2025-09-07 | P05 |
| https://blog.sandbase.ai/multimodal-coding-agents-screenshot-to-fix-2026/ | blog | 2026-08-22 | P05, P06, P09, P11, P14 |
| https://blog.gitguardian.com/ai-coding-agents-credential-security/ | blog | 2026-09 | P06 |
| https://github.com/anthropics/claude-code/issues/30925 | github-issue | 2026-03-05 | P07 |
| https://github.com/anthropics/claude-code/issues/32005 | github-issue | 2026-03-08 | P07, P09 |
| https://github.com/anthropics/claude-code/issues/12676 | github-issue | 2025-11-29 | P08 |
| https://rumana.dev/blog/visual-bug-reporting-tools-compared | blog | 2026-04-01 | P09, P12 |
| https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/171 | github-issue | 2025-09-26 | P10 (title via search API) |
| https://github.com/microsoft/playwright-mcp/issues/889 | github-issue | 2025-08-14 | P10 (title via search API) |
| https://news.ycombinator.com/item?id=47570359 | hn | — | P11 |
| https://news.ycombinator.com/item?id=49119881 | hn | — | P12 |
| https://github.com/anthropics/claude-code/issues/13480 | github-issue | 2025-12-09 | P15 |
| https://github.com/anthropics/claude-code/issues/56016 | github-issue | 2026-05-04 | P15 |

## Dropped / blocked sources

- Reddit `search.json` for `r/ClaudeAI`, `r/cursor`, `r/ChatGPTCoding`, `r/QualityAssurance` — returned an HTML block page (no JSON), so no Reddit evidence was cited. Fall back to web search with `site:reddit.com` returned only subreddit home pages, no usable threads.
- `https://api.github.com/search/issues?q=repo:getcursor/cursor+...` — HTTP 422 (repo renamed/unavailable).
- `https://api.github.com/search/issues?q=repo:sst/opencode+...` — HTTP 422 (repo renamed). `All-Hands-AI/OpenHands` also 422; re-searched as `OpenHands/OpenHands` (low signal, no vision pain worth a node).

## Raw JSON kept for the owner

- `raw/gh-claude-*.json`, `raw/gh-*.json` — GitHub search API responses (reactions/comments signals).
- `raw/hn-*.json` — HN Algolia responses (points/comments).
- `raw/reddit-*.json` — the blocked Reddit HTML (for transparency; not real data).
