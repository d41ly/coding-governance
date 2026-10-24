# TOOL-dDeclaredLoop-80 deviation 801 — the round-5 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dDeclaredLoop-80

- **Departs from:** dDeclaredLoop [roster]
- **Hand-off:** design-to-spec
- **Before:** dDeclaredLoop's roster carries thirty-four units, `TOOL-dDeclaredLoop-1` to `TOOL-dDeclaredLoop-34`, one per clause of its row, beside `TOOL-dDeclaredLoop-35`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dDeclaredLoop-80`, the no-own-conf-read rule stops at a named fixture boundary, so the plants that write the confs are outside its population.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the spec-audit round 5 finding 20 (HIGH, item H1). This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-5 spec audit, `memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md`; the rescope add row for `TOOL-dDeclaredLoop-80` in `memory/builds/dDeclaredLoop/RUN.md`; the unit's spec, `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-80.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dDeclaredLoop-80
- **Caused-by:** PLAY-dClosedLoop-2
