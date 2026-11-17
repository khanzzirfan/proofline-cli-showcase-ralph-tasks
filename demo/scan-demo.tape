# Records scan-demo.gif: `proofline scan` against demo/mock_console.py, a local
# stand-in for the Proofline API. Render from this folder:
#   PROOFLINE_BIN=/path/to/proofline vhs scan-demo.tape

Output scan-demo.gif
Set Shell "bash"
Set FontSize 13
Set Width 1500
Set Height 760
Set Padding 18
Set TypingSpeed 35ms
Set Theme "Builtin Dark"

Hide
Type `python3 -I mock_console.py 8787 >/dev/null 2>&1 & sleep 1` Enter
Type `export PROOFLINE_BASE_URL=http://127.0.0.1:8787 PROOFLINE_TOKEN=pld_demo PROOFLINE_ORGANIZATION_ID=0190f3a0-0000-7000-8000-000000000001 PROOFLINE_NO_UPDATE_CHECK=1` Enter
Type `proofline() { "$PROOFLINE_BIN" "$@"; }; cd "$(mktemp -d)"; PS1='$ '; clear` Enter
Sleep 1s
Show

Type "# proofline scan, against a local stand-in for the Proofline API (demo/mock_console.py)" Enter
Sleep 1.5s

Type "# 1. A scan spends credits, so there is no default budget:" Enter
Type "proofline scan --repo acme/web --ref main; echo exit=$?" Enter
Sleep 3s

Type "# 2. Scan main within 200 credits; the command waits for the result:" Enter
Type "proofline scan --repo acme/web --ref main --budget 200; echo exit=$?" Enter
Sleep 9s

Type "clear" Enter
Type "# 3. The server fails after accepting the request. Did the scan start?" Enter
Type "proofline scan --repo acme/web --ref release/2026.11 --budget 200 --request-id 0190f3a0-0000-7000-8000-00000000c0de; echo exit=$?" Enter
Sleep 4s

Type "# 4. Exit 4 means unknown. Rerun with the same request ID: no second scan, no second charge." Enter
Type "proofline scan --repo acme/web --ref release/2026.11 --budget 200 --request-id 0190f3a0-0000-7000-8000-00000000c0de; echo exit=$?" Enter
Sleep 7s
