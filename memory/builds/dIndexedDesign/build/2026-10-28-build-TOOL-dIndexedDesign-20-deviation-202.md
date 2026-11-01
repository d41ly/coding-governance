# TOOL-dIndexedDesign-20 deviation 202 — the spec stage split a clause and added a unit to carry its second part

**Serves:** deviation TOOL-dIndexedDesign-20

- **Departs from:** dIndexedDesign [roster]
- **Hand-off:** design-to-spec
- **Before:** dIndexedDesign's roster carries sixteen units, `TOOL-dIndexedDesign-1` to `TOOL-dIndexedDesign-16`, one per clause of its row, beside `TOOL-dIndexedDesign-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dIndexedDesign-20`.
- **Cause:** spec split
- **Reason:** BUILD-METHOD M2's one-mechanism test failed for `TOOL-dIndexedDesign-8`, so its writer carried `cl-dClosedLoop-0390` in parts and this unit carries part 2/2: TOOL-dIndexedDesign-8's writer split cl-dClosedLoop-0390 by M2's one-mechanism test: unit 8 carries part 1/2 (design.decompose, feature designs, forks); this unit carries part 2/2 (design.reentry, the additive-versus-breaking diff, design.input and the re-design inventory). This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it.
- **Evidence:** the rescope add row for `TOOL-dIndexedDesign-20` in `memory/builds/dIndexedDesign/RUN.md`; the spec stage's returns, `memory/builds/dIndexedDesign/build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md`; the unit's spec, `memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-20.md`.
- **Risk:** additive
- **Approver:** author, the run's main loop, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dIndexedDesign-20
- **Caused-by:** PLAY-dClosedLoop-2
