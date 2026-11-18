# TOOL-dDeclaredLoop-70 deviation 702 — the parent arm's red reads unanswered, the sweep's stale figures, and the names the inventory does not list

**Serves:** deviation TOOL-dDeclaredLoop-70

- **Departs from:** `TOOL-dDeclaredLoop-70@rev-4` [§4, §5, §6]
- **Hand-off:** spec-to-code
- **Before:** §6 AC2's Red-when says a parent read passing no tree exits 2 printing `loop: unarmed` and naming `STAGING`; §5's sweep counts the rows of this spec in `memory/project/positional-refs.txt` as five, and §4's Evidence says no tracked file under `tools/` or `help/` spells `derive_phase_position`; §4's Inventory mints `read_driver_conf` alone among module names.
- **After:** that red exits 2 printing `loop: unanswered`, naming `STAGING`: `tools/loop/loop_parents.py#read_withdrawn_parents` turns the phase reading's LookupError into a ValueError, which the route prints `unanswered`. At this pass's base the registry holds no row of this spec, 0 PINNED, and units 52, 63 and 56 spell `derive_phase_position` in `tools/loop/loop_table.py`, `tools/loop/loop_parents.py` and `tools/loop/README.md`, as §5's ordering expects. `tools/loop/loop_lib.py` also binds three PINNED module constants beside the reader: the process memo `DRIVER_CONF_READS`, the sentinel pair `CONF_SENTINEL` and the name shape `CONF_NAME`. The verb's `adopter phase` marker reads "the map holds no row of the phase and the reading answered" as the phase's absence from the map's rows, the reading having raised otherwise.
- **Cause:** builder discovery
- **Reason:** the Red-when word predates unit 56's landed conversion of the refusal; the registry's rows went with the positional shrink after rev-3; the constants keep the reader's literals named once.
- **Evidence:** a probe at this pass with `derive_phase_position` wrapped to drop `tree` printed `loop: unanswered · the parent tParent's phase STAGING maps to no state: phase STAGING: no row`, exit 2, and the plant as built printed `route none`, exit 0; `grep -c 'spec-TOOL-dDeclaredLoop-70.md' memory/project/positional-refs.txt` printed 0 PINNED; `git grep -c derive_phase_position HEAD -- tools help` named the three PINNED files.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage — the close observes the `tools/loop/loop_parents.py` arm RED as `loop: unanswered`, exit 2, where the arm's Red-when says `unarmed`; the `loop parent routes` leg reads the plant as built
- **Caused-by:** PLAY-dClosedLoop-2
