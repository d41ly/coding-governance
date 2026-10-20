# Phase 0 revision brief: the defects a builder found in P0.1 and P0.2, turned into a revision proposal for the owner

**Serves:** research PLAY-dClosedLoop-1

The handoff for dispatch 238 renders from this brief record through `handoff.py render --role gov-spec-writer --input
prompt=<this file>`. The builder of dispatch 234 built P0.6, then stopped before P0.1 and P0.2 of
`build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` `[phase-0]`: it measured two defects in their population
and listed eleven more gaps. Its evidence is `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-deviations-instruments.md`,
and its return is quoted below. The Phase 0 handoff says a plan error is raised with the owner as a question, never
fixed silently (`prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-59-session.md`).

## The prompt

Write a revision proposal for P0.1, P0.2 and the parts of P0.7 and P0.3 the builder's findings reach. Verify each
finding against the source it cites. For each one, state the defect as measured, the options and a recommendation,
and the exact revised plan text for the recommendation. Say which findings touch a decision the owner made, quoting
that decision, and which are the plan writer's design. Do not edit the plan.

The builder's findings, verbatim from its return:

1. Row 3 (which commit is a pass): the fix says to read a pass "as `routed_commits.py:22-26` does", but those lines
   say their union reading is not the pass reader. The harness commits every spec as `spec(<slug>): <ids>` with
   `Pass: none` (`unattended-build.js:1182`). Under the union reading, `Pass: none` keeps the subject's ids, so the
   spec or records commit becomes the unit's first pass, and every later revision becomes a member, which contradicts
   the plan's own `[constraints]` row. Measured on dRenderedAnchor's 7 specs: union counts 19 after-pass revisions,
   against 9 for today's trailer-only reading; its first "pass" for unit 1 is `f576bd192`, a `Pass: none` records
   commit. The driver's own reader is no fix: it counts 17, taking trailer-less status flips like `0f787ab62` as the
   pass.
2. Row 8 / the population: only Status-only edits are excepted. All 9 of the 9 after-pass revisions the trailer
   reading counts on dRenderedAnchor change only a `<!-- gen:... -->` region (the spec-records region, re-rendered as
   later records land). Each would be listed "recorded by nobody".
3. Hand-backs: no RUN.md row records one. The only trace is the `prompts/` revision record the `/build` skill writes,
   whose Goal opens `DIVERGENCE:`. The plan should name that source and its join address.
4. Ledger rows: an `amended rev-N` row names no record, so its join address is unstated.
5. Audited revision: P0.2 lists revisions "after the pinned audited revision", but no such pin exists in the tree.
6. Run kind: the report's run kind (spec or build) needs README rule 1's test; nothing says how the instrument gets
   it.
7. Policy versus plants: under the default `report` every plant exits 0; the plan should say whether plants are read
   under `refuse`, and give the exit code for row 5's refused Baseline.
8. Row 6: under `author-recorded` the existing `approver` plant turns green; the plan should say what replaces it,
   and `[phase-1]`'s "approver below its risk" loses its meaning.
9. Decision ids: ids written `missing:` in the instrument mean either the approver arm strips the prefix, or
   `deviations.py` is edited when P0.8 lands and every packet is re-pinned.
10. Fixture ids: `missing:` ids fail the generator's H1 and backlog grammars; a fixture family declared in the fixture
    repo's own conf would work.
11. P0.7: the bare-id predicate will print the ids the opening mints, so "must print nothing" goes red as written.
12. Row 10: "every report prints each instrument's blob hash" falls into `deviations.py --report`, which no brief
    assigns.
13. `asbuilt.py` reads its baseline unpinned, the same class as row 5.

And from the carries builder (dispatch 235, `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-carries-instruments.md`):

14. The token arm reads only the owner build's own specs, so a clause correctly moved by a `**Moved:**` line reds its
    token whenever its owner build is measured too, though the carrying spec holds the token.

And from the schedule red tests (dispatch 237, `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-schedule-redtests.md`):

15. Row 9 of P0.4 differs: `run()` builds the "claim absent from that run, left unpinned" note and `main()` discards
    it (script lines 373-374), though the script's docstring says it is printed.

## The brief

### Goal

One record, `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-revision.md`, that the owner can answer in one or two
questions: every finding verified or refuted against source, each with options, a recommendation and the revised plan
text, grouped into the decisions the owner must make and the fixes that follow from the plan's own answers.

### Items

1. Each of the fifteen findings, verified against the cited source (file and line), marked CONFIRMED, REFUTED or
   PARTLY, with what you measured.
2. For each confirmed finding: options, a recommendation, and the revised plan text for P0.1, P0.2, P0.3, P0.4 or
   P0.7 as it would read.
3. A short `[owner]` section listing only the findings whose fix changes or reads against an owner answer in the
   execution record (`build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md` `[answers]` to `[answers-4]`, `[walk]`),
   each quoting that answer, with a recommended option first.
4. A `[builder]` section: the revised acceptance for the deviations builder, in the order it would build.

### Acceptance

- Every finding has a verdict and a cited source line read for this record.
- Every confirmed finding's revised text keeps the plan's decided answers and v2 unchanged, or the record names the
  answer it would change in `[owner]`.
- No unit id that no build has minted appears bare: write it `missing:<id>`.

### Gates

None of the bar's legs. The main loop runs memory hygiene on the staged record.

### Non-goals

- No edit to the execution plan, v2, any instrument or any other record. The record proposes; the owner decides; a
  later dispatch applies.
- No product code, no chain build's folder, no decision row.
- Write any probe as a file under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unruffled-aryabhata-d89ede/1cef2554-91c7-4cd1-9950-7f33d1289103/scratchpad/d238/`
  only, never through a heredoc, and never delete anything outside it.
- Do not commit: the main loop commits the record.
