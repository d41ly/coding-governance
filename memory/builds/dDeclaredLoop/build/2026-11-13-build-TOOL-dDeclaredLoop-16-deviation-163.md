# TOOL-dDeclaredLoop-16 deviation 163 — helper names beside the spec's inventory, and two refusals it does not state

**Serves:** deviation TOOL-dDeclaredLoop-16

- **Departs from:** `TOOL-dDeclaredLoop-16@rev-4` [§4 "### Inventory"]
- **Hand-off:** spec-to-code
- **Before:** `TOOL-dDeclaredLoop-16`'s spec at rev-4 mints `read_dispositions`, `resolve_disposition`, `read_outcome_set` and `check_disposition_record` in `loop_lib.py`, and `write_disposition` and `read_disposition` in `build_records.py`; `read_outcome_set` has three answers, the set, the row's own list and `None`; the door refuses a value outside the kind's shapes and the closed `Channel` set.
- **After:** `loop_lib.py` also defines the constants `SEG`, the one-word shape, and `OUTCOMES_REF`, the word `dispositions` an item row's `outcomes` may hold; `build_records.py` also defines `SEG`, which `TAG` is now composed from, `DISPOSITION_CHANNELS` and `check_disposition_fields`, the kind's field rules shared by the reader and the writer. `read_outcome_set` raises `LoopError` for an `item` table that is no array of tables and for a row found whose `outcomes` is neither the reference nor a non-empty list of words. `write_disposition` refuses an empty `--reason` where one is given.
- **Cause:** builder discovery
- **Reason:** the reader and the writer of the kind grade the same two shapes, so one function holds them, as each landed kind has its own; a declared item row with no readable outcome set answered as `None` would print `unarmed` for a broken row, and answered as a list would grade against nothing; every landed door refuses an empty text flag. The lexicon answered OK for `check_disposition_fields` on 2026-11-13.
- **Evidence:** `tools/loop/loop_lib.py#read_outcome_set`, `tools/memory-tree/build_records.py#check_disposition_fields` and `tools/memory-tree/build_records.py#write_disposition` at the pass commit of `TOOL-dDeclaredLoop-16`.
- **Risk:** stricter
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** TOOL-dDeclaredLoop-16
