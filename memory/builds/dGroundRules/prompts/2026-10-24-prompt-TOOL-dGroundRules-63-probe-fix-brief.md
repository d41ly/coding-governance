**Serves:** research TOOL-dGroundRules-63

# Probe brief — TOOL-dGroundRules-63 against the built branch, before its builder starts

## The prompt

> A read-only spec review of steps 15 to 20 at HEAD e1c7051cb found this spec stale against the built branch; the items below are the run's rulings on its findings.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-63.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. S1 and S2: TOOL-dGroundRules-46 rev-3 (6e8863f43) already re-measured its population (12 operands in 10 specs, one bare, unit 34's) and widened `SOURCE_CMD` to a backtick-led command; restate S1 and S2 as done there, and drop or replace AC2 so no criterion is green before this unit.
2. S3 and AC3: only unit 34, which is CLOSED, carries a bare operand at HEAD; restate the premise and the Red when.
3. The id range `TOOL-dGroundRules-65 to TOOL-dGroundRules-52` is backwards: name the promoted units as TOOL-dGroundRules-65 plus -14 to -52, and spell `ROSTER_JOIN` so it expands that set.
4. AC5 and AC7 read dGroundRules' packet, which is red at HEAD (`packet.py --check dGroundRules`); state that they are observed after the main loop re-renders this build's packet, a close step taken before this unit builds.
5. §4: the live-run line lists dGroundRules `BUILDING` and dFairHearing, dSafePassage and dTrueNorth `LANDING`; cite `read_landed_derivation` by symbol.
6. §7 adds `policy fixtures`, whose guard holds `tools/check-spec-tokens.py` since TOOL-dGroundRules-20.
7. Units 1 to 41 are built (HEAD 8eab342e0); TOOL-dGroundRules-51, -53, -54, -57, -58 and -59 are retired WONTDO, so no criterion may consume a literal of theirs.
8. Re-cite every moved line by symbol or AC id, not line number.
9. The status header's rev rises by one, with a revision-log line (§9 in a Tier-2 spec, §8 in a Tier-1 one) naming the disagreements and the rulings. Keep the file under 48600 bytes measured with its records region; every acceptance-section code span stays on one line; every acceptance bullet keeps a `Red when:` clause, and no line in the acceptance section starts at column 0 with `AC<n>`, wrapped prose included; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token; an untracked or fixture-relative path sits inside a fenced block or carries its target placeholder; every command a criterion runs is spelled so it runs from the repository root; a criterion that is green before this unit is restated as such, with the staged break or later observation that can red.

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
