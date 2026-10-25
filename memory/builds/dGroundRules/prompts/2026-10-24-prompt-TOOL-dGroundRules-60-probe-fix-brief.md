**Serves:** research TOOL-dGroundRules-60

# Probe brief — TOOL-dGroundRules-60 against the built branch, before its builder starts

## The prompt

> A read-only spec review of steps 15 to 20 at HEAD e1c7051cb found this spec stale against the built branch; the items below are the run's rulings on its findings.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-60.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. AC1 is the same observation as TOOL-dGroundRules-52 AC5 and -45 rev-3 AC2: drop it and its S-item, recording the ruling.
2. AC2 is kept, re-pointed at TOOL-dGroundRules-45's `PAIRS_TABLE` (TOOL-dGroundRules-58 is retired); under `PY_RAW` its disjoint line reads `tools/policy tools/policy-x.py disjoint True 1`.
3. The disjoint row is `policy` against `policy-x.py`, relative to `PFX`, owned by TOOL-dGroundRules-40 S1; restate §4 and §5.
4. Cite TOOL-dGroundRules-52's items by S and AC id.
5. Units 1 to 41 are built (HEAD 8eab342e0); TOOL-dGroundRules-51, -53, -54, -57, -58 and -59 are retired WONTDO, so no criterion may consume a literal of theirs.
6. Re-cite every moved line by symbol or AC id, not line number.
7. The status header's rev rises by one, with a revision-log line (§9 in a Tier-2 spec, §8 in a Tier-1 one) naming the disagreements and the rulings. Keep the file under 48600 bytes measured with its records region; every acceptance-section code span stays on one line; every acceptance bullet keeps a `Red when:` clause, and no line in the acceptance section starts at column 0 with `AC<n>`, wrapped prose included; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token; an untracked or fixture-relative path sits inside a fenced block or carries its target placeholder; every command a criterion runs is spelled so it runs from the repository root; a criterion that is green before this unit is restated as such, with the staged break or later observation that can red.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); every `**Carries:**`/`**Derived:**` line, the H1 and the RESOLVED marks of the open-questions section survive; every acceptance-section code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
The probe read HEAD e1c7051cb with read-only probes; TOOL-dGroundRules-41 (277c9e37f) and the retirements (8eab342e0) landed since.

### Reuse
The steps 15 to 20 probe records `2026-10-24-prompt-TOOL-dGroundRules-51-1-spec-reviewer.md`, `-53-1-spec-reviewer.md`, `-55-1-spec-reviewer.md` and `-63-1-spec-reviewer.md`.
