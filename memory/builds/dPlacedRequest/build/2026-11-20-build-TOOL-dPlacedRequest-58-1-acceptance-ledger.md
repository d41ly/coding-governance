# TOOL-dPlacedRequest-58 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-58

The unit was built from its spec at rev-5 on base `c817c0402`. Built: S2, the absence test after the
clear and before A in the placed race's attempt loop of `tools/unattended/unattended.test.sh`, its
`DPR58 AC1` row placed before the `DPR48 AC3` row, the block's header naming the reset, and the two
floors. S1 is unit 52's clear, observed under AC2. No gate, suite or bar ran in this pass. Every
reading below is a probe of the changed code: the loop and its new row, cut from the suite by `awk`
and run by `bash` over a stub `run_request_arm` that copies its text through the block's own stub
`cp`, a stub driver line for the bound, and a fixture repository under `%TEMP%` for the health-log
path, each removed after.

**Evidences:** TOOL-dPlacedRequest-58
- AC1 — `reset`: the cut as built, B ending inside the bound, kept attempt 1 and the `DPR58 AC1` row read `reset`; `jobs -p` printed nothing. (DERIVED)
- AC1 — `request race state not reset`: a copy of the cut whose loop carries no clear and whose attempt 1 alone sleeps past the bound between `held` and B discarded attempt 1 as a placement overrun and the row failed `request race state not reset at attempt 2`; `jobs -p` printed nothing. (DERIVED)
- AC1 — `reset`: the same overrun copy with the clear kept discarded attempt 1, kept attempt 2, and the row read `reset`. (DERIVED)
- AC1 — `NODE_LOCK_BOUND`: the probe's stub driver line set it to 1 and the staged sleep ran 3 s, standing in for the criterion's 11 s over the driver's own bound. (PINNED)
- AC2 — `for pr_n in 1 2 3; do`: the criterion's `awk` cut of the block, then `grep -A1 -xF` on that line, printed the clear of `$pr_h/once`, `$pr_h/held` and `$pr_h/release` as the next line. (DERIVED)
- AC2 — `$pr_h/once`: the S3 bullet of spec 56 names `$pr_h/once`, `$pr_h/held` and `$pr_h/release` in one sentence, one `grep -c` line. (DERIVED)

## Readings beside the criteria

- `bash -n` read the changed suite clean. (DERIVED)
- The diff mints, renames and deletes no function: the new name is the variable `pr_dirty`. (DERIVED)

## Items diverged

- The failing value reads `request race state not reset at attempt <n>`, the named failure followed by the attempt the loop stopped on, so AC1's "on attempt 2" is read off the row itself.
- A stopped loop keeps no attempt, so the `DPR52 AC4` bound row reds beside the `DPR58 AC1` row on the same run; that row is unit 52's as built, which the spec's design leaves untouched, and the `DPR58 AC1` row is placed first so the reset is named before it.

## Owed at the close

- AC1 in the suite run of shard 8, and the `New arm:` line's RED-first observation: a copy of the block whose loop carries no clear and sleeps 11 s (PINNED) between `held` and B on attempt 1 only, red `request race state not reset`, and green with the clear kept.
- `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8`, each raised by the one row, read by the suite run.
- The legs the spec's Gates section names, run once by the main loop.
