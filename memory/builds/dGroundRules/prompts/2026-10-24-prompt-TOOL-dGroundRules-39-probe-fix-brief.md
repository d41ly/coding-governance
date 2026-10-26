**Serves:** research TOOL-dGroundRules-39

# Probe brief — TOOL-dGroundRules-39 against the built branch, before its builder starts

## The prompt

> A read-only spec review at HEAD 74d17b3a0 found: §4's citations into TOOL-dGroundRules-34 drifted (that spec is at rev-9); S2/AC4 is already built by TOOL-dGroundRules-29 (b8b4f0815), since `derive_census_tree` refuses two candidates and `arm_cap_census` turns it into one finding naming both, so AC4 is green before the build; S1 and the §4 pseudo-code expect `derive_census_tree` to answer `source` at the govkit directory, but it returns the tool root (`tools`); the search AC2 stages is the copy in `tools/policy/check_policy.py` `derive_census_tree`, not the one §4 cites in `tools/govkit/govkit.py`; §3's `census-ambiguous-registry` exists only once TOOL-dGroundRules-34 is built; and §7 says the policy legs do not exist at this spec's base, though both exist since TOOL-dGroundRules-1.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-39.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. Cite TOOL-dGroundRules-34's criteria by AC id, not line.
2. S2/AC4 are restated as already built by TOOL-dGroundRules-29, with the observation that confirms it; if this unit still owes anything there, say what.
3. S1 and the §4 pseudo-code expect the tool root `tools`, the value `derive_census_tree` returns.
4. AC2's staged break (`DEPTH3_LIVE`, `TOPLEVEL`) stages the search in `tools/policy/check_policy.py` `derive_census_tree`.
5. §3 names `census-ambiguous-registry` as TOOL-dGroundRules-34's, built before this unit.
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
