# TOOL-dDeclaredLoop-76 deviation 763 — the sweep's stale figures, a fifth caller, and the README rows beside the two the spec adds

**Serves:** deviation TOOL-dDeclaredLoop-76

- **Departs from:** `TOOL-dDeclaredLoop-76@rev-6` [§4, §5]
- **Hand-off:** spec-to-code
- **Before:** §5's sweep prices the budget leg's row at 476 PINNED seconds and the breakpoint leg's at 179 PINNED, names the callers of `resolve_memory_root` in `tools/loop/adapt.py`, `tools/loop/budget.py`, `tools/loop/loop_transition.py` and `tools/loop/breakpoints.py` alone, and counts this spec's rows in `memory/project/positional-refs.txt` as two PINNED, which a shrink takes out; S5 has the kit README gain one row for each of S1 and S2; §4's plants write no scratch tree for `no-own-conf-read`.
- **After:** at this pass's base the budget row read 482 PINNED and the breakpoint row 315 PINNED, both as unit 72 re-priced them; each is re-priced from a timed run of the added plants, the budget row to 485 PINNED and the breakpoint row to 317 PINNED, and neither leg's 300 PINNED ceiling in the leg manifest is raised. `tools/loop/termination.py#read_live_builds` also calls `resolve_memory_root`, as unit 72 recorded; it keeps its call and its answer and is not edited. The registry held no row of this spec, 0 PINNED, so no shrink runs. The README's `resolve_memory_root` row now names the pair's root, the `resolve_memory_root_source` row carrying the resolution it described, and the paragraph naming the function that imports `read_design_conf` names `resolve_memory_root_source`, the function that now does. `run_budget_plant` and `run_breakpoint_plant` make their empty temp folder before the case dispatch, so the `no-own-conf-read` branch creates and removes that folder and writes nothing in it.
- **Cause:** builder discovery
- **Reason:** the spec was re-grounded before unit 72 landed its re-prices and its fifth caller, and after an earlier positional shrink took the registry's rows; a README row describing a body that moved, beside the row that now holds it, would say one fact twice; the temp folder is the plant runner's own, shared by every case.
- **Evidence:** `git grep -n -w resolve_memory_root -- tools/loop` at this pass's base named `tools/loop/termination.py` beside the four modules §5 names; `grep -c 'spec-TOOL-dDeclaredLoop-76.md' memory/project/positional-refs.txt` printed 0 PINNED; the three added plants run alone by direct CLI on node d took 664, 920 and 575 milliseconds, each priced at 1 PINNED second.
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** gap — the breakpoint leg's priced row stands at 317 PINNED seconds above its 300 PINNED ceiling, as the budget leg's already does; the main loop re-prices both from its first reading of each leg at the close
- **Caused-by:** PLAY-dClosedLoop-2
