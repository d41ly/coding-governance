**Serves:** research TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-52

# dIndexedDesign's specs against the parent revisions it had not read: a read-only cross-check

Node d, 2026-11-05, base `ab976b5b3` (origin/main). dIndexedDesign has never been cross-read; its spec run began at `4bf0f400d`. Since then `git log 4bf0f400d..ab976b5b3 -- memory/builds/<parent>/spec/` over its parents (dDeclaredLoop, dTotalRecall, dKeptSession, dBoundRoles and dLinkedLibrary) names `63669d505` (2026-11-02, TOOL-dFoldedAudit-8: TOOL-dDeclaredLoop-20 and -32 to rev-3, TOOL-dFairHearing-17 to rev-4) and `66f7b8d32` and `58b395b6e` (2026-11-02 and 2026-11-03, the owner's picks on TOOL-dTotalRecall-2 §8 F6: TOOL-dTotalRecall-2 to rev-8, TOOL-dTotalRecall-1 to rev-5), generated-region rewrites and the no-op merge `e5de11e9e` apart. The owner asked for this pass on 2026-11-05, after a verification found these revisions unread. This record is not an audit: no spec was edited by it, and its mismatches feed the re-ground brief [`2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-reground`](../prompts/2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-reground.md).

**Counts:** 121 assumptions · 95 AGREES · 19 MISMATCH · 7 UNKNOWN UNTIL BUILT, over 22 specs with rows. 13 specs hold a MISMATCH: 1 (row 3); 2 (rows 7 and 9); 5 (row 37); 8 (rows 42 and 43); 9 (row 50); 10 (rows 57 and 58); 11 (row 64); 13 (rows 73 and 77); 14 (row 81); 20 (rows 95 and 99); 32 (row 106); 38 (rows 115 and 117); 46 (row 121). By rule: 2 HD, 17 cite.

## Method

- **Population by citation.** this is the build's first cross-read, so it is FULL: every spec citing any unit of the five parents, as `TOOL-<build>-<n>`, a bare `<build>-<n>` or the build named bare, outside the generated regions, 23 specs (1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 31, 32, 33, 34, 38 and 46), every assumption classified against today's text whether or not a revision touched it. `4bf0f400d` holds every earlier re-ground of the five parents; `git merge-base --is-ancestor` puts `e5de11e9e`, `2bd5e10d4`, `fffe4aadf`, `0689e7fa1` and `933e67399` inside it. The other 17 specs (6, 35 to 37, 39 to 45, 47 to 53) cite no parent unit: their edges name dIndexedDesign siblings only.
- **Population by rule.** The SA probe named 3 (:97) and 14 (:307), RH's none, and HD's 1 (:357, a hand-off) and 8 (:141). The rules: **SA**, the spec-audit rules: a spec subject takes `no-fall`, ends at its target or bound and is promoted ` · to units`; dl20's dispose row folds a local finding on an unbuilt spec; a chain's stop is BUILD-METHOD M4's derived verdict (dl32:47-63, dl20:86-89, :128, fh17:64-65); **RH**, the lease holder read: through TOOL-dPlacedRequest-34 S22's `--lease status build <slug>`, its six-field prefix kept and a seventh class field asked (tr2:196-203, :345-369); **HD**, the `hand` writer: legal on any row tr2 S9 does not move; S9 moves only `fields`-form rows, and the promise of a door for every `hand` row is dropped (tr1:196-201, :223-226).
- **Readers.** Three `gov-spec-reviewer` agents, read-only, one per group of the brief [`2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-crosscheck`](../prompts/2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-crosscheck.md), their handoffs beside it (group A led by spec 1, group B by spec 9, group C by spec 16). Their returns, every MISMATCH's both sides quoted with its `Change:` and `Cause:`, are [`2026-11-05-build-TOOL-dIndexedDesign-1-crosscheck-returns`](2026-11-05-build-TOOL-dIndexedDesign-1-crosscheck-returns.md).
- **The main loop** assembled the table below from the returns' tables by script, stable-sorted by spec, and derived the counts from it. It re-read both sides of the rows the re-ground brief names and changed no verdict.
- **Aliases:** `idN:L` is line L of this build's spec N; `dlN:L`, `fhN:L`, `trN:L`, `prN:L`, `ksN:L`, `brN:L` and `llN:L` of dDeclaredLoop's, dFairHearing's, dTotalRecall's, dPlacedRequest's, dKeptSession's, dBoundRoles' and dLinkedLibrary's spec N; all at `ab976b5b3`.
- **What it does not check:** the 17 specs that cite no parent; anything a parent's build run decides. dOrderedCharter's and dFairHearing's live build runs on node a were not read, only their specs on main. The probes are a text heuristic. No skeptic re-ran the verdicts; the writer re-reads both sides before it edits.
- **The fork fold.** A sibling session was folding the owner's picks on the chain's 47 open forks while the readers ran. Rows are read at `ab976b5b3`; the re-ground re-checks every row that fold moved before it edits.

## Summary table

| # | Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|---|
| 1 | 1 | dl12 S2 seeds `[[item]]` rows for `item.design.ready` and `item.design.exit` (id1:99) | cite | AGREES | dl12:36-38, one row per item of flow-steps' `[design]` table; dl12:138 counts 13 design items; flow-steps:246-247 lists both, owner dIndexedDesign |
| 2 | 1 | dl13 S8 holds a `[[stand-in]]` row for `item.design.exit` (id1:99, :322) | cite | AGREES | dl13:62-65; dl13:227 |
| 3 | 1 | dl13 S8 holds a stand-in row for "the second" item only, exit, and none for `item.design.ready`, which spec 1 carries (id1:6, :99) | cite | MISMATCH | dl13:231-233 |
| 4 | 1 | The stand-in is "the mover naming its witnessing commit" (id1:322) | cite | AGREES | dl13:226-227 |
| 5 | 1 | dl13 states the witness-reader contract in one sentence ("spec line 239") and specifies nothing more; an owning build arms its item by landing its witness reader and deleting its stand-in row (id1:324, :328) | cite | AGREES | dl13:239-240, dl13:86-87. `grep -rn 'witness reader'` over dDeclaredLoop's specs finds only dl13:239 |
| 6 | 1 | dl12 and dl13 are DEFERRED at base (id1:99) | cite | AGREES | dl12:3, dl13:3 |
| 7 | 2 | `record_kinds.py new overlap --tag record.overlap` registers the row through tr1 S9 (id2:71-72, :102) | cite | MISMATCH | tr1:105-107; tr1:68-70; tr16:36-37; tr18:45-46 |
| 8 | 2 | dl12 S2 seeds the row for `item.design.overlaps` (id2:102) | cite | AGREES | flow-steps:241; dl12:36-38 |
| 9 | 2 | Spec 2 carries `item.design.overlaps` (id2:6) and builds its witness, but leaves dl13 S8's stand-in row for that item unmentioned | cite | MISMATCH | dl13:231-233; dl13:86-87 |
| 10 | 2 | Routing an overlap back to decompose is the loop engine's transition, dDeclaredLoop's (id2:91-93) | cite | AGREES | dl13:47 (S5 `derive_move`) |
| 11 | 2 | The registry is tr1's and absent until it lands (id2:282) | cite | AGREES | tr1:3 DEFERRED; tr1:66 |
| 12 | 3 | dl19 S8 specifies the opt-in derivation: `off`/`opt-in`/`owed`/`owed-above-tier`, the `policy` source of `AUTH_SPEC_AUDIT_FROM`, the preflight line, and M4's "When" (id3:34-36, :88-90) | cite | AGREES | dl19:73-80; dl19:173-180 |
| 13 | 3 | dl19 S8 adds the `review.design` read to `check_authorization` (id3:39-40, :111, :128) | cite | AGREES | dl19:73-74 |
| 14 | 3 | An unset `review.design` reads `opt-in`, which dl19 makes today's behaviour (id3:191) | cite | AGREES | dl19:176; dl19:45 |
| 15 | 3 | dl19 §4 reads `review.design` at the landed revision (id3:214, :313, :360) | cite | AGREES | dl19:182 |
| 16 | 3 | `derive_breakpoints` reads `review.<stage>` for `--plan` (dl19 S1) (id3:91) | cite | AGREES | dl19:40-45; dl19:81 |
| 17 | 3 | The README key and `SPEC_AUDIT_DEFAULT` are kept, as dl19 §8 F2 ruled (id3:100) | cite | AGREES | dl19:308-311 |
| 18 | 3 | dl22: `--recommend <slug> --stage design`, its record, the harness `reason` stage, its caller documented in S5/S7, and "a recommendation writes no opt-in" in §3 (id3:93, :115, :317) | cite | AGREES | dl22:11; dl22:73; dl22:84-89; dl22:94-96; dl22:110-111 |
| 19 | 3 | The stage-exit recommendation is dDeclaredLoop's (id3:27) | cite | AGREES | dl22:1 |
| 20 | 3 | `review.design.rounds` and `review.design.round-count` are dDeclaredLoop's keys, read by its review program (id3:97) | cite | AGREES | dl21:8; dl21:30; dl21:65; dl32:52-53 (`verb_review` derives the target from `review.design.rounds`). SA does not bind (see 4) |
| 21 | 3 | dl18 §4: "a kit imports no sibling kit" (id3:225) | cite | AGREES | dl18:146 |
| 22 | 3 | br21 S1 `read_policy_setting` and S2's re-pointed `resolve_stage_efforts` order (id3:60-66, :113) | cite | AGREES | br21:41-54 |
| 23 | 3 | Order steps 1 and 2 to 5 as br21 §4 gives them (id3:169-171) | cite | AGREES | br21:118-122 |
| 24 | 3 | br21 §8 F2 rules out importing a sibling kit (id3:224, :316) | cite | AGREES | br21:285-293 |
| 25 | 3 | br21 S1 turns a `get` exit 2 into a `RolesError` (id3:242, :316) | cite | AGREES | br21:47-48 |
| 26 | 3 | dl19 and br21 are specified and not yet built (id3:81-82, :319) | cite | AGREES | dl19:3; br21:3 |
| 27 | 4 | The scout record's name `<date>-build-<unit id>-reuse-scout[-<x>].md` and its binding (ll2 S6) (id4:37-38, :129) | cite | AGREES | ll2:78-79 binds `**Serves:** research <ids>`, which id4:69 reads as backing no outcome until id13's `seams` kind |
| 28 | 4 | `derive_owed_units` in `reuse_entries.py` keys on `no existing seam fits` (ll1 S4) (id4:38-39, :144) | cite | AGREES | ll1:95-100 |
| 29 | 4 | ll3 S2 puts a derived cutoff on `hasP`, drops the two lookup spellings and adds `-reuse-scout` (id4:39-40, :139-140) | cite | AGREES | ll3:73-79 |
| 30 | 5 | br16 S4: the `experiment` kind, its `[workflow.experiment]` table, R9, the table homed on the entry (id5:36-37, :134, :150, :252) | cite | AGREES | br16:47-50; br16:153-170; br16:149 (`gov-reuse-scout` declares `experiment`) |
| 31 | 5 | br20 S3/S4: `compose_workflows`, the overlay rows, the open registry replacing `WORKFLOW_NAMES` (id5:38, :150) | cite | AGREES | br20:58-71 |
| 32 | 5 | ll2 S11's `reuse-bench.js`, its committed manifest and its `project-owned` row; ll2 S12's `help/reuse.md` names the bench (id5:28, :41, :113-115, :152) | cite | AGREES | ll2:112-119; ll2:120-121 |
| 33 | 5 | ll2's committed bench manifest runs one variant, `house-index`, scorer `scouted-seam` (id5:108-109) | cite | UNKNOWN UNTIL BUILT | ll2:112-119 names the scorer shape and the cases, but no variant or arm name |
| 34 | 5 | ll2's bar of 16 of 24 and 8 of 12 is pinned in §4 (id5:130, :323, :327) | cite | AGREES | ll2:194-197 |
| 35 | 5 | ll13 S1's kind line and `read_declared_kind`; ll13 S2 says `design.research` writes the line (id5:41, :122-123, :152) | cite | AGREES | ll13:35-39; ll13:50-52; ll13:105; ll13:119 |
| 36 | 5 | dl11 maps the directives `researched` and `solution-tested` onto `item.design.research` (id5:124-125) | cite | AGREES | dl11:117-118 |
| 37 | 5 | dl24 S6's factory `loop_items.py new design.research --step step.design …` appends the `item.design.research` row (id5:42, :119-121, :153) | cite | MISMATCH | dl24:61-63; dl24:240-243; dl12:36-38 and :138 with flow-steps:240; dl13:231-233 |
| 38 | 5 | ll30 is an open ask of dLinkedLibrary (id5:143) | cite | AGREES | `memory/builds/dLinkedLibrary/BACKLOG.md:9`, :34 |
| 39 | 7 | tr1 §4 has a `spec` row; tr1 is DEFERRED at base (id7:87) | cite | AGREES | tr1:211; tr1:3 |
| 40 | 7 | tr9 S2 writes the `sections` column (id7:78) | cite | AGREES | tr9:84-85; tr1:203-205 admits it |
| 41 | 8 | tr1 S1 and S9 provide the registry and the factory (id8:49, :363) | cite | AGREES | tr1:66-70; tr1:105-109 |
| 42 | 8 | The three registrations, as spelled, pass tr1 S9's `new` (id8:64-65, :78-79, :93-95) | cite | MISMATCH | tr1:68-70; tr16:36-37; tr18:45-46; ll13:40-50 |
| 43 | 8 | "their writer is `hand`, the class TOOL-dTotalRecall-2 replaces with doors" (id8:141-142) | HD | MISMATCH | tr1:198-200; tr1:224-226; tr1:414-416; tr2:84-88 |
| 44 | 8 | dl12 S2 transcribes every `design.*` item with owner dIndexedDesign, and dl13 S8 holds a stand-in for each until that build lands (id8:50, :173-174, :352) | cite | AGREES | dl12:36-38; flow-steps:235-247 owner column; dl13:231-233 |
| 45 | 8 | S11: the decompose stand-in row leaves when its witness lands, and needs, outcomes and routes stay as dl12 transcribed them (id8:126-127, :229) | cite | AGREES | dl13:86-87; dl13:239-240 |
| 46 | 8 | dl13 S4 owns F1 to F6 (id8:145); dl24 is the item factory (id8:51) | cite | AGREES | dl13:44; dl13:176-181; dl24:61-63 |
| 47 | 8 | tr19 writes `**Edges:** implements=feature.record-door` under a heading (id8:175-176); `feature.<seg>` is dTotalRecall's namespace (id8:217) | cite | AGREES | tr19:182-188; tr9:77-78 (the `feature` extractor, tag `feature.*`) |
| 48 | 9 | tr43 S25 holds a parity arm against `SPEC_TITLE_NUMBERS` (id9:114-115) | cite | AGREES | tr43:138-139 |
| 49 | 9 | tr9 §4 "The section table" keys legacy headings `heading = "1. Goal"`, and its AC3 spells `section.acceptance-criteria` (id9:118, :341-342) | cite | AGREES | tr9:183-193, :290-291. The F3 ask the spec says "the main loop" filed is not in the parent's backlog: `grep 'SPEC_SECTION_TAGS\ | dIndexedDesign-9' memory/builds/dTotalRecall/BACKLOG.md` prints nothing |
| 50 | 9 | S6 and AC8 edit and run `tools/codebase-map/replay-phrases.py` (`_SEC10`, :139) when this build runs (id9:73-74, :210, :285) | cite | MISMATCH | ll3:46-50 deletes the file |
| 51 | 10 | tr1 S9's factory `record_kinds.py new … --writer --check`, with `--purpose` (id10:36-40) | cite | AGREES | tr1:105-106; tr16:36-37 |
| 52 | 10 | tr18's columns are set "through that unit's landed verb" (id10:40-41) | cite | UNKNOWN UNTIL BUILT | tr18 S1 requires the columns (tr18:45-49) but names no verb or flag that sets them |
| 53 | 10 | AC6: tr16 and tr18 require the columns (id10:224) | cite | AGREES | tr16:36-38; tr18:45-49 |
| 54 | 10 | tr1 §4 admits `header` for "a grammar its owner grades", naming the owner's leg in `check` (id10:261-262) | cite | AGREES | tr1:178-180 |
| 55 | 10 | tr25 S4's `fence` form needs a memory-tree validator (id10:257-258) | cite | AGREES | tr25:56-58 |
| 56 | 10 | tr18 §4 "Columns" makes `home` a literal glob (id10:255) | cite | AGREES | tr18:126-133 |
| 57 | 10 | tr42 S5 "makes the kind decide and the home admit", so a `**/*.md` home misgrades nothing and "every path … stays a record of the kind" (id10:251-254) | cite | MISMATCH | tr42:53-58; tr43:82-84; tr53:94-96 |
| 58 | 10 | tr2's door gives the `playbook` row (form `header`) a door, and `hand` holds only until then (id10:99-100) | HD | MISMATCH | tr1:197-200, :224-226; tr2:84-88 |
| 59 | 10 | `--writer hand` on a `header` row is legal (id10:38) | HD | AGREES | tr1:197-200 |
| 60 | 10 | ks18 S5 is the path stand-in and S6 the `help/loop.md` sentence that the S4 landing prunes (id10:70-72) | cite | AGREES | ks18:56-61; ks18 F2 at :186-191 asks for exactly this |
| 61 | 10 | `help/loop.md` is dl1's page (id10:74, :233) | cite | AGREES | dl1:87 |
| 62 | 11 | tr1 S9's factory with `--purpose`; tr16 and tr18 columns (id11:69-77, :218) | cite | AGREES | tr1:105-106; tr16:36-37; tr18:45-49 |
| 63 | 11 | tr18's columns "set through its landed verb" (id11:73) | cite | UNKNOWN UNTIL BUILT | tr18 names no verb (as for spec 10) |
| 64 | 11 | F2: tr42 S5 "has the kind decide and the home admit", so `**/set-*.md` is safe (id11:245-247) | cite | MISMATCH | tr42:53-58. The set record has no `Serves` line: `grep -c Serves tools/unattended/fixture-records/set-dScriptedRepeat.md` prints 0 |
| 65 | 12 | dOrderedCharter is an ancestor through dDeclaredLoop's README `parents:` (id12:33-35) | cite | AGREES | `memory/builds/dDeclaredLoop/README.md:9` reads `parents: dOrderedCharter dFairHearing` |
| 66 | 12 | ll22 S6 spells `decides=` targets through `parse_edge_target`, widened to any node (id12:54-55) | cite | AGREES | ll22:35-37, :84-89 |
| 67 | 12 | ll17 AC3 plants `decides=feature.alpha` (id12:295) | cite | AGREES | ll17:252-255 |
| 68 | 12 | tr19 §4 writes a section edge line under a heading; its only `**Edges:**` lines sit in a fence at :188-189 (id12:126, :158, :181, :290) | cite | AGREES | tr19:181-193 |
| 69 | 12 | tr43 S10 adds the `playbook` `requires_if` row to `tools/memory-tree/kit.toml` (id12:69-71, :100) | cite | AGREES | tr43:73-76 |
| 70 | 13 | ll2 S2, S3, S5 and S6: the house index, `## Steps`, `## Matches`, the record name and `read_reuse_scouts` (id13:28, :37-39, :50-55, :91) | cite | AGREES | ll2:50, :59-64, :71-82 |
| 71 | 13 | `help/reuse.md` is ll2's page (id13:99, :242) | cite | AGREES | ll2:120-122 |
| 72 | 13 | ll3 S1 deletes `reuse-lookup.agent.md` (id13:130) | cite | AGREES | ll3:46 |
| 73 | 13 | S1: `record_kinds.py new seams --tag … --writer hand --check … --field Index` (no `--purpose`, no columns) registers the row through tr1 S9 (id13:48-51) | cite | MISMATCH | tr16:36-37 and AC2 at :167-170; tr1:66-70; tr18:45-49 |
| 74 | 13 | `--writer hand` on a `fields` row added after tr2's pass stays legal (id13:49) | HD | AGREES | tr1:197-200. S9 moves rows at tr2's pass; this row lands later, so S9 never moves it |
| 75 | 13 | dl12 S2's rows and dl13 S8's `[[stand-in]]` rows (id13:40-41, :82-84) | cite | AGREES | dl12:36-38; dl13:62-65 |
| 76 | 13 | dl29 S1 to S4: the `upstream` field, gate `record` as default, no entry `measured`, `## Establishes` grammar with the closed kind set, `derive_upstream_rows` (id13:41, :77-81, :137-138) | cite | AGREES | dl29:33-51 |
| 77 | 13 | S6 adds a non-empty `upstream` to `item.design.decompose` with no `finding` route, and the loader takes it (id13:79-81) | cite | MISMATCH | dl29:65-68 and AC9 at :253-254; decompose's outcomes at flow-steps.md:239; id8:126 keeps them as transcribed |
| 78 | 14 | ll2 S2, S3 and S7: the house index, `## Steps`, the slot (id14:37) | cite | AGREES | ll2:50, :59, :83-87 |
| 79 | 14 | br16 S4 `[workflow.experiment]` with `cases`, `variants`, `fan`, `scorer` and `reruns` (id14:41, :94-98) | cite | AGREES | br16:47-50, :156-168 |
| 80 | 14 | br20 S3 overlay `[[workflow]]` rows in `.governance/instructions.toml` (id14:41, :94-95) | cite | AGREES | br20:58-68, :182 |
| 81 | 14 | ll24 S5 makes a gated class leave "the index the corpus reads" (id14:138-139) | cite | MISMATCH | ll24:68-73, :74-78 |
| 82 | 14 | The ll2 spec is absent at its own base `5fede642` (id14:160-161, :219) | cite | AGREES | `git cat-file -e 5fede642:memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-2.md` prints "exists on disk, but not in '5fede642'", exit 128 |
| 83 | 15 | tr25 registers stream-plan with no writer yet; S2 schema, S3 shape-only check, §4 data model, same-order parallel group (id15:27-28, :61, :88, :158, :171, :327) | cite | AGREES | tr25:34-50, :86-95, :185-187 |
| 84 | 15 | tr4 S1 `FRONT_MATTER_KEYS`; `streams` is derived (id15:80-83, :160-161) | cite | AGREES | tr4:38-40, :44-45 |
| 85 | 15 | The writer cell moves "through TOOL-dTotalRecall-18's landed verb" (id15:88-90) | cite | UNKNOWN UNTIL BUILT | tr18 names no verb |
| 86 | 15 | tr42 S3's `unarmed` key on the stream-plan row (id15:90-91) | cite | AGREES | tr42:47-50 |
| 87 | 15 | The stream-plan row's `hand` writer is replaced by the planner, with no reliance on tr2's door (id15:88-90) | HD | AGREES | tr25:38 (form `fence`); tr1:197-200 |
| 88 | 15 | br1 S4: `plan` entry with `harness none` and driver `agent`, its F1; the `gov-planner` slot (id15:100, :338-339) | cite | AGREES | br1:80-82, :133, :325-326 |
| 89 | 15 | dl12 S2 transcribes `item.design.streams`, with `returns` and `witness` fields (id15:106-113, :313) | cite | AGREES | dl12:36-38, :110-115 |
| 90 | 15 | dDeclaredLoop's route evaluator reads `plan_streams.py when` for the route out of `design.overlaps` (id15:146, :109-110) | cite | UNKNOWN UNTIL BUILT | `grep -rlnE 'streams-when\ | plan_streams' memory/builds/dDeclaredLoop/spec/` prints nothing |
| 91 | 16 | The memory-tree adapter `tools/memory-tree/policy_value.py` with `read_policy_value(key, root, rev=None)` is created by tr8 S10 | cite | AGREES | id16:41-42, :153, :265, :422; tr8:81-83 "the memory-tree kit's adapter `tools/memory-tree/policy_value.py`, built to PLAY-dOrderedCharter-7's §4 'The policy reads' contract", and oc7:199 gives `(key, root, rev=None)` |
| 92 | 16 | The adapter is "built before this build run" by the parent dTotalRecall | cite | UNKNOWN UNTIL BUILT | id16:153; tr8:315-323 F1's loss route: if the measurement fails, tr8 is retired `WONTDO` "and TOOL-dTotalRecall-16 then creates `policy_value.py` itself" |
| 93 | 16 | F4: a parent spec creates the adapter, and dLinkedLibrary and dTotalRecall specs read through it | cite | AGREES | id16:392-398. I re-ran `git grep -l "memory-tree/policy_value.py" ab976b5b3 -- 'memory/builds/*/spec/*'`: the creator is tr8, readers are ll1, 4, 8, 15, 22 and tr2, 3, 4, 5, 7, 16, 43 (count drift only, see section 4) |
| 94 | 20 | `record_kinds.py new` and `record-kinds.toml` come from tr1 S1 and S9 | cite | AGREES | id20:47; tr1:66-70 (S1), tr1:106-110 (S9) |
| 95 | 20 | S4 and S7 register `diff` and `inventory` with `new <name> --tag --writer --check --field…` only, which the factory accepts | cite | MISMATCH | id20:81-83, :104-106; tr16:36-38, tr1:68-70, tr18:45-49 |
| 96 | 20 | `inventory` is a `fields`-form row with `--writer hand`, written by the architect | HD | AGREES | id20:104-106, :154; tr1:196-198 "`hand` is legal on any row TOOL-dTotalRecall-2 S9 does not move". S9 is a one-time rewrite at tr2's pass (tr2:84-88), and this row is registered later, so S9 never moves it. Under the old text (`git diff 4bf0f400d ab976b5b3`: "legal until TOOL-dTotalRecall-2 registers a door") the same row would have been illegal |
| 97 | 20 | `[[item]]` and `[[stand-in]]` rows come from dl12 S2 and dl13 S8, and the item factory from dl24 | cite | AGREES | id20:48-49, :164; dl12:36-38; dl13:62-65; dl24:59-61 (S6) |
| 98 | 20 | S10: the stand-ins of `item.design.input`, `item.design.reentry` and `item.design.inventory` exist and are deleted together with the landing witness | cite | AGREES | id20:130-134, Rollout; dl13:233-234 lists every row item owned outside dDeclaredLoop, and dl13:241-242 says "an owning build arms its item by landing its witness reader and deleting the row together" |
| 99 | 20 | S10: the rows' `returns` name `record-kind.diff` and `record-kind.inventory`, with no version | cite | MISMATCH | id20:133; dl24:144-145 |
| 100 | 20 | S6: `item.design.input`'s outcomes (`amendment`, `plan revision`, …) and routes are as dl12 transcribes them | cite | UNKNOWN UNTIL BUILT | id20:94-97, AC6; dl12:129 "`outcomes`, `routes` · yes · Then", and dl13:128-130 "the build pass takes the spelling `TOOL-dDeclaredLoop-12`'s item rows carry" |
| 101 | 20 | dl12:118-131 shows the item row already declares its outcomes and routes | cite | AGREES | id20:287; dl12:117-120 is `[item.routes]`, and dl12:129 is the key-table row. The `outcomes =` line itself sits at :114 |
| 102 | 20 | dl13:174 and :181: U5 re-enters on `spec wrong`, and F6 reads `item.design.reentry` only as `breaking` | cite | AGREES | id20:183-184, :375; dl13:174 `\ | U5 \ | unit \ | built \ | item.design.reentry \ | spec wrong \ | designed \ | ` and dl13:181 `\ | F6 \ | … \ | breaking \ | decomposed \ | `. F1's ask is still open, and the parent text is unchanged |
| 103 | 20 | The loop's routing and transition rows are dDeclaredLoop's (dl12, dl13) | cite | AGREES | id20:155-156; dl12:39-44, dl13 §4 tables |
| 104 | 31 | The parent bench, ll2 S11, dispatches one scout per case "over its tree and index" | cite | AGREES | id31:92; ll2:112-114 "dispatches one `gov-reuse-scout` agent per case over its tree and index" |
| 105 | 32 | tr1 S9 only "appends a conforming row" | cite | AGREES | id32:23, :43; tr1:106-107 "appends a conforming row and refuses one missing a required column" |
| 106 | 32 | The untyped head of `RECORD_KIND_TOKENS` is `spec-audit`, `diff-review`, `journal`, `research` | cite | MISMATCH | id32:52-53; tr18:76-80 |
| 107 | 32 | The left-shift registry gate would extend tr1 S3 | cite | AGREES | id32:70-71; tr1:76-82 (S3, `check_record_kinds`) |
| 108 | 32 | `HYGIENE.md`'s kind list is rendered from the registry by tr1 S6 | cite | AGREES | id32:72; tr1:87-90 |
| 109 | 32 | tr25 S6 and ll8 S1 make their kinds bind through `TYPED_RECORD_KINDS` | cite | AGREES | id32:183; tr25:53-59; ll8:70-72 |
| 110 | 33 | The `seams` row unit 13 S1 writes goes through `record_kinds.py new` (tr1 S9) | cite | AGREES | id33:37; tr1:106-107 |
| 111 | 33 | The scout record's home is ll2 S6's `<date>-build-<unit id>-reuse-scout[-<x>].md`, bound `research` at base, with `read_reuse_scouts` reading over `read_bindings` | cite | AGREES | id33:42-43, :53-54, S2; ll2:78-82 |
| 112 | 33 | The left-shift registry gate is tr1 S3's | cite | AGREES | id33:57; tr1:76-82 |
| 113 | 34 | The left-shift registry gate is tr1 S3's | cite | AGREES | id34:62; tr1:76-82 |
| 114 | 34 | `inventory`'s writer stays `hand` (unit 20 S7) while the kind turns typed | HD | AGREES | id34:59-60; tr1:196-198 (see the spec 20 HD row). The convention for typed members is noted in section 6 |
| 115 | 38 | S3: a spec audit is declared when the README carries `spec-audit:` OR when `review.design` prints a value dl19 S8's table derives as owed | cite | MISMATCH | id38:97-100; dl19:73-77, :176-180 |
| 116 | 38 | S4: the loop kit's stand-in reader is dl13 S8's and is unbuilt at base | cite | AGREES | id38:105-107; dl13:62-65 (`read_stand_ins`), status DEFERRED |
| 117 | 38 | S9: `coverage-lens` is registered by `python record_kinds.py new coverage-lens --tag … --writer "tier2-review.js coverage=only" --check "memory hygiene"` | cite | MISMATCH | id38:120-121; tr16:36-38, tr18:45-49 |
| 118 | 38 | S9: the kind list moves into tr1 S6's generated region | cite | AGREES | id38:123-125; tr1:87-90 |
| 119 | 38 | br1 supplies the `gov-planner` role and a `plan` entry in `workflows.toml`, which S18 then re-drives | cite | AGREES | id38:153-156, :254, :474-479; br1:80-82 (S4, `plan` with roles `gov-planner`), br1:324-331 (F1: driver `agent`, harness `none`) |
| 120 | 46 | S12: the loop kit and its stand-in reader are dl13 S8's and unbuilt, and keeping the four stand-ins until the owner lands is legal | cite | AGREES | id46:124-131; dl13:62-65, :238-240 "a stand-in row whose item is declared with the same owner stays legal, and the list is pruned when the owner lands" |
| 121 | 46 | S11: the opt-in follows "the dated rule `check_authorization` applies": README, then `SPEC_AUDIT_DEFAULT`, then `review.design` (no dl unit cited) | cite | MISMATCH | id46:119-122; dl19:73-77, :180 |

## The MISMATCHes

Two of the nineteen are the revision's (rows 43 and 58, HD); seventeen were already there at the spec base, which no cross-read had looked at. They fall into seven classes:

- **The registry factory's grammar, rows 7, 42, 73, 95 and 117 (specs 2, 8, 13, 20, 38).** Each `record_kinds.py new` call lacks `--purpose`, which tr16:36-37 refuses, and the `home`, `lifecycle`, `readers` and `layer` columns tr18:45-46 requires; spec 2 also lacks `--writer` and `--check`. Specs 10 and 11 and ll13:40-50 spell it right.
- **The `hand` writer, rows 43 and 58 (specs 8, 10), the revision's.** Both rely on tr2 giving their rows a door; since tr1 rev-5 tr2 S9 moves only `fields`-form rows, and those rows land after tr2's pass.
- **The loop's stand-ins and items, rows 3, 9 and 37 (specs 1, 2, 5).** dl13 S8 derives a stand-in for every item owned outside dDeclaredLoop (dl13:231-233), so `item.design.ready` and `item.design.overlaps` have stand-ins specs 1 and 2 never name; dl12 already transcribes `item.design.research`, so spec 5's factory call would exit 2 and its AC9 is met before the unit builds.
- **The kind classifier, rows 57 and 64 (specs 10, 11).** tr42 S5 decides a record's kind from its `**Serves:**` kind only (tr42:53-56), and tr43 S13 makes it the `record` extractor's sole classifier; a playbook or set record has no Serves line, so neither is ever tagged.
- **Dispositions the loader refuses, row 77 (spec 13).** A non-empty `upstream` on `item.design.decompose` needs a `finding` route, or dl29 S7 (dl29:66-68) refuses the row; AC7 reads the TOML without the loader.
- **Reads of dl19 S8's derivation, rows 115 and 121 (specs 38, 46).** Both read the README key before `review.design`, while dl19 S8 reads `review.design` first and consults the README only under `opt-in` (dl19:73-77, :176-180).
- **Single facts that moved, rows 50, 81, 99 and 106 (specs 9, 14, 20, 32).** ll3 S1 deletes the `replay-phrases.py` spec 9 edits; ll24 S5 cuts gated classes from `cmd_for_paths` but not from the index spec 14's corpus reads; dl24 writes `returns` as `record-kind.<name>@<n>` (dl24:144-145); tr18 S7 renames the untyped head's `journal` to `log` (tr18:76-80).

## Unknown until built

- Rows 52, 63 and 85: the verb that sets tr18's columns; no dTotalRecall spec names it (tr18:45-49). dTotalRecall's build of tr18 decides it.
- Row 90: how dDeclaredLoop's route evaluator reads `plan_streams.py when`. dl12 and dl13's build decides it.
- Row 92: whether tr8 S10 or tr16 creates `policy_value.py`, by tr8 F1's measurement (tr8:315-323).
- Row 33: the variant ll2's committed bench manifest runs. Row 100: the spelling of `item.design.input`'s outcomes dl12 transcribes.

## Asks not filed

- id3 §8 F5's ask to dBoundRoles (a derived default for an unset `review.design.effort`) and F2's to dDeclaredLoop are absent from both builds' `BACKLOG.md`; id3 AC6 depends on the first, since br21:47-48 turns `get`'s exit 2 into a `RolesError`. id9 F3's ask to dTotalRecall is absent too. Filed by this build's run, as each fork says; named here so the run does not assume them filed.

## Parent text that looks wrong (not edited)

- tr1 S9's `new` (tr1:105-107) has no flag for the columns tr16 and tr18 require later, so tr1 AC10's red fires on its own fixture once tr18 lands.
- tr1:198-200 ties `hand`'s legality to what tr2 S9 "does not move", a one-time pass: a `fields`-form `hand` row registered after it stays legal while an identical earlier one was moved. tr1:191 still defines `hand` as "for a kind no command writes yet".
- tr42 S5 classifies by the Serves kind alone while tr43 S13 makes it the sole classifier, so every kind without a Serves line is untaggable.
- br21:45-48 turns `policy.py get`'s exit 2 into a `RolesError`, but `get` refuses every unset key with a derived catalogue default, `roles.effort.default` among them (`tools/policy/catalogue.toml:308-310`).
- dl12:113's example writes `returns` with no `@<n>`, while dl24:299-303 says dl12's rows take it.
- tr1:212-221's typed-member row says nothing of a kind made typed later with writer `hand` and no `source` (id34 S1 over id20 S7).

## For the re-ground

Thirteen specs from the rows, plus 34 and 52, which restate a revised sibling (id20 S10's versioned `returns`, id46 S11's order). The decisions taken: each registration takes `--purpose` and sets tr18's columns through tr18's landed verb, as id10, id11 and ll13 do; rows tr2 S9 never moves keep `hand` and say why, with no door promised; specs 1 and 2 name their stand-ins, 1 keeping `item.design.ready`'s as F5 keeps exit's and 2 arming `item.design.overlaps`'s as id8 S11 arms decompose's; spec 5 arms dl12's existing `item.design.research` row instead of minting one; specs 10 and 11 state that their records are registered but not tagged by the `record` extractor until dTotalRecall gives a non-Serves classifier, the ask their run files; spec 13 adds a `finding` outcome and route to decompose and runs the loader in AC7; specs 38, 46 and 52 derive the audit's opt-in from dl19 S8's order.

## After the re-ground

The owner's fork fold landed on origin/main at `11ebd1e87` after the readers ran, and this branch fast-forwarded to it before any spec was edited. Thirty-seven rows cite a spec the fold revised (id38, dl11 to dl13, dl18, dl29, tr18, tr19, ll8, ll17, ll22 or br20). The lines cited by three of them changed: row 6 (dl12 and dl13's Status lines, both still DEFERRED) and rows 31 and 80 (TOOL-dBoundRoles-20 S3, whose compose verb is now named as dOrderedCharter's ask and which gains S11's scenario rows). All three still read AGREES.

The writers' returns are [`2026-11-05-build-TOOL-dIndexedDesign-1-reground-returns`](2026-11-05-build-TOOL-dIndexedDesign-1-reground-returns.md). The three group writers re-read both sides at the tip and refused no row; fifteen specs moved a rev. Past the items' letter, each named in its spec's §9: spec 8 and spec 20 give their `fields` rows tr42 S2's `unarmed` key until a first record exists; spec 8's fork home is `*-fork-[0-9]*.md`, since `*-fork-*.md` matches three tracked files no fork kind wrote; spec 13 routes decompose's `finding` outcome to `item.design.overlaps`; spec 14 picks the reading where the corpus also cuts gated classes, so both arms rank one class set.

The group writers also found two defects in specs they did not own, folded by one more writer under the follow-up brief [`2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-reground-followup`](../prompts/2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-reground-followup.md) within the same revs: the `--purpose` texts of specs 10, 11 and 13 ran 198, 132 and 137 bytes against TOOL-dTotalRecall-16 S1's 120-byte cap, now 114, 115 and 117; and spec 8 S11's `returns` lacked its version, now `record-kind.feature-design@1`. That writer refused one part: no unit can add spec 8's `[[record-version]]` row, because TOOL-dDeclaredLoop-24 §4 hashes a version from `build_records.py`'s kind rows, which hold typed kinds only, and `feature-design` is untyped (spec 32 S2). Spec 8 S11 now says the pin waits on that parent.

For the parents' owners, unedited: TOOL-dDeclaredLoop-24 §4 needs a hash source for an untyped kind's version; TOOL-dTotalRecall-18 names no verb or flag that sets its four columns, so specs 2, 8, 10, 11, 13, 20 and 38 lean on "tr18's landed verb" (rows 52, 63, 85); tr1 S9's `new` grammar has no column flags; dl12:113's example writes `returns` without `@<n>`. Spec 38's `coverage-lens` schema form stays unstated, as no item named it.

Each revised spec carries one spec-revised record: [`2026-11-05-build-TOOL-dIndexedDesign-1-deviation-13`](2026-11-05-build-TOOL-dIndexedDesign-1-deviation-13.md), [`2026-11-05-build-TOOL-dIndexedDesign-2-deviation-21`](2026-11-05-build-TOOL-dIndexedDesign-2-deviation-21.md), [`2026-11-05-build-TOOL-dIndexedDesign-5-deviation-51`](2026-11-05-build-TOOL-dIndexedDesign-5-deviation-51.md), [`2026-11-05-build-TOOL-dIndexedDesign-8-deviation-82`](2026-11-05-build-TOOL-dIndexedDesign-8-deviation-82.md), [`2026-11-05-build-TOOL-dIndexedDesign-9-deviation-91`](2026-11-05-build-TOOL-dIndexedDesign-9-deviation-91.md), [`2026-11-05-build-TOOL-dIndexedDesign-10-deviation-101`](2026-11-05-build-TOOL-dIndexedDesign-10-deviation-101.md), [`2026-11-05-build-TOOL-dIndexedDesign-11-deviation-111`](2026-11-05-build-TOOL-dIndexedDesign-11-deviation-111.md), [`2026-11-05-build-TOOL-dIndexedDesign-13-deviation-131`](2026-11-05-build-TOOL-dIndexedDesign-13-deviation-131.md), [`2026-11-05-build-TOOL-dIndexedDesign-14-deviation-141`](2026-11-05-build-TOOL-dIndexedDesign-14-deviation-141.md), [`2026-11-05-build-TOOL-dIndexedDesign-20-deviation-203`](2026-11-05-build-TOOL-dIndexedDesign-20-deviation-203.md), [`2026-11-05-build-TOOL-dIndexedDesign-32-deviation-322`](2026-11-05-build-TOOL-dIndexedDesign-32-deviation-322.md), [`2026-11-05-build-TOOL-dIndexedDesign-34-deviation-343`](2026-11-05-build-TOOL-dIndexedDesign-34-deviation-343.md), [`2026-11-05-build-TOOL-dIndexedDesign-38-deviation-385`](2026-11-05-build-TOOL-dIndexedDesign-38-deviation-385.md), [`2026-11-05-build-TOOL-dIndexedDesign-46-deviation-462`](2026-11-05-build-TOOL-dIndexedDesign-46-deviation-462.md), [`2026-11-05-build-TOOL-dIndexedDesign-52-deviation-522`](2026-11-05-build-TOOL-dIndexedDesign-52-deviation-522.md). No fork was opened or resolved.
