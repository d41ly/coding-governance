# TOOL-dTendedCadence-1 deviation 11 — the Maintain checklist walked inside the cadence's argv until the flow's executor walks a cadence program

**Serves:** deviation TOOL-dTendedCadence-1

- **Departs from:** `cl-dClosedLoop-0442@53466888`
- **Hand-off:** design-to-spec
- **Before:** the Maintain run as its step checklist on the flow's executor, never a recipe-mode playbook
- **After:** the Maintain run as its step checklist, `[[item]]` rows in the flow's item schema, launched and leased by the executor's cadence (`run_cadence_period`) and walked in their `needs` order by `tools/drift-audit/maintain.py` until the flow's executor walks a cadence program keyed by (cadence, period), never a recipe-mode playbook
- **Cause:** design defect
- **Reason:** The flow's executor is the supervisor, which asks the position engine for a build's next item, keyed by slug; no parent spec gives it a key for a cadence period, and `run_cadence_period` runs one argv under the period lease. So the checklist runs on the executor's lease and launch while its item walk sits inside that argv. TOOL-dTendedCadence-1 §8 F2 settled it by the plan's rung 3, the most feature-rich survivor, and files ask TOOL-dTendedCadence-28 so the walk retires into the executor. The rows keep the flow's schema, so nothing about the checklist changes when it does. The clause's text is unchanged and still carried whole.
- **Evidence:** the supervisor asking `position.py <slug>`, `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-6.md` S1; `run_cadence_period` running one argv, `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-13.md` S6; scout A's finding that no seam fits a period-keyed walk, `memory/builds/dTendedCadence/build/2026-11-01-build-TOOL-dTendedCadence-1-reuse-scout-a.md:13`; the fork, `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-1.md` §8 F2; rung 3, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:910`
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dTendedCadence's spec run, under the chain's `author-recorded` value (README rule 5); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0442@53466888
- **Caused-by:** TOOL-dTendedCadence-1
