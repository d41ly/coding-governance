**Serves:** research TOOL-dLinkedLibrary-1

# dLinkedLibrary's specs against dTotalRecall's re-grounded specs: a read-only cross-check

Node d, 2026-10-28, base `1a61f21a2` (origin/main). dLinkedLibrary's spec run began at `82a392696`, the
parent of its first spec commit `5a9183011`. That base holds the second wave's re-grounds but none of
the third wave's: dTotalRecall's (`794a0f5fb`, landed as `2bd5e10d4`), dBoundRoles' (`ac8ab8d5f`,
landed as `fffe4aadf`) or dKeptSession's (`ff44fb2a2`, landed as `0689e7fa1`). Their deviation records
confirm what each revised: dTotalRecall units 1, 2, 4, 8, 9, 11, 15, 18, 19, 20, 22, 25, 26, 43 and 76;
dBoundRoles units 1, 2, 3, 5, 6, 11, 12, 14, 20, 21, 22, 23, 25, 43 and 60; dKeptSession units 1, 5, 7
to 13, 18, 20, 25, 36, 44 and 56. This record compares each assumption the exposed specs make about a
parent with what the parents' DEFERRED specs say now. It is not an audit: no spec was edited, no review
harness ran, and the mismatches feed the re-ground brief
[`2026-10-28-prompt-TOOL-dLinkedLibrary-1-parents-reground`](../prompts/2026-10-28-prompt-TOOL-dLinkedLibrary-1-parents-reground.md).

**Counts:** 85 assumptions · 45 AGREES · 36 MISMATCH · 4 UNKNOWN UNTIL BUILT, over 30 specs (the 23
citation specs and the 7 rule-wide hits the readers found bound; the other 23 hits are not bound). 20
specs hold at least one MISMATCH: 1, 2, 3, 4, 7, 8, 9, 10, 12, 13, 14, 16, 17, 19, 22, 23, 46, 47, 52
and 74. By rule: 12 citation, 7 R1, 2 R2, 13 R3 and 2 R4. 4 mismatches sit outside the citation
population, found only by rule scoping: rows 34 (ll10, R1), 67 and 68 (ll23, R1 and R4) and 85 (ll74,
R3). Every mismatch was already one at `82a392696` except part of row 26: ll8's unversioned `returns`
was already against dl24, and tr18's re-ground moved its `written by` join onto the
`record-kind.<name>@<n>` form, so the row now also misses that join.

## Method

- **Population by citation.** `grep -oE` over `spec/*.md` for the units the three re-grounds revised,
  both `<FAMILY>-<build>-<n>` and the bare `<build>-<n>`. That gives 23 specs; only spec 20 also cites a
  dBoundRoles unit (br14), and none cites a dKeptSession unit.
- **Population by rule.** The last wave found that citation misses a rule a parent applies to every
  spec. The brief restates R1 to R8 from the parents' cross-check records and the third wave's own
  seams, and a text probe for each over the other 68 specs named 30 candidates. The readers found 7 of
  them bound (ll6, ll10, ll11, ll18, ll23, ll64, ll74), of which ll10, ll23 and ll74 hold a mismatch;
  the rest import their own kit's library, cite a parent line as evidence, or are not kit code.
- **Readers.** Four `gov-spec-reviewer` agents, read-only, one per group of the brief
  [`2026-10-28-prompt-TOOL-dLinkedLibrary-1-parents-crosscheck`](../prompts/2026-10-28-prompt-TOOL-dLinkedLibrary-1-parents-crosscheck.md),
  their handoffs beside it. Groups A1 and A2 are the citation population and applied R1 to R8 to their
  own specs; groups B1 and B2 verified the rule-wide hits. Their returns, with every MISMATCH's both
  sides quoted, its `Change:` and its `Cause:`, are
  [`2026-10-28-build-TOOL-dLinkedLibrary-1-crosscheck-returns`](2026-10-28-build-TOOL-dLinkedLibrary-1-crosscheck-returns.md).
- **The main loop** assembled the table from the returns' tables by script, sorted by spec, and
  derived the counts from it. It changed no verdict. Two readers' prose counts disagree with their own
  tables (A1 says 37 rows, its table holds 42; A2 says 31, its table 32); the tables win.
- **Aliases:** `llN:L` is line L of `spec/2026-10-2?-spec-TOOL-dLinkedLibrary-N.md`; `trN:L`, `brN:L`,
  `ocN:L`, `dlN:L`, `wbN:L` and `prN:L` of the parents' spec N under `../../<build>/spec/`; all at
  `1a61f21a2`.
- **What it does not check:** anything a parent's build run decides; dSafePassage and dGroundRules
  surfaces dLinkedLibrary names directly; specs neither population reached. The rule-wide probe is a
  text heuristic, so a spec that breaks a rule without using any of its probe words is missed. No
  skeptic re-ran the verdicts. Instead each re-ground writer re-reads both sides before it edits, and
  returns a row it cannot bear out as refused.

## What the mismatches have in common

- **A sibling kit reached in process (ll1, ll2, ll4, ll7, ll8, ll12, ll16, ll17, ll19, ll22, ll52,
  ll74).** R3, the largest class, as in every earlier wave. Memory-tree code reads policy keys through
  the policy kit's `resolve` (ll1, ll8) or `policy.resolve` (ll22) where tr8 S10's `policy_value.py`
  adapter runs `policy.py get`; the codebase-map kit calls the playbook kit's `read_policy_value` (ll2);
  memory-tree, playbook, drift-audit, codebase-map and workflows modules call each other's functions
  (ll4, ll12, ll16, ll17, ll19, ll52, ll74); a hook `require`s `policy-mirror.js` (ll7), which ks8's
  re-ground replaced with a spawn. Pre-existing.
- **A leg written by hand with no `enforces` (ll7, ll9, ll10, ll23, ll46, ll47, ll52).** R1. ll7, ll9,
  ll10 and ll23 write rows into `tools/gate-legs.json`, which wb11 makes a render of the kit
  declarations; ll46, ll47 and ll52 S32 declare through the factory but name no `enforces`, which oc7
  S3 reds. ll52 S32, the batch that re-declares units 7, 9, 10 and 23's legs, leaves it out too.
  Pre-existing.
- **The record-kind factory's columns (ll1, ll3, ll4, ll8, ll13, ll22).** Citation. Each
  `record_kinds.py new` call omits the `--purpose` tr16 requires and the `home`, `layer`, `lifecycle`
  and `readers` columns tr18 requires; tr25 S1 shows the full call. ll3 names a function as `writer`,
  ll22 registers a front-matter kind in the `fields` form, and ll52 claims a value check tr1 does not
  make. Pre-existing.
- **Typed kinds and the door (ll1, ll8, ll13).** R2 and citation. ll8 names `census` and `ruling`
  records `-<kind>-<n>.md` with no `TYPED_RECORD_KINDS` join and expects tr18 S7 to admit them; ll1
  writes a `journal` record where tr18 makes `log` the written value; ll13 has the door write a
  `kind:` line its template does not render. Pre-existing.
- **dl12's row schema (ll8, ll23).** R4. Unversioned `returns`, command actors with no `inputs`, a
  route to `done` and two actors on one item (ll8), and an `item.adopt.instructions` row given as four
  facts (ll23). Pre-existing, with part of ll8's from tr18's re-ground.
- **Single defects, pre-existing:** ll14's arm names the `code record` leg for a `--selftest` it does
  not run; ll16 calls `code_record.py --tree`, which tr8 defines only as a modifier.

## Summary table

| # | Spec | Group | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|---|---|
| 1 | ll1 | A1 | tr1 S9's `record_kinds.py new decision --tag … --writer hand --check …` appends a conforming row with home `memory/DECISIONS.md` | cite | MISMATCH | ll1:121-125; tr1:101-103, tr1:65-67; tr18:45-47; tr16:36; tr25:33-37 |
| 2 | ll1 | A1 | `writer = "hand"` stays legal for a `rows`-form kind after tr2 | cite | AGREES | ll1:123-124; tr2:77-81; tr1:194-196 |
| 3 | ll1 | A1 | `record_kinds.py --check` is tr1's gate and passes with the row (AC9) | cite | AGREES | ll1:353-356; tr1:75-83 |
| 4 | ll1 | A1 | the reuse-proposal record is written by `reuse_entries.py` itself as `**Serves:** journal` | R2 | MISMATCH | ll1:74-76; tr18:76-82, tr18:95-97; tr2:45-50, tr2:77-79 |
| 5 | ll1 | A1 | memory-tree code reads `reuse.propose` and `decisions.major` through the policy kit's `resolve` (`policy.py:752`) | R3 | MISMATCH | ll1:84, ll1:105; oc7:202-206; TOOL-dGroundRules-1:113 |
| 6 | ll1 | A1 | `decision` is a registry row, not a typed `-<kind>-<n>.md` record, so it owes no `TYPED_RECORD_KINDS` join | R2 | AGREES | ll1:121-125; oc42:45-49 |
| 7 | ll2 | A1 | `gov_code.py callers` reads the core `code` record (tr8 S7) | cite | AGREES | ll2:37-38; tr8:69-73 |
| 8 | ll2 | A1 | `house_index.py` (codebase-map) reads `reuse.delivery` through `read_policy_value` (PLAY-dOrderedCharter-7 §4) | R3 | MISMATCH | ll2:39, ll2:90-91, ll2:132; oc7:197-212 |
| 9 | ll2 | A1 | `render_handoff` (roles) runs `house_index.py --slot` as a subprocess found by `resolve_kit_dir` | R3 | AGREES | ll2:83-88; oc7:202-206 |
| 10 | ll3 | A1 | `record find` (tr9 S3) exists, with `query.py` as its thin adapter | cite | AGREES | ll3:38, ll3:127-129; tr9:89-96 |
| 11 | ll3 | A1 | the `recall-index` row lands through `record_kinds.py new recall-index` with writer `tag_index.build_index` | cite | MISMATCH | ll3:126-130; tr1:186-196; tr1:101-103; tr18:45-47; tr16:36 |
| 12 | ll4 | A1 | the memory-tree `extract_code` copy (tr8 S2) and the policy adapter (tr8 S10) exist | cite | AGREES | ll4:40-43; tr8:48-51, tr8:81-89 |
| 13 | ll4 | A1 | `annotation-index` lands through `record_kinds.py new … --writer generator:… --check "codebase-map coverage + freshness"` | cite | MISMATCH | ll4:84-87; tr1:101-103; tr18:45-47; tr16:36; leg name probed: present |
| 14 | ll4 | A1 | tr9 §3 gives the annotations system to dLinkedLibrary (F3) | cite | AGREES | ll4:405-407; tr9:143-144 |
| 15 | ll4 | A1 | memory-tree `annotations.py` reads `TAG_RE` from the playbook kit's `tag_index.py` via `resolve_kit_dir` | R3 | MISMATCH | ll4:60-61; oc19:47-49; oc7:202-204; `tools/memory-tree/kit.toml:7-8` (no `playbook` row) |
| 16 | ll4 | A1 | playbook `edge_grammar.py` calls memory-tree's `parse_note_line`; drift-audit imports `annotations.py`; `gen_map.py` imports it | R3 | MISMATCH | ll4:100-102, ll4:124-126, ll4:204-208; oc7:202-204; TOOL-dGroundRules-1:113 |
| 17 | ll5 | A1 | the build README carries tr4 S5's routing region, which the `<build>` cell links to | cite | AGREES | ll5:47-49, ll5:85; tr4:56-57 |
| 18 | ll6 | B1 | The research view reads every build's records bound `**Serves:** research` and selected by ll13's `kind: research-return` line. It mints no Serves token, no typed kind and no `new <kind>` door, and `research` is still an untyped kind the parents serve. | R2 | AGREES | ll6:54-59, ll6:203-207; ll13:37-41, ll13:204 (no new Serves token); tr1:67-71, tr1:208 (`research` is a `fields` row, Serves only); oc42:35-39 (`research` stays outside `TYPED_RECORD_KINDS`) |
| 19 | ll7 | A1 | the memory-tree policy adapter (tr8 S10) is a precondition | cite | AGREES | ll7:44; tr8:81-89 |
| 20 | ll7 | A1 | three legs (`annotations`, `annotations selftest`, `annotations-read self-test`) are hand-written rows in `tools/gate-legs.json`, with no `enforces` | R1 | MISMATCH | ll7:47-63, ll7:93-97, ll7:193; wb11:36-47, wb11:57-58; oc7:58-63; tr9:97-103 |
| 21 | ll7 | A1 | `annotations-read.js` (hooks) `require`s `../policy/policy-mirror.js` for `readPolicy` and a new `resolveBash` | R3 | MISMATCH | ll7:74-77, ll7:90-92; oc7:202-204; dKeptSession record :106, :330-332 |
| 22 | ll8 | A1 | the factory and the tr18 columns are preconditions; the `census`/`ruling`/`baseline` rows name form, writer, check and fields only | cite | MISMATCH | ll8:46-48, ll8:58-65; tr18:45-47; tr16:36; tr25:33-37 |
| 23 | ll8 | A1 | the door `gov_record.py new <kind>` sits over `write_new_record` in `build_records.py` and takes `--field` | cite | AGREES | ll8:48-50; tr2:39-44 |
| 24 | ll8 | A1 | door-written kinds join the Serves kinds through tr18 S7, so `tree_lib.py:406` is left alone | cite | MISMATCH | ll8:422-425; tr18:76-80; oc42:35-40 |
| 25 | ll8 | A1 | `census` and `ruling` records named `-<kind>-<n>.md` and served as their own kind need no `TYPED_RECORD_KINDS` or factory-table join | R2 | MISMATCH | ll8:189-190, ll8:60; tr2:51-55; oc42:25, oc42:35-49, oc42:57 |
| 26 | ll8 | A1 | the item rows: `returns` with no `@<n>`; command actors with no `inputs`; routes to `done`; two actors on one item | R4 | MISMATCH | ll8:236-240; dl24:144-145; dl12:39-44, dl12:125-128; tr18:52-56 |
| 27 | ll8 | A1 | `adopt_program.py` (memory-tree) reads the three `retrofit.*` keys through `resolve` | R3 | MISMATCH | ll8:127-128, ll8:48-50; oc7:202-206 |
| 28 | ll8 | A1 | `core.py adopt` dispatches to memory-tree by subprocess | R3 | AGREES | ll8:71-75; oc7:202-206 |
| 29 | ll8 | A1 | `program = "adopt"` in place of `step` is admitted (F2's ask to dDeclaredLoop) | R4 | UNKNOWN UNTIL BUILT | ll8:296-305; dl12:34-35, dl12:122-123 |
| 30 | ll9 | A1 | `read_header_edges` reads column-0 lines for an untyped record and fields for a typed one (tr19 S1) | cite | AGREES | ll9:39-44; tr19:52-56 |
| 31 | ll9 | A1 | the door and `write_new_record` (tr2 S1 to S5) | cite | AGREES | ll9:34; tr2:39-66 |
| 32 | ll9 | A1 | `record find` rows are `key · kind · build · bytes · path:line`, and `record show` slices (tr9 S3, S5) | cite | AGREES | ll9:64-68; tr9:94-96, tr9:104-107 |
| 33 | ll9 | A1 | two legs (`record origin …`, `record origin selftest`) are written into `tools/gate-legs.json`, with no `enforces` | R1 | MISMATCH | ll9:59-63, ll9:188; wb11:36-47, wb11:57-58; oc7:58-63 |
| 34 | ll10 | B1 | The new leg `retrofit progress selftest` is written by hand into `tools/gate-legs.json`, with no `enforces`. | R1 | MISMATCH | ll10:155, ll10:216-219; oc7:58-63; wb11:36-47 |
| 35 | ll10 | B1 | `retrofit_progress.py` reads the ledger through memory-tree's own inline `legacy_ledger.py`. `manifest-check.sh` reaches the module by `resolve_kit_file` and runs it as a bounded subprocess. | R3 | AGREES | ll10:31-35, ll10:47-50; wb13:57-58 (S8, the inline copy in `tools/memory-tree/`) |
| 36 | ll11 | B2 | S6 deletes the drift builder, which removes drift-audit's in-process import of memory-tree's `annotations.py`. The seed argv (S3) reaches `annotations.py` as a subprocess. | R3 | AGREES | ll11:88-91 "which the builder imports; the deletion removes that import"; ll11:47-48 the `seed = ["python3", "{prefix}/memory-tree/annotations.py", …]` argv; oc7:202-205 "A kit may not import a sibling kit" |
| 37 | ll12 | A1 | tr9 S1's `extract_marker` and the `marker` namespace row | cite | AGREES | ll12:27-28, ll12:33-35; tr9:81-82 |
| 38 | ll12 | A1 | memory-tree `annotations.py` reads the namespace row through the playbook kit's `read_namespaces` | R3 | MISMATCH | ll12:33-35, ll12:82; oc19:51-54, oc19:258; oc7:202-204 |
| 39 | ll13 | A1 | `research-return` lands through `record_kinds.py new … --writer hand --check …`, form `header`, home `memory/builds/*/*/*.md` | cite | MISMATCH | ll13:38-42; tr1:101-103; tr18:45-47; tr16:36 |
| 40 | ll13 | A1 | tr2's record door is a future writer of the `kind: research-return` line | cite | MISMATCH | ll13:95-97; tr2:51-55, tr2:77-79 |
| 41 | ll13 | A1 | `instrument` is a registered kind (tr18) and `design-record` one (tr1) | cite | AGREES | ll13:134-137; tr18:59-62; tr1:208-212 |
| 42 | ll14 | A1 | tr8's `derive_code_record` and its four tables, with edge types `calls`/`tests`/`mention`/`invokes`/`registers` | cite | AGREES | ll14:32-35; tr8:69-73, tr8:144, tr8:194, tr8:275-276 |
| 43 | ll14 | A1 | the `code record` leg runs `gov_code.py --selftest` beside `code_record.py --selftest` | cite | MISMATCH | ll14:249; tr8:100-106 |
| 44 | ll14 | A1 | `grep_words` is carried inline under a parity row, as in tr8 S5 | cite | AGREES | ll14:278-281; tr8:60-65 |
| 45 | ll15 | A1 | tr8 S2 and S7's key and `code_row.hash`, and the S10 adapter | cite | AGREES | ll15:35-39; tr8:69-73, tr8:81-89 |
| 46 | ll15 | A1 | the `code_purpose(blob, …)` table is written "through PLAY-dOrderedCharter-19 S4's `build_index`" | cite | UNKNOWN UNTIL BUILT | ll15:49-51; tr8:69-73; oc19:64-65 |
| 47 | ll16 | A2 | The record at a past tree comes from `code_record.py --tree <rev>` | cite | MISMATCH | ll16:42; tr8:44, :188 |
| 48 | ll16 | A2 | tr8 §3 gives the `code` slot to dBoundRoles, and no dBoundRoles spec carries it | cite | AGREES | ll16:233; tr8:136; `git grep "code slot\ | memory.code-budget\ | code-roles" 1a61f21a2 -- memory/builds/dBoundRoles/spec/` printed nothing |
| 49 | ll16 | A2 | `replay_scorer.py` (workflows kit) calls memory-tree's `derive_callers`/`derive_callees`/`derive_tests` and runlog's readers in process | R3 | MISMATCH | ll16:40, :61, :100; `tools/workflows/kit.toml:10` |
| 50 | ll17 | A2 | tr8 S2 `extract_ranges` adds `end_line` on tr13's block, and S7 stores `code_row(blob, kind, key, name, line, end_line, hash, text)` keyed `<path>::<qualified name>` | cite | AGREES | ll17:41-43, :112-114; tr8:48-50, :69, :126, :152 |
| 51 | ll17 | A2 | tr9 S1 registers the `class` namespace, tag `class.<name>` | cite | AGREES | ll17:43; tr9:79-80 |
| 52 | ll17 | A2 | `tools/playbook/edge_grammar.py` adapters call memory-tree's `gotchas.parse_front_matter`, `derive_decision_rows` and `scan_annotations`, and codebase-map's `parse_dossier`, in process | R3 | MISMATCH | ll17:44, :56, :64, :138, :196 |
| 53 | ll18 | B2 | Eleven kits share the region factory as inline parity-gated copies, never by import from another kit. | R3 | AGREES | ll18:72-77 "Each Python site inlines the `region_py` block once per kit module … `format-guard.js` carries `region_js`"; oc7:202-204 "a kit carries shared code inline"; dGroundRules-1 §4:113 "so a kit carries shared code inline" |
| 54 | ll19 | A2 | tr8 S12 admits `symbols` and re-keys staleness to body hashes | cite | AGREES | ll19:38, :98; tr8:94-98 |
| 55 | ll19 | A2 | tr9 S1's `extract_feature` lands anchor rows only, and its row names no source this unit owns | cite | AGREES | ll19:40-45; tr9:77-78 |
| 56 | ll19 | A2 | memory-tree's `record_extract.py` reads codebase-map's `read_feature_nodes` in process, "an optional sibling through the inlined `resolve_kit_dir`" | R3 | MISMATCH | ll19:40-45, :182; `tools/memory-tree/kit.toml:8` (no codebase-map row) |
| 57 | ll20 | A2 | tr9 S1 registers the `feature` row and names no `role` | cite | AGREES | ll20:107, :171; tr9:77-78 |
| 58 | ll20 | A2 | br14 S5 `check_role_bindings` binds a role's `rules:` to the units naming it | cite | AGREES | ll20:83-85; br14:59-62 |
| 59 | ll20 | A2 | br14 registers `role` as a `selects` row | cite | AGREES | ll20:109-110; br14:116, :131 |
| 60 | ll20 | A2 | br14 S8 extends `gov_tag.py --fixture` | cite | AGREES | ll20:263; br14:70-71 |
| 61 | ll21 | A2 | tr8 S2, S7, S9 and S10 (key form, tables, `degraded`, `memory.code-languages`, exit 2 on a missing ctags) and AC8's stub | cite | AGREES | ll21:31-35, :42, :115; tr8:69-89, :290-294 |
| 62 | ll21 | A2 | tr8 §4's body-hash rule for built-in rows | cite | AGREES | ll21:55; tr8:146-149 |
| 63 | ll22 | A2 | tr1 S9 `record_kinds.py new <name> --tag --writer --check --field` exists | cite | AGREES | ll22:34-35, :54-56; tr1:101-105 |
| 64 | ll22 | A2 | That `new` call with no `home`/`layer`/`lifecycle`/`readers` writes a conforming `gotcha` row | cite | MISMATCH | ll22:54-56; tr1:66; tr18:45-49 |
| 65 | ll22 | A2 | A front-matter kind registered through `--field` is graded as tr1 grades it | cite | MISMATCH | ll22:37-39, :54-56; tr1:83-85, :174-176 |
| 66 | ll22 | A2 | `gotchas.py` reads the `platforms.supported` allowed set through `policy.resolve` in process | R3 | MISMATCH | ll22:35, :41, :292; oc7:202-205, :379-380 |
| 67 | ll23 | B1 | The new leg `adopt instructions selftest` is written by hand into `tools/gate-legs.json`, with no `enforces`. | R1 | MISMATCH | ll23:197, ll23:267-270; oc7:58-63; wb11:36-47 |
| 68 | ll23 | B1 | `item.adopt.instructions` is a complete dl12 row from four facts: actor `command`, needs, proven-by, and "each proposal an owner item". It names no actor name, no `inputs`, no `returns`, no `outcomes` and no `routes`. | R4 | MISMATCH | ll23:88-91; dl12:43, dl12:109, dl12:113, dl12:127-129, dl12:147-148; ll8:232-240 (the sibling adopt rows name the actor, `returns` and routes) |
| 69 | ll23 | B1 | The row's step slot, an adopt item that belongs to none of the five steps | R4 | UNKNOWN UNTIL BUILT | dl12:80-81; ll8:122-126, ll8:379-388 (F2 asks for `program = "adopt"` in place of `step`) |
| 70 | ll37 | A2 | tr2's door `gov_record.py new <kind>` writes the ruling plant's record | cite | AGREES | ll37:52-54, :78; tr2:30, :39-44 |
| 71 | ll37 | A2 | The door mints in a remote-less scratch repo with no lease or claim | cite | UNKNOWN UNTIL BUILT | ll37:144-145; tr2:188-196, :335 |
| 72 | ll40 | A2 | tr9 S1's `marker` row holds no member list | cite | AGREES | ll40:33, :43-45; tr9:81-82 |
| 73 | ll46 | A2 | tr8 S13's `code record` leg runs `code_record.py --check`, not `--selftest` | cite | AGREES | ll46:25, :57, :73-74; tr8:100 |
| 74 | ll46 | A2 | `code_record.py --selftest` exists with its own plants | cite | AGREES | ll46:35-37; tr8:310 |
| 75 | ll46 | A2 | A memory-tree leg is declared in `tools/memory-tree/kit.toml` through the factory | cite | AGREES | ll46:40-44; tr8:100-103 (rev-3 moved `code record` there too) |
| 76 | ll46 | A2 | The new leg's `enforces` is named | R1 | MISMATCH | ll46:43-44, AC3 :120-123; oc7:58-63; tr8:104-106, AC10 :299-304 |
| 77 | ll47 | A2 | tr1 S3's `record-kinds` leg is `record_kinds.py --check` | cite | AGREES | ll47:24, :50, :67; tr1:73-77 |
| 78 | ll47 | A2 | The new leg's `enforces` is named | R1 | MISMATCH | ll47:36-37, AC1 :101-104; oc7:58-63 |
| 79 | ll52 | A2 | The `ruling` row lands in tr1's registry | cite | AGREES | ll52:73; tr1:58-66 |
| 80 | ll52 | A2 | A door field check that lands with tr1 reads the `ruling` row's values | cite | MISMATCH | ll52:71-74, :75-77; tr1:83-85, :174-176; tr2:56-60 |
| 81 | ll52 | A2 | S32 legs re-declared through `leg_factory.py new` carry `enforces` | R1 | MISMATCH | ll52:141-143, AC16 :363-366; oc7:58-63 |
| 82 | ll52 | A2 | S17, S42 and S51 reach sibling kits' modules in process | R3 | MISMATCH | ll52:91-92, :170-172, :195-198 |
| 83 | ll64 | B1 | S10 and S11 re-guard the `adopt program selftest` and `code record selftest` legs in their `tools/memory-tree/kit.toml` declarations, and `tools/gate-legs.json` is the render. Both legs already carry `enforces` from ll46 and ll47. | R1 | AGREES | ll64:76-81, ll64:109-111, ll64:183, ll64:242-244; wb11:36-47; ll46:40-43; ll47:33-36; oc7:109-111 reds guard plus `enforces` only under `never`, and gov runs `with-hooks-report` (`.governance/policy.json:173-176`, `tools/policy/catalogue.toml:29-32`) |
| 84 | ll74 | B2 | The `tree_kill_py` block (canonical in run-gates `regen.py`) is carried inline in memory-tree's `gotchas.py`. `region_py` and `region_nth` are inline copies. | R3 | AGREES | ll74:68-70 (S10), ll74:125-129 (S25), ll74:87-92 (S16), ll74:93-97 (S17); oc7:202-204 |
| 85 | ll74 | B2 | `dossier_move.py`, in the codebase-map kit, validates `--build` and `--unit` against memory-tree's `SLUG_RE` and `GRANT_ID_RE`, reused rather than re-implemented. | R3 | MISMATCH | ll74:130-132; ll74:363-364; ll74:215; oc7:202-205; wb28:63-64 |

## The mismatches, both sides quoted

Each reader wrote the bullets for its own specs, with both sides quoted, the `Change:` and the
`Cause:`. They are kept once, in section 2 of each group's return in
[`2026-10-28-build-TOOL-dLinkedLibrary-1-crosscheck-returns`](2026-10-28-build-TOOL-dLinkedLibrary-1-crosscheck-returns.md):
Group A1 (ll1, ll2, ll3, ll4, ll7, ll8, ll9, ll12, ll13, ll14), Group A2 (ll16, ll17, ll19, ll22,
ll46, ll47, ll52), Group B1 (ll10, ll23) and Group B2 (ll74).

## UNKNOWN UNTIL BUILT

- **Rows 29 (ll8 F2) and 69 (ll23's step slot):** whether a row may name `program = "adopt"` in place
  of `step` is dDeclaredLoop's answer to ll8 F2's ask, or `check_program` as built; dl12 requires
  `step` until then (dl12:80-81, :122-123).
- **Row 46 (ll15 S1):** whether oc19's `build_index` admits the `code_purpose` table from a module with
  no `[[namespace]]` row is decided when oc19 builds.
- **Row 71 (ll37):** whether `gov_record.py new ruling` mints in a remote-less scratch repo waits on
  tr2's build and its open F6 (tr2:193-197, :335).

## Rule-wide hits the rules do not bind

Of the 30 candidates, 23 are not bound, each with its reason in section 4 of its group's return: ll24,
ll25, ll49, ll53, ll61, ll67, ll86, ll96 and ll102 (B1), and ll43, ll51, ll69, ll75, ll80, ll90, ll91,
ll92, ll94, ll97, ll98, ll99, ll100 and ll101 (B2). The usual reasons: the module imports its own
kit's library, the path is `tools/lib/` or a root tool (no `kit.toml`), the hit is a probe or an
evidence cite, or the "import" is a census ruling, not code.

## For the re-ground

Every spec below is revised by one writer of the re-ground brief, for the rows named. The other
mismatch-free specs stay as they are.

By spec: ll1: rows 1, 4 and 5; ll2: row 8; ll3: row 11; ll4: rows 13, 15 and 16; ll7: rows 20 and 21;
ll8: rows 22, 24, 25, 26 and 27; ll9: row 33; ll10: row 34; ll12: row 38; ll13: rows 39 and 40; ll14:
row 43; ll16: rows 47 and 49; ll17: row 52; ll19: row 56; ll22: rows 64, 65 and 66; ll23: rows 67 and
68; ll46: row 76; ll47: row 78; ll52: rows 80, 81 and 82; ll74: row 85.

- **Group A, record kinds and the factory** (writer led by spec 1): specs 1, 3, 8, 13 and 22.
- **Group B, legs** (writer led by spec 7): specs 7, 9, 10, 14, 23, 46, 47 and 52.
- **Group C, sibling kits** (writer led by spec 2): specs 2, 4, 12, 16, 17, 19 and 74.

## After the re-ground

The three writers' returns are
[`2026-10-28-build-TOOL-dLinkedLibrary-1-reground-returns`](2026-10-28-build-TOOL-dLinkedLibrary-1-reground-returns.md).
Each re-read both sides and found the parent line the record cites; one row was refused in part.
Every revised spec stays `DEFERRED`, each with one spec-revised deviation record. What they found
beyond the rows:

- **Row 26, refused in part.** ll8's `item.adopt.decisions` was not split into one actor per item:
  flow-steps names one actor, "reviewer, as two raters", and dl9 refuses only a list or two kinds,
  not one role dispatched twice. Its actor is now the single slot `role:gov-researcher`.
- **Spec 64 revised beside spec 74.** ll74 S26 now runs `fullmatch` on ll64 S14's inline copy of
  `SLUG_RE` and `GRANT_ID_RE`, which moves into a shared `tools/lib/id_value_re.py` block under a new
  parity row. ll64 has its own deviation record.
- **Edits beyond the listed rows, kept consistent:** ll52 S10 to S12 now point at the `ruling` row of
  the factory's per-kind table, which ll8 makes a typed kind; ll23's Files touched drops the
  `record-kinds.toml` values; ll46's Evidence re-cites ll14; ll9 and ll10's hands-off lines mirror
  ll52's "completes".
- **The `enforces` tags are the writers' judgement.** No unit's clause is in a v2 `[enforcement]`
  row, so each tag follows wb11's step 2 or wb51 S12: `practice.one-fact` for `annotations`,
  `practice.derive` for `record origin`, and `practice.verify` for the seven self-test legs. The
  closing review of each build pass should check them.
- **Two adopt-item route spellings.** ll8's terminal outcomes route through new F5, and ll23's to
  `transition`; both wait on ll8 F2's `program = "adopt"` ask, and dl12 names no terminal route for a
  program with no step.
- **Sibling consequences outside the population:** ll11:88-91 still has the drift builder import
  `derive_defined_ids`, which ll4 now serves as `annotations.py defined-ids --json`; if ll17 F4 (a) is
  picked, its `gen_map.py --dossiers` overlaps ll19's new `--feature-nodes`.
- **Parent text that looks wrong (not edited):** tr25 S1, the brief's full-call precedent, names no
  `readers` value and a `fence` form tr1 does not list; tr1 S9's `new` has flags for no column but
  tag, writer, check and field, and no dTotalRecall spec defines the verb that sets the rest; tr18's
  `gov-index` home overlaps ll3's `recall-index` home; oc28 S4 and S5's `edge_grammar.py` reads
  memory-tree's `tree_lib` in process; tr17 S1 reads runlog's readers in process from the workflows
  kit.

**Forks left open for the owner** (each names the ask the build run would file):

- ll8 F5: an adopt item's terminal outcome routes to `end`, filed with F2's ask to dDeclaredLoop
  (recommended). ll8 F2 itself stays open.
- ll16 F3: declared `requires_if` rows for `memory-tree` and `runlog` on `tools/workflows/kit.toml`
  (recommended), over subprocess verbs with asks to ll14, runlog's owner and dTotalRecall, or a mix.
- ll17 F4: mint `gotchas.py --front-matter` and `gen_map.py --dossiers` as subprocess verbs
  (recommended), over `requires_if` rows or copied parsers.
- ll22 F4: an ask to dGroundRules for a `policy.py get <key> --allowed` mode (recommended), since
  `get` prints a key's value, not the catalogue's allowed set.

Resolved by the writers, `RESOLVED (agent, 2026-10-28, delegated)`: ll4 F2 on rung 1 (`TAG_RE` in a
shared parity block, other kits reach `annotations.py` by subprocess), ll7 F5 (the hook spawns
`policy-mirror.js get` and carries `resolveBash` inline under a parity arm) and ll52 F4 (`derive_pin_hash`
inline, `gotchas.py --leg-names` and `runlog.py read-paths` as subprocess verbs). ll4 F3's ask was
reworded, not reopened.
