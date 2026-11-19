# TOOL-dSkippedRecord-1 — acceptance ledger

**Serves:** journal TOOL-dSkippedRecord-1

No merge bar, no self-test suite, no `--selftest` and no leg argv ran in this pass. The pass started
at 25ac107a5, and this ledger rides in the product commit that closes the spec. AC1 to AC4 were
observed by a `bash` probe under the session scratchpad that sources `tools/unattended/lib-unattended.sh`,
slices `run_render_helper` out of the built `tools/unattended/unattended.test.sh` and `write_run_record`
out of a driver copy, and calls the helper in each mode in a repository under `%TEMP%`. The base
driver is `git show 81657e77c:tools/unattended/unattended.sh`.

**Evidences:** TOOL-dSkippedRecord-1
- AC1 — `HEAD: same` — the built driver printed `unattended: run record unchanged`, `HEAD: same`
  and no `its commit failed` in mode `same`. The base driver printed "its commit failed" with git's
  "no changes added to commit" beneath it, and no skip line, in the same mode.
- AC2 — `HEAD: moved` — the built driver printed `run record committed at`, `HEAD: moved` and
  `SUBJECT: records(tRun): the run record` in mode `moved`, and so did the base driver.
- AC3 — `git could not stage what the index render moved: memory/LIVE.md` — the built driver printed
  that line and `HEAD: same`, with no `run record committed at`. A copy with the `return 0` after
  that line deleted printed `run record committed at` and `HEAD: moved`.
- AC4 — `git could not test whether the stage holds a change (git diff --cached exited 128)` — the
  built driver printed that line and `HEAD: same`. A copy with the `case`'s catch-all arm removed,
  and the base driver, each committed and printed `HEAD: moved`.
- AC5 — `unchecked 0` — section 4's `scan_stage_file` probe over the built driver printed
  `unchecked 0` and a one-item list holding the `records($slug): the run record` commit line; over
  the base it printed `unchecked 1` and an empty list. The registry `grep -c` printed 0.
- AC6 — `grep -h -e 'unattended: run record' tools/unattended/unattended.sh` — against the
  `git grep` at 81657e77 it printed every base line unchanged and in order, plus the skip and
  refusal lines and nothing else. The `return [1-9]` count over `write_run_record` printed 0, and
  the `holds a diff` count over the comment and the function printed 2.

**Also probed:** the two existing no-mode calls of `run_render_helper` still answered their
`src/lu.sh` refusal and their `memory/LIVE.md` stage through the probe.

**Owed to the close (the main loop, after every unit is terminal):**
- New arm `tools/unattended/unattended.test.sh` region 8, mode `same` with `moved` as its control,
  covering AC1 and AC2: RED with `write_run_record` restored from 81657e77, GREEN once restored.
- New arm `tools/unattended/unattended.test.sh` region 8, modes `addfail` and `difffail`, covering
  AC3 and AC4: RED with the `return 0` after the second stage's refusal line deleted, and with the
  catch-all arm removed, GREEN once restored.
- The stage-commit leg's argv over the drained registry, and the gates section 7 names.
