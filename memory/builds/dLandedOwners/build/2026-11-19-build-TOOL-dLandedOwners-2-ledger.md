# TOOL-dLandedOwners-2 — acceptance ledger

**Serves:** journal TOOL-dLandedOwners-2

No merge bar, gate or self-test suite ran in this pass. Each criterion was observed by the spec's own
command, or by a `python -c` probe calling the unit's functions, from the worktree root, with the landed
revision L at `5a311c9f` (the remote-tracking `origin/main` at this pass). Every red was observed either at
the pass's base `7c5b5fa3`, before the first edit, or as a staged break made inside the probe's own
process by replacing a name on the imported module, so no file was edited to observe it. The fixture
repositories were made by the case's own `tempfile.mkdtemp(prefix="pol-")` under `%TEMP%` and removed by
`remove_repo`; the real repository's refs were never written.

**Evidences:** TOOL-dLandedOwners-2
- AC1 — `scan_reader_keys` through the spec's command printed
  `['deps.on-parent-withdrawn', 'flow.adapt', 'flow.on-exhausted', 'flow.rework-budget', 'flow.route-backs', 'flow.scenario-conflict', 'flow.scenario-default', 'flow.wait-ceiling', 'transitions.record']`,
  every key of the inventory. Red: at the base it printed `['flow.route-backs', 'flow.wait-ceiling']`.
  With `READER_SHAPES` cut to its first three rows, the keys the new row adds over the tree, intersected
  with the catalogue, were exactly the seven of the inventory and no other. With the row replaced by the
  consuming `[A-Za-z_][\w.]*\((?P<args>[^()\n]*)`, the scan spelled no `flow.scenario-default` and no
  `flow.scenario-conflict`.
- AC2 — `read_budget_value('.')` printed `(4, 2, 3)`, the tuple it printed at the base in the same tree.
- AC3 — `check_reader_coverage('.', landed={'dDeclaredLoop'})` printed `32`, DERIVED from the
  catalogue's dDeclaredLoop rows, and one finding line, `deviation.approval`, which TOOL-dLandedOwners-3
  owns. Red: at the base it printed eight finding lines, the seven of the inventory and `deviation.approval`.
- AC4 — `run_reader_coverage('reader-coverage')` printed `case reader-constant: green` and
  `case constant-unread: red`, no line carrying `WRONG:`, and returned `(13, 0)` (PINNED, this pass).
  Red: with the new row dropped from `READER_SHAPES`, `case reader-constant: red` printed
  `WRONG: graded 1` naming `fixture.planted`, `(13, 1)` (PINNED, this pass); with `MODULE_CONSTANT`
  recompiled without its `^`, `case constant-unread: green` printed `WRONG: graded 1`, the
  function-local `key` in `local.py` bound, `(13, 1)` (PINNED, this pass). The case's run through
  `check_policy.py --fixture reader-coverage`, with the guard-trace and count lines, is the
  `policy fixtures` leg's and is the main loop's at the close.
- AC5 — `grep -n "resolve(KEY)"` printed `help/policy.md:160` and `tools/policy/README.md:357` and `:507`,
  each stating the module-constant shape, and
  `grep -c "a key passed through a variable reads as unread" tools/policy/README.md` printed `0`.
  Red: at the base the first grep found no line in either file and the count printed `1`.

## New-arm observations (main loop, M8)

Observed at `f3a64d91b` in an LF clone under `%TEMP%/armlo`, through `python tools/policy/check_policy.py --fixture <case>`, one staged break at a time, the file restored byte for byte after each run. Before the breaks and after the restore every fixture below read `0 wrong` at `f3a64d91b`.

- `--fixture reader-coverage` · break: the fourth `READER_SHAPES` row deleted · RED: `case reader-constant` printed WRONG, rc 1 at `f3a64d91b` · GREEN once restored.
- `--fixture reader-coverage` · break: `MODULE_CONSTANT` unanchored from column 0 (`^` removed) · RED: `case constant-unread` printed `WRONG: graded 1`, rc 1 at `f3a64d91b` · GREEN once restored.
