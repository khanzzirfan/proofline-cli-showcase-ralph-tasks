verified: 51, unverified: 9, dropped: 1

US-003 re-check (2026-11-17): every cited URL was fetched again (HTTP status), and every quoted string in nodes/ was grepped against the page or API text (GitHub API body and comments, HN Algolia item, Discourse HTML). All quotes matched except the two Product Hunt quotes: those pages return 403 to curl, so they moved to unverified (they were vendor marketing and are not the main claim of any node; P03 relies on HN 46047931/48795580 and Darnly, P09 on cc#12676/#14805). The argos-ci.com page now loads (HTTP 200, title "Agents, show your work: media sharing puts screenshots on pull requests"); it is counted verified but is not cited in any node.

## Popular places covered (12 of the PRD list)
anthropics/claude-code, openai/codex (community.openai.com too), anomalyco/opencode (was sst/opencode), OpenHands, RooCodeInc/Roo-Code, cline/cline, ChromeDevTools/chrome-devtools-mcp, microsoft/playwright-mcp, forum.cursor.com, GitHub community discussions (Copilot), Hacker News, Chrome Web Store (Jam), Product Hunt (FlowLens, markupR). Also dev.to blogs.

## Tool status
- GitHub search API with `sort=reactions`: worked. Saved in `raw/gh*.json`, `raw/i-*.json`, `raw/j-*.json`. Plain keyword queries match issue bodies and return noise (account and usage-limit issues), so I used `in:title`.
- HN Algolia: worked. `raw/hn-*.json`.
- Reddit JSON (www and old.reddit): blocked, returned an HTML page. `site:reddit.com` web searches returned no Reddit threads either (3 tries). **No Reddit evidence in this run.** r/ClaudeAI, r/cursor, r/ChatGPTCoding, r/webdev, r/QualityAssurance, r/ExperiencedDevs are NOT covered.
- Cursor forum: Discourse `.json` endpoint worked (`raw/cf-*.json`).
- Chrome Web Store: Jam reviews opened. BetterBugs and Marker.io returned "This item is not available". G2 returned 403.
- Vision and video: searched (see P04 to P09). Evidence of a real gap in images for cloud agents, image size limits, and PR screenshots; video evidence is one 57-reaction request plus vendor pages.

## Verified (opened by API, curl or web fetch)
GitHub issues (reactions / comments as read from the API):
- https://github.com/anthropics/claude-code/issues/57034 (76 / 7)
- https://github.com/anthropics/claude-code/issues/75632 (8 / 3)
- https://github.com/anthropics/claude-code/issues/52907 (1 / 5)
- https://github.com/anthropics/claude-code/issues/37364 (0 / 3)
- https://github.com/anthropics/claude-code/issues/61075 (0 / 2)
- https://github.com/anthropics/claude-code/issues/101957 (11 / 4)
- https://github.com/anthropics/claude-code/issues/26831 (9 / 3)
- https://github.com/anthropics/claude-code/issues/1361 (49 / 70)
- https://github.com/anthropics/claude-code/issues/8324 (45 / 48, listing)
- https://github.com/anthropics/claude-code/issues/12644 (35 / 26)
- https://github.com/anthropics/claude-code/issues/13480 (90 / 111)
- https://github.com/anthropics/claude-code/issues/2939 (63 / 39, listing)
- https://github.com/anthropics/claude-code/issues/12676 (57 / 21)
- https://github.com/anthropics/claude-code/issues/14805 (1 / 7)
- https://github.com/anthropics/claude-code/issues/20298 (41 / 51, listing)
- https://github.com/anthropics/claude-code/issues/10646 (1 / 3, read only)
- https://github.com/anthropics/claude-code/issues/36559 (0 / 2, read only)
- https://github.com/openai/codex/issues/2221 (21 / 9)
- https://github.com/openai/codex/issues/57641 (42 / 53, listing)
- https://github.com/openai/codex/issues/39136 (44 / 82, listing)
- https://github.com/anomalyco/opencode/issues/906 (22 / 37)
- https://github.com/anomalyco/opencode/issues/15728 (10 / 12)
- https://github.com/OpenHands/OpenHands/issues/17637 (0 / 1)
- https://github.com/microsoft/playwright-mcp/issues/889 (13 / 15)
- https://github.com/microsoft/playwright-mcp/issues/395 (14 / 8)
- https://github.com/microsoft/playwright-mcp/issues/806 (9 / 3, listing)
- https://github.com/microsoft/playwright-mcp/issues/1211 (6 / 30, listing)
- https://github.com/microsoft/playwright-mcp/issues/403 (5 / 2, listing)
- https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/140 (61 / 29)
- https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/825 (32 / 21, listing)
- https://github.com/RooCodeInc/Roo-Code/issues/8045 (2 / 9, listing; browser screenshots shown as base64 text)
- https://github.com/cline/cline/issues/13263 (10 / 27, listing; not used in a node)
Forum and discussions:
- https://github.com/orgs/community/discussions/153112 (22 votes, 19 comments)
- https://community.openai.com/t/codex-ide-extension-no-image-read-hallucinating-playwright-review/1356235 (5 posts)
- https://forum.cursor.com/t/cursor-cloud-agents-do-not-post-their-screenshots-or-videos-to-pr/152974 (950 views, 17 posts)
- https://forum.cursor.com/t/agent-screen-captures-are-not-in-sync/173589 (61 views)
- https://forum.cursor.com/t/browser-take-screenshot-cursor-ide-browser-mcp-serves-cached-pngs-that-disagree-with-browser-snapshot-on-the-same-tab/160422 (124 views)
- https://forum.cursor.com/t/browser-automation-agent-cant-access-content-of-a-network-tab/151228 (177 views, 3 likes)
- https://forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console-which-opens-inside-the-cursor-as-a-separate-tab/152452 (260 views)
- https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803 (752 views)
Hacker News (Algolia items):
- https://news.ycombinator.com/item?id=47499672 (ProofShot, 161 points, 106 comments)
- https://news.ycombinator.com/item?id=46047931 (FlowLens, 5 / 2)
- https://news.ycombinator.com/item?id=48795580 (Heckle, 6 / 3)
- https://news.ycombinator.com/item?id=50339913 (Momentic, 168 / 135)
- https://news.ycombinator.com/item?id=45215032 (Ghostship, 53 / 23)
Blogs, reviews, vendor pages (vendor = weak evidence):
- https://dev.to/branch42-labs/why-my-coding-agent-couldnt-see-my-apps-api-calls-and-the-3-fixes-i-use-4705 (vendor-affiliated)
- https://dev.to/hassantayyab/stop-wasting-tokens-on-ui-bugs-how-chrome-devtools-mcp-changed-my-debugging-workflow-3ma9
- https://blog.buildbetter.ai/how-to-hand-off-bugs-to-a-coding-agent/ (vendor)
- https://chromewebstore.google.com/detail/darnly-bug-reports-for-ai/gognoljafcabnmbbpfoeeamcflpbgidj (vendor listing)
- https://chromewebstore.google.com/detail/jam-bug-reporting-for-dev/iohjgamcilhbgmhbnllfolmkmmekfmci/reviews (4.3, 292 ratings; used as context only, in no node)

## Unverified (seen only in search results or blocked on re-check; not the main claim of any node)
- https://www.producthunt.com/products/flowlens-ai-native-bug-reports (403 on re-check; vendor, 132 upvotes as first read)
- https://www.producthunt.com/products/markupr (403 on re-check; vendor)
- https://github.com/AryaaSk/replay
- https://pypi.org/project/bug2context/
- https://www.tella.com/auto-capture/bug-reproduction-video
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/provide-visual-inputs (image limit 3 MiB, from a snippet)
- https://forum.cursor.com/t/built-in-browser-automation/149085
- https://www.shakebugs.com/blog/ai-bug-reporting-benefits/ (vendor)
- https://dev.to/pvgomes/copilot-browser-tools-make-the-frontend-reviewable-293p

- https://argos-ci.com/blog/agents-show-their-work (verified on re-check, HTTP 200; earlier 404; not cited in nodes)

## Dropped
- https://www.g2.com/products/jam-dev/reviews (403); BetterBugs and Marker.io Chrome Web Store review pages ("not available") also gave nothing. Counted as one dropped group.
