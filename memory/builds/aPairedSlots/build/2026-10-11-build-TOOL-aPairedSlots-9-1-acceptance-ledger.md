# Acceptance ledger — node a's slot count and share rule, from the two-bar A/B

**Serves:** journal TOOL-aPairedSlots-9

Observed on node a on 2026-10-12, by reading the committed results record and running its rule
check over the committed rows against the tree, and then against two staged breaks.

**Evidences:** TOOL-aPairedSlots-9
- AC1 — `2026-10-11-build-TOOL-aPairedSlots-9-ab-results.md` — A1's MAKESPAN row is 8440 s with
  both bars reporting all 65 legs. B1 and C1 each carry a lower bound past 8440 s from an arm-run
  stopped there, and every arm-run carries a grade from its samples' foreign-process column: all
  three contaminated. The void B1 launch is named and decides nothing.
- AC2 — `2026-10-11-build-TOOL-aPairedSlots-9-rule-check.py` — over the committed rows and the tree
  it printed AGREE: no `slots` key on the `capable` row and `TS_SHARE_RULE=full`. With `slots=2`
  staged onto a copy of the row it printed DISAGREE, and with `TS_SHARE_RULE=half` staged into a
  copy of the runner it printed DISAGREE.
