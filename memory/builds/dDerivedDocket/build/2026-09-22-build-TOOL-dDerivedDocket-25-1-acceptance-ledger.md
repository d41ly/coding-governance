# TOOL-dDerivedDocket-25 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-25

The merge-bar runner now owns its scratch: `WORK` is a named `gate-work.*` dir under the ambient
`TMPDIR` carrying an `owner` record, every leg's `TMPDIR` is exported into it before the first leg
dispatches, each bar sweeps the scratch of this repository's dead bars and prints `TMPDIR entries <n>`
once, a relatively started runner re-execs through its absolute path, and a bar over a moved tree with
no failed leg exits 3, `TREE MOVED`, while a failed leg outranks the move and its RED line names it.

NO MERGE BAR, NO GATE LEG, NO `*.test.sh` SUITE AND NO RUN OF THE RUNNER ITSELF happened in this
pass, on the pass's own instruction. What ran instead, from the run's scratch root and never this
tree, were three harnesses that LIFT the changed code verbatim out of the runner and drive it over
fixtures, each with its breaks staged and observed RED:

- the owner writer, the dead-scratch sweep and the ambient count, over a fixture ambient dir holding
  a dead and a CR-ended dead owner of this repository, a live one, a dead one of another repository,
  a malformed pid, an empty owner, a dir with no owner, an unrelated dir, dotfiles, and the run's own
  dir under a dead-looking record: 22 checks green. Three breaks, each RED on exactly its own check:
  the common-dir test removed swept the foreign dir, the liveness test removed swept the live bar's,
  and the self guard removed swept the run's own.
- the re-exec block, lifted into a stub that prints its argv: a relative start came back with an
  absolute `$0` and `/proc/<pid>/cmdline`, the arguments intact, the caller's `$!` equal to the
  exec'd pid, `-x` carried, an absolute start untouched, and a runner fed on stdin left alone. With
  the exec removed, the argv stayed `bash|kit/run-gates/run-gates.sh`, the TOOL-aReapedSpinner-14
  condition, and both argv checks went RED.
- the verdict derivation and the final exit block over stubbed counts: GREEN exits 0; moved and
  green exits 3 with the `gates TREE MOVED — ` line in stdout and in the summary file; moved and red
  exits 1 with `(the tree moved while the bar ran)` on its RED line; a wall breach stays RED. With
  the TREE MOVED assignment removed, the moved bar exited 0 GREEN, the BASE behaviour, and went RED.

AC1 to AC8 each carry a `permission:` line deferring their observation to the build's one post-build
bar, `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, so none gets a line here; the
orchestrator writes each after that run. The owed legs are `run-gates canary` (section 8, arms 8a to
8e, and arm 3a's new presence check), `run-gates turnstile` (arm 22), `run-gates run-log line` (the
AC2 moved-tree bar and its exit-table row), `template size gate selftest`, `kit version markers`,
`kickoff-manifest ratchet` and `memory hygiene`.

**Evidences:** TOOL-dDerivedDocket-25
- AC1 — `tools/run-gates/run-gates.test.sh` — the `run-gates canary` leg ran it at the post-build bar
  at 364278a8 and exited 0 on `PASS (266 assertions)` with no failure line, so arm 8a held: after an
  idle-mover control that exits 0 and stamps, a bar whose leg edits a tracked file mid-run exits 3,
  prints `gates TREE MOVED — `, records `verdict TREE MOVED` and writes no full-green stamp.
- AC2 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — at 364278a8 its canary
  arm 8d held: two fixture bars killed by signal 9 while a leg held `mktemp -d` scratch, under a
  private ambient `TMPDIR`, left a third bar printing the same `TMPDIR entries <n>` as the first and
  announcing that it swept a dead bar's scratch.
- AC3 — `tools/run-gates/run-gates.turnstile.test.sh` — the `run-gates turnstile` leg ran it at the
  same bar and exited 0 on `PASS (74 assertions)`; its arm 22, bars run with `GATE_TURNSTILE=0`,
  printed that a LIVE bar's scratch survived a second bar's sweep, that a dead bar's scratch whose
  owner names another repository survived, and that the first bar's verdict stayed rc 0, GREEN.
- AC4 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — at 364278a8 its canary
  arm 8c held: a fixture leg's `mktemp -d` landed under the run's own `gate-work.*/tmp`, was gone
  once the bar exited 0, and the private ambient `TMPDIR` held nothing afterwards.
- AC5 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — at 364278a8 its canary
  arm 8e held and printed no SKIP line: the `/proc/<pid>/cmdline` of a relatively started runner,
  its pid read from the beacon's `pid` file, carries an absolute path ending in
  `tools/run-gates/run-gates.sh`.
- AC6 — `template size gate selftest` — the leg exited 0 at the post-build bar at 364278a8, a bar run
  with `GATE_FULL=1 GATE_SELFTESTS=1` whose selftests chunk ran 58 legs and held none, printing that
  every arm of `check-template-size.test.sh` held; that bar printed `TMPDIR entries 26270`, the
  line the runner prints just before it exports `TMPDIR` as its own `$WORK/tmp` for every leg.
- AC7 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — at 364278a8 its canary
  arm 8b held: with one fixture leg failing and another editing a tracked file mid-bar, the bar exits
  1, its RED line reads 1/2 legs failed and names the moved tree, and the run record says RED over a
  moved tree rather than `verdict TREE MOVED`.
- AC8 — `kickoff-manifest ratchet` — at 364278a8 the leg exited 0 with no output, so check 5 passes
  against the re-stamped `last-audit`; the §B trap there says every leg's `TMPDIR` is the runner's
  own `gate-work.*/tmp`, gone on exit, and names this unit.
- AC9 — `wc -c < memory/guides/SESSION-KICKOFF.md` — 24172 at this unit's commit against 24184 at
  its parent 5c33fd5a, the four-line trap bullet replaced by one of 353 bytes against 365; and
  `grep -c 'at an empty dir' tools/run-gates/README.md` prints 1, in the README's new scratch section.
- AC10 — `tools/run-gates/run-gates.sh:3` — the runner's exit-code header line now ends
  `2 = must run from the repo · 3 = TREE MOVED.`, beside the exits 0, 1 and 2 it carried at BASE;
  and `tools/run-gates/README.md` carries a new `## Exit codes` section whose table names exit 3 as
  TREE MOVED.
