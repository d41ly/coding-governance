# TOOL-dFairHearing-50 deviation 501 — the close's first suite baseline and bar promoted one batch unit for their reds

**Serves:** deviation TOOL-dFairHearing-50

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster ends at `TOOL-dFairHearing-48`, CLOSED at order 32.
- **After:** the roster also carries `TOOL-dFairHearing-50`, ordered at 33 after it, its header naming no ask: one batch unit carrying the reds of the baseline at `948e4141b` and the bar at `57b1cf127`, and the two leftovers unit 48's write gate refused.
- **Cause:** builder discovery
- **Reason:** no pass may run a suite, so the close's baseline was the first run of these arms, and six of twelve suites read red. The bar added three legs in the same files. The fixes share the suites and the kit, so they stay one unit.
- **Evidence:** the rescope add row for `TOOL-dFairHearing-50` in `memory/builds/dFairHearing/RUN.md`; the unit's brief, `memory/builds/dFairHearing/prompts/2026-11-05-prompt-TOOL-dFairHearing-50-spec-brief.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-11-05-spec-TOOL-dFairHearing-50.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the run's promotion stage, under the build's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-50
- **Caused-by:** PLAY-dClosedLoop-2
