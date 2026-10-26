**Serves:** research TOOL-dTotalRecall-61

# The round-4 fix pass — dTotalRecall, its return

The return of the gov-spec-writer dispatched from `memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-61-1-spec-writer.md` over the round-4 fix brief, run direct/ae5c0eb9ac884bc33, extracted from its transcript by script.

I've fixed all three `<rev>:<path>` spellings, and my own probe of the edited acceptance criteria now finds no path-shaped word that isn't tracked. I couldn't confirm it with `check-spec-tokens.py` itself: scratch-guard blocks that script for this role. The hygiene gate exits 1 on check 9, which is a stale generated build index that only the generator can clear. My edits didn't cause it, and you'll need to run the generator before the commit.

Files edited (staged earlier; my edits are unstaged and nothing is committed):

- `C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-64.md`: AC2 now reads "`git show <unit 54's pass commit>` of `id_grammar.py`, run from `tools/memory-tree/`". The full path stays at line 68. No rev bump, and the design is unchanged.
- `C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-66.md`:
  - AC14 now reads "`git show <unit 19's seed commit>` of `legacy-records.txt`, run from `memory/project/`".
  - AC22 now reads "`git show 462d20f3` of `tree_lib.py`, run from `tools/memory-tree/`".
  - The full `tree_lib.py` path stays in the spec's other sections and Files touched (lines 65, 200, 206, 216). `legacy-records.txt` appeared only in AC14, so I added it nowhere else: putting it in Files touched would claim this unit writes it. No rev bump, and the design is unchanged.

The probe is a copy of the token check's path test from `check-spec-tokens.py:1122-1139`, run over units 61 to 66 and exiting 0. It's at `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-unattended-dtotalrecall-4bf827\23826028-3fee-42de-ac69-b4090f699257\scratchpad\probe.py`. The real check still needs a run in the main session.

On the hygiene failure: check 9 reports that the generated build index differs from a fresh render. It names `memory/builds/dTotalRecall/README.md` and `spec/2026-10-26-spec-TOOL-dTotalRecall-61.md` as stale, and neither is a file I edited. The fix it suggests is `python tools/memory-tree/gen_build_index.py --write`, which my role may not run.

Last line of the hygiene gate run (`bash tools/memory-tree/check-memory-hygiene.sh`, exit 1; check 9 is the only FAILED line):
`memory-hygiene: curation-debt.txt — memory/builds/aUnmannedHelm/README.md earns check(s) 7 of the 6 7 it is waived from`
