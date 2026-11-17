#!/usr/bin/env python3
"""Compare the four research runs: reads runs/*/ranking.json and writes compare/comparison.md.

Matching across runs is by title words (each agent numbers its own nodes), so the consensus table
groups nodes whose titles share enough keywords. The owner (or Claude) then reads the nodes by hand.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = sorted(p for p in (HERE / "runs").iterdir() if p.is_dir())
STOP = set("a an the to of in and or for with is are be on it its my your their agent agents ai coding can cant not no".split())


def words(title: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]+", title.lower()) if w not in STOP and len(w) > 2}


def load(run: Path) -> dict | None:
    try:
        return json.loads((run / "ranking.json").read_text())
    except Exception as error:  # missing or invalid output is itself a result
        return {"error": str(error)}


def main() -> None:
    out = ["# Comparison of the four research runs", ""]
    data = {run.name: load(run) for run in RUNS}
    out += ["## Run health", "", "| Run | Stories passed | Nodes | Verified line in sources.md | Files |", "|---|---|---|---|---|"]
    for run in RUNS:
        prd = json.loads((run / "prd.json").read_text())
        passed = sum(s["passes"] for s in prd["userStories"])
        nodes = len(list((run / "nodes").glob("P*.md")))
        src = run / "sources.md"
        first = src.read_text().splitlines()[0][:60] if src.exists() and src.read_text().strip() else "missing"
        files = ", ".join(sorted(p.name for p in run.iterdir() if p.suffix in (".md", ".json") and p.name != "prd.json"))
        out.append(f"| {run.name} | {passed}/{len(prd['userStories'])} | {nodes} | {first} | {files} |")

    out += ["", "## Top 5 by pick_score, per run", ""]
    clusters: list[dict] = []
    for name, d in data.items():
        out.append(f"### {name}")
        if not d or "error" in d:
            out += [f"No usable ranking.json ({(d or {}).get('error', 'missing')}).", ""]
            continue
        by_id = {n["id"]: n for n in d.get("nodes", [])}
        top = d.get("top_pick", {})
        out.append(f"Top pick: **{top.get('feature', '?')}** ({top.get('node', '?')})")
        out += ["", "| Rank | Node | pick | pain | Feature idea |", "|---|---|---|---|---|"]
        for rank, node_id in enumerate(d.get("pick_rank", [])[:5], 1):
            n = by_id.get(node_id, {})
            out.append(f"| {rank} | {n.get('title', node_id)} | {n.get('pick_score', '?')} | {n.get('pain_score', '?')} | {n.get('feature_idea', '')} |")
        out.append("")
        pick_pos = {nid: i for i, nid in enumerate(d.get("pick_rank", []))}
        for n in d.get("nodes", []):
            w = words(n.get("title", "") + " " + n.get("feature_idea", ""))
            entry = (name, n, pick_pos.get(n["id"], 99))
            for c in clusters:
                if len(w & c["words"]) >= 3:
                    c["items"].append(entry)
                    c["words"] |= w
                    break
            else:
                clusters.append({"words": set(w), "items": [entry]})

    out += ["## Consensus (rough keyword clusters, check by hand)", "",
            "| Runs agreeing | Mean pick_score | Best rank | Example titles |", "|---|---|---|---|"]
    rows = []
    for c in clusters:
        runs = {name for name, _, _ in c["items"]}
        scores = [n.get("pick_score", 0) for _, n, _ in c["items"]]
        rows.append((len(runs), sum(scores) / len(scores), min(p for _, _, p in c["items"]) + 1,
                     " / ".join(f"{name.split('-')[0]}: {n.get('title', '')[:60]}" for name, n, _ in c["items"][:4])))
    for runs, mean, best, titles in sorted(rows, key=lambda r: (-r[0], -r[1]))[:15]:
        out.append(f"| {runs} | {mean:.1f} | {best} | {titles} |")

    (HERE / "compare").mkdir(exist_ok=True)
    (HERE / "compare" / "comparison.md").write_text("\n".join(out) + "\n")
    print("comparison written")


if __name__ == "__main__":
    main()
