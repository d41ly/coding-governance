# Build brief — DEPL-dRetiredFork-2

**Serves:** journal DEPL-dRetiredFork-2

## Both defects confirmed before writing anything

**The population is the receipt.** `_cmd_update` builds `rows_all` from `receipt["files"]` and
classifies with `for row in rows_all:`. A gov source with no receipt row is never constructed, never
classified, never counted, never printed — so the verb built to move an adopter forward cannot land
anything gov newly started shipping.

**`--kits` is parsed and discarded.** `cmd_update` takes no `kits` parameter and `main` passes none.
Measured: `update --target <nc> --kits memory-tree` and the same command without the flag produce
**byte-identical output**. A scoped run silently runs unscoped, and nothing says so.

## The severe risk, and why rev-1's gate was wrong

Overwriting a target-owned `seed` file. The destination exists BY DESIGN, gov does not own the
repository, and this verb's whole selling point is that it needs no operator turn.

rev-1 gated on `LANDABLE_ROLES`, which is `tuple(k for k, v in ROLE_KINDS.items() if v == "write")`
— and `ROLE_KINDS` marks BOTH `engine` and `seed` as `"write"`. So that gate admitted `seed`, a role
whose own `UPDATE_ROLE["seed"] = "report-reseed"` says this verb never writes it. **The gate is
`UPDATE_ROLE`'s `table` disposition — engine only.**

`land_through_index` writes unconditionally with no `dp.exists()` check; `_cmd_apply` has the
copy-once guard with its reason beside it. S3b carries that guard across.

**A new `rendered` source must be REPORTED, never written.** Its `kind` is not `write`, so it has no
landable body, and writing it would land an unrendered template. The measured trap is the unattended
kit's `VERBS.template.md`.

## What the numbers should come out as

AC5 wants five currently-invisible additions at NicoCares and a count reconcilable with
`plan --coverage`'s 59-of-142 at inCMS. Those are the spec's figures; the run's are what count, and
where they differ the measurement wins and the difference is recorded.

## F1, ratified

`evidence: "vintage-match"` — literally true the instant the row lands, and it adds no member to a
closed set that is joined to the engine by its own arm. `landed-new` would be a contract change this
unit does not need.

## Not this unit

`--add-kits` (an owner decision, filed elsewhere). Running the kit's adopter — that is
`DEPL-dRetiredFork-3`. And "just run `apply`", which writes every engine destination unconditionally
and runs the kit's `[adopt]`: for an adopter holding a kit deliberately inert that is a posture flip,
and it is how the safe verb stayed unable to add.
