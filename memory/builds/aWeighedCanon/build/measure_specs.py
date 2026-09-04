"""Corpus measurements for the spec-template research. stdlib only, no agents."""
import re, sys, subprocess, collections, pathlib, json

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
specs = sorted((ROOT / "memory" / "builds").glob("*/spec/**/*.md"))

HDR = re.compile(
    r"^\*\*Status:\*\*\s*(?P<tok>[A-Z]+)\s*·\s*rev-(?P<rev>\d+)\s*·\s*(?P<date>\d{4}-\d{2}-\d{2})"
    r".*?·\s*Tier-(?P<tier>[12])",
    re.M,
)
SEC = re.compile(r"^## (\d+)\. (.+)$", re.M)

rows = []
for p in specs:
    t = p.read_text(encoding="utf-8", errors="replace")
    m = HDR.search(t)
    secs = SEC.findall(t)
    rows.append(
        dict(
            path=str(p.relative_to(ROOT)).replace("\\", "/"),
            build=p.parts[len(ROOT.parts) + 2],
            bytes=len(t.encode()),
            lines=t.count("\n") + 1,
            tok=m.group("tok") if m else None,
            rev=int(m.group("rev")) if m else None,
            date=m.group("date") if m else None,
            tier=int(m.group("tier")) if m else None,
            nsec=len(secs),
            secnames=[s[0] for s in secs],
            has8=any(s[0] == "8" for s in secs),
            has10=any(s[0] == "10" for s in secs),
        )
    )


def dist(vals):
    c = collections.Counter(vals)
    return {k: c[k] for k in sorted(c, key=lambda x: (x is None, x))}


def pct(n, d):
    return f"{100.0*n/d:.1f}%" if d else "n/a"


print(f"### corpus: {len(rows)} spec files")
print(f"unparsed status header: {sum(1 for r in rows if r['tok'] is None)}")
print(f"total bytes: {sum(r['bytes'] for r in rows):,}")
print(f"median bytes: {sorted(r['bytes'] for r in rows)[len(rows)//2]:,}")
print(f"mean bytes: {sum(r['bytes'] for r in rows)//len(rows):,}")

print("\n### rev high-water (ALL specs)")
revs = [r["rev"] for r in rows if r["rev"]]
print(dist(revs))
print(f"n={len(revs)}  rev-1 share: {pct(sum(1 for v in revs if v==1), len(revs))}")
print(f"median rev: {sorted(revs)[len(revs)//2]}   mean rev: {sum(revs)/len(revs):.2f}")
print(f">=rev-5: {sum(1 for v in revs if v>=5)} ({pct(sum(1 for v in revs if v>=5), len(revs))})")

print("\n### rev by tier")
for tier in (1, 2):
    v = [r["rev"] for r in rows if r["tier"] == tier and r["rev"]]
    if v:
        print(
            f"Tier-{tier}: n={len(v)} mean={sum(v)/len(v):.2f} "
            f"rev1={pct(sum(1 for x in v if x==1), len(v))} max={max(v)}"
        )

print("\n### status tokens")
print(dist([r["tok"] for r in rows]))

print("\n### tier split")
print(dist([r["tier"] for r in rows]))

print("\n### section counts (how many ## N. sections)")
print(dist([r["nsec"] for r in rows]))

print("\n### size vs rev — does a longer spec churn less?")
byrev = collections.defaultdict(list)
for r in rows:
    if r["rev"]:
        byrev[min(r["rev"], 6)].append(r["bytes"])
for k in sorted(byrev):
    v = sorted(byrev[k])
    lbl = f"rev-{k}" + ("+" if k == 6 else "")
    print(f"{lbl}: n={len(v):3d} median bytes={v[len(v)//2]:6,}")

print("\n### WONTDO — specs written then abandoned")
wd = [r for r in rows if r["tok"] == "WONTDO"]
print(f"{len(wd)} ({pct(len(wd), len(rows))}) — bytes: {sum(r['bytes'] for r in wd):,}")
print(f"their mean rev: {sum(r['rev'] for r in wd if r['rev'])/max(1,len([r for r in wd if r['rev']])):.2f}")

print("\n### per-build spec counts")
b = collections.Counter(r["build"] for r in rows)
print(f"builds with specs: {len(b)}  max units in one build: {max(b.values())}")

json.dump(rows, open(sys.argv[2], "w") if len(sys.argv) > 2 else sys.stdout if False else open("specrows.json", "w"), indent=0)
print("\nwrote specrows.json")
