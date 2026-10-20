# **Serves:** research PLAY-dClosedLoop-1
"""Join the gap register's keys against architecture v1's chain table: every gap owned exactly once,
every chain build owning at least one. Reads both records; writes nothing. Ranges like
`gap-test-01 to gap-test-09` are expanded.

Promoted from the session's scratchpad (`join_canonical.py`) for the whole-design audit's Stage 0, which runs it in any tree;
byte for byte its scratch original but for this note and the Serves line.
"""
import re
import sys

reg_path, arch_path = sys.argv[1], sys.argv[2]
with open(reg_path, encoding="utf-8") as fh:
    keys = [m.group(1) for m in re.finditer(r"^\| (gap-[a-z]+-\d\d) \|", fh.read(), flags=re.M)]
with open(arch_path, encoding="utf-8") as fh:
    arch = fh.read()

owners = {}
for line in arch.splitlines():
    m = re.match(r"^\| (d[A-Z][A-Za-z]+) \| [^|]+ \| [^|]+ \| [^|]+ \| (.+) \|$", line)
    if not m:
        continue
    build, cell = m.group(1), m.group(2)
    owned = set()
    for a, b in re.findall(r"(gap-[a-z]+-\d\d) to (gap-[a-z]+-\d\d)", cell):
        stem, lo, hi = a.rsplit("-", 1)[0], int(a.rsplit("-", 1)[1]), int(b.rsplit("-", 1)[1])
        owned |= {f"{stem}-{i:02d}" for i in range(lo, hi + 1)}
    owned |= set(re.findall(r"gap-[a-z]+-\d\d", re.sub(r"gap-[a-z]+-\d\d to gap-[a-z]+-\d\d", "", cell)))
    owners[build] = owned

count = {k: [b for b, s in owners.items() if k in s] for k in keys}
unowned = [k for k, bs in count.items() if not bs]
multi = {k: bs for k, bs in count.items() if len(bs) > 1}
phantom = sorted({g for s in owners.values() for g in s} - set(keys))
empty = [b for b, s in owners.items() if not s]
print(f"register keys {len(keys)} · chain builds {len(owners)}")
print("unowned:", unowned or "none")
print("owned twice or more:", multi or "none")
print("owned but not in the register:", phantom or "none")
print("builds owning nothing:", empty or "none")
sys.exit(1 if (unowned or multi or phantom or empty) else 0)
