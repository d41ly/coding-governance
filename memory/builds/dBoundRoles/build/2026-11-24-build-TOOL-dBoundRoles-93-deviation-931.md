# TOOL-dBoundRoles-93 deviation 931 — the builder's departures from its own section 4

**Serves:** deviation TOOL-dBoundRoles-93

- **Departs from:** `TOOL-dBoundRoles-93@rev-1` [§4 "The PowerShell block", "Rows", "The plants", "Documents", AC3]
- **Hand-off:** spec-to-code
- **Before:** §4 scans a substitution inside a block twice, once through the substitution and once through the block, and drops the second entry in `addTarget`; the polling rows carry no label of the tool; the plants section does not say how the directory outside every repository is made; the README's items are the polling row, the polling paragraph, the block sentence and the escapes.
- **After:** (1) In `tools/hooks/scratch-guard.js#scanCommandHeads` the substitutions are masked first, the blocks are found, and a substitution that lies inside a block is left to that block's own scan, so each text is scanned once per level. Every target and head is the one the spec's order yields. The masking keeps the base's form, so the pop of `scanSubstitutions` keeps the row AC4 reads. (2) The README and the header say "a Bash `for` loop" where they named the short `sleep` the polling rows do not see, since a PowerShell one now refuses, and the README's role-gate section names the block beside the polling paragraph. (3) The polling rows print the tool in their label where they carry one. (4) `tools/loop/loop_items.py#run_declaration_plant` makes the directory with `tempfile.TemporaryDirectory`, and both `declaration-` rows that owe the composed item share one expected line. (5) The usage marker of `help/loop.md` is unchanged: `python tools/govkit/docs_leg.py --fingerprints` prints the value the page holds. (6) The AC3 reading ran over the commands the rows hold, the polling rows included, and `checkPollWait` beside the two readers it names.
- **Cause:** builder discovery
- **Reason:** with each text scanned twice, blocks and substitutions nested in turn double the work at every level; a scratch copy over a deep nest of them threw on the entries it pushed, and a throw in the arm refuses a role agent. The rest keeps the pages true and reuses what stands.
- **Evidence:** the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-93-1-acceptance-ledger.md`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value; reported by the `report` value
- **Follow-through:** none
- **Caused-by:** TOOL-dBoundRoles-93
