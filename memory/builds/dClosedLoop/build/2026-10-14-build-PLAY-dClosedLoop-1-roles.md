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
