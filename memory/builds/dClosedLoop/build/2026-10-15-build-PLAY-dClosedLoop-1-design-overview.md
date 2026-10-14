# The product design at this stage: an overview

**Serves:** research PLAY-dClosedLoop-1

Composed 2026-10-15 for the owner's question "How does the product design look like at this stage?",
from the records at `2323a2a23`. This is a snapshot. Each section names the record that owns its
content, and where the two differ, that record wins.

The two diagrams shown with the answer are kept beside this record:
- `build/2026-10-15-build-PLAY-dClosedLoop-1-design-overview-layers.svg`;
- `build/2026-10-15-build-PLAY-dClosedLoop-1-design-overview-cycle.html`.

## [shape] Three layers, one loop

Gov is a development lifecycle governance product. It governs a loop of Plan, Design, Build, Test,
Deploy and Maintain, with Review at any step, in any repository that adopts it, for concurrent,
multi-node, agentic work. The owner set three layers, and they form one loop (roles `[layers]`):

1. **Charter instructions**: what every session or API call loads first, and their ranks.
2. **The DLG flow**: the steps, each a checklist whose items are witnessed.
3. **Roles**: bound workers, each a static system instruction plus one task per item.

The loop runs like this:
- the charter teaches every agent to drive the flow;
- the flow's checklist names each item and its actor;
- a role performs the item and returns a typed record;
- the records move the build, and `next` reads them to name the next item.

## [charter] Layer 1: the charter instructions

Owned by v2's `[front-door]`, `[principles]`, `[policies]`, `[presets]` and `[floor]`.

**The ladder.** Every load-bearing document carries a generated envelope that names its rank (P13).

| Rank | What sits there |
|---|---|
| 0 | the platform's own instructions |
| 1 | the charter, and beside it the build's orientation card; the charter wins a conflict |
| 2 | the loop and the repository's policy values |
| 3 | stage methods and protocols |
| 4 | kit runbooks, Skills and path rules |
| 5 | the role |
| 6 | the task |
| 7 | records and memory, as evidence only |

**The charter's order.** It fits Codex's 32 KiB limit, and dOrderedCharter writes it.
1. what gov is;
2. the precedence and override rule;
3. the instruction map;
4. the core principles;
5. the decision principles;
6. the active practices, each with its reach per stage;
7. the drive section: how to start, each stage's commands, one line per role;
8. the preset and its overrides;
9. the repository's own block.

**The principles.** P1 to P26 are fixed, and change only by an amendment the owner ratifies.

| Group | Principles |
|---|---|
| The loop | P1 one loop, declared once; P2 witnessed hand-offs; P3 local-first verdict; P4 one contract, two authorizations; P6 Maintain closes the loop; P7 review by policy; P20 the flow is the layer above the build |
| Governance | P8 every adopter is an adopter; P9 measured weight; P10 every behaviour a switchable policy; P11 facts, not prose; P13 ranked instructions; P14 practices with reach; P15 the charter starts the loop and the tools continue it; P16 the core cannot be built around |
| Design | P12 specs are structured contracts; P17 features carry the design between units; P18 decision principles settle unattended forks, and no build parks; P19 built work is never rewritten in place |
| Coordination | P5 concurrency by lease, inside the flow; P21 builds coordinate before they wait |
| Determinism | P22 position is derived, never remembered; P23 claims are trusted by key and source; P24 the checklist is a program; P25 role functions only in role agents; P26 every exchange between roles is a typed record |

**The policies.**
- One catalogue lives in one policy file: 94 keys, 89 of them presettable.
- There are four presets: `velocity`, `standard` (the owner's answers, and the default), `strict` and
  `guarded`. A repository may declare its own.
- The floor is always on:
  - a binding verdict runs before the default branch moves;
  - every change is recorded;
  - the guard protects its own switch;
  - no witness reads state an agent typed.

## [flow] Layer 2: the DLG flow

Owned by the flow record, v2's `[contracts]`, and P20 and P21.

**Entry.**
- Complex features enter at Plan.
- In-goal amendments and patch builds enter at Design.
- Every request gets a disposition: continue, amend, new, patch, ask or none. The agent places it
  alone, and its facts are checked.

**The checklists.** There are 70 items, each with one actor and a witness:
- Plan 11, Design 10, Build 10, Test 8, Deploy 10, Maintain 9;
- a stage review 7, the Loop Review 5.

| Step | Takes in | Hands out | Exit witness |
|---|---|---|---|
| Plan | a request, an ask, a Maintain filing, a Loop Review proposal | a placed, leased build in the plan by priority and parents | the request, written by the intake hook, is the ratification |
| Design | the ratified plan record | features, units, interfaces and a structured spec set, forks recorded | derived READY; interfaces confirmed to dependents |
| Build | a READY unit and its lease | in-scope commits and one closing review per build | history checks at the push; core checks at the exit |
| Test | the built range | a hook-written verdict per tree; flake and seen-red records | the declared backend's verdict |
| Deploy | a verified tree | the landing, release notes, verify records, adopter currency | the lander's and the engine's records; `landed` sent to dependents |
| Maintain | the cadence | safe fixes applied; filings to Plan; patch builds to Design | detector readings; fixes inside the declared set |

**How a build moves.**
- A build's step is its least-advanced unit's.
- Builds run unattended past Plan.
- Backward transitions are recorded like forward ones.
- Every role's return is routed on a closed set of outcomes.

## [roles] Layer 3: roles

Owned by the roles record's `[roster]` and the flow-roles record's `[cycle]` and `[steps]`.

**The roster: fourteen roles.**
- Sidechain: orientation scout, prompt writer.
- Plan and Design: planner, researcher, reuse scout, architect, spec writer.
- Build onward: builder, tester, deployer, maintainer.
- Review: reviewer (one role, its lens set per step, the loop included), skeptic, synthesizer.

The driver is not a role. It is the main session when attended and the executor when not, it does no
role work, and it makes only cheap state reads.

**The item cycle.**
1. `next` names the item and its actor.
2. The driver hands the prompt writer the item's details.
3. The prompt writer returns the task.
4. The executor wraps the task in a hashed work order and spawns the actor fresh.
5. The actor returns its template through the schema-forced channel, retried up to `roles.retries`.
6. The driver resolves the witness, persists the return, reads the mailbox, and asks `next` again.

**Each step as a role sequence.**

| Step | Sequence |
|---|---|
| Entry | the scout composes the card and the placement evidence |
| Plan | the planner drafts, the researcher answers its questions, review roles check it, and the owner's request ratifies it |
| Design | the reuse scout, then the architect, then one spec writer per unit in parallel, then review |
| Build | one builder per unit, then the scope report, then the closing review through the diff lens |
| Test | the hook's verdict, then the tester routes each red |
| Deploy | commands land; the deployer writes the notes and judges the verifies |
| Maintain | the tester and the maintainer file to Plan; patches go to Design |

**Exclusivity holds at four points**: the work order's construction, the tool call, the return, and
an after-the-fact verifier.

## [mechanics] What holds it together

**Orientation** (the orientation record).
- The scout composes the card in a sidechain.
- The card's truth is a ref per build on the remote. It reaches rank 1 through an imported
  per-worktree file.
- The full kickoff runs only when there is no READY card.
- A claim is trusted by its key and its source.

**Card upkeep.**
- The whole card is re-rendered at each transition (`card.follows`).
- Its pointers are updated at every item (`card.pointers`).
- A terminal snapshot is committed.

**Compaction** (the compaction results).
- The default is to compact with the current card. A fresh session at the boundary is allowed.
- The summary is a lead, never a source.
- "The executor holds no model context" is an owed check.

**Coordination** (the coordination record).
- Leases are refs, written by compare-and-swap.
- Each build has a mailbox with a closed set of message kinds plus `intake`, read at every item.
- Interfaces are confirmed at Design's exit.
- A dependent's landing is held until its parent lands.
- Landings go through the turnstile queue in plan priority.

**The owner's touchpoints.**
- The request, recorded by a hook, is the ratification.
- Questions are answered with best effort, and no build parks on one.
- Amendments arrive as intake.
- Progress is reported in the micro-formats at the end of each turn.

## [chain] The chain: eleven builds

Owned by v2's `[chain]`. The join against the register shows 97 gaps, each owned once.

| Build | Stage | Parents | Gaps owned |
|---|---|---|---|
| dOrderedCharter | Foundation | dClosedLoop | 9 |
| dDeclaredLoop | Spine | dOrderedCharter | 18 |
| dBoundRoles | Roles | dDeclaredLoop | 11 |
| dWitnessedBar | Test | dDeclaredLoop | 10 |
| dRankedPlan | Plan | dDeclaredLoop | 10 |
| dIndexedDesign | Design | dDeclaredLoop | 8 |
| dScopedBuild | Build | dIndexedDesign, dWitnessedBar | 7 |
| dShippedRelease | Deploy | dWitnessedBar | 9 |
| dTendedCadence | Maintain | dWitnessedBar, dRankedPlan | 7 |
| dCalibratedLens | Review | dTendedCadence | 5 |
| dConvergedCharter | Convergence | dScopedBuild, dShippedRelease, dCalibratedLens | 3 |

## [open] What is still open

- **K1**, the reading of `core.bypass`, awaits the owner's confirmation.
- **v2's `[open]`** holds interpretations to confirm at chain approval: positional references beyond
  `§`, and the coordination interpretations.
- **v2's `[owed]`**:
  - the executor and its checklist engine have no owning build yet;
  - the executor's always-spawn harness, the turnstile and the lander are left to the lower-level
    step;
  - so are the compaction checks.
- **The chain re-cut** gives the executor a home, and settles whether gap-orient-08 moves with it.
- **The owner's announced polish** of the flow steps, now that all three layers are in place.
- **Then**:
  1. approval;
  2. the spec;
  3. the declared audit;
  4. the chain's folders;
  5. the decision rows;
  6. the acceptance joins;
  7. the live-build mapping;
  8. the full bar.
