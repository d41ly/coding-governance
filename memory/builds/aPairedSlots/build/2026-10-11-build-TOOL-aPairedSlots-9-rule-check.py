#!/usr/bin/env python3
# **Serves:** journal TOOL-aPairedSlots-9
"""Recompute TOOL-aPairedSlots-9 §4's rule from the committed rows and compare it with the tree.

Usage: <rows.tsv> <gate-profiles.txt> <run-gates.sh>; exits 1 when either value disagrees."""
import re
import sys

rows, profiles, runner = sys.argv[1:4]
mk = {}
for line in open(rows, encoding="utf-8"):
    f = line.rstrip("\n").split("\t")
    if len(f) > 12 and f[2] == "MAKESPAN":
        proven = f[12] not in ("NO",) and "NO" not in f[12].split()
        mk[f[0] + f[1]] = (int(f[6]), proven)  # the last row per arm-run wins: the void B1 is first
a, a_ok = mk["A1"]
assert a_ok, "A1 unproven: the rule cannot decide"
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
