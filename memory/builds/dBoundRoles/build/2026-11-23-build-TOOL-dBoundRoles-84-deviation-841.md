# TOOL-dBoundRoles-84 deviation 841 — the builder's departures from the actor-patch seat spec

**Serves:** deviation TOOL-dBoundRoles-84

- **Departs from:** `TOOL-dBoundRoles-84@rev-1` [S1, S3, S5, §4, AC1, AC2]
- **Hand-off:** spec-to-code
- **Before:** S1 asks that the schema's header comment say what `widens = "changes"` and `ref = "actor"` declare; S3 says `check_item_composition` "adds the seat's refusals" without placing them; §4 "The seat" spells the seat's block reading `op["tag"]`, `op["value"]` and `op["row"]`; S5 names only the "What you may change on gov's items" paragraph of `help/loop.md`; AC1 and AC2 name the seat's `loop: refused` line and are silent on any other refusal the patched row draws.
- **After:** `tools/loop/item-schema.toml` says it twice: a header line under the field list naming `actor` open on `changes` with `ref = "actor"`, and a comment above the `actor` row naming the seat in `tools/loop/loop_items.py#check_actor_patches`. `tools/loop/loop_items.py#check_item_composition` appends the seat's refusals after the record-input join, last of its refusals, and the seat reads each operation through `get`, so an operation lacking a key prints `None` rather than raising. `help/loop.md` also adds the new plants to the "See a refusal" case list and "an actor patch" to the refusals `check` exits 1 on. The plants `patch-actor-repo` and `patch-actor-gov` print, beside the seat's line, the refusal `tools/loop/loop_lib.py#check_item_declarations` already gives a role item whose `allowance` is no `none`, since gov's `item.test.select` keeps its own allowance under a role actor; the selftest rows of `tools/loop/loop_items.py#CASES` match the seat's line by its own needle, so the extra refusal moves no case.
- **Cause:** builder discovery
- **Reason:** the schema's field comments sit beside their rows elsewhere in the file, so the header and the row each carry the part a reader there needs; the seat runs over the payload's operations alone, so its place among the composition's refusals changes no verdict; the help page lists every plant and every refusal class, so a new plant and a new refusal belong in those lists; the allowance refusal is the declarations check judging the composed row as it judges any role item, and the seat's verdict does not depend on it.
- **Evidence:** the build brief `memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-84-build-brief.md` and the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-84-1-acceptance-ledger.md`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value; reported by the `report` value
- **Follow-through:** none
- **Caused-by:** TOOL-dBoundRoles-84
