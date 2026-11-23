**Serves:** journal TOOL-dBoundRoles-19

# TOOL-dBoundRoles-19 — the main loop's decision: the unit waits on its F4 ask, and the roster's consumers wait with it

Unit 19's spec at its live revision resolves §8 F4 to option (a): an ask that `adopter-rule` type a level-5 `repo`
unit, the unit waiting on it. At `55fd56fd3` the gap holds: the module docstring of the playbook kit's
`instruction_units.py` and `check_unit_row` still hold an `adopter-rule` to a level-0 `repo` unit. dOrderedCharter
is CLOSED, so the run filed the ask in this build's own `BACKLOG.md` as `TOOL-dBoundRoles-80`, with its severity
row, beside the four that hold unit 20 (`TOOL-dBoundRoles-77` to `-79` and `TOOL-dDeclaredLoop-120`).

The main loop walked every remaining roster spec's `consumes-from` edges over units 19, 20, 25 and 43, to a fixed
point. Every remaining unit but TOOL-dBoundRoles-18 consumes from one of them, directly or through another:
42, 44, 50, 51, 56, 57, 58, 60, 62, 63, 64, 65, 66, 67, 68 and 69. A unit built before what it consumes would
build against code its spec says is not there, so each is deferred with `--rescope --act defer`, its reason naming
the unit it waits on. Options weighed: (a) wait, as the specs' F4 and F8 picked; (b) build the five gaps in the
playbook and loop kits here, the option both forks refused because it widens a unit into sibling kits' grammar,
a design no spec of this build states. Pick (a). options: (a) > (b) · admitted-by: principle.p18 · widens: none ·
relaxes: none.

The run builds TOOL-dBoundRoles-18, then closes. The deferred set, its five asks and every defer act are the
owner's at the wrap-up: the build's carry-forward rule leaves a deferred unit an earlier run added unmet, so the
close hands the build to the owner rather than landing it as complete.
