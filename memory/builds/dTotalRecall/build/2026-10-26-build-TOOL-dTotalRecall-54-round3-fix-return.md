**Serves:** research TOOL-dTotalRecall-54

# The round-3 fix pass — dTotalRecall, its return

The return of the gov-spec-writer dispatched from `memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-54-1-spec-writer.md` over the round-3 fix brief, run direct/a2d90afbf4c3393a9, extracted from its transcript by script.

All four findings are fixed. I couldn't confirm the first goal: the scratch-guard hook blocks `check-spec-tokens.py` for the spec-writer role, so the main session needs to run `python tools/check-spec-tokens.py` before the commit.

To stand in for it, I wrote two read-only scripts that copy two of that checker's checks. One checks that every path an acceptance criterion names in backticks exists at HEAD. The other checks that every leg a Files-touched path trips is listed in §7. Both now report nothing on units 43 and 54 to 60. The leg script listed all three codebase-map legs as missing on the staged copy of unit 55, so it does catch a miss. The only dTotalRecall hits left in the path check are glob tokens in units 37 and 42, which are committed and not in the brief. I didn't touch them; the real checker may treat globs differently. The hygiene gate prints no FAILED line.

**Files edited**, all under `C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\spec\`:
- `2026-10-26-spec-TOOL-dTotalRecall-54.md`: F2, the three codebase-map legs added to the §7 leg line.
- `2026-10-26-spec-TOOL-dTotalRecall-55.md`: F1, AC1 and AC2 now spell `python record_causes.py ...` run from `tools/memory-tree/`. F2, the three codebase-map legs added to §7.
- `2026-10-26-spec-TOOL-dTotalRecall-56.md`: F1, AC2 now spells `python record_kinds.py --check` run from `tools/memory-tree/`.
- `2026-10-26-spec-TOOL-dTotalRecall-57.md`: F1, AC1 cites `record_causes.py` by basename, and the `tools/x.py` fixture example is now described in prose.
- `2026-10-26-spec-TOOL-dTotalRecall-58.md`: F1, AC1 cites `record_causes.py` by basename, run from `tools/memory-tree/`.
- `2026-10-26-spec-TOOL-dTotalRecall-59.md`: F1, AC1 and AC2 cite `legacy_ledger.py` by basename, run from `tools/lib/`. AC2's grep is split in two because `kit.toml` lives in another folder. F2, the three codebase-map legs added to §7.
- `2026-10-26-spec-TOOL-dTotalRecall-60.md`:
  - F1: AC3 and AC11 cite `id_grammar.py` and `record_causes.py` by basename. AC32 now cites the revision `462d20f3` and `tree_lib.py` separately.
  - F2: the three codebase-map legs added to §7.
  - F3: S1 gains a `**Readers:**` clause. By name: unit 53's spec file, the only place that spells the empty-diff demand; a git grep finds it there and in the round-1 review record only. By value: `NO VALUE READERS`, because nothing compares or derives from that one-time check.
- `2026-10-26-spec-TOOL-dTotalRecall-43.md`: F4, prose trimmed and the rev-3 line in §9 extended with "non-criterion prose cut to the size cap". §6, the `gen:spec-records` region, and every scope item and finding id are untouched. The cuts:
  - §1, the §2 lead-in, the Inventory, the "How the batch builds" paragraph, the §8 forks and three hands-off parentheticals were tightened.
  - Rationale tails were dropped from S27 and S30.
  - Some §2 items now cite a file by basename where Files touched keeps the full path (S1, S6, S9, S12, S13, S20, S44, S50, S54).
  - S33's NOT OBSERVED reason now reads "as S32".
  - Reworded with the same meaning: S2, S5, S7, S31 and S48.

**Size of unit 43:** 48574 bytes, generated region included and LF line endings, against the 48600 target and the 49152 ceiling. That leaves only 26 bytes of room under the target.

**Last line of the hygiene gate run:** `HYGIENE --only 2,5,12,21,25 ran checks 2 5 12 21 25`

Nothing was committed and no index was regenerated.
