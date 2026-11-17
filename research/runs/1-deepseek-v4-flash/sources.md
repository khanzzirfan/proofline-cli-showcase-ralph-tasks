verified: 67, unverified: 12, dropped: 4

# Sources — pain research run `1-deepseek-v4-flash`

Method note: verified with `web_fetch` (GitHub issue pages, repo pages, blog/doc pages) and
`curl -sL -A "pain-research/1.0"` (Hacker News Algolia items, GitHub search API). Every URL below was
opened and its content read on 2026-11-16/17. Raw JSON I relied on is in `raw/`. Reaction counts are
from the issue page (`👍 React with 👍 N`) unless noted.

Status legend: **verified** = I opened the page (or its API record) and read its content;
**unverified** = blocked (Reddit) or JS-rendered so I could only see the title/snippet (forum.cursor.com);
**dropped** = not used.

## Clean-up done in this pass (US-003)

- **Merged duplicate nodes:** `P10` (verify-the-fix proof) is the same pain as `P04` (cloud agents / no
  proof of fix) — both are "a claimed fix needs visual proof" and both rest on OpenHands#8372. `P10` was
  deleted; its evidence (thunkle.ai, TraceBug failing-Playwright-test, apidog) was folded into `P04`.
  No other node merged: P01 (capture/observe) vs P03 (hand-off), P02 (clipboard) vs P13 (payload size),
  and P09 (repro state) vs P12 (environment/flaky) are related but distinct pains.
- **Dropped claims with no verified source:** none had to be removed — after re-checking, every node has
  at least one verified source for its main claim (see per-node `status`).
- **Fixed quotes that were not verbatim:** P06 (sitepoint, dev.to jackm), P09 (negiadventures),
  P11 (modem.ai), P14 (videolens, HN 49119880) now quote the pages word-for-word.
- **Upgraded to verified after re-check:** claude-code#13480 (was unverified), anomalyco/opencode#1429
  (was unverified), and the P09 blogs negiadventures + dev.to/yureki_lab.

## Popular places covered (PRD list)

1. **anthropics/claude-code** — issues #57034, #75632, #52907, #12676, #32005, #18170, #16157, #13480.
2. **getcursor/cursor + forum.cursor.com** — 5 forum threads read as titles only (JS-rendered body).
3. **openai/codex** — issue #31685.
4. **github/copilot-cli + GitHub docs/blog** — issues #1276, #3370; GitHub blog; docs.github.com; changelog.
5. **OpenHands/OpenHands** (renamed from All-Hands-AI) — issues #8372, #8387.
6. **RooCodeInc/Roo-Code** — PR #11065 (repo now archived, read-only).
7. **sst/opencode (now anomalyco/opencode)** — issue #1429.
8. **cline/cline** — issues #9902, #9340.
9. **ChromeDevTools/chrome-devtools-mcp** — issues #96, #407, #1172, #1921; Chrome DevTools for agents blog.
10. **microsoft/playwright-mcp** — issues #1629, #982, #978, #198 (all real but 0-reaction / weak).
11. **Hacker News** — items 48795580, 46047931, 49119880, 45215032, 47075182, 48197661, 47460525.
12. **r/ClaudeAI, r/cursor, r/ChatGPTCoding, r/webdev, r/QualityAssurance, r/ExperiencedDevs** — Reddit
    blocks this host; evidence is from `site:reddit.com` search snippets and marked unverified.
13. **Chrome Web Store / vendor listings** — Jam Chrome Web Store listing + Toolradar pricing page.
14. **Vendor docs / blogs** — Chrome DevTools for agents, GitHub docs, and the BugDump / TraceBug /
    videolens / aitasks / thunkle / apidog write-ups.

## GitHub issues — verified (opened via web_fetch; reaction totals from the page)

- https://github.com/anthropics/claude-code/issues/57034 — verified — browser-sharing API so Claude can validate web UI; **open**, 👍76 (+1:55), 7 comments.
- https://github.com/anthropics/claude-code/issues/75632 — verified — browser view / tools in cloud sessions; **closed**, 👍8, 3 comments.
- https://github.com/anthropics/claude-code/issues/52907 — verified — browser rendering / DOM inspection; **closed**, 👍1, 5 comments.
- https://github.com/anthropics/claude-code/issues/12676 — verified — video input support; **open**, 57 reactions (+1:46), 21 comments.
- https://github.com/anthropics/claude-code/issues/32005 — verified — image/screenshot paste in terminal; **closed as not planned (stale)**, 👍8, 17 comments.
- https://github.com/anthropics/claude-code/issues/18170 — verified — copy/paste indentation; **open**, 👍304 (+😕1 = 305), 140 comments.
- https://github.com/anthropics/claude-code/issues/16157 — verified — usage limits; **open**, 728 reactions (👍697 …), 1499 comments.
- https://github.com/anthropics/claude-code/issues/13480 — verified — oversized image breaks conversation; **closed/locked**, 👍90.
- https://github.com/openai/codex/issues/31685 — verified — paste screenshots into Codex CLI; **closed (completed)**.
- https://github.com/github/copilot-cli/issues/1276 — verified — paste images into copilot CLI; **open**, 👍8, 11 comments.
- https://github.com/github/copilot-cli/issues/3370 — verified — image/screenshot paste; **closed (completed)**.
- https://github.com/OpenHands/OpenHands/issues/8372 — verified — save browser screenshot as PR evidence; **closed**, 👍3.
- https://github.com/OpenHands/OpenHands/issues/8387 — verified — browser tab stopped showing latest screenshot; **closed**.
- https://github.com/microsoft/vscode/issues/256095 — verified — Copilot agent can't see image via #file; **open**, 👍5, label `chat-vision`.
- https://github.com/microsoft/vscode/issues/280570 — verified — background agent does not see screenshot; **closed** ("not worth shipping").
- https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/96 — verified — extension dev/debugging support; **closed (completed in #1922)**, 77 reactions (👍61+❤2+🚀9+👀5).
- https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/407 — verified — interactive debugging; **open**, 👍12.
- https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1172 — verified — page-level WebSocket frame debugging; **open**, 👍3.
- https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1921 — verified — browser hangs with many tabs; **open (Feature, p3)**, 👍12 (+👀2 = 14).
- https://github.com/cline/cline/issues/9902 — verified — browser automation base64 image error; **closed as not planned**, 👍4.
- https://github.com/cline/cline/issues/9340 — verified — image/vision support for multimodal models; **closed as not planned**, 👍1.
- https://github.com/RooCodeInc/Roo-Code/pull/11065 — verified — it is a **PR** (not an issue): VS Code LM image support, merged then reverted (#11068) and re-applied (#11069); repo archived. Weak as a pain source.
- https://github.com/anomalyco/opencode/issues/1429 — verified — paste images from clipboard; **closed**, 👍16.
- https://github.com/microsoft/playwright-mcp/issues/1629 — verified — `--output-ttl` artifact cleanup; **closed**, 0 reactions (weak).
- https://github.com/microsoft/playwright-mcp/issues/982 — verified — make MCP ping timeout configurable; **closed**, weak.
- https://github.com/microsoft/playwright-mcp/issues/978 — verified — MCP permission manifest review; **closed**, weak.
- https://github.com/microsoft/playwright-mcp/issues/198 — verified — `ref=` attributes in browser_snapshot; **closed**, weak.

## GitHub repositories — verified (page + star count)

- https://github.com/s17labs/videobug — verified — "Your coding agent can't watch video"; key frames + motion timeline; 0★.
- https://github.com/amagilabs/amagi-screen — verified — "Send Claude a video of your bug"; key frames + OCR + error-flag timeline; 0★.
- https://github.com/SaintPepsi/openjam — verified — open-source Jam.dev; console/network/rrweb replay; GPL-3.0; 10★.
- https://github.com/AmElmo/pointa — verified — annotate app, let AI coding tool fix via MCP; 37★.
- https://github.com/UseVynix/vynix-mcp — verified — "Give AI coding agents access to your visual feedback and bug reports"; 10★.
- https://github.com/chriswu727/argus — verified — MCP tools for agents to test web apps and deliver evidence-backed reports; 7★.
- https://github.com/BugTraceAI/BugTraceAI-CLI — verified — agentic web-scanning with browser validation and MCP; 183★.
- https://github.com/lintlab/visual-regression-action — verified — PR-preview vs production pixel diff Action; 0★.

## Repo discovery (GitHub search API) — verified

- `https://api.github.com/search/repositories?q=bug+report+mcp+agent&sort=stars` — verified — 54 results; top: BugTraceAI/BugTraceAI-CLI 183★, UseVynix/vynix-mcp 10★.
- `https://api.github.com/search/repositories?q=bug+report+chrome+extension&sort=stars` — verified — 135 results; top: AmElmo/pointa 37★.

## Hacker News — verified (Algolia API, titles + comment text read)

- https://news.ycombinator.com/item?id=48795580 — verified — "Show HN: Heckle – Send a bug's full browser context to your coding agent"; 6 pts; top comment: "saves me having to copy paste from browser console to my coding agent".
- https://news.ycombinator.com/item?id=46047931 — verified — "Show HN: A better way to handoff web bugs to AI agents" (flowlens-mcp-server); 5 pts.
- https://news.ycombinator.com/item?id=49119880 — verified — "Turning screen recordings into structured incident and bug reports" (Tentomushi); 1 pt, 4 comments.
- https://news.ycombinator.com/item?id=45215032 — verified — "Launch HN: Ghostship (YC S25) – AI agents that find bugs in your web app"; 53 pts, 23 comments.
- https://news.ycombinator.com/item?id=47075182 — verified — "Show HN: Crit – Visual QA for iOS apps and AI coding agents"; 5 pts.
- https://news.ycombinator.com/item?id=48197661 — verified — "Show HN: Coding agent where a second agent QAs every PR in a real browser"; 1 pt.
- https://news.ycombinator.com/item?id=47460525 — verified — "OpenCode – Open source AI coding agent"; 1274 pts (place coverage).

## Forum threads (forum.cursor.com) — unverified (title loads, body is JS-rendered)

- https://forum.cursor.com/t/the-agent-cannot-access-the-network-and-the-browser-console-which-opens-inside-the-cursor-as-a-separate-tab/152452 — unverified — title read; body not rendered.
- https://forum.cursor.com/t/browser-automation-agent-cant-access-content-of-a-network-tab/151228 — unverified — title read ("agent can't access content of a Network tab"); body not rendered.
- https://forum.cursor.com/t/in-app-browser-console/141207 — unverified — from 00-context-notes.
- https://forum.cursor.com/t/when-i-try-to-copy-and-paste-debug-terminal-output-the-agent-can-no-longer-see-it/58803 — unverified — from 00-context-notes section 6.
- https://forum.cursor.com/t/how-to-disable-cache-write-and-cache-read/118864 — unverified — from search snippet.

## Reddit — unverified (Reddit API and web_fetch both blocked; "Prove your humanity" HTML shell)

- https://www.reddit.com/r/QualityAssurance/comments/jndw3s/bad_to_create_a_lot_of_bug_reports/ — unverified — "bug reports that are way too long and contain unnecessary info".
- https://www.reddit.com/r/QualityAssurance/comments/rrbacl/what_is_the_ideal_bug_report_for_developers/ — unverified — report "should include all the info to enable the dev to reproduce the bug".
- https://www.reddit.com/r/QualityAssurance/comments/ud41mk/whats_your_process_to_document_communicate_an/ — unverified — "anything that isn't in ticket will be forgotten".
- https://www.reddit.com/r/QualityAssurance/comments/152t1kx/bug_reporting_tool/ — unverified — Jam.dev praised for saving time.
- https://www.reddit.com/r/webdev/comments/11sbjpo/building_a_bug_reporting_extension_to_autocapture/ — unverified — "auto-capture console logs and network requests".
- https://www.reddit.com/r/webdev/comments/ymooqx/i_made_a_browser_extension_that_makes_it_easier/ — unverified — annotate UI, post screenshot to PR/issue (reviewlens).
- https://www.reddit.com/r/webdev/comments/15p9r2j/made_opensource_chrome_extension_to_capture_debug/ — unverified — Requestly: record browsing activity to share bug details.

## Blogs / docs / vendor pages — verified (opened and read)

- https://developer.chrome.com/blog/devtools-for-agents-v1 — verified — Chrome DevTools for agents 1.0 (2026-05-19); "they cannot observe its behavior or inspect its output in a live browser" (vendor).
- https://bugdump.com/blog/ai-agent-screen-recording-frames-mcp — verified — "MCP has no video content type, and Claude doesn't take video as input"; frame extraction MCP; "a 1280×720 frame costs Claude about 1,230 tokens" (vendor).
- https://bugdump.com/blog/whisper-transcribing-narrated-bug-reports — verified — Whisper transcription of narrated reports and "where it goes wrong" (vendor).
- https://safeguard.sh/resources/blog/what-an-ai-code-review-bot-cannot-see — verified — "A pull request shows what changed. It rarely shows why."
- https://tracebug.dev/blog/jam-dev-alternatives — verified — why teams leave cloud capture (price/privacy/agent workflow); local MCP; failing Playwright test (vendor).
- https://rumana.dev/blog/visual-bug-reporting-tools-compared — verified — QA tool comparison with pricing (Jam $14, Marker.io $39/mo, Loom $18).
- https://www.infosecurity-magazine.com/news/chrome-extension-ai-engine-act-mcp/ — verified — local MCP servers "unrestricted access … without authentication".
- https://github.blog/ai-and-ml/github-copilot/assigning-and-completing-issues-with-coding-agent-in-github-copilot/ — verified — assign issue → agent session on GitHub Actions (vendor).
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs — verified — **redirects** to a renamed page; "Cloud agent processes images—such as screenshots, sketches, or designs—as part of your task description."
- https://github.blog/changelog/2026-07-01-copilot-vision-is-generally-available/ — verified — Copilot vision GA 2026-07-01; images/PDFs; CLI attaches image paths (vendor).
- https://negiadventures.github.io/blog/environment-manifests-ai-coding-agents.html — verified — "environment failures wearing a reasoning costume"; the agent "patches symptoms instead of causes".
- https://thunkle.ai/blog/verify-ai-agent-fix — verified — "An AI agent's passing test is not proof of a security fix."
- https://apidog.com/blog/ai-agents-screenshot-proof-reality-checker/ — verified — "requires screenshot proof before AI agents can approve work"; PASS/FAIL.
- https://www.sitepoint.com/review-ai-generated-ui-changes/ — verified — "Reviewing AI-generated UI changes in a traditional diff viewer is not just slow; it is structurally inadequate".
- https://dev.to/stendya/your-ai-assistant-ships-ui-10x-faster-add-visual-regression-to-github-actions-in-5-minutes-1chn — verified — "every UI change your agent ships carries the same five visual bugs".
- https://dev.to/jackm-singularity/visual-qa-agents-catch-ui-regressions-before-ai-written-code-ships-28pg — verified — "A visual QA agent closes that gap by driving the app like a user".
- https://dev.to/yureki_lab/how-i-debug-a-misbehaving-ai-coding-agent-my-4-step-playbook-3m12 — verified — "reproduce minimally → find the divergence turn in the transcript".
- https://modem.ai/guides/best-tools-to-deduplicate-bug-reports — verified — "Every bug tracker fills up with duplicates. One survey puts the average at 12% of bug reports." (vendor).
- https://videolens.io/screen-recording-analyzer — verified — "Turn a screen recording into an actionable report"; "Transcript + frame vision + OCR" (vendor).
- https://www.aitasks.io/docs/workflows/screen-recordings/bug-report/ — verified — "Turn a bug-report screen recording into key screens, the glitch frame, and a step-by-step report".
- https://byteiota.com/chrome-devtools-mcp-debug-browser-with-ai-agents-2026/ — verified — "they can't see what their generated code actually does in the browser".
- https://chromewebstore.google.com/detail/jam/iohjgamcilhbgmhbnllfolmkmmekfmci — verified — listing read: 4.3 (292 ratings), 200,000 users; "Route Jam context to AI agents like Claude, Codex and Cursor with Jam MCP". Individual reviews not rendered.
- https://toolradar.com/tools/jam — verified — Jam Team $14/creator/mo; free plan 30 Jams/month.

## Dropped

- Reddit JSON API (`search.json`, `top.json`) — dropped — blocked for this host (HTML "Prove your humanity"); replaced by `site:reddit.com` search.
- `repo:All-Hands-AI/OpenHands` — dropped — GitHub validation error (repo moved); used `OpenHands/OpenHands`.
- https://news.ycombinator.com/item?id=17516516 ("Show HN: Screen Recording for Bug Reports") — dropped — off-topic, 7 pts, no usable claim.
- https://github.com/amagilabs/amagi-watch — dropped — related project, not needed for evidence.

## Vision and video — why the evidence is here

Searched terms: `screenshot`, `image`, `vision`, `video`, `visual regression` across claude-code,
codex, copilot-cli, vscode, opencode, cline, Roo-Code, ChromeDevTools MCP, OpenHands, plus HN Algolia
and `site:` web searches. The gap is real and well documented (nodes P06, P07, P08): AI PR review
cannot see the rendered UI (P06), several CLI/background agents still cannot read a pasted image (P07),
and no agent watches video, so tools exist to cut frames + a timeline (P08). Session Recorder already
records tab video, screenshots and annotations, so P08 is actionable; P07 is partly addressable by making
the report's images consumable by text-only agents.
