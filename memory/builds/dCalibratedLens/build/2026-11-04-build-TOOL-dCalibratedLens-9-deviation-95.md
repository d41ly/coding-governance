# TOOL-dCalibratedLens-9 deviation 95 — TOOL-dCalibratedLens-9's spec revised by the cross-check folds' spec audit

**Serves:** deviation TOOL-dCalibratedLens-9

- **Departs from:** `TOOL-dCalibratedLens-9@rev-4`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dCalibratedLens-9`'s spec as the revision at `TOOL-dCalibratedLens-9@rev-4` reads it: a 60 s bound sized on a one-process read the fold replaced with one `show` per act, and probe records listed by `git ls-files`.
- **After:** the spec at rev-5, revised for the review's items M4 and L5: the bound re-derived as 180 s for one `show` per act with a recorded 500-act timing, and probe records read through `find --kind probe --all` and `show`, as the brief `memory/builds/dCalibratedLens/prompts/2026-11-04-prompt-TOOL-dCalibratedLens-1-crosscheck-audit-disposal.md` states.
- **Cause:** review
- **Reason:** the 2026-11-04 spec audit of the 2026-11-03 cross-check folds, run on the owner's "rest with recommendations", confirmed each item, and every one is LOCAL under BUILD-METHOD M4's nature rule, so it folds at the disposal. No code has started.
- **Evidence:** `memory/builds/dCalibratedLens/reviews/2026-11-04-review-TOOL-dCalibratedLens-1-crosscheck-spec-audit.md`, and the rev-5 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dCalibratedLens/prompts/2026-11-04-prompt-TOOL-dCalibratedLens-9-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dCalibratedLens-18
- **Caused-by:** 2026-11-04-review-TOOL-dCalibratedLens-1-crosscheck-spec-audit
