# TOOL-dTrueNorth-32 deviation 35 — the round-3 closing diff review's confirmed findings and one hygiene red, promoted to a unit

**Serves:** deviation TOOL-dTrueNorth-32

- **Departs from:** dTrueNorth [roster]
- **Hand-off:** design-to-spec
- **Before:** dTrueNorth's roster carries `TOOL-dTrueNorth-1` to `TOOL-dTrueNorth-20`, `TOOL-dTrueNorth-23` to `TOOL-dTrueNorth-27` and `TOOL-dTrueNorth-29` to `TOOL-dTrueNorth-31`, every one CLOSED at `2057f2272`.
- **After:** the roster also carries `TOOL-dTrueNorth-32`, the round-3 closing diff review's 16 confirmed findings in 14 items, M1 to M6 and L1 to L8, with the memory-hygiene conf-example parity red unit 31's `GIT_CONFIG_GLOBAL` read caused, batched into one unit.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 disposes every confirmed MEDIUM and LOW at a review's exit by promoting it, batched into one unit naming them all. The round-3 closing diff review over `ef8fd59d0...2057f2272` exited CLEAN WITH FIXES with no blocker or high, and at `3c4271e8f` the memory-hygiene self-test reds one arm unit 31 caused, so this unit is that batch, and the run builds it rather than carrying it forward, since dTrueNorth is a whole run (README rule 1). The owner's instruction of 2026-10-22 ends the closing review rounds, so the unit is built because it also clears that red, and no review follows it.
- **Evidence:** the round-3 closing diff review, `memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-31-closing-diff-review-round3.md`; the owner's instruction, `memory/builds/dTrueNorth/prompts/2026-10-22-prompt-TOOL-dTrueNorth-1-owner-no-more-rounds.md`; the rescope add row for `TOOL-dTrueNorth-32` in `memory/builds/dTrueNorth/RUN.md`; the unit's spec, `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-32.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-32
- **Caused-by:** PLAY-dClosedLoop-2
