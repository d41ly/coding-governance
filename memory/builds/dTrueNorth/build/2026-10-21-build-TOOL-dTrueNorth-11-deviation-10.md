# TOOL-dTrueNorth-11 deviation 10 — the round-1 spec audit promoted a unit

**Serves:** deviation TOOL-dTrueNorth-11

- **Departs from:** dTrueNorth [roster]
- **Hand-off:** design-to-spec
- **Before:** dTrueNorth's roster carries the seven units its README opened with: the six clauses of its v2 row and `TOOL-dTrueNorth-7`.
- **After:** the roster also carries `TOOL-dTrueNorth-11`, the build-index and memory-hygiene self-test legs guard the spec-token checker their arms load.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a spec audit's exit to a unit whose mechanism closes it; this unit closes one confirmed high of that round, and the run builds it rather than carrying it forward, since dTrueNorth is a whole run (README rule 1).
- **Evidence:** the round-1 spec audit, `memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md`; the rescope add row for `TOOL-dTrueNorth-11` in `memory/builds/dTrueNorth/RUN.md`; the unit's spec, `memory/builds/dTrueNorth/spec/2026-10-21-spec-TOOL-dTrueNorth-11.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-11
- **Caused-by:** PLAY-dClosedLoop-2
