# TOOL-dDeclaredLoop-27 deviation 272 — TOOL-dDeclaredLoop-27's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-27

- **Departs from:** `TOOL-dDeclaredLoop-27@rev-3`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-27`'s spec as the revision at `TOOL-dDeclaredLoop-27@rev-3` reads it.
- **After:** the spec at rev-4: the unit fills the pending kind.scenario row from the pack's plain path, any kind registered with a schema is activatable (F7), activated rows reach a composition through compose --kind --rows - (F8), the transition writer derives the scenario pin (F9, F10), and the factory is a scenario subcommand of factories.py (F11, F12).
- **Cause:** design defect
- **Reason:** the spec predated the pending kind.scenario row, the schema reader that rejects an activatable list, unit 26's derived composition pin and unit 6's factories.py, and the lexicon refused select_scenarios and compose_scenarios.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-27-reground-brief.md`, and the rev-4 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-prompt-TOOL-dDeclaredLoop-27-reground-brief
