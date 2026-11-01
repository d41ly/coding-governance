**Serves:** journal TOOL-dSafePassage-99

# TOOL-dSafePassage-99 — acceptance ledger

The unit as built, at spec rev-2. Product write: `tools/govkit/selftest.py` only. S1:
`govkit_module()` takes the body of the spec's §4 "The held engine" fenced text, with the one
module-level name `GOVKIT_HELD`. S2: the three helpers and the six `main` sites of §4 "Inventory"
read `govkit_module()`, each `main` site's `sys.path.insert` line gone with its import; `govkit_mod`
is untouched. S3: four `[dSP-99]` checks at the end of `check_staged_copies`, after its `[dSP-71]`
checks, in the order of §4 "The arm". `tools` did not move between the spec's base `f519c1934` and
this pass's parent `512df720c`, and every cited line was where the spec says.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1 and AC2 call suite
functions, which scratch-guard's row G3 refuses to this role, so both are owed at the close. In their
place a scratch probe ran on node a (Windows 11) from this worktree's root, in a fresh process per
run: it imported `selftest`, called `govkit_module()`, staged a copy of the unchanged step module
through `build_staged_copy` under the run's scratchpad, called the copy's `load_govkit()`, then
re-ran the arm's checks 1, 2 and 4 and the `demand_contained_dest("../x", ...)` catch that
`read_refusal` depends on. Fixed body: `c1 displaced True`, `c2 held True`,
`c4 step load_govkit True`, the refusal caught by the first engine's `Refusal`. With
`govkit_module()` given back its `import govkit` body in memory: `c1 displaced True`,
`c2 held False`, `c4 step load_govkit False`, and `upgrade_steps.Refusal` raised past that catch,
which is the `leaked72` crash's cause. Check 3's break is AC3's red case.

Owed at the close: AC1 and AC2 by their own commands in a `git clone --shared` at the build commit,
the RED-first observation of §7's `New arm:` line, and the §7 legs at the bar.

**Evidences:** TOOL-dSafePassage-99
- AC1 — owed at the close: `check_upgrade_steps` by the spec's command to `FAILURES []`, and red with `govkit_module()` given back its `import govkit` body. The scratch probe above stands in for it in this pass.
- AC2 — owed at the close: `check_staged_copies` by the spec's command, four `ok   [dSP-99]` lines then `FAILURES []`; the scratch probe above observed checks 1, 2 and 4 under the fix and under the break, as §4 "The arm" predicts.
- AC3 — `git grep -n -E "^\s*(import|from) govkit\b" -- "*selftest.py"` printed nothing and exited 1. Red: at `f519c1934` the same lines were present at selftest.py:128, 139, 146, 153, 5792, 9099, 9187, 9562, 18394 and 18499, read before the edit at this pass's parent.
