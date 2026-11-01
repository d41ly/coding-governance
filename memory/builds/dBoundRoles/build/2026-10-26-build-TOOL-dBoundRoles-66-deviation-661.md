# TOOL-dBoundRoles-66 deviation 661 — the round-7 spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dBoundRoles-66

- **Departs from:** dBoundRoles [roster]
- **Hand-off:** design-to-spec
- **Before:** dBoundRoles' roster carries twenty-six units, `TOOL-dBoundRoles-1` to `TOOL-dBoundRoles-26`, one per clause of its row, beside `TOOL-dBoundRoles-27`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dBoundRoles-66`, from the round-7 spec audit: spec-audit round1 of unit 64 minors batched in one unit (BUILD-METHOD M4, no disjoint split by M6): MEDIUM ids 2 10 18 8 19 3 1 12 16 22 23 (items M1-M8) and LOW ids 24 20 4 5 6 7 13 9 14 15 17 21 (items L1-L11).
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it and the minors batched; this unit closes the findings named in After. This is a spec run, so the unit is specced, audited as M4 provides, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-7 spec audit, `memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-64-spec-audit-round1.md`; the rescope add row for `TOOL-dBoundRoles-66` in `memory/builds/dBoundRoles/RUN.md`; the unit's spec, `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-66.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dBoundRoles-66
- **Caused-by:** PLAY-dClosedLoop-2
