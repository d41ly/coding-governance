# TOOL-dDeclaredLoop-58 deviation 582 — TOOL-dDeclaredLoop-58's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-58

- **Departs from:** `TOOL-dDeclaredLoop-58@rev-1`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-58`'s spec as the revision at `TOOL-dDeclaredLoop-58@rev-1` reads it.
- **After:** the spec at rev-2: the range unit 38 already settled leaves the scope, and a line predicate checks the CLI's output line by line against the fixture's commits, with §8 F2 and F3 resolved.
- **Cause:** design defect
- **Reason:** the spec predates unit 38's build, which already reads the range this unit planned to correct, and two of its claims about the CLI's exit and fixture were wrong at HEAD.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-58-reground-brief.md`, and the rev-2 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-14-prompt-TOOL-dDeclaredLoop-58-reground-brief
