**Serves:** research TOOL-dRankedPlan-1

# dRankedPlan's specs against dBoundRoles' and dTotalRecall's re-grounded specs: a read-only cross-check

Node d, 2026-10-28, base `d1721ef20` (origin/main). dRankedPlan's spec run began at `911a70393`, the
parent of its first spec commit `7f1846d4c`. That base holds dDeclaredLoop's re-ground and the other
second-wave ones, but neither dBoundRoles' (`ac8ab8d5f`, landed as `fffe4aadf`) nor dTotalRecall's
(`794a0f5fb`, landed as `2bd5e10d4`). Their deviation records confirm what each revised: dBoundRoles
units 1, 2, 3, 5, 6, 11, 12, 14, 20, 21, 22, 23, 25, 43 and 60; dTotalRecall units 1, 2, 4, 8, 9, 11,
15, 18, 19, 20, 22, 25, 26, 43 and 76. Every other parent spec is byte-identical between `911a70393`
and `d1721ef20`. Specs 82 and 83 were written after both merges and are out of scope. This record
compares each assumption the exposed specs make about a parent with what the parents' DEFERRED specs
say now. It is not an audit: no spec was edited, no review harness ran, and the mismatches feed the
re-ground brief
[`2026-10-28-prompt-TOOL-dRankedPlan-1-parents-reground`](../prompts/2026-10-28-prompt-TOOL-dRankedPlan-1-parents-reground.md).

**Counts:** 68 assumptions · 42 AGREES · 23 MISMATCH · 3 UNKNOWN UNTIL BUILT, over 46 specs (the 10
citation specs and the 36 rule-wide candidates). 15 specs hold at least one MISMATCH: 1, 2, 3, 4, 9,
13, 15, 16, 21, 22, 24, 29, 31, 37 and 45. By rule: 1 citation, 2 citation and R2, 7 R1, 11 R3 and 2
R4. 15 mismatches, in 10 specs, sit outside the citation population and were found only by rule
scoping: rows in groups B1 and B2 (specs 4, 9, 15, 21, 22, 24, 29, 31, 37 and 45). 2 mismatches come
from a re-ground: rows 12 and 39, the writer cell of a typed kind (tr1 rev-4 and tr2 rev-6 moved it
to the owner's command, else the factory and its flags). The other 21 already read so at
`911a70393`.

## Method

- **Population by citation.** `grep -oE` over `spec/*.md` for the units the two re-grounds revised,
  both `TOOL-<build>-<n>` and the bare `<build>-<n>`: 10 specs.
- **Population by rule.** The brief states R1 to R9, as dWellOiledMachine's cross-check of the same
  day does: dFurnishedOrders' R1 to R8, and R9 for br21's `with_default`. A text probe for each over
  the other 70 specs named 36 candidates. The readers named three R3 breaks outside the probe's R3 hits
  (rp15, rp24 and rp21's `sys.path` precedent); they sit in specs the probe named for another rule.
- **Readers.** Three `gov-spec-reviewer` agents, read-only, one per group of the brief
  [`2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck`](../prompts/2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md),
  their handoffs beside it. Their returns, with every MISMATCH's both sides quoted, its `Change:` and
  its `Cause:`, are
  [`2026-10-28-build-TOOL-dRankedPlan-1-crosscheck-returns`](2026-10-28-build-TOOL-dRankedPlan-1-crosscheck-returns.md).
- **The main loop** assembled the table from the returns' tables by script, sorted by spec, and
  derived the counts from it. It changed no verdict. Group A's prose says 27 assumptions; its table
  holds 32, and the table wins.
- **Aliases:** `rpN:L` is line L of `spec/2026-10-2?-spec-TOOL-dRankedPlan-N.md`; `brN:L`, `trN:L`,
  `dlN:L`, `ksN:L`, `ocN:L`, `wbN:L` and `prN:L` of the parents' spec N under `../../<build>/spec/`;
  all at `d1721ef20`.
- **What it does not check:** anything a parent's build run decides; dSafePassage and dGroundRules
  surfaces the specs name directly; the 34 specs neither population reached. The probe is a text
  heuristic, and dWellOiledMachine's cross-check showed it under-counts R3. No skeptic re-ran the
  verdicts. Instead each re-ground writer re-reads both sides before it edits, and returns a row it
  cannot bear out as refused.

## What the mismatches have in common

- **A sibling kit reached in process (rp1, rp2, rp3, rp9, rp15, rp21, rp22, rp24, rp37).** R3. Policy
  keys read through the policy kit's in-process `resolve` (rp1, rp2, rp9), where memory-tree's adapter
  is tr8 S10's `read_policy_value` in `tools/memory-tree/policy_value.py` and the loop kit runs
  `policy.py get`; memory-tree loading the loop kit by `read_slot_mode`'s `sys.path` precedent (rp21,
  rp22, rp37); the loop kit calling memory-tree's `read_record`, `find_plan_record` and
  `read_bindings` (rp2, rp9, rp15, rp24); memory-tree computing a key with the roles kit's
  `derive_section_sha` (rp3). Pre-existing.
- **A leg written by hand (rp13, rp15, rp29, rp31, rp37, rp45).** R1. The `plan-fields selftest`,
  `loop plan revision` and `session-predicate callers` legs are written into `tools/gate-legs.json`
  beside or instead of their declarations, with no `enforces`; two guards are widened in the manifest.
  wb11 makes the manifest a render. Pre-existing.
- **A typed kind's writer (rp3, rp16).** Citation and R2, from the re-ground: the `triage`, `dupes`
  and `plan` rows name `gov_record.py new <kind>` as their writer, where tr1:187-193 and tr2:296-298
  now take the owner's command, else the factory with `--build`, `--unit` and the kind's flags.
- **The life items' disposition records (rp4, rp24).** R4. rp24's reader keeps only records
  `check_disposition_record` admits, and dl16:59-61 admits nothing for an item with no `[[item]]` row,
  which `item.life.request` and `item.life.close` are (dl13:234-235), so rp4's `dispose` is always held.
  Pre-existing.
- **Single defect:** rp2 S1 writes the planner's limits into its body, where br1:149-150 and br2
  S3's R5 keep every limit in `never`. Pre-existing.

## Summary table

| # | Spec | Group | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|---|---|
| 1 | rp1 | A | `FRONT_MATTER_KEYS` is a dict of `(role, type, required)` that `parse_front_matter` closes, so `priority` joins it as `("authored","rank",False)` | cite | AGREES | rp1:46-48; tr4:38-43, :116-137 |
| 2 | rp1 | A | The `build-readme` row's `fields` must equal the `FRONT_MATTER_KEYS` keys both ways, so `priority` goes into both | cite | AGREES | rp1:46-48, :115; tr1:74-80 (S3: "schema.source whose literal no longer matches the row's fields either way"); tr4:214-225 |
| 3 | rp1 | A | `plan.unplaced` is read in process: `resolve()` from `tools/policy/policy.py`, with the policy kit put on `sys.path` the way `read_slot_mode` does it | R3 | MISMATCH | rp1:75-78, :131-132; oc7:202-205, :379-380; `tools/memory-tree/kit.toml:8` has no `policy` `requires_if` row; `gen_build_index.py:2293-2296` |
| 4 | rp2 | A | br1 S2 creates `gov-planner.agent.md` under a 3072-byte `BODY_CEILINGS` row | cite | AGREES | rp2:41-42; br1:63-67, :150-151 |
| 5 | rp2 | A | br1 S4 adds the `plan` and `design` workflow entries and `WORKFLOW_NAMES`, and writes no `loop.toml` row, so rp2 S2 writes it | cite | AGREES | rp2:46-50, :133-135; br1:80-82 (rev-3 still writes no loop row) |
| 6 | rp2 | A | The planner body may hold the authority limits as prose ("…proposed, never written"), and `check_roles.py` still exits 0 (AC1) | cite | MISMATCH | rp2:41-45, AC1; br1:149-150; br2:44-47 |
| 7 | rp2 | A | `check_ratified_order` reads `plan.authority` through the policy kit's in-process `resolve`, the way `read_slot_mode` does | R3 | MISMATCH | rp2:55-58, Evidence ("the generator already imports a policy-kit module"); oc7:202-205, :379-380 |
| 8 | rp2 | A | `plan_items.py` (loop kit) witnesses `item.plan.research` by calling memory-tree's `read_bindings` (`tree_lib.py:471`) | R3 | MISMATCH | rp2:162; oc7:202-205; the loop kit declares no `requires_if` row for memory-tree |
| 9 | rp2 | A | `item.plan.lease` reads `unattended.sh --claims` by subprocess for a live row held by this node | R3/R8 | AGREES | rp2:164; pr1:124 ("The `--claims` row's node column prints the fleet tag"), :206-208 (fields 1 to 5) |
| 10 | rp2 | A | `check_plan_dupes` calls `derive_request_content_key` inside its own kit | R3 | AGREES | rp2 S6; pr19:144 (`tools/loop/request.py`, the same loop kit) |
| 11 | rp3 | A | `record_kinds.py new triage` / `new dupes` (tr1 S9) appends the row | cite | AGREES | rp3:70-72, :84-86; tr1:101-105 |
| 12 | rp3 | A | The typed `triage` and `dupes` rows carry the writer `gov_record.py new <kind>` | cite/R2 | MISMATCH | rp3:72-73, :86; tr1:187-193, :215; tr2:45-50, :296-298 |
| 13 | rp3 | A | `triage`/`dupes` join `TYPED_RECORD_KINDS`, the factory table and the HYGIENE list (through rp28's hand-off) | R2 | AGREES | rp3:135; rp28 S1-S3 |
| 14 | rp3 | A | `write_new_record` is the door's one function | cite | AGREES | rp3:133; tr2:39-44 |
| 15 | rp3 | A | `triage.py` (memory-tree) computes the `Rows` key with the roles kit's `derive_section_sha` (`tools/roles/handoff.py:307`) | R3 | MISMATCH | rp3:74-75, :439; oc7:202-205 |
| 16 | rp3 | A | `plan.triage` is read by a `policy.py get` subprocess | R3 | AGREES | rp3:44-46; oc7:379-380 |
| 17 | rp4 | B1 | S1 reads each build's newest `transition` record, and S3 reads `disposition` records named under the build's first unit id. Each kind is read under the name its parent serves. | R2 | AGREES | rp4:31-37, :43-46, :111-112; dl3:42-49; dl16:46-56, :123-125 |
| 18 | rp4 | B1 | The three moves' records name `item.life.request` and `item.life.close`. They are read through rp24's reader, which keeps only records `check_disposition_record` admits. | R4 | MISMATCH | rp4:43-46, :80, :105-109; rp24:35-38, :55-60; dl16:57-61; dl13:234-236; dl12:80 |
| 19 | rp4 | B1 | `dispose` records through `write_transition`, with `--witness` set to the commit that added the record. S1 sees a disposal only through the log channel, and the spec states this as a risk with a `NOTE:`. | R8 | AGREES | rp4:43-49, :173-175; dl3:42-49, :54-59, :60-64 |
| 20 | rp5 | B1 | `item.entry.place-owner` declares `outcomes = "dispositions"`, so its `amend` and `continue` records are graded by `check_disposition_record`. | R4 | AGREES | rp5:43-48; pr3:54-57, :157; dl16:57-61 |
| 21 | rp9 | B1 | S1 reads `plan.ratification` through an in-process `resolve("plan.ratification", root)` of `tools/policy/policy.py`. | R3 | MISMATCH | rp9:36-41, :119-120, :274; oc7:202-205, :379-380 |
| 22 | rp9 | B1 | `ratify.py` (loop kit) calls memory-tree's `read_record` (S4) and `find_plan_record` (S5) in process. | R3 | MISMATCH | rp9:56-62, :164; rp16:68-72, :219; oc7:87-91, :202-205 |
| 23 | rp9 | B1 | The `terminal-command` arm reads the `disposition` kind by its `Item` field and by `Channel` = `terminal`. | R2 | AGREES | rp9:56-59; dl16:46-56 |
| 24 | rp9 | B1 | F3: `item.entry.intake` has no `[[item]]` row, and a stand-in row that names no row item is red. | R4 | AGREES | rp9:242-248; dl12:80; dl13:62-65 |
| 25 | rp11 | A | `check_read_set(root, role, keys)` in `record_find.py` sizes a set against `memory.item-budget` (`96` gives 96,000 B), and `memory.over-budget` decides inside it. The report line is `memory over budget: <role> <bytes> B > <cap> B` | cite | AGREES | rp11:50-58, AC3; tr9:108-114 |
| 26 | rp11 | A | `record show` and per-kind section tags resolve `id#tag` keys | cite | AGREES | rp11:31-36; tr9:67-88, :104-107 |
| 27 | rp11 | A | `render_handoff --read <key>` takes the keys | cite | AGREES | rp11:59-61; tr9:119-125 |
| 28 | rp11 | A | `plan_fields.py` imports the loop kit's `read_items` in process | R3 | AGREES | rp11:45-49, S5 declares a `requires_if` row for `loop`, which R3 admits |
| 29 | rp12 | B1 | Reads pr7's `probe-trigger` and `probe` kinds by `Asker`, `Subject`, `Trigger`, `Verdict` and `Kind`. | R2 | AGREES | rp12:51-57; pr7:91-101; tr1:72-73 |
| 30 | rp13 | A | `code_file` carries a `kit` column; the kit is the nearest `tools/<kit>/` holding a `kit.toml`; `code_meta.degraded` means readers fall back to the tree | cite | AGREES | rp13 S3, S5; tr8:66-80, :175 |
| 31 | rp13 | A | The leg `plan-fields selftest` is "declared as a `[[gate_leg]]` in `tools/memory-tree/kit.toml` and in `tools/gate-legs.json`" | R1 | MISMATCH | rp13:91-93, :195-196; wb11:36-49; tr8:100-107 (rev-3 model) |
| 32 | rp13 | A | `scope-paths` reaches `plan_fields.py scope` by a subprocess through an inline `resolve_kit_dir` | R3 | AGREES | rp13 S8; oc7:202-205 |
| 33 | rp14 | B1 | The placement's scenario pin is read through `read_transitions`, which works under any channel set. | R8 | AGREES | rp14:32-37; dl3:69-74 |
| 34 | rp15 | B1 | The new leg `loop plan revision` is written by hand into `tools/gate-legs.json`, and no `enforces` tag is named anywhere. | R1 | MISMATCH | rp15:88-89, :183, :199-202, :279; dl3:75-84; wb11:36-49; oc7:58-63 |
| 35 | rp15 | B1 | A revision is a region of the plan record and adds no kind. | R2 | AGREES | rp15:40-50, :207-208, :289-292 |
| 36 | rp15 | B1 | `revised` joins the outcomes of `item.plan.record` and is routed `transition`. | R4 | AGREES | rp15:35-39; dl12:39-46 |
| 37 | rp15 | B1 | B6 is recorded with `--witness` set to the commit just made. `revision=` rides `TRANSITION_FIELDS` and is read back through `read_transitions`. | R8 | AGREES | rp15:51-67, :137-138; dl3:42-49, :60-64, :69-74 |
| 38 | rp15 | B1 | `plan_revision.py` (loop kit) finds the plan record with memory-tree's `find_plan_record` and reads fields in the factory's `FIELD` form, in process. This is outside the probe's R3 hits. | R3 | MISMATCH | rp15:40-41, :78-79, :195; rp16:68-72; oc7:202-205 |
| 39 | rp16 | A | `record_kinds.py new plan … --writer "gov_record.py new plan"` registers the typed `plan` kind | cite/R2 | MISMATCH | rp16:35-38; tr1:187-193, :215; tr2:45-50, :296-298 |
| 40 | rp16 | A | `plan` joins `TYPED_RECORD_KINDS`, the factory table and the HYGIENE kind list, served as `plan` | R2 | AGREES | rp16 S2 |
| 41 | rp16 | A | `gov_record.py new plan --build --unit --title --field` writes the record, and tr1 S4's generated field check grades it | cite | AGREES | rp16 S3; tr2:39-50; tr1:83-85 |
| 42 | rp16 | A | tr4 closes the README key set, so `read_levels` checks `front-matter:` keys against it | cite | AGREES | rp16:243-244, S5; tr4:38-43 |
| 43 | rp16 | A | The roles kit runs `plan_record.py field` by subprocess, the way tr9 S8 runs `budget` | cite/R3 | AGREES | rp16:89-92, :245-246; tr9:119-122 |
| 44 | rp16 | A | `check_record_kinds` admits a `[[level]]` table in `record-kinds.toml` beside the `[[record-kind]]` rows | cite | UNKNOWN UNTIL BUILT | rp16:74-79; tr1:62-80, :198 (the admitted extras are columns only) |
| 45 | rp21 | B1 | S3: memory-tree's `check_ratified_order` asks the loop kit's `read_exit_ratification`, finding the kit "as `read_slot_mode` finds the policy kit", which means a `sys.path` insert and an `import`. | R3 | MISMATCH | rp21:47-53, :96-97; `tools/memory-tree/gen_build_index.py:2293-2296` at 0689e7fa1; oc7:202-205 |
| 46 | rp21 | B1 | The `ratification` and `harness` fields of the `plan.exit` move are read through `read_transitions`. | R8 | AGREES | rp21:36-42; dl3:42-49, :69-74 |
| 47 | rp22 | B1 | `tools/memory-tree/triage.py` is an admitted in-process caller of `read_plan_ratification(` (loop kit). S2 only recognises a Python call or a shell `ratify.py` line as a caller. | R3 | MISMATCH | rp22:34-46, :48-51; rp3:77; oc7:202-205 |
| 48 | rp24 | B1 | S1 admits records by `check_disposition_record`, and S4 makes it rp4's reader for the `item.life.*` moves. | R4 | MISMATCH | rp24:35-38, :55-60; dl16:57-61; dl13:234-236; dl12:80 |
| 49 | rp24 | B1 | `ratify.py` reads disposition records with memory-tree's `read_record`, in process. This is outside the probe's R3 hits. | R3 | MISMATCH | rp24:36-37, :118; oc7:87-91, :202-205 |
| 50 | rp24 | B1 | `check_disposition_record` admits a releasing word such as `continue` on an `item.plan.exit` record. | R4 | UNKNOWN UNTIL BUILT | rp24:35-38; rp26:26-29, :113-115; dl16:57-61; dl12:39-46; flow-steps.md:190 |
| 51 | rp25 | B1 | AC1 spells `loop_transition.py record … --witness <sha>`. | R8 | AGREES | rp25:116-118; dl3:60-64 |
| 52 | rp26 | B1 | AC1 spells `loop_transition.py record … --witness <sha>`. | R8 | AGREES | rp26:113-115; dl3:60-64 |
| 53 | rp28 | B1 | `triage` and `dupes` join `TYPED_RECORD_KINDS`, the factory table and the HYGIENE closed list. They are written through tr2's door `gov_record.py new <kind>`. Their registry rows come from rp3 through `record_kinds.py new`. | R2 | AGREES | rp28:34-50, :62; oc42 S1-S5; tr1:75-81, :88-91, :186-193 (re-grounded; still agrees); tr2:1, :39; tr4:174, :180-184 |
| 54 | rp29 | B2 | S25 finishes the rows the `plan-fields selftest` leg owes by writing the leg's `chunk` and `ceiling` straight into `tools/gate-legs.json`. | R1 | MISMATCH | rp29:182-186, :336, :445-449; rp13:91-93; wb11:36-42, :43-45, :154 |
| 55 | rp29 | B2 | S26 says it finishes the rows the `loop plan revision` leg owes: the dossier claim, `ceiling-evidence.txt` and `WHOLE_RUN`. AC20 treats that as the full set, but it has no `enforces` and no `[[gate_leg]]` declaration. | R1 | MISMATCH | rp29:187-190, :450; rp15:88, :199; oc7:58-63; wb11:36-42 |
| 56 | rp30 | B2 | The callers' paths are derived through the loop kit's inline `resolve_kit_dir` block. It only builds a path and loads no sibling module. | R3 | AGREES | rp30:41-48, :84-91; oc7:202-205 |
| 57 | rp31 | B2 | The new leg `session-predicate callers (asked only at the act)` gets a `[[gate_leg]]` in the loop kit's `kit.toml` with no `chunk`, plus its own separately written row in `tools/gate-legs.json` that has `chunk` `declarations`. Neither carries `enforces`. | R1 | MISMATCH | rp31:34-44, :106-107; wb11:36-45, :154; oc7:58-63 |
| 58 | rp32 | B2 | The caller check lives in the loop kit and reads files as text and `ast`. It counts the argv-list subprocess form, which R3 requires for a cross-kit call, as a caller. | R3 | AGREES | rp32:24-26, :37-49; oc7:202-205, :379-380 |
| 59 | rp33 | A | The seed writes the plan record through the copied `gov_record.py new plan` in a scratch repository joined to rp9 S7's claim ref | cite | UNKNOWN UNTIL BUILT | rp33:38-42, :88; tr2:188-196, :345 |
| 60 | rp37 | B2 | S13 widens the guards of `build-index selftest` and `loop selftest` by editing `tools/gate-legs.json` and each kit's `[[gate_leg]]` by hand. | R1 | MISMATCH | rp37:106-110, :269, :339-343; wb11:36-45, :154; `tools/memory-tree/kit.toml:277`; dl79:157-158 |
| 61 | rp37 | B2 | S1 and S13: memory-tree's `gen_build_index.py` reaches the loop kit "by `backlog.resolve_kit_dir`, as TOOL-dRankedPlan-21 S3 does", and its `drafts-cross-session` plant imports the loop kit's `ratify.py`. | R3 | MISMATCH | rp37:57-63, :106-108; rp21:47-51; oc7:202-205; `tools/memory-tree/gen_build_index.py:2293-2296`; `tools/memory-tree/kit.toml:8` |
| 62 | rp37 | B2 | Disposition records are read as the typed kind `disposition` (S21, S25). The freshness bound goes to dDeclaredLoop as a backlog ask, and no `new <kind>` door is claimed. | R2 | AGREES | rp37:141-145, :166-170; dl16:45-52 |
| 63 | rp45 | B2 | S6 writes `ceiling = 300` into the manifest row and the descriptor. S7 lists the meta-gates that grade a new leg but leaves out the `enforces` meta-check. S18 widens two guards in the manifest and the descriptors. | R1 | MISMATCH | rp45:90-98, :143-146, :290; wb11:43-45, :52-53, :154; oc7:58-63 |
| 64 | rp45 | B2 | The unattended kit reaches `ratify.py` through `resolve_kit_dir` and runs it as a command (S26, AC20). The in-process forms in S2 and S11 are plant text that the check refuses. | R3 | AGREES | rp45:79, :113, :175-177, :387-389; oc7:202-205 |
| 65 | rp48 | A | tr8 adds the memory-tree kit's copy `tools/memory-tree/extract_code.py` | cite | AGREES | rp48:77-78; tr8:126, :195-196, :205 |
| 66 | rp52 | A | tr8 creates the kit copy `tools/memory-tree/extract_code.py` that units 41 and 45 name | cite | AGREES | rp52:104-107; tr8:205 |
| 67 | rp57 | B2 | The pre-commit hook runs `resolve_kit_gate loop guard.py`, then `"$py" "$g" --staged`. | R7 | AGREES | rp57:44-45, :66-67, :83; dl2:44-49, :100-101 |
| 68 | rp62 | B2 | S12 puts the `spans` keyword into the canonical block `tools/lib/extract_code.py`, and every kit carries a byte-identical copy. The sibling assignment readers are cited, not imported. | R3 | AGREES | rp62:113-118, :175; oc7:202-205 |

## The mismatches, both sides quoted

Each reader wrote the bullets for its own specs, with both sides quoted, the `Change:` and the
`Cause:`. They are kept once, in section 2 of each group's return in
[`2026-10-28-build-TOOL-dRankedPlan-1-crosscheck-returns`](2026-10-28-build-TOOL-dRankedPlan-1-crosscheck-returns.md):
Group A (rp1, rp2, rp3, rp13, rp16), Group B1 (rp4, rp9, rp15, rp21, rp22, rp24) and Group B2 (rp29,
rp31, rp37, rp45).

## UNKNOWN UNTIL BUILT

- **Row 44 (rp16 S5):** whether tr1's `check_record_kinds` admits a top-level `[[level]]` table in
  `record-kinds.toml`; tr1 decides only extra columns (tr1:198), so its built conformance gate decides.
- **Row 50 (rp24, with rp25 and rp26):** whether `check_disposition_record` admits `continue` on an
  `item.plan.exit` record; the outcome set dl12 S2 transcribes for `item.plan.exit` decides, and only
  dDeclaredLoop's build fixes it.
- **Row 59 (rp33 S1):** whether the copied door mints in a scratch repository with no remote holding
  rp9 S7's claim ref; tr2's built minting rung and the owner's pick on tr2 F6 decide.

## Rule-wide hits the rules do not bind

Section 4 of each rule-wide group's return gives each unbound hit with its reason. Of the 36
candidates, 26 hold no mismatch: rp5, rp6, rp7, rp8, rp12, rp14, rp19, rp23, rp25, rp26, rp27, rp28,
rp30, rp32, rp38, rp42, rp51, rp57, rp60, rp61, rp62, rp64, rp67, rp74, rp77 and rp81.

## For the re-ground

Every spec below is revised by one writer of the re-ground brief, for the rows named. The other
mismatch-free specs stay as they are.

By spec: rp1: row 3; rp2: rows 6, 7 and 8; rp3: 12 and 15; rp4: 18; rp9: 21 and 22; rp13: 31; rp15:
34 and 38; rp16: 39; rp21: 45; rp22: 47; rp24: 48 and 49; rp29: 54 and 55; rp31: 57; rp37: 60 and 61;
rp45: 63.

- **Group A, led by spec 1:** specs 1, 2, 3, 4, 9, 15, 16 and 24.
- **Group B, led by spec 13:** specs 13, 21, 22, 29, 31, 37 and 45.

## After the re-ground

The two writers' returns, and Group A's resumed pass, are
[`2026-10-28-build-TOOL-dRankedPlan-1-reground-returns`](2026-10-28-build-TOOL-dRankedPlan-1-reground-returns.md).
No writer refused a row; each re-read both sides. All 15 specs moved one rev, stay `DEFERRED` and
under 49152 bytes, and each carries one spec-revised deviation record. What they found beyond the
rows:

- **A break the record did not row, fixed as writer-found:** rp3 S6 had `triage.py ratify` call the
  loop kit's `read_plan_ratification` in process; it now runs `ratify.py <home>` as a subprocess, as
  rp22 S1 does.
- **The life items (rows 18 and 48):** the writer picked one reader for both specs. rp24 S1 keeps the
  `check_disposition_record` filter only for an item whose outcome set the loop declares, and passes
  records of `item.life.request` and `item.life.close`, which have no `[[item]]` row, unfiltered; rp4
  S3 grades them against its disposal moves and `derive_move` refuses the rest. The other option, a
  second value check inside the reader dl16 S5 owns, is recorded as rejected in rp24 §4.
- **A correction the main loop asked for:** the writers' first pass spelled the typed kinds' writer
  cell `build_records.py new <kind> --build --unit --field`, a door tr1:193 says no parent claims; rp3
  S5 and S7 and rp16 S1 now spell it as tr1:167 spells the `deviation` row's.
- **New surfaces this build owns, with no ask:** `ratify.py <slug> --exited` now ends with a
  `ratifying` / `not ratifying` verdict (rp21 F3), and `ratify.py` gains its own `read_policy_value`
  to oc7 §4's contract (rp9 S1).
- **Parent text that looks wrong (not edited):** dl3 S4 reads `transitions.record` through an
  in-process `resolve(...)` from the loop kit, which oc7:202-205 rules out; rp3 S2 spells `policy.py
  get plan.triage` inside Python, bypassing memory-tree's `read_policy_value` (row 16 judged it
  AGREES, so it was left); rp24 §5 marks UNVERIFIED whether `record find`'s index sees a record
  committed in the same pass.

**Fork re-resolved by a writer**, `RESOLVED (agent, 2026-10-28, delegated)` on rung 1: rp21 F3 (the
crossing's verdict printed on `--exited`'s line, since memory-tree cannot import `RATIFYING_EXITS`).

**Forks open for the owner** (3), each with its recommendation in the spec:

- rp9 F6: which memory-tree verb `ratify.py` finds the plan record by; recommends asking
  TOOL-dRankedPlan-16 for `plan_record.py path <slug>`. rp15 cites it.
- rp15 F8: which principle the `loop plan revision` leg enforces; recommends `principle.p20`, as dl3
  F7 does.
- rp31 F1: which principle the `session-predicate callers` leg enforces; recommends `principle.p2`.

`tools/run-gates/leg_factory.py` is not in the tree: every leg spec records that a hand edit of the
manifest stands in for the render until TOOL-dWitnessedBar-11 lands.

## The owner's picks, 2026-10-29

> take the recommendations on the forks

— owner, 2026-10-29. One `gov-spec-writer` agent, by the brief
[`2026-10-29-prompt-TOOL-dRankedPlan-1-owner-forks`](../prompts/2026-10-29-prompt-TOOL-dRankedPlan-1-owner-forks.md),
marked the three open forks `RESOLVED (owner, 2026-10-29)` to the option each recommends. Its return
is the last section of the re-ground returns record. Specs 9, 15, 16 and 31 each moved one rev and
carry one deviation record.

- rp9 F6 (a): `plan_record.py path <slug>`, a verb unit 16's S4 now adds with its own AC10, read by
  rp9 S5 and rp15. Both units are this build's, so no ask is filed.
- rp15 F8 (a): the `loop plan revision` leg enforces `principle.p20`.
- rp31 F1 (a): the `session-predicate callers` leg enforces `principle.p2`.
