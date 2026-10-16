# TOOL-dRedressedBar-21 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-21

This is the build pass of the round-1 closing diff review's one high, H1, with the owner's ruling
that folded in the run's own capture, built from spec 21 rev-2. `<w21>` is `e41b65e47`, the
spec-writer pass that gave specs 18 and 19 their mirrors. `<p21>` is `dc732dba3`, the product
commit. `<p21m>` is `361003ae2`, the manifest re-stamp. `<pre>` is `e114f1356`, whose `tools/`
equals `bf42c5113`'s.

The product commit changes the gate profiler and its selftest, `held_halves.write_held_stamp` and
the new `held_halves.write_replace`, the `measure-legs selftest` guard in `tools/gate-legs.json`
and the help page. `memory/map/generated/symbols.json` came from `gen_map.py --write`, run alone,
and the build README's rows and `memory/LIVE.md` from `gen_build_index.py --write` over spec 21's
dispatched INPROGRESS header, committed with them. The kickoff ratchet's staged check requires a
re-stamp on a commit that stages `tools/gate-legs.json`, so `<p21>` holds one at its parent and
`<p21m>` re-stamps at `<p21>`, advancing `last-body-change` after a section B re-read.

No merge bar, no gate leg and no self-test suite was run by this pass, and no arm of
`measure_legs.py --selftest` or `held_halves.py --selftest` was called: the three new arms and the
widened `test_scratch_sweep` were compiled, read and lexicon-checked, never executed, so the close's
`measure-legs selftest` run is their first execution. The naming lexicon ran, as this role may run
it, and read OK with 1087 offenders against its pin of 1087. The pre-commit hook's staged legs,
memory hygiene and the kickoff ratchet among them, passed both commits.

Every criterion was observed by a direct probe, written independently of the arms: an in-process
python call of the changed functions, or `measure_legs.main` over a one-leg `spawn.py` manifest with
`TMPDIR` pointed at the session scratchpad. Each probe ran on node d under Python 3.12, where
PYBIN is an App Execution Alias and the runs read `SUBSTITUTED`, and where this process can make a
file symlink, so no symlink plant was UNEXERCISED. A red half "over `<pre>`" ran the same probe
against `tools/run-gates/` and `tools/process-monitor/` exported from `<pre>` by `git archive` into
the scratchpad. The red halves a criterion states as a copy of the new code with one compare taken
out are the staged breaks of the four `New arm:` lines, and are owed to the close with them.

**Evidences:** TOOL-dRedressedBar-21
- AC1 — `owner.json` — a dead owner (an exited child, its own pid and creation time) planted
  `gate-profile.dead0000` naming `record` as `<t>/elsewhere`, with a credential in its capture.
  After the profile, `<t>/elsewhere` held no file, the log under the run's own
  `recovered/gate-profile.dead0000/0.log.recovered` carried `://***:***@`, its `raw_recovered`
  entry named that log, and the run's own `owner.json` held the keys `created` and `pid` alone.
  Red over `<pre>`: `<t>/elsewhere/0.log.recovered` existed and the run's `owner.json` carried `record`.
- AC2 — `SECRET-TOKEN` — in the same run, `hln0000` (a hard link to the secret), `sym0000` (a file
  symlink to it), `jnr0000` (a junctioned `raw/`) and `jnd0000` (a junctioned scratch dir) were
  planted. `SECRET-TOKEN` occurred in no file under `<o>` or `<t>/elsewhere`, the secret and both
  outside captures still read their bytes, and the hard link and the symlink still existed. The
  hln and sym captures and jnr's `raw/` each had a `raw_recovered` entry with no log and a `kept`
  opening `not read: `, no entry named `jnd0000`, and the plain dead capture was recovered and gone.
  Red over `<pre>`: `SECRET-TOKEN` landed in `<t>/elsewhere/0.log.recovered`, `outside-raw/0.out` and
  `outside-scratch/raw/0.out` were deleted, every plant had a log, and an entry named `jnd0000`.
- AC3 — `check_pinned_handle` — `read_scratch_file` over a plain `gate-profile.pin0001/raw/0.out`
  returned `b'PLAIN'`. Over `gate-profile.pin0000/raw`, a junction to a dir holding `SECRET`, it
  raised from its `lstat` check (tag `0xa0000003`), and with `os.lstat` rebound to `os.stat` it
  raised `OSError` whose message named the junction target's final path, `pin-target\0.out`. The
  red half, a copy without the final-path compare, is owed with the `test_scratch_read_pin` arm.
- AC4 — `measure_legs.derive_redacted` — rebound to a wrapper that renamed a `tempfile.mkstemp`
  file holding `swapped` over the capture, `write_recovered_logs` over `gate-profile.swp0000`
  returned one entry with a log carrying `://***:***@` and a `kept` opening `not deleted: `, and
  `raw/0.out` read `swapped`. The red half is owed with the `test_scratch_read_pin` arm.
- AC5 — `outside-bytes` — with `x.json.tmp` hard-linked to `outside.txt`, `write_atomic` returned
  True, `outside.txt` and `x.json.tmp` read `outside-bytes`, `x.json` read `new`, and the dir held
  exactly those two. A dangling `y.json.tmp` symlink left `made-by-link` absent. `write_atomic` onto
  a directory returned False and left no `sub.*.tmp`. `write_held_stamp` over a hard-linked
  `held-green.tmp` returned its path, `held-green` read `sha\tx\n`, `outside.txt` kept its bytes, and
  the dir held exactly `held-green` and `held-green.tmp`; over `gd2` it raised `PermissionError` and
  left no `held-green.*.tmp`. Red over `<pre>`: `outside.txt` read `new`, then `sha\tx\n`, and
  `made-by-link` existed; `<pre>` also left `sub.tmp` and `held-green.tmp` behind on failure.
- AC6 — `write_replace` — an `ast` walk of the 12 `*.py` files under `tools/run-gates/` outside
  `__pycache__` found 2 rename calls, `held_halves.py` in `write_replace` and `measure_legs.py` in
  the selftest's nested `write_swapped_capture`. Each sits in a function that calls
  `tempfile.mkstemp` with `dir` and calls neither `os.open` nor `open`. Red over `<pre>`: the set
  was the two calls in `write_held_stamp` and `write_atomic`, each with no `mkstemp` and an open by name.
- AC7 — `LaunchFailed` — its docstring carries `capture: <reason>`, `ast.get_docstring` of
  `measure_legs.py` carries `TOOL-dRedressedBar-21`, `grep -c "in that run's record dir"` over
  the help page printed 0, and its "What it writes" section carries `recovered/<scratch name>/`,
  `left in place` and `capture: `. Red at `<pre>`: the same grep printed 1.
- AC8 — `TOOL-dRedressedBar-21` — `git diff` over `<w21>` shows specs 18 (rev-5 to rev-6) and 19
  (rev-6 to rev-7), each CLOSED on both sides with one new revision line naming
  `TOOL-dRedressedBar-21` and H1. Spec 18's §3 hands-off to unit 21 names `build_capture_file`,
  spec 19's carries the hands-off too, and spec 19 at `<w21>` holds no `<record>/<i>.log.recovered`.
  `git diff --name-only` over `<p21>` names this spec alone, for its dispatched header, and over
  `<p21m>` names none. This ledger carries `**Serves:** journal TOOL-dRedressedBar-21`.
- AC9 — `measure_legs.build_scratch` — rebound to plant a hard link to the secret at the scratch's
  `raw/0.out`, `measure_legs.main` returned 0, the leg's `0.json` read `fail`, rc 1 and a
  `launch_error` opening `capture: `, the secret still read `SECRET-TOKEN=abc123`, the link still
  existed, and `raw_kept` named that path with a reason opening `unreadable: `. In-process,
  `build_capture_file` over a dangling symlink at `1.out` raised and left `made-by-capture` absent,
  `3.out` returned a descriptor whose `fstat` named the identity returned, and over a junctioned
  `cjn0000/raw` with `os.lstat` rebound it raised naming `cap-target\2.out`. Red over `<pre>`: the
  leg read `ok`, the secret was truncated to the leg's empty output, and the link was deleted. The
  two copy red halves are owed with the `test_capture_pin` arm.
- AC10 — `capture_id` — with a hard link to the secret at the capture's name,
  `write_leg_capture(lg, True)` returned a reason opening `unreadable: ` naming 2 names, wrote no
  log, and left the secret and the link. Over a planted plain file it returned `unreadable: ` and
  wrote no log. With no `capture_id` it returned `unreadable: this run made no capture at` and the
  path. A capture this run made and left alone returned None, its log masked and the capture gone.
  Red over `<pre>`: the hard-link plant wrote a log carrying `SECRET-TOKEN` and removed the link.
- AC11 — `_winapi.CreateJunction` — with `derive_redacted` rebound to remove `raw/` and junction it
  to `<t>/victim`, `write_leg_capture(lg, True)` returned `not deleted: ` (the `lstat` check), its log
  carried `://***:***@`, and `victim/0.out` read `victim`. With `os.lstat` also rebound past that
  check, it returned `not deleted: ` from the identity compare and `victim/0.out` still read
  `victim`. Red over `<pre>`: the same staging deleted `victim/0.out` through the junction. The copy
  red half is owed with the `test_capture_pin` arm.
- AC12 — `manifest-audit:` — with `{prefix}` read as `tools`, all 12 `*.py` under
  `tools/run-gates/` lie under the `measure-legs selftest` guard, which names both new exact files.
  `last-audit:` names `dc732dba3`, whose `tools/gate-legs.json` holds both, and
  `git log -1 --format=%B 361003ae2` carries `manifest-audit:`. Red at `bf42c5113`: `check-receipt.py`
  and `regen.py` were outside that guard.

## Owed to the close

The section 7 gates, run once by the main loop as the bar: `measure-legs selftest`,
`held-halves selftest`, `recall floor`, `recall floor arms`, `run-gates canary`,
`run-gates gov canary`, `kickoff-manifest ratchet`, `memory hygiene`, `spec tokens`,
`encoding posture`, `codebase-map coverage + freshness`, `codebase-map gate coverage`, `kit epoch`,
`kit version markers`, `install-prefix` and `testsuite counts`. And the RED-first observation of
the four `New arm:` lines: `test_scratch_sweep` (AC1, AC2), `test_scratch_read_pin` (AC3, AC4),
`test_write_atomic_temp` (AC5, AC6) and `test_capture_pin` (AC9, AC10, AC11).
