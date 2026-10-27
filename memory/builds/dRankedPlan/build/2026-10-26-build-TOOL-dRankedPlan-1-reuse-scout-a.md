**Serves:** research TOOL-dRankedPlan-1 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-16

# Reuse scout A — dRankedPlan

The gov-reuse-scout return for the handoff `memory/builds/dRankedPlan/prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-1-reuse-scout.md`, extracted from its transcript by script, never retyped.

## Scout A: reuse map for dRankedPlan units 1, 7, 8, 11, 12, 13, 14, 16

**What exists today:**
- All six policy rows this build owns are already in the catalogue at HEAD: `tools/policy/catalogue.toml:204` (`kickoff.runs`), `:531` (`plan.ratification`) and `:896-918` (`plan.authority`, `plan.unplaced`, `plan.triage`, `plan.kickoff`). They are read through `resolve()` at `tools/policy/policy.py:752`, `policy.py get <key>`, or `bash tools/policy/policy-shim.sh get <key>` from bash. So no unit writes a catalogue row; each one only reads its key.
- `tools/loop/` does not exist. Neither does any part of the record factory: `tools/playbook/core.py`, `tools/memory-tree/build_records.py`, `gov_record.py`, `record-kinds.toml`, `tools/playbook/kinds.toml` and `namespaces.toml` are all absent.
- The one live record-field parser is `deviation_join.py`: `FIELD` at `:145`, `read_record` at `:212`.
- No build README declares `priority:` (`git grep -l '^priority:'` over the READMEs returned 0).

I ran the kit's `reuse_lookup.py` once per unit. The shortlists pointed at `gen_build_index.py`, `manifest-check.sh`, `roles_lib`/`handoff.py`, `tools/policy/` and `runlog/record.py`. I opened every source the rows below cite.

### Per-clause table

| Unit | Seam to extend | What already exists | Design sources that decide it | Product paths |
|---|---|---|---|---|
| TOOL-dRankedPlan-1 (cl-0369, priority beside `parents:`, plan view) | **Key:** `parse_front_matter` (`tools/memory-tree/gen_build_index.py:405`) and the build dict's `parents` (`:1212`). Model the `priority` grammar on the strict `order` verb parser (`_parse_order` `:458`, `ORDER_RE` `:213`).<br>**Graph:** `plan()` already inverts `parents:` into children and refuses an edge to nothing (`:2686-2698`).<br>**View:** `render_live` (`:2079`) is the file-level renderer to copy the shape of; its artifact is added at `:2807`. `render_edges` (`:1775`) and `render_order` (`:1748`) are the region-level precedents. | The `parents:` grammar, the edge region `gen:build-edges`, and LIVE.md with dormant and landed-unclosed columns. No priority anywhere; no view orders builds. | walkthrough.md:318-391 (P1: "Front matter + generated view"; planned unit 1, "ratification is an owner-authorized change to them"); flow.md:135 (Repository level: "the plan view … the order of builds"); flow-steps.md:184 (`plan.record` drafts priority, parents), :186 (`plan.place` regenerates the plan view); research-plan.md:60, :90; gap-register:341 | `gen_build_index.py` (parse, render, artifact, selftest); a new generated file under `MEMORY_ROOT` (see fork F1b); `tools/memory-tree/README.md`. Also `check_index_input` (`:894`, `:916`) and the `:848` LIVE.md exclusion, so the new view is treated as a render input like LIVE.md. |
| TOOL-dRankedPlan-7 (cl-0375, `plan.kickoff` offer-next/binding/advisory; attended briefs gated) | **offer-next / advisory:** `render_card` in `skills/session-kickoff/manifest-check.sh:517`. Its `live —` cell (`:519-531`) already reads `MEMORY_ROOT/LIVE.md` and has the `skipped:` forms; add a `plan —` cell beside it that reads the view.<br>**binding:** `check_card_route` (`:1006`) and its R-rule awk. A new rule there refuses a `- build:` line that is not the plan's next.<br>**Attended briefs:** R5 (`:1051-1052`) checks only that the brief is a tracked path. The content grader that already exists is `check_prompt_brief` (`tools/unattended/unattended.sh:3763`) with `read_brief_subheads` (`:3719`) and `BRIEF_FIVE` (`:3696`). It is gated to `AUTH_MODE=prompt` (`:3765`), so it never grades an attended brief. That is gap-plan-07 exactly.<br>**Policy:** `policy.py get plan.kickoff`. | The card, the route grammar and an R5 path check. The run-built brief grade exists but is unattended-only. | walkthrough P4 :375-377, :390, planned unit 8 ("Kickoff reads the plan, and attended briefs are gated as run-built ones are"); v2:1286 and presets v2:1603; night-pass.md:111 (the owner kept "attended briefs gated"); gap-register:347 | `manifest-check.sh` and its test; `skills/session-kickoff/SKILL.md` (see size note); possibly `tools/unattended/unattended.sh`, if R5 calls its grader. |
| TOOL-dRankedPlan-8 (cl-0376, full kickoff only where `kickoff.runs` says) | Parent spec **TOOL-dPlacedRequest-3 S5** already specs the `no-ready-card` stand-in in `SKILL.md`, keyed on the predicate R6 reads (`manifest-check.sh:1054`, the `READY — none yet` check; matches HEAD). Its hands-off (§3, spec line 111) says dRankedPlan "lands `kickoff.runs` and arms S5's stand-in with its value". **TOOL-dPlacedRequest-3 S6** narrows Step 1 the same way.<br>The extension point is the `render_card` cell list (`:517-545`): a `kickoff — <value> · full\|re-orient` line from `policy-shim.sh get kickoff.runs`. | The `READY — none yet` line (`:544`), the R6 predicate and the catalogue row (`catalogue.toml:204`). | orientation.md:259-263 (OR-2, the owner's words: "Full kickoff should be run in a session that doesn't have a card READY"); v2:1172, presets v2:1497; TOOL-dPlacedRequest-3 S5 and the `:224` paragraph | `manifest-check.sh` and its test; `SKILL.md`, one sentence at most. |
| TOOL-dRankedPlan-11 (cl-0379, each role item's memory read set sized at Plan as `id#tag`) | Parent specs:<br>- **TOOL-dTotalRecall-9 S6**: `check_read_set(root, role, keys)`, run as `gov_record.py budget --role <role> <key>…`.<br>- **S5**: `record show <id>[#<tag>]`.<br>- **S8 / F5**: `render_handoff` (`tools/roles/handoff.py:312`) takes `--read <key>` and writes a `reads:` list.<br>- Item rows and actors: **TOOL-dDeclaredLoop-12 §4** (`actor = "<kind>:<name>"`, `inputs = ["<layer tag>:<what>"]`).<br>- The `id#tag` form: **PLAY-dOrderedCharter-24** table, spec line 143.<br>- The planner role: **TOOL-dBoundRoles-1 S4** (`gov-planner`, `plan` workflow). | `handoff.py` has a static `reads:` key list per role file (`:336`), spelled with `field.*` tags after TOOL-dBoundRoles-14 S7. There are no per-build keys and no budget. | research-memory-structure-b.md:126 ("each item declares its read set as `id#tag`"); TOOL-dTotalRecall-9 S6/S8 | The plan record (field); no `handoff.py` change beyond TOOL-dTotalRecall-9 S8's. |
| TOOL-dRankedPlan-12 (cl-0380, `plan.record` declaring probes owed before Design) | Parent spec **TOOL-dPlacedRequest-7**:<br>- **S3**: `python tools/loop/probe.py trigger --cause <c> --asker <item> --subject … --build <slug> [--at <item>]`. The causes are data: `[[trigger-cause]]` rows in `loop.toml`, read by `read_trigger_causes`.<br>- **S6**: the `probe`/`probe-trigger` kinds.<br>The frontier is **TOOL-dDeclaredLoop-7 S3** (`next` returns owed probe items, per flow-steps [probe]). The gate is the `plan.exit` transition (**TOOL-dDeclaredLoop-3**, `write_transition`). | Nothing. | night-pass.md:118-175 (point 2: placed at a boundary, the record handed down, `next` returns it); flow-steps.md:604-628 ([probe]), :180 (`plan.input` under `verify-at-plan`), :186-191 (`plan.exit`) | The plan record (field); one `[[trigger-cause]]` row if fork F12a goes that way; the `plan.exit` witness check. |
| TOOL-dRankedPlan-13 (cl-0381, affected systems derived from `code` and checked; open questions as fork tags) | Parent spec **TOOL-dTotalRecall-8**: S6 (a file's kit is the nearest `tools/<kit>/` holding `kit.toml`) and S7 (`code_file(tree, path, blob, lang, kit, test, skipped)`, `code_edge`).<br>The seed is **TOOL-dPlacedRequest-8 S4**: `resolve_item_seed`'s `scope-paths` arm is "unarmed until the plan record carries a scope, which dRankedPlan's `plan.record` writes". So this unit's scope field is what arms it.<br>Fork tags: **no seam fits**. Probe: `git grep -E 'fork tag\|`fork\.\|fork\.<'` over every spec and v2 hits only night-pass.md:397. **PLAY-dOrderedCharter-19** (tag grammar, `namespaces.toml`) is where a namespace row would go, and that file is absent at HEAD. | Nothing. | night-pass.md:202-213 (point 3, the code record and `code` slot); :365, :396-397 (S3, "affected systems … derived from the code map and checked, and open questions as fork tags"); :403 (scope drift reads the affected systems, owned by dCalibratedLens); gap-register:348 | The plan record (fields); a check over `code_file` rows; one `[[namespace]]` row in `tools/playbook/namespaces.toml` (fork F13c). |
| TOOL-dRankedPlan-14 (cl-0382, the scenario field) | Parent specs:<br>- **TOOL-dPlacedRequest-10**: S1 return `scenarios: <tag>+<tag>…`; S3 `placement.check` re-evaluates every predicate; S5 the placement record gains `scenarios:`.<br>- **TOOL-dDeclaredLoop-27**: S5 `select_scenarios`; S8 `scenario=<tag>+<tag>` is pinned on each transition record into a step, and "a scenario changes only at a step boundary".<br>- **TOOL-dDeclaredLoop-15**: `item.plan.record`'s `revised` outcome carries a later re-pick (the other scout's unit 15). | Nothing. | night-pass-two.md:99-106 (NT-1, NT-2: "the planner may re-pick at Plan; a later re-pick happens only at a step boundary") | The plan record (field and reason). |
| TOOL-dRankedPlan-16 (cl-0498, artifact levels; one plan record per build; brief derived; red on a planted brief typing a plan field) | **Plan record home:**<br>- **TOOL-dTotalRecall-1 S9** (`record_kinds.py new`) registers the `plan` kind.<br>- **PLAY-dOrderedCharter-7 S7** gives the record-file factory, extracted from `deviation_join.py:145/:212`.<br>- **TOOL-dTotalRecall-2 S7** routes `new build-readme` through `cmd_new_build` (`gen_build_index.py:4122`, scaffold `render_new_build_readme` `:4041`).<br>- **TOOL-dPlacedRequest-21 F2** already chose the README scaffold as the stand-in for "a derived plan record" until this build's kind lands.<br>**Brief shape:** `BRIEF_SKELETON` (`manifest-check.sh:120-162`) is what authors Goal, Items, Acceptance, Gates and Non-goals today. The unattended grader follows it past `PROMPT_BRIEF_SKELETON_CUTOFF` (`.unattended.conf:517` = 2026-10-11; `unattended.sh:3782-3790`). So a skeleton change reaches the run-built grade with no second edit.<br>**Derived brief:** `render_handoff` (`handoff.py:312`) is already derived (flow.md:139 calls the handoff "the brief"). Its `brief:` keys read an authored prompt record through `resolve_brief_record` (`:283`) and `extract_brief_section` (`:210`). | Levels are declared nowhere. The packet generator (`packet.py`) already renders a derived brief, but it is an instrument, not product. | flow.md:98-104 (FL-P2, the owner's words), :130-139 (the levels table), :143-145 (FL-P5 confirmed); orientation.md:49; gap-register:109; fold-brief-w3:208 | `manifest-check.sh` (`BRIEF_SKELETON`, R5); `handoff.py` (brief keys resolved from the plan record); the record-kinds registry row; the levels declaration (fork F16b); `memory/TEMPLATE-SPEC.md` only if the brief section names the levels. |

### Where specs and source disagree (HEAD 0689e7fa1)

- **`cmd_new_build`:** TOOL-dPlacedRequest-21 S4 and TOOL-dTotalRecall-2 S7 cite `gen_build_index.py:4050`. At HEAD it is `:4122`, and `render_new_build_readme` is `:4041`.
- **`resolve_ask_path`:** TOOL-dPlacedRequest-8 S4 cites `gen_build_index.py:3185`. At HEAD it is `:3256`.
- **SKILL.md size row:** TOOL-dDeclaredLoop-56 cites `tools/template-size-limits.txt:60` for the `SKILL.md` 18432 row. At HEAD that row is `:63`.
- **SKILL.md headroom:** `SKILL.md` is 18310 bytes today, which leaves 122 bytes. TOOL-dPlacedRequest-3 S5/S6 already add prose to it. Units 7 and 8 must put their behaviour in `manifest-check.sh` (card cells and rules), not in `SKILL.md`.
- **Record factory spelling:** the packet says "record factory `tools/playbook/core.py new`". PLAY-dOrderedCharter-7 has two different things:
  - `core.py new <kind> <name>` is the kinds-register factory (S4/S5).
  - `tools/memory-tree/build_records.py` is the record-file factory (S7), which TOOL-dPlacedRequest-7 S6 uses.
  - TOOL-dTotalRecall-2 grows `gov_record.py new <kind>` from it.

  None exists at HEAD, so a plan record file should be called as TOOL-dTotalRecall-2's `gov_record.py new plan`.
- **No front-matter `status:` here:** `render_new_build_readme` writes `status: OPEN` (`:4041` head block), which ties to the open ask PLAY-dClosedLoop-31. Any plan-record scaffold built on it must not add the key.

### Shared interfaces

1. **`priority:` front-matter key.** Used by units 1 and 7, and by the other scout's units 2 (planner drafts), 4 (dormancy in the view), 5 (live mapping) and 6 (Plan Review). Proposed spelling: `priority: <n>`, a positive integer, lower first, at most once, with anything that looks like it but does not conform refused. Nothing spells it yet; the nearest grammar is the `order <n>` verb (`memory/TEMPLATE-SPEC.md:83`, `ORDER_RE` at `gen_build_index.py:213`).
2. **The plan view file.** Units 1 and 7, the other scout's 2, 4 and 6, and TOOL-dDeclaredLoop-8 S1, which already lists "the plan view" as a `view` trust class. Proposed: `<MEMORY_ROOT>/PLAN.md`, generated by `gen_build_index.py plan()` beside `LIVE.md` (artifact pattern `:2807`). Its row shape is `| Build | Priority | Parents | Status | Lease |`. The name "plan view" comes from flow.md:135.
3. **The plan record kind and its fields.** Units 11-14 and 16, plus the other scout's 2, 3 (select into `plan.record`), 9 and 10 (ratification covers it) and 15 (the revision carries the same fields).
   - Kind: `record-kind.plan` (layer-memory.md:407).
   - File name: `<date>-build-<FAMILY>-<slug>-1-plan-1.md` in `build/`. This follows PLAY-dOrderedCharter-7 S7's grammar and the `<FAMILY>-<slug>-1` anchor of TOOL-dPlacedRequest-21 F6.
   - Fields, each in `deviation_join.py:145`'s `FIELD` form (`- **Xxx yyy:** value`): `Scope`, `Affected systems`, `Open questions`, `Probes owed`, `Read sets`, `Scenario`, `Scenario reason`. Each two-word name fits the regex's one lowercase second word.
   - Priority and parents stay in front matter only, because each fact has one home (cl-0498).
4. **The `id#tag` read key.** Unit 11, and the other scout's planner unit 2. Spelled `<id>#<tag>` (PLAY-dOrderedCharter-24, spec line 143); consumed by TOOL-dTotalRecall-9 S5/S6/S8. Proposed `Read sets` value: `<item tag>: <id>#<tag>, …; <item tag>: …`. The item tags are TOOL-dDeclaredLoop-12's (`item.design.unit-spec`).
5. **The scenario value.** Unit 14, and the other scout's 15. Spelled `<tag>+<tag>…` (TOOL-dPlacedRequest-10 S1, TOOL-dDeclaredLoop-27 S8).
6. **Policy reads.** Units 7 and 8, and the other scout's 2, 3, 9 and 10. Use `python tools/policy/policy.py get <key>`, or `bash tools/policy/policy-shim.sh get <key>` from bash (`policy-shim.sh:4-5`). Do not read `.governance/policy.toml` directly.
7. **Card cells.** Units 7 and 8. Proposed: `plan — next <slug> · <value>` and `kickoff — <value> · full|re-orient`, in `render_card`'s line form (`manifest-check.sh:529-541`), each with its `skipped:` forms.
8. **Brief sub-heads.** Units 7 and 16. These are `BRIEF_SKELETON` (`manifest-check.sh:120-162`), `BRIEF_FIVE` (`unattended.sh:3696`) and `read_brief_subheads` (`:3719`). The kickoff skeleton stays the one source; the unattended grader already reads it at BASE.
9. **Probe trigger cause.** Unit 12 and dPlacedRequest. Proposed: `--cause point --at item.plan.exit` (TOOL-dPlacedRequest-7 S3's closed set), with no new word.
10. **Scope field arming `scope-paths`.** Unit 13 and TOOL-dPlacedRequest-8 S4. The `Scope` value is repo-relative paths normalised by `resolve_ask_path` (`gen_build_index.py:3256`).

### Proposed build order within my group

1. **Unit 16, first.** It declares the levels and registers the `plan` kind, which fixes where every later field lives.
2. **Unit 1.** It is pure `gen_build_index.py` with no unbuilt parent, and it produces the view unit 7 reads.
3. **Unit 14.** It is the simplest field: a copy of the placement record's `scenarios:` plus a reason, and it proves the field writer.
4. **Unit 13.** Its `Scope` field arms TOOL-dPlacedRequest-8's seed. It needs TOOL-dTotalRecall-8's `code_file` rows, or the nearest-`kit.toml` rule as a stand-in.
5. **Unit 11.** It needs item tags (TOOL-dDeclaredLoop-12) and the budget (TOOL-dTotalRecall-9 S6). It goes after 13 because both size a role's load.
6. **Unit 12.** It needs `probe.py` (TOOL-dPlacedRequest-7) and `plan.exit`'s witness, and is the last plan-record field.
7. **Unit 8.** It arms TOOL-dPlacedRequest-3 S5's stand-in and adds the card's `kickoff —` cell, which unit 7 sits beside.
8. **Unit 7, last.** It reads the plan view (unit 1), the card cell pattern (unit 8) and the brief shape (unit 16).

### Open forks per unit, with the execution-plan rung that settles each

**Unit 1**
- F1a, the `priority` grammar (integer rank or bands; ties broken by slug or opened date): no v2 text gives one. Rung 3.
- F1b, the view's home, a separate `PLAN.md` or a region in `LIVE.md`: `LIVE.md` is in check 7's entry budget (`gen_build_index.py` comment at `:2116-2118`), which favours a separate file. Rung 2, by measuring the rendered row width against that cap.
- F1c, whether a `priority:` edit needs the owner's ratification: settled by walkthrough P1, rung 1. The guard itself is the other scout's unit 2 or 9.

**Unit 7**
- F7a, what "the plan's next item" is (the first unleased non-terminal build in the view, or an ask): walkthrough unit 8 implies builds, rung 1. The tie-break is rung 3.
- F7b, where `binding` is enforced (a new `check_card_route` R-rule, or `placement.check`): rung 3.
- F7c, how attended briefs are graded: R5 can call `unattended.sh`'s grader through `resolve_kit_dir` (`manifest-check.sh:791`), skipping when it is not installed, or carry it inline. The kickoff kit is junction-installed and carries shared code inline. Rung 2, by probing whether `resolve_kit_dir` finds the unattended kit in an adopter, then rung 3.

**Unit 8**
- F8a, verdict on the card or as SKILL prose: SKILL has 122 bytes of headroom. Rung 2, which favours the card cell.
- F8b, the predicates for `opening-a-build` and `plan-absorbs`: OR-2 gives the option text only. Rung 3.

**Unit 11**
- F11a, the read set's home, the plan record or a static `loop.toml` item field: "sized at Plan" means per build, so the plan record. Rung 1.
- F11b, whether `plan.exit` refuses an over-budget set or only records it: rung 1, read through `memory.over-budget` (TOOL-dTotalRecall-9 S6).

**Unit 12**
- F12a, the cause word: `point` with `--at item.plan.exit`, or a new `[[trigger-cause]] plan` row. Rung 3.
- F12b, whether `plan.exit` refuses while an owed probe has no `probe` record: "owed before Design" says yes. Rung 1.

**Unit 13**
- F13a, the unit of "affected system" (the kit from `code_file.kit`, the layer, or paths): rung 2, probing on the code record or the `kit.toml` rule.
- F13b, "checked" means recompute and refuse a mismatch, or warn: rung 3.
- F13c, the fork-tag grammar: no namespace is specced anywhere. The options are a new `[[namespace]] fork` row (PLAY-dOrderedCharter-19's registry) or reusing §8 `F<n>` ids. The clause names fork tags, so a namespace row stays within it. Rung 3; rung 5 if it is judged a registry widening.

**Unit 14**
- F14a, the field pair or a revision record for a re-pick at Plan: NT-2 settles it, rung 1. A re-pick after Plan goes through unit 15, also rung 1.
- F14b, whether a re-pick re-runs `placement.check` admission: NT-2 ("re-evaluates every predicate"), rung 1.

**Unit 16**
- F16a, the plan record's home, a build-folder `plan` record file or the README front matter and slots: P1 settles priority in front matter (rung 1). FL-P2's "one plan" and the flat `key: value` front-matter parser (`:405-456`, no lists) favour a record file for the rest. TOOL-dPlacedRequest-21 F2's README stand-in must then be re-pointed. Rung 3.
- F16b, where the levels are declared (memory-tree README, `HYGIENE.md`, or a data table the check reads): rung 3, choosing data so the red is mechanical.
- F16c, which "brief" the planted red targets (the kickoff `-brief.md` record or the handoff): flow.md:139 names the handoff, and gap-flow-03 names README, brief and card, so both. Rung 1. Removing Goal, Acceptance and Non-goals from `BRIEF_SKELETON` changes `check_prompt_brief`'s required set for every build opened after 2026-10-11. Rung 2: probe that grader's suite on the changed skeleton before committing.
