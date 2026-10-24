**Serves:** research TOOL-dGroundRules-36

# Probe brief — TOOL-dGroundRules-36 against the built branch, before its builder starts

## The prompt

> A read-only spec review of this spec against HEAD 7106e5abc found: the `PLANT_IGNORED` staging target `build_fresh_target` does not exist (TOOL-dGroundRules-32 kept the one builder `build_install_target(name, ids)`); after TOOL-dGroundRules-35 (764a8a282) maps every `__pycache__` `.pyc` read back to its `.py`, a normal run keeps no git-ignored path, so the unit guards a class rather than a live defect and AC3's count is normally 0; TOOL-dGroundRules-33's S4 sweep was moved to the close's first `policy fixtures` run by deviation-78, so no unit-33 sweep remains for S3 to narrow; `print_legs_for` and its all-untracked refusal moved in `tools/check-spec-tokens.py`; the built trace pipe is `read_legs_for(top, checker, kept)` called from `check_guard_trace`, not a new subprocess call; and the `(not tracked at HEAD)` header parse already exists in `read_legs_for`, from TOOL-dGroundRules-25 (b663756ca), not TOOL-dGroundRules-43.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-36.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. Stage `PLANT_IGNORED`'s `open()` into `build_install_target`.
2. §1 restates the premise on the branch after TOOL-dGroundRules-35: a normal run keeps no ignored path, and the unit guards the class; AC3's planted read is its red, and its count is normally 0.
3. S3 and §1 bind the population rule to the close's deviation-78 sweep, not a unit-33 sweep.
4. §4's design feeds the guardable set to `read_legs_for`; describe no new subprocess call.
5. Credit the `(not tracked at HEAD)` parse to TOOL-dGroundRules-25 as already built.
6. Re-cite `print_legs_for` and its refusal by symbol.
7. AC3's no-`WRONG` observation is stated as observed at the close, after the deviation-78 sweep and TOOL-dGroundRules-38.
8. The status header's rev rises by one, with a §9 line naming the disagreements and the rulings. Keep the file under 48600 bytes measured with its records region; every §6 code span stays on one line; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token, and a fixture-relative path carries its target placeholder.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
The probe read HEAD 7106e5abc through `git show`; TOOL-dGroundRules-34 is being revised and rebuilt meanwhile and builds before this unit.

### Reuse
The probe record `memory/builds/dGroundRules/prompts/2026-10-24-prompt-TOOL-dGroundRules-36-1-spec-reviewer.md`'s run, quoted in the prompt above.
