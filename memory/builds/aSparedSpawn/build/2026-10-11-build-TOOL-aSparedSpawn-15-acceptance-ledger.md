# Acceptance ledger — TOOL-aSparedSpawn-15

**Serves:** journal TOOL-aSparedSpawn-15

Node `a`, 2026-10-11, bash 5.3 under MSYS, node 22, Python 3.14, beside other sessions' bars, so
"quiet" below means no load this pass added. The pass ran no bar, no suite, no held leg and no slice
of a suite. Every observation drove the changed construct over a hand-built fixture through the
instrument committed beside this ledger, `2026-10-11-build-TOOL-aSparedSpawn-15-direct-checks.sh`,
one step per criterion; "12 fork loops" is its twelve background `/usr/bin/true` loops. `bash -n`
passed on the seven changed shell files and the instrument, `py_compile` on the govkit selftest.
Every criterion whose witness is a suite arm is owed at VERIFYING and says so.

**Evidences:** TOOL-aSparedSpawn-15
- AC1 — `direct-checks.sh ac1` — shipped hook: one line 630 ms against 838 ms one per line quiet,
  1580 ms against 1170 ms under 12 fork loops, both within 4x plus 2000 ms, both runs exit 0. With
  the per-quote prefix copy restored in a scratch copy: 22264 ms against 662 ms quiet and 23517 ms
  against 1993 ms loaded, red on the ratio both times. The arm's old `f(a1, 'lit1')` payload never
  reached the walk (3.3 s against 1.9 s with the copy restored, under the ratio), which spec rev-2
  records; the payload now puts `void` before every literal. The suite arm itself is OWED at
  VERIFYING.
- AC2 — `run-gates.turnstile.test.sh` — OWED at VERIFYING: its expired-wait arm under twelve fork
  loops did not run in the pass. Read in the diff: the refresher writes
  `$EPOCHSECONDS`, so its loop spawns only the `sleep`.
- AC3 — `direct-checks.sh ac3` — the R6 arm's measurement over the shipped `ts_tick_start`: one tick
  2013 ms quiet (TTL 7 s) and 3014 ms under 12 fork loops (TTL 10 s); with `cat` and `date` put back
  in a scratch copy of the runner, 2640 ms quiet and 6235 ms loaded, so the printed period rises; over
  a file with no ticker it printed "no measured period", the arm's FAIL branch. Whether a live holder
  longer than the derived TTL is reaped under twelve fork loops is the R6 arm itself, OWED at
  VERIFYING.
- AC4 — `run-gates.evidence.test.sh` — OWED at VERIFYING: its moved-tree arm in the normal order and
  with the header write delayed past the run's end did not run in the pass. Read in the diff: the mover moves only once
  the header exists, writes `no` when the run's end marker appears first, and that reds naming "the
  mover never saw the header" before any verdict is read.
- AC5 — `direct-checks.sh ac5` — against the shipped `run_bounded`: the child returned rc 124 with its
  marker absent, the grandchild's marker was absent at the return, and the kills afterwards wrote no
  marker; the control's marker was PRESENT when its substitution returned. With a bound that captures
  through a command substitution, the grandchild's marker was PRESENT at the return (the arm's red)
  after 72 s. The suite arms are OWED at VERIFYING.
- AC6 — `direct-checks.sh ac6` — `read_task_gone`, extracted from the suite with `derive_winpid`: a
  sleep killed by `taskkill` read 1 after 1 s; a sleep nobody killed read 0 after 121 s and printed
  "was still listed at the 120 s hang bound". The AC4 and AC13 arms of `resume-tick.test.sh` are OWED
  at VERIFYING.
- AC7 — `govkit/selftest.py` — OWED at VERIFYING, whole and under twelve fork loops (spec rev-2: a
  pass runs no slice). The lock wait's deadline is 120 s and its loop still ends on
  the lock or the first run's exit.
- AC8 — `direct-checks.sh ac8` — the S4 command, `timeout 120` with stdin a fifo held open, over a
  scratch repository: the shipped checker exited 0 after 6 s with one path line; a copy whose
  `read_session_id` reads stdin although `--session` answered exited 124 after 120 s with none. The
  suite arm is OWED at VERIFYING.

Checked as well, none of them a bar leg over a suite: `sh_hygiene.py --spawn-idioms` over the leg's
own pathspecs measured 19 `cat-file` sites in `run-gates.sh` where the registry said 20, the row now
says 19 and the scan matches; `sh_hygiene.py` over the substitution-fed loop registry and
`--location-probes` exited 0; `lexicon.py` exited 0 at 1063 verb offenders, where the first draft's
three stand-in functions in the turnstile suite had made it 1066 (spec rev-3); `check-spec-tokens.py`
reported nothing for this spec once §7 named `recall floor`; `gen_map.py --check` exited 0.
`check-arms.py --check` reports six run-gates exit sites, the same six at HEAD before this pass.
S7's budgets and kit version bumps are graded at VERIFYING and by the main loop's bump.
