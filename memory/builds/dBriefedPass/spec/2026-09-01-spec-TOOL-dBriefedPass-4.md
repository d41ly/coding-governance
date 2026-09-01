# TOOL-dBriefedPass-4 — the harness: one Workflow script driving spec, audit, fold and build in order

**Status:** CLOSED · rev-5 · 2026-09-01 · node d · Tier-2 · base 269dacae · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-build-TOOL-dBriefedPass-4-1-harness.md](../build/2026-09-01-build-TOOL-dBriefedPass-4-1-harness.md) | journal | — |
| [2026-09-01-prompt-TOOL-dBriefedPass-1.md](../prompts/2026-09-01-prompt-TOOL-dBriefedPass-1.md) | research | TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-5 |
| [2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round1.md](../reviews/2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round1.md) | spec-audit | TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-5 |
| [2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round2.md](../reviews/2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round2.md) | spec-audit | TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-5 |
| [2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round3.md](../reviews/2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round3.md) | spec-audit | TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-5 |

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
- **S2** — three sequential stages: SPEC, AUDIT, BUILD. A unit reaches BUILD only by having passed
  through SPEC and an AUDIT in the same program run, and only when that audit's verdict is TERMINAL.
  This is the unit's whole mechanism and it is JS control flow, not a check.
- **S2b** — the harness runs ONE audit round and GATES on its verdict: `CONVERGING` returns early
  without reaching BUILD, and only `CONVERGED`, `NON-CONVERGENT` or `CEILING` admit it. The LOOP
  lives in the caller, which folds and re-invokes; the harness holds the GATE, which is the half that
  has to be structural. It is not a loop here because it cannot be — `agent-cap.js` denies an
  `agent()` in any loop body, and a convergence loop's iteration count is data-dependent by
  definition, so no bounded unroll exists. The owner's 2026-09-01 ruling is preserved in the half
  that matters: the `--review` VERDICT is what decides whether BUILD is reachable, and no round cap
  is introduced anywhere. The CHANNEL that token arrives on is declared rather than assumed: the AUDIT stage's own agent runs
  `bash tools/unattended/unattended.sh --review <slug> --subject <subject> --verdict <v>
  --blockers <n>` and returns the driver's answer in its schema, so the harness reads a field of a
  stage return it already awaits. No callback and no new `args` field: a Workflow script has no
  filesystem and cannot run that command itself, and an undeclared callback would be an input this
  spec names nowhere. The blocker count it passes comes from the same `workflow()` return the AUDIT
  stage already receives. The site that yields an INTEGER `blockers` is `tier2-review.js:608`, the
synthesis return; `:373`, `:383` and `:476` are DEGRADED-PATH returns that yield `blockers: null` by
design, and the file says so — null, never 0, so a stated absence cannot be read as a clean bill.
That distinction is load-bearing here rather than pedantic: `unattended.sh:3821` refuses a
non-integer `--blockers`, and `:3768` emits `CONVERGED` only on a count of 0, so routing the loop
through a null-yielding site makes the CONVERGED exit unreachable and every audit look degraded. The
AUDIT stage therefore reads the synthesis return, and a null `blockers` is a REFUSAL that surfaces
the degraded run rather than a number it invents. After each
  round the harness reads that verdict token; `CONVERGING` re-enters AUDIT, and `CONVERGED`, `NON-CONVERGENT` and `CEILING` all exit
  to BUILD. On the two non-clean exits every standing blocker is PROMOTED to a unit through S6's
  sub-flow rather than carried into BUILD, which is what `BUILD-METHOD.md` M4 requires at the exit.
  The harness holds NO round cap of its own: the owner ruled on 2026-09-01 that convergence stays
  uncapped precisely because the harness obeys this verdict, so a cap here would quietly re-take a
  decision that was made against it.
- **S3** — the AUDIT stage delegates to the shipped engine via `workflow('tools/workflows/tier2-review.js', {kind: 'spec-audit', subjects: [...]})`. It does not
  re-implement a review fan, so the trust accounting — the orchestrator-assigned integer id join,
  the dead-lens and dead-skeptic counters, unverified-is-not-refuted — is inherited rather than
  re-lost. `TOOL-dHonouredPark-5` measured what re-implementing costs: 67 findings carrying 18
  distinct ids, and a whole verify stage discarded.
- **S4** — the BUILD stage is ONE agent, handed the units in the ORDER the caller passed and told to
  take them one at a time, each from its brief path and its spec path and nothing else. One agent per
  unit was specified through rev-4 and is not buildable: `tools/hooks/agent-cap.js` denies any
  `agent()` inside a loop body unconditionally and names no marker that admits one, so the only
  shapes it permits are a bounded PARALLEL fan — which `TOOL-cBriefedPilot-21` forbids — and a single
  call. What the harness keeps is the property the owner's prompt is actually about: the STAGE order
  stays structural, so BUILD is unreachable except through SPEC and AUDIT. Per-unit order moves to
  `TOOL-dBriefedPass-3`'s `--dispatch` refusal, which is a machine check over the tree and is
  therefore stronger than JS control flow, not weaker. Dispatch is STRICTLY SEQUENTIAL,
  including within a shared order value: `TOOL-cBriefedPilot-21`'s ratified verdict is
  `parallelism route: none`, and the Workflow-sidechain route this harness would otherwise take is
  that hunt's R2, which cleared E1 and E2 and FAILED E3 and E4. A shared order value therefore
  declares that two units MAY run together and this harness still runs them one at a time; the
  declaration is what a later run re-uses if the route is ever re-opened.
- **S5** — every stage agent returns a `schema`-validated object. A stage that cannot return one is a
  refusal, not a defaulted pass. The AUDIT stage's schema REQUIRES a `verdict` field over the
  driver's four-state closed set, so an audit returning no verdict is a refusal rather than a silent
  absence that would otherwise read as CONVERGED — which is the one absence that would let this
  harness build on an unreviewed spec set.
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
- **Concurrent build-pass dispatch through the sidechain.** Rejected on a RATIFIED verdict rather
  than on judgement. `TOOL-cBriefedPilot-21` recorded `parallelism route: none`, with the evidence at
  `memory/builds/cBriefedPilot/build/2026-08-15-build-TOOL-cBriefedPilot-15-2-parallelism-routes.md`;
  the verdict token is line 5 of that record. This harness is that hunt's route R2, and R2 failed E3
  and E4 — E4 being that each pass can commit at its own end without the two commits racing one
  index. The same record names R5, one git worktree per concurrent pass, as the checkout shape any
  surviving route would need, and R5 is out of scope here. `TOOL-cBriefedPilot-28` is OPEN at
  `memory/backlog/TOOL.md:131` and names exactly what would re-open it: "R2+R5 needs E3 and E4 RUN
  (they never were)". Shipping R2 without R5 into one worktree with one index is also this repo's own
  recorded `shared primary tree, shared index` trap. Running E3 and E4 is a build of its own, and
  this unit does not pretend to have run them.
- **Have the harness read `--plan` itself.** Rejected as impossible rather than undesirable: the
  runtime has no filesystem. Recorded because it is the first thing a reader will propose.

### Files touched (estimate)

`tools/workflows/unattended-build.js` (new), `tools/workflows/unattended-build.test.sh` (new),
`tools/workflows/kit.toml`, `tools/gate-legs.json`, and the CODEBASE-MAP carriers the new file
obliges: a `workflow-scripts` claim in `memory/map/features/`'s relevant dossier plus the
regenerated `memory/map/generated/MAP.md` and `inventories.json`. A new workflow script is a new
inventory key against a baseline that holds none, and `codebase-map coverage + freshness` is
`chunk: declarations`, `subject: repo`, NO guard — so it runs on every bar and reports the key
UNCLAIMED from the creating commit onward. This unit does NOT add a `gate_leg` block: it ships no
merge-bar leg of its own, and `tools/gate-legs.json` appears here only because the harness's test
file is registered like its siblings.

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

- **AC1** — `node tools/workflows/check-workflow-syntax.js tools/workflows/unattended-build.js`
  exits 0, matching the `argv` that `tools/workflows/kit.toml:59` and the `gate-legs.json` row both
  declare; the file's own shebang is `#!/usr/bin/env node` and invoking it through `bash` exits 2.
  And the `agent-cap` hook admits the harness: every `agent(` fan is over a receiver the hook can prove bounded, and no raw
  `parallel(`/`pipeline(` appears except on a `gov:bounded-fanout` helper line.
- **AC2** — invoked with a prose string instead of an object, the script THROWS naming the missing
  `repo`, and invoked with a valid object it does NOT throw. Both arms, because the first cut of the
  guard this copies refused every legitimate caller.
- **AC3** — the stage order is asserted from the file's own text: the SPEC stage's `await` precedes
  the AUDIT stage's, which precedes FOLD, which precedes BUILD. A reordering reds the arm.
- **AC4** — in `tools/workflows/unattended-build.test.sh`, the file contains NO `agent(` call inside
  any loop body and no `parallel(`/`pipeline(` call at all, asserted over the script's own text, and
  `node tools/hooks/agent-cap.js` ADMITS it when handed a Workflow call naming this script. Two arms:
  the textual absence, and the hook's own verdict. At rev-1 this criterion asserted a concurrent
  dispatch that a ratified decision forbids; at rev-4 it asserted a sequential loop the hook denies.
- **AC7** — in `tools/workflows/unattended-build.test.sh`, an AUDIT stage returning `CONVERGING`
  returns WITHOUT reaching BUILD, and `CONVERGED`, `NON-CONVERGENT` and `CEILING` each admit it. Four
  arms over the driver's four states, because a gate tested only on the state that opens it is a gate
  nothing proved closes.
- **AC8** — in `tools/workflows/unattended-build.test.sh`, the harness reports the number of AUDIT
  rounds it ran and an arm asserts that count is at least 1 on a run that reached BUILD. Without it a harness whose verdict channel is broken runs
  zero rounds and reads as convergence on the first pass, which is the reassuring-zero shape this
  repo refuses in its probes one layer down.
- **AC9** — an AUDIT stage return carrying NO `verdict` field is REFUSED by S5's schema, asserted as
  a refusal and not merely as a non-CONVERGED path. An AUDIT stage whose `blockers` is `null` is
  likewise a refusal naming the degraded run, not a count.
- **AC10** — `python3 tools/codebase-map/test_codebase_map.py` is GREEN with the new script present,
  which is the criterion for the dossier claim and the regenerated artifacts §4 names. Observed RED
  first: an unclaimed new key reports `UNCLAIMED (new key? claim it in a feature dossier ...)`.
- **AC5** — the AUDIT stage's call names `kind: 'spec-audit'`. Asserted, because `tier2-review.js`
  DEFAULTS an absent kind to `diff-review`, which would review a spec with code-shaped lenses and
  report it as a review — the exact failure M4 exists to prevent.
- **AC6** — in `tools/workflows/unattended-build.test.sh`, a stage agent returning null is counted and named in the run's output. Observed on a
  fixture that forces one, not argued.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `workflow script syntax` · `verifier fan-out` ·
`harness arms (fail branches armed or pinned)` · `review-join ban (no ref-keyed join)` ·
`codebase-map coverage + freshness` ·
the `agent-cap` hook's admission of this file. Every leg name resolves against
`tools/gate-legs.json`; `review-harness gates` was listed at rev-2 and resolves to nothing.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · authored under the dBriefedPass mandate.
- rev-2 · 2026-09-01 · round-1 spec-audit fold. B4 (finding 49): S4 shipped concurrent dispatch,
  which is `TOOL-cBriefedPilot-21`'s route R2 against a ratified `parallelism route: none` and an
  open re-opening row naming the two experiments nobody has run; dispatch becomes strictly
  sequential, AC4 is inverted to assert that, and Alternatives rejected now carries the citation the
  document lacked entirely. B5 (finding 55): the README records an owner ruling from this run's one
  turn — the harness calls `--review` and obeys its verdict — that no unit implemented, and spec 4
  contained zero occurrences of `--review`; S2 becomes three stages plus a converging pair, S2b
  states the loop and its four exits, and AC7 observes all four. L1 (finding 29): AC1 invoked a
  node file through bash, which exits 2 against the declared argv.
- rev-5 · 2026-09-01 · found by BUILDING it, M2's route for a divergence: spec first, then code.
  S4's one-agent-per-unit loop is not buildable — `tools/hooks/agent-cap.js:95-112` denies any
  `agent()` in a loop body, its whitelist is closed, and it names no marker for the case. Measured by
  running the hook's own predicate over the file: it denied both loop sites, calling a strictly
  sequential `await agent(...)` "a loop-built thunk array". The conflict is exact and is PARKED for
  the owner: bounded-parallel is permitted by the hook and forbidden by `parallelism route: none`,
  sequential is required by that verdict and forbidden by the hook. S4 becomes one agent per STAGE
  holding the ordered unit list, which keeps the stage order structural and moves per-unit order onto
  `--dispatch`'s refusal. THE SAME DENIAL REACHES S2b, the second and larger consequence: the
  AUDIT/FOLD convergence loop also spawns an agent inside a loop body, and unlike the per-unit case
  it cannot be unrolled, because a convergence loop's iteration count is data-dependent by
  definition. So the LOOP moves to the caller and the harness keeps the GATE — `CONVERGING` returns
  early and never reaches BUILD. AC4 and AC7 are restated as arms over the new shape.
- rev-3 · 2026-09-01 · round-2 spec-audit fold. H1 and H2 (findings 14 and 6, one defect from two
  axes): the rev-2 convergence loop keyed on a "caller-supplied review callback" that the §4 args
  table never declared and no other section named, so the loop's only input came from nowhere — S2b
  now routes the verdict through the AUDIT stage's own agent and its schema return, S5 makes that
  field required so an absent verdict refuses instead of reading as CONVERGED, and AC8 asserts the
  round count is non-zero. Round 1's B5 fix created the loop and did not say where its input came
  from. Also the §7 leg-name correction, one name that resolves to nothing.
- rev-4 · 2026-09-01 · round-3 spec-audit fold, at the NON-CONVERGENT exit; both blockers here are
  document defects and FOLD rather than promote. B2 (finding 8): the rev-3 fix named
  `tier2-review.js:383` as the blocker-count channel, and that is a degraded-path return yielding
  `blockers: null` BY DESIGN — the integer path is `:608`. Since `unattended.sh:3768` emits
  `CONVERGED` only on 0 and `:3821` refuses a non-integer, a CLEAN audit could not have reached the
  CONVERGED exit at all. Round 2's fix named a line; it named the wrong one, which is the citation
  class round 2 itself proposed a gate for. B3 (finding 21): `tools/workflows/unattended-build.js`
  is a new `workflow-scripts` inventory key against an empty baseline, claimed by no dossier, and
  the map leg is unguarded — the same landing-without-its-carrier mechanism as spec 3's B1, in a
  different declaration system. H5 (finding 21's sibling): §4 named the descriptor pair a new LEG
  needs while this unit declares none, which is now said explicitly.

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
