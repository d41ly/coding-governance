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
2. **The driver hands the prompt writer the item's resolved work order**: the item's definition and
   acceptance, its inputs as keyed handed content with a reference only for optional depth, its
   allowance, and the actor's return template (layer-roles `[trust]` 1, R3-E).
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
needs is in a record its work order hands it.

Revised: 2026-10-16, after the roles layer's two Tier-2 rounds
(`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md`, `[revised]`): steps 2 and 4 hand content,
not references. The prompt writer frames a work order already resolved, and the executor wraps that
framing in it.

## [steps] Each step as a sequence of role items

Revised: 2026-10-16: the role-to-step relation is now derived from the step definitions
(layer-roles `[matrix]`), and this table stays as the record of the flow revisit that produced it.

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

Each role works from what its work order hands it and writes only its own class. A build moves
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

## [forks] Asked, 2026-10-15

**FR-1 (H1). "Your plan ratification is the mandate for every unattended step after Plan, so it must
be witnessed, never relayed by an agent. How is it witnessed by default?"** Offered: Your words,
hook-recorded (Recommended); A terminal command; A signed commit. Answer, in the owner's words:
"Starting a session and requesting a build _is_ ratification. Hook-recorded keywords can be an
owner-adjustable option."

**FR-2 (H3). "After ratification, where does the executor run the unattended steps by default?"**
Offered: The ratifying node, background (Recommended); The OS scheduler; A cloud routine. Answer, in
the owner's words: "The ratifying node, background by default, but each option is owner-adjustable."

**FR-3 (H12). "How should you hear about unattended progress by default?"** Offered: On park and on
landing (Recommended); At every transition; Only on park. Answer, in the owner's words: "As it is now -
microformats at the end of each turn. Each option is owner-adjustable."

**FR-4 (H15). "Mid-run, a role needs your answer (a planner's scope question, a fork the goal cannot
survive) while you are away. What happens by default?"** Offered: Park the item, continue the rest
(Recommended); Park the whole build; Stop the run. Answer, in the owner's words: "An agent makes the
best possible effort to resolve the fork and records it. Builds DO NOT get parked on the unresolved
fork pretext."

### Settled after FR-1 to FR-4, 2026-10-15

- **The owner's request is the ratification** (`plan.ratification`, default `request`). Starting a
  session and requesting a build is the mandate. Its witness is the request itself, written verbatim
  by the prompt-submit hook, so H2's hook is now load-bearing. A hook-recorded keyword, a terminal
  command or a signed commit are the allowed alternatives. Plan's item 10 is witnessed by the intake
  record; there is no separate ratification turn. Where `autonomy` keeps the owner's gate at Plan,
  that gate is met as `plan.ratification` says.
- **The executor runs on the node where the request was made, in the background** (`run.host`,
  default `requesting-node`, with `os-scheduler` and `cloud-routine` allowed); its liveness is its
  build lease's beat.
- **Progress reaches the owner as today: the micro-format lines that end each turn** (`notify.owner`,
  default `turn-micro-formats`, with `park-and-landing`, `every-transition` and `park-only`
  allowed). Nothing pushes a notification by default.
- **A build never parks on an unresolved fork** (`run.on-owner-question`, default
  `best-effort-recorded`, with `park-item`, `park-build` and `stop-run` allowed). The role that meets
  the fork resolves it with its best effort under the decision principles, and records the options,
  the choice and the reason. This holds for a question that would otherwise go to the owner, and, as
  read here, for a fork the goal cannot survive: the planner's plan revision proceeds under the
  request's mandate and is recorded for the owner. That reading awaits confirmation.

### Follow-ups asked, 2026-10-15

**FR-5 (H6). "Units with disjoint write sets build in parallel, but in the one shared worktree you
chose as the default, two builders contend for git's index lock. What should the default be?"**
Offered: Shared, commits queued (Recommended); Own worktree when parallel; Always one per unit.
Answer, in the owner's words: "Shared, commits queued but 'own worktree' as an owner-adjustable option
per adopter."

**FR-6 (H7). "Every landing on a node needs that node's primary tree, so two builds landing at once on
one node collide. What should the default be?"** Offered: A node landing lease (Recommended); Land
from the build's worktree. Answer, in the owner's words: "Turnstile landing queue already exists in the
repo. Tooling that changes how the product operates and its mechanical processes is to be reviewed at a
later step."

**FR-7 (H13). "A build that depends on another could reach Deploy before its parent has landed. What
should the default be?"** Offered: Hold the dependent's landing (Recommended); Let its Test decide.
Answer: Hold the dependent's landing (Recommended).

**FR-8 (H5, H9). "Messages that arrive mid-step, such as an amendment from another session or a
parent's breaking change, wait hours if the mailbox is read only at transitions. What should the
default be?"** Offered: Every item, plus an intake kind (Recommended); Transitions only, as settled;
Every item, amendments at transitions. Answer: Every item, plus an intake kind (Recommended).

### Settled after FR-5 to FR-8, 2026-10-15

- **Parallel units share the build's worktree, their commits queued by the executor** so the index
  lock never collides; `build.worktree` keeps `shared` as its default, and a unit's own worktree stays
  an allowed value each adopter can choose.
- **Landings on a node pass through the turnstile landing queue that already exists.** How that
  tooling fits the new architecture is reviewed at the lower-level step, with the other mechanical
  processes. Revised: 2026-10-16: no landing queue exists. The turnstile is the host-wide bar
  semaphore, and `push-main.sh` never takes it, so dShippedRelease builds the queue (`gap-flow-08`).
- **A dependent build's landing waits for its parent's** (`deps.landing`, default
  `hold-until-parent-lands`, with `test-decides` allowed).
- **The executor reads the build's mailbox at every item boundary** (`mailbox.reads`, default
  `every-item`, with `transitions-only` and `every-item-amendments-at-transitions` allowed), and the
  message kinds gain `intake`, which carries an amendment from a session that does not hold the
  build's lease to the session that does.

### Last round, asked 2026-10-15

**FR-9 (H8). "Units created from a closing review's findings are built after that review. Does the
closing review run again over them by default?"** Offered: Follow-up rounds while they find
(Recommended); One closing review per build; Only after a HIGH finding. Answer, in the owner's words:
"Only after a HIGH finding but it's an owner-adjustable setting per adopting repo - either option
should be available."

**FR-10 (H16). "The prompt writer precedes every role dispatch. When a step sends several workers of
one role at once (five spec writers, say), how many prompt-writer calls by default?"** Offered: One
per batch (Recommended); One per task. Answer: One per batch (Recommended).

**FR-11 (H2, H10, H11, H14). "Which of these mechanical resolutions do you accept as proposed?"**
Offered, multi-select: H2 Intake by hook; H10 Back-steps recorded; H11 Core checks at Build's exit;
H14 Fresh session in the worktree. Answer: all four.

**FR-12. ""Builds DO NOT get parked on the unresolved fork pretext." Read here: even a fork the goal
cannot survive is resolved by best effort, and the planner's plan revision proceeds under your
request's mandate, recorded for you. Is that right?"** Offered: Yes, even goal-level forks
(Recommended); Goal-level forks still wait. Answer: Yes, even goal-level forks (Recommended).

### Settled after the last round, 2026-10-15

- **A follow-up closing review runs only after a HIGH or BLOCKER finding** (`review.follow-up`, default
  `after-high`, with `while-finding` and `never` allowed per adopting repository).
- **One prompt-writer call composes each batch of same-role tasks** (`prompts.batch`, default
  `per-batch`, with `per-task` allowed); each task remains its own prompt, hashed on its own.
- **H2**: the prompt-submit hook writes each of the owner's prompts verbatim to the session's intake log,
  the witness for intake and, under `plan.ratification: request`, for the mandate.
- **H10**: backward transitions (Test to Build, Build to Design) are recorded like forward ones; only
  Plan is never re-entered.
- **H11**: the executor runs the core checks, cheap and leg-free, at the Build-to-Test transition.
- **H14**: until the card-import fixture passes, `next` recommends restarting in the build's worktree.
- **No fork parks a build, a goal-level one included**: the planner's plan revision proceeds under the
  request's mandate, recorded with its evidence for the owner.

## [closed] Every hole, settled

| Hole | Settled by |
|---|---|
| H1 ratification's witness | FR-1: the request is the ratification, witnessed by the hook |
| H2 verbatim intake | FR-11: the prompt-submit hook |
| H3 the executor's host | FR-2: `run.host` |
| H4 actors per item | the roles layer's item map |
| H5 an amendment without the lease | FR-8: the `intake` message kind |
| H6 parallel units in one worktree | FR-5: commits queued; own worktree allowed |
| H7 the primary tree at landing | FR-6: a landing queue, which dShippedRelease builds (`gap-flow-08`; revised 2026-10-16, since none exists); tooling reviewed later |
| H8 review of review-born units | FR-9: `review.follow-up` |
| H9 when the mailbox is read | FR-8: `mailbox.reads` |
| H10 backward transitions | FR-11 |
| H11 Build's core check | FR-11 |
| H12 telling the owner | FR-3: `notify.owner` |
| H13 a dependent's landing | FR-7: `deps.landing` |
| H14 a session moving into its worktree | FR-11 |
| H15 an owner question mid-run | FR-4 and FR-12: `run.on-owner-question` |
| H16 prompt-writer calls per batch | FR-10: `prompts.batch` |

