**Serves:** research TOOL-dWellOiledMachine-1

# dWellOiledMachine — the cross-check readers' returns, verbatim

The `gov-spec-reviewer` returns the cross-check record [`2026-10-28-build-TOOL-dWellOiledMachine-1-parents-crosscheck`](2026-10-28-build-TOOL-dWellOiledMachine-1-parents-crosscheck.md) is assembled from, each copied from its agent transcript by script; only the headings are the main loop's, each returned heading demoted two levels. Group A1, citation, read specs 3, 4, 7, 8, 9, 11, 16, 19, 27, 30 and 32; Group A2, citation, read specs 34, 39, 42, 43, 44, 45, 48, 51, 53, 54, 56 and 58; Group B1, rule-wide, read specs 1, 2, 5, 6, 10, 12, 13, 14, 15, 17, 20, 21, 22, 23, 24, 25, 26, 28, 29, 31, 33 and 36; Group B2, rule-wide, read specs 38, 40, 41, 46, 47, 49, 55, 57, 59, 61, 64, 74, 79, 81, 90, 92, 93, 94, 96, 97, 108 and 126; Group B3, rule-wide for R3 alone, read specs 35, 37, 50, 52, 63, 65, 68, 91, 95, 112, 115, 117 and 120.

## Group A1

Group A1 (specs 3, 4, 7, 8, 9, 11, 16, 19, 27, 30, 32) comes to 51 assumptions: 21 AGREES, 25 MISMATCH and 5 UNKNOWN UNTIL BUILT.

Twenty-four of the mismatches are pre-existing: the parent text already read that way at `ab864dfc8`. dDeclaredLoop, dPlacedRequest, dOrderedCharter, dKeptSession and dWitnessedBar specs are unchanged since then (`git diff --stat ab864dfc8 d1721ef20` printed nothing). Row 34's dBoundRoles-25 surface was also already there. The one mismatch the re-grounds caused is row 51: the `record find` cap moved from tr9 S3 into S4 at `794a0f5fb`. In rows 18 and 23, dBoundRoles' re-ground changed its own specs (br5 S4, br22 S5) to apply R3 to the very key the dWellOiledMachine spec still reads through `resolve`.

#### 1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 3 | `lifecycle-request` and `attendance-override` are `[[record-kind]]` rows in `tools/memory-tree/record-kinds.toml` | cite | AGREES | wm3:49-51, :97; tr1:62-66. The rows name only `home`, `writer` and `check`, so the builder must fill tr1's other required columns. |
| 3 | The row's `check` names a leg, `runtime selftest` | cite | AGREES | wm3:51; tr1:196. wm1:207 mints that leg. |
| 3 | Both kinds are ref-commit records, not typed build-folder records | R2 | AGREES | wm3:45-49, :93-94; oc42:35-39 |
| 3 | `flow.wait-ceiling` and `attendance.scope` are read through `resolve` in process from `tools/runtime/lifecycle.py` | R3 | MISMATCH | wm3:62, :96, :186; oc7:202-205, :379-380 |
| 3 | `derive_breakpoints` (loop kit) is re-pointed to the verb `lifecycle.py attendance` | R3 | AGREES | wm3:98-102 (a verb, not an import) |
| 3 | `unattended.sh --claims` shows whether the build lease is absent, `released` or terminal | R8 | AGREES | wm3:86-87; pr1:206-208 (fields 1-5 keep status in field 3); `unattended.sh:2204` |
| 4 | The `intake` row in `record-kinds.toml` has `layer = "runtime"`, `home = ""`, and no `lifecycle` or `readers` | cite | MISMATCH | wm4:70-74; tr1:64-66; tr18:45-49, :130-133 |
| 4 | `derive_request_content_key` (loop kit `request.py`) is reached through `resolve_kit_dir` and called in process | R3 | MISMATCH | wm4:39-40; pr19:33-36 (`python request.py key <file>` exists); oc7:202-205 |
| 4 | The session binding is read through the verb `session_binding.py read <id>` | R3 | AGREES | wm4:56-57 |
| 7 | br3's work order carries an `allow` list of permission-rule entries, and a `script` | cite | MISMATCH | wm7:34-39, :99-100, :113; br3:48-61 |
| 7 | br22 S1 declares each stage's `role` and `fan`, read through `load_workflows` | cite | AGREES | wm7:77-79; br22:34-45 |
| 7 | br25 S2 moves `checkHarnessCall` into `tools/roles/spawn-guard.js` | cite | AGREES | wm7:122-124; br25:47-53 |
| 7 | `act_binding.py` calls the roles kit's `load_workflows` and `load_run_journal`, and runlog's `resolve_session_tree`, in process | R3 | MISMATCH | wm7:36-37, :80-82, :153; oc7:202-205 |
| 7 | `read_claims` fetches the remote | R8 | AGREES | wm7:162-163; pr1:76-80 |
| 8 | Return validation is dBoundRoles' return check | cite | AGREES | wm8:98-99; br5:39-54 |
| 8 | The `return` row: `layer` `runtime`, `schema` header with a `source` and no `fields`, `readers` `supervise.py`, `lifecycle` in prose | cite | MISMATCH | wm8:81-85; tr1:177-182, :79-81; tr18:45-49, :130-133 |
| 8 | Door writes land tracked records in the act's working tree | cite | AGREES | wm8:186-188; tr2:82-83 (S8 `git add`) |
| 8 | `roles.retries` is read through `resolve` (I31) in process | R3 | MISMATCH | wm8:58-59; br5:63-67; oc7:379-380 |
| 8 | The new leg `runtime returns block parity` is written into `tools/gate-legs.json` with no `enforces` | R1 | MISMATCH | wm8:88-91, :166, :179; wb11:36-49; oc7:58-63 |
| 9 | The work order carries a `fan`, its stage's declared `fan`, rendered by dBoundRoles | cite | MISMATCH | wm9:54-57, :92, :207; br3:48-54; br22:34-37 |
| 9 | br22 S5's `read_agent_limit` reads the same key inside the roles kit | cite | AGREES | wm9:222-224; br22:53-58 |
| 9 | `runtime.agents-in-flight` is read through `resolve` in process | R3 | MISMATCH | wm9:40-42; br22:53-56; oc7:379-380 |
| 11 | The `workspace` kind's row lands in `record-kinds.toml` "(TOOL-dTotalRecall-2)" | cite | AGREES | wm11:57, :114. The registry is tr1's (tr1:62); tr2 only reads it (tr2:45-50). The writer `write_workspace_record` is legal there. |
| 11 | `build.worktree` is read through `resolve` in process | R3 | MISMATCH | wm11:33-35; oc7:379-380 |
| 11 | The worktree root comes from the playbook kit's `resolve_node_overrides` and `derive_worktree_root`, called by name | R3 | MISMATCH | wm11:36-38, :275; oc7:202-205; `render_playbook.py:1777` has `--answers` |
| 11 | branch-reconcile reads the records as files and imports nothing from the runtime kit | R3 | AGREES | wm11:82-85 |
| 11 | The new leg `runtime workspace fixtures` is written into `tools/gate-legs.json` | R1 | MISMATCH | wm11:86-89, :164, :174; wb11:36-49; oc7:58-63 |
| 16 | tr18 renames the memory tree's Serves kind `journal` to `log`, freeing the word for runtime's journal kind | cite | AGREES | wm16:82-84; tr18:76-82, :108-109 |
| 16 | `record-kind.journal` can own `<git common dir>/runlog/` under that name | cite | UNKNOWN UNTIL BUILT | wm16:82-84; tr18:79, :144, :167, :172-173 |
| 16 | `runtime.journal` is read through the policy kit's `resolve` in process | R3 | MISMATCH | wm16:69-70, :133; oc7:379-380 |
| 16 | runlog carries the grammar inline under a parity row; the tick runs `journal.py prune` as a subprocess | R3 | AGREES | wm16:40-44, :74-77 |
| 19 | `F` comes from each stage key's `fan` in the stage rows | cite | AGREES | wm19:38, :51; br22:34-37 |
| 19 | The review-only `shape-run` record: `Kind` is `diff-review` or `spec-audit`, and `Round`, `Intensity` and `At` are required | cite | AGREES | wm19:110-111; tr11 §4 `SHAPE_RE` and the record |
| 19 | Author/verifier separation belongs to br25's admission | cite | MISMATCH | wm19:88; br25:41-61, :88 |
| 19 | `gov_record.py new shape-run --act <act>` writes an act-form row; a repeat writes nothing | cite | UNKNOWN UNTIL BUILT | wm19:69-73, :212-221; tr11:59-65; tr2:62-66 |
| 19 | `roles.shape-enforce` is read through `readPolicy` (`policy-mirror.js:132`) inside `act-binding.js` | R3 | MISMATCH | wm19:56-57; ks8:62-66 |
| 19 | The reconcile reads `load_agent_transcript` from `tools/roles/handoff.py` in process | R3 | MISMATCH | wm19:62-63, :72; oc7:202-205 |
| 27 | The `build-readme` and `claim` rows carry `root = true` as tr19 S3's stand-in, for dWellOiledMachine to drain | cite | AGREES | wm27:26-27, :62-63; tr19:62-67 |
| 27 | `check_causes` in `record_causes.py` is the causes check that gains the `root-until` read | cite | AGREES | wm27:64-67; tr19:90-96 |
| 27 | `record-kinds.toml` accepts a new column `root-until` | cite | UNKNOWN UNTIL BUILT | wm27:63-64, :126; tr1:198-200 |
| 27 | An `intake-key` `[[native]]` row with a `module:NAME` pattern and resolver | R3 | AGREES | wm27:68-71; oc28:42-49, :119-129 (the parent's own form) |
| 30 | Act-form `shape-run` records exist with `Variant`, `Effort` and `Rerun`, readable per build | cite | UNKNOWN UNTIL BUILT | wm30:37-41, :57-61, :73; tr11:53-59 |
| 30 | The experiment reconcile reads `load_run_journal` and `load_agent_transcript` in process | R3 | MISMATCH | wm30:49-51; oc7:202-205 |
| 32 | The `act` row has `tag = "record-kind.act"` and `layer = "runtime"` | cite | MISMATCH | wm32:67-68; tr1:173, :234-235; tr18:133 |
| 32 | The door mints `<date>-build-<anchor id>-act-<act12>.md` | cite | MISMATCH | wm32:69; tr2:174-187 |
| 32 | `write_act_record` writes through the door with no `Caused-by` | cite | MISMATCH | wm32:69-73; tr19:58-67 |
| 32 | The door, one write per id, refuses a different value | cite | AGREES | wm32:186-187; tr2:62-66 |
| 32 | The door accepts the act record written at the act's exit (lease authority) | cite | UNKNOWN UNTIL BUILT | wm32:71-72; tr2:188-197, :335-345 |
| 32 | `act` is a new build-folder record kind with no join to `TYPED_RECORD_KINDS`, the factory table or HYGIENE | R2 | MISMATCH | wm32:67-71, :230; oc42:35-59 |
| 32 | `render_wall` (`tools/roles/handoff.py:737`) is called from `tools/runtime/act.py` | R3 | MISMATCH | wm32:75-76, :283; oc7:202-205 |
| 32 | The `Acts` table has one row per act record of the run, read through `record find` | cite | MISMATCH | wm32:88-89; tr9:89-103 |

#### 2. Mismatches

**Row 4 (wm3, policy reads in process)**
- wm3:62 says "the ceiling read through `resolve`", and wm3:96 says "`attendance.scope` … through `resolve` at the write".
- oc7:202-205 says "A kit may not import a sibling kit … runs `<sys.executable> <kit>/policy.py get <key>`". oc7:379-380 says "read through the policy kit's `get` verb … as a subprocess, the one seam a sibling kit may reach".
- Change: wm3 reads both keys by running `policy.py get <key>` as a subprocess, finding the policy kit through an inline `resolve_kit_dir`.
- Cause: pre-existing.

**Row 7 (wm4, `intake` row cells)**
- wm4:71-73 says "`layer = "runtime"`, `home = ""` … `schema = { form = "rows" }`", with no `lifecycle` and no `readers`.
- tr1:64-66 says "`layer`, `home`, `readers` and `lifecycle` are admitted and required from TOOL-dTotalRecall-18".
- tr18:45-49 says "Every row … carries non-empty `home`, `lifecycle`, `readers` and `layer` … `layer` a layer tag … `home` … `<git-common-dir>/<glob>`". tr18:131 closes `lifecycle` to `append-only`, `current-state`, `frozen`, `generated` and `out`.
- Change: S6 sets `home = "<git-common-dir>/requests/*"`, `layer` to a layer tag such as `layer.runtime`, `lifecycle = "append-only"`, and `readers` either as read keys or `[]` with `readers-none`.
- Cause: pre-existing.

**Row 8 (wm4, content key loaded in process)**
- wm4:39-40 says "`derive_request_content_key(text)` … reached through `resolve_kit_dir` from the loop kit".
- oc7:202-205 says "A kit may not import a sibling kit". pr19:36 provides "`python request.py key <file>` prints it".
- Change: `intake.py` runs `request.py key` as a subprocess, or `tools/runtime/kit.toml` declares a `requires_if` row naming `loop`.
- Cause: pre-existing.

**Row 10 (wm7, the work order's `allow` list and `script`)**
- wm7:34-39 says "`tool` (`Workflow` when the work order carries `script` …) … `allow`, the work order's list of permission-rule entries". wm7:99-100 says "Rendering the work order's `allow` list: dBoundRoles' work-order renderer (TOOL-dBoundRoles-3)".
- br3:48-54 renders five blocks only: `### item`, `### inputs`, `### allowance`, `### return`, `### witness`. br3:55-61 says the allowance is "repo-relative path prefixes in the `ROUTED_PATHS` grammar".
- `grep -cE '`allow`|permission-rule|script'` over br3 prints 0, both today and at `ab864dfc8`. No dBoundRoles spec or BACKLOG row names a permission-rule list.
- Change: wm7 either owns the `allow` and `script` fields (where they come from and who renders them) or files an ask to dBoundRoles (br3) for them. Its non-goal stops citing br3 for something br3 does not render.
- Cause: pre-existing.

**Row 13 (wm7, sibling modules in process)**
- wm7:36-37 says "read through `load_workflows`, `tools/roles/roles_lib.py:364`". wm7:80-82 says "through `resolve_session_tree` (`tools/runlog/extract.py:266`) … `load_run_journal` (`tools/roles/handoff.py:686`)".
- oc7:202-205 says "A kit may not import a sibling kit".
- Change: `act_binding.py` reaches the roles and runlog kits through their verbs by subprocess (or files asks for verbs that print stage rows, a run's journal and a session tree), or declares `requires_if` rows in `tools/runtime/kit.toml`.
- Cause: pre-existing.

**Row 16 (wm8, `return` row cells)**
- wm8:83-84 says "schema form `header` sourced at `tools/runtime/returns.py:RETURN_FIELDS`, … readers `supervise.py`, lifecycle "written once per spawn site, cleared when the item is witnessed"", with `layer runtime`.
- tr1:177-180 says "The row's `fields` and the literal must agree both ways". tr1:79-81 reds "a `schema.source` whose literal no longer matches the row's `fields`".
- tr18:131-133 requires `lifecycle` in the closed set, `readers` as read keys `<family>:<field>` or `[]` with `readers-none`, and `layer` as a layer tag. dTotalRecall-11's own row (its §4) uses the same loose cells, but tr18 S1 is the rule.
- Change: S8 adds `fields = [...]` equal to `RETURN_FIELDS`, `lifecycle = "current-state"` (or `out`), `readers` as read keys or `readers-none`, and a layer tag.
- Cause: pre-existing.

**Row 18 (wm8, `roles.retries` in process)**
- wm8:58-59 says "`roles.retries` … read through `resolve`, I31".
- br5:63-67 says "`roles.retries` read by running … `policy.py get roles.retries` as a subprocess … a kit imports no sibling kit". oc7:379-380 says the same.
- Change: `returns.py` reads the key by a `policy.py get` subprocess.
- Cause: pre-existing. The rule (oc7) is unchanged since `ab864dfc8`; br5's re-ground (rev-3) applied it to this same key.

**Row 19 (wm8, hand-written leg)**
- wm8:90-91 says "the leg `runtime returns block parity` in `tools/gate-legs.json` runs it", with `tools/gate-legs.json` in Files touched (:179).
- wb11:36-38 says "Each leg is declared exactly once: a `[[gate_leg]]` row in its kit's descriptor … `--write` renders `tools/gate-legs.json`". oc7:60-61 says "a leg carrying no `enforces` is red".
- Change: S9 declares the leg once as a `[[gate_leg]]` row of `tools/runtime/kit.toml` through `leg_factory.py new`, names its `enforces` tag, and renders the manifest with `leg_factory.py --write`.
- Cause: pre-existing.

**Row 20 (wm9, `fan` on the work order)**
- wm9:56-57 says "the work order's `fan` being its stage's declared `fan` (TOOL-dBoundRoles-22 S1 …)". wm9:92 says "TOOL-dBoundRoles-22's stage `fan`, carried by the work order dBoundRoles renders".
- br22:34-37 puts `fan` on the `[[workflow.stages]]` rows of `workflows.toml`. br3:48-54's five work-order blocks carry no `fan`, and no dBoundRoles spec puts `fan` into a work order.
- Change: the supervisor takes the act's fan from the workflow entry's stage rows through a roles-kit verb, or wm9 files an ask to dBoundRoles (br3) for a `fan` field on the work order.
- Cause: pre-existing.

**Row 22 (wm9, `runtime.agents-in-flight` in process)**
- wm9:41 says "read once per call through `resolve` (`tools/policy/policy.py:752`, I31)".
- br22:53-56 says "through TOOL-dBoundRoles-21 S1's `read_policy_setting` …, the roles kit's one runner of the `policy.py get` subprocess". oc7:379-380 states the rule.
- Change: `slots.py` reads the key by a `policy.py get` subprocess. A refused read keeps the catalogue default it already names.
- Cause: pre-existing. br22's re-ground moved the parent's own read of this key away from `resolve`.

**Row 24 (wm11, `build.worktree` in process)**
- wm11:33-34 says "`resolve("build.worktree")` (I31; `tools/policy/policy.py:752`)".
- oc7:379-380 states the subprocess rule.
- Change: `allocate_workspace` runs `policy.py get build.worktree` as a subprocess.
- Cause: pre-existing.

**Row 25 (wm11, the worktree root)**
- wm11:37-38 says "`worktree_root` override (`resolve_node_overrides`, `tools/playbook/render_playbook.py:399`) else `derive_worktree_root` (`:560`)".
- oc7:202-205 says "A kit may not import a sibling kit".
- Change: the runtime kit reads the root through the playbook kit's CLI (`render_playbook.py --answers worktree_root`, `:1777`) as a subprocess, or files an ask for a verb.
- Cause: pre-existing.

**Row 27 (wm11, hand-written leg)**
- wm11:88-89 says "the leg `runtime workspace fixtures` in `tools/gate-legs.json` runs every case".
- wb11:36-38 requires one declaration rendered by `leg_factory.py --write`; oc7:60-61 reds a leg with no `enforces`.
- Change: S10 declares the leg as a `[[gate_leg]]` row of `tools/runtime/kit.toml` with `enforces`, rendered by the factory.
- Cause: pre-existing.

**Row 30 (wm16, `runtime.journal` in process)**
- wm16:69-70 says "reads `runtime.journal` through the policy kit's `resolve` (`tools/policy/policy.py:752`)". wm16:133 has `value = resolve("runtime.journal", R)`.
- oc7:379-380 states the subprocess rule.
- Change: `journal.py prune` runs `policy.py get runtime.journal` as a subprocess.
- Cause: pre-existing.

**Row 34 (wm19, author/verifier separation)**
- wm19:88 says "The separation of author and verifier: TOOL-dBoundRoles-25's admission".
- br25:41-61 (S1-S4) is rule 6, `checkHarnessCall`, rule 7, landed-blob admission and the helpers' homes; br25:88 retires `agent-cap.js`. `grep -nE 'author|verifier|separat'` over br25 finds no such rule, and no dBoundRoles spec names one.
- Change: the non-goal names the unit that actually owns author/verifier separation, or is dropped.
- Cause: pre-existing.

**Row 36 (wm19, `readPolicy` in process)**
- wm19:56-57 says "read through `readPolicy` (`tools/policy/policy-mirror.js:132`, I31)", inside the runtime kit's `act-binding.js`.
- ks8:62-66 says "running dGroundRules' JS reader's own CLI as a subprocess, `node <policy kit>/policy-mirror.js get …` … the hook never `require`s the policy kit's module".
- Change: `act-binding.js` spawns `node <policy kit>/policy-mirror.js get roles.shape-enforce --repo <repo>` under a bounded timeout.
- Cause: pre-existing.

**Row 37 (wm19, `load_agent_transcript` in process)**
- wm19:62-63 says "read through `load_agent_transcript` (`tools/roles/handoff.py:626`)", from the runtime kit's reconcile.
- oc7:202-205 says "A kit may not import a sibling kit".
- Change: reach the roles kit through a verb by subprocess (or an ask for one), or declare a `requires_if` row.
- Cause: pre-existing.

**Row 43 (wm30, roles functions in process)**
- wm30:50-51 says "reads each started agent's label through `load_run_journal` (`tools/roles/handoff.py:686`) and its effort through `load_agent_transcript` (`:626`)".
- oc7:202-205 states the rule.
- Change: same as row 37.
- Cause: pre-existing.

**Row 44 (wm32, `tag` and `layer`)**
- wm32:68 says "`tag = "record-kind.act"`, `layer = "runtime"`".
- tr1:173 says "`tag` is `record.<name>` …; the node id is `record-kind.<name>`". tr1:234-235 makes `new` refuse "a `tag` outside `record.`". tr18:133 says `layer` is "a layer tag".
- Change: S7 writes `tag = "record.act"` and a layer tag, plus `lifecycle` and `readers` in tr18's grammar.
- Cause: pre-existing.

**Row 45 (wm32, `id-rule` placeholders)**
- wm32:69 says "`id-rule = "<date>-build-<anchor id>-act-<act12>.md"`".
- tr2:177 says the door "mints each placeholder it holds; a grammar holding none names a given id". tr2:180-186 lists only `<n>`, `<seq>`, `<slug>`, `<date>` and `<unit id>`.
- Change: spell the rule in the door's placeholders, `<unit id>` for the anchor, or file an ask to dTotalRecall for a given-id suffix.
- Cause: pre-existing.

**Row 46 (wm32, no `Caused-by`)**
- wm32:69-71 lists the fields `Act` … `Wall`, with no `Caused-by` and no `--caused-by` on the door call.
- tr19:62-64 says "A kind whose registry row is not a root and a call with no `--caused-by` … is refused: exit 2 naming the kind and `Caused-by`, nothing written".
- Change: `write_act_record` passes `--caused-by` with a target that resolves (the act id once wm35's `act` class lands, or the work order's record key).
- Cause: pre-existing.

**Row 49 (wm32, `act` as an unjoined typed kind)**
- wm32:67-71 and :230 put a `-act-<act12>.md` record in the build's `build/` folder, written by `gov_record.py new act`.
- oc42:35-39 says the typed kinds are the ones named `<date>-build-<unit id>-<kind>-<n>.md`, and `RECORD_KIND_TOKENS` is the four untyped kinds plus `TYPED_RECORD_KINDS`. oc42:40-59 says the factory's kind list, the file-name join and HYGIENE's closed list are kept as one.
- Change: `act` joins `TYPED_RECORD_KINDS`, the factory's per-kind table and HYGIENE's closed kind list in one pass, as tr11 S3 does for `shape-run`, and its Serves line binds.
- Cause: pre-existing.

**Row 50 (wm32, `render_wall` in process)**
- wm32:75-76 says "`Wall` from its `duration_ms` rendered by `render_wall` (`tools/roles/handoff.py:737`)", in `tools/runtime/act.py`.
- oc7:202-205 says "A kit may not import a sibling kit".
- Change: render the wall time in the runtime kit, or reach a roles-kit verb by subprocess.
- Cause: pre-existing.

**Row 51 (wm32, `record find` cap)**
- wm32:88-89 says "one row per act record of the run read through `record find` (TOOL-dTotalRecall-9): `act`, `session`, `tokens` and `wall`".
- tr9:94-96 says "At most 40 rows, one per record, `key · kind · build · bytes · path:line`, no content", and "past 40, the last line reads `<total> rows match`". `find` has no run filter.
- Change: S10 says how it narrows to one run (`--kind act --build <slug> --paths`), reads the four fields per row through `record show` or the file, and handles a run with more than 40 act records instead of truncating it.
- Cause: re-ground. At `ab864dfc8` the 40-row cap and the field list sat in tr9 S4; `794a0f5fb` rewrote S3 and moved them there.

#### 3. UNKNOWN UNTIL BUILT

- **Row 29 (wm16, `record-kind.journal`).** tr18 frees the word (tr18:108-109) but keeps `KIND_ALIASES = {"journal": "log"}`, where "a comparison by value goes through `canonical_kind`" (:167, :172-173). It also registers a `runlog-journal` witness row over `<git-common-dir>/runlog/*` (:144), the same home. dTotalRecall's build of tr18 S5/S7 and tr9's home-to-kind join decide whether a `journal` row and that pocket can coexist.
- **Rows 35 and 42 (wm19 and wm30, act-form `shape-run`).** dTotalRecall's disposal of ask TOOL-dTotalRecall-105 (`memory/builds/dTotalRecall/BACKLOG.md:15`) decides it: whether tr11 gains `--act`, `Kind` `act`, an act-id `Caused-by` that tr11 S5 accepts, a `<unit id>` for the record name, and `Variant`/`Effort`/`Rerun`.
- **Row 40 (wm27, `root-until`).** tr1's build decides it: whether `check_record_kinds` refuses a column outside the two later columns it admits (tr1:198-200).
- **Row 48 (wm32, door lease authority).** tr2's door now refuses "a lease or claim held by another" session and reads the holder "through the verb §8 F6 asks dPlacedRequest for" (tr2:188-197, :335-345, added in the re-ground). The owner's F6 pick and dPlacedRequest's holder verb decide whether the supervisor's exit-time `write_act_record` counts as the lease-holding session. The same applies to the door writes of wm19 S6 and wm30 S5.
- **Not a table row (wm8 against br5 S3/S6).** br5:76-82 routes every schema-bearing stage through `spawnWithRetries`, and br5:55-62 holds a stop up to `roles.retries` with a SubagentStop `decision: block`. wm8 S5/S6 rewrites "every `agent(` call site" and adds a second SubagentStop hold on the same key. The landing order and dBoundRoles' build decide whether `readKeptReturn` wraps `spawnWithRetries` and whether one agent is held up to twice `roles.retries`.

#### 4. Text-probe hits the rules do not bind

This is a citation group, so no rule-wide hits were assigned; these are the term hits found while applying R1 to R9.

- `budget-ms` in wm4:61, wm7:70 and wm8:48 is a hook pack's I9 timeout, not dl33's budget edges (R8).
- `budget-spent` and "latency budget" in wm16:55 and :92 are a journal class and a CLI latency note (R8).
- `returns` in wm7:38, :196 and wm8:78 is the harness-args map, not a loop item's `returns` (R4).
- `disposition` in wm27:56-57 and :112-114 is dPlacedRequest's placement disposition, not dl16's door (R5).
- `journal` in each spec's `gen:spec-records` table is a generated Serves cell; tr18 keeps it as an alias (R2).

#### 5. Revised units cited that no assumption depends on

- wm3 (tr1): none.
- wm4 (tr1): none.
- wm7 (br3, br22, br25): none.
- wm8 (br5, tr1, tr2): tr2 appears only in a rejected alternative and in F1's rejected option; no design depends on it.
- wm9 (br22): none.
- wm11 (tr2): tr2 is cited, but the row's dependency is tr1's registry; nothing depends on tr2's door.
- wm16 (tr18): none.
- wm19 (br22, br25, tr2, tr11): br25 appears only in the non-goal at :88; no design depends on it.
- wm27 (tr19): none.
- wm30 (tr11): none.
- wm32 (tr1, tr2, tr9): none.

The parent specs most cited are in `C:\projects\coding-governance\.claude\worktrees\elastic-lalande-a8b091\memory\builds\`: `dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-{1,2,9,11,18,19}.md`, `dBoundRoles\spec\2026-10-25-spec-TOOL-dBoundRoles-{3,5,22,25}.md`, `dOrderedCharter\spec\2026-10-23-spec-PLAY-dOrderedCharter-7.md` and `dOrderedCharter\spec\2026-10-24-spec-PLAY-dOrderedCharter-42.md`.

## Group A2

I checked group A2 (specs 34, 39, 42, 43, 44, 45, 48, 51, 53, 54, 56 and 58) against the parents as they stand at `d1721ef20`. The tally is 38 rows: 17 AGREES, 20 MISMATCH and 1 UNKNOWN UNTIL BUILT.

- **Caused by the re-grounds (4):** wm42's list of readers of `.claude/roles.json`, wm48 S2, wm56 S1/S2 and wm58's lease-holder read.
- **Already there at `ab864dfc8` (16):** the larger share. Two classes recur. Nine are R3 sibling-kit reads, mostly the runtime kit calling `resolve`, `roles_lib`, `handoff.py` or memory-tree code in process. Four assume more from tr9's `record find` than it gives: at most 40 rows, and no content.

##### 1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 34 | `record find` / `record show` are tr9's verbs (S3, S5) | cite | AGREES | wm34:41-43 · tr9:89-96, :104-107 |
| 34 | One `record find` query returns every record naming the key, so `trace.rows = all` keeps every row | cite | MISMATCH | wm34:41-43, :57-60 · tr9:94-96, :207-209 |
| 34 | `build_run_model` reads records through `gov_record.py` subprocesses | R3 | AGREES | wm34:70-72 · oc7:379-380 |
| 34 | `trace.py` (runtime kit) resolves transcripts with runlog's `resolve_session_tree` | R3 | MISMATCH | wm34:47-48, :281 · oc7:202-205 |
| 34 | `trace.rows` is read by a `policy.py get` subprocess | R3 | AGREES | wm34:34-37 |
| 39 | The new leg `runtime bindings fixtures` is written by hand into `tools/gate-legs.json`, with no `enforces` | R1 | MISMATCH | wm39:83, :175, Files touched · wb11:36-49 · oc7:58-63 |
| 39 | tr19 S8's `check_causes` has a commit range it could grade through `bindings.py --check` (the F4 ask) | cite | MISMATCH | wm39:96, :270-273 · tr19:90-95 |
| 39 | `trace.identity` is read through `policy-shim.sh get` | R3 | AGREES | wm39 S2 |
| 42 | br1 gives `gov-session` its `layer` and `acts-as` and leaves its retirement to Runtime | cite | AGREES | wm42:103 · br1:107-108, :143-146, :333-336 (the cited `:98` is now `:107`) |
| 42 | S1 lists every by-value reader of `.claude/roles.json` | cite | MISMATCH | wm42:43-46 · br1 F6 rev-3 (`check_layer_roles` reads `.claude/roles.json`) |
| 42 | `handoff.py send` posts through the mailbox writer, which can only be reached by running `unattended.sh --mail post` | R3 | AGREES | wm42:53-54 · ks5 S5 |
| 43 | A workflow's stage `fan` (br22 S1) is the number of agents the run holds in flight | cite | MISMATCH | wm43:47-48 · br22:108-109 |
| 43 | `inflight.py` can read the stage rows of the workflow whose harness matches `scriptPath` | cite/R3 | MISMATCH | wm43:47-48 · br22:38-44 (`load_workflows`, the one reader, returning the composition) |
| 43 | Rule 7 lives in `tools/roles/spawn-guard.js` (br25 S2) | cite | AGREES | wm43:93-95, :167 · br25:47-50, :195 |
| 43 | `inflight.py` calls roles-kit `load_run_journal`, `load_session_calls`, `NOTIFICATION_RE` and process-monitor's `scan_processes`, `build_self_chain` in process | R3 | MISMATCH | wm43:67, :76-77, :82-83 · oc7:202-205 |
| 43 | The policy kit reads `inflight.mode` as a data file found through `resolve_kit_dir` | R3 | AGREES | wm43:91-92 |
| 44 | `record show` exits 2 on an unknown key, which is where the mirror read hooks in | cite | AGREES | wm44:77 · tr9:106 |
| 44 | `record find --build` can append mirror rows after its local rows | cite | MISMATCH | wm44:79-80 · tr9:94-96, :207-209 |
| 44 | `record_find.py` (memory-tree) may call `read_mirrored` (runtime kit) | R3 | MISMATCH | wm44:71, :92 · oc7:202-205 |
| 44 | `memory.mirror` is read "through `resolve`" in `mirror.py` | R3 | MISMATCH | wm44:48 · oc7:379-380 |
| 45 | The declared fan comes from br22 S1, "as wm43 S2 reads it" | cite | MISMATCH | wm45:57-58 · br22:38-44, :108-109 |
| 45 | `admit` reads the limit with `resolve("runtime.agents-in-flight")` | R3 | MISMATCH | wm45:132 · oc7:379-380 |
| 48 | `handoff.py owner-question --kind <k> [--attended]` exists, and `best-effort-recorded` reads as `resolve` | cite | AGREES | wm48:53-57 · br11:60-70 |
| 48 | Every answer of `owner-question` is one of its answer words | cite | MISMATCH | wm48:53-56 · br11:63-65 |
| 48 | `owner_items.py` reads the run keys through `resolve` and `read_catalogue_row` | R3 | MISMATCH | wm48:60-61, :71, :93 · oc7:379-380 |
| 51 | `record find` returns all of a build's act records with their `Tokens-*` and `Wall` fields | cite | MISMATCH | wm51:38-41 · tr9:94-96 |
| 51 | `measured` holds a stated figure until 30 measured work orders, as tr9 S6 does | cite | AGREES | wm51 §4 · tr9:108-111 |
| 51 | `build.spend-cap` is read by a `policy.py get` subprocess | R3 | AGREES | wm51:34-37 |
| 53 | `record find` gives the `Wall` of the act records whose `Item` is a given kind | cite | MISMATCH | wm53:62-65 · tr9:89-96 |
| 53 | `runtime.act-ceiling` and `runtime.admission-scope` are read through `resolve` | R3 | MISMATCH | wm53:65, :71 · oc7:379-380 |
| 54 | A role-schema `[[field]]` row `hardware` is one row (br2 S1) | cite | AGREES | wm54:73-75 · br2:33-38 |
| 54 | `resolve_role_model` reads `roles.model.<role>.<harness>` and raises `RolesError` on a harness with no equivalent | cite/R9 | AGREES | wm54:46, :81-82 · br21:62-65, :134-142 |
| 54 | `roles_lib.py model` answers for "the effective assignment" being checked | cite | MISMATCH | wm54:77-82 · br21:41-44 |
| 54 | A `[[stream]]` lists `units` with `order` (tr25 S2) | cite | AGREES | wm54:57-59 · tr25:40-42 |
| 54 | `--claims` gives each lease's `status` and `offer` | R8 | MISMATCH | wm54:31-33, :63, :113-114 · pr1:206-208 · `unattended.sh:2202` |
| 54 | `discover.py` (runtime kit) calls memory-tree `collect`, and roles-kit `load_workflows`, `resolve_role_model`, `resolve_role_harness`, in process | R3 | MISMATCH | wm54:33-34, :44-46 · oc7:202-205 |
| 54 | The preset check reaches roles through a `roles_lib.py model` subprocess | R3 | AGREES | wm54:81-82 |
| 54 | How `pick` reads the stream-plan record | R2 | UNKNOWN UNTIL BUILT | wm54:57-59 · tr25:34-39, S5-S6 |
| 56 | `read_policy_setting` returns None when the key is at its default (br21 S1), which is how `own` is derived | cite | AGREES | wm56:49 · br21:41-47 |
| 56 | The catalogue defaults `claude-code` and `setup-token, oauth-shared` are typed as fallbacks after a None | R9 | MISMATCH | wm56:36-39, :42-44 · br21:41-50 |
| 56 | `launch_act` (runtime) calls `resolve_role_harness`, `resolve_role_auth`, `derive_credential_target`, `check_credential_role` in `roles_lib.py` | R3 | MISMATCH | wm56:53-56 · oc7:202-205 |
| 58 | `gov_record.py` is tr2 S1's record door, and gains a `door` verb | cite | AGREES | wm58:40-41 · tr2:39-43 |
| 58 | `record-kinds.toml` is tr1's registry, and a `[[record-kind]]` row registers a kind | cite | AGREES | wm58:101-102 · tr1:62-67 |
| 58 | The door can read the build lease's holder (session) | cite | MISMATCH | wm58:72-74, :91, :106 · tr2:189-196, :335-345 |
| 58 | `quiesce` is a new kind written by `gov_record.py new quiesce`, with no typed join | R2 | MISMATCH | wm58:101-104, :212 · oc42:35-39, :45-50 · tr2:52 · tr1:67-73 |
| 58 | The door reads the binding through a `session_binding.py read` subprocess, and `GOVREF_DOOR` is resolved through `resolve_kit_dir` | R3 | AGREES | wm58:42-45, :55-56 |

##### 2. MISMATCHes

- **wm34, `record find` row cap.** wm34:41-43 "gathers, in one query: the records naming the key ... through `record find`" and :59 "every row under `all`". tr9:94-96 "At most 40 rows, one per record, ... no content ... past 40, the last line reads `<total> rows match; narrow with ...`".
  Change: S2 should state that a key named by more than 40 records reaches past `record find`'s cap. Either it filters (`--tag`/`--paths`) and re-queries until the total line is gone, or it files an ask to dTotalRecall for an uncapped `find` mode. `all` cannot be promised otherwise.
  Cause: pre-existing.
- **wm34, runlog function in the runtime kit.** wm34:47-48 "resolved on this node by `resolve_session_tree` (`tools/runlog/extract.py:266`)", from `tools/runtime/trace.py`. oc7:202-205 "A kit may not import a sibling kit". wm34's own F1 also rejects "the runtime kit importing runlog".
  Change: carry the resolver inline under a parity row, as S4 does for `timeline_py`, or run a runlog verb by subprocess.
  Cause: pre-existing.
- **wm39, hand-written leg.** wm39:83 "the leg `runtime bindings fixtures` in `tools/gate-legs.json` runs every case". Files touched lists `tools/gate-legs.json` with no declaration. wb11:36-38 "Each leg is declared exactly once: a `[[gate_leg]]` row in its kit's descriptor ... else an `[[exempt_leg]]` row". oc7 S3 "a leg carrying no `enforces` is red", and the pending list only shrinks (oc7:58-63).
  Change: declare the leg as a `[[gate_leg]]` row of `tools/runtime/kit.toml` with every manifest key and a named `enforces`, render it with `leg_factory.py --write`, and add `--check` to an AC.
  Cause: pre-existing.
- **wm39, F4 ask to tr19.** wm39:271-273 "for TOOL-dTotalRecall-19 S8's `check_causes` to grade act-made commits through `bindings.py --check` over its range; accept line: `check_causes` over a commit whose `Gov-Act:` ...". tr19:90-92 "`check_causes(root)` ...: a tracked record ... red when it carries no `Caused-by` or one that does not resolve". It grades records, not commits, and has no range.
  Change: restate the ask against tr19's population. For example: a record whose `Made-by`/`Caused-by` names an act whose binding `refs/gov/bindings` lacks reads `not-local` and never passes, read through a `bindings.py --read` subprocess.
  Cause: pre-existing.
- **wm42, new reader of `.claude/roles.json`.** wm42:43-46 lists by value only `render_agents.py`, `handoff.py roster`, `agent-cap.js` and `scratch-guard.js` as readers of `.claude/roles.json`. br1 rev-3 F6: "Each role's slot and `layer` are read as JSON data from `.claude/roles.json`" by `check_layer_roles` (`tools/playbook/check_layers.py`).
  Change: add `check_layer_roles` to S1's by-value readers, stating that dropping `gov-session`'s row leaves its item arm unchanged because no item's actor names that role.
  Cause: re-ground.
- **wm43, `fan` versus `cap`.** wm43:47-48 "a `Workflow` call asks for its harness's declared fan, the largest stage `fan`". br22:108-109: `fan` is "the most agents the stage spawns in one call", and `cap` is "the most of them in flight at once".
  Change: reserve the largest stage `cap`, which is what the in-flight ledger counts, or state why `fan` is used. wm45 S3 follows the same way.
  Cause: pre-existing.
- **wm43, no admitted read of the stage rows.** wm43:47-48 reads the stages of "the workflow whose `harness` is its `scriptPath`" from the runtime kit. br22:38-44 makes `load_workflows` (`roles_lib.py`) "one reader of the rows", returning the composition. The runtime kit may not import it, and no roles verb prints stage `fan`/`cap` (`handoff.py harness-args` prints only `{key: role}`).
  Change: name the read. Either file an ask to dBoundRoles for a roles-kit verb printing each stage's `fan`/`cap` for a harness, run by subprocess through `resolve_kit_dir`, or reserve the limit until that verb exists.
  Cause: pre-existing.
- **wm43, `handoff.py` and process-monitor in process.** wm43:67 "`load_run_journal`, `tools/roles/handoff.py:686`", :76-77 "`load_session_calls` and `NOTIFICATION_RE` (`tools/roles/handoff.py:576`, `:125`)", :82-83 "`scan_processes` and `build_self_chain` (`tools/process-monitor/census.py:260`, `scope.py:254`)", all called from `tools/runtime/inflight.py`. oc7:202-205 "A kit may not import a sibling kit".
  Change: reach them through roles-kit and process-monitor verbs by subprocess, carry them inline under parity rows, or declare `requires_if` rows on `tools/runtime/kit.toml`.
  Cause: pre-existing.
- **wm44, `record find` appending rows.** wm44:79-80 "`record find --build <slug>` (its S3) appends, after its local rows, a row per mirror record". tr9:207-209 "The total line is the only line past the rows, so a reader that counts lines counts rows plus one at most". The 40-row cap is at tr9:94-96.
  Change: mirror rows must count inside the 40-row cap, with the total line kept last. Otherwise the change has to be filed as an ask to tr9, because it changes the output contract tr9 states.
  Cause: pre-existing.
- **wm44, `read_mirrored` from memory-tree.** wm44:71 "through `read_mirrored(kind, key, repo)` in `mirror.py` and its CLI". `record_find.py` is in memory-tree (Files touched), and :92's census counts in-process `read_mirrored` calls as legal readers. oc7:202-205.
  Change: `record_find.py` runs `mirror.py get|scan` by subprocess through an inline `resolve_kit_dir`, and `read_mirrored` is called only inside the runtime kit.
  Cause: pre-existing.
- **wm44, `memory.mirror` through `resolve`.** wm44:48 "Read through `resolve` (I31)". oc7:379-380 "The policy keys are read through the policy kit's `get` verb ... as a subprocess".
  Change: read `memory.mirror` through a `policy.py get` subprocess, as wm34 and wm51 do.
  Cause: pre-existing.
- **wm45, the declared fan.** wm45:57-58 "its declared fan (TOOL-dBoundRoles-22 S1, as TOOL-dWellOiledMachine-43 S2 reads it)". It inherits both wm43 MISMATCHes, `fan` versus `cap` and no admitted read.
  Change: follow wm43's fix.
  Cause: pre-existing.
- **wm45, limit through `resolve`.** wm45:132 `limit = resolve("runtime.agents-in-flight")` in `tools/runtime/admission.py`. oc7:379-380.
  Change: read the limit through a `policy.py get` subprocess.
  Cause: pre-existing.
- **wm48, `owner-question` can now refuse.** wm48:54-55 "raises an item through S1 for every answer but `resolve`". br11:63-65 "A `get` exit 2, or no policy kit found, refuses naming the key and the reader's line or the kit." That text was added in rev-3.
  Change: S2 must say that a refusal from `owner-question` (non-zero exit) raises nothing and that `ask` exits 2 with the refusal line, and add an AC case for it.
  Cause: re-ground.
- **wm48, run keys through `resolve`.** wm48:60-61 "`read_catalogue_row` (`tools/policy/policy.py:219`) ... through `resolve` (`:752`)", and :71 and :93 "read through `resolve`", all in `tools/runtime/owner_items.py`. oc7:379-380.
  Change: read the keys with a `policy.py get` subprocess, and get the row's `direction` from a policy verb, for example `get --explain`, or from an ask to the policy kit.
  Cause: pre-existing.
- **wm51, act records through `record find`.** wm51:38-40 "sums `Tokens-In` plus `Tokens-Out`, and `Wall`, over the build's act records ... read through `record find`". tr9:94-96 "At most 40 rows ... `key · kind · build · bytes · path:line`, no content".
  Change: enumerate the acts with `record find --kind act --build <slug>`, handling past 40 as in the wm34 fix, and read each act's fields through `record show`. Without that, a build with more than 40 acts under-counts its spend.
  Cause: pre-existing.
- **wm53, `Wall` by item kind.** wm53:62-65 "the nearest-rank p90 of the `Wall` field of the act records whose `Item` is that item kind ... read through ... `record find`". tr9:89-90 lists `record find`'s filters as `--kind`, `--tag`, `--build` and `--paths` only, and :94-96 caps it at 40 rows with no content.
  Change: name the read. Either `find --kind act` paged, then `record show` per act with the `Item` filter applied in `ledgers.py`, or an ask to dTotalRecall for a field filter.
  Cause: pre-existing.
- **wm53, `resolve` in the runtime kit.** wm53:65 and :71 "read through `resolve`" in `tools/runtime/ledgers.py`. oc7:379-380.
  Change: read both keys through a `policy.py get` subprocess.
  Cause: pre-existing.
- **wm54, model answer from the landed revision.** wm54:77-82 `check_role_models` runs "over the effective assignment" and asks `python roles_lib.py model <role> <harness>`. br21:41-44: `read_policy_setting` runs `policy.py get`, and "`get` reads the landed revision". So the answer reflects the landed policy, not the file being checked; AC6's planted `roles.model.gov-builder.codex` is invisible to it unless committed.
  Change: read `roles.model.<role>.<harness>` from the assignment itself, and ask the roles kit only for the adapter equivalent, through a CLI mode that skips the policy read.
  Cause: pre-existing (br21 rev-2 already read "at one landed revision").
- **wm54, `--claims` fields.** wm54:31-33 reads leases through `--claims`, and S1/S3 then need each lease's `status`, released-as-hand-over state and `offer` (:63). pr1:206-208 "`print_claims` still prints fields 1 to 5", which the code confirms: `cut -f1-5` at `unattended.sh:2202`, fields `slug, node, status, beat-age-s, verdict`. `offer` and `kind` are not among them.
  Change: read the lease fields through a dPlacedRequest verb over `read_claims` that prints them (the same ask as tr2 F6), not `--claims`.
  Cause: pre-existing.
- **wm54, sibling kits in `discover.py`.** wm54:33-34 calls memory-tree's `collect` (`gen_build_index.py:1106`), and :44-46 calls `load_workflows`, `resolve_role_harness` and `resolve_role_model` in `roles_lib.py`, all from `tools/runtime/discover.py`. oc7:202-205.
  Change: reach these through verbs by subprocess, as S6 already does with `roles_lib.py model`. For example the build index's CLI output, and a roles verb printing a unit's needed roles, harnesses and models.
  Cause: pre-existing.
- **wm56, typed catalogue defaults.** wm56:38-39 "else `read_policy_setting("runtime.act-harness", root)`, else the catalogue default `claude-code`", and :43-44 "else its default `setup-token, oauth-shared`". br21:46-47 makes `with_default` "the form a read with a catalogue default takes", and without it None also means no policy kit.
  Change: read the two `runtime.*` keys with `with_default=True` and delete the typed defaults. Keep the per-role read without `with_default`, because S3's `own` needs its source.
  Cause: re-ground (`with_default` arrived in br21 rev-3).
- **wm56, `launch_act` into `roles_lib.py`.** wm56:53-56: `launch_act` (`tools/runtime/launch.py`) "takes the first harness S1 returns" and calls `derive_credential_target` and `check_credential_role` in `roles_lib.py`. oc7:202-205.
  Change: expose S1-S3 as a `roles_lib.py` CLI, as wm54 S6 does, and run it by subprocess from `launch.py`.
  Cause: pre-existing.
- **wm58, lease-holder read.** wm58:72-74 "the writer holds the build lease `refs/gov/leases/<slug>/build` (live, naming the writer)", judged inside `gov_record.py door`. tr2:191-194 "`unattended.sh --claims` cannot serve: it prints fields 1 to 5, no session among them", and tr2 F6 (:335-345) leaves the holder read open as an ask to dPlacedRequest, rejecting (c) "the door parses the lease commit's `session:` key itself".
  Change: route S4(c) and S5's holder test through the same holder verb tr2 F6 asks for, and record that wm58 waits on F6's pick.
  Cause: re-ground.
- **wm58, `quiesce` kind not joined.** wm58:101-104 adds `record-kind.quiesce`, "written by `gov_record.py new quiesce`", and touches only `record-kinds.toml`. tr2:52 renders "`**Serves:** <kind> <ids>`". oc42:35-39 lets a Serves line bind only for `RECORD_KIND_TOKENS` (the four untyped kinds plus `TYPED_RECORD_KINDS`). oc42:45-50 reads a misnamed or mis-served typed record as malformed.
  Change: join `quiesce` to `TYPED_RECORD_KINDS`, the factory's per-kind table and HYGIENE's closed list (tr25 S6's pattern), with a `-quiesce-<n>.md` file name and its writer cell spelled as tr1 §4 requires. Or serve it as an existing untyped kind and say so.
  Cause: pre-existing.

##### 3. UNKNOWN UNTIL BUILT

- **wm54, stream-plan read.** How `pick`/`discover` reads the stream-plan record and its fence is undecided. tr25 S5 says none exists until dIndexedDesign's planner writes one, and tr25 S6 makes it typed. It is decided when the planner lands and wm54's build picks a read, for example `record find --kind stream-plan`, then `record show` and the fence.

##### 4. Rule-wide hits the rule does not bind

None: A2 is a citation group, so there were no probe hits to verify. Two terms that look like rule triggers do not bind:
- `budget` in wm51 means dDeclaredLoop's rework budget, not dl33's edges.
- `budget-ms` in wm43 and wm45 is a hook pack's timeout, not dl33's edges.

##### 5. Cited revised units no assumption depends on

- 34 (tr9): none
- 39 (tr19): none
- 42 (br1): none
- 43 (br22, br25): none
- 44 (tr9): none
- 45 (br22): none
- 48 (br11): none
- 51 (tr9): none
- 53 (tr9): none
- 54 (br2, br21, tr25): none
- 56 (br21): none
- 58 (tr1, tr2): none

## Group B1

I checked the 22 specs of group B1 (1, 2, 5, 6, 10, 12, 13, 14, 15, 17, 20, 21, 22, 23, 24, 25, 26, 28, 29, 31, 33, 36) against R1 to R9. Every probe only read files, and I ran no gate.

The rule texts did not move in either re-ground: `git diff ab864dfc8 d1721ef20 --stat` over oc7, oc42, wb11, pr1, ks8 and every dDeclaredLoop spec prints nothing. So every mismatch below was already there at `ab864dfc8`.

Most of the R3 mismatches have one root cause. The spec brief's I31 (`prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md:228`) names the in-process readers as the policy readers: Python `resolve(key)` (`policy.py:752`) and JS `readPolicy` (`policy-mirror.js:132`). oc7 and ks8 say a sibling kit runs the `get` verb as a subprocess (oc7:202-205, :379-380; ks8:62-66). 23 specs cite I31, so fixing I31 fixes the class.

Rows marked "(not a probe hit)" are R3 or R8 breaks I found while reading specs of this group that the probe did not name for that rule. They are flagged so you can drop them if you want to keep strictly to the brief.

The brief's R8 summary cites the wrong sections. The witness channel set is dl3 S4 (dl3:54-59), not dl3 S2, which is the log channel. The contention rule is dl30 S5 (dl30:58), not dl33 S3, which is rule `reachable` (dl33:48). Where the two differ, I judged by the parent text.

#### 1. Table

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| wm1 | The `runtime selftest` leg is added to `tools/gate-legs.json` by hand, with no `enforces` | R1 | MISMATCH | wm1:207, :229; wb11:36-49, :154; oc7:58-63 |
| wm1 | S3: `launch_act` reads `runtime.spawn-backend` through the policy kit's `resolve`, loaded as `load_tree_lib` loads its sibling | R3 | MISMATCH | wm1:64-66, :165, :355-357; oc7:202-205, :379-380; `tools/policy/check_policy.py:879-887` (does `sys.path.insert` then `import tree_lib`) |
| wm1 | S7: the policy kit's `check_policy.py` loads the runtime kit's `build_headless_argv` through `resolve_kit_dir`, in process | R3 | MISMATCH | wm1:107-110, :322-329; oc7:202-205 |
| wm2 | S8: the `runtime next tails` leg is added to `tools/gate-legs.json` by hand, with no `enforces` | R1 | MISMATCH | wm2:70-72, :149, :243; wb11:36-49; oc7:58-63 |
| wm2 | S1 and S6: `next.py` calls the loop kit's `derive_position` and the policy kit's `check_shrink_list`/`write_shrink_list` (not a probe hit) | R3 | MISMATCH | wm2:34-35, :60-63; dl7:31 (`tools/loop/position.py`); ks19:30 (`tools/policy/policy.py`); oc7:202-205 |
| wm5 | S2: `derive_witness_adapter` reads `runtime.owner-harness` through `resolve(key, repo, rev)` in process | R3 | MISMATCH | wm5:38-40, :217-218; oc7:379-380 |
| wm5 | S3 to S5: `ratify.py` calls `check_owner_disposition`; the loop kit's `breakpoints.py` "reads S3"; the loop kit's `placement.py` reads through `read_build_disposition` | R3 | MISMATCH | wm5:41-64, :123 (verbs `check`, `fixture` only); dl31:60-63 (`check_owner_disposition` is a bash function of the unattended driver); oc7:202-205 |
| wm5 | S5: the disposition lines are read from the build's claim commit, not from `--claims` | R8 | AGREES | wm5:57-64; pr21:45-49 (`refs/gov/claims/<slug>`) |
| wm6 | S2: the lease's fleet tag and live/held status are read through `unattended.sh --claims` | R8 | AGREES | wm6:46-48; pr1:203-208; `tools/unattended/unattended.sh:2204` (`cut -f1-5`; fields slug, node, status, …) |
| wm6 | S6 and S7: the lease's epoch is read through `unattended.sh --claims` | R8 | MISMATCH | wm6:85-89, :92-96; pr1:203-208 |
| wm6 | S5: `runtime.relaunch` is read through `resolve` (`policy.py:752`) (not a probe hit) | R3 | MISMATCH | wm6:77-78; oc7:379-380 |
| wm10 | S5: settings-merge reads `runtime.hook-failure` by running `python <prefix>/policy/policy.py get` | R3 | AGREES | wm10:73-74; oc7:379-380 |
| wm10 | S6 and S8: `dispatch.js` reads `runtime.hook-failure` (and the judge keys) through `readPolicy(…, {repo})` in process | R3 | MISMATCH | wm10:75-80, :88-95; ks8:62-66 |
| wm12 | S11: the `runtime session-binding fixtures` leg is added to `tools/gate-legs.json` by hand, with no `enforces` | R1 | MISMATCH | wm12:101-104, :205, :219; wb11:36-49; oc7:58-63 |
| wm13 | S6: a run lease's `landed` status (field 3) and its name `run/<cadence>/<period>` (field 1) are read through `--claims` | R8 | AGREES | wm13:58-62; pr1:203-205 |
| wm15 | S3: `run.host` is read through `resolve("run.host")` in process | R3 | MISMATCH | wm15:45-46; oc7:379-380 |
| wm15 | S5: `clock-offset` becomes "a twelfth `CLAIM_ROWS` column" (not a probe hit) | R8 | MISMATCH | wm15:60-66; pr1:203-208 |
| wm17 | S3 and S4: `runtime.secret-scan` and `runtime.secret-home` are read through `resolve` (`policy.py:752`) in process | R3 | MISMATCH | wm17:49-51, :55-56; oc7:379-380 |
| wm17 | S1 and S6: `scan_secrets` is called inside the runtime kit, where TOOL-dWellOiledMachine-16 moves it | R3 | AGREES | wm17:63-65, :119-120 |
| wm20 | The `runtime points registry` leg is added to `tools/gate-legs.json` by hand, with no `enforces` | R1 | MISMATCH | wm20:172, :182; wb11:36-49; oc7:58-63 |
| wm22 | S5: the purpose-review record is served as `research`, an untyped kind, in a file not named `-<kind>-<n>.md` | R2 | AGREES | wm22:56-58; `tools/memory-tree/tree_lib.py:406`; oc42:45-50 |
| wm23 | The `runtime hook-cap fixtures` leg is added to `tools/gate-legs.json` by hand, with no `enforces` | R1 | MISMATCH | wm23:71, :130, :139; wb11:36-49; oc7:58-63 |
| wm24 | S2: `memory.project-map` is read through `resolve`, and the roles kit's `load_roles` is called in process (not a probe hit) | R3 | MISMATCH | wm24:44-47; oc7:202-205, :379-380 |
| wm25 | S4: `runtime.act-harness` is read through `resolve` (I31) (not a probe hit) | R3 | MISMATCH | wm25:57-58; oc7:379-380 |
| wm26 | S2 to S4: `step.py` calls the roles kit's `extract_microformat_shapes`/`render_shape_line` and the loop kit's `derive_position`, `resolve_item_declaration` and `read_attendance` in process (not a probe hit) | R3 | MISMATCH | wm26:39-57; ks17:45, :137 (`tools/loop/loop_lib.py`); dl7:31; oc7:202-205 |
| wm33 | S8: the `commit keys name their act` leg is a `[[gate_leg]]` row of `tools/runtime/kit.toml` and is also written into `tools/gate-legs.json`, with no `enforces` | R1 | MISMATCH | wm33:85-91; wb11:36-49, :154; oc7:58-63 |
| wm33 | S5: `trace.identity` is read by running `policy.py get` as a subprocess | R3 | AGREES | wm33:58-59; oc7:379-380 |
| wm36 | S5: `runtime.binary` is read through `resolve` (I31) (not a probe hit) | R3 | MISMATCH | wm36:68-69; oc7:379-380 |

#### 2. MISMATCHes

**R1, a leg hand-added to the manifest (wm1, wm2, wm12, wm20, wm23)**
- Spec side:
  - wm1:207 `| \`runtime selftest\` | gate leg | \`tools/gate-legs.json\` |`
  - wm2:70 "The leg `runtime next tails` in `tools/gate-legs.json`"
  - wm12:103-104 "the leg `runtime session-binding fixtures` in `tools/gate-legs.json`"
  - wm20:182 "`tools/gate-legs.json` — the `runtime points registry` leg"
  - wm23:71 "the leg `runtime hook-cap fixtures` in `tools/gate-legs.json`"
  - None of the five names an `enforces` (`grep -c "enforces\|gate_leg\|exempt_leg\|leg_factory"` prints 0 for each).
- Parent side:
  - wb11:36-38: "Each leg is declared exactly once: a `[[gate_leg]]` row in its kit's descriptor when an adopter receives it, else an `[[exempt_leg]]` row in `tools/govkit/registry.toml`"
  - wb11 S2: "`--write` renders `tools/gate-legs.json` from every declaration"
  - oc7:61: "a leg carrying no `enforces` is red"
- Change: declare each leg as a `[[gate_leg]]` row of `tools/runtime/kit.toml`, or as an `[[exempt_leg]]` row if it is gov-only, through `leg_factory.py new`, with `enforces` naming the principle or practice tags it enforces. Render the manifest with `leg_factory.py --write`, and drop the hand edit of `tools/gate-legs.json` from S8, S11, §4 and the Files touched.
- Cause: pre-existing.

**R1, wm33's leg declared twice**
- Spec side: wm33:89-90 "a new manifest leg, `commit keys name their act`, in `tools/gate-legs.json` and as a `[[gate_leg]]` row of `tools/runtime/kit.toml`".
- Parent side: wb11:38-39 "A declaration holds every manifest key its leg carries: … `enforces` …"; wb11 S2 says the manifest is a render; oc7:61.
- Change: keep the `[[gate_leg]]` row and give it `enforces`. The manifest line comes from `leg_factory.py --write`, not a hand edit.
- Cause: pre-existing.

**R3, wm1 S3 and S7**
- Spec side:
  - wm1:64-66 "`launch_act` reads `runtime.spawn-backend` through the policy kit's `resolve` (`tools/policy/policy.py:752`, reached by `resolve_kit_dir` as `load_tree_lib` reaches its sibling…)"
  - wm1:107-109 "`run_live_session` … builds its argv with `build_headless_argv(…)` … reached through `resolve_kit_dir("runtime", "launch.py", kit)`"
  - `load_tree_lib` (check_policy.py:884-887) does `sys.path.insert(0, lib)` then `import tree_lib`.
- Parent side: oc7:202-205 "A kit may not import a sibling kit … so the module carries the inline `resolve_kit_dir` block, finds `policy.py` with it, and runs `<sys.executable> <kit>/policy.py get <key>`"; oc7:379-380.
- Change:
  - S3 runs `policy.py get runtime.spawn-backend` as a subprocess, and takes the refusal from `get`'s exit 2 rather than calling `check_value` in process.
  - S7 needs a `launch.py` verb that prints the argv for `run_live_session` to run, or a declared `requires_if` row admitting the import.
  - F1's "needs no `requires` change" must be revisited.
- Cause: pre-existing.

**R3, wm2 S1 and S6**
- Spec side: wm2:34 "it calls `derive_position(repo, slug)`"; wm2:61 "`check_shrink_list("runtime", "next-laggards.txt", derived, compare)`".
- Parent side: these live in `tools/loop/position.py` (dl7:31) and `tools/policy/policy.py` (ks19:30). oc7:202-205 says a kit may not import a sibling kit.
- Change: reach the engine through `position.py <slug> --json` as a subprocess. Reach the shrink-list factory through a policy-kit verb as a subprocess, or file an ask for one.
- Cause: pre-existing.

**R3, wm5 S2 to S5**
- Spec side:
  - wm5:39-40 "`runtime.owner-harness` resolved at the witness's commit through `resolve(key, repo, rev)`"
  - wm5:46 "read through `check_owner_disposition`"
  - wm5:51-52 "The plan gate's release in `tools/loop/breakpoints.py` … reads S3"
  - wm5:62-63 "`placement.py record` … read the disposition through it" (`read_build_disposition`, which has no verb: wm5:123 lists only `check` and `fixture`)
- Parent side:
  - oc7:379-380 says policy keys go through `get` as a subprocess, and oc7:202-205 says no kit imports a sibling.
  - dl31:62 makes `check_owner_disposition <run-state file> <decision row>` a bash function. The spec cites it as TOOL-dDeclaredLoop-16 S4, but `grep -l check_owner_disposition` over the dDeclaredLoop specs names dl19, dl31, dl53 and dl56, not dl16.
- Change:
  - S2 runs `policy.py get runtime.owner-harness --rev <C>` as a subprocess.
  - S3 reaches dl31's check through a command.
  - S4 runs `ratify.py check` as a subprocess, found through `resolve_kit_dir`.
  - S5 gains a `ratify.py` verb printing the disposition lines for `placement.py` to run.
- Cause: pre-existing.

**R8, wm6 S6 and S7**
- Spec side: wm6:92-94 "Each beat re-reads the build lease from the remote through `unattended.sh --claims`; a lease whose epoch moved past the one S1 was started with"; wm6:88 says an act is adopted when its "`epoch` is the lease's current epoch".
- Parent side: pr1:207-208 says "`print_claims` still prints fields 1 to 5 (`:2204`)". `epoch` is field 12 (pr1:205-206), and source `unattended.sh:2204` reads `cut -f1-5`.
- Change: read the epoch through a reader that prints it. The `--lease` verbs print `epoch <n>` (pr1:86); otherwise file an ask to dPlacedRequest for a read verb. Keep `--claims` for the status and fleet tag alone.
- Cause: pre-existing.

**R3, wm6 S5; wm15 S3; wm17 S3 and S4; wm24 S2; wm25 S4; wm36 S5 (in-process `resolve`)**
- Spec side:
  - wm6:77-78 "`runtime.relaunch` … read through `resolve` (`tools/policy/policy.py:752`)"
  - wm15:46 "read through `resolve("run.host")`"
  - wm17:50 "through `resolve("runtime.secret-scan")`" and :56 "read through `resolve`"
  - wm24:45-46 "read through `resolve` (I31, `tools/policy/policy.py:752`), `roles` the roles kit's `load_roles`"
  - wm25:58 "`runtime.act-harness` … through `resolve` (I31)"
  - wm36:69 "read through `resolve` (I31)"
- Parent side: oc7:379-380 "The policy keys are read through the policy kit's `get` verb … as a subprocess, the one seam a sibling kit may reach"; oc7:202-205.
- Change:
  - Read each key by running `policy.py get <key>` as a subprocess, found through the inlined `resolve_kit_dir`, behind one runtime-kit helper as oc7 rules for the playbook kit. wm5's at-a-revision read passes `--rev`.
  - wm24 reads roles through a roles-kit verb instead of `load_roles`.
  - Better still, fix I31 in the brief once.
- Cause: pre-existing.

**R3, wm10 S6 and S8**
- Spec side: wm10:79 "The value is read once per run through `readPolicy("runtime.hook-failure", {repo})` (I31)".
- Parent side: ks8:62-66 "running dGroundRules' JS reader's own CLI as a subprocess, `node <policy kit>/policy-mirror.js get actions.free --repo <repo>` … A kit imports no sibling kit … so the hook never `require`s the policy kit's module."
- Change: `dispatch.js` spawns `node <policy kit>/policy-mirror.js get runtime.hook-failure --repo <repo>` (and the same for `runtime.attended-judge` and `runtime.attended-allowance`) under a bounded timeout. It locates the file through the `resolvePolicyHelper` that `scratch-guard.js` exports.
- Cause: pre-existing.

**R8, wm15 S5**
- Spec side: wm15:61-62 "the reader also carries the renewing beat's `clock-offset` as a twelfth `CLAIM_ROWS` column".
- Parent side: pr1:203-207 "`CLAIM_ROWS` grows from eleven TAB fields to eighteen: the eleven …, then `epoch`, `kind`, `renews`, `witness`, `offer`, `offer-deadline` and `last-fetch`." Column 12 is `epoch`.
- Change: append `clock-offset` as field 19, after `last-fetch`, and say that `--claims`' fields 1 to 5 are unchanged.
- Cause: pre-existing.

**R3, wm26 S2 to S4**
- Spec side: wm26:44-46 "`extract_microformat_shapes` (`tools/roles/roles_lib.py:252`) and filled by `render_shape_line` (`tools/roles/handoff.py:708`)"; wm26:43 "`resolve_item_declaration`"; wm26:50 "it calls `derive_position(repo, slug)`"; wm26:56 "`read_attendance(value)`" (`tools/loop/loop_lib.py`, ks17:137).
- Parent side: oc7:202-205; TOOL-dGroundRules-1 §4.
- Change: reach each through its kit's command as a subprocess: `position.py --json`, a `loop_lib.py` declaration/attendance verb, and a roles-kit shape-render verb. Where a verb does not exist, file an ask, or declare a `requires_if` row.
- Cause: pre-existing.

#### 3. UNKNOWN UNTIL BUILT

None in this group.

#### 4. Rule-wide hits the rule does not bind

- **wm1 R8:** "budget" is `tools/run-gates/selftest-budgets.txt` (wm1:229), not dl30's rework budget.
- **wm1 R9:** the reader is in the runtime kit, not the roles kit, so R3 judges it (row 2).
- **wm2 R8:** "reads witnesses through the engine" (wm2:192) defines no witness channel.
- **wm5 R8:** "witness" is the ratification witness, a record read, not a dl3 S4 transition channel. Its claim-commit read is in the table as AGREES.
- **wm6 R8 (part):** `commit-witness.log` (wm6:72-74) and the non-goal's "budget draw" (wm6:132) are neither dl3's channels nor dl30's budget. The `--claims` reads are in the table.
- **wm10 R8:** `witnesses.toml` rows and `budget-ms` are the pack contract's own, not dl3's or dl30's.
- **wm10 R9:** runtime kit, not the roles kit. Its reads are R3 rows.
- **wm12 R4:** "what returns" and "a route naming a build" (wm12:75) are prose; no loop item row is added.
- **wm12 R8:** `refs/gov/checkpoints/<sid>/<n>` (wm12:80) is a never-pushed local ref, not a claims read.
- **wm14 R9:** the only roles-kit change is `adopt-roles.sh` reading `GOV_SKILL_HOME` with a `.claude/skills` fallback (wm14:84-86), which is not a policy-key read. `runtime.harnesses` goes through `policy.py get` (wm14:75), as R3 asks.
- **wm17 R1:** "enforces" at wm17:26 is prose. §7 adds arms only, no leg.
- **wm17 R8:** the S9 "witness" line and "claims today through `write_claim`" (wm17:74) read no claim.
- **wm20 R4:** `layers.toml` `declares` words seed point rows (wm20:65). No loop item, input or `returns` row.
- **wm21 R8:** "budget" is a template unit's `line`/`block` budget (wm21:48).
- **wm22 R4:** `layers.toml` appears only in a point row's `contract` string.
- **wm23 R8:** the "hook channel" cap and the map's `32k` budget (wm23:77, :99-103) are neither dl3's nor dl30's.
- **wm24 R8:** `budget-ms` 3000 (wm24:35).
- **wm25 R8:** "a hook's witness arrives with its event" (wm25:85) is an item witness, not a transition channel.
- **wm26 R6:** "never composed from a guess" (wm26:47) is not the overlay composition.
- **wm28 R8:** the `selftest-budgets.txt` rows and govkit's step verb `witness` (wm28:147-149, :169).
- **wm29 R8:** the DOM and console "witness" of a visual check (wm29:150).
- **wm31 R1:** "one object per rule the pack enforces" (wm31:33) is prose; §7 adds arms only.
- **wm31 R7:** `tools/policy/guard.py:41` `REMEDY` is dGroundRules' policy guard, not dl2's `tools/loop/guard.py`.
- **wm31 R8:** `budget-ms` (wm31:102).
- **wm33 R9:** runtime kit, not the roles kit. Its read uses R3's subprocess form (AGREES row).
- **wm36 R6:** "composed from Codex's documented event shapes" (wm36:59) is not the overlay composition.

#### 5. Citation specs: revised parent units cited but not depended on

None. Group B1 is a rule-wide group with no citation specs.

Files:
- `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/` (the specs reviewed)
- `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md` (line 228, I31)
- `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/tools/policy/check_policy.py` (lines 879-887)
- `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/tools/unattended/unattended.sh` (line 2204)

## Group B2

#### Cross-check of group B2 (rule-wide, led by spec 38) against R1 to R9 at `d1721ef20`

Every parent spec these verdicts rest on is unchanged between `ab864dfc8` and `d1721ef20`: wb11, oc7, oc42, pr1, dl12, dl16 and dl30. The probe was `git diff --stat ab864dfc8 d1721ef20 -- <spec>`, which printed nothing for each, and `git cat-file -e ab864dfc8:<spec>` shows each existed at the base. So every MISMATCH below is **pre-existing**.

None of the rules R1 to R9 binds spec 38, the group's lead. I give it one R3 row, outside the probe's hits.

Three things the brief's rule summary says differ from the parent text, so the parents were used instead:
- R8's channel rule is dl3 S4, not S2.
- "Contention draws nothing" is dl30 S5, not dl33 S3.
- pr1 S4 says `read_claims` fetches `refs/gov/leases/*` **and** the legacy `refs/gov/runs/*`.

Several R3 rows are marked "outside the hits". These are cross-kit calls I found while reading a hit spec that the probe did not flag for R3.

**Totals: 23 rows, 14 AGREES, 9 MISMATCH, 0 UNKNOWN UNTIL BUILT.**

##### 1. Table

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 38 | The kickoff kit's code reaches the runtime kit's `session_binding.py` only through its command-line verbs (`read <sid> --card`, `put-card`). `scratch-guard.js` reads the binding as file text and imports no runtime code. (Outside the hits.) | R3 | AGREES | wm38:36-38, :49-53, :131-132; oc7:202-205 |
| 40 | `build.push` is read by running `policy.py get` as a subprocess from the runtime kit | R3 | AGREES | wm40:32-35; oc7:379-380 |
| 41 | `build.unit-holders` is read by running `policy.py get` as a subprocess | R3 | AGREES | wm41:32-37; oc7:379-380 |
| 41 | The offer verb learns whether this session holds the build lease by reading `unattended.sh --claims` | R8 | MISMATCH | wm41:39-43; pr1:207-208; tools/unattended/unattended.sh:2113-2114, :2204 |
| 46 | A stuck item's route draws `route-back` at the transition writer, or `re-dispatch` from `planning`/`designing`. Neither is contention. | R8 | AGREES | wm46:75-81; dl30:43-50, :52-57, :58-61 |
| 46 | AC5 reads the lease as `stale` through `--claims` (the verdict is field 5) | R8 | AGREES | wm46:213-215; pr1:207-208 |
| 46 | `runtime.no-progress` is read through the policy kit's `resolve` inside `progress.py` (outside the hits) | R3 | MISMATCH | wm46:52-53; oc7:202-205, :379-380 |
| 46 | `progress.py` calls the loop kit's `write_transition` and `record_draw` as functions (outside the hits) | R3 | MISMATCH | wm46:75-80, :118; dl3:60-61; dl30:43, :139; oc7:202-205 |
| 47 | The hold ceiling is read through `resolve` (`policy.py:752`) inside `supervise.py` | R3 | MISMATCH | wm47:40-43; oc7:379-380 |
| 47 | Restarts are read through `policy-shim.sh get`, and an act is killed through `reap.py --kill`, both as subprocesses | R3 | AGREES | wm47:64-68, :83-86; oc7:202-205 |
| 47 | This node's leases are picked by `fleet-tag` from `--claims` (field 2) | R8 | AGREES | wm47:47-50; pr1:204-208 |
| 49 | `runtime.refusal-repeats` is read by running `policy.py get` as a subprocess | R3 | AGREES | wm49:30-35; oc7:379-380 |
| 49 | When the breaker opens, the draw is `budget.py draw --cause re-dispatch` through br26's door (ask F3). The cause is in the closed set and is not contention. | R8 | AGREES | wm49:76-80, :305-311; dl30:43-50, :58-61 |
| 55 | `policy.py`'s `check_value` reads the runtime kit's `points.toml` as TOML data, finds it through its own inline `resolve_kit_dir`, and never imports it | R3 | AGREES | wm55:82-89; oc7:202-205 |
| 57 | `gov_record.py` (memory-tree) runs `secret_scan.py payload` as a subprocess found by `resolve_kit_dir`. `scan_secrets` is imported only inside the runtime kit. | R3 | AGREES | wm57:32-36, :41-44; oc7:202-205 |
| 59 | `cadence.py` reads each host key and `flow.on-exhausted` through `resolve` | R3 | MISMATCH | wm59:47-49, :65-66; oc7:379-380 |
| 59 | `cadence.py` calls the loop kit's `derive_ending`, `budget_state` and `derive_period_budget` in process | R3 | MISMATCH | wm59:51-52, :55-63, :65-66; dl31:40, :150; dl30:222, :235; oc7:202-205 |
| 59 | A period's spend counts every `released` record: each failed lap is one draw, with no contention exclusion | R8 | MISMATCH | wm59:55-62; dl30:58-61 |
| 64 | The moved hooks load their renderer from their own kit by `__dirname`; loading it from the sibling unattended kit was rejected | R3 | AGREES | wm64:30-35, :95-96 |
| 79 | S13, S29 and S40 change, delete and "claim" the runtime legs by hand in `tools/gate-legs.json`. `kit.toml` rows only mirror the manifest, and no leg names its `enforces`. | R1 | MISMATCH | wm79:96-100, :155-160, :204-207, :343; wb11:36-44; oc7:58-63 |
| 81 | `stall-recorder.js` reads the transcript itself; reading it through runlog's extractor in Python was rejected | R3 | AGREES | wm81:31-40, :103-106 |
| 90 | S3, S35 and S37 change a leg's command, its guard and its ceiling by hand in `tools/gate-legs.json` | R1 | MISMATCH | wm90:51-53, :169-170, :174-176, :337; wb11:36-44 |
| 90 | The process-monitor and runlog self-tests read health events through `journal.py read --producer health` | R3 | AGREES | wm90:119-121, :166-168; oc7:202-205 |

##### 2. Mismatches

- **wm41 R8.**
  - wm41:39-43: "`run_unit_offer` first reads the build lease `refs/gov/leases/<slug>/build` through the one lease reader (`unattended.sh --claims`, `read_claims` …) and refuses `offer refused — not the driver · <slug>` unless this session holds it".
  - pr1:207-208: "`print_claims` still prints fields 1 to 5 (`:2204`), so the `--claims` row shape … is unchanged".
  - Those five fields are name, fleet tag, status, beat-age and liveness verdict. `session` is field 7 (`unattended.sh:2114`), so `--claims` cannot say whether this session holds the lease.
  - Change: S2 should read the holder from a source that carries `session`: either the lease record itself, or pr1 S6's `lease` mode class `mine` (pr1:90-91). Otherwise it should file an ask to dPlacedRequest for a verb that prints it. AC5 should be staged against that read.
  - Cause: pre-existing.

- **wm46 R3 (`resolve`).**
  - wm46:53: "`runtime.no-progress` (`tools/policy/catalogue.toml:451`, read through `resolve`)".
  - oc7:379-380: "The policy keys are read through the policy kit's `get` verb … as a subprocess, the one seam a sibling kit may reach".
  - Change: `progress.py` should run `<prefix>/policy/policy.py get runtime.no-progress` as a subprocess, finding the policy kit through an inline `resolve_kit_dir`, as wm41 and wm49 already do.
  - Cause: pre-existing. The source is the build brief's I31 row (prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md:228, "Python `resolve(key)` (`policy.py:752`)"), which the parent contradicts. That makes this a class across the build, not one spec.

- **wm46 R3 (loop kit functions).**
  - wm46:78-80: "recorded through `write_transition` (TOOL-dDeclaredLoop-3) … `record_draw(build, "re-dispatch", item)` alone".
  - oc7:202-205: "A kit may not import a sibling kit". The loop kit's own seams are commands: dl3:61 `loop_transition.py record --build … --witness <sha>`, and dl30:139 "Each draw site calls `"$py" "<prefix>/loop/budget.py" draw --build <slug> --cause <c> --item <id>`".
  - Change: S7 should route through `loop_transition.py record` and `budget.py draw --cause re-dispatch` as subprocesses, found by `resolve_kit_dir`, and its edge line should name those verbs.
  - Cause: pre-existing.

- **wm47 R3.**
  - wm47:43: "the ceiling read through `resolve` (`tools/policy/policy.py:752`)", inside `tools/runtime/supervise.py`.
  - oc7:379-380 (quoted above).
  - Change: S1 should read `runtime.hold-ceiling` with `policy.py get` as a subprocess.
  - Cause: pre-existing (from I31).

- **wm59 R3 (`resolve`).**
  - wm59:49 and :66: "read the `host-key`'s value through `resolve` (I31, `tools/policy/policy.py:752`)" and "`flow.on-exhausted` … through `resolve`".
  - oc7:379-380.
  - Change: `cadence.py` should read both keys with `policy.py get <key>` as a subprocess.
  - Cause: pre-existing (from I31).

- **wm59 R3 (loop kit functions).**
  - wm59:66: "calls `derive_ending(value, [], state)` (TOOL-dDeclaredLoop-31 S2)". wm59:52 and :55-63 have `cadence.py` "read S4's budget" from `budget_state` and `derive_period_budget` in `tools/loop/budget.py`.
  - oc7:202-205. dl31:150 gives `endings.py derive` as the seam. dl30's only verbs are `budget.py draw`, `value` and `--fixture` (dl30:222, :235).
  - Change: the tick should call `endings.py derive` as a subprocess. S4 should add a `budget.py` verb that prints `open`/`exhausted <s>/<t>` for the `run/<cadence>/<period>` key, and `cadence.py` should run that verb rather than calling the module.
  - Cause: pre-existing.

- **wm59 R8.**
  - wm59:59-62: "its spend is the number of `released` records (… the hand-over `run_cadence_period` writes on a failed run) … Each lap that ended without the period's witness is one draw".
  - dl30:58-61: "Contention draws nothing. `classify_repeat(event)` returns `contention` for … a wait on a lease another live build holds and an unreachable remote; … no draw row is written".
  - Change: S4 should exclude a lap whose failure `classify_repeat` answers `contention`. For example, the hand-over could record the cause, and only non-contention `released` records would count. An AC should observe that an unreachable remote costs a period nothing.
  - Cause: pre-existing.

- **wm79 R1.**
  - wm79:205-206: "`tools/runtime/kit.toml` carries a `[[gate_leg]]` row per runtime leg in `tools/gate-legs.json`". wm79:99 says "the `runtime selftest` leg runs it". wm79:158-160 says "the leg `runtime returns block parity` are deleted. … by name: `tools/gate-legs.json` (the leg's row)". Files touched lists `tools/gate-legs.json` (:343). No leg names `enforces`.
  - wb11:36-44: "Each leg is declared exactly once: a `[[gate_leg]]` row in its kit's descriptor … A declaration holds every manifest key its leg carries: … `enforces` … `--write` renders `tools/gate-legs.json` from every declaration".
  - oc7:61: "a leg carrying no `enforces` is red".
  - Change: each runtime leg should be declared once in `tools/runtime/kit.toml` with every key, `enforces` among them. S13's argv change and S29's deletion should be edits to that declaration. `tools/gate-legs.json` should leave Files touched, rendered by `leg_factory.py --write`. AC40 should be observed by `leg_factory.py --check`/`--conform`, not by `govkit.py selfcheck` "claimed".
  - Cause: pre-existing.

- **wm90 R1.**
  - wm90:52-53: "the leg's command in `tools/gate-legs.json` runs `selftest.py --modules`".
  - wm90:169-170: "The `manifest-check self-test` guard in `tools/gate-legs.json` gains `tools/runtime/session_binding.py`".
  - wm90:175: "written into its budget row and the leg's `ceiling`". Files touched lists `tools/gate-legs.json` (:337).
  - wb11:36-44 (quoted above).
  - Change: S3, S35 and S37 should edit the declaring rows: the runtime kit's `[[gate_leg]]` and the kickoff manifest leg's declaration, or its `[[exempt_leg]]` row in `tools/govkit/registry.toml`. They should then re-render with `leg_factory.py --write`. AC35 should read the declaration or the render, and `tools/gate-legs.json` should leave Files touched.
  - Cause: pre-existing.

##### 3. Unknown until built

None.

##### 4. Rule-wide hits the rule does not bind

- wm38 R1: it adds no leg. Its §7 `New arm:` lines extend four existing suites (wm38:232-235).
- wm38 R8: "witnessed" is the orientation check's witness line (wm38:60-64, :139-143). It is not one of dl3's channels and not a budget edge.
- wm40 R8: `item-witness` is one of the commit queue's push events (wm40:35-38). It names no channel, no budget and no `--claims` field.
- wm40, wm41, wm49, wm55 and wm59 R9: their code is in the runtime or policy kit, not `tools/roles/`. R3 governs their reads (rows above).
- wm57 R8: "notification channel" is unit 48's adapter (wm57:50-52), and `witness` is a lease-record key a fixture plants a token in (wm57:206-207).
- wm61 R4: `record-kind.node-profile` is a Carries tag for a node-local file outside the record factory (wm61:6, :92-94). The spec has no loop item, input, `returns` or `routes`.
- wm61 R7: `tools/policy/guard.py` is cited as a precedent (wm61:86-88). The write uses dl2's inline `check_terminal_proof` (wm61:68-71) and claims nothing about `guard.py --staged` or the `Gov-Policy:` trailer.
- wm74 R4: "returns" are kept agent returns keyed by site label (wm74:21-22, :40-41), not a loop row's `returns`.
- wm79 R4: it has no `[[item]]` row, layer tag or `routes`.
- wm79 R8: `budget-spent` is a journal class (:91), `budget-ms` is a hook-pack budget (:221), and `selftest-budgets.txt` is the run-gates file. None is dl30's budget.
- wm90 R8: "claim" is the supervisor's start claim from unit 78 (wm90:219-221), not `--claims`. "budget" is `selftest-budgets.txt`.
- wm92 R2: it writes a BACKLOG ask row and states "no new record kind is minted" (wm92:152-154).
- wm93 R3: `tools/check-spec-tokens.py` is a repo-root tool, not a kit, and it already loads `design_lib.py` by path (tools/check-spec-tokens.py:416-428). `design_lib.py` and `gen_build_index.py` are the same kit. Option (c), which would have a kit import the tool, was rejected (wm93:182-185).
- wm94 R1: it names existing legs on spec §7 leg lines and cites a leg's guard as evidence (wm94:155-158, :259). It edits no leg or manifest.
- wm96 R3: the acceptance criteria's `python -c` import of `design_lib` is a probe run inside the memory-tree kit (wm96:155, :168).
- wm97 R1: S16 edits spec 94's §7 leg line, not the manifest (wm97:99-105, :192-194).
- wm97 R5: the "disposition row" is a BACKLOG SEV row (wm97:133-135, :298-300), not dl16's disposition door.
- wm97 R8: "spawn budget" is a gate leg's name (wm97:102).
- wm108 R1, R3 and R8: it touches only specs 95-97 and a README. The hits are a list of leg names (:278-283), a rejected token-parse alternative (:208), an `ast` walk inside a probe command (:79), and "liveness half" or "spawn budget" wording.
- wm126 R3: `spec_from_file_location` loads `check-spec-tokens.py` inside a probe command (wm126:140), not kit code. Files touched is specs and a README only.

##### 5. Citation specs

None: group B2 is rule-wide, so it holds no citation specs.

Files read: memory/builds/dWellOiledMachine/spec/2026-10-2?-spec-TOOL-dWellOiledMachine-{38,40,41,46,47,49,55,57,59,61,64,74,79,81,90,92,93,94,96,97,108,126}.md; memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-11.md; memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md; memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-1.md; memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-{2,3,30,31,33}.md; memory/builds/dBoundRoles/spec/*-dBoundRoles-{21,43}.md; tools/unattended/unattended.sh:2108-2210.

## Group B3

I found two R3 mismatches, both in group B3's specs: spec 37 and spec 50. Spec 35 has one UNKNOWN UNTIL BUILT. Every other R3 assumption in the group agrees with the parents, and six specs are probe hits the rule does not bind. Both mismatches already read so at `ab864dfc8`: `git diff --stat ab864dfc8 d1721ef20` over oc7, oc19, oc28 and the dDeclaredLoop specs printed nothing. I also found one R8 defect in spec 52, outside B3's rule. It gets its own row, because spec 52 sits in no R8 group.

**1. Table**

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 35 | `session_node.py` reads the session binding through `session_binding.py read` and the act binding through `read_binding` | R3 | AGREES | Both are in the runtime kit, the same kit as `session_node.py` (wm35:40-43, :50; wm12:41; wm39:48, :60 `tools/runtime/bindings.py`). |
| 35 | Commits are read through `read_commits` | R3 | AGREES | `read_commits` is in `tools/lib/commit_trailers.py` (dl23:39), which is not a sibling kit. A copy-installed kit carries it inline, as wm39:78 does; spec 35 does not say this, but that gap is outside R3. |
| 35 | `session_node.py ring` reads the message's `to` from `read_mailbox`'s row | R3 | AGREES | `read_mailbox` is a bash function in `tools/unattended/unattended.sh` (ks5:79; ks6:33), so Python cannot load it in process. The spec names no verb (`--mail read`) and no locator: a gap, not an in-process import. |
| 35 | `run_mail_ring` (unattended) and `render_pointers` (kickoff) run `session_node.py ring` and `sessions` | R3 | AGREES | These are subprocess calls (wm35:62-77), the form oc7:202-205 allows. The `resolve_kit_dir` locator is not stated. |
| 35 | The `[[native]]` rows `pattern = "handoff:SESSION_ID_RE"` (roles kit) and `"act:ACT_RE"`, and `resolver = "session_node:resolve_session"` / `"session_node:resolve_act"` (runtime kit), all resolved by the playbook kit | R3 | UNKNOWN UNTIL BUILT | oc28:42-49: `pattern` is "the module and name that compile it". oc28's own rows name memory-tree modules from the playbook kit (oc28:119-129), and one resolver is a CLI form (`corpus_ids:--print-defined-ids`). Neither oc28 nor oc19 says whether the playbook loads `<module>:<name>` in process. The playbook descriptor has `requires = []` (`tools/govkit/entries/playbook.kit.toml:7`), and `tools/playbook/namespaces.toml` is absent at HEAD. |
| 37 | `run_with_credentials` reads `runtime.act-auth` through the policy kit's in-process `resolve` | R3 | MISMATCH | wm37:60-61 against oc7:202-205 and oc7:379-380. `tools/policy/policy.py:752` is `def resolve(key, repo=".", rev=None):`. |
| 37 | S6 adds `last` to `catalogue.toml` and an arm to `check_value` in the policy kit | R3 | AGREES | Editing the policy kit's own files is not a cross-kit call (wm37:72-76). |
| 37 | `read_secret_ref` and `read_capability` | R3 | AGREES | Both are in the runtime kit (wm17:54 `tools/runtime/secret_scan.py`; wm14:53). |
| 50 | `wait_graph.py` (runtime kit) reads a parent's transitions through `read_transitions` | R3 | MISMATCH | wm50:37-38 against dl3:69-74: `read_transitions` is a Python function in the loop kit (`tools/loop/loop_transition.py`, dl3:224) with no read verb. |
| 50 | The release records a move "through `write_transition`" | R3 | MISMATCH | wm50:61 against dl3:60-61, which offers `python tools/loop/loop_transition.py record …`. |
| 50 | `loop_parents.py route` is run as a subprocess and resolved through `resolve_kit_dir` | R3 | AGREES | wm50:59, :71. |
| 50 | Open questions are read from `--mail read`, and the half-deadline from `check_deadline_passed` | R3 | AGREES | `--mail read` is a verb. `check_deadline_passed` is a shell function (pr17:50, :121) reached through wm18's sweep. Neither is an in-process import. |
| 50 | `scan_cycles` is moved to `tools/lib` and carried inline in `backlog.py` and `wait_graph.py` | R3 | AGREES | `tools/lib` is not a sibling kit, and a parity row covers the copies (wm50:44-50). |
| 52 | `write_claim_beat` runs `python beat.py render`, and `beat.py members` runs `unattended.sh --claims` | R3 | AGREES | Both are subprocess calls (wm52:57, :67). |
| 52 | `beat.py members` reads each node's capacity, free slots, load and beat time "through `unattended.sh --claims`" | R8 (outside B3's rule) | MISMATCH | wm52:65-68 against pr1:206-208. |
| 63 | `GOVREF_DOOR` gains `--node` and `--memory`, and the door is reached by its verb | R3 | AGREES | wm63:30-35; wm58:56 shows `resolve_kit_dir "$py" memory-tree gov_record.py`. |
| 63 | `gov_record.py` (memory-tree) applies `read_host_name`'s rule and `derive_ref_segment` | R3 | AGREES | It restates a rule and loads no module (wm63:41, :47). `derive_ref_segment` is a bash function (pr12:33), and this usage is inherited from wm58:65. |
| 65 | `stall-recorder.js` (unattended) runs `journal.py write`, and `supervise.py` runs `journal.py read` | R3 | AGREES | These are subprocess verbs (wm65:34, :40). wm16:63 says the JS producer runs `python journal.py write` "through its resolved" path. |
| 91 | `readLimitRecord` renders the reset through `lease.renderUtc` | R3 | AGREES | `stall-recorder.js` and `run-lease.js` are in the same kit, unattended (wm91:41-42). |

**2. Mismatches**

- **Spec 37, S5.** wm37:60-61: "`classes` is `runtime.act-auth` read through `resolve` (`tools/policy/policy.py:752`)". oc7:202-205: "A kit may not import a sibling kit (TOOL-dGroundRules-1, §4 Evidence), so the module carries the inline `resolve_kit_dir` block … and runs `<sys.executable> <kit>/policy.py get <key> --explain`". oc7:379-380: "The policy keys are read through the policy kit's `get` verb … as a subprocess, the one seam a sibling kit may reach".
  - Change: S5 should read `runtime.act-auth` by running `policy.py get runtime.act-auth` as a subprocess, found through an inline `resolve_kit_dir`, through the runtime kit's one shared reader. It should state what it does with no policy kit present or on exit 2. The §10 seam cite moves from `resolve` to `get`.
  - Cause: pre-existing. It comes from brief row I31 (`2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md:228`).
- **Spec 50, S2.** wm50:37-38: "a parent whose last transition, read through `read_transitions` (TOOL-dDeclaredLoop-3 S7), is not terminal". dl3:69-74 places `read_transitions(build, repo)` in the loop kit, with only the verbs `record` and `check` (dl3:61, :65). The runtime kit's descriptor declares no `requires_if` row naming the loop kit (wm1:48 `requires = ["policy"]`; wm28:40 adds `settings-merge`).
  - Change: either declare a `requires_if` row on `tools/runtime/kit.toml` naming the loop kit and import through `resolve_kit_dir`, or reach a loop-kit read verb by subprocess. dDeclaredLoop has no such verb today, so that option needs an open ask in §8.
  - Cause: pre-existing.
- **Spec 50, S5.** wm50:61: "a move answer is recorded through `write_transition` on row P1". dl3:60-61: "`write_transition` and `python tools/loop/loop_transition.py record --build <slug> --from <state> --item <tag> --outcome <o> --witness <sha>…`".
  - Change: S5 should record the move by running `loop_transition.py record` as a subprocess, found through `resolve_kit_dir` as S7 already finds `loop_parents.py`, not by calling the Python function.
  - Cause: pre-existing.
- **Spec 52, S5 (R8; outside B3's rule, but spec 52 sits in no R8 group).** wm52:65-67: "one line per fleet tag whose lease record carries a node beat … `<tag> · capacity <n> · free <m> · load <x> · beat <utc>`, read through `unattended.sh --claims`". pr1:206-208: "`print_claims` still prints fields 1 to 5 (`:2204`), so the `--claims` row shape … is unchanged".
  - Change: `members` needs a reader that returns the record's `node-*` lines, such as a lease-record read verb or an asked-for `--claims` field. `--claims` cannot carry these values.
  - Cause: pre-existing (pr1:207 at `ab864dfc8`).

**3. Unknown until built**

- Spec 35's `[[native]]` rows: the build of PLAY-dOrderedCharter-19/28's native resolution decides it. If that build imports `<module>:<name>` in process, the playbook kit reaches `handoff` (roles kit) and `session_node`/`act` (runtime kit) without a `requires_if` row. Spec 35 would then owe one, or should name a CLI resolver such as its own `show` verb.

**4. Probe hits the rule does not bind**

- **68:** it edits descriptor rows and adopter variables only. `resolve_kit_dir` appears only as a reuse-lookup result (wm68:131), and its other hits are citations.
- **95:** it edits spec prose only. The cites `design_lib.py:528-540` and `unattended-build.js:2187-2197` are evidence, not code.
- **112:** it adds a fixture and a criterion to spec 108. `build_commit` and `build_fixture` are cited, not imported by kit code.
- **115:** it edits spec prose only. `resolve_shell_argv` is matched by name in an AST walk inside a criterion. The S13/S20 predicate sources `lib-unattended.sh` in a spec probe that no kit ships.
- **117, 120:** rev bumps to spec 115. The `design_lib.py:525` and `lib-unattended.sh:1186` cites are evidence.
- Partial hits in the bound specs: in 52 and 91 the `import` hits are `python -c` measurement probes (wm52:198, wm91:85). In 37, `check_policy.py:4289` is the live launcher cited as evidence. The other `tools/<kit>/<file>:<line>` hits in 63 and 65 are citations of the same kit.

**5. Citation specs:** none. Group B3 is rule-wide, R3 only.

