# TOOL-dWitnessedBar-29 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-29

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon's `--suggest`
excepted. The criteria were observed on node d, 2026-11-20, at base `60f08d3db`, by the size gate and
the policy kit's `budgets.py` run over scratch fixtures, by `routed_commits.py --newest-unit` in this
repository and its own fixture builder over a scratch repository, by slices of the runner's
`scan_leg_warnings`, its inlined resolver and its verdict-write block run over planted work dirs, by
in-process probes of `profile_bar.py`, `load_sets.py` and `render_playbook.py`, and by `grep`,
`bash -n` and `ast.parse` over the edited files. The runner itself was not run: a fixture bar is a
suite's, so the bar half of AC3, AC4 and AC6 is owed to the `New arm:` lines of spec section 7,
`run-gates.test.sh` arm 9e3, `check-template-size.test.sh` arm A6m/A7m and `routed_commits.py
--selftest`'s `dWB29 AC5` pair, written and not run; their runs, their RED-first observations and the
legs of section 7 are owed to the main loop at the close.

**Evidences:** TOOL-dWitnessedBar-29
- AC1 — `TEMPLATE-SIZE WARN`: `bash tools/check-template-size.sh <fixture> "" <highwater>` over a
  12-byte scratch file no census row names, its planted row 5, printed the warning and on the next line
  `gate-warn<TAB>size<TAB><the row's key><TAB>5 -> 12 (+7) over high-water`, exit 0; with the row at 12
  it printed neither. Arm A6m/A7m's logic, run alone over a scratch bump, read the marker's third field
  equal to the record's key.
- AC2 — `gate-warn`: the two census queries of §4 named thirteen files, the table's, and `git grep -c
  'gate-warn'` matched each of them, one to two lines each.
- AC3 — `GATE warn`: the sliced `scan_leg_warnings` over a planted work dir printed one `GATE warn
  sizer  (memory/guides/BUILD-METHOD.md: 1 -> 2 (+1) over high-water; grown by TOOL-aTrimmedWait-19)`
  for `0.rc` 0, none for `0.rc` 1, none for a marker in `0.rerun.out` beside a red `0.rc`, one beside
  `0.heldrun` with `0.rc` 0, and none for `0.heldrun` with `0.rc` 1 and a marker in `0.retry.out` under
  `0.retry.rc` 0; a passing retry copy was read, a `.sample.out` and a mid-line or indented marker were
  not. Arm 9e3's five slice assertions, run alone with the suite's helpers stubbed, all held.
- AC4 — `warned`: the planted breach run through the sliced verdict-write block wrote `verdict GREEN`,
  `warned 1` and `warn.1<TAB>sizer<TAB>size<TAB>memory/x.md<TAB>-`, whose fourth TAB field of the line,
  the value's third grammar position, is the subject: AC4's "value's fourth TAB field" is read as the
  line's, the position S7's grammar puts the subject at.
- AC5 — `--newest-unit`: `python routed_commits.py --newest-unit HEAD memory/guides/BUILD-METHOD.md` in
  `tools/memory-tree/` printed `TOOL-aTrimmedWait-19`, the first specced id among the subjects `git log
  --no-merges HEAD -- memory/guides/BUILD-METHOD.md` lists, and with two arguments printed
  `TOOL-dWitnessedBar-29`, what the base's copy of the file printed. Over a scratch repository from the
  module's own `build_fixture`, the path named `TOOL-tFix-1`, which touched it, and no path `TOOL-tFix-2`,
  the newest, which did not.
- AC6 — `grown by -`: the slice with KITDIR at an empty scratch directory printed the line ending
  `no memory-tree kit to attribute it: no memory-tree kit holding routed_commits.py in this install:
  looked in ...; grown by -)`; a subject that is not a path read `no commit touching it names a specced
  unit; grown by -`, and one outside the tree `the attribution failed: routed-commits REFUSED — ...`.
- AC7 — `grep -nE 'warned|warn\.<k>' tools/run-gates/README.md`: it named both keys, and `grep -n 'gate-warn' tools/run-gates/README.md tools/check-template-size.sh help/size-caps.md`
  named the marker in each file.
- AC8 — `[] True`: the section-6 `python -c` in `tools/run-gates/` printed `[] True`, and
  `parse_verdicts` over `GATE ok    a` and `GATE warn  a  (...)` returned the one leg `ok`.
- AC9 — `'gate-warn\tsize\ta b\tx y'`: the section-6 `python -c` in `tools/policy/` printed it; `budgets.py
  check fx.md=default:10 20` in a scratch repository whose committed policy file set `budgets.enforce =
  "warn"` printed its `BUDGET WARN` line and then `gate-warn<TAB>size<TAB>fx.md<TAB>fx.md · 20 bytes (DERIVED from the builder's probe)
  over 10`, exit 0, and under `refuse` its `BUDGET REFUSE` line alone, exit 1.
