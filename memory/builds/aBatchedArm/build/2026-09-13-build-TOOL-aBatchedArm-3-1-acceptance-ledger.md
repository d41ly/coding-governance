# TOOL-aBatchedArm-3 — acceptance ledger

**Serves:** journal TOOL-aBatchedArm-3

Written as the readings were taken, not after. Every long run went on a frozen `git clone --local`
under `C:/Users/daily-agent/AppData/Local/Temp/u3/` with stdout and stderr redirected to a file and
`date +%s` stamped beside it; the runner helper is `u3/runsuite.sh`, which also routes bash's xtrace
to fd 9 so the floor-graded `$n` can be read from a RED run (the suite prints it only on `PASS` or on
a floor breach, and the suite is RED at BASE). The trace shares no fd with anything an arm captures.

## Host state

The box was NOT idle when this unit started, 2026-09-13 19:25 local: `ps -ef` showed another
session's five `check-unattended.test.sh --shard 2/2` runs (started 18:36 under
`$TEMP/ar2/`), one unsharded `tip/check-unattended.test.sh`, a `run-gates.sh` bar (19:23) and a
`run-gates.test.sh`. Every UNTIMED run below was taken beside them; every TIMED reading names the
`ps` answer beside it, and a reading taken beside another bar is written as NO READING.

## Runs

- `s2base` — the unsharded run at BASE `0422ea2e` on clone `u3/base` (suite blob
  `29b8175b`), started 19:27 local, untimed. Yields AC12's baseline `FAIL` set and AC6's pre-split
  floor-graded count, read from the trace line `'[' <n> -ge 392 ']'`.

**Evidences:** TOOL-aBatchedArm-3
- AC12 — pending.

## What this ledger does not evidence

Pending.
