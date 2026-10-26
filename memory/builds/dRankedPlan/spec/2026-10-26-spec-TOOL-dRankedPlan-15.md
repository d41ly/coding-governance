# TOOL-dRankedPlan-15 — the plan revision record: a fork the goal cannot survive moves the build back to planning, and Design re-enters on the ratified revision

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 13 · advances TOOL-dRankedPlan-17

**Carries:** cl-dClosedLoop-0497@2b8de50e whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-1-fix-return.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-fix-return.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-13 TOOL-dRankedPlan-16 |
| [2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-b.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 |
| [2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-fix-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-13 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-16 |
| [2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) | spec-audit | TOOL-dRankedPlan-16 TOOL-dRankedPlan-1 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-2 TOOL-dRankedPlan-14 TOOL-dRankedPlan-13 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-8 TOOL-dRankedPlan-7 |

<!-- /gen:spec-records -->

## 1. Goal

A critical planning issue has no path today: no record of a plan revision exists, and none has
occurred in 173 builds (`gap-flow-04`). The owner's FL-P6 answer asks that "the plan needs to be
revised with a record, and its build re-designed" (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md:147-154`),
and FR-12 has the revision proceed under the request's mandate rather than park
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md:269-272`). This
unit builds the plan revision record: a fork the goal cannot survive moves the build from
`designing` back to `planning` by the move table's row B6, the planner records in the build's one
plan record what the revision changes in the ratified plan and why, the revision is ratified as the
plan is, and Design re-enters on the ratified revision, which a reader prints for Design to take.

## 2. Scope (IN)

- **S1** — The outcome. `revised` is one of the closed `outcomes` of the `item.plan.record` row in
  `tools/loop/loop.toml`, routed `transition`. The row's actor is `role:gov-planner` (I10, unit 2);
  `revised` is the plan revision's outcome that TOOL-dDeclaredLoop-15 §8 F2 names and its parent row
  P1 fires on, so TOOL-dDeclaredLoop-13 S6 grades P1's outcome against a declared value. Where the
  row at the build run's base already declares it, S1 changes nothing. Observed by AC6.
- **S2** — The entry grammar, I20. The build's one plan record (`record-kind.plan`, I3), found by
  `find_plan_record(root, slug)` (unit 16 S4), gains a `## Revisions` region at its end, holding one
  line per revision:
  `- **Revision <n>:** <what changed in the ratified plan> · <why> · from <sha8>`. `<n>` runs from 1
  with no gap; `<what>` and `<why>` are each one non-empty line holding no ` · `; `from` is the `sha`
  field of the build's newest `planning -> designing` transition, the commit at which the ratified
  plan the revision departs from was read. `check_plan_revisions(text)` in
  `tools/loop/plan_revision.py` returns the entries in order and raises naming the line on any other
  shape. An entry is not a field line in I3's `FIELD` form, since `Revision <n>` carries a digit
  `deviation_join.py`'s `FIELD` (:145) refuses, so no plan field reader misreads one. Observed by AC1,
  AC3 and AC8.
- **S3** — The verb, `record_revision(slug, what, why, repo)` and
  `python tools/loop/plan_revision.py revise --build <slug> --what <text> --why <text>`, the body of
  `item.plan.record`'s `revised` outcome, run by the planner. It refuses, exit 1 naming the cause and
  writing nothing, when the build's newest transition, read through `read_transitions`
  (TOOL-dDeclaredLoop-3 S7), does not end in `designing`, the one state B6 leaves, and when the
  index holds a staged path other than the plan record; it exits 2 on a `--what` or `--why` that is
  empty, longer than 200 characters, or holds ` · `, a newline or another control character. Then it
  appends the entry, commits the plan record alone with the subject `plan revision(<slug>): <n>`,
  and records B6 through `write_transition` (TOOL-dDeclaredLoop-3 S5): `--from designing --item
  item.design.decompose`, the outcome word B6's `[[transition]]` row carries, read from that row and
  never typed here, `--witness` the commit just made, as the witness cell of flow-steps.md:742 reads,
  and `--field revision=<n>`. It prints `revision — <n> · designing → planning · <sha8>`. The
  planner then rewrites the plan's fields in `planning`, where unit 14 admits a re-pick of
  `Scenario` with its `Scenario reason` and Plan's exit pins it (I19). Observed by AC1, AC4 and AC5.
- **S4** — The trailer field. `revision` joins `TRANSITION_FIELDS` in
  `tools/loop/loop_transition.py`, the tuple TOOL-dDeclaredLoop-3 §4 "The trailer" ships for later
  units to extend, so B6's trailer and log record carry `revision=<n>`. Observed by AC1.
- **S5** — Ratified as the plan is, and Design re-entered. `derive_revision_state(slug, repo)` and
  `python tools/loop/plan_revision.py show --build <slug>` read the newest entry `<n>`, its B6 move
  by the trailer's `revision=<n>`, any `planning -> designing` move newer than that B6, which is
  Design re-entered, and the ratification through `read_plan_ratification(slug)` (I6, unit 9). The
  revision takes no ratification path of its own: the move out of `planning` is `plan.exit`'s, held
  by whatever `plan.ratification` and unit 10's fallback hold the plan's. It prints one line:
  `revision — none`; `revision — <n> · awaiting ratification · <what>` while no re-entry follows the
  B6; or `revision — <n> · ratified · <value> · <witness> · design re-entered at <sha8>`. Two
  re-entries exit 1 instead: one that `read_plan_ratification` answers with no witness prints
  `revision — <n> · design re-entered without ratification`, and one at whose commit every field
  line of the plan record outside `## Revisions` equals the same field at `from`, read by
  `git show <from>:<path>` in the factory's `FIELD` form, prints
  `revision — <n> · no field changed since <sha8>`, since a revision records what it changes in the
  ratified plan. This line is what Design receives: the stand-in for dIndexedDesign's
  `design.input` reading "a ratified plan revision" (flow-steps.md:223, :235) until that build
  lands. Observed by AC1, AC2 and AC7.
- **S6** — The plants of `plan_revision.py --selftest [--plant <case>]`: `goal-fork`, `no-change`,
  `bad-entries`, `wrong-state`, `bad-text`, `unratified-reentry` and `second-revision`, in a scratch
  repository under the system temp directory, with the loop kit's own `write_transition` and
  `read_transitions` and a stub `read_plan_ratification` answering the planted value and witness.
  The leg `loop plan revision` runs it, with the rows a new leg owes, as TOOL-dDeclaredLoop-3 S8 adds
  its own. Observed by AC1 to AC5, AC7 and AC8, through the `New arm:` line.
- **S7** — The page `help/loop.md` (TOOL-dDeclaredLoop-1's) gains a section on the plan revision:
  when a build moves back to planning, the `revise` and `show` verbs, the entry grammar, and that the
  revision is ratified as the plan is. Observed by AC9.

## 3. Non-goals (OUT)

- Design's re-design inventory after a revision, each completed unit kept, amended or retired:
  dIndexedDesign's `design.inventory` (`gap-flow-25`, v2:721, flow-steps.md:237).
- Detecting a fork the goal cannot survive: dIndexedDesign's `design.decompose` raises it
  (flow-steps.md:239). Until it lands, whoever meets such a fork in Design runs `revise`.
- The ratification itself, its intake and its owner-gate fallback: units 9 and 10, and
  TOOL-dDeclaredLoop-19's owner gate at `item.plan.exit`. S5 reads the answer and adds no gate.
- The plan record's kind, file, writer and fields: unit 16's. A revision rewrites fields that unit
  owns and appends only its own region.
- The scenario field, its re-pick and its check: unit 14's `check_plan_scenario`, which admits a
  re-pick in the `planning` a revision moves the build back to and refuses one anywhere past it.
- A plan revision's review: unit 6 pins it as a Plan Review subject.
- The parent-withdrawal route P1 and `deps.on-parent-withdrawn`: TOOL-dDeclaredLoop-15's, which
  routes its own `replan` through the same `revised` outcome.
- Parking on a goal-level fork: `run.on-owner-question` and `design.forks` (v2's P18) are not read.

### Edges

- **consumes-from** `TOOL-dRankedPlan-16` — `record-kind.plan`, the one plan record per build whose fields a revision rewrites and whose end this unit's `## Revisions` region joins
- **consumes-from** `TOOL-dRankedPlan-9` — `read_plan_ratification`, which S5 reads to say whether the revision was ratified as the plan is, and with which witness
- **consumes-from** `TOOL-dRankedPlan-2` — `gov-planner`, the role whose `item.plan.record` row carries the `revised` outcome and who runs `revise`
- **consumes-from** `TOOL-dRankedPlan-14` — `Scenario reason`, the field a planner rewrites with `Scenario` in the `planning` a revision reopens, the one route to a re-pick after Plan
- **hands-off** `TOOL-dRankedPlan-6` — `## Revisions`, the region whose newest entry a Plan Review of a revision reads at its pinned blob
- **consumes-from** external — dDeclaredLoop, built before this build run: `write_transition`, `read_transitions` and `TRANSITION_FIELDS` (TOOL-dDeclaredLoop-3 S5, S7, §4), rows B4 and B6 (TOOL-dDeclaredLoop-13), the backward move recorded like any other (TOOL-dDeclaredLoop-10 S2, S5), and P1 with its §8 F2 (TOOL-dDeclaredLoop-15)
- **hands-off** external — dIndexedDesign: its `design.decompose` runs `revise` on a fork the goal cannot survive, and its `design.input` reads the ratified revision `show` prints
- **hands-off** `TOOL-dRankedPlan-23` — `derive_revision_state` and `show`, whose ratification read that unit re-points to the recorded re-entry (round-1 spec audit, id 4)
- **hands-off** `TOOL-dRankedPlan-29` — `revise`, `show` and the `loop plan revision` leg, which that unit's S26 and S36 correct (round-1 spec audit, ids 31, 46)

## 4. Design

### Evidence

- The move exists as a row, not as a record: B6 `designing --item.design.decompose--> planning`
  (TOOL-dDeclaredLoop-13 §4, from flow-steps.md:742, whose witness cell reads "the plan
  revision"), recorded through `write_transition` with no direction branch (TOOL-dDeclaredLoop-10
  S2), and Plan re-entered by a recorded row (its S5).
- `item.plan.record`'s `revised` outcome is the plan revision (TOOL-dDeclaredLoop-15 §8 F2), and
  flow-steps' `plan.record` row names no `revised` in its Then cell (flow-steps.md:184), so no
  parent declares the value.
- Design's seven inputs include "a ratified plan revision" (flow-steps.md:223), routed by
  `design.input` to `design.inventory` (:235, :237), both dIndexedDesign's.
- `TRANSITION_FIELDS` admits a later unit's field, each value `[A-Za-z0-9._:+@-]+`
  (TOOL-dDeclaredLoop-3 §4 "The trailer"), which an integer revision number meets.
- No code seam: `plan_state` (`tools/unattended/unattended.sh:4458`) grades §8 forks, and `plan` in
  `tools/memory-tree/gen_build_index.py:2674` is the index's build plan; neither records a revision.

### The flow

| Step | Act | Recorded as | State after |
|---|---|---|---|
| 1 | Design meets a fork the goal cannot survive | the fork, in the spec's §8 | designing |
| 2 | `revise` appends `Revision <n>` and commits it | `plan revision(<slug>): <n>` | designing |
| 3 | `revise` records B6, witness the commit of 2 | `Gov-Transition: designing -> planning · … · revision=<n>` | planning |
| 4 | the planner rewrites the plan's fields, a `Scenario` re-pick with its reason among them | the plan record's commits | planning |
| 5 | ratification, as `plan.ratification` holds the plan's | units 9 and 10, TOOL-dDeclaredLoop-19 | planning |
| 6 | `plan.exit` records B4, unit 14 pinning the scenario | `Gov-Transition: planning -> designing · …` | designing |
| 7 | Design reads `show` | `revision — <n> · ratified · …` | designing |

Under `plan.ratification: request`, step 5 is the request already standing: FR-12's "the planner's
plan revision proceeds under your request's mandate, recorded for you". Under any other value it is
the owner gate at `item.plan.exit`, released by the owner's disposition record.

### Data model

```markdown
## Revisions

- **Revision 1:** Scope narrows to the reader; the writer moves to a new build · F2 of the unit-3 spec: no option keeps the goal's write path · from 3f9c2a71
```

```
REVISION_RE = ^- \*\*Revision ([1-9][0-9]*):\*\* ([^\n]+?) · ([^\n]+?) · from ([0-9a-f]{8,40})$
```

`show`'s three states read only the newest entry; `check_plan_revisions` grades every entry.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/loop/plan_revision.py` | module | none |
| `record_revision`, `derive_revision_state`, `check_plan_revisions` | Python functions | `py.function`, asked at the pass |
| `REVISION_RE` | constant | none |
| `revise`, `show`, `--selftest`, `--plant` | verbs and flags of `plan_revision.py` | none |
| `revision` | `Gov-Transition` field | none |
| `## Revisions` | plan-record region | none |
| `revised` | outcome word of `item.plan.record` | none |
| `loop plan revision` | gate leg | none |

### Migration

None. A plan record with no `## Revisions` region reads `revision — none`.

### Rollout

Live at landing. Nothing runs `revise` but a planner meeting a fork the goal cannot survive.

### Files touched (estimate)

- `tools/loop/plan_revision.py`: S2, S3, S5, S6
- `tools/loop/loop_transition.py`: `TRANSITION_FIELDS` gains `revision`
- `tools/loop/loop.toml`: `revised` on `item.plan.record`
- `tools/loop/kit.toml`: the module shipped
- `tools/gate-legs.json`: the leg `loop plan revision`
- `tools/govkit/registry.toml`: the rows the new leg owes
- `tools/govkit/subject-pins.tsv`: the rows the new leg owes
- `tools/run-gates/selftest-budgets.txt`: the leg's budget row
- `help/loop.md`: S7

### Alternatives rejected

- **A record kind of its own for the revision.** The owned nodes hold `record-kind.plan` and no
  revision kind, and the clause's "one plan record per build" (unit 16) keeps one home (§8 F2).
- **A second plan record per revision.** Two plan records per build break I3's one file, and every
  field reader would have to pick one.
- **The revision fired by `item.plan.record` alone, through P1.** P1 is the parent-withdrawal row,
  `when = "before-push"`, witnessed by the parent's post; a fork's move is B6's (§8 F1).
- **Design's re-entry derived from a field on the `plan.exit` trailer.** That writes into unit 10's
  and dDeclaredLoop's exit; the re-entry is derivable from the move order, so `show` derives it.

## 5. Production-readiness checklist

- security — one new write path: `revise` writes the build's own plan record and one commit in the
  session's tree. `--what` and `--why` are validated at that boundary (S3); `--build` is held to
  `^[A-Za-z0-9]+$` before it reaches a path. A staged foreign path refuses the commit.
- perf / scale — one `read_transitions` and one commit per revision; `show` adds one `git show`.
- error / empty / loading states — every refusal names its cause and writes nothing; a malformed
  region exits 2 naming the line; a build with no plan record exits 2 naming the build.
- observability — the printed line, the `revision=<n>` field on B6, and the `show` line.
- risks — two sessions revising one build: the second `revise` finds the state `planning` and is
  refused before it writes. A revision whose fields the planner never rewrites is caught only when
  Design re-enters, by `show`'s exit 1, not before ratification. A planner editing fields past
  `planning` without `revise` is unit 14's and unit 16's checks' to grade.
- testing — S6's plants, red and green.
- migration — none.
- user docs — `help/loop.md`, S7.

## 6. Acceptance criteria

- **AC1** — When `python plan_revision.py --selftest --plant goal-fork` runs, a scratch build `tFix`
  at `designing` after a B4 whose `sha` is A, its plan record's `Scope` rewritten, `revise --build
  tFix --what <w> --why <y>` prints `revision — 1 · designing → planning`; the plan record ends in
  `- **Revision 1:** <w> · <y> · from <A>`; the newest `Gov-Transition` trailer reads
  `designing -> planning · build=tFix · item=item.design.decompose` with `revision=1`; `show`
  prints `awaiting ratification`; and after a planted `plan.exit` move with the stub answering
  `request` and a witness, `show` prints `revision — 1 · ratified · request · <witness> · design
  re-entered at <sha8>`.
  Red when: the B6 trailer is absent or carries no `revision=`, or `show` prints `ratified` before
  the `planning -> designing` move.
- **AC2** — When the plant `no-change` revises, leaves every field as it stood at A and records the
  `plan.exit` move, `show` exits 1 printing `revision — 1 · no field changed since <A>`.
  Red when: a revision that changes nothing in the ratified plan reads as ratified.
- **AC3** — When the plant `bad-entries` runs `check_plan_revisions` over a region numbered 1 then
  3, over an entry with no `from`, and over an entry whose `<what>` holds ` · `, each raises naming
  its line; over a well-formed region it returns the entries.
  Red when: a malformed or gapped region is accepted.
- **AC4** — When the plant `wrong-state` runs `revise` on a build whose newest transition ends in
  `building`, and again on one at `planning`, each exits 1 naming the state and no trailer is
  written.
  Red when: a revision opens from a state B6 does not leave.
- **AC5** — When the plant `bad-text` runs `revise` with a `--what` holding ` · `, then a newline,
  then 201 characters, each exits 2 naming `--what`, and the branch gains no commit.
  Red when: text that would break the entry grammar is written.
- **AC6** — When `python loop_table.py check` (TOOL-dDeclaredLoop-13 S9) runs over the tree, it
  exits 0 with P1's `revised` resolved on `item.plan.record`; on a scratch copy of `loop.toml`
  without `revised` in that row's `outcomes`, it reds naming `item.plan.record` and `revised`.
  Red when: P1 fires on an outcome its item does not declare.
  fixture: the loop kit is dDeclaredLoop's, untracked at base until it lands.
- **AC7** — When the plant `unratified-reentry` records a `planning -> designing` move after the
  B6 with the stub answering no witness, `show` exits 1 printing `design re-entered without
  ratification`.
  Red when: a re-entry with no ratification reads as ratified.
- **AC8** — When the plant `second-revision` revises a build already revised and ratified once,
  the entry is `Revision 2` and its `from` is the second B4's `sha`.
  Red when: numbering restarts, or `from` names the first ratification.
- **AC9** — When `grep -n "plan revision" loop.md` runs over the help page, it finds S7's section
  naming `revise`, `show` and the `## Revisions` region.
  Red when: the page does not describe the revision.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/loop/plan_revision.py · covers AC1 AC2 AC3 AC4 AC5 AC7 AC8 · the `loop plan revision` leg's `--selftest`, its failing case staged by a `revise` that records B6 without the `revision=` field · none

## 8. Open questions

- **F1 — Which item fires the move, and from which states?** The clause moves the build "from
  designing back to planning"; B6 is that row, fired by `item.design.decompose` on a fork the goal
  cannot survive (flow-steps.md:742), while P1 also reaches `planning` on `item.plan.record`'s
  `revised` but is the parent-withdrawal row. RESOLVED (agent, 2026-10-26, delegated): B6, from
  `designing` only, its witness the revision commit as :742's witness cell reads, rung 1; the record
  is `item.plan.record`'s `revised` (TOOL-dDeclaredLoop-15 §8 F2). widens: none · relaxes: none
- **F2 — A revision kind of its own, or a region of the plan record?** RESOLVED (agent, 2026-10-26,
  delegated): a `## Revisions` region of the build's one plan record, rung 1: the packet's owned
  nodes hold `record-kind.plan` and no revision kind, and the sibling clause gives each build one
  plan record. widens: none · relaxes: none
- **F3 — "Ratified as the plan is" against FR-12's "proceeds under your request's mandate".**
  RESOLVED (agent, 2026-10-26, delegated): the same reading, rung 1: under `plan.ratification:
  request` the standing request ratifies the revision, which is what FR-12 says, and under any other
  value the owner gate at `item.plan.exit` does; S5 reads `read_plan_ratification` and adds no path.
  widens: none · relaxes: none
- **F4 — Does this unit inventory the completed work Design keeps?** RESOLVED (agent, 2026-10-26,
  delegated): no, rung 1: the re-design inventory is `gap-flow-25`, dIndexedDesign's (v2:721), a
  non-goal. widens: none · relaxes: none
- **F5 — Who records B6 while no Design item raises the fork?** Options: (a) `revise` records the
  revision and then B6, its witness the revision commit; (b) the caller records B6 and `revise`
  writes the entry only. (b) splits one act into two commands whose order the witness cell fixes,
  and a B6 recorded first has no revision to witness. RESOLVED (agent, 2026-10-26, delegated): (a),
  rung 3, the most feature-rich survivor: the witness is always the revision, and dIndexedDesign's
  `design.decompose` calls the same verb when it lands. widens: none · relaxes: none
- **F6 — How does Design receive the revision before `design.input` lands?** Options: (a) a
  `revision=` field on B6 and a `show` line deriving the re-entry from the move order; (b) a field
  on the `plan.exit` trailer naming the revision. (b) writes into unit 10's and dDeclaredLoop's exit
  for a fact the order already carries. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3.
  widens: none · relaxes: none
- **F7 — I20's entry grammar: does an entry name the ratified plan it departs from?** The brief's
  proposed spelling is `- **Revision <n>:** <what changed in the ratified plan> · <why>`. RESOLVED
  (agent, 2026-10-26, delegated): it gains ` · from <sha8>`, rung 3: without it "what the revision
  changes in the ratified plan" is a claim no reader can check, and with it S3 refuses a revision
  that changes nothing. The refinement is the owner unit's, I20's, and is returned to the main loop.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 15, FL-P6, FR-12, flow-steps.md:184,
  :223, :235-239 and :742, TOOL-dDeclaredLoop-3 S5 and S7, -10 S2 and S5, -13 §4, -15 S4 and §8 F2,
  and scout B's row for this unit.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-23`, the hands-off edge to `TOOL-dRankedPlan-29`, each the reciprocal of that promoted unit's own edge (round-1 spec audit, `reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams extended are TOOL-dDeclaredLoop-3's transition writer and reader (`write_transition`,
`read_transitions`) and its `TRANSITION_FIELDS` tuple, which that spec ships for later units to
extend; TOOL-dDeclaredLoop-13's row B6 and TOOL-dDeclaredLoop-15's `revised` outcome; and unit 16's
plan record. `python tools/codebase-map/reuse_lookup.py "record a plan revision moving a build from
designing back to planning"` ranked name stems only (`build`, `records`, `plan` in
`tools/memory-tree/gen_build_index.py:2674`, `plan_state` at `tools/unattended/unattended.sh:4458`,
`DesignRefusal`); each was opened and none records a revision or a backward move, so no existing
seam fits the record and the verb is new beside the loop kit's transition modules. Scout B's row
named `tools/loop/loop_table.py` for "the move only, no new code path"; that holds, since B6 is
recorded through the writer unchanged, and the scout's `record-kinds.toml` row for the plan kind is
unit 16's, not this unit's. The recall query returned the clause text, scout B's row and
TOOL-dDeclaredLoop-13's table, and no prior revision mechanism.

Recall terms used: `python tools/memory-recall/query.py "how is a plan revision recorded when a fork the goal cannot survive sends a build back to planning" --terms "plan revision fork goal cannot survive designing planning B6 write_transition ratified re-design FR-12"`
