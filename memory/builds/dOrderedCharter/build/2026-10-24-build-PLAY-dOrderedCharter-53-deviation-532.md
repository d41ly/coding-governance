# PLAY-dOrderedCharter-53 deviation 532 — F2's choice relaxes a bound, recorded so the departures report joins it

**Serves:** deviation PLAY-dOrderedCharter-53

- **Departs from:** dOrderedCharter [fork F2 of PLAY-dOrderedCharter-53]
- **Hand-off:** design-to-spec
- **Before:** unit 26 S3 reds every file:line reference the check finds in live text
- **After:** a reference whose line the commit blame names was written by a commit outside the check's landing `L`'s descendants is grandfathered, print-only, so a reference only new text wrote is the one that reds
- **Cause:** review finding
- **Reason:** F2: the file's adding commit, unit 47's rule, is the round-2 finding itself, since an old file gains new references; write-once folders leave specs ungraded. Blame per line is the only option that grades exactly the text written after the check, and it relaxes S3's red for older lines.
- **Evidence:** the §8 mark of F2 in `memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-53.md`; the fork rungs, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:900-946`
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit PLAY-dOrderedCharter-53
- **Caused-by:** PLAY-dClosedLoop-2
- **Bound:** unit 26 S3's red, for a reference whose line a commit outside `L`'s descendants wrote
- **Tier:** weakest, a criterion a sibling spec of this build added beyond its clause
