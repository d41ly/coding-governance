# TOOL-dRankedPlan-6 — Plan Review: the plan record a review subject, run with the lenses of the preset `review.pin` passes until dCalibratedLens's Plan lenses land

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 14 · advances TOOL-dRankedPlan-17

**Carries:** cl-dClosedLoop-0374@c6143eda whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-1-fix-return.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-fix-return.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-5 TOOL-dRankedPlan-13 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-build-TOOL-dRankedPlan-1-repin-return.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-repin-return.md) | research | TOOL-dRankedPlan-5 TOOL-dRankedPlan-9 |
| [2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-b.md) | research | TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-15 |
| [2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-fix-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-5 TOOL-dRankedPlan-13 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-repin-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-repin-brief.md) | research | TOOL-dRankedPlan-5 TOOL-dRankedPlan-9 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing reviews a plan, a backlog or a priority order (`gap-plan-04`). dDeclaredLoop places a Plan
breakpoint before `item.plan.exit` under `review.<stage>` (TOOL-dDeclaredLoop-19 S2) and fires it
through `--trigger` (TOOL-dDeclaredLoop-20 S2), and dFairHearing's `review.pin` stand-in maps each
subject to a preset (TOOL-dFairHearing-3 S8), but no lens catalogue row is a Plan lens until
dCalibratedLens lands one, and v2's whole-design audit found the Plan breakpoint would run with no
lens in the meantime (C5-F14, v2:706-707). This unit makes the build's plan record, and a plan
revision in it, a review subject that `review.pin` maps to a preset of its own, so Plan Review runs
the five lenses of the preset `review.pin` passes from dFairHearing's catalogue, seen on a tree that
holds no Plan lens.

## 2. Scope (IN)

- **S1** — The plan arm of `review.pin`. `tools/workflows/review_pin.py` reads each non-spec
  subject's `**Serves:**` line, the first line of the file opening `**Serves:** `, and takes its
  first word as the subject's record kind; a subject whose kind is `plan`, the token of
  `record-kind.plan` (I3, unit 16), is a plan subject. When every subject is a plan subject the
  preset is `PLAN_RECORD_PRESET`, a module constant whose value is `unit-spec`; a plan subject beside
  any other subject counts as a non-design subject under TOOL-dFairHearing-3 S8's rule, which then
  maps the set to `unit-spec`. `DESIGN_RECORD_PRESET` and `--design-record-preset` therefore never
  reach a plan record, since a plan is neither a design nor an architecture record
  (flow-steps.md:570). A subject file that does not open or carries no `**Serves:**` line reads as a
  design subject, as it does at base. Observed by AC1 and AC2.
- **S2** — The subject. A Plan Review's subject is the build's one plan record, the file
  `gov-planner` drafts at `item.plan.record` and `find_plan_record(root, slug)` returns (unit 16 S4),
  passed to TOOL-dDeclaredLoop-20's
  `--trigger <slug> --subject <path> --cause <c>` when the Plan breakpoint fires, and to the harness
  as a spec-audit subject `{path, blob, id}` whose `id` is the anchor id the plan record's
  `**Serves:**` line names. The harness already admits a subject outside `builds/<slug>/spec/` as a
  design-document subject served bare, with no `rev` (`tools/workflows/tier2-review.template.js:317`,
  :428-434). A plan revision is reviewed as the same file at the blob that carries its newest
  `## Revisions` entry (unit 15), which the record's `Reviewed: <path>@<blob>` line pins. Observed by
  AC3.
- **S3** — The arms in `tools/workflows/tier2-review.test.sh`: `review_pin.py` over a planted plan
  record, alone and beside a spec and a design record, under each `--design-record-preset` value;
  and the harness evaluated with stub agents over that record as its one subject, recording five
  finder spawns. Observed by AC1, AC2 and AC3, through the `New arm:` line.
- **S4** — The docs. `tools/workflows/README.md`'s `review_pin.py` section gains the plan arm and
  `PLAN_RECORD_PRESET`; `help/loop.md` (TOOL-dDeclaredLoop-1's page) gains a paragraph on Plan
  Review: its subject, its preset until dCalibratedLens's Plan lenses land, and that it is placed
  only where `review.<stage>` places the Plan breakpoint. Observed by AC5.

## 3. Non-goals (OUT)

- The Plan lenses, "order, dependencies, duplicates, overlap with live work and readiness"
  (walkthrough.md:354-355): dCalibratedLens's, which re-points `PLAN_RECORD_PRESET` to its Plan
  literal in the landing that ships that literal's marker and rows.
- Where the Plan breakpoint sits, when it fires and who disposes it: TOOL-dDeclaredLoop-19's
  `review.<stage>` and `derive_breakpoints`, and TOOL-dDeclaredLoop-20's `--trigger`.
- The disposal of a plan subject's findings: `review.dispose` declares "a plan revision →
  `plan.record`" as a route and arms no consumer (TOOL-dDeclaredLoop-20 §3), and arming it is a
  disposal mechanism of its own (§8 F5).
- The harness's subject validation, the binding line and the lens catalogue: dFairHearing's and
  dTrueNorth's, read here and never re-specced.
- The plan record and its revision region: units 16 and 15.

### Edges

- **consumes-from** `TOOL-dRankedPlan-16` — `record-kind.plan`, the kind whose `**Serves:**` token `plan` makes a subject a plan subject, and the one plan record a Plan Review pins
- **consumes-from** `TOOL-dRankedPlan-2` — `gov-planner`, whose `item.plan.record` drafts the record the Plan breakpoint reviews before `item.plan.exit`
- **consumes-from** `TOOL-dRankedPlan-15` — `## Revisions`, the region whose newest entry marks the blob a Plan Review of a revision pins
- **consumes-from** external — dFairHearing, built before this build run: `review_pin.py` and `DESIGN_RECORD_PRESET` (TOOL-dFairHearing-3 S8, -25 S5), the lens catalogue and its markers (TOOL-dFairHearing-13), the `preset` argument (TOOL-dFairHearing-2)
- **consumes-from** external — dDeclaredLoop: the Plan breakpoint (TOOL-dDeclaredLoop-19 S2) and `--trigger` (TOOL-dDeclaredLoop-20 S2)
- **hands-off** external — dCalibratedLens re-points `PLAN_RECORD_PRESET` to its Plan literal when its Plan lenses land

## 4. Design

### Evidence

- The harness tells a spec subject from a design subject by path alone,
  `SPEC_SUBJECT_PATH = /(?:^|\/)builds\/[^/]+\/spec\//` (`tools/workflows/tier2-review.template.js:317`),
  and admits a design subject with an `id` in `PIN_ID`'s grammar and no `rev` (:416, :428-434), served
  bare on the binding line (:318-329). A plan record under `builds/<slug>/build/` is such a subject.
- `review_pin.py` maps every design subject to `DESIGN_RECORD_PRESET`, `unit-spec` until a replay
  verdict flips it to `design-audit` (TOOL-dFairHearing-3 S8, TOOL-dFairHearing-25 S5), and
  TOOL-dFairHearing-23 widens `--design-record-preset` to `whole-design`. Without S1 a plan record
  would follow those flips.
- flow-steps' `review.pin` passes `design-audit` only "when every pinned spec revision is a design or
  architecture record by the record-kind registry" (flow-steps.md:570), and names "the plan
  revision" first among the artifacts it pins.
- At base no lens literal is a Plan literal: `tools/workflows/tier2-review.template.js` holds two
  literals, `DIFF_LENSES` (:774) and `SPEC_LENSES` (:810), and `tools/workflows/lenses.toml` does
  not exist; the parents add `diff-review`, `unit-spec`, `design-audit` and `whole-design` as marked
  literals (TOOL-dFairHearing-13 S3, -2, -18) and none for Plan.

### The mapping

| Subjects | Preset `review_pin.py` prints |
|---|---|
| every subject a plan record | `PLAN_RECORD_PRESET`, `unit-spec` |
| any spec subject, or a plan record beside another subject | `unit-spec`, TOOL-dFairHearing-3 S8's rule |
| every subject a design record | `DESIGN_RECORD_PRESET`, or `--design-record-preset` |

```
python <kit>/review_pin.py --subject memory/builds/dX/build/2026-10-27-build-TOOL-dX-1-plan-1.md
{"preset": "unit-spec"}
```

The kind is read from the subject itself, the one place `record-kind.plan`'s writer states it, so
`review_pin.py` spells no plan-record filename of its own; the workflows kit reads no sibling kit's
registry. `--opt-in`'s entry for `unit-spec` applies to a plan subject as to a spec subject.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `PLAN_RECORD_PRESET` | constant, `tools/workflows/review_pin.py` | none |
| `read_subject_kind` | Python function, `review_pin.py` | `py.function`, asked at the pass |
| the plan arms of S3 | suite arms | none |

### Migration

None. A subject set holding no plan record maps exactly as at base.

### Rollout

Live at landing wherever `review.<stage>` places the Plan breakpoint; under its default, `opt-in`,
only for a build that opts in.

### Files touched (estimate)

- `tools/workflows/review_pin.py`: S1
- `tools/workflows/tier2-review.test.sh`: S3
- `tools/workflows/README.md`: S4
- `help/loop.md`: S4

### Alternatives rejected

- **A filename test for the plan record.** It would spell unit 16's name grammar a second time in
  another kit (§8 F4).
- **Detecting a Plan literal in the rendered harness and switching to it.** It fixes the name of a
  literal dCalibratedLens has not chosen, a later build's surface the packet's Non-goals keep out
  (§8 F1).
- **A plan subject left on the design-record preset.** A replay verdict about design records would
  then move Plan Review's lenses with no Plan reason (§8 F1).

## 5. Production-readiness checklist

- security — no new write path: `review_pin.py` reads at most one line of each subject file it is
  handed and prints one JSON line; the subject paths are the caller's, refused as TOOL-dFairHearing-23
  S46 refuses a backslashed one.
- perf / scale — one bounded read per non-spec subject.
- error / empty / loading states — an unreadable subject or one with no `**Serves:**` line reads as
  a design subject, the base behaviour; the harness's own refusals are unchanged.
- observability — the printed `preset`, and the review record's `Reviewed:` and binding lines.
- risks — a plan record whose `**Serves:**` kind is mistyped reviews under the design-record preset;
  unit 16's writer is the one producer of that line. Until `review.dispose`'s plan route is armed, a
  Plan Review's confirmed findings are read by whoever runs the breakpoint (§8 F5).
- testing — S3's arms, red and green.
- migration — none.
- user docs — `help/loop.md`, S4.

## 6. Acceptance criteria

- **AC1** — When `python review_pin.py --subject <plan record>` runs over a planted plan record
  whose first `**Serves:**` line reads `**Serves:** plan TOOL-dX-1`, it prints `{"preset":
  "unit-spec"}`, and with `--design-record-preset design-audit` it still prints `unit-spec`.
  Red when: a plan record maps to the design-record preset.
- **AC2** — When the same command runs with the plan record beside a spec subject, it prints
  `unit-spec`; over a design record alone with `--design-record-preset design-audit`, it prints
  `design-audit`; over a plan-named file whose `**Serves:**` kind is `research`, it prints the
  design-record preset.
  Red when: the plan arm moves a subject set holding no plan record, or a filename alone makes a
  plan subject.
- **AC3** — When `grep -nE "(SPEC_SUBJECT_PATH|PIN_ID) = /" tier2-review.js` runs over the rendered
  harness at the pass tip and `node -e` tests the two printed patterns against a planted plan record,
  named `2026-10-27-build-TOOL-dX-1-plan-1.md` under a fixture build's `build/` folder, and its anchor
  id `TOOL-dX-1`: the record's path does not match `SPEC_SUBJECT_PATH`, so the harness takes it as a
  design-document subject served bare with no `rev` (:428-434), and the id matches `PIN_ID` (:416).
  The harness evaluated with stub agents over that one subject at `kind: spec-audit`, `preset:
  unit-spec`, five finder spawns at the `unit-spec` literal's lens keys and the bare binding line
  `**Serves:** spec-audit TOOL-dX-1`, is the §7 `New arm:` line's to observe.
  Red when: the plan record's path reads as a spec subject, or its anchor id falls outside `PIN_ID`.
- **AC4** — When `grep -n "gov:lens-slots" tier2-review.template.js` and `grep -n "presets"
  lenses.toml` run over the tree AC3 evaluates, no marker and no row names a Plan literal, and the
  preset AC1 prints is one of the marked literals; the same greps print each marker and row they
  find, so a Plan literal, once added, is listed.
  Red when: AC3 passes only because a Plan literal is present.
  fixture: the catalogue and its markers are dFairHearing's, untracked at base until it lands.
- **AC5** — When `grep -n "PLAN_RECORD_PRESET" README.md` runs over `tools/workflows/` and
  `grep -n "Plan Review" loop.md` over the help page, each finds S4's text.
  Red when: either page omits the plan arm.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `verifier fan-out self-test`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3 · `review_pin.py` and the harness over a planted plan record, the failing case a plan record that maps to the design-record preset under `--design-record-preset design-audit` · none

## 8. Open questions

- **F1 — Which preset does a plan subject take until the Plan lenses land?** Options: (a) TOOL-dFairHearing-3
  S8's design-record preset, as any non-spec subject; (b) a constant of its own, `unit-spec`, that
  dCalibratedLens re-points; (c) a Plan literal detected in the rendered harness. (a) moves with a
  replay verdict about design records, which flow-steps.md:570 scopes to design and architecture
  records; (c) names a literal of a later build. RESOLVED (agent, 2026-10-26, delegated): (b), rung
  1: the clause's "the preset `review.pin` passes" is `unit-spec` for a non-design subject, and
  flow-steps.md:570 keeps the design-record presets off a plan. widens: none · relaxes: none
- **FACT-QUESTION · F2 — Is "a tree that holds no Plan lens" the tree this unit is built on?** Probe:
  `git grep -n "gov:lens-slots" -- tools/workflows/` and `git ls-files tools/workflows/lenses.toml`
  at base, and a read of the literals TOOL-dFairHearing-13, -2 and -18 add. Observation, 2026-10-26
  at `911a7039`: no marker, no catalogue file, and the specced literals are `diff-review`,
  `unit-spec`, `design-audit` and `whole-design`. Liveness: the grep prints every marker it finds,
  so a Plan literal would be listed. RESOLVED (agent, 2026-10-26, delegated): yes, and AC4 re-reads
  it on the tree AC3 runs. widens: none · relaxes: none
- **F3 — Does this unit write the Plan lenses walkthrough.md:354-355 lists?** RESOLVED (agent,
  2026-10-26, delegated): no, rung 1: they are dCalibratedLens's, the clause runs "until" they land,
  and the packet's Non-goals keep that build's surfaces out. widens: none · relaxes: none
- **F4 — How does `review.pin` know a subject is a plan record?** Options: (a) the subject's own
  `**Serves:**` kind; (b) a filename pattern for I3's name; (c) the record-kind registry's `home`
  glob. (b) spells unit 16's grammar twice, and (c) has the workflows kit read a sibling kit's
  registry. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, by the tie-break: one spelling,
  the record's own. widens: none · relaxes: none
- **F5 — Does this unit arm `review.dispose`'s plan route?** Options: (a) arm "a plan revision →
  `plan.record`" here; (b) leave the declared route to its own unit. (a) adds a disposal mechanism
  across the driver's owed count and the build harness's DISPOSAL stage (TOOL-dDeclaredLoop-20 S4,
  S5), a second mechanism in this spec (BUILD-METHOD M2), and the clause asks for the review to run.
  RESOLVED (agent, 2026-10-26, delegated): (b), rung 3; the main loop is asked to file the arming
  as an ask: target dRankedPlan, "a Plan Review's confirmed findings on a plan record or revision
  are disposed to `item.plan.record` as `review.dispose` declares", accept: a planted Plan Review
  finding reaches `plan.record`'s next draft, seen red with the route unarmed. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 6, C5-F14 (v2:706-707),
  flow-steps.md:570, TOOL-dFairHearing-3 S8, TOOL-dDeclaredLoop-19 S2 and -20 §3, and scout B's row
  for this unit.

## 10. Reuse audit

The seam extended is TOOL-dFairHearing-3 S8's `review_pin.py`, its subject-to-preset mapping, with
the harness's design-document subject path (`tools/workflows/tier2-review.template.js:317`,
:428-434, verified at base) carrying the plan record unchanged. `python
tools/codebase-map/reuse_lookup.py "map a review subject's record kind to the lens preset passed to
the review harness"` ranked name stems (`records`, `map_root`, `read_records`,
`resolve_harness_path`); none maps a subject to a preset, and `review_pin.py` is absent at base, so
the seam is the parent spec's and no other existing seam fits. Scout B's row named the same seam
and `tools/loop/loop.toml`'s `review.dispose` route, which §8 F5 leaves to its own unit. The recall
query returned the clause, TOOL-dFairHearing-3's brief row and spec, and scout B's F6a, and no
disagreement with source beyond the literals, which are specced and not built at base.

Recall terms used: `python tools/memory-recall/query.py "which lens preset does a plan review run before the Plan lenses exist" --terms "Plan Review review.pin preset lens catalogue dCalibratedLens stand-in unit-spec DESIGN_RECORD_PRESET plan record subject"`
