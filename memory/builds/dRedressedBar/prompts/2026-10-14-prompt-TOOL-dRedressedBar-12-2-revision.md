# Revision — dRedressedBar: TOOL-dRedressedBar-12, -14 and -16, the build pass writes no sibling spec

**Serves:** research TOOL-dRedressedBar-12 TOOL-dRedressedBar-14 TOOL-dRedressedBar-16

## The brief

### Goal
Unit 10's builder diverged because its spec put sibling-spec corrections into the build-pass commit. Under `.claude/roles.json` only gov-spec-writer may write spec files, and scratch-guard lets a builder change only its own spec's status and date cells (`tools/hooks/scratch-guard.js:91-99`). So no build pass can commit an edit to another spec. The writer that restructured units 10, 13, 17 and 19 found units 12, 14 and 16 READY with the same defect: their §4 Files touched name spec 11, 11 and 12. Give each of them the shape units 13, 17 and 19 now have (see their latest §9 lines): the sibling-spec edits move to a spec-writer pass at that unit's own turn, before its build, as `<w12>`, `<w14>`, `<w16>`. The build pass writes only product files, the manifest and the ledger, and every criterion that reads the sibling edit reads that spec-writer commit.

### Items
1. **TOOL-dRedressedBar-12, -14 and -16** — each to a new rev with a §9 line naming the moved S-items and criteria. Fold nothing now: their targets are specs whose units have not built.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades units 12, 14 and 16 READY, and none of their §4 build-pass Files touched names a spec file other than its own. No other READY unit in the build does either; check every unit 11 to 19 and say which you checked.

### Gates
`memory hygiene`

### Non-goals
- No code. No status change. No edit to any spec but 12, 14 and 16.
