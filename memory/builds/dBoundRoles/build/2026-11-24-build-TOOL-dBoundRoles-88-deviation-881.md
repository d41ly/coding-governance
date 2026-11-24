# TOOL-dBoundRoles-88 deviation 881 — the builder's departures from its own section 4

**Serves:** deviation TOOL-dBoundRoles-88

- **Departs from:** `TOOL-dBoundRoles-88@rev-1` [§4 "The mechanism", "Ceiling", "Inventory", "The arms"]
- **Hand-off:** spec-to-code
- **Before:** the Inventory mints the two functions alone; the scan splits the text at a line feed; the ceiling names `workflow` bound to another name, and a template literal's line opening `//`, as what the scan does not see; the refused-literal rows stand on `h.js`.
- **After:** (1) `tools/roles/spawn-guard.js#buildHarnessKey` holds the fold `resolveHarnessEntry` spelled, and both readers call it, as section 4 allows; it is not exported. (2) The text is split wherever JavaScript ends a line, a lone carriage return, U+2028 and U+2029 included, so a comment line hides no code that runs after one. (3) The docblock and the README state the hiding forms found while building as well: a call not spelled `workflow(`, a line opening `//` that a block comment spans, and a second `scriptPath` key or a spread after the first in the same literal. S1 admits that literal, so the scan does not refuse it. (4) The suite's rows stand on one landing: `h7.js`, `h8.js` and `h9.js` hold the variable, the undeclared path and the comment. Its `run_landed` gains `run_landed_call`, the payload both it and the real-harness rows send. (5) The unreadable working-tree file is refused in the walk by name, and a deleted one by `checkHarnessLanded`'s own hash refusal. (6) Named and not changed: the literal is folded to lower case as `resolveHarnessEntry` folds its path, so on a case-sensitive filesystem a literal differing from its entry by case alone is held as that entry.
- **Cause:** builder discovery
- **Reason:** the charter's reuse rule asks for the factory at a kind's second instance, and the security rule asks that a stated ceiling hold each form known.
- **Evidence:** the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-88-1-acceptance-ledger.md`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value; reported by the `report` value
- **Follow-through:** none
- **Caused-by:** TOOL-dBoundRoles-88
