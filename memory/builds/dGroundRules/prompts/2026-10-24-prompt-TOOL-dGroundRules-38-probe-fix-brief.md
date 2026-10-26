**Serves:** research TOOL-dGroundRules-38

# Probe brief — TOOL-dGroundRules-38 against the built branch, before its builder starts

## The prompt

> A read-only spec review of this spec against HEAD 7106e5abc found: §1 and S3 count an exclude-file read that TOOL-dGroundRules-34 S1 adds, and §10 states TOOL-dGroundRules-34 S28's `--path-format=absolute` flag as present, but neither is at HEAD yet (`build_source_snapshot` copies only the index, with a relative `--git-path`); TOOL-dGroundRules-34 is ordered before this unit and is being rebuilt; and §1 says the sweep runs in a build pass, but deviation-78 moved it to the close's first `policy fixtures` run.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-38.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. §1, S3 and §10 state the exclude-file read and the absolute `--git-path` flag as what the branch holds after TOOL-dGroundRules-34, which builds before this unit, naming that dependency.
2. §1 places the sweep at the close's deviation-78 run, not a build pass.
3. The status header's rev rises by one, with a §9 line naming the disagreements and the rulings. Keep the file under 48600 bytes measured with its records region; every §6 code span stays on one line; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token, and a fixture-relative path carries its target placeholder.

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
