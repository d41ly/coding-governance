**Serves:** research TOOL-dLinkedLibrary-1

# dLinkedLibrary — the cross-check readers' returns, verbatim

The `gov-spec-reviewer` returns the cross-check record
[`2026-10-28-build-TOOL-dLinkedLibrary-1-parents-crosscheck`](2026-10-28-build-TOOL-dLinkedLibrary-1-parents-crosscheck.md)
is assembled from, each copied from its agent transcript; only the headings are the main loop's. Group A1, citation read specs 1, 2, 3, 4, 5, 7, 8, 9, 12, 13, 14 and 15; Group A2, citation read specs 16, 17, 19, 20, 21, 22, 37, 40, 46, 47 and 52; Group B1, rule-wide, legs and kinds read specs 6, 10, 23, 24, 25, 49, 53, 61, 64, 67, 86, 96 and 102; Group B2, rule-wide, sibling kits read specs 11, 18, 43, 51, 69, 74, 75, 80, 90, 91, 92, 94, 97, 98, 99, 100 and 101.

## Group A1, citation

I checked Group A1 (specs 1, 2, 3, 4, 5, 7, 8, 9, 12, 13, 14, 15) against the parents at `1a61f21a2`. It found 37 assumptions: 18 AGREES, 17 MISMATCH and 2 UNKNOWN UNTIL BUILT. Every MISMATCH is pre-existing. Each one already read the same way at `82a392696`, and neither re-ground (`794a0f5fb`, `ac8ab8d5f`) moved a parent line that a group spec relies on. Every probe was a read: `git show <rev>:<spec>`, the re-ground diffs, grep, and one `python -c` read of the leg names in `tools/gate-legs.json`.

**1. Assumptions**

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| ll1 | tr1 S9's `record_kinds.py new decision --tag … --writer hand --check …` appends a conforming row with home `memory/DECISIONS.md` | cite | MISMATCH | ll1:121-125; tr1:101-103, tr1:65-67; tr18:45-47; tr16:36; tr25:33-37 |
| ll1 | `writer = "hand"` stays legal for a `rows`-form kind after tr2 | cite | AGREES | ll1:123-124; tr2:77-81; tr1:194-196 |
| ll1 | `record_kinds.py --check` is tr1's gate and passes with the row (AC9) | cite | AGREES | ll1:353-356; tr1:75-83 |
| ll1 | the reuse-proposal record is written by `reuse_entries.py` itself as `**Serves:** journal` | R2 | MISMATCH | ll1:74-76; tr18:76-82, tr18:95-97; tr2:45-50, tr2:77-79 |
| ll1 | memory-tree code reads `reuse.propose` and `decisions.major` through the policy kit's `resolve` (`policy.py:752`) | R3 | MISMATCH | ll1:84, ll1:105; oc7:202-206; TOOL-dGroundRules-1:113 |
| ll1 | `decision` is a registry row, not a typed `-<kind>-<n>.md` record, so it owes no `TYPED_RECORD_KINDS` join | R2 | AGREES | ll1:121-125; oc42:45-49 |
| ll2 | `gov_code.py callers` reads the core `code` record (tr8 S7) | cite | AGREES | ll2:37-38; tr8:69-73 |
| ll2 | `house_index.py` (codebase-map) reads `reuse.delivery` through `read_policy_value` (PLAY-dOrderedCharter-7 §4) | R3 | MISMATCH | ll2:39, ll2:90-91, ll2:132; oc7:197-212 |
| ll2 | `render_handoff` (roles) runs `house_index.py --slot` as a subprocess found by `resolve_kit_dir` | R3 | AGREES | ll2:83-88; oc7:202-206 |
| ll3 | `record find` (tr9 S3) exists, with `query.py` as its thin adapter | cite | AGREES | ll3:38, ll3:127-129; tr9:89-96 |
| ll3 | the `recall-index` row lands through `record_kinds.py new recall-index` with writer `tag_index.build_index` | cite | MISMATCH | ll3:126-130; tr1:186-196; tr1:101-103; tr18:45-47; tr16:36 |
| ll4 | the memory-tree `extract_code` copy (tr8 S2) and the policy adapter (tr8 S10) exist | cite | AGREES | ll4:40-43; tr8:48-51, tr8:81-89 |
| ll4 | `annotation-index` lands through `record_kinds.py new … --writer generator:… --check "codebase-map coverage + freshness"` | cite | MISMATCH | ll4:84-87; tr1:101-103; tr18:45-47; tr16:36; leg name probed: present |
| ll4 | tr9 §3 gives the annotations system to dLinkedLibrary (F3) | cite | AGREES | ll4:405-407; tr9:143-144 |
| ll4 | memory-tree `annotations.py` reads `TAG_RE` from the playbook kit's `tag_index.py` via `resolve_kit_dir` | R3 | MISMATCH | ll4:60-61; oc19:47-49; oc7:202-204; `tools/memory-tree/kit.toml:7-8` (no `playbook` row) |
| ll4 | playbook `edge_grammar.py` calls memory-tree's `parse_note_line`; drift-audit imports `annotations.py`; `gen_map.py` imports it | R3 | MISMATCH | ll4:100-102, ll4:124-126, ll4:204-208; oc7:202-204; TOOL-dGroundRules-1:113 |
| ll5 | the build README carries tr4 S5's routing region, which the `<build>` cell links to | cite | AGREES | ll5:47-49, ll5:85; tr4:56-57 |
| ll7 | the memory-tree policy adapter (tr8 S10) is a precondition | cite | AGREES | ll7:44; tr8:81-89 |
| ll7 | three legs (`annotations`, `annotations selftest`, `annotations-read self-test`) are hand-written rows in `tools/gate-legs.json`, with no `enforces` | R1 | MISMATCH | ll7:47-63, ll7:93-97, ll7:193; wb11:36-47, wb11:57-58; oc7:58-63; tr9:97-103 |
| ll7 | `annotations-read.js` (hooks) `require`s `../policy/policy-mirror.js` for `readPolicy` and a new `resolveBash` | R3 | MISMATCH | ll7:74-77, ll7:90-92; oc7:202-204; dKeptSession record :106, :330-332 |
| ll8 | the factory and the tr18 columns are preconditions; the `census`/`ruling`/`baseline` rows name form, writer, check and fields only | cite | MISMATCH | ll8:46-48, ll8:58-65; tr18:45-47; tr16:36; tr25:33-37 |
| ll8 | the door `gov_record.py new <kind>` sits over `write_new_record` in `build_records.py` and takes `--field` | cite | AGREES | ll8:48-50; tr2:39-44 |
| ll8 | door-written kinds join the Serves kinds through tr18 S7, so `tree_lib.py:406` is left alone | cite | MISMATCH | ll8:422-425; tr18:76-80; oc42:35-40 |
| ll8 | `census` and `ruling` records named `-<kind>-<n>.md` and served as their own kind need no `TYPED_RECORD_KINDS` or factory-table join | R2 | MISMATCH | ll8:189-190, ll8:60; tr2:51-55; oc42:25, oc42:35-49, oc42:57 |
| ll8 | the item rows: `returns` with no `@<n>`; command actors with no `inputs`; routes to `done`; two actors on one item | R4 | MISMATCH | ll8:236-240; dl24:144-145; dl12:39-44, dl12:125-128; tr18:52-56 |
| ll8 | `adopt_program.py` (memory-tree) reads the three `retrofit.*` keys through `resolve` | R3 | MISMATCH | ll8:127-128, ll8:48-50; oc7:202-206 |
| ll8 | `core.py adopt` dispatches to memory-tree by subprocess | R3 | AGREES | ll8:71-75; oc7:202-206 |
| ll8 | `program = "adopt"` in place of `step` is admitted (F2's ask to dDeclaredLoop) | R4 | UNKNOWN UNTIL BUILT | ll8:296-305; dl12:34-35, dl12:122-123 |
| ll9 | `read_header_edges` reads column-0 lines for an untyped record and fields for a typed one (tr19 S1) | cite | AGREES | ll9:39-44; tr19:52-56 |
| ll9 | the door and `write_new_record` (tr2 S1 to S5) | cite | AGREES | ll9:34; tr2:39-66 |
| ll9 | `record find` rows are `key · kind · build · bytes · path:line`, and `record show` slices (tr9 S3, S5) | cite | AGREES | ll9:64-68; tr9:94-96, tr9:104-107 |
| ll9 | two legs (`record origin …`, `record origin selftest`) are written into `tools/gate-legs.json`, with no `enforces` | R1 | MISMATCH | ll9:59-63, ll9:188; wb11:36-47, wb11:57-58; oc7:58-63 |
| ll12 | tr9 S1's `extract_marker` and the `marker` namespace row | cite | AGREES | ll12:27-28, ll12:33-35; tr9:81-82 |
| ll12 | memory-tree `annotations.py` reads the namespace row through the playbook kit's `read_namespaces` | R3 | MISMATCH | ll12:33-35, ll12:82; oc19:51-54, oc19:258; oc7:202-204 |
| ll13 | `research-return` lands through `record_kinds.py new … --writer hand --check …`, form `header`, home `memory/builds/*/*/*.md` | cite | MISMATCH | ll13:38-42; tr1:101-103; tr18:45-47; tr16:36 |
| ll13 | tr2's record door is a future writer of the `kind: research-return` line | cite | MISMATCH | ll13:95-97; tr2:51-55, tr2:77-79 |
| ll13 | `instrument` is a registered kind (tr18) and `design-record` one (tr1) | cite | AGREES | ll13:134-137; tr18:59-62; tr1:208-212 |
| ll14 | tr8's `derive_code_record` and its four tables, with edge types `calls`/`tests`/`mention`/`invokes`/`registers` | cite | AGREES | ll14:32-35; tr8:69-73, tr8:144, tr8:194, tr8:275-276 |
| ll14 | the `code record` leg runs `gov_code.py --selftest` beside `code_record.py --selftest` | cite | MISMATCH | ll14:249; tr8:100-106 |
| ll14 | `grep_words` is carried inline under a parity row, as in tr8 S5 | cite | AGREES | ll14:278-281; tr8:60-65 |
| ll15 | tr8 S2 and S7's key and `code_row.hash`, and the S10 adapter | cite | AGREES | ll15:35-39; tr8:69-73, tr8:81-89 |
| ll15 | the `code_purpose(blob, …)` table is written "through PLAY-dOrderedCharter-19 S4's `build_index`" | cite | UNKNOWN UNTIL BUILT | ll15:49-51; tr8:69-73; oc19:64-65 |

**2. MISMATCHES**

- **ll1:121-125, ll3:126-130, ll4:84-87, ll13:38-42, ll8:58-65 — the `new` call omits the columns the factory refuses without.**
  - Our side: ll1 reads "through TOOL-dTotalRecall-1 S9's `python record_kinds.py new decision --tag record.decision --writer hand --check "memory hygiene"`, schema form `rows`, home `memory/DECISIONS.md`". The other four use the same short form.
  - Parent side: tr16:36 says "`record_kinds.py new` refuses a row with no `--purpose`". tr18:45-46 says "Every row … carries non-empty `home`, `lifecycle`, `readers` and `layer`; `check_record_kinds` … reds a row missing one". tr1:65-67 says those columns are "required from TOOL-dTotalRecall-18". tr25:33-35 shows the expected form: "written through `record_kinds.py new` … with every column TOOL-dTotalRecall-18 and TOOL-dTotalRecall-16 require".
  - Change: each spec spells the full call, with `--purpose`, `layer`, `home`, `lifecycle` and `readers`, as tr25 S1 does. For ll8 that means `census`, `ruling` and `baseline`.
  - Cause: pre-existing.
- **ll3:128 — the writer is a function, which the column does not admit.**
  - Our side: "writer `tag_index.build_index`".
  - Parent side: tr1:186-187 says "`writer` is a door, spelled as the command that writes the kind …, `generator:<path>` for a generated kind, or `hand`".
  - Change: name a command or a `generator:<path>`, for example `generator:` plus the index writer's path.
  - Cause: pre-existing.
- **ll1:74-76 — `reuse_entries.py` writes its own journal record.**
  - Our side: "writes the proposal record … (`**Serves:** journal <unit id>`)".
  - Parent side: tr18:95 says "Every writer of the value writes `log`", and tr18:79 says `journal` is a read-only alias. tr2:47 says "each kind has one door and the registry names it", and tr2:77-79 makes the `journal` row's writer `gov_record.py new <kind>`.
  - Change: write the proposal through `gov_record.py new log`, or have the module write `**Serves:** log`.
  - Cause: pre-existing.
- **ll1:84 and :105, ll8:127-128 — policy keys read through an in-process `resolve`.**
  - Our side: ll1 reads "`reuse.propose`, read through `resolve` (`tools/policy/policy.py:752`)"; ll8 says the keys are "each read once per verb through `resolve`".
  - Parent side: oc7:202-206 says "A kit may not import a sibling kit … finds `policy.py` with it, and runs `<sys.executable> <kit>/policy.py get <key> --explain`".
  - Change: read each key through the memory-tree adapter `policy_value.py` (tr8 S10), which runs `policy.py get` as a subprocess.
  - Cause: pre-existing.
- **ll2:39 and :90-91 — the codebase-map kit calls the playbook kit's policy helper.**
  - Our side: "read once per slot through `read_policy_value("reuse.delivery", root)`", citing "`read_policy_value` (PLAY-dOrderedCharter-7 §4)".
  - Parent side: oc7:197-198 says "`read_policy_value` … in `tools/playbook/policy_value.py` is the playbook kit's one caller", and oc7:211-212 says "neither kit can import the other's".
  - Change: `house_index.py` carries its own adapter to the oc7 §4 contract, or runs `policy.py get` as a subprocess.
  - Cause: pre-existing.
- **ll4:60-61, :100-102, :124-126, :204-208 — four in-process imports across kits.**
  - Our side: "A tag fits `TAG_RE`, read through `resolve_kit_dir("playbook", "tag_index.py", here)`". Also "the drift builder imports it", and "`edge_grammar.py` … calling `parse_note_line` through `resolve_kit_dir("memory-tree", …)`". The spec justifies the imports with "drift-audit already requires memory-tree … so it may import" and "so `gen_map.py` may import `annotations.py`".
  - Parent side: oc7:202-203 says "A kit may not import a sibling kit". TOOL-dGroundRules-1:113 says "a kit carries shared code inline". `tools/memory-tree/kit.toml:7-8` has `requires = []` and no `requires_if` row for `playbook`.
  - Change: carry `TAG_RE` inline under a parity row, or validate tags through a `tag_index.py` subprocess. Declare a `requires_if` row for each remaining edge (drift-audit to memory-tree, codebase-map to memory-tree, playbook to memory-tree), or reach `parse_note_line` and `derive_defined_ids` through a memory-tree CLI verb.
  - Cause: pre-existing.
- **ll7:47-63 and :193 — legs written by hand, with no `enforces`.**
  - Our side: "One row in `tools/gate-legs.json`, shaped like the `recall floor` row". Files touched: "`tools/gate-legs.json`: the three legs of S1 and S5". None of the three legs names `enforces`.
  - Parent side: wb11:36-37 says "Each leg is declared exactly once: a `[[gate_leg]]` row in its kit's descriptor". wb11:44-45 says "`--check` exits 1 when the file differs". wb11:57-58 says "Each declaration's `enforces` names the `principle.*` and `practice.*` tags". oc7:60-61 says "a leg carrying no `enforces` is red". tr9:99-102 shows the `recall floor` row ll7 copies is itself declared as an `[[exempt_leg]]`.
  - Change: declare all three through `leg_factory.py new`, the first two in `tools/memory-tree/kit.toml` and the read-hook leg in `tools/hooks/kit.toml`, each with `enforces`, and render `gate-legs.json` by `--write`. ll52 S32 moves the declarations later but adds no `enforces`.
  - Cause: pre-existing.
- **ll7:74-77 and :90-92 — the hook loads the policy kit in process.**
  - Our side: "reads `annotations.grammar` through `readPolicy` (`require` of `../policy/policy-mirror.js`, as `tools/hooks/agent-cap.js:465` does)", and "`resolveBash`, added to `tools/policy/policy-mirror.js`'s exports".
  - Parent side: oc7:202-203 says "A kit may not import a sibling kit". The dKeptSession record :106 classes ks8's "`scratch-guard.js` requires the policy kit's `policy-mirror.js` in process" as an R3 MISMATCH, and :330-332 says agent-cap's own `:465-469` breaks the same rule and that "ks8 now spawns `policy-mirror.js get` instead".
  - Change: spawn `policy-mirror.js get annotations.grammar` as ks8 does. Find bash without importing a policy-kit export, for example with an inline copy under a parity row.
  - Cause: pre-existing.
- **ll8:422-425 — the spec expects tr18 S7 to admit its kinds.**
  - Our side: "its proposal to edit `tree_lib.py:406` is not needed, since door-written kinds join the Serves kinds through TOOL-dTotalRecall-18 S7".
  - Parent side: tr18:76-80 says `RECORD_KIND_TOKENS` "becomes `("spec-audit", "diff-review", "log", "research") + TYPED_RECORD_KINDS` … since TOOL-dTotalRecall-11 adds `shape-run` through `TYPED_RECORD_KINDS`". Nothing joins a registry row on its own.
  - Change: drop the claim and add `census` and `ruling` to `TYPED_RECORD_KINDS`, as in the next bullet.
  - Cause: pre-existing.
- **ll8:189-190 and :60 — typed-shaped records with no typed join.**
  - Our side: "Records are named `<date>-build-<unit id>-<kind>-<n>.md` …, the factory's grammar", writer `gov_record.py new <kind>`.
  - Parent side: tr2:52 renders "the `**Serves:** <kind> <ids>` line". oc42:25 says "`read_bindings` marks any other first token malformed". oc42:40-42 makes the factory's kind list and field table `TYPED_RECORD_KINDS`. oc42:57 keeps the closed list in HYGIENE.
  - Change: Files touched gains `tools/memory-tree/tree_lib.py`, adding both kinds to `TYPED_RECORD_KINDS`, plus their rows in `build_records.py`'s per-kind field table. S12's HYGIENE text names them in the closed kind list.
  - Cause: pre-existing.
- **ll8:236-240 — the item rows break the loop program's schema.**
  - Our side: `returns` `record-kind.census` with no version; `command:` actors with no `inputs`; "`ruled` to done"; "`role:reviewer`, two raters".
  - Parent side: dl24:144-145 says "`returns` is written `record-kind.<name>@<n>`". dl12:127 says "`inputs` | yes for a non-role actor". dl12:41-42 says "every route names a declared item of the program, `transition` …, or `stand-in`". dl12:125 says "Actor, one per item". tr18:52-56 now joins `written by` only on `record-kind.<name>@<n>`.
  - Change: version every `returns`, add layer-tagged `inputs` to the command items, route the terminal outcomes to an exit item or `transition`, and split `item.adopt.decisions` into one actor per item.
  - Cause: pre-existing for dl12 and dl24. tr18's re-ground moved its own join onto the `@<n>` form.
- **ll9:59-63 and :188 — legs written by hand, with no `enforces`.**
  - Our side: "The leg `record origin (stored origin against history)` in `tools/gate-legs.json` … and the leg `record origin selftest`".
  - Parent side: the same lines as the ll7 leg bullet: wb11:36-37, wb11:57-58 and oc7:60-61.
  - Change: declare both legs in `tools/memory-tree/kit.toml` through `leg_factory.py new` with `enforces`. ll52 S32 and S33 declare them later, still without `enforces`.
  - Cause: pre-existing.
- **ll12:33-35 — the namespace row is read through a playbook-kit function.**
  - Our side: "`tools/playbook/namespaces.toml`, read through PLAY-dOrderedCharter-19 S2's `read_namespaces`".
  - Parent side: oc19:51-53 puts the registry and `read_namespaces` in `tools/playbook/` (`tag_index.py`, oc19:258). oc7:202-203 says "A kit may not import a sibling kit".
  - Change: call memory-tree's own `record_extract.extract_marker` directly, or read the row with `tomllib` from the path `resolve_kit_dir` finds.
  - Cause: pre-existing.
- **ll13:95-97 — the door cannot write the kind line.**
  - Our side: "The writers of new returns: the flow's `plan.research` and `design.research` items, and TOOL-dTotalRecall-2's record door. Until they write the line…".
  - Parent side: tr2:51-54 renders "the `**Serves:** <kind> <ids>` line and one `- **<Key>:** ` line per field". A bare `kind: <name>` line is not in that template.
  - Change: drop the door as a writer of the line, or ask dTotalRecall to have the door render a declared `kind:` line.
  - Cause: pre-existing.
- **ll14:249 — the arm names a leg that runs something else.**
  - Our side: "`gov_code.py --selftest` run by the `code record` leg beside `code_record.py --selftest`".
  - Parent side: tr8:100 says "The leg `code record`, argv `python {prefix}/memory-tree/code_record.py --check`".
  - Change: name ll46's `code record selftest` leg in the arm line.
  - Cause: pre-existing.

**3. UNKNOWN UNTIL BUILT**

- ll8 F2, `program = "adopt"`: decided by whether dDeclaredLoop accepts ll8's ask, so that `check_program` holds an adopt item to every rule except step-exit. dl12 requires `step` until then.
- ll15 S1, the `code_purpose` table: oc19 S4 says the index is "written by the extractors alone through `build_index`". Whether `build_index` admits a table from a module with no `[[namespace]]` row is decided when oc19's `build_index` is built.

**4. Rule probes the rule does not bind**

- ll5 S2: `library_views.py` imports `id_grammar` from its own kit.
- ll8 S3: `core.py` reaches `adopt_program.py` as a subprocess.
- ll2 S8 and ll3 S4: `handoff.py` and `unattended.sh` reach other kits by subprocess.
- ll2 S4: the `record_origin.py --of` call is a subprocess (ll9 S6).
- ll14 S7: `grep_words` is an inline canonical copy, not an import.
- ll15 S1: `derive_purpose`'s normaliser is imported within memory-tree.
- ll1 S8 and ll8 S6 (`-decision-routing.md`), ll2 S6 (`-reuse-scout`): none is a member of `TYPED_RECORD_KINDS`, so serving `research` is legal.
- ll13: `research-return` keeps `**Serves:** research`, so it owes no typed join.
- ll1 S6: `re-dispatch` is in dl30's closed cause set.
- ll3 S1: no leg's guard or argv in `tools/gate-legs.json` names a file it deletes (grep probe).

**5. Revised parent units cited but not depended on**

- ll1: none. ll2: none. ll3: none. ll4: none. ll5: none. ll7: none.
- ll8: none. ll9: none. ll12: none. ll13: none. ll14: none. ll15: none.

Relevant paths:
- C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dLinkedLibrary\spec\ (the 12 group specs)
- C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dTotalRecall\spec\ (tr1, tr2, tr4, tr8, tr9, tr16, tr18, tr19, tr25)
- C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dKeptSession\build\2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck.md

## Group A2, citation

The 11 specs of Group A2 (16, 17, 19, 20, 21, 22, 37, 40, 46, 47, 52) hold 31 assumptions: 18 AGREES, 12 MISMATCH and 1 UNKNOWN UNTIL BUILT. Every mismatch was already there at `82a392696`; none comes from the third-wave re-grounds. Eight break R1 or R3, and four are citation mismatches against tr1, tr2 and tr8.

1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 16 | The record at a past tree comes from `code_record.py --tree <rev>` | cite | MISMATCH | ll16:42; tr8:44, :188 |
| 16 | tr8 §3 gives the `code` slot to dBoundRoles, and no dBoundRoles spec carries it | cite | AGREES | ll16:233; tr8:136; `git grep "code slot\|memory.code-budget\|code-roles" 1a61f21a2 -- memory/builds/dBoundRoles/spec/` printed nothing |
| 16 | `replay_scorer.py` (workflows kit) calls memory-tree's `derive_callers`/`derive_callees`/`derive_tests` and runlog's readers in process | R3 | MISMATCH | ll16:40, :61, :100; `tools/workflows/kit.toml:10` |
| 17 | tr8 S2 `extract_ranges` adds `end_line` on tr13's block, and S7 stores `code_row(blob, kind, key, name, line, end_line, hash, text)` keyed `<path>::<qualified name>` | cite | AGREES | ll17:41-43, :112-114; tr8:48-50, :69, :126, :152 |
| 17 | tr9 S1 registers the `class` namespace, tag `class.<name>` | cite | AGREES | ll17:43; tr9:79-80 |
| 17 | `tools/playbook/edge_grammar.py` adapters call memory-tree's `gotchas.parse_front_matter`, `derive_decision_rows` and `scan_annotations`, and codebase-map's `parse_dossier`, in process | R3 | MISMATCH | ll17:44, :56, :64, :138, :196 |
| 19 | tr8 S12 admits `symbols` and re-keys staleness to body hashes | cite | AGREES | ll19:38, :98; tr8:94-98 |
| 19 | tr9 S1's `extract_feature` lands anchor rows only, and its row names no source this unit owns | cite | AGREES | ll19:40-45; tr9:77-78 |
| 19 | memory-tree's `record_extract.py` reads codebase-map's `read_feature_nodes` in process, "an optional sibling through the inlined `resolve_kit_dir`" | R3 | MISMATCH | ll19:40-45, :182; `tools/memory-tree/kit.toml:8` (no codebase-map row) |
| 20 | tr9 S1 registers the `feature` row and names no `role` | cite | AGREES | ll20:107, :171; tr9:77-78 |
| 20 | br14 S5 `check_role_bindings` binds a role's `rules:` to the units naming it | cite | AGREES | ll20:83-85; br14:59-62 |
| 20 | br14 registers `role` as a `selects` row | cite | AGREES | ll20:109-110; br14:116, :131 |
| 20 | br14 S8 extends `gov_tag.py --fixture` | cite | AGREES | ll20:263; br14:70-71 |
| 21 | tr8 S2, S7, S9 and S10 (key form, tables, `degraded`, `memory.code-languages`, exit 2 on a missing ctags) and AC8's stub | cite | AGREES | ll21:31-35, :42, :115; tr8:69-89, :290-294 |
| 21 | tr8 §4's body-hash rule for built-in rows | cite | AGREES | ll21:55; tr8:146-149 |
| 22 | tr1 S9 `record_kinds.py new <name> --tag --writer --check --field` exists | cite | AGREES | ll22:34-35, :54-56; tr1:101-105 |
| 22 | That `new` call with no `home`/`layer`/`lifecycle`/`readers` writes a conforming `gotcha` row | cite | MISMATCH | ll22:54-56; tr1:66; tr18:45-49 |
| 22 | A front-matter kind registered through `--field` is graded as tr1 grades it | cite | MISMATCH | ll22:37-39, :54-56; tr1:83-85, :174-176 |
| 22 | `gotchas.py` reads the `platforms.supported` allowed set through `policy.resolve` in process | R3 | MISMATCH | ll22:35, :41, :292; oc7:202-205, :379-380 |
| 37 | tr2's door `gov_record.py new <kind>` writes the ruling plant's record | cite | AGREES | ll37:52-54, :78; tr2:30, :39-44 |
| 37 | The door mints in a remote-less scratch repo with no lease or claim | cite | UNKNOWN UNTIL BUILT | ll37:144-145; tr2:188-196, :335 |
| 40 | tr9 S1's `marker` row holds no member list | cite | AGREES | ll40:33, :43-45; tr9:81-82 |
| 46 | tr8 S13's `code record` leg runs `code_record.py --check`, not `--selftest` | cite | AGREES | ll46:25, :57, :73-74; tr8:100 |
| 46 | `code_record.py --selftest` exists with its own plants | cite | AGREES | ll46:35-37; tr8:310 |
| 46 | A memory-tree leg is declared in `tools/memory-tree/kit.toml` through the factory | cite | AGREES | ll46:40-44; tr8:100-103 (rev-3 moved `code record` there too) |
| 46 | The new leg's `enforces` is named | R1 | MISMATCH | ll46:43-44, AC3 :120-123; oc7:58-63; tr8:104-106, AC10 :299-304 |
| 47 | tr1 S3's `record-kinds` leg is `record_kinds.py --check` | cite | AGREES | ll47:24, :50, :67; tr1:73-77 |
| 47 | The new leg's `enforces` is named | R1 | MISMATCH | ll47:36-37, AC1 :101-104; oc7:58-63 |
| 52 | The `ruling` row lands in tr1's registry | cite | AGREES | ll52:73; tr1:58-66 |
| 52 | A door field check that lands with tr1 reads the `ruling` row's values | cite | MISMATCH | ll52:71-74, :75-77; tr1:83-85, :174-176; tr2:56-60 |
| 52 | S32 legs re-declared through `leg_factory.py new` carry `enforces` | R1 | MISMATCH | ll52:141-143, AC16 :363-366; oc7:58-63 |
| 52 | S17, S42 and S51 reach sibling kits' modules in process | R3 | MISMATCH | ll52:91-92, :170-172, :195-198 |

2. MISMATCH

- **ll16, the `--tree` flag.** ll16:42 says "derived at a past tree by `code_record.py --tree <rev>`". tr8 defines `--tree` only as a modifier: tr8:44 "`python code_record.py --time --tree <rev>`" and tr8:188 "`python code_record.py --dump --tree <rev>`, the record's rows rendered". `Change:` name `code_record.py --dump --tree <rev>`, or state how `render_code_slot` gets the record. `Cause:` pre-existing.
- **ll16, sibling kits (R3).** ll16:61 says "through TOOL-dLinkedLibrary-14's `derive_callers`, `derive_callees` and `derive_tests`", and ll16:40 says "over runlog's `resolve_session_tree`, `read_records` and `extract_segments`". The code is in `tools/workflows/replay_scorer.py`, and `tools/workflows/kit.toml:10` reads `requires = ["agent-cap", "policy"]`. R3 (TOOL-dGroundRules-1 §4; oc7:202-205): code reaches another kit's verb by subprocess. `Change:` reach `gov_code.py callers`/`tests` by subprocess (ll14 has no `callees` verb, so ask ll14 for one), and runlog through a runlog verb; or declare `requires_if` rows on `tools/workflows/kit.toml`. tr17, which ll16 shares its transcript readers with, uses the same runlog read, so the fix may need an ask to dTotalRecall. `Cause:` pre-existing.
- **ll17, sibling kits (R3).** ll17:56 says "parsed by `gotchas.parse_front_matter` (`tools/memory-tree/gotchas.py:233`)". ll17:64 says "each row `derive_decision_rows(root, conf)` (`tools/memory-tree/row_grammar.py`…)". ll17:138 says "`parse_dossier` (`tools/codebase-map/map_lib.py:1022`)". The code lives in `tools/playbook/edge_grammar.py` (ll17:196). `Change:` reach each reader through a memory-tree or codebase-map verb printing JSON rows, run as a subprocess the way br14 rev-4 F5 did for the roles grammar; or declare `requires_if` rows on `tools/playbook/kit.toml`. One caveat: oc28 S5's own header site reads `tree_lib.read_bindings` in process (oc28:63), so the same rule binds the parent. `Cause:` pre-existing.
- **ll19, sibling kits (R3).** ll19:41-43 says "where the codebase-map kit resolves as an optional sibling through the inlined `resolve_kit_dir`, one row per `FeatureNode`". The code is in `tools/memory-tree/record_extract.py` (ll19:182). `tools/memory-tree/kit.toml:8`'s `requires_if` holds no codebase-map row. `Change:` add a `requires_if` row for codebase-map, or have `map_lib`'s `read_feature_nodes` printed by a codebase-map verb run as a subprocess. `Cause:` pre-existing.
- **ll22, the registry columns.** ll22:54-55 runs "`python tools/memory-tree/record_kinds.py new gotcha --tag record.gotcha --writer hand --check "gotchas selftest" --field cause …`". tr1:66 says "`layer`, `home`, `readers` and `lifecycle` are admitted and required from TOOL-dTotalRecall-18". tr18:45-47 says "Every row … carries non-empty `home`, `lifecycle`, `readers` and `layer`; `check_record_kinds` … reds a row missing one". All of dTotalRecall lands before this run, so the row reds. `Change:` S4 names `home = "memory/gotchas/*.md"`, `layer.memory`, a `lifecycle` value and `readers`, and AC5 checks them. tr1 S9's `new` has no such flags, so set them per tr18's landed verb, or file an ask. `Cause:` pre-existing.
- **ll22, the form.** ll22:37-38 puts the fields in "front-matter keys `cause:`, `language:`, `platform:` and `from:`", and S4 registers them as `--field`s. tr1:174-176 says "`fields` (records carrying `**Key:**` lines, graded by S4), `header` (a status or front-matter grammar its owner grades) … Only `fields` is graded by S4". tr1:83-85 grades every record under `home` for `**Key:**` lines. A fields-form row would red all 148 classes. `Change:` register `gotcha` with `form = "header"`, graded by `gotchas selftest`, and say how `new` sets the form. `Cause:` pre-existing.
- **ll22, the policy read (R3).** ll22:41 says "the allowed set on the `platforms.supported` row `resolve` returns", and ll22:292 says "`policy.resolve` (`tools/policy/policy.py:752`)". R3 requires that "a policy key is read by `policy.py get` as a subprocess (oc7:379-380)". `Change:` read the set through a policy-kit verb run as a subprocess, or through tr8's adapter `tools/memory-tree/policy_value.py`. `gotchas.py:504-508` already imports the policy kit's `budgets` this way today; that is precedent, not cover. `Cause:` pre-existing.
- **ll46, the leg's `enforces` (R1).** ll46:43-44 asks for "the `ceiling`, `tag`, `purpose` and `enforces` the factory's gate requires" and names no value, and AC3 does not observe it. oc7:58-63 says "a leg carrying no `enforces` is red … excused only by a row of the shrink-only pending list". tr8:104 does it as "`enforces = ["principle.p32"]` among them", with AC10. ll46 carries no clause (ll46:5 `**Derived:**`), so step 1 of wb11's rule (wb11:190-192) cannot reach it. `Change:` name the tag in S2 (a `practice.*` by wb11:193-194, or `principle.p32` with a stated reason) and add an AC that reads `enforces` from `tools/gate-legs.json`, as tr8 AC10 does. `Cause:` pre-existing.
- **ll47, the leg's `enforces` (R1).** It is the same as ll46, at ll47:36-37 and AC1 ll47:101-104. `Change:` name the tag and observe it in AC1. `Cause:` pre-existing.
- **ll52, the `ruling` value check.** ll52:73-74 says "the door's field check that reads the row lands with TOOL-dTotalRecall-1", and ll52:76 says "`gov_record.py new ruling`'s field check". tr1's data model has no value-set column (tr1:174-176 is form only), and tr1:83-85 checks only that each field is present, in order. tr2:60 says "The door adds no validator of its own." `Change:` S10 to S12 name the reader that actually closes the `Ruling` set (`adopt_instructions.py`, or a `values` column asked of dTotalRecall), and drop the claim that a tr1 or tr2 check reads the row's values. `Cause:` pre-existing.
- **ll52, S32's `enforces` (R1).** ll52:141-143 says "The legs units 7, 9, 10 and 23 wrote … are declared through `leg_factory.py new` …; `leg_factory.py --check` exits 0", with no `enforces` named, and AC16 does not observe it. oc7:58-63 applies. `Change:` name each leg's `enforces` and have AC16 read it. `Cause:` pre-existing.
- **ll52, sibling kits (R3).** Three items reach another kit's module in process, and `requires_if` admits none of them:
  - **S17** (ll52:91-92): playbook's `tools/playbook/adopt_instructions.py` calls "`derive_pin_hash(text)` (`tools/memory-tree/design_lib.py` …), read through `resolve_kit_dir`".
  - **S42** (ll52:170-171): codebase-map's `house_index.py` reads the legs "through `gotchas.load_leg_names`, loaded by `resolve_kit_dir("memory-tree", "gotchas.py", here)`".
  - **S51** (ll52:195-198): memory-tree's `annotations.py lookup --command` calls runlog's `derive_read_paths`, printing "`shell reads — runlog not installed`".

  `Change:` use subprocess verbs, or add `requires_if` rows on the playbook, codebase-map and memory-tree descriptors. `Cause:` pre-existing.

3. UNKNOWN UNTIL BUILT

- ll37 `adopt-ruling`: whether `gov_record.py new ruling` mints in a scratch repo with no remote is decided by tr2's build. Its lease read now fetches `refs/gov/leases/*` from the remote (tr2:193-194), and that read waits on F6, which is open for the owner (tr2:335). The `leases.offline` value (tr2:197) also bears on it.

4. Checked and not bound

- ll16 S3: `extract_files_touched` is loaded from `tools/check-spec-tokens.py`, which is not in a kit directory, so R3 does not apply.
- ll19 S3: `dossier_move.py` reaches `reuse_entries.py propose` as a CLI, which is a subprocess, so R3 is met.
- ll20: it writes no code, only one field of `namespaces.toml`. The row's `record_extract` extractor is tr9's design.
- ll21: `code_ctags.py` runs an external binary and reads policy through tr8's same-kit adapter.
- ll37: `record_origin.py`'s plants call `gov_record.py` and `adopt_program.py` in its own kit.
- ll40: the `reader` cell of `marker-words.toml` is a path pointer, not an import.
- ll46, ll47: `code_record.py --selftest` runs its sibling modules as subprocesses from its own kit.
- ll52 S46: the `grep_words` copy is inline under its parity row, not an import.
- ll22 S5: it reads `Decided:` trailers on history through `read_commits`, never at pre-commit, so R7 is not engaged.
- ll16 S7 and ll19 S3: the records `-code-replay-verdict.md`, `-code-replay-manifest.json` and `-dossier-<feature>.md` are not `-<kind>-<n>.md` forms, so R2 is not engaged (oc42:45-49).

5. Revised units cited but not depended on

- ll16 (tr8): none.
- ll17 (tr8, tr9): none.
- ll19 (tr8, tr9): none.
- ll20 (br14, tr9): none. ll20 relies only on br14 S5 and S8, not the S2/S3 extractors the re-ground moved.
- ll21 (tr8): none. Its re-ground change, the S13 leg move, is not relied on.
- ll22 (tr1): none.
- ll37 (tr2): none.
- ll40 (tr9): none.
- ll46 (tr8): none.
- ll47 (tr1): none. The move of `record-kinds` to an `[[exempt_leg]]` row is not relied on.
- ll52 (tr1): none.

Files:
- `C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dLinkedLibrary\spec\2026-10-26-spec-TOOL-dLinkedLibrary-{16,17,19,20,21,22,37,40,46,47,52}.md`
- `C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-{1,2,8,9,18}.md`
- `C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dBoundRoles\spec\2026-10-25-spec-TOOL-dBoundRoles-14.md`
- `C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dOrderedCharter\spec\2026-10-23-spec-PLAY-dOrderedCharter-7.md`
- `C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dOrderedCharter\spec\2026-10-23-spec-PLAY-dOrderedCharter-28.md`
- `C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\tools\memory-tree\kit.toml`
- `C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\tools\workflows\kit.toml`

## Group B1, rule-wide, legs and kinds

1.

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 6 | The research view reads every build's records bound `**Serves:** research` and selected by ll13's `kind: research-return` line. It mints no Serves token, no typed kind and no `new <kind>` door, and `research` is still an untyped kind the parents serve. | R2 | AGREES | ll6:54-59, ll6:203-207; ll13:37-41, ll13:204 (no new Serves token); tr1:67-71, tr1:208 (`research` is a `fields` row, Serves only); oc42:35-39 (`research` stays outside `TYPED_RECORD_KINDS`) |
| 10 | The new leg `retrofit progress selftest` is written by hand into `tools/gate-legs.json`, with no `enforces`. | R1 | MISMATCH | ll10:155, ll10:216-219; oc7:58-63; wb11:36-47 |
| 10 | `retrofit_progress.py` reads the ledger through memory-tree's own inline `legacy_ledger.py`. `manifest-check.sh` reaches the module by `resolve_kit_file` and runs it as a bounded subprocess. | R3 | AGREES | ll10:31-35, ll10:47-50; wb13:57-58 (S8, the inline copy in `tools/memory-tree/`) |
| 23 | The new leg `adopt instructions selftest` is written by hand into `tools/gate-legs.json`, with no `enforces`. | R1 | MISMATCH | ll23:197, ll23:267-270; oc7:58-63; wb11:36-47 |
| 23 | `item.adopt.instructions` is a complete dl12 row from four facts: actor `command`, needs, proven-by, and "each proposal an owner item". It names no actor name, no `inputs`, no `returns`, no `outcomes` and no `routes`. | R4 | MISMATCH | ll23:88-91; dl12:43, dl12:109, dl12:113, dl12:127-129, dl12:147-148; ll8:232-240 (the sibling adopt rows name the actor, `returns` and routes) |
| 23 | The row's step slot, an adopt item that belongs to none of the five steps | R4 | UNKNOWN UNTIL BUILT | dl12:80-81; ll8:122-126, ll8:379-388 (F2 asks for `program = "adopt"` in place of `step`) |
| 64 | S10 and S11 re-guard the `adopt program selftest` and `code record selftest` legs in their `tools/memory-tree/kit.toml` declarations, and `tools/gate-legs.json` is the render. Both legs already carry `enforces` from ll46 and ll47. | R1 | AGREES | ll64:76-81, ll64:109-111, ll64:183, ll64:242-244; wb11:36-47; ll46:40-43; ll47:33-36; oc7:109-111 reds guard plus `enforces` only under `never`, and gov runs `with-hooks-report` (`.governance/policy.json:173-176`, `tools/policy/catalogue.toml:29-32`) |

2.

- **ll10, the leg by hand.** The spec says (ll10:155): "`tools/gate-legs.json`: the `retrofit progress selftest` leg". It names no `enforces` anywhere (grep `enforces` over ll10 prints nothing). The parent says (wb11:36-38): "Each leg is declared exactly once: a `[[gate_leg]]` row in its kit's descriptor when an adopter receives it, else an `[[exempt_leg]]` row", and (wb11:43-45) "`--write` renders `tools/gate-legs.json` from every declaration; `--check` exits 1 when the file differs". The meta-check (oc7:61-62) adds: "a leg carrying no `enforces` is red. Each red is excused only by a row of the shrink-only pending list".
  Change: Files touched and §7 should declare the leg with `leg_factory.py new` as a `[[gate_leg]]` row in `tools/memory-tree/kit.toml`, the kit that ships `retrofit_progress.py`, and render it with `--write`. The row needs a non-empty `enforces` naming the `principle.*` or `practice.*` tags it holds. ll52 S34 (ll52:148-150), at order 27, re-declares this leg later but names no `enforces` either. So the declaration and `enforces` belong at ll10's own pass (order 22), or ll52 S34 must name `enforces` and ll10 must not hand-write the row.
  Cause: pre-existing. oc7 and wb11 read the same at `82a392696` (`git show 82a392696:<spec> | diff - <spec>` is empty for both).
- **ll23, the leg by hand.** The spec says (ll23:197): "`tools/gate-legs.json`: the `adopt instructions selftest` leg". It names no `enforces`. The parent says the same as above: wb11:36-38, wb11:43-45 and oc7:61-62.
  Change: declare the leg with `leg_factory.py new` in `tools/playbook/kit.toml`, the kit of `adopt_instructions.py`, with `enforces` named, and render it with `--write`. ll52 S35 (ll52:151-152), at order 27, comes after ll23 (order 25) and also names no `enforces`.
  Cause: pre-existing (oc7 and wb11 unchanged since `82a392696`).
- **ll23, the loop row.** The spec says (ll23:88-91): "`item.adopt.instructions`, a `[[item]]` row of `tools/loop/loop.toml` in TOOL-dDeclaredLoop-12's schema beside TOOL-dLinkedLibrary-8 S9's five: actor `command`, needs the install, proven by the legacy pairs and the `ruling` records". The parent says (dl12:109): `actor = "command:plan.recommend"  # <kind>:<name>`. It requires (dl12:127-129) `inputs`, then `allowance` and `returns`, "yes for a non-role actor", and `outcomes` and `routes`, "yes". It checks (dl12:43) that "every input names a layer tag of `tools/playbook/layers.toml`", (dl12:113) that `returns` is a `record-kind.*` tag, and (dl12:148) that `routes` holds "exactly the outcomes as keys".
  Change: S8 should spell the row whole. That means `actor = "command:adopt.instructions"`, `inputs` as `layer.<tag>:<what>` entries (the harness files and the legacy list), `allowance`, `returns = "record-kind.ruling"`, a closed `outcomes` set (for example captured, ruled and none) and one route per outcome, in the shape of ll8's table (ll8:232-240). AC8 should then grade the row through `check_program`, not a bare grep for the tag.
  Cause: pre-existing (dl12 is byte-identical at `82a392696`).

3.

- **ll23, the row's step.** dl12 requires `step` (dl12:123) and keeps adopt items out of the five steps (dl12:80-81). ll23 depends on ll8 F2's ask, that a row may name `program = "adopt"` in place of `step`. That ask is not answered in any dDeclaredLoop spec or BACKLOG: grepping for `ADOPT-PROGRAM` and `program = "adopt"` under `memory/builds/dDeclaredLoop/` prints nothing. dDeclaredLoop's answer to that ask, or `check_program` as built, decides it.

4.

- **ll6, R2 (a record kind):** answered by the AGREES row above. The view only reads `research`-bound records through ll13's selector and adds no kind.
- **ll24, R2:** not bound. `gate`, `planted`, `shape` and `observed` are front-matter keys of gotcha class records. They are not a `**Serves:**` kind, and tr1's rows hold no gotcha kind (tr1:203-214). Reading `LEG_MANIFEST` adds no leg.
- **ll25, R2:** not bound. `note` is a value of `gotchas.KINDS` (`tools/memory-tree/gotchas.py:75`), not a record kind.
- **ll25, R3:** not bound. The `sys.path.insert(0, "tools/codebase-map")` at ll25:125 is a §4 evidence probe run at the repo root, not kit code. Each product edit stays inside its own kit.
- **ll49, R1:** not bound. S2 reads a leg's `ceiling` from the rendered manifest and adds or reshapes no leg.
- **ll49, R2:** not bound. The only kind is the generated records table's `deviation` row.
- **ll53, R1:** not bound. It cites `tools/gate-legs.json:1368` as evidence, and S7 edits a spec's §7 leg line, not a leg.
- **ll61, R1:** not bound. It adds no leg.
- **ll61, R2:** not bound. It adds no kind. It also keeps to R3 by carrying `tree_kill_py` inline and rejecting the import of `regen.py` (ll61:92-94).
- **ll67, R3:** not bound. `importlib` loads `corpus_ids.py`, which sits in the same kit (`tools/memory-tree/gotchas.py:146-153`; ll67:78-81).
- **ll67, R2:** not bound. It adds no kind.
- **ll86, R2:** not bound. Its "acceptance ledgers" (ll86:232) are BUILD-METHOD's per-unit ledgers, named `-<n>-acceptance-ledger.md`, for example `2026-10-04-build-TOOL-aBatchedMinors-2-1-acceptance-ledger.md`. They are not dl17's typed `-acceptance-<n>.md` record (dl17:35-43), so oc42 S3's file-name join does not match them.
- **ll86, R3:** not bound. Every code edit sits in its own kit. `read_pid_image` is only cited in a comment, and AC19's `regen.py` load is a scratch-copy probe.
- **ll96, R1:** not bound. It reads that the `codebase-map coverage + freshness` leg has no `guard` (ll96:221-222) and adds no leg.
- **ll96, R3:** not bound. S11's read of `tree_lib.unfenced_lines` and `sh_hygiene.extract_heredoc_body` lives in `tools/lib/resolve-python.test.sh`. `tools/lib/` has no `kit.toml` and is gov-internal, so no kit imports a sibling. S8's `read_blobs_at` belongs to the census's own kit, memory-tree.
- **ll102, R1:** not bound. It names the `lexicon naming predicates` leg (`tools/gate-legs.json:1455`) and adds none.
- **ll102, R3:** not bound. `adopt_program.py` reads memory-tree's own `tree_lib`. `lexicon.py --suggest` and `gen_map.py --write` are pass commands, not kit code.

5.

- No citation spec is in this group. Group B1 is rule-wide, so there are no uncited revised units to report.

## Group B2, rule-wide, sibling kits

I found one MISMATCH in Group B2, in spec 74 (S26). Specs 11 and 18 and the rest of spec 74 agree with R3. The hits in the other 14 specs either stay inside their own kit or are not code inside a kit at all. Nothing was written.

1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 11 | S6 deletes the drift builder, which removes drift-audit's in-process import of memory-tree's `annotations.py`. The seed argv (S3) reaches `annotations.py` as a subprocess. | R3 | AGREES | ll11:88-91 "which the builder imports; the deletion removes that import"; ll11:47-48 the `seed = ["python3", "{prefix}/memory-tree/annotations.py", …]` argv; oc7:202-205 "A kit may not import a sibling kit" |
| 18 | Eleven kits share the region factory as inline parity-gated copies, never by import from another kit. | R3 | AGREES | ll18:72-77 "Each Python site inlines the `region_py` block once per kit module … `format-guard.js` carries `region_js`"; oc7:202-204 "a kit carries shared code inline"; dGroundRules-1 §4:113 "so a kit carries shared code inline" |
| 74 | The `tree_kill_py` block (canonical in run-gates `regen.py`) is carried inline in memory-tree's `gotchas.py`. `region_py` and `region_nth` are inline copies. | R3 | AGREES | ll74:68-70 (S10), ll74:125-129 (S25), ll74:87-92 (S16), ll74:93-97 (S17); oc7:202-204 |
| 74 | `dossier_move.py`, in the codebase-map kit, validates `--build` and `--unit` against memory-tree's `SLUG_RE` and `GRANT_ID_RE`, reused rather than re-implemented. | R3 | MISMATCH | ll74:130-132; ll74:363-364; ll74:215; oc7:202-205; wb28:63-64 |

2. MISMATCH

- **ll74:130-132 (S26) and ll74:363-364 (§10).**
  - The spec's side: "`dossier_move.py apply` tests `--build` and `--unit` with `fullmatch` on `SLUG_RE` and `GRANT_ID_RE` (`tools/memory-tree/backlog.py:129`, :453)". The reuse audit adds that these are extended seams and "no item mints a second implementation of any". Files touched puts the code in the codebase-map kit: ll74:215 "`tools/codebase-map/dossier_move.py`: S26", and ll19:176 makes it a new file there.
  - The spec never says "import". But with no second implementation allowed, the only way to build it is to import `backlog.py` in process from codebase-map.
  - The parent's side: oc7:202-205 "A kit may not import a sibling kit (TOOL-dGroundRules-1, §4 Evidence), so the module carries the inline `resolve_kit_dir` block … and runs `<sys.executable> <kit>/policy.py get …`". wb28:63-64 "A run-gates or govkit module imports no playbook module (TOOL-dGroundRules-1 §4; …)".
  - Nothing admits the import. `tools/codebase-map/kit.toml:7` holds only `requires = ["memory-tree"]` and no `requires_if` row. Probe: `grep -rn requires_if tools/*/kit.toml` prints only the memory-tree and roles rows. `grep -rn 'memory-tree\|import backlog\|tree_lib' tools/codebase-map/*.py` shows no codebase-map module imports memory-tree today.
  - Change: S26 picks one of three. (a) Carry the two patterns inline under a parity row whose canonical is `backlog.py`, and say in §10 that this is the parity copy, not a second implementation. (b) Validate through a memory-tree verb run by subprocess, found by the inline `resolve_kit_dir`. (c) Add a `requires_if` row to `tools/codebase-map/kit.toml` declaring the import. Whichever is chosen also binds the clause it amends, 64 S14 (ll64:88-90, ll64:318, outside this group).
  - Cause: pre-existing. `git show 82a392696:…PLAY-dOrderedCharter-7.md` already prints line 202, "A kit may not import a sibling kit", and `git show 82a392696:tools/codebase-map/kit.toml` already holds only `requires`.

3. UNKNOWN UNTIL BUILT

- None.

4. Hits the rule does not bind

- 11, other mentions: `annotations.py` uses memory-tree's own `legacy_ledger.py` copy and `derive_pin_hash`, which lives in `tools/memory-tree/design_lib.py` (oc24:62). The `annotations.resolve-scope` read comes from spec 4 S7, through memory-tree's own `policy_value.py` (ll4:43), so its row belongs to spec 4's group.
- 18: the `sys.path.insert(0, 'tools/lib')` at ll18:261 is an AC2 probe, and `tools/lib` is not a kit (it has no `kit.toml`). `deviation_join.py`'s read of `GEN_REGION_AWK` is a §3 non-goal, already declared by memory-tree's `requires_if` row for `unattended`.
- 43: `check-microformats.sh` is a root tool and `run-gates.test.sh` is a gov-internal suite. Both source `tools/lib/region.sh`, and `tools/lib` is not a sibling kit.
- 51, 90, 94: "import" means the census ruling that admits a CI job as a leg, not a Python import. The govkit, gate-lint and drift-audit paths they cite are precedents.
- 69: `govkit.py` is loaded by path from `tools/govkit/steps/retire_reuse_lookup.py`, inside the govkit kit itself.
- 75: `reuse_entries.py` reads dossier data under `memory/map/features/`, and `check_reuse_entries` is memory-tree's own.
- 80: `corpus_ids.resolve_bash` and `row_grammar` are memory-tree modules. S12 restates the `read_pid_image` rule in Python rather than calling it. S18 only names govkit and `tools/lib` in a docstring.
- 91: S24's `tools/gate-lint` on `sys.path` and its `tree_lib.unfenced_lines` read are in `tools/lib/resolve-python.test.sh` (ll91:253). That is gov-internal `tools/lib`, not kit code. The 86 S25 it amends belongs to spec 86's group.
- 92: `tools/govkit/matrix.py:453` is cited as precedent for `core.autocrlf`, not called.
- 97, 99, 100: the walk follows `adopt_program.py`'s own imports into memory-tree's `tree_lib`, all in one kit. The `gen_map.py --write` they name is the Rollout's re-render command.
- 98, 101: these touch only build records. 101's `sys.path` entry (ll101:38) is a scratch copy's directory in a probe.

5. Unused citations

- Not applicable. Group B2 is rule-wide and holds no citation spec.
