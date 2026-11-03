# TOOL-dCalibratedLens-38 deviation 381 — the round-2 spec audit promoted a unit for its high H5

**Serves:** deviation TOOL-dCalibratedLens-38

- **Departs from:** dCalibratedLens [roster]
- **Hand-off:** design-to-spec
- **Before:** dCalibratedLens's roster carries seventeen units, `TOOL-dCalibratedLens-1` to `TOOL-dCalibratedLens-17`, one per clause of its row, beside `TOOL-dCalibratedLens-18`, the opening's build ask in `BACKLOG.md`, and `TOOL-dCalibratedLens-19` to `TOOL-dCalibratedLens-30`, the round-1 spec audit's promotions.
- **After:** the roster also carries `TOOL-dCalibratedLens-38`: the work orders' adding commits are read through `tree_lib.read_adding_commits` and their policy text through `read_blobs_at`, proved on a re-added and a renamed work order, so no second adding-commit reader is written.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it; this unit closes one confirmed high of the round-2 spec audit, item H5 (finding id 19), and repairs `TOOL-dCalibratedLens-29`. This is a spec run, so the unit is specced, audited and carried forward to the build run, which builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-2 spec audit, `memory/builds/dCalibratedLens/reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`; the rescope add row for `TOOL-dCalibratedLens-38` in `memory/builds/dCalibratedLens/RUN.md`; the unit's spec, `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-38.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dCalibratedLens's spec run at the round-2 audit's disposal, under the chain's `author-recorded` value (README's deviation values)
- **Follow-through:** new unit TOOL-dCalibratedLens-38
- **Caused-by:** TOOL-dCalibratedLens-38
