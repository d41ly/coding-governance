# **Serves:** journal TOOL-aMeteredSweep-1
"""Join a run-gates run record's `N.leg` rows to the leg manifest, one TSV row per leg.

    python <this file> <git-dir>/gate-run/<run-id> tools/gate-legs.json > rows.tsv

Columns: pool seconds, leg, chunk, subject, ceiling, pool verdict, retry seconds (blank when the leg
did not overrun), final verdict, the census's foreign-process count. The rows this build recorded are
the `-legs.tsv` file beside this one. WHAT THIS DOES NOT CHECK: that the run was quiet, or that a
leg's seconds are its own cost rather than the pool's contention; the serial retry column is the only
uncontended reading the record holds.
"""
import glob
import json
import os
import sys

run, manifest = sys.argv[1], sys.argv[2]
meta = {leg["name"]: leg for leg in json.load(open(manifest, encoding="utf-8"))}
rows = {}
for p in glob.glob(os.path.join(run, "*.leg")):
    f = open(p, encoding="utf-8").read().rstrip("\n").split("\t")
    r = rows.setdefault(f[0], {})
    r["retry" if ".retry." in p else "pool"] = (f[1], float(f[3]), f[7] if len(f) > 7 else "")
out = []
for name, r in rows.items():
    m = meta.get(name, {})
    st, secs, fo = r["pool"]
    rt = r.get("retry")
    out.append((secs, name, m.get("chunk", ""), m.get("subject", ""), m.get("ceiling", ""), st,
                f"{rt[1]:.0f}" if rt else "", rt[0] if rt else st, fo))
print("secs\tleg\tchunk\tsubject\tceiling\tpool\tretry_secs\tfinal\tforeign")
for row in sorted(out, reverse=True):
    print(f"{row[0]:.0f}\t" + "\t".join(str(c) for c in row[1:]))
