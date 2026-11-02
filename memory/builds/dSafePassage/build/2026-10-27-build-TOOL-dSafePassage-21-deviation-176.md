# TOOL-dSafePassage-21 deviation 176 — the `file` class's help row and summary name its second source

**Serves:** deviation TOOL-dSafePassage-21

- **Departs from:** TOOL-dSafePassage-21@rev-3 [§5 Production-readiness checklist]
- **Hand-off:** spec-to-code
- **Before:** §5 reads "user docs: N/A — `help/step-gate.md` names the class, not its source", and §4 Files touched names `govkit.py`, `step_gate.py` and `selftest.py` alone.
- **After:** `help/step-gate.md`'s `file` row and the `file` class's `summary` in `tools/govkit/surface-classes.toml`, which `step_gate.py --list` prints, each add "else each destination gov's own plan derives" after the receipt they already named.
- **Cause:** builder discovery
- **Reason:** both texts name the receipt as the class's one source, so after this unit they misstate it on every tree carrying no receipt, which is gov's branch; the charter's `[docs]` rule holds a user-facing change undone until its help page is current.
- **Evidence:** `help/step-gate.md` line 15 and `tools/govkit/surface-classes.toml` line 18 at base 4cabc885 both read "each `files` row's path in gov's source-mode receipt, `.governance/install.json`".
- **Risk:** editorial
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-21, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** TOOL-dSafePassage-21
