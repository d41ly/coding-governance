# TOOL-dDeclaredLoop-10 deviation 101 — TOOL-dDeclaredLoop-10's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-10

- **Departs from:** `TOOL-dDeclaredLoop-10@rev-1`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-10`'s spec as the revision at `TOOL-dDeclaredLoop-10@rev-1` reads it.
- **After:** the spec at rev-2: S2, S3 and S5 leave scope as already built, derive_direction takes (state, to, tables) and reads a step-order key read_transition_rows adds, the steps are read in their fixed order (F4), the direction case runs as a selftest case and a probe (F5), the direction table covers every row, and the direction prints on the loop: recorded line.
- **Cause:** design defect
- **Reason:** the spec predated unit 3's transition writer and units 13 and 15's tables, which already treat backward moves like forward ones, so its scope, its signature and its fixtures no longer matched the code at HEAD.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-10-reground-brief.md`, and the rev-2 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-prompt-TOOL-dDeclaredLoop-10-reground-brief
