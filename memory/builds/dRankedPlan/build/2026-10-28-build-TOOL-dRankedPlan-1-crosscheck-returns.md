**Serves:** research TOOL-dRankedPlan-1

# dRankedPlan — the cross-check readers' returns, verbatim

The `gov-spec-reviewer` returns the cross-check record [`2026-10-28-build-TOOL-dRankedPlan-1-parents-crosscheck`](2026-10-28-build-TOOL-dRankedPlan-1-parents-crosscheck.md) is assembled from, each copied from its agent transcript by script; only the headings are the main loop's, each returned heading demoted two levels. Group A, citation, read specs 1, 2, 3, 10, 11, 13, 16, 33, 48 and 52; Group B1, rule-wide, read specs 4, 5, 6, 7, 8, 9, 12, 14, 15, 19, 21, 22, 23, 24, 25, 26, 27 and 28; Group B2, rule-wide, read specs 29, 30, 31, 32, 37, 38, 42, 45, 51, 57, 60, 61, 62, 64, 67, 74, 77 and 81.

## Group A

#### Return: Group A, cross-check of dRankedPlan specs 1, 2, 3, 10, 11, 13, 16, 33, 48 and 52 against dBoundRoles and dTotalRecall at `d1721ef20`

**Totals:** 27 assumptions: 18 AGREES, 7 MISMATCH, 2 UNKNOWN UNTIL BUILT. Of the 7 mismatches, 2 trace to the re-ground (both are the writer cell of a typed kind). The other 5 were already there at `911a70393`: one is the role body's prohibition rule, three are sibling-kit reads, and one is a leg written by hand into `tools/gate-legs.json`. Specs 10, 11, 48 and 52 hold no mismatch.

##### 1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 1 | `FRONT_MATTER_KEYS` is a dict of `(role, type, required)` that `parse_front_matter` closes, so `priority` joins it as `("authored","rank",False)` | cite | AGREES | rp1:46-48; tr4:38-43, :116-137 |
| 1 | The `build-readme` row's `fields` must equal the `FRONT_MATTER_KEYS` keys both ways, so `priority` goes into both | cite | AGREES | rp1:46-48, :115; tr1:74-80 (S3: "schema.source whose literal no longer matches the row's fields either way"); tr4:214-225 |
| 1 | `plan.unplaced` is read in process: `resolve()` from `tools/policy/policy.py`, with the policy kit put on `sys.path` the way `read_slot_mode` does it | R3 | MISMATCH | rp1:75-78, :131-132; oc7:202-205, :379-380; `tools/memory-tree/kit.toml:8` has no `policy` `requires_if` row; `gen_build_index.py:2293-2296` |
| 2 | br1 S2 creates `gov-planner.agent.md` under a 3072-byte `BODY_CEILINGS` row | cite | AGREES | rp2:41-42; br1:63-67, :150-151 |
| 2 | br1 S4 adds the `plan` and `design` workflow entries and `WORKFLOW_NAMES`, and writes no `loop.toml` row, so rp2 S2 writes it | cite | AGREES | rp2:46-50, :133-135; br1:80-82 (rev-3 still writes no loop row) |
| 2 | The planner body may hold the authority limits as prose ("…proposed, never written"), and `check_roles.py` still exits 0 (AC1) | cite | MISMATCH | rp2:41-45, AC1; br1:149-150; br2:44-47 |
| 2 | `check_ratified_order` reads `plan.authority` through the policy kit's in-process `resolve`, the way `read_slot_mode` does | R3 | MISMATCH | rp2:55-58, Evidence ("the generator already imports a policy-kit module"); oc7:202-205, :379-380 |
| 2 | `plan_items.py` (loop kit) witnesses `item.plan.research` by calling memory-tree's `read_bindings` (`tree_lib.py:471`) | R3 | MISMATCH | rp2:162; oc7:202-205; the loop kit declares no `requires_if` row for memory-tree |
| 2 | `item.plan.lease` reads `unattended.sh --claims` by subprocess for a live row held by this node | R3/R8 | AGREES | rp2:164; pr1:124 ("The `--claims` row's node column prints the fleet tag"), :206-208 (fields 1 to 5) |
| 2 | `check_plan_dupes` calls `derive_request_content_key` inside its own kit | R3 | AGREES | rp2 S6; pr19:144 (`tools/loop/request.py`, the same loop kit) |
| 3 | `record_kinds.py new triage` / `new dupes` (tr1 S9) appends the row | cite | AGREES | rp3:70-72, :84-86; tr1:101-105 |
| 3 | The typed `triage` and `dupes` rows carry the writer `gov_record.py new <kind>` | cite/R2 | MISMATCH | rp3:72-73, :86; tr1:187-193, :215; tr2:45-50, :296-298 |
| 3 | `triage`/`dupes` join `TYPED_RECORD_KINDS`, the factory table and the HYGIENE list (through rp28's hand-off) | R2 | AGREES | rp3:135; rp28 S1-S3 |
| 3 | `write_new_record` is the door's one function | cite | AGREES | rp3:133; tr2:39-44 |
| 3 | `triage.py` (memory-tree) computes the `Rows` key with the roles kit's `derive_section_sha` (`tools/roles/handoff.py:307`) | R3 | MISMATCH | rp3:74-75, :439; oc7:202-205 |
| 3 | `plan.triage` is read by a `policy.py get` subprocess | R3 | AGREES | rp3:44-46; oc7:379-380 |
| 11 | `check_read_set(root, role, keys)` in `record_find.py` sizes a set against `memory.item-budget` (`96` gives 96,000 B), and `memory.over-budget` decides inside it. The report line is `memory over budget: <role> <bytes> B > <cap> B` | cite | AGREES | rp11:50-58, AC3; tr9:108-114 |
| 11 | `record show` and per-kind section tags resolve `id#tag` keys | cite | AGREES | rp11:31-36; tr9:67-88, :104-107 |
| 11 | `render_handoff --read <key>` takes the keys | cite | AGREES | rp11:59-61; tr9:119-125 |
| 11 | `plan_fields.py` imports the loop kit's `read_items` in process | R3 | AGREES | rp11:45-49, S5 declares a `requires_if` row for `loop`, which R3 admits |
| 13 | `code_file` carries a `kit` column; the kit is the nearest `tools/<kit>/` holding a `kit.toml`; `code_meta.degraded` means readers fall back to the tree | cite | AGREES | rp13 S3, S5; tr8:66-80, :175 |
| 13 | The leg `plan-fields selftest` is "declared as a `[[gate_leg]]` in `tools/memory-tree/kit.toml` and in `tools/gate-legs.json`" | R1 | MISMATCH | rp13:91-93, :195-196; wb11:36-49; tr8:100-107 (rev-3 model) |
| 13 | `scope-paths` reaches `plan_fields.py scope` by a subprocess through an inline `resolve_kit_dir` | R3 | AGREES | rp13 S8; oc7:202-205 |
| 16 | `record_kinds.py new plan … --writer "gov_record.py new plan"` registers the typed `plan` kind | cite/R2 | MISMATCH | rp16:35-38; tr1:187-193, :215; tr2:45-50, :296-298 |
| 16 | `plan` joins `TYPED_RECORD_KINDS`, the factory table and the HYGIENE kind list, served as `plan` | R2 | AGREES | rp16 S2 |
| 16 | `gov_record.py new plan --build --unit --title --field` writes the record, and tr1 S4's generated field check grades it | cite | AGREES | rp16 S3; tr2:39-50; tr1:83-85 |
| 16 | tr4 closes the README key set, so `read_levels` checks `front-matter:` keys against it | cite | AGREES | rp16:243-244, S5; tr4:38-43 |
| 16 | The roles kit runs `plan_record.py field` by subprocess, the way tr9 S8 runs `budget` | cite/R3 | AGREES | rp16:89-92, :245-246; tr9:119-122 |
| 16 | `check_record_kinds` admits a `[[level]]` table in `record-kinds.toml` beside the `[[record-kind]]` rows | cite | UNKNOWN UNTIL BUILT | rp16:74-79; tr1:62-80, :198 (the admitted extras are columns only) |
| 33 | The seed writes the plan record through the copied `gov_record.py new plan` in a scratch repository joined to rp9 S7's claim ref | cite | UNKNOWN UNTIL BUILT | rp33:38-42, :88; tr2:188-196, :345 |
| 48 | tr8 adds the memory-tree kit's copy `tools/memory-tree/extract_code.py` | cite | AGREES | rp48:77-78; tr8:126, :195-196, :205 |
| 52 | tr8 creates the kit copy `tools/memory-tree/extract_code.py` that units 41 and 45 name | cite | AGREES | rp52:104-107; tr8:205 |

##### 2. Mismatches

- **rp1 S6, `plan.unplaced` read in process (R3).** rp1:75-77: "read once per run by `read_plan_unplaced(root)` through the policy reader, `resolve("plan.unplaced", root)` (`tools/policy/policy.py:752`), the kit found by `backlog.resolve_kit_dir("policy", "budgets.py", …)` as `read_slot_mode` (:2283) finds it." The parent side, oc7:202-205: "A kit may not import a sibling kit … finds `policy.py` with it, and runs `<sys.executable> <kit>/policy.py get <key> --explain`". tr8:81-82 adds that memory-tree reads keys through its adapter `tools/memory-tree/policy_value.py`.
  - **Change:** read `plan.unplaced` with `read_policy_value("plan.unplaced", root)` from `tools/memory-tree/policy_value.py` (tr8 S10), which runs `policy.py get`. Drop the in-process `resolve` and the `read_slot_mode` precedent from S6, §4 Evidence and §10.
  - **Cause:** pre-existing (oc7:202, :379 read the same at `911a70393`).

- **rp2 S1, limits in the planner body (cite br1).** rp2:41-45: the body "gains two paragraphs: … the order's authority, one sentence per value of `plan.authority`, ending with the rule that a reorder the planner may not commit is proposed, never written". AC1 then needs `check_roles.py` to exit 0. The parent side, br1:149-150: "Each new body states the role's job … and keeps every limit in `never` (TOOL-dBoundRoles-2 S3)". br2:44-46 adds: "R5 reds a body line carrying a prohibition word (`never`, `do not`, `don't`, `must not` …) … the remedy 'move it to `never`'". S1's own sentence carries "never", so AC1 goes red.
  - **Change:** put each value's refusal and the propose-don't-write rule in `gov-planner`'s `never:` field, as `<limit> — <enforcer>` entries whose enforcer is the `--ratified-order` pre-commit block. Keep only the job in the body, and make AC1 grep the rendered `never` line.
  - **Cause:** pre-existing (br1:141 and br2:41 read so at `911a70393`).

- **rp2 S3, `plan.authority` read in process (R3).** rp2:57: "through the policy kit's `resolve` (I14), as `read_slot_mode` reads its cap". The parent side is oc7:202-205 and :379-380: keys are read "through the policy kit's `get` verb … as a subprocess, the one seam a sibling kit may reach".
  - **Change:** read the key through tr8's `read_policy_value` adapter, a `policy.py get` subprocess. Keep exit 2 on a refused read.
  - **Cause:** pre-existing.

- **rp2 S5, `item.plan.research` reads memory-tree in process (R3).** rp2:162: "a record of kind `research` … read by `read_bindings` (`tools/memory-tree/tree_lib.py:471`)", called from `tools/loop/plan_items.py`. The parent side, oc7:202-205: "A kit may not import a sibling kit". No `requires_if` row in the loop kit admits the call.
  - **Change:** reach memory-tree through a verb by subprocess, for example `gen_build_index.py --print-bindings` (the form rp28 S4 already uses), found through the loop kit's inline `resolve_kit_dir`. The other route is to declare a `requires_if` row for `memory-tree` on the loop kit's descriptor.
  - **Cause:** pre-existing.

- **rp3 S5 and S7, writer of the typed `triage` and `dupes` kinds (cite tr1 and tr2, R2).** rp3:72-73: "written through `gov_record.py new triage`"; rp3:86: "its writer `gov_record.py new dupes`". rp28 S1-S2 makes both kinds typed. The parent side:
  - tr1:187-193: "A factory kind's writer is the command its owning spec names … else the factory with `--build`, `--unit` and the kind's field flags".
  - tr1:215: "each member of `TYPED_RECORD_KINDS` | … | its owner's command, else the factory and its flags".
  - tr2:296-298: "the `deviation` row's writer names the factory".
  - tr2:45-50: the door refuses a kind "whose `writer` names another door", and admits a factory-writer kind as its own.
  - **Change:** set each row's `writer` to the factory with `--build`, `--unit` and the kind's field flags, so `gov_record.py new <kind>` stays the adapter tr2 S2 admits. If rp3 means `triage.py pass`/`ratify` and `plan_items.py dedupe --record` to be the owner's command, name that instead and have those commands call the factory, not `gov_record.py`.
  - **Cause:** the re-ground. tr1 rev-4 and tr2 rev-6 moved the typed-kind writer to "owner's command, else the factory and its flags". At `911a70393`, tr1:197 named `build_records.py new <kind>`.

- **rp3 S5, `Rows` key from the roles kit (R3).** rp3:74: "the key `derive_section_sha` (`tools/roles/handoff.py:307`)", computed in `tools/memory-tree/triage.py`. The parent side, oc7:202-205: "A kit may not import a sibling kit".
  - **Change:** use memory-tree's own `derive_content_key` (tr2:62-66, "the shape of `derive_section_sha`") or an inline 12-hex SHA-256 helper. Update §10.
  - **Cause:** pre-existing.

- **rp13 S10, leg written by hand (R1).** rp13:91-93: "declared as a `[[gate_leg]]` in `tools/memory-tree/kit.toml` and in `tools/gate-legs.json`". Files touched, rp13:196, lists "`tools/gate-legs.json`: S10's leg". The parent side, wb11:36-37: "Each leg is declared exactly once: a `[[gate_leg]]` row in its kit's descriptor". wb11:43-45 adds that `--write` renders `tools/gate-legs.json`, and `--check` exits 1 when the file differs. tr8:100-104 follows the same model.
  - **Change:** declare the leg once, with `leg_factory.py new` into `tools/memory-tree/kit.toml` (keeping `enforces = ["principle.p32"]`), and render `tools/gate-legs.json` with `leg_factory.py --write`. Mark the file "rendered" in Files touched, and add a `leg_factory.py --check` probe. rp29 S25, which edits this leg's `chunk`/`ceiling` in `tools/gate-legs.json`, needs the same fix (group B2's spec).
  - **Cause:** pre-existing (wb11 S1 read so at `911a70393`).

- **rp16 S1, writer of the typed `plan` kind (cite tr1 and tr2, R2).** rp16:35-36: `record_kinds.py new plan --tag record.plan --writer "gov_record.py new plan"`. The parent side is tr1:187-193, :215 and tr2:296-298, as quoted for rp3.
  - **Change:** give the `plan` row the factory-and-flags writer (or a named owner's command that calls the factory). S3's `gov_record.py new plan` stays as the door's adapter call.
  - **Cause:** the re-ground (tr1 rev-4, tr2 rev-6; at `911a70393`, tr1:197 named `build_records.py new <kind>`).

##### 3. Unknown until built

- **rp16 S5:** whether tr1's `check_record_kinds` admits a top-level `[[level]]` table in `record-kinds.toml`. tr1 decides only extra columns (tr1:198), so tr1's built conformance gate decides it.
- **rp33 S1:** whether the copied door mints in a scratch repository with no remote that holds rp9 S7's claim ref. tr2 rev-6 reads the lease from the remote through `read_claims`, and refuses a claim held by another session (tr2:188-196). The holder verb is still open (tr2 F6, :345). tr2's built minting rung and F6's pick decide it, together with whose claimant rp9's fixture plants.

##### 4. Rule-wide hits the rule does not bind

None. Group A is a citation group, and every R-rule hit above lies inside its own specs.

##### 5. Revised parent units cited that no assumption depends on

- **rp1:** none. tr1 and tr4 are both relied on.
- **rp2:** none. br1 is relied on.
- **rp3:** none. tr1 and tr2 are relied on.
- **rp10:** tr1, cited only as F5's rejected option (b) (rp10:335-338).
- **rp11:** none. tr9 is relied on.
- **rp13:** br11, named only in a non-goal ("the fork record's grade is TOOL-dBoundRoles-11's"). tr8 is relied on.
- **rp16:** none. tr1, tr2, tr4 and tr9 are relied on; tr9 only as S7's subprocess precedent.
- **rp33:** none. tr2 is relied on.
- **rp48:** none. tr8 is relied on.
- **rp52:** none. tr8 is relied on.

Files:
- C:\projects\coding-governance\.claude\worktrees\elastic-lalande-a8b091\memory\builds\dRankedPlan\spec\2026-10-26-spec-TOOL-dRankedPlan-1.md
- C:\projects\coding-governance\.claude\worktrees\elastic-lalande-a8b091\memory\builds\dRankedPlan\spec\2026-10-26-spec-TOOL-dRankedPlan-2.md
- C:\projects\coding-governance\.claude\worktrees\elastic-lalande-a8b091\memory\builds\dRankedPlan\spec\2026-10-26-spec-TOOL-dRankedPlan-3.md
- C:\projects\coding-governance\.claude\worktrees\elastic-lalande-a8b091\memory\builds\dRankedPlan\spec\2026-10-26-spec-TOOL-dRankedPlan-13.md
- C:\projects\coding-governance\.claude\worktrees\elastic-lalande-a8b091\memory\builds\dRankedPlan\spec\2026-10-26-spec-TOOL-dRankedPlan-16.md
- C:\projects\coding-governance\.claude\worktrees\elastic-lalande-a8b091\memory\builds\dRankedPlan\spec\2026-10-27-spec-TOOL-dRankedPlan-33.md

## Group B1

1. **Assumptions table**

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| rp4 | S1 reads each build's newest `transition` record, and S3 reads `disposition` records named under the build's first unit id. Each kind is read under the name its parent serves. | R2 | AGREES | rp4:31-37, :43-46, :111-112; dl3:42-49; dl16:46-56, :123-125 |
| rp4 | The three moves' records name `item.life.request` and `item.life.close`. They are read through rp24's reader, which keeps only records `check_disposition_record` admits. | R4 | MISMATCH | rp4:43-46, :80, :105-109; rp24:35-38, :55-60; dl16:57-61; dl13:234-236; dl12:80 |
| rp4 | `dispose` records through `write_transition`, with `--witness` set to the commit that added the record. S1 sees a disposal only through the log channel, and the spec states this as a risk with a `NOTE:`. | R8 | AGREES | rp4:43-49, :173-175; dl3:42-49, :54-59, :60-64 |
| rp5 | `item.entry.place-owner` declares `outcomes = "dispositions"`, so its `amend` and `continue` records are graded by `check_disposition_record`. | R4 | AGREES | rp5:43-48; pr3:54-57, :157; dl16:57-61 |
| rp9 | S1 reads `plan.ratification` through an in-process `resolve("plan.ratification", root)` of `tools/policy/policy.py`. | R3 | MISMATCH | rp9:36-41, :119-120, :274; oc7:202-205, :379-380 |
| rp9 | `ratify.py` (loop kit) calls memory-tree's `read_record` (S4) and `find_plan_record` (S5) in process. | R3 | MISMATCH | rp9:56-62, :164; rp16:68-72, :219; oc7:87-91, :202-205 |
| rp9 | The `terminal-command` arm reads the `disposition` kind by its `Item` field and by `Channel` = `terminal`. | R2 | AGREES | rp9:56-59; dl16:46-56 |
| rp9 | F3: `item.entry.intake` has no `[[item]]` row, and a stand-in row that names no row item is red. | R4 | AGREES | rp9:242-248; dl12:80; dl13:62-65 |
| rp15 | The new leg `loop plan revision` is written by hand into `tools/gate-legs.json`, and no `enforces` tag is named anywhere. | R1 | MISMATCH | rp15:88-89, :183, :199-202, :279; dl3:75-84; wb11:36-49; oc7:58-63 |
| rp15 | A revision is a region of the plan record and adds no kind. | R2 | AGREES | rp15:40-50, :207-208, :289-292 |
| rp15 | `revised` joins the outcomes of `item.plan.record` and is routed `transition`. | R4 | AGREES | rp15:35-39; dl12:39-46 |
| rp15 | B6 is recorded with `--witness` set to the commit just made. `revision=` rides `TRANSITION_FIELDS` and is read back through `read_transitions`. | R8 | AGREES | rp15:51-67, :137-138; dl3:42-49, :60-64, :69-74 |
| rp15 | `plan_revision.py` (loop kit) finds the plan record with memory-tree's `find_plan_record` and reads fields in the factory's `FIELD` form, in process. This is outside the probe's R3 hits. | R3 | MISMATCH | rp15:40-41, :78-79, :195; rp16:68-72; oc7:202-205 |
| rp21 | S3: memory-tree's `check_ratified_order` asks the loop kit's `read_exit_ratification`, finding the kit "as `read_slot_mode` finds the policy kit", which means a `sys.path` insert and an `import`. | R3 | MISMATCH | rp21:47-53, :96-97; `tools/memory-tree/gen_build_index.py:2293-2296` at 0689e7fa1; oc7:202-205 |
| rp21 | The `ratification` and `harness` fields of the `plan.exit` move are read through `read_transitions`. | R8 | AGREES | rp21:36-42; dl3:42-49, :69-74 |
| rp22 | `tools/memory-tree/triage.py` is an admitted in-process caller of `read_plan_ratification(` (loop kit). S2 only recognises a Python call or a shell `ratify.py` line as a caller. | R3 | MISMATCH | rp22:34-46, :48-51; rp3:77; oc7:202-205 |
| rp24 | S1 admits records by `check_disposition_record`, and S4 makes it rp4's reader for the `item.life.*` moves. | R4 | MISMATCH | rp24:35-38, :55-60; dl16:57-61; dl13:234-236; dl12:80 |
| rp24 | `ratify.py` reads disposition records with memory-tree's `read_record`, in process. This is outside the probe's R3 hits. | R3 | MISMATCH | rp24:36-37, :118; oc7:87-91, :202-205 |
| rp24 | `check_disposition_record` admits a releasing word such as `continue` on an `item.plan.exit` record. | R4 | UNKNOWN UNTIL BUILT | rp24:35-38; rp26:26-29, :113-115; dl16:57-61; dl12:39-46; flow-steps.md:190 |
| rp25 | AC1 spells `loop_transition.py record … --witness <sha>`. | R8 | AGREES | rp25:116-118; dl3:60-64 |
| rp26 | AC1 spells `loop_transition.py record … --witness <sha>`. | R8 | AGREES | rp26:113-115; dl3:60-64 |
| rp28 | `triage` and `dupes` join `TYPED_RECORD_KINDS`, the factory table and the HYGIENE closed list. They are written through tr2's door `gov_record.py new <kind>`. Their registry rows come from rp3 through `record_kinds.py new`. | R2 | AGREES | rp28:34-50, :62; oc42 S1-S5; tr1:75-81, :88-91, :186-193 (re-grounded; still agrees); tr2:1, :39; tr4:174, :180-184 |
| rp14 | The placement's scenario pin is read through `read_transitions`, which works under any channel set. | R8 | AGREES | rp14:32-37; dl3:69-74 |
| rp12 | Reads pr7's `probe-trigger` and `probe` kinds by `Asker`, `Subject`, `Trigger`, `Verdict` and `Kind`. | R2 | AGREES | rp12:51-57; pr7:91-101; tr1:72-73 |

2. **Mismatches**

- **rp4 and rp24, R4 (life items).**
  - rp4:105-109: "`**Item:** item.life.request`, `**Disposition:** pause`… `**Item:** item.life.close`, `**Disposition:** withdrawn`".
  - rp24:37-38: "keeps those whose `Item` is `item` and which `check_disposition_record` admits".
  - rp24:55-58: "`read_build_disposition` is built on S1, asking it once per item of its three moves".
  - Against: dl16:59-61: "`read_outcome_set(item)` … nothing for an item the definition does not declare, printed `unarmed`, never green".
  - And: dl13:234-235: "An item outside the five programs, `item.entry.claim`, `item.life.request` and `item.life.close`, has no `[[item]]` row".
  - Effect: every rp4 disposal record is filtered out, so `dispose` is always held and AC3 cannot go green.
  - Change: rp24 S1 should admit a record for an item with no `[[item]]` row against the move tables instead (B19, B20, T11 and T12 through `derive_move`). Or rp4 should take its records from rp24 without the `check_disposition_record` filter and rely on `derive_move`'s refusal. rp4 S3 should say which.
  - Cause: pre-existing.
- **rp9, R3 (policy read).**
  - rp9:37-38: "read once through the policy reader, `resolve("plan.ratification", root)` (`tools/policy/policy.py:752`)".
  - Against: oc7:379-380: "policy keys are read through the policy kit's `get` verb … as a subprocess, the one seam a sibling kit may reach".
  - Change: read the key by running `<policy kit>/policy.py get plan.ratification` as a bounded subprocess, with the policy kit found through an inline `resolve_kit_dir`. Exit 2 maps to S1's refusal.
  - rp9 §4 Evidence (:119-120) justifies `resolve(` by reader coverage. That coverage question has to be answered for the subprocess form, as rp7 F5 and rp8 F6 do for theirs.
  - Cause: pre-existing.
- **rp9, R3 (memory-tree in process).**
  - rp9:57-58: "read by the record factory's `read_record` (PLAY-dOrderedCharter-7 S7)".
  - rp9:61-62: "the file `find_plan_record` returns (TOOL-dRankedPlan-16 S4)".
  - Both functions live in memory-tree (`build_records.py`, and `plan_record.py` per rp16:219), while rp9's code lives in `tools/loop/ratify.py`.
  - Against: oc7:202-203: "A kit may not import a sibling kit".
  - Change: reach both through memory-tree verbs as subprocesses found by `resolve_kit_dir`. One way is a `plan_record.py` verb that prints the record path, asked of rp16; another is tr9's `gov_record.py find`/`show`. The alternative is a declared `requires_if` row.
  - Cause: pre-existing.
- **rp15, R1.**
  - rp15:88-89: "The leg `loop plan revision` runs it, with the rows a new leg owes, as TOOL-dDeclaredLoop-3 S8 adds its own".
  - rp15:199: "`tools/gate-legs.json`: the leg `loop plan revision`". No `enforces` tag appears anywhere in the spec.
  - Against: wb11:36-38: "Each leg is declared exactly once: a `[[gate_leg]]` row in its kit's descriptor … else an `[[exempt_leg]]` row".
  - And: wb11:45-46: "`--write` renders `tools/gate-legs.json`".
  - And: oc7:60-61: "a leg carrying no `enforces` is red", with only a shrink-only pending list to excuse it.
  - And: dl3:75-78, which names `enforces` among the rows and settles the tag in an §8 fork.
  - Change: declare the leg once, as a `[[gate_leg]]` row in `tools/loop/kit.toml` or an `[[exempt_leg]]` row, with every manifest key and a named `enforces` tag. Settle the tag in a new §8 fork, as dl3 F7 does for cl-dClosedLoop-0088. Render `tools/gate-legs.json` with `leg_factory.py --write`. Until wb11's factory lands (`tools/run-gates/leg_factory.py` is absent from the tree), record the hand edit as a stand-in.
  - Cause: pre-existing.
- **rp15, R3 (beyond the probe's hits).**
  - rp15:41: "found by `find_plan_record(root, slug)` (unit 16 S4)".
  - rp15:79: "read by `git show <from>:<path>` in the factory's `FIELD` form". The code is `tools/loop/plan_revision.py` (rp15:195), and both names live in memory-tree.
  - Against: oc7:202-203.
  - Change: find the record and read its fields through `plan_record.py` verbs (`field`, plus a path verb) run as subprocesses via `resolve_kit_dir`, as rp14 S1 already does.
  - Cause: pre-existing.
- **rp21, R3.**
  - rp21:50-52: "read once per build per run, the loop kit found by `backlog.resolve_kit_dir` as `read_slot_mode` finds the policy kit".
  - That precedent does `sys.path.insert(0, kit)` and `import budgets` (`gen_build_index.py:2293-2296` at 0689e7fa1), so rp21 imports `ratify.py` into memory-tree.
  - Against: oc7:202-203. The brief's R3 also names a `sys.path` insert as a MISMATCH.
  - Change: S3 runs `ratify.py <slug> --exited` (rp21's own S1 CLI) as a bounded subprocess and parses its `plan.exit — crossed · <how> …` line against `RATIFYING_EXITS`. The S4 plant and rp37's "guards S4's import" are re-spelled to match.
  - Cause: pre-existing.
- **rp22, R3.**
  - rp22:36-38: "`tools/memory-tree/triage.py`, where `TOOL-dRankedPlan-3` S6 asks at the owner-batches write".
  - rp22:50-51: "the same line [`read_plan_ratification(`] in a planted `tools/memory-tree/triage.py` is admitted". Following rp3:77, that is an in-process call from memory-tree into the loop kit.
  - Against: oc7:202-203.
  - Change: S1's entry and the S3 plant spell the subprocess form, `ratify.py <slug>` found through `resolve_kit_dir`. S2's caller definition (rp22:41-45) must then also catch a Python subprocess argv naming `ratify.py` with no `--` argument. Today it catches only shell lines, so the forced subprocess form would escape the gate.
  - Cause: pre-existing.
- **rp24, R3 (beyond the probe's hits).**
  - rp24:36-37: "through the record factory's `read_record` (PLAY-dOrderedCharter-7 S7)", in `tools/loop/ratify.py`.
  - Against: oc7:202-203.
  - Change: the same memory-tree subprocess route as rp9's change.
  - Cause: pre-existing.

3. **UNKNOWN UNTIL BUILT**

- **rp24 (and rp25, rp26):** does `check_disposition_record` admit `continue` on an `item.plan.exit` record? That depends on the outcome set dl12 S2 transcribes for `item.plan.exit` from flow-steps.md:190, whose Then cell reads only "Design" and whose move is B4's `pass`. Only dDeclaredLoop's build decides between `"dispositions"` and a list. If it is a list, rp26 AC1's `continue` record is never admitted.

4. **Rule-wide hits the rule does not bind**

- rp27 R1: reads the existing `kit epoch` leg's `reads.base`; adds and reshapes no leg.
- rp6 R2: reads the `plan` kind of its own unit 16, not a parent's kind.
- rp6 R4: names `item.plan.record` and `item.plan.exit` only; adds no loop row.
- rp14 R2: no kind added; plan fields are read through rp16's `plan_record.py field`.
- rp14 R4: no loop row; S3 extends dl27's `derive_step_scenarios`.
- rp12 R4: names `item.plan.record` and `item.probe.pin` as asker and reader; adds no row.
- rp12 R8: "witness" means `item.plan.record`'s item witness, not dl3's channels.
- rp21 R2: line 135 rejects a second record kind; none is added.
- rp5 R8: `Channel` here is dl16 S4's disposition channel; `prompt` and `terminal` are both members.
- rp7 R8: "R8" is a route rule and "byte budget" is prose size, not dl33.
- rp7 R9: kickoff kit, not the roles kit; it reads through pr2's `read_card_policy`.
- rp8 R9: kickoff kit, not the roles kit; the catalogue-default verdict follows pr2 S11.
- rp9 R8: "witness" is the ratification evidence line.
- rp9 R9: loop kit, not the roles kit; R3 applies, as recorded above.
- rp19 R8: "witness" is `item.plan.record`'s witness line from `plan_record.py check`.
- rp22 R8: "budget row" is the selftest-budgets file, and "witness" is ratification.
- rp23 R8: "witness" is ratification; transitions are reached through rp21's reader.

5. **Per citation spec:** none. This is rule-wide group B1, with no citation specs.

The parent spec trees for dDeclaredLoop, dOrderedCharter, dWitnessedBar, dPlacedRequest and dKeptSession are unchanged between `911a70393` and `d1721ef20`: `git diff --stat` printed nothing. That is why every mismatch above is pre-existing. The one re-grounded text touched, tr1, still agrees with rp28.

Files read: `C:\projects\coding-governance\.claude\worktrees\elastic-lalande-a8b091\memory\builds\dRankedPlan\spec\2026-10-26-spec-TOOL-dRankedPlan-{4,5,6,7,8,9,12,14,15,19,21,22,23,24,25,26,27,28}.md`

## Group B2

1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 29 | S25 finishes the rows the `plan-fields selftest` leg owes by writing the leg's `chunk` and `ceiling` straight into `tools/gate-legs.json`. | R1 | MISMATCH | rp29:182-186, :336, :445-449; rp13:91-93; wb11:36-42, :43-45, :154 |
| 29 | S26 says it finishes the rows the `loop plan revision` leg owes: the dossier claim, `ceiling-evidence.txt` and `WHOLE_RUN`. AC20 treats that as the full set, but it has no `enforces` and no `[[gate_leg]]` declaration. | R1 | MISMATCH | rp29:187-190, :450; rp15:88, :199; oc7:58-63; wb11:36-42 |
| 31 | The new leg `session-predicate callers (asked only at the act)` gets a `[[gate_leg]]` in the loop kit's `kit.toml` with no `chunk`, plus its own separately written row in `tools/gate-legs.json` that has `chunk` `declarations`. Neither carries `enforces`. | R1 | MISMATCH | rp31:34-44, :106-107; wb11:36-45, :154; oc7:58-63 |
| 37 | S13 widens the guards of `build-index selftest` and `loop selftest` by editing `tools/gate-legs.json` and each kit's `[[gate_leg]]` by hand. | R1 | MISMATCH | rp37:106-110, :269, :339-343; wb11:36-45, :154; `tools/memory-tree/kit.toml:277`; dl79:157-158 |
| 45 | S6 writes `ceiling = 300` into the manifest row and the descriptor. S7 lists the meta-gates that grade a new leg but leaves out the `enforces` meta-check. S18 widens two guards in the manifest and the descriptors. | R1 | MISMATCH | rp45:90-98, :143-146, :290; wb11:43-45, :52-53, :154; oc7:58-63 |
| 37 | S1 and S13: memory-tree's `gen_build_index.py` reaches the loop kit "by `backlog.resolve_kit_dir`, as TOOL-dRankedPlan-21 S3 does", and its `drafts-cross-session` plant imports the loop kit's `ratify.py`. | R3 | MISMATCH | rp37:57-63, :106-108; rp21:47-51; oc7:202-205; `tools/memory-tree/gen_build_index.py:2293-2296`; `tools/memory-tree/kit.toml:8` |
| 37 | Disposition records are read as the typed kind `disposition` (S21, S25). The freshness bound goes to dDeclaredLoop as a backlog ask, and no `new <kind>` door is claimed. | R2 | AGREES | rp37:141-145, :166-170; dl16:45-52 |
| 30 | The callers' paths are derived through the loop kit's inline `resolve_kit_dir` block. It only builds a path and loads no sibling module. | R3 | AGREES | rp30:41-48, :84-91; oc7:202-205 |
| 32 | The caller check lives in the loop kit and reads files as text and `ast`. It counts the argv-list subprocess form, which R3 requires for a cross-kit call, as a caller. | R3 | AGREES | rp32:24-26, :37-49; oc7:202-205, :379-380 |
| 45 | The unattended kit reaches `ratify.py` through `resolve_kit_dir` and runs it as a command (S26, AC20). The in-process forms in S2 and S11 are plant text that the check refuses. | R3 | AGREES | rp45:79, :113, :175-177, :387-389; oc7:202-205 |
| 62 | S12 puts the `spans` keyword into the canonical block `tools/lib/extract_code.py`, and every kit carries a byte-identical copy. The sibling assignment readers are cited, not imported. | R3 | AGREES | rp62:113-118, :175; oc7:202-205 |
| 57 | The pre-commit hook runs `resolve_kit_gate loop guard.py`, then `"$py" "$g" --staged`. | R7 | AGREES | rp57:44-45, :66-67, :83; dl2:44-49, :100-101 |

2. MISMATCHES

- **rp29 S25.** The spec reads: "its manifest row's `chunk` and `ceiling` in `tools/gate-legs.json`" (rp29:185-186). Its Files touched names `tools/gate-legs.json` for S25 but not the memory-tree `kit.toml` (rp29:335-336), and AC20 probes the manifest (rp29:448-449). The parent reads: "A declaration holds every manifest key its leg carries: `name`, `argv`, `guard`, `chunk`, `subject`, `ceiling`, …" (wb11:39-41). It also reads "`--write` renders `tools/gate-legs.json` from every declaration; `--check` exits 1 when the file differs" (wb11:43-44). The `fresh` arm reds "the manifest differs from the render" (wb11:154). The leg is a `[[gate_leg]]` of `tools/memory-tree/kit.toml` (rp13:92).
  Change: S25 puts `chunk` and `ceiling` on the leg's `[[gate_leg]]` row in `tools/memory-tree/kit.toml` and renders the manifest with `leg_factory.py --write`. Files touched names the descriptor, and AC20 reads both the descriptor and `leg_factory.py --check` exit 0.
  Cause: pre-existing. wb11 and oc7 are byte-unchanged between `911a70393` and `d1721ef20`.

- **rp29 S26.** S26 lists the `loop plan revision` leg's owed rows as "its claim in the `gate-legs` list …, its `tools/run-gates/ceiling-evidence.txt` row, and its `WHOLE_RUN` entry" (rp29:187-190), and AC20's red case is "a new leg lacks a row it owes" (rp29:450). The leg itself is added to `tools/gate-legs.json` alone (rp15:199). The parent reads: "a leg carrying no `enforces` is red. Each red is excused only by a row of the shrink-only pending list" (oc7:60-62). It also says each leg is declared once, "a `[[gate_leg]]` row in its kit's descriptor" (wb11:36-37).
  Change: S26's set adds the leg's `[[gate_leg]]` in `tools/loop/kit.toml`, with an `enforces` list naming real `principle.*`/`practice.*` tags, rendered by `leg_factory.py --write`. AC20 checks that `core.py meta-check` names no `leg` red for `loop plan revision`.
  Cause: pre-existing.

- **rp31 S1 and S2.** S1 declares "A `[[gate_leg]]` in `tools/loop/kit.toml` … `subject = "repo"`, `argv = …` and `guard = []`. Its row in `tools/gate-legs.json` carries the same name, argv …, `subject` `repo`, `chunk` `declarations`" (rp31:34-38). Files touched lists the two as separate edits (rp31:106-107), and no `enforces` appears anywhere in the spec. The parent's declaration holds every key, `chunk` and `enforces` included (wb11:39-41); the manifest is a render (wb11:43-44); and oc7 S3 reds a leg with no `enforces` (oc7:60-61). As written, the descriptor lacks `chunk`, so the render differs from the hand-written row and `fresh` reds (wb11:154).
  Change: S1 declares `chunk = "declarations"`, `ceiling` (as rp45 S6 adds) and `enforces = [...]` on the `[[gate_leg]]` row, and replaces the manifest row with `leg_factory.py --write`. S2's owed-rows list adds `enforces`, and AC1 also reads the descriptor.
  Cause: pre-existing. rp31 S2 copies dl75 S21's list (dl75:125-129), which also omits `enforces`, but oc7 binds every leg.

- **rp37 S13.** S13 reads: "Two guards widen, in `tools/gate-legs.json` and in their kits' `[[gate_leg]]` entries" (rp37:106-107), Files touched lists `tools/gate-legs.json` as an edited file (rp37:269), and AC11 reads both (rp37:339-342). The parent says the manifest is rendered from the declarations and `--check` reds any difference (wb11:43-44, :154). `build-index selftest` is declared at `tools/memory-tree/kit.toml:277`, and `loop selftest` in `tools/loop/kit.toml` (dl79:157-158).
  Change: S13 widens each guard in the declaring `[[gate_leg]]` only, using a `[gate_leg.gov]` sub-table where gov's value differs (wb11:41-42), and runs `leg_factory.py --write`. Files touched names the manifest as a render, and AC11 adds `leg_factory.py --check` exit 0.
  Cause: pre-existing.

- **rp45 S6, S7 and S18.** S6 reads: "The row … in `tools/gate-legs.json`, and its `[[gate_leg]]` in `tools/loop/kit.toml`, each carry `ceiling = 300`" (rp45:90-92). S7 lists "`govkit selfcheck`, `codebase-map coverage + freshness` and `leg ceilings clear their evidenced maximum`, the unguarded meta-gates that grade a new leg" (rp45:96-98). S18 reads: "Two guards widen in `tools/gate-legs.json` and in their kits' `[[gate_leg]]`" (rp45:143). The parent: wb11:43-44 and :154 make the manifest a render, and oc7:58-63 adds the `core.py meta-check` red for a leg without `enforces`. wb11 S4's leg `gate-leg conformance` grades each declaration (wb11:51-53).
  Change: S6 and S18 edit the declarations only and render the manifest with `leg_factory.py --write`. S7's list adds `gate-leg conformance` and the playbook meta-check leg, and AC5 requires the new leg's `enforces`.
  Cause: pre-existing.

- **rp37 S1 and S13, R3.** S1 reads: "The generator reaches the loop kit by `backlog.resolve_kit_dir`, as `TOOL-dRankedPlan-21` S3 does" (rp37:62-63). S13 reads: "`{prefix}/loop/ratify.py`, which `TOOL-dRankedPlan-21` S4's plant imports" (rp37:107-108). rp21 S3 copies `read_slot_mode` (rp21:49-51), and that function does `sys.path.insert(0, kit)` and then `import budgets` (`gen_build_index.py:2293-2296`), an in-process load. The parent reads: "A kit may not import a sibling kit (TOOL-dGroundRules-1, §4 Evidence)" (oc7:202), and a policy key is read through `get` "as a subprocess, the one seam a sibling kit may reach" (oc7:379-380). `tools/memory-tree/kit.toml:8` holds no `requires_if` row for the loop kit.
  Change: S1 has the generator and its plant run the loop kit's CLIs as subprocesses, found through `resolve_kit_dir`: `ratify.py <slug> --exited` (rp21:41-42) and `ratify.py --fixture --seed`. S13 then says the plant "runs" `ratify.py`, not "imports" it; the guard widening still stands. The alternative is a declared `requires_if` row for `loop` in `tools/memory-tree/kit.toml`.
  Cause: pre-existing. oc7 is unchanged since `911a70393`.

3. UNKNOWN UNTIL BUILT

None.

4. Hits the rule does not bind

- rp29, R8: "witness" is the plan-ratification witness (rp29:78-82, :211-212), and "budget" is `selftest-budgets.txt` (rp29:183). `refs/gov/claims/*` is dPlacedRequest-21's claim ref, not a lease. The spec uses no dl3 channel, no dl33 edge and no `--claims` read.
- rp37, R8: "witness" is the `ratification=witness` value and the `ratified · witness` output (rp37:73-84).
- rp45, R8: the hits are `seed_plan_witness` and `selftest-budgets.txt` (rp45:99, :197, :396-398).
- rp29, R9: the roles-kit files it touches read no policy key. `handoff.py` (S33) reads `plan_record.py field` by exit code, which is a subprocess and fits R3, and `adopt-roles.test.sh` (S22) reads a TOML literal. Its policy reads sit in the memory-tree and loop kits (`triage.py`, `ratify.py`, `gen_build_index.py`; rp29:92-102, :128-132, :231-233), where R3 rules, and units 1, 3 and 9 decide how those reads are made.
- rp60, R9: the hits are "deny-by-default" and evidence citing `policy-mirror.js` (rp60:22, :64). The only code it touches is `ratify.py`, which reads no policy.
- rp61, R1: it only reads `tools/gate-legs.json` (rp61:79) and moves spec leg lines. No leg is added or changed.
- rp62, R1: it reads the manifest for `loop selftest`, and S4's manifest edit happens in a scratch clone fixture (rp62:71-81). The tree's legs are untouched.
- rp37, R3, other hits: S22 imports `RATIFYING_EXITS` inside the loop kit (rp37:146-147), and S23's `tree_lib.py` import stays inside memory-tree (rp37:151-152).
- rp38, R3: the in-process forms are plant text the check refuses (rp38:44-48). The only code touched is `ratify.py`.
- rp42, R3: "two in-process calls" are `gen_build_index.py`'s own `_read_asks_run` inside its own selftest (rp42:30-34, :90).
- rp51, rp74, rp81, R3: an AC probe imports the loop kit's own module (rp51:144, rp74:141, rp81:237, :247).
- rp67, R3: the `sys.path.insert(0, "tools/memory-tree"); import design_lib` line is a population command run from the repository root (rp67:395-403), not kit code. The only code touched is plants in `ratify.py`.
- rp77, R3: `design_lib` is imported by unit 67's population command (rp77:114-118), and the lexicon lines are cited as evidence (rp77:126, :133).
- rp64, R7: `guard.py` is a string inside a JS plant (rp64:43-45, :79). The spec claims nothing about the guard's verdict or trailer.

5. Citation specs

None. Group B2 is rule-wide and holds no citation spec.

