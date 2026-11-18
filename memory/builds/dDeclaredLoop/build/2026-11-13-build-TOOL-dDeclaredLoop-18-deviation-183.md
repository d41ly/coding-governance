# TOOL-dDeclaredLoop-18 deviation 183 — TOOL-dDeclaredLoop-18's spec revised after its builder's divergence

**Serves:** deviation TOOL-dDeclaredLoop-18

- **Departs from:** `TOOL-dDeclaredLoop-18@rev-3`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-18`'s spec as the revision at `TOOL-dDeclaredLoop-18@rev-3` reads it.
- **After:** the spec at rev-4: six claims re-grounded on the code at `cb34ba603`, §8 F6 resolved to (a) and F7 to (b).
- **Cause:** builder discovery
- **Reason:** the build run's first dispatch returned before its code because six claims of rev-3 fail against the code dOrderedCharter landed; F6 (a) is the only option that lands green with S5 kept, and F7 (b) calls the one matcher in process.
- **Bound:** the rev-3 Non-goal "a family resolver inside PLAY-dOrderedCharter-19 S7's `resolves` check"
- **Tier:** weakest, a non-goal the spec writer added beyond the unit's clause
- **Evidence:** the builder return `memory/builds/dDeclaredLoop/build/2026-11-13-build-TOOL-dDeclaredLoop-18-1-builder-return.md`, and the rev-4 line in this spec's §9.
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate and the standing ruling ER:328
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-13-build-TOOL-dDeclaredLoop-18-1-builder-return
