**Serves:** research TOOL-dWellOiledMachine-1

# dWellOiledMachine's specs against dBoundRoles' and dTotalRecall's re-grounded specs: a read-only cross-check

Node d, 2026-10-28, base `d1721ef20` (origin/main). dWellOiledMachine's spec run began at
`ab864dfc8`, the parent of its first spec commit `4bc4aaf90`. That base holds dKeptSession's re-ground
and the second wave's, but neither dBoundRoles' (`ac8ab8d5f`, landed as `fffe4aadf`) nor
dTotalRecall's (`794a0f5fb`, landed as `2bd5e10d4`). Their deviation records confirm what each revised:
dBoundRoles units 1, 2, 3, 5, 6, 11, 12, 14, 20, 21, 22, 23, 25, 43 and 60; dTotalRecall units 1, 2, 4,
8, 9, 11, 15, 18, 19, 20, 22, 25, 26, 43 and 76. Every other parent spec is byte-identical between
`ab864dfc8` and `d1721ef20`. Spec 127 was written after both merges and is out of scope. This record
compares each assumption the exposed specs make about a parent with what the parents' DEFERRED specs
say now. It is not an audit: no spec was edited, no review harness ran, and the mismatches feed the
re-ground brief
[`2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-reground`](../prompts/2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-reground.md).

**Counts:** 167 assumptions · 77 AGREES · 83 MISMATCH · 7 UNKNOWN UNTIL BUILT, over 80 specs (the 23
citation specs and the 57 rule-wide candidates). 46 specs hold at least one MISMATCH: 1, 2, 3, 4, 5, 6,
7, 8, 9, 10, 11, 12, 15, 16, 17, 19, 20, 23, 24, 25, 26, 30, 32, 33, 34, 36, 37, 39, 41, 42, 43, 44,
45, 46, 47, 48, 50, 51, 52, 53, 54, 56, 58, 59, 79 and 90. By rule: 20 citation, 1 citation and R3,
11 R1, 2 R2, 42 R3, 6 R8 and 1 R9. 34 mismatches, in 24 specs, sit outside the citation population and
were found only by rule scoping: rows in groups B1, B2 and B3 (specs 1, 2, 5, 6, 10, 12, 15, 17, 20,
23, 24, 25, 26, 33, 36, 37, 41, 46, 47, 50, 52, 59, 79 and 90). 5 mismatches come from a re-ground:
rows 76 (tr9's `record find` cap moved into S3), 101 (br1 F6's `check_layer_roles` reads
`.claude/roles.json`), 122 (br11 rev-3's `owner-question` refusal), 148 (br21's `with_default`) and
153 (tr2's lease-holder read, left open as tr2 F6). The other 78 already read so at `ab864dfc8`.

## Method

- **Population by citation.** `grep -oE` over `spec/*.md` for the units the two re-grounds revised,
  both `TOOL-<build>-<n>` and the bare `<build>-<n>`: 23 specs.
- **Population by rule.** The brief states R1 to R9: dFurnishedOrders' R1 to R8, as the re-grounds
  apply them, and R9, dBoundRoles' rule-wide change itself (br21's `with_default`, made the
  catalogue-default form by br43 S21). A text probe for each over the other 102 specs named 44
  candidates. Groups B1 and B2 then found that the probe missed most R3 breaks, so a second probe for
  the forms they found (I31, `resolve`, `readPolicy`, sibling-kit function names and
  `tools/<kit>/<file>.py:<line>` cites) over the specs neither population held named 13 more, checked
  by group B3 for R3 alone.
- **Readers.** Five `gov-spec-reviewer` agents, read-only, one per group of the brief
  [`2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-crosscheck`](../prompts/2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-crosscheck.md),
  their handoffs beside it; group B3's paragraph and row were added to the brief after the first four
  returned, so only B3's handoff carries them. Their returns, with every MISMATCH's both sides quoted,
  its `Change:` and its `Cause:`, are
  [`2026-10-28-build-TOOL-dWellOiledMachine-1-crosscheck-returns`](2026-10-28-build-TOOL-dWellOiledMachine-1-crosscheck-returns.md).
- **The main loop** assembled the table from the returns' tables by script, sorted by spec, and
  derived the counts from it. It changed no verdict. Where a reader's prose count differs from its
  table (A2 says 38 rows, its table 46; B1's and A1's totals differ by one or two), the table wins.
  Rows B1 and B2 mark "not a probe hit" are kept: they are R3 breaks in specs the rule-wide probe
  named for another rule.
- **Aliases:** `wmN:L` is line L of `spec/2026-10-2?-spec-TOOL-dWellOiledMachine-N.md`; `brN:L`,
  `trN:L`, `ksN:L`, `ocN:L`, `dlN:L`, `wbN:L` and `prN:L` of the parents' spec N under
  `../../<build>/spec/`; all at `d1721ef20`.
- **The brief's own errors.** Readers B1 and B2 found R8's cites wrong: the witness channel set is dl3
  S4 (dl3:54-59), not S2, and "contention draws nothing" is dl30 S5 (dl30:58), not dl33 S3. They judged
  by the parent text, so no verdict rests on the brief's cite.
- **What it does not check:** anything a parent's build run decides; dSafePassage and dGroundRules
  surfaces the specs name directly; the 45 specs neither population reached. The probes are text
  heuristics, and B1 and B2 showed the first one under-counts R3. No skeptic re-ran the verdicts.
  Instead each re-ground writer re-reads both sides before it edits, and returns a row it cannot bear
  out as refused.

## What the mismatches have in common

- **A policy key read in process (I31; 23 specs).** R3. The build's own spec brief, row I31 of
  [`2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief`](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md)
  (line 228), names the policy kit's Python `resolve(key)` (`policy.py:752`) and JavaScript
  `readPolicy` (`policy-mirror.js:132`) as the readers. oc7:202-205 and :379-380 make `policy.py get`
  by subprocess "the one seam a sibling kit may reach", and ks8:62-66 makes a hook spawn
  `policy-mirror.js get`. The brief's third reader, `policy-shim.sh get`, already agrees. Specs 1, 3,
  5, 6, 8, 9, 10, 11, 15, 16, 17, 19, 24, 25, 36, 37, 44, 45, 46, 47, 48, 53 and 59 read through
  `resolve` or `readPolicy`; wm33, wm40, wm41 and wm49 already run `get`. Pre-existing; dBoundRoles' re-ground
  moved its own reads of two of the same keys (br5 `roles.retries`, br22 `runtime.agents-in-flight`).
- **A sibling kit's function called in process (19 specs).** R3. The runtime kit calls the roles kit's
  `load_workflows`, `load_run_journal`, `load_agent_transcript`, `render_wall` and `resolve_role_*`,
  the loop kit's `derive_position`, `write_transition`, `read_transitions`, `record_draw` and
  `derive_ending`, runlog's `resolve_session_tree`, memory-tree's `collect`, process-monitor's
  `scan_processes`, and the playbook kit's `derive_worktree_root` by name (wm1, wm2, wm4, wm5, wm7,
  wm11, wm19, wm24, wm26, wm30, wm32, wm34, wm43, wm44, wm46, wm50, wm54, wm56, wm59). Pre-existing.
- **A leg written into `tools/gate-legs.json` by hand (wm1, wm2, wm8, wm11, wm12, wm20, wm23, wm33,
  wm39, wm79, wm90).** R1. None names `enforces`, and wb11 makes the manifest a render of one
  declaration per leg. Pre-existing.
- **`unattended.sh --claims` asked for fields it does not print (wm6, wm15, wm41, wm52, wm54).** R8.
  pr1:206-208 keeps it to fields 1 to 5; session, epoch, offer and node beats are not among them, and
  wm15's `clock-offset` cannot be column 12, which pr1 gives `epoch`. wm59's sixth R8 row is its
  contention draw (dl30 S5). wm58's holder read (row 153, re-ground) is the same gap, waiting on tr2 F6.
- **`record find` read as uncapped or with content (wm32, wm34, wm44, wm51, wm53).** tr9:94-96 caps
  it at 40 rows with no content and only `--kind`, `--tag`, `--build` and `--paths` filters. Row 76 is
  from the re-ground; the rest pre-existing.
- **dBoundRoles surfaces read wider than they are (wm7, wm9, wm19, wm43, wm45).** br3's work order
  renders five blocks and no `allow`, `script` or `fan`; br22 separates a stage's `fan` (spawned per
  call) from its `cap` (in flight at once); br25 states no author/verifier separation. Pre-existing.
- **Registry rows short of tr1 and tr18's cells, and unjoined typed kinds (wm4, wm8, wm32, wm58).**
  `tag` outside `record.`, `layer` not a layer tag, no `lifecycle` or `readers`, an `id-rule` holding a
  placeholder the door does not mint, no `Caused-by`; `act` and `quiesce` added as build-folder kinds
  with no join to `TYPED_RECORD_KINDS`. Pre-existing.
- **Single defects:** wm42's readers of `.claude/roles.json` miss br1 F6's `check_layer_roles`
  (re-ground); wm48 S2 ignores `owner-question`'s new refusal (re-ground); wm56 types catalogue
  defaults after a None (re-ground); wm39 F4's ask to tr19 names a commit range tr19 does not grade;
  wm54's model check reads the landed revision, not the assignment it checks; wm59 counts every failed
  lap as a draw.

## Summary table

| # | Spec | Group | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|---|---|
| 1 | wm1 | B1 | The `runtime selftest` leg is added to `tools/gate-legs.json` by hand, with no `enforces` | R1 | MISMATCH | wm1:207, :229; wb11:36-49, :154; oc7:58-63 |
| 2 | wm1 | B1 | S3: `launch_act` reads `runtime.spawn-backend` through the policy kit's `resolve`, loaded as `load_tree_lib` loads its sibling | R3 | MISMATCH | wm1:64-66, :165, :355-357; oc7:202-205, :379-380; `tools/policy/check_policy.py:879-887` (does `sys.path.insert` then `import tree_lib`) |
| 3 | wm1 | B1 | S7: the policy kit's `check_policy.py` loads the runtime kit's `build_headless_argv` through `resolve_kit_dir`, in process | R3 | MISMATCH | wm1:107-110, :322-329; oc7:202-205 |
| 4 | wm2 | B1 | S8: the `runtime next tails` leg is added to `tools/gate-legs.json` by hand, with no `enforces` | R1 | MISMATCH | wm2:70-72, :149, :243; wb11:36-49; oc7:58-63 |
| 5 | wm2 | B1 | S1 and S6: `next.py` calls the loop kit's `derive_position` and the policy kit's `check_shrink_list`/`write_shrink_list` (not a probe hit) | R3 | MISMATCH | wm2:34-35, :60-63; dl7:31 (`tools/loop/position.py`); ks19:30 (`tools/policy/policy.py`); oc7:202-205 |
| 6 | wm3 | A1 | `lifecycle-request` and `attendance-override` are `[[record-kind]]` rows in `tools/memory-tree/record-kinds.toml` | cite | AGREES | wm3:49-51, :97; tr1:62-66. The rows name only `home`, `writer` and `check`, so the builder must fill tr1's other required columns. |
| 7 | wm3 | A1 | The row's `check` names a leg, `runtime selftest` | cite | AGREES | wm3:51; tr1:196. wm1:207 mints that leg. |
| 8 | wm3 | A1 | Both kinds are ref-commit records, not typed build-folder records | R2 | AGREES | wm3:45-49, :93-94; oc42:35-39 |
| 9 | wm3 | A1 | `flow.wait-ceiling` and `attendance.scope` are read through `resolve` in process from `tools/runtime/lifecycle.py` | R3 | MISMATCH | wm3:62, :96, :186; oc7:202-205, :379-380 |
| 10 | wm3 | A1 | `derive_breakpoints` (loop kit) is re-pointed to the verb `lifecycle.py attendance` | R3 | AGREES | wm3:98-102 (a verb, not an import) |
| 11 | wm3 | A1 | `unattended.sh --claims` shows whether the build lease is absent, `released` or terminal | R8 | AGREES | wm3:86-87; pr1:206-208 (fields 1-5 keep status in field 3); `unattended.sh:2204` |
| 12 | wm4 | A1 | The `intake` row in `record-kinds.toml` has `layer = "runtime"`, `home = ""`, and no `lifecycle` or `readers` | cite | MISMATCH | wm4:70-74; tr1:64-66; tr18:45-49, :130-133 |
| 13 | wm4 | A1 | `derive_request_content_key` (loop kit `request.py`) is reached through `resolve_kit_dir` and called in process | R3 | MISMATCH | wm4:39-40; pr19:33-36 (`python request.py key <file>` exists); oc7:202-205 |
| 14 | wm4 | A1 | The session binding is read through the verb `session_binding.py read <id>` | R3 | AGREES | wm4:56-57 |
| 15 | wm5 | B1 | S2: `derive_witness_adapter` reads `runtime.owner-harness` through `resolve(key, repo, rev)` in process | R3 | MISMATCH | wm5:38-40, :217-218; oc7:379-380 |
| 16 | wm5 | B1 | S3 to S5: `ratify.py` calls `check_owner_disposition`; the loop kit's `breakpoints.py` "reads S3"; the loop kit's `placement.py` reads through `read_build_disposition` | R3 | MISMATCH | wm5:41-64, :123 (verbs `check`, `fixture` only); dl31:60-63 (`check_owner_disposition` is a bash function of the unattended driver); oc7:202-205 |
| 17 | wm5 | B1 | S5: the disposition lines are read from the build's claim commit, not from `--claims` | R8 | AGREES | wm5:57-64; pr21:45-49 (`refs/gov/claims/<slug>`) |
| 18 | wm6 | B1 | S2: the lease's fleet tag and live/held status are read through `unattended.sh --claims` | R8 | AGREES | wm6:46-48; pr1:203-208; `tools/unattended/unattended.sh:2204` (`cut -f1-5`; fields slug, node, status, …) |
| 19 | wm6 | B1 | S6 and S7: the lease's epoch is read through `unattended.sh --claims` | R8 | MISMATCH | wm6:85-89, :92-96; pr1:203-208 |
| 20 | wm6 | B1 | S5: `runtime.relaunch` is read through `resolve` (`policy.py:752`) (not a probe hit) | R3 | MISMATCH | wm6:77-78; oc7:379-380 |
| 21 | wm7 | A1 | br3's work order carries an `allow` list of permission-rule entries, and a `script` | cite | MISMATCH | wm7:34-39, :99-100, :113; br3:48-61 |
| 22 | wm7 | A1 | br22 S1 declares each stage's `role` and `fan`, read through `load_workflows` | cite | AGREES | wm7:77-79; br22:34-45 |
| 23 | wm7 | A1 | br25 S2 moves `checkHarnessCall` into `tools/roles/spawn-guard.js` | cite | AGREES | wm7:122-124; br25:47-53 |
| 24 | wm7 | A1 | `act_binding.py` calls the roles kit's `load_workflows` and `load_run_journal`, and runlog's `resolve_session_tree`, in process | R3 | MISMATCH | wm7:36-37, :80-82, :153; oc7:202-205 |
| 25 | wm7 | A1 | `read_claims` fetches the remote | R8 | AGREES | wm7:162-163; pr1:76-80 |
| 26 | wm8 | A1 | Return validation is dBoundRoles' return check | cite | AGREES | wm8:98-99; br5:39-54 |
| 27 | wm8 | A1 | The `return` row: `layer` `runtime`, `schema` header with a `source` and no `fields`, `readers` `supervise.py`, `lifecycle` in prose | cite | MISMATCH | wm8:81-85; tr1:177-182, :79-81; tr18:45-49, :130-133 |
| 28 | wm8 | A1 | Door writes land tracked records in the act's working tree | cite | AGREES | wm8:186-188; tr2:82-83 (S8 `git add`) |
| 29 | wm8 | A1 | `roles.retries` is read through `resolve` (I31) in process | R3 | MISMATCH | wm8:58-59; br5:63-67; oc7:379-380 |
| 30 | wm8 | A1 | The new leg `runtime returns block parity` is written into `tools/gate-legs.json` with no `enforces` | R1 | MISMATCH | wm8:88-91, :166, :179; wb11:36-49; oc7:58-63 |
| 31 | wm9 | A1 | The work order carries a `fan`, its stage's declared `fan`, rendered by dBoundRoles | cite | MISMATCH | wm9:54-57, :92, :207; br3:48-54; br22:34-37 |
| 32 | wm9 | A1 | br22 S5's `read_agent_limit` reads the same key inside the roles kit | cite | AGREES | wm9:222-224; br22:53-58 |
| 33 | wm9 | A1 | `runtime.agents-in-flight` is read through `resolve` in process | R3 | MISMATCH | wm9:40-42; br22:53-56; oc7:379-380 |
| 34 | wm10 | B1 | S5: settings-merge reads `runtime.hook-failure` by running `python <prefix>/policy/policy.py get` | R3 | AGREES | wm10:73-74; oc7:379-380 |
| 35 | wm10 | B1 | S6 and S8: `dispatch.js` reads `runtime.hook-failure` (and the judge keys) through `readPolicy(…, {repo})` in process | R3 | MISMATCH | wm10:75-80, :88-95; ks8:62-66 |
| 36 | wm11 | A1 | The `workspace` kind's row lands in `record-kinds.toml` "(TOOL-dTotalRecall-2)" | cite | AGREES | wm11:57, :114. The registry is tr1's (tr1:62); tr2 only reads it (tr2:45-50). The writer `write_workspace_record` is legal there. |
| 37 | wm11 | A1 | `build.worktree` is read through `resolve` in process | R3 | MISMATCH | wm11:33-35; oc7:379-380 |
| 38 | wm11 | A1 | The worktree root comes from the playbook kit's `resolve_node_overrides` and `derive_worktree_root`, called by name | R3 | MISMATCH | wm11:36-38, :275; oc7:202-205; `render_playbook.py:1777` has `--answers` |
| 39 | wm11 | A1 | branch-reconcile reads the records as files and imports nothing from the runtime kit | R3 | AGREES | wm11:82-85 |
| 40 | wm11 | A1 | The new leg `runtime workspace fixtures` is written into `tools/gate-legs.json` | R1 | MISMATCH | wm11:86-89, :164, :174; wb11:36-49; oc7:58-63 |
| 41 | wm12 | B1 | S11: the `runtime session-binding fixtures` leg is added to `tools/gate-legs.json` by hand, with no `enforces` | R1 | MISMATCH | wm12:101-104, :205, :219; wb11:36-49; oc7:58-63 |
| 42 | wm13 | B1 | S6: a run lease's `landed` status (field 3) and its name `run/<cadence>/<period>` (field 1) are read through `--claims` | R8 | AGREES | wm13:58-62; pr1:203-205 |
| 43 | wm15 | B1 | S3: `run.host` is read through `resolve("run.host")` in process | R3 | MISMATCH | wm15:45-46; oc7:379-380 |
| 44 | wm15 | B1 | S5: `clock-offset` becomes "a twelfth `CLAIM_ROWS` column" (not a probe hit) | R8 | MISMATCH | wm15:60-66; pr1:203-208 |
| 45 | wm16 | A1 | tr18 renames the memory tree's Serves kind `journal` to `log`, freeing the word for runtime's journal kind | cite | AGREES | wm16:82-84; tr18:76-82, :108-109 |
| 46 | wm16 | A1 | `record-kind.journal` can own `<git common dir>/runlog/` under that name | cite | UNKNOWN UNTIL BUILT | wm16:82-84; tr18:79, :144, :167, :172-173 |
| 47 | wm16 | A1 | `runtime.journal` is read through the policy kit's `resolve` in process | R3 | MISMATCH | wm16:69-70, :133; oc7:379-380 |
| 48 | wm16 | A1 | runlog carries the grammar inline under a parity row; the tick runs `journal.py prune` as a subprocess | R3 | AGREES | wm16:40-44, :74-77 |
| 49 | wm17 | B1 | S3 and S4: `runtime.secret-scan` and `runtime.secret-home` are read through `resolve` (`policy.py:752`) in process | R3 | MISMATCH | wm17:49-51, :55-56; oc7:379-380 |
| 50 | wm17 | B1 | S1 and S6: `scan_secrets` is called inside the runtime kit, where TOOL-dWellOiledMachine-16 moves it | R3 | AGREES | wm17:63-65, :119-120 |
| 51 | wm19 | A1 | `F` comes from each stage key's `fan` in the stage rows | cite | AGREES | wm19:38, :51; br22:34-37 |
| 52 | wm19 | A1 | The review-only `shape-run` record: `Kind` is `diff-review` or `spec-audit`, and `Round`, `Intensity` and `At` are required | cite | AGREES | wm19:110-111; tr11 §4 `SHAPE_RE` and the record |
| 53 | wm19 | A1 | Author/verifier separation belongs to br25's admission | cite | MISMATCH | wm19:88; br25:41-61, :88 |
| 54 | wm19 | A1 | `gov_record.py new shape-run --act <act>` writes an act-form row; a repeat writes nothing | cite | UNKNOWN UNTIL BUILT | wm19:69-73, :212-221; tr11:59-65; tr2:62-66 |
| 55 | wm19 | A1 | `roles.shape-enforce` is read through `readPolicy` (`policy-mirror.js:132`) inside `act-binding.js` | R3 | MISMATCH | wm19:56-57; ks8:62-66 |
| 56 | wm19 | A1 | The reconcile reads `load_agent_transcript` from `tools/roles/handoff.py` in process | R3 | MISMATCH | wm19:62-63, :72; oc7:202-205 |
| 57 | wm20 | B1 | The `runtime points registry` leg is added to `tools/gate-legs.json` by hand, with no `enforces` | R1 | MISMATCH | wm20:172, :182; wb11:36-49; oc7:58-63 |
| 58 | wm22 | B1 | S5: the purpose-review record is served as `research`, an untyped kind, in a file not named `-<kind>-<n>.md` | R2 | AGREES | wm22:56-58; `tools/memory-tree/tree_lib.py:406`; oc42:45-50 |
| 59 | wm23 | B1 | The `runtime hook-cap fixtures` leg is added to `tools/gate-legs.json` by hand, with no `enforces` | R1 | MISMATCH | wm23:71, :130, :139; wb11:36-49; oc7:58-63 |
| 60 | wm24 | B1 | S2: `memory.project-map` is read through `resolve`, and the roles kit's `load_roles` is called in process (not a probe hit) | R3 | MISMATCH | wm24:44-47; oc7:202-205, :379-380 |
| 61 | wm25 | B1 | S4: `runtime.act-harness` is read through `resolve` (I31) (not a probe hit) | R3 | MISMATCH | wm25:57-58; oc7:379-380 |
| 62 | wm26 | B1 | S2 to S4: `step.py` calls the roles kit's `extract_microformat_shapes`/`render_shape_line` and the loop kit's `derive_position`, `resolve_item_declaration` and `read_attendance` in process (not a probe hit) | R3 | MISMATCH | wm26:39-57; ks17:45, :137 (`tools/loop/loop_lib.py`); dl7:31; oc7:202-205 |
| 63 | wm27 | A1 | The `build-readme` and `claim` rows carry `root = true` as tr19 S3's stand-in, for dWellOiledMachine to drain | cite | AGREES | wm27:26-27, :62-63; tr19:62-67 |
| 64 | wm27 | A1 | `check_causes` in `record_causes.py` is the causes check that gains the `root-until` read | cite | AGREES | wm27:64-67; tr19:90-96 |
| 65 | wm27 | A1 | `record-kinds.toml` accepts a new column `root-until` | cite | UNKNOWN UNTIL BUILT | wm27:63-64, :126; tr1:198-200 |
| 66 | wm27 | A1 | An `intake-key` `[[native]]` row with a `module:NAME` pattern and resolver | R3 | AGREES | wm27:68-71; oc28:42-49, :119-129 (the parent's own form) |
| 67 | wm30 | A1 | Act-form `shape-run` records exist with `Variant`, `Effort` and `Rerun`, readable per build | cite | UNKNOWN UNTIL BUILT | wm30:37-41, :57-61, :73; tr11:53-59 |
| 68 | wm30 | A1 | The experiment reconcile reads `load_run_journal` and `load_agent_transcript` in process | R3 | MISMATCH | wm30:49-51; oc7:202-205 |
| 69 | wm32 | A1 | The `act` row has `tag = "record-kind.act"` and `layer = "runtime"` | cite | MISMATCH | wm32:67-68; tr1:173, :234-235; tr18:133 |
| 70 | wm32 | A1 | The door mints `<date>-build-<anchor id>-act-<act12>.md` | cite | MISMATCH | wm32:69; tr2:174-187 |
| 71 | wm32 | A1 | `write_act_record` writes through the door with no `Caused-by` | cite | MISMATCH | wm32:69-73; tr19:58-67 |
| 72 | wm32 | A1 | The door, one write per id, refuses a different value | cite | AGREES | wm32:186-187; tr2:62-66 |
| 73 | wm32 | A1 | The door accepts the act record written at the act's exit (lease authority) | cite | UNKNOWN UNTIL BUILT | wm32:71-72; tr2:188-197, :335-345 |
| 74 | wm32 | A1 | `act` is a new build-folder record kind with no join to `TYPED_RECORD_KINDS`, the factory table or HYGIENE | R2 | MISMATCH | wm32:67-71, :230; oc42:35-59 |
| 75 | wm32 | A1 | `render_wall` (`tools/roles/handoff.py:737`) is called from `tools/runtime/act.py` | R3 | MISMATCH | wm32:75-76, :283; oc7:202-205 |
| 76 | wm32 | A1 | The `Acts` table has one row per act record of the run, read through `record find` | cite | MISMATCH | wm32:88-89; tr9:89-103 |
| 77 | wm33 | B1 | S8: the `commit keys name their act` leg is a `[[gate_leg]]` row of `tools/runtime/kit.toml` and is also written into `tools/gate-legs.json`, with no `enforces` | R1 | MISMATCH | wm33:85-91; wb11:36-49, :154; oc7:58-63 |
| 78 | wm33 | B1 | S5: `trace.identity` is read by running `policy.py get` as a subprocess | R3 | AGREES | wm33:58-59; oc7:379-380 |
| 79 | wm34 | A2 | `record find` / `record show` are tr9's verbs (S3, S5) | cite | AGREES | wm34:41-43 · tr9:89-96, :104-107 |
| 80 | wm34 | A2 | One `record find` query returns every record naming the key, so `trace.rows = all` keeps every row | cite | MISMATCH | wm34:41-43, :57-60 · tr9:94-96, :207-209 |
| 81 | wm34 | A2 | `build_run_model` reads records through `gov_record.py` subprocesses | R3 | AGREES | wm34:70-72 · oc7:379-380 |
| 82 | wm34 | A2 | `trace.py` (runtime kit) resolves transcripts with runlog's `resolve_session_tree` | R3 | MISMATCH | wm34:47-48, :281 · oc7:202-205 |
| 83 | wm34 | A2 | `trace.rows` is read by a `policy.py get` subprocess | R3 | AGREES | wm34:34-37 |
| 84 | wm35 | B3 | `session_node.py` reads the session binding through `session_binding.py read` and the act binding through `read_binding` | R3 | AGREES | Both are in the runtime kit, the same kit as `session_node.py` (wm35:40-43, :50; wm12:41; wm39:48, :60 `tools/runtime/bindings.py`). |
| 85 | wm35 | B3 | Commits are read through `read_commits` | R3 | AGREES | `read_commits` is in `tools/lib/commit_trailers.py` (dl23:39), which is not a sibling kit. A copy-installed kit carries it inline, as wm39:78 does; spec 35 does not say this, but that gap is outside R3. |
| 86 | wm35 | B3 | `session_node.py ring` reads the message's `to` from `read_mailbox`'s row | R3 | AGREES | `read_mailbox` is a bash function in `tools/unattended/unattended.sh` (ks5:79; ks6:33), so Python cannot load it in process. The spec names no verb (`--mail read`) and no locator: a gap, not an in-process import. |
| 87 | wm35 | B3 | `run_mail_ring` (unattended) and `render_pointers` (kickoff) run `session_node.py ring` and `sessions` | R3 | AGREES | These are subprocess calls (wm35:62-77), the form oc7:202-205 allows. The `resolve_kit_dir` locator is not stated. |
| 88 | wm35 | B3 | The `[[native]]` rows `pattern = "handoff:SESSION_ID_RE"` (roles kit) and `"act:ACT_RE"`, and `resolver = "session_node:resolve_session"` / `"session_node:resolve_act"` (runtime kit), all resolved by the playbook kit | R3 | UNKNOWN UNTIL BUILT | oc28:42-49: `pattern` is "the module and name that compile it". oc28's own rows name memory-tree modules from the playbook kit (oc28:119-129), and one resolver is a CLI form (`corpus_ids:--print-defined-ids`). Neither oc28 nor oc19 says whether the playbook loads `<module>:<name>` in process. The playbook descriptor has `requires = []` (`tools/govkit/entries/playbook.kit.toml:7`), and `tools/playbook/namespaces.toml` is absent at HEAD. |
| 89 | wm36 | B1 | S5: `runtime.binary` is read through `resolve` (I31) (not a probe hit) | R3 | MISMATCH | wm36:68-69; oc7:379-380 |
| 90 | wm37 | B3 | `run_with_credentials` reads `runtime.act-auth` through the policy kit's in-process `resolve` | R3 | MISMATCH | wm37:60-61 against oc7:202-205 and oc7:379-380. `tools/policy/policy.py:752` is `def resolve(key, repo=".", rev=None):`. |
| 91 | wm37 | B3 | S6 adds `last` to `catalogue.toml` and an arm to `check_value` in the policy kit | R3 | AGREES | Editing the policy kit's own files is not a cross-kit call (wm37:72-76). |
| 92 | wm37 | B3 | `read_secret_ref` and `read_capability` | R3 | AGREES | Both are in the runtime kit (wm17:54 `tools/runtime/secret_scan.py`; wm14:53). |
| 93 | wm38 | B2 | The kickoff kit's code reaches the runtime kit's `session_binding.py` only through its command-line verbs (`read <sid> --card`, `put-card`). `scratch-guard.js` reads the binding as file text and imports no runtime code. (Outside the hits.) | R3 | AGREES | wm38:36-38, :49-53, :131-132; oc7:202-205 |
| 94 | wm39 | A2 | The new leg `runtime bindings fixtures` is written by hand into `tools/gate-legs.json`, with no `enforces` | R1 | MISMATCH | wm39:83, :175, Files touched · wb11:36-49 · oc7:58-63 |
| 95 | wm39 | A2 | tr19 S8's `check_causes` has a commit range it could grade through `bindings.py --check` (the F4 ask) | cite | MISMATCH | wm39:96, :270-273 · tr19:90-95 |
| 96 | wm39 | A2 | `trace.identity` is read through `policy-shim.sh get` | R3 | AGREES | wm39 S2 |
| 97 | wm40 | B2 | `build.push` is read by running `policy.py get` as a subprocess from the runtime kit | R3 | AGREES | wm40:32-35; oc7:379-380 |
| 98 | wm41 | B2 | `build.unit-holders` is read by running `policy.py get` as a subprocess | R3 | AGREES | wm41:32-37; oc7:379-380 |
| 99 | wm41 | B2 | The offer verb learns whether this session holds the build lease by reading `unattended.sh --claims` | R8 | MISMATCH | wm41:39-43; pr1:207-208; tools/unattended/unattended.sh:2113-2114, :2204 |
| 100 | wm42 | A2 | br1 gives `gov-session` its `layer` and `acts-as` and leaves its retirement to Runtime | cite | AGREES | wm42:103 · br1:107-108, :143-146, :333-336 (the cited `:98` is now `:107`) |
| 101 | wm42 | A2 | S1 lists every by-value reader of `.claude/roles.json` | cite | MISMATCH | wm42:43-46 · br1 F6 rev-3 (`check_layer_roles` reads `.claude/roles.json`) |
| 102 | wm42 | A2 | `handoff.py send` posts through the mailbox writer, which can only be reached by running `unattended.sh --mail post` | R3 | AGREES | wm42:53-54 · ks5 S5 |
| 103 | wm43 | A2 | A workflow's stage `fan` (br22 S1) is the number of agents the run holds in flight | cite | MISMATCH | wm43:47-48 · br22:108-109 |
| 104 | wm43 | A2 | `inflight.py` can read the stage rows of the workflow whose harness matches `scriptPath` | cite/R3 | MISMATCH | wm43:47-48 · br22:38-44 (`load_workflows`, the one reader, returning the composition) |
| 105 | wm43 | A2 | Rule 7 lives in `tools/roles/spawn-guard.js` (br25 S2) | cite | AGREES | wm43:93-95, :167 · br25:47-50, :195 |
| 106 | wm43 | A2 | `inflight.py` calls roles-kit `load_run_journal`, `load_session_calls`, `NOTIFICATION_RE` and process-monitor's `scan_processes`, `build_self_chain` in process | R3 | MISMATCH | wm43:67, :76-77, :82-83 · oc7:202-205 |
| 107 | wm43 | A2 | The policy kit reads `inflight.mode` as a data file found through `resolve_kit_dir` | R3 | AGREES | wm43:91-92 |
| 108 | wm44 | A2 | `record show` exits 2 on an unknown key, which is where the mirror read hooks in | cite | AGREES | wm44:77 · tr9:106 |
| 109 | wm44 | A2 | `record find --build` can append mirror rows after its local rows | cite | MISMATCH | wm44:79-80 · tr9:94-96, :207-209 |
| 110 | wm44 | A2 | `record_find.py` (memory-tree) may call `read_mirrored` (runtime kit) | R3 | MISMATCH | wm44:71, :92 · oc7:202-205 |
| 111 | wm44 | A2 | `memory.mirror` is read "through `resolve`" in `mirror.py` | R3 | MISMATCH | wm44:48 · oc7:379-380 |
| 112 | wm45 | A2 | The declared fan comes from br22 S1, "as wm43 S2 reads it" | cite | MISMATCH | wm45:57-58 · br22:38-44, :108-109 |
| 113 | wm45 | A2 | `admit` reads the limit with `resolve("runtime.agents-in-flight")` | R3 | MISMATCH | wm45:132 · oc7:379-380 |
| 114 | wm46 | B2 | A stuck item's route draws `route-back` at the transition writer, or `re-dispatch` from `planning`/`designing`. Neither is contention. | R8 | AGREES | wm46:75-81; dl30:43-50, :52-57, :58-61 |
| 115 | wm46 | B2 | AC5 reads the lease as `stale` through `--claims` (the verdict is field 5) | R8 | AGREES | wm46:213-215; pr1:207-208 |
| 116 | wm46 | B2 | `runtime.no-progress` is read through the policy kit's `resolve` inside `progress.py` (outside the hits) | R3 | MISMATCH | wm46:52-53; oc7:202-205, :379-380 |
| 117 | wm46 | B2 | `progress.py` calls the loop kit's `write_transition` and `record_draw` as functions (outside the hits) | R3 | MISMATCH | wm46:75-80, :118; dl3:60-61; dl30:43, :139; oc7:202-205 |
| 118 | wm47 | B2 | The hold ceiling is read through `resolve` (`policy.py:752`) inside `supervise.py` | R3 | MISMATCH | wm47:40-43; oc7:379-380 |
| 119 | wm47 | B2 | Restarts are read through `policy-shim.sh get`, and an act is killed through `reap.py --kill`, both as subprocesses | R3 | AGREES | wm47:64-68, :83-86; oc7:202-205 |
| 120 | wm47 | B2 | This node's leases are picked by `fleet-tag` from `--claims` (field 2) | R8 | AGREES | wm47:47-50; pr1:204-208 |
| 121 | wm48 | A2 | `handoff.py owner-question --kind <k> [--attended]` exists, and `best-effort-recorded` reads as `resolve` | cite | AGREES | wm48:53-57 · br11:60-70 |
| 122 | wm48 | A2 | Every answer of `owner-question` is one of its answer words | cite | MISMATCH | wm48:53-56 · br11:63-65 |
| 123 | wm48 | A2 | `owner_items.py` reads the run keys through `resolve` and `read_catalogue_row` | R3 | MISMATCH | wm48:60-61, :71, :93 · oc7:379-380 |
| 124 | wm49 | B2 | `runtime.refusal-repeats` is read by running `policy.py get` as a subprocess | R3 | AGREES | wm49:30-35; oc7:379-380 |
| 125 | wm49 | B2 | When the breaker opens, the draw is `budget.py draw --cause re-dispatch` through br26's door (ask F3). The cause is in the closed set and is not contention. | R8 | AGREES | wm49:76-80, :305-311; dl30:43-50, :58-61 |
| 126 | wm50 | B3 | `wait_graph.py` (runtime kit) reads a parent's transitions through `read_transitions` | R3 | MISMATCH | wm50:37-38 against dl3:69-74: `read_transitions` is a Python function in the loop kit (`tools/loop/loop_transition.py`, dl3:224) with no read verb. |
| 127 | wm50 | B3 | The release records a move "through `write_transition`" | R3 | MISMATCH | wm50:61 against dl3:60-61, which offers `python tools/loop/loop_transition.py record …`. |
| 128 | wm50 | B3 | `loop_parents.py route` is run as a subprocess and resolved through `resolve_kit_dir` | R3 | AGREES | wm50:59, :71. |
| 129 | wm50 | B3 | Open questions are read from `--mail read`, and the half-deadline from `check_deadline_passed` | R3 | AGREES | `--mail read` is a verb. `check_deadline_passed` is a shell function (pr17:50, :121) reached through wm18's sweep. Neither is an in-process import. |
| 130 | wm50 | B3 | `scan_cycles` is moved to `tools/lib` and carried inline in `backlog.py` and `wait_graph.py` | R3 | AGREES | `tools/lib` is not a sibling kit, and a parity row covers the copies (wm50:44-50). |
| 131 | wm51 | A2 | `record find` returns all of a build's act records with their `Tokens-*` and `Wall` fields | cite | MISMATCH | wm51:38-41 · tr9:94-96 |
| 132 | wm51 | A2 | `measured` holds a stated figure until 30 measured work orders, as tr9 S6 does | cite | AGREES | wm51 §4 · tr9:108-111 |
| 133 | wm51 | A2 | `build.spend-cap` is read by a `policy.py get` subprocess | R3 | AGREES | wm51:34-37 |
| 134 | wm52 | B3 | `write_claim_beat` runs `python beat.py render`, and `beat.py members` runs `unattended.sh --claims` | R3 | AGREES | Both are subprocess calls (wm52:57, :67). |
| 135 | wm52 | B3 | `beat.py members` reads each node's capacity, free slots, load and beat time "through `unattended.sh --claims`" | R8 (outside B3's rule) | MISMATCH | wm52:65-68 against pr1:206-208. |
| 136 | wm53 | A2 | `record find` gives the `Wall` of the act records whose `Item` is a given kind | cite | MISMATCH | wm53:62-65 · tr9:89-96 |
| 137 | wm53 | A2 | `runtime.act-ceiling` and `runtime.admission-scope` are read through `resolve` | R3 | MISMATCH | wm53:65, :71 · oc7:379-380 |
| 138 | wm54 | A2 | A role-schema `[[field]]` row `hardware` is one row (br2 S1) | cite | AGREES | wm54:73-75 · br2:33-38 |
| 139 | wm54 | A2 | `resolve_role_model` reads `roles.model.<role>.<harness>` and raises `RolesError` on a harness with no equivalent | cite/R9 | AGREES | wm54:46, :81-82 · br21:62-65, :134-142 |
| 140 | wm54 | A2 | `roles_lib.py model` answers for "the effective assignment" being checked | cite | MISMATCH | wm54:77-82 · br21:41-44 |
| 141 | wm54 | A2 | A `[[stream]]` lists `units` with `order` (tr25 S2) | cite | AGREES | wm54:57-59 · tr25:40-42 |
| 142 | wm54 | A2 | `--claims` gives each lease's `status` and `offer` | R8 | MISMATCH | wm54:31-33, :63, :113-114 · pr1:206-208 · `unattended.sh:2202` |
| 143 | wm54 | A2 | `discover.py` (runtime kit) calls memory-tree `collect`, and roles-kit `load_workflows`, `resolve_role_model`, `resolve_role_harness`, in process | R3 | MISMATCH | wm54:33-34, :44-46 · oc7:202-205 |
| 144 | wm54 | A2 | The preset check reaches roles through a `roles_lib.py model` subprocess | R3 | AGREES | wm54:81-82 |
| 145 | wm54 | A2 | How `pick` reads the stream-plan record | R2 | UNKNOWN UNTIL BUILT | wm54:57-59 · tr25:34-39, S5-S6 |
| 146 | wm55 | B2 | `policy.py`'s `check_value` reads the runtime kit's `points.toml` as TOML data, finds it through its own inline `resolve_kit_dir`, and never imports it | R3 | AGREES | wm55:82-89; oc7:202-205 |
| 147 | wm56 | A2 | `read_policy_setting` returns None when the key is at its default (br21 S1), which is how `own` is derived | cite | AGREES | wm56:49 · br21:41-47 |
| 148 | wm56 | A2 | The catalogue defaults `claude-code` and `setup-token, oauth-shared` are typed as fallbacks after a None | R9 | MISMATCH | wm56:36-39, :42-44 · br21:41-50 |
| 149 | wm56 | A2 | `launch_act` (runtime) calls `resolve_role_harness`, `resolve_role_auth`, `derive_credential_target`, `check_credential_role` in `roles_lib.py` | R3 | MISMATCH | wm56:53-56 · oc7:202-205 |
| 150 | wm57 | B2 | `gov_record.py` (memory-tree) runs `secret_scan.py payload` as a subprocess found by `resolve_kit_dir`. `scan_secrets` is imported only inside the runtime kit. | R3 | AGREES | wm57:32-36, :41-44; oc7:202-205 |
| 151 | wm58 | A2 | `gov_record.py` is tr2 S1's record door, and gains a `door` verb | cite | AGREES | wm58:40-41 · tr2:39-43 |
| 152 | wm58 | A2 | `record-kinds.toml` is tr1's registry, and a `[[record-kind]]` row registers a kind | cite | AGREES | wm58:101-102 · tr1:62-67 |
| 153 | wm58 | A2 | The door can read the build lease's holder (session) | cite | MISMATCH | wm58:72-74, :91, :106 · tr2:189-196, :335-345 |
| 154 | wm58 | A2 | `quiesce` is a new kind written by `gov_record.py new quiesce`, with no typed join | R2 | MISMATCH | wm58:101-104, :212 · oc42:35-39, :45-50 · tr2:52 · tr1:67-73 |
| 155 | wm58 | A2 | The door reads the binding through a `session_binding.py read` subprocess, and `GOVREF_DOOR` is resolved through `resolve_kit_dir` | R3 | AGREES | wm58:42-45, :55-56 |
| 156 | wm59 | B2 | `cadence.py` reads each host key and `flow.on-exhausted` through `resolve` | R3 | MISMATCH | wm59:47-49, :65-66; oc7:379-380 |
| 157 | wm59 | B2 | `cadence.py` calls the loop kit's `derive_ending`, `budget_state` and `derive_period_budget` in process | R3 | MISMATCH | wm59:51-52, :55-63, :65-66; dl31:40, :150; dl30:222, :235; oc7:202-205 |
| 158 | wm59 | B2 | A period's spend counts every `released` record: each failed lap is one draw, with no contention exclusion | R8 | MISMATCH | wm59:55-62; dl30:58-61 |
| 159 | wm63 | B3 | `GOVREF_DOOR` gains `--node` and `--memory`, and the door is reached by its verb | R3 | AGREES | wm63:30-35; wm58:56 shows `resolve_kit_dir "$py" memory-tree gov_record.py`. |
| 160 | wm63 | B3 | `gov_record.py` (memory-tree) applies `read_host_name`'s rule and `derive_ref_segment` | R3 | AGREES | It restates a rule and loads no module (wm63:41, :47). `derive_ref_segment` is a bash function (pr12:33), and this usage is inherited from wm58:65. |
| 161 | wm64 | B2 | The moved hooks load their renderer from their own kit by `__dirname`; loading it from the sibling unattended kit was rejected | R3 | AGREES | wm64:30-35, :95-96 |
| 162 | wm65 | B3 | `stall-recorder.js` (unattended) runs `journal.py write`, and `supervise.py` runs `journal.py read` | R3 | AGREES | These are subprocess verbs (wm65:34, :40). wm16:63 says the JS producer runs `python journal.py write` "through its resolved" path. |
| 163 | wm79 | B2 | S13, S29 and S40 change, delete and "claim" the runtime legs by hand in `tools/gate-legs.json`. `kit.toml` rows only mirror the manifest, and no leg names its `enforces`. | R1 | MISMATCH | wm79:96-100, :155-160, :204-207, :343; wb11:36-44; oc7:58-63 |
| 164 | wm81 | B2 | `stall-recorder.js` reads the transcript itself; reading it through runlog's extractor in Python was rejected | R3 | AGREES | wm81:31-40, :103-106 |
| 165 | wm90 | B2 | S3, S35 and S37 change a leg's command, its guard and its ceiling by hand in `tools/gate-legs.json` | R1 | MISMATCH | wm90:51-53, :169-170, :174-176, :337; wb11:36-44 |
| 166 | wm90 | B2 | The process-monitor and runlog self-tests read health events through `journal.py read --producer health` | R3 | AGREES | wm90:119-121, :166-168; oc7:202-205 |
| 167 | wm91 | B3 | `readLimitRecord` renders the reset through `lease.renderUtc` | R3 | AGREES | `stall-recorder.js` and `run-lease.js` are in the same kit, unattended (wm91:41-42). |

## The mismatches, both sides quoted

Each reader wrote the bullets for its own specs, with both sides quoted, the `Change:` and the
`Cause:`. They are kept once, in section 2 of each group's return in
[`2026-10-28-build-TOOL-dWellOiledMachine-1-crosscheck-returns`](2026-10-28-build-TOOL-dWellOiledMachine-1-crosscheck-returns.md):
Group A1 (wm3, wm4, wm7, wm8, wm9, wm11, wm16, wm19, wm30, wm32), Group A2 (wm34, wm39, wm42, wm43,
wm44, wm45, wm48, wm51, wm53, wm54, wm56, wm58), Group B1 (wm1, wm2, wm5, wm6, wm10, wm12, wm15, wm17,
wm20, wm23, wm24, wm25, wm26, wm33, wm36), Group B2 (wm41, wm46, wm47, wm59, wm79, wm90) and Group B3
(wm37, wm50, wm52).

## UNKNOWN UNTIL BUILT

- **Row 46 (wm16):** whether a `record-kind.journal` row and tr18's `runlog-journal` witness row can
  share `<git-common-dir>/runlog/`, with tr18's `KIND_ALIASES` keeping `journal`; dTotalRecall's build
  of tr18 S5 and S7 decides it.
- **Rows 54 and 67 (wm19, wm30):** act-form `shape-run` records (`--act`, `Variant`, `Effort`,
  `Rerun`); dTotalRecall's disposal of ask TOOL-dTotalRecall-105 decides it.
- **Row 65 (wm27):** whether `check_record_kinds` admits a `root-until` column; tr1's build decides it.
- **Row 73 (wm32):** whether the door accepts an act record written at the act's exit as the
  lease-holding session; the owner's pick on tr2 F6 and dPlacedRequest's holder verb decide it. The
  same holds for wm19 S6's and wm30 S5's door writes.
- **Row 88 (wm35):** whether the playbook kit loads a `[[native]]` row's `<module>:<name>` in process;
  the build of PLAY-dOrderedCharter-19 and -28 decides it.
- **Row 145 (wm54):** how `pick` reads the stream-plan record; tr25 S5 says none exists until
  dIndexedDesign's planner writes one.
- **Not a table row (wm8 against br5 S3 and S6):** whether wm8's second SubagentStop hold and
  `readKeptReturn` wrap br5's `spawnWithRetries`, so one agent is held up to twice `roles.retries`;
  the landing order and dBoundRoles' build decide it.

## Rule-wide hits the rules do not bind

Section 4 of each rule-wide group's return gives each unbound hit with its reason. Of the 57
candidates, 33 hold no mismatch, only AGREES or UNKNOWN rows or no row at all: wm13, wm14, wm21, wm22,
wm28, wm29, wm31, wm35, wm38, wm40, wm49, wm55, wm57, wm61, wm63, wm64, wm65, wm68, wm74, wm81, wm91,
wm92, wm93, wm94, wm95, wm96, wm97, wm108, wm112, wm115, wm117, wm120 and wm126.

## For the re-ground

Every spec below is revised by one writer of the re-ground brief, for the rows named. The other
mismatch-free specs stay as they are.

By spec: wm1: rows 1, 2 and 3; wm2: 4 and 5; wm3: 9; wm4: 12 and 13; wm5: 15 and 16; wm6: 19 and 20;
wm7: 21 and 24; wm8: 27, 29 and 30; wm9: 31 and 33; wm10: 35; wm11: 37, 38 and 40; wm12: 41; wm15: 43
and 44; wm16: 47; wm17: 49; wm19: 53, 55 and 56; wm20: 57; wm23: 59; wm24: 60; wm25: 61; wm26: 62;
wm30: 68; wm32: 69, 70, 71, 74, 75 and 76; wm33: 77; wm34: 80 and 82; wm36: 89; wm37: 90; wm39: 94 and
95; wm41: 99; wm42: 101; wm43: 103, 104 and 106; wm44: 109, 110 and 111; wm45: 112 and 113; wm46: 116
and 117; wm47: 118; wm48: 122 and 123; wm50: 126 and 127; wm51: 131; wm52: 135; wm53: 136 and 137;
wm54: 140, 142 and 143; wm56: 148 and 149; wm58: 153 and 154; wm59: 156, 157 and 158; wm79: 163; wm90:
165.

- **Group A, led by spec 1:** specs 1, 2, 3, 4, 5, 6, 7, 8 and 9.
- **Group B, led by spec 10:** specs 10, 11, 12, 15, 16, 17, 19, 20, 23 and 24.
- **Group C, led by spec 25:** specs 25, 26, 30, 32, 33, 34, 36, 37 and 39.
- **Group D, led by spec 41:** specs 41, 42, 43, 44, 45, 46, 47 and 48.
- **Group E, led by spec 50:** specs 50, 51, 52, 53, 54, 56, 58, 59, 79 and 90.

## After the re-ground

The five writers' returns, and the four resumed passes, are
[`2026-10-28-build-TOOL-dWellOiledMachine-1-reground-returns`](2026-10-28-build-TOOL-dWellOiledMachine-1-reground-returns.md).
No writer refused a row; each re-read both sides. Row 142 is borne out only in part: `--claims` does
print `status` (field 3), so wm54 corrected only its `offer` read. All 46 specs moved one rev, stay
`DEFERRED` and under 49152 bytes, and each carries one spec-revised deviation record. What they
found beyond the rows:

- **Breaks the record did not row, fixed as writer-found:** wm1 S2 (dBoundRoles' renderer fills no
  `fan` or `script`), wm3 S3 (`write_transition` called by name), wm6 S1 (`derive_position` in
  process), wm25 S5 (`derive_position` in process), wm32 S6 (runlog's `resolve_session_tree`), wm32
  S9 (a leftover `resolve` clause) and wm19 S3 (`load_workflows` in process). Each spec's §9 line
  says "writer-found, not a record row". The probes under-count R3; specs neither population reached
  may hold more.
- **Edits beyond the rows, kept consistent:** wm42 S1 names wm24's `map_reads.py` among the readers
  of `.claude/roles.json`; wm9 and wm45 reserve the stage's `cap`, not its `fan` (br22:108-109); wm51
  reuses wm53's `read_act_records` and gains the edge pair; wm24 reads `writes` from
  `.claude/roles.json` as data, as br1 F6 does.
- **New verbs this build mints in its own kits, with no ask:** `launch.py argv` (wm1),
  `ratify.py disposition` (wm5), `roles_lib.py act` and `credential-check` (wm56), `roles_lib.py
  model --equivalent` and `hardware` (wm54), `budget.py state --key` (wm59), and the inline
  `session_glob_py` block (wm34 F4, also read by wm7 and wm32).
- **One owning fork per asked verb.** A dedupe pass made wm43 F3 the one stage-row ask
  (`handoff.py stage-rows <harness>`, read by wm1, wm7, wm9, wm19, wm45 and wm54), wm30 F3 the one ask
  for a run's started agents, and wm32 F6 the one `record find` cap ask; wm7 F4 was left with nothing
  of its own and is re-resolved.
- **The brief's errors:** R8's cites (above), and its "`--explain` where the spec needs the catalogue
  row": `policy.py get --explain` prints only key, source and reason (`tools/policy/policy.py:1333-1336`),
  which is why wm48 F4 asks for a `--row` mode. The build's spec brief row I31 still names `resolve`
  and `readPolicy`; it is a frozen prompt, not edited.
- **Parent text that looks wrong (not edited):** dl56 S47 names `loop_lib.py disposition --hold` the
  one reader of a disposition record but not what it prints; ks19 S1 gives the shrink-list factory no
  verb another kit can call; pr19 S1's `request.py key` reads only a file; tr11's own `shape-run`
  row carries a `layer`, `readers` and `lifecycle` outside tr18's grammar; tr18's `home` column reds a
  newly registered `fields` kind (wm32's `act`, wm58's `quiesce`) until its first record is committed;
  br1 puts `gov-session` in `layer.runtime` with no registration row naming it (unchecked whether that
  layer is core).

**Forks re-resolved by the writers**, `RESOLVED (agent, 2026-10-28, delegated)` on rung 1: wm1 F1
(`launch.py argv` by subprocess, oc7), wm6 F3 (`position.py --json`), wm7 F3 (TOOL-dBoundRoles-3),
wm7 F4 (folded into the canonical forks), wm9 F2 (`cap`, br22), wm32 F4 and F5 (the act id in the
`Act` field, `--caused-by` the anchor unit), wm34 F4 (the inline transcript block) and wm39 F4 (the
ask restated against tr19 S8's records; it could instead stay open, for the owner to say).

**Forks open for the owner** (24), each with its recommendation in the spec:

- Asks of dBoundRoles: wm7 F5 (where a launch's `script` and `allow` come from), wm26 F5
  (`handoff.py shape-line`), wm30 F3 (`handoff.py agents --json`), wm43 F3 (`handoff.py stage-rows
  <harness>`; it does not yet print each entry's `driver` and `stage`, which wm54 S2 also needs, so the
  ask may widen) and wm43 F4 (`handoff.py run-state`).
- Asks of dPlacedRequest: wm4 F3 (`request.py key -`, a stdin form), wm6 F4 (`epoch` on tr2 F6's
  holder verb) and wm52 F3 (the `node-` keys as `CLAIM_ROWS` columns and a field-printing verb).
  wm58 F5 waits on tr2 F6, already open, and files nothing new.
- Asks of dDeclaredLoop: wm5 F3 (`loop_lib.py disposition --hold` printing the record's path) and
  wm26 F4 (`loop_lib.py declaration <item> --json`, the verb br3 F5 already asks for; one answer
  serves both).
- Ask of dKeptSession: wm2 F4 (a shrink-list verb over a named kit's list).
- Ask of dTotalRecall: wm32 F6 (an uncapped `record find` mode).
- Ask of the playbook kit's owner: wm11 F4 (`render_playbook.py --answers worktree_root` answering
  the node override).
- This build adds the verb: wm43 F5 (`scope.py --self-chain` in process-monitor), wm48 F4
  (`policy.py get --row`) and wm54 F5 (`gen_build_index.py --units`).
- Which principle a new leg enforces (no v2 `[enforcement]` row names its clause): wm1 F4, wm11 F5,
  wm12 F5, wm20 F2, wm23 F4, wm33 F4 and wm39 F6.

`tools/run-gates/leg_factory.py` is not in the tree: every leg spec records that a hand edit of the
manifest stands in for the render until TOOL-dWitnessedBar-11 lands.
