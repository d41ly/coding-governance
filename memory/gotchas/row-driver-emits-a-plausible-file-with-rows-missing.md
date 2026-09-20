---
name: row-driver-emits-a-plausible-file-with-rows-missing
description: the backlog row driver never errors on a wrong input order or a two-sided rotation — it emits a well-formed shard with the other side's rows silently gone
kind: class
---

# The row driver emits a plausible file with rows missing

## Symptom

A backlog merge completes, the shard parses, every row it holds has one status token, and rows
that existed on the other side are not in it. Nothing reported a conflict on those rows. Two
distinct triggers, one output shape.

- **Wrong argument order.** `tools/memory-tree/merge-rows.py` takes `%O %A %B` — BASE, OURS,
  THEIRS — and writes into the OURS path. Given the placeholders in another order it does not
  error: BASE is read as a side, a side is read as BASE, and the rows only the mis-cast side added
  read as deletions.
- **Both sides rotated.** Two branches can each rotate `memory/backlog/<FAMILY>.md` into
  `memory/archive/`. The driver sees the other side's rotation as DELETES of every row it moved and
  conflicts, or — when the rotations do not overlap — merges them as deletions.

## Where it bit

The argument-order form is stated behaviour, carried in the kickoff manifest as a trap until this
record: the driver's usage text names all four placeholders and `.gitattributes` spells their order
because nothing downstream can detect a transposition. The two-sided rotation happened on
2026-08-17, when two concurrent builds each rotated the tooling shard; reconciling that pair is the
`TOOL-cSpliceWarden-4` and `TOOL-cSpliceWarden-7` story the shard's own header carries.

## The fix

**Diff the merged id-set against BOTH inputs, never eyeball the output.** For the order form:
every id in OURS and every id in THEIRS is in the merge, or the merge names it as a deliberate
delete. For the rotation form: union the rows, carry BOTH rotation notes in the header, and check
that every id absent from the union sits in some `memory/archive/<FAMILY>.*.md` — a count of 0
absent-and-unarchived ids is the check, and it is a count you compute, not a glance.

No machine gate for either output shape: the driver cannot tell a mis-cast BASE from a real one,
and `tools/memory-tree/merge-rows.test.sh` pins the placeholder usage text and the empty-BASE union
but not a transposed wiring. The documented check is the id-set diff above, run after any merge
that touched a `memory/backlog/` shard.
