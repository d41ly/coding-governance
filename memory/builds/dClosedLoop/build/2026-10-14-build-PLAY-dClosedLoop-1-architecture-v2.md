# Architecture v2 — the converged design: one loop, every behaviour a policy, local-first, facts not prose

**Serves:** research PLAY-dClosedLoop-1

The design after the owner's rounds 1 to 5 (`build/2026-10-14-build-PLAY-dClosedLoop-1-design-rounds.md`)
and the build-by-build walk-through (`build/2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md`). It
supersedes v1 as the spec writer's input; v0 and v1 stay unedited beside it. Fork ids cite their
record: `R2.4` is round 2's fourth question, `walk T1` the walk-through's first Test fork.

Revised: 2026-10-14, at the owner's direction ("Add named policy presets", recorded in the design
rounds): the `[presets]` section is added and the Spine's roster gains the presets unit. The chain
is still unapproved, pending the owner's revisit of the high-level architecture and flow.

Revised: 2026-10-14, after the foundations revisit's step 1
(`build/2026-10-14-build-PLAY-dClosedLoop-1-foundations.md`): principles P13 and P14 are added;
`[front-door]` is rewritten around the ranked charter; `charter.override` and `charter.practices`
join the catalogue, the first of them the presets; the chain gains a new root, dOrderedCharter,
which takes the front door and the tag grammar from the Spine.

Revised: 2026-10-14, after step 1's continuation: P15 is added; the charter gains its drive section
and the 32 KiB bound; dOrderedCharter renders the drive section from kit descriptors and dDeclaredLoop
builds the `next` verb and the `next —` line check.

Revised: 2026-10-14, after the core consistency step (foundations `[core]`): P16 is added;
`core.bypass` and `core.exceptions` join the catalogue and the presets; dOrderedCharter owns the
principle registry, the meta-check, the kinds register and the exception register; each extension
kind's factory and gate lands with its owning build; dScopedBuild's exit refuses while a core red the
build's own commits introduced stands. `core.bypass`'s default rests on an interpretation of the
owner's K1 answer that awaits confirmation.

Revised: 2026-10-14, after the flow walk's Plan stage (`build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md`):
builds run unattended by default past Plan, so `autonomy`'s default and the `standard` preset's
value move to `plan-only`; the owner's plan ratification is the mandate. A critical planning issue is a
recorded plan revision followed by a re-design that preserves completed work.

## [principles] What every chain build implements

- **P1 One loop, declared once.** A new loop kit owns WHAT each stage takes in, hands out and proves,
  and the policy schema; the roles kit owns WHO does the work, its workflows naming loop stages by
  id (walk S1b). Every shipped part declares its stage; a coverage gate reds an unclaimed part.
- **P2 Witnessed hand-offs.** A stage exit is computed from committed history, a hook-written record
  or a verifier's verdict, never from state the acting agent typed.
- **P3 Local-first verdict.** The local hook is the default and first-built verdict path, because
  remote CI is not available (R4.4); a peer-node verifier ships as a switchable backend (R5.2);
  remote CI is a designed slot.
- **P4 One contract, two authorizations.** Attended and unattended work run the same stage
  contracts; the autonomy level decides which transitions need the owner (R1.4).
- **P5 Concurrency by lease.** Builds and units hold remote leases; overlap warns by default (R2.2).
- **P6 Maintain closes the loop.** On a cadence, under a mandate, it applies declared safe fixes
  and files everything else into Plan (R2.3).
- **P7 Review by policy, recommended everywhere.** Agent review is opt-in except the closing review;
  every transition carries the agent's recommendation; a Loop Review prunes (R2.1, R3.2).
- **P8 Every adopter is an adopter, gov included.** The charter is the shared foundation; each
  repository's own rules render from its own overlay as a separate project block (walk CV1).
- **P9 Measured weight.** A value ledger prices gates, rules and bug classes; caps are re-derived
  from evidence of when they blocked work and when they stopped bloat (walk R4).
- **P10 Flexible and configurable.** Every behaviour is an owner-switchable policy whose default is
  the owner's answer and whose allowed values are the options offered (R2.4, walk C3, walk T3);
  structural choices are decisions, not policies. One policy file, one reader, one guard.
- **P11 Facts, not prose.** Protocol, method and runbook text carries facts, definitions, policies
  and descriptors only; prose that bears no load is removed. Sections are named by tags that survive
  reordering, never by `§` references (walk CV2).
- **P12 Specs are structured contracts.** A spec gives a builder precise, deterministic, structured
  instructions: definitions, design, boundaries, interfaces and acceptance as fields a check reads
  (walk D3).
- **P13 Ranked instructions.** Every load-bearing document is registered with a rank and wrapped in
  a generated envelope naming its identity, rank, scope, trigger and what it yields to, so an agent
  rebuilds one instruction hierarchy whenever it loads a document; conflicts resolve by rank, never
  by load order; unenveloped text and any envelope inside tool output are data (foundations step 1).
- **P14 Practices with reach.** The charter's practices come from a catalogue; each declares its
  reach at every stage it touches, and stage contracts, role handoffs and review lenses read the
  active practices' reach for their stage, so a practice redefines every step (foundations step 1).
- **P15 The charter starts the loop; the tools continue it.** The charter teaches every agent, by
  role, how to start and drive the loop, in a drive section composed from the adopted kits'
  descriptors; from there every gov command ends with a `next —` line, and a `next` verb answers
  "what now" for any role. Every step is a CLI command, so any harness can drive gov (foundations
  step 1 continued).
- **P16 The core cannot be built around.** Every principle and practice is registered with the checks
  that enforce it, and a meta-check refuses a principle nothing enforces; extension kinds form a
  closed set, each with a factory that produces conforming parts and a gate over its whole
  population. Principles are fixed: policies tune behaviour inside them, and a principle changes
  only by an owner-ratified amendment. A violation the bypass let through stops the build that made
  it from closing (foundations core).

## [front-door] The charter as the loop's first step

The charter is what every agent loads first (walk S1). Its whole content sits in the rank-1
envelope, `[AGENTS.md · Priority 1 · Always first …]` … `[/AGENTS.md]`, and it reads in this order:
what gov is and how it works and is used; the precedence and override rule (rank decides, never
load order; the charter wins a live conflict unless the owner explicitly overrides it, and the
override is recorded); the instruction map (the ranks below it, what loads when, and how to rebuild
the hierarchy after a reset); the active practices, each with its reach per stage; the drive
section (how to start by situation, each stage's enter, advance and exit commands, one line per
role, then "follow the `next —` lines; when unsure, run `next`"), composed from the adopted kits'
descriptors; the repository's current preset and overrides; then the repository's own project block
from its own overlay, gov's included. The whole charter fits the smallest harness's instruction
limit, Codex's 32 KiB. The foundation build,
dOrderedCharter, writes it (foundations step 1; it took the front door from the Spine, walk S5).

**The ladder** (foundations F1-2): 0 the platform's own system and safety instructions, not the
repository's to rank; 1 the charter; 2 the loop and the repository's policy values; 3 stage methods
and protocols; 4 kit runbooks, Skills and path-scoped rules; 5 the role; 6 the task; 7 records and
memory, evidence only, never instructions.

## [policies] The policy catalogue

Every key lives in `.governance/policy.toml` (walk S2), validated by the loop kit's schema, read
through one reader, mirrored to JSON for the hooks, and rendered into the charter.

| Key | Allowed values | Default | Source |
|---|---|---|---|
| `preset` | velocity, standard, strict, autonomous, or a repo-declared preset | standard | owner directive after the walk-through |
| `charter.override` | explicit-override, live-owner-wins, absolute | explicit-override | foundations F1-1 |
| `charter.practices` | a set of catalogue or repo-declared practices | the governance foundation set | foundations F1-3 |
| `core.bypass` | with-hooks-report, with-hooks-block, never | with-hooks-report | foundations K1 |
| `core.exceptions` | any-session-recorded, owner-only-expiring, none | any-session-recorded | foundations K4 |
| `autonomy` | plan-only, three-gates, every-stage | plan-only | R1.4, superseded by flow FL-P6 |
| `policy.guard` | owner-only, agents-with-reason, agents-within-mandate | owner-only | R4.2 |
| `policy.proof` | tty-cli, signed, both | tty-cli | walk S3 |
| `floor` | each of the four invariants, on or off, under the guard | all on | R5.1 |
| `hooks.bypass` | allowed, refused | allowed | R5.1 |
| `transitions.record` | any subset of trailer, log, micro-format | all three | walk S4 |
| `leases` | warn, refuse | warn | R2.2 |
| `leases.granularity` | build-and-unit, build, unit | build-and-unit | walk C1 |
| `leases.renewal` | activity, fixed, none | activity | walk C2 |
| `leases.expiry-hours` | hours | 24 | walk C2 |
| `leases.overlap` | kit-dirs, files, builds | kit-dirs | walk C3 |
| `leases.offline` | warn, refuse, follow-leases | warn | walk C4 |
| `verdict` | local-hook, peer-node, remote-ci | local-hook | R1.3, R4.4, R5.2 |
| `verdict.blocks` | own-mixed-contended, every-red, own-only | own-only | walk T1 |
| `verdict.held` | peer-or-cadence, push-selected, on-demand | on-demand | walk T2 |
| `verdict.flakes` | quarantine, record, retry-only; a threshold | quarantine | walk T3 |
| `tests.product` | declared, declared-with-runners, none | declared-with-runners | walk T4 |
| `plan.authority` | planner-drafts-owner-ratifies, planner-within-themes, owner-orders | planner-drafts-owner-ratifies | R2.4 |
| `plan.unplaced` | warn, refuse-new, review-only | warn | walk P2 |
| `plan.triage` | owner-batches, rules, archive-legacy | rules | walk P3 |
| `plan.kickoff` | offer-next, binding, advisory | offer-next | walk P4 |
| `design.handoff` | derived-ready, ready-plus-audit, status-and-tier | derived-ready | walk D1 |
| `design.overlap` | warn, refuse, index-only | warn | walk D2 |
| `build.scope` | warn-and-ask, refuse, report | warn-and-ask | walk B1 |
| `build.worktree` | per-unit, parallel-only, shared | shared | walk B2 |
| `deploy.runs` | landing-node, adopter-ci, operator | landing-node | walk DP1 |
| `deploy.promotion` | owner-approves-prod, auto-on-green, owner-approves-each | auto-on-green | walk DP2 |
| `deploy.on-verify-fail` | rollback-and-ask, halt-and-alert, roll-forward | roll-forward | walk DP3 |
| `deploy.currency` | pull-and-watch, push-branches, pull-only | pull-and-watch | walk DP4 |
| `maintain.host` | session-start, os-scheduler, cloud-routine | session-start | walk M1 |
| `maintain.cadence` | daily, weekly, every-session | daily | walk M2 |
| `maintain.fixes` | a set of named safe fixes | reap, prune landed, regenerate stale, defer dormant, records-only fixes, close finished run records | R2.3 |
| `maintain.on-breach` | file-ask, red-leg, report | file-ask | walk M3 |
| `review.<stage>` | off, opt-in, owed, owed-above-tier | opt-in; Build owed | R2.1 |
| `review.<stage>.effort` | the role efforts | the role's declared effort | R2.1 |
| `review.recommendation` | advice, binding, binding-above-tier | advice | R4.3 |
| `review.build.when` | per-build, per-unit, per-landing | per-build | walk B3 |
| `review.loop.cadence` | weekly, monthly, every-n-landings | weekly | walk R1 |
| `review.loop.retire` | propose-ratify, demote-then-propose, report | propose-ratify | walk R2 |
| `review.loop.window-days` | days | 60 | walk R3 |
| `budgets.*` | each cap's value and its mode, hard or soft | re-derived from evidence | walk R4 |

## [presets] Named policy presets

41 keys are too many to set one by one, and switching them one at a time is how a single policy file
would rebuild the sprawl gap-spine-06 measured. A preset is a named, complete assignment of the
policy keys; a repository names one preset and overrides individual keys on top of it.

**Rules.**
- `preset` is itself a policy key; its default is `standard`. Choosing or switching a preset is a
  policy change: guarded and recorded like any other.
- The effective policy is the preset's assignment with the repository's overrides applied. The
  charter renders the preset's name and only the keys that differ from it, so a reader sees the
  posture and its exceptions, not 41 lines.
- Every shipped preset assigns every presettable key, and only values that key allows; a check
  refuses a preset with a key missing or a value outside the schema, and a new key cannot land
  without a value in every shipped preset.
- Presets never touch the floor, `policy.guard`, `policy.proof` or `charter.practices`: loosening
  the guard or switching an invariant off stays an explicit owner choice, never a side effect of
  picking a posture, and a methodology is a choice about the product, not a posture.
- A repository may declare its own named presets in its policy file, each extending a shipped one,
  under the same completeness check.

**The four shipped presets.**
- `velocity`: least friction, for a solo owner or an early repository. Everything warns or records,
  nothing refuses but the floor, the closing review is opt-in too, and records are kept to the
  commit trailer.
- `standard`: the default. Exactly the owner's answers in rounds 1 to 5 and the walk-through:
  guarded governance (owner-only guard, the closing review owed, flakes quarantined), the owner gating
  only the plan with builds unattended past it (flow FL-P6),
  with speed-leaning delivery (bypass allowed, auto-promotion, roll-forward).
- `strict`: maximum assurance. Overlaps and stray scope refuse, every red blocks, reviews are owed at
  Design and Build and above-tier at Test and Deploy, recommendations bind, production waits for the
  owner, failed verifies roll back.
- `autonomous`: for unattended fleets under `plan-only` autonomy. The owner gates only the plan, so
  the guardrails that stand in for the owner's eyes are on: leases refuse, kickoff opens only
  planned work, recommendations bind above the tier, worktrees are per unit, production waits for
  the owner, failed verifies roll back.

`strict` and `autonomous` refuse hook bypass. Until dWitnessedBar's reliability bar is met, choosing
either one will stall on the same gate problems that made the owner allow bypass (R5.1). `strict`
and `autonomous` also declare the peer-node verifier, which needs a second fleet node; a solo
repository on either overrides `verdict` to `local-hook`.

| Key | velocity | standard (default) | strict | autonomous |
|---|---|---|---|---|
| `autonomy` | plan-only | plan-only | every-stage | plan-only |
| `charter.override` | live-owner-wins | explicit-override | absolute | explicit-override |
| `core.bypass` | with-hooks-report | with-hooks-report | never | never |
| `core.exceptions` | any-session-recorded | any-session-recorded | owner-only-expiring | owner-only-expiring |
| `hooks.bypass` | allowed | allowed | refused | refused |
| `transitions.record` | trailer | trailer, log, micro-format | trailer, log, micro-format | trailer, log, micro-format |
| `leases` | warn | warn | refuse | refuse |
| `leases.granularity` | build | build-and-unit | build-and-unit | build-and-unit |
| `leases.renewal` | activity | activity | activity | activity |
| `leases.expiry-hours` | 24 | 24 | 24 | 12 |
| `leases.overlap` | kit-dirs | kit-dirs | files | kit-dirs |
| `leases.offline` | warn | warn | refuse | follow-leases |
| `verdict` | local-hook | local-hook | peer-node | peer-node |
| `verdict.blocks` | own-only | own-only | every-red | own-mixed-contended |
| `verdict.held` | on-demand | on-demand | peer-or-cadence | peer-or-cadence |
| `verdict.flakes` | record | quarantine | record | quarantine |
| `tests.product` | declared | declared-with-runners | declared-with-runners | declared-with-runners |
| `plan.authority` | planner-within-themes | planner-drafts-owner-ratifies | owner-orders | planner-within-themes |
| `plan.unplaced` | review-only | warn | refuse-new | warn |
| `plan.triage` | rules | rules | owner-batches | rules |
| `plan.kickoff` | advisory | offer-next | binding | binding |
| `design.handoff` | derived-ready | derived-ready | ready-plus-audit | derived-ready |
| `design.overlap` | index-only | warn | refuse | warn |
| `build.scope` | report | warn-and-ask | refuse | warn-and-ask |
| `build.worktree` | shared | shared | per-unit | per-unit |
| `deploy.runs` | landing-node | landing-node | landing-node | landing-node |
| `deploy.promotion` | auto-on-green | auto-on-green | owner-approves-each | owner-approves-prod |
| `deploy.on-verify-fail` | roll-forward | roll-forward | rollback-and-ask | rollback-and-ask |
| `deploy.currency` | pull-and-watch | pull-and-watch | push-branches | pull-and-watch |
| `maintain.host` | session-start | session-start | os-scheduler | os-scheduler |
| `maintain.cadence` | weekly | daily | daily | daily |
| `maintain.fixes` | the full safe set | the full safe set | reap and regenerate only; the rest filed as asks | the full safe set |
| `maintain.on-breach` | report | file-ask | red-leg | file-ask |
| `review.plan` | opt-in | opt-in | opt-in | opt-in |
| `review.design` | opt-in | opt-in | owed | owed-above-tier |
| `review.build` | opt-in | owed | owed | owed |
| `review.test` | opt-in | opt-in | owed-above-tier | opt-in |
| `review.deploy` | opt-in | opt-in | owed-above-tier | opt-in |
| `review.maintain` | opt-in | opt-in | opt-in | opt-in |
| `review.<stage>.effort` | the role's effort | the role's effort | the role's effort | the role's effort |
| `review.recommendation` | advice | advice | binding | binding-above-tier |
| `review.build.when` | per-build | per-build | per-unit | per-build |
| `review.loop.cadence` | monthly | weekly | weekly | weekly |
| `review.loop.retire` | propose-ratify | propose-ratify | propose-ratify | propose-ratify |
| `review.loop.window-days` | 60 | 60 | 90 | 60 |
| `budgets.*` | every cap soft | each cap's evidence-derived mode | every cap hard | each cap's evidence-derived mode |

## [floor] The default floor

On by default, each switchable only under the policy guard (R5.1): a binding verdict runs before
the default branch moves; every policy change and stage transition is recorded; the guard protects
its own switch; no stage witness reads actor-typed state. Refusing hook bypass is a policy,
`hooks.bypass`, allowed by default until gate reliability is fixed; each bypass is recorded.

## [witnesses] Local-first witnesses

Harness refusals of agent writes to the policy file, hooks and verdict refs; a policy CLI that
needs an interactive terminal; a verdict the pre-push hook writes per tree hash; build exits
re-derived from committed history at the push; a peer node that re-runs the bar on the pushed tree
where `verdict = peer-node`.

## [contracts] Stage contracts

| Stage | Takes in | Hands out | Witness | Owner gate under `three-gates` (the default `plan-only` keeps only Plan's) | Review default |
|---|---|---|---|---|---|
| Plan | a prompt, an ask, a Maintain finding, a Loop Review proposal | a build placed in the plan by priority and `parents:`, leased | the placement predicate (warn); the ratification change | plan ratification | opt-in |
| Design | a planned, leased build and its brief | a structured spec set at a revision, forks resolved, overlaps acknowledged | derived READY; the design index (warn) | the design go | opt-in |
| Build | a unit in derived READY with its lease | in-scope commits and one closing review per build | history checks at the push: scope (warn and ask), review recorded | none | owed |
| Test | a built range | a hook-written verdict per tree; gate health, flake and seen-red records | the verdict from the declared backend; OWN reds block | none | opt-in |
| Deploy | a verified tree | a landing record; kit release notes; per-SHA deploy and verify records; adopter currency | lander and engine records; the currency probe | landing authorization | opt-in |
| Maintain | the daily cadence at session start | safe fixes applied; asks filed by stage; a maintenance record | detectors pinned and owned; fixes inside the declared set | none | the weekly Loop Review |

## [chain] The chain: eleven builds, final rosters

| Build | Stage | Parents | Planned units | Gaps owned |
|---|---|---|---|---|
| dOrderedCharter | Foundation | dClosedLoop | the practice catalogue with each practice's reach per stage, and `charter.practices`; the charter re-founded in its rank-1 envelope (front door, precedence and override rule with `charter.override` and its record, instruction map, active practices with reach, hand-off to the loop, the repository's project block from its own overlay); the instruction registry and the ladder; envelopes rendered for every registered document and the gate over them; the instruction map re-injected on compact and resume; ranked envelopes in every subagent handoff; the section-tag grammar and its resolver; the drive section composed from a drive table in each adopted kit's descriptor, checked both ways, each subagent's role line repeated in its handoff, the charter held inside 32 KiB; the core: the principle registry, the meta-check, the kinds register with each kind's owning build, the conformance-gate contract, the exception register and the `core.*` policies, and the factories and gates for governing documents, practices and Skills | gap-found-01, gap-found-02, gap-found-03, gap-found-04, gap-found-05, gap-found-07, gap-found-08 |
| dDeclaredLoop | Spine | dOrderedCharter | the loop kit and definition keyed by the stage tags, roles re-pointed after aOrientedCast closes; `.governance/policy.toml`, schema, one reader, JSON mirror; the named presets and their completeness check; the guard, the TTY CLI and the default floor; the transition record three ways; stage claims and the coverage gate; the witness-class rule; policy at govkit intake; the `next` verb over the loop's state, the `next —` micro-format, and the check that every declared command ends with one or declares itself terminal, laggards on a shrink-only list owned by their stage's build; the factories and conformance gates for commands, policy keys, presets, stages, hooks, roles and workflows | gap-spine-01, gap-spine-02, gap-spine-06, gap-design-01, gap-found-06 |
| dLeasedFleet | Concurrency | dDeclaredLoop | the lease grammar with run claims migrated; acquisition and release in both modes; overlap warn or refuse and takeover; fleet identity and remote uniqueness; offline behaviour | gap-conc-01, gap-conc-02 |
| dWitnessedBar | Test | dDeclaredLoop | gate health measured and the reliability bar; bypasses recorded; attribution deciding what blocks; the hook-written verdict; held legs by policy; the peer-node verifier; seen-red records; flake quarantine; the product-test contract with runner adapters; derived pre-commit list and multi-node cost evidence; the gate-leg factory and its conformance gate, every leg declaring the principles it enforces | gap-test-01, gap-test-02, gap-test-03, gap-test-04, gap-test-05, gap-test-06, gap-test-07, gap-test-08, gap-test-09 |
| dRankedPlan | Plan | dDeclaredLoop, dLeasedFleet | priority beside `parents:` and the generated plan view; the planner and triager role and Plan workflow; the placement predicate; rule-based triage; dormancy disposal; the live-build mapping carried out; Plan Review; kickoff offering the next item and attended briefs gated | gap-plan-01, gap-plan-02, gap-plan-03, gap-plan-04, gap-plan-05, gap-plan-06, gap-plan-07 |
| dIndexedDesign | Design | dDeclaredLoop | the derived-READY hand-off; the design index; design review by policy; reuse and alternatives backed by recorded probes; the research harness; agreement and tier checks; the spec measured, recommendations emitted, and the spec redesigned as a structured, tagged contract | gap-design-02, gap-design-03, gap-design-04, gap-design-05, gap-design-06, gap-design-07, gap-design-09 |
| dScopedBuild | Build | dIndexedDesign, dLeasedFleet, dWitnessedBar | one exit contract with a history-derived base, refusing a build's exit while a core red its own commits introduced stands; scope at the push; the closing review recorded; worktrees by policy; a write gate reading derived state; the checklist witnessed | gap-spine-03, gap-conc-03, gap-build-01, gap-build-02, gap-build-03, gap-build-04 |
| dShippedRelease | Deploy | dWitnessedBar | the landing record; kit release notes; the deploy engine; the incms adapter; the fleet register and currency watch; lander hardening; optional emitted CI; a derived runbook; the kit factory and its conformance gate | gap-deploy-01, gap-deploy-02, gap-deploy-03, gap-deploy-04, gap-deploy-05, gap-deploy-06, gap-deploy-07, gap-deploy-08 |
| dTendedCadence | Maintain | dWitnessedBar, dRankedPlan | the maintenance recipe; three hosts and the cadence; the safe-fix set; detectors with owners; map freshness; the maintenance record | gap-maint-01, gap-maint-02, gap-maint-05, gap-maint-06, gap-maint-07, gap-maint-08 |
| dCalibratedLens | Review | dTendedCadence | review by policy per stage and effort; the stage-exit recommendation; lenses for Plan, Test, Deploy and Maintain; the shared value ledger; the weekly Loop Review; caps re-derived from evidence and review cost | gap-review-01, gap-review-02, gap-review-03, gap-maint-03, gap-design-08 |
| dConvergedCharter | Convergence | dScopedBuild, dShippedRelease, dCalibratedLens | protocol text derived to facts only, each document in its envelope; every remaining positional reference migrated to tags; records merged by evidence; superseded parts retired through ratified proposals; adopters migrated onto the ranked charter and the loop; the record-kind factory and its conformance gate | gap-spine-04, gap-spine-05, gap-maint-04 |

The live-build mapping is v1's table, unchanged; the Plan build carries it out with the owner's
ratification and confirms dPolishedVitrine's track, which went dormant on 2026-10-14.

## [open] Interpretations to confirm at chain approval

- Positional section references other than `§` (numbered method steps such as `M5`, numbered spec
  sections, numbered hygiene checks) carry the defect walk CV2 names, so the tag grammar would
  replace them too, inventoried by Convergence.
