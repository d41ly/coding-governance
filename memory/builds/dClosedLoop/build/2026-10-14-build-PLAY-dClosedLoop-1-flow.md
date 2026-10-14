# The flow, step by step — each stage's scope, boundaries and checklist, as settled with the owner

**Serves:** research PLAY-dClosedLoop-1

The foundations revisit's step 2 (`build/2026-10-14-build-PLAY-dClosedLoop-1-foundations.md` holds
step 1 and the core). Each stage below holds the draft as presented, the forks asked and the answers
verbatim; agent roles are left aside until the owner returns to them.

## [layering] The owner's words, and the layers they set

> 2. Charter and its instructions are step 1 - this is what gets loaded first in any agent session,
> but the lifecycle flow of 'Plan' - 'Design' - 'Build' - 'Test' - 'Deploy' - 'Maintain' + 'Review'
> is the fundamental layer where an agent arrives with its fundamental instructions loaded.
> Primarily, this is designed in and for Claude Code but should not exclude any other agents or
> manual owner interactions. Every step of this design is a clear, deterministic process - it
> requires a set, mechanically enforced checklist of actions and specific agent roles (lower level)
> with their directives, so the cannot deviate. Each step of the flow is its own integrated process
> of a build. Builds are still the primary unit of this kit, but they exist on a different layer now
> - the flow now governs the actions that need to be taken. Let's go through each step of the flow,
> leaving agent roles aside for the time being, to determine the scope and boundaries at each of the
> steps.

The layers this sets, top to bottom:

1. **The charter**: what an agent loads first (foundations step 1).
2. **The flow**: the seven stages, each a deterministic process with a mechanically enforced
   checklist. The flow decides which action comes next; nothing outside a stage's checklist is a
   flow action.
3. **The build**: the primary unit of work, now a traveller through the flow. Each stage is an
   integrated process OF the build: the build carries that stage's records, and its state is the
   stage it is in and how much of that stage's checklist is witnessed.
4. **The roles**: the agents that carry out checklist actions under their directives, deferred.

Every checklist item is an action with a witness a check can read; a stage's exit is its last
item's witness, and the transition to the next stage is refused until every item before it holds.
Claude Code is the primary harness; every item is a CLI command too, so another agent or the owner
by hand walks the same checklist.

## [plan] Plan

### Current state, measured 2026-10-14

- **The plan is written up to three times.** The build README's five slots (the first is the build's
  goal bound, then improvements, detriments, rules, parked decisions), the brief (goal, items,
  acceptance, gates, non-goals, limitations, reuse, the owner's prompt and confirmation) and the
  kickoff card's task (title, goal, in, out, to-do, reuse, acceptance, gates): the goal three times;
  acceptance, gates, non-goals and reuse twice each.
- **Only 52 of 173 builds have a brief**, across 467 brief files; nothing else records a build's
  intake.
- The rest of Plan's measured state is the research record's: no priority or order record, 435 of
  521 live asks unlabelled, 165 of 167 builds opened from a prompt, 21 of 25 live builds dormant,
  nothing reviewing a plan.

### Draft scope

- **Intake.** Every source of work becomes a recorded intake item first: an owner prompt verbatim,
  an ask, a Maintain finding, a Loop Review proposal, adopter feedback.
- **Triage.** Severity, acceptance and readiness, by the declared rules (foundations walk P3).
- **Disposition.** Each item attaches to a live build, opens a new build, is deferred, or is refused
  as a duplicate or out of scope, and the choice is recorded.
- **The build's plan record.** Problem, goal, scope in and out as a cut-line, acceptance as
  observations, priority, dependencies on other builds, and each active practice's Plan reach
  answered (`[yagni]`: is the need real now?).
- **Placement and order.** The plan view is regenerated with the build in it.
- **Ratification and lease.** The owner ratifies under the repository's autonomy level and plan
  authority; the build lease is taken.

### Draft boundaries

- **Starts** when an intake item is recorded.
- **Ends** when the build is ratified, placed and leased, with its plan record complete and checked.
- **Hands Design** the plan record, with no mechanism chosen.
- **Does not** choose a mechanism or a seam, split the build into specs, touch product code, or run
  a gate.
- **Neighbours**: Maintain and Review feed its intake; Design receives its plan record.

### Draft checklist (each item witnessed by a check)

1. The intake item is recorded verbatim with its source.
2. Duplicates and overlaps with live builds and open asks are checked against the derived index, and
   the result recorded.
3. Triage is applied, and the rule that applied is recorded.
4. The disposition is recorded.
5. The plan record is complete: problem, goal, in and out, acceptance, priority, dependencies.
6. Each active practice's Plan reach is answered.
7. The plan view is regenerated and the placement predicate passes.
8. The build lease is held.
9. The Plan review recommendation is emitted, and the review run where policy owes it.
10. Ratification is recorded under the autonomy level and plan authority.
11. The Plan-to-Design transition is recorded, its witness the items above.

### Forks asked, 2026-10-14

**FL-P1. "Where is the boundary between Plan and Design: does splitting the build into units belong
to Plan?"** Offered: No units at Plan (Recommended); A named unit roster. Answer: No units at Plan
(Recommended).

**FL-P2. "The plan is written up to three times today (README, brief, card). Should a build have one
plan record?"** Offered: One record, the rest derived (Recommended); Three records, checked; Keep as
is. Answer, in the owner's words: "There should be one plan, that is the concrete details. The rest
depends on their function - briefs are handed to sidechain agents to orient them, they are of course
derived. 'Card' is a session orientation artifact, it feeds the session with mandatory details to
stay on track and not go out of scope, but that artifact is level above the plan - card exists
before anything else is written. Hierarchy and purpose here needs to be clearly established."

**FL-P3. "Should Plan set a cost budget for each build?"** Offered: Budget per build (Recommended);
Measure only; No cost tracking. Answer: Measure only.

**FL-P4. "Does every change pass through Plan?"** Offered: Yes, with a fast path (Recommended); Yes,
full checklist always; Small changes skip the flow. Answer, in the owner's words: "This needs to be
further evaluated - PLAN exists to map out larger, complex features and their integration into an
existing codebase. A full flow from the very first step is detrimental to amendments and mid-build
adjustments of an already mapped out feature. Open, fully planned builds, should adopt changes at
design stage (where implementation is brought into an existing plan shape), and a build shouldn't
and CANNOT re-enter plan stage mid-execution - this means it was not planned correctly."

### Settled for Plan, 2026-10-14

- **Plan is for larger, complex features and their integration** into an existing codebase. It
  hands Design a ratified build with no units; splitting into units is Design's.
- **One plan record per build** holds the build's concrete details. Cost is measured per build and
  per stage and read by the Loop Review; Plan sets no budget.
- **A ratified plan is fixed.** An open build adopts a change at Design, where implementation is
  brought into the plan's existing shape. A build never re-enters Plan: the transition engine refuses
  any transition back to Plan, and needing one is a planning miss, recorded and counted by the Loop
  Review. What happens to a build that hits one is asked below.

### The artifact hierarchy, as proposed for confirmation

Facts flow down the levels; records flow up. Each fact has one home, and a lower level renders what
it needs from a higher one rather than restating it.

| Level | Artifact | Purpose | Written | Holds |
|---|---|---|---|---|
| Repository | the charter, the loop definition, the policy file, the plan view | what every session works inside | before any work | rules, the flow, behaviour, the order of builds |
| Session | the card | orient one session and keep it on track and in scope | first, by the session-start hook, before anything else in the session | who and where (node, tree, branch, base), the build and stage the session works in, the session's own slice of scope, the active preset, the next action, and the plan's mandatory details rendered from the plan |
| Build | the plan record, the intake records, each stage's records, the transitions | the build's concrete details and its history through the flow | the plan in Plan; the rest by each stage | goal, cut-line, acceptance, priority, dependencies, practice reach; the owner's words verbatim; specs, passes, verdicts, landings, reviews |
| Unit | the spec | one unit's structured contract | in Design | definitions, design, boundaries, interfaces, acceptance |
| Agent | the brief (the handoff) | orient one sidechain agent for one task | derived, never authored | its role, its task, and the plan, spec and stage facts it needs, rendered |

### Follow-ups asked, 2026-10-14

**FL-P5. "Does this hierarchy capture card → plan → brief the way you see it?"** Offered: Confirm as
proposed (Recommended); Card points, renders nothing; Card above the repository level. Answer:
Confirm as proposed (Recommended).

**FL-P6. "A build hits a planning miss: a needed change no longer fits its ratified plan. What
happens by default?"** Offered: Pause, owner decides (Recommended); Finish as planned + new build;
Stop and supersede. Answer, in the owner's words: "By default past the planning stage, builds are
unattended, which is now the foundation of this product (the unattended kit becomes the centerpiece
of building). There needs to be more details on this - so far there doesn't seem to have been a
planning 'miss' incident, but I may be mistaken. In case of a critical planning issue, the plan
needs to be revised with a record, and its build re-designed preserving and/or amending the work
that might have been completed and is possible to preserve."

### Has a planning miss happened? Measured 2026-10-14

- **In-goal amendments are routine.** The unattended runs' records (`memory/builds/*/RUN*.md`) carry
  `rescope` rows: 376 `item add`, 14 `item retire`, 5 `item supersede`, 3 `item defer`, across 51
  builds; the commonest reasons for an added unit are a spec, a closing-review round, a split from
  another unit and a spec-audit round. This is the absorption the owner describes, already
  mechanised: the build method's M3 bounds a run's authority at the README's goal statement ("the
  README's GOAL statement is what a run may not amend"), and a fork the goal cannot survive is
  parked for the owner.
- **Goal-level misses: none found.** A search of every build record for an amended goal or a fork
  the goal could not survive finds two files, and both amend a spec's NON-goal
  (`aFusedCharter` PLAY-aFusedCharter-2, `dHashedPrelude` TOOL-dHashedPrelude-2), not a build's plan.
  The owner's recollection holds: across 173 builds the record shows no planning miss, only
  amendments inside the goal.

### Settled, 2026-10-14

- **Unattended is the default past Plan, and the unattended kit becomes the centerpiece of
  building.** The owner's plan ratification is the mandate; Design, Build, Test and Deploy run
  unattended by default. `autonomy`'s default moves from `three-gates` (round 1, R1.4) to `plan-only`,
  and so does the `standard` preset's. The other autonomy levels stay switchable. What the kit
  becomes as the flow's executor is the subject of the stage walks that follow; the chain is re-cut
  around it once they finish.
- **A critical planning issue is a recorded plan revision, then a re-design.** The trigger is the one
  the method already names: a fork the build's goal cannot survive. The run stops on it; the plan
  record takes a recorded revision, drafted and ratified under `plan.authority` (the owner by
  default), naming the evidence that forced it; the build returns to Design, which inventories the
  completed work and gives each unit a recorded verdict (kept as built, amended through a new spec
  revision, or retired) so everything that can be preserved is; then the run resumes. The build
  never re-runs Plan's intake and placement; only its plan record is revised. Every revision is
  counted, so the Loop Review can show whether planning misses stay as rare as the record says they
  have been.

## [design] Design

### Current state, measured 2026-10-14

The Design research record holds the measurements: the spec format's two tiers and ten Tier-2
sections; the build method's M1 to M5 and M12; `plan_state` deriving MISSING, THIN, FORKED or READY
while the write gate reads only status and tier (TOOL-dNarrowedAnchor-1 is INPROGRESS and FORKED);
41 live-spec pairs from different builds sharing a path, unseen; spec audits declared by 3 of 173
builds, and 0 of 254 audits clean. In-goal amendments land here already: the 376 units the
unattended runs added after opening.

### Draft scope

- **Input**: the ratified plan record; or, for an open build, an admitted amendment inside its goal;
  or a ratified plan revision.
- **Decomposition**: the build split into units, one mechanism each, with their order and write
  sets (Design owns decomposition, FL-P1).
- **Each unit's contract**: the structured spec (definitions, design, boundaries, interfaces,
  acceptance as observations with their commands), its reuse probes and alternatives recorded, each
  active practice's Design reach answered.
- **Forks**: every fork resolved, by its probe where it is a fact-question, by the owner or within the
  mandate otherwise; a fork the goal cannot survive stops the run for a plan revision.
- **Coherence across builds**: overlaps the design index finds are acknowledged in the specs'
  boundaries.
- **Review**: the stage-exit recommendation, and the spec audit where policy owes it, its findings
  folded.
- **Amendments and re-design**: in-goal amendments (add, defer, retire, supersede a unit) and the
  re-design after a plan revision (each completed unit kept, amended or retired, with its reason).

### Draft boundaries

- **Starts** when one of its three inputs is recorded.
- **Ends** when every unit in scope is in derived READY and the roster is recorded.
- **Hands Build** READY units with their order and write sets.
- **Does not** write product code, change the plan's goal or cut-line (only a ratified plan revision
  does), or run a gate beyond the spec-level checks.

### Draft checklist (each item witnessed by a check)

1. The input is recorded: plan record, admitted amendment, or plan revision.
2. The reuse and precedent probes are run and recorded (map, recall, bug classes, open asks).
3. The units are decomposed and the roster recorded with order and write sets.
4. Each unit's spec is written in the structured contract format.
5. Each active practice's Design reach is answered for each unit.
6. Every fork is resolved, or the run has stopped for a plan revision.
7. Every overlap the design index finds is acknowledged.
8. The review recommendation is emitted; the spec audit is run and folded where policy owes it.
9. Every unit in scope is in derived READY.
10. The Design-to-Build transition is recorded, its witness the items above.

### Entry points, partly settled

- **Settled:** a new, complex feature enters at Plan; an amendment that fits an open build's plan
  enters at Design; no build re-enters Plan.
- **Open, to evaluate after Design and Build are walked:** where a small, self-contained change that
  belongs to no planned build enters (a bugfix, a typo, a docs or records fix, a hotfix), and how
  Maintain's safe fixes sit beside it. The candidates depend on what Design and Build define: a
  micro-spec entering at Design, a patch path entering at Build, or Maintain's own process.
