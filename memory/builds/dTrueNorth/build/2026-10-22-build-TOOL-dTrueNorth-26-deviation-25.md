# TOOL-dTrueNorth-26 deviation 25 — the closing diff review promoted its minors to a unit

**Serves:** deviation TOOL-dTrueNorth-26

- **Departs from:** dTrueNorth [roster]
- **Hand-off:** design-to-spec
- **Before:** dTrueNorth's roster carries the twenty units its spec run and both spec audits gave it, and the three units the closing diff review's highs added, `TOOL-dTrueNorth-23` to `TOOL-dTrueNorth-25`.
- **After:** the roster also carries `TOOL-dTrueNorth-26`, the closing diff review's confirmed minors, items M1 to M9 and L1 to L7, M7 discharged by `TOOL-dTrueNorth-25` with H3.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 disposes every confirmed MEDIUM and LOW at a review's exit by promoting it, batched into one unit naming them all; this unit is that batch, and the run builds it rather than carrying it forward, since dTrueNorth is a whole run (README rule 1).
- **Evidence:** the closing diff review, `memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md`; the rescope add row for `TOOL-dTrueNorth-26` in `memory/builds/dTrueNorth/RUN.md`; the unit's spec, `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-26.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-26
- **Caused-by:** PLAY-dClosedLoop-2
