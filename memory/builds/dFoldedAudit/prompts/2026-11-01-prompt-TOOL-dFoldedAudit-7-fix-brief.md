# Fix brief — TOOL-dFoldedAudit-7: fixture K and the reader's untested rows

**Serves:** research TOOL-dFoldedAudit-7

## The brief

### Goal
Revise TOOL-dFoldedAudit-7 so its builder can observe AC2 and AC3, as its DIVERGENCE return asked. Its return is `build/2026-11-01-build-TOOL-dFoldedAudit-7-2-stopped-dispatches.md` plus this brief. Commit nothing; the main loop commits.

### Items
1. §6's fixture K must also hold `tools/policy/budgets.py`. `validate` runs whenever a policy file is committed and does `import budgets` at `tools/policy/policy.py:599`, so on K as written AC2 and AC3 print a traceback. The builder ran the whole probe with K plus that one file; `tools/policy/caps.toml` is not needed, and "Fixture N is K without `tools/policy/`" stays correct.
2. §4's reader rows for a closed-set value and for a bad argument have no criterion and no `New arm:` line. Add one criterion and one `New arm:` for them.
3. State in §4 or §7 the two-commit shape the precedent `d7e8a027a` uses: the mirror goes second under its own `--dispatch` with its own `Pass:` trailer, and that second commit carries the CLOSED flip with README and LIVE.md re-rendered.

### Acceptance
TOOL-dFoldedAudit-7 carries a rev bump and a §9 line, and its status cell stays INPROGRESS.

### Gates
`tools/check-spec-tokens.py`, run by the main loop after this pass.

### Non-goals
No §4 design change beyond item 3, no code, no write outside this one spec.
