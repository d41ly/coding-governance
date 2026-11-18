# TOOL-dDeclaredLoop-54 deviation 542 — the plant grader drops the composition it no longer reads

**Serves:** deviation TOOL-dDeclaredLoop-54

- **Departs from:** `TOOL-dDeclaredLoop-54@rev-4` [§2, §4]
- **Hand-off:** spec-to-code
- **Before:** S4 changes the `dead-end` entry of `tools/loop/termination.py#check_plant_found` to stop reading `derive_unchecked_levels` and names no change to the function's parameters, which take the first run's composition beside the case, the findings and the misses.
- **After:** `check_plant_found(case, found, misses)`: the composition parameter goes with the one entry that read it, and `run_termination_plant`, its one caller, stops passing it.
- **Cause:** builder discovery
- **Reason:** the `dead-end` entry's `derive_unchecked_levels(composition)` was the only read of the parameter, so once S4 removed it the parameter was passed and never read.
- **Evidence:** `git grep check_plant_found` over the tree outside the build records named the definition and its one call in `tools/loop/termination.py` and the codebase map's symbol row only; `--fixture --plant` for `dead-end`, `unit-dead-end` and `empty-states` each closed `held`, exit 0.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage — the close's `loop termination` leg runs every plant through the grader as built
- **Caused-by:** TOOL-dDeclaredLoop-33
