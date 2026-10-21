# TOOL-dTrueNorth-10 deviation 9 — the round-1 spec audit promoted a unit

**Serves:** deviation TOOL-dTrueNorth-10

- **Departs from:** dTrueNorth [roster]
- **Hand-off:** design-to-spec
- **Before:** dTrueNorth's roster carries the seven units its README opened with: the six clauses of its v2 row and `TOOL-dTrueNorth-7`.
- **After:** the roster also carries `TOOL-dTrueNorth-10`, deviation records 2 and 3, written verbatim at kind `deviation`, the view re-rendered in their commit.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a spec audit's exit to a unit whose mechanism closes it; this unit closes one confirmed high of that round, and the run builds it rather than carrying it forward, since dTrueNorth is a whole run (README rule 1).
- **Evidence:** the round-1 spec audit, `memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md`; the rescope add row for `TOOL-dTrueNorth-10` in `memory/builds/dTrueNorth/RUN.md`; the unit's spec, `memory/builds/dTrueNorth/spec/2026-10-21-spec-TOOL-dTrueNorth-10.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-10
- **Caused-by:** PLAY-dClosedLoop-2
