"""Per-section mass and vestigiality across the spec corpus. stdlib only."""
import re, sys, pathlib, collections, statistics

ROOT = pathlib.Path(sys.argv[1])
specs = sorted((ROOT / "memory" / "builds").glob("*/spec/**/*.md"))
SEC = re.compile(r"^## (\d+)\.\s*(.*)$", re.M)

NAMES = {
    "1": "Goal", "2": "Scope (IN)", "3": "Non-goals (OUT)", "4": "Design",
    "5": "Production-readiness", "6": "Acceptance criteria", "7": "Gates",
    "8": "Open questions", "9": "Revision log", "10": "Reuse audit",
}

mass = collections.defaultdict(list)
na = collections.Counter()
present = collections.Counter()
tiny = collections.Counter()          # section body under 200 bytes
na_lines_s5 = collections.Counter()   # per-line N/A inside section 5
s5_lines_total = 0
s5_na_total = 0
unverified = 0
specs_with_unverified = 0
total_bytes = 0

for p in specs:
    t = p.read_text(encoding="utf-8", errors="replace")
    total_bytes += len(t.encode())
    u = len(re.findall(r"UNVERIFIED", t))
    unverified += u
    if u:
        specs_with_unverified += 1
    hits = list(SEC.finditer(t))
    for i, m in enumerate(hits):
        num = m.group(1)
        if num not in NAMES:
            continue
        end = hits[i + 1].start() if i + 1 < len(hits) else len(t)
        body = t[m.end():end].strip()
        b = len(body.encode())
        mass[num].append(b)
        present[num] += 1
        if re.match(r"^N/A\b", body) or re.match(r"^\*?\*?N/A", body):
            na[num] += 1
        if b < 200:
            tiny[num] += 1
        if num == "5":
            for ln in body.splitlines():
                ln = ln.strip()
                if ln.startswith("-") or ln.startswith("*"):
                    s5_lines_total += 1
                    if "N/A" in ln or "n/a" in ln:
                        s5_na_total += 1

n = len(specs)
print(f"### {n} specs, {total_bytes:,} bytes total\n")
grand = sum(sum(v) for v in mass.values())
print(f"{'§':>3} {'section':<22} {'present':>7} {'median B':>9} {'mean B':>8} "
      f"{'% of mass':>9} {'N/A':>5} {'<200B':>6}")
for k in sorted(NAMES, key=int):
    v = mass.get(k, [])
    if not v:
        continue
    share = 100.0 * sum(v) / grand
    print(f"{k:>3} {NAMES[k]:<22} {present[k]:>7} {int(statistics.median(v)):>9,} "
          f"{int(statistics.mean(v)):>8,} {share:>8.1f}% {na[k]:>5} {tiny[k]:>6}")

print(f"\n### section 5 checklist lines: {s5_lines_total:,} bullets, "
      f"{s5_na_total:,} carry N/A ({100.0*s5_na_total/max(1,s5_lines_total):.1f}%)")
print(f"### UNVERIFIED markers: {unverified} occurrences in {specs_with_unverified} of {n} specs "
      f"({100.0*specs_with_unverified/n:.1f}%)")
print(f"\n### body mass outside section 4 (the mechanism): "
      f"{100.0*(grand-sum(mass.get('4',[])))/grand:.1f}% of all section bytes")
