---
id: P04
title: "The agent can't see the screenshot in my GitHub issue, or I can't attach one"
who: developers, QA, product
tools: [Claude Code on the web, Copilot coding agent, Codex]
status: verified
---
## Pain
Many bug reports show the problem in an image. Cloud agents that start from a GitHub issue often cannot fetch the image attachment, or the tool will not accept images at all. The agent then works from half the report.
## Evidence
- https://github.com/anthropics/claude-code/issues/61075 (github-issue, 2026-05-21, verified): "it cannot see screenshots attached to the issue/PR it's working on." 0 reactions, 2 comments.
- https://github.com/orgs/community/discussions/153112 (github-discussion, 2025-03-05, verified): "Facing the same problem (August 2025), that's absurd? Every other coding agent supports image attachments." 22 votes, 19 comments.
- https://community.openai.com/t/codex-ide-extension-no-image-read-hallucinating-playwright-review/1356235 (forum, 2025-09-04, verified): "It cannot view images at all and the send image UI is redundant and misleading." 5 posts.
## How users want it fixed
- Resolve issue image attachments into the agent's context (cc#61075).
## Workarounds people use today
- Describe the screenshot in text; save the image into the repo; paste it into the agent by hand.
## Session Recorder angle
The extension files issues with screenshots. Gap: images in a GitHub issue are links the cloud agent may not fetch. A text description of each screenshot in the issue body (what the annotation points at, the URL, the console line near it) would let an agent work without the image. Partly overlaps #48 (labels) only by touching the filing flow.
## Scores
frequency: 3  severity: 3  fit: 3  smallness: 3  novelty: 4
