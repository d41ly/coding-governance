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
  `prompts/`, and each return is saved verbatim beside this record. Agent-cap admits five direct spawns per prompt, so
  the questions go out in waves of at most five (point 7 measures how it counts, and retires it).
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
| 130 | 3, today and the design, measured | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-11-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-storage-measured.md` | markdown holds as the store of record; the designed JSON index does not hold at 10x; a derived SQLite file per node keyed by blob |
| 131 | 3, prior art | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-12-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-storage-prior-art.md` | files in git, one derived SQLite index, per-sender refs, an ids-only doorbell |
| 132 | 4, the converged design | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-13-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-handoffs-design.md` | five carriers and no one contract; commitment rows on the record graph, the branch pushed per witnessed item |
| 133 | 4, prior art | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-14-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-handoffs-prior-art.md` | eight families; a schema rendered per work order, and create-only registers keyed by derived keys |
| 134 | 5, caps | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-15-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-caps.md` | 24 caps, 18 refusing; one switch at warn, made visible on a passing run, priced and trended, with consumer limits, correctness checks and limits that define a format kept outside it |
| 135 | 6, gotchas | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-16-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-gotchas.md` | 6.2% precision on code reviews and 18% at the moment of the edit; retire writing-time serving by anchors, keep classes on review, gate the syntactic ones |
| 136 | 7, agent-cap | `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-17-researcher.md` | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-agent-cap.md` | it counts claims per prompt, never agents in flight, and a notification resets it; one Runtime key enforced at three scopes |

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
above five wait on point 7, which makes the limit the owner's `runtime.agents-in-flight`. A change of meaning in prose (a lens brief reworded for one call) leaves no structural
deviation for the step-boundary comparison to see, the same limit the adoption pass found.

**Folded.** v2's P8, four `flow.*` keys with their preset rows, and clauses on dDeclaredLoop, dPlacedRequest,
dRankedPlan, dKeptSession, dBoundRoles and dCalibratedLens, each pending its fork; the foundations record's C3 gains
`item`, `lens` and `scenario`; flow-steps and the review-system record say a lens is data; the systems record has five
kinds, workflow stages as data and the `scenario` namespace; the adoption record's frame admits a splice; layer-roles'
matrix reads the composition; the memory plan's `promoted-from` takes a scenario source; and the register gains
`gap-flow-20`, `gap-flow-21` and `gap-review-18`. The design map reddened once on the fold: it reads each namespace
owner line as one line, and the fold had wrapped dDeclaredLoop's in two; it is one line again.

## [p2-scoutedseam] Point 2: aScoutedSeam's measured principles, applied

**What aScoutedSeam measured.** The owner's `origin/main`, at `a60b0c7dc`, holds the build's records and its handoff,
and dispatch 129 re-derived every figure from its instruments. The reuse check went from 4 of 23 cases to 33 of 35
across a tuned and an untuned set, with no change of model. The 94% is the union of two stages, one run each with one
judge per case:
- an orientation scout at kickoff, which frames needs and a concrete sketch before it searches, runs a convention
  census, and returns at most twelve seams and five MUSTs;
- an enumerated diff check, which lists every unit a diff adds, answers one closed-vocabulary row per unit, and answers
  one row per orientation MUST: `used`, `bypassed` or `not-applicable`.

Both stages run at medium. At `low` the check covered 8 of 23 where medium covered 14, and the open question at
`extra` covered 11. The build states thirteen principles, each marked measured or not: only reuse finding was measured,
and every other kind of step is a hypothesis to measure.

**What the re-derivation adds.** The rows' +7 on the diff check (13 to 20 of 23) added no union recall on the tuning
set: all seven cases were ones the orientation had already found. What the rows did was move the orientation's advisory
catch into the step that gates. Rows therefore belong first on the edges that feed a gate. The pass also found three
places where aScoutedSeam's own records disagree: a row headed "blind judge" that a path matcher graded, an orientation
to spec edge called measured that no arm ran, and a spec half called unmeasured that a later arm measured.

**What gov's flow lacks.** The inventory counts 23 agent calls in the target flow. Against them:
- **The diff-time check is missing entirely.** No Build item runs it, the diff preset has no reuse lens, and the diff
  reviewer reads only the diff and the spec.
- **No edge hands its commitments as rows.** A handed fact needs a disposition only when it proves false (P29), and the
  review finder's schema holds findings only, with the line "a class with no hit needs no finding", which is the silent
  drop the principles name.
- **The reuse scout's return is unspecified.** It returns "the seam", singular.
- **The shape exists in places.** Five role items already answer their inputs one to one: refutation, report, fold,
  attribution and inventory. It is not yet the rule.
- **v2 is stale.** It still quotes the earlier figures and calls aScoutedSeam's branch unmerged.

**The design worked in.**
1. **The measured shape, adopted** (NT-11, NT-13). dScopedBuild gains `build.reuse-check`, per unit before the closing
   review. It runs the reuse scout at medium over the units the unit's commits add, listed from the code record and
   capped at sixty, one closed-vocabulary row per unit, added rows for what the lister cannot see, a no-stop line, and
   one row per MUST seam the unit's spec carried. A `duplicate` or `bypassed` row is a fix pass. Its acceptance is a
   reproduction of the measured figures through gov's own route, on the 23 tuning and 12 held-out cases.
2. **The scout's contract** (NT-10). dIndexedDesign's reuse scout returns under M1c's contract: needs and a sketch,
   anchors, a census, at most twelve seams and five MUSTs, MUST defined as a defect, the unmet needs, and its seams
   handed on as rows.
3. **Rows on edges, gated by evidence** (NT-10). dDeclaredLoop gives an item an `upstream` field. Every commitment it
   names arrives as a row the return answers, the join is computed at the return, and a `bypassed` row is also a
   finding. The rows are recorded on every edge but gate only where a measurement passed, the reuse edge first.
4. **The prompt writer's frame** (NT-10). dBoundRoles composes every role item's task in the skeleton's order: role and
   job kind, material, boundaries, population, upstream rows, row contract, added rows, the no-stop line, and the
   return contract last, every output bounded.
5. **An effort floor** (NT-12, answered in the owner's words). Effort is the owner's setting: medium by default,
   and no agent takes a role below medium without the owner's explicit authorization, though the owner may set
   and run it at low.
6. **The experiment's method.** dFairHearing's experiment shape takes the measurement discipline that produced the
   figures: a held-out set frozen before tuning, one variable per arm, parsed replies counted first, a blind judge with
   rotated labels, and the union read as one system.
7. **Stale lines corrected.** v2's `[owed]` gains the measured system, dFairHearing's "unmerged" is corrected,
   dLinkedLibrary's acceptance names the held-out set, layer-roles' effort reading and "unmerged" are revised, and
   flow-steps' experiment shape takes the method.

**What waits on measurement.** The rest of the ranked changes are hypotheses until measured, each with its plan in the
return: S-item and acceptance rows into the closing review, seam rows through decomposition and the spec's reuse
section, checklist classes as rows, plan observations into decomposition, and needs listed from the plan record. The
owner's "apply it across Flow and Role layers" therefore lands as structure now and as gates edge by edge, as each
measurement passes.

**Folded.** v2's `[owed]`, dFairHearing's and dLinkedLibrary's corrections, clauses on dFairHearing, dDeclaredLoop,
dBoundRoles, dIndexedDesign and dScopedBuild, and the key `build.reuse-check.second-pass` with its preset row;
flow-steps' Build table gains `build.reuse-check` and its route; layer-roles' two stale passages are revised; and the
register gains `gap-build-06`, `gap-roles-27` and `gap-design-11`.

## [p3-storage] Point 3: storage, a relational structure, and news between nodes

**The owner's four questions, answered.**
1. *Is it time for a different format than markdown?* Not for the store of record. Dispatch 130 measured `memory/`
   at 4,375 files and 72.7 MB, growing 2.3 times in the last month. Storing it is not the problem: every reader, the
   verdict and the design map ran with no remote, cat, grep and git read it, and a review reads its diffs. What does
   not scale is how it is read. The designed index, one JSON file per tree rebuilt on every tree miss, took about 30 s
   to rebuild and 1.6 GB to load at ten times today's tree. memory-recall's per-worktree cache is already 478 MB and is
   rebuilt whole after any edit. The memory legs re-read the whole tree on every run, 83 s at 54 MB.
2. *A relational structure that maintains the connections mechanically?* Yes, and it is the derived index, done as
   a database: one SQLite file per node in the git common directory, rows keyed by blob, so a commit re-parses only
   the blobs it changed. At ten times today's tree a one-file update took 9 ms and an inverse query about 1 ms, on
   the standard library's `sqlite3`, the engine memory-recall already uses. Only extractors write it, so it can never
   disagree with the records the way beads' writable SQLite and JSONL did. Connections stay correct by two rules:
   relations are derived from the records, never typed beside them, and each edge type's cardinality is checked per
   target over the merged tree. Dispatch 131's probe D showed why the second is owed: two branches each superseding
   one decision merged clean in git, and only the index saw the conflict.
3. *Coordinating several nodes in real time?* The transport is not the delay. A fetch takes 0.6 s, and the median
   gap between pass commits is 7.5 minutes. A node learns news only when it reads, and the design reads at items and
   transitions. So the fix is the read point. A hook shows unread message ids at every tool call (a median of 10.5 s
   apart), read from the node's local copy of the refs, which a detached fetch refreshes, so no tool call waits on the
   network. The live message becomes a doorbell carrying only the message's ref and id, so a lost ring costs latency,
   never a fact. The mailbox's single chain per build is the part that does not last: eight concurrent writers took
   4.5 times the ideal compare-and-swap attempts. One ref per sender took none extra.
4. *A cloud relational database?* Not as the store of record, and not as the transport. A node offline for a day
   could neither read nor write. The verdict would stop being local (P3). The witness would leave committed history
   (P2). Every node would hold a new connection secret, and a git-only adopter could not run gov. A synced SQLite
   (cr-sqlite, libSQL) silently keeps one of two concurrent decisions. A git-backed database (Dolt) needs a binary on
   every node and splits the repository into two stores. A database or a bus fits only behind the doorbell, as an
   optional adapter: Postgres `NOTIFY`, ntfy or NATS ringing with ids. The agent-friendly approach is the one gov
   already has, made fast: files in git, one derived index, and the CLI over it. An MCP server over the index stays
   possible as an optional read surface and is not built, since the CLI is the floor (P36).

**The design worked in.**
1. **Text in git stays the store of record** (NT-14), and, by the owner's answer, a cloud relational database is
   an accounted extension: a change feed every write joins, and a memory-mirror point an adapter fills for
   real-time sharing across nodes, the database itself planned.
2. **The index becomes one SQLite file per node** (NT-15). dOrderedCharter's index clause, the systems record's
   `[cross]` and its index bullet are revised: rows keyed by blob, or by path and blob for what a path names, the tree id only a freshness key, JSON only as
   `gov tag`'s output, and a deleted file rebuilt to identical rows. dTotalRecall moves memory-recall's FTS5 tables
   into the same file, and its memory legs read the index for unchanged blobs, an index read and a full read agreeing
   on a planted tree.
3. **Relations checked per target after merge.** dTotalRecall declares each edge type's cardinality per target as
   well as per source and checks it over the merged tree, seen red on probe D's two supersessions.
4. **One mail ref per writing session** (NT-16): `refs/gov/mail/<slug>/<fleet tag>/<session>`, revised in v2,
   coordination and the memory plan, keyed by session after the review found one node's sessions sharing a ref.
5. **News at every item, or at every tool call by policy** (NT-17, the owner's default: every item). dKeptSession
   gains `mailbox.notice` (`every-item` by default, `every-tool-call` or `off`) and `mailbox.fetch-seconds` (60). The doorbell carries ids only, and the disposal still happens at items
   and transitions, as `mailbox.reads` says.
6. **Leases with a history, and writes free of the lander.** dPlacedRequest writes each lease and claim as a commit
   whose parent is the ref's previous tip, so the history the design names as the witness exists. Lease, claim and
   mail writes take no lock the lander holds, which today blocks them for a median 334 s per landing.

**Left open, each measured by the build that owns it.** The push latency to the real remote, and the host's rate
limit on a fetch a minute, are unmeasured. The rebuild-equality test is owed. The 100-times figures are a linear
extrapolation. The lease expiry stays at its ratified 24 hours. The tick-renewed lease that would let it drop is
Runtime's to propose.

**Folded.** v2's dOrderedCharter, dKeptSession, dTotalRecall and dPlacedRequest rows, with eight gaps, and the keys
`mailbox.notice` and `mailbox.fetch-seconds` with their preset rows; the systems record's table, `[cross]` and index
bullet; coordination's items 6 and 7; the memory plan's mail ref; and the register's `gap-found-33`, `gap-mem-41` to
`gap-mem-43` and `gap-conc-04` to `gap-conc-07`. The preset check's free values gain "seconds", the class of "hours".

## [p4-handoffs] Point 4: handoffs between agents, sessions and nodes

**What the design held.** Dispatch 132 traced one build's hand-offs end to end: eleven hops over five carriers, the
work order and its return, the records `next` reads, the card, the mailbox and the coordination refs. They share keys
but no contract. Inside one item the hand-off is typed and checked: a schema-forced return, the witness computed and
never typed. Between items, between nodes, and for the owner's "completed work, decisions taken, problems
encountered", it is not:
- **Between items and steps** no commitment crosses as a row the next step must answer. Point 2 folded the rows.
- **Between nodes** no rule pushes a build's branch before its landing, so another node cannot see finished units,
  and a take-over cannot read the witnesses the runtime record says it reads.
- **Completed work, decisions and problems** have no message kind, and nothing keys a decision by its question.
  Dispatch 133's probe 2 showed two sessions deciding one question differently: both landed in the mailbox's chain,
  and only a reader would notice.

It also found twelve contradictions between the records, folded below where a record could be corrected.

**What prior art adds.** Dispatch 133 read eight families, from transcript transfer to durable workflows. Two of its
probes decide the shape:
- A static return schema passed a dropped, an invented and a doubled commitment row. A schema rendered per work order,
  with the order's row ids as its only allowed values and each one required, refused all three.
- A create-only ref keyed by a derived key refused the second of two conflicting decisions, and turned a retried post
  into a no-op. An append-only chain kept both.

**How agents shape and pass data.** One contract: every commitment crosses an edge as a row the receiver answers.
1. Each role return declares what it establishes: seams, criteria, interfaces, resolved forks, findings and repairs.
2. The next work orders hand those on as upstream rows (point 2's `upstream` field).
3. Each order's return schema is rendered from its own rows, so a dropped, invented or doubled row fails the return
   and is retried. A `bypassed` row is a finding that routes. Rows gate only where a measurement passed, as point 2
   set.

**How work moves between sessions on one build.** Through the trail, pushed, and through registers:
- **The branch.** The commit queue commits each role return into the trail at its item's witness and pushes the
  build's branch as `build.push` says, every pass commit by default (the owner's NT-19). A push takes no lock the
  lander holds and runs no gate: a build branch's push skips the bar (110 pushes, median 0.44 s), and CI runs only
  on `main`. Another node then reads the same witnesses, derives the
  card's pointers from the branch, and can take over (NT-19).
- **Units across sessions.** A session that does not hold the build may take one of its units under that unit's
  lease, as `build.unit-holders` says. It drives only that unit's passes on its own branch, and the build's driver
  alone runs transitions (NT-20).
- **Decisions.** A decision is written once to `refs/gov/decisions/<build>/<key>`, keyed by the work-order slot that
  raised it, never by its wording. A second session deciding the same slot is refused and reads the first (NT-18).
- **Problems.** A problem is written to `refs/gov/problems/<encoded subject>/<problem id>`: the subject is a path, a
  definition, a tag or a node fact encoded into a legal ref name, and the id is derived from the filing act and
  the problem, so two problems on one path both land. A work order cut later is handed the problems whose subject meets its item's seed (NT-18).
- **Messages.** The mailbox keeps only traffic that crosses a lease, each message's id derived from its sender's act or
  session, item and pass, kind, subject and the id it answers, so a retry is refused as a duplicate while two answers
  both land. Its closed set of kinds is one list.

**The contradictions, as folded.**
1. dBoundRoles' work order still read "its inputs as record fields at their SHAs": now "handed as content".
2. `gov-session` folded into the prompt writer, which acts in no item: it now retires into the `intake` message or a
   unit offered at placement, in dWellOiledMachine, with the fates row moved (NT-21).
3. The mailbox's closed set was three lists: coordination's item 6 now declares one.
4. flow-interactions' FI-6 still said no reply within a bound means unreachable: revised to the owner's RC-5 and
   FR-8.
5. The ownership record named dDeclaredLoop for the mailbox and the lease: now dKeptSession and dPlacedRequest, as
   NP-24 moved them.
6. The closing review was handed the range alone: flow-roles' Build 8 and dScopedBuild now hand it the criteria and
   MUST seams as rows, recorded until measured.
7. No P7 rows at any edge: point 2's fold.
8. A take-over assumed pushed witnesses: `build.push`.
9. The return's writer was unnamed: the commit queue, at its item's witness.
10. The card's per-item pointers had no store: derived from the pushed branch.
11. The prompt writer's framing had no checker: dBoundRoles checks every anchor at render.
12. Live delivery cannot reach an act, since an act makes one call. That stays: an act hears news when its next work
    order is cut, with the problems that meet its seed. Interrupting an act mid-item is left open.

**Left open.** The worst case dispatch 133 names: two sessions meeting a question no work-order slot declares derive
different keys, and both decisions land. Only a lease overlap or the closing review catches it. The build that owns
the registers must run that fixture as its losing test.

**Folded.** v2's dBoundRoles, dFurnishedOrders, dPlacedRequest, dKeptSession, dScopedBuild and dWellOiledMachine
rows, with eight gaps, and the keys `build.push` and `build.unit-holders` with their preset rows; coordination's item
6; flow-roles' Build 8; flow-interactions' FI-6; four ownership rows; layer-memory's return row; the fates row for
`gov-session`; and the register's `gap-rt-33`, `gap-roles-28`, `gap-roles-29`, `gap-conc-08` to `gap-conc-11` and
`gap-flow-22`.

## [p5-caps] Point 5: caps advisory, under one switch

**The owner's direction, taken as decided.** Caps become advisory. Their values stay the owner's. One switch decides
enforcement, and it warns by default. What the night had to work out is what the switch covers, and how a warning
avoids becoming noise.

**What exists.** Dispatch 134 inventoried 24 size caps, and 18 of them refuse a commit, a push or a render. They
cover the charter template, the rendered charter, the kickoff engine, the guides, every live spec, line lengths,
index entries, build READMEs and their five slots, dossiers, role bodies, one-line rules, roster lines, the kickoff
manifest, the card, the count of universal bug classes and the recall export. Their history bears out the owner's
complaint:
- The read-path ceiling moved 26 times in 17 days, then retired, its own header saying the movements "bought no
  trim".
- The method guide was raised four times, and the unattended protocol, pinned with no headroom, three times in three
  days.
- Caps forced a cut three times, and blocked a merge where neither branch alone was over.

The design already leaned this way:
- P9 re-derives caps from evidence.
- Walk R4 defined a soft cap.
- `budgets.*` gave each cap a mode, hard or soft.
- `orient.budget` and `memory.over-budget` were already advisory.

But `instructions.checks` and `annotations.budget` still refused by default, and each cap carried its own mode.

**What a plain warning costs.** Two of dispatch 134's losing tests decide the shape:
- **A warning in a passing leg reaches nobody.** The runner prints only `GATE ok <name>`, and two size warnings fire
  unseen today. Prior art agrees: Google's experience is that developers ignore warnings they are not shown at the
  moment of review.
- **One switch over everything would loosen correctness too.** `instructions.checks` refuses a load set missing a
  required unit under the same switch as its size budget.

A consumer's own limit also differs from a cap. The harness keeps 10,000 characters of hook context and Codex 32 KiB
of instructions, and past them text is silently lost.

**The design worked in.**
1. **One switch** (NT-22). dGroundRules builds `budgets.enforce`, read by every gate that enforces a size cap on a
   document or record: `warn` by default, as the owner set it, with `refuse` the other value. Each cap's
   value stays the owner's under `budgets.*`, which loses its per-cap mode, and the owner may pin named caps to
   refuse through `budgets.pinned` (NT-22). Line and entry lengths are size caps
   too, so they fall under the switch. Two things stay outside it:
   - a consumer's own limit, which fits or refuses, because over it text is lost;
   - a check of correctness, which is no cap.

   Dispatch 134 kept a third class outside: the limits that define a format, such as a one-line rule's 200
   characters and an index entry's length, which never moved. The fold departs from that pick, since the owner's
   words remove every hard cap, and NT-22 offers it as its second option (the review's correction).
2. **Correctness split out.** `instructions.checks` now governs only a load set missing a required unit. P27, the
   systems record's slot budget and dOrderedCharter's load-set and composition clauses read the size half under
   `budgets.enforce`.
3. **`annotations.budget` retired into the switch.** Its budget is a value under `budgets.*`, still counted over the
   blocks a commit touches. `memory.over-budget` stays as the owner's MS-3 set it: memory slices are reported, never
   refused, whatever the switch says.
4. **A warning that bites** (NT-23). Four parts:
   - dWitnessedBar shows every size warning on a passing run, in the runner's summary and its verdict record,
     attributed to the unit that grew the file.
   - dCalibratedLens prices each breach in the value ledger by its bytes and its reads.
   - The Loop Review raises an owner item for a breach that persists or grows, counting only new or grown breaches,
     so the warnings never turn into noise.
   - The advisory caps keep the brake they lose at the commit.
5. **One record corrected.** layer-instruction's "the charter's 32 KiB cap" is the rendered charter's 20 KiB. The
   32 KiB is Codex's own limit.

**Where an advisory cap still fails.** It fails where no Loop Review runs, as under `velocity` or in a repository
without one. It fails in unattended runs, whose output nobody reads until the review. At a consumer's limit, the
refusal stays. Dispatch 134 also found the slot-limits file saying its values "bind nothing today" while the README
contract binds 98 READMEs. That is a product file, left to the build that owns it.

**A note on the research.** Dispatch 134 ran `check-template-size.sh` six times on its scratch clone before it
learned that a researcher's gate grant is empty. The scratch guard then refused its next gate run. The six runs wrote
nothing, and the return says so.

**Folded.** P9 and P27; dGroundRules, dWitnessedBar and dCalibratedLens clauses, and dOrderedCharter's two clauses
revised, with four gaps; the keys `budgets.enforce`, new, `budgets.*` and `instructions.checks` revised, and
`annotations.budget` retired, with their preset rows; the systems record's slot budget and annotation keys;
layer-instruction's charter cap; and the register's `gap-tool-24`, `gap-test-22`, `gap-found-34` and `gap-review-19`.

## [p6-gotchas] Point 6: the bug-class lookup, reshaped where it works and retired where it does not

**The owner's question.** The lookup files classes and finds them well, but does not serve the class a session is
about to trip. Can it take a better shape, in the orientation agents or the runtime, or should it retire?

**What it does.** Dispatch 135 read `gotchas.py`:
- **Anchors.** A class's anchors are harvested from the paths its body mentions.
- **Selection.** A path selects a class by substring or basename, and tiers only order the list.
- **Universals.** Six universal classes ride every checklist.
- **Callers.** The unattended build's per-pass checklist, the default-off prebuild, the review harness and the
  charter's "run it before any review".
- **The design.** v2 hands classes to the builder's work order by the unit's write set (SA-7).

**What it measured.** The lookup ran again at the head of each of the 47 closed reviews that record a range, of the 66
whose appendices carry a classes column, and its selections were compared with the classes of the confirmed findings:
- **Precision.** On code reviews it was 6.2%: 82 hits in 1,317 classes selected. On a diff of 85 files or more it
  selected 60 to 95% of the catalogue, and twelve classes were selected on every code review.
- **Use.** Sessions ran the lookup 1,127 times on this node, and a class's body was opened 45 times.
- **At the moment of the mistake.** Run on the one file a confirmed finding cites, the selector picked the right
  class 18 times in 98. It picked nothing 68 times.
- **Recall.** The selector never missed a class that existed and fit. Its failure is noise, and the wrong moment.
- **What a class is.** The classes that carry the hits are shaped by an act, not a path: amending a rule, answering
  one question twice, routing an output, an observed-by claim no arm discharges. A spec or an intent shows them. A
  file path does not.
- **Coverage of findings.** Of 1,771 confirmed findings, 1,371 carry no class.

**The answer.**
1. **Writing-time serving by path retires** (NT-24). The builder's work order no longer carries classes its write
   set selects, and the unattended per-pass checklist and the prebuild go with it.
2. **Runtime is rejected, measured.** Three ways were tested:
   - A hook serving classes by the edited path inherits the 18%.
   - A content trigger, such as a text-mode `open`, fires on 53 of 111 Python files.
   - A pre-tool hook's context arrives beside the tool's result, after the write.

   A trigger precise enough to stay quiet is a gate, and that is the next point.
3. **Syntactic classes become gates.** Under `review.left-shift`, a syntactic class becomes a gate at its second
   occurrence, and a gated class leaves every checklist. dLinkedLibrary derives each class's gate status, gated only where the
   class names a leg seen to refuse a planted case of it, and marks its anchors as where it bit, never what triggers it.
4. **Classes stay on review** (NT-25). There they are the only source of labels and left-shift dispositions.
   dFairHearing's checklist is still selected by the pinned range, and dLinkedLibrary, once it derives the status,
   takes every fully gated class off it, which cuts 29% of the items for 5% of the labels. A replay with the checklist and without it, over the known-defect corpus, decides
   between that selection and every ungated class. The charter's "run it before any review" retires, since the harness
   hands the checklist itself.
5. **Orientation may serve by intent, if it earns it** (NT-26). dIndexedDesign's reuse scout already reads a unit's
   needs and sketch under the measured contract point 2 adopted. It also names at most five classes from the
   catalogue's one-line index, each with a reason, for the unit's spec to carry. That is armed only once a replay
   over the closed code reviews beats the anchor ranking's top five, at a precision of at least 20%. Each scout gets
   its unit's spec and the index as they stood before the build, never the review. If the scout loses, serving
   while code is written retires outright, as the owner allowed.

**Left open.** Two figures leave doubt:
- Fifteen review records state a smaller checklist than the lookup re-selects over their recorded range. Their
  callers passed another range or tool version, so the noise figures describe the recorded ranges.
- The design reviews' precision, 19.9%, is inflated by classes anchored on this build's own records.

**Folded.** dFurnishedOrders' bug-class field revised; dIndexedDesign, dFairHearing and dLinkedLibrary clauses,
with three gaps; flow-steps' Build memory and extension points and the checklist's note; and the register's
`gap-mem-44`, `gap-mem-45` and `gap-review-20`.

## [p7-agent-cap] Point 7: agent-cap retired, the agent limit the owner's

**The owner's report, measured.** Dispatch 136 piped synthetic hook payloads through a copy of
`tools/hooks/agent-cap.js` and read this session's own slot ledger. agent-cap never counts agents in flight:
- It gives each (session, prompt id) pair five claims. A claim frees 45 minutes after it was made, whether its agent
  still runs or finished long ago.
- Every new prompt id starts a fresh budget, and a task notification brings a new prompt id: 73 of this session's
  143 prompt ids were notifications. So the owner's "5 every 45 minutes" holds within one prompt, and across prompts
  nothing bounds the total.
- It never counts a Workflow agent: three Workflow calls of five agents each touched no slot.
- Five idle claims refuse a sixth agent, and five claims aged 46 minutes admit five more while the first five run.

**Why per window.** A PreToolUse hook cannot see an agent end: a background `Agent` call's PostToolUse returns at
launch. The harness offers two better counters:
- **Its own settings.** `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` bounds Agent-tool spawns, 20 by default, and
  `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` bounds one Workflow run, 16 or fewer by default. This node's 2.1.292
  binary carries both.
- **Two hook events.** SubagentStart fired for every agent in this session, 466 Workflow agents and 89 direct ones.
  SubagentStop carries the agent's id, but whether it fires for a killed, stopped or stalled agent is unmeasured.

agent-cap's own comment says the Workflow cap is "NOT lowerable from userland", which the harness's documentation
and binary now contradict.

**Which layer.** The limit is Runtime's, since Runtime runs the cycle and already designs a reservation released at
SubagentStop. The key belongs to the policy file, so dGroundRules declares it and every build may read it. It is
enforced at three scopes:
1. **The harness's own settings**, rendered from the key, for one session's direct spawns and one Workflow run. They
   are the only reliable in-flight counters today. A Workflow agent over the limit queues, but a direct spawn over
   it is refused with "Do not retry", and the harness does not enforce the direct bound under ultracode (`gap-rt-35`, the
   review's correction). dGroundRules lands them
   with the key, and agent-cap's slot ledger, its conf, its `AGENT_CAP` refusal and its print mode retire in that
   unit.
2. **An in-flight ledger**, dWellOiledMachine's hook pack, for the session's total: a slot claimed at SubagentStart,
   released at SubagentStop, and swept when a session dies. A Workflow agent's claim converts one slot of its
   call's reservation, so it counts once. It is armed only once the spike shows SubagentStop firing
   for every way an agent ends. Otherwise the limit splits into direct and Workflow budgets, with one live run per
   session.
3. **The supervisor's reservation** under the lease, for act sessions and nodes, as layer-runtime designed it.

**`runtime.agents-in-flight`.** The key is an agent count, 6 by default by the owner's answer. The owner raises or lowers it
by a policy write (NT-28), and a spawn over it waits in Runtime's admission queue instead of being refused. Today's cap is lower-only, because an environment knob "leaves no diff", and a tracked policy write
leaves one. No preset sets it, since the limit is a fact about the owner's plan and machine, like the harness keys
presets already never touch.

**Where agent-cap's other rules go** (NT-27):

| Rule | Its home | Build |
|---|---|---|
| the slot ledger, `FANOUT_CAP`, `--print-cap`, the `AGENT_CAP` refusal | the key, rendered into the harness's settings | dGroundRules |
| the raw `parallel` and `pipeline` ban, and the concurrency half of the bound rule | retired: the harness queues | dGroundRules |
| the verifier total, the loop markers and the lens count | the merge bar's harness checks, and the shapes' declared fan | dFairHearing, dBoundRoles |
| the ref-keyed join ban | `check-review-join.sh` alone | dFairHearing |
| the spec-audit opt-in | a review-kit pack on Workflow calls | dFairHearing |
| the handoff spawn guard and harness admission | the roles pack, admission comparing a harness with its landed blob | dBoundRoles |

`tools/hooks/agent-cap.js` retires in dBoundRoles once its last rule has moved, with an upgrade step and its readers
inventoried by value. The charter's agent-cap line is among them.

**Left open.** Whether SubagentStop fires for every way an agent ends is the spike's to measure, and the in-flight
ledger waits on it. An adopter with no roles file loses the inline-script total check, though the harness settings
still bound its concurrency.

**Folded.** v2's `runtime.agents-in-flight`, on the list presets never touch; the kit-conf passage and an owed check
revised; dGroundRules, dFairHearing, dBoundRoles and dWellOiledMachine clauses, and four clauses revised; layer-runtime's
bound, per-prompt total, script rules, agent-cap's arm, the owner-pack row, the carriers table, the roster and the
in-flight test; and the register's `gap-rt-34` and `gap-roles-30`, with `gap-rt-05` amended.

## [reviewed] The night's folds, reviewed twice and folded

The owner's "Run tier2 reviews on the folds twice": two independent light diff reviews read `ad54fe388` over
`e1a54ac67`, dispatches 137 and 138, and `build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two-reviews-compared.md` compares them defect by defect. They confirmed 31 defects, three of
them high, and none needed the owner: where the runs left two routes, the owner's words or an earlier answer chose
one. Most were folds that landed in v2 and nowhere else, which this record's sections above now state as folded. The
rest tightened the design itself:
- a problem keyed per problem under its encoded subject, a message id that includes the id it answers, and mail refs
  keyed per writing session;
- index rows for what a path names keyed by path and blob, and each worktree's uncommitted rows its own;
- a Workflow agent counted once, the spike red on each way an agent can end, and the interim agent limit recorded as
  `gap-rt-35`;
- a class's gated status derived from a leg seen to refuse it, never declared;
- every catalogued value of the new flow and unit keys given its arm.

NT-22 gains the caps research's own pick as an option. NT-27 and NT-28 drop the options the owner's words rule out.

## [forks] Parked for the owner, 2026-10-19

Answered by the owner on 2026-10-19, in `[answers]` below.

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
| NT-10 | How far do aScoutedSeam's principles reach now? | the measured shape and contracts now, the skeleton as the prompt writer's frame, and rows recorded on every edge but gating only where a measurement passed; every edge's rows gating at once; only the measured reuse shape | a structural decision |
| NT-11 | Where does the diff-time reuse check run? | a Build item per unit before the closing review, its duplicates and bypassed MUSTs fix passes; a reuse lens in the closing review's panel; once per build at Test | a structural decision |
| NT-12 | May a coverage step run below medium effort? | only with an experiment record that shows the lower effort holds; freely, as the effort keys say | a structural decision: a check on the effort keys' values |
| NT-13 | Does the reuse check run a second, independent pass? | off by default, on where a miss is expensive; always; never | `build.reuse-check.second-pass`'s default: off, on |
| NT-14 | What is the store of record for instructions and memory? | text in git, markdown and TOML, as today; a git-backed database such as Dolt; a cloud relational database | a structural decision |
| NT-15 | What shape does the derived index take? | one SQLite file per node keyed by blob, memory-recall's tables inside it and the memory legs reading it; one JSON file per tree, as designed; per-worktree caches, as today | a structural decision |
| NT-16 | How do senders share a build's mailbox? | one ref per writing session per build; one ref per build, as designed | a structural decision |
| NT-17 | When does a session learn of a message? | at every tool call, from a local copy a detached fetch keeps fresh, with the live channel ringing ids only; at every item, as `mailbox.reads` alone; never between reads | `mailbox.notice`'s default: every-tool-call, every-item, off |
| NT-18 | How are decisions, problems and messages kept between sessions and nodes? | create-only registers keyed by derived keys: decisions by their work-order slot, problems by subject, and message ids derived so a retry is refused; the mailbox's chain alone, as designed | a structural decision |
| NT-19 | When is a build's branch pushed? | at every witnessed item; at every pass commit; at every transition; at the landing | `build.push`'s default: every-item, every-pass, every-transition, at-landing |
| NT-20 | May another session drive one unit of a build it does not hold? | yes, under that unit's lease, the build's driver alone running transitions; no, one driver per build, as designed | `build.unit-holders`' default: any-session, driver-only |
| NT-21 | What replaces `gov-session`? | the `intake` message or a unit offered at placement, with the receiving session's prompt writer rendering its work order; the prompt writer, as designed; `gov-session` kept | a structural decision |
| NT-22 | What does the one cap switch cover? | every size cap on a document or record, line and entry lengths included, with a consumer's own limit and every check of correctness left outside it; every size cap but the limits that define a format, which keep refusing, as dispatch 134 picked; the same as the first, with the owner able to pin one cap to refuse; every check, correctness included | a structural decision; its default is the owner's: warn |
| NT-23 | How does an advisory cap keep a brake? | shown on a passing run, attributed to its unit, priced by its reads, and trended into an owner item by the Loop Review; shown on a passing run only; printed by its leg, as today | a structural decision |
| NT-24 | Does the builder's work order carry the classes its write set selects? | no: serving by path retires, with the per-pass checklist and the prebuild; yes, as designed; yes, without fully gated classes | a structural decision |
| NT-25 | How does a review get its classes? | the checklist its range selects, minus fully gated classes, until a replay with and without the checklist decides between that and every ungated class; every ungated class; no checklist at review | a structural decision |
| NT-26 | Who serves classes while code is written? | the reuse scout by intent, at most five with reasons, armed only after it wins its replay, else no one; a runtime hook by path or content; no one | a structural decision |
| NT-27 | Where does the agent limit live, and what enforces it? | one Runtime key, enforced by the harness's own settings now, an in-flight ledger on SubagentStart and SubagentStop once the spike passes, and the supervisor's reservation, every other agent-cap rule moved to its home; the harness's settings alone; the limit split between direct and Workflow budgets with one live run per session, the research's fallback | a structural decision |
| NT-28 | How far may the owner raise the agent limit? | to any count, by a policy write, which leaves a diff; only up to the harness's own defaults, 20 direct agents and up to 16 per Workflow run | a structural decision; the key's default stays 5 |

## [answers] The owner's answers, 2026-10-19

The owner asked, "put the forks to me", and answered them in seven batches, each question with its recommendation
first. The owner's words, verbatim:

| Fork | The owner's answer |
|---|---|
| NT-1 | "Registered kind (Recommended)" |
| NT-2 | "Scout, rechecked (Recommended)" |
| NT-3 | "Yes, scoped (Recommended)" |
| NT-4 | "Additive auto (Recommended)" |
| NT-5 | "Loop proposes (Recommended)" |
| NT-6 | "Design-only scenario (Recommended)" |
| NT-7 | "Union, refuse conflicts (Recommended)" |
| NT-8 | "Stages as data (Recommended)" |
| NT-9 | "Swap or exclude (Recommended)" |
| NT-10 | "Measured shape now (Recommended)" |
| NT-11 | "Per unit in Build (Recommended)" |
| NT-12 | "Effort is an owner-controlled setting, and it's possible for the owner to set and run it at low. By default, effort is medium and agents do NOT go below medium without an explicit owner authorization." |
| NT-13 | "Off; on in strict (Recommended)" |
| NT-14 | "Text in git now but cloud relational db needs to be an accounted extension - multi-node concurrent builds are on the map and memory architecture needs to be ready to account for real-time memory sharing." |
| NT-15 | "SQLite per node (Recommended)" |
| NT-16 | "Ref per session (Recommended)" |
| NT-17 | "Every item by default, every tool call is settable by policy" |
| NT-18 | "Keyed registers (Recommended)" |
| NT-19 | "settable by policy, every pass commit by default. This creates a question of contention and gate runs." |
| NT-20 | "Yes, by unit lease (Recommended)" |
| NT-21 | "Intake + work order (Recommended)" |
| NT-22 | "Plus per-cap pins" |
| NT-23 | "Shown, priced, trended (Recommended)" |
| NT-24 | "No, retire it (Recommended)" |
| NT-25 | "Range minus gated (Recommended)" |
| NT-26 | "Scout by intent, if earned (Recommended)" |
| NT-27 | "Runtime key, 3 scopes (Recommended)" |
| NT-28 | "Any count by a policy write, raise default cap to 6, a need a mechanism to maintain a queue of agents/workflows instead of simply refusing." |

Twenty-two took the recommendation. NT-22 took another listed option, and five answers are the owner's own words:
- **NT-12.** Effort is the owner's setting: medium by default, and no agent goes below medium without the owner's
  explicit authorization. It replaces the recommended rule that an experiment record must justify a lower effort.
- **NT-14.** Text in git stays the record now, and a cloud relational database becomes an accounted extension, so
  memory is ready for real-time sharing across nodes.
- **NT-17.** `mailbox.notice` defaults to every item, and every tool call stays a value the owner's policy may set.
- **NT-19.** `build.push` defaults to every pass commit, settable by policy. The owner's question on contention and
  gate runs, answered from the tree: a build branch has one writer, a unit branch one each, and a push of a branch
  other than the default one skips the bar (110 pushes, median 0.44 s), while remote CI runs only on `main`. The one
  real contention was the lander's lock, which a push no longer takes.
- **NT-22.** Every size cap sits under the one switch, and the owner may pin named caps to refuse.
- **NT-28.** The limit takes any count by a policy write and defaults to 6, and a spawn over it waits in a queue
  instead of being refused.

## [answers-folded] Where the answers went, 2026-10-19

- **Every pending marker** in v2 and the layer records now reads "the owner's NT-x".
- **NT-12:** dBoundRoles' clause and the two `roles.effort.*` rows. No role declares an effort below medium today:
  the roles kit's default is medium, and its roles run at medium, high or xhigh.
- **NT-14:**
  - a change feed in dPlacedRequest, which dTotalRecall's record writes and dKeptSession's mail writes join;
  - the memory-mirror point in dWellOiledMachine and Runtime's `[extend]` table;
  - `memory.mirror`, which presets never touch;
  - the database itself in v2's `[planned]`;
  - the memory plan's pockets for the feed, the mirror and point 4's two registers;
  - `gap-mem-46`.
- **NT-17:** `mailbox.notice`'s default and presets, dKeptSession's clause and coordination's item 7.
- **NT-19:** `build.push`'s default and presets, and dWellOiledMachine's clause, a push now free of the lander's lock.
- **NT-22:** `budgets.pinned`, which presets never touch, and dGroundRules' clause and witness.
- **NT-28:**
  - `runtime.agents-in-flight` at 6;
  - the admission queue in dWellOiledMachine;
  - layer-runtime's attended entry and `in-flight` fixture, which now queue;
  - `gap-rt-36`.
- **The review's leftover.** `[p5-caps]` still listed `record` among `budgets.enforce`'s values, which the review had
  dropped. It is corrected.
