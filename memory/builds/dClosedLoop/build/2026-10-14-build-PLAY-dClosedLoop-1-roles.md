# Roles — the third layer: deterministic workers, their static instructions and their tasks, mapped to the flow's steps

**Serves:** research PLAY-dClosedLoop-1

The owner's third layer, after the charter's instructions and the DLG steps. This record holds the
owner's words, what the layer must answer, the research dispatched, and then the measured current
state, the design, the forks and the answers as they are made.

## [words] The owner's words

> 3. We will revisit the [2. Architectural Flow Steps] later to polish once more given more
> consolidated detail from points 1-3 altogether. Let's drill down into the lower level for now -
> ROLES, which follow the steps. So far we went though 1. CHARTER INSTRUCTIONS (instructions that are
> ingested in any session/api call governed by GOV from the first request and their hierarchy); 2.
> ARCHITECTURAL (DLG) STEPS (DLG - Development Lifecycle Governance, process architecture that Gov
> introduces and governs in any repo it's adopted to - Gov's primary function); now we're designing
> the implementation of 3. ROLES - deterministic agents, their instructions, behavior, and
> interactions with each other between the FLOW STEPS. These three layers define the higher-level
> principles of this product - what it does and the principle that drives its objective from start to
> finish. ROLES already exist in the repo - these are unique, specific definitions for agents (jobs)
> that perform a certain function - session orientation, research and planning, reuse discovery,
> feature architecture and design, prompt writing, specification writing, code building, testing,
> deployment and maintenance, and various review processes across each of the DLG steps. Important -
> each of the roles and their interactions between each others (driven by the main session) should be
> thoroughly mapped out to the architectural DLG steps. Each role should be treated as an 'individual
> worker' with their static 'system instructions' (that define what the role entails and its scope
> limitations) and 'tasks' that're given to them throughout the session. Key feature of this product -
> functions driven by the 'roles' (or jobs) should not be allowed outside of these oriented agents.
> We're defining a deterministic systemic loop: 'Instructions (1.)' -> 'Flow Step (2.)' -> 'Roles
> (3.)'. It's an environment where trusted workers work through the looped steps by receiving and
> exchanging instructions depending on what step they are on.

## [layers] The three layers, as the owner set them

1. **Charter instructions**: what any session or API call governed by gov ingests from its first
   request, and their hierarchy (foundations step 1; the ladder, with the build's card at rank 1).
2. **The DLG steps** (Development Lifecycle Governance): the process architecture gov introduces and
   governs in every repository that adopts it, gov's primary function (the flow record).
3. **Roles**: deterministic agents, their instructions, their behaviour, and their interactions
   between the flow's steps.

Together they form one loop: instructions, then the flow step, then the roles. The owner will revisit
layer 2 once all three are consolidated, so the session model's holes, H1 to H14, wait for that
revisit.

## [asks] What this layer must answer

1. **Anatomy**: a role as an individual worker, with static system instructions that define its job
   and its scope limits, and tasks handed to it through the session.
2. **Roster and mapping**: a role for every function the owner listed (session orientation, research
   and planning, reuse discovery, feature architecture and design, prompt writing, specification
   writing, code building, testing, deployment and maintenance, and every step's review), each mapped
   to the checklist items it performs.
3. **Exclusivity**: a role's function is never performed outside an agent oriented in that role.
4. **Interactions**: how roles receive and exchange instructions from step to step, driven by the
   main session.
5. **Trust**: what makes each worker trusted.

## [research] Dispatched, 2026-10-14

Four researchers, one question each, through the roles kit's handoffs:

| Handoff | Question |
|---|---|
| `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-11-researcher.md` | Anatomy: each role's static instructions, its task, its allowance, and what enforces each |
| `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-12-researcher.md` | Coverage: every step's checklist items against today's roles, and role work done outside a role |
| `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-13-researcher.md` | Interactions: every hop between roles, its medium, and how it fails |
| `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-14-researcher.md` | Prior art: how other multi-agent systems define deterministic role workers, and what fits gov |

The returns are recorded verbatim beside this record:
`build/2026-10-14-build-PLAY-dClosedLoop-1-research-roles-{anatomy,coverage,interactions,priorart}.md`.
The main loop checked each return's load-bearing citations against the tree; every one held.

## [current] The current state, measured 2026-10-14

**Roles cover a sliver of the steps.** Of the 70 checklist items across the seven steps, 11 are
performed by a role today, 18 by the main session, 9 by a command and 32 by nobody. No role exists
for planning, feature design, testing, deployment or maintenance, or for the Plan, Test, Deploy and
Loop reviews. Three roles saw no spawn in 60 days: the orienter, the reuse scout and the diff
reviewer.

**The main session does role work.** In 60 days it wrote or edited specs 605 times across 233
files, product code 565 times, folded review findings into specs 367 times, and wrote plans 336
times and task briefs 74 times. Since the role arm landed on 2026-10-12, spec and product writes
from untyped agents have stopped (0), but the main session's shell still wrote into role paths 85
times, and typed roles' shells 66 times.

**Inside a role, roles behave.** Over 142 typed transcripts and 7,425 tool calls, no role made a
Write or Edit outside its tools, and the read-only roles made no live commit. The published
taxonomy of multi-agent failures agrees: disobeying a role specification is 1.5% of failures, while
step repetition (15.7%) and not knowing when to stop (12.4%) lead. The problem is role work outside
roles, and transitions chosen by an agent instead of code.

**A role's limits are prose.** The role bodies state 59 prohibitions, and 1 names the check that
enforces it. `writes` is a class, not an allowance: any routed path is open while any unit is
buildable. The index the hooks trust, `.claude/roles.json`, and the agent files sit outside every
role gate, so a role holding Write could edit them. `role-sha` is never compared with the role.

**Exchanges are retyped by the main session.** 64.5% of a rendered task's bytes are free text the
main session typed; 71 of 126 direct spawns carried a free-text prompt; 258 of 449 workflow calls
were inline scripts; and 844 of 901 spec fold commits came from no unit. Direct-spawn returns are
free text in 48 of 48 cases, while harness returns are structured in 94 of 94. A builder's
divergence goes back to "the caller", and nothing routes it.

## [design] Roles as bound workers, as proposed

Every researcher's surviving candidate is one architecture seen from four sides:
- **Anatomy**: a static role plus a per-item work order.
- **Coverage**: item-bound actors.
- **Interactions**: an executor hub with typed records.
- **Prior art**: a program-driven graph, as in LangGraph's coded edges, MetaGPT's SOPs and CrewAI's
  tasks.

The owner's words settle two choices without a fork:
- Interactions are "driven by the main session", so roles exchange work through it, never with each
  other.
- Role functions "should not be allowed outside of these oriented agents", so the main session drives
  and does no role's work.

### [model] A worker, a task, a driver

- **A role's static instructions** are its system prompt, rendered from the roles kit at rank 5: its
  job, its scope limits (each paired with the check that enforces it), its ceiling (tools, write
  classes, gate legs), the charter practices it binds, and its typed return. They never change
  within a session, and its identity is keyed: `role-sha` is compared with the rendered role at
  every spawn.
- **A task is a work order** rendered from the checklist item, at rank 6:
  - the item and its step, build and unit;
  - its inputs, as references to fields of earlier records at their source SHAs;
  - its allowance: the role's ceiling narrowed to the item, for example the unit's write set;
  - its return schema, and the witness the driver will resolve.
  
  The work order is hashed into the spawn marker, and the agent's calls are bound to it through the
  agent id the platform supplies.
- **The driver** is the main session when attended, and the executor when not:
  - it runs `next`, places requests, dispatches each item to its actor, and validates returns;
  - it resolves witnesses, records transitions and asks the owner;
  - it does no worker's job, its own writes are limited to intake, transition and bookkeeping
    records, and only read-only probes are free.

### [roster] The proposed roster

| Role | Job | Never | Ceiling | Returns | Status |
|---|---|---|---|---|---|
| gov-planner | drafts the plan record and the Plan reach; triages what no rule decides | chooses a mechanism, splits units, writes code | read tools; writes the plan record | plan fields, research requests | new |
| gov-researcher | answers one question with candidates and the test that could make each lose | writes files, decides | read tools, web; writes none | a typed research record | kept, return typed |
| gov-reuse-scout | finds the seams a mechanism should extend, each with its probe's digest | designs, writes | read tools; writes none | seams and digests | kept, return typed |
| gov-architect | decomposes a build into features and units; declares interfaces, order and write sets; resolves feature forks | writes unit specs or code | read tools; writes feature designs | roster, feature designs, fork records | new |
| gov-spec-writer | writes each unit's structured spec, including units born of findings and re-designs, and folds audit findings into a new revision | edits a built unit's spec; writes code | read tools; writes specs | spec path and SHA | kept |
| gov-builder | builds one unit from its spec and records its acceptance | edits a spec; runs gate legs; writes outside its write set | read, write, edit; product inside the item's write set; the naming lexicon | committed or diverged, as an enum; SHA; checks run | kept |
| gov-tester | attributes each red of a verdict and names its route; files reported reds | fixes code; re-runs the bar | read tools; writes asks | per red: class, route, evidence | new |
| gov-deployer | writes release notes from the landed units; disposes a release verify that needs judgment | lands or pushes by hand; changes code | read tools; writes notes | notes, verify dispositions | new |
| gov-maintainer | turns detector readings into filings: severity, acceptance, patch-build intakes | changes tracked content directly | read tools; writes asks and intakes | filings | new |
| gov-reviewer | reviews one pinned artifact through one lens: plan, specs, diff, gates, landing, maintenance run | edits what it reviews | read tools; writes none | findings | merges the spec and diff reviewers |
| gov-skeptic | tries to refute each finding | adds findings | read tools; writes none | verdicts | kept |
| gov-synthesizer | merges the verified findings into one report | changes a verdict | read tools; writes the review report | report path | kept |
| gov-loop-reviewer | reads the loop's metrics and drafts proposals | changes a gate, rule or cap itself | read tools; writes none | proposals | new |

The orienter and the session-handoff template are left out of the table on purpose. Session
orientation and prompt writing are both in the owner's list, and where each lives is asked below.

### [map] Every checklist item, mapped to its actor

A command is code the driver runs, needing no model; the owner and the driver are named where they
act. Where a review runs, the reviewer, skeptic and synthesizer act as the stage-review checklist
says.

| Step | Item | Actor |
|---|---|---|
| Plan | 1 intake recorded verbatim | command (session-model hole H2) |
| | 2 duplicates and overlaps | command |
| | 3 triage | command by rule; planner where no rule decides |
| | 4 disposition | driver (placement) |
| | 5 the plan record | planner |
| | 6 each practice's Plan reach | planner |
| | 7 plan view and placement predicate | command |
| | 8 build lease | command |
| | 9 review recommendation; review where owed | command scores, driver reasons; review roles when run |
| | 10 ratification | owner |
| | 11 transition | command |
| Design | 1 input recorded | command |
| | 2 reuse and precedent probes | reuse scout |
| | 3 features, units, order, write sets, interfaces | architect |
| | 4 each unit's spec | spec writer |
| | 5 each practice's Design reach | spec writer |
| | 6 forks resolved | architect (feature), spec writer (unit); researcher where a fact decides |
| | 7 overlaps acknowledged | command finds; spec writer acknowledges |
| | 8 recommendation; spec audit where owed, folded | command and driver; review roles; spec writer folds |
| | 9 every unit derived READY | command |
| | 10 transition | command |
| Build | 1 base and mandate | command |
| | 2 unit leases and write sets | command |
| | 3 passes | builder |
| | 4 acceptance observations | builder |
| | 5 bug-class trailer | builder |
| | 6 divergence back to Design | driver routes the enum; spec writer or architect |
| | 7 scope check | command |
| | 8 closing review; findings disposed | review roles; command disposes by policy; spec writer specs new units |
| | 9 no core red | command |
| | 10 transition | command |
| Test | 1 tree fixed | command |
| | 2 legs and levels selected | command |
| | 3 the bar and its verdict | command |
| | 4 reds attributed, routed, filed | tester |
| | 5 flakes | command |
| | 6 seen-red records | command |
| | 7 recommendation; gate review where owed | command and driver; review roles |
| | 8 transition | command |
| Deploy | 1 verdict current | command |
| | 2 landing authorized | command |
| | 3 lander | command |
| | 4 landing record | command |
| | 5 kit versions and release notes | command mints; deployer writes notes |
| | 6 promotions and verifies | command; deployer where a verify needs judgment |
| | 7 a failed verify, by policy | command; deployer records the disposition |
| | 8 recommendation; landing review where owed | command and driver; review roles |
| | 9 leases released | command |
| | 10 transition | command |
| Maintain | 1 maintenance lease | command |
| | 2 detectors | command |
| | 3 cadence test levels and held legs | command runs; tester attributes and files |
| | 4 safe fixes; tracked ones as patch builds | command applies; maintainer opens the intakes |
| | 5 breaches filed | maintainer |
| | 6 tagged release | command cuts; deployer writes notes |
| | 7 adopter currency | command |
| | 8 maintenance record | command |
| | 9 lease released | command |
| Stage review | 1 trigger | command |
| | 2 artifact pinned | command |
| | 3 lenses | reviewer |
| | 4 refutation | skeptic |
| | 5 report | synthesizer |
| | 6 disposal and left-shift | command by policy; spec writer for new units |
| | 7 cost to the value ledger | command |
| Loop Review | 1 cadence lease | command |
| | 2 metrics | command |
| | 3 proposals | loop reviewer |
| | 4 proposals filed and ratified | command; owner as `review.loop.retire` says |
| | 5 record | command |

### [exchange] How workers exchange instructions

- **Every exchange is a typed record routed by the driver.** A worker returns a typed record. The
  driver validates it, persists it with its hash, and renders the next work order from its fields.
  Workers never message each other, and nothing is retyped between them. Free text enters a work
  order only as the owner's own words.
- **A worker that needs another worker asks in its return.** For example, the planner returns a
  research request with its question. The driver dispatches the researcher, then hands the record
  back.
- **Every route back is an item.** A divergence routes by its enum, to the spec writer or the
  architect. A fold is a spec-writer revision that the next audit round re-reviews. Findings become
  new units by policy.
- **Across builds, sessions and nodes, drivers talk** through the build's mailbox (the coordination
  record). Workers never do.

### [guard] How exclusivity holds

1. **By construction.** Every role function is an item with one actor, and the driver dispatches
   only that actor. With no item, there is no role work.
2. **At the tool call.** Writes are checked against the work order's allowance, Bash writes included.
   The driver holds no worker's write class. A spawn is admitted only for the item's role, with its
   work order and a `role-sha` that matches. A tree with no role index is refused, never left
   unarmed.
3. **At the return.** A subagent-stop check validates the return against the work order's schema,
   with a bounded retry. The driver then resolves the witness before any item depends on it.
4. **After the fact.** The transition verifier reads git and the transcripts, and refuses a
   transition over any act outside an allowance.

Role definitions, the role index and the agent files sit outside every worker's reach. They change
only through the roles build's own units, under the owner's guard.

### [trust] Why a worker is trusted

A worker is trusted because it is constrained and checked, not because it is believed:
- its identity is rendered and keyed;
- its static instructions come only from the kit;
- its allowance is enforced at every call;
- its return is validated;
- each claim it makes is witnessed before anything depends on it.

### [gaps-proposed] Gaps to register once the roster's home is settled

1. HIGH. Of 70 checklist items, 11 have a role performer. The steps lack roles for planning, feature
   design, testing, deployment, maintenance and four reviews.
2. HIGH. The main session performs role functions: specs, product code, folds, plans and briefs.
3. HIGH. Role limits are prose: 58 of 59 prohibitions name no enforcer. `writes` is a class, not an
   allowance, and shell writes escape every role gate.
4. HIGH. Direct-spawn returns are free text (48 of 48); `returns` is prose nothing reads; no
   subagent-stop check exists.
5. HIGH. Exchanges are retyped by the main session: 64.5% of task bytes, and 844 of 901 fold commits.
6. HIGH. The guard shares state with what it guards: the role index sits outside every role gate,
   and a tree with no index is unarmed.
7. MED. Roles go unused or double up: three roles had no spawn in 60 days, and the spec writer also
   holds disposal.
8. MED. The work order names no checklist item, allowance or witness key, and a builder's divergence
   has no route back.

## [forks] Asked, 2026-10-14

**RL-1. "Every step's review needs a reviewer. Should one reviewer role cover them all, with the lens
set by the step's artifact (plan, specs, diff, gates, landing, maintenance run), or should each have
its own?"** Offered: One reviewer, lens per step (Recommended); One reviewer per step; Keep two, add
four. Answer, in the owner's words: "Which setup is better? Doesn't seem that having more than a single
reviewer role is actually beneficial - what matters is the instructions given and the way their task
is explained." The main loop's reply: one reviewer is better. Its job is the same at every step, to
hunt defects in one pinned artifact; what differs per step is the lens and the artifact, and both
belong in the task. Two reviewer roles exist today and one had no spawn in 60 days; the published
failure taxonomy finds disobeyed task specifications (11.8%) far more often than disobeyed roles
(1.5%).

**RL-2. "Test, Deploy and Maintain are mostly commands, with a few items that need judgment:
attributing reds, release notes and verifies, filing breaches. How many roles carry that
judgment?"** Offered: Three: tester, deployer, maintainer (Recommended); One operations role; Tester,
plus one for release and upkeep. Answer: Three: tester, deployer, maintainer (Recommended).

**RL-3. "Session orientation is in your list of role functions. With `next` and the build's card now
orienting every session, where should it live?"** Offered: Commands only (Recommended); Keep the
orienter role. Answer, in the owner's words: "No sessions should orient inline, that's one of the major
points. Upon a new user session being started, orientation should be handled by a scout role workflow,
keeping any unnecessary tool output in the sidechain - outside the main session. Main session should
receive an extensive, fully composed orientation card with all the necessary scope details to continue
its session without the noise."

**RL-4. "Prompt writing is in your list too. Today 64.5% of a task's text is typed by the main
session. Who writes a worker's task?"** Offered: The requesting worker, rendered (Recommended); A
prompt-writer role. Answer, in the owner's words: "Main session's primary purpose is to ORIENT its
sidechain agents/roles - new prompt-writer roles receives only the details necessary to write a tight,
well-oriented prompt from the main session and passes it further along to its destination. Main
session, again, should keep as much of the noise out of its context as possible."

### Settled after RL-1 to RL-4, 2026-10-14

- **One reviewer role**, its lens and artifact set by the task: plan, specs, diff, gates, landing,
  maintenance run, and the loop's metrics. The loop reviewer folds into it, the synthesizer's report
  carrying the Loop Review's proposals; the skeptic and synthesizer stay shared.
- **Three operations roles**: tester, deployer and maintainer.
- **Orientation is a scout's workflow in a sidechain, never inline.** At session start an orientation
  scout (today's orienter, re-scoped) composes the card: the full kickoff where no READY card exists,
  a refreshed card where one does. The main session receives one extensive, fully composed card with
  every scope detail it needs, and none of the tool output that produced it.
- **A prompt-writer role writes every worker's task.** The main session's primary purpose is to orient
  its sidechains: it hands the prompt writer only the details the task needs, and the prompt writer
  composes a tight, well-oriented prompt that passes unchanged to its destination role, bound by the
  spawn marker's hash. The rendered work order (item, allowance, return schema, witness) stays
  mechanical around it. Today's session-handoff template folds into the prompt writer.
- **The main session keeps the noise out of its context**: it holds composed cards and typed returns,
  never the raw output that produced them.

### Follow-ups asked, 2026-10-14

**RL-5. "No session orients inline, and the main session keeps the noise out. Can the main session
still run read-only probes itself (file reads, greps, git commands)?"** Offered: None: probes go to a
scout (Recommended); Cheap state reads only; As settled before. Answer: Cheap state reads only.

**RL-6. "Where does the roles layer get built? Charter and flow each have a foundation build in the
chain (`dOrderedCharter`, `dDeclaredLoop`)."** Offered: Its own chain build (Recommended); Spread over
the step builds; Decide at the re-cut. Answer: Its own chain build (Recommended).

**RL-7. "A worker's return fails its schema. What happens by default?"** Offered: Retry up to 3, then
park (Recommended); Retry once, then park; Park at once. Answer, in the owner's words: "Retry up to 3,
then park by default. The number of retries is owner-adjustable. Why would a worker fail its schema in
the first place? Workers should be handed templates that structurally eliminate the possibility." The
main loop's reply: today's direct spawns are asked for their shape in prose, so 48 of 48 returned free
text, while harness spawns return through a schema-forced tool, 94 of 94 structured. A template filled
through that forced channel makes a format failure impossible by construction; what remains is a value
that fails to resolve, such as a claimed commit that does not exist, and the retries cover only that.

**RL-8. "A harness that cannot spawn subagents, or you working by hand, reaches an item a role must
perform. What happens by default?"** Offered: A role session the executor starts (Recommended); A
recorded stand-in, by waiver; Refuse. Answer, in the owner's words: "This possibility should be
mechanically and structurally eliminated - a built-in harness should be used that can ALWAYS spawn
subagents as necessary. This already exists in the repo, it should be improved to the new architecture
(this is a lower level design we haven't reached yet). Otherwise, a role session the executor starts."

### Settled after RL-5 to RL-8, 2026-10-14

- **The main session reads only cheap state** (`driver.reads`, default `state-reads-only`): `next`, a
  record it was handed, a short git state command. Anything exploratory is a scout's task. Workers keep
  their read-only probes inside their items.
- **The roles layer is built by its own chain build**, the third foundation beside the charter's and the
  flow's: `dBoundRoles`, child of `dDeclaredLoop`.
- **Returns are filled templates through a schema-forced channel**, so a format failure cannot occur. A
  value that fails to resolve is retried up to `roles.retries` times (default 3, any count the owner
  sets), then the item parks.
- **The no-spawn case is eliminated by construction**: the executor runs on a built-in harness that can
  always spawn subagents (the repository's workflow harness, improved to this architecture in the
  lower-level design). Where it is absent, the executor starts a role session for the item
  (`roles.no-spawn`, default `executor-role-session`).

### The roster, settled

| Role | Job | Never | Returns |
|---|---|---|---|
| gov-orientation-scout | composes the session's card in a sidechain at session start: the full kickoff where no READY card exists, a refreshed card where one does; composes a request's placement evidence | acts on the work it orients | the composed card; placement evidence |
| gov-prompt-writer | composes each worker's task from the main session's details and the records, a tight prompt passed unchanged to its destination | dispatches, or performs the task | the task prompt |
| gov-planner | drafts the plan record and its Plan reach; triages what no rule decides | chooses a mechanism, splits units, writes code | plan fields; research requests |
| gov-researcher | answers one question with candidates and the test that could make each lose | writes files; decides | a research record |
| gov-reuse-scout | finds the seams a mechanism should extend, each with its probe's digest | designs; writes | seams and digests |
| gov-architect | decomposes a build into features and units; declares interfaces, order and write sets; resolves feature forks | writes unit specs or code | roster; feature designs; fork records |
| gov-spec-writer | writes each unit's structured spec, including units born of findings and re-designs, and folds audit findings into a new revision | edits a built unit's spec; writes code | spec path and SHA |
| gov-builder | builds one unit from its spec and records its acceptance | edits a spec; runs gate legs; writes outside its write set | committed or diverged; SHA; checks run |
| gov-tester | attributes each red and names its route; files reported reds | fixes code; re-runs the bar | per red: class, route, evidence |
| gov-deployer | writes release notes; disposes a release verify that needs judgment | lands or pushes by hand; changes code | notes; verify dispositions |
| gov-maintainer | turns detector readings into filings: severity, acceptance, patch-build intakes | changes tracked content directly | filings |
| gov-reviewer | reviews one pinned artifact through the lens its task names: plan, specs, diff, gates, landing, maintenance run, the loop's metrics | edits what it reviews | findings |
| gov-skeptic | tries to refute each finding | adds findings | verdicts |
| gov-synthesizer | merges verified findings into one report; for the Loop Review, the proposals | changes a verdict | report path |

The main session is the driver, not a worker, and the executor drives when no one is attending. Every
row of the item map whose actor is a role is now dispatched through the prompt writer. The orientation
scout runs at session start, before Plan's first item. Loop Review item 3 is the reviewer with the
loop's lens, its skeptic and its synthesizer.

