# Revision — dRedressedBar: TOOL-dRedressedBar-10 rev-2, F1 resolved by the owner

**Serves:** research TOOL-dRedressedBar-10

## The brief

### Goal
The owner resolved §8 F1 as option (c), 2026-10-14. This unit keeps S22 as option (a) states it:
the second `must_not_exist` term, the matrix row, AC15, AC16, AC17 and the §7 arm. It does not
state the receipt-homed residual as accepted, because the receipt-reading probe term that closes it
is a new unit, `TOOL-dRedressedBar-11`, added by the owner rather than held in this minors batch
(M2, M4). Revise this spec to rev-2. Mark F1 `RESOLVED (owner, 2026-10-14): (c)` in place, and point
S22's residual at unit 11. Add an Edges line `hands-off` to `TOOL-dRedressedBar-11` for the residual,
and a §9 revision line naming what moved.

### Items
1. Revise `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md` to rev-2 as the
   goal states. Nothing else in the spec moves.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades TOOL-dRedressedBar-10
READY, not FORKED.

### Gates
`govkit selftest` · `govkit acceptance matrix` · `memory hygiene`

### Non-goals
- No code. No edit to unit 11's spec, which a sibling writer is authoring concurrently.

### Limitations
- Children run no bar and no whole suite.

### Reuse
The spec's own S22 as option (a) states it.
