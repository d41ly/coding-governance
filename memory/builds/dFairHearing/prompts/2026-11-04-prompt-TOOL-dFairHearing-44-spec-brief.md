# Spec brief — TOOL-dFairHearing-44: finding 5's docstrings, the closing review's second batch unit

**Serves:** research TOOL-dFairHearing-44

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Write the spec for `TOOL-dFairHearing-44` at `memory/builds/dFairHearing/spec/2026-11-04-spec-TOOL-dFairHearing-44.md`. It carries one finding of the closing diff review, `memory/builds/dFairHearing/reviews/2026-11-04-review-TOOL-dFairHearing-1-40-diff-review.md`, id 5: `check_ungated` has no caller outside its selftest. The review's severity rule batches the minors into one unit, or two across disjoint write sets. Unit 43's dispatch refused `tools/memory-tree/gotchas.py` beside its generated `memory/gotchas/INDEX.md`, so this finding is the second batch unit. Commit nothing; the main loop commits.

### Items
1. Carry unit 43 rev-2's S8 and AC8 as this spec's scope and criterion, re-grounded on today's tree. `check_ungated` stays, because unit 30's committed instrument calls it and unit 40's AC17 runs that instrument; only the docstrings are corrected.
2. The write set is `tools/memory-tree/gotchas.py` and this unit's ledger, with the renders a hook forces. It declares no `memory/gotchas/INDEX.md`. Say in the design why the map's `symbols.json` does or does not move.
3. Write the unit's departure record the way `memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-43-deviation-431.md` was written.
4. Header: order 29, no ask clause, the way unit 43's header reads and for the reason its design states.
5. Every criterion must be one a correct build can pass on today's tree. Check the acceptance section's backticked words against `tools/check-spec-tokens.py`'s `BAR` pattern (lines 419 to 424). Every change-log line names a section, a scope id or an acceptance id. New text cites no check, section or method rule by a bare number.

### Acceptance
A spec conforming to `memory/TEMPLATE-SPEC.md`, its criterion red on today's code and green on a correct build, and its departure record beside it.

### Gates
None you run.

### Non-goals
No code, and no other spec.
