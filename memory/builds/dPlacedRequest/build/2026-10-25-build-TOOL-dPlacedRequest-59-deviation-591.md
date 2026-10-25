# TOOL-dPlacedRequest-59 deviation 591 — the round-6 spec audit promoted a unit for its batched minors

**Serves:** deviation TOOL-dPlacedRequest-59

- **Departs from:** dPlacedRequest [roster]
- **Hand-off:** design-to-spec
- **Before:** dPlacedRequest's roster carries twenty-one units, `TOOL-dPlacedRequest-1` to `TOOL-dPlacedRequest-21`, one per clause of its row, beside `TOOL-dPlacedRequest-22`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dPlacedRequest-59`, the round-5 promotions' minors: every oracle reader passes a base, one claim-line reader, criteria that can fail, and cites by label.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the spec-audit round 6 minors batch. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-6 spec audit, `memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md`; the rescope add row for `TOOL-dPlacedRequest-59` in `memory/builds/dPlacedRequest/RUN.md`; the unit's spec, `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dPlacedRequest-59
- **Caused-by:** PLAY-dClosedLoop-2
