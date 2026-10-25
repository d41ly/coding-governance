**Serves:** research TOOL-dGroundRules-52

# Probe brief — TOOL-dGroundRules-52 against the built branch, before its builder starts

## The prompt

> A read-only spec review of steps 15 to 20 at HEAD e1c7051cb found this spec stale against the built branch; the items below are the run's rulings on its findings.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-52.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. §1: drop the claim that order 16 sits above every unit; state its actual order.
2. S1, S5's AC3 half and S10 (findings 3, 12, 25) are restated as closed by TOOL-dGroundRules-43 rev-5 (6e8863f43), whose `EVIDENCE` reads the build README whole; S7 and S17 (findings 14 and 7) as closed by -43 rev-5's `ORDER_SHIFT` (AC6).
3. S4 and AC4: `derive_parallel_step` is built by TOOL-dGroundRules-25 (b663756ca) in `tools/memory-tree/gen_build_index.py`, and the steps hold more than two units; restate the edge and the criterion, or drop them if nothing remains.
4. S6 and AC6: `derive_guardable_reads` already sends bytes (TOOL-dGroundRules-36, cc4b4e53b); the unbuilt parts are `-z`, `fsencode` and the matched count, and AC6 observes those.
5. S8 and S23 are built (`os.fsdecode` in `check_guard_trace`'s helper, TOOL-dGroundRules-33, eb67e2cc8); S25's suppress half is built (TOOL-dGroundRules-35, 764a8a282) and only the `unmapped` line is new; the module set is `SOURCE_READS` and `kept` is a local of `check_guard_trace`.
6. S9: `check_guard_lines` is built (7a600abf5), called by `run_fixture`, and TOOL-dGroundRules-43 rev-5 AC8, AC9, AC11 and AC12 rest on it; S9 keeps it and takes out no part of it, and its Readers line names `run_fixture`.
7. S13 and AC11 observe through TOOL-dGroundRules-41's `INSTALL_LINES` and `HELP_LEGS` (rev-4, built at 277c9e37f); -48 rev-2 defines no `INSTALL_LINES_WHOLE`; update the consumes-from edges to name -41.
8. S21: `check_writes_intersect` is already graded by TOOL-dGroundRules-40's arm over `OVERLAP_PAIRS`; restate what this unit adds, if anything.
9. AC5: -43 rev-5 AC1 observes through TOOL-dGroundRules-40's `PAIRS_PY`/`PAIRS_SH`; AC5 names those, or -45's `PAIRS_TABLE` only with the precondition that -45 is built.
10. Every staging into `build_fresh_target` (`PLANT_TWO`, `PLANT_NONASCII`, `PLANT_BYTES`, `PLANT_REFUSED`) names `run_fresh_target`, the case runner in `tools/policy/check_policy.py`.
11. S18 and AC15: the deny branch is built by TOOL-dGroundRules-38 (8b50fc8bb); `NO_GIT` staging targets `policy.run_git` callers, so restate AC15 as green before this unit or drop it.
12. Every bare `check_policy.py` in a literal (`GUARD_LINES_GONE`, `PREFIXED`, `COLD_WRITING`, AC3, AC10) is spelled `tools/policy/check_policy.py`, and the §6 preamble's claim about -43 is restated.
13. Units 1 to 41 are built (HEAD 8eab342e0); TOOL-dGroundRules-51, -53, -54, -57, -58 and -59 are retired WONTDO, so no criterion may consume a literal of theirs.
14. Re-cite every moved line by symbol or AC id, not line number.
15. Drop any claim that the policy legs or `tools/policy/check_policy.py` do not exist or cannot run; `policy fixtures` is a leg in `tools/gate-legs.json`.
16. The status header's rev rises by one, with a revision-log line (§9 in a Tier-2 spec, §8 in a Tier-1 one) naming the disagreements and the rulings. Keep the file under 48600 bytes measured with its records region; every acceptance-section code span stays on one line; every acceptance bullet keeps a `Red when:` clause, and no line in the acceptance section starts at column 0 with `AC<n>`, wrapped prose included; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token; an untracked or fixture-relative path sits inside a fenced block or carries its target placeholder; every command a criterion runs is spelled so it runs from the repository root; a criterion that is green before this unit is restated as such, with the staged break or later observation that can red.

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
