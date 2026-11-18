# Brief — aTrimmedWait: the `--check-specs` verb's parity row

**Serves:** research TOOL-aTrimmedWait-13

## The prompt

The main loop ran `bash tools/unattended/unattended.test.sh` on a frozen clone of `c50583f10`, after
the reconcile with local main, as TOOL-aTrimmedWait-12's §7 owes. It exited 1 on 24 FAIL lines. One
is this build's own, quoted:

> FAIL parity: the verb --check-specs has no row in the parity table

`TOOL-aTrimmedWait-1` added the `--check-specs` verb to the driver's dispatch, and the suite's
parity arm requires a `PARITY_ROWS` row for every verb `verbs_all` lists. Unit 1's arms ran only
shards 3 and 4, so the parity arm, outside them, was never read. The other 23 rows come from main's
side or were recorded red before this build. The owner ruled on 2026-11-16 to repair this one before
the landing merge and to file the rest.

## The brief

### Goal
Author the spec for TOOL-aTrimmedWait-13, a repair unit after which the driver suite's parity arm
reads `--check-specs` as a row, with no other verdict moved.

### Items
1. One `PARITY_ROWS` row in `tools/unattended/unattended.test.sh` for `--check-specs`, its argv a
   form the verb accepts over the parity fixture's `tRun` build, so the row runs the script and the
   in-process call over the same tree and compares output, exit status and the tree left behind.
2. The floors the row's assertions move (`FLOOR_ASSERTIONS` and the floor of the shard that runs the
   parity arm), each raised by the count the row adds, counted off the loop's own `same` calls, with
   a raise-log line in the form the floors already use.
3. The row's RED-first case is the suite at `c50583f10`, where the parity arm printed the FAIL line
   above; the GREEN is the main loop's at the close.

### Acceptance
- `python tools/check-spec-tokens.py --spec <the new spec>` exits 0.
- `bash tools/unattended/unattended.sh --check-specs aTrimmedWait TOOL-aTrimmedWait-13` prints its
  clean line.

### Gates
The merge bar once at the close, without the self-test suites, run by the main loop; the driver suite
once at the close on a frozen clone, also the main loop's. The pass runs only direct checks.

### Non-goals
- The other 23 FAIL rows: main's `KEEPALIVE_INTERVAL` and `--wake` rows, the parity rows of
  `register-task`, `release-task` and `liveness`, and the rows earlier builds recorded. They are
  filed as asks.
- Any change to `tools/unattended/unattended.sh`.
- ANY SELF-TEST SUITE OR BAR INSIDE THE PASS, A SLICED SUITE INCLUDED.

## Owner confirmation

> Fix it, then land
