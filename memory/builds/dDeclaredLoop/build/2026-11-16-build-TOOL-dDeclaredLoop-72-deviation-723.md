# TOOL-dDeclaredLoop-72 deviation 723 — a caller the re-ground predates, the sweep's stale figures, and what the build adds beside the inventory

**Serves:** deviation TOOL-dDeclaredLoop-72

- **Departs from:** `TOOL-dDeclaredLoop-72@rev-6` [§2, §4, §5]
- **Hand-off:** spec-to-code
- **Before:** §4's callers table, §2 S3's Readers clause and §4's Files touched name the callers of `read_memory_root` in `tools/loop/adapt.py`, `tools/loop/budget.py`, `tools/loop/loop_transition.py` and `tools/loop/breakpoints.py` alone; §5's sweep counts this spec's rows in `memory/project/positional-refs.txt` as three PINNED and prices the breakpoint leg's row at 179 PINNED seconds; §4's Inventory mints `resolve_memory_root` alone; §4's plants call the pre-placement staging with a root and README paths, and S5 adds one paragraph to `help/loop.md`.
- **After:** `tools/loop/termination.py#read_live_builds`, which `TOOL-dDeclaredLoop-33` landed after the re-ground, also called `read_memory_root`; the pass's grep found it and it moves to `resolve_memory_root`, as §4's callers section says of a caller an earlier order added. The registry holds no row of this spec, 0 PINNED, so no shrink runs. `tools/loop/loop_lib.py` binds one module constant beside the resolver, `DRIVER_ROOTS`, the hold per resolved tree and conf bytes, and drops `read_driver_conf`'s held `MEMORY_ROOT` answer before a changed conf is read again, since that reader holds its answer per conf path. `tools/loop/breakpoints.py#write_pre_placement_tree` takes a `confs` argument, the files of its conf commit, so the `unattended-root` plant writes both confs in that commit. The fixture list of `help/loop.md`'s breakpoints section names the two new plants. The breakpoint row is re-priced to 315 PINNED seconds from 297 PINNED, past the leg's 300 PINNED ceiling, which is not raised; the budget row to 482 PINNED from 476 PINNED.
- **Cause:** builder discovery
- **Reason:** the spec was re-grounded before unit 33's caller landed; the registry's rows went with an earlier positional shrink; the read-through of the driver conf's held answer and the staging argument are what S1's keying and §4's plant need from the code at this base; a plant list that omits two plants is a stale help page.
- **Evidence:** `git grep -n -w read_memory_root -- tools/loop` at this pass's base named `tools/loop/termination.py` beside the four modules §4 names; `grep -c 'spec-TOOL-dDeclaredLoop-72.md' memory/project/positional-refs.txt` printed 0 PINNED; the four new plants run alone by direct CLI took 2, 2, 8 and 4 PINNED seconds on node d.
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** gap — the breakpoint leg's priced row stands at 315 PINNED seconds above its 300 PINNED ceiling, as the budget leg's already does; the main loop re-prices both from its first reading of each leg at the close
- **Caused-by:** PLAY-dClosedLoop-2
