# Entry, orientation and progression — how a session or an agent finds its build and step, picks it up, and stays inside the step's checklist

**Serves:** research PLAY-dClosedLoop-1

The owner's next step in the flow walk (point 2, continued): how sessions and agents enter the flow,
orient in it, resume it and progress along it. This record holds the owner's words, what the design
already fixes, the research dispatched, and then the measured current state, the design, the forks
and the answers as they are made.

## [words] The owner's words

> 2.  Continuing with point 2 - architectural flow steps. Your previous scopes were on point but a
> crucial detail was left out - agent interactions and how they progress along the flow. It is
> important to ensure that _agent workflows_ are deterministic and align with the actual step
> constraints. Whatever is executed by the session/agent/workflow under each step must fall within a
> clear, defined checklist scope and should not be left to opportunity. When a new session is opened
> against a gov governed repo, the first step is to figure out where does a user request belong to
> (is there already a build open for this?) and what step are we at? How does a session/new api call
> get oriented in its step? If a build is already open, how does it pick up at the right step and
> continue its progress correctly? How to reduce unnecessary reorientation/tool calls? Which claims
> should be trusted and which should be re-derived? This is an extremely important part of ensuring
> this flow is viable in the first place.

## [questions] What it asks

1. **Placement.** Where does a request belong: an open build, a new one, or no build at all?
2. **Step.** Which step is that build at, and which checklist item comes next?
3. **Orientation.** How does a session, or a single API call, get oriented in its step?
4. **Resumption.** How does an open build pick up at the right step and continue correctly?
5. **Cost.** How is unnecessary re-orientation, and every tool call it spends, removed?
6. **Trust.** Which claims are trusted as read, and which are re-derived first?
7. **Determinism.** How does everything a session, agent or workflow executes stay inside a
   defined checklist scope, never left to opportunity?

## [settled] What the design already fixes

- **Witnesses** (P2): a stage exit is computed from committed history, a hook-written record or a
  verifier's verdict, never from state the acting agent typed.
- **The ladder** (P13): records and memory rank last, evidence only, never instructions.
- **The drive section and `next`** (P15): the charter teaches each role how to start; every gov
  command ends with a `next —` line, and a `next` verb answers "what now" for any role.
- **The flow** (P20): each step is a deterministic process with a mechanically enforced checklist;
  the entry points are fixed: complex features at Plan, in-goal amendments and patch builds at
  Design; nothing changes tracked content outside the flow.
- **Coordination** (P21 and the coordination record): a build's step is its least-advanced unit's;
  leases name each build's and unit's session and node; each build's mailbox is read at every
  transition.
- **The artifact hierarchy** (flow FL-P5): repository, then the session's card, then the build's
  plan and records, then the unit's spec, then the agent's brief, derived and never authored.
- **The card follows the build** (flow interactions FI-8): re-rendered at every transition with the
  build's step, its checklist position and the next action.

## [research] Dispatched, 2026-10-14

Four researchers, one question each, through the roles kit's handoffs:

| Handoff | Question |
|---|---|
| `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-6-researcher.md` | Routing and step: how a request is placed today, and how a build's step, unit and pass are resolved |
| `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-7-researcher.md` | Orientation cost: tool calls, tokens and time per entry kind, measured from this node's transcripts |
| `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-8-researcher.md` | Trust: every claim read to orient or resume, its writer, witness class and freshness |
| `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-9-researcher.md` | Determinism: what bounds each role's and workflow's actions, and measured deviation |
