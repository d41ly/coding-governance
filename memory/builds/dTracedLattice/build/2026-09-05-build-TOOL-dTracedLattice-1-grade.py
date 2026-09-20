# **Serves:** research TOOL-dTracedLattice-1 TOOL-dTracedLattice-7
# Committed as evidence for the recall measurement. The root is DERIVED here; the
# Accessor names are conformed to this repo's declared VERBS table; behaviour is unchanged
# and every rename is applied across all committed copies, so cross-file calls follow. The
# figures in the report were produced by the scratchpad originals, which differ from these
# copies in the derived root and in these names only.
# scratchpad original hardcoded this session's worktree and would resolve to nothing.
#!/usr/bin/env python3
"""Baseline-grade scen-2-recall.json so the set is demonstrably LIVE rather than a JSON file.

Two things it proves, and one it measures:

  LIVENESS   every expected id resolves to at least one document in `records`. An entry that
             resolves to none is a DEAD PROBE and is printed as one, never averaged in as a 0.
  CONTROL    the 12 shipped questions must reproduce the declared floor RECALL_FLOOR in
             .memory-tree.conf (records:fts5:r@5). A harness that misses it is broken upstream of
             anything the new scenarios could tell you.
  TERMS      the same questions ranked with and without the recorded `Recall terms used:` rewrite.
             bench.py never reads terms, so this arm exists only because the scenarios carry them.
             It APPROXIMATES query.py: that program ORs `match_expr(question)` with each supplied
             term quoted whole, and this concatenates before tokenizing, which splits a hyphenated
             term. Treat the delta as directional, not as query.py's number.

Usage: python grade.py <repo-root> <scratch-dir>
"""
from __future__ import annotations
import json, pathlib, sys, collections

REPO = pathlib.Path(sys.argv[1]).resolve()
SCR = pathlib.Path(sys.argv[2]).resolve()
sys.dont_write_bytecode = True
sys.path.insert(0, str(REPO / "tools" / "memory-recall"))
import bench  # noqa: E402

DATA = SCR / "data"
doc = json.loads((SCR / "scen-2-recall.json").read_text(encoding="utf-8"))
qs = doc["queries"]
anchors = json.loads((DATA / "anchors.json").read_text(encoding="utf-8"))
docs = bench.load(DATA, "records")
db = bench.build_index(docs)
KS = [1, 5, 10, 20]

print("corpus: %d records docs" % len(docs))
rows = []
dead = []
for q in qs:
    targets = bench.expected_by_target(docs, q, anchors)
    if not targets:
        dead.append(q["scenario_id"])
        continue
    r_plain = bench.run_fts(db, q["query"], max(KS), False)
    s_plain = bench.score(docs, r_plain, targets, KS)
    if q.get("terms"):
        r_terms = bench.run_fts(db, q["query"] + " " + q["terms"], max(KS), False)
        s_terms = bench.score(docs, r_terms, targets, KS)
    else:
        s_terms = None
    rows.append((q, s_plain, s_terms))

if dead:
    print("DEAD PROBE -- expected ids resolve to no document: %s" % ", ".join(dead))
else:
    print("liveness: every one of %d scenarios resolves at least one target document" % len(rows))


def build_agg(sel, key, field):
    v = [s[field] for q, sp, st in rows for s in [{"plain": sp, "terms": st}[key]]
         if sel(q) and s is not None]
    return (sum(v) / len(v), len(v)) if v else (float("nan"), 0)


print("\n%-16s %4s   %-28s   %s" % ("class", "n", "question only  r@1/5/10/20", "with recorded terms"))
for cls in ("CONTROL", "GRADED", "STABILITY-ONLY"):
    sel = lambda q, c=cls: q["class"] == c
    n = sum(1 for q, _, _ in rows if sel(q))
    p = "/".join("%.2f" % build_agg(sel, "plain", "r@%d" % k)[0] for k in KS)
    tv = [build_agg(sel, "terms", "r@%d" % k) for k in KS]
    t = "/".join("%.2f" % a for a, _ in tv) if tv[0][1] else "     n/a (no terms recorded)"
    print("%-16s %4d   %-28s   %s" % (cls, n, p, t))

for kind in ("graded-miss", "graded-binding"):
    sel = lambda q, kk=kind: q["provenance"]["kind"] == kk
    n = sum(1 for q, _, _ in rows if sel(q))
    print("  %-14s %4d   %-28s   %s" % ("..." + kind, n,
          "/".join("%.2f" % build_agg(sel, "plain", "r@%d" % k)[0] for k in KS),
          "/".join("%.2f" % build_agg(sel, "terms", "r@%d" % k)[0] for k in KS)))

sel_clean = lambda q: q["class"] == "STABILITY-ONLY" and not q["overlap_over_max"]
n = sum(1 for q, _, _ in rows if sel_clean(q))
print("%-16s %4d   %-28s   %s" % ("  ...overlap-ok", n,
      "/".join("%.2f" % build_agg(sel_clean, "plain", "r@%d" % k)[0] for k in KS),
      "/".join("%.2f" % build_agg(sel_clean, "terms", "r@%d" % k)[0] for k in KS)))

pin = None
for line in (REPO / ".memory-tree.conf").read_text(encoding="utf-8").splitlines():
    if line.startswith("RECALL_FLOOR="):
        pin = line.split("=", 1)[1].strip().strip('"')
print("\ndeclared %s" % pin)
ctrl_r5, cn = build_agg(lambda q: q["class"] == "CONTROL", "plain", "r@5")
print("measured CONTROL records:fts5:r@5 = %.4f over %d questions -- %s"
      % (ctrl_r5, cn, "AT OR ABOVE the floor" if ctrl_r5 >= float(pin.split(">=")[1]) else "BELOW"))
print("\nper-scenario r@5 (question only):")
for q, sp, st in rows:
    if q["class"] == "GRADED":
        print("  %s %-14s r@5=%.0f  terms r@5=%s  %s"
              % (q["scenario_id"], q["provenance"]["kind"], sp["r@5"],
                 ("%.0f" % st["r@5"]) if st else "-", ",".join(q["expected_ids"])))
