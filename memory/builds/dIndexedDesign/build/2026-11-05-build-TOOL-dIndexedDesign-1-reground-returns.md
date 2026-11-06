**Serves:** research TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-52

# dIndexedDesign — the re-ground writers' returns, verbatim

The `gov-spec-writer` returns for the re-ground brief [`2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-reground`](../prompts/2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-reground.md), extracted by script from each agent's transcript and not retyped. The cross-check record it folds is [`2026-11-05-build-TOOL-dIndexedDesign-1-parents-crosscheck`](2026-11-05-build-TOOL-dIndexedDesign-1-parents-crosscheck.md); each group's handoff sits beside the brief.

## Group A, led by spec 2 (specs 2, 1, 5 and 8)

I've revised all four Group A specs: 1, 2, 5 and 8. All six rows held up when I re-read both sides against today's text, so none was refused. The 2026-11-05 fork-pick commit `740e19214` touched only spec 38 in this build. The parents revised since the readers ran (TOOL-dTotalRecall-18 rev-4, TOOL-dDeclaredLoop-12 rev-4, TOOL-dDeclaredLoop-13 rev-3) didn't change any section these rows rest on. Each spec's Status line carries its new rev and 2026-11-05, and its §9 has one new line in the brief's form.

## What moved

- **TOOL-dIndexedDesign-2** (rev-3, rows 7 and 9)
  - **S7:** now spelled `record_kinds.py new overlap --tag record.overlap --writer "design_lib.py --overlaps --record <slug>" --check "memory hygiene" --purpose "…"`. The columns TOOL-dTotalRecall-18 S1 requires are set through its landed verb:
    - layer `layer.memory`
    - home `memory/builds/*/build/*-overlap-[0-9]*.md`
    - id-rule `<date>-build-<first unit id>-overlap-<n>.md`
    - form `rows`
    - lifecycle `append-only`
    - `readers = []` with a `readers-none` reason
  - **New S10:** deletes TOOL-dDeclaredLoop-13 S8's stand-in row for `item.design.overlaps` and points the item's `witness` at `design_lib.py --overlaps`. The external edge, Rollout and Files touched (`tools/loop/loop.toml`) record this.
  - **ACs:** AC9 now checks the writer, purpose and columns, and is red on a missing column. A new AC11 reads `loop.toml` for the armed witness and the deleted stand-in.
- **TOOL-dIndexedDesign-1** (rev-5, row 3)
  - The external edge and the non-goal now name TOOL-dDeclaredLoop-13 S8's stand-in rows for both `item.design.ready` and `item.design.exit`.
  - §8 F5 keeps its pick. It gains one sentence keeping ready's row on the same ground as exit's. Its "spec line 239" cite became §4 "The stand-ins".
- **TOOL-dIndexedDesign-5** (rev-3, row 37)
  - The `loop_items.py new` factory call is gone. S8 now arms the existing `item.design.research` row from TOOL-dDeclaredLoop-12: its witness becomes the `read_declared_kind` / `research-return` check, and its stand-in row is deleted.
  - The §2 preconditions, external edge and Files touched follow, and the item's row is out of Inventory.
  - AC9 reads the armed witness and the stand-in's absence, so it is red before the unit builds.
- **TOOL-dIndexedDesign-8** (rev-4, rows 42 and 43)
  - **Registrations:** S1, S4 and S6 now carry `--purpose`, and a new §4 "The registry rows" table holds TOOL-dTotalRecall-18's columns. `feature-design` and `fork` are `fields`, `roster` is `rows`.
  - **Fork home:** the fork row's home is `*-fork-[0-9]*.md`, because a plain `*-fork-*.md` glob matches three tracked files at `11ebd1e87` that no fork kind wrote.
  - **`hand` non-goal:** restated on TOOL-dTotalRecall-1 §4: TOOL-dTotalRecall-2 S9 never moves these rows, and no door is promised for them.
  - **Edges and AC:** a new external edge cites TOOL-dTotalRecall-16 S2, -18 S1 and -42 S2. AC8 checks the columns and is red on a missing one.
  - **Shared-files paragraph:** I also changed it. It said "this unit first at order 8", which became false once spec 2 arms its loop row at order 6.

## Beyond the items: please check

- **`unarmed` keys on spec 8.** The brief doesn't mention these. Without them, TOOL-dTotalRecall-18 S1 reds a `fields` row whose home matches no tracked file, and neither kind has a record at landing. So `feature-design` and `fork` each carry an `unarmed` key under TOOL-dTotalRecall-42 S2. TOOL-dTotalRecall-42 S2 reds the key once a record exists, so the commit that writes a kind's first record must delete it.
- **Lifecycle values** (`append-only` for overlap, `current-state` for the other three) are my own choice. Each has a one-line reason in the spec.

## Hygiene gate

`check-memory-hygiene.sh --staged`, run over a copy of the index with only these four specs staged, exits 1 on check 9 alone: a render is owed for LIVE.md and the dDeclaredLoop, dIndexedDesign, dLinkedLibrary, dRankedPlan and dTotalRecall READMEs. That's the main loop's `gen_build_index.py --write`. Nothing else names these specs except check 25's coverage note on spec 5 S7's `help/reuse.md`, which is existing text. I deleted the index copy; nothing is staged in the real index. Sizes run from 30,671 bytes (spec 1) to 35,471 bytes (spec 8), all under 49,152.

## Problems outside my group (noted, not edited)

- **Unversioned `returns`.** Spec 8 S11 sets `returns` to `record-kind.feature-design` with no `@<n>`. That's the same problem as row 99, but the cross-check didn't flag it for spec 8.
- **Purpose over the cap.** TOOL-dTotalRecall-16 S1 caps a purpose `text` at 120 bytes. Spec 10's playbook purpose is 198 bytes and spec 11's playbook-set purpose is 132. Both belong to Group B.
- **Parent grammar gap.** TOOL-dTotalRecall-1 S9's `new` grammar still has no flag for tr18's columns, so every caller leans on tr18's verb.

Files revised:
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dIndexedDesign\spec\2026-10-28-spec-TOOL-dIndexedDesign-2.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dIndexedDesign\spec\2026-10-28-spec-TOOL-dIndexedDesign-1.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dIndexedDesign\spec\2026-10-28-spec-TOOL-dIndexedDesign-5.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dIndexedDesign\spec\2026-10-28-spec-TOOL-dIndexedDesign-8.md

## Group B, led by spec 10 (specs 10, 9, 11, 13 and 14)

Group B is revised: specs 9, 10, 11, 13 and 14. I re-read both sides of all seven rows (50, 57, 58, 64, 73, 77, 81) against the branch tip. Every one still holds, so none is refused. The fork fold of 2026-11-05 moved TOOL-dTotalRecall-18 (its F6) and TOOL-dDeclaredLoop-29 (its S9 and AC12), but neither change touches what these rows rest on.

**TOOL-dIndexedDesign-10** (rev-3, rows 58 and 57)
- The writer non-goal in §3 now says the writer stays `hand`: TOOL-dTotalRecall-1 §4 "Data model" allows it on a `header` row, which TOOL-dTotalRecall-2 S9 never moves. Any door is the unattended kit's own, or an ask of whichever build would own it.
- §8 F1 keeps its pick (a). Its ground now says S2's resolver decides membership and the home only admits. The `record` extractor does not tag a playbook, because TOOL-dTotalRecall-42 S5 classifies by the Serves kind alone, TOOL-dTotalRecall-43 S13 makes that the only classifier, and TOOL-dTotalRecall-53 S21 passes it the kind `read_bindings` found. The ask this build's run files in dTotalRecall's `BACKLOG.md` is written out in full. Its title is "THE RECORD EXTRACTOR TAGS NO KIND WITHOUT A SERVES LINE", and it covers both `playbook` and `playbook-set`.

**TOOL-dIndexedDesign-11** (rev-2, row 64)
- §8 F2 keeps its pick (a). Its ground is restated the same way and points to spec 10 §8 F1 for the one ask, so the row text exists in only one place.

**TOOL-dIndexedDesign-9** (rev-3, row 50)
- `replay-phrases.py` and its `_SEC10` are gone from S6, AC8 and Files touched, and S6 says TOOL-dLinkedLibrary-3 S1 takes the harness out before this unit builds.
- S11 has no twin table of its own: it reads the twins through S6, so it needed no edit.
- §4 "Why twins and not one import" no longer lists codebase-map as a twin kit.

**TOOL-dIndexedDesign-13** (rev-3, rows 73 and 77)
- **S1:** the `new seams` call gains `--purpose`, and the TOOL-dTotalRecall-18 columns are set through that unit's landed verb:
  - layer `layer.memory`
  - home `memory/builds/*/build/*-reuse-scout*.md`
  - lifecycle `append-only`, following TOOL-dLinkedLibrary-13 S2
  - readers `["task:reuse"]`, the key TOOL-dLinkedLibrary-2 S7's slot renders the record under
  - schema `fields` form
- **S6:** decompose's row gains the outcome `finding`, routed to `item.design.overlaps`. I derived that route rather than treating it as a fork: on a `record` edge the return stands (TOOL-dDeclaredLoop-29 S6), and this spec's Rollout says the edge gates nothing.
- **AC6** now runs `record_kinds.py --check` and goes red on a missing column.
- **AC7** runs `python tools/loop/loop_lib.py --check`, including a case where the route is dropped.
- The §2 preconditions now cite TOOL-dTotalRecall-16 S2, TOOL-dTotalRecall-18 S1 and TOOL-dDeclaredLoop-29 S7.

**TOOL-dIndexedDesign-14** (rev-3, row 81)
- I chose the reading where the corpus filters gated classes out too:
  - S1 extracts `cmd_for_paths` as TOOL-dLinkedLibrary-24 S5 and S6 leave it, with the gated cut and the `record` tier. The function becomes `derive_class_ranking(recs, paths, m, gated)`.
  - S2 derives one `gated` set per case and uses it to cut both `anchor` and `index`, so both arms rank the same classes.
- The §3 non-goal is restated, and §3 says it does not check that each case's gated status is computed against today's leg manifest and plants, not as they stood at `before`.
- AC1 and AC2 each gain a gated-class case.
- I added a consumes-from edge to dLinkedLibrary and a matching precondition.

**Checks**
- **Size:** all five specs are under 49152 bytes: 9 at 32,320, 10 at 26,074, 11 at 23,823, 13 at 29,321 and 14 at 31,590.
- **Hygiene gate:** I ran `check-memory-hygiene.sh --staged` over a copy of the index with only these five specs staged, then deleted the copy. The real index has nothing staged. The first run flagged check 25 on spec 9's S6, because my wording read as retiring a name. S6 retires nothing (TOOL-dLinkedLibrary-3 S1 does), so I reworded it, and the rerun no longer flags it.
- **Left for the main loop:** check 9, "render owed under --staged" for spec 10. Only `gen_build_index.py --write` fixes it.

**Parent text that looks wrong** (not edited)
- No dTotalRecall spec names the flag or verb that sets TOOL-dTotalRecall-18's four columns. Specs 10, 11 and 13 all depend on "that unit's landed verb", which is unknown until dTotalRecall builds it.
- TOOL-dTotalRecall-1 §4 ties `hand` being legal to rows "TOOL-dTotalRecall-2 S9 does not move". S9 is a one-time pass, so spec 13's `fields`-form `hand` row is legal only because it lands after that pass.

Revised specs:
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dIndexedDesign\spec\2026-10-28-spec-TOOL-dIndexedDesign-9.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dIndexedDesign\spec\2026-10-28-spec-TOOL-dIndexedDesign-10.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dIndexedDesign\spec\2026-10-28-spec-TOOL-dIndexedDesign-11.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dIndexedDesign\spec\2026-10-28-spec-TOOL-dIndexedDesign-13.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dIndexedDesign\spec\2026-10-28-spec-TOOL-dIndexedDesign-14.md

## Group C, led by spec 20 (specs 20, 34, 32, 38, 46 and 52)

I revised all six Group C specs: 20, 34, 32, 38, 46 and 52. Every row still held when I re-read both sides against today's text, so I refused none, and the 2026-11-05 fork picks settled none of them. Each spec is under 49152 bytes, carries its next rev dated 2026-11-05 with the other status fields kept, and has one new revision-log line naming the re-ground brief. The hygiene gate, run over a copy of the index with only these six staged, names none of them except under check 9. That is the build-index render you owe in the main loop (`gen_build_index.py --write`), and I left it alone. The index copy is deleted.

**Revised**
- **TOOL-dIndexedDesign-20** (rev-4), rows 95 and 99:
  - S4 and S7 now pass `--purpose` (each under the 120-byte limit tr16 S1 sets) and declare form `fields`. They set tr18 S1's four columns through tr18's landed verb: layer `layer.memory`, homes `memory/builds/*/build/*-diff-*.md` and `memory/builds/*/build/*-inventory-*.md`, lifecycle `append-only`, and `readers = []` with a `readers-none` reason.
  - The external edge now cites tr16 S2 and tr18 S1.
  - S10's `returns` now read `record-kind.diff@1` and `record-kind.inventory@1`. Their `[[record-version]]` rows are deferred to spec 34's pass.
  - AC9 now runs `record_kinds.py --check`. It goes red on a missing column or a `returns` with no version.
- **TOOL-dIndexedDesign-34** (rev-4), the knock-on from row 99: a new S3 adds the two `[[record-version]]` rows in `tools/loop/item-schema.toml`, landing in the same commit as the S1 table rows they hash. A new AC5 checks them with `loop_items.py check`, including a red case where a hash moves while the version stays at 1. The change is also in the Goal, preconditions, Edges, Inventory, Rollout and Files touched.
- **TOOL-dIndexedDesign-32** (rev-3), row 106: S2 now names the untyped head as `spec-audit`, `diff-review`, `log`, `research`, with `journal` a read-only alias. S2, the preconditions and the external edge cite tr18 S7.
- **TOOL-dIndexedDesign-38** (rev-5, since rev-4 was the owner's F1 pick), rows 115 and 117:
  - S3 now follows dl19 S8's table in its order: `review.design` first, and the README key decides only under `opt-in`. AC3 plants `off` with a dated README key, which must print no lens line.
  - S9 gains `--purpose` and tr18's columns, with home `memory/builds/*/reviews/*.md`. AC7 now goes red on a missing column.
  - The external edge cites tr16 S2, tr18 S1 and dl19 S8.
- **TOOL-dIndexedDesign-46** (rev-3), row 121: S11 reads in dl19 S8's order. The README key and the dated `SPEC_AUDIT_DEFAULT` are consulted only under `opt-in`. AC9 plants `off` with a present dated README key, a new external edge cites dl19 S8, and §10 is updated to match.
- **TOOL-dIndexedDesign-52** (rev-2), which restates spec 46's reader:
  - S1 and §4's table now apply only under `opt-in`. The table's last row drops "then `review.design`".
  - The non-goal and a new external edge cite dl19 S8.
  - AC1 adds a case: `spec-audit: yes` under `off` neither exits 2 nor prints a lens line.

**Choices beyond the items' literal text, for review**
- **`unarmed` on spec 20's rows.** I gave the `diff` and `inventory` rows tr42 S2's `unarmed` key. tr18 §4 "Columns" turns a `fields` home red when it matches no tracked file, and no diff or inventory record exists when the unit lands. ll8 S1 does the same.
- **Spec 20's `returns` before the version rows land.** S10 says dl24 S4 names no check that would turn a `returns` red in the gap before spec 34 adds its version row. I checked this against dl24 S4 and "The checks, in order".
- **Spec 38's `coverage-lens` schema form is still unstated.** S9 passes no `--field`, and neither the items nor spec 16 say whether the form is `fields` or `header`.

**Parent text that looks wrong (not edited)**
- tr18 still names no verb or flag for setting its columns, so "tr18's landed verb" stays unknown until built (rows 52, 63 and 85).
- dl12:113's example writes `returns` without `@<n>`, while dl24 F2 says dl12's rows take the suffix.

Files are in C:/projects/coding-governance/.claude/worktrees/vigilant-einstein-2d0f7d/memory/builds/dIndexedDesign/spec/:
- 2026-10-28-spec-TOOL-dIndexedDesign-20.md
- 2026-10-28-spec-TOOL-dIndexedDesign-32.md
- 2026-10-28-spec-TOOL-dIndexedDesign-34.md
- 2026-10-28-spec-TOOL-dIndexedDesign-38.md
- 2026-10-28-spec-TOOL-dIndexedDesign-46.md
- 2026-10-28-spec-TOOL-dIndexedDesign-52.md

## Follow-up, led by spec 8 (specs 8, 10, 11 and 13), from the brief [`2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-reground-followup`](../prompts/2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-reground-followup.md)

I've finished the fold on all four specs (8, 10, 11 and 13). Three of the four item parts are done in full. The fourth, placing spec 8's `[[record-version]]` row, is refused because no unit has the row it would hash, and I'm returning it to the main loop as an item.

## What moved

Each spec keeps its 2026-11-05 rev and date on its Status line. Each one's 2026-11-05 §9 line is extended and ends with the follow-up brief's path.

- **TOOL-dIndexedDesign-10** (rev-3): S1's playbook `--purpose` drops from 198 bytes to 114. It now reads "a playbook: dScriptedRepeat's twelve-section canon and declaration block, followed by recipe-mode runs and repeats". AC6 only says "its purpose" and doesn't quote the text, so no AC moved.
- **TOOL-dIndexedDesign-11** (rev-2): S5's playbook-set `--purpose` drops from 132 bytes to 115. It now reads "a playbook run's set record: its pieces joined by hash, the set identity derived from them, a verdict per set check". AC7 doesn't quote it.
- **TOOL-dIndexedDesign-13** (rev-3): S1's `seams` `--purpose` drops from 137 bytes to 117. It now reads "a reuse scout's return: needs, sketch, anchors, census, up to twelve seams and five MUSTs, unmet needs, seams as rows". AC6 doesn't quote it.
- **TOOL-dIndexedDesign-8** (rev-4):
  - S11's `returns` is now `record-kind.feature-design@1`, the form TOOL-dDeclaredLoop-24 §4 "Records at a version" gives (dl24:144-145, its F2).
  - The external edge now cites dl24 §4.
  - §4 "What it does not check" now names the unpinned version.
  - AC8 now reads the `@1` and goes red on a `returns` with no `@<n>`.

## Refused: where spec 8's `[[record-version]]` row goes

No unit's pass adds this row, because there is nothing for it to hash:
- dl24:155 says: "The check recomputes each `fields` hash from `tools/memory-tree/build_records.py`'s kind row."
- PLAY-dOrderedCharter-42 S2 (its spec, lines 40-43) refuses `build_records.py` at import when its per-kind table's keys differ from `TYPED_RECORD_KINDS`.
- TOOL-dIndexedDesign-32 S2 (lines 53-57) makes `feature-design` untyped, "never `TYPED_RECORD_KINDS`". Its only per-kind row, added in its S1, is for `fork`.

So the model spec 20 S10 / spec 34 S3 use has no counterpart here. Spec 8 S11 now says that, and that the pin waits on the parent. Before it's pinned:
- dl24 S4 names no check that reds a `returns` with no version row.
- A grep over `memory`, `tools` and `skills` found no input naming `record-kind.feature-design`.

**Item for the main loop:** TOOL-dDeclaredLoop-24 §4 needs a hash source for an untyped record kind's version, for example its `record-kinds.toml` `fields` schema. Until it has one, `record-kind.feature-design@1` can't be pinned. That's the parent's decision, so I didn't open a fork.

## Checks

- **Sizes** (`wc -c`): spec 8 is 36,971 bytes, 10 is 26,316, 11 is 24,144 and 13 is 29,596, all under 49,152.
- **Purpose lengths:** I re-measured every `--purpose` in specs 8, 10, 11 and 13. All are 120 bytes or fewer.
- **Hygiene gate:** I ran `check-memory-hygiene.sh --staged` over a uniquely named copy of the index with only these four specs staged. It exits 1, on check 9 only, which `gen_build_index.py --write` fixes, so I left it for you:
  - "render owed under --staged" names spec 10.
  - The stale files are `memory/LIVE.md` and the dDeclaredLoop, dIndexedDesign, dLinkedLibrary, dPlacedRequest, dRankedPlan and dTotalRecall READMEs.
  
  No other check names these specs. I deleted the index copy and my scratch files, and the real index has nothing staged.

## Parent text that looks wrong (not edited)

- TOOL-dDeclaredLoop-24 §4 hashes versions only over `build_records.py`'s kind rows. That table holds only typed kinds, so an untyped record kind's `returns` can never be pinned. This is the refused item above.

Files revised, in `C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dIndexedDesign\spec\`:
- 2026-10-28-spec-TOOL-dIndexedDesign-8.md
- 2026-10-28-spec-TOOL-dIndexedDesign-10.md
- 2026-10-28-spec-TOOL-dIndexedDesign-11.md
- 2026-10-28-spec-TOOL-dIndexedDesign-13.md
