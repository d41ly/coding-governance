# TOOL-dFairHearing-44 deviation 441 — the closing diff review's second batch unit, for finding 5's docstrings

**Serves:** deviation TOOL-dFairHearing-44

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster ends at `TOOL-dFairHearing-40`, CLOSED at order 28, and `TOOL-dFairHearing-43` at order 29, one batch unit whose rev-2 scope carries all eight minors of the closing diff review, finding id 5's docstrings in `tools/memory-tree/gotchas.py` among them.
- **After:** the roster also carries `TOOL-dFairHearing-44`, ordered at 29 beside `TOOL-dFairHearing-43`, its header naming no ask: a second batch unit whose one scope item corrects the `check_gate_token` and `check_ungated` docstrings to state who calls `check_ungated`, the function itself unchanged, while `TOOL-dFairHearing-43` keeps the finding's class record and the index regeneration.
- **Cause:** review finding
- **Reason:** the build method's severity rule batches every MEDIUM and LOW of a diff review into one unit, two only across disjoint write sets. `TOOL-dFairHearing-43` could not stay one unit: its second build pass was refused at dispatch, because its write set declared `memory/gotchas/INDEX.md` together with that index's generator, `tools/memory-tree/gotchas.py`, the one pairing the verb forbids. Only finding id 5 writes the generator, so moving it leaves two disjoint write sets. This is the build run, so the unit is specced and built in this run.
- **Evidence:** the closing diff review, `memory/builds/dFairHearing/reviews/2026-11-04-review-TOOL-dFairHearing-1-40-diff-review.md`; the refused pass, `memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-43-2-builder-return.md`; the rescope add row for `TOOL-dFairHearing-44` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-11-04-spec-TOOL-dFairHearing-44.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the run's promotion stage, under the build's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-44
- **Caused-by:** PLAY-dClosedLoop-2
