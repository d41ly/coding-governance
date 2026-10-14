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

The returns are recorded verbatim beside this record:
`build/2026-10-14-build-PLAY-dClosedLoop-1-research-orientation-{routing,cost,trust,determinism}.md`.
The main loop spot-checked each return's load-bearing code citations against the tree before using
them here; every one held.

## [current] The current state, measured 2026-10-14

**Placement is the agent's unaided judgment.** Kickoff tells the agent to "DERIVE these fields
yourself" (`skills/session-kickoff/SKILL.md:126-131`); nothing matches a request against the live
builds or the asks. The route check verifies existence and pairing only, so a route to a terminal
build or to another session's build lands (`manifest-check.sh:995-1001`). An unattended run handed a
prompt always opens a new build (`tools/unattended/SKILL.template.md:28-32`). Placement cannot be
inferred from paths: the predecessor a README names ranked first 0 of 5 times, and 110 of 110 builds
that declare paths share one with a build live when they opened. Only 6 of 131 recent builds name a
predecessor, so a mis-placement cannot even be audited.

**The position is read from typed state.** A unit's step, order and pass come from status headers the
agent types and from RUN.md's `phase:`; the write gate admits on a typed INPROGRESS
(`tools/hooks/scratch-guard.js:796`). All 10 INPROGRESS units had been idle 8 days or more. No resolver
says which of the method's five pass kinds is due. `memory/LIVE.md` is byte-valid but inherits the typed
headers: 7 of 30 non-terminal headers sit under a build merged after they last changed. Derivation is
feasible: 1,187 of 1,244 CLOSED units have a commit naming them.

**Orientation is exploratory and costly.** Across 64 sessions on this node, a new session spent a
median 35 tool calls (p90 67) and 146k fresh input tokens before its first productive write. Of those
calls, 58% read content, 14% read method documents, 13% located the work, and 7% re-ran git state the
card had printed. Kickoff's Step 1 orders that re-derivation (`SKILL.md:49-56`): a median 6
card-answerable calls per session. READY reached the card in 19 of 64 sessions, 2 of them before the
first write. A resume spent a median 4 calls but 467k fresh input tokens, because the whole context is
cached again; a compaction spent a median 15 calls, 80% of them re-reading content. Briefed agents
spent 15% of their calls on method documents and 15% locating; agents read the charter 123 times and
their own prompt file 10 times.

**Claims carry no freshness keys.** The card's cells go stale unmarked: in this session the dirty
count went from 11 to 0 and the worktrees from 13 to 14. After this session's compaction, the replay's
`now —` line read the primary tree (`97e782d5 · main · clean`) instead of this session's worktree
(`f5fba66e0` on its own branch), because `derive_head_state` reads whichever tree the hook runs in
(`manifest-check.sh:499`, observed by the main loop). Run claims disagree with their RUN.md in 4 of 17
cases, and nothing joins them. `role-sha` is never compared with the role it was rendered from
(`tools/hooks/agent-cap.js:55-60`). The auto-memory loads unchecked: 12 of the 98 paths it names are
gone. Trusting by witness class alone fails, because hook-written cells go stale too; a key that
recomputes, with a floor on actor-typed sources, survived every test.

**Most work is bound to no step.** Of 28,727 main-loop tool calls, about 63% follow no protocol step:
ad-hoc shell probes alone are 40%. Typed role agents are 4.1% of subagents (116 of 2,800). The role-gate
arm let 34 typed gate runs through in the field, though a replay of the same commands is refused; the
cause is unknown. Bash writes never reach the write gate (`scratch-guard.js:83-86`), and the `none` and
`review` write classes are read by nothing (`:101-104`). One harness branch reads free text
(`tools/workflows/unattended-unit.js:348`), and researcher returns are unchecked: 5 of 10 ended without
a final turn. What already works: 98.8% of harness results are structured, and 105 of 105 claimed
commits exist.

## [design] Entry, orientation and progression, as proposed

Three mechanisms carry the design, each the candidate that survived its researcher's losing test: a
position derived by one engine, claims trusted by key and source, and the checklist as a program.
Placement is the one judgment left, and it is declared and checked, never inferred.

### [position] One engine answers "where am I, and what next"

- **The position** is a session's binding, its build, each unit's step, the build's step, the next
  checklist item, that item's actor, and any interrupt. `next` computes it; the card renders it; the
  executor reads it as JSON.
- **Only witnesses decide it**: commits and their trailers, hook-written verdicts per tree, the
  remote's lease and mailbox refs, and generated views whose keys match. A status word an agent typed
  never decides a position.
- **A unit's step**: designed when its spec is committed and derived READY; built when its attributed
  pass commits and acceptance record hold; tested when the verdict for the build's prepared merge
  holds; deployed when the landing contains it. The build's step is its least-advanced unit's (FI-1).
- **The next item** is the first item of the current step whose witness does not hold. Items are
  idempotent by witness: a witnessed item is done, and a crashed one re-checks its witness before it
  runs again.
- **Interrupts come first**, in this order: an owner decision the build waits on; mailbox messages
  addressed to the build; witnesses invalidated since the last transition (a verdict a landing made
  stale, a lease expired or taken over, a parent's breaking interface change); dependency gates.
- **One call** returns the build's slice of the card: the step, the checklist with its witnessed items,
  the next item and its actor, the item's read set at its source SHAs, and every claim used with its
  key and verdict. It ends with the `next —` line.

### [placement] Every request gets a disposition

- **A bound session needs no placement.** A session holding a build's lease, on its branch or
  worktree, is that build's session, mechanically.
- **Any other request is an intake**, the session's first message or any later one that asks for a
  change. Its disposition is declared, never inferred: `continue <build>`, `amend <build>` (re-entry at
  Design), `new` (Plan intake), `patch` (a patch build at Design), `ask <build>`, or `none` (read-only:
  a question, research or a review, with no tracked change).
- **Evidence, not a decision**: `next --place` lists the candidate builds by plan goal and design
  index, and the open asks, beside the request.
- **Checked**: a disposition's witness must hold before the session acts. For `continue` or `amend`,
  the build is live and its lease is free or this session's; for `new`, a Plan intake record holds the
  owner's words verbatim; for `patch`, a derived plan record is placed; for `ask`, the ask is filed; for
  `none`, the write gate refuses every tracked write.
- **Recorded**: the disposition and its reason go into the intake record, so a mis-placement can be
  audited.
- **Whose judgment** is a policy, asked below.
- **An unattended run handed a prompt** places it the same way, rather than always opening a new build.

### [entry] Four ways in, one engine

1. **A new attended session**: the session-start hook writes the card's repository and session cells
   and runs `next` into it; the agent places the request first; the full kickoff runs as a policy says,
   asked below, and consumes the card and `next` rather than re-deriving them.
2. **A resumed or compacted session**: the hook re-keys the card in the session's own tree,
   re-deriving every cell whose key moved, and runs `next`; the compaction summary is evidence only.
3. **The executor**, unattended: code, not a model. It calls `next`, runs the item's actor, resolves
   the item's witness, and repeats. A model is invoked only for a role's item, in a fresh agent with
   its brief, so no unattended context is ever resumed.
4. **A subagent or a single API call**: oriented by its brief alone. The brief is rendered from the
   item and carries the facts the item needs at their source SHAs, not pointers to them, with the write
   set, the allowed tools and the return schema. The agent never runs kickoff or `next`, never re-reads
   what its brief carries, and every read outside the brief is a probe counted against the item.

### [trust] Claims are trusted by key and source

- **Every stored claim carries a key** over what it was derived from: the commit or tree it read, the
  base, the remote ref values, and its age.
- **A session acts on a claim only when its key recomputes equal and its weakest source is not
  actor-typed.** Otherwise it re-derives the claim (most derivers run in under 600 ms) or, where no
  deriver exists, holds the claim as evidence.
- **By class:**

| Claim | Rule |
|---|---|
| A commit and its trailers; a verdict keyed by tree fingerprint; BASE | trusted for exactly that commit or tree |
| The card's cells, `LIVE.md`, the plan view, the design index, generated regions | trusted while their key matches; re-derived when it moves |
| Leases, mailbox entries, run claims | trusted while their remote and clock keys match; a claim and its run record are joined |
| The owner's verbatim words; a ratification through the guarded CLI; the policy file | authoritative for intent, by provenance |
| Status words an agent typed, README status, READY text, session logs, a compaction summary, auto-memory | evidence only; they never decide a position |

- **`next` prints each claim it used with its key and verdict**: fresh, re-derived, or evidence. A
  session re-derives nothing fresh and acts on nothing stale.

### [program] The checklist is a program

- **Each item is declared in the loop definition** with its actor (the owner, the main loop, a role,
  the executor, or a command), its inputs, its allowance (tools, the write set from its lease, gate
  legs), its return schema and its witness.
- **The executor walks the items**: it renders the brief, dispatches one schema-bound agent per role
  item, validates the structured return, and resolves the witness (the git object, the file, the
  verdict) before it starts the next item. Control flow branches only on structured fields, so
  `diverged` becomes an enum.
- **The attended main loop walks the same items** through `next`.
- **Three layers enforce it.** The program prevents by construction. The hooks are the backstop: the
  write gate reads the derived position and the lease's write set, Bash writes included; the spawn
  guard admits only the item's role with its rendered brief; the role-gate arm is repaired once its
  field escape is explained. The transition verifier reads the transcript and git, and refuses a
  transition over an act outside the item's allowance.
- **What a session may do outside an item** is a policy, asked below.

### [resume] Picking up an open build

- **The position lives only in witnessed state**, so any session on any node picks up any open build:
  it takes the build's lease, or takes over an expired one, runs `next`, clears the interrupts, and
  continues at the first unwitnessed item.
- **Partial work** found in the tree, uncommitted inside the item's write set, is handled by a policy,
  asked below.
- **A fresh session can be cheaper than a resumed one**, because orienting costs one call; what gov
  recommends is a policy, asked below.

### [cost] Orientation is priced

- Each session's and agent's calls and tokens before its first item action are recorded per stage
  in the value ledger, and the Loop Review reads the trend; what happens past a ceiling is asked below.
- **The savings the research measured, as targets for the chain's acceptance:** about 5 locate and
  state calls per new session (20% of pre-productive calls), a median 6 card-answerable re-derivations,
  the charter and prompt re-reads by agents, 15% method-document reads by briefed agents, and a median
  467k fresh input tokens per unattended resume.

## [gaps] Ten gaps, in the register

`gap-orient-01` to `gap-orient-10` in `build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md` hold
the measured gaps. Their owners in architecture v2's chain table: placement (01) goes to dRankedPlan;
binding, position, orientation cost, claim keys, resume cost and unbound work (02 to 06, and 08) go to
dDeclaredLoop, the flow's build; briefs (07) to dOrderedCharter; allowances (09) to dScopedBuild; the
memory's dead pointers (10) to dTendedCadence. The executor's home is still owed to the chain re-cut,
and `gap-orient-08` moves with the executor if the re-cut places it elsewhere.

## [forks] Asked, 2026-10-14

**OR-1. "A request names no build and the session holds no build's lease. How is it placed by
default? (Paths can't decide it: the build a README names as its predecessor ranked first 0 of 5
times.)"** Offered: Declared, checked (Recommended); You place every request; Agent places alone.
Answer: Agent places alone.

**OR-2. "When should a session run the full kickoff (manifest audit, scope derivation, READY)? Today
every session is told to, and re-derives what the card printed (a median 6 calls)."** Offered: Only
when opening a build (Recommended); Every session; Never: Plan absorbs it. Answer, in the owner's
words: "Full kickoff should be run in a session that doesn't have a card READY (there should be a
mechanism to save and update it as necessary). When a build/flow step is resumed, a card should be
looked up first and used to reorient."

**OR-3. "What may a session or agent do that no checklist item names? Today about 63% of main-loop
tool calls follow no protocol step."** Offered: Read-only probes only (Recommended); Only the item's
declared reads; Anything, recorded. Answer: Read-only probes only (Recommended).

**OR-4. "A session picks up a build and finds uncommitted work inside the next item's write set,
which no witness covers. What happens by default?"** Offered: Continue from it (Recommended); Restart
the item clean; Ask you. Answer: Continue from it (Recommended).

### Follow-ups asked, 2026-10-14

**OR-5. "Your kickoff answer saves the READY card and looks it up when a build or step resumes. Where
should a build's saved card live?"** Offered: On the remote, beside the lease (Recommended); Committed
in the build folder; Local to the clone. Answer, in the owner's words: "All three options currently. A
better way to preserve orientation should be researched and adopted if there is one. A build
orientation card should be priority 1 along the charter."

**OR-6. "Under "agent places alone", should a placement whose facts fail still be refused, e.g.
continuing a closed build, or one another session's live lease holds?"** Offered: Yes, still refused
(Recommended); No, recorded only. Answer: Yes, still refused (Recommended).

**OR-7. "Resuming a session re-caches its whole context (median 467k fresh tokens, against 146k for a
new one), while a fresh session reorients from its saved card in one call. What should gov recommend
for attended sessions? Unattended items always run in fresh agents."** Offered: Fresh when idle
(Recommended); Always resume; Always fresh. Answer: Fresh when idle (Recommended).

**OR-8. "Each session's and agent's calls and tokens before its first item action will be recorded per
stage. Should orientation have a ceiling?"** Offered: Warn at an evidence ceiling (Recommended); Record
only; Your ceiling. Answer: Record only.

### Settled, 2026-10-14

- **The agent places every request alone** (`placement`, default `agent-places`): it declares the
  disposition and its reason in the intake record and asks the owner nothing; the Plan Review audits
  placements. A placement whose facts fail is still refused (`placement.check`, default `refuse`): a
  live build, a free or own lease, a filed ask.
- **The full kickoff runs only in a session with no READY card** (`kickoff.runs`, default
  `no-ready-card`). The card is saved, and updated as the build moves (`card.follows`, FI-8); a
  resumed build or step looks its card up first and reorients from it.
- **The build's orientation card ranks at priority 1, beside the charter.** The ladder's rank 1 now
  holds the charter and the build's card; every session and agent loads both first.
- **The card is kept in all three places for now** (`card.store`, any subset, default all three): a
  ref per build on the shared remote beside the lease, a card record committed in the build's folder
  with each transition, and the local clone under `.git/orientation/`, looked up by build. A better
  way to preserve orientation is researched (dispatch 15) and adopted if one is found.
- **Off-item acts are read-only probes** (`actions.free`, default `read-only-probes`): free inside the
  current item and counted against it; every write, spawn, commit or push belongs to an item, and
  anything else is filed as an intake.
- **Partial work is continued** (`resume.partial`, default `continue-item`): uncommitted work inside
  the item's write set is kept, the item continues and its witness is still owed; changes outside the
  write set are reported.
- **Gov recommends a fresh session when one is idle** (`resume.context`, default `fresh-when-idle`):
  past the prompt-cache window with a large context, `next` recommends starting fresh and reorienting
  from the card; unattended items always run in fresh agents.
- **Orientation cost is recorded only** (`orient.budget`, default `record-only`): per session, agent
  and stage, read by the Loop Review, never warned.
