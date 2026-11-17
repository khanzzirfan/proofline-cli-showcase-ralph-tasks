"""A local stand-in for the three Proofline endpoints `proofline scan` uses.

It is for the demo recording only. It is not Proofline's API: responses follow
the shapes in the CLI's openapi.public.json, and the review content is made up.

- GET  /api/v1/organizations/{org}/repository-names
- POST /api/v1/organizations/{org}/repositories/{repo}/scans
- GET  /api/v1/organizations/{org}/reviews/{review}

Behaviour the demo relies on:
- A request_id seen before returns EXISTING with the first review (idempotency).
- The ref "release/2026.11" is recorded, then answered with a 502 the first time,
  like a gateway failing after the server accepted the request.
- A new scan reads RUNNING once, then COMPLETED with one finding.

Run: python3 mock_console.py [port]   (default 8787, loopback only)
"""

import json
import sys
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ORG = "0190f3a0-0000-7000-8000-000000000001"
REPO = "0190f3a0-0000-7000-8000-000000000022"
FLAKY_REF = "release/2026.11"

scans = {}  # request_id -> (resolution_id, review_id)
reads = {}  # review_id -> number of reads
flaky_failed = set()


def review(review_id, status):
    finding = {
        "id": "0190f3a0-0000-7000-8000-0000000000f1",
        "finding_fingerprint": None,
        "severity": "SERIOUS",
        "risk_domain": "error_handling",
        "claim": "A failed upload retry reuses a consumed idempotency key, so the second attempt is silently dropped.",
        "impact": "Users see a success message while the report never reaches storage.",
        "lifecycle_state": "OPEN",
        "remediation": "Generate the key once per logical upload and keep it across retries.",
        "evidence_refs": [{
            "kind": "CODE",
            "label": "upload retry loop",
            "provenance_status": "VERIFIED",
            "repository_path": "src/upload/retry.ts",
            "start_line": 42,
            "end_line": 58,
            "commit_sha": "3f9c2a1e8b7d6c5b4a3928170f6e5d4c3b2a1908",
            "companion_repository": None,
        }],
    }
    done = status == "COMPLETED"
    return {
        "id": review_id,
        "kind": "REVISION_SCAN",
        "status": status,
        "assessment_count": 1,
        "assessments": [{
            "id": "0190f3a0-0000-7000-8000-000000000044",
            "environment_display_name": "production",
            "status": "COMPLETED" if done else "RUNNING",
            "incompleteness_kind": None,
            "findings": [finding] if done else [],
            "checks": {"receipt_recorded": True, "status": "READY", "families": []},
        }],
        "head_commit_sha": "3f9c2a1e8b7d6c5b4a3928170f6e5d4c3b2a1908",
        "repository_full_name": "acme/web",
    }


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass  # keep the recording clean

    def send(self, status, body, content_type="application/json"):
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        base = f"/api/v1/organizations/{ORG}"
        if self.path == f"{base}/repository-names":
            return self.send(200, {"repositories": [{"id": REPO, "full_name": "acme/web"}]})
        if self.path.startswith(f"{base}/reviews/"):
            review_id = self.path.rsplit("/", 1)[1]
            reads[review_id] = reads.get(review_id, 0) + 1
            status = "RUNNING" if reads[review_id] == 1 else "COMPLETED"
            return self.send(200, review(review_id, status))
        self.send(404, {"title": "not found", "status": 404}, "application/problem+json")

    def do_POST(self):
        if self.path != f"/api/v1/organizations/{ORG}/repositories/{REPO}/scans":
            return self.send(404, {"title": "not found", "status": 404}, "application/problem+json")
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        request_id = body["request_id"]
        if request_id in scans:
            resolution, review_id = scans[request_id]
            reads[review_id] = max(reads.get(review_id, 0), 1)  # finished meanwhile
            return self.send(200, {"resolution_id": resolution, "outcome": "EXISTING", "review_id": review_id})
        resolution, review_id = str(uuid.uuid4()), str(uuid.uuid4())
        scans[request_id] = (resolution, review_id)
        if body.get("ref") == FLAKY_REF and FLAKY_REF not in flaky_failed:
            flaky_failed.add(FLAKY_REF)
            return self.send(502, {"title": "Bad Gateway", "status": 502,
                                   "detail": "The upstream connection closed before a response."},
                             "application/problem+json")
        self.send(200, {"resolution_id": resolution, "outcome": "CREATED", "review_id": review_id})


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8787
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
