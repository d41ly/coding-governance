# TOOL-dRankedPlan-16 — the artifact levels: one plan record per build, and a brief that renders it and never types it

**Status:** OPEN · rev-3 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 1 · advances TOOL-dRankedPlan-17

**Carries:** cl-dClosedLoop-0498@e9d43f26 whole
**Carries:** node:record-kind.plan
**Carries:** node:item.plan.record

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-1-fix-return.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-fix-return.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-13 TOOL-dRankedPlan-15 |
| [2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-a.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 |
| [2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-fix-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-13 TOOL-dRankedPlan-15 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 |
| [2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) | spec-audit | TOOL-dRankedPlan-1 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-2 TOOL-dRankedPlan-14 TOOL-dRankedPlan-13 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-15 TOOL-dRankedPlan-6 TOOL-dRankedPlan-8 TOOL-dRankedPlan-7 |

<!-- /gen:spec-records -->

## 1. Goal

The plan of a build is written up to three times today, in the README, the kickoff brief and the
card, and the levels of card, plan and brief are declared nowhere (gap-flow-03). The owner settled
the hierarchy in the flow round (FL-P2, FL-P5, flow.md:98-145): the card at the session's level above
the plan, one plan record per build holding its concrete details, and the brief derived from the plan,
the spec and the stage's facts and never authored. This unit lands the `plan` record kind, declares
the three levels as data a check reads, renders plan fields into the derived brief, and reds a brief
that types a plan field.

## 2. Scope (IN)

- **S1** — The kind's row. `python record_kinds.py new plan --tag record.plan --writer "gov_record.py
  new plan" --check record-kinds --field Problem --field Goal --field Scope --field Non-goals --field
  Acceptance --field "Affected systems" --field "Open questions" --field "Probes owed" --field "Read
  sets" --field Scenario --field "Scenario reason"` (TOOL-dTotalRecall-1 S9) appends the `plan` row to
  `tools/memory-tree/record-kinds.toml`: `layer.memory`, home `memory/builds/*/build/*-1-plan-1.md`,
  id-rule `<date>-build-<FAMILY>-<slug>-1-plan-1.md`, `schema.form = "fields"`. The eleven fields are
  I3's, refined in §8 F1. Observed by AC1 and AC2.
- **S2** — The typed kind. `plan` joins `TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py` and the
  record factory's kind table in `tools/memory-tree/build_records.py` (PLAY-dOrderedCharter-42 S1, S2;
  PLAY-dOrderedCharter-7 S7), its required fields the row's eleven, and the closed kind list of
  `tools/memory-tree/HYGIENE.template.md`, rendered to `memory/HYGIENE.md`. A plan record is served
  `**Serves:** plan <FAMILY>-<slug>-1`, the build's first id (TOOL-dPlacedRequest-21 F6's anchor). The
  typed-kind file-name join (PLAY-dOrderedCharter-42 S3) reads a file as named for a kind only on the
  stem `-build-<unit id>-<kind>-<n>.md`, so the six research records named
  `…-execution-return-plan-<n>.md` stay bound (§8 F5). Observed by AC2 and AC3.
- **S3** — `item.plan.record`, its write and its witness. The planner writes the build's one plan record
  through the door, `python tools/memory-tree/gov_record.py new plan --build <slug> --unit
  <FAMILY>-<slug>-1 --title "Plan — <slug>" --field <Name>=<value>…` (TOOL-dTotalRecall-2 S1), each value
  one line, `none` where the field holds nothing. The witness is the plan-record schema check
  (flow-steps.md:184), `check_plan_record(root, slug)` in the new module
  `tools/memory-tree/plan_record.py`, run as `python tools/memory-tree/plan_record.py check <slug>`:
  the row's generated field check (TOOL-dTotalRecall-1 S4) over the record `find_plan_record` returns,
  then each field owner's check, which units 11 to 14 add as calls inside it. It prints
  `item.plan.record — witnessed · <path>` or `item.plan.record — unwitnessed · <why>`, exit 0 either
  way, in the line form of TOOL-dRankedPlan-2's `plan_items.py witness`. The item's row is
  TOOL-dDeclaredLoop-12 S2's; it is armed as TOOL-dDeclaredLoop-13 §4 "The stand-ins" says an owning
  build arms its item, by landing this witness reader and deleting the `[[stand-in]]` row naming
  `item.plan.record` from `tools/loop/loop.toml` in the same pass.
  **Readers:** by name: READER NOT IN TREE — the loop kit is absent at base 0689e7fa; the row's readers
  are TOOL-dDeclaredLoop-13's stand-in reader in its `loop_table.py` and TOOL-dDeclaredLoop-7's
  `derive_position`, both specced and unbuilt · by value: NO VALUE READERS — the row carries only the
  item and its owner, and each reader stops answering `stand-in dRankedPlan` for it at this pass, the
  arming the row waits for. Observed by AC2.
- **S4** — One plan record per build. `find_plan_record(root, slug)` returns the one tracked file under
  the build's `build/` folder matching the row's home, `None` for none, and raises naming both paths for
  two; `read_plan_fields(root, slug)` returns that record's fields by the factory's `read_record`, the
  field reader every unit of this build reads a plan field through; `python plan_record.py field <slug>
  <Name>` prints one value, exit 0, 1 for no record or no such field, 2 for two records. Observed by
  AC6 and AC7.
- **S5** — The levels as data. A `[[level]]` table in `tools/memory-tree/record-kinds.toml`, its rows in
  level order from the highest: `card` (the session card, holding the session's own facts), `plan`
  (holding `kind:plan`, `front-matter:priority`, `front-matter:parents`), and `brief` (`renders =
  ["plan"]`, its artifacts every file under a build's `prompts/` carrying the handoff marker
  `<!-- gov:handoff `). `read_levels(root)` in `plan_record.py` refuses a row whose `renders` names a
  level not above it, a `kind:` naming no row and a `front-matter:` key outside the build README's
  declared keys. Observed by AC4.
- **S6** — The check, `check_brief_derived(root)` in `plan_record.py`, run by `python record_kinds.py
  --check` as one arm of the `record-kinds` leg. For each artifact of a level that renders a higher one,
  every line in the factory's `FIELD` form naming a field of a `kind:` the higher level holds, and every
  column-0 `<key>:` line naming a `front-matter:` key it holds, is a typed plan fact:
  `levels: <path>:<line> types <fact>, whose home is <home>; render it with plan:<key>`, exit 1. Every
  run prints `levels: card > plan > brief · graded <n> brief(s) against <m> fact(s)`, and an empty
  population prints `levels: graded 0 briefs, so this arm checked nothing`. Observed by AC4 and AC5.
- **S7** — The brief renders the plan. `render_handoff` (`tools/roles/handoff.py:312`) gains the key
  family `plan:<field>`, the field's name lower-cased with its space as a dash (`plan:goal`,
  `plan:non-goals`, `plan:affected-systems`), whose value is `plan_record.py field <slug> <Name>`'s
  output, the module found by `resolve_kit_dir` as the render finds the kickoff checker; exit 1 on no
  record reads as absent, exit 2 refuses the render naming both records. `gov-spec-writer` reads
  `plan:goal?, plan:acceptance?, plan:non-goals?` beside its `brief:` keys. Observed by AC6 and AC7.
- **S8** — The patch's and the repeat's plan record. `--placed-build` (TOOL-dPlacedRequest-21 S4,
  `tools/memory-tree/gen_build_index.py`) writes, after the README it scaffolds, the build's plan record
  through the door: `Problem` `request <content key>`, `Goal` `patch of <origin slug>` or `playbook run
  of <path>`, every other field `none` (flow-steps.md:127, §8 F4). The README keeps `parents:`,
  `mode:` and `playbook:`. Observed by AC8.
- **S9** — The docs: a new page `help/plan.md` with a section "The artifact levels" naming the three
  levels, the plan record's fields, the `plan:` keys and the check's line, a row for it in
  `help/README.md`, and a `tools/memory-tree/README.md` section naming `plan_record.py` and the
  `[[level]]` table. Observed by AC9.

## 3. Non-goals (OUT)

- Each intent field's grammar and check: `Scope`, `Affected systems`, `Open questions`
  (TOOL-dRankedPlan-13), `Read sets` (TOOL-dRankedPlan-11), `Probes owed` (TOOL-dRankedPlan-12),
  `Scenario` and `Scenario reason` (TOOL-dRankedPlan-14). This unit declares the names and their order.
- The plan revision's `## Revisions` region: TOOL-dRankedPlan-15's, on the same file.
- `priority:` and the plan view: TOOL-dRankedPlan-1's. Who may change a plan: TOOL-dRankedPlan-2's.
- The kickoff brief record and `BRIEF_SKELETON`, left unchanged: the record is the intake at the plan
  level, the owner's words and the session's confirmation, and `check_prompt_brief` grades it (§8 F3).
- The card's plan cell: TOOL-dRankedPlan-7's. The card is declared above the plan and graded by nothing
  here.
- A practice-reach field: flow-steps.md:184 lists it, and no clause of this build carries it.
- The record door, the registry, its gate and the factory: dTotalRecall's and dOrderedCharter's.

### Edges

- **hands-off** `TOOL-dRankedPlan-1` — `record-kind.plan`, whose one record per build the plan view's `Plan` cell links, found by `find_plan_record`
- **hands-off** `TOOL-dRankedPlan-9` — `record-kind.plan`, whose record's newest commit `signed-commit` verifies
- **hands-off** `TOOL-dRankedPlan-14` — `record-kind.plan`, the record whose `Scenario` and `Scenario reason` fields that unit sets
- **hands-off** `TOOL-dRankedPlan-13` — `record-kind.plan`, the record whose `Scope`, `Affected systems` and `Open questions` fields that unit defines, and `check_plan_record`, the schema check its call joins
- **hands-off** `TOOL-dRankedPlan-11` — `record-kind.plan`, the record whose `Read sets` field that unit sizes
- **hands-off** `TOOL-dRankedPlan-12` — `record-kind.plan`, the record whose `Probes owed` field that unit declares
- **hands-off** `TOOL-dRankedPlan-15` — `record-kind.plan`, the one record per build a revision rewrites
- **hands-off** `TOOL-dRankedPlan-6` — `record-kind.plan`, the record whose `plan` Serves kind makes a review subject a plan subject
- **hands-off** `TOOL-dRankedPlan-7` — `BRIEF_SKELETON`, kept the intake record's one shape at the plan level, whose sub-heads that unit's attended-brief grade reads
- **consumes-from** external — dTotalRecall: `record_kinds.py new` and `--check` (TOOL-dTotalRecall-1 S3, S4, S9), the door `gov_record.py new` (TOOL-dTotalRecall-2 S1 to S4)
- **consumes-from** external — dOrderedCharter: `TYPED_RECORD_KINDS` and the file-name join (PLAY-dOrderedCharter-42 S1 to S3), the factory `build_records.py` and its `FIELD` (PLAY-dOrderedCharter-7 S7)
- **consumes-from** external — dPlacedRequest: `--placed-build` and `render_placed_build_readme` (TOOL-dPlacedRequest-21 S4)
- **hands-off** `TOOL-dRankedPlan-19` — `plan_record.py check`, `item.plan.record`'s witness line that unit's gate requires before Plan's exit (round-1 spec audit, id 1)
- **hands-off** `TOOL-dRankedPlan-20` — S8's patch and repeat plan record, whose `Scenario: none` that unit's plants feed to the scenario reader (round-1 spec audit, id 2)
- **hands-off** `TOOL-dRankedPlan-27` — S7's `plan:` keys on `gov-spec-writer`'s `reads:` line, which that unit admits to the roles vocabulary (round-1 spec audit, id 27)
- **hands-off** `TOOL-dRankedPlan-29` — `plan_record.py`, the handoff's `plan:` render and the `[[level]]` marker, which that unit's S10, S16, S22 and S33 correct (round-1 spec audit, ids 11, 19, 25, 40)
- **hands-off** `TOOL-dRankedPlan-33` — S3's door and `plan_record.py check`, through which that unit's seed writes and asserts a witnessed plan record (spec audit of units 19 to 29, id 21)
- **hands-off** `TOOL-dRankedPlan-37` — §4's population line and §5's perf line, whose figure 697 that unit corrects to 695 (spec audit of units 19 to 29, ids 18, 25)

## 4. Design

### Evidence

- The handoff is the derived brief today: `render_handoff` (`tools/roles/handoff.py:312`) renders
  `task:`, `card:`, `brief:` and `input:` keys and hashes the result into its marker; `check_handoff`
  (:426) re-derives both hashes, so a hand edit after the render already fails `check`.
- The kickoff brief record's shape is `BRIEF_SKELETON` (`skills/session-kickoff/manifest-check.sh:119`),
  read at BASE by `read_brief_subheads` (`tools/unattended/unattended.sh:3719`), which refuses a skeleton
  that does not keep `BRIEF_FIVE` (:3696) in order (:3731-3741).
- The flow's table names the agent level's artifact "the brief (the handoff)", "derived, never
  authored" (flow.md:139), and the plan level's artifacts "the plan record, the intake records"
  (flow.md:137).
- No handoff types a plan field today: of the 697 tracked files under `prompts/` carrying the marker,
  none holds a `FIELD` line naming one of S1's eleven fields or a `priority:`/`parents:` line
  (PINNED, `git grep` at `0689e7fa1`). The FIELD lines they do hold are the charter's facts
  (`Product`, `Layout`, `Streams` and seven more), none sharing a plan field's name.

### Data model

```toml
# tools/memory-tree/record-kinds.toml, beside the [[record-kind]] rows
[[level]]
name = "card"            # the session: who and where, the session's scope slice, its next action
holds = []
[[level]]
name = "plan"            # the build: its one plan record and the README's two plan keys
holds = ["kind:plan", "front-matter:priority", "front-matter:parents"]
[[level]]
name = "brief"           # the agent: the handoff, derived and never authored
holds = []
renders = ["plan"]
artifacts = { glob = "builds/*/prompts/*.md", marker = "<!-- gov:handoff " }
```

A plan record, as the door writes it:

```markdown
**Serves:** plan TOOL-dX-1

# Plan — dX

- **Problem:** request 3f9c2a7d01be
- **Goal:** the plan view orders every live build
- **Scope:** tools/memory-tree/gen_build_index.py
- **Non-goals:** the card's plan cell
- **Acceptance:** AC1 the view lists dX first; AC2 an unplaced build sits under Unplaced
- **Affected systems:** memory-tree
- **Open questions:** none
- **Probes owed:** none
- **Read sets:** none
- **Scenario:** feature
- **Scenario reason:** none
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `plan` row, tag `record.plan` | record kind, `record-kinds.toml` | none declared |
| `[[level]]` with `name`, `holds`, `renders`, `artifacts` | table, `record-kinds.toml` | none declared |
| `tools/memory-tree/plan_record.py` | module | none |
| `find_plan_record`, `read_plan_fields`, `check_plan_record`, `read_levels`, `check_brief_derived` | functions | `py.function`, asked at the pass |
| `check`, `field` | verbs of `plan_record.py` | none |
| `plan:<field>` | handoff key family | none |
| `plan-kind`, `plan-name-join`, `level-order`, `brief-types-plan-field` | selftest plants | none |

### Migration

None. No plan record exists before this unit; a build with none renders every `plan:` key absent.

### Rollout

Live at landing. The check grades every handoff from its landing; the population probe above
measured none it would red.

### Files touched (estimate)

- `tools/memory-tree/record-kinds.toml`: S1's row, S5's table
- `tools/memory-tree/plan_record.py` (new): S3 to S6
- `tools/memory-tree/record_kinds.py`: S6's arm in `--check`, the plants in `--selftest`
- `tools/memory-tree/tree_lib.py`: S2's member and the file-name join's stem
- `tools/memory-tree/build_records.py`: S2's kind table entry
- `tools/memory-tree/HYGIENE.template.md`: S2's kind list line
- `memory/HYGIENE.md`: its render, by `adopt-memory-tree.sh --render`
- `tools/memory-tree/gen_build_index.py`: S8, and its `--selftest` arm
- `tools/loop/loop.toml`: S3's `[[stand-in]]` row for `item.plan.record`, deleted
- `tools/memory-tree/README.md`: S9's section
- `tools/memory-tree/kit.toml`: the kit version moved
- `tools/roles/handoff.py`: S7
- `tools/roles/agents/gov-spec-writer.agent.md`: S7's `reads:` line, the edit. The harness's agent
  file is its copy, which `render_agent_file` (`tools/roles/render_agents.py:144-155`) writes from the
  front-matter keys it names and never from `reads:`, so the copy stays byte-identical and is not in
  this write set
- `tools/roles/adopt-roles.test.sh`: S7's arm
- `tools/roles/kit.toml`: the kit version moved
- `help/plan.md` (new), `help/README.md`: S9

### Alternatives rejected

- **The levels as prose in `HYGIENE.md` or the kit README.** Nothing could read them, so the red on a
  typed field would rest on a list spelled again inside the check.
- **Plan fields carried in the README's front matter.** The front-matter parser reads flat
  `key: value` lines (`tools/memory-tree/gen_build_index.py:405-456`) and TOOL-dTotalRecall-4 closes the
  key set; eleven free-text values there would put the plan back into the README.
- **The handoff reading the record itself.** A second reader of the record's grammar in the roles kit;
  S7 runs the one reader as a subprocess, as TOOL-dTotalRecall-9 S8 runs its budget.

## 5. Production-readiness checklist

- security — no new write path but the door's; `plan_record.py` reads tracked files and prints field
  values, which the handoff copies verbatim, as it copies a brief record's sections.
- perf / scale — one subprocess per `plan:` key in a render; the check reads each handoff once, 697 files
  today.
- error / empty / loading states — no record reads as absent; two refuse naming both; an empty brief
  population announces itself.
- observability — every check run prints the level order and the graded counts.
- risks — a charter fact named like a plan field would red every handoff; none does today, and the red
  names the clash.
- testing — the plants of §6 and the roles adopter arm.
- migration — none.
- user docs — `help/plan.md`, S9.

## 6. Acceptance criteria

- **AC1** — When `python record_kinds.py --template plan` runs at the pass tip, it prints `**Serves:**
  plan` and the eleven field lines, `Problem` first and `Scenario reason` last, in S1's order.
  Red when: a field is missing or out of order.
- **AC2** — When `python record_kinds.py --selftest` runs its `plan-kind` plant, `gov_record.py new plan
  --build tFix --unit TOOL-tFix-1` with all eleven `--field` values writes
  `<date>-build-TOOL-tFix-1-plan-1.md` served `plan TOOL-tFix-1`, `plan_record.py check tFix` exits 0,
  and `gen_build_index.py --print-bindings` lists it bound; the same call without `--field Goal=…`
  exits 2 naming `Goal` and writes nothing; with the record removed, `plan_record.py check tFix` prints
  `item.plan.record — unwitnessed`. At the pass tip `grep -n "item.plan.record" loop.toml` finds no
  `[[stand-in]]` row for it.
  Red when: a plan record with no `Goal` is written, its `plan` Serves kind reads malformed, or the
  stand-in row survives beside its armed reader.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --print-bindings` runs at the pass tip,
  the rows of the six `-execution-return-plan-<n>.md` records are byte-identical to the rows it prints
  at base, each of kind `research`; the selftest's `plan-name-join` plant reds a file named
  `<date>-build-TOOL-tFix-1-plan-2.md` that serves `research`.
  Red when: a research record named `…-plan-<n>.md` outside the strict stem reads malformed.
  figure: six, PINNED at `0689e7fa1` by `git ls-files`.
- **AC4** — When `python record_kinds.py --check` runs at the pass tip, it prints `levels: card > plan >
  brief` and `graded <n> brief(s)`, `<n>` the tracked handoff count DERIVED at the run, and exits 0; the
  `level-order` plant, which puts `brief` above `plan`, exits 1 naming the row.
  Red when: a level that renders a level below it passes.
- **AC5** — When the selftest's `brief-types-plan-field` plant adds `- **Scope:** tools/x` to a fixture
  handoff, `check_brief_derived` exits 1 naming the file, the line, `Scope` and `plan:scope`; a planted
  `priority: 2` line is named the same way; the handoff as rendered exits 0.
  Red when: a brief typing a plan field passes.
- **AC6** — When the roles adopter arm renders `gov-spec-writer` with `handoff.py render --stdout` for a
  fixture build whose plan record's `Goal` is `ship the view`, the output holds `### plan:goal` followed
  by `ship the view`; for a build with no plan record, `plan:goal` is named on the `Not supplied,
  optional:` line.
  Red when: the value comes from anywhere but the plan record, or an absent record refuses.
- **AC7** — When the same arm plants a second plan record in the fixture build `tFix`, the first
  named `2026-10-26-build-TOOL-tFix-1-plan-1.md` and the second `2026-10-27-build-TOOL-tFix-1-plan-1.md`,
  both matching the row's home, `handoff.py render --stdout` exits 1 and its refusal prints both
  names, `2026-10-26-build-TOOL-tFix-1-plan-1.md` and `2026-10-27-build-TOOL-tFix-1-plan-1.md`, and
  writes nothing.
  Red when: the render picks one of two plan records.
- **AC8** — When `python tools/memory-tree/gen_build_index.py --selftest` runs its placed-build arm, a
  patch `tPatch` with origin `tOrigin` stages its README and `<date>-build-TOOL-tPatch-1-plan-1.md`
  whose `Problem` is `request <key>`, `Goal` is `patch of tOrigin` and every other field `none`.
  Red when: `--placed-build` writes the README alone.
- **AC9** — When `grep -n "## The artifact levels" plan.md` runs over the help page, it finds S9's
  section naming `card`, `plan`, `brief`, the `plan:` keys and `check_brief_derived`.
  Red when: the page does not describe the levels.

## 7. Gates

`memory hygiene` · `policy fixtures` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `build-index selftest` · `roles adopter self-test` · `roles catalogue` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/record_kinds.py · covers AC1 AC2 AC3 AC4 AC5 · the `record-kinds` leg's `--selftest` gaining the `plan-kind`, `plan-name-join`, `level-order` and `brief-types-plan-field` plants, staged by a `check_brief_derived` that passes a typed `Scope` line · none

New arm: tools/roles/adopt-roles.test.sh · covers AC6 AC7 · the `plan:` key render over a fixture build holding one, two and no plan records, staged by a render that takes the first of two records · none

New arm: tools/memory-tree/gen_build_index.py · covers AC8 · the `--selftest` placed-build arm gaining the plan record, staged by `--placed-build` writing its README alone · none

## 8. Open questions

- **F1 — Which fields does the plan record hold?** Options: (a) I3's seven, the intent fields units 11
  to 14 set; (b) those seven and the plan facts flow-steps.md:184 has `plan.record` draft, `Problem`,
  `Goal`, the cut-line out as `Non-goals`, and `Acceptance`, with the cut-line in as `Scope`; (c) (b) and
  a practice-reach field. (a) leaves the plan's goal and acceptance with no home at the plan level,
  which fails the clause's "one plan record per build holding its concrete details"; (c) adds a field no
  clause of this build carries. RESOLVED (agent, 2026-10-26, delegated): (b), rung 1, flow-steps.md:184
  and flow.md:137 name each; priority and parents stay in the front matter (walkthrough P1), and the
  file name is `-1-plan-1.md`, refining I3's proposed `-1-plan.md` to the typed-kind grammar
  PLAY-dOrderedCharter-42 S3 requires. widens: none · relaxes: none
- **F2 — Where are the levels declared?** Options: (a) a `[[level]]` table the check reads, in the
  registry of record kinds whose fields it names; (b) prose in `HYGIENE.md`; (c) prose in the
  memory-tree README. Only (a) makes the clause's red mechanical. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the most feature-rich survivor, and the tie-break's reuse of
  TOOL-dTotalRecall-1's registry and leg. widens: none · relaxes: none
- **FACT-QUESTION · F3 — Which artifact is the derived brief the check grades?** Options: (a) the
  handoff alone; (b) the handoff and the kickoff brief record, its plan facts struck from
  `BRIEF_SKELETON`. The probe: the sub-head walk of `read_brief_subheads`
  (`tools/unattended/unattended.sh:3731-3741`), run in the run's scratch over `--brief-skeleton`'s output
  as it stands and with `### Goal` removed. The observation: as it stands it prints the seven
  sub-heads from `Goal` to `Reuse`, which is its liveness; without `### Goal` it refuses
  `first missing ### Goal`, the path that fails 117 for every prompt-mode build opened after
  `PROMPT_BRIEF_SKELETON_CUTOFF`. RESOLVED (agent, 2026-10-26, delegated): (a), rung 2 then rung 1:
  the probe rules (b) out as written, and flow.md:137-139 places the intake records at the plan level and
  calls the handoff the brief. `BRIEF_SKELETON` stays the intake record's one shape, which refines I5.
  widens: none · relaxes: none
- **F4 — What is a patch's or a repeat's plan record, now that the kind lands?** Options: (a)
  `--placed-build` writes a minimal plan record through the door, citing the request by key; (b) the
  README stand-in of TOOL-dPlacedRequest-21 F2 stays, with an ask to dPlacedRequest. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 1: flow-steps.md:127 has `entry.claim` write "a patch's minimal plan
  record from its intake or filing, a repeat's from its playbook", and TOOL-dPlacedRequest-21 §3 holds
  the README scaffold only "until that kind lands". widens: none · relaxes: none
- **FACT-QUESTION · F5 — Can the kind be named `plan` beside the records already named `-plan-<n>.md`?**
  The probe: `git ls-files 'memory/builds/*/build/*'` matched against the loose stem `-plan-<n>.md` the
  typed-kind join generalises from `deviation_named` (`tools/memory-tree/tree_lib.py:491`), and against
  the strict stem `-build-<unit id>-plan-<n>.md`. The observation: six research records match the loose
  stem, `2026-10-20-build-PLAY-dClosedLoop-1-execution-return-plan-2.md` to `-7.md`, which is its
  liveness, and none matches the strict one. RESOLVED (agent, 2026-10-26, delegated): the kind keeps its
  node's name, and the named arm reads the strict stem for every typed kind, so those six stay bound
  (AC3); S2 carries the narrowing, and the main loop files the ask for dOrderedCharter, target
  PLAY-dOrderedCharter-42, accept "the typed-kind file-name join reads `-<kind>-<n>.md` only on the stem
  `-build-<unit id>-<kind>-<n>.md`, seen on a research record named `…-return-plan-2.md` staying bound
  once `plan` joins `TYPED_RECORD_KINDS`", which S2 satisfies if that build has not.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 16, the brief's I3 to I5, scout A's row 8,
  flow.md:98-145, flow-steps.md:127 and :184, and the two probes of §8 F3 and F5.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-19`, the hands-off edge to `TOOL-dRankedPlan-20`, the hands-off edge to `TOOL-dRankedPlan-27`, the hands-off edge to `TOOL-dRankedPlan-29`, each the reciprocal of that promoted unit's own edge (round-1 spec audit, `reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`); no other section moves.
- rev-3 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-33`, the hands-off edge to `TOOL-dRankedPlan-37`, each the reciprocal of that promoted unit's own edge (spec audit of units 19 to 29, `reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams extended are TOOL-dTotalRecall-1's registry and its factory verb `record_kinds.py new`, the
door `gov_record.py new` (TOOL-dTotalRecall-2), PLAY-dOrderedCharter-42's `TYPED_RECORD_KINDS` and the
factory `build_records.py`, and `render_handoff` (`tools/roles/handoff.py:312`) with its key families
and its `resolve_kit_dir` lookup. `python tools/codebase-map/reuse_lookup.py "check that a derived brief
never restates a field whose home is a higher level record"` ranked name stems (`check`, `records`,
`field`, `read_records`); none declares levels or grades a brief against a record's fields, so no
existing seam fits the levels check and S6 adds it beside the registry's own check. Scout A's row cited
`deviation_join.py:145` for `FIELD` and `:212` for `read_record`, both verified at base; it placed the
derived brief in `resolve_brief_record` (:283), which reads the intake record and is left as it is. The
recall query returned scout A's row, the brief's I3 to I5 and the night-pass instrument's quote of the
clause.

Recall terms used: `python tools/memory-recall/query.py "where are the artifact levels card plan brief declared and is the brief derived from the plan record" --terms "artifact levels card plan brief handoff derived never authored plan record one home FL-P2 gap-flow-03"`
