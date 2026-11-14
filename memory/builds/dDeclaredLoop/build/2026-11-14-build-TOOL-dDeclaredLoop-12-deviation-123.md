# TOOL-dDeclaredLoop-12 deviation 123 — TOOL-dDeclaredLoop-12's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-12

- **Departs from:** `TOOL-dDeclaredLoop-12@rev-4`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-12`'s spec as the revision at `TOOL-dDeclaredLoop-12@rev-4` reads it.
- **After:** the spec at rev-5: the helpers take lexicon-declared names (scan_cycles, derive_needs_order), routes are an inline table per row spelled with the install prefix, the outcome-set rule is shared through derive_outcome_set, the scope derivation runs under its own --scopes verb (F6), the loop kit declares no playbook requires (F7), and a Needs cell that is not one tag becomes an any-one-of entry (F8).
- **Cause:** design defect
- **Reason:** the spec predated the code units 5, 18 and 37 and PLAY-dOrderedCharter-11 landed, so its helper names, its empty-scope wording and its route spelling no longer held at HEAD.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-12-reground-brief.md`, and the rev-5 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-14-prompt-TOOL-dDeclaredLoop-12-reground-brief
