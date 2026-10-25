# TOOL-dGroundRules-37 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-37

No merge bar, no gate leg and no self-test suite ran in this pass. The criteria were probed on a
`git clone` of the branch under `%TEMP%/g37` carrying the changed `check_policy.py`, by
`python tools/policy/check_policy.py --fixture budgets-ships-join` there, with each literal staging
applied by a script under the run's scratchpad and the manifest restored after it. Every run also
printed eight `guard-trace` `WRONG tools/<kit>/kit.toml · not under the policy fixtures guard` lines:
the kit descriptors are the close's deviation-78 sweep's, not this unit's. Owed at the close: the
`policy fixtures` leg over the built tree, and the new arm's red-first observation (AC1, AC3, AC4);
at HEAD before this commit the same command prints no `guard line(s) checked` line at all.

**Evidences:** TOOL-dGroundRules-37
- AC1 — `WARM_CACHE` then `PYC_GUARD` — the run printed `policy-fixture: guard-trace · 52 guard line(s) checked`, then `policy-fixture: guard-trace · WRONG guard {prefix}/govkit/__pycache__/govkit.cpython-314.pyc · names no file git tracks`, naming `__pycache__`.
- AC2 — unmodified copy — the run printed `policy-fixture: guard-trace · 51 guard line(s) checked`, the count the manifest's row holds, and no `WRONG guard` line; `121 assertion(s) executed · 8 wrong`, the eight being the kit descriptors above.
- AC3 — `NEW_GUARD` — the run printed `policy-fixture: guard-trace · WRONG guard {prefix}/govkit/probe_new.py · names no file git tracks`, naming `probe_new.py`; after `STAGE_NEW` it printed `52 guard line(s) checked` and no `WRONG guard` line.
- AC4 — `NO_ROW` — the run printed `policy-fixture: guard-trace · WRONG: the manifest holds no policy fixtures row, so no guard line was checked`. An unparsable manifest printed `policy-fixture: guard-trace · WRONG: the manifest did not parse: Expecting property name enclosed in double quotes: line 1 column 2 (char 1), so no guard line was checked`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: WARM_CACHE+PYC_GUARD -> `WRONG guard {prefix}/govkit/__pycache__/govkit.cpython-314.pyc · names no file git tracks`; NEW_GUARD -> `WRONG guard {prefix}/govkit/probe_new.py · names no file git tracks`, after STAGE_NEW `65 guard line(s) checked`, 0 wrong; NO_ROW -> `WRONG: the manifest holds no policy fixtures row, so no guard line was checked` (34 wrong). GREEN `64 guard line(s) checked`, 0 wrong.
