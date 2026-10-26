**Serves:** research TOOL-dGroundRules-41

# Probe brief — TOOL-dGroundRules-41 against the built branch, before its builder starts

## The prompt

> A read-only spec review at HEAD 74d17b3a0 found: AC4's `INSTALL_LINES` and AC5's `HELP_LEGS` spell a bare `policy.md`, so they fail from the repository root; S3/AC4 is already built (the `## Install` heading and the deferral line are in `help/policy.md`, from TOOL-dGroundRules-1 and TOOL-dGroundRules-31), so AC4 cannot fail; `run_fresh_target` checks only the substring `mirror deferred` in its output and never captures the printed line, which `tools/policy/adopt-policy.sh` prints, so S1 must extract it; §4's citations into TOOL-dGroundRules-34 drifted; AC1 to AC3 can red or print `WRONG` for reasons unrelated to the parity until TOOL-dGroundRules-34 lands, since a refused apply stops the case; and §7 says the policy legs do not exist, though both exist since TOOL-dGroundRules-1. S2's guard line for `help/policy.md` is unbuilt and conflicts with no other build's spec.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-41.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. AC4 and AC5 spell `help/policy.md` whole.
2. S3/AC4 are restated as already built (TOOL-dGroundRules-1 and -31), with the observation that confirms it.
3. S1 extracts the deferral line from the scaffold's output itself, naming where `adopt-policy.sh` prints it.
4. AC2 and AC3 require their `WRONG` to name `help/policy.md` and the printed line, so an unrelated refusal cannot pass for them.
5. Cite TOOL-dGroundRules-34's criteria by AC id, not line.
6. §7 drops the claim that the policy legs do not exist.
7. The status header's rev rises by one, with a §9 line naming the disagreements and the rulings. Keep the file under 48600 bytes measured with its records region; every §6 code span stays on one line; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token, and an untracked or fixture-relative path sits inside a fenced block or carries its target placeholder.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
The probe read HEAD 74d17b3a0; TOOL-dGroundRules-34 builds before this unit and was uncommitted while it ran.

### Reuse
The probe record `memory/builds/dGroundRules/prompts/2026-10-24-prompt-TOOL-dGroundRules-39-1-spec-reviewer.md`'s run.
