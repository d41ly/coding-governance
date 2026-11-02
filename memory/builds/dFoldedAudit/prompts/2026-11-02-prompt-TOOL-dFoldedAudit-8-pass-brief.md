# Pass brief — TOOL-dFoldedAudit-8: dClosedLoop takes the same rules

**Serves:** research TOOL-dFoldedAudit-8

## The brief

### Goal
Carry out TOOL-dFoldedAudit-8 exactly as its spec's §4 states, at `memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-8.md`. Read that spec whole first; it wins over this brief. Commit nothing and regenerate no index; the main loop does both.

### Items
1. The revision of TOOL-dDeclaredLoop-32, its `**Carries:**` pin moved with the amended clause.
2. The revision of TOOL-dDeclaredLoop-20.
3. The revision of TOOL-dFairHearing-17.
4. The deviation record `memory/builds/dClosedLoop/build/2026-11-01-build-TOOL-dFoldedAudit-8-deviation-81.md`, amending `cl-dClosedLoop-0117`.
5. Before any write, read `bash tools/unattended/unattended.sh --claims` and each of the three specs whole. A build reading `live` is not touched. Edits match on old text, never on a line number; if an old text is gone, stop and report that edit instead of adapting it.
6. Do not edit TOOL-dFoldedAudit-8's own spec; the main loop flips its status.

### Acceptance
The return reports each of the spec's AC1 to AC7 as observed, or as owed to the main loop with the reason. The writes are exactly the four declared paths.

### Gates
`tools/check-spec-tokens.py` and hygiene, run by the main loop after this pass.

### Non-goals
`PLAY-dClosedLoop-1`, dClosedLoop v2, dSafePassage, any landed record, any other spec. Nothing ships to `tools/`.
