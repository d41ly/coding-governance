**Serves:** research TOOL-dTotalRecall-77

# The round-7 fix pass — dTotalRecall, its return

The return of the gov-spec-writer dispatched from `memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-77-1-spec-writer.md` over the round-7 fix brief, run direct/a98034a66c8dc6985, extracted from its transcript by script.

Every finding in the round-7 fix brief is cleared, and nothing in any spec's design changed. Hygiene checks 2, 5, 12, 21 and 25 now print no FAILED line. The lexicon gate (`python tools/check-spec-tokens.py`) has not been run: scratch-guard blocks it for this role, so the main session needs to run it before the commit. The new F1 text only uses tokens that gate does not grade (bare basenames, and folders with no extension). The four `path:line` citations I added are to real lines I checked.

Files edited, all still at rev-1 with no rev bump. The edits are not staged on top of the earlier staging, and nothing was committed.

- `C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-77.md`: §2 S2 gains a Readers clause (F2). By name: the scratch worktree is spelled by `add_scratch_worktree` / `remove_scratch_worktree` and their three run-gates callers. By value: NO VALUE READERS, because the worktree is made and removed inside the item.
- `C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-78.md`: §2 S3 gains the same kind of Readers clause for its scratch worktree per unit (F2).
- `C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-87.md`: §2 S1 gains a Readers clause (F2). By name: the memory-tree kit's Python readers of `MEMORY_ROOT`, plus `runlog_lib.py`'s `resolve_memory_root`, and every other reader is whatever `git grep -l` for the name lists. By value: `resolve_kept_registration`, the only caller.
- `C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-88.md`:
  - **F1:** §6 AC3 now cites the three not-yet-created files by basename. It runs `git grep -n "absorbs" -- kit.toml legacy_ledger.py` from `tools/memory-tree/`, then `-- legacy_ledger.py` from `tools/lib/` and from `tools/gate-lint/`. The full paths stay in §2 S6.
  - **F2, S26:** By name: READER NOT IN TREE, because the registered home and `resolve_kept_registration` are created by units 68 and 73 and are absent at base `462d20f3`. By value: `read_kept_path`, `record_causes.py --check`, and the factory verbs that S13 hands off.
  - **F2, S29:** By name: the readers that spell the edge head `consumes-from`, which are `read_consumes_from` (`lib-unattended.sh:348`), the Edges arms of `check-memory-hygiene.sh` (`:2474`, `:2714`) and `unattended-build.js:859`. By value: `scan_consumes_cycles` (`:399`) and the `--dispatch` edge refusal, for which a duplicate reads as the same edge twice.

Decision for you: in 77 S2, 78 S3 and 87 S1, check 25 fired on a removal verb next to a backticked identifier, but nothing named is being retired. The verbs are "removed" for a temporary scratch worktree, and "drops" for empty and `.` segments of one value. I followed the brief and wrote Readers clauses that say so. The other option is to reword those verbs, which would avoid a clause that answers for no real retirement.

Last line of the hygiene gate run:
```
HYGIENE --only 2,5,12,21,25 ran checks 2 5 12 21 25
```
The run exited 0. Its only dTotalRecall lines about the edited files are notices that check 25 did not grade names covered by READER NOT IN TREE, on 87 S2 and 88 S26; these do not fail the gate.
