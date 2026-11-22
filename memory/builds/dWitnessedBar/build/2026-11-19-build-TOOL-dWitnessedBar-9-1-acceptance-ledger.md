# TOOL-dWitnessedBar-9 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-9

This pass ran no merge bar and no gate leg. Every criterion below was checked on node d on 2026-11-20
by probing the unit's own code: `product_tests.py check --fixture`, whose planted repositories sit
under `%TEMP%`, `product_tests.py check` and `leg_factory.py --check`/`--write` on the built tree,
`run_level.py --detect` on gov's tree and over a scratch git repository under `%TEMP%`, `policy.py get`
and `lists --write`, and `python -c` calls into `product_tests.py`. The close owes every leg of
section 7, the `product-test contract (tests.product)` leg, and the RED-first observation of the
section's `New arm:` line.

**Evidences:** TOOL-dWitnessedBar-9
- AC1 — `case none-with-level: red` — `python product_tests.py check --fixture none-with-level` printed
  `case none-with-level: red` with `row 'alpha check' carries level 'unit', and tests.product = none
  admits no product-test row`, then `case none-with-level, level removed: green`; the planted
  `tests.product = "none"` was read by `policy.py get` from the planted repository's `main`.
- AC2 — `declared` — the `declared` case printed `case declared: red` with `runner 'pytest' declares
  level(s) unit, and no row carries a level`, and its render held no `pack` `product-tests` row; `case
  declared, level unit declared: green`; `case declared, level smoke declared: red` with `row 'alpha
  check' carries level 'smoke', outside unit, integration, e2e, performance`.
- AC3 — `leg.pytest.unit` — the `declared-with-runners` case printed `green`, and its rendered manifest
  held `{"name": "pytest unit tests", "tag": "leg.pytest.unit", ..., "argv": ["python3",
  "{prefix}/pytest-parallel-guardrails/run_level.py", "unit"], "pack": "product-tests", "level":
  "unit"}`; `case declared-with-runners, pytest table removed: green` with no adapter row rendered. With
  `derive_adapter_row` patched in process to write another `pack`, the case printed `FAIL case
  declared-with-runners: the render holds no adapter row leg.pytest.unit at level unit` and the
  fixture exited 1. The whole fixture read `7 of 7 cases read as planted`, exit 0, in 7.3 s. On gov's
  tree `check` printed `tests.product = declared-with-runners · read by policy.py get · default ...`,
  `0 product-test legs declared` and `green`; `leg_factory.py --write` added only the contract leg.
- AC4 — `--detect` — over a scratch repository whose tracked `pyproject.toml` declares markers `unit`,
  `e2e` and `smoke`, `python run_level.py --detect` exited 0 printing `unit` and `e2e`; untracked it
  exited 1; with the table broken it exited 2 naming the parse error. On gov's tree it exited 1:
  `run_level: no tracked pyproject.toml declares a marker for any of unit, integration, e2e,
  performance`. `run_level.py smoke` exited 2: no level of the pytest row.
- AC5 — `LEG_KEY_FLOORS` — `grep -n '"level"' run-gates.test.sh` names arm 1a's `level` control row
  (line 961); the criterion's quoted pattern cannot match the space-separated `LEG_KEYS` line, the
  observation unit 51 S14 owns, so `grep -n '^LEG_KEYS=.* level"'` was read instead and names line
  356. `grep -n '"level"' govkit.py` names `LEG_KEY_FLOORS = {..., "level": (1, 54)}` (line 5962);
  `KIT_RUN_GATES_VERSION=1.54`. The canary's arm 1a control pair is the suite's, owed to the close.
- AC6 — `declared-with-runners` — `python policy.py get tests.product` printed `declared-with-runners`;
  `policy.py lists --write` drained `tests.landing-levels, tests.product, tests.without-cadence`, and
  `grep -cE '^tests\.(product|landing-levels|without-cadence)$' unsummarised-keys.txt` printed 0. The
  three rows' `usage` lines pass `policy.check_shape`, read in process.
