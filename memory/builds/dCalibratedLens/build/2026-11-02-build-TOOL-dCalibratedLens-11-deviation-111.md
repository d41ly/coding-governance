# TOOL-dCalibratedLens-11 deviation 111 — lead time measured from the build's opening commit, not from its intake record

**Serves:** deviation TOOL-dCalibratedLens-11

- **Departs from:** `cl-dClosedLoop-0468@8f541e2a`
- **Hand-off:** design-to-spec
- **Before:** the Loop Review's delivery metrics: lead time, landing frequency, change failure rate, time to restore, first-pass verdict rate, route-backs per build and scope drift (night pass, point 6), and the owner queue's depth, read with no bound (NP-18)
- **After:** the Loop Review's delivery metrics: lead time, from the first commit adding the build's README to the landing commit, each a committer time every node reads from git and the landing read from the landing record DEPL-dShippedRelease-1 writes, landing frequency, change failure rate, time to restore, first-pass verdict rate, route-backs per build and scope drift (night pass, point 6), and the owner queue's depth, read with no bound (NP-18)
- **Cause:** design defect
- **Reason:** The intake record (TOOL-dWellOiledMachine-4) is homed at `<git-common-dir>/requests/*`, on the node that took the request and on no other, so a Loop Review on any other node would read no lead time at all, the reason v2:1345 gives `review.loop.catch-source` its `verdict-records` default. The build's opening commit is the earliest point of a build every node holds. TOOL-dCalibratedLens-11 §8 F1 settled it by the plan's rung 3. The rest of the clause is unchanged, and the amended clause below is carried whole.
- **Evidence:** the night pass's S4, `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md` `[p6-sdlc]`; the intake record's home, `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-4.md` S-item at its line 79; the fork, `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-11.md` §8 F1; rung 3, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:910`
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dCalibratedLens's spec run, under the chain's `author-recorded` value (README rule 5); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0468@8f541e2a
- **Caused-by:** TOOL-dCalibratedLens-11
