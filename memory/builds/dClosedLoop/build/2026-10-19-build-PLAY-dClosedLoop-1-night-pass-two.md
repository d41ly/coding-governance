# The night pass two: the owner's seven points, worked unattended

**Serves:** research PLAY-dClosedLoop-1

While two review runs read the last three folds, the owner reviewed the Flow and Role layers' adoption piece, answered
its forks, and then handed over seven points to be worked unattended through the night. This record holds the words,
what the design held on each point, the research, the design worked in, and the forks parked for the owner's return.

## [words] The owner's words, 2026-10-19

> I'm stepping away for the night, you will continue this pass unattended until fully my points are fully reviewed. Go through each of them separately, one after another, understand them and their fit into the current design. Run agents/workflows at medium effort to assist you in research and design, park all the forks for me to go at for when I return.
>
> ### Review points
> 1. Continuing our review of the Flow and Role Layers - how flexible is it to introduce new workflows, processes and roles? Currently, we're designing against a baseline loop scenario of 5 steps (+review) and a set number of Roles doing work across those steps but how flexible the loop is to accomodate for sub-scenarios? Case: an edge case is identified which requires its flow steps to be in different order, new roles added and inserted into the flow. How easy is it for the current design to accomodate? Is it possible to define additional work scenarios in the flow and for the runtime to pick one (or several) based on the work it's driving (eg. one scenario for design work, another for developing a mobile application, third for coding a high-precision data system)? Is it possible to create and adapt scenarios on the fly and record them after? Pick scenarios from a pre-shipped set and build scenario pipelines? Modify and reshape workflows (case: single agent; a set of parallel agents; a workflow of a single step; a workflow of 2 or more steps; a mix or different roles in a workflow; variable agent caps)? 'Lenses' are simple prompt instructions, so how easy it is to add or remove a 'lens'? Does all this functionality converge in a cohesive method?
>
> 2. Another build, aScoutedSeam, has finished running its reuse workflow experiment and merged its findings to Gov's origin/main. Particularly, it was able to achieve 94% test cases solved through two important methods - workflow shape and prompt-writing rules. I believe, its findings can apply to the entire core Gov's layer to improve work accuracy across Flow and Role layers. Read 'memory/builds/aScoutedSeam/prompts/2026-10-19-prompt-DEPL-aScoutedSeam-1-1-session.md' on Gov's origin main, review aScoutedSeam's findings, apply it's best performing workflow shape and prompt writing principles to work in the design.
>
> 3. Instruction and Memory layers - is it time to find a different data format and storage implementation as opposed to the current plaintext/markdown structure? Is there a more efficient, relational structure that would be able to mechanically maintain connections between data points in large adopting repos? If a build was to occur across several nodes at the same time, how would they efficiently coordinate and update each other on completed work, decisions taken, problems encountered in real time? We'd previously decided on a mailbox approach but this isn't a long-term solution, and definitely not an efficient one. Would using an actual relational cloud database be a viable solution? Or is there a more agent-friendly approach?
> 4. In continuation of the previous point - is there a handoff system between agents, between sessions? Effective communication between automated systems and agens is paramount to producing higher-quality work and Gov is being architected exactly for this purpose. How will agents shape and pass data between each other, how will it move between different sessions potentially working on different pieces of the same build?
>
> 5. Instruction caps. Currently, many documents - charter, methods, protocols, prompts, etc.. have caps enforced on them by Gov. The idea is great - to prevent them from growing out of control, bloating the read path. However, this is already a blocking point in many builds, and agents keep relaxing the caps. Let's take a different approach for our design - remove any hard-caps and make them advisory instead of blocking. Row/KB size limit policies can still be owner-defined, but a single enforcing switch is set to WARN by default instead of refuse. Research and recommend a better implementation for this, if there is any.
>
> 6. Gotcha lookup doesn't perform its job currently - it's good for filing gotchas and looking them up but it's purpose - serve gotchas relevant to the ongoing work that an agent or a session may trip isn't served. Agents may call on gotcha orientation several times per session and still never catch the right one. How can this tool take a more useful shape? Can this functionality move to orientation agents? Or runtime? If there is no way to make this more efficient, it's better to retire this functionality.
>
> 7. Tooling issue - agent-cap.js is currently broken and doesn't perform its function (instead of capping agents at 5 max, it limits spawns to 5 every 45 minutes). This tool must be retired, and agent limits must be owner-adjustable by policy, governed by the runtime? or the which layer is appropriate for this task?
>
> ---
>
> Don't stop until you've worked out each point, once you have - prepare a report for me on this and a resulting state of the project, and park all the forks for me to go at once when I return. Run tier2 reviews on the folds twice.

## [method] How the pass runs

- **One point at a time.** Each point gets its own section: what the design already holds, what the research found,
  the design worked in, and its forks. Research runs ahead in waves, since a point's design waits on its returns.
- **Research.** Researchers run at the owner's medium effort, read-only, one question each. Each handoff is in
  `prompts/`, and each return is saved verbatim beside this record. Agent-cap admits five direct spawns at a time, so
  the questions go out in waves of at most five.
- **Forks.** Each fork's first option is the recommendation. The design as folded shows the recommendation, marked
  pending on its fork, as the first night pass did. The `NT` family numbers them.
- **Reviews.** The night's folds are reviewed twice, as two independent Tier-2 runs compared defect by defect, and
  the defects are folded before the report.
- **Bounds.** No product code, no merge and no push, as the build's brief says; the design map and the atlas are
  regenerated after each design change.

## [research] Dispatched, 2026-10-19

Researchers ran at the owner's medium effort, read-only, one question each, never more than five at once. Each handoff
is in `prompts/`, and each return is saved verbatim beside this record. A row's outcome is filled when its return
arrives.

| Dispatch | Point | Handoff | Return | Outcome |
|---|---|---|---|---|
| 127 | 1, the converged design | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-8-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-scenarios-design.md` | six seams carry parts of a variant and none selects; a `scenario` kind over the composition |
| 128 | 1, prior art | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-9-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-scenarios-prior-art.md` | eight families, none whole; pinned fragments chosen per build, recorded and promoted |
| 129 | 2, aScoutedSeam applied | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-10-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-scoutedseam-apply.md` | 23 agent calls inventoried; the diff-time reuse check missing; most edges carry no rows |
| 130 | 3, today and the design, measured | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-11-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-storage-measured.md` | running |
| 131 | 3, prior art | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-12-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-storage-prior-art.md` | files in git, one derived SQLite index, per-sender refs, an ids-only doorbell |
| 132 | 4, the converged design | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-13-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-handoffs-design.md` | five carriers and no one contract; commitment rows on the record graph, the branch pushed per witnessed item |
| 133 | 4, prior art | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-14-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-handoffs-prior-art.md` | running |
| 134 | 5, caps | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-15-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-caps.md` | running |
| 135 | 6, gotchas | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-16-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-gotchas.md` | running |
| 136 | 7, agent-cap | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-17-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-agent-cap.md` | running |

## [p1-scenarios] Point 1: scenarios, one method for flexible flows and workers

**What the design held** (dispatch 127). Six seams each carry part of a variant, and none of them selects one:
- the entry-point table, which picks only where a build starts;
- playbooks and `repeat`, a content recipe that enters at Design;
- presets, one per repository;
- the composition with its repository stages, one per repository (FA-1 to FA-7);
- the per-boundary policy sets, `review.breakpoints` and `probe.points`, repository-wide;
- the shape and lens registries.

Nothing records what kind of work a build is: none of the 173 build READMEs carries a kind, and the plan record has no
field for one. A structural change mid-build goes only through the overlay, and it moves every build at its next step
boundary. The shapes registry already expresses one agent (`single`), parallel agents (`per-unit`), mixed roles over
stages (`panel`), twin runs and experiments, with caps per workflow under agent-cap's fixed five, and a lens has been a
catalogue row since FA-1. The pass also found records disagreeing: the lens entering by an edit to the harness in
flow-steps and the review-system record, four shape kinds in the systems record against five, the closed kind set
without `item` or `lens`, the frame's transitions fixed though a splice may sit between stages, and the role matrix
silent on repository roles. Each is folded below.

**What outside systems teach** (dispatch 128). Eight families, none covering every case:
- configurable superset models (C-YAWL, GitLab `rules`), which only switch parts off;
- pinned templates included by reference (Azure `extends` with its required-template check, GitHub reusable
  workflows), safe but unrecorded mid-run;
- late-bound repertoires chosen per work item and refined by recorded rejections (YAWL worklets, Camunda ad-hoc
  subprocesses);
- case plans with discretionary items and sentries (CMMN);
- structure computed by code with versioned execution (Temporal, LangGraph): a probe ran a reordered variant to a
  run-time `KeyError` and compiled an orphan role without complaint;
- instance change with migration of compliant instances (ADEPT2, Camunda migration);
- model-chosen handoffs (the OpenAI Agents SDK, Claude's subagents), recorded only as transcripts;
- process mining, which sees a deviation only after the fact.

**The answer.** Today the flow bends in five places but has no unit for a variant, so none of the owner's cases has
one home. The recommendation gives it one: a build runs one composition, gov's rows, the repository's, the scenarios
it was placed under and its own recorded changes, pinned per step and checked whole.
1. **A scenario is a registered kind** (NT-1). A `scenario` row names the scenario it extends, an admission predicate
   over a request's facts, its entry, the rows of registered kinds it activates (stages, items, field patches,
   exclusions, roles, workflow entries, lens opt-ins, leg packs), a preset slot and caps. Gov ships some, a repository
   adds its own in its overlay, and every check runs on the composed result, so a scenario cannot reorder or drop a gov
   stage or touch the fixed set.
2. **Selection at placement** (NT-2). The orientation scout names the scenarios whose predicates hold over the request,
   with the facts; `placement.check` re-evaluates every predicate; the planner may re-pick at Plan; a later re-pick
   happens only at a step boundary. A request no scenario admits runs `flow.scenario-default`.
3. **Policy per scenario** (NT-3). A scenario's preset slot scopes a preset and overrides to its builds, never a key
   presets never touch, so a high-precision scenario can run strict while the repository runs standard.
4. **Changing a build's flow mid-build** (NT-4). A role proposes rows for its own build. Under `flow.adapt`'s default, a
   change that only adds items, roles, stages or stricter values applies unattended at the next step boundary and is
   recorded; one that removes, reorders or loosens waits for the owner while the build carries on. At each step
   boundary the build's witnessed path is compared with its pinned composition, so an unrecorded deviation files an
   order.
5. **Recording and promotion** (NT-5). Every change is kept in the build's folder. The Loop Review proposes a scenario
   from a change two or more builds carried, the owner ratifies it through `instructions.edit` with `promoted-from`
   edges to those changes, and builds in flight move to it only at a step boundary and only if they comply.
6. **The shipped set** (NT-6). Gov ships the scenarios its records already know: feature, amendment, patch,
   playbook-run and design-only, the last passing all five stages with record units, so P20 stands. Expansions
   register their own, and domain scenarios, a mobile application or a high-precision data system, are a repository's.
7. **Several scenarios and pipelines** (NT-7). A build may run several, unioned in a declared order. Two that set one
   field differently red at composition and wait for the owner, as `flow.scenario-conflict` says. A scenario may name
   the one that takes over at a step's exit, which makes an in-build pipeline, and a cross-build pipeline is builds
   filed with `depends-on`. Scenarios per feature or per unit wait on the owed feature and unit tables (`gap-flow-15`).
8. **Workflow shapes as data** (NT-8). A workflow entry declares its ordered stages, each with its role, fan, cap,
   effort and the rows it receives and returns, and the five kinds become named defaults over them. One agent, a
   parallel set, one step, several steps, mixed roles and variable caps are then all data, each cap at or under the
   repository's agent limit (point 7).
9. **Lenses** (NT-9). A lens is added as a catalogue row whose brief is a unit and removed by a swap or an exclusion;
   a repository lens records a replay result when one ran and never owes one.
10. **Cohesion.** One selector, the scenario, sits over one composition; one pin per step records what ran; one door,
    `instructions.edit`, writes every structural row; one check runs the whole. The six seams become fields of it.

**The owner's cases.**

| Case | Under the recommendation |
|---|---|
| An edge case needs its steps in another order and a new role inserted | a recorded change: `needs` patches reorder items, a repository role item is inserted, a repository stage may be spliced between gov's; gov's stages keep their order |
| A scenario per kind of work, picked by the runtime | `scenario` rows with admission predicates, chosen at placement and re-checked mechanically |
| Create or adapt a scenario on the fly, and record it | a build's recorded change, applied at a step boundary, kept in its folder, promoted by the Loop Review and the owner |
| Pick from a shipped set and build pipelines | gov's five, extended by the repository's; in-build successors at a step's exit, and cross-build `depends-on` |
| Reshape workflows | a workflow entry's ordered stages as data, the five kinds named defaults, caps under the agent limit |
| Add or remove a lens | a catalogue row, swapped or excluded |

**What it leaves for later.** Scenarios per feature or per unit wait on the feature and unit transition tables. Caps
above five wait on point 7. A change of meaning in prose (a lens brief reworded for one call) leaves no structural
deviation for the step-boundary comparison to see, the same limit the adoption pass found.

**Folded.** v2's P8, four `flow.*` keys with their preset rows, and clauses on dDeclaredLoop, dPlacedRequest,
dRankedPlan, dKeptSession, dBoundRoles and dCalibratedLens, each pending its fork; the foundations record's C3 gains
`item`, `lens` and `scenario`; flow-steps and the review-system record say a lens is data; the systems record has five
kinds, workflow stages as data and the `scenario` namespace; the adoption record's frame admits a splice; layer-roles'
matrix reads the composition; the memory plan's `promoted-from` takes a scenario source; and the register gains
`gap-flow-20`, `gap-flow-21` and `gap-review-18`. The design map reddened once on the fold: it reads each namespace
owner line as one line, and the fold had wrapped dDeclaredLoop's in two; it is one line again.

## [forks] Parked for the owner, 2026-10-19

Each fork's first option is the recommendation, and the design as folded shows it, marked pending. Where the answer
sets a key's default, the options are the key's allowed values (P10); where it is a structural choice, it is a
decision.

| Fork | Question | Options, the recommendation first | What the answer sets |
|---|---|---|---|
| NT-1 | What is a scenario? | a registered kind: named, pinned overlay rows with a preset slot, chosen per build; presets and playbooks extended to carry structure; no scenarios, one composition per repository | a structural decision |
| NT-2 | Who picks a build's scenario? | the orientation scout at placement, `placement.check` re-evaluating its predicates, the planner able to re-pick at Plan; the owner, always; a table mapping request labels to scenarios | a structural decision, and `flow.scenario-default`'s value |
| NT-3 | May a scenario set policy for its builds? | yes, a preset and overrides scoped to its builds, never a key presets never touch; no, policy stays repository-wide | a structural decision |
| NT-4 | Who may change a build's own flow mid-build? | a role proposes, a change that only adds applies unattended at the next step boundary and is recorded, one that removes, reorders or loosens waits for the owner; the owner approves every change; no changes | `flow.adapt`'s default: additive-recorded, owner-approves, off |
| NT-5 | How does a recorded change become reusable? | the Loop Review proposes a scenario from a change two or more builds carried, and the owner ratifies it; only the owner promotes; never | `flow.promote`'s default: loop-proposes, owner-only, off |
| NT-6 | How does a design-only build end? | a `design-only` scenario passes all five stages with record units, P20 unchanged; P20 amended with a transition from Design to a terminal state | a structural decision |
| NT-7 | Can a build run several scenarios? | yes, unioned in a declared order, a conflict refused for the owner to order, with in-build successors at a step's exit; one scenario per build | `flow.scenario-conflict`'s default: refuse, declared-order |
| NT-8 | How are workflows reshaped? | each workflow entry's ordered stages as data, the five kinds named defaults; the five kinds only | a structural decision |
| NT-9 | How is a lens removed, and must a repository lens prove itself? | a swap or an exclusion, and a repository lens records a replay result when one ran but never owes one; swaps only; every repository lens owes the blind replay | a structural decision |
