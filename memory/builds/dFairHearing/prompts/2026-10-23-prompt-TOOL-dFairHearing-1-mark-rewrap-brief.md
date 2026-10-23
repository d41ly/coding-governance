**Serves:** research TOOL-dFairHearing-2 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-16 TOOL-dFairHearing-23

# Mark-rewrap brief — twelve §8 marks the pinned deviations instrument misreads

`deviations.py --report dFairHearing` (the pinned instrument, `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py`) reports twelve findings of the form `entry N's widens: [none ·] joins no record`.

Its `KEY` pattern ends a value at whitespace-`·`-whitespace or at the next key. A §8 RESOLVED mark that breaks its line right after `widens: none ·`, so the next line opens `relaxes: none`, makes it read `none ·` as the widens value. This is the defect dTrueNorth met: read `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-24-deviation-38.md` and `memory/builds/dTrueNorth/prompts/2026-10-22-prompt-TOOL-dTrueNorth-1-mark-rewrap-brief.md`. The instrument is pinned and never edited, so the marks move.

## The marks

The first line of each mark, by spec and line:

- `2026-10-23-spec-TOOL-dFairHearing-10.md:223`
- `2026-10-23-spec-TOOL-dFairHearing-11.md:321`
- `2026-10-23-spec-TOOL-dFairHearing-13.md:344`
- `2026-10-23-spec-TOOL-dFairHearing-14.md:244`
- `2026-10-23-spec-TOOL-dFairHearing-16.md:287`
- `2026-10-23-spec-TOOL-dFairHearing-2.md:227`
- `2026-10-23-spec-TOOL-dFairHearing-2.md:237`
- `2026-10-23-spec-TOOL-dFairHearing-23.md:600`
- `2026-10-23-spec-TOOL-dFairHearing-9.md:227`
- `2026-10-23-spec-TOOL-dFairHearing-9.md:232`
- `2026-10-23-spec-TOOL-dFairHearing-9.md:236`
- `2026-10-23-spec-TOOL-dFairHearing-9.md:242`

All are under `memory/builds/dFairHearing/spec/`.

## 1. Re-wrap each mark

Re-wrap each mark so that no line of it ends in `·`, for example by carrying `widens: none ·` down onto the `relaxes:` line.

- Change no word, mark, rev, status line or §9 line: whitespace only.
- Check the result by loading the instrument as a module and applying its `KEY` pattern to each mark's joined text. Do not run its `--report`.

## 2. One deviation record per spec revised

Each re-wrap is a spec revision past the spec's audited revision, which the report counts as a member. Write one record per spec in the grammar of dTrueNorth's deviation 38:

- **Departs from:** `<unit>@rev-<audited revision>`. The audited revision is the pin of the latest spec-audit record whose **Serves:** line names that unit, under `memory/builds/dFairHearing/reviews/`.
- **Hand-off:** `spec-revised`.
- **Cause:** `external`.
- **Risk:** `editorial`.
- **Approver:** author, the run's main loop, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`).
- **Follow-through:** `usage §8-mark-wrap`.
- **Caused-by:** `PLAY-dClosedLoop-2`.
- **Evidence:** the report's twelve findings, and this brief.

Two specs already have a staged record at their audited address:

- Unit 14: `2026-10-23-build-TOOL-dFairHearing-14-deviation-149.md`, at `TOOL-dFairHearing-14@rev-3`.
- Unit 16: `2026-10-23-build-TOOL-dFairHearing-16-deviation-169.md`, at `TOOL-dFairHearing-16@rev-1`.

If a spec's audited address equals one of those, extend that record's Before, After and Evidence with the re-wrap instead of writing a second record at the same address. Otherwise write a new record under `memory/builds/dFairHearing/build/` as `2026-10-23-build-TOOL-dFairHearing-<n>-deviation-<n>8.md`: `-28`, `-98`, `-108`, `-118`, `-138` or `-238`.

## Rules for this pass

- Touch nothing else.
- Do not commit, stage, or run any gate or the index generator.
- Report each mark's old and new lines, each record's path and address, and your `KEY`-pattern check's result.
