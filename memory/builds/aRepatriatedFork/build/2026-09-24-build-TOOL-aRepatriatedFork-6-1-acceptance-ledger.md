# TOOL-aRepatriatedFork-6 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-6

Written at the main loop from the unit pass's return (commits `68af7553` and `eb9d5c58`), because
the pass closed the unit without one and hygiene check 23 then named every criterion. Each line is
an observation that pass made and reported; nothing here was re-run to write it. No merge bar and no
suite ran in the pass. The new suite arms in `tools/unattended/unattended.test.sh` and
`tools/unattended/check-unattended.test.sh` have never executed, and the close owes them.

**Evidences:** TOOL-aRepatriatedFork-6
- AC1 — `yes` — the driver's `set_fact` and `fact`, extracted from the worktree into a scratchpad probe, store `yes` and a value holding a literal line feed returns rc 1 with the fail 17 text, the file hash unchanged
- AC2 — `yes\nphase: LANDED` — at a7c78ad2 the backslash-n form wrote a second `phase` line and phase read LANDED; in the worktree it is stored on one line exactly as written and phase reads RUNNING
- AC3 — `tools/unattended/unattended.sh` — the S4 matrix over every value-writing verb is written as suite arms and not executed; the close owes it, and `record-piece` and `record-set` may refuse a non-recipe run before the hostile value is reached
- AC4 — `git hash-object` — the run-state file's hash is unchanged after each refused write in the probe, so the guard runs before the file is touched
- AC5 — `phase: RUNNING` — a `phase: FORGED` line planted above the real phase in a tracked run-state file made check 34 exit 1 naming the file, `phase` and both values; the exact RUNNING/LANDED arm is a suite arm the close owes
- AC6 — `tools/unattended/check-unattended.sh` — `GOV_UNATTENDED_REPORT=1` over gov's tree exits 0 and prints that check 34 graded 67 run-state files; a predicate pass over the same files found 0 hits and one same-value near-miss
- AC7 — `--close` — the refusal block, sliced out of the shipped driver and run per item, prints the override remedy for `build-complete` and `closing-review-recorded` and nothing for `gates-green`, `authorization-reachable` and `pieces-complete`
- AC8 — `bash tools/check-kit-versions.sh` — exits 0 with unattended at 1.29, and exits 1 naming the file with one carrier reverted to 1.28
