# Acceptance ledger — TOOL-aQuenchedHarness-7

**Serves:** journal TOOL-aQuenchedHarness-7

**Evidences:** TOOL-aQuenchedHarness-7

Tier-2 · node a · 2026-09-07. One line per numbered criterion, each naming the observation that
answered it. A line saying MET without an observation is a checkbox, which is why the gate refuses
one; a line saying NOT MET is equally a result and is recorded the same way.

- AC1 — MET, OBSERVED — `bash tools/unattended/check-unattended.sh` produces byte-identical stdout and exit status across the change, 46 lines and rc 1 on both arms of a controlled A/B, each arm asserting it did the work rather than only how long it took.
- AC2 — MET, OBSERVED — 20.9 git spawns per `RUN*.md` record against the declared 22, and 51.3 before; all external processes 5420 to 2321.
- AC3 — NOT MET on both halves. Wall is 435 s and 487 s across two quiet readings against a declared `400` s, missed by 9% at best. And `BUDGET_kit_gate` moves UP, 240 to 660, because the tree it walks doubled between the two readings: records x1.96 while the leg's cost went x3.34.
- AC4 — NOT DONE. The spawn-count regression arm has one home, `tools/unattended/check-unattended.test.sh`, which measured 9067 s and is RED; a pin in a suite nobody can afford to run is the shape this build argues against, and a standalone leg would cost the 435 s the unit exists to remove.
- AC5 — NOT DONE. The `check-pass-order.sh` erosion pin was not written; its win at `274aa39b` is cited but unguarded.
- AC6 — NOT DONE. `run-unattended-gates.sh` and `tools/gate-legs.json` still do not cross-point at each other's figure for this leg.
