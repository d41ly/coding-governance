# TOOL-dRedressedBar-22 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-22

This is the build pass of the round-1 closing diff review's profiler batch, report ids 2, 3, 6, 9,
10, 11, 14, 15 and 16, built from spec 22 rev-1. `<w22>` is `c744689e3`, the spec-writer pass that
corrected specs 18 and 19. `<p22>` is `b1ea4be92`, the product commit. `<pre>` is `c744689e3`, the
code the build pass started from, which unit 21 left.

The product commit changes the gate profiler and its selftest, two fixtures (`orphan.sh` new,
`memio.py`), the run-gates descriptor's literal fixture list, the README's profiler section and one
sentence of the help page. `memory/map/generated/symbols.json` came from `gen_map.py --write`, run
alone, and the build README's rows and `memory/LIVE.md` from `gen_build_index.py --write` over spec
22's dispatched INPROGRESS header, committed with them. No file the kickoff manifest watches moved.

No merge bar, gate leg or self-test suite was run by this pass, and no arm of
`measure_legs.py --selftest` was called: the six new arms and the five moved ones were compiled,
read and lexicon-checked, never executed, so the close's `measure-legs selftest` run is their first
execution. The naming lexicon answered OK for both new functions, the six new arms and the three
nested wrappers the arms define. The pre-commit hook's staged legs, memory hygiene among them,
passed `<p22>`.

Every criterion was observed by a direct probe written apart from the arms: an in-process python
program that imports `measure_legs`, rebinds what the criterion names, and runs `main` or the
function, with `TMPDIR` and `--out` under the session scratchpad. Each probe ran on node d under
Python 3.12.10, where PYBIN is the `python3` App Execution Alias, substituted by
`pythoncore-3.14-64/python.exe`. A red half "over `<pre>`" ran the same probe against
`tools/run-gates/` and `tools/process-monitor/` exported from `<pre>` by `git archive`, with
`orphan.sh` copied in beside its fixtures. The red halves a criterion states as a staged break of
the new code are the `New arm:` lines' RED-first observations, owed to the close.

**Evidences:** TOOL-dRedressedBar-22
- AC2 — `write_final_capture(` — over `orphan.sh 6` then `spawn.py 0 6`, the wrapped
  `write_leg_capture` noted `orphan` kept with `2 process(es) still running at the root's exit`,
  and the wrapped `scan_root_exits` raised on its next call. `main` returned 130 in 3.1 s, the
  envelope's `exit` read 130, and `raw_kept` held `hold` with `interrupted` and `orphan`, its path
  still on disk, with `interrupted; held by a process still running: [WinError 32] ...`. `0.json`
  existed, the stderr line read `INTERRUPTED — 1 leg(s) left running; 2 raw capture(s) kept, each
  named in raw_kept`, and `run_profile`'s source carries `write_final_capture(` twice. Both kept
  captures unlinked within the probe's 30 s wait. Spec 18's "The record" carries
  `TOOL-dRedressedBar-22`. Red over `<pre>`: `raw_kept` named `hold` alone, the line read `their
  captures kept`, and the orphan's unredacted capture stayed on disk with no name.
- AC3 — `_base_executable` — a venv made by `-m venv --without-pip` from `sys._base_executable`
  took 0.05 s. `measure_job_children` over its `Scripts/python.exe` read (4, 3), a difference of 1,
  and with `JOB_CHILD_PROGRAM` rebound to spawn `sys.executable` read (5, 3), a difference of 2.
  With `GOV_PYTHON` naming the venv python, `main` over `spawn.py 0 0` returned 0, the envelope's
  `pybin` named the venv python and its `interpreter_probe` read 4 and 3. `JOB_CHILD_PROGRAM`
  carries `_base_executable`, as do the three fixture lines carrying `sys.executable`, in
  `churn.py`, `hog.py` and `spawn.py`. Spec 18's "Alias launchers" carries `_base_executable`.
  Red over `<pre>`: the probe read (5, 3) with the shipped program, and the `GOV_PYTHON` run
  returned 2 with a REFUSED line carrying `keeps no child`.
- AC11 — `keeps no child` — with `measure_job_children` rebound to (2, 2), `main` over
  `serial.json` returned 2 with exactly one REFUSED line carrying `keeps no child`, no `Traceback`
  and `--out` empty. With `check_app_alias` also reading True for a `bash` stem, it returned 2 with
  one line naming `C:/Program Files/Git/usr/bin/bash.exe` and `no rule here resolves an alias that
  is not PYBIN`, `--out` empty. `resolve_launcher_aliases` over a launcher whose path names no file
  refused carrying `os.lstat cannot`, and over the base interpreter with `measure_job_children` at
  (2, 1) returned no substitution. `resolve_alias_interpreter` refused `echo` carrying `no plain
  file`, and returned `C:/Users/d41ly/AppData/Local/Programs/Python/Python312/python.exe`, a file,
  for the base interpreter. Spec 18's §5 carries `TOOL-dRedressedBar-22`. Both red halves are
  staged breaks, owed with the `test_alias_refusals` arm.
- AC15 — `memio: wrote 200 MiB` — `measure_legs.py --serial` over `memio.py 1` exited 0 and its
  `0.log` read `memio: wrote 1 MiB`. On node d, with `resolve_launcher_aliases` rebound to
  `([], None)`, `main` over a `serial.json` copy returned 0, `spawn six`, `spawn none` and `memio`
  each read `ok`, memio's log carried `memio: wrote 200 MiB`, the spawn difference read 0, and
  memio's peak was under 200 MiB with `write_bytes` 0. An `ast` walk of the file found three
  `test_*` functions subtracting two `procs_total` reads, `test_serial_run`,
  `test_resolution_disabled` and `test_fork_count`, each reading `verdict`. Spec 18's AC1 carries
  `verdict`. Red: the same alias run over a copy whose memio row names a missing script read memio
  `fail` with no line, while the readings `<pre>`'s arm grades still held, difference 0, peak under
  200 MiB and `write_bytes` 0; and the walk over `<pre>` found the same three functions reading no
  `verdict`. The arm's red is owed with the `New arm:` line.
- AC6 — `if pending and not running` — `check_admit` at §4's eight rows read hold, admit, hold,
  hold, admit, admit, hold and hold. Wrapped to record every call over AC9's manifest, it was called
  17 times and returned True twice, `('serial', 2, 0, None, 73, True)` at a host tick and
  `('serial', 1, 0, None, 73, False)` at the drained site, each with `running` 0. `run_profile`'s
  source carries no `if pending and not running`. Spec 18's AC5 carries `TOOL-dRedressedBar-22`.
  Red over `<pre>`: the recorder saw no call at all for a serial run. The drained-clause break is
  owed with the `test_check_admit` and `test_legs_table` arms.
- AC9 — `rewritten whole` — over `orphan.sh 2` then `spawn.py 0 5`, `main` returned 0 in 9.3 s,
  `legs.tsv` held the `LEGS_COLUMNS` header and two rows, and each row equalled `render_legs_row`
  over its leg's `<i>.json`, column for column. The orphan's log read `early\nlate\n`, its row and
  its `<i>.json` both read `log_bytes` 11, and `raw_kept` was empty. The README's profiler section
  carries `rewritten whole`, and spec 18's record table's `legs.tsv` row carries `run end`. Red over
  `<pre>`: the orphan's row read `log_bytes` 6 where its `<i>.json` read 11.
- AC10 — `len(made) == 3` — with `build_job` rebound to close only the third job it made, `main`
  over `launch` then `after` returned 0 in 4.8 s, having made four jobs. `launch` read `fail`, rc 1,
  `launch: AssignProcessToJobObject 6`, `after` read `ok` with `procs_total` 2, and `legs.tsv` held
  two rows. `test_launch_failure`'s source carries `len(made) == 3`, and spec 19's AC35 carries
  `after`. The red half, `pending.clear()` added to the `LaunchFailed` branch, is owed with the
  `test_launch_failure` arm.
- AC16 — `has run is ever killed` — `nothing is ever signalled` occurs 0 times in the README, whose
  profiler section, joined, carries `terminate`, `suspended` and `launch_error`. The help page holds
  no `Nothing is ever killed` and carries `has run is ever killed`. The module docstring carries
  `terminate` and `launch_error` and no `nothing is ever signalled`. Red over `<pre>`: the README
  held the sentence once and its section no `terminate`.
- AC17 — `hands-off` — over `<w22>`, spec 18 moved rev-6 to rev-7 and spec 19 rev-7 to rev-8, each
  CLOSED on both sides with one new revision line naming `TOOL-dRedressedBar-22`: spec 18's names
  ids 2, 3, 6, 9, 11, 14 and 15, and spec 19's id 10. Each gained one §3 `hands-off`
  `TOOL-dRedressedBar-22` bullet. `git diff --name-only` over `<p22>` names this spec alone, for its
  dispatched header, and this ledger carries `**Serves:** journal TOOL-dRedressedBar-22`.

## Owed to the close

The section 7 gates, run once by the main loop as the bar: `measure-legs selftest`,
`foreign-prefix parity`, `run-gates canary`, `run-gates gov canary`, `govkit selfcheck`,
`kit epoch`, `kit version markers`, `install-prefix`, `python resolver`,
`codebase-map coverage + freshness`, `codebase-map gate coverage`, `lexicon naming predicates`,
`encoding posture`, `spec tokens`, `recall floor`, `recall floor arms` and `memory hygiene`. And the
RED-first observation of the seven `New arm:` lines: `test_interrupt_capture` (AC2),
`test_venv_interpreter` (AC3), `test_alias_refusals` (AC11), `test_resolution_disabled` and
`test_ab_arms_read_verdicts` (AC15), `test_check_admit` and `test_legs_table` (AC6, AC9),
`test_launch_failure` (AC10) and `test_signal_docs` (AC16). The selftest's added cost, estimated at
about 50 s in spec 22 §5, is unmeasured until that run, which re-prices the leg's pinned budget.
