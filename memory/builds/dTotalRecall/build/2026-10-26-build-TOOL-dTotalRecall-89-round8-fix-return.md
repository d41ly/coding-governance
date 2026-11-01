**Serves:** research TOOL-dTotalRecall-89

# The round-8 fix pass — dTotalRecall, its return

The return of the gov-spec-writer dispatched from `memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-89-1-spec-writer.md` over the round-8 fix brief, run direct/a5e2fcef6964f5d08, extracted from its transcript by script.

I fixed all three findings in unit 92. Nothing else in its design changed, and it stays at rev-1. The hygiene gate (`--only 2,5,12,21,25`) now prints no FAILED line at all, and no line naming unit 92. One check is still owed: I could not run `python tools/check-spec-tokens.py`, because scratch-guard blocks it for the spec-writer role. That leaves F1 unconfirmed against the token check, so the main loop needs to run it before the commit.

Files edited:
- `C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-92.md`
  - **F1 (AC12):** the one-liner now reads `open(sys.argv[1], encoding='utf-8')` instead of the hard-coded README path. The prose says it runs "with the build README as its argument". I ran it with that argument and it printed `[('## Build-level rules', 1540)]`, which matches the 1540 B the spec pins in §4.
  - **F2 (AC9):** the bullet now names its witness in backticks: the figure the main loop timed over one `add_scratch_worktree`, `read_checker` and `remove_scratch_worktree` at the pass base. It also says S9's completion lines are each unit's scratch file from §4's sweep.
  - **F3 (S9):** I added a `**Readers:**` clause modelled on unit 78's S3 clause:
    - **By name:** no name retires; the scratch worktree path is spelled by `add_scratch_worktree` and `remove_scratch_worktree` (`tools/run-gates/lib-attribute.sh:59`, `:63`), which are called from `post-merge.sh`, `run-gates.sh` and `run-selftests.sh`. I found these with `git grep`.
    - **By value:** `check_pockets` (minted by TOOL-dTotalRecall-18), with the `gate-ledger` pocket row covering `gate-mc92`. This matches what S13 already says.
  - **F3 (S11):** the `· by` / `value:` text broke across two lines, so the check could not find a `by value:` half. I reflowed the clause so `· by value:` sits on one line. The wording is unchanged.

Last line of the hygiene gate run:
`HYGIENE --only 2,5,12,21,25 ran checks 2 5 12 21 25`
