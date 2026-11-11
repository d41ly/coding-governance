# TOOL-dCalibratedLens-5 deviation 51 — `demote-then-propose` files the demotion, the loop performs none

**Serves:** deviation TOOL-dCalibratedLens-5

- **Departs from:** `dCalibratedLens` [review.loop.retire]
- **Hand-off:** design-to-spec
- **Before:** `review.loop.retire` · propose-ratify, demote-then-propose, report · propose-ratify (v2:1343), the owner's R2 options "Propose, you ratify", "Demote, then propose" and "Report only" for a gate, rule or bug class that caught nothing in its window
- **After:** under `demote-then-propose` the Loop Review files a `demote` proposal for an idle priced row or a unit bearing no load, and proposes its retirement once an earlier review a full window back proposed the demotion; the loop itself demotes nothing, and the owner applies a demotion as any other filed proposal
- **Cause:** design defect
- **Reason:** No clause or record says how a loop demotes, and every route to a demotion is a write the loop may not make: a unit is written only through `instructions_edit.py`, which refuses an agent under the default `instructions.edit`; a leg or cap is a policy or manifest change, and the brief's S8 has a loop item write no policy value. Performing the demotion would widen the loop's write surface to instruction text and gate manifests, a security veto. The spec keeps the value distinct from its two siblings, each seen on its planted case: a demotion comes first and a retirement only after a window, rather than a retirement at once (`propose-ratify`) or nothing filed (`report`). TOOL-dCalibratedLens-5 §8 F2 records the options.
- **Evidence:** the walkthrough's R2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md:737-739`; the policy row, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1343`; the guarded write, `memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md` S3 and S4; the brief's S8, `memory/builds/dCalibratedLens/prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md:117-123`; the fork, `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-5.md` §8 F2; rung 3, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:909`
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of dCalibratedLens's spec run, under the chain's `author-recorded` value (README rule 5); carried for the owner's walk unless it rules otherwise
- **Follow-through:** usage review.loop.retire
- **Caused-by:** TOOL-dCalibratedLens-5
