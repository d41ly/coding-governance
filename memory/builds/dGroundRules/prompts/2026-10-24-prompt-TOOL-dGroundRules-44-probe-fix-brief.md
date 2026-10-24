**Serves:** research TOOL-dGroundRules-44

# Probe brief — TOOL-dGroundRules-44 against the built branch, before its builder starts

## The prompt

> A read-only spec review of step 14 at HEAD 0860b8c1e found this spec stale against the built branch; the items below are the run's rulings on its findings.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-44.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. S1 and S3 are restated as already done by TOOL-dGroundRules-40 rev-4 (the disjoint row is the string-prefix trap `policy` against `policy-x.py`, `PFX`-relative, and its AC3 observes it under `RAW_BOTH`); S2, the row check, is what remains.
2. Any row this unit names is spelled relative to `PFX`, as TOOL-dGroundRules-40 S1 requires; the suite never spells a literal prefix.
3. `TRAP_PROBE` filters TOOL-dGroundRules-40's row spelling, so AC1 sees the row and AC3 can show the planted not-a-trap row.
4. `TRAP_SH` sources `tools/unattended/lib-unattended.sh` and names whole paths.
5. Cite `check_guard_trips` in `tools/memory-tree/design_lib.py`.
6. §3 states that TOOL-dGroundRules-32 is built (the arm exists).
7. Re-cite every moved line by symbol, not line number.
8. The status header's rev rises by one, with a §9 line naming the disagreements and the rulings. Keep the file under 48600 bytes measured with its records region; every §6 code span stays on one line; every acceptance bullet keeps a `Red when:` clause, and no note line in §6 starts with `AC<n>`; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token; an untracked or fixture-relative path sits inside a fenced block or carries its target placeholder; every command a criterion runs is spelled so it runs from the repository root.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
The probe read HEAD 0860b8c1e with `git show`; TOOL-dGroundRules-37 was uncommitted while it ran and builds before this unit.

### Reuse
The step-14 probe records `2026-10-24-prompt-TOOL-dGroundRules-43-1-spec-reviewer.md` and `-47-1-spec-reviewer.md`.
