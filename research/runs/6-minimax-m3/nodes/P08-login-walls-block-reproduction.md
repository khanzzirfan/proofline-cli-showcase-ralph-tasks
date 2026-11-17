---
id: P08
title: "The agent can't log in, so it can't reproduce the bug behind the login"
who: developers, QA
tools: [claude-code, playwright-mcp, cursor, chrome-extension]
status: verified
---
## Pain
Most real bugs live behind a login — an admin panel, a dashboard, a CMS, a staging
environment. Agents refuse to type credentials, and even when the user explicitly supplies
and authorizes them, the session stalls. The workaround is for the human to sit in the loop
and log in by hand, which destroys any unattended or scheduled workflow.

## Evidence
- https://github.com/anthropics/claude-code/issues/82668 (github-issue, verified): "the agent refuses to type credentials into a login form — even when the user explicitly supplies them, explicitly authorizes their use, and owns the target site." (signal: 7 comments; a maintainer marked the duplicate #82669 as "Playwright automation is unusable behind logins"; closed as not planned 2026-09-07)
- https://github.com/anthropics/claude-code/issues/82668 (github-issue, verified): "The overwhelming majority of real automation targets are behind a login... If the agent cannot get past a login form, browser automation is effectively limited to public pages" (signal: 7 comments)
- https://forum.cursor.com/t/can-not-login-to-aws-via-cursors-browser/162714 (forum, 2026-06-08, verified): "aws-vault login hands the sign-in URL to your OS default browser, e.g. Chrome, and command-line tools like it can't currently be pointed at Cursor's built-in browser." (signal: 3 posts, 106 views)
- https://forum.cursor.com/t/cursor-does-not-have-access-to-built-in-browser-anymore/164605 (forum, 2026-07-02, verified): Cursor staff — "Models often deny tools that are actually connected." (signal: 3 posts, 174 views, 4 likes)

## How users want it fixed
- A credential-broker style mechanism: "the user approves per-item, the value is injected directly into the page, and the agent never sees it." (https://github.com/anthropics/claude-code/issues/82668)
- Reuse a profile the user already authenticated: "Support for reusing an existing authenticated browser profile or storage state, so the login already happened out of band and the agent simply inherits the session." (same issue)
- At minimum, clearer guidance: "clearer guidance distinguishing 'do not exfiltrate or improvise with credentials' from 'never authenticate at all,' so agents do not over-refuse on the user's own infrastructure." (same issue)

## Workarounds people use today
- The human logs in manually and then hands over (https://github.com/anthropics/claude-code/issues/82668)
- Run `aws-vault login prod --stdout` and paste the URL into the agent's browser tab (https://forum.cursor.com/t/can-not-login-to-aws-via-cursors-browser/162714)
- Use chrome-devtools-mcp's cookie/session debugging skills instead of a fresh login (https://github.com/ChromeDevTools/chrome-devtools-mcp)

## Session Recorder angle
This is the pain Session Recorder is **uniquely** positioned to help, because it records the
*real* browser where the user is already authenticated. A recorded session of a logged-in
page contains the DOM state, the requests with their real headers and the console output
that reproduce the bug, without the agent ever needing to log in. The extension already
records network bodies and console output; what is missing is any way to tell the agent
"this session was authenticated as this user, here is the state". That also makes redaction
of cookies and tokens in the export critical — the open PRs #42, #44, #37, #38, #31 cover
exactly that. Overlapping open PRs: #42 (secret protection across evidence), #37 (redact
tokens in URLs), #38 (redact card, IBAN, tax IDs), #44 (WebSocket frame redaction), #31
(redact URL params). No open PR records the authenticated *state* for the agent.

## Scores
frequency: 3  severity: 4  fit: 4  smallness: 3  novelty: 3
pain_score: 14  pick_score: 28
