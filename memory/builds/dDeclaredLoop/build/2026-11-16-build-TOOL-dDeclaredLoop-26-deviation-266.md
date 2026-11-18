# TOOL-dDeclaredLoop-26 deviation 266 — the new leg's row carries the stage claim the spec does not name

**Serves:** deviation TOOL-dDeclaredLoop-26

- **Departs from:** `TOOL-dDeclaredLoop-26@rev-6` [§2 S8]
- **Hand-off:** spec-to-code
- **Before:** `TOOL-dDeclaredLoop-26`'s spec at rev-6 gives the leg `loop composition fixtures` its argv, chunk `selftests`, subject `kit`, the ceiling of `loop position fixtures` and `enforces` holding `principle.p8`, and names no `stage` key.
- **After:** the leg's row in `tools/gate-legs.json` also carries `"stage": ["step.test"]`, its last key, as every other loop fixture leg's row does.
- **Cause:** builder discovery
- **Reason:** every row of the manifest carries a `stage` claim, which `loop stage coverage` joins both ways and reds where absent (its `unclaimed-leg` plant), so a row without one newly reds a leg; the claim is the one every sibling loop fixture leg makes.
- **Evidence:** the row `loop composition fixtures` in `tools/gate-legs.json` at the pass commit of `TOOL-dDeclaredLoop-26`, beside the `stage` of `loop upstream fixtures` and `loop position fixtures`.
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** TOOL-dDeclaredLoop-26
