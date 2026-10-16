# TOOL-dRedressedBar-25 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-25

This is the build pass of the round-2 closing diff review's profiler batch, report ids 4, 11, 15,
18, 20 and 23, built from spec 25 rev-1. `<w25>` is `7c7950204`, the spec-writer pass that corrected
specs 18, 21 and 22. `<p25>` is `e23b49536`, the product commit, and `<p25m>` is `45c6b6911`, the
kickoff-manifest re-stamp at it. `<pre>` is `7c7950204`, the code the build pass started from, whose
`tools/` equals `bc6a4c9f`'s.

The product commit changes the gate profiler and its selftest arms, two fixtures (`orphan.sh`, and
`waitmark.py` new), the run-gates descriptor's literal fixture list and the `measure-legs selftest`
row's guard, and re-stamps the kickoff manifest at its parent. `memory/map/generated/symbols.json`
came from `gen_map.py --write`, run alone, and the build README's rows and `memory/LIVE.md` from
`gen_build_index.py --write` over spec 25's dispatched INPROGRESS header, committed with them. The
pre-commit hook's staged legs, memory hygiene and the manifest ratchet among them, passed both
commits.

No merge bar, gate leg or self-test suite was run by this pass, and no arm of
`measure_legs.py --selftest` was called: the moved arms were compiled and read, never executed, so
the close's `measure-legs selftest` run is their first execution. The naming lexicon answered OK for
the five new functions as `py.function`.

Every criterion was observed by a direct probe written apart from the arms, on node d under Python
3.12.10, where PYBIN is the `python3` App Execution Alias, substituted by
`pythoncore-3.14-64/python.exe`, and MSYS bash 5.3.9. Each probe imported `measure_legs` from the
worktree. `<old>` is `git show 7c7950204:tools/gate-legs.json`, written under the session
scratchpad, as are every `--out`, `TMPDIR` and temp manifest.

**Evidences:** TOOL-dRedressedBar-25
- AC15 — `derive_verdictless_tree(` — `read_blind_ab_arms` over the parse of `measure_legs.py`
  returned found `test_serial_run`, `test_resolution_disabled` and `test_fork_count`, and an empty
  blind list. `derive_verdictless_tree` over each returned a count of 1 and a tree over which
  `read_blind_ab_arms` named that function blind; `test_fork_count`'s staged condition unparsed to
  `rc == 0 and len(rows) == 2 and (diff >= 10)`. `inspect.getsource` of
  `test_ab_arms_read_verdicts` carries `derive_verdictless_tree(`. `check_verdict_read` read False
  for a bare constant `"verdict"` and True for `x["verdict"]` and `x.get("verdict")`. Red: the
  rule as at `<p25>~1`, every constant value and attribute name, named neither the copy of
  `test_serial_run` nor that of `test_fork_count` blind, because each failure message still reads
  the verdict, and a walk of every `check_arm` argument, detail included, named neither blind
  either.
- AC4 — `check_guard_trips` — the `measure-legs selftest` row's `guard` in `tools/gate-legs.json`
  equals S4's six entries in order. With `check_guard_trips` loaded from
  `tools/check-spec-tokens.py` and `{prefix}` read as `tools`, all 52 probe paths tripped an entry:
  `tools/run-gates/README.md`, `kit.toml`, `run-gates.sh`, the 44 paths `git ls-files` lists under
  `tools/run-gates/`, `.githooks/pre-push`, the three process-monitor files and
  `tools/gate-legs.json`. The `last-audit:` line of `memory/guides/SESSION-KICKOFF.md` names
  `e23b49536`, whose row's guard opens `{prefix}/run-gates/`, `{prefix}/gate-legs.json`, and
  `git log -1 --format=%B 45c6b6911` carries one `manifest-audit:` line. Red: over `<old>`,
  `tools/run-gates/README.md` and `tools/gate-legs.json` each tripped no entry.
- AC20 — `new_writer.py` — `tools/run-gates/new_writer.py`, which no file holds, tripped
  `{prefix}/run-gates/` in the live row, and `read_guard_misses` over it returned an empty list.
  Red: over `<old>` it tripped no entry, and `read_guard_misses` with `legs_path` set to `<old>`
  returned it, beside `<old>`'s own path, which lies outside the tree.
- AC23 — `read_guard_misses` — over the README path `test_signal_docs` opens it returned an empty
  list, and with `legs_path` set to `<old>` it returned `tools/run-gates/README.md` and `<old>`'s
  own path. Over a copy of the live manifest whose row also carries `{prefix}/run-gates/*.py` it
  returned that entry. Over a copy holding no row that runs `measure_legs.py --selftest` it returned
  one string, opening `0 rows of` and closing `where exactly one must`; an absent manifest and a row
  with its guard deleted each returned one string naming the cause. Over the 13 `*.py` the arm's walk finds it returned an empty list. `inspect.getsource` of
  `test_signal_docs` and of `test_write_atomic_temp` each carry `read_guard_misses(`, and that of
  `run_profile` carries `derive_kit_rel(`. `derive_kit_rel` over the top level returned
  `tools/run-gates`, the value of the three lines it replaced. Red: as at `<p25>~1` neither arm
  read a guard, so the README trips no entry of the row and a README-only commit skips the arm.
  The criterion's run of `test_signal_docs` itself, with `read_guard_misses` rebound to a partial
  over `<old>`, is an arm call, owed to the close below.
- AC18 — `waitmark.py` — `measure_legs.main` with `--serial`, a temp `--legs` manifest of
  `bash orphan.sh 7 <mark>` named `orphan` and `python3 waitmark.py <mark> 30` named `hold`, and
  the selftest's flags returned 0 in 10.8 s. `orphan`'s `<i>.log` read `early` and `late`, its
  `log_bytes` 11, `raw_kept` was empty and `hold` read verdict `ok` at 7.1 s.
  `inspect.getsource(measure_legs.test_legs_table)` carries `WAITMARK_PY`, which reads
  `{prefix}/run-gates/fixtures/measure-legs/waitmark.py`. The `project-owned` list in
  `tools/run-gates/kit.toml` names `fixtures/measure-legs/waitmark.py`, and the set compare
  `test_fixtures_withheld` makes, rebuilt in the probe, read equal over 15 fixtures. Red: the
  manifest as at `<p25>~1` with the orphan's sleep at 7 s, `orphan.sh 7` then `spawn.py 0 5`,
  returned 0 in 8.8 s with the orphan's log `early` alone, `log_bytes` 6, and `raw_kept` naming
  `orphan`, held by a process still running, WinError 32.
- AC24 — `hands-off` — `git diff 7c7950204~1 7c7950204` under the spec dir shows specs 18, 21 and
  22, each CLOSED at `<w25>~1`, with one header rev change, one new revision line naming
  `TOOL-dRedressedBar-25` and its ids, 4, 11, 20 and 23 for 18 and 21, and 15, 18, 4, 11 and 23 for
  22, and a §3 bullet `hands-off` `TOOL-dRedressedBar-25`. Spec 18's "The selftest and its leg",
  cut and joined, and spec 21's AC12 bullet each carry `{prefix}/run-gates/`; spec 22's AC15 bullet
  carries `check_arm` and its AC9 bullet `waitmark.py`. `git diff --name-only` over `<p25>` under
  `memory/builds/dRedressedBar/spec/` names this spec alone, for its dispatched header, and over
  `<p25m>` names nothing. This ledger carries `**Serves:** journal TOOL-dRedressedBar-25`.

## Owed to the close

The section 7 gates, run once by the main loop as the bar, `measure-legs selftest` among them,
whose run is the first execution of the four moved arms and of AC23's own clause, `test_signal_docs`
adding one name to `ARM_FAILED` under a partial over `<old>`. And the RED-first observation of the
four `New arm:` lines: `test_ab_arms_read_verdicts` with `read_blind_ab_arms` walking every
`check_arm` argument (AC15), `test_signal_docs` under the guard as at `<p25>~1` (AC4, AC23),
`test_write_atomic_temp` under that guard with an untracked `new_writer.py` (AC20), and
`test_legs_table` with `orphan.sh` creating its mark before its sleep (AC18). The guard as at
`<p25>~1` carries no `{prefix}/gate-legs.json`, so under it `read_guard_misses` also names the
manifest's own path: those two arms red on that path as well as on the README or `new_writer.py`,
and the detail each prints names both.
