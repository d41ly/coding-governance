**Serves:** research TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-23

# The fix pass's return — dLinkedLibrary

The spec writer's final return, extracted from its transcript by script, never retyped.

All 15 findings are fixed, and `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` now exits 0 with none of the build's files named. It does print one information line ("did not grade") about unit 4 S10's `READER NOT IN TREE`, which is expected because PLAY-dOrderedCharter-28 creates `edge_grammar.py`. Check 30 also exits 0 (`as-built clean · 983 deviation records`). I did not run `check-spec-tokens.py`, which my role doesn't permit. Instead I re-ran its hand-off join and the §3 reciprocity rule as a small script over all 25 specs: no token is missing on the receiving side and no edge is one-sided. All edits were in place, with no rev bump and no §9 line, nothing committed and no index regenerated.

## By finding

**Unit 4** (`2026-10-26-spec-TOOL-dLinkedLibrary-4.md`)
1. The placeholder was the literal `YYYY-MM-DD` in S6, which check 12 matches. It now describes the date in words: a four-digit year, two-digit month and two-digit day, dash-joined.
2. S13 already said NOT OBSERVED, but the words were split across two lines, so the check couldn't see them. They are now on one line, followed by the reason (the two kit-version legs grade it at the close).
3. S10's NO VALUE READERS was split across lines the same way. It is now on one line, and its reason adds what a `git grep` for `refs=` over tools, skills and .githooks found: only shell variables (in the pre-push hook, its runlog suite and check-wiring), none of which reads a note.
4. Added the missing edge to unit 15 in §3: `**hands-off** TOOL-dLinkedLibrary-15 — parse_note_line … under in-code-notes`. Unit 4 defines `parse_note_line` in S2.
9. Changed the anchor to `gov:feature <tag>` in S2, S8 and the bullet that takes from unit 19, matching I9. The node is still `feature.<name>`, where `<name>` is that `<tag>`.
10. The bullet to unit 17 was wrong: unit 17 never reads `extract_comment_spans`. It now hands off `parse_note_line`, `scan_annotations` and each row's `block_end`, which is what unit 17 actually takes.
11. The bullet to unit 11 keeps `derive_defined_ids` and says why: unit 11 deletes the drift builder that imports it.

**Unit 11**
- 11. S6 now says the builder imports `derive_defined_ids` (unit 4 S7), so deleting the builder leaves `check_resolve` as its only caller. Its bullet that takes from unit 4 names the function too.

**Unit 7**
- 5. S1 says the `annotations` leg is the `leg` value in unit 11's two `[[ledger]]` rows (TOOL-dWitnessedBar-13 S2). The bullet that takes from unit 11 names `[[ledger]]`.
- 6. S1 and the bullet that takes from unit 12 now say `annotations.py --selftest`.
- 7. S1 and the bullet that takes from unit 17 now name `annotations.py check --only span`.

**Unit 12**
- 6. The sender's bullet was wrong: `--selftest` is a flag on the module itself, not under `check`. It now reads `annotations.py --selftest` (the `annotations selftest` leg runs it), so both specs spell it the same way.

**Unit 23**
- 8. `apply_region` is now `splice_region` in four places: the preconditions, S1, S7 and the bullet that takes from unit 18. Unit 18 deliberately renamed I14's write function, because the build-index generator already has an `apply_region` with a different signature. The preconditions note says so.

**Unit 19**
- 12. AC7 now cites `python dossier_move.py plan` by basename. The full path stays in §2, §4 and Files touched.

**Unit 6**
- 13. AC5 now reads "a planted stray view file under the views folder".

**Unit 16**
- 14. Added `recall floor` and `recall floor arms` to the §7 leg line. Both legs exist in `tools/gate-legs.json`.

**Deviation 11** (`build/2026-10-26-build-TOOL-dLinkedLibrary-1-deviation-11.md`)
- 15. `**Follow-through:**` now reads `amends cl-dClosedLoop-0238@36136b48`. `**After:**` is the clause's full text with one change: "today's 200 rows" became every live row of `memory/DECISIONS.md` at the routing's base (213 at `82a392696`, counted again by `decision_rubric.py rows` at the pass). It has no `|`.

## For the main loop
- **Unit 17 is out of step on the anchor.** It still writes `gov:feature <name>` in S1. That doesn't trip the hand-off join, but it no longer matches units 4 and 19. It was outside this brief, so I left it.
- **Clause 0238's hash may move (not checked).** Once deviation 11 is tracked and the as-built view is re-rendered, the view puts the record's `**After:**` text in place of the clause. That should change 0238's current hash, while unit 1's `**Carries:**` still pins `36136b48`. Please check what `carries.py --report dLinkedLibrary` shows after the view is re-rendered.

Files changed, all under `C:\projects\coding-governance\.claude\worktrees\unattended-dlinkedlibrary-4f9fd9\memory\builds\dLinkedLibrary\`:
- `spec\2026-10-26-spec-TOOL-dLinkedLibrary-4.md`
- `spec\2026-10-26-spec-TOOL-dLinkedLibrary-6.md`
- `spec\2026-10-26-spec-TOOL-dLinkedLibrary-7.md`
- `spec\2026-10-26-spec-TOOL-dLinkedLibrary-11.md`
- `spec\2026-10-26-spec-TOOL-dLinkedLibrary-12.md`
- `spec\2026-10-26-spec-TOOL-dLinkedLibrary-16.md`
- `spec\2026-10-26-spec-TOOL-dLinkedLibrary-19.md`
- `spec\2026-10-26-spec-TOOL-dLinkedLibrary-23.md`
- `build\2026-10-26-build-TOOL-dLinkedLibrary-1-deviation-11.md`
