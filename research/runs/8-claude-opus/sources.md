verified: 78, unverified: 9, dropped: 14

# Sources: run 8-claude-opus

Collected 2026-11-17. "verified" = I opened the page or its JSON API record and saw the quoted text or title. "unverified" = seen only in a search result. "dropped" = searched or opened but not used (reason given).

## Popular places covered (12 of the PRD list)

anthropics/claude-code, openai/codex, github/copilot-cli, sst/opencode (now anomalyco/opencode), ChromeDevTools/chrome-devtools-mcp, microsoft/playwright-mcp, forum.cursor.com, Hacker News, r/ClaudeAI, r/cursor, r/QualityAssurance, r/ExperiencedDevs (Reddit: search results only), Chrome Web Store. Also searched with low yield: All-Hands-AI/OpenHands (now OpenHands/OpenHands), RooCodeInc/Roo-Code, cline/cline (see dropped rows); r/webdev and r/ChatGPTCoding returned nothing relevant.

## Access notes

- Reddit `search.json` returned an HTML block page for `curl -A "pain-research/1.0"` (www and old.reddit). The built-in web search tool refuses reddit.com. Reddit posts were found through SerpAPI (Google) and are all `unverified`; quotes are search snippets.
- GitHub search API without a token: 10 calls/min; core API 60 calls/hour (hit 32 of 60). Raw JSON in `raw/gh-*.json`, issue bodies in `raw/gh-issue-bodies.json`.
- HN via Algolia (`raw/hn-*.json`), Cursor forum via Discourse `/t/<id>.json` (`raw/cursor-forum.jsonl`).
- G2 and Product Hunt returned 403. Chrome Web Store listings load reviews by script, so only listing text (users, rating) was readable.

## US-003 verification pass (2026-11-17)

- Re-opened every cited non-Reddit URL (84 evidence lines across 15 nodes): GitHub and blog pages by `curl -sL -A "pain-research/1.0"`, HN through the Algolia item API, Cursor forum through Discourse `/t/<id>.json`. All returned HTTP 200.
- Checked each quote word for word against the fetched text (punctuation and HTML escapes ignored): 83 of 84 matched. The one miss was P04 alphaxiv 2607.09553: the old quote is not on the abstract page, so it was replaced with a verbatim abstract sentence. P03's Heckle line now quotes the repo tagline and the Show HN title.
- Reddit (9 URLs): still blocked. `www.reddit.com/.json` and `api.reddit.com` return 403, `old.reddit.com` returns a login wall, and the web-fetch agent is refused for both hosts. They stay `unverified` and no node relies on them for its main claim.
- Fixed source types: docs.github.com is now vendor-doc, and the bug0.com and dev.to (creatman) posts are now blog/web (they had been labelled playwright-mcp).
- Duplicates: no nodes merged. P03 (hand evidence to the agent) and P15 (agent replays the recorded steps) share playwright-mcp #734 but describe different needs; each node now says so. P09 (no image input) and P12 (images break sessions) stay separate: one is about missing input, the other about failing input.
- Status rule: `verified` = every cited source verified; `partly-verified` = main claim backed by at least 2 verified sources, but some supporting quotes are unverified (Reddit). Partly verified: P02, P07, P10, P14. All others: verified.

## Vision and video area

Searched GitHub (`in:title image|screenshot|video` in claude-code, codex, copilot-cli, opencode, OpenHands; `visual regression`), HN (`claude code screenshot`, `bug report video LLM`, `visual regression AI`), web (AI PR review cannot see UI; video to key frames). Result: three nodes. P08 (PR review blind to UI), P09 (CLI agents lack image input), P10 (agents cannot watch video). P12 (image limits break sessions) is related. The strongest gap for Session Recorder is P10: `video/*.webm` in the ZIP is unreadable to text agents.

## All URLs

| URL | place | status | nodes | note |
|---|---|---|---|---|
| https://github.com/anthropics/claude-code/issues/57034 | anthropics/claude-code | verified | P01,P13 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/75632 | anthropics/claude-code | verified | P01,P08 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/52907 | anthropics/claude-code | verified | P01 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console-which-opens-inside-the-cursor-as-a-separate-tab/152452 | forum.cursor.com | verified | P01 | US-003 2026-11-17: re-opened (Discourse JSON), HTTP 200, quote found |
| https://forum.cursor.com/t/browser-automation-agent-cant-access-content-of-a-network-tab/151228 | forum.cursor.com | verified | P01 | US-003 2026-11-17: re-opened (Discourse JSON), HTTP 200, quote found |
| https://dev.to/dedupedai/let-claude-code-or-cursor-debug-your-page-in-a-real-chrome-browser-ldc | blog/web | verified | P01 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://news.ycombinator.com/item?id=47390817 | Hacker News | verified | P01 | US-003 2026-11-17: re-opened (HN Algolia item API), HTTP 200, quote found |
| https://forum.cursor.com/t/i-made-a-vscode-extension-that-forwards-frontend-errors-back-to-composer/50807 | forum.cursor.com | verified | P02 | US-003 2026-11-17: re-opened (Discourse JSON), HTTP 200, quote found |
| https://forum.cursor.com/t/feedback-loop-for-errors/92299 | forum.cursor.com | verified | P02 | US-003 2026-11-17: re-opened (Discourse JSON), HTTP 200, quote found |
| https://forum.cursor.com/t/helping-cursor-extract-or-interrogate-chrome-dev-tools-js-console-logs/144346 | forum.cursor.com | verified | P02 | US-003 2026-11-17: re-opened (Discourse JSON), HTTP 200, quote found |
| https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803 | forum.cursor.com | verified | P02 | US-003 2026-11-17: re-opened (Discourse JSON), HTTP 200, quote found |
| https://news.ycombinator.com/item?id=48795668 | Hacker News | verified | P02 | US-003 2026-11-17: re-opened (HN Algolia item API), HTTP 200, quote found |
| https://www.thesingularityproject.ai/p/copying-and-pasting-console-logs | blog/web | verified | P02 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://www.reddit.com/r/ClaudeCode/comments/1lvtbrm/a_powerful_cli_tool_that_captures_browser/ | r/ClaudeCode | unverified | P02 | US-003: still blocked (curl 403/login wall on www, old and api.reddit.com; web-fetch agent blocked); SerpAPI snippet only |
| https://news.ycombinator.com/item?id=46047931 | Hacker News | verified | P03 | US-003 2026-11-17: re-opened (HN Algolia item API), HTTP 200, quote found |
| https://github.com/microsoft/playwright-mcp/issues/734 | microsoft/playwright-mcp | verified | P03,P15 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://jam.dev/docs/jam-mcp | vendor-doc (Jam) | verified | P03,P10 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://chromewebstore.google.com/detail/darnly-bug-reports-for-ai/gognoljafcabnmbbpfoeeamcflpbgidj | Chrome Web Store | verified | P03 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/UseVynix/vynix-mcp | GitHub repo | verified | P03 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/rbsriram/heckle | GitHub repo | verified | P03 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://news.ycombinator.com/item?id=48795580 | Hacker News | verified | P03 | US-003 2026-11-17: re-opened (HN Algolia item API), HTTP 200, quote found |
| https://overreacted.io/how-to-fix-any-bug/ | blog/web | verified | P04,P14,P15 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://dev.to/skyestrela/stop-asking-ai-coding-agents-to-fix-vague-bugs-4ji6 | blog/web | verified | P04,P05 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://www.alphaxiv.org/abs/2607.09553 | blog/web | verified | P04 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found; old quote not on page, replaced with abstract quote |
| https://sep.com/blog/agentic-bug-fixing-experience-report/ | blog/web | verified | P04 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs | vendor-doc (GitHub Docs) | verified | P04 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/32733 | anthropics/claude-code | verified | P05 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/401 | anthropics/claude-code | verified | P05 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://bug0.com/blog/playwright-mcp-cli-secret-redaction-2026 | blog/web (about playwright-mcp) | verified | P05 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://news.ycombinator.com/item?id=47391801 | Hacker News | verified | P05 | US-003 2026-11-17: re-opened (HN Algolia item API), HTTP 200, quote found |
| https://tenetsecurity.ai/blog/agentjacking-coding-agents-with-fake-sentry-errors/ | blog/web | verified | P06 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://news.ycombinator.com/item?id=48507994 | Hacker News | verified | P06 | US-003 2026-11-17: re-opened (HN Algolia item API), HTTP 200, quote found |
| https://news.ycombinator.com/item?id=47391875 | Hacker News | verified | P06 | US-003 2026-11-17: re-opened (HN Algolia item API), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/80950 | anthropics/claude-code | verified | P07 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/37818 | anthropics/claude-code | verified | P07 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/66054 | anthropics/claude-code | verified | P07 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/42834 | anthropics/claude-code | verified | P07 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/319 | anthropics/claude-code | verified | P07 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://www.ssw.com.au/rules/done-video-by-ai | blog/web | verified | P07,P08 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://www.reddit.com/r/cursor/comments/1l2213c/so_claude_40_lied_to_me_yep_it_lies/ | r/cursor | unverified | P07 | US-003: still blocked (curl 403/login wall on www, old and api.reddit.com; web-fetch agent blocked); SerpAPI snippet only |
| https://github.com/anthropics/claude-code/issues/101957 | anthropics/claude-code | verified | P08 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/26831 | anthropics/claude-code | verified | P08 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://argos-ci.com/blog/visual-testing-ai-coding-agents | blog/web | verified | P08 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/github/copilot-cli/issues/476 | github/copilot-cli | verified | P09 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/github/copilot-cli/issues/1217 | github/copilot-cli | verified | P09 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/1361 | anthropics/claude-code | verified | P09 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/12644 | anthropics/claude-code | verified | P09 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/openai/codex/issues/2221 | openai/codex | verified | P09 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/openai/codex/issues/30529 | openai/codex | verified | P09 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anomalyco/opencode/issues/906 | sst/opencode (now anomalyco/opencode) | verified | P09 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anomalyco/opencode/issues/15728 | sst/opencode (now anomalyco/opencode) | verified | P09 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/15597 | anthropics/claude-code | verified | P09 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://news.ycombinator.com/item?id=48489942 | Hacker News | verified | P09 | US-003 2026-11-17: re-opened (HN Algolia item API), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/12676 | anthropics/claude-code | verified | P10 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/2614 | anthropics/claude-code | verified | P10 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/14805 | anthropics/claude-code | verified | P10 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/AryaaSk/replay | GitHub repo | verified | P10 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://www.reddit.com/r/ClaudeAI/comments/1xwjdzc/how_i_show_claude_code_a_ui_bug_without_writing_a/ | r/ClaudeAI | unverified | P10 | US-003: still blocked (curl 403/login wall on www, old and api.reddit.com; web-fetch agent blocked); SerpAPI snippet only |
| https://www.reddit.com/r/ClaudeCode/comments/1ssub0g/a_plugin_that_lets_claude_code_watch_videos_image/ | r/ClaudeCode | unverified | P10 | US-003: still blocked (curl 403/login wall on www, old and api.reddit.com; web-fetch agent blocked); SerpAPI snippet only |
| https://www.reddit.com/r/ClaudeAI/comments/1t9frna/built_an_mcp_that_gives_claude_code_the_ability/ | r/ClaudeAI | unverified | P10 | US-003: still blocked (curl 403/login wall on www, old and api.reddit.com; web-fetch agent blocked); SerpAPI snippet only |
| https://www.reddit.com/r/ClaudeAI/comments/1uppopb/clipy_mcp_claude_code_can_now_watch_my_screen/ | r/ClaudeAI | unverified | P10 | US-003: still blocked (curl 403/login wall on www, old and api.reddit.com; web-fetch agent blocked); SerpAPI snippet only |
| https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/171 | ChromeDevTools/chrome-devtools-mcp | verified | P11 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/microsoft/playwright-mcp/issues/1216 | microsoft/playwright-mcp | verified | P11 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/microsoft/playwright-mcp/issues/806 | microsoft/playwright-mcp | verified | P11 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/microsoft/playwright-mcp/issues/1290 | microsoft/playwright-mcp | verified | P11 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/microsoft/playwright-mcp/issues/395 | microsoft/playwright-mcp | verified | P11 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://news.ycombinator.com/item?id=47391926 | Hacker News | verified | P11 | US-003 2026-11-17: re-opened (HN Algolia item API), HTTP 200, quote found |
| https://news.ycombinator.com/item?id=47391877 | Hacker News | verified | P11 | US-003 2026-11-17: re-opened (HN Algolia item API), HTTP 200, quote found |
| https://dev.to/creatman/playwright-mcp-burns-15m-tokens-cli-does-it-in-27k-so-i-built-the-skill-that-splits-the-phases-50j7 | blog/web (about playwright-mcp) | verified | P11,P12 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/13480 | anthropics/claude-code | verified | P12 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/2939 | anthropics/claude-code | verified | P12 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/19031 | anthropics/claude-code | verified | P12 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/anthropics/claude-code/issues/62466 | anthropics/claude-code | verified | P12 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/openai/codex/issues/31040 | openai/codex | verified | P12 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/140 | ChromeDevTools/chrome-devtools-mcp | verified | P13 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/825 | ChromeDevTools/chrome-devtools-mcp | verified | P13 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/microsoft/playwright-mcp/issues/403 | microsoft/playwright-mcp | verified | P13 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/microsoft/playwright-mcp/issues/1388 | microsoft/playwright-mcp | verified | P13 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://news.ycombinator.com/item?id=46130602 | Hacker News | verified | P13 | US-003 2026-11-17: re-opened (HN Algolia item API), HTTP 200, quote found |
| https://news.ycombinator.com/item?id=47391195 | Hacker News | verified | P13 | US-003 2026-11-17: re-opened (HN Algolia item API), HTTP 200, quote found |
| https://www.reddit.com/r/QualityAssurance/comments/1nq62ti/how_do_you_deal_with_cant_reproduce_bugs_in_your/ | r/QualityAssurance | unverified | P14 | US-003: still blocked (curl 403/login wall on www, old and api.reddit.com; web-fetch agent blocked); SerpAPI snippet only |
| https://www.reddit.com/r/QualityAssurance/comments/1swiriv/how_do_you_deal_with_bug_reports_that_devs_cant/ | r/QualityAssurance | unverified | P14 | US-003: still blocked (curl 403/login wall on www, old and api.reddit.com; web-fetch agent blocked); SerpAPI snippet only |
| https://www.reddit.com/r/ExperiencedDevs/comments/ointdy/why_is_it_so_hard_to_add_steps_to_reproduce_a_bug/ | r/ExperiencedDevs | unverified | P14 | US-003: still blocked (curl 403/login wall on www, old and api.reddit.com; web-fetch agent blocked); SerpAPI snippet only |
| https://forum.cursor.com/t/debug-mode-browser-fetch-to-ingest-server-127-0-0-1-7772-never-writes-debug-sessionid-log-agent-cant-read-runtime-evidence/167378 | forum.cursor.com | verified | P14 | US-003 2026-11-17: re-opened (Discourse JSON), HTTP 200, quote found |
| https://github.com/microsoft/playwright-mcp/issues/280 | microsoft/playwright-mcp | verified | P15 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/microsoft/playwright-mcp/issues/1645 | microsoft/playwright-mcp | verified | P15 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://github.com/microsoft/playwright-mcp/issues/123 | microsoft/playwright-mcp | verified | P15 | US-003 2026-11-17: re-opened (curl page fetch), HTTP 200, quote found |
| https://www.g2.com/products/jam-dev/reviews | G2 | dropped | - | HTTP 403 on fetch; review cons only seen via search summary |
| https://www.producthunt.com/products/flowlens-ai-native-bug-reports | Product Hunt | dropped | - | HTTP 403 on fetch; FlowLens covered by HN post instead |
| https://www.builder.io/blog/setting-up-agent-native-clips-the-free-loom-alternative-that-captures-browser-errors | blog | dropped | - | HTTP 404 |
| https://clipfix-website.pages.dev/ | vendor | dropped | - | page renders by JS; no text to verify |
| https://pypi.org/project/bug2context/ | vendor | dropped | - | page returned no readable text |
| https://github.com/anthropics/claude-code/issues/23377 | anthropics/claude-code | dropped | - | "GitHub Issue Prompt Too Long": body is a general prompt-length bug, not about issues |
| https://github.com/camunda/camunda/issues/51936 | GitHub | dropped | - | visual regression search hit; 0 reactions, internal ticket |
| https://claudeissues.com/issue/80950-bug-claude-kept-saying-fixed-without-checking-burned-a-huge-amount-of-tokens-ove | mirror | dropped | - | third-party mirror; cited the original GitHub issue instead |
| https://www.reddit.com/r/ClaudeCode/comments/1uoibue/i_got_tired_of_claude_code_treating_videos_as/ | r/ClaudeCode | dropped | - | search snippet only; enough Reddit video evidence already |
| https://www.reddit.com/r/chrome_extensions/comments/1xartyw/my_first_extension_a_bug_recorder_with_a_rolling/ | reddit | dropped | - | competitor launch post; snippet only |
| https://github.com/OpenHands/OpenHands/issues/8372 | OpenHands/OpenHands | dropped | - | "Allow the agent to save a browser screenshot as an image", 4 reactions: low signal, not cited |
| https://github.com/RooCodeInc/Roo-Code/issues/8045 | RooCodeInc/Roo-Code | dropped | - | "screenshots display as base64 text after ~5 actions", 2 reactions: low signal |
| https://github.com/cline/cline/issues/762 | cline/cline | dropped | - | "browser viewport 900x600 too small for UI testing", 5 reactions: low signal |
| https://github.com/cline/cline/issues/3139 | cline/cline | dropped | - | "Browser vision no longer working after latest update", 4 reactions: low signal |
