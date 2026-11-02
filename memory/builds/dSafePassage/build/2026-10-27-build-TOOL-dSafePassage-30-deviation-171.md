# TOOL-dSafePassage-30 deviation 171 — the gitlink walk reads each index with `core.fsmonitor=false`

**Serves:** deviation TOOL-dSafePassage-30

- **Departs from:** TOOL-dSafePassage-30@rev-3 [§2 S1]
- **Hand-off:** spec-to-code
- **Before:** S1's gitlink walk reads each repository's index with `git ls-files -s -z` under `build_step_env`'s environment, and nothing else on the command line; §3's Edges hand the fsmonitor half of finding 27 to `TOOL-dSafePassage-42`.
- **After:** `read_target_repositories` runs that read as `git -C <work tree> -c core.fsmonitor=false ls-files -s -z`, still under `build_step_env`'s environment.
- **Cause:** builder discovery
- **Reason:** an index read runs the repository's `core.fsmonitor`, and the walk runs before any config is graded, so S1 as written runs the very executor TOOL-dSafePassage-24's `local-fsmonitor` plant refuses: built without the flag, `fixture isolation --plant local-fsmonitor` printed `isolation: fsmonitor canary: present · fsmonitor` and `isolation: FAILED · the refused step spawned, or its executor ran`. Shipping that would regress a CLOSED unit's AC; the one flag is the smallest change that keeps it, and the grading-order half of finding 27 stays with TOOL-dSafePassage-42.
- **Evidence:** this unit's acceptance ledger, its "Unbroken neighbours" line: with the flag, `--plant local-fsmonitor` exits 1 with `fsmonitor canary: absent` and `core.fsmonitor=false · not refused · git add exits 0`.
- **Risk:** stricter
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-30, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-42
- **Caused-by:** TOOL-dSafePassage-24
