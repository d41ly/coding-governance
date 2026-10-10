# DEPL-aBenchedProbe-4 — acceptance ledger

**Serves:** journal DEPL-aBenchedProbe-4

Built inline by the main loop on 2026-10-10, for the reason DEPL-aBenchedProbe-3's ledger gives. No
merge bar and no self-test suite ran: slices `S` and `A` are the spec's section 6 commands, run from
the repo root. Mutations of the worktree's `tools/govkit/govkit.py` were restored from a byte copy and
confirmed with `cmp`, with `__pycache__` cleared; slice `A`'s mutations were made in its gov copy only.
The close still owes `govkit selftest` whole, which is the one place S7's call from `main()` runs.

**Evidences:** DEPL-aBenchedProbe-4
- AC1 — `[]` — slice `S` printed `[]`, with `ok` lines for the receipt check, the second apply's exit,
  the kept 3600 and the second keep line.
- AC2 — `"ceiling": row.get("ceiling"),` — with the receipt write mutated to that, slice `S` printed
  FAIL for the receipt check and for CE4b's kept 3600 (and the second keep line); restored, `[]`.
- AC3 — `kept the target's ceiling` — with the keep print split into two calls, the leg on the first
  and `kept the target's ceiling` on the second, slice `S` printed FAIL for CE4's naming check. The
  pre-edit half (the same split leaving the old two-substring check `ok`) was not re-run.
- AC4 — `[]` — slice `A` printed `[]`, with `ok` for each staged replace's `LIVENESS` check, a1, a2,
  both ceiling values, arm (c) and the restored copy's exit 0.
- AC5 — `if chunk:` — with the copy's 7j4 exempt test widened to `if chunk:`, its glob tuple emptied,
  the 7h clause made `if False:` and the absent-manifest branch made unreachable, slice `A` printed
  FAIL for a1, a2, both ceiling arms and arm (c), whose output carried a `Traceback`, and `ok` for the
  restored copy.
- AC6 — `manifest_chunk: dict` — `grep -n "manifest_chunk: dict" tools/govkit/govkit.py` printed
  nothing; `python tools/govkit/govkit.py selfcheck` on the real tree exited 0 with no `NameError`, and
  its note read 59 graded and 22 self-test-shaped.
- AC7 — `line-claim-matched-over-the-whole-output` — `python tools/memory-tree/gotchas.py --check`
  exited 0 after the index render, and `--for-paths tools/govkit/selftest.py` listed the class.
