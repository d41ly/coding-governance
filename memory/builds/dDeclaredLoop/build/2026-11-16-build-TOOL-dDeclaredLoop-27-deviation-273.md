# TOOL-dDeclaredLoop-27 deviation 273 — the activated item rows reach the position through `read_composed_items`

**Serves:** deviation TOOL-dDeclaredLoop-27

- **Departs from:** `TOOL-dDeclaredLoop-27@rev-4` [§2 S9, §4 Inventory]
- **Hand-off:** spec-to-code
- **Before:** `TOOL-dDeclaredLoop-27`'s spec at rev-4 has the position engine pass the activated item rows to `read_composition_at`, and its inventory gives a `rows` argument to `read_composition` and `kind` and `rows` to `read_composition_at` alone.
- **After:** `tools/loop/loop_items.py#read_composed_items` also takes `rows`, passed through to `read_composition` or `read_composition_at`, and `tools/loop/position.py#derive_position_into` hands the activated item rows to it, so they still reach `read_composition_at` at the pin.
- **Cause:** builder discovery
- **Reason:** unit 26 as built reads the position's items through `read_composed_items(repo, pin)`, the one owner of the composition's exit mapping (gov's own rows where unarmed, a ValueError where refused); calling `read_composition_at` from the position directly would copy that mapping, which the reuse rule forbids.
- **Evidence:** `tools/loop/loop_items.py#read_composed_items` and `tools/loop/position.py#derive_position_into` at the pass commit of `TOOL-dDeclaredLoop-27`; the `two-builds` and `mid-step-switch` plants of `tools/loop/scenario.py` read the activated rows through it.
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** TOOL-dDeclaredLoop-27
