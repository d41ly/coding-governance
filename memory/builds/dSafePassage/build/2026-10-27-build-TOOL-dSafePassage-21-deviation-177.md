# TOOL-dSafePassage-21 deviation 177 — the `entry` plant drops its retired kit from gov's deploy `kits`

**Serves:** deviation TOOL-dSafePassage-21

- **Departs from:** TOOL-dSafePassage-21@rev-3 [§3 Non-goals]
- **Hand-off:** spec-to-code
- **Before:** §3 puts "the other eight classes and the gate's verdict" out of scope, and `write_entry_plant` in `tools/govkit/step_gate.py` deletes a registry `[[entry]]` row and its descriptor and nothing else.
- **After:** `write_entry_plant` also removes the retired id from the `kits` array of the clone's `.governance/deploy.toml` where that array names it. No class reader, no witness and no verdict moved; the `file` plant gained a branch writing a source receipt from the plan where the clone carries none, which AC2 needs on a tree with no receipt.
- **Cause:** builder discovery
- **Reason:** the `file` class now reads gov's plan on a tree with no receipt, and gov's plan refuses a deploy `kits` naming an id the registry lacks, so the unchanged plant made `--fixture --plant entry` exit 2 where TOOL-dSafePassage-10's fixture arm wants 1 and then 0. A kit retired on gov leaves gov's own deploy file in the same landing, so the plant now stages that retirement whole.
- **Evidence:** this unit's acceptance ledger: before the change `--fixture --plant entry` printed `step-gate: REFUSED · the target's deploy.toml names check-install-prefix in kits, which is not a registry entry` and exited 2 bare and with `--with-row`; after it, it exits 1 naming `entry:check-install-prefix` and its four `file:` and `installable:` destinations, and 0 with the row.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-21, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** TOOL-dSafePassage-21
