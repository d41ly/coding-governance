**Serves:** research TOOL-dBoundRoles-1

# dBoundRoles's specs against dDeclaredLoop's, dWitnessedBar's and dPlacedRequest's re-grounded specs: a read-only cross-check

Node d, 2026-10-26, base `c8d46e188` (origin/main). dBoundRoles's spec run began at `4283cb44f`, the
parent of its first spec commit `4914545b1`. That base holds none of its parents' re-grounds:
dDeclaredLoop's (`783f1ad3a`, landed as `e5de11e9e`), dWitnessedBar's (`443775a2f`, landed as
`191ba7ab5`) or dPlacedRequest's (`2740f0a3d`, landed as `60d90cb71`). Their deviation records confirm
what each revised: dDeclaredLoop units 1 to 6, 12, 16, 17, 18, 22, 24 to 28, 33, 34, 46 and 56;
dWitnessedBar units 1, 3, 6, 8, 11, 12, 14, 15, 16, 18, 23, 25, 28, 51 and 56; dPlacedRequest units 1
to 7, 9, 21 and 34. This record compares each assumption the exposed specs make about a parent with
what the parents' DEFERRED specs say now. It is not an audit: no spec was edited, no review harness
ran, and the mismatches feed the re-ground brief
[`2026-10-26-prompt-TOOL-dBoundRoles-1-parents-reground`](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-parents-reground.md).

**Counts:** 53 assumptions · 27 AGREES · 23 MISMATCH · 3 UNKNOWN UNTIL BUILT, over 35 specs. 15
specs hold at least one MISMATCH: 1, 2, 3, 5, 6, 11, 12, 14, 20, 21, 22, 23, 25, 43 and 60. The other 20 agree throughout or are not bound: 9, 15, 16, 17, 24, 37, 42, 49, 50, 54, 55, 56, 57, 58, 59, 62, 63, 64, 66 and 69. 4
mismatches come from a re-ground: dl18's dropped `resolve` import precedent (br21 F2, and through it
br22 S5 and br43 S21) and wb28 S5's "a govkit module imports no playbook module" (br43 S23). The other
19 were already mismatches at `4283cb44f`.

## Method

- **Population by citation.** `grep -oE` over `spec/*.md` for the units the three re-grounds revised,
  both `TOOL-<build>-<n>` and the bare `<build>-<n>`. That gives 14 specs.
- **Population by rule.** The last wave found that citation misses a rule a parent applies to every
  spec: dOrderedCharter unit 7 S3 reds a leg with no `enforces`, and 13 dDeclaredLoop units broke it
  without citing unit 7. The brief names eight such rules, R1 to R8, read from the three parents'
  cross-check records. A text probe for each rule over the other 45 specs named 21 candidates. The
  rough leg probe the hand-off quoted (10 of 10 leg-naming specs never say `enforces`) is among them;
  the reader found that only br25 and br60 add or reshape a leg row, and the rest name existing legs
  on a §7 line, in a risk or in a probe.
- **Readers.** Two `gov-spec-reviewer` agents, read-only, one per group of the brief
  [`2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck`](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md),
  their handoffs beside it. Group A is the citation population and also applied R1 to R8 to its own
  specs; group B verified the rule-wide hits, and reported three R3 rows outside the probe's hits (br3,
  br6, br25), each marked in its return. Their returns are
  [`2026-10-26-build-TOOL-dBoundRoles-1-crosscheck-returns`](2026-10-26-build-TOOL-dBoundRoles-1-crosscheck-returns.md).
- **The main loop** assembled the table, sorted by spec, and derived the counts from it. It changed no
  verdict. Group A's prose summary counts 18, 14 and 3; its table holds 25, 17 and 3, because several
  rows carry two rules, and the table is what this record counts.
- **Aliases:** `brN:L` is line L of `spec/2026-10-2?-spec-TOOL-dBoundRoles-N.md`; `dlN:L`, `wbN:L`,
  `prN:L` and `ocN:L` of the parents' spec N under `../../<build>/spec/`; all at `c8d46e188`.
- **What it does not check:** anything a parent's build run decides; dSafePassage and dGroundRules
  surfaces dBoundRoles names directly; specs neither population reached. The rule-wide probe is a text
  heuristic, so a spec that breaks a rule without using any of its probe words is missed. No skeptic
  re-ran the verdicts. Instead each re-ground writer re-reads both sides before it edits, and returns a
  row it cannot bear out as refused.

## What the mismatches have in common

- **A sibling kit reached in process (br1, br3, br5, br11, br12, br14, br20, br21, br22, br25, br43).**
  R3. The roles kit is imported by the playbook kit (br1, br14) and the loop kit (br12, br20, br43),
  and the roles kit imports the playbook kit's composer (br20) and the hooks kit's module (br25). Policy
  keys are read through an in-process `resolve` (br5, br11, br21, br22, br43), where oc7:379-380 makes
  `policy.py get` by subprocess "the one seam a sibling kit may reach"; br15 S6 already reads so. br3
  runs the loop kit by subprocess but names a verb dl9 does not have. Four from the re-ground (br21,
  br22 S5, br43 twice); the rest pre-existing.
- **A leg row written by hand (br25, br60).** R1. Both edit `tools/gate-legs.json` with no `enforces`,
  where oc7 S3 reds the leg and wb11 makes the manifest a render of the kit declarations. Pre-existing.
- **dDeclaredLoop's guard (br6, br23).** R7. dl2 makes `tools/loop/guard.py --staged` the pre-commit
  verdict, refuses an agent commit to `guarded-paths.txt` under every value, and admits an agent's
  policy commit under `agents-with-reason`. Pre-existing.
- **Kind rows and activation (br20, br22).** br20's `kind.role` and `kind.workflow` rows carry only
  `schema` (oc7 S4 asks `binds`, `population`, `factory` and `gate`); dl27's `activatable` list does
  not hold them. Pre-existing.
- **Single defects, pre-existing:** br1's item arm grades gov's rows only where dl24 S3 composes; br2's
  tester template drops wb23's `test.reason` answer.

## Summary table

| # | Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|---|
| 1 | br1 | `check_item_composition` exists in `tools/loop/loop_items.py` and can call the new `check_item_roles` arm | cite | AGREES | br1:82-85 · dl24:51-56 |
| 2 | br1 | The item actor is spelled `role:<slot>` | cite | AGREES | br1:83, :192 · dl24:61 (`--actor <kind:name>`), the `actor` widens list includes `role` |
| 3 | br1 | The new arm reads "gov's items only" | cite | MISMATCH | br1:101, :192 · dl24:46-50 |
| 4 | br1 | The `loop item kind` leg (dl24 S8) runs the arm, and br1 adds no leg | cite / R1 | AGREES | br1:299-300 · dl24:68-69 (the leg carries `enforces`) |
| 5 | br1 | AC6 runs `loop_items.py check` over a fixture loop definition | cite | UNKNOWN UNTIL BUILT | br1:287-293 · dl24:68 (`check --selftest`), dl24 §6 (`--fixture --plant`) |
| 6 | br1 | `gov-tester` sits in workflow `gate-bar`, writes `none`, and gains the two new fields | cite | AGREES | br1:58, :130 · wb23:36-38, :43-45 |
| 7 | br1 | AC2 counts 12 roles at `layer.roles` once the tester has landed | cite | AGREES | br1:269-270 · wb23:41-45 |
| 8 | br1 | `check_layers.py` (playbook kit) imports `roles_lib.load_roles` in process through `resolve_kit_dir` | R3 | MISMATCH | br1:185-186 · oc7:202-203 |
| 9 | br2 | `role-schema.toml`'s `[kind]` table mirrors dl24 S2's `item-schema.toml` | cite | AGREES | br2:31 · dl24:40-41 |
| 10 | br2 | The tester's role file has a `returns:` line, which br2 moves to `return` | cite | AGREES | br2:82 · wb23:36-38, :122 |
| 11 | br2 | The tester's template is `outcome:code-miss\|spec-wrong`, "the set its S7 names", and nothing more | cite | MISMATCH | br2:321-325 · wb23:29-31, :122 |
| 12 | br3 | S1 gets one item's declaration from `resolve_item_declaration` by running the loop kit in a subprocess and reading JSON back. (Outside the probe's hits: R3) | R3 | MISMATCH | br3:35-40, :254-258 against dl9:35, :94, :156, :167-175 |
| 13 | br5 | The orientation return is a `key: value` block | cite | AGREES | br5:38-40 · pr4:51-55 |
| 14 | br5 | `roles.retries` is read through `resolve`, located by `resolve_kit_dir` (an in-process import) | R3 | MISMATCH | br5:60-61 · oc7:379-380 |
| 15 | br6 | Agent commits can pass the policy kit's `guard.py --staged` with one new admitted shape, after S2 lists `.claude/roles.json` and `.claude/agents/` in `guarded-paths.txt`. | R7 | MISMATCH | br6:38-44, :114-121, :32-37 against dl2:44-49, :57-60, :95-98, :100-101, :177, :182-184, :190-192 |
| 16 | br6 | The policy guard reaches `render_agents.py --check` by subprocess through `resolve_kit_dir("roles", …)`. (Outside the probe's hits: R3) | R3 | AGREES | br6:41-42. This is the subprocess shape that dl12:49 and oc7:202-205 use. |
| 17 | br11 | The catalogue row is written through dl6 S4's `new policy-key` | cite | AGREES | br11:53-55 · dl6:65-68 |
| 18 | br11 | `resolve_owner_question` in `roles_lib` reads the key through `resolve()` in process | R3 | MISMATCH | br11:57-58, :150 · oc7:379-380 |
| 19 | br12 | The four keys are spelled as pr4 S3 and S4 spell them | cite | AGREES | br12:33-37 · pr4:51-55, :61-70 |
| 20 | br12 | `place --request <key> --return <file>` is the place to bind the check | cite | AGREES | br12:38-42 · pr4:36-42 |
| 21 | br12 | `item.entry.place`'s body is `placement.py place --return` | cite | AGREES | br12:61-62, :81-82 · pr3:155 |
| 22 | br12 | The disposition set and records belong to dl16 and are only called here | cite / R5 | AGREES | br12:59-60 · pr4:40-42, pr3:157 (the factory's flags, no door claimed) |
| 23 | br12 | The unattended prompt path places through the same `place`, under a `gov-orienter` work order | cite | UNKNOWN UNTIL BUILT | br12:63-64, :43-47 · pr4:102-111, :318-325 |
| 24 | br12 | br12 adds no leg; pr4's `loop placement fixtures` leg runs its plants | R1 | AGREES | br12:195-196 · pr4:112-118 |
| 25 | br12 | `placement.py` (loop kit) calls `roles_lib.validate_return` in process through `resolve_kit_dir` | R3 | MISMATCH | br12:38-41, :90, :98-100 · oc7:202-203, dl12:49, wb3:189-190 |
| 26 | br14 | The actor's native id `role:<slot>` stays dl24's | cite | AGREES | br14:78-79 · dl24:61 |
| 27 | br14 | `extract_role` and `extract_field` in `tag_index.py` (playbook kit) import `roles_lib` in process | R3 | MISMATCH | br14:38-46 · oc7:202-203, dl18:146-147 |
| 28 | br15 | `gov-tester` arrives with a 3072-byte ceiling and is priced at the pass | cite | AGREES | br15:120-122 · wb23:41-42 |
| 29 | br15 | `instructions.task-charter` is read through `policy.py get` as a subprocess | R3 | AGREES | br15:62-67 · oc7:379-380 |
| 30 | br16 | R9, in the roles kit, reads the `INSTANCES` keys of the review-harness kit's `replay_scorer.py` through `resolve_kit_dir`, and the lookup is a note where that kit is absent. | R3 | AGREES | br16:163-166, :318-324. The edge is already declared in `tools/roles/kit.toml:19`, which names "a note on the catalogue checker" when review-harness is absent. That matches R3's `requires_if` exception. |
| 31 | br17 | wb15 S4's unregistered form `legacy_ledger.py seed --home <path> -- <argv>` | cite | AGREES | br17:58-64 · wb15:48-50 (unchanged at rev-6) |
| 32 | br20 | A composition at "the landed revision" is a composition at HEAD | R6 | AGREES | br20:50-53 · oc46:42-47, :65-71 |
| 33 | br20 | `roles_lib` composes through the playbook kit's `read_overlay_rows` and `compose_rows` | R3 | MISMATCH | br20:50-53 · dl26:280-291, oc7:202-203 |
| 34 | br20 | dl24's `check_item_composition` (loop kit) calls `roles_lib.check_actor_patch` | cite / R3 | MISMATCH | br20:76-81 · dl24:51-56, oc7:202-203 |
| 35 | br20 | `kind.role` and `kind.workflow` rows name only `schema` | R1 | MISMATCH | br20:44-49 · oc7:66-75, dl27:361-367 |
| 36 | br21 | Importing `resolve` in process follows "the import TOOL-dDeclaredLoop-18 §4 makes" | cite / R3 | MISMATCH | br21:37-41, :278-283 · dl18:146-147, :311-314 |
| 37 | br22 | The `[[workflow.stages]]` table never trips dl1's `^stage` grep | cite | AGREES | br22:31-34 · dl1:292-293 |
| 38 | br22 | Moving the integer `stage` key out is dl1 S4's job | cite | AGREES | br22:70 · dl1:67-70 |
| 39 | br22 | Teaching dl6 S8's `new workflow` the row keys is an ask | cite | AGREES | br22:68-69 · dl6:82-85 |
| 40 | br22 | br20 composes the role and workflow rows that dl27 S3's `activates` table names | cite | MISMATCH | br22:62-64, :248-255 · dl27:50-56 |
| 41 | br22 | `read_agent_limit` uses br21's in-process `resolve` import | R3 | MISMATCH | br22:50-53 · oc7:379-380, dl18:146-147 |
| 42 | br22 | The row kinds are read from the loop kit's `upstream.py` through `resolve_kit_dir` | R3 | MISMATCH | br22:113-115 · oc7:202-203, dl12:49 |
| 43 | br23 | No agent can carry a `roles.effort.*` value below medium into the policy file, because "the guard" refuses every agent change except the budget raise. | R7 | MISMATCH | br23:68-72, :185, :225-228 against dl2:100-101, :190-192 |
| 44 | br25 | A new leg, `spawn-guard self-test`, is added by hand as a `tools/gate-legs.json` row with a guard and no `enforces`. The old leg retires with its `[[exempt_leg]]` row. | R1 | MISMATCH | br25:59-60, :78, :268, :315. `grep -c "enforces\|gate_leg\|leg_factory"` over spec 25 prints 0. oc7:58-63, :110-111, :228. wb11:36-49, :73-74, :384-395 |
| 45 | br25 | The roles pack's `spawn-guard.js` imports `tools/hooks/scratch-guard.js` in process, and the roles kit's `requires` gains `agent-cap`. (Outside the probe's hits: R3) | R3 | MISMATCH | br25:55-57, :62-66, :186-188, :452-458 against dl12:273-276, :282-286 and oc7:202-203 |
| 46 | br37 | wb23 S6 derives the same two counts, and br37 builds on it where it has landed | cite | AGREES | br37:52-54, :175-180 · wb23:53-56, AC3 :208-211 |
| 47 | br43 | The orienter's four placement keys are typed "as pr4 S3 and S4 spell them" | cite | UNKNOWN UNTIL BUILT | br43:190-192 · pr4:51-55 vs :68 |
| 48 | br43 | `--agent` beside `--return` is additive to pr4 S1's interface | cite | AGREES | br43:181-184, :571-572 · pr4:36-39 |
| 49 | br43 | `placement.py` (loop kit) calls `handoff.resolve_agent_transcript` (roles kit) | R3 | MISMATCH | br43:181-184, :215-217 · oc7:202-203 |
| 50 | br43 | `read_policy_setting` (an in-process import) is the only reader, and AC21 forbids the `policy.py get` subprocess | R3 | MISMATCH | br43:101-105, :421-423 · oc7:379-380 |
| 51 | br43 | The govkit step `reviewer_merge.py` calls the playbook kit's `write_overlay_units` | R3 | MISMATCH | br43:109-112 · wb28:63-64 |
| 52 | br54 | wb23 S4 seeds `tools/roles/house/gov-tester.md` | cite | AGREES | br54:81-83 · wb23:46-47 |
| 53 | br60 | S20 widens the guard of the `scratch-guard self-test` row by editing `tools/gate-legs.json`, and names no `enforces`. | R1 | MISMATCH | br60:110-112, :388-391. The same grep over spec 60 prints 0. oc7:58-63. wb11:36-49, :57-62 |

## The mismatches, both sides quoted

Each reader wrote the bullets for its own specs; the main loop changed only the headings.

### Group A, citation

**br1, the item arm's population**
- br1:101 "This unit's arm reads gov's items only"; br1:192 "for each item of gov's loop definition".
- dl24:46-50 "gov's `[[item]]` rows and the overlay's composed … and every check of S4 … runs over the composition".
- **Change:** S7 should state that `check_item_roles` grades every composed item, repository rows included. Otherwise it must state which rows it skips and how it tells them apart. Add a plant with a repository item whose actor is an expansion role.
- **Cause:** pre-existing. S3's composition sentence read the same at `4283cb44f`.

**br1, `check_layers.py` imports `roles_lib`**
- br1:185-186 "read through `roles_lib.load_roles`, imported through `resolve_kit_dir("roles", "roles_lib.py", here)`".
- oc7:202-203 "A kit may not import a sibling kit".
- **Change:** `check_layer_roles` should reach the role files through a roles-kit verb run as a subprocess (for example `.claude/roles.json` or a `check_roles.py` print verb). Where no such verb exists, add a §8 fork naming the ask, or declare a `requires_if` row.
- **Cause:** pre-existing.

**br2, the tester's return template**
- br2:323-324 "this unit gives it `never` and `return` (`outcome:code-miss|spec-wrong`, the set its S7 names)".
- wb23:29-31 says the tester also "plays … `test.reason` (answering the Test step's one question)". wb23:122 `returns: … for the Test step's question, its answer and the evidence`.
- **Change:** F4's template needs a field for the reason answer and its evidence, or a closed outcome that covers the question act. The template as written refuses every `test.reason` return.
- **Cause:** pre-existing. wb23's rev-3 moved only S7 and AC6.

**br5 S4 and br11 S5, policy reads in process**
- br5:60-61 "`roles.retries` read through TOOL-dGroundRules-2 S6's `resolve`, located through `roles_lib.resolve_kit_dir`". br11:150 "read once through resolve()".
- oc7:379-380 "policy keys are read through the policy kit's `get` verb … as a subprocess, the one seam a sibling kit may reach".
- **Change:** read both keys with `policy.py get <key>` as a subprocess, located by the inline `resolve_kit_dir`, as br15 S6 already does.
- **Cause:** pre-existing.

**br12, `validate_return` called in process from the loop kit**
- br12:90 "`lines = roles_lib.validate_return("gov-orienter", text)`"; br12:98-100 "locates the roles library … and imports nothing by a typed path".
- oc7:202-203 says a kit may not import a sibling kit. dl12:49 says the same. wb3:189-190 "`judge` reaches both siblings by subprocess".
- **Change:** `place` should run a roles-kit verb (for example a `handoff.py validate-return --role <slot> --file <f>`) as a subprocess. Add a §8 fork naming the ask to br5, since br5 mints no such verb, or declare a `requires_if` row on `tools/loop/kit.toml`.
- **Cause:** pre-existing.

**br14, the extractors import `roles_lib`**
- br14:38-41 "`roles_lib.parse_front_matter` imported through `resolve_kit_dir("roles", "roles_lib.py", here)`"; br14:46 uses `roles_lib.derive_stage_field_tag`.
- oc7:202-203. dl18:146-147, the pattern br14 copies, now reads "A kit imports no sibling kit, so the policy kit is reached only by that subprocess".
- **Change:** reach the roles grammar through a roles-kit verb as a subprocess, or add a §8 fork for one. Then re-check br14's own rejection of "`READ_KEYS` read by importing `roles_lib`" (br14:233), which already concedes the import problem.
- **Cause:** pre-existing for the rule. dl18's pattern also moved at `783f1ad3a`.

**br20 S3, composition through playbook functions**
- br20:52 "composed through `read_overlay_rows` and `compose_rows` (PLAY-dOrderedCharter-35 S1, I22)", inside `roles_lib`.
- dl26:283-291 "`compose_rows` … is a function whose callers import it inside the playbook kit … Recommendation: (a) [a `compose` verb run as a subprocess] … OPEN for the owner".
- **Change:** S3 should reach the composition the way dl26 §8 F5 settles, through a subprocess `compose` verb, and carry a §8 fork that tracks dl26 F5.
- **Cause:** pre-existing. dl26 F5 was open before the re-ground.

**br20 S6, `check_actor_patch` called from the loop kit**
- br20:80-81 "TOOL-dDeclaredLoop-24 S4's `check_item_composition` calls it", where `check_actor_patch` lives in `tools/roles/roles_lib.py` (br20:77).
- dl24:51-56 lists no such call, and oc7:202-203 forbids the import.
- **Change:** expose the check as a roles-kit verb that `loop_items.py` runs as a subprocess, or put the check in the loop kit reading `.claude/roles.json` as br1 S7 does. Name the change to dl24 S4 as an ask.
- **Cause:** pre-existing.

**br20 S2, kind rows missing their contract fields**
- br20:44-46 "`[[kind]]` rows `kind.role` and `kind.workflow` … each with `schema` naming its kind file". There is no `binds`, `population`, `factory` or `gate`.
- oc7:66-69 says each row carries "`binds` … `population` … `factory` and `gate`". oc7:72-74 says the gate leg's "`enforces` holds every tag of the kind's `binds`". dl27:366-367 (rev-3): "`kind.scenario` names `binds` and `gate`, and its leg carries `enforces`".
- **Change:** each row should name its `binds`, `population`, `factory` (dl6 S7/S8 `new role` and `new workflow`) and `gate` (`roles catalogue`). S2 should then give `roles catalogue` an `enforces` holding those binds, or name the pending-list row.
- **Cause:** pre-existing. oc7 S4 and S5 read so at base.

**br21 F2, the `resolve` import precedent is gone**
- br21:281-283 "(b), rung 3, the import TOOL-dDeclaredLoop-18 §4 makes for `read_catalogue_row`".
- dl18:146-147 "A kit imports no sibling kit, so the policy kit is reached only by that subprocess". dl18:311-314 (rev-2): "reads the policy kit by subprocess through `read_policy_value`, never by import".
- **Change:** re-open F2. Take (a), `policy.py get` as a subprocess (one revision resolved and passed as `--rev`), or record an ask for a batch `get` verb. Its cited precedent no longer exists.
- **Cause:** re-ground (`783f1ad3a`).

**br22 F2, scenario-activated rows**
- br22:250-251 "TOOL-dBoundRoles-20, which registers the role and workflow kinds a scenario's `activates` table names (TOOL-dDeclaredLoop-27 S3)".
- dl27:53-56 "The kinds a scenario may activate are the schema's `activatable` list, `kind.item` … and `kind.splice` … so each later build admits its own kind's rows by adding its kind". br20 never mentions scenarios or `activatable`.
- **Change:** either br20 adds `kind.role` and `kind.workflow` to dl27's `activatable` list and composes scenario-activated rows, or br22 F2 hands this to no unit and records it unowned.
- **Cause:** pre-existing.

**br22 S5, the agent limit read**
- br22:51-52 "through the same `resolve` import TOOL-dBoundRoles-21 S1 makes".
- oc7:379-380, and dl18:146-147 as above.
- **Change:** read `runtime.agents-in-flight` through `policy.py get` as a subprocess, following br21's revision.
- **Cause:** re-ground. It inherits br21 F2, whose precedent moved at `783f1ad3a`.

**br22, the row kinds read from the loop kit**
- br22:113 "The row kinds are read from the loop kit through `resolve_kit_dir("loop", "upstream.py", here)`".
- oc7:202-203. dl12:49 "A kit may not import a sibling kit".
- **Change:** read the row kinds through a loop-kit verb run as a subprocess, keeping the `seg`-shape fallback. Otherwise add a §8 fork for that verb.
- **Cause:** pre-existing.

**br43 S43 and S56, the transcript resolver**
- br43:181-183 "`tools/loop/placement.py place --return <file>` takes `--agent <agent-id>` … found through S56's `resolve_agent_transcript`", which is "a module-level function of `handoff.py`" (br43:215-216).
- oc7:202-203.
- **Change:** `placement.py` should run a `handoff.py` verb that prints the agent's last text and its meta role, as a subprocess. Name that verb in S56.
- **Cause:** pre-existing.

**br43 S21 and AC21, one in-process policy reader**
- br43:102-105 "`read_policy_setting` (unit 21 S1) is the only reader … no file under `tools/roles/` runs `policy.py get` as a subprocess". AC21 at br43:421-423 holds that.
- oc7:379-380 says the `get` subprocess is "the one seam a sibling kit may reach".
- **Change:** make `read_policy_setting` the one subprocess caller of `policy.py get`. Rewrite AC21 to red an import of `resolve` and admit only that subprocess call.
- **Cause:** re-ground. It rests on br21 F2, whose dl18 precedent moved at `783f1ad3a`.

**br43 S23, `write_overlay_units` called from govkit**
- br43:109-111 "`reviewer_merge.py`'s value edit of `.governance/instructions.toml` goes through `write_overlay_units` in `tools/playbook/overlay.py`".
- wb28:63-64 "A run-gates or govkit module imports no playbook module".
- **Change:** call the overlay writer through a playbook verb as a subprocess (the re-key mode exposed on a verb), or add a §8 fork naming that ask of dOrderedCharter.
- **Cause:** re-ground. This wb28 S5 sentence is absent at `4283cb44f` and was added at `443775a2f`.

### Group B, rule-wide

- **br25 R1.** The spec reads: "A new leg, `spawn-guard self-test`, runs it." (br25:59-60). Its inventory row reads: "leg `spawn-guard self-test` | `tools/gate-legs.json`, chunk `selftests`, subject `kit`, guard the pack's three files and `{prefix}/hooks/scratch-guard.js`" (br25:268). The parent says "a leg carrying no `enforces` is red" (oc7:61), and "The pending list … only shrinks after" (oc7:227-228). It also says "`never` makes the meta-check red any leg whose `enforces` is non-empty and which carries a `guard`" (oc7:110-111). wb11 makes the manifest generated: "`--write` renders `tools/gate-legs.json` from every declaration; `--check` exits 1 when the file differs" (wb11:43-45), and "the factory refuses a manifest row no declaration produces" (wb11:74). Today the leg is a `[[exempt_leg]]` in `tools/govkit/registry.toml:575`, and a probe of the 144 manifest rows printed `0 144` for rows carrying `enforces`. **Change:** S5, S8, the Inventory and Files touched should declare the renamed leg once. It should be an `[[exempt_leg]]` row in `registry.toml` (the suite is project-owned) or a roles `[[gate_leg]]`, written through `leg_factory.py new`, with a named `enforces` list and the manifest regenerated rather than hand-edited. The spec should also say how the leg's guard sits with oc7 S10 while wb11 F5 is open. **Cause:** pre-existing. oc7 S3 and :228 and wb11 S1, S2 and S8 already read this way at `4283cb44f`.
- **br60 R1.** The spec reads: "S20 — id 30. The `scratch-guard self-test` row of `tools/gate-legs.json` guards `{prefix}/memory-tree/tree_lib.py`" (br60:110-111). F5 resolves to "(a) the guard in `tools/gate-legs.json`" (br60:388-391). The parent text is wb11:36-41 ("Each leg is declared exactly once … A declaration holds every manifest key its leg carries: `name`, `argv`, `guard`, … `enforces`"), wb11:43-45 (the manifest is a render that `--check` reds) and oc7:61. **Change:** S20, F5 and AC12 should widen the guard in the leg's declaration and regenerate the manifest with `leg_factory.py --write`. S20 should keep or name the leg's `enforces`, which wb11 S6 writes. The re-stamp in S18 then covers the descriptor as well as the manifest. **Cause:** pre-existing.
- **br6 R7.** The spec reads: "`tools/policy/guarded-paths.txt` gains `.claude/roles.json` and `.claude/agents/`, and `guard.py --staged` gains one admitted shape for them" (br6:38-40). It also reads: "An adopter's own file under `.claude/agents/`, named by no index row, keeps today's verdict" (br6:36-37). The parent says: "the verdict it runs becomes `tools/loop/guard.py --staged`" (dl2:101). It says a staged change to "`tools/policy/guarded-paths.txt` is refused for every agent commit under every value of `policy-file.guard`" (dl2:58-59). Under `agents-with-reason` an agent write is admitted only when "only `.governance/policy.toml` changed" (dl2:191). S10 "denies an Edit, Write, MultiEdit or NotebookEdit whose path is listed in `tools/policy/guarded-paths.txt`, naming `policy_edit.py` as the door" (dl2:96-98). As written, the pass's own commit to the list file is refused by guard-self. Under the two non-default values the new shape is never consulted, so every agent re-render of `roles.json` is refused. dl2's harness arm also names `policy_edit.py`, not `render_agents.py --write`, and it does not know the index, so AC1's adopter-own file can be denied. **Change:** S2 should name dl2's `tools/loop/guard.py` as the pre-commit verdict. It should route the list-file edit through the owner's terminal, or add a §8 fork. It should state the shape under each `policy-file.guard` value, and settle with dl2 S10 which arm answers a write to `.claude/agents/<file>`. **Cause:** pre-existing. dl2 S3, S10 and S11 already read this way at `4283cb44f`.
- **br23 R7.** The spec reads: "reaches `.governance/policy.toml` only through TOOL-dGroundRules-6's guard, which … refuses every agent change but its one budget shape" (br23:69-70). It also reads: "the guard already makes every value in it the owner's" (br23:185). The parent says: "the verdict it runs becomes `tools/loop/guard.py --staged`" (dl2:101), and its table row reads "`agents-with-reason` | only `.governance/policy.toml` changed, a change record … naming each changed key … and `memory/DECISIONS.md` gains a row" (dl2:191). Under `agents-with-reason` or `agents-within-mandate`, an agent's commit setting `roles.effort.default = "low"` is admitted, so S5 would pass an agent-set level as the owner's. AC5 drives `tools/policy/guard.py` on the default value, so it stays green either way. **Change:** S6, §4 "The floor" and AC5 should cite dl2's verdict. They should either limit the claim to `policy-file.guard = owner-only` and state what happens under the other two values, or read provenance from the change record dl2 requires. AC5 should add a plant for each non-default value. **Cause:** pre-existing.
- **br3 R3.** The spec reads: "reads the item's declaration through TOOL-dDeclaredLoop-9 S2's `resolve_item_declaration`, called in a subprocess of the loop kit … the declaration returned as JSON" (br3:36-38). dl9 gives `resolve_item_declaration(item, roles)` as a function (dl9:35, :94). The only CLI it names is `loop_lib.py --check`, which "prints each item's effective declaration", and `--fixture` (dl9:156, :167-175). No verb takes one tag and returns JSON. R3 as the parents apply it asks for a §8 fork for the missing verb (dl12:277-292). **Change:** S1 should name the verb it runs. F4 should become an ask to dDeclaredLoop for something like `loop_lib.py declaration --item <tag> --json`, or S1 should state another admitted read. **Cause:** pre-existing. dl9 is still rev-1.
- **br25 R3.** The spec reads: "A helper read by two kits moves into `tools/hooks/scratch-guard.js`'s `module.exports`, which both packs already import" (br25:56-57). Its disposition table moves `extractWorkflowArgs` and `extractBuildSlug`, which the pack imports, to "`tools/hooks/scratch-guard.js`'s `module.exports`" (br25:188). It also says "The roles kit's `requires` gains the hooks entry `agent-cap`" (br25:65-66). The parent rule: "A kit may not import a sibling kit (TOOL-dGroundRules-1, §4 Evidence)" (oc7:202), and "(b) makes two kits import a sibling, which copy-installed kits cannot" (dl12:274-275). Today `grep -rn "require(.*scratch-guard"` finds only same-kit requires: `tools/hooks/agent-cap.js` (four sites) and `tools/hooks/format-guard.js:91`. **Change:** S4, S6 and F3 should either carry the two shared exports as a `tools/lib/` canonical block inlined into each kit under a parity row (the shape dl12 F4 takes), or declare the in-process edge as a `requires_if` row whose `why` names this require, as dl12:282-285 describes. **Cause:** pre-existing.

## UNKNOWN UNTIL BUILT

### Group A, citation

- **br1 AC6:** whether `loop_items.py check` takes a fixture loop definition, or only `--selftest` and `--fixture --plant`. dl24's build of the CLI decides it.
- **br12 S3 on the unattended path:** whether the step-3 placement of pr4 F3(a) spawns `gov-orienter` under a marked work order, or the main loop writes the return itself. If the main loop writes it, br12 S3 refuses every unattended placement. pr4's build of the VERBS step-3 sentence decides it.
- **br43 S46, the type of `observations`:** pr4 S3 makes it each claimed observation, which S6 needs for one probe per observation. pr4 S4 records it as `<n>`. A `list` type would also switch off br5's `key: value` fallback. pr4's build of `place`'s parse decides it.

### Group B, rule-wide



## Rule-wide hits the rules do not bind

### Group A, citation

- **br37 S1 and br54 S1** (`importlib` load of `roles_lib` in `tools/govkit/selftest.py`): R3 does not bind. `tools/govkit/` has no `kit.toml`, so it is not a copy-installed kit. Its self-test already loads installed kits' modules by path (selftest.py:769-772, :820-823). wb28:63-64 bars govkit from importing playbook modules only.

### Group B, rule-wide

- br3 R2: `work-order` is a `prompts/` file with the renderer's name (br3:62-67, :235-241), and the factory was rejected in F1. oc42 S3 joins only `-<kind>-<n>.md` files in a build's `build/` folder (oc42:45-49). The file still serves `journal` (`tools/roles/handoff.py:422`), so the reader is not broken.
- br3 R4: the spec writes no `loop.toml` row ("This unit reads the declaration and never writes a row", br3:74-75). AC1's row is a scratch fixture, and the `item.build.unit · step.build` block (br3:120) is rendered output.
- br9 R1: `"gates": { "manifest": "tools/gate-legs.json" }` (br9:108) is a role-index key that points at the manifest. It is not a leg row.
- br16 R3, br24 R3, br59 R3: the `import roles_lib` lines (br16:257, br24:183, br59:100-103) are criterion probes or the roles kit's own suite importing its own library.
- br42 R1: S5 declares spellings in the dead-path leg's exception list (br42:61). It touches no leg row.
- br49 R1 and R3: S3 calls spec 37's `derive_roles_expected`, and the in-process `roles_lib` load is spec 37 S1's (br37:39-42, Group A). Widening the `govkit selftest` guard is a non-goal (br49:60), and AC1's import is a probe.
- br50 R1: S1 and S2 edit §7 leg lines of specs and read manifest rows (br50:58-65, :251-256). The leg itself is renamed by unit 25.
- br55 R3: S1 to S3 change a compare inside govkit's own self-test. AC1's import of that module (br55:132) is a probe.
- br56 R1: names the size leg in a risk line (br56:143) and hands the guard change to unit 60 (br56:80). It reshapes no row.
- br57 R1: S3 names an existing leg on its §7 line (br57:45).
- br58 R1: S20 runs an existing row's argv (br58:131-132).
- br62, br64, br66, br69 R1: §7 lines name existing legs plus the boilerplate about unit 25's rename (br62:171, br64:284, :471, br66:409, br69:349). br69:148's "M7's gate leg" is a non-goal.
- br63 R1 and R3: S12's import of govkit's self-test module is the observation form, a probe (br63:72, :86-90). §7 adds no arm or leg (br63:283).

5. Citation specs: not applicable, since Group B is rule-wide.

Files:
- C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dBoundRoles\spec\2026-10-25-spec-TOOL-dBoundRoles-3.md
- C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dBoundRoles\spec\2026-10-25-spec-TOOL-dBoundRoles-6.md
- C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dBoundRoles\spec\2026-10-25-spec-TOOL-dBoundRoles-23.md
- C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dBoundRoles\spec\2026-10-25-spec-TOOL-dBoundRoles-25.md
- C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dBoundRoles\spec\2026-10-26-spec-TOOL-dBoundRoles-60.md
- C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-2.md
- C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-9.md
- C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-11.md
- C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dOrderedCharter\spec\2026-10-23-spec-PLAY-dOrderedCharter-7.md

## For the re-ground

Every spec below is revised by one writer of the re-ground brief, for the rows named. The other
mismatch-free specs stay as they are.

By spec: br1: rows 3 and 8; br2: row 11; br3: row 12; br5: row 14; br6: row 15; br11: row 18; br12: row 25; br14: row 27; br20: rows 33, 34 and 35; br21: row 36; br22: rows 40, 41 and 42; br23: row 43; br25: rows 44 and 45; br43: rows 49, 50 and 51; br60: row 53.

- **Group A, items, actors and composition** (writer led by spec 1): specs 1, 2, 12, 14 and 20.
- **Group B, policy reads and the placement return** (writer led by spec 21): specs 5, 11, 21, 22 and
  43.
- **Group C, the guard and the legs** (writer led by spec 6): specs 3, 6, 23, 25 and 60.

## After the re-ground

The three writers' returns are
[`2026-10-26-build-TOOL-dBoundRoles-1-reground-returns`](2026-10-26-build-TOOL-dBoundRoles-1-reground-returns.md).
No writer refused a row; each re-read both sides and found the parent line the record cites. Every
revised spec stays `DEFERRED`, each with one spec-revised deviation record. What they found beyond the
rows:

- **New roles-kit verbs, owned by this build.** The writers routed the cross-kit reads through verbs
  the roles kit would add in its own pass: `handoff.py check-return-file` (br12; the lexicon refused
  `validate`), `check_roles.py --print-tag-rows` (br14), `check_roles.py --check-actor-patch` (br20)
  and `handoff.py agent-return` (br43). br1 reads `.claude/roles.json` as data. Those forks are marked
  `RESOLVED (agent, 2026-10-26, delegated)`, since no parent change is needed; the owner may re-open
  them.
- **br21's `read_policy_setting` gains `with_default`**, since br43 makes it the one caller of `get`
  and br5, br11 and br22 need the catalogue default.
- **br23 F3 picks a stricter floor:** a policy-file level below medium is admitted only while
  `policy-file.guard` is `owner-only`. Keeping the old reading would let an agent's recorded change set
  a level below medium under the other two values.
- **br25 keeps its cross-kit `require` as a declared `requires_if` row naming `agent-cap`**, rejecting a
  `tools/lib/` inline block, which would move only the two exports and not rule 6's index readers.
- **br43 sits at 48756 bytes** after trimming its §2 item titles and the rung-3 `widens` lines; no
  design moved.
- **dl6 S1's `kind.role` population is the agent files alone**, while dl24 S1 composes overlay rows into
  its item population, so repository roles miss oc7 S5's both-ways read; dl6 also never states
  `kind.workflow`'s `binds`.
- **oc31 S4 and oc49 S11's govkit steps write through `write_overlay_units` with no route**, the same gap
  as br43 F17, against wb28:63-64.
- **The same cross-kit pattern outside the population:** `tools/hooks/agent-cap.js:465` loads the
  policy kit's `policy-mirror.js` in process, and dFairHearing-16's `spec-audit-optin.js` reads
  `scratch-guard.js` from the hooks kit.
- **br6 S2's directory line probably guards nothing:** `guarded-paths.txt` matches exact paths
  (`tools/policy/guard.py:87`, the pre-commit `grep -xF`), so `.claude/agents/` as a line guards no
  file in it. It was so before the re-ground; dl2 S10 does not say whether "listed" means exact or
  prefix.
- **wb23's `returns` names one judgment per red**, which br2's single `outcome` field cannot hold for
  several reds in one return; not a record row.

**Forks left open for the owner** (each names the ask the build run would file):

- br3 F5: a `loop_lib.py declaration --item <tag> --json` verb from dDeclaredLoop (recommended), over
  parsing `--check` or a `requires_if` row.
- br6 F4: whether dl2 S10's policy-path arm passes over the render paths, step 5a answering first
  (recommended, an ask to dl2 S10); br6 F5: a step in dl2's verdict that answers the render paths
  under every `policy-file.guard` value (recommended).
- br20 F6: dl26 F5's `compose` verb, naming `kind.role` and `kind.workflow` among its callers; br20 F7:
  dl24 S4's `check_item_composition` running `check_roles.py --check-actor-patch` (recommended).
- br22 F2: unit 20 adds `kind.role` and `kind.workflow` to dl27's `activatable` list (recommended), or
  the scenario half is recorded unowned; br22 F5: an `upstream.py kinds` verb from dDeclaredLoop
  (recommended).
- br43 F17: an `overlay.py` write verb from dOrderedCharter (recommended), which would also serve oc31
  S4 and oc49 S11.

Re-resolved on rung 1, `RESOLVED (agent, 2026-10-26, delegated)`: br2 F4, br20 F3, br21 F2, br23 F3,
br25 F3 and br60 F5. New and resolved: br1 F6, br12 F4 and br14 F5.
