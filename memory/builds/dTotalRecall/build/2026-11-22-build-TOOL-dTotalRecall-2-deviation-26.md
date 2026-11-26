# TOOL-dTotalRecall-2 deviation 26 — the names, the shared claim call and the rules the record door needed beside its inventory

**Serves:** deviation TOOL-dTotalRecall-2

- **Departs from:** `TOOL-dTotalRecall-2@rev-13` [§2 S2, S4, S5, S6; §4 "Minting", "Inventory"; §6 AC4, AC7]
- **Hand-off:** spec-to-code
- **Before:** §4 "Inventory" mints `write_new_record`, `derive_content_key`, `check_mint_authority` and `check_typed_record` in `build_records.py`, `read_lease_class` and `read_claim_lines`; S5 keys a record by its field values in schema order; §4 "Minting" names the counter `gov-claim.sh ask <FAMILY> <slug>` without saying where `<FAMILY>` comes from, and the claim rung compares a claim's `session` with this session's without naming a session the harness exposes none of; AC4 and AC7 run in a scratch clone of the pass tip.
- **After:** beside the minted names the pass adds `tools/memory-tree/build_records.py#read_kind_row` (the row read and its door refusal, S2), `#DOOR_WRITER` and `#SEQ_RULE`, and a `check(rel, text)` argument on `#write_record` run over the exact bytes before the file opens (S4); `tools/memory-tree/gen_build_index.py#run_claim_cli`, extracted from `#write_slug_claim`, which the counter mint shares. The content key hashes each field as `Key: value`, the row's fields first in schema order, then the rest in file order. A `<FAMILY>-<slug>-<seq>` rule takes its family from `--unit`'s prefix and its slug from `--build`. A claim `session: absent` admits a caller whose session is also absent. A loop kit that does not resolve beside the unattended kit prints `unarmed — no loop kit` and reads the claim. `--name` on a minting row, and an id-rule placeholder outside a typed kind and the counter shape, are refused. The suite's arms seed a minimal repository rather than a clone of the pass tip, AC4's spec planted there.
- **Cause:** builder discovery
- **Reason:** a constant, a row reader and a shared claim call each need a name, and a second caller of the claim CLI is a factory, never a copy; a key name hashed beside its value keeps one value from matching under another field; the spec names the counter and no family source; no row at HEAD needs a placeholder the door does not mint, so minting one would invent a second minter; a full clone of the tree renders the whole tree in every arm.
- **Evidence:** the pass commit of TOOL-dTotalRecall-2 and its acceptance ledger, `2026-11-22-build-TOOL-dTotalRecall-2-2-acceptance-ledger.md`
- **Risk:** additive
- **Approver:** author, under the build's `author-recorded` value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-2
