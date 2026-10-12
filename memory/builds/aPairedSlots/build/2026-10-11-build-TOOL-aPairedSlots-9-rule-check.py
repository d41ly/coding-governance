#!/usr/bin/env python3
# **Serves:** journal TOOL-aPairedSlots-9
"""Recompute TOOL-aPairedSlots-9 §4's rule from the committed rows and compare it with the tree.

Usage: <rows.tsv> <gate-profiles.txt> <run-gates.sh>; exits 1 when either value disagrees."""
import re
import sys

rows, profiles, runner = sys.argv[1:4]
# AN ARM-RUN IS PROVEN BY ITS OWN TWO BAR ROWS (TOOL-aPairedSlots-12), never by the MAKESPAN row's
# proof column: on A1 that column collected the expected-leg count, because each bar row carried the
# verdict file's `ended<TAB><time>` as two fields. A seventeen-field row with `ended` in its verdict
# column is that shifted layout, and is read one place right.
mk = {}
bars = []
for line in open(rows, encoding="utf-8"):
    f = line.rstrip("\n").split("\t")
    if line.startswith("#") or len(f) < 13 or f[0] == "arm":
        continue
    if f[2] == "MAKESPAN":
        # The last arm-run of a name wins: B1's void launch comes first.
        mk[f[0] + f[1]] = (int(f[6]), len(bars) == 2 and all(bars))
        bars = []
        continue
    o = 1 if len(f) == 17 and f[8] == "ended" else 0
    ok, fail, exp, proof = f[9 + o], f[10 + o], f[11 + o], f[12 + o]
    summed = all(x.isdigit() for x in (ok, fail, exp)) and int(ok) + int(fail) == int(exp)
    bars.append(proof == "yes" and summed)
a, a_ok = mk["A1"]
if not a_ok:
    print(f"A1 {a} is unproven: its bar rows do not both carry every leg, so the rule cannot decide")
    sys.exit(2)
passes = [k for k in ("B1", "C1") if mk[k][1] and mk[k][0] <= a]
want_slots = "2" if passes else None
b, c = mk["B1"], mk["C1"]
shown_b_lt_c = (b[1] and c[1] and b[0] < c[0]) or (b[1] and not c[1] and b[0] < c[0])
want_rule = "half" if shown_b_lt_c else "full"

cap = [l for l in open(profiles, encoding="utf-8") if re.match(r"^capable\s", l)]
assert len(cap) == 1, cap
m = re.search(r"\bslots=(\d+)", cap[0])
have_slots = m.group(1) if m else None
rules = re.findall(r"^TS_SHARE_RULE=(\w+)", open(runner, encoding="utf-8").read(), re.M)
assert len(rules) == 1, rules
print(f"A1 {a} proven; B1 {b}; C1 {c}")
print(f"slots: rule {want_slots or 'none (1)'}, tree {have_slots or 'none (1)'}")
print(f"TS_SHARE_RULE: rule {want_rule}, tree {rules[0]}")
ok = want_slots == have_slots and want_rule == rules[0]
print("AGREE" if ok else "DISAGREE")
sys.exit(0 if ok else 1)
