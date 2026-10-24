# TOOL-dDeclaredLoop-100 deviation 1001 — the round-12 spec audit promoted a unit for its batched minors

**Serves:** deviation TOOL-dDeclaredLoop-100

- **Departs from:** dDeclaredLoop [roster]
- **Hand-off:** design-to-spec
- **Before:** dDeclaredLoop's roster carries thirty-four units, `TOOL-dDeclaredLoop-1` to `TOOL-dDeclaredLoop-34`, one per clause of its row, beside `TOOL-dDeclaredLoop-35`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dDeclaredLoop-100`, the round-12 spec audit's 21 minors, batched.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the spec-audit round 12 minors batch. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-12 spec audit, `memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md`; the rescope add row for `TOOL-dDeclaredLoop-100` in `memory/builds/dDeclaredLoop/RUN.md`; the unit's spec, `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-100.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dDeclaredLoop-100
- **Caused-by:** PLAY-dClosedLoop-2
