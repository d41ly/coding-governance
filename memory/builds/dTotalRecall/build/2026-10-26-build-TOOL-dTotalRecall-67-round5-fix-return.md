**Serves:** research TOOL-dTotalRecall-67

# The round-5 fix pass — dTotalRecall, its return

The return of the gov-spec-writer dispatched from `memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-67-1-spec-writer.md` over the round-5 fix brief, run direct/a7c1a1752a3e28b5f, extracted from its transcript by script.

Both findings in the round-5 fix brief are fixed. The hygiene gate (`--only 2,5,12,21,25`) now prints no FAILED line, and the last line of its run is:

`HYGIENE --only 2,5,12,21,25 ran checks 2 5 12 21 25`

My role isn't allowed to run `python tools/check-spec-tokens.py`; the hook blocked it. So I copied that tool's acceptance-path rule (`check_path_shaped` and the bullet loop at `tools/check-spec-tokens.py:1514-1525`) into a probe of my own. Before the edits it found exactly the six paths the brief lists; after them it finds none in any dTotalRecall spec. The main loop still needs to run the real `check-spec-tokens.py` to confirm.

Files edited (units 67 to 70 stay at rev-1, as the brief says; no design change):

- `C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-68.md`: in AC1, the home is now cited as "the home S2 rewrites, `census-kept-paths.txt` under `memory/project/`" instead of by its full path (F1).
- `C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-70.md`:
  - **F2, S8:** the `by value:` half of the **Readers:** clause now names its readers in backticks: `read_kept_path`'s domain loop and refusal message (unit 57), and the marker reader's remedy message that `check_cause_writers` and `check_alias_compares` print (unit 58).
  - **F1, AC3:** the `git grep` now takes the basenames `record_causes.py record_kinds.py tree_lib.py` and runs from `tools/memory-tree/`. The `CENSUS_KEPT_PATHS` grep is now stated to run from the repository root, so its pathspec `tools` keeps its meaning.
  - **F1, AC5:** the planted file is now cited as `census-kept-paths.txt` under `memory/project/`.
  - **F1, AC9:** the two revision reads now name the revision and the basename apart: "`git show 462d20f3` of `tree_lib.py`, run from `tools/memory-tree/`", and "`git show` of `legacy-records.txt` at unit 19's seed commit". The full paths stay in §2, §4 and Files touched.

The edits are unstaged changes on top of the staged files. I did not commit or regenerate any index, so whoever dispatched me needs to stage both files before the commit.
