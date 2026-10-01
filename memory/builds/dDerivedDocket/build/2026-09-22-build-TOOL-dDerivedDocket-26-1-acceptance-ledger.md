# TOOL-dDerivedDocket-26 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-26

The merge-bar runner now defers a leg whose own ceiling fired to one serial retry after the pool
drains, counts a pass on it green and `retried`, names the neighbours beside every timeout, prints
`gate queue: acquired <iso-utc> from <state>` and records the pair in the run header, calibrates a
per-clone spawn floor and exits 4 HOST when every failed leg timed out twice while a spawn cost more
than `GATE_HOST_RATIO` times it, and refuses exit 0 without a leg line and a written verdict file.
The pre-push hook reads `verdict GREEN` from the record of the id it pinned after every exit 0. The
drift report gains `legs_retried_after_timeout`. Fork F5 was resolved at spec rev-8 as the
process-group reap, after a read of the existing `timeout` on node `d`.

NO MERGE BAR, NO GATE LEG, NO SUITE AND NO RUN OF THE RUNNER ITSELF happened in this pass, on the
pass's own instruction. What ran instead, from the run's scratch root and never this tree, were
harnesses that LIFT the changed code verbatim out of the runner, the hook and the drift report and
drive it over fixtures, each with its break staged and observed RED:

- `runleg` with the group reap, over a leg leaving a TERM-ignoring spawning grandchild: 6 checks
  green, the worker writing `.sec`, `.rc` and a `timeout` row and the reparented grandchild dead.
  With the reap removed the grandchild stayed alive and `check_residue_gone` named it; with the reap
  rooted at the worker's own `$BASHPID` the worker was SIGKILLed before `.rc` and the grandchild
  survived as well, the two breaks the spec's F5 names.
- the spawn floor's reader, writer and measurement: 15 checks green, including a directory at the
  floor path read unreadable and a directory at its temp path leaving the held line byte-identical;
  with the writer omitted, 7 went RED.
- `report_one`, `chunk_close`, `measure_neighbours` and `run_leg_retry` driven as the reader drives
  them: a contended leg deferred beside 1 neighbour and green on its retry with its chunk `pending`,
  a lone hang beside 0 and FAIL naming the missing calibration, a planted 1 ms floor under a 50 ms
  spawn reading HOST, a self-kill under a 600 s ceiling never deferred: 17 green. With the deferral
  removed 12 went RED, and with a constant neighbour count the lone hang's count went RED.
- the verdict and exit tail over stubbed counts: exits 0, 2 (no leg line), 2 (verdict fault), 4, 4
  over a moved tree, 1 naming the move and the HOST leg, and 3: 12 green. With the three new guards
  removed, 7 went RED.
- real pushes through the changed hook with a stub runner at its default command: 9 green, with the
  record check removed 4 went RED.
- the drift signal over fixture git dirs: 6 green; with a dead population read as live, 2 went RED.
- the run-log suite's own exit lexer and table, lifted, over the changed runner: no unknown,
  miscounted or stale row once the three new exits had theirs.
- after the checklist pass: `scan_group` over a shadowed `ps` with no PGID column returns rc 2, the
  reap reports it could not scan and `check_residue_gone` fails naming why, 5 checks green; and
  every message the new arms pin was found verbatim in the runner or the hook, 19 of 19.

**Evidences:** TOOL-dDerivedDocket-26
- AC1 — `tools/run-gates/run-gates.test.sh` — the `run-gates canary` leg ran it at 364278a8 in
  the post-build bar and exited 0 with `PASS (266 assertions)`, its log carrying no `canary:`
  failure or SKIP line, so the ceiling arms ran. Its AC1 arms pin the contended leg's first
  timeout as `GATE retry  contended` with `beside 1 neighbours`, its retry as
  `(retried after timeout)`, that bar's exit 0 and `retried 1` in its record, and the lone hang's
  `beside 0 neighbours` retry line and exit 1.
- AC2 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — at 364278a8 the
  `run-gates canary` leg exited 0 with `PASS (266 assertions)` and no failure line; its AC2 arms
  pin the deferred leg's chunk closing `---- chunk default: pending` and its retry line reading
  `---- retry: green  (1 retried, 0 failed)`.
- AC3 — `gate queue: acquired` — at 364278a8 the `run-gates canary` leg exited 0 with
  `PASS (266 assertions)` and no failure line; its AC3 arms check that a fixture bar queued behind
  a planted live holder, that the acquire line directly follows the wait line, and that the run
  record's header carries the same instant. The bar itself printed `gate queue: waited 0s` and
  then `gate queue: acquired 2026-09-28T03:43:29Z from held`, and its header's `acquired` row
  holds that same instant.
- AC4 — `GATE_SPAWN_CMD` — at 364278a8 the `run-gates canary` leg exited 0 with
  `PASS (266 assertions)` and no failure line. Its AC4 arms: over a 1 ms floor and a 50 ms seamed
  spawn a double timeout exits 4, reads HOST in its tail, its `gates HOST` line and its record,
  and stamps no full green; with no floor file it ends `GATE FAIL` naming the missing calibration;
  a clone's first bar writes one `<per-spawn-ms><TAB><iso-utc>` line, a cheaper spawn lowers it
  and a dearer one leaves it byte-identical; `GATE_SPAWN_FLOOR` at a directory is announced
  unreadable and reads no HOST; and a temp path staged as a directory leaves the held line
  byte-identical.
- AC5 — `.githooks/pre-push.test.sh` — the `pre-push self-test` leg exited 0 at 364278a8 with
  `pre-push.test: all cases ok`, including this case:
  `VR AC5 an exit 0 with no run record is blocked, naming the missing verdict`. The
  `run-gates canary` leg exited 0 with `PASS (266 assertions)`; its AC5 arms pin a bar under a
  dead-pid beacon printing its `gates GREEN` line and writing a verdict file that reads GREEN.
- AC6 — `GATE_REUSE=1` — at 364278a8 the `run-gates canary` leg exited 0 with
  `PASS (266 assertions)` and no failure line. Its AC6 arms rerun a fixture bar with
  `GATE_REUSE=1`: over an `ok` ledger row the leg is reused, `GATE reuse cached`, and after that
  row is rewritten to `retried` the next bar runs it, `GATE ok    cached`.
- AC7 — `tools/drift-audit/selftest.py` — the `drift-audit selftest` leg exited 0 at 364278a8
  with `all checks passed (315 executed, floor 277)`. Its `legs_retried_after_timeout` block,
  running `drift_report.py --json` over fixture git dirs, printed ok for two run records carrying
  `retried 1` reporting 2, and for a git dir with no run record reporting DEAD rather than 0; that
  arm asserts the signal's `live` is false, not the human report's printed `DEAD PROBE` text.
- AC8 — `tools/run-gates/README.md` — its exit-code table now lists exit 4 HOST beside 0 to 3, a
  paragraph states the precedence 2 REFUSED, 1 RED, 4 HOST, 3 TREE MOVED, 0 GREEN, and a new section
  names the `GATE retry` tail and the `pending` chunk verdict.
- AC9 — `4h-nobound` — at 364278a8 the `run-gates canary` leg exited 0 with
  `PASS (266 assertions)` and no failure or SKIP line, so arms 4h, stubborn, 4h-kill and
  4h-nobound all ran and held: the leg SIGKILLed about 2 s into a 600 s ceiling got no
  `GATE retry` line and ended `GATE FAIL` on its `killed after` tail with no timed-out text; 4h
  and stubborn pin the serial-retry tail; the no-ceiling self-kill reads `(killed after <s>s)`.
- AC10 — `bash tools/run-gates/run-gates.sh` — at 364278a8 the `run-gates canary` leg exited 0
  with `PASS (266 assertions)` and no failure line. Its AC10 arms, over a 1 ms floor and a 50 ms
  seamed spawn: a bar whose only failed leg timed out twice while the tree moved exits 4 and its
  `gates HOST` line names the move; with an assertion failure beside it the bar exits 1 and its
  RED line names the move and `1 HOST: lone`.
- AC11 — `run_leg_reap` — at 364278a8 the `run-gates canary` leg exited 0 with
  `PASS (266 assertions)` and no failure line. Its AC11 arms: the grandchild is dead when the
  serial retry starts; a reap rooted at an exited pid leaves its orphan alive while the same reap
  rooted at a live pid reaches it; and the timed-out worker survives to write its row and its
  seconds, the pool printing `GATE retry  residue` rather than leaving the leg outstanding.
- AC12 — `REFUSED` — at 364278a8 the `run-gates canary` leg exited 0 with
  `PASS (266 assertions)` and no failure line. Its AC12 arms: an empty manifest exits 2 printing
  `gates REFUSED — no leg line was reported`; a green whose verdict file was not written exits 2
  and its refusal names the verdict file; the same bar with its record written exits 0.
- AC13 — `bash skills/session-kickoff/manifest-check.sh` — the `kickoff-manifest ratchet` leg
  exited 0 at 364278a8 and printed no finding. There the §B ceiling line,
  `memory/guides/SESSION-KICKOFF.md:183`, gives a leg outliving its ceiling ONE serial retry and
  says all-HOST exits 4; `git show` reads the same line at `:174` at this unit's commits 58ffc5c1
  and 153d3cb7.
- AC14 — `wc -c < memory/guides/SESSION-KICKOFF.md` — 24171 at each of this unit's three commits
  against 24172 at the parent of the first, 68942eb0: the command-block ceiling line was replaced by
  one of 156 bytes against 157, and each re-stamped `last-audit:` line is the same length as the one
  it replaced.
- AC15 — `.githooks/pre-push.test.sh` — the `pre-push self-test` leg exited 0 at 364278a8 with
  `pre-push.test: all cases ok`, including these two cases:
  `VR AC15 an inherited id naming a planted GREEN record is not honoured` and
  `VR AC15 two pushes pin two different ids, neither the inherited one`.
