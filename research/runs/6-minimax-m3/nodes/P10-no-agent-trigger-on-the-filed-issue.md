---
id: P10
title: "The report is filed but the agent never picks it up — the trigger is missing"
who: developers, QA, product
tools: [copilot-coding-agent, jules, codex, openhands, devin, github-actions]
status: verified
---
## Pain
Filing a good issue is only half the workflow. Users want the cloud agent that their repo
already has to *notice* the issue and start working, without a human copying the issue body
into a chat. Today each agent has its own secret trigger, and the trigger is not documented
where the reporter is looking.

## Evidence
- https://github.com/anthropics/claude-code/issues/75632 (github-issue, 2026-07-08, verified): "GitHub's Copilot coding agent has shipped a built-in browser (Playwright MCP) with screenshots in the pull request since July 2025" (signal: 👍 8, 21 comments) — i.e. the assign-an-issue flow exists but its verification half does not
- https://github.com/microsoft/hve-core/blob/main/.github/agents/issue-triage.agent.md (github-repo, verified): "You classify a single issue, apply appropriate labels (type, area, and priority), detect duplicates, assess quality, and optionally mark qualifying issues for automated implementation." (signal: repo file; part of Microsoft's own agentic workflows)
- https://github.github.com/gh-aw/gallery/ai-issue-triage/ (github-repo, verified): "The workflow first checks whether the report is complete and searches for related issues... assesses whether the issue is ready for a coding agent" (signal: GitHub Agentic Workflows gallery)
- https://github.com/orgs/community/discussions/169913 (github-discussion, 2025-08-15, verified): a cloud agent is triggered by assigning an issue to Copilot and asking for screenshots in the issue body — "When creating an issue for front end bugfixes, and then assigning to copilot, I was previously getting a screenshot showing before and after. I cannot get this now." (signal: 3 comments, 4 participants, unanswered; the trigger exists but is undocumented and unreliable)
- https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows/ (github-blog, 2026-01-13, verified): "When a new issue is opened, the triage agent analyzes its content, does research in the codebase and other issues, responds with a comment, and applies appropriate labels" (signal: GitHub Agentic Workflows announcement)

## How users want it fixed
- The issue body itself should carry the instructions for the agent, so any agent that reads
  the issue knows what to do (the "agent instructions block" in the notes' option B).
- The reporter should not need to know the trigger: "When a new issue is opened, the triage agent analyzes its content, does research in the codebase and other issues, responds with a comment, and applies appropriate labels" (https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows/)
- The trigger must be discoverable where the reporter is looking — today the same user cannot get the agent to attach a screenshot reliably even when asking in the issue (https://github.com/orgs/community/discussions/169913).

## Workarounds people use today
- Assign the issue to the Copilot coding agent, or add the agent's label, or comment its
  trigger on the issue (https://github.com/orgs/community/discussions/169913)
- Run the agent locally and paste the report in by hand (see P02)

## Session Recorder angle
The extension already files a GitHub issue (`entrypoints/share/`) and already supports labels
and assignees via open PR #48. The missing piece is the **agent instructions block** — a
short, standard section in the issue body that tells any coding agent how to read
`report.md`: read the markers first, cite `[mm:ss]`, follow `linkedRequestId`, and say which
verbosity level to re-export if a detail is missing. That block is small, reusable across
agents, and is not covered by any open PR.
Overlapping open PRs: #48 (labels and assignees when filing) — do not duplicate its label
or assignee UI. #24 (Linear issues) is a different tracker.

## Scores
frequency: 3  severity: 3  fit: 4  smallness: 5  novelty: 2
pain_score: 12  pick_score: 27
