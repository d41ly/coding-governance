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
- AC8 — `tools/run-gates/README.md` — its exit-code table now lists exit 4 HOST beside 0 to 3, a
  paragraph states the precedence 2 REFUSED, 1 RED, 4 HOST, 3 TREE MOVED, 0 GREEN, and a new section
  names the `GATE retry` tail and the `pending` chunk verdict.
- AC14 — `wc -c < memory/guides/SESSION-KICKOFF.md` — 24171 at each of this unit's two commits
  against 24172 at the parent of the first, 68942eb0: the command-block ceiling line was replaced by
  one of 156 bytes against 157, and each re-stamped `last-audit:` line is the same length as the one
  it replaced.
