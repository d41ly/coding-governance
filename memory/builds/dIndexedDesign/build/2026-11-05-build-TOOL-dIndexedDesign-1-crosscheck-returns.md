**Serves:** research TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-46

# dIndexedDesign — the parents cross-check readers' returns, verbatim

The `gov-spec-reviewer` returns the cross-check record [`2026-11-05-build-TOOL-dIndexedDesign-1-parents-crosscheck`](2026-11-05-build-TOOL-dIndexedDesign-1-parents-crosscheck.md) is assembled from, extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-crosscheck`](../prompts/2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-crosscheck.md); each group's handoff sits beside it.

## Group A, full, led by spec 1 (specs 1, 2, 3, 4, 5, 7 and 8)

**dIndexedDesign Group A (specs 1, 2, 3, 4, 5, 7, 8) against parent specs at `ab976b5b3`**

I read every parent mention in the seven specs against each parent's text at `ab976b5b3`. HEAD is `ab976b5b3`, so the working tree reads as that commit. No file was written and no gate was run.

- **Rows:** 47 assumptions. 41 AGREES, 5 MISMATCH, 1 UNKNOWN UNTIL BUILT.
- **Where the mismatches are:** spec 1 (one), spec 2 (two), spec 5 (one), spec 8 (two; the registration-grammar mismatch is one row shared with spec 2, which is why there are 5 rows but 6 spec hits).
- **What caused them:** one comes from revision `58b395b6e`. The other four were already there at the spec base `4bf0f400d`.
- **Rules:** SA and RH bind nothing in this group.

## 1. Table

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 1 | dl12 S2 seeds `[[item]]` rows for `item.design.ready` and `item.design.exit` (id1:99) | cite | AGREES | dl12:36-38, one row per item of flow-steps' `[design]` table; dl12:138 counts 13 design items; flow-steps:246-247 lists both, owner dIndexedDesign |
| 1 | dl13 S8 holds a `[[stand-in]]` row for `item.design.exit` (id1:99, :322) | cite | AGREES | dl13:62-65; dl13:227 |
| 1 | dl13 S8 holds a stand-in row for "the second" item only, exit, and none for `item.design.ready`, which spec 1 carries (id1:6, :99) | cite | MISMATCH | dl13:231-233 |
| 1 | The stand-in is "the mover naming its witnessing commit" (id1:322) | cite | AGREES | dl13:226-227 |
| 1 | dl13 states the witness-reader contract in one sentence ("spec line 239") and specifies nothing more; an owning build arms its item by landing its witness reader and deleting its stand-in row (id1:324, :328) | cite | AGREES | dl13:239-240, dl13:86-87. `grep -rn 'witness reader'` over dDeclaredLoop's specs finds only dl13:239 |
| 1 | dl12 and dl13 are DEFERRED at base (id1:99) | cite | AGREES | dl12:3, dl13:3 |
| 2 | `record_kinds.py new overlap --tag record.overlap` registers the row through tr1 S9 (id2:71-72, :102) | cite | MISMATCH | tr1:105-107; tr1:68-70; tr16:36-37; tr18:45-46 |
| 2 | dl12 S2 seeds the row for `item.design.overlaps` (id2:102) | cite | AGREES | flow-steps:241; dl12:36-38 |
| 2 | Spec 2 carries `item.design.overlaps` (id2:6) and builds its witness, but leaves dl13 S8's stand-in row for that item unmentioned | cite | MISMATCH | dl13:231-233; dl13:86-87 |
| 2 | Routing an overlap back to decompose is the loop engine's transition, dDeclaredLoop's (id2:91-93) | cite | AGREES | dl13:47 (S5 `derive_move`) |
| 2 | The registry is tr1's and absent until it lands (id2:282) | cite | AGREES | tr1:3 DEFERRED; tr1:66 |
| 3 | dl19 S8 specifies the opt-in derivation: `off`/`opt-in`/`owed`/`owed-above-tier`, the `policy` source of `AUTH_SPEC_AUDIT_FROM`, the preflight line, and M4's "When" (id3:34-36, :88-90) | cite | AGREES | dl19:73-80; dl19:173-180 |
| 3 | dl19 S8 adds the `review.design` read to `check_authorization` (id3:39-40, :111, :128) | cite | AGREES | dl19:73-74 |
| 3 | An unset `review.design` reads `opt-in`, which dl19 makes today's behaviour (id3:191) | cite | AGREES | dl19:176; dl19:45 |
| 3 | dl19 §4 reads `review.design` at the landed revision (id3:214, :313, :360) | cite | AGREES | dl19:182 |
| 3 | `derive_breakpoints` reads `review.<stage>` for `--plan` (dl19 S1) (id3:91) | cite | AGREES | dl19:40-45; dl19:81 |
| 3 | The README key and `SPEC_AUDIT_DEFAULT` are kept, as dl19 §8 F2 ruled (id3:100) | cite | AGREES | dl19:308-311 |
| 3 | dl22: `--recommend <slug> --stage design`, its record, the harness `reason` stage, its caller documented in S5/S7, and "a recommendation writes no opt-in" in §3 (id3:93, :115, :317) | cite | AGREES | dl22:11; dl22:73; dl22:84-89; dl22:94-96; dl22:110-111 |
| 3 | The stage-exit recommendation is dDeclaredLoop's (id3:27) | cite | AGREES | dl22:1 |
| 3 | `review.design.rounds` and `review.design.round-count` are dDeclaredLoop's keys, read by its review program (id3:97) | cite | AGREES | dl21:8; dl21:30; dl21:65; dl32:52-53 (`verb_review` derives the target from `review.design.rounds`). SA does not bind (see 4) |
| 3 | dl18 §4: "a kit imports no sibling kit" (id3:225) | cite | AGREES | dl18:146 |
| 3 | br21 S1 `read_policy_setting` and S2's re-pointed `resolve_stage_efforts` order (id3:60-66, :113) | cite | AGREES | br21:41-54 |
| 3 | Order steps 1 and 2 to 5 as br21 §4 gives them (id3:169-171) | cite | AGREES | br21:118-122 |
| 3 | br21 §8 F2 rules out importing a sibling kit (id3:224, :316) | cite | AGREES | br21:285-293 |
| 3 | br21 S1 turns a `get` exit 2 into a `RolesError` (id3:242, :316) | cite | AGREES | br21:47-48 |
| 3 | dl19 and br21 are specified and not yet built (id3:81-82, :319) | cite | AGREES | dl19:3; br21:3 |
| 4 | The scout record's name `<date>-build-<unit id>-reuse-scout[-<x>].md` and its binding (ll2 S6) (id4:37-38, :129) | cite | AGREES | ll2:78-79 binds `**Serves:** research <ids>`, which id4:69 reads as backing no outcome until id13's `seams` kind |
| 4 | `derive_owed_units` in `reuse_entries.py` keys on `no existing seam fits` (ll1 S4) (id4:38-39, :144) | cite | AGREES | ll1:95-100 |
| 4 | ll3 S2 puts a derived cutoff on `hasP`, drops the two lookup spellings and adds `-reuse-scout` (id4:39-40, :139-140) | cite | AGREES | ll3:73-79 |
| 5 | br16 S4: the `experiment` kind, its `[workflow.experiment]` table, R9, the table homed on the entry (id5:36-37, :134, :150, :252) | cite | AGREES | br16:47-50; br16:153-170; br16:149 (`gov-reuse-scout` declares `experiment`) |
| 5 | br20 S3/S4: `compose_workflows`, the overlay rows, the open registry replacing `WORKFLOW_NAMES` (id5:38, :150) | cite | AGREES | br20:58-71 |
| 5 | ll2 S11's `reuse-bench.js`, its committed manifest and its `project-owned` row; ll2 S12's `help/reuse.md` names the bench (id5:28, :41, :113-115, :152) | cite | AGREES | ll2:112-119; ll2:120-121 |
| 5 | ll2's committed bench manifest runs one variant, `house-index`, scorer `scouted-seam` (id5:108-109) | cite | UNKNOWN UNTIL BUILT | ll2:112-119 names the scorer shape and the cases, but no variant or arm name |
| 5 | ll2's bar of 16 of 24 and 8 of 12 is pinned in §4 (id5:130, :323, :327) | cite | AGREES | ll2:194-197 |
| 5 | ll13 S1's kind line and `read_declared_kind`; ll13 S2 says `design.research` writes the line (id5:41, :122-123, :152) | cite | AGREES | ll13:35-39; ll13:50-52; ll13:105; ll13:119 |
| 5 | dl11 maps the directives `researched` and `solution-tested` onto `item.design.research` (id5:124-125) | cite | AGREES | dl11:117-118 |
| 5 | dl24 S6's factory `loop_items.py new design.research --step step.design …` appends the `item.design.research` row (id5:42, :119-121, :153) | cite | MISMATCH | dl24:61-63; dl24:240-243; dl12:36-38 and :138 with flow-steps:240; dl13:231-233 |
| 5 | ll30 is an open ask of dLinkedLibrary (id5:143) | cite | AGREES | `memory/builds/dLinkedLibrary/BACKLOG.md:9`, :34 |
| 7 | tr1 §4 has a `spec` row; tr1 is DEFERRED at base (id7:87) | cite | AGREES | tr1:211; tr1:3 |
| 7 | tr9 S2 writes the `sections` column (id7:78) | cite | AGREES | tr9:84-85; tr1:203-205 admits it |
| 8 | tr1 S1 and S9 provide the registry and the factory (id8:49, :363) | cite | AGREES | tr1:66-70; tr1:105-109 |
| 8 | The three registrations, as spelled, pass tr1 S9's `new` (id8:64-65, :78-79, :93-95) | cite | MISMATCH | tr1:68-70; tr16:36-37; tr18:45-46; ll13:40-50 |
| 8 | "their writer is `hand`, the class TOOL-dTotalRecall-2 replaces with doors" (id8:141-142) | HD | MISMATCH | tr1:198-200; tr1:224-226; tr1:414-416; tr2:84-88 |
| 8 | dl12 S2 transcribes every `design.*` item with owner dIndexedDesign, and dl13 S8 holds a stand-in for each until that build lands (id8:50, :173-174, :352) | cite | AGREES | dl12:36-38; flow-steps:235-247 owner column; dl13:231-233 |
| 8 | S11: the decompose stand-in row leaves when its witness lands, and needs, outcomes and routes stay as dl12 transcribed them (id8:126-127, :229) | cite | AGREES | dl13:86-87; dl13:239-240 |
| 8 | dl13 S4 owns F1 to F6 (id8:145); dl24 is the item factory (id8:51) | cite | AGREES | dl13:44; dl13:176-181; dl24:61-63 |
| 8 | tr19 writes `**Edges:** implements=feature.record-door` under a heading (id8:175-176); `feature.<seg>` is dTotalRecall's namespace (id8:217) | cite | AGREES | tr19:182-188; tr9:77-78 (the `feature` extractor, tag `feature.*`) |

## 2. MISMATCH

- **Spec 1, the stand-in for `item.design.ready`.**
  - Spec side, id1:99: "TOOL-dDeclaredLoop-13 S8's stand-in row for the second", and id1:6 carries `node:item.design.ready`.
  - Parent side, dl13:231-233: "Every other row item whose owning build has not landed gets its row the same way: the build pass derives the list from the `[[item]]` rows' `owner` field, so every row item owned outside dDeclaredLoop is on it". `item.design.ready` is owned by dIndexedDesign (flow-steps:246), so it has a stand-in row too.
  - **Change:** id1 §3's edge names dl13 S8's stand-in row for `item.design.ready` as well. §8 F5, or a new fork, then states whether this unit keeps that row, as it keeps exit's, or arms it.
  - **Cause:** pre-existing, none (spec base `4bf0f400d`).

- **Specs 2 and 8, the registry factory's grammar.**
  - Spec 2 side, id2:71-72: "The kind registered through `record_kinds.py new overlap --tag record.overlap` (TOOL-dTotalRecall-1 S9)". It has no `--writer` and no `--check`.
  - Spec 8 side, id8:64-65, :78-79 and :93-95: `new feature-design|roster|fork … --writer hand --check "memory hygiene" [--field …]`. None of them has `--purpose`.
  - Parent side:
    - tr1:105-107: "`new <name> --tag <tag> --writer <door> --check <leg> --field <Key>…` appends a conforming row and refuses one missing a required column".
    - tr1:68-70: `layer`, `home`, `readers` and `lifecycle` are "required from TOOL-dTotalRecall-18".
    - tr16:36: "`record_kinds.py new` refuses a row with no `--purpose`".
    - tr18:45-46: `check_record_kinds` "reds a row missing one" of `home`, `lifecycle`, `readers`, `layer`.
    - ll13:40-50 is the parent family's own correct spelling: `--purpose`, the six columns "through TOOL-dTotalRecall-18's landed verb", and an explicit `schema.form`.
  - **Change:**
    - Spell each registration with `--writer`, `--check` and `--purpose`.
    - Declare `layer`, `home`, `id-rule`, `lifecycle`, `readers` and the `schema.form` (`fields` for feature-design and fork; spec 8's roster is a README region, so not `fields`). Set them through tr18's verb, as ll13 S2 does.
    - id2's AC9 gains the writer and the purpose.
  - **Cause:** pre-existing, none (spec base `4bf0f400d`).

- **Spec 2, the stand-in for `item.design.overlaps`.**
  - Spec side, id2:102: it consumes only "TOOL-dDeclaredLoop-12 S2's `[[item]]` row for `item.design.overlaps`", while carrying the node (id2:6) and building the witness (`design_lib.py --overlaps`).
  - Parent side:
    - dl13:231-233 derives a stand-in row for every non-dDeclaredLoop item.
    - dl13:86-87: "Each owning build arms its own item and deletes its stand-in row in the same landing."
    - dl13:239-240: "an owning build arms its item by landing its witness reader and deleting the row together".
  - **Change:** add the consumes-from edge for dl13 S8's `item.design.overlaps` stand-in row. Then either arm it, by deleting the row and pointing the row's `witness` at `design_lib.py --overlaps` as id8 S11 does, or keep it with a stated reason as id1 F5 does.
  - **Cause:** pre-existing, none (spec base `4bf0f400d`).

- **Spec 5, the `item.design.research` row.**
  - Spec side, id5:119-121: "The item factory, `loop_items.py new design.research`, appends its `[[item]]` row to `tools/loop/loop.toml` with `--step step.design`…"
  - Parent side:
    - dl24:61-63: "`loop_items.py new <name> --step <step> --actor <kind:name> --witness-by <text> --owner <build>`".
    - dl24:240-243: `new item demo --step step.test` "appends `item.test.demo` … the same name run again exits 2".
    - dl12:36-38 transcribes every flow-steps `[design]` item, 13 of them (dl12:138), and flow-steps:240 is `design.research`, owner dIndexedDesign.
    - dl13:231-233 gives that row a stand-in.
  - So the row already exists. A second `new` either exits 2, or with the dotted name mints `item.design.design.research`. The row's stand-in is never deleted.
  - **Change:** S8 arms dl12's existing `item.design.research` row: set its `witness` to the `read_declared_kind` check and delete its dl13 stand-in row, as id8 S11 does. Drop the factory call. Re-point AC9 to the tag `item.design.research` with the witness that arming writes. As written, AC9 is already met by dl12's transcribed row, so it cannot fail.
  - **Cause:** pre-existing, none (spec base `4bf0f400d`).

- **Spec 8, the `hand` writer (HD).**
  - Spec side, id8:141-142: "Writing a door for these records: their writer is `hand`, the class TOOL-dTotalRecall-2 replaces with doors; this unit adds none."
  - Parent side:
    - tr1:198-200: "`hand` is legal on any row TOOL-dTotalRecall-2 S9 does not move. S9 moves only the `fields`-form `hand` rows onto its door, and a `hand` row of another form keeps `hand`".
    - tr1:414-416, rev-5: "the promise that unit 2 gives every `hand` row a door is dropped".
    - tr2:84-88: S9 rewrites the `fields` rows its pass finds to `gov_record.py new <kind>`.
  - These rows land after tr2's pass, since dTotalRecall is an ancestor, so S9 moves none of them. `roster` is not `fields`-form, so no door is ever promised for it.
  - **Change:** restate the non-goal on tr1:198-200's ground: `hand` is legal because tr2 S9 does not move these rows, and no door is promised. Then either register the two `fields`-form kinds, feature-design and fork, with `writer = "gov_record.py new <kind>"`, the door tr2 S9 gives `fields` rows, or keep `hand` and say so. `roster` keeps `hand`.
  - **Cause:** the revision `58b395b6e` (tr1 rev-5, tr2 S9).

## 3. UNKNOWN UNTIL BUILT

- **id5:108-109:** the variant and arm name that ll2's committed bench manifest runs are decided by ll2's build run, which commits `-reuse-bench.json` (ll2:115-117).

One AC risk sits outside the row count. id3 AC6 (an unset `review.design.effort` must not refuse `stage-efforts`) depends on br21's build run adopting id3 §8 F5's ask. Today br21:47-48 turns exit 2 into a `RolesError`, and `grep -nE 'DERIVED-DEFAULT|derived default|dIndexedDesign' memory/builds/dBoundRoles/BACKLOG.md` prints nothing: the ask is not filed. id3 §8 F2's ask is also absent from `memory/builds/dDeclaredLoop/BACKLOG.md` (same grep, empty).

## 4. Rule-wide hits no rule binds

- **id3:97 (SA probe):** it names the rounds keys' owner only. It relies on no stop, no NON-CONVERGENT, no routing, no disposal and no `review_state` shape.
- **id1:357 (HD probe):** "hand-off" is the Design-to-Build hand-off, not a registry `writer`.
- **id1:40, :58-60:** it reads a spec-audit record's `@rev` pin, not the audit loop's stop or disposal, so SA does not bind.
- **id2:94, :202:** `leases.overlap` is a policy key. No holder, session, class or epoch is read, so RH does not bind.
- **id7:119, :125:** "rework" is M3's count of revisions, not the rework budget that routes findings, so SA does not bind.
- Group A has no `--claims`, `read_claims`, `--lease status`, `review_state`, `no-fall`, `REVIEW_ROUNDS` or precision-floor hit: `grep -nE` over the seven specs prints none.

## 5. Revised parent sections cited that no assumption depends on

- **Spec 1:** none. It cites dl12 and dl13, and neither was revised.
- **Spec 2:** none. It cites tr1 S9, not tr1 §4's revised writer bullet.
- **Spec 3:** none. It names dl32 S3's `review.design.rounds` key by owner only. Its no-fall stop (dl32:47-55) is not relied on.
- **Spec 4:** none.
- **Spec 5:** none.
- **Spec 7:** tr1 §4. Its row depends only on the `spec` row, writer `gen_build_index.py --new-spec`, not on the rev-5 writer bullet or the note under the rows.
- **Spec 8:** tr2 §3's external edge, §4 "Minting" and §8 F6. Only S9 bears on spec 8, through the HD row above.

## 6. Parent text that looks wrong

- **tr1:105-107 against tr1:68-70, tr16:36 and tr18:45-46:** S9's `new` grammar has no flag for `layer`, `home`, `readers`, `lifecycle`, `id-rule`, `schema.form` or `purpose`, yet later units require them. ll13:48-49 has to say "S9's verb takes no flag for those six columns". A row registered through `new` alone is refused once tr18 lands.
- **br21:45-48:** an exit 2 becomes a `RolesError`, but `policy.py get` refuses every unset key whose catalogue default is `{ derived = … }` (`tools/policy/policy.py:694-696`, `DerivedDefault`). `roles.effort.default` is derived (`tools/policy/catalogue.toml:308-310`), so br21's own order would refuse on an unset key.

## Group B, full, led by spec 9 (specs 9, 10, 11, 12, 13, 14 and 15)

## Group B parent cross-read: dIndexedDesign specs 9 to 15 against `ab976b5b3`

I read seven specs (9, 10, 11, 12, 13, 14, 15) whole and checked them against their parents' specs at `ab976b5b3`. The result is 7 MISMATCH rows, 4 UNKNOWN UNTIL BUILT rows (three of them one fact, the dTotalRecall-18 column verb, seen in specs 10, 11 and 15) and the rest AGREES. Only one MISMATCH comes from a revision since the spec base, the `hand` writer rule (`58b395b6e`). The other six were already wrong at `4bf0f400d`; `git diff 4bf0f400d ab976b5b3 --stat` touches only dl20, dl32, tr1 and tr2.

### 1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 9 | tr43 S25 holds a parity arm against `SPEC_TITLE_NUMBERS` (id9:114-115) | cite | AGREES | tr43:138-139 |
| 9 | tr9 §4 "The section table" keys legacy headings `heading = "1. Goal"`, and its AC3 spells `section.acceptance-criteria` (id9:118, :341-342) | cite | AGREES | tr9:183-193, :290-291. The F3 ask the spec says "the main loop" filed is not in the parent's backlog: `grep 'SPEC_SECTION_TAGS\|dIndexedDesign-9' memory/builds/dTotalRecall/BACKLOG.md` prints nothing |
| 9 | S6 and AC8 edit and run `tools/codebase-map/replay-phrases.py` (`_SEC10`, :139) when this build runs (id9:73-74, :210, :285) | cite (no citation; the dependency is on a parent unit the spec does not name) | MISMATCH | ll3:46-50 deletes the file |
| 10 | tr1 S9's factory `record_kinds.py new … --writer --check`, with `--purpose` (id10:36-40) | cite | AGREES | tr1:105-106; tr16:36-37 |
| 10 | tr18's columns are set "through that unit's landed verb" (id10:40-41) | cite | UNKNOWN UNTIL BUILT | tr18 S1 requires the columns (tr18:45-49) but names no verb or flag that sets them |
| 10 | AC6: tr16 and tr18 require the columns (id10:224) | cite | AGREES | tr16:36-38; tr18:45-49 |
| 10 | tr1 §4 admits `header` for "a grammar its owner grades", naming the owner's leg in `check` (id10:261-262) | cite | AGREES | tr1:178-180 |
| 10 | tr25 S4's `fence` form needs a memory-tree validator (id10:257-258) | cite | AGREES | tr25:56-58 |
| 10 | tr18 §4 "Columns" makes `home` a literal glob (id10:255) | cite | AGREES | tr18:126-133 |
| 10 | tr42 S5 "makes the kind decide and the home admit", so a `**/*.md` home misgrades nothing and "every path … stays a record of the kind" (id10:251-254) | cite | MISMATCH | tr42:53-58; tr43:82-84; tr53:94-96 |
| 10 | tr2's door gives the `playbook` row (form `header`) a door, and `hand` holds only until then (id10:99-100) | HD | MISMATCH | tr1:197-200, :224-226; tr2:84-88 |
| 10 | `--writer hand` on a `header` row is legal (id10:38) | HD | AGREES | tr1:197-200 |
| 10 | ks18 S5 is the path stand-in and S6 the `help/loop.md` sentence that the S4 landing prunes (id10:70-72) | cite | AGREES | ks18:56-61; ks18 F2 at :186-191 asks for exactly this |
| 10 | `help/loop.md` is dl1's page (id10:74, :233) | cite | AGREES | dl1:87 |
| 11 | tr1 S9's factory with `--purpose`; tr16 and tr18 columns (id11:69-77, :218) | cite | AGREES | tr1:105-106; tr16:36-37; tr18:45-49 |
| 11 | tr18's columns "set through its landed verb" (id11:73) | cite | UNKNOWN UNTIL BUILT | tr18 names no verb (as for spec 10) |
| 11 | F2: tr42 S5 "has the kind decide and the home admit", so `**/set-*.md` is safe (id11:245-247) | cite | MISMATCH | tr42:53-58. The set record has no `Serves` line: `grep -c Serves tools/unattended/fixture-records/set-dScriptedRepeat.md` prints 0 |
| 12 | dOrderedCharter is an ancestor through dDeclaredLoop's README `parents:` (id12:33-35) | cite | AGREES | `memory/builds/dDeclaredLoop/README.md:9` reads `parents: dOrderedCharter dFairHearing` |
| 12 | ll22 S6 spells `decides=` targets through `parse_edge_target`, widened to any node (id12:54-55) | cite | AGREES | ll22:35-37, :84-89 |
| 12 | ll17 AC3 plants `decides=feature.alpha` (id12:295) | cite | AGREES | ll17:252-255 |
| 12 | tr19 §4 writes a section edge line under a heading; its only `**Edges:**` lines sit in a fence at :188-189 (id12:126, :158, :181, :290) | cite | AGREES | tr19:181-193 |
| 12 | tr43 S10 adds the `playbook` `requires_if` row to `tools/memory-tree/kit.toml` (id12:69-71, :100) | cite | AGREES | tr43:73-76 |
| 13 | ll2 S2, S3, S5 and S6: the house index, `## Steps`, `## Matches`, the record name and `read_reuse_scouts` (id13:28, :37-39, :50-55, :91) | cite | AGREES | ll2:50, :59-64, :71-82 |
| 13 | `help/reuse.md` is ll2's page (id13:99, :242) | cite | AGREES | ll2:120-122 |
| 13 | ll3 S1 deletes `reuse-lookup.agent.md` (id13:130) | cite | AGREES | ll3:46 |
| 13 | S1: `record_kinds.py new seams --tag … --writer hand --check … --field Index` (no `--purpose`, no columns) registers the row through tr1 S9 (id13:48-51) | cite | MISMATCH | tr16:36-37 and AC2 at :167-170; tr1:66-70; tr18:45-49 |
| 13 | `--writer hand` on a `fields` row added after tr2's pass stays legal (id13:49) | HD | AGREES | tr1:197-200. S9 moves rows at tr2's pass; this row lands later, so S9 never moves it |
| 13 | dl12 S2's rows and dl13 S8's `[[stand-in]]` rows (id13:40-41, :82-84) | cite | AGREES | dl12:36-38; dl13:62-65 |
| 13 | dl29 S1 to S4: the `upstream` field, gate `record` as default, no entry `measured`, `## Establishes` grammar with the closed kind set, `derive_upstream_rows` (id13:41, :77-81, :137-138) | cite | AGREES | dl29:33-51 |
| 13 | S6 adds a non-empty `upstream` to `item.design.decompose` with no `finding` route, and the loader takes it (id13:79-81) | cite | MISMATCH | dl29:65-68 and AC9 at :253-254; decompose's outcomes at flow-steps.md:239; id8:126 keeps them as transcribed |
| 14 | ll2 S2, S3 and S7: the house index, `## Steps`, the slot (id14:37) | cite | AGREES | ll2:50, :59, :83-87 |
| 14 | br16 S4 `[workflow.experiment]` with `cases`, `variants`, `fan`, `scorer` and `reruns` (id14:41, :94-98) | cite | AGREES | br16:47-50, :156-168 |
| 14 | br20 S3 overlay `[[workflow]]` rows in `.governance/instructions.toml` (id14:41, :94-95) | cite | AGREES | br20:58-68, :182 |
| 14 | ll24 S5 makes a gated class leave "the index the corpus reads" (id14:138-139) | cite | MISMATCH | ll24:68-73, :74-78 |
| 14 | The ll2 spec is absent at its own base `5fede642` (id14:160-161, :219) | cite | AGREES | `git cat-file -e 5fede642:memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-2.md` prints "exists on disk, but not in '5fede642'", exit 128 |
| 15 | tr25 registers stream-plan with no writer yet; S2 schema, S3 shape-only check, §4 data model, same-order parallel group (id15:27-28, :61, :88, :158, :171, :327) | cite | AGREES | tr25:34-50, :86-95, :185-187 |
| 15 | tr4 S1 `FRONT_MATTER_KEYS`; `streams` is derived (id15:80-83, :160-161) | cite | AGREES | tr4:38-40, :44-45 |
| 15 | The writer cell moves "through TOOL-dTotalRecall-18's landed verb" (id15:88-90) | cite | UNKNOWN UNTIL BUILT | tr18 names no verb |
| 15 | tr42 S3's `unarmed` key on the stream-plan row (id15:90-91) | cite | AGREES | tr42:47-50 |
| 15 | The stream-plan row's `hand` writer is replaced by the planner, with no reliance on tr2's door (id15:88-90) | HD | AGREES | tr25:38 (form `fence`); tr1:197-200 |
| 15 | br1 S4: `plan` entry with `harness none` and driver `agent`, its F1; the `gov-planner` slot (id15:100, :338-339) | cite | AGREES | br1:80-82, :133, :325-326 |
| 15 | dl12 S2 transcribes `item.design.streams`, with `returns` and `witness` fields (id15:106-113, :313) | cite | AGREES | dl12:36-38, :110-115 |
| 15 | dDeclaredLoop's route evaluator reads `plan_streams.py when` for the route out of `design.overlaps` (id15:146, :109-110) | cite | UNKNOWN UNTIL BUILT | `grep -rlnE 'streams-when\|plan_streams' memory/builds/dDeclaredLoop/spec/` prints nothing |

### 2. MISMATCHES

- **id9 S6 and AC8 against ll3 S1.**
  - id9:73-74: "`_SEC10` (`tools/codebase-map/replay-phrases.py:139`)"; AC8 runs `replay-phrases.py` (id9:285).
  - ll3:46-49: "the harnesses that score only its ranking (`tools/codebase-map/rank_harness.py`, `tools/codebase-map/replay-phrases.py`, …) … are deleted".
  - dLinkedLibrary is a parent, so the file is gone when unit 9 builds. AC8 cannot run and S6 has nothing to edit.
  - **Change:** drop `replay-phrases.py` from S6, AC8, §4 Files touched and S11's twin table. State that ll3 S1 removes this reader.
  - **Cause:** pre-existing (none, spec base `4bf0f400d`). `git show 4bf0f400d:…Library-3.md | grep -c replay-phrases.py` prints 2.
- **id10 F1 and id11 F2 against tr42 S5.**
  - id10:251-254: "TOOL-dTotalRecall-42 S5 makes the kind decide and the home admit, so a home matching many paths misgrades nothing, and every path recipe mode and the `repeat` route already follow stays a record of the kind". id11:246-247 says the same for `**/set-*.md`.
  - tr42:53-56: "`derive_record_kind(path, text, rows)` … returns the row whose `name` equals `canonical_kind(<the record's Serves kind>)` … and `None` otherwise". tr43:82-84 makes the `record` extractor take its kind from that function.
  - A playbook and a set record carry no `**Serves:**` line, so neither is ever tagged `record.playbook` or `record.playbook-set`.
  - **Change:** id10 F1 and id11 F2 must stop claiming the kind is decided by tr42 S5. Either ask dTotalRecall for a non-Serves classifier (for example, the row's `check` predicate, `check-playbook.sh --resolve`), or state that these records are registered but never tagged by the extractor.
  - **Cause:** pre-existing (none, spec base `4bf0f400d`). tr42 is unchanged since then.
- **id10 §3 against tr1 rev-5 and tr2 S9.**
  - id10:99-100: "A writer door for the kind: TOOL-dTotalRecall-2's door registers one; until then the writer is `hand`".
  - tr1:198-200: "`hand` is legal on any row TOOL-dTotalRecall-2 S9 does not move. S9 moves only the `fields`-form `hand` rows onto its door, and a `hand` row of another form keeps `hand`". tr2:84-88 says the same.
  - The `playbook` row is `{ form = "header" }`, so tr2 gives it no door.
  - **Change:** the non-goal should read: the kind's writer stays `hand` (tr1 §4, a non-`fields` row tr2 S9 does not move), and any door is this kit's or an ask, named by owner.
  - **Cause:** revision `58b395b6e` (tr1 rev-5). tr2 S9's fields-only scope already read so at `4bf0f400d` (tr2:77 there).
- **id13 S1 against tr1 S1/S9, tr16 S2 and tr18 S1.**
  - id13:48-49: "registered by `python record_kinds.py new seams --tag record.seams --writer hand --check "memory hygiene" --field Index`".
  - tr16:36-37: "`record_kinds.py new` refuses a row with no `--purpose`". AC2 at :167-169 says it "exits 2 and writes nothing".
  - tr18:45-46: every row carries non-empty `home`, `lifecycle`, `readers` and `layer`; tr1:68-70 makes them "required from TOOL-dTotalRecall-18".
  - id13's home is a filename pattern, not the glob tr18 asks for.
  - **Change:** S1 adds `--purpose "<…>"` and sets layer, home as a glob (for example `memory/builds/*/build/*-reuse-scout*.md`), lifecycle and `readers` or `readers-none`, the way id10 S1 and id11 S5 do.
  - **Cause:** pre-existing (none, spec base `4bf0f400d`).
- **id13 S6 against dl29 S7.**
  - id13:79-81: "`item.design.decompose`'s row … gains `upstream = [{ item = "item.design.seams" }]`, gate `record`".
  - dl29:66-68: "An item whose `upstream` is non-empty must declare a route for the outcome `finding` in its closed outcome set …, or the loader refuses it". AC9 at :253-254 shows the load refusing.
  - decompose's outcomes are decomposed, a fact fork, and an unsurvivable fork (flow-steps.md:239), and id8:126 keeps them "as TOOL-dDeclaredLoop-12 transcribed them".
  - AC7 reads `loop.toml` with `tomllib` alone, so it never sees the loader's refusal.
  - **Change:** S6 adds a `finding` outcome and its route to decompose's row, and AC7 runs the loop loader over the row.
  - **Cause:** pre-existing (none, spec base `4bf0f400d`).
- **id14 §3 against ll24 S5 and S6.**
  - id14:138-139: "Once TOOL-dLinkedLibrary-24 S5 marks a class gated it leaves the index the corpus reads".
  - ll24:68-70: "`cmd_for_paths` (:671) … leaves out every class whose status is `gated`". ll24:77 keeps `INDEX.md` with a `Gate` column, and ll24 never touches `load_records_at`.
  - So a gated class drops out of the anchor arm (S1 extracts from `cmd_for_paths`) but stays in the intent arm's `index`. The two arms then compare over different class sets. ll24 S6 also adds a `record` tier to the ranking S1 extracts.
  - **Change:** §3 and S1 should state that S1 extracts `cmd_for_paths` as ll24 S5 and S6 leave it (gated cut, `record` tier), and say whether the corpus filters gated classes out of `index` too.
  - **Cause:** pre-existing (none, spec base `4bf0f400d`).

### 3. UNKNOWN UNTIL BUILT

- **tr18's "landed verb"** (id10:40-41, id11:73, id15:90). tr18 requires the four columns but no dTotalRecall spec names the `new` flags or verb that sets them. dTotalRecall's build of tr18 decides it.
- **dDeclaredLoop's route evaluator reading `plan_streams.py when`** (id15:146). No dDeclaredLoop spec names a predicate verb for a conditional route. dDeclaredLoop's build of the route table (dl12 S3, dl13) decides it.

### 4. Probe hits no rule binds

- **id14:307 (the SA probe), and :29, :181 and :265.** The "precision floor" is the replay scorer's 20% arming test, not a chain's stop under BUILD-METHOD M4.
- **id10:23 and :39.** "disposition" is the `repeat` disposition, not a review disposal.
- **id13:103.** "its disposition" is an ask's disposition, not a spec-audit finding.
- **id15:76.** "disposed each row" is `design.overlap`'s policy, not a review.
- **RH.** No spec in this group reads a lease, `--claims`, a session, an epoch or tr2 F6.

### 5. Revised parent sections cited but not depended on

- **9:** none.
- **10:** tr2 §3 external edge, §4 "Minting", §8 F6.
- **11:** tr1 §4 writer bullet and the note under the rows (its writer is a named command).
- **12:** none.
- **13:** none (its HD row depends on tr1's writer bullet).
- **14:** none.
- **15:** none.

### 6. Parent text that looks wrong

- tr1 S9's `new` takes only `--tag`, `--writer`, `--check` and `--field` (tr1:105-106). Once tr18 lands, tr18 S1 requires four more columns that no spec gives a flag (tr18:45-47). tr1 AC10's red ("`new` writes a row the gate then refuses", tr1:363) then fires on its own fixture.
- tr1:198-200 ties `hand`'s legality to what tr2 S9 "does not move", but S9 is a one-time pass. A `fields`-form `hand` row registered after it (id13's `seams`) stays legal, while an identical earlier one was moved.
- tr42 S5 classifies only by the `Serves` kind (tr42:53-56), yet tr43 S13 makes it the `record` extractor's sole classifier (tr43:82-84). Every registered kind without a `**Serves:**` line, such as `header` rows and path-keyed kinds, is untaggable.

## Group C, full, led by spec 16 (specs 16, 20, 31, 32, 33, 34, 38 and 46)

# Parents cross-read, Group C: dIndexedDesign specs 16, 20, 31, 32, 33, 34, 38 and 46 against origin/main at `ab976b5b3`

Five MISMATCHes turned up, and every one is pre-existing: the three revision commits caused none. The worst is that four `record_kinds.py new` commands in specs 20 and 38 would be refused as written, because they pass no `--purpose`. None of the three rule sets binds anything in this group. HD's hits read as AGREES, and the revision actually made spec 20's `hand` row legal.

## 1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 16 | The memory-tree adapter `tools/memory-tree/policy_value.py` with `read_policy_value(key, root, rev=None)` is created by tr8 S10 | cite | AGREES | id16:41-42, :153, :265, :422; tr8:81-83 "the memory-tree kit's adapter `tools/memory-tree/policy_value.py`, built to PLAY-dOrderedCharter-7's §4 'The policy reads' contract", and oc7:199 gives `(key, root, rev=None)` |
| 16 | The adapter is "built before this build run" by the parent dTotalRecall | cite | UNKNOWN UNTIL BUILT | id16:153; tr8:315-323 F1's loss route: if the measurement fails, tr8 is retired `WONTDO` "and TOOL-dTotalRecall-16 then creates `policy_value.py` itself" |
| 16 | F4: a parent spec creates the adapter, and dLinkedLibrary and dTotalRecall specs read through it | cite | AGREES | id16:392-398. I re-ran `git grep -l "memory-tree/policy_value.py" ab976b5b3 -- 'memory/builds/*/spec/*'`: the creator is tr8, readers are ll1, 4, 8, 15, 22 and tr2, 3, 4, 5, 7, 16, 43 (count drift only, see section 4) |
| 20 | `record_kinds.py new` and `record-kinds.toml` come from tr1 S1 and S9 | cite | AGREES | id20:47; tr1:66-70 (S1), tr1:106-110 (S9) |
| 20 | S4 and S7 register `diff` and `inventory` with `new <name> --tag --writer --check --field…` only, which the factory accepts | cite | MISMATCH | id20:81-83, :104-106; tr16:36-38, tr1:68-70, tr18:45-49 |
| 20 | `inventory` is a `fields`-form row with `--writer hand`, written by the architect | HD | AGREES | id20:104-106, :154; tr1:196-198 "`hand` is legal on any row TOOL-dTotalRecall-2 S9 does not move". S9 is a one-time rewrite at tr2's pass (tr2:84-88), and this row is registered later, so S9 never moves it. Under the old text (`git diff 4bf0f400d ab976b5b3`: "legal until TOOL-dTotalRecall-2 registers a door") the same row would have been illegal |
| 20 | `[[item]]` and `[[stand-in]]` rows come from dl12 S2 and dl13 S8, and the item factory from dl24 | cite | AGREES | id20:48-49, :164; dl12:36-38; dl13:62-65; dl24:59-61 (S6) |
| 20 | S10: the stand-ins of `item.design.input`, `item.design.reentry` and `item.design.inventory` exist and are deleted together with the landing witness | cite | AGREES | id20:130-134, Rollout; dl13:233-234 lists every row item owned outside dDeclaredLoop, and dl13:241-242 says "an owning build arms its item by landing its witness reader and deleting the row together" |
| 20 | S10: the rows' `returns` name `record-kind.diff` and `record-kind.inventory`, with no version | cite | MISMATCH | id20:133; dl24:144-145 |
| 20 | S6: `item.design.input`'s outcomes (`amendment`, `plan revision`, …) and routes are as dl12 transcribes them | cite | UNKNOWN UNTIL BUILT | id20:94-97, AC6; dl12:129 "`outcomes`, `routes` · yes · Then", and dl13:128-130 "the build pass takes the spelling `TOOL-dDeclaredLoop-12`'s item rows carry" |
| 20 | dl12:118-131 shows the item row already declares its outcomes and routes | cite | AGREES | id20:287; dl12:117-120 is `[item.routes]`, and dl12:129 is the key-table row. The `outcomes =` line itself sits at :114 |
| 20 | dl13:174 and :181: U5 re-enters on `spec wrong`, and F6 reads `item.design.reentry` only as `breaking` | cite | AGREES | id20:183-184, :375; dl13:174 `\| U5 \| unit \| built \| item.design.reentry \| spec wrong \| designed \|` and dl13:181 `\| F6 \| … \| breaking \| decomposed \|`. F1's ask is still open, and the parent text is unchanged |
| 20 | The loop's routing and transition rows are dDeclaredLoop's (dl12, dl13) | cite | AGREES | id20:155-156; dl12:39-44, dl13 §4 tables |
| 31 | The parent bench, ll2 S11, dispatches one scout per case "over its tree and index" | cite | AGREES | id31:92; ll2:112-114 "dispatches one `gov-reuse-scout` agent per case over its tree and index" |
| 32 | tr1 S9 only "appends a conforming row" | cite | AGREES | id32:23, :43; tr1:106-107 "appends a conforming row and refuses one missing a required column" |
| 32 | The untyped head of `RECORD_KIND_TOKENS` is `spec-audit`, `diff-review`, `journal`, `research` | cite | MISMATCH | id32:52-53; tr18:76-80 |
| 32 | The left-shift registry gate would extend tr1 S3 | cite | AGREES | id32:70-71; tr1:76-82 (S3, `check_record_kinds`) |
| 32 | `HYGIENE.md`'s kind list is rendered from the registry by tr1 S6 | cite | AGREES | id32:72; tr1:87-90 |
| 32 | tr25 S6 and ll8 S1 make their kinds bind through `TYPED_RECORD_KINDS` | cite | AGREES | id32:183; tr25:53-59; ll8:70-72 |
| 33 | The `seams` row unit 13 S1 writes goes through `record_kinds.py new` (tr1 S9) | cite | AGREES | id33:37; tr1:106-107 |
| 33 | The scout record's home is ll2 S6's `<date>-build-<unit id>-reuse-scout[-<x>].md`, bound `research` at base, with `read_reuse_scouts` reading over `read_bindings` | cite | AGREES | id33:42-43, :53-54, S2; ll2:78-82 |
| 33 | The left-shift registry gate is tr1 S3's | cite | AGREES | id33:57; tr1:76-82 |
| 34 | The left-shift registry gate is tr1 S3's | cite | AGREES | id34:62; tr1:76-82 |
| 34 | `inventory`'s writer stays `hand` (unit 20 S7) while the kind turns typed | HD | AGREES | id34:59-60; tr1:196-198 (see the spec 20 HD row). The convention for typed members is noted in section 6 |
| 38 | S3: a spec audit is declared when the README carries `spec-audit:` OR when `review.design` prints a value dl19 S8's table derives as owed | cite | MISMATCH | id38:97-100; dl19:73-77, :176-180 |
| 38 | S4: the loop kit's stand-in reader is dl13 S8's and is unbuilt at base | cite | AGREES | id38:105-107; dl13:62-65 (`read_stand_ins`), status DEFERRED |
| 38 | S9: `coverage-lens` is registered by `python record_kinds.py new coverage-lens --tag … --writer "tier2-review.js coverage=only" --check "memory hygiene"` | cite | MISMATCH | id38:120-121; tr16:36-38, tr18:45-49 |
| 38 | S9: the kind list moves into tr1 S6's generated region | cite | AGREES | id38:123-125; tr1:87-90 |
| 38 | br1 supplies the `gov-planner` role and a `plan` entry in `workflows.toml`, which S18 then re-drives | cite | AGREES | id38:153-156, :254, :474-479; br1:80-82 (S4, `plan` with roles `gov-planner`), br1:324-331 (F1: driver `agent`, harness `none`) |
| 46 | S12: the loop kit and its stand-in reader are dl13 S8's and unbuilt, and keeping the four stand-ins until the owner lands is legal | cite | AGREES | id46:124-131; dl13:62-65, :238-240 "a stand-in row whose item is declared with the same owner stays legal, and the list is pruned when the owner lands" |
| 46 | S11: the opt-in follows "the dated rule `check_authorization` applies": README, then `SPEC_AUDIT_DEFAULT`, then `review.design` (no dl unit cited) | cite | MISMATCH | id46:119-122; dl19:73-77, :180 |

## 2. MISMATCHes

**Spec 20 S4 and S7: the factory calls carry no `--purpose` and no tr18 columns.**
- Spec side: id20:81-83 `python record_kinds.py new diff --tag record.diff --writer "design_lib.py --reentry --write" --check "memory hygiene" --field Feature …`, and id20:104-106 `… new inventory --tag record.inventory --writer hand --check "memory hygiene" --field Input …`.
- Parent side:
  - tr16:36 "`record_kinds.py new` refuses a row with no `--purpose`".
  - tr1:69-70 "`layer`, `home`, `readers` and `lifecycle` are admitted and required from TOOL-dTotalRecall-18".
  - tr18:45-46 "Every row … carries non-empty `home`, `lifecycle`, `readers` and `layer`".
  - ll8:65-70 spells the parents' own route: `--purpose "<line>"`, with the tr18 columns set "through TOOL-dTotalRecall-18's landed verb".
- Probe: `git grep -c -- "--purpose" ab976b5b3 -- memory/builds/dIndexedDesign/spec/` matches specs 10 and 11 only. Those two siblings already do it right; 20 and 38 do not.
- Consequence: both commands as written are refused at the build pass, and AC9 checks only that the rows exist.
- Change: add `--purpose "<line>"` to both commands, set `layer`, `home`, `readers` and `lifecycle` through tr18's verb, cite tr16 S2 and tr18 S1 in the external consumes-from edge, and make AC9 red on a missing column, as id10 and id11 already do. This is a rev of id20.
- Cause: pre-existing (none, spec base 4bf0f400d).

**Spec 20 S10: `returns` has no version.**
- Spec side: id20:133 "the `returns` of the second and third name `record-kind.diff` and `record-kind.inventory`".
- Parent side:
  - dl24:144-145 "`returns` is written `record-kind.<name>@<n>`".
  - dl24:146-150 says `[[record-version]]` rows pin each kind's version over the `build_records.py` kind row's fields.
  - tr18:58 reads "the items whose `returns` is `record-kind.<name>@<n>`".
- Change: write `returns = "record-kind.diff@1"` and `"record-kind.inventory@1"`, and add their `[[record-version]]` rows in `tools/loop/item-schema.toml`. Those rows are hashed over the per-kind table rows that id34 S1 adds, so they land in id34's pass or later. This is a rev of id20 S10 and AC9, and a note in id34.
- Cause: pre-existing (none, spec base 4bf0f400d).

**Spec 32 S2: the untyped head is named with `journal`.**
- Spec side: id32:52-53 "`feature-design` joins the untyped head of `RECORD_KIND_TOKENS` beside `spec-audit`, `diff-review`, `journal` and `research`".
- Parent side: tr18:76-80 "`RECORD_KIND_TOKENS` … becomes `("spec-audit", "diff-review", "log", "research") + TYPED_RECORD_KINDS` … `KIND_ALIASES = {"journal": "log"}` beside it is read-only".
- Change: name the head as `spec-audit`, `diff-review`, `log` and `research`, with `journal` a read-only alias (tr18 S7), and cite tr18 S7 as the head's shape at the pass. This is a rev of id32.
- Cause: pre-existing (none, spec base 4bf0f400d).

**Spec 38 S9: same factory-call defect as spec 20.**
- Spec side: id38:121 `python record_kinds.py new coverage-lens --tag record.coverage-lens --writer "tier2-review.js coverage=only" --check "memory hygiene"`.
- Parent side: tr16:36 "refuses a row with no `--purpose`", and tr18:45-46 requires non-empty `home`, `lifecycle`, `readers` and `layer`.
- Change: add `--purpose`, set tr18's columns through its verb, and cite tr16 S2 and tr18 S1 in id38:254's external edge. This is a rev of id38.
- Cause: pre-existing (none, spec base 4bf0f400d).

**Spec 38 S3: the README disjunct overrides dl19 S8.**
- Spec side: id38:97-100 "true when the README carries `spec-audit:` or when `policy.py get review.design --rev <base>` … prints a value TOOL-dDeclaredLoop-19 S8's table derives as owed".
- Parent side:
  - dl19:74 "reads `review.design` first".
  - dl19:180 "`off` · present · no, the key named as unread".
  - dl19:179 "`owed-above-tier` · any · yes when a spec at BASE is Tier-2".
- Consequence: under `off`, or under `owed-above-tier` with no Tier-2 spec, a present README key makes id38's predicate true where the driver says no audit is owed.
- Change: make `check_spec_audit_declared` derive from dl19 S8's table, with `review.design` read first and the README consulted only under `opt-in`. This is a rev of id38 S3 and AC3.
- Cause: pre-existing (none, spec base 4bf0f400d).

**Spec 46 S11: the dated rule is read in the wrong order.**
- Spec side: id46:119-122 "applies the dated rule `check_authorization` applies … a dated README `spec-audit:` key, else a dated `SPEC_AUDIT_DEFAULT` on the default branch, else `review.design` as unit 3 reads it".
- Parent side: dl19:73-77 re-points that same derivation to read `review.design` first, and dl19:180 has the `off` row above.
- Change: state the order dl19 S8 gives `check_authorization` once it lands (`review.design` first, README and default only under `opt-in`), cite dl19 S8, and make AC9 plant `off` with a present README. This is a rev of id46, and of id52, which restates it.
- Cause: pre-existing (none, spec base 4bf0f400d).

## 3. UNKNOWN UNTIL BUILT

- **id16, the adapter's creator:** tr8's build run decides it. Its F1 measurement (30 s or 1 MB) either lands S10's `policy_value.py` or retires tr8 `WONTDO`, in which case tr16 creates the adapter (tr8:315-323).
- **id20 S6, the outcome words:** dl12's build pass decides the exact spelling of `item.design.input`'s outcomes and routes, which it transcribes from flow-steps:235's Then cell (dl12:129, dl13:128-130). id20 reads the row, so only AC6's fixture words could diverge.

## 4. Rule-wide hits that no rule binds

- id16:379 "folded through M4's disposal" is SA vocabulary, but it sits inside F2's rejected option (b) and nothing relies on it.
- id38:409 "high precision" is about AC17's replay-scorer arm being armed. It is not a precision floor read as a chain's stop.
- id20:247 "a hand-edited diff record" means an edit by hand, not the registry writer `hand`.
- id32:72 "A hand edit of `memory/HYGIENE.md`" is the same, not the writer `hand`.
- id38:110, :182, :237 and :384 match `hand` only inside "hand-off".
- id16:105 names the driver's `spec-audit` preflight line, not a spec-audit subject's exit, so SA does not bind.
- RH has no hit anywhere in Group C: no `--lease`, `--claims`, `epoch`, `fleet-tag` or `read_claims`.
- id16:396 "five dLinkedLibrary and dTotalRecall specs" is a run-at-writing count. Today's probe prints 5 dLinkedLibrary plus 7 dTotalRecall readers. Only the count drifted; F4's deciding observation (a parent spec creates the adapter) still holds.

## 5. Revised parent sections each spec cites without depending on them

- 16: none.
- 20: none. Its HD reliance does depend on tr1 §4's revised writer bullet.
- 31: none.
- 32: none. It cites tr1 S3, S6 and S9, which were not revised.
- 33: none.
- 34: none. It depends on tr1 §4's revised writer bullet without citing it.
- 38: none.
- 46: none.

## 6. Parent text that looks wrong

- tr1:191 still defines `hand` as "for a kind no command writes yet", while tr1:196-198 (rev-5) makes `hand` legal on any row S9 does not move. A `fields`-form row registered `hand` after tr2's door lands (id20 S7) is one that `gov_record.py new` could write. tr2 S2 (tr2:52-56) does not say whether the door refuses or admits such a row.
- tr1:212-221's row for typed members (source `build_records.py:<its field tuple>`, writer "its owner's command, else the factory") covers members at dTotalRecall's base only. It says nothing on a kind made typed later with writer `hand` and no `source` (id34 S1 over id20 S7).
- dl12:113's example writes `returns = "record-kind.recommendation"` with no `@<n>`, though dl24:299-303 (F2) says dl12's rows "take the `@<n>` suffix".
