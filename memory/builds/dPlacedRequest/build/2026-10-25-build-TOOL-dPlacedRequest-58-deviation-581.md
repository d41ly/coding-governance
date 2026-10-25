# TOOL-dPlacedRequest-58 deviation 581 — the round-6 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dPlacedRequest-58

- **Departs from:** dPlacedRequest [roster]
- **Hand-off:** design-to-spec
- **Before:** dPlacedRequest's roster carries twenty-one units, `TOOL-dPlacedRequest-1` to `TOOL-dPlacedRequest-21`, one per clause of its row, beside `TOOL-dPlacedRequest-22`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dPlacedRequest-58`, every attempt of the placed race starts with no handshake file an earlier attempt left.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the spec-audit round 6 finding 20 (HIGH, item H2). This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-6 spec audit, `memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md`; the rescope add row for `TOOL-dPlacedRequest-58` in `memory/builds/dPlacedRequest/RUN.md`; the unit's spec, `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-58.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dPlacedRequest-58
- **Caused-by:** PLAY-dClosedLoop-2
