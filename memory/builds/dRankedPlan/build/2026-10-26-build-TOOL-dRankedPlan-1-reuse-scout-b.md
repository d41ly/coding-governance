**Serves:** research TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-15

# Reuse scout B — dRankedPlan

The gov-reuse-scout return for the handoff `memory/builds/dRankedPlan/prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-2-reuse-scout.md`, extracted from its transcript by script, never retyped.

I followed `reuse-lookup.agent.md`: one `reuse_lookup.py` query per behaviour, then opened the sources each shortlist named. One finding up front: most of the seams these units need exist only as parent specs. None of `tools/loop/`, `review_pin.py`, `lenses.toml`, `record-kinds.toml`, `gov_record.py`, `gov-planner.agent.md` or `tools/playbook/kinds.toml` exists at HEAD. No harness capability table and no prompt-submit hook exists anywhere, in source or in any spec. Paths are relative to `C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/`. Nothing was written in the repo.

## Seam table

| Unit | Seam to extend | What exists today | Design lines that decide it | Product paths |
|---|---|---|---|---|
| **-2** planner and triager role, Plan workflow, `plan.authority` | **The role and entry:** TOOL-dBoundRoles-1 S2 and S4 already spec `gov-planner` (writes `records`) and a `plan` workflow entry. **The cap:** `WORKFLOW_NAMES` at `tools/roles/check_roles.py:92` (spec cites :90) is widened to twelve by that unit's §8 F1. **Item rows:** TOOL-dDeclaredLoop-24 S6 `loop_items.py new`. **Key read:** `resolve(key, repo, rev)` at `tools/policy/policy.py:752`. **Owner-only writes:** `tools/policy/guard.py`, path-level, listed in `guarded-paths.txt`. **Agents only propose:** `verb_propose` at `tools/unattended/unattended.sh:12940`. | Catalogue row `plan.authority` at `tools/policy/catalogue.toml:896-899` (3 values, default, owner dRankedPlan). The ten-entry `tools/roles/workflows.toml:13-105`. No planner file, no `plan` entry, no order check. | v2:1779 (the row's clause text), v2:1283 and :1600 (presets), flow-steps:180-190 (the `plan.triage-judge`, `plan.record` and `plan.reason` actors are all `planner`, so "triager" is the same slot), v1:108, walkthrough:338-339, flow-roles FR-1 :173-199 | `tools/roles/agents/gov-planner.agent.md` body, `tools/loop/loop.toml` (the `[[workflow]]` row for `plan` and the `item.plan.*` rows), `tools/policy/guard.py` or the plan-view check (fork F2a), `tools/roles/workflows.toml` |
| **-3** triage by `plan.triage` (`rules` / `owner-batches` / `archive-legacy`) | **Labels:** `render_sev_row` at `tools/memory-tree/backlog.py:1538` (`SEV · id · level · why`, the why names the rule); severity fold at :993-995. **Defer/retire:** `render_status_row` :1532. **Readiness rule:** `derive_ready` :1386. **Legacy archive:** `render_relocated_row` :1542 and `migrate_backlog.py --triage-ask`. **Read side:** `gen_build_index.py --asks` (`cmd_asks` :3805, `build_grade_row` :3599). **Batches:** owner gate TOOL-dDeclaredLoop-19 S6 and disposition record -16. **Kinds:** TOOL-dTotalRecall-1 S9 `record_kinds.py new triage` and `new dupes`. | The SEV grammar, severities and READY grades all exist; nothing applies a declared rule. Catalogue row `plan.triage` at catalogue.toml:908-911. Moves T4-T6 (planning to deferred/retired/refused) are specced in TOOL-dDeclaredLoop-15:97-99. | v2:1285 and :1602, walkthrough:350-353 (P3 answer `rules`), :380-383 (rule-based labeller, every label records its rule, owner sees only HIGH and BLOCKER), flow-steps:164-169 (the pass runs outside any build), :182-183, :737, gap-register:342 | `tools/memory-tree/backlog.py`, one declared-rules home (fork F3a), `tools/memory-tree/gen_build_index.py` (`--asks`), `tools/memory-tree/record-kinds.toml` rows `triage` and `dupes` |
| **-4** dormancy disposal | **The label:** `render_live` at `tools/memory-tree/gen_build_index.py:2080-2112`, threshold `LIVE_DORMANT_DAYS="21"` at `.memory-tree.conf:1034`. **Report:** `build_live_builds_without_activity` at `tools/drift-audit/drift_report.py:3479`, report-only. **Unit-level defer:** `verb_rescope ... defer` at `unattended.sh:13300` (needs a live RUN.md). **Pause move:** B19 `item.life.request` pause, TOOL-dDeclaredLoop-13:154. | Labelled only. LIVE.md today has 18 rows marked dormant. No row in any transition table moves a dormant build. | walkthrough:346-347 ("deferred as one of Maintain's safe fixes, and the plan view shows it"), v2:1321 (`maintain.fixes` "defer dormant" belongs to dTendedCadence, this build's child), research-plan:51 and :94, gap-register:345 | `tools/memory-tree/gen_build_index.py` (render_live and the plan view), `tools/memory-tree/backlog.py` or spec status rows, `tools/drift-audit/drift_report.py` (report becomes the disposer's input) |
| **-5** live-build mapping carried out | **Per-build owner ruling:** the disposition record (TOOL-dDeclaredLoop-16, `**Item:**` / `**Disposition:**` / `**Channel:**` / `**Reason:**`). **Absorption:** the supersession field of the plan record (`design.input`, flow-steps:235). **Population:** `memory/LIVE.md`. No code seam fits: the probe for an "absorbed-by" key over `gen_build_index.py` found only `parents:` at :1212. | Nothing. v1's table has 23 rows. Probe: LIVE.md holds three live builds no v1 row maps (aScoutedSeam, dScriptedRepeat, and dClosedLoop itself). Every row v1 maps is still live. | v2:1787-1792, v1:147-177, walkthrough:356 and :362-363 (the unit "runs only with the owner's ratification") | Mostly records under `memory/builds/*/`. Product paths only if it renders into the plan view (scout A's -1). |
| **-6** Plan Review with `review.pin`'s preset | **The pin:** TOOL-dFairHearing-3 S8 `tools/workflows/review_pin.py` maps a subject's record kind to `preset` (design record to `unit-spec`, dark); extend it with the plan kind. **The subject:** the harness already admits a non-spec subject as a design-document subject with no rev (`tools/workflows/tier2-review.js:428-434`, `SPEC_SUBJECT_PATH` :317, kind `spec-audit` :190-199). **Placement:** Plan breakpoint before `item.plan.exit`, TOOL-dDeclaredLoop-19 S2. **Disposal:** TOOL-dDeclaredLoop-20 leaves "disposal of a plan revision" unarmed for a later build (:105, :132). | Fixed lens literals `SPEC_LENSES` at tier2-review.js:810 and `DIFF_LENSES` :774. No preset, no Plan lens, no `review_pin.py`, no `lenses.toml`. | v2:707 (C5-F14), v2:802, flow-steps:570 (`review.pin` pins "the plan revision"), :574, walkthrough:354-355, gap-register:344 | `tools/workflows/review_pin.py` (kind mapping), `tools/loop/loop.toml` (`review.dispose` route for plans), `tools/workflows/tier2-review.template.js` only if the subject check needs a plan arm |
| **-9** intake log, `entry.intake` hook, `plan.ratification` | **Stand-in intake:** TOOL-dPlacedRequest-19 S2 and S5 `<git-common-dir>/requests/<key>.md` plus `.typed`, and `check_request_consent` ("relayed: data with provenance, never consent"), keyed by `request_content_key` (I11), which "keys an absent intake the same way". **Transcript-side owner classifier:** `_derive_owner_class` at `tools/runlog/extract.py:587`, with typed / queued / interrupt at :709-734. **Key:** `plan.ratification` at catalogue.toml:531-534. | No prompt-submit hook. `.claude/settings.json` registers no UserPromptSubmit, and no file under tools/ or skills/ names it. No intake kind: it is dWellOiledMachine's, which has no `spec/` folder. | v2:95, :401 (PM-9), :1224, :1546, flow-roles:193-199 ("written verbatim by the prompt-submit hook"), flow-steps:190 and :193-194 | A ratification reader in `tools/loop/` (beside dPlacedRequest's `request.py`) |
| **-10** `plan.exit` fallback to the owner gate, Codex-shaped adapter | **Gate placement:** TOOL-dDeclaredLoop-19 S1, S3, S6 (`derive_breakpoints`, owner gate at `item.plan.exit`, released by `check_owner_disposition`). **Release record:** -16 disposition record. **Witness:** -17 computes witnesses. **Gate scope:** -53 (an owner gate holds only builds opened after it was placed). **Adapter selector:** `runtime.harnesses` at catalogue.toml:505-509 ("named harness adapters"). **Capability table:** no seam fits. A grep for `capability table`, `UserPromptSubmit` and `prompt-submit` over tools/, skills/ and every parent spec finds none. | Nothing beyond the catalogue row. | v2:433-436 (RC-9), :707 (CS1-F1), :774 (FK-9-1), flow-steps:193-194 and :316, layer-runtime:829-844 (each adapter carries a capability table, "measured and never claimed"; the Codex row) | `tools/loop/breakpoints.py` (the ratification arm), a capability probe, a planted adapter fixture |
| **-15** plan revision, designing back to planning | **The move:** row B6 `designing --item.design.decompose / a fork the goal cannot survive--> planning` (TOOL-dDeclaredLoop-13:141), recorded by TOOL-dDeclaredLoop-10 S2 and S5 through -3's `write_transition`. **The record:** `item.plan.record` outcome `revised`, already named the plan revision by TOOL-dDeclaredLoop-15:113-121 and §8 F2. **The writer:** TOOL-dTotalRecall-2 `gov_record.py new`. | Nothing. The driver has no PLANNING phase; `verb_rescope` (`unattended.sh:13300`) is unit-level only. | v2:34, :911 (P18), :707 (C5-F13), :721 (re-design inventory split to gap-flow-25), flow-steps:223, :235-237, :742, flow-roles FR-12 :269-272 | `tools/loop/loop.toml` (arm the `revised` outcome and the dispose route), `tools/memory-tree/record-kinds.toml` (`plan` row fields), `tools/loop/loop_table.py` (the move only, no new code path) |

## Where specs, records and source disagree

- **TOOL-dBoundRoles-1 S4** cites `check_roles.py:90` for `WORKFLOW_NAMES`; at HEAD it is :92.
- **The live-build mapping:** v1's table predates aScoutedSeam and dScriptedRepeat, which are live today and unmapped.
- **Old line cites in research-plan:21/:94 and the walkthrough:**
  - They cite `render_live` at `gen_build_index.py:1766-1807` and `:1797`; it is now at :2080, with the dormant label at :2110.
  - The walkthrough's `plan_state` cite (:4411) is now :4458.
- **TOOL-dPlacedRequest-3:90-95, §8 F8:** the `[[fixed-row]]` for `entry.intake` in TOOL-dDeclaredLoop-24 is triggered by dPlacedRequest declaring the item, but dWellOiledMachine declares it. As written it is never armed, so -10's "until the intake kind lands" probe has no row to read.
- **Missing loop.toml row:** TOOL-dDeclaredLoop-1 S2 ships exactly ten `[[workflow]]` rows in `loop.toml`. TOOL-dBoundRoles-1 S4 adds `plan` to `workflows.toml` but names no `loop.toml` row, so a `plan` workflow with `step = "step.plan"` is owed by nobody.
- **The Codex row:** layer-runtime:833-835 records that Codex 0.139 *documents* UserPromptSubmit. The clause plants a Codex-shaped adapter that falls back, so the plant must leave the event undeclared as unmeasured.

## Shared interfaces

1. **Record kind `plan`** (`record-kind.plan`). Shared by -2, -6, -15 and scout A's -1, -12, -13, -14, -16. Proposed: row `plan`, tag `record.plan`, home `memory/builds/*/build/*-plan-*.md`, id-rule `<date>-build-<unit id>-plan-<n>.md`. That copies the shape of the `stream-plan` row in TOOL-dTotalRecall-25 S1. Write it through `record_kinds.py new` (TOOL-dTotalRecall-1 S9).
2. **The plan revision is a `plan` record, not its own kind.** The owned nodes list `record-kind.plan`, `triage` and `dupes`, and no `plan-revision`. TOOL-dDeclaredLoop-15 F2 already spells the revision as `item.plan.record`'s outcome `revised`. Shared by -15, -6 (`review.pin` pins it) and scout A's -14 ("a later re-pick only ... through a plan revision").
3. **Record kinds `triage` and `dupes`** (-3, and -2 through `plan.triage-judge`). Witness spellings: "the triage record naming its rule" and "the dupes record" (flow-steps:181-182).
4. **Item tags `item.plan.{input,dedupe,triage-rule,triage-judge,record,research,place,lease,exit}`**, spelled as in flow-steps:180-190 and TOOL-dDeclaredLoop-13:115. Registered by -2 via `loop_items.py new`. `item.plan.exit` is TOOL-dDeclaredLoop-24's fixed row, owner dRankedPlan.
5. **Role slot `gov-planner`, actor `role:gov-planner`, workflow `plan`.** TOOL-dBoundRoles-1 §4 roster. Triager means the same slot.
6. **Policy reads only through `tools/policy/policy.py:752 resolve`:**
   - Mine: `plan.authority`, `plan.triage`, `plan.ratification`.
   - Scout A's: `plan.unplaced`, `plan.kickoff`, `kickoff.runs`, all owned by this build.
7. **One ratification predicate**, used by -2, -3 (owner-batches), -10, -15, and A's -7 (attended briefs gated). Proposed spelling: `read_plan_ratification(build) -> (value, witness)`, owned by -9. Nothing spells it yet. Its parts are already spelled: `check_request_consent` (TOOL-dPlacedRequest-19 S5) and `check_owner_disposition` (TOOL-dDeclaredLoop-19 S6).
8. **The fallback witness:** the literal `intake not installed` (clause 0378 text). -10 writes it; -9 reads it.
9. **The owner gate and its release:** TOOL-dDeclaredLoop-19's gate at `item.plan.exit` and the -16 disposition record, `--channel terminal`. Shared by -2, -3, -5, -10, -15.
10. **Priority key:** `priority:` beside `parents:` in README front matter (walkthrough:338; v2:1779 "priority beside `parents:`"). Scout A's -1 owns it. -2 governs who may write it; -4 and -5 render into A's plan view.
11. **One dormancy threshold:** `LIVE_DORMANT_DAYS` (`.memory-tree.conf:1034`). -4 reads it and never declares a second threshold.
12. **Severity row:** `SEV · <id> · <BLOCKER|HIGH|MED|LOW> · <why>` (`backlog.py:1538`). In -3, the why names the rule that set the label.

## Build order within group B

1. **-9:** the ratification predicate and the intake stand-in come first, because -10, -2, -3 and -15 all read it.
2. **-10:** the fallback gate wraps -9's predicate on TOOL-dDeclaredLoop-19's owner gate. Plan's exit is reachable only after this.
3. **-2:** registers the planner's body, the `plan` workflow and the `item.plan.*` rows that -3 and -15 route through, and enforces `plan.authority` on the ratification from 1 and 2.
4. **-3:** triage needs the planner (the judge actor), the item rows, and the `triage`/`dupes` kinds.
5. **-4:** dormancy disposal reuses -3's defer grammar and needs a disposer before -5 confirms dPolishedVitrine's track.
6. **-5:** a records operation that needs the owner's ratification (1 and 2) and dormancy disposal (5).
7. **-15:** needs the `plan` kind (scout A's -12/-13/-14), ratification (1 and 2), and the item rows (3).
8. **-6:** Plan Review's subjects are the plan record and the plan revision (flow-steps:570), so it lands last.

## Open forks, with the rung that settles each

- **-2**
  - F2a: where "the planner adds but never reorders between ratifications" is enforced. Option 1 is a key-level arm on `guard.py`, which is path-level today, so it widens a governance carrier. Option 2 is a check in A's plan-view render against the last ratified order. **Rung 3**, or **rung 5** (`widens:`) if the guard is chosen.
  - F2b: who adds the `loop.toml` `[[workflow]]` row for `plan`. **Rung 1** (TOOL-dBoundRoles-1 §8 F1 chose a dedicated entry); otherwise an ask row in dBoundRoles' `BACKLOG.md`.
  - F2c: one slot or two for planner and triager. **Rung 1** (flow-steps:183 names the actor `planner`).
- **-3**
  - F3a: home of the declared rules: a loop-kit data file or a policy-file table. **Rung 3.**
  - F3b: what counts as "legacy" under `archive-legacy`, and whether archiving is a `RELOCATED` row or a `DEFERRED` status. **Rung 2** (a probe of `migrate_backlog.py --triage-ask` and the 297 asks deferred onto the one owner-triage ask), then **rung 3**.
  - F3c: the triage pass runs outside any build (flow-steps:164-167), but owner gates hold builds (TOOL-dDeclaredLoop-19 and -53), so `owner-batches` has no gate to sit on. **Rung 3**, else **rung 6**.
- **-4**
  - F4a: the move. There is no dormant-to-deferred row; B19 pause is the only standing move. **Rung 1** (walkthrough:346 says "deferred"), then **rung 5** if a parent table row is added (an ask to dDeclaredLoop).
  - F4b: disposer now versus dTendedCadence's later `maintain.fixes` "defer dormant". **Rung 3:** build it here and hand off the safe-fix name.
- **-5**
  - F5a: the population is v1's 23 rows or LIVE.md at the run's base (two more unmapped builds). **Rung 2.**
  - F5b: how absorption is recorded: a disposition record per build, or the plan record's supersession field. **Rung 3.**
- **-6**
  - F6a: which preset a plan subject maps to. **Rung 1:** the clause says "the preset `review.pin` passes", which is TOOL-dFairHearing-3 S8's dark `unit-spec` default.
  - F6b: whether "a tree that holds no Plan lens" is shown by `lenses.toml` holding no plan row. **Rung 2.**
  - F6c: the walkthrough:354 lens list belongs to dCalibratedLens. **Rung 1** (a non-goal).
- **-9**
  - F9a: the intake stand-in: dPlacedRequest's `.typed` consent, or runlog's transcript classifier. **Rung 3** (the first works per request; the second is post hoc).
  - F9b: whether a request relayed between sessions ratifies. **Rung 1** (FR-1: "never relayed by an agent").
- **-10**
  - F10a: no adapter or capability-table grammar exists, and dWellOiledMachine is unspecced. Option 1: treat an absent table as "undeclared", **rung 2/3**. Option 2: mint a minimal adapter row, which widens a dWellOiledMachine surface, **rung 5** (`widens:`).
  - F10b: the planted Codex adapter leaves UserPromptSubmit undeclared although Codex documents it. **Rung 1** (layer-runtime:829, "measured and never claimed").
  - F10c: TOOL-dDeclaredLoop-53 exempts builds opened before the gate was placed from the fallback. **Rung 1**, else **rung 6**.
- **-15**
  - F15a: which item fires. **Rung 1:** B6 makes the move (flow-steps:742) and `item.plan.record` `revised` writes the record.
  - F15b: its own kind, or a `plan` record. **Rung 1:** the owned-nodes list has no revision kind.
  - F15c: "ratified as the plan is" against FR-12's "proceeds under the request's mandate". **Rung 1:** under `request` it reads -9's predicate and needs no owner turn.
  - F15d: Design's inventory after a revision belongs to dIndexedDesign (gap-flow-25, v2:721). **Rung 1** (a non-goal).

The query outputs are in `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-drankedplan-1fc3d7/43fa2011-5bb6-422a-bd52-776c30d97bd4/scratchpad/s/B/` (q1.txt to q8.txt, plus the v1-versus-LIVE comparison lists).
