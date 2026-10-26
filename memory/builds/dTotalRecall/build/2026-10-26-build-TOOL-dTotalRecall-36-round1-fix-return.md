**Serves:** research TOOL-dTotalRecall-36 TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43

# The round-1 fix pass — dTotalRecall, its return

The return of the gov-spec-writer dispatched from `memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-1-spec-writer.md` over the round-1 fix brief, run direct/a3bd294b0665d4dfc, extracted from its transcript by script.

All five findings are cleared over units 36 to 43 and the three deviations. Nothing is committed, and the build index was not regenerated. My edits sit unstaged in the worktree, on top of the staged files.

I did not run `check-spec-tokens.py`, since it isn't a gate my role may run. Instead I copied the logic of its paths and guards arms into a scratch probe. On the staged copies that probe reproduced F3's 18 missing-leg hits exactly. On the edited files it finds no criterion path that is not tracked at HEAD, and no missing leg across every live dTotalRecall spec. The main loop's real run is still the confirmation.

**Files edited** (all under `C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\`):
- `spec\2026-10-26-spec-TOOL-dTotalRecall-36.md`: F1 review citation re-pointed; F2 two §6 commands now cite `record_causes.py` by basename; F3 the three codebase-map legs added to §7.
- `spec\2026-10-26-spec-TOOL-dTotalRecall-37.md`: F1; F2 AC4 cites `code_record.py` by basename; F3.
- `spec\2026-10-26-spec-TOOL-dTotalRecall-38.md`: F1; F2 AC1, AC2 and AC4 cite `id_grammar.py` by basename; F3.
- `spec\2026-10-26-spec-TOOL-dTotalRecall-39.md`: F1; F2 AC2 and AC3 cite `record_causes.py` and `edge_grammar.py` by basename. It needed no F3 change.
- `spec\2026-10-26-spec-TOOL-dTotalRecall-40.md`: F1; F2 AC3 cites `record_kinds.py` by basename; F3.
- `spec\2026-10-26-spec-TOOL-dTotalRecall-41.md`: F1; F3. AC1 now also cites `gov_record.py` by basename. The checker did not flag that line (its backticks wrap across a line break); I changed it to match the other units.
- `spec\2026-10-26-spec-TOOL-dTotalRecall-42.md`: F1; F2:
  - AC1 and AC2 cite `record-kinds.toml` and `record_kinds.py` by basename.
  - AC2's planted record is described in prose.
  - AC3's grep now takes the pathspec `'*record_kinds.py'`, so it still runs from the repo root.
  - F3.
- `spec\2026-10-26-spec-TOOL-dTotalRecall-43.md`: F1; F2 and F4:
  - **F2:** every §6 command now cites its file by basename, and the git greps in AC11 and AC12 take a `'*<file>'` pathspec. The example fixture paths in AC1, AC16, AC17 and AC43 are now described in prose or as named plants.
  - **F4 trims:**
    - The 31-row item table is replaced by one sentence giving the item-to-scope order. I checked it against the old table, row by row.
    - The Edges bullets keep what each edge consumes but drop the lists of scope items, which each scope item already states.
    - Files touched is packed several to a line with every full path kept; the declared write set is byte-for-byte the same token set.
    - One rejected alternative and one non-goal that repeated other text are cut.
    - §10 now points at the scope items' citations instead of repeating them. While there I fixed its claim that S10 carries a line citation it doesn't, by keeping `tools/memory-tree/kit.toml:8` in §10.
  - Every criterion, scope item and finding id is kept.
- `build\2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md`, `-8-deviation-81.md`, `-23-deviation-231.md`: F5. Each **After** is now the whole baseline clause, taken from the packet at `19ea7b40c` (the last version before it was re-rendered over the fragment Afters), with only the departed words changed. Every backtick token the old After carried is kept, none holds a `|`, and `deviation_join.read_record` reports no malformed field for any of the three. I did not touch the `**Carries:**` pins.

**Unit 43 size:** 48,783 bytes against the 49,152 ceiling, the same with carriage returns stripped.

**Hygiene gate** (`bash tools/memory-tree/check-memory-hygiene.sh --only 2,5,12,21,25`, run in place): exit 0, no FAILED line. Its last line is `HYGIENE --only 2,5,12,21,25 ran checks 2 5 12 21 25`.

**Still citing the old name:** `RUN.md` lines 34 to 48 still cite `2026-10-26-review-dTotalRecall-spec-audit-round1.md` in their rescope rows. F1 covered the specs only, and RUN.md belongs to the main loop, so I left it.
