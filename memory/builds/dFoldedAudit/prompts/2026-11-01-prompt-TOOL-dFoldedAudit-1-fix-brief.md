# Fix brief — TOOL-dFoldedAudit-1: one more carrier

**Serves:** research TOOL-dFoldedAudit-1

## The brief

### Goal
Give TOOL-dFoldedAudit-1 the one carrier unit 6 left short, so its builder can write it under a Scope line. The stopped builder's return is `build/2026-11-02-build-TOOL-dFoldedAudit-1-7-stopped-dispatch.md`. Commit nothing; the main loop commits.

### Items
1. Add a new Scope line S14 stating unit 6's exemption as built: a revision whose §9 entry cites a spec-audit record of its build naming the unit joins neither revision arm and owes no record, and a move with no such citation is still reported. Read `tools/memory-tree/design_lib.py`, `tools/memory-tree/deviation_join.py` and its `check_audit_fold` for the shipped wording; do not trust unit 6's spec where the code differs.
2. Add `tools/memory-tree/README.md` to §4's Files touched, and one acceptance criterion that observes `tools/memory-tree/README.md:27` naming the cited fold.
3. §3's sentence that `coding-governance-agents.template.md` and `memory/HYGIENE.md` state no M4 rule stays exactly as written.

### Acceptance
TOOL-dFoldedAudit-1 carries a rev bump and a §9 line, its status cell stays INPROGRESS, and every new line has an observation.

### Gates
`tools/check-spec-tokens.py`, run by the main loop after this pass.

### Non-goals
No change to M4's target text, no change to `memory/HYGIENE.md`, no code, no write outside this one spec.
