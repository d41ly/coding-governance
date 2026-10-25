# TOOL-dPlacedRequest-44 deviation 441 — the round-3 spec audit promoted a unit for a blocker

**Serves:** deviation TOOL-dPlacedRequest-44

- **Departs from:** dPlacedRequest [roster]
- **Hand-off:** design-to-spec
- **Before:** dPlacedRequest's roster carries twenty-one units, `TOOL-dPlacedRequest-1` to `TOOL-dPlacedRequest-21`, one per clause of its row, beside `TOOL-dPlacedRequest-22`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dPlacedRequest-44`, the version-bump oracle walks the build's side of the prepared merge.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the spec-audit round 3 finding 26 (BLOCKER, item B1). This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-3 spec audit, `memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md`; the rescope add row for `TOOL-dPlacedRequest-44` in `memory/builds/dPlacedRequest/RUN.md`; the unit's spec, `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-44.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dPlacedRequest-44
- **Caused-by:** PLAY-dClosedLoop-2
