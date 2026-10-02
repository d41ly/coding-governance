# TOOL-aRepatriatedFork-53 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-53

Written by the unit pass on node a, 2026-10-01. No merge bar and no suite ran: the spec's rev-2
committed before any code, and AC1 to AC8 were observed by a scratch fixture repository that drives
the driver with the same commands the new `unattended.test.sh` block spells, 48 assertions, exit 0.
Red first: the same fixture over the `56c7befa` driver failed 32 of the 48, every registration
refused as check 14's unknown argument and no task line printed. The suite block itself is owed its
first run to the main loop, with the floor raised by its 34 counted assertions.

**Evidences:** TOOL-aRepatriatedFork-53
- AC1 — `--register-task` — a task `leg-a` registered with a heartbeat touched one second earlier prints `unattended-audit: task leg-a · registered … · last-beat <n>s ago · PROGRESSING` and `--audit` exits 0. Red first: the `56c7befa` driver refused the verb with check 14
- AC2 — `TASK_STALL_BOUND` — at a declared bound of 60 the heartbeat aged an hour by `touch -d` prints `STALLED`, then the one remedy line naming `leg-a`, and `--audit` still exits 0
- AC3 — `no heartbeat-bearing tasks registered` — a run with no registry prints that line beside `no unit is dispatched and open` and exits 0
- AC4 — `last-beat none` — a heartbeat path not yet written reads PROGRESSING from its new row, and STALLED once that row's time is set an hour back
- AC5 — `fail 51` — a `stat` stub printing nothing makes `--audit` exit 1 with `UNATTENDED check 51 FAILED` naming `stat -c %Y on the heartbeat of task leg-a` and the file, and no PROGRESSING line
- AC6 — `--release-task` — the release exits 0, the next audit prints no `task leg-a` line, a second release refuses with check 88, a second registration of an open name refuses, and a fresh registration is graded from its new row
- AC7 — `read_bound_key` — a conf declaring `TASK_STALL_BOUND="0"` makes `--audit` exit 2 with the REFUSING line, and a conf without the key prints the NOTE naming the 5400s default; `--status` prints no such NOTE
- AC8 — `--heartbeat` — a relative path and a tab-bearing name each refuse with check 88 and the registry file is never created
- AC9 — `memory/guides/UNATTENDED-VERBS.md` — names `--register-task`, `--release-task` and `TASK_STALL_BOUND`, and `bash tools/unattended/adopt-unattended.sh --check` prints `in sync` and exits 0 after the re-render
- AC10 — `bash tools/check-kit-versions.sh` — exits 0 with every carrier at 1.51, and `python tools/govkit/govkit.py epoch --base 56c7befa` reports the unattended kit clean at 1.51 over the build commit
