# PLAY-dOrderedCharter-46 deviation 462 — F3's choice widens a bound, recorded so the departures report joins it

**Serves:** deviation PLAY-dOrderedCharter-46

- **Departs from:** dOrderedCharter [fork F3 of PLAY-dOrderedCharter-46]
- **Hand-off:** design-to-spec
- **Before:** the one renderer reads instruction rows only from the landed revision, `HEAD`, on every verb
- **After:** a render verb also admits a candidate overlay file the caller names, so a write door renders the rows it just wrote before its commit; check verbs still read `HEAD` alone
- **Cause:** review finding
- **Reason:** F3: a write door that renders from `HEAD` leaves its own new rows unrendered until a second command, the defect the round-1 finding names; committing inside the verb takes the commit from the session. The candidate read is the only option that closes it, and it widens what a render verb reads, so the choice carries `widens:`.
- **Evidence:** the §8 mark of F3 in `memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-46.md`; the fork rungs, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:900-946`
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit PLAY-dOrderedCharter-46
- **Caused-by:** PLAY-dClosedLoop-2
- **Surface:** the renderer may read a caller-named overlay file on a render verb
