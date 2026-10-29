**Serves:** journal TOOL-dSafePassage-86

# TOOL-dSafePassage-86 — acceptance ledger

The unit as built, at spec rev-3. Product write: `tools/govkit/upgrade_walk.py` (S1 the function
`derive_release_engine` under the release-0 banner and the release-0 `apply` call running it; S2 the
nested grader `check_grade_release_engine`, the `release-engine` row after `fixture-keys`, and the
`check_graders` docstring naming this unit). `memory/map/generated/symbols.json` regenerated for the
new function.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node
a (Windows 11): AC1 and AC3 from this worktree's root over its working copy; AC2 from the
`scripts/govkit` directory of a `git clone --no-hardlinks` of this branch's HEAD `b0106aa1f` under
`%TEMP%/sp86`, with `git mv tools scripts` committed and then the unit's `upgrade_walk.py` committed
over the moved copy; the clone was removed after.

Owed at the close: the RED-first observation of §7's `New arm:` line — the `release-engine` grader of
`check_graders`, staged red by a `derive_release_engine` that returns the clone joined with HERE's
relative path — and the §7 legs at the bar. The probe below monkeypatched the function in a
`python -c` and edited no file, so it does not discharge the arm's staged-break observation.

**Evidences:** TOOL-dSafePassage-86
- AC1 — `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import upgrade_walk as u; print(u.check_graders())"` — printed six `ok` grader lines, among them `upgrade-walk: grader · release-engine · ok`, and last line `[]`. With `u.derive_release_engine` monkeypatched to `clone / f'{rel}/govkit.py'` (HERE-relative, `rel` = `tools/govkit`) the same call printed `upgrade-walk: grader · release-engine · RED · a pin at scripts derived ...\pin-scripts\tools\govkit\govkit.py, not ...\pin-scripts\scripts\govkit\govkit.py` and `['grader release-engine']`.
- AC2 — `FOREIGN_PREFIX_PROBE=1 python upgrade_walk.py --case up` from the moved clone's `scripts/govkit` — exit 2, printed `upgrade-walk: release-0 applied by the pinned clone's own apply over the fixture's kits line · exit 0 · receipt schema 3`, then `nothing measured: plant engine-edit: scripts/memory-tree/README.md is absent at release-0` (M7, TOOL-dSafePassage-87's), and no line holding `release-0's apply exited`. With the clone's `upgrade_walk.py` reverted to HEAD's, the same run printed `nothing measured: release-0's apply exited 2` and `can't open file '...\gov\scripts\govkit\govkit.py'`, exit 2.
- AC3 — `git grep -n -F 'clone / ctx["govkit"]'` printed nothing; `git grep -n -F "derive_release_engine("` printed three lines, `upgrade_walk.py:183` (the definition), `:219` (the `apply` call) and `:1046` (the grader); `git grep -n -F '"govkit": f"{rel}'` printed one line, `:211`, the HERE-relative `ctx["govkit"]`.
