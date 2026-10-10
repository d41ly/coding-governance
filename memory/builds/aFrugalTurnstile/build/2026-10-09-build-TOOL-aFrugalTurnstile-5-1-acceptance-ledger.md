# TOOL-aFrugalTurnstile-5 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-5

No merge bar and no self-test suite ran in this pass. AC1 to AC7 and AC12 ran one scratch fixture
script under short temp roots, building scratch repos the way the turnstile suite's `mk_repo` does,
with every run's `GATE_TURNSTILE_DIR` set to a scratch dir and never the host default. Each case ran
the runner at `bef97330` first and then the working runner. At base, AC1 peaked at 2 with no queue
line, AC2 found no beacon in the host dir, AC3 printed no nested line, AC4 ignored the host beacon,
AC5 reaped a live holder as stalled by the waiter's 60 s, AC6 ran the legs and printed `gates GREEN`
with rc 0, AC7 exited 0, and AC12 printed no NOTE: all RED. On the working runner all eight were
GREEN. AC8 evaluated `check_knob_classes` out of the hook suite at HEAD and in the working tree.
AC9 evaluated `print_interrupted_acts` out of the base and working driver. AC10, AC11 and AC13 are
greps, each `0` at base. The new arms 23 to 28 of the turnstile suite also ran as slices, prologue
plus those arms, deleted before the map regenerated; all 23 assertions passed in the end. The first
slice of arm 24 found two arm defects, both fixed: the inner runner inherited the outer bar's
`GATE_LEGS` and nested without end, and the control's inner bar did not queue behind an outer bar
running a 5 s TTL on a loaded host, so the outer now runs 30 and the inner 5. The close still owes every §7 leg:
the whole turnstile suite with arm 3 now covering AC4 in the host dir, the evidence suite, the
canary, the hook suite's H49 arm, and the AC9 arm in `tools/unattended/unattended.test.sh`.

**Evidences:** TOOL-aFrugalTurnstile-5
- AC1 — `another bar holds this host —` — repo 2 printed it naming repo 1's top level, run id and pid while queued, and the occupancy peak was 1.
- AC2 — `ttl` — the beacon under `GATE_TURNSTILE_DIR` held `repo`, `run` and `ttl` equal to repo 1's top level, its run id and 1800, its TTL.
- AC3 — `gate queue: nested under` — the inner runner printed it, its header read `queued_from` `nested` and `queued` 0; with the knob unset it printed `queued at position` and expired after 20 s.
- AC4 — `reaping the beacon of a dead holder` — printed for pid 999999 in the host dir, then `gates GREEN`.
- AC5 — `another bar holds this host` — printed 1.8 s after start under a beacon with `ttl` 600, no `reaping` line, and the beacon outlived the killed waiter; with no `ttl` it reaped as `stalled` with `ttl 60s`.
- AC6 — `--hold -- false` — exited 1 with no `gate-bar-beacon` left; the held command printed `GATE_TURNSTILE_HOLDER` equal to the beacon's `nonce`; `--hold -- true` exited 0 and no run record was written.
- AC7 — `--hold needs a command` — `--hold` alone and `--hold true` each exited 2, printing the usage line.
- AC8 — `check_knob_classes` — over the changed runner it printed nothing; over a copy reading `GATE_TURNSTILE_PLANTED` it named that knob; the HEAD suite named both new knobs `unclassified-or-twice`.
- AC9 — `no interrupted act` — the base driver printed it over a dead-pid ticket in the host queue; the working driver printed `INTERRUPTED — a turnstile ticket names a pid that is not running`.
- AC10 — `1` — `grep -c 'GATE_TURNSTILE_DIR:-$HOME/.gov/gate-turnstile'` printed `1` over the runner and `1` over `tools/unattended/unattended.sh`.
- AC11 — `grep -n 'GATE_TURNSTILE_DIR' tools/run-gates/run-selftests.sh` — showed line 1275, the per-row export on the same line as the row's private `TMPDIR`.
- AC12 — `could not be created, so this bar queues per repository` — printed with `GATE_TURNSTILE_DIR` naming a regular file, and the beacon appeared under the scratch repo's common dir.
- AC13 — `1` — `grep -c '## The turnstile — one bar per host' tools/run-gates/README.md` and `grep -c 'NESTING TRUSTS AN INHERITED NONCE'` over the runner each printed `1`.
