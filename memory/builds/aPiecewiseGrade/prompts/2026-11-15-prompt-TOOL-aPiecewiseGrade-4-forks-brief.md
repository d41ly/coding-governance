# Revision — aPiecewiseGrade: the owner's answer to the promotion fork, and TOOL-aPiecewiseGrade-4

**Serves:** research TOOL-aPiecewiseGrade-4 TOOL-aPiecewiseGrade-2

## The prompt

> (c) New unit on unit 1

The owner's answer, 2026-11-15, to the question the session's question tool put after TOOL-aPiecewiseGrade-2's builder diverged, recorded in `2026-11-15-prompt-TOOL-aPiecewiseGrade-2-revision`: "How should unit 2 promote?", with options (b) copy with no rename, (a) raise the shrink-only temp-name registry, and (c) a new unit that changes unit 1's contract.

## The brief

### Goal
TOOL-aPiecewiseGrade-1 is CLOSED and frozen, and its contract has the checker write the next cache generation to the fixed name `<dir>.next` for the caller to rename into place. That rename is a fixed-name temp renamed into place, which the `shell hygiene (a fixed-name temp renamed into place)` leg refuses, and its registry may only shrink. A new unit, TOOL-aPiecewiseGrade-4, changes the checker's contract so the driver can promote a generation with no fixed-name temp. TOOL-aPiecewiseGrade-2 then builds on that contract.

### Items
1. Write `memory/builds/aPiecewiseGrade/spec/2026-11-15-spec-TOOL-aPiecewiseGrade-4.md`, status SPECCED, rev-1, node a, base `aebbb4a72`, streams tooling, order 3, Tier-2, in the shape `memory/TEMPLATE-SPEC.md` states. Its mechanism changes where `tools/check-spec-tokens.py`'s `SPEC_TOKENS_CACHE` mode writes its next generation so that the caller's promotion passes `tools/gate-lint/sh_hygiene.py`'s `scan_temp_file` with no registry row. Read the cache contract at HEAD (the header docstring's `SPEC_TOKENS_CACHE` paragraph, `read_spec_cache`, `write_spec_cache` and where `main` arms them) and `scan_temp_file` with its fixture table before choosing.
2. Weigh at least two mechanisms by what would make each lose, as `doc.build-method#m12-research-test-choose-when-the-solution-is-not-given` states. Candidates: the caller names the next generation's directory, made with `mktemp -d` under the sidecar root, through a second environment variable, so the rename's source is a `$(mktemp` binding the lint follows; or the checker promotes its own generation in Python with `os.replace`, the driver telling it whether to keep the result. State for each what the lint, the tree-moved bracket of TOOL-aLightenedLoop-3 S6, and a run killed mid-write each do to it. A choice the code does not decide is a fork in §8 with a recommendation.
3. Every behaviour TOOL-aPiecewiseGrade-1 built that this unit does not change keeps its bytes: the plain run, `--spec`, `--pass-spec`, `--list`, the `SPEC_TOKENS_INPUTS` record, the per-spec key and the differential arm's steps. The unit's criteria include the differential arm still passing, and a new arm for the changed contract that can be seen red.
4. Revise `memory/builds/aPiecewiseGrade/spec/2026-11-15-spec-TOOL-aPiecewiseGrade-2.md`: its promotion uses unit 4's contract, its order becomes 4, its edges name unit 4, and it folds the two smaller notes in `2026-11-15-prompt-TOOL-aPiecewiseGrade-2-revision`: where the new verbs-guide sentence goes, and how the read half `run_spec_token_check` reaches the per-spec cache path. Bump its rev and add a revision-log line naming both records by their file stems.
5. Each spec's §3 edges name the build order 3, 1, 4, 2.
6. Stage both specs and clear `python tools/check-spec-tokens.py --spec` over each. Do not commit. Return each spec's path and status line, each new criterion's id with one line, every fork with its recommendation, and the checker's final line for each.

### Acceptance
- TOOL-aPiecewiseGrade-4's spec names a promotion the shell-hygiene lint admits with no registry row, and the observation that shows it: the lint's scan over the driver's promotion code, and a new arm.
- TOOL-aPiecewiseGrade-2 at a bumped rev, order 4, its promotion on unit 4's contract, and its revision log naming both records.

### Gates
`check-spec-tokens.py --spec` over each spec.

### Non-goals
- Any edit to TOOL-aPiecewiseGrade-1's CLOSED spec.
- A row raised in `memory/project/temp-name-sites.txt`.
- A promotion by copying.
- Any change to a verdict, a refusal line, the summary line or an exit status.
- Building anything: the builders follow once both specs are committed.
