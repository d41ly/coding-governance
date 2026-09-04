"""Where does the rev-driven growth actually land? Per-section mass bucketed by rev high-water."""
import re, sys, pathlib, collections, statistics

ROOT = pathlib.Path(sys.argv[1])
specs = sorted((ROOT / "memory" / "builds").glob("*/spec/**/*.md"))
SEC = re.compile(r"^## (\d+)\.\s*(.*)$", re.M)
HDR = re.compile(r"^\*\*Status:\*\*\s*[A-Z]+\s*·\s*rev-(\d+).*?·\s*Tier-([12])", re.M | re.S)
NAMES = {"1": "Goal", "2": "Scope", "3": "Non-goals", "4": "Design", "5": "Prod-ready",
         "6": "Acceptance", "7": "Gates", "8": "Open-q", "9": "Rev-log", "10": "Reuse"}

buckets = collections.defaultdict(lambda: collections.defaultdict(list))
counts = collections.Counter()

for p in specs:
    t = p.read_text(encoding="utf-8", errors="replace")
    m = HDR.search(t)
    if not m:
        continue
    rev = int(m.group(1))
    b = 1 if rev == 1 else (2 if rev <= 2 else (3 if rev <= 4 else (5 if rev <= 5 else 6)))
    counts[b] += 1
    hits = list(SEC.finditer(t))
    for i, h in enumerate(hits):
        num = h.group(1)
        if num not in NAMES:
            continue
        end = hits[i + 1].start() if i + 1 < len(hits) else len(t)
        buckets[b][num].append(len(t[h.end():end].strip().encode()))

order = [1, 2, 3, 5, 6]
lbl = {1: "rev-1", 2: "rev-2", 3: "rev-3/4", 5: "rev-5", 6: "rev-6+"}

print(f"{'section':<12}" + "".join(f"{lbl[b]:>10}" for b in order) + f"{'growth':>10}")
print("-" * (12 + 10 * len(order) + 10))
tot = {}
for k in sorted(NAMES, key=int):
    row = []
    for b in order:
        v = buckets[b].get(k, [])
        row.append(statistics.median(v) if v else 0)
    g = (row[-1] / row[0]) if row[0] else 0
    print(f"{NAMES[k]:<12}" + "".join(f"{int(x):>10,}" for x in row) + f"{g:>9.1f}x")
    tot[k] = row

print("-" * (12 + 10 * len(order) + 10))
sums = [sum(tot[k][i] for k in tot) for i in range(len(order))]
print(f"{'TOTAL':<12}" + "".join(f"{int(x):>10,}" for x in sums) +
      f"{sums[-1]/sums[0]:>9.1f}x")
print(f"{'n specs':<12}" + "".join(f"{counts[b]:>10,}" for b in order))

print("\n### share of the rev-1 -> rev-6+ median growth, by section")
delta_total = sums[-1] - sums[0]
rows = sorted(((tot[k][-1] - tot[k][0], k) for k in tot), reverse=True)
for d, k in rows:
    print(f"  {NAMES[k]:<12} +{int(d):>7,} B   {100.0*d/delta_total:>5.1f}% of the growth")

print("\n### section 9 (revision log) as a share of the whole spec, by bucket")
for i, b in enumerate(order):
    print(f"  {lbl[b]:<8} rev-log {int(tot['9'][i]):>6,} B of {int(sums[i]):>7,} B "
          f"= {100.0*tot['9'][i]/sums[i]:>4.1f}%")
