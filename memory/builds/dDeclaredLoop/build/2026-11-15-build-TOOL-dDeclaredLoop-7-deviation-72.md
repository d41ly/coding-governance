# TOOL-dDeclaredLoop-7 deviation 72 — TOOL-dDeclaredLoop-7's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-7

- **Departs from:** `TOOL-dDeclaredLoop-7@rev-3`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-7`'s spec as the revision at `TOOL-dDeclaredLoop-7@rev-3` reads it.
- **After:** the spec at rev-4: the engine reads through read_transitions, read_transition_rows, read_composition and read_acceptance, unit states come from [states], a recorded move is checked by a new check_recorded_move sharing derive_move's from expansion, the undecided ask ranks below act (F4), only items with a reader are witnessed (F5), a parent lands on a recorded or derived landing (F6), and the leg is gov's own exempt_leg.
- **Cause:** design defect
- **Reason:** the spec predated units 13, 15, 3 and 17, which landed the tables, the transition records and the acceptance record its engine reads, so its readers and its states no longer matched the code at HEAD.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-7-reground-brief.md`, and the rev-4 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-prompt-TOOL-dDeclaredLoop-7-reground-brief
