# TOOL-dGroundRules-35 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-35

No merge bar, no gate leg and no self-test suite ran in this pass. The criteria were probed on a
`git clone` of the branch under `%TEMP%/d35` carrying the changed `check_policy.py`, by a `python`
script under the run's scratchpad that imports it, sets `TRACE_ROOTS` to the clone's top, installs
`add_source_read` with `sys.addaudithook` as `run_fixture` does, loads `tools/govkit/govkit.py` through
`importlib.util.spec_from_file_location` and `exec_module` as `budgets-ships-join` does, and calls
`check_guard_trace`. Before the change, one `--fixture budgets-ships-join` run on that clone kept
`tools/govkit/__pycache__/govkit.cpython-314.pyc` both cold and warm, and printed eight `WRONG` lines for
kit descriptors (`tools/branch-reconcile/kit.toml` and seven more) that unit 33's deviation 78 leaves to
the close's sweep. Owed at the close: the `--fixture budgets-ships-join` runs AC1 to AC3 name, after
that sweep, and the new arm's red-first observation (AC3).

**Evidences:** TOOL-dGroundRules-35
- AC1 — `COLD_CACHE` — after it, the probe printed `cold: govkit reads kept ['tools/govkit/govkit.py'] · any .pyc kept: False`, then `policy-fixture: guard-trace · 1 source read(s)` and no `WRONG`; driven directly, `govkit.cpython-314.pyc` at mode `'r'` and the temporary `govkit.cpython-314.pyc.2080703160112` at mode None each kept `tools/govkit/govkit.py`. The full `--fixture budgets-ships-join` count line is owed at the close.
- AC2 — `WARM_CACHE` — after it, the probe printed `warm: govkit reads kept ['tools/govkit/govkit.py'] · any .pyc kept: False` and no `guard-trace` `WRONG`; the `cpython-312.opt-1` name kept the same path, and `__pycache__/govkit.pyc`, which `source_from_cache` refuses, was kept as spelled.
- AC3 — `UNGUARD` — with `WARM_CACHE` run and the `{prefix}/govkit/govkit.py` entry taken out of the clone's `policy fixtures` guard, the probe printed `policy-fixture: guard-trace · WRONG tools/govkit/govkit.py · not under the policy fixtures guard` and returned `(2, 1)`; with `tools/gate-legs.json` restored it printed no `WRONG` and returned `(2, 0)`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: WARM_CACHE + UNGUARD -> `guard-trace · WRONG tools/govkit/govkit.py · not under the policy fixtures guard` (1 wrong); UNGUARD reverted, cache warm -> `134 assertion(s) executed · 0 wrong`.
