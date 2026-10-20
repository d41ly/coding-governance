# Phase 0 brief: the revision applied to the execution plan

**Serves:** research PLAY-dClosedLoop-1

The handoff for dispatch 240 renders from this brief record through `handoff.py render --role gov-spec-writer`. The
owner answered the revision record's questions on 2026-10-20 (`build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md`
`[phase0-answers]`): "Apply all 13 (Recommended)", "List it first (Recommended)" and "Rows name the ids
(Recommended)".

## The prompt

Apply `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-revision.md` to
`build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md`: every confirmed finding's recommended revised text,
finding 7 as "listed first", and finding 9 as "rows name the ids".

## The brief

### Goal

The execution plan's P0.1, P0.2, P0.4, P0.7, P0.8 and the line the revision record names for finding 8 (plan:719) read
as the revision record's recommended text, with the owner's three answers folded in, so the builders and the owner's
opening read work from one current plan.

### Items

1. Each finding's revised text from the revision record, applied where it says. Read the revision record whole
   first, then `[phase0-answers]` in the execution record.
2. Finding 7: the "Listed first" option. Finding 9: the "Rows name the ids" option, including the P0.8 sentence the
   record proposes, so row 1 names dTrueNorth's extra unit's id and row 6 names `cl-dClosedLoop-0120`.
3. A dated note at the head of `[phase-0]` saying the section was revised on 2026-10-20 from the revision record at
   the owner's answers, citing `[phase0-answers]`.
4. Where an applied text changes a line another section cites (a P0.x number, a plant name, a check's wording),
   update the citing line too, and list every such line in your return.

### Acceptance

- Every confirmed finding of the revision record maps to a changed passage of the plan, listed in your return as
  finding → plan lines.
- No decided answer of the execution record and no v2 text changes. The plan's `[defaults]` keep their quotes.
- No unit id that no build has minted appears bare: write it `missing:<id>`.

### Gates

None of the bar's legs. The main loop runs memory hygiene on the staged plan.

### Non-goals

- Your tree is the main loop's worktree. Edit only the execution plan; never commit, the main loop does.
- No edit to v2, the revision record, any instrument, any other record or any decision row.
- No product code and no chain build's folder.
- Probes go under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unruffled-aryabhata-d89ede/1cef2554-91c7-4cd1-9950-7f33d1289103/scratchpad/d240/`
  only, as files, never through a heredoc; never delete anything outside it.
