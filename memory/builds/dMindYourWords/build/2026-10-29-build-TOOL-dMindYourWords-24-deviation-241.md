# TOOL-dMindYourWords-24 deviation 241 — a spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dMindYourWords-24

- **Departs from:** dMindYourWords [roster]
- **Hand-off:** design-to-spec
- **Before:** dMindYourWords's roster carries seventeen units, `TOOL-dMindYourWords-1` to `TOOL-dMindYourWords-17`, one per clause of its row, beside `TOOL-dMindYourWords-18`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dMindYourWords-24`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes 2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md id 23 (HIGH, item H2): the policy read finds its kit by a parent.parent probe instead of resolve_kit_dir
- **Evidence:** the spec audit, `memory/builds/dMindYourWords/reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md`; the rescope add row for `TOOL-dMindYourWords-24` in `memory/builds/dMindYourWords/RUN.md`; the unit's spec, `memory/builds/dMindYourWords/spec/2026-10-29-spec-TOOL-dMindYourWords-24.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dMindYourWords-24
- **Caused-by:** PLAY-dClosedLoop-2
