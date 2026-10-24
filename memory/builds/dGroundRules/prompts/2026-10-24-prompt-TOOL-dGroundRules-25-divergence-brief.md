**Serves:** research TOOL-dGroundRules-25

# Divergence brief — TOOL-dGroundRules-25, S35's hygiene half and S7's two install-day premises

## The prompt

> Its builder built and probed every finding of TOOL-dGroundRules-25 at HEAD 4298cfcc7, then handed it back as a DIVERGENCE with nothing committed (the work is saved as a patch). Two findings cannot be built as specced. S35/AC35: TOOL-dGroundRules-21 S31 added no no-launcher branch to `tools/memory-tree/check-memory-hygiene.sh`; with no python it still stops at its `resolve_python` line with exit 2, which is no `fail <n>` call or `exit 1` refusal site, so `check-arms.py --report` lists no branch for it and AC35 can never print it armed; the template-size half reaches the existing `fail 5` call, already ARMED, so its arm adds an assertion and moves no floor. S7: on install day `mirror --write` refuses with `uncommitted changes` because `--scaffold` has just written the policy file, so every `govkit apply` of the policy kit exits 1 and `adopter-fresh-target`, `limit-fresh-target-spawn` and arm 4 of `adopt-policy.test.sh` (so `adopter-suite`) read red; TOOL-dGroundRules-31 (order 9, consuming from this unit) is the unit that turns that refusal into a named deferral. And even with the mirror written, the installed `regen.py --check` exits 1 until the memory-tree kit's adopter runs a second time after the first commit, since its first run seeds and stops; re-running it makes regen report 5 of 5 fresh.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-25.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. S35 and AC35: the hygiene half is observed by its own arm asserting the exit-2 no-launcher line by its text, not through `check-arms.py --report`; S35 says TOOL-dGroundRules-21 S31 added no hygiene branch, and that the template-size arm adds an assertion and moves no `ARMS_FLOORS` row. AC35 keeps only what `--report` can print.
2. S7: state that the install-day `mirror --write` refusal stands until TOOL-dGroundRules-31 lands its deferral, and that `adopter-fresh-target`, `limit-fresh-target-spawn` and `adopter-suite` (arm 4 of `adopt-policy.test.sh`) read red on this unit's commit and go green at TOOL-dGroundRules-31; the criteria that observe those cases say they are observed at the close, after TOOL-dGroundRules-31. Folding TOOL-dGroundRules-31's deferral into this unit is refused: it is that unit's whole scope and its spec is audited.
3. S7: name the step in the fresh-target fixture that re-runs the memory-tree kit's adopter after the first commit, so its render check and `gen_build_index --check` are fresh before the installed `regen.py --check` is graded.
4. Re-cite by symbol or current line the three citations the builder found moved: the template predicate (now :80), `extract_files_touched` (now :536) and the check-12 grammar (now :2553), each in the file the spec already names.
5. The status header's rev rises by one, with a §9 line naming the disagreements and the rulings. The spec must stay at or under 48600 bytes measured with `wc -c` including its records region, which grows by about 300 bytes when this handoff is recorded: keep it at or under 48300 before that, trimming prose outside §2 and §6; introduce no retirement word in §2.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); `wc -c` prints at most 48300; every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`; every finding the builder built green.

### Limitations
The builder's probes stand: every other finding was built and probed green or already held at HEAD, and its `--dispatch` re-measure found exactly the one waived `[guards]` hit.

### Reuse
The builder's saved patch is the build; the next dispatch applies it.
