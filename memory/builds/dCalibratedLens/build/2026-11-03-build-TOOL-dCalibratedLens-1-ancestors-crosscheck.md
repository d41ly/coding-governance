**Serves:** research TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-42

# dCalibratedLens's specs against dTotalRecall's and dDeclaredLoop's specs: a read-only cross-check

Node d, 2026-11-03, base `0d1c1dda4` (origin/main, dShippedRelease's landing). This is the second pass
the first-pass record
[`2026-11-03-build-TOOL-dCalibratedLens-1-parents-crosscheck`](2026-11-03-build-TOOL-dCalibratedLens-1-parents-crosscheck.md)
recommended for the two deeper ancestors it scoped out, run on the owner's "rest with
recommendations" the same day. Since the spec base `22a8efac3`, `git diff --name-only` over both
builds' `spec/` names two files: TOOL-dTotalRecall-2 (rev-7 in `66f7b8d32`, rev-8 in `58b395b6e`) and
TOOL-dTotalRecall-1 (rev-5 in `58b395b6e`). No dCalibratedLens spec cites tr2, and no row below rests
on a tr1 line those commits moved. This record is not an audit: no spec was edited to write it. The
mismatches feed the re-ground brief
[`2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-reground`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-reground.md).

**Counts:** 159 assumptions · 110 AGREES · 41 MISMATCH · 8 UNKNOWN UNTIL BUILT, over the 24 citation
specs. 16 specs hold at least one MISMATCH: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 16, 19, 20 and 42.
By rule: 124 citation, 27 RB, 8 ask (one marked `cite / ask`). Every MISMATCH is pre-existing: the
ancestor text already read so at `22a8efac3`.

## Method

- **Population by citation.** Every spec matching `TOOL-dTotalRecall-<n>`, `TOOL-dDeclaredLoop-<n>`,
  the bare forms or a continuation list, outside the generated records tables: 24 specs. The
  name-only mentions (cl1:40, :108, :128, :436-441; cl3:325, :527-530; cl5:147; cl6:80, :286,
  :338-342; cl7:93; cl19:122; cl20:75; the H1 lines of cl32 and cl42) were assumptions too.
- **Checks riding the citations.** The asks a spec relies on (`ask`), and RB: a fact a spec states
  about a file at base that a cited ancestor unit's §2 changes. The first pass's RH rule was not
  re-run, since `0d1c1dda4` moves no row it read.
- **Readers.** Five `gov-spec-reviewer` agents, read-only, at effort medium, one per group of the
  brief [`2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-crosscheck`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-crosscheck.md),
  with their handoffs beside it. Their returns are
  [`2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-returns`](2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-returns.md).
- **The main loop** assembled the table below from the returns' tables by script, sorted by spec, and
  derived the counts from it, changing no verdict. Where a reader's prose count differs from its
  table, the table wins: A's opening says 21 AGREES and 9 MISMATCH, and its table holds 22 and 8 (its
  `find --all` row is an `ask` row); B's says 6 MISMATCH and 3 UNKNOWN, and its table holds 7 and 2
  (one UNKNOWN is a section 3 line only); E's says 15 MISMATCH, and its table holds 14.
- **Aliases:** `clN:L` is line L of `spec/2026-11-0?-spec-TOOL-dCalibratedLens-N.md`. `trN` and `dlN`
  are the same for dTotalRecall and dDeclaredLoop, and the first pass's aliases hold for any other
  build. All are read at `0d1c1dda4`.

## Classes

- **An ask the spec relies on that no BACKLOG holds (7 rows: 7, 13, 26, 50, 77, 86, 130).** Specs 1, 3,
  6 and 16 say "the main loop files" an ask, and spec 20 files one only if its AC goes red. None was
  filed. Spec 13's verb is a fork the owner has not picked (dl26 §8 F5 OPEN), and spec 9's `find --all`
  is dWellOiledMachine's own ask (wm32 F6).
- **`unarmed` outlives its population (5 rows: 20, 30, 38, 126, 134).** TOOL-dTotalRecall-42 S2 reds a
  row carrying `unarmed` once its home matches a file. No spec drops the key when its first record
  lands, and the plants that commit a record expect exit 0.
- **`TYPED_RECORD_KINDS` tied to the factory form (3 rows: 16, 31, 131).** PLAY-dOrderedCharter-42 S2
  and S3 tie the tuple to `build_records.py`'s per-kind table and the `-<kind>-<n>.md` name, which a
  `memory/loop-review/` record does not take.
- **dl12's row form (3 rows: 11, 24, 40).** A non-role actor's item row needs `inputs`, `allowance`,
  `returns` as `record-kind.<name>`, and `witness`.
- **dl27's `+`-joined scenario list (2 rows: 94, 110).** A transition record's `scenario=` is the
  placed list, not one tag.
- **A surface read from the wrong unit or section (the rest).** Among them: cl1's breakpoint caller and
  Maintain boundary, cl16's draw-row semantics against dl30, cl20's kind read against tr53 S21, and a
  handful of citations to the wrong section.

## Table

| # | Spec | Group | Assumption about the ancestor | Rule | Verdict | Evidence |
|---|---|---|---|---|---|---|
| 1 | 1 | E | `--trigger` is dl20 S2's verb in `unattended.sh`: `--trigger <slug> --subject <s> --cause <c>`, takes no `--stage`, passes opt-in and unclassed to `review_pin.py`, prints that line with `trigger` and `blocks` added. cl1 adds `--stage` and `efforts` | cite | AGREES | cl1:83-86, :206-208, :410 · dl20:51-57, :137-144 |
| 2 | 1 | E | The key set the `--trigger` line prints is `{"preset","optIn","trigger","blocks","efforts"}` | cite | MISMATCH | cl1:209 · dl20:281 |
| 3 | 1 | E | dl19 S6 has a "firing site" that passes the step segment of the breakpoint's `position` tag, written `item.<step>.<name>`, as `--stage` | cite | MISMATCH | cl1:87-88, :205 · dl19:64-65, :100-101, :140-146 |
| 4 | 1 | E | A Maintain review runs where `review.breakpoints` (dl19 S4) places a breakpoint at an `item.maintain.*` boundary; "dDeclaredLoop places a review breakpoint for each stage" | cite | MISMATCH | cl1:40, :104-106, :434-435 · dl19:54-57 · dl1:57 · `grep -rn "item\.maintain" memory/builds/dDeclaredLoop/spec/` printed nothing · tc1:58-60 |
| 5 | 1 | E | `derive_breakpoints` reads `review.<stage>` for five stages and never `review.maintain` | cite | AGREES | cl1:107, :433-434, :442-443 · dl19:43-45, :126 |
| 6 | 1 | E | `review.<stage>` defaults to `opt-in`, so no stage lens fires until the stage opts in or is owed | cite | AGREES | cl1:113-114 · dl19:44-45, :148-150 |
| 7 | 1 | E | §8 F4's ask "DERIVE_BREAKPOINTS READS NO REVIEW.MAINTAIN" is to be served by dDeclaredLoop | ask | MISMATCH | cl1:128, :440-445 · `memory/builds/dDeclaredLoop/BACKLOG.md:5-13` holds asks 35 and 101-108; `grep -n -i maintain` there printed nothing. dl19 neither serves nor refuses it |
| 8 | 1 | E | AC9's fixture is "the `--trigger` fixture TOOL-dDeclaredLoop-20 lands in the unattended kit's suite" | cite | UNKNOWN UNTIL BUILT | cl1:390-391 · dl20:332-335 |
| 9 | 1 | E | Files touched vs dl19/dl20 §2. Shared files: `unattended.sh`, `unattended.test.sh`, `VERBS.template.md`, `tier2-review.template.js`, `tier2-review.test.sh`, `tools/workflows/README.md`. cl1's facts about the template at base are line regions (`:260-277`, `:356-360`, `:781-849`); dl20 S3 edits only `renderShapeLine` (`:78-83`) and adds arguments | RB | AGREES | cl1:141-142, :340 · dl20:58-61 · dl19:209-218 |
| 10 | 2 | D | dl1 gives the loop kit `tools/loop/`, its `kit.toml` and `loop.toml` | cite | AGREES | cl2:47-48, :156 · dl1:54-61 |
| 11 | 2 | D | The `item.loop.price` row is "in the row form of TOOL-dDeclaredLoop-12 §4 'Data model'" with keys `step`, `actor`, `needs`, `outcomes`, `routes`, `returns`, `owner` | cite | MISMATCH | cl2:112-118 · dl12:105-130; dl9:29-34 |
| 12 | 2 | D | `check_program` grades the routes, and the `stand-in:<path>` route word is legal; `loop_lib.py --check` runs it | cite | AGREES | cl2:115, :266, AC8 :435-438 · dl12:39-44, :145-153 |
| 13 | 2 | D | AC8 passing depends on "the ask F5 states" (cl3 §8 F5, filed on dDeclaredLoop) | ask | MISMATCH | cl2:323-325; cl3:529-534 · `grep -n 'CADENCE' memory/builds/dDeclaredLoop/BACKLOG.md` prints nothing (0 of 26 lines); `grep -rn 'CADENCE STEP VALUE'` hits only cl3:530 |
| 14 | 2, 4 | D | The leg is claimed by a new dossier `memory/map/features/loop-review.md` "(new when no dossier claims `tools/loop/`)" | RB | MISMATCH | cl2:318-322, :362; cl4:244-246, :263 · dl1:85, :260, :318; dl3:237 |
| 15 | 2 | D | dl1 provides `record-kinds.toml` and its `record-kinds` leg; `check = "record-kinds"` names that leg | cite | AGREES | cl2:50, :156, :241 · tr1:66-70, :78-86 |
| 16 | 2 | D | `value-ledger` joins `TYPED_RECORD_KINDS`, its snapshot at `memory/loop-review/<date>-value-ledger-<key>.md` | cite | MISMATCH | cl2:279-283, :359, :97 · tr1:71-77, :222-224; dOC42:35-49 |
| 17 | 2 | D | `record_kinds.py --write` renders the `gen:record-kinds` region, then `--render` copies it (tr1 S6) | cite | AGREES | cl2:309-312 · tr1:92-95, :230-236 |
| 18 | 2 | D | Writer cell `loop_review.py price; loop_review.py record` (tr1 rev-5, the `hand` rule) | cite | AGREES | cl2:303-304 · tr1:195-200, :414-417 (applies to `hand` rows only) |
| 19 | 2 | D | Home `memory/loop-review/*-value-ledger-*.md`, spelled as tr42 S1 spells the shape-run home | cite | AGREES | cl2:275-277 · tr42:36-39 |
| 20 | 2 | D | The row carries `unarmed` "until `loop_review.py record` lands the first period" | cite | MISMATCH | cl2:305-308 · tr42:40-46 |
| 21 | 2 | D | tr42 S5 grades the snapshot by its own row | cite | AGREES | cl2:282-283 · tr42:53-59 |
| 22 | 2 | D | `record-kinds.toml`, `HYGIENE.template.md`, `loop.toml`, `kit.toml`: rows or regions are added and no at-base fact is relied on | RB | AGREES | cl2:349-355 · tr1:66, :92-95 and dl12:34-37 are additive |
| 23 | 3 | E | dl12 supplies the `[[item]]` rows, `check_program`, `order_by_needs` with its inline `needs_graph_py` block, and `read_items(kit_dir, step=…)` | cite | AGREES | cl3:54, :319, :563 · dl12:36-37, :40-46, :48-53 |
| 24 | 3 | E | The four `item.loop.*` rows are "in TOOL-dDeclaredLoop-12's data model" as §4 "The items" lists them: actor, needs, outcomes and routes, witness | cite | MISMATCH | cl3:59-60, :209-217 · dl12:127-128 · dl50:35-36 |
| 25 | 3 | E | dl50 S3 admits only `step = "none"`, and only on `item.review.*` rows | cite | AGREES | cl3:524-525 · dl50 S3 (`check_program` admits `none` for those rows alone) |
| 26 | 3 | E | §8 F5's ask "THE LOOP KIT REFUSES A CADENCE STEP VALUE" is to be served by dDeclaredLoop (named again at :325) | ask | MISMATCH | cl3:325, :530-534 · `memory/builds/dDeclaredLoop/BACKLOG.md:5-13`; `grep -n -i cadence` printed nothing. dl12:108 and dl50 S3 refuse the value today |
| 27 | 3 | E | `item.loop.record` routes `recorded → transition` | cite | UNKNOWN UNTIL BUILT | cl3:217 · dl12:42 |
| 28 | 3 | E | tr1's registry: column order, `tag = record.<name>`, `writer` is a door command, `check` names the `record-kinds` leg. tr1 rev-5's `hand` change does not reach this row | cite | AGREES | cl3:55, :247-258, :567 · tr1 S1, S3, §4 writer bullet |
| 29 | 3 | E | id 1: `home` is the id-rule's glob "as TOOL-dTotalRecall-42 S1 spells the shape-run home" | cite | AGREES | cl3:285-287 · tr42:41-43 |
| 30 | 3 | E | id 37: the row carries `unarmed = "no record is tracked until the first period's record lands"`, and the record lands later through a patch build (S8) | cite | MISMATCH | cl3:327, S8 · tr42:40-44 |
| 31 | 3 | E | id 36: `loop-review` joins `TYPED_RECORD_KINDS` and HYGIENE's closed `<kind>` list | cite | MISMATCH | cl3:288-290 · tr11:53-57 · `PLAY-dOrderedCharter-42:40-44` |
| 32 | 3 | E | Files touched vs dl12, tr1, tr42 §2 (`loop.toml`, `record-kinds.toml`, `HYGIENE.template.md`, `memory/HYGIENE.md`): no fact about these files at base is stated that those units' scopes change | RB | AGREES | cl3 Files touched · dl12, tr1, tr42 Files touched |
| 33 | 4 | D | `python tools/loop/policy_edit.py propose <key> <value>` writes nothing and prints the row diff and the command (dl2 S4) | cite | AGREES | cl4:45-51, :107-110, :119, :198, :408 · dl2:61-63, :208 |
| 34 | 4 | D | `raise` condition 1 is the working tree's file over the old value (dl2 §4) | cite | AGREES | cl4:267-270, :366-371 · dl2:209-215 |
| 35 | 4 | D | "The command's own guard (TOOL-dDeclaredLoop-2 S1) is untouched" | cite | AGREES | cl4:279-280 · dl2:44-50 |
| 36 | 4 | D | `tools/loop/kit.toml` and `gate-legs.json` get rows; the at-base facts about `tools/policy/guard.py:141` and `check_raise_shape` | RB | AGREES | cl4:97, :257-258, :415-417 · dl2:102 and Files touched (dl2:310-329) add rows, and dl2 wraps `tools/policy/guard.py` without editing it |
| 37 | 5 | B | The registry `record-kinds.toml` and `record_kinds.py` are tr1's; the keep row's columns are tr1 S1's, and its writer is a door (cl5:48, :157, :246-260, :277, :468) | cite | AGREES | tr1:66-71 (S1), :78-89 (S3), :195-200 (writer bullet, rev-5: `hand` is legal on rows tr2 S9 does not move, and keep's writer is `loop_review.py keep`, not `hand`) |
| 38 | 5 | B | The keep row carries `unarmed = "no keep is tracked until the owner's first keep"`, and AC9 has `record_kinds.py --check` exit 0 in a scratch worktree holding one well-formed keep record (cl5:317-319, :463-466, by name) | cite | MISMATCH | tr42:40-46 (S2): the check "reds the row, naming the key, once its home matches a file, so the declaration cannot outlive its population" |
| 39 | 5 | B | The keep record is graded by its own row through its `Serves: keep` line, and the home is the id-rule's glob (cl5:286-290) | cite | AGREES | tr42:50-58 (S4 refuses a bare directory; S5 `derive_record_kind`) |
| 40 | 5 | B | `item.loop.propose` is "in TOOL-dDeclaredLoop-12's row form" with `step = "cadence.loop"`, `actor`, `needs`, `outcomes`, `routes`, `returns = "proposals"`, `owner` (cl5:121-125) | cite | MISMATCH | dl12:113 (`returns` is "the record kind it writes", `record-kind.<name>`), :127-130 (`inputs`, `allowance` and `returns` required for a non-role actor; `witness` required); dl50:44-48 admits only `step = "none"`, on `item.review.*` rows; dDeclaredLoop BACKLOG.md (26 lines) holds no cadence-step ask |
| 41 | 5 | B | "dDeclaredLoop's breakpoints call `keep` once they land" (cl5:147, by name) | cite | MISMATCH | dl19 S1-S7 (breakpoints) and dl20 hold no call to `loop_review.py keep`; an owner gate is released by "the owner's disposition record" (dl19 S6). `grep -n "loop_review\|keep record"` over the dDeclaredLoop specs: no hit |
| 42 | 5 | B | RB `record-kinds.toml`, `HYGIENE.template.md`, `tree_lib.py` `TYPED_RECORD_KINDS`: a row, the closed `<kind>` prose list and a tuple member are added; the registry view is regenerated by `record_kinds.py --write` | RB | AGREES | tr1:84-85 (S2), :92-96 (S6 adds a new `gen:record-kinds` section and leaves the `<kind>` prose list at HYGIENE.template.md:628 authored), :241-243 |
| 43 | 6 | B | tr9 S6 reads `measured` as 96,000 B for every role until 30 sliced work orders, names no reading after, and hands each role's p90 to the Loop Review; that is "tr9's reading today" (cl6:26-29, :104-106, :149-150) | cite | AGREES | tr9:110-111, :142, :359-361 (F4) |
| 44 | 6 | B | tr9 S8 has `render_handoff` write a `reads:` list, one key per line with its bytes, the only writer of a work order's slice bytes (cl6:38-40, :106, :320-323) | cite | AGREES | tr9:119-122 ("one key per line with its bytes and any mark") |
| 45 | 6 | B | The `reads:` list stays a block of its own whose lines S1 parses as `<key> <bytes>`, and a work order with no such block is unsliced (cl6:36-42) | cite | UNKNOWN UNTIL BUILT | tr9:121-122 gives no line grammar beyond "bytes and any mark"; dTotalRecall BACKLOG.md:22 (tr104, open) asks that the list be rendered as the body of the `### memory` slot through `render_slot` |
| 46 | 6 | B | "TOOL-dTotalRecall-9 §4 treats it as the work order" (cl6:107-109) | cite | MISMATCH | tr9 §4 (:167-262) says nothing about it; it is tr9 S8 :119 and §10 :398-399 |
| 47 | 6 | B | `check_read_set` lives in `record_find.py`, run as `gov_record.py budget --role`; over the cap under `report` it prints `memory over budget: <role> <bytes> B > <cap> B` (cl6:63-64, AC7 :291-295) | cite | AGREES | tr9:108-114 |
| 48 | 6 | B | "`record_find.py` and `gov_record.py` are TOOL-dTotalRecall-9's" (cl6:301) | cite | MISMATCH | tr9:151-152: `gov_record.py` is TOOL-dTotalRecall-2's door; tr9 adds only the `find`, `show` and `budget` verbs |
| 49 | 6 | B | dTotalRecall is the key's owner, and tr9 S6 already reads "a per-role value" (cl6:80, :337-343) | cite | AGREES | tr9:17 (`Carries: node:policy-key.memory.item-budget`), :111; catalogue.toml at `8bec4cef` :1457-1461 (`owner = "dTotalRecall"`) |
| 50 | 6 | B | Ask F4, THE ITEM BUDGET HAS NO PER-ROLE FORM, is filed in `memory/builds/dTotalRecall/BACKLOG.md` and lands before this unit's pass; S3, S5 and AC5 rely on it (cl6:51, :80, :87, :145, :286, :337-349) | ask | MISMATCH | The BACKLOG holds tr27-35 and tr101-106 and no such row; `git grep -n -i "per-role form\|item budget has no" 0d1c1dda4 -- memory` matches only cl6 itself. tr9 neither serves nor refuses it: S10 :130-133 adds only `summary` and `usage` |
| 51 | 6 | B | The slice manifest has no producer: tr12 S9 hands it to dWellOiledMachine's executor, ask tr35 is still open, and tr12 reads the channel `unarmed` until then (cl6:81-82, :317-319, :379) | cite | AGREES | tr12:54-55, :83-85, :108; dTotalRecall BACKLOG.md:13, :39-40 |
| 52 | 6 | B | The owner writes through `policy_edit.py set` at a terminal; `propose <key> <value>` writes nothing and prints the row diff and the command (cl6:57-62, :78-79, :93, :143) | cite | AGREES | dl2:61-68 (S4), :206-208 |
| 53 | 6 | B | Under the default guard, an agent's staged `memory.item-budget` change is refused (cl6:239-242, by name) | cite | AGREES | dl2:44-50 (S1), :190 (`owner-only`: "every other write refused") |
| 54 | 6 | B | RB `tools/roles/handoff.py`: `render_handoff` at `:312`, verbs `check` and `roster`, `MARKER_RE`; tr9 S8 changes `render_handoff` and its CLI, and cl6 names it | RB | AGREES | tr9:119-125 adds `--read` and the list only; at `8bec4cef` `handoff.py:942` `render`, `:955` `check`, `:956` `roster`; `roles_lib.py:79` |
| 55 | 6 | B | RB `tools/memory-tree/record_find.py`: S6 adds `read_measured_item_budget` beside tr9's `check_read_set`, and names tr9 S6 | RB | AGREES | tr9:108, :238 (new file); no at-base fact is stated |
| 56 | 6, 8 | B | Ask tr35 (the slice channel has no producer) is a BACKLOG row of dTotalRecall | cite | AGREES | dTotalRecall BACKLOG.md:13, :39-40 (DEFERRED until tr12) |
| 57 | 7 | C | tr11 registers the `shape-run` kind. Its record is `<date>-build-<unit id>-shape-run-<n>.md`, with `Kind` to `Out-tokens` and `Caused-by` required, and `Trigger`/`Shape`/`Efforts`/`Role-sha` present only when the line carries them. Its writer is `gov_record.py new shape-run --review`. | cite | AGREES | cl7:31-33, :88-90, :225; tr11:60-65, :155-162, :176 |
| 58 | 7 | C | S1 reads `builds/*/build/*-shape-run-*.md` and takes each record's date from the file name's `<date>` | cite | AGREES | cl7:39-41; tr42:36-38, :89; tr11:176 |
| 59 | 7 | C | `Kind` is `spec-audit` or `diff-review`. `Out-tokens` is a number or `unknown`. A count may read `-` and never means 0. | cite | AGREES | cl7:44-49, :50-53; tr11:121, :126, :130-131 |
| 60 | 7 | C | dl20 S3 appends `trigger=` `shape=` `efforts=` `role-sha=`, with `shape=` reading `-` until dBoundRoles lands its registry | cite | AGREES | cl7:34-35, :45-47, :86-87; dl20:59-62, and dl20 §4 "The record line" |
| 61 | 7 | C | `review.cost` (dl20 S3) writes the shape-run records for review acts and is one of the kind's "two writers" | cite | MISMATCH | cl7:25-26, :60-61, :66-67, :166; dl20:59-62, :130; tr11:60, :91-93; tr42:45, :91 |
| 62 | 7 | C | tr11 S1 makes `shape_run.py` the line's one parser. `check_shape_runs` compares each record with its line. The CLI parses lines, not records. | cite | AGREES | cl7:141-144, :232-234; tr11:46-52, :66-69 |
| 63 | 7 | C | The act form (`--act`, `Kind` `act`, `Workflow` `Shape` `Shape-match` `Agents` `Efforts` `Out-tokens` `Caused-by`) is an ask filed on dTotalRecall. Note: the ask is named at cl7:93 (§4 Evidence, as wm19 §8 F2), not at cl7 §8 F2, which is about catches. | ask | AGREES (the row exists and says it; tr11 neither serves nor refuses it) | cl7:35, :91-93; dTotalRecall/BACKLOG.md:15 (TOOL-dTotalRecall-105, required `Workflow`, `Shape`, `Shape-match`, `Agents`, `Out-tokens`, `Caused-by`, optional `Efforts`...), :43; tr11:60 (`--review` only), :121 (closed `kind` set) |
| 64 | 7 | C | RB: cl7 states facts about `renderShapeLine`, the `-` rule and output-only tokens (`tier2-review.template.js:74-86`). dl20 §2 S3 changes that function, and cl7 names dl20 S3 at :86. tr11 S7 changes `tier2-review.test.sh` and `README.md`, which cl7 states nothing about. | RB | AGREES | cl7:84-87, :163-164; dl20:59-62; tr11:79-85; `git show 8bec4cef:tools/workflows/tier2-review.template.js` :74-86 matches cl7's account |
| 65 | 8 | B | `review.dispose`'s module is `tools/loop/review_dispose.py`, and the DISPOSAL stage in `unattended-build.template.js` runs `review_dispose.py classes` (cl8:45-46, :82-85, :127, :327) | cite | AGREES | dl20:74-78 (S6), :190-195, :238 |
| 66 | 8 | B | `review_dispose.py classes` "reads `disposition` by name as well (TOOL-dDeclaredLoop-20 §4)" (cl8:141-142) | cite | UNKNOWN UNTIL BUILT | dl20:190 says only that it "reads every review record's disposition column"; it says neither by header name nor by position |
| 67 | 8 | B | The map and its renderer are tr14's (cl8:109) | cite | AGREES | tr14:46-50 (S2 `gov_map.py`), :37-44 (Goal) |
| 68 | 8 | B | The map's pre-build losing test is tr17, whose `lose` files the slice-manifest-only ask on dCalibratedLens (cl8:110) | cite | AGREES | tr17:65-70 (S7), :144-145 |
| 69 | 8 | B | On `lose`, S3 "already computes the cause without the map", so the tr17 ask is served (cl8:110-112) | cite | MISMATCH | tr17:68-69: the ask is "compute its not-in-view cause from the slice manifest alone"; cl8 S3 (:56-63) counts every `ORDER_SLOTS` slot's paths (`code`, `bug-classes` and others) |
| 70 | 8 | B | No spec writes a slice manifest: tr12 S9 hands it to dWellOiledMachine's executor, and tr9 §3 to dBoundRoles' renderer (cl8:131, :314-316) | cite | AGREES | tr12:83-85, :96-97; tr9:137-138 |
| 71 | 8 | B | A `cause` verb on `review_dispose.py` would need a second appendix parser, since the loop kit imports no sibling (cl8:327-330, F3) | cite | AGREES | dl20:77-78, :190 (`review_dispose.py` sits in the loop kit, `tools/loop/`, and reads the disposition column itself) |
| 72 | 8 | B | RB `unattended-build.template.js` and its render: dl20 §2 S4, S5, S7 and S8 change the DISPOSAL stage and the fold instruction; cl8 states no at-base fact about them and names dl20 S6 for the call it sits beside | RB | AGREES | dl20:64-73, :84-87, :238-239; cl8 S5 :82-86 |
| 73 | 8 | B | RB `tools/workflows/README.md`: dl20 and cl8 each add a name | RB | AGREES | dl20:240; cl8:233; no at-base fact is stated |
| 74 | 8 | B | RB `tools/roles/handoff.py`: `orders` sits beside `roster` (`:956`), markers are read through `MARKER_RE` (`roles_lib.py:79-80`); tr9 S8 (cited in F2) changes only `render` and its list | RB | AGREES | tr9:119-125; `8bec4cef` `handoff.py:956`, `roles_lib.py:79-80` |
| 75 | 8 | B | RB `tools/workflows/replay_scorer.py`: `parse_appendix_rows` keeps its confirmed-only filter; tr17 S1 adds a `map-replay` row to `INSTANCES` and touches no parser | RB | AGREES | tr17:33-40 |
| 76 | 9 | A | The record door's `find` and `show` (tr9 S3, S5). `show <key>` gives the whole record, and `find` stops at 40 rows. | cite | AGREES | cl9:46-48, :54-55, :121, :189-191; tr9:89-96, :104-107 |
| 77 | 9 | A | `read_act_records` runs over "the uncapped `find --all`". | ask | MISMATCH | cl9:43-45, :199; tr9:89-96 has no `--all`; wm32:318-329; `grep -n -- '--all' dTotalRecall/BACKLOG.md`: no hit |
| 78 | 9 | A | `position.py <slug> --json` (dl7). | cite | AGREES | cl9:327-330; dl7:61-63 |
| 79 | 9 | A | tr11 lists `probe.run` among the shape-run writers, and a shape-run record holds "no token cost". | cite | MISMATCH | cl9:367-369; tr11:91-93, :175-179 (`"Out-tokens"` is a schema field) |
| 80 | 9 | A | The `compactions` line's item tags are `item.build.unit` and `item.review.synth` (by name). | cite | MISMATCH | cl9:158; neither tag is in any dDeclaredLoop spec (grep: the build's tags are `item.build.unit-pass`, and dl20's six `item.review.*`: trigger, pin, report, dispose, fold, cost) |
| 81 | 9 | A | Shared file `tools/loop/README.md` (dl7). cl9 states no at-base fact about it. | RB | AGREES | cl9 Files touched; dl7 Files touched |
| 82 | 10 | A | tr17 is a scorer instance, not an eval over instruction units. | cite | AGREES | cl10:463-465; tr17:34-35 |
| 83 | 10 | A | Shared files `replay_scorer.py` and `tools/workflows/README.md` (tr17 adds the `map-replay` row). cl10 states no instance count. | RB | AGREES | cl10 Files touched; tr17:34, :140-141 |
| 84 | 11 | A | "TOOL-dDeclaredLoop-32's bound counts both", and a fix pass's rounds reach `route-backs-per-build` "only where they are recorded as review rows". | cite | MISMATCH | cl11:231-232; dl32:63-71, :198-200 |
| 85 | 11 | A | `REVIEW_EXITS` (`tools/runlog/model.py:110`) ends a loop. dl32 edits `model.py`. | RB | AGREES | cl11:130; dl32:198-199 change only `PARK_KINDS` (`model.py:98`); `model.py:110` read |
| 86 | 13 | A | dl26 §8 F5's `compose` verb on `overlay_rows.py` is a specced precondition, and S3 reaches `compose_rows` through it. | cite / ask | MISMATCH | cl13:44-46, :66-70, :133; dl26:280-291 ("OPEN for the owner"; "The ask the build run would file is that verb"); `grep -rln overlay_rows */BACKLOG.md`: no hit |
| 87 | 13 | A | dl20 S2 reads `review.opt-in` one member per line. | cite | AGREES | cl13:337-338; dl20:54-55 reads through `policy.py get`; `policy.py:1347-1348` ("a list one member per line") |
| 88 | 13 | A | The item and stage kinds keep their step-gate class functions in their own kit's module (dl24 S7, dl25). | cite | AGREES | cl13:353-357; dl24:64-67, :184-187, :203-207 (`loop_items.py`); dl25:64-65, :193 (`splice.py`) |
| 89 | 13 | A | dl27 S1 and S2 are the template for the kind and namespace rows. | cite | AGREES | cl13:362, :378-380; dl27:36-49, :131-152 |
| 90 | 13 | A | Shared files `kinds.toml`, `namespaces.toml`, `tag_index.py`, `surface-classes.toml`, `gate-legs.json`, `subject-pins.tsv` and `kinds.md` (dl24, dl25, dl27). Every change there adds a row or an extractor. | RB | AGREES | cl13 Files touched; dl24:203-210; dl25:207; dl27:233-244 |
| 91 | 14 | A | `--trigger <slug> --subject <s> --cause <c>` is dl20 S2's verb in `unattended.sh`. It reads policy through `policy.py get` and passes `--opt-in` to `review_pin.py`. cl14 S2 widens it, and AC4's fixture is the one dl20 lands in `unattended.test.sh`. | cite | AGREES | cl14:43-45, :124, :306-312, :362; dl20:51-57, :139-144, :332 |
| 92 | 14 | A | AC4: with `review.opt-in` filling the slot, the `--trigger` JSON line carries the swap. | cite | UNKNOWN UNTIL BUILT | cl14:306-310; dl20:54-55, :142-143 pass `get`'s output as `--opt-in`; `policy.py:1347-1348` prints a list one member per line; catalogue.toml:417-422 makes the key a `set`; fh3:67-69 reads a JSON map |
| 93 | 14 | A | dl28's rows: `rescope · flow <act> <row tag> · change <stem>` and `flow-state <row tag> · applied`. A held or refused change is not carried. `After` is `<tag>@<hash8>` over the canonical form, so one row gives one `After`. | cite | AGREES | cl14:51-57, :143-145; dl28:37-43, :44-50, :58-67, :116-119 |
| 94 | 14 | A | A carrier's `scenario=` field gives "the scenario its build ran", one tag, and that tag fills the proposed row's `extends`. | cite | MISMATCH | cl14:55-56, :177; dl27:80-83, :50-51 |
| 95 | 14 | A | The activatable kinds are `kind.item` or `kind.splice`. | cite | MISMATCH | cl14:60-62, :178; dl27:54-56 |
| 96 | 14 | A | `derive_step_scenarios` (dl27 §4) runs at a transition into a step, and a scenario changes only at a step boundary (S8). cl14 S9 adds promoted scenarios at that point. | cite | AGREES | cl14:81-88, :148-150, :272-273; dl27:86-88, :201-204, :215, :240-241 |
| 97 | 14 | A | `compare_path` (dl28 S7) can find "no `skip` against [the promoted scenario] over the steps already walked". | cite | MISMATCH | cl14:84-86, :401-405; dl28:73-77, :154-157 |
| 98 | 14 | A | A row inherits `admits`, `entry` and `then` from its `extends` (dl27 §4). | cite | AGREES | cl14:181-183; dl27:186-187 |
| 99 | 14 | A | Gov's pack has one writer, `core.py new scenario`, which writes the pack only (dl27 S1). dl27 and dl28 both leave promotion to a later program. | cite | AGREES | cl14:111-113, :388-394; dl27:36-45, :108; dl28:93 |
| 100 | 14 | A | Re-picking a scenario between placement and close belongs to dl27's `then` edges and to dPlacedRequest. | cite | AGREES | cl14:114-115; dl27:86-88, :104-105 |
| 101 | 14 | A | The `loop scenario fixtures` leg (dl27 S10) and `scenario.py --fixture --plant <case>`. | cite | AGREES | cl14:337, :356-359, :365; dl27:92-97 |
| 102 | 14 | A | `help/loop.md` is dl1 S7's page. | cite | AGREES | cl14:92-94; dl1:85-87 |
| 103 | 14 | A | The owner's disposition record (dl16) lives in a build's folder under a unit id. | cite | AGREES | cl14:384-386; dl16:45-47 |
| 104 | 14 | A | Shared files `unattended.sh`, `unattended.test.sh`, `scenario.py`, `help/loop.md` and `tier2-review.test.sh` (dl20 S2/S3, dl27, dl28 S2, dl1 S7). cl14's at-base facts: the `flow.promote` row as at base, `review_pin.py` reading only its arguments, the harness reading no policy. | RB | AGREES | cl14:136-138, :163-165; catalogue.toml:826-830; dl20:258 ("`review_pin.py` still checks the opt-in's shape only"); dl20's `reviewPolicy` goes to the build harness (dl20:81, :201), not tier2-review; `grep -l flow.promote` over both builds' specs: no file |
| 105 | 15 | A | tr12 S9 hands the slice manifest to dWellOiledMachine, where it is unspecced. | cite | AGREES | cl15:367-369; tr12:83-86, :96, :108 |
| 106 | 15 | A | Shared files `runlog.py`, `selftest.py` and `README.md` (tr12 adds the `memory` verb). cl15's facts: the `extract --ready` walk, and `read_records` / `resolve_projects_root` unchanged. | RB | AGREES | cl15:57, :371-372; tr12:51-62 reuse `read_records` (:308) and `resolve_projects_root` (:185) unchanged |
| 107 | 16 | D | An instance key is `<item tag>@<round\|pass>#<inputs>`, so the item is the text before `@` (dl7 S3) | cite | AGREES | cl16:64-65, AC3 :281-282 · dl7:45-49 |
| 108 | 16 | D | `read_transitions` exists and reads a build's transition records newest first (dl3 S7) | cite | AGREES | cl16:67, :122, :392 · dl3:69-73 |
| 109 | 16 | D | Each transition record gives a time and a commit, so S4 can take "the newest … at or before the line's `t`" and S8 can run `policy.py get --rev <the commit of its newest transition record>` | cite | UNKNOWN UNTIL BUILT | cl16:66-67, :88-91 · dl3:69-73 (return shape not stated); dl3:42-46 (fields `Build`, `From`, `To`, `Item`, `Sha`; `Sha` is the witness commit) |
| 110 | 16 | D | The `scenario` field of a transition record is one scenario tag, used as the tuple's scenario (`scenario.feature`) | cite | MISMATCH | cl16:65-67, AC3 :284-286, AC12 :320-321 · dl27:80-83 |
| 111 | 16 | D | Draw and freeze row grammar; `record_draw` returns `exhausted`; `budget_state` reads those rows (dl30 S2, S3) | cite | AGREES | cl16:139-141, :149, :348 · dl30:39, :43-51, :131, :135 |
| 112 | 16 | D | `flow.rework-budget` takes the form `<base>+<per-unit>` and both flow keys are `raise-loosens` | cite | AGREES | cl16:109-110, :149, :166 · dl30:32-36 |
| 113 | 16 | D | `flow.rework-budget` evidence is `max(0, spent - per_unit*units)` per build; AC7 plants spends of 3 to 32 under `4+2` with one unit | cite | MISMATCH | cl16:149, AC7 :298-304 · dl30:37-41, :49-50 |
| 114 | 16 | D | `flow.route-backs` evidence is "the most `route-back` draws one item took" | cite | MISMATCH | cl16:150 · dl30:62-63 |
| 115 | 16 | D | A build "ran under" `flow.rework-budget` when the value at its newest transition's commit equals HEAD's | cite | MISMATCH | cl16:88-91 · dl30:37-42 |
| 116 | 16 | D | A closed build's draw rows are fixed at close, so the first record after close keeps them and no later record re-reads them (S7, id 54) | cite | MISMATCH | cl16:81-87, :228-231 · dl30:67-71 |
| 117 | 16 | D | `policy_edit.py propose <key> <value>` writes nothing and prints the row diff and an apply command (dl2) | cite | AGREES | cl16:115, :165-166, :254-255 · dl2:61-63, :208 |
| 118 | 16, 4 | D | The proposal's `accept` is "the `policy_edit.py set` command propose printed", applied by the owner, for keys such as `flow.rework-budget` and `budgets."AGENTS.md"` | cite | UNKNOWN UNTIL BUILT | cl16:206-207; cl4:220, :172-173 · dl2:206 (`set … --unit <id>`, typed `yes`), :207 (`raise`), :208 (propose: "the command that would apply it") |
| 119 | 16 | D | `gov_record.py find --kind --build` and `show <id>`; `find` caps output at 40 rows, which id 50 avoids by not calling `find` (tr9 S3, S5) | cite | AGREES | cl16:69, :115, :122, :215 · tr9:89-96, :104-107 |
| 120 | 16 | D | `help/loop.md` "gains a section" (S9) | RB | AGREES | cl16:95, :239 · dl1:85-87 creates the page; dl3, dl27 S11 and dl30 S10 add sections only |
| 121 | 16 | D | `measure.py`, `loop_review.py`, `tools/runtime/journal.py` and its README | RB | AGREES | cl16:235-238 · no cited dl or tr §2 names these files |
| 122 | 19 | D | tr42 S4 refuses a home that ends in `/` or names a directory, naming the row | cite | AGREES | cl19:27-28, :58-59 · tr42:51-52 |
| 123 | 19 | D | tr42 S5 grades a record once, by its Serves kind, so overlapping homes give no red; tr1 S4's reading is replaced; tr42 rejected a disjoint-homes refusal | cite | AGREES | cl19:28-31, :52, :67-69, :117-118 · tr42:53-59, :126-128; tr1:87-89 |
| 124 | 19 | D | The precedent: tr42 S1 narrows a home to its id-rule's glob | cite | AGREES | cl19:41, :93-94, :183 · tr42:36-39 |
| 125 | 19 | D | `record_kinds.py --check` is tr1's and absent at base | cite | AGREES | cl19:49-50, :151 · tr1:78-80 |
| 126 | 19 | D | The `three-homes` plant (a scratch worktree, one snapshot and one record committed) gets exit 0 from `record_kinds.py --check` | cite | MISMATCH | cl19:47-51, AC2 :147-151 · tr42:40-46; cl2:305-307, cl3:326-327 |
| 127 | 19 | D | (by name, cl19:122) a rejected ask on dTotalRecall to scope S4 by `id-rule`; the owner is tr42 S4, and no ask is relied on | cite | AGREES | cl19:122-123 · tr42:51-52 |
| 128 | 19 | D | `tools/loop/loop_review.py`, the only file touched | RB | AGREES | cl19:113 · no cited dl or tr §2 names it |
| 129 | 20 | E | `derive_record_kind` reads the kind from the record's own Serves line and returns None when there is none; the edge reads "the kind read from a record's Serves line" | cite | MISMATCH | cl20:23-25, :48, :74, :86, :113 · tr53:94-96 · `tools/memory-tree/tree_lib.py:421-425` |
| 130 | 20 | E | The hands-off ask "THE RECORD-KIND CHECK READS NO SERVES LINE OUTSIDE THE BUILD FOLDERS" is filed only if AC2 goes red at the build run | ask | MISMATCH | cl20:75 · `memory/builds/dTotalRecall/BACKLOG.md:5-19` has no such row · tr53:94-96 already decides the case |
| 131 | 20 | E | Each kind joins `TYPED_RECORD_KINDS` and HYGIENE's list "as TOOL-dTotalRecall-11 S3 joins `shape-run`" | cite | MISMATCH | cl20:36-41, :175-176 · tr11:53-57 · `PLAY-dOrderedCharter-42:40-44` |
| 132 | 20 | E | `TYPED_RECORD_KINDS` is the concatenation of PLAY-dOrderedCharter-42 S1 and tr18 S7; `canonical_kind` returns a row name unchanged | cite | AGREES | cl20:84-85, :94 · tr18:76-81 |
| 133 | 20 | E | A gap that "TOOL-dTotalRecall-42 §4 'The kind decides'" names | cite | MISMATCH | cl20:58 · tr42:53, :84, :97 |
| 134 | 20 | E | AC2: `record_kinds.py --check` in a scratch worktree holding committed records exits 0 over the whole records | cite | MISMATCH | cl20:140 · tr42:40-44 · cl3:327 · cl2:306 |
| 135 | 20 | E | AC2's fixture: `record_kinds.py` comes from tr1 and tr42 | cite | AGREES | cl20:143 · tr1 Inventory · tr42 Inventory |
| 136 | 20 | E | Facts about `tree_lib.py` at base (`record_paths`, `read_bindings` and its population) vs tr18 S7, which changes `read_bindings`. cl20 names tr18 S7, and S7 only adds alias acceptance, so the population fact holds | RB | AGREES | cl20:80-85 · tr18:76-82 |
| 137 | 28 | B | tr9 S3 caps `gov_record.py find` at 40 rows and then prints `<total> rows match; narrow ...` (cl28:22-23, :66) | cite | AGREES | tr9:94-96, AC4 :294-297 |
| 138 | 28 | B | `find`'s order is not by commit time (cl28:25-26) | cite | AGREES | tr9:207 ("Rows sort by build, then key") |
| 139 | 28 | B | A record is read through `gov_record.py show` (cl28:36-37) | cite | AGREES | tr9:104-107 (S5) |
| 140 | 28 | B | `find`'s cap and order are tr9's to change (cl28:51) | cite | AGREES | tr9:89-96, §5 risks :272 |
| 141 | 32 | C | tr42 S4: `check_record_kinds` reds a home that ends in `/` or names a directory, naming the row (H1 by name, and §1, §3, §4, §10) | cite | AGREES | cl32:1, :27-28, :52-53, :63-65, :143-144; tr42:51-52, :160-162 |
| 142 | 32 | C | tr42 S5 and its table: a record under two homes is graded once by its kind, and a mismatch is counted only when the Serves kind names another row, never red | cite | AGREES | cl32:25-27, :66-67, :85-87; tr42:53-58, :101-103, :106-108 |
| 143 | 32 | C | The registry `tools/memory-tree/record-kinds.toml` and `record_kinds.py` are tr1's and tr42's | cite | AGREES | cl32:38, :70-71; tr42:36, :41, :118-119; tr1:152 |
| 144 | 32 | C | AC2: the unmutated registry check exits 0 in the plant's scratch worktree | cite | UNKNOWN UNTIL BUILT | cl32:110-111; tr42:40-46, :151-152; tr53:101-103 (the S23 homeless arm) |
| 145 | 32 | C | RB: Files touched is `tools/loop/loop_review.py`, which no cited unit's §2 changes | RB | AGREES | cl32:79-81; tr42:36-58 |
| 146 | 33 | C | `record_kinds.py --check` grades by Serves kind and stays green whether homes overlap or not. tr42 rejected refusing overlapping homes, saying "deciding by the Serves kind needs no disjoint homes". | cite | AGREES | cl33:24-25, :52-54, :76-77; tr42:53-58, :106-108, :126-128 |
| 147 | 33 | C | tr42 S5 and its §5 "one glob match and one dict lookup per record" moved past tr1 §5's "one `git ls-files` per home glob" | cite | AGREES (tr1's line is now :303, not :297, after rev-5; drift only) | cl33:68-72; tr42:137; tr1:303 (was :297 at `22a8efac3`) |
| 148 | 33 | C | `derive_record_kind(path, <kind>, rows)` takes a kind as its second argument (tr53 S21). Passing a row's name with `[row]` returns that row exactly when its home admits the path. A tr42-form function reads the argument as text and admits nothing. | cite | AGREES | cl33:37-41, :73-75, :105-107; tr53:94-96; tr42:53-56; tr18:168 (`canonical_kind` is identity on a non-alias) |
| 149 | 33 | C | tr42 S1 makes the shape-run home name its own kind (narrowed to its id-rule glob) | cite | AGREES | cl33:94-96; tr42:29-32, :36-38 |
| 150 | 33 | C | RB: Files touched is `tools/loop/loop_review.py`, which no cited unit's §2 changes. The registry facts are build-run preconditions, and the one ancestor change to them (tr53 S21) is named. | RB | AGREES | cl33:85-87; tr42:36-58; tr53:94-96 |
| 151 | 34 | C | tr1 S4 grades every tracked record under a home against that row's fields | cite | AGREES (rev-5 changed only the §4 writer bullet and the note under the rows) | cl34:23-24, :76-77; tr1:87-89; `git diff 22a8efac3 0d1c1dda4 -- …dTotalRecall-1.md` |
| 152 | 34 | C | tr42 S4 and S5 at their revision moved grading to the Serves kind ("deciding by the Serves kind needs no disjoint homes") | cite | AGREES (tr42 is at rev-2, unmoved) | cl34:24-25, :35-37, :40-41, :78-79; tr42:51-58, :127-128, :191 |
| 153 | 34 | C | RB: Files touched is `memory/gotchas/*`, `INDEX.md` and `memory/map/generated/`. No cited unit's §2 touches them. | RB | AGREES | cl34:100-102; tr42:36-58; tr1:87-89 |
| 154 | 35 | E | `derive_record_kind(path, written_kind, rows)`, citing tr42 S5 `:53-58` and tr53 S21 `:94-96` | cite | AGREES | cl35:37-41, :61, :71-76 · tr42:53-58 · tr53:94-96 |
| 155 | 35 | E | tr42's check prints only the unarmed kinds and the mismatch count | cite | AGREES | cl35:95-96 · tr42:140 |
| 156 | 42 | E | The S21 signature is `(path, written_kind, rows)` with no Serves line parsed inside | cite | AGREES | cl42:1, :23-24, :66, :72-80 · tr53:94-96, AC21 |
| 157 | 42 | E | S2 reads the written kind through `BIND_RE` itself rather than through `read_bindings`, and calls this "the form TOOL-dTotalRecall-53 S21 gives it" | cite | MISMATCH | cl42:1, :39-46 · tr53:94-96 |
| 158 | 42 | E | Facts about `tree_lib.py` at base (`BIND_RE :401`, `BIND_HEAD_LINES :410`, `unfenced :515-532`, `record_paths :421-425`) vs tr53 §2, which edits `tree_lib.py` only for `read_header_edges` (S17) | RB | AGREES | cl42:40-44 · tr53 Files touched, S17 |
| 159 | 48 | B | Spec 33's §4 is re-cited to tr42 S5 and §5, where the grader admits a path inside `derive_record_kind` (cl48:68-70) | cite | AGREES | tr42:53-58 (S5), :137 (§5 "one glob match and one dict lookup per record") |

## UNKNOWN UNTIL BUILT

Rows 8, 27, 45, 66, 92, 109, 118 and 144. Each return's section 3 names what decides it: dl20's build
run (8, 66), dl19's (the position's literal form, under row 3), the transition-table grading the
TOOL-dDeclaredLoop-110 ask lands (27), tr104's disposal and tr9's build run (45), the `review.opt-in`
grammar spec 13 §8 F2's ask settles (92), dl3's build run (109), dl2's (118), and the shipped
`check_record_kinds` (144).

## Asks filed by the main loop

Each ask a dCalibratedLens spec relies on and no BACKLOG held is now a row in the target build's
`BACKLOG.md`, filed 2026-11-03 with a SEV disposition, as dWellOiledMachine's spec run filed
TOOL-dTotalRecall-105:

- Ask TOOL-dDeclaredLoop-109, DERIVE_BREAKPOINTS READS NO REVIEW.MAINTAIN · cl1 §8 F4 (row 7).
- Ask TOOL-dDeclaredLoop-110, THE LOOP KIT REFUSES A CADENCE STEP VALUE · cl3 §8 F5 (rows 13, 26, 40).
- Ask TOOL-dDeclaredLoop-111, REVIEW.COST WRITES NO SHAPE-RUN RECORD · cl7 (row 61), new: the return's
  first route.
- Ask TOOL-dTotalRecall-107, THE ITEM BUDGET HAS NO PER-ROLE FORM · cl6 §8 F4 (row 50).
- Ask TOOL-dTotalRecall-108, THE RECORD-KIND CHECK READS NO SERVES LINE OUTSIDE THE BUILD FOLDERS · cl20's
  hands-off (rows 129, 130).
- Ask TOOL-dWellOiledMachine-128, THE PERIOD KEY HAS NO MONTH AND NO LANDING COUNT · cl3 §8 F2, the
  first pass's parked ask.
- Ask TOOL-dWellOiledMachine-129, TWO STALL AND LOOP CLASSES HAVE NO WRITER · cl16 §8 F1, the first
  pass's parked ask.

Not filed: spec 9's `find --all` (row 77) is wm32 F6's ask, which wm32:327-329 has dWellOiledMachine's
build run file, and spec 13's `compose` verb (row 86) waits on the owner's pick on dl26 §8 F5.

## Re-ground

Five `gov-spec-writer` agents folded the brief
[`2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-reground`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-reground.md),
at effort medium, with their handoffs beside it. The brief also carried the owner's pick on the first
pass's row 9. Their returns are
[`2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-reground-returns`](2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-reground-returns.md).

- **Outcome:** of the 41 MISMATCH rows, all 41 were folded and none was refused. Row 86 is folded with
  one part parked (below). Row 9 of the first pass is folded as the owner picked.
- **Specs revised, 16:**
  - 1 rev-5, 2 rev-6, 3 rev-6, 4 rev-6, 5 rev-5, 6 rev-5, 7 rev-3, 8 rev-5;
  - 9 rev-4, 11 rev-4, 13 rev-4, 14 rev-3, 16 rev-4, 19 rev-3, 20 rev-3, 42 rev-2.

  Each spec carries one §9 line naming the brief and its rows. Each has a spec-revised deviation
  record written by the main loop, `TOOL-dCalibratedLens-<n>-deviation-<k>`, with (n, k) =
  - (1, 16), (2, 26), (3, 36), (4, 46), (5, 55), (6, 66), (7, 73), (8, 86);
  - (9, 94), (11, 115), (13, 134), (14, 144), (16, 164), (19, 192), (20, 202), (42, 423).

  cl1's record has Cause `owner`, for row 9.
- **§8 marks:**
  - cl1 has a new F7, `RESOLVED (owner, 2026-11-03): (b)`.
  - These agent-delegated marks were re-worded to name a filed ask: cl1 F4, cl3 F2 and F5, cl6 F4 and
    cl16 F1.
  - No mark the owner resolved was changed.
- **Routes the writers took where the return offered two:**
  - cl14 refuses a multi-scenario carrier.
  - cl14 widens `compare_path` with `composition` and `file_orders`.
  - cl16 states the rework-budget evidence as censored at the base.
  - cl16 re-reads committed keys at each derivation.
  - cl8 names its departure from tr17 S7's ask rather than restricting its view.
- **What the folds do not check:** no reviewer re-read the fold text before the spec audit below.
  Each writer probed that the contradicted child text is gone, and ran memory hygiene over a copy of
  the index. The only finding was the index render, which the main loop owes.
- **Sizes:**
  - cl3 is 51906 bytes and cl5 49147 after the folds.
  - cl3 was already 51098 at the first pass's commit, because of its generated records region.
  - No gate caps a spec's size.

## Parked

- **cl13 S3 under dl26 §8 F5 (b).** F5 is OPEN for the owner in dDeclaredLoop. Under (a) S3 reaches
  `compose_rows` through the playbook kit's `compose` verb, an ask on dOrderedCharter that no BACKLOG
  holds. Under (b) dl26 offers only an import row on `tools/loop/kit.toml`, which gives the workflows
  kit's `render_lenses.py` no route. Options: a declared import row on `tools/workflows/kit.toml`, or
  the workflows kit taking the verb anyway. The writer recommends settling it with the owner's F5 pick.
- **cl1's Maintain boundary may be refused.** TOOL-dTendedCadence-1 homes the `item.maintain.*` rows
  in `tools/drift-audit/kit.toml` with `step = "cadence.maintain"`, and dl19 S4 refuses a
  `review.breakpoints` tag "the loop definition does not declare". No text says the loop definition
  admits those rows.
- **Gaps the writers saw outside their rows:**
  - cl16's example and AC3 still use `item.build.unit`.
  - cl19 AC3's red on a `memory/loop-review/` record also waits on TOOL-dTotalRecall-108.
  - cl2's first-snapshot `unarmed` drop is observed by no cl3 AC; cl3's AC8 observes the
    `loop-review` row only.

## Ancestor text that looks wrong (reported, not edited)

Each line is quoted in its return's section 4:

- **dTotalRecall:**
  - tr11:91-92 names `review.cost` (dl20) as a shape-run writer, which dl20 S3 is not;
    TOOL-dDeclaredLoop-111 asks for it.
  - tr53:94-96 does not say whether `canonical_kind` still applies to `written_kind`. It also routes
    every caller through `read_bindings`, whose population is the build folders, which is what
    TOOL-dTotalRecall-108 asks about.
  - tr14:97 gives the `map` slot to dBoundRoles where the catalogue says dFurnishedOrders (ask tr102
    is open).
  - tr9:137 gives the slice manifest to dBoundRoles' renderer, where tr12:83-85 gives it to
    dWellOiledMachine's executor alone.
  - tr17:68-69 asks a cause "from the slice manifest alone", an input no spec produces.
  - tr18:76-77's untyped `RECORD_KIND_TOKENS` is a 4-tuple, where `tree_lib.py:406` already holds a
    fifth token, `deviation`.
- **dDeclaredLoop:**
  - dl20:143 passes `review_pin.py` subjects positionally, where fh3:186 uses `--subject`.
  - dl20:55 and :142-143 pass a `set` key's one-per-line output as `--opt-in`, which fh3:67-69 parses
    as a JSON map.
  - dl19:43-45 reads five `review.<stage>` keys while v2:1656 lists `review.maintain`.
  - dl27:38-39 and :138 spell the scenario factory two ways.
  - dl28:60 and :161 key `flow-state` rows by row tag alone.
  - dl26:286-289's F5 (b) gives a caller outside the loop kit no route.
  - dl3:69-71 names dl30 as a `read_transitions` reader, but dl30 S3 reads through `build_records.py`.
  - dl1:85-87 and dl2:102 put legs straight into `gate-legs.json`, where tr1 and tr9 render through
    `leg_factory.py`.
- **Elsewhere:**
  - dBoundRoles-20:62 reads dl26 F5 as settled.
  - wm32:327-330 has dWellOiledMachine's build run file `find --all`, and no BACKLOG holds it yet.
  - tc1:181 and :189 spell the lease row's actor as a bare `executor` without saying whether it is a
    role actor.

## The reader handoffs were re-rendered after dispatch

The brief as first rendered opened a bullet with `- **TOOL-dTotalRecall-2:** rev-7`. That shape is an
id anchor, so hygiene check 13 read five handoffs and the brief as dCalibratedLens claiming
TOOL-dTotalRecall-2. A handoff's text cannot be edited without its marker's `task-sha` failing
`handoff.py check`. So the brief's line now reads `- **tr2, TOOL-dTotalRecall-2:** rev-7`, and the five
reader handoffs were re-rendered in place with `--out`. Each differs from what its reader was sent in
that one line and its marker's `task-sha`. Each reader's transcript holds the text it received.

## The spec audit over both passes' folds

A Tier-2 spec audit at full intensity read the 24 specs both passes revised on 2026-11-04. Its record
is
[`2026-11-04-review-TOOL-dCalibratedLens-1-crosscheck-spec-audit`](../reviews/2026-11-04-review-TOOL-dCalibratedLens-1-crosscheck-spec-audit.md).

- **Verdict:** CLEAN WITH FIXES. No blocker and no high, with 12 medium and 9 low items.
- **Disposal:** all 21 items were folded as LOCAL into 15 specs, and unit 20 then gained the edges that pair M6's. That record's "Disposal" section
  lists them.
