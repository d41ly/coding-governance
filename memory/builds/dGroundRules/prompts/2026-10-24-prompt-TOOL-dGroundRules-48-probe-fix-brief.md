**Serves:** research TOOL-dGroundRules-48

# Probe brief — TOOL-dGroundRules-48 against the built branch, before its builder starts

## The prompt

> A read-only spec review of step 14 at HEAD 0860b8c1e found this spec stale against the built branch; the items below are the run's rulings on its findings.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-48.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. S1 is restated: TOOL-dGroundRules-41 rev-4's `INSTALL_LINES` already spells `help/policy.md` whole, so this unit observes through it and adds no second command; the unit writes no product code beyond what S2 needs, and says so.
2. §4 restates that `help/policy.md` is tracked at HEAD.
3. AC1 is stated as green before this unit, with AC2's `HELP_MOVED` break the observation that can red.
4. Re-cite every moved line by symbol, not line number.
5. The status header's rev rises by one, with a §9 line naming the disagreements and the rulings. Keep the file under 48600 bytes measured with its records region; every §6 code span stays on one line; every acceptance bullet keeps a `Red when:` clause, and no note line in §6 starts with `AC<n>`; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token; an untracked or fixture-relative path sits inside a fenced block or carries its target placeholder; every command a criterion runs is spelled so it runs from the repository root.

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
