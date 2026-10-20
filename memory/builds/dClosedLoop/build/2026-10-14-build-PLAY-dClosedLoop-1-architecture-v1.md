# Architecture v1 — the closed loop after four design rounds: configurable by default, local-first, chained as a DAG

**Serves:** research PLAY-dClosedLoop-1

The converged design after the owner's rounds 1 to 4
(`build/2026-10-14-build-PLAY-dClosedLoop-1-design-rounds.md`), written over v0
(`build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v0.md`), which stays unedited. This is
the input the spec writer turns into `PLAY-dClosedLoop-1`. Items marked PROPOSED await the owner's
round 5.

## What the rounds changed in v0

| v0 | v1 | Round |
|---|---|---|
| P3: the binding verdict lives off the actor's node | the verdict is a per-repo policy; the LOCAL HOOK is the default and the first-built path, because remote CI is not available; a remote verifier is an optional backend | R1.3, R4.4 |
| review risk-tiered, on by default | agent review opt-in by default, except the closing review at Build, owed by default; every stage's review switchable, with its effort | R2.1 |
| — | a stage-exit review recommendation, emitted by the agent before every transition, advice by default, switchable to binding | R2.1, R4.3 |
| leases refuse | leases warn by default, switchable to refuse | R2.2 |
| Maintain reports | Maintain applies a declared set of safe fixes under its own mandate | R2.3 |
| deploy contract only | deploy contract plus a shipped deploy engine and adapters, the first adapter fitted to incms | R1.2, R3.1 |
| — | autonomy level per repo: plan-only, three-gates (default), every-stage | R1.4 |
| — | plan authority per repo: planner-drafts/owner-ratifies (default), planner-within-themes, owner-orders | R2.4 |
| — | P10: every policy has a default and is owner-switchable per repo, per stage and per effort where it matters; one policy file; the policy guard is itself a policy | R2.4, R4.1, R4.2 |

## Principles

- **P1. One loop, declared once.** A machine-readable loop definition holds the stages, their
  contracts, roles, harnesses, witnesses, review keys and the policy schema with its defaults. It
  grows from `tools/roles/workflows.toml`. Every shipped part declares the stage it serves, and a
  coverage gate reds a part that serves none and a stage that has no witness.
- **P2. A hand-off is witnessed.** Each stage exit is computed from committed history, a
  hook-written record or a remote verdict. A witness that reads actor-typed state (a self-set
  status, an agent-written route) is refused by the loop definition's own check.
- **P3. Local-first verdict, pluggable backend.** The binding verdict runs in the local hook by
  default. A peer-node verifier (PROPOSED) and a remote CI verifier are declared backends a repo may
  switch to. Every node reads one verdict per tree from a hook-written record.
- **P4. One contract, two authorizations.** Attended and unattended work run the same stage
  contracts; the autonomy level and the mode decide only who authorizes a transition.
- **P5. Concurrency by lease.** Builds and units hold remote leases with the fleet tag, a heartbeat
  and an expiry, in both modes; overlap warns by default and refuses by policy; a design index
  makes overlap between live specs visible.
- **P6. Maintain feeds Plan and fixes what is safe.** Maintain runs on a cadence under a maintenance
  mandate, applies the declared safe fixes, and files every other finding as an ask Plan must place
  or dispose.
- **P7. Review where it pays, recommended everywhere.** Each stage has a review whose default and
  effort are policies; every transition carries the agent's recorded recommendation; the Loop Review
  reads the loop's metrics and proposes contract changes, including retirement.
- **P8. The product is the loop.** The loop definition, the policy schema and the stage kits ship;
  gov's repository is adopter zero with a thin overlay; adopters receive every stage's contract.
- **P9. Weight is budgeted and pruned.** A value ledger records what each gate, rule and bug class
  catches and costs; the Loop Review retires what catches nothing in a declared window; budgets cap
  legs, guide bytes and registry rows; records overhead is a metric with a ceiling.
- **P10. Flexible and configurable, inside a floor.** Every policy has a sensible default, lives in
  ONE per-repo policy file, is read through one reader and is rendered into the charter. A safety
  floor (PROPOSED) holds regardless of policy.

## The policy catalogue

| Policy | Values | Default | Scope | Round |
|---|---|---|---|---|
| `autonomy` | plan-only, three-gates, every-stage | three-gates: the owner ratifies the plan, gives each design its go, authorizes landing | repo | R1.4 |
| `verdict` | local-hook, peer-node (PROPOSED), remote-ci | local-hook | repo; declared at deployment or switched later | R1.3, R4.4 |
| `review.<stage>` | off, opt-in, owed, owed-above-tier | opt-in at every stage; owed at Build (the closing review) | repo × stage | R2.1 |
| `review.<stage>.effort` | the role efforts | the role's declared effort | repo × stage | R2.1 |
| `review.recommendation` | advice, binding, binding-above-tier | advice | repo | R4.3 |
| `leases` | warn, refuse | warn | repo | R2.2 |
| `maintain.fixes` | a set of named safe fixes | reap stale processes, prune landed branches and worktrees, regenerate stale outputs, close builds dormant past a threshold, land records-only fixes | repo | R2.3 |
| `maintain.cadence` | a schedule | a declared default the Maintain build sets | repo | R2.3 |
| `plan.authority` | planner-drafts-owner-ratifies, planner-within-themes, owner-orders | planner-drafts-owner-ratifies | repo | R2.4 |
| `policy.guard` | owner-only, agents-with-reason, agents-within-mandate | owner-only, gate-checked | repo | R4.2 |
| `budgets` | caps on legs, guide bytes, registry rows; the records-overhead ceiling; the retirement window | set by the Review build from measurement | repo | R3.2 |

Kit mechanics, such as cutoffs, paths and thresholds that are not owner choices, stay in each kit's
own conf; the policy file holds only the owner's switches.

## The safety floor (PROPOSED for round 5)

Invariants no policy value can switch off, because without them a repository is not governed:

1. A binding verdict runs before the default branch moves. Which backend runs it is a policy;
   whether one runs is not.
2. Every policy change and every stage transition is recorded: who, when, why, and the witness.
3. The policy guard protects its own switch: loosening it needs the current guard's authorization.
4. No stage witness reads actor-typed state.
5. The hooks cannot be bypassed from an agent's tools: no `--no-verify`, no hooks-path override, no
   agent write to a hook, the policy file or a verdict ref outside the guard.

## Local-first witnesses

Remote CI is unavailable, so the local verdict has to be trustworthy on its own:

- **Harness refusals** (`tools/hooks/scratch-guard.js`, a PreToolUse hook on Bash and PowerShell):
  refuse `--no-verify`, `core.hooksPath` overrides and agent writes under `refs/gov/`.
- **Owner-only paths**: the policy file, `.githooks/`, the hook scripts and `.claude/settings.json`
  are written only under the policy guard, and a commit touching them carries the guard's
  authorization, which a gate checks.
- **Hook-written verdicts**: pre-push writes the verdict for the tree it graded, keyed by tree hash
  and readable by every node; nothing else writes it.
- **History legs at push**: the Build exit (scope, closing review recorded, pass order) is
  re-derived from committed history inside the bar.
- **Peer verification (PROPOSED)**: a fleet node other than the pusher re-runs the bar for the
  pushed tree, giving a multi-node fleet an independent verifier without cloud CI.

## Stage contracts

| Stage | Takes in | Roles | Hands out | Witness | Owner gate (three-gates) | Review default |
|---|---|---|---|---|---|---|
| Plan | an owner prompt, an ask, a Maintain finding, a Loop Review proposal | planner and triager (new), orienter | a build opened and placed in the ordered plan, with dependencies and a lease | every live build and open BLOCKER or HIGH ask placed or disposed; the ratification record | plan ratification | opt-in Plan Review |
| Design | a planned, leased build and its brief | reuse scout, researcher, spec writer; spec reviewer, skeptic, synthesizer | a spec set at a named revision, forks resolved, overlaps acknowledged | derived design state READY, never FORKED; the design index; an audit record where owed | the design go | opt-in spec audit |
| Build | a unit with its design witness and lease | one builder per unit, each in its own worktree | in-scope commits, owed arms observed, a closing review over the range | history legs in the bar: scope at kit granularity, closing review recorded, pass order | none | closing review owed |
| Test | a built range | the bar (program); a gate reviewer where owed | a hook-written verdict for the tree; seen-red, flake and product-test records | the verdict from the declared backend | none | opt-in gate review |
| Deploy | a verified tree | the lander; the deploy engine and its adapter; govkit | a landed SHA; release notes; per-SHA deploy and verify verdicts; adopter currency | verdict records from the lander and the deploy engine; the currency probe | landing authorization (or a mandate) | opt-in landing and release review |
| Maintain | a cadence tick or an event | maintainer under the maintenance mandate; triager | safe fixes applied; asks with severity and acceptance; a maintenance record; loop metrics | every detector pinned and owned; every fix inside the declared set | none | the Loop Review, periodic |

Every transition writes a transition record: build, unit, from-stage, to-stage, witness, the
agent's review recommendation with its reason, and the authorization (owner turn or mandate).

## The chain: ten builds as a DAG

```text
dClosedLoop ── dDeclaredLoop (Spine) ─┬─ dLeasedFleet (Concurrency) ──┬─ dRankedPlan (Plan) ───────┐
                                      │                               └───────────┐                │
                                      ├─ dWitnessedBar (Test) ────┬───────────────┼─ dScopedBuild (Build)
                                      │                           ├─ dShippedRelease (Deploy)      │
                                      │                           └─ dTendedCadence (Maintain) ◄───┘
                                      └─ dIndexedDesign (Design) ──── dScopedBuild               │
                                                                      dCalibratedLens (Review) ◄─┘
                                      all of the above ──► dConvergedCharter (Convergence)
```

| Build | Stage | Parents | Planned units | Gaps owned |
|---|---|---|---|---|
| dDeclaredLoop | Spine | dClosedLoop | the loop definition grown from `tools/roles/workflows.toml`; the policy file, its schema, defaults, one reader and the guard; the safety floor; the transition record; stage claims on every part and the coverage gate; the witness-class rule; the rendered charter loop section | gap-spine-01, gap-spine-02, gap-spine-06, gap-design-01 |
| dLeasedFleet | Concurrency | dDeclaredLoop | the lease ref grammar with the fleet tag, heartbeat and expiry, generalising run claims; acquisition at route and dispatch in both modes; warn or refuse on overlap, takeover on expiry; slug uniqueness against the remote | gap-conc-01, gap-conc-02 |
| dWitnessedBar | Test | dDeclaredLoop | harness bypass refusals; the hook-written verdict per tree; held self-tests on the pre-landing path by change selection inside a budget; the seen-red recorder; flake records and quarantine; the adopter product-test contract; peer-node and remote-CI backends; a derived pre-commit list and multi-node cost evidence | gap-test-01 to gap-test-09 |
| dRankedPlan | Plan | dDeclaredLoop, dLeasedFleet | the plan record and its ratification; the planner and triager role and the Plan workflow; the placement predicate; the triage drain; Plan Review; the live-build mapping carried out; attended briefs gated | gap-plan-01 to gap-plan-07 |
| dIndexedDesign | Design | dDeclaredLoop | the derived design state as the hand-off witness; the design index across builds; design review policy and effort; reuse-truth and alternatives checks; the research harness and binding; sub-spec and tier checks | gap-design-02 to gap-design-07, gap-design-09 |
| dScopedBuild | Build | dIndexedDesign, dLeasedFleet, dWitnessedBar | one exit contract for both modes with a history-derived base; scope attribution at kit granularity; the closing review recorded per build; a worktree per unit; the shell-write and checklist gaps | gap-spine-03, gap-conc-03, gap-build-01 to gap-build-04 |
| dShippedRelease | Deploy | dWitnessedBar | the deploy engine (environments, promotion, signed releases, verify, rollback, canary and fleet-roll steps); the first adapter, fitted to incms; per-SHA deploy and verify verdicts; the fleet register, currency watch and outbox grading; release notes and landing review; lander hardening; emitted CI as an optional backend; a runbook derived from descriptors | gap-deploy-01 to gap-deploy-08 |
| dTendedCadence | Maintain | dWitnessedBar, dRankedPlan | the maintenance recipe on a cadence and its mandate; the declared safe-fix set; bound detectors; run-record and dormant-build closure; map freshness | gap-maint-01, gap-maint-02, gap-maint-05 to gap-maint-08 |
| dCalibratedLens | Review | dTendedCadence | review policy and effort per stage; the stage-exit recommendation line; lens sets for Plan, Test, Deploy and Maintain; the value ledger; the Loop Review with retirement, budgets and the records-overhead ceiling; review cost controls | gap-review-01 to gap-review-03, gap-maint-03, gap-design-08 |
| dConvergedCharter | Convergence | dScopedBuild, dShippedRelease, dCalibratedLens | the charter regrouped by stage with rendered policy values and gov's overlay split out; guides and runbook consolidated and derived inside budget; record kinds consolidated; superseded legs, rules and builds retired; adopters migrated through govkit | gap-spine-04, gap-spine-05, gap-maint-04 |

`gap-spine-06` is new, from round 4's measurement: per-repo configuration is spread over at least
eight surfaces holding about 160 keys, with no single answer to "what is this repo's policy".

## The live builds, mapped (a recommendation the Plan build carries out)

The owner named four builds that finish on their own track (R3.3): aOrientedCast, aRoutedQuill,
dPinnedHandoff, dPolishedVitrine. On 2026-10-14 `memory/LIVE.md` re-labelled dPolishedVitrine
dormant (its last record is 2026-09-22); the Plan build confirms its track with the owner.

| Live build | Status, activity | Subject | Absorbing chain build |
|---|---|---|---|
| aOrientedCast | OPEN, active | every agent is handed a rendered role | dDeclaredLoop, after it closes |
| aRoutedQuill | DEFERRED, active | every code build is routed through orientation, a brief and a specced unit | dScopedBuild, after it closes |
| dPinnedHandoff | SPECCED, active | NicoCares handoff habits as spec shapes | dIndexedDesign, after it closes |
| dPolishedVitrine | INPROGRESS, dormant since 2026-10-14 | the build harness rendered at install | dShippedRelease, after it closes |
| aBatchedLintel | INPROGRESS, dormant | hygiene checks collapsed to one awk each | dWitnessedBar |
| aDeclaredBound | OPEN, dormant | hardcoded thresholds become declarations | dDeclaredLoop |
| aDeployScout | SPECCED, dormant | the govkit deployer research | dShippedRelease |
| aFerriedDossier | OPEN, dormant | an adopter's dossier carried in from inCMS | dShippedRelease |
| aGradedDoorway | INPROGRESS, dormant | an adopter kit at a non-default prefix | dShippedRelease |
| aMendedLedger | SPECCED, dormant | finish the memory rework | dConvergedCharter |
| aPacedTurnstile | SPECCED, dormant | the merge bar's execution discipline | dWitnessedBar |
| aPortableWarden | SPECCED, dormant | the worktree-guards kit | dScopedBuild |
| aQuarriedLantern | INPROGRESS, dormant | memory-recall kit 1.0 | dIndexedDesign |
| aTetheredScratch | INPROGRESS, dormant | agent scratch out of the operator's home | dScopedBuild |
| aTunedCompass | BLOCKED, dormant | the orientation chain, measured | dRankedPlan |
| aWalkedCorpus | DEFERRED, dormant | one walk over the corpus, graded | dTendedCadence |
| aWeighedCanon | OPEN, dormant | is the spec format earning what it costs | dCalibratedLens |
| bConvergentLodestar | SPECCED, dormant | the reuse-convergence layer for the map | dIndexedDesign |
| dLandedVerdict | INPROGRESS, dormant | a spec that landed and never said so | dTendedCadence |
| dNarrowedAnchor | INPROGRESS, dormant | the second anchor per mode | dScopedBuild |
| dPromptedSeam | DEFERRED, dormant | a refused name answers "does this exist" | dIndexedDesign |
| dRetiredFork | DEFERRED, dormant | gov stops generating forks and takes back adopter fixes | dShippedRelease |
| dScaffoldedMirror | DEFERRED, dormant | the lexicon stops deriving its standard from what it grades | dIndexedDesign |
| dScriptedRepeat | SPECCED, dormant | playbook mode for repeatable content | dTendedCadence |
