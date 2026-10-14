# The flow revisited: how roles interact with and progress through the steps

**Serves:** research PLAY-dClosedLoop-1

The owner's revisit of layer 2 with layer 3 in place. This record defines one cycle every role item
follows, then each step as a sequence of role items with their routes, the chain of records that
carries work from step to step, and the owner's touchpoints. It ends with the holes the session model
left (H1 to H14), now that roles exist. It builds on the flow, flow-interactions, coordination,
orientation, session-model and roles records, and repeats none of their settled text.

## [words] The owner's words

> Let's revisit the 2. flow steps now and define how 3. roles interact with and progress through the
> steps.

## [cycle] The item cycle: one shape for every role item

1. **`next`** names the item and its actor.
2. **The driver hands the prompt writer the item's details**: the item's definition and acceptance,
   references to its input records, its allowance, and the actor's return template.
3. **The prompt writer returns the task prompt**, a record of its own.
4. **The executor wraps it in the work order** (the item, its allowance, its return template, its
   witness, the hashes) and spawns the actor in a fresh agent. The actor's static instructions load
   as its system prompt.
5. **The actor works inside its allowance** and returns its filled template through the
   schema-forced channel. A value that fails to resolve is retried up to `roles.retries`.
6. **The driver resolves the witness**, persists the return with its hash, reads the build's
   mailbox, and asks `next` again.

Every return template ends in an outcome from a closed set, and the driver routes on that outcome by
a table, never on prose. A role carries nothing from one item to the next: whatever a later item
needs is in a record its work order references.

## [steps] Each step as a sequence of role items

Item numbers are those of each step's checklist in the flow record. "Review roles" means the
reviewer with the step's lens, then the skeptic, then the synthesizer.

### Entry

| When | Actor | Receives | Returns | Then |
|---|---|---|---|---|
| a session starts or resumes | orientation scout | the session's tree, its leases, the remote's card refs | the composed card | rendered into the imported card file; the main session reads only the card |
| a request arrives and the session is unbound | orientation scout | the request, the plan view, the design index, the open asks | placement evidence | the driver places it, the disposition and its reason recorded, its facts checked |
| the disposition is `new`, or the placed build has no READY card | orientation scout | the placement, the kickoff manifest | the full kickoff's card: scope, reading, risks, bug classes | saved to the remote ref, the clone's cache and the imported file |
| the disposition is `none`, a question | orientation scout or researcher, as the question needs | the question | a typed answer | the driver relays it to the owner |

### Plan

| Item | Actor | Work order carries | Returns | Routes |
|---|---|---|---|---|
| 1 to 4 | commands; the driver places | — | intake, duplicates, triage, disposition | — |
| 5, 6 | planner | the intake, the triage, the duplicates, the owner's answers so far | the plan record's fields; research requests; owner questions | a research request goes to the researcher, then back to the planner; an owner question goes to the owner, or parks while the owner is away |
| on request | researcher | the planner's question | a research record | back to the planner's next revision |
| 7, 8 | commands | — | plan view; build lease | — |
| 9 | command scores, driver reasons; review roles when run | the plan record | findings, then a report | each finding becomes a planner revision; the review blocks the transition |
| 10 | owner | the plan record | ratification | the mandate |
| 11 | command | — | the transition | the card re-rendered; Design's input is the ratified plan record |

### Design

| Item | Actor | Work order carries | Returns | Routes |
|---|---|---|---|---|
| 1 | command | — | the input recorded | — |
| 2 | reuse scout | the plan's goal and scope; the map's dossiers | seams, each with its probe's digest | to the architect |
| 3 | architect | the plan record; the seams | features, units with order and write sets, feature designs with interfaces, fork records; research requests | a fact fork goes to the researcher, then back; a fork the goal cannot survive becomes a plan revision for the planner and the owner |
| 4 to 7 | spec writer, one per unit, in parallel up to the bound | the unit's row, its feature design and interfaces, the seams, the overlaps the design index finds | spec path and SHA; unit forks; overlap acknowledgments; Design reach | a unit fork that proves feature-level goes to the architect |
| 8 | command and driver; review roles when owed | the spec set at its revision | findings, then a report | each finding becomes a spec-writer revision, re-reviewed by the next round while rounds still find |
| 9, 10 | commands | — | derived READY; the transition | `confirmed` interfaces posted to dependent builds |

### Build

| Item | Actor | Work order carries | Returns | Routes |
|---|---|---|---|---|
| 1, 2 | commands | — | base; unit leases | — |
| 3 to 5 | builder, one per unit, in order; disjoint units in parallel | the spec at its SHA, the write set, the acceptance commands, the bug classes | `committed` with SHA and checks, or `diverged` as spec-wrong, interface-change or fork | spec-wrong goes to the spec writer (the unit is unbuilt); interface-change to the architect (feature re-entry); a fork by `design.forks`; then READY again and back to the builder |
| 6 | driver | — | the routes above | — |
| 7 | command | the commits; the write sets | the scope report | a stray path warns and files an ask |
| 8 | review roles, diff lens | the build's range | findings, then a report | `review.findings` disposes: the spec writer specs new units (built specs stay frozen), the builder builds them |
| 9, 10 | commands | — | core checks; the transition | — |

### Test

| Item | Actor | Work order carries | Returns | Routes |
|---|---|---|---|---|
| 1 to 3 | commands | — | the prepared merge; the selection; the hook-written verdict | — |
| 4 | tester | the verdict; the attribution labels; the diff; the specs | per red: its class, its route, its evidence | code misses its spec: a builder fix pass, back to Build; spec wrong: a new unit, back to Design; inherited: an ask; a merge conflict: a builder resolution pass, or the architect when an interface clashes |
| 5, 6 | commands | — | flakes; seen-red records | — |
| 7 | command and driver; review roles, gate lens, when owed | the verdict and the gates | findings, then a report | disposed as in Build |
| 8 | command | — | the transition | — |

### Deploy

| Item | Actor | Work order carries | Returns | Routes |
|---|---|---|---|---|
| 1 to 4 | commands | — | currency; the mandate; the landing; the landing record | a moved tip sends the build back to Test |
| 5 | command mints versions; deployer | the landed units' records | release notes | — |
| 6, 7 | commands; deployer where a verify needs judgment | the verify outputs | verify dispositions under `deploy.on-verify-fail` | — |
| 8 | review roles, landing lens, when owed | the landing record | findings, then a report | — |
| 9, 10 | commands | — | leases released; the transition | the build closes; `landed` goes to dependents; the card's terminal snapshot is committed |

### Maintain

| Item | Actor | Work order carries | Returns | Routes |
|---|---|---|---|---|
| 1, 2 | commands | — | the period lease; detector readings | — |
| 3 | commands; tester | the cadence levels' reds | attributions and filings | to Plan's triage |
| 4 | commands apply the untracked fixes; maintainer | the readings | patch-build intakes for tracked fixes | each to Design as a patch build |
| 5 | maintainer | the breaches | filings with severity and acceptance | to Plan's triage |
| 6 | command cuts the release; deployer | the release's units | release notes | — |
| 7 to 9 | commands | — | currency; the record; the lease released | — |

### Review

| Kind | Actors | Work order carries | Returns | Routes |
|---|---|---|---|---|
| a stage review | reviewer with the step's lens; skeptic; synthesizer | the pinned artifact | findings, verdicts, then a report | disposed by the step that owns the work, through `review.findings` |
| the Loop Review | reviewer with the loop's lens; skeptic; synthesizer | the metrics window | proposals, in the synthesizer's report | filed into Plan, ratified as `review.loop.retire` says |

## [records] How work progresses: records travel, roles do not

```text
owner's words ──► intake ──► plan record ──► seams ──► feature designs ──► specs ──► commits
(hook)            (command)  (planner)       (scout)   (architect)         (spec      and acceptance
                                                                           writer)    (builder)
                                                                                         │
   Plan's triage ◄── filings ◄── release notes ◄── landing ◄── attributions ◄── verdict ◄─┘
                  (maintainer)   (deployer)        (command)   (tester)        (hook)
```

Review reports, from the synthesizer, branch off every step and return as new units or asks.

Each role reads only what its work order references and writes only its own class. A build moves
because its records accumulate and `next` reads them; no worker remembers where the build is.

## [owner] Where the owner appears

- **Typing a request.** It is recorded by the hook, with no agent between the owner and the record.
- **Answering an owner question** returned by the planner or the architect: at once when attending,
  or later from a parked ask.
- **Ratifying the plan**, which is the mandate.
- **Asking for an amendment**: an intake, never a side task.
- **Reading a notification**, and the card at the next session.

## [holes] The session model's holes, with roles in place

- **Resolved by the roles layer:** H4. Every item now has its actor.
- **Asked below as forks:**
  - H1, ratification's witness.
  - H3, where the executor runs.
  - H12, telling the owner.
  - H6, parallel units in one worktree.
  - H7, the node's primary tree at landing.
  - H13, a dependent's landing.
  - H5 and H9, messages arriving mid-step.
  - H8, review of units born from a review.
- **Proposed for confirmation together:** H2, H10, H11 and H14.
- **New with roles, asked below:**
  - **H15:** an owner question raised mid-run while the owner is away.
  - **H16:** how many prompt-writer calls a step's batch of same-role tasks costs.
