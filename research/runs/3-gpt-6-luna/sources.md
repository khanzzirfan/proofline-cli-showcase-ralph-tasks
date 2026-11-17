verified: 14, unverified: 4, dropped: 1

Counts are unique URLs cited in node Evidence sections: 14 verified and 4 unverified. One attempted OpenHands docs URL returned 404 and was dropped; it was discovery-only, not node evidence.

# Source coverage

Places searched (named): anthropics/claude-code, getcursor/cursor and forum.cursor.com, openai/codex, github/copilot-cli and GitHub Community discussions, All-Hands-AI/OpenHands, RooCodeInc/Roo-Code, sst/opencode, cline/cline, ChromeDevTools/chrome-devtools-mcp, microsoft/playwright-mcp, r/ClaudeAI, r/cursor, r/QualityAssurance, r/webdev and Hacker News. Useful opened evidence came primarily from Claude Code issues, GitHub Community, Hacker News, GitHub docs, tool repositories and vendor-authored technical posts. Repo-specific searches for OpenHands, Roo, opencode, Cline, DevTools MCP and Copilot CLI did not produce usable direct reports in this run.

## Verified node evidence URLs

- https://github.com/anthropics/claude-code/issues/57034 — GitHub issue, opened; 76 reactions (55 👍, 21 ❤️), 7 comments; browser sharing request.
- https://github.com/anthropics/claude-code/issues/52907 — GitHub issue, opened; 1 reaction; browser rendering/DOM inspection request.
- https://github.com/anthropics/claude-code/issues/75632 — GitHub issue, opened; 8 reactions, 9 comments; cloud browser verification request.
- https://github.com/anthropics/claude-code/issues/21371 — GitHub issue, opened; 79 reactions, 40 comments; Chrome MCP connection failure.
- https://github.com/anthropics/claude-code/issues/11791 — GitHub issue, opened; 17 reactions, 18 comments; web sandbox/browser automation limitation and workarounds.
- https://news.ycombinator.com/item?id=48795580 — HN item, opened; 6 points, 3 comments; comment reports avoiding manual console copy/paste.
- https://news.ycombinator.com/item?id=45293848 — HN item, opened; 2 points, 2 comments; comment describes missing expected-behavior assertions.
- https://github.com/rbsriram/heckle — GitHub project, opened; 3 stars; first-person maintainer pain and agent handoff workflow (promotional, not independent prevalence data).
- https://github.com/natethegreat/crit — GitHub project, opened; 2 stars; annotated visual-feedback workflow (project claims).
- https://github.com/orgs/community/discussions/169913 — GitHub Community discussion, opened; 3 comments; inconsistent/missing PR screenshot artifacts.
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs — GitHub vendor docs, opened; confirms Copilot cloud agent accepts image input.
- https://dev.to/branch42-labs/why-my-coding-agent-couldnt-see-my-apps-api-calls-and-the-3-fixes-i-use-4705 — first-person vendor blog, opened; auth/API context, credentials in cURL/HAR and network-volume concerns; promotional/weak generalization.
- https://dev.to/dedupedai/let-claude-code-or-cursor-debug-your-page-in-a-real-chrome-browser-ldc — vendor-authored tutorial, opened; describes browser debugging and structured network/console results; promotional/weak generalization.
- https://www.infosecurity-magazine.com/news/chrome-extension-ai-engine-act-mcp/ — security reporting, opened; 2025-04-25; local MCP exposure reporting, not coding-agent user-frequency evidence.

## Unverified node evidence URLs

Web fetch resolves these forum URLs but returns only page titles; the report text could not be checked. They are not used as sole support for any node’s main claim:

- https://forum.cursor.com/t/browser-automation-agent-cant-access-content-of-a-network-tab/151228 — cited in P06; title only, no body available.
- https://forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console-which-opens-inside-the-cursor-as-a-separate-tab/152452 — cited in P06; title only, no body available.
- https://forum.cursor.com/t/agent-can-t-access-browser-automation-tools-navigate-click-screenshot-even-though-browser-capabilities-page-lists-them-and-browser-automation-is-connected/148651 — cited in P05; title only, no body available.
- https://forum.cursor.com/t/browser-screenshot-tool-now-missing/145855 — cited in P05; title only, no body available.

## Other opened discovery URLs (not node evidence)

- https://forum.cursor.com/t/send-console-logs-browser-screenshot-as-context-to-cursor/26825 — web fetch returned only the page title; not used in a node.
- https://www.browserstack.com/docs/percy/ai-agents/visual-review-agent/overview — verified vendor docs; not cited in a node.
- https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/research-plan-iterate — fetched successfully after redirect to a general guide; not used as evidence for image-input claims.
- https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803 — opened only to title, not cited in a node.
- https://docs.openhands.dev/openhands/usage/run-openhands/github-action — fetch returned 404; dropped.

## Unverified (discovery only; not used as proof in nodes)

- https://www.reddit.com/r/QualityAssurance/comments/16i8vid/what_tools_do_you_use_to_capture_bugs/ — search snippet found but fetch hit a Reddit humanity challenge; excluded from node evidence.
- Broad web-search snippets about Codex, Roo, OpenHands, Cline, opencode, ChromeDevTools MCP and Playwright MCP are not used to assert node claims.

## Opened but not usable for intended claim

- https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/research-plan-iterate — fetched successfully after redirect to a general guide, but not relevant to the image-input claim; excluded from evidence counts.

## Dropped

- https://docs.openhands.dev/openhands/usage/run-openhands/github-action — web fetch returned 404.

## Vision and video search outcome

Visual coverage is evidenced by P08 (unreliable screenshots attached to PRs) and P09 (agent-specific image-input support/gaps). Search queries also targeted agents watching bug videos, turning recordings into key frames/timelines, and video analysis for bug reports. Results were mostly product promotion (including an Atrium QA Capture YouTube product video) or generic marketing; the YouTube page fetch exposed no substantive video transcript or user discussion. I found no separately verifiable first-person complaint specifically that coding agents cannot consume a bug recording, so I do not claim a video-specific pain. Session Recorder already captures video and screenshots in its ZIP, so the demonstrated concern is handoff/consumption, not missing recording capture.

## API records saved under raw/

- `raw/github-reactions.json` — required reactions-sorted Claude Code issue query; 852 matches; raw response is about 128 KB.
- `raw/reddit-top.json` — required Reddit top-search request; returned HTML network-security block, not JSON.
- `raw/hn-stories.json` and `raw/hn-comments.json` — required HN Algolia story and comment queries.
- `raw/codex-image.json`, `raw/openhands-browser.json`, `raw/roo-image.json`, `raw/cline-image.json`, `raw/opencode-image.json`, `raw/devtools-mcp.json`, `raw/playwright-mcp.json`, `raw/copilot-cli.json` — supplementary repo issue searches; some responses were rate-limited/error JSON or returned irrelevant matches.

## Search/tool limitations

Web search covered broad and source-specific queries, but several calls returned temporary 502 errors or irrelevant results. Web fetch opened all URLs cited as verified node evidence; Cursor forum pages returned titles only. Public curl APIs were used for GitHub reactions, Reddit top posts, HN stories/comments and repo issue searches. Reddit’s JSON endpoint was blocked by network security. No account login was used.
