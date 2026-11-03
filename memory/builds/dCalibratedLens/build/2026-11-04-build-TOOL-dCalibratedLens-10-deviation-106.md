# TOOL-dCalibratedLens-10 deviation 106 — TOOL-dCalibratedLens-10's spec revised by the cross-check folds' spec audit

**Serves:** deviation TOOL-dCalibratedLens-10

- **Departs from:** `TOOL-dCalibratedLens-10@rev-5`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dCalibratedLens-10`'s spec as the revision at `TOOL-dCalibratedLens-10@rev-5` reads it: a leg needing `leg_factory.py` with no precondition while its siblings plan for its absence, and two Inventory rows joined on one line.
- **After:** the spec at rev-6, revised for the review's items M9 and L3: the two-case form units 46 and 47 use, decided by `test -f tools/run-gates/leg_factory.py`, and the Inventory rows split, as the brief `memory/builds/dCalibratedLens/prompts/2026-11-04-prompt-TOOL-dCalibratedLens-1-crosscheck-audit-disposal.md` states.
- **Cause:** review
- **Reason:** the 2026-11-04 spec audit of the 2026-11-03 cross-check folds, run on the owner's "rest with recommendations", confirmed each item, and every one is LOCAL under BUILD-METHOD M4's nature rule, so it folds at the disposal. No code has started.
- **Evidence:** `memory/builds/dCalibratedLens/reviews/2026-11-04-review-TOOL-dCalibratedLens-1-crosscheck-spec-audit.md`, and the rev-6 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dCalibratedLens/prompts/2026-11-04-prompt-TOOL-dCalibratedLens-14-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dCalibratedLens-18
- **Caused-by:** 2026-11-04-review-TOOL-dCalibratedLens-1-crosscheck-spec-audit
