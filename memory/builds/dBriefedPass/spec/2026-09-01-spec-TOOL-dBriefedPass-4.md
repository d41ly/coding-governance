# TOOL-dBriefedPass-4 — the harness: one Workflow script driving spec, audit, fold and build in order

**Status:** SPECCED · rev-1 · 2026-09-01 · node d · Tier-2 · base 269dacae · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-prompt-TOOL-dBriefedPass-1.md](../prompts/2026-09-01-prompt-TOOL-dBriefedPass-1.md) | research | TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-5 |

<!-- /gen:spec-records -->

## 1. Goal

Ship `tools/workflows/unattended-build.js`, a Workflow script that performs a build's SPECCING,
REVIEWING, FOLDING and BUILDING passes as ordered stages of one program, so the pass order is a
property of control flow rather than of an agent's recollection across a context that compacts.

## 2. Scope (IN)

- **S1** — the script takes a structured `args` object carrying `repo`, `slug`, `base`, `units` and
  `briefDir`, and REFUSES a prose string or a missing `repo` with the parse-then-validate guard
  `tier2-review.js:32-60` already carries. `TOOL-dTieredTribunal-4` records that the two drift-audit
  siblings lack it and audit whatever directory the process stands in; this file does not join them.
- **S2** — four stages in fixed order: SPEC, AUDIT, FOLD, BUILD. A unit reaches BUILD only by having
  passed through the three before it in the same program run. This is the unit's whole mechanism and
  it is JS control flow, not a check.
- **S3** — the AUDIT stage delegates to the shipped engine via `workflow('tools/workflows/tier2-review.js', {kind: 'spec-audit', subjects: [...]})`. It does not
  re-implement a review fan, so the trust accounting — the orchestrator-assigned integer id join,
  the dead-lens and dead-skeptic counters, unverified-is-not-refuted — is inherited rather than
  re-lost. `TOOL-dHonouredPark-5` measured what re-implementing costs: 67 findings carrying 18
  distinct ids, and a whole verify stage discarded.
- **S4** — the BUILD stage iterates the units in the ORDER the caller passed, one `agent()` per unit,
  each handed its brief path and its spec path and nothing else. Units sharing an order value are
  dispatched through `boundedParallel` at the cap `agent-cap.js` resolves; different order values are
  strictly sequential.
- **S5** — every stage agent returns a `schema`-validated object. A stage that cannot return one is a
  refusal, not a defaulted pass.
- **S6** — the NEW-FINDING sub-flow: a unit added mid-build re-enters at SPEC and traverses all four
  stages. It is the same code path, reached with a one-element unit list, so a new finding cannot
  reach BUILD by a shorter route.
- **S7** — `tools/workflows/check-workflow-syntax.js` passes, the `agent-cap` hook admits every
  fan-out in the file, and `tools/workflows/check-verifier-fanout.sh` stays green.
- **S8** — an arms test at `tools/workflows/unattended-build.test.sh`, in the shape
  `tier2-review.test.sh` uses: the guard refusals and their PASSING case, and the stage ordering
  asserted over the script's own text.

## 3. Non-goals (OUT)

- **The harness does not drive orientation, preflight, the owner turn, closing, landing or the
  keepalive.** Those are main-loop acts by construction: the scheduling store is in-memory and
  session-scoped, `--preflight` must precede the kickoff hand-back, and `--close` and `--landed` run
  after the harness has returned. This is recorded as a scope cut rather than a limitation, because
  the owner's prompt asks for steps (a) and (f) and they cannot move.
- **The harness performs no enforcement.** A Workflow script has no filesystem, so every observation
  it could make is a claim its own agent returned. The refusal lives in `TOOL-dBriefedPass-3`.
  A stage in this file that claimed to VERIFY the tree would be the could-not-fail shape.
- Recipe mode is out. Its pieces are not specs and its per-piece records already carry its ordering.
- No existing harness is refactored. `tier2-review.js` is CALLED, not changed.

## 4. Design

### Data model

The `args` object, and what each field is for:

| field | shape | why the harness cannot derive it |
|---|---|---|
| `repo` | absolute path | the script has no filesystem and no cwd it may trust |
| `slug` | build slug | names the build folder every agent is pointed at |
| `base` | immutable sha | the review round-1 anchor; a moving ref is refused downstream |
| `units` | ordered array of `{id, order, specPath, briefPath}` | derived by the CALLER from `--plan`, because reading the tree is the caller's capability |
| `briefDir` | repo-relative | where the SPEC stage writes each unit's brief |

`units` arriving pre-ordered is the load-bearing choice: the caller runs `--plan`, which takes its
set and order from the generated units region, so the harness and the driver cannot disagree about
what "next" means.

### Rollout

The harness cannot drive its own creation — units 1 through 4 are built the ordinary way, and this
build's own closing rounds are the first thing it could have driven. That is stated rather than
worked around: a bootstrap that ran the harness over its own unbuilt source would be asserting the
thing under test.

### Alternatives rejected

- **Direct `Agent` spawns instead of a Workflow.** Rejected on a measured constraint, not taste:
  `tools/hooks/README.md` states direct spawns are counted five per USER PROMPT, and an unattended
  run has no next user prompt to reset the count. `BUILD-METHOD.md` M4 already records three specs
  exhausting it mid-set with the remaining lenses refused and nobody to read the refusal. Agents
  inside a Workflow sidechain are not counted against it. The prompt's "(or Agent if workflows are
  not available)" is therefore answered: where Workflow is unavailable the harness does not degrade
  to direct spawns, it degrades to the sequential main-loop build the kit already has.
- **One workflow per stage, orchestrated by the main loop.** Rejected: the ordering would then live
  in the main loop's recollection again, which is the defect. Nesting is one level deep, which S3's
  single `workflow()` call spends and no stage may spend twice.
- **Have the harness read `--plan` itself.** Rejected as impossible rather than undesirable: the
  runtime has no filesystem. Recorded because it is the first thing a reader will propose.

### Files touched (estimate)

`tools/workflows/unattended-build.js` (new), `tools/workflows/unattended-build.test.sh` (new),
`tools/workflows/kit.toml`, `tools/gate-legs.json`.

## 5. Production-readiness checklist

- **Security** — the script spawns agents with the repo's own tools; it adds no external surface. The
  `repo` guard is what stops it operating on a tree nobody briefed it on.
- **Performance · scale** — fan width is the `agent-cap` constant, never a computed value.
- **Error states** — a stage agent returning null is filtered and REPORTED, never silently dropped;
  `TOOL-dTieredTribunal-22` is the live row for the uncounted `filter(Boolean)` predicate and this
  file must not add an instance of it.
- **Observability** — each stage emits a `log()` line naming the unit and the stage, and the BUILD
  stage names any unit it SKIPPED and why. A skip that looks like a pass is the class this repo names.
- **Testing** — S8.
- **Migration · rollback** — the file is new and nothing calls it until `TOOL-dBriefedPass-5` wires
  it. Deleting it is the rollback.

## 6. Acceptance criteria

- **AC1** — `bash tools/workflows/check-workflow-syntax.js` accepts the file, and the `agent-cap`
  hook admits it: every `agent(` fan is over a receiver the hook can prove bounded, and no raw
  `parallel(`/`pipeline(` appears except on a `gov:bounded-fanout` helper line.
- **AC2** — invoked with a prose string instead of an object, the script THROWS naming the missing
  `repo`, and invoked with a valid object it does NOT throw. Both arms, because the first cut of the
  guard this copies refused every legitimate caller.
- **AC3** — the stage order is asserted from the file's own text: the SPEC stage's `await` precedes
  the AUDIT stage's, which precedes FOLD, which precedes BUILD. A reordering reds the arm.
- **AC4** — in `tools/workflows/unattended-build.test.sh`, a unit list carrying two units at order 1 and one at order 2 dispatches the pair together
  and the third strictly after. Asserted on the dispatch sequence the script emits, not on wall clock.
- **AC5** — the AUDIT stage's call names `kind: 'spec-audit'`. Asserted, because `tier2-review.js`
  DEFAULTS an absent kind to `diff-review`, which would review a spec with code-shaped lenses and
  report it as a review — the exact failure M4 exists to prevent.
- **AC6** — in `tools/workflows/unattended-build.test.sh`, a stage agent returning null is counted and named in the run's output. Observed on a
  fixture that forces one, not argued.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `workflow script syntax` · `verifier fan-out` ·
`review-harness gates` · `harness arms` · `agent-cap` hook admission.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · authored under the dBriefedPass mandate.

## 10. Reuse audit

The seam this unit extends is `tools/workflows/tier2-review.js`, cited by path: it is called rather
than copied, and it already carries the subject descriptor `TOOL-dTieredTribunal-11` landed, so a
spec audit is a supported `kind` on the shipped engine rather than something this harness must
build. `python tools/codebase-map/reuse_lookup.py "drive a build's passes through an orchestrated
workflow harness in a fixed order"` returned `agent-cap.topLevelArgs` as the affordance seam
bounding any fan-out, and `check-workflow-syntax.js` as the existing validator for this file class;
both are honoured rather than re-implemented. The `boundedParallel` helper is inlined from that same
engine because workflow scripts cannot import, which is the documented reason the duplication is
sanctioned here and nowhere else.

Recall terms used: unattended mandate pass ordering workflow harness spec before code regrounding
compaction driver orchestration agent-cap fan-out build-method handoff prompt.
