**Serves:** journal DEPL-dGaugedVintage-11

# Acceptance ledger — DEPL-dGaugedVintage-11, the fan-out rung

**Evidences:** DEPL-dGaugedVintage-11

- AC1 — amended rev-3 — the end-to-end `update` over a two-destination fixture was not built; the
  resolution that decides it was, and is asserted directly. Logged in §9.
- AC2 — `python tools/govkit/selftest.py` — `DEPL-dCarriedReceipt-9`'s own AC2 arm still passes,
  which is the regression check: it asserts the run names the dropped ambiguous directory and both
  destinations. It caught a reword of that message during this build and the original wording was
  restored, since that arm asserts a ratified contract.
- AC3 — `python tools/govkit/govkit.py update --target <fixture>` — over a receipt with no fan-out
  the run prints `carry map: 1 directory pair(s), 2 needle(s), 0 fanned-out director(y|ies)`. The
  zero is explicit; before this the line stopped at the needle count and a run that dropped nothing
  was indistinguishable from one whose drop report never executed.
- AC4 — `python tools/govkit/selftest.py` — two rows under ONE gov directory resolve to different
  destinations, each from its own `(source, path)` pair: `scripts/k` for the engine row and
  `.claude/skills/k` for the Skill row. A row with no pair falls back to the global map rather than
  emptying it. No descriptor is re-resolved, which `derive_carry_map`'s docstring forbids.
- AC5 — `bash tools/run-gates/run-gates.sh` — `govkit acceptance matrix` and the whole govkit
  selftest stay green, so `relocate` is unchanged for non-fanning kits.

## What this ledger does not claim

The GLOBAL needle map still holds one destination per gov directory and still drops a fan-out — it
cannot hold two, and this unit did not change that. What changed is that rows under a dropped
directory are no longer rewritten through nothing. The count of kits fanning out on the measured
adopter is the review lens's, never re-derived here.
