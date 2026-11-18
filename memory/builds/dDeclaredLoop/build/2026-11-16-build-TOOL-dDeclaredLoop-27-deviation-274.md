# TOOL-dDeclaredLoop-27 deviation 274 — `check` exits unarmed where the scenario composition is unarmed

**Serves:** deviation TOOL-dDeclaredLoop-27

- **Departs from:** `TOOL-dDeclaredLoop-27@rev-4` [§4 The rules `check_scenarios` holds, §4 The CLI]
- **Hand-off:** spec-to-code
- **Before:** `TOOL-dDeclaredLoop-27`'s spec at rev-4 says the rules hold over gov's pack beside the repository rows the scenario composition answers at HEAD, gov's pack alone where that composition answers unarmed, and its CLI says `check` exits 2 `unarmed` where the kind is unregistered, its schema is absent or HEAD holds no pack, which are the composition's unarmed answers.
- **After:** `tools/loop/scenario.py#run_check` exits 2 printing `loop: unarmed · <why>` wherever the scenario composition answers unarmed, and grades gov's pack from the working tree beside the repository rows only where it answers 0.
- **Cause:** builder discovery
- **Reason:** the two sentences name the same condition with two outcomes; the CLI's is the narrower and deny-by-default reading, and every case the spec's plants and the factory's gate run composes armed, so no criterion moves.
- **Evidence:** `tools/loop/scenario.py#run_check` at the pass commit of `TOOL-dDeclaredLoop-27`; the factory's `scenario-new` and `scenario-hand` plants run it in a clone whose HEAD holds the pack.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** TOOL-dDeclaredLoop-27
