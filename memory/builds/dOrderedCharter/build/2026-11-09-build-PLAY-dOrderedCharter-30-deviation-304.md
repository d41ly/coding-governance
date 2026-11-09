# PLAY-dOrderedCharter-30 deviation 304 — the four paired legs' own pending rows deleted with the pairing

**Serves:** deviation PLAY-dOrderedCharter-30

- **Departs from:** `PLAY-dOrderedCharter-30@rev-6` [Design]
- **Hand-off:** spec-to-code
- **Before:** the pairing section says the pending list loses the two retired practice rows and gains the three rule rows, and names no other change to `tools/playbook/core-pending.txt`.
- **After:** the pending list also loses the `leg` rows of `encoding posture (text IO names its encoding)`, `shell hygiene (a location probe asked from a moved directory)`, `shell hygiene (a fixed-name temp renamed into place)` and `python resolver (behaviour + inline parity + idiom ban)`, the four legs that now carry the rule tags in `enforces`.
- **Cause:** builder discovery
- **Reason:** the meta-check counts a leg carrying `enforces` as claimed, so each of those four legs' pending row would red as stale, and AC3 asks the meta-check to exit 0 over the tree after the pass; the list is shrink-only, so deleting a row the pairing arms is the move its header names.
- **Evidence:** a probe over the tree after the pass read the legs' `enforces`, the pending rows and the catalogue: no leg row pending while its leg enforces, every rule tag enforced or pending, no rule tag both.
- **Risk:** additive
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-30
