# PLAY-dOrderedCharter-47 deviation 472 — F2's choice relaxes a bound, recorded so the departures report joins it

**Serves:** deviation PLAY-dOrderedCharter-47

- **Departs from:** dOrderedCharter [fork F2 of PLAY-dOrderedCharter-47]
- **Hand-off:** design-to-spec
- **Before:** unit 26 S3 reds every positional citation the check finds, in any record
- **After:** a build record whose adding commit does not descend from the commit that landed the check is graded print-only, so records written before the check stay readable without a rewrite
- **Cause:** review finding
- **Reason:** F2: grading every record red rewrites history the check never governed; print-only for all of `memory/builds/` stops grading new records; a date trusts a clock. Ancestry against the landing commit keeps every new record graded and relaxes the red only for records that predate it.
- **Evidence:** the §8 mark of F2 in `memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-47.md`; the fork rungs, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:900-946`
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit PLAY-dOrderedCharter-47
- **Caused-by:** PLAY-dClosedLoop-2
- **Bound:** unit 26 S3's red, for a build record whose adding commit does not descend from the check's landing
- **Tier:** weakest, a criterion a sibling spec of this build added beyond its clause
