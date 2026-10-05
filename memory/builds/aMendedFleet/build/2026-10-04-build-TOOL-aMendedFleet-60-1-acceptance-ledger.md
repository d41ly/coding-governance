# TOOL-aMendedFleet-60 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-60

**Evidences:** TOOL-aMendedFleet-60
- AC1 — `tools/drift-audit/drift_report.py` — under `%TEMP%`/ov60 a clone of the worktree carrying the unit's driver was committed, cloned bare, and cloned twice more; the second clone force-pushed `side` with one appended line to that file, and in the third clone `bash tools/unattended/unattended.sh --preflight aMendedFleet --keepalive-id probe` printed the summary line `1 sharing a path; this run is NOT blocked` and `origin/side · <tip> · 0d old · 1 shared: tools/drift-audit/drift_report.py (diff)`. Exit status 1 before the branch existed and 1 with it, the clone standing on its default branch both times
- AC2 — `KIT_UNATTENDED_VERSION` — `side` reset to the base with only that line moved from 1.61 to 1.62 in `tools/unattended/unattended.sh`: the summary counted the ref and printed `no shared path`, no line naming the file tagged `diff`. Staged break: with the marker test in the formatting awk replaced by `if (0)` the same run printed `tools/unattended/unattended.sh (diff)`
- AC3 — `GIT_COMMITTER_DATE` — `side` re-made thirty days in the past with the AC1 edit: the summary read `1 aged out past 14 days` and `no shared path`, and no line named `origin/side`
- AC4 — `tools/runlog/runlog.py` — `side` adding one `SPECCED` spec under `memory/builds/tSide/spec/` whose Files touched names that path, no product edit: the line read `1 shared: tools/runlog/runlog.py (declared)`; the spec flipped to `WONTDO` and re-pushed, the summary read `no shared path`
- AC5 — `memory/DECISIONS.md` — `side` appending a row to that file only: `no shared path`; with the third clone carrying its own committed edit to the same file, the exclusion's containment test replaced by `if (0)` printed `memory/DECISIONS.md (diff)` and the restored driver printed `no shared path`. With the clone's remote URL set to a path that does not exist, stdout carried `overlap probe UNAVAILABLE — no observed default-branch tip names a commit in this clone`
- AC6 — `grep -n "check_cross_run_overlap" tools/unattended/unattended.sh` — printed two lines: the definition, and one call `check_cross_run_overlap "$slug" || true` on the line after `check_single_live || true` in `verb_preflight`; no comment spells the name. The card's verb `print_overlaps` is a later unit's and is not in this commit
- AC7 — `grep -n "overlap probe" tools/unattended/README.md` — hit the new section "The overlap probe at `--preflight`", whose bullets say it never fetches and refuses nothing

## The suite arm

The fourteen new assertions in `tools/unattended/unattended.test.sh`, beside the concurrent-run arms
in region one, were cut out by line range behind the suite's prologue with `HERE` pinned to the kit
dir and run alone from the session scratchpad: 34 assertions passed, prologue included. With the
probe's one call deleted from the working driver the same slice failed nine of them, the `miss`
arms passing vacuously as they must; the call was restored byte for byte. The whole suite was not
run; it is owed at the close, and both floors were raised by the fourteen counted off the block.
