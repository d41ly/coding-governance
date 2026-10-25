**Serves:** research TOOL-dGroundRules-43

# Probe brief — TOOL-dGroundRules-43 against the built branch, before its builder starts

## The prompt

> A read-only spec review of step 14 at HEAD 0860b8c1e found this spec stale against the built branch; the items below are the run's rulings on its findings.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. S5, S8, S11 and S12 are restated as already built (S8 by TOOL-dGroundRules-34 at 75b1ffe59, S11 and S12 by TOOL-dGroundRules-25 at b663756ca, S5 in TOOL-dGroundRules-34 AC26), each with the observation that confirms it; where a criterion's no-`WRONG` half is green before this unit, its staged half is what it observes.
2. S7 and AC7: TOOL-dGroundRules-30 removed the version-staging arm at 93e4b4d31; `OLD_ARM` names the revision `93e4b4d31^`, whose file still holds it.
3. AC3's `EVIDENCE` reads `memory/builds/dGroundRules/README.md` at the cited revision, not the root README.
4. AC6's `ORDER_SHIFT` shifts a unit from a step holding more than one unit, so the count of distinct orders rises.
5. S14 and AC14: TOOL-dGroundRules-34 S21 makes the receipt prefix rule stricter than the deployer's on purpose; S14 states that, names the function it adds, and AC14 asserts the expected agreement on the parity values and the expected disagreement on `a/..` and `x/../y`, calling `demand_contained_dest` with both of its arguments.
6. S15: `resolve_govkit` catches the `LookupError` from `resolve_kit_dir` and raises the `RuntimeError` its callers already catch, so AC15's `WRONG` prints.
7. §1 states the unit's actual order and drops the claim that it is above every unit of the build.
8. AC8, AC9, AC11 and AC12 name that their no-`WRONG` halves also rest on TOOL-dGroundRules-37's dead-guard check, built before this unit.
9. Re-cite every moved line by symbol, not line number.
10. §7 drops any claim that the policy legs do not exist.
11. The status header's rev rises by one, with a §9 line naming the disagreements and the rulings. Keep the file under 48600 bytes measured with its records region; every §6 code span stays on one line; every acceptance bullet keeps a `Red when:` clause, and no note line in §6 starts with `AC<n>`; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token; an untracked or fixture-relative path sits inside a fenced block or carries its target placeholder; every command a criterion runs is spelled so it runs from the repository root.

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
