# TOOL-aMeasuredDrag-12 — acceptance ledger

**Serves:** journal TOOL-aMeasuredDrag-12

No merge bar, no self-test suite and no bar over a fixture ran in this pass. The pass started at
b71a5553c. Each probe below ran from the worktree root in Git Bash as a script under the session
scratchpad: `ac1.sh`, `ac2.sh`, `arms23.sh` (arms 1m2 and 1m3 cut from the suite with `sed`),
`leg1m.sh` (arm 1m's wrapper and `leg.sh` cut from the suite and run with a hand-built memo, no
bar) and `tpl.sh` (the template arm cut from the hook suite, its fixture repository under
`%TEMP%`). The copies were re-synced by one scripted pass, `sync.py` in the same scratchpad, which
replaced the text between the two resolver markers of each file the S3 `git grep` names with the
canonical block. No criterion of this unit is a timing, so no before and after is measured; the
spawn baseline is unit 11's, and on the absolute path this unit spawns nothing it did not.

**Evidences:** TOOL-aMeasuredDrag-12
- AC1 — `C:\abs\py` — `ac1.sh` sourced the spec's `sed -n '/^PY_MM=""/,/^esac/p'` cut of the
  built runner five times with `PY_ID='3.15.0'`: `/abs/py`, `C:/abs/py` and `C:\abs\py` each
  exported a memo whose line 2 is that `PYBIN`; `rel/py` and `py` left `GATE_RESOLVED_PY` unset.
- AC2 — `nosuchpy` — `ac2.sh` ran the spec's command with line 2 `no/such/py` and then `nosuchpy`;
  `cmp` found stdout, stderr and the exit status equal to the run with `GATE_RESOLVED_PY` unset in
  both. With line 2 `/no/such/py` and then `C:/no/such/py` it printed that line, wrote nothing to
  stderr and exited 0, the control that the same memo construction can hit.
- AC3 — `python tools/lib/python_floor.py check` — the `sed -n` marker range of each of the 80 files PINNED at b71a5553c
  the S3 `git grep` names compared with the canonical's by `cmp`: 0 differ.
  `python tools/lib/python_floor.py check` exited 0. The re-sync rewrote 79 files besides the PINNED at b71a5553c
  canonical, each by the same 4 added and 2 removed lines (PINNED at b71a5553c).
- AC4 — `PYBIN` — the spec's `grep -nE` over `tools/run-gates/run-gates.sh` prints four lines, in
  the order unset, `PYBIN`, digest, export; the export is the `case` arm's line, which the
  `^[^#]*export GATE_RESOLVED_PY` alternative still matches.
- AC5 — `FLOOR_ASSERTIONS=456` — `grep -n -B3 '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.test.sh`
  prints it with the ledger line `450 -> 456, TOOL-aMeasuredDrag-12` above it. The arms 1m, 1m2 and
  1m3 hold 6 `n=$((n+1))` lines, all after the `HAVE_TIMEOUT` gate closes (PINNED at b71a5553c).
- AC6 — `grep -n 'absolute' help/python-floor.md` — prints the memo paragraph's line saying the
  runner hands on only an absolute launcher.

**Scratch probes of the new arms (not their RED-first observation, which is the close's):**
- Arms 1m2 and 1m3, cut from the suite and run over the built runner: both green. Over a runner copy
  whose `case` was dropped, 1m2 failed; over one whose export block was moved above the digest, 1m3
  failed.
- Arm 1m's wrapper and `leg.sh`, run with GOV_PYTHON naming the wrapper: a memo matching GOV_PYTHON
  and PATH left the hit counter empty and filled the miss counter; the same memo with those two
  fields swapped filled the hit counter.
- The template arm in `.githooks/pre-commit.test.sh`, cut from the suite: both `ck` lines passed
  against the built hook, and both failed against a hook copy whose `st_template` pattern was
  misspelled.
- The tag arm in `tools/playbook/instructions_edit.py`: parsed only; not run, because running it is
  running the fixture.

**Owed to the close (the main loop, after every unit is terminal):**
- New arm `tools/lib/resolve-python.test.sh` (e2)'s two new memos, covering AC2: RED with the line-2
  group of `_rp_re` restored to `[^\n]+`, GREEN once restored.
- New arm `tools/run-gates/run-gates.test.sh` 1m's hit and miss counters: RED with the GOV_PYTHON
  and PATH fields of the export swapped, or with `PY_MM` replaced by an empty string.
- New arm `tools/run-gates/run-gates.test.sh` 1m2, covering AC1: RED with the `case` dropped.
- New arm `tools/run-gates/run-gates.test.sh` 1m3, covering AC4: RED with the export moved above
  the digest.
- New arm in `tools/playbook/instructions_edit.py` `arm_retired_rows`: RED with the `check_tree`
  default flipped to `tags=False` (the write half) and with `run_check` passing `tags=True` (the
  check half).
- New arm in `.githooks/pre-commit.test.sh`, the template-size leg: RED with the `st_template` case
  pattern misspelled.
- The gates in spec section 7, `FLOOR_ASSERTIONS=456` among them through `run-gates canary`.
  `bash -n` over every edited script and an `ast.parse` of the edited module stand in for none of
  them.
