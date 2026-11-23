"""Count the cold-FDE v1 classification (rulings CF1-CF5).

Reads the table and cluster table in engagement/03-requirements/handoff-v1-classification.md,
prints the counts, and with --write puts them between the COUNTS markers in that file.
Real-gap questions = REAL GAP + AMBIGUOUS lean real (CF3). Distinct gaps = clusters whose
questions include at least one real-gap question (CF2); I/J is one cluster.

Run: python analysis/handoff_counts.py [--write]
"""
import re
import sys
from collections import Counter
from pathlib import Path

FILE = Path(__file__).resolve().parent.parent / "engagement/03-requirements/handoff-v1-classification.md"
text = FILE.read_text(encoding="utf8")

rows = re.findall(r"^\| (Q\d+) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \|", text.split("## Classification")[1].split("## Clusters")[0], re.M)
label = {q: l for q, l, _, _ in rows}
severity = {q: s for q, _, s, _ in rows}
assert len(rows) == 56, len(rows)

REAL = {"REAL GAP", "AMBIGUOUS, lean real"}
c = Counter("DUPLICATE" if l.startswith("DUPLICATE") else l for l in label.values())
real = [q for q, l in label.items() if l in REAL]
noise = [q for q, l in label.items() if l.startswith("NOISE") or l == "AMBIGUOUS, lean noise"]

clusters = re.findall(r"^\| ([A-M/]+) \| .+? \| ([Q\d, ]+) \| (.+?) \|$", text.split("## Clusters")[1].split("## Where")[0], re.M)
distinct = [(n, [q for q in re.findall(r"Q\d+", qs) if q in real]) for n, qs, _ in clusters]
distinct = [(n, qs) for n, qs in distinct if qs]
blocking = [n for n, qs, sev in clusters if sev.startswith("Blocks") and any(q in real for q in re.findall(r"Q\d+", qs))]
orphans = sorted(set(real) - {q for _, qs in distinct for q in qs}, key=lambda x: int(x[1:]))

lines = [
    "| Measure | Count |", "|---|---|",
    f"| Questions | {len(rows)} |",
    f"| **Real-gap questions** | **{len(real)}** ({c['REAL GAP']} firm, {c['AMBIGUOUS, lean real']} lean real) |",
    f"| **Distinct gaps** (clusters, I/J once) | **{len(distinct)}** |",
    f"| Distinct gaps that block routing | {len(blocking)} ({', '.join(blocking)}) |",
    f"| Already known | {c['ALREADY KNOWN']} |",
    f"| Out of scope | {c['OUT OF SCOPE']} |",
    f"| Duplicates | {c['DUPLICATE']} |",
    f"| Noise, including lean noise | {len(noise)} ({c['NOISE, answered by v1']} answered by v1, {c['NOISE, engineering choice']} engineering choice, {c['AMBIGUOUS, lean noise']} lean noise) |",
]
check = len(real) + len(noise) + c["ALREADY KNOWN"] + c["OUT OF SCOPE"] + c["DUPLICATE"]
assert check == 56 and not orphans, (check, orphans)
block = "\n".join(lines)
print(block)
if "--write" in sys.argv:
    new = re.sub(r"<!-- COUNTS -->.*<!-- /COUNTS -->", lambda m: "<!-- COUNTS -->\n" + block + "\n<!-- /COUNTS -->", text, flags=re.S)
    FILE.write_text(new, encoding="utf8")
    print("\nwritten")
