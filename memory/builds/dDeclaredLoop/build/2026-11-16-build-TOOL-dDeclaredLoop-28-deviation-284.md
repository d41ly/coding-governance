# TOOL-dDeclaredLoop-28 deviation 284 — the position's `undeclared` field maps each tag to the states its moves left

**Serves:** deviation TOOL-dDeclaredLoop-28

- **Departs from:** `TOOL-dDeclaredLoop-28@rev-6` [§2 S7]
- **Hand-off:** spec-to-code
- **Before:** `TOOL-dDeclaredLoop-28`'s spec at rev-6 gives the position an `undeclared` field holding each tag a recorded move names that the composition at the pin lacks, and has `derive_path_deviations(pos, state)` file an `extra` for each such tag a move out of the move's from-state named.
- **After:** `tools/loop/position.py#derive_position_into` writes `undeclared` as a mapping from each such tag to the from-states of the moves naming it, and `tools/loop/adapt.py#derive_path_deviations` reads an `extra` where that list holds the from-state.
- **Cause:** builder discovery
- **Reason:** the comparison's signature takes the position and the state alone, and a bare list of tags drops which state each move left, so the `extra` clause could not be read without a second read of the moves that the position already made.
- **Evidence:** `tools/loop/position.py#derive_position_into` and `tools/loop/adapt.py#derive_path_deviations` at the pass commit of `TOOL-dDeclaredLoop-28`; a `python -c` probe of `derive_path_deviations` read one `extra` for the state the mapping held and none for another.
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** TOOL-dDeclaredLoop-28
