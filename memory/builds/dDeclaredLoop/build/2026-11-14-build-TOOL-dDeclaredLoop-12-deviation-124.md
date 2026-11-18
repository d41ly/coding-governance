# TOOL-dDeclaredLoop-12 deviation 124 — two helpers, two refusals and the scope plants' own verdicts the spec did not name

**Serves:** deviation TOOL-dDeclaredLoop-12

- **Departs from:** `TOOL-dDeclaredLoop-12@rev-5` [§4 The program check, §4 Inventory]
- **Hand-off:** spec-to-code
- **Before:** `TOOL-dDeclaredLoop-12`'s spec at rev-5 mints `read_items`, `check_program`, `derive_outcome_set`, `read_layer_tags` and `derive_item_scope` in the loop reader, lists what `check_program` refuses, and says the `scope-no-kit` plant exits 0.
- **After:** the reader also carries `read_item_rows`, the array-of-tables read of the item table that `read_outcome_set` already made and `check_program` shares, and `check_scope_plant`, which runs the scope verb under the two scope plants; `check_program` also refuses an item tag declared twice and a row whose `step` is not the step its tag opens; and each scope plant exits 1 with a `loop: refused` line where the scope verb misbehaves, the planted unit listed on any line but its item's, or a line armed with no playbook kit.
- **Cause:** builder discovery
- **Reason:** the needs graph is keyed by tag, so a repeated tag would silently merge two rows, and a step's exit is graded by the row's `step`, which means nothing unless it agrees with the tag; a plant that only prints its lines is an arm nobody reads, so each plant grades its own output as the refusal plants do.
- **Evidence:** the pass commit of `TOOL-dDeclaredLoop-12`, `tools/loop/loop_lib.py#check_program`, `tools/loop/loop_lib.py#check_scope_plant`, and the acceptance ledger `2026-11-14-build-TOOL-dDeclaredLoop-12-1-acceptance-ledger.md`.
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage — the two refusals and the scope plants' verdicts are described in `tools/loop/README.md` and `help/loop.md`
- **Caused-by:** TOOL-dDeclaredLoop-12
