# TOOL-dLinkedLibrary-85 deviation 851 — the round-5 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dLinkedLibrary-85

- **Departs from:** dLinkedLibrary [roster]
- **Hand-off:** design-to-spec
- **Before:** dLinkedLibrary's roster carries twenty-five units, `TOOL-dLinkedLibrary-1` to `TOOL-dLinkedLibrary-25`, one per clause of its row, and the spec audit's promotions `TOOL-dLinkedLibrary-37` to `TOOL-dLinkedLibrary-80`, beside `TOOL-dLinkedLibrary-26`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dLinkedLibrary-85`, the CI census reads a block-scalar header on a list item that opens with a key, the GitHub `- run: |` step.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit of units 75 to 80 round1 (reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md) finding id 35 at HIGH, report item H4 (id 1 binds the same defect at MEDIUM, item M1, batched in TOOL-dLinkedLibrary-86); repairs TOOL-dLinkedLibrary-77. This is a spec run, so the unit is specced, audited as M4 and the owner's ruling of 2026-10-27 provide, and carried forward once, and the build run after it builds it.
- **Evidence:** the round-5 spec audit, `memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md`; the rescope add row for `TOOL-dLinkedLibrary-85` in `memory/builds/dLinkedLibrary/RUN.md`; the unit's spec, `memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-85.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dLinkedLibrary-85
- **Caused-by:** PLAY-dClosedLoop-2
