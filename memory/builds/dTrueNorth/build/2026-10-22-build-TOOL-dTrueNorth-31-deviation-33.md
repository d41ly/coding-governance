# TOOL-dTrueNorth-31 deviation 33 — the round-2 closing diff review's confirmed findings, promoted to a unit

**Serves:** deviation TOOL-dTrueNorth-31

- **Departs from:** dTrueNorth [roster]
- **Hand-off:** design-to-spec
- **Before:** dTrueNorth's roster carries `TOOL-dTrueNorth-1` to `TOOL-dTrueNorth-20`, `TOOL-dTrueNorth-23` to `TOOL-dTrueNorth-27`, `TOOL-dTrueNorth-29` and `TOOL-dTrueNorth-30`, every one CLOSED at `072d97f5c`.
- **After:** the roster also carries `TOOL-dTrueNorth-31`, the round-2 closing diff review's 16 confirmed findings in 15 items, M1 to M9 and L1 to L6, batched into one unit.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 disposes every confirmed MEDIUM and LOW at a review's exit by promoting it, batched into one unit naming them all. The round-2 closing diff review over `6f5f4ddec...072d97f5c` exited CLEAN WITH FIXES with no blocker or high, so this unit is that batch, and the run builds it rather than carrying it forward, since dTrueNorth is a whole run (README rule 1).
- **Evidence:** the round-2 closing diff review, `memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-23-closing-diff-review-round2.md`; the rescope add row for `TOOL-dTrueNorth-31` in `memory/builds/dTrueNorth/RUN.md`; the unit's spec, `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-31.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-31
- **Caused-by:** PLAY-dClosedLoop-2
