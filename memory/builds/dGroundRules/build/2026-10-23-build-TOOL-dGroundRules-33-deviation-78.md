# TOOL-dGroundRules-33 deviation 78 — the build's sweep is the close's first run, not the pass's

**Serves:** deviation TOOL-dGroundRules-33

- **Departs from:** TOOL-dGroundRules-33@rev-6 [§2 S4]
- **Hand-off:** spec-to-code
- **Before:** S4 adds to the `policy fixtures` row, in this unit's commit, every path the first `--fixture` run over the built tree reports in a `guard-trace` `WRONG`.
- **After:** this unit's commit adds S1's `{prefix}/govkit/selftest.py` alone; the first `--fixture` run over the built tree is the close's `policy fixtures` leg, and the paths it reports are added there, after `TOOL-dGroundRules-35`, `-36`, `-37` and `-38` have reshaped what the trace keeps.
- **Cause:** builder discovery
- **Reason:** the run that reports the paths is the `policy fixtures` leg's own argv, which scratch-guard refuses to the gov-builder role (allowlist `lexicon naming predicates`); a hand-typed list of the files the cases read is §4's rejected alternative, so the pass guesses none. The kept set it would report is also not yet final: 35 maps bytecode-cache reads, 36 drops ignored reads, 37 holds additions to tracked files and 38 keeps the git directory out, so a sweep now would add paths those units remove.
- **Evidence:** the scratch-guard refusal of `python tools/policy/check_policy.py --fixture --strict-from memory/builds/dClosedLoop/build/` in this pass; the probe in this unit's acceptance ledger, which drives `add_source_read` and `check_guard_trace` directly.
- **Risk:** loosening
- **Approver:** author, the gov-builder pass of TOOL-dGroundRules-33, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dGroundRules-12
- **Caused-by:** TOOL-dGroundRules-33
