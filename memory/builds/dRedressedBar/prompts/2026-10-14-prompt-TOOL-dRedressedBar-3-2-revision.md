# Revision — dRedressedBar: TOOL-dRedressedBar-3 rev-2, F1 resolved by the owner

**Serves:** research TOOL-dRedressedBar-3

## The brief

### Goal
The owner resolved §7 F1 as option (c), 2026-10-14: scope the two `[-8]` arms with
`--kits check-wiring`, and fix the update defect S5 names in a new product unit,
`TOOL-dRedressedBar-9`, rather than recording it as a finding. Revise this spec to rev-2. Mark F1
`RESOLVED (owner, 2026-10-14): (c)` in place. S4 scopes only the `[-8]` arms' writing updates (the
`d8-ac1` and `d8-ac4` fixtures). The other three arms, `and re-stamps the receipt at the new commit`
and `[-12] AC4/AC9 NEGATIVE`, stay unscoped so they witness unit 9's fix. S5 stops being a finding
and points at unit 9. The unit's order moves after unit 9's, and its acceptance for those three arms
reads green only over unit 9's fix. Add the §8 revision line naming what moved.

### Items
1. Revise `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-3.md` to rev-2 as the
   goal states. Its §3 non-goal "No edit to `tools/govkit/govkit.py`…" stays true for THIS unit,
   because unit 9 owns that edit. Its Edges gain `depends-on TOOL-dRedressedBar-9`.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades TOOL-dRedressedBar-3 READY,
not FORKED. The spec's S4 and AC4 name exactly the `[-8]` writing calls as scoped.

### Gates
`govkit selftest` · `memory hygiene`

### Non-goals
- No code. No edit to unit 9's spec, which a sibling writer is authoring concurrently.

### Limitations
- Children run no bar and no whole suite.

### Reuse
The spec's own §4 S4 and S5 analysis, unchanged where the resolution does not move it.
