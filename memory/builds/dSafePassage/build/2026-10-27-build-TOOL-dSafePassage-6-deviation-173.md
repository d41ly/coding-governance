# TOOL-dSafePassage-6 deviation 173 — the window's count takes the repository it asks

**Serves:** deviation TOOL-dSafePassage-6

- **Departs from:** TOOL-dSafePassage-6@rev-6 [§4 The window]
- **Hand-off:** spec-to-code
- **Before:** step 3 spells `derive_shim_window(landing, releases, window)`, which counts the releases that descend from the landing commit and answers open-allowed or held.
- **After:** `derive_shim_window(landing, releases, window, root)` in `tools/govkit/shims.py` returns `(may close, releases since)`: `root` is the repository `git merge-base --is-ancestor` asks, and the count is returned so `check_shim_windows`'s refusal line prints it without counting a second time.
- **Cause:** builder discovery
- **Reason:** whether a release descends from a commit is a question only git can answer, and git needs the repository; a function holding three arguments had no way to ask the scratch repository a fixture builds rather than the working directory, and a second count in the caller would be the same answer computed twice.
- **Evidence:** this unit's acceptance ledger, its AC6 line: every pair of the AC6 table exits as the table states, each refusal line printing the count, e.g. `landed at 1a490e4f, 3 release(s) cut since of 3, window 4`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-6, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** TOOL-dSafePassage-6
