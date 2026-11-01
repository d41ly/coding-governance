**Serves:** research TOOL-dTotalRecall-93

# The round-9 fix pass — dTotalRecall, its return

The return of the gov-spec-writer dispatched from `memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-93-1-spec-writer.md` over the round-9 fix brief, run direct/a46ae283c052d8e54, extracted from its transcript by script.

All three findings are fixed in five spec files. I edited them in place with no rev bump and committed nothing. My role isn't allowed to run `check-spec-tokens.py` (the hook blocked it), so that gate is still owed by the main loop. The hygiene gate run after the edits shows no FAILED line.

**Edited files** (all under `C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\spec\`):
- `2026-10-26-spec-TOOL-dTotalRecall-100.md`:
  - **F1:** AC5 now backticks `memory/guides/SESSION-KICKOFF.md` (tracked) on its own and names the `pass_of 69` commit, `git show` and `grep -c 'kickoff-manifest:'` in prose. The untracked `69):...` fragment is gone.
  - **F1:** AC9 describes its fixture path in prose ("a none-deviation-0.md in the build folder") instead of a backticked path literal.
  - **F2:** S14 gets a `**Readers:**` clause modelled on unit 92's S13.
    - By name: `add_scratch_worktree` and `remove_scratch_worktree` (`tools/run-gates/lib-attribute.sh:59`, `:63`) and their callers `tools/run-gates/post-merge.sh` and `tools/run-gates/run-gates.sh`, each found by `git grep`.
    - By value: `check_pockets`, from `TOOL-dTotalRecall-18`.
- `2026-10-26-spec-TOOL-dTotalRecall-98.md`:
  - **F1:** AC1 names the fixture's deleted record as "x-deviation-1.md under the fixture's build folder" instead of a backticked path literal.
  - **F2:** S2 gets a `**Readers:**` clause.
    - By name: no name retires. The item deletes only a record in a temporary fixture repository, and `git grep` finds no tracked reader of `x-deviation-` (only the brief, the round-1 review record and this spec).
    - By value: `NO VALUE READERS` with its reason, kept on one line.
- `2026-10-26-spec-TOOL-dTotalRecall-14.md` (**F3**): the mark at line 243 has `relaxes: none` joined onto its RESOLVED line. Whitespace only.
- `2026-10-26-spec-TOOL-dTotalRecall-24.md` (**F3**): the mark at line 217, same join. Whitespace only.
- `2026-10-26-spec-TOOL-dTotalRecall-26.md` (**F3**): the mark at line 340, same join. Whitespace only.

**My own checks** (copies of each tool's rules, not the gates themselves):
- **Departures instrument:** it reads a mark's keys only from the line holding `RESOLVED (` (`deviations.py:711`). Using its `KEY` regex over every RESOLVED line in the build's specs now finds no value ending in `·`, so all three now read whole. Other marks with wrapped tails (for example 14:254, 26:334) don't have `RESOLVED (` on that line, so the instrument never reads them, and I left them as they were.
- **AC paths:** the paths rule from `check-spec-tokens.py` (with the waiver file) finds no untracked path in the acceptance criteria of units 93 to 100. `.claude/SESSION-KICKOFF.md` in AC5 is already waived at line 25 of `memory/project/spec-token-waivers.txt`.

The remaining `check 25 did not grade … READER NOT IN TREE` lines in the output are notices that were already there, not failures.

Last line of the hygiene gate run (`bash tools/memory-tree/check-memory-hygiene.sh --only 2,5,12,21,25`, exit 0):
```
HYGIENE --only 2,5,12,21,25 ran checks 2 5 12 21 25
```
