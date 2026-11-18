# TOOL-dDeclaredLoop-79 deviation 793 — the scratch kits' descriptor body shared by the two vintage arms

**Serves:** deviation TOOL-dDeclaredLoop-79

- **Departs from:** `TOOL-dDeclaredLoop-79@rev-7` [§4]
- **Hand-off:** spec-to-code
- **Before:** §4 "The gained prune" and its inventory mint one function, `check_gained_prune_vintage`, built on `tools/govkit/selftest.py#build_steps_gov`, and say nothing of the scratch descriptor body `tools/govkit/selftest.py#check_requires_vintage` spells inline.
- **After:** that body is the module constant `VINTAGE_KIT_BODY` in `tools/govkit/selftest.py`, read by both arms; `check_requires_vintage` reads the same bytes it spelled, and its docstring's unchecked clause now names the new arm as the gained prune's check.
- **Cause:** builder discovery
- **Reason:** the new arm needs the same descriptor body for each of its three kits, and the charter's reuse rule extracts at the second instance rather than copying; no arm's behaviour moves.
- **Evidence:** the AC19 probe of `check_gained_prune_vintage` printed `ok` on every row; the extraction is a byte-identical move of the string.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage — the next arm staging a scratch kit reads the constant.
- **Caused-by:** PLAY-dClosedLoop-2
