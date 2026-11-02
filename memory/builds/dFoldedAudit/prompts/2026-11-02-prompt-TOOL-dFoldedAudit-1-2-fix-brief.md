# Fix brief — TOOL-dFoldedAudit-1: the decision row lands first

**Serves:** research TOOL-dFoldedAudit-1

## The brief

### Goal
Record that this unit's decision row landed before its pass. `memory/DECISIONS.md` is a shared record `--dispatch` refuses, so no pass commit can carry it. The stopped builder's return is `build/2026-11-02-build-TOOL-dFoldedAudit-1-9-stopped-dispatch.md`. Commit nothing; the main loop commits.

### Items
1. §4 "The ceiling": term 4 of `tools/template-size-limits.txt` is met by "before", not "with". The row landed in its own `Pass: none` records commit ahead of the pass commit, written by the main loop. Its text is byte-identical to §4's fence.
2. §4 Files touched: mark `memory/DECISIONS.md` as "its own `Pass: none` records commit, already landed", out of the pass's write set, as TOOL-dTrueNorth-27 rev-2 did.
3. S10 and §4 "The decision row": say the main loop wrote it, and the builder writes nothing to that file.
4. AC10 stands as written and the builder observes it.
5. AC7's `adopt-unattended.sh --check` and AC12's `adopt-roles.sh --check` are legs only the main loop can run. Mark those two clauses as owed to the close, so the builder does not attempt them.

### Acceptance
TOOL-dFoldedAudit-1 carries a rev bump and a §9 line, its status cell stays INPROGRESS, and `memory/DECISIONS.md` leaves the write set.

### Gates
`tools/check-spec-tokens.py`, run by the main loop after this pass.

### Non-goals
No change to M4's target text or to the row's text, no code, no write outside this one spec.
