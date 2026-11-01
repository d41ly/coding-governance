# TOOL-dLinkedLibrary-49 deviation 491 — the round-1 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dLinkedLibrary-49

- **Departs from:** dLinkedLibrary [roster]
- **Hand-off:** design-to-spec
- **Before:** dLinkedLibrary's roster carries twenty-five units, `TOOL-dLinkedLibrary-1` to `TOOL-dLinkedLibrary-25`, one per clause of its row, beside `TOOL-dLinkedLibrary-26`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dLinkedLibrary-49`, `--observe` records `refused` only on the leg's failing status, bounded, and every other outcome as `unobservable`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit round1 (reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) finding id 64 at HIGH, report item R13; repairs TOOL-dLinkedLibrary-24. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-1 spec audit, `memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`; the rescope add row for `TOOL-dLinkedLibrary-49` in `memory/builds/dLinkedLibrary/RUN.md`; the unit's spec, `memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-49.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dLinkedLibrary-49
- **Caused-by:** PLAY-dClosedLoop-2
