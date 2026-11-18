# TOOL-dDeclaredLoop-57 deviation 573 — TOOL-dDeclaredLoop-57's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-57

- **Departs from:** `TOOL-dDeclaredLoop-57@rev-3`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-57`'s spec as the revision at `TOOL-dDeclaredLoop-57@rev-3` reads it.
- **After:** the spec at rev-4: the rq11b fixture in the govkit selftest claims kickoff-manifest so its arm stays green under the new refusal, section 5 names every receipt the refusal reaches, and §8 F3 is resolved to (a).
- **Cause:** builder discovery
- **Reason:** the builder found that the rq11b fixture claims agent-cap without its kickoff-manifest dependency, which the new refusal would stop before the arm's adopter runs.
- **Evidence:** `memory/builds/dDeclaredLoop/build/2026-11-14-build-TOOL-dDeclaredLoop-57-1-builder-return.md`, and the rev-4 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-14-build-TOOL-dDeclaredLoop-57-1-builder-return
