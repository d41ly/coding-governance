# The flow's steps, defined: what goes into each

**Serves:** research PLAY-dClosedLoop-1

The owner, 2026-10-15: "Prior to moving to layer 3, let's review each of the layer 2's steps and
define what exactly goes into them."

This record defines each core step of the flow layer, and the breakpoint, item by item. It draws on:
- the flow record's settlements (FL-*);
- the flow-roles record;
- the item audit (`build/2026-10-15-build-PLAY-dClosedLoop-1-research-flow-items-{a,b}.md`);
- the instruction and flow rounds (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-{instruction,flow}.md`).

The audit's fixes are applied, and so is the fold of two Tier-2 rounds (`[revised]`). Each item is the
draft that dDeclaredLoop's loop definition declares. Checklist numbers are retired. Item tags sit in
the `item` namespace: the tables write them short, and their full spelling, such as `item.build.scope`,
never collides with a policy key such as `policy.build.scope` (instruction layer R-B).

## [rules] What every step shares

- **One actor per item, of one kind:** a role, a command the supervisor runs, the executor, a hook the
  supervisor awaits, or the owner. Every item the audit found with several actors is split, and an item
  whose actor a policy value chooses is one item per value.
- **No witness is typed by the acting agent.** A witness is computed from history, written by a hook
  or a command, or a verifier's verdict. An agent's typed return is evidence that the witness joins.
- **Every item declares what it needs.** The `Needs` column names the items whose witnesses it waits
  for. Independent items run in parallel within the fan-out bound (P24).
- **Every item's outcome set is closed, and every outcome routes.**
  - A refusal routes by default: it is recorded, and `next` returns the frontier, the unwitnessed items
    whose needs are witnessed.
  - Routes are declared explicitly where a policy value decides them.
  - Every role item's outcome set includes `probe`, routed to `[probe]` under `probe.raise`, the probe's record
    returned as the item's input on re-entry (night pass, point 2).
- **Attendance changes no item.** Whether the owner attends never changes an item's actor, the driver or a binding.
  It adds only the owner's interactions: the announcement, confirmations at breakpoints and owner questions asked
  live (P4; `[breakpoint]`; night pass, point 1).
- **Every route back is bounded.** A route back, a review round included, counts in the build's
  transition record. Past `flow.route-backs` returns to the same item, the loop becomes an owner item,
  resolved as [breakpoint]'s owner gate is (FH1).
- **Every ask an item files states its acceptance** in one of the mechanical forms the memory layer's
  `[asks]` declares (LR-5). The forms are cited from there, never copied.
- **Every work order loads its load set (P27):**
  - the units scoped to every reader;
  - the role's units;
  - the item's scope tags;
  - the step's practice reach;
  - the policy values the item reads.
- **At every item boundary,** the executor reads the build's mailbox (`mailbox.reads`) and updates the
  card's pointers (`card.pointers`).
- **Closing a mailbox.** When `deploy.unlease` or `life.unlease` closes a build's mailbox, every message
  still on its mailbox ref, disposed or not, is copied into the build folder, and the undisposed ones
  are marked so in that copy. Only then is the ref pruned, and a missing ref counts as done. Unlease
  closes the mailbox, not the build: under `build.closes: after-release-verifies` with `close-only`,
  the build stays open after `deploy.unlease` until `deploy.close` records its transition.
- **Every step ends in an exit item.** Its witness is the witnesses of every item the run reached. An
  item a route skipped is not owed, and the transition record lists the path the run took. A breakpoint
  declared there blocks it until disposed.
- **A recommendation is scored by a command.** Under `review.recommendation.source:
  scored-signals-and-reasoning`, the step's producing role then answers one question, with the score
  handed: should this be reviewed, and why. That is the step's `reason` item. Where the step has no
  single producing role, or under `signals-only`, the recommendation is signals only (P7).
- **A range check reads the build's own work only.** Commits are read `--first-parent` and without
  merges, so a merge of the default branch into the build never reads as the build's additions (the
  gotcha `a-merge-of-the-default-branch-read-as-additions`).
- **Every command item declares whether it is idempotent or reconciles**, as Runtime requires of every
  command adapter.

- **Every item names its owning build** in its table's `Owner` column (revised 2026-10-17, PM-8 and PM-10, `build/2026-10-17-build-PLAY-dClosedLoop-1-ownership.md`). A step's owners are its items' owners, so a step can have several.

## [entry] Entry: placing a request

The flow's router, before any step.

| Item | Actor | Needs | Does | Proven by | Then | Owner |
|---|---|---|---|---|---|---|
| `entry.intake` | hook: prompt-submit, in an owner-bound session only | — | records the owner's prompt, its secrets redacted and its size capped | the hook-written intake entry, carrying the session binding it came from, keyed by its session and content, so it mints no id | `entry.orient`; no intake, because the hook crashed or never fired → `entry.orient` records it absent, and no request mandate exists | dWellOiledMachine |
| `entry.orient` | orientation scout | `entry.intake` | composes the session's card: refreshed, or the full kickoff's where no READY card exists | the card written to its stores, its keys recomputing | `entry.place`, `entry.place-check` or `entry.place-owner`, as `placement` says | dPlacedRequest |
| `entry.place` | orientation scout, under `placement: agent-places` | `entry.orient` | returns the disposition from the closed set (continue, amend, new, patch, repeat, ask, none), with its reason and evidence, and names each observation the request claims | `placement.check` over the return's facts | new → `entry.claim`, then Plan, or `plan.triage-rule` on a re-placement after `plan.dedupe`; amend → Design re-entry, or an `intake` message to the session holding the build; patch → `entry.claim`, then Design as a patch build; repeat → `entry.claim`, then Design as a playbook run, its playbook supplying the feature design; an observation the request claims → `probe.trigger` first, as `probe.observations` says, and back to `entry.place` with the probe's record; continue → that build's `next`; ask → filed; none → the answer relayed; a failed check → back to `entry.place` with the refusal | dPlacedRequest |
| `entry.place-check` | command, under `placement: declared-checked` | `entry.orient` | checks the placement the request declares | `placement.check` over the declared placement | as `entry.place`'s outcomes; a failed check → the request returned with the refusal | dPlacedRequest |
| `entry.place-owner` | owner, under `placement: owner-places` | `entry.orient` | places the request | the owner's disposition record | as `entry.place`'s outcomes | dPlacedRequest |
| `entry.claim` | command | a `new`, `patch` or `repeat` disposition from any of the three placing items, or triage's select | mints the build's slug as memory `[names]` says, and claims it by a compare-and-swap push that creates `refs/gov/claims/<slug>` on the remote, the way unattended claims `refs/gov/runs/<slug>`; `check_slug_claimed` is only its local pre-check. The claim commit carries the claimant's key, the session and the intake's or the ask's content key, so a retry that finds its own key counts as claimed. On `patch` or `repeat` it also takes the build's lease, which such a build never reaches `plan.lease` to take | the claim ref on the remote; on `patch` or `repeat`, the lease record too | claimed → Plan, or Design on `patch` or `repeat`; the slug claimed under another key → a fresh slug, within `flow.route-backs`; the lease refused → as `leases` says; the remote unreachable → no local id minted, the claim queued or refused as `leases.offline` says (DA-M13, FL1) | dPlacedRequest |

- **Whose prompt is intake.** Only a session whose binding record says "owner" writes intake: the session the
  owner types in, attended or not, since attendance is a mode and not a kind of session (night pass, point 1). An
  act session is bound to its act, and a `claude -p` the owner's session runs from its shell is unbound,
  so neither writes intake (Runtime's session binding).
- **What intake keeps.** The prompt passes the secret scanner runlog ships (`scan_secrets` and its
  closed class list), which moves into the core with runlog's journal grammar. A match is redacted in
  the record and reported to the owner. A prompt over the record's size cap keeps its first bytes, its
  length and its hash.
- **The hook is Runtime's.** Its event joins Runtime's enforcement surface, with a witness its reader
  checks (`gap-rt-14`).
- **Policies:** `placement`, `placement.check`, `builds.slug-*`, `leases.*` and `flow.route-backs`.
- **Owner** (revised 2026-10-17, PM-9, and 2026-10-18, SP-1): dPlacedRequest builds the step's items, and `entry.intake`'s
  hook stays dWellOiledMachine's, with `gap-rt-14`. The owner column lands with the ownership table
  (PM-8, PM-10).

Other sources enter Plan's triage directly:
- asks, which are core;
- Maintain's filings and the Loop Review's proposals, from observability;
- trackers and adopter feedback, from integrations.

A prompt that reaches no owner session, through the mailbox's `intake` message or a cadence filer, a cyclic
playbook's `repeat` included, is recorded as intake by dWellOiledMachine's filer and placed by `entry.place` the same
way (night pass, point 1).

## [plan] Plan: is this worth building, and what exactly?

**Enters** on a `new` disposition, or on a select from a pass of the triage over the open asks, filings
and proposals. Either way the build's slug is claimed first, by `entry.claim`. Revised: 2026-10-17, the
debt round's fold: that pass runs outside any build. It keys its triage records by the entry's content,
as intake is, so they mint no id before the claim, and its select routes to `entry.claim`, then
`plan.input`. Inside the build, the pass's triage record already witnesses `plan.triage-rule`, so the
build goes on to `plan.record`.

**Exits** when the plan record is complete and checked, placed and leased:
- under `plan.ratification: request`, the request is the ratification;
- under any other value, ratification is an owner breakpoint at `plan.exit`.

**Takes in** the intake record (the owner's words) or the selected ask. **Hands Design** the ratified
plan record.

| Item | Actor | Needs | Does | Proven by | Then | Owner |
|---|---|---|---|---|---|---|
| `plan.input` | command | — | pins the intake record, or the selected ask, filing or proposal | its SHA | `plan.dedupe`; an observation the request claims, under `probe.observations: verify-at-plan` → `probe.trigger` first, then `plan.dedupe` with the probe's record | dRankedPlan |
| `plan.dedupe` | command | `plan.input` | checks for duplicates and overlaps against live builds, the design index and open asks | the dupes record, keyed by the derived index | none → `plan.triage-rule`; a duplicate or an overlap → `entry.place`, with the finding | dRankedPlan |
| `plan.triage-rule` | command | `plan.dedupe` | applies the declared rules: severity, acceptance, readiness | the triage record naming its rule | select → `plan.record`, through `entry.claim` first on a pass outside any build; defer → filed as an ask, with its acceptance; retire → the ask retired, with the rule; refuse → out of scope, and the requester told; no rule decides → `plan.triage-judge` | dRankedPlan |
| `plan.triage-judge` | planner | `plan.triage-rule` | triages what no rule decides, choosing select, defer, retire or refuse | the schema check over its return, its choice joined to the triage record | as `plan.triage-rule`'s outcomes | dRankedPlan |
| `plan.record` | planner | a select | drafts the plan record: problem, goal, cut-line in and out, acceptance as observations, priority, parents with the interfaces it expects, and each active practice's Plan reach | the plan-record schema check | drafted → `plan.place`; a research request → `plan.research`; an owner question → an owner item, resolved as [breakpoint]'s owner gate is (FH1) | dRankedPlan |
| `plan.research` | researcher | the request of `plan.record` | answers the planner's question | the research record's schema check | `plan.record` | dRankedPlan |
| `plan.place` | command | `plan.record` | regenerates the plan view, the build placed by priority and parents | the placement predicate | placed → `plan.lease`; unplaced → as `plan.unplaced` says | dRankedPlan |
| `plan.lease` | command | `plan.place` | takes the build lease by compare-and-swap | the lease record the lease engine writes at each take | held → `plan.recommend`; an overlap → noted on the card and in the other build's mailbox; refused → as `leases` says | dRankedPlan |
| `plan.recommend` | command | `plan.lease` | scores the review recommendation | the recommendation record | `plan.reason`, or under `signals-only`: no review → `plan.exit`, a review → the Plan breakpoint | dDeclaredLoop |
| `plan.reason` | planner | `plan.recommend` | answers the step's one question, the score handed | the schema check, its answer joined to the recommendation record | no review → `plan.exit`; a review → the Plan breakpoint | dDeclaredLoop |
| `plan.exit` | command | every item the run reached | records the transition; under `plan.ratification: request`, the intake record stands as the ratification | the transition record over the reached items' witnesses | Design; the card is re-rendered and the executor launched where `run.host` says | dRankedPlan |

- **Roles:** planner and researcher; reviewers at a breakpoint.
- **Instruction:**
  - the practices' Plan reach (for `[yagni]`: is the need real now?);
  - the planning view;
  - the intake and plan-record schemas;
  - the policies: `plan.triage`, `plan.authority`, `plan.ratification`, `autonomy`, `plan.unplaced`, `leases.*`, `run.host`, `run.on-owner-question`, `review.plan`, `review.recommendation`, `review.recommendation.source`, `deps.coordination` and `flow.route-backs`.
- **Memory:**
  - reads the intake log, the plan view, the design index, the asks, and the research view and the
    decision log, each selected by build: the plan's parents and the builds `plan.dedupe` matched;
  - writes the dupes, triage, plan and research records, the lease record, the recommendation and the
    transition.
- **Runtime:** the prompt-submit hook, the lease engine, the executor's launch.
- **Breakpoints:** none by default. The ratification is an owner breakpoint at `plan.exit` under any
  `plan.ratification` other than `request`, and under `three-gates` and `every-stage`. An owner may add
  one there to see the plan before Design starts.
- **Extension points:**
  - intake sources (observability, integrations);
  - the planner's recall slot: past research and decisions, found by recall, an optional memory
    component (KN-1);
  - recommendation signals from the value ledger (observability);
  - notifications (integrations).

## [design] Design: how will it be built, and in what pieces?

**Enters** on any of seven inputs:
- the ratified plan record;
- an admitted in-goal amendment;
- a ratified plan revision;
- a patch build's derived plan record, its slug claimed and its lease taken by `entry.claim`;
- a review finding disposed into a new unit;
- a fix unit, for a red whose spec is wrong or a core red the build's own commits introduced;
- a playbook run's derived plan record, its playbook pinned beside it, its slug claimed and its lease taken by
  `entry.claim` (the `repeat` disposition; night pass, point 1).

**Exits** when every unit in scope is READY, the roster is recorded and the confirmed interfaces are
posted to dependents. The build moves through Design whole (FL-D1).

| Item | Actor | Needs | Does | Proven by | Then | Owner |
|---|---|---|---|---|---|---|
| `design.input` | command | — | pins the input and its kind | its SHA and kind | plan record → `design.seams`; amendment → `design.reentry`; plan revision → `design.inventory`; patch → `design.unit-spec`, as a micro-spec; finding or fix unit → `design.unit-spec` for its new unit, or `design.decompose` when it changes an interface; playbook run → `design.unit-spec`, one unit for each piece its playbook declares | dIndexedDesign |
| `design.reentry` | command | `design.input` | classifies an amendment by a structural diff of the declared interfaces (FL-B4) | the diff record | additive and untriggered → `design.unit-spec` for the new units; breaking, or a `design.reentry` trigger → `design.decompose` for that feature | dIndexedDesign |
| `design.inventory` | architect | `design.input` | after a plan revision, gives each completed unit a verdict (kept, amended by a new unit, or retired) with its reason | the inventory joined to every built unit | `design.decompose` | dIndexedDesign |
| `design.seams` | reuse scout | `design.input` | finds the seams by a tree search over the plan's scope paths and the open asks, adding the map's and recall's sources where installed | the seams' probe digests, re-derived by the executor | `design.decompose` | dIndexedDesign |
| `design.decompose` | architect | `design.seams`, `design.inventory` or `design.reentry` | decomposes into features and units: feature designs declaring interfaces structurally (producer, consumers, contract), units with their order and write sets, and feature forks recorded | the roster and interface schema check; every raised feature fork joined to its fork record, which carries its id, its resolver and its declared class | decomposed → `design.overlaps`; a fact fork → `design.research`; a fork the goal cannot survive → a plan revision under the mandate (FR-12) | dIndexedDesign |
| `design.research` | researcher | the asking item | answers a fact fork | the research record's schema check | back to the item that asked | dIndexedDesign |
| `design.overlaps` | command | `design.decompose` | runs the design index over the roster's write sets, against live builds | the overlap record | `design.unit-spec` | dIndexedDesign |
| `design.unit-spec` | spec writer, one per unit, in parallel within the bound | `design.overlaps`, or the input's unit | writes the unit's structured spec: definitions, design, boundaries, interfaces, acceptance as observations with their commands, and each active practice's Design reach; resolves unit forks by `design.forks`; acknowledges the unit's overlaps in its boundaries | the format check on the spec at its SHA; every raised fork joined to its fork record, which carries its id, its resolver and its declared class | authored → `design.recommend`; a feature-level fork → `design.decompose` | dIndexedDesign |
| `design.recommend` | command | every unit's `design.unit-spec` | scores the recommendation | the recommendation record | `design.reason`, or under `signals-only`: no review → `design.ready`, a review → the spec audit | dDeclaredLoop |
| `design.reason` | architect | `design.recommend` | answers the step's one question, the score handed | the schema check, its answer joined to the recommendation record | no review → `design.ready`; a review → the spec audit | dDeclaredLoop |
| `design.ready` | command | `design.recommend`, and the spec audit where it ran | derives READY per unit | derived READY: none MISSING, THIN or FORKED | all READY → `design.exit`; any not → back to that unit's spec writer | dIndexedDesign |
| `design.exit` | command | `design.ready` | records the transition, and posts the confirmed interfaces to dependents | the transition record | Build | dIndexedDesign |

- **Roles:** reuse scout, architect, spec writer and researcher; reviewers at a breakpoint.
- **Instruction:**
  - the practices' Design reach;
  - the decomposition and spec-writing views;
  - the feature-design schema, the structured spec and the micro-spec;
  - the policies: `design.forks`, `design.reentry`, `design.overlap`, `design.handoff`, `deps.early-build`, `deps.messaging`, `review.design`, `review.design.rounds`, `review.design.round-count`, `review.recommendation.source` and `flow.route-backs`.
- **Memory:**
  - reads the plan record, the design index and the parents' confirmed interfaces;
  - writes the roster, the feature designs, the specs, the fork records, each resolved fork with its
    id, its decision, its resolver (a role or the owner) and its declared class, the overlap and research records, the transition and the
    confirmed messages.
- **Runtime:** the fan-out bound, the design index.
- **Breakpoints:**
  - The spec audit sits after `design.recommend` and `design.reason`, before `design.ready`. It is
    opt-in by default, owed under `strict`, and owed above the tier under `guarded`.
    - It runs one round by default.
    - `review.design.rounds` allows four other rules: rounds until no BLOCKER, until no HIGH, until
      clean, or a fixed count (`review.design.round-count`). Each round folds into the unbuilt specs
      before the next (`[breakpoint]`'s `review.fold`), and rounds count against `flow.route-backs`.
  - The owner's design go sits at `design.exit` under `three-gates` and `every-stage`.
- **Extension points:**
  - the map and recall for `design.seams`, and the lexicon for naming, memory's optional components
    (KN-1). Bug classes and the research library left this list at KN-1: they are memory's library
    side, in the core;
  - audit cost (observability);
  - live delivery of confirmed messages (integrations).

## [build] Build: is each unit built to its spec?

**Enters** when every unit is READY and the mandate is active.

**Exits** when:
- every unit is built, with its acceptance recorded;
- the closing review is folded, its findings built as new units;
- no core red stands that the build's own commits introduced.

| Item | Actor | Needs | Does | Proven by | Then | Owner |
|---|---|---|---|---|---|---|
| `build.base` | command | — | pins the base from history, and the mandate | the base SHA and the intake record | `build.unit-lease` | dScopedBuild |
| `build.unit-lease` | command | `build.base` | takes each starting unit's lease with its write set, declared as the driver's `--dispatch --pass <id> --writes <path>` declares one | the lease record | held → `build.unit-pass`; an overlap → warned (`leases.overlap`); refused → as `leases` says | dScopedBuild |
| `build.unit-pass` | builder, one per unit, in declared order; disjoint write sets in parallel | `build.unit-lease` | builds and commits one pass, with the unit id and its trailers; the executor queues its commits | the commit, resolved by the executor. Each unit `reuse.propose` selects carries its reuse line, `proposed <tag>` or `none` with its reason: under `new-seam`, a unit whose spec's reuse audit records a new seam; under `every-unit`, every unit; under `owner-asks`, none, as below. A fix unit carries the class records its findings' `new:` dispositions owe, in its write set, and where the map is installed the claiming dossier's edit. Revised 2026-10-17, the debt round's fold: the line is computed, never taken as typed. `proposed <tag>` joins the instruction command's proposal record for that unit and tag. `none` from a unit whose spec's reuse-audit token (`gap-design-05`) records an existing seam joins that token; from a unit whose token records a new seam, it carries a reason from a closed set (single-use, internal to its feature, or covered by an existing entry whose tag resolves). Under `owner-asks`, no line is owed, and the owner names the features to enter through the instruction command, as LB-2 offered it. For each `new:` slug a fix unit's findings owe, a record under `memory/gotchas/` exists at the unit's commit, its `from:` naming the review and the finding; a missing one is red | committed → `build.acceptance`; spec wrong → the spec writer (unit re-entry); interface change → the architect (feature re-entry if breaking); fork → as `design.forks` says | dScopedBuild |
| `build.acceptance` | executor | `build.unit-pass` | re-runs the spec's acceptance commands on the commit | the executor-written acceptance record | pass → `build.scope`; fail → a fix pass | dScopedBuild |
| `build.scope` | command | `build.acceptance` | checks the commit's paths against its unit's write set, from history, as the driver's `--check-commit` and check 23 already grade a pass; and, where retrofit's ledger is seeded, the touch join over the unit's own commits (retrofit `[drain]`) | the scope report | in scope → the unit's next pass, or, its last pass done, `build.reuse-check`; stray → as `build.scope` says: warned with an ask, reported, or refused. A refused stray routes to a revert pass on the unit, and a stray the range later reverts passes | dScopedBuild |
| `build.reuse-check` | reuse scout, one per unit, at medium | `build.scope` | lists the units the unit's commits add, from the code record, capped at sixty with an overflow line, and answers one row per unit (`duplicate`, `should-extend`, `new` or `not-a-unit`, each with its nearest existing symbol or what was searched), added rows for what the lister cannot see, and one row per MUST seam the unit's spec carried (`used`, `bypassed` or `not-applicable`), under a no-stop line | a computed join: every listed unit and every MUST has one row, and a `bypassed` MUST is also a `duplicate` | clean → the unit built; a `duplicate` or `bypassed` row → a fix pass on the unit; under `build.reuse-check.second-pass: on`, a second independent pass, its rows unioned (the night pass two, point 2) | dScopedBuild |
| `build.recommend` | command | every unit built and reuse-checked | scores the recommendation, signals only: Build runs a builder per unit, so it has no single producing role | the recommendation record | the closing review where owed; otherwise `build.ratify` under `decisions.major: author-owner-ratifies`, else `build.distill` | dDeclaredLoop |
| `build.ratify` | owner, under `decisions.major: author-owner-ratifies` | `build.recommend`, and the closing review where it ran | rules on each fork its author classed major: ratified, or rejected, when the command re-classes the fork as not major on its fork record, acting on the verdict | the owner's disposition record for each major fork | `build.distill`; held → until the owner's disposition record, a ratification `run.on-owner-question` never resolves (FH1) | dScopedBuild |
| `build.distill` | command, idempotent | `build.recommend`, the closing review where it ran, and `build.ratify` under `author-owner-ratifies` | appends to the decision log, in the build's own branch, a row for each of its resolved forks whose class is major, as `decisions.major` says: its date, its build, the fork's id, the decision, a pointer to its rationale, and the reuse entry it created, if any. Its population is the fork records that Design's witnesses and Build's fork records joined, never a directory listing. Under `owner-only`, only a fork the owner resolved may be major; under `author-owner-ratifies`, only a ratified fork's row is written. A row already present, keyed by (build, fork id), is skipped | a one-to-one join on (build, fork id) between the build's resolved forks, each with its class declared, and a row for each major one; a fork with no class, or a second row for one key, is red; under `owner-only`, a major row whose fork the owner did not resolve is red | `build.core`; a fork with no class → back to the role that resolved it, a unit re-entry counted against `flow.route-backs`; under `owner-only`, a major fork the owner did not resolve → an owner item: re-classed as not major, or resolved by the owner | dScopedBuild |
| `build.core` | executor | `build.distill` | runs the core checks over the build's range, the decision-log rows included | the executor-written result | clean → `build.exit`; an own red → a fix unit through Design, or excepted (`core.exceptions`) | dScopedBuild |
| `build.exit` | command | `build.core` | records the transition | the transition record | Test | dScopedBuild |

**The closing review** is the breakpoint between `build.recommend` and `build.ratify` under
`decisions.major: author-owner-ratifies`, otherwise `build.distill`, owed by default:
- it reviews through the diff lens;
- its findings become new units by `review.findings`, so built specs stay frozen (P19), and those
  units pass through Design and back;
- a follow-up round runs after a HIGH finding (`review.follow-up`);
- `build.ratify` where it applies, then `build.distill` and `build.core`, run over the range, the
  findings' units included, so the core checks grade the decision-log rows too (Revised 2026-10-17, the
  debt round's fold and the folds' closing review).

- **Roles:** builder; the spec writer and the architect on a divergence; reviewers at the closing
  review.
- **Instruction:**
  - the practices' Build reach;
  - the unit-building and divergence views;
  - the trailer and builder-return schemas;
  - the policies: `build.worktree`, `build.scope`, `leases.*`, `design.forks`, `design.reentry`, `review.build`, `review.findings`, `review.follow-up`, `reuse.propose`, `decisions.major`, `core.bypass`, `core.exceptions`, `hooks.bypass`, `resume.partial`, `run.on-owner-question` and `flow.route-backs`.
- **Memory:**
  - reads the specs at their SHAs, the write sets, and the bug classes the specs name (revised 2026-10-19,
    the night pass two, point 6, pending NT-24: no longer those the write sets select);
  - writes the commits, the acceptance records, the scope reports, the review report, the core result,
    the reuse lines and proposals, the fix units' class records, the fork records of forks resolved in
    Build, each with its id, resolver and class, written by whoever `design.forks` names to resolve
    it, a rejected fork's re-class, the decision-log rows and the transition.
- **Runtime:**
  - unit leases;
  - the commit queue in the shared worktree;
  - the executor's acceptance re-runs and core checks;
  - the write gate.
- **Breakpoints:** the closing review; `build.ratify`, the owner's ratification of major decisions under
  `decisions.major: author-owner-ratifies`, before `build.distill`; the owner's gate at `build.exit` under `every-stage`.
- **Extension points:**
  - the lexicon, an optional memory component (KN-1). The bug-class checklist left this list at KN-1:
    bug classes are core, on memory's library side, and ride the builder's work order as its unit's spec
    names them, never by its write set (revised 2026-10-19, the night pass two, point 6, pending NT-24);
  - review cost (observability).

## [test] Test: does the merged result hold?

**Enters** at the Build-to-Test transition.

**Exits** when:
- the verdict for the tree to be landed is recorded;
- no red blocks: each blocking red is fixed or excepted;
- the verified tree is on the build's lease record.

| Item | Actor | Needs | Does | Proven by | Then | Owner |
|---|---|---|---|---|---|---|
| `test.merge` | command: the lander's `--prepare` | — | under `verdict.tree: prepared-merge`, prepares the landing merge in Test's worktree: the build merged onto the default branch's tip, kit versions minted where distribution fills the version slot, otherwise the announced skip, and outputs regenerated into it. Under `build-tip`, it pins the build's tip | the prepared merge's SHA and tree hash, or the tip's | prepared → `test.select`; a conflict → Build for a resolution pass, or the architect when an interface clashes; refused → an ask naming the lander's refusal | dWitnessedBar |
| `test.select` | command | `test.merge` | selects the legs the paths claim, the declared product-test levels (`tests.landing-levels`) and the held legs (`verdict.held`). A held leg whose verdict records show `verdict.flakes`' threshold of consecutive greens since its hold, or whose manifest row changed, is released: selected as an ordinary leg, its held-flaky-leg ask closed citing the streak. Without observability's Maintain, the levels left to its cadence too, as `tests.without-cadence` says | the selection record | `test.verdict` | dWitnessedBar |
| `test.verdict` | command: the bar's runner, on the declared backend | `test.select` | runs the bar with attribution (`GATE_ATTRIBUTE`); the runner writes the verdict record for the tree, which the pre-push hook reads | the runner-written verdict per tree hash, each red classed OWN, INHERITED, MIXED, CONTENDED or DEAD PROBE | green → `test.seen-red`; red → `test.route`; stale → `test.merge` | dWitnessedBar |
| `test.route` | command | `test.verdict` | re-runs each red leg once on the same tree, under `test.verdict`'s env, then routes each red by its computed class, as `verdict.blocks` says. A leg red then green is nondeterministic | every red joined to one route, with its re-run's verdict | a nondeterministic leg → `test.flakes`; an OWN or MIXED red → `test.attribute`; a blocking CONTENDED red → a re-run on a quiet host; a blocking DEAD PROBE → the probe repaired, or an owner exception (`core.exceptions`); a blocking INHERITED red → a fix unit through Design, or an owner exception; a red that does not block → an ask | dWitnessedBar |
| `test.attribute` | tester | the OWN and MIXED reds of `test.route` | judges each such red: the code misses its spec, or the spec is wrong | a computed join: every such red has one judgment, and the artifact its route names exists | as `verdict.red-route` says: under `fix-pass-or-design`, a code miss → a fix pass in Build and a wrong spec → a new unit through Design; under `always-new-unit`, both → a new unit through Design | dWitnessedBar |
| `test.flakes` | command | the nondeterministic reds of `test.route` | records each nondeterministic leg as the flake record, of which it is the one writer, except under `retry-only`, and acts as `verdict.flakes` says | the flake record, a flow record kind; under `retry-only`, the re-entry's routing record | under `quarantine`, a leg past the threshold `verdict.flakes` declares is held, an ask is filed in the held-flaky-leg form, keyed by the leg's name, unless one is open for that leg, and the run re-enters `test.select`, which applies the hold, while a leg below it goes as under `record`; under `record`, the flake is recorded and the run re-enters `test.verdict`; under `retry-only`, the run re-enters `test.verdict` and nothing is recorded. Each re-entry counts against `flow.route-backs` | dWitnessedBar |
| `test.seen-red` | command | `test.verdict` | checks that every gate the build added or changed has a seen-red record | the seen-red records | all present → `test.recommend`; one missing → a fix pass on the unit that added the gate | dWitnessedBar |
| `test.recommend` | command | `test.seen-red` | scores the recommendation | the recommendation record | `test.reason`, or under `signals-only`: the gate review where declared, otherwise `test.exit` | dDeclaredLoop |
| `test.reason` | tester | `test.recommend` | answers the step's one question, the score handed | the schema check, its answer joined to the recommendation record | the gate review where declared, otherwise `test.exit` | dDeclaredLoop |
| `test.exit` | command | `test.recommend`, and the gate review where it ran | records the transition, and the verified tree on the build's lease record | the transition record and the lease record | Deploy | dWitnessedBar |

- **Where a flake is seen.** `test.route`'s re-run of a red leg on the same tree is a runner mode
  dWitnessedBar owes (`gap-test-04`), with its probe: Test's declared invocation, over a fixture whose
  leg reds then greens, reaches `test.flakes`. Today the bar retries only timeouts. It prints its own
  `nondeterministic · <leg>` line only for a cached-green leg that a reuse run samples, under
  `GATE_REUSE` or the pre-push hook's `GATE_REUSE_PUSH`, which Test's invocation never sets. That line
  is a second source when a reuse run prints it.
- **The bar's quarantine is another thing.** Its `quarantine.<name key>` keeps a leg out of the reuse
  cache until its manifest row changes. A held leg is the flow's carrier for a flaky one.
- **A held product leg.** Today the bar's held class is the kit self-test subject (`subject = "kit"`),
  run only on request. dWitnessedBar's held legs by policy extend it to any leg a quarantine holds,
  and `verdict.held` decides when a held leg runs: `peer-or-cadence`, `push-selected` or `on-demand`.
- **The remote verdict before the landing.** Under `verdict: remote-ci`, P3's designed slot, the
  lander publishes a candidate ref, as under `peer-node`. Remote CI runs the bar on it, and
  `test.verdict` reads its verdict under integrations' witness rule, keyed by the candidate's SHA. It
  is built when CI exists (R5.2).
- **A fix pass keeps its check** (night pass, point 6). A fix pass's allowance excludes the red leg's own test files
  and its gate script. Changing them takes the tester's `test.attribute` judgment that the spec is wrong, which
  routes to Design as a new unit (P19). Its arm is seen red on a planted fix pass that writes the red leg's test file,
  and a fix pass after a failed `build.acceptance` leaves the acceptance commands' own files alone too (M16).
- **The tester before dBoundRoles** (WK-1). Until dBoundRoles re-founds the roles, dWitnessedBar's minimal tester
  agent plays `test.attribute`, `test.reason` and the fix pass's judgment, its allowance scratch only.
- **Test is the landing verdict; testing elsewhere is a probe** (`[probe]`, P31).
- **Roles:** tester; builders and the architect through its routes; reviewers with the gate lens at a
  breakpoint.
- **Instruction:**
  - the practices' Test reach;
  - the bar and attribution views;
  - the tester-return schema, its judgment set closed;
  - the policies: `verdict`, `verdict.tree`, `verdict.blocks`, `verdict.held`, `verdict.red-route`, `verdict.flakes`, `tests.landing-levels`, `tests.without-cadence`, `tests.product`, `hooks.bypass`, `review.test`, `review.recommendation.source` and `flow.route-backs`.
- **Memory:** writes the merge, selection, routing and attribution records, the runner-written verdict,
  the flake and seen-red records, the transition and the verified tree.
- **Runtime:** Test's worktree, the verdict backend, leases.
- **Breakpoints:** the gate review, opt-in by default and above-tier under `strict`; the owner's gate at
  `test.exit` under `every-stage`.
- **Extension points:**
  - verdict backends, a registry: `local-hook` and `peer-node` are core, built by dWitnessedBar, and
    integrations registers `remote-ci`, read before the landing under `verdict: remote-ci` and after it
    for `deploy.core` under `GATE_POST_MERGE=ci`;
  - the version slot in `test.merge`: `kits.version`, which distribution fills;
  - leg packs: gate-lint, the pytest guardrails, the lexicon's two drift signals, and distribution's
    `currency` leg under `currency.on-behind: red`;
  - product-test runner adapters;
  - the gate-health and flake signals that observability reads.

## [deploy] Deploy: is it landed?

The core runs to the landing, and the build closes there (`build.closes: at-landing`).

**Enters** at the Test-to-Deploy transition, with a current verdict.

**Exits** when:
- the build is landed and recorded;
- its major decisions' rows are in the decision log at the landed SHA;
- its dependents are notified;
- the card's terminal snapshot is committed;
- its leases are released and its mailbox pruned;
- under `build.closes: after-release-verifies`, a release verified its SHA or a later SHA that
  contains it, or the owner closed it unreleased.

| Item | Actor | Needs | Does | Proven by | Then | Owner |
|---|---|---|---|---|---|---|
| `deploy.current` | command | — | checks that the verdict's tree equals the prepared merge on the current tip, or under `verdict.tree: build-tip`, the build's tip | the comparison record | current → `deploy.mandate`; stale → Test | dShippedRelease |
| `deploy.mandate` | command | `deploy.current` | checks the landing's authority: the request's mandate under `plan-only`; under `three-gates` and `every-stage`, the disposition of the owner's landing gate, the breakpoint before this item | the intake record, or the gate's witness | `deploy.parents` | dShippedRelease |
| `deploy.parents` | command | `deploy.mandate` | reads each parent's state, as `deps.landing` says | the parents' records | every parent landed → `deploy.land`; under `test-decides`, the build's own verdict green without the parents' unlanded work → `deploy.land`; a parent unlanded or paused → holds; a parent withdrawn, or ended in planning without landing (deferred, retired, refused or answered) → as `deps.on-parent-withdrawn` says; a parent superseded or merged → the link moves to its replacement, or to the build it merged into, and the hold reads that | dShippedRelease |
| `deploy.land` | command: the lander's `--land`, run with `GOV_PUSH_MAIN_MAX_RETRIES=1` | `deploy.parents` | pushes HEAD of the prepared merge, gated by the pre-push bar for that tree. On a race it re-prepares onto the new tip and exits without a second push | the outcome class, from the lander's exit, the pre-push hook's allow and bar records, and probes of the remote's default branch before and after the push; a landing is the remote holding the pushed SHA that it did not hold before the push, and the lander's marker is optional | landed and gated, the allow record naming the SHA and the bar record a real bar → `deploy.core`; landed ungated, no allow record naming the SHA or a bar record reading a stub → `deploy.core`, the landing recorded ungated until its bar is green; nothing pushed, the remote holding the SHA before the push → `deploy.core`, the landing recorded as already held; refused before the push, a race included → Test, which grades the merge `--land` re-prepared, or an ask for a carried commit; the remote unreachable, a failed probe included → the supervisor's retry, then an owner item; an argument → an ask on the adapter | dShippedRelease |
| `deploy.core` | command | `deploy.land` | starts the post-merge bar on the landed SHA unless a run for that SHA already shows, and reads its verdict keyed by that SHA (K1), as `GATE_POST_MERGE` declares | the bar's verdict for the landed SHA, copied into the landing record when read | green → `deploy.record`; red → a patch build through the entry-point table's post-close row, and the close waits for its filing; refused → one re-run after a fetch, then an owner item; a failed publication → the verdict routes as above, and the publication is re-tried once, then an owner item; still running → waits, within the act's ceiling; no verdict past it → an owner item | dShippedRelease |
| `deploy.record` | command | `deploy.core` | writes the landing record: SHA, the builds and units carried, the outcome class, the pre-push verdict or ungated, the core re-check's verdict, and the `build.closes` value in force. It reads the lander's marker where one was written, otherwise the pushed SHA and the remote tip | the landing record | `deploy.distill` | dShippedRelease |
| `deploy.distill` | command, idempotent | `deploy.record` | confirms that the decision-log rows `build.distill` wrote are in the log at the landed SHA | the rows at the landed SHA, joined one to one on (build, fork id) to the build's major forks | `deploy.recommend`; rows missing at the landed SHA → a patch build through the entry-point table's post-close row, as `deploy.core`'s red does, its append keyed by (build, fork id) so it stays idempotent | dShippedRelease |
| `deploy.recommend` | command | `deploy.distill` | scores the recommendation, signals only, since core Deploy has no producing role | the recommendation record | the landing review where declared, otherwise `deploy.notify` | dDeclaredLoop |
| `deploy.notify` | command, idempotent | `deploy.recommend`, and the landing review where it ran | posts `landed` to dependents, keyed by the landing SHA, so a repeated post is a no-op | the mailbox posts | `deploy.released` and `deploy.snapshot` | dShippedRelease |
| `deploy.released` | command | `deploy.notify` | reads `build.closes`. Under `after-release-verifies`, it is an event wait: the release slot's exit record for the landed SHA, or for a later SHA that contains it, wakes it, once for each waiting build whose landed SHA it contains, and the supervisor runs each under that instance's cadence lease, since under `close-only` the build's lease is gone by then. Under the other two values, it passes at once | the wake's witness, keyed by (exit record id, build), naming the slot's exit record, with its SHA, environment and outcome, and the build it answered; under the other two values, the landing record's `build.closes` value | verified, or a pass → `deploy.close`, once `deploy.unlease` is done; held, rolled forward, rolled back, halted or unverified → the release hold's owner item, keyed by (build, landed SHA) and opened unless one is open, through the owner's notification adapter, since the build's mailbox may be closed, resolved as `run.on-owner-question` says: close unreleased, the outcome on the transition, or wait for a later release; no exit record within `build.release-ceiling`, which the supervisor's sweep watches → the same owner item; `release.environments` emptied, or integrations removed, after the landing → as `policy.on-missing-expansion` says | dShippedRelease |
| `deploy.snapshot` | command, idempotent | `deploy.notify`, and under `build.release-hold: whole-close`, `deploy.released` | commits the card's terminal snapshot; an equal snapshot is a no-op | the snapshot commit | `deploy.unlease` | dShippedRelease |
| `deploy.unlease` | command, idempotent | `deploy.snapshot` | deletes the build's lease refs, a missing ref counting as done, and closes its mailbox (`[rules]`) | the deleted refs, and the mailbox's messages in the folder | `deploy.close`, once `deploy.released` has passed | dShippedRelease |
| `deploy.close` | command | `deploy.unlease` and `deploy.released` | records the transition, with the release outcome under `after-release-verifies`, minted under the build's claim ref, which is never pruned (layer-memory `[contract]`) | the transition record | the build is closed | dShippedRelease |

- **The core re-check's witness** (K1):
  - under `GATE_POST_MERGE=local` or undeclared, `deploy.core` starts `post-merge.sh` on the landed
    SHA as the lander does, unless the start record `<common-dir>/gate-post-merge.start` or the
    per-SHA log `<common-dir>/gate-post-merge-<sha8>.log` already shows a run for that SHA. That
    covers an ungated landing, a landing whose marker failed, a start the lander declined, and an
    undeclared key, as on gov's own tree today;
  - under `ci`, the remote CI's result for the landed SHA is the witness, under integrations' witness
    rule. A red is written as the per-SHA verdict record and published as `refs/gov/bar-red` by the
    node that read it. With no `remote-ci` backend registered, `ci` is refused, or falls back to the
    local run with a report, as `policy.on-missing-expansion` says;
  - under `ci` with `verdict.remote.trust: app-only`, the remote result is a claim, not a witness, so
    `deploy.core` starts the local run, as under `local`, and advances only on it;
  - the verdict is read keyed by the landed SHA, from its per-SHA log, never from the single
    last-verdict file `<common-dir>/gate-post-merge`, which a later landing overwrites. A per-SHA
    verdict record is owed (`gap-deploy-02`);
  - `post-merge.sh` answers green, red or REFUSED. It publishes a red as `refs/gov/bar-red` only when
    that ref is absent or names an ancestor of the SHA, and otherwise keeps it. The publication can
    fail beside either verdict, and then the per-SHA log prints `publish FAILED` and no verdict. So,
    until `gap-deploy-02`'s per-SHA record lands, `deploy.core` reads the verdict from the bar's run
    record that `post-merge.sh` copies to `<common-dir>/gate-run/<run id>/`. REFUSED re-runs once
    after a fetch, then becomes an owner item;
  - the bar is the full bar (`GATE_FULL=1`), which covers the core checks.
- **The lander's outcomes are classes, not exit codes.** `deploy.land` routes on landed and gated,
  landed ungated, nothing pushed, refused before the push, the remote unreachable, and an argument.
  Today the adapter derives them from the lander's exit, the pre-push hook's allow and bar records and
  probes of the remote's default branch before and after the push, since one exit code covers
  several, and a failed probe counts as unreachable. A landing needs the remote not to have held the
  SHA before the push, so no push is both landed and nothing pushed. The lander's own outcome record is owed (`gap-deploy-09`).
- **The landing order.** Landings on a node are ordered by `landing.order` over the verified trees on
  the builds' leases. The turnstile is the host-wide bar semaphore, admitting `slots` concurrent bars,
  and `push-main.sh` never takes it, so no landing queue exists yet (`gap-flow-08`).
- **Roles:** none in the core: every item is a command. The deployer works only in the expansions.
- **Instruction:**
  - the practices' Deploy reach;
  - the landing view;
  - the policies: `autonomy`, `plan.ratification`, `verdict.tree`, `landing.order`, `deps.landing`, `deps.on-parent-withdrawn`, `hooks.bypass`, `core.bypass`, `core.exceptions`, `build.closes`, `build.release-hold`, `build.release-ceiling`, `release.environments`, `card.snapshot`, `run.on-owner-question`, `review.deploy` and `flow.route-backs`.
- **Memory:** writes the landing record, the transition, the terminal snapshot and the `landed`
  messages, reads the decision log at the landed SHA and, under `after-release-verifies`, the release
  slot's exit record, and deletes the lease refs and the mailbox ref.
- **Runtime:** the lander, the hook, the post-merge bar and its verdict record.
- **Breakpoints:**
  - the landing review, between `deploy.recommend` and `deploy.notify`. It blocks the close, not the
    push, and its findings enter as patch builds by the entry-point table's post-close row;
  - the owner's landing gate, before `deploy.mandate`, under `three-gates` and `every-stage`.
- **Extension points:**
  - the release slot, after `deploy.core` is green: integrations' `release.*` program, per
    environment, each environment naming an engine, a verify adapter and whether it is production,
    routed by `deploy.on-verify-fail`. Every pass ends by writing the slot's exit record for its SHA,
    a flow record kind keyed by SHA with an outcome (verified, held, rolled forward, rolled back,
    halted or unverified), the environment that ended the pass and its release record's id, which
    `deploy.released` reads;
  - notifications, through Runtime's notification adapters, which integrations fills.

`build.closes`'s other two values each need an expansion (LR-4):
- `after-release-verifies` holds the close at `deploy.released` until the release slot's exit record
  verifies the landed SHA, or a later SHA that contains it. `build.release-hold` says what waits
  (RH-1): the close alone under `close-only`, the default, or the snapshot, the leases and the mailbox
  too under `whole-close`. It needs integrations with at least one environment listed; otherwise
  `policy.on-missing-expansion` decides;
- `at-landing-maintain-owns` closes at landing, and observability's Maintain owns the release after
  it: its `release-verify-failed` run files a failed verify of the closed build as an owner item. It
  needs observability; otherwise `policy.on-missing-expansion` decides.

## [breakpoint] The breakpoint: review at any boundary

A breakpoint declares three things:
- its position: an item boundary, or a step's exit;
- its disposer: a reviewer lens with its skeptic and synthesizer, or the owner;
- its trigger: owed by policy, a binding recommendation, or the owner's request.

It blocks as `review.blocks` says. Once disposed, the flow resumes at the item the breakpoint stands
before.

- **Its names**, the words a route uses to reach this program, read by the reconciliation probe: `breakpoint`, `owner gate`, `owner item`, `spec audit`, `gate review`, `closing review` and `landing review` (FM8).

**An owner breakpoint is an owner item,** dDeclaredLoop's owner gate, held until the owner's disposition
record (DA-H1, FH1). Once dBoundRoles lands `run.on-owner-question`, that key resolves it, never for a
ratification (LR-3): the supervisor's recorded choice under `best-effort-recorded`, the item or the build
parked under `park-item` or `park-build`, and the run stopped under `stop-run`. Its witness is one of two:
- the owner's disposition record, written by whichever channel carried it: the mailbox, a terminal
  command or a prompt;
- under `best-effort-recorded`, the supervisor's recorded choice, never for a ratification.

`autonomy` places the owner's gates:
- `plan-only` places the Plan ratification, unless the request ratifies;
- `three-gates` adds the design go at `design.exit` and the landing gate before `deploy.mandate`;
- `every-stage` adds a gate at every step's exit.

`attendance` adds the owner's interactions while the owner attends (night pass, point 1):
- every attended value announces each act before it runs, with the `step —` line, and asks owner questions live;
- `confirm-steps` adds a gate at every step's exit, and `confirm-acts` one before every act;
- no value changes an item's actor, the driver or a binding, which the attendance rule's arm checks.

**A reviewer breakpoint runs this program.** Its lens, refute and report items are one harness act,
`tools/workflows/tier2-review.js` (finders, skeptic batches, one synthesis), which Runtime runs as one
multi-agent act. The items are its witnessed stages:

| Item | Actor | Needs | Does | Proven by | Then | Owner |
|---|---|---|---|---|---|---|
| `review.trigger` | command | — | records why the breakpoint fired | the policy value, the recommendation record, or the owner's request record | fired → `review.pin`; not fired → the flow continues | dDeclaredLoop |
| `review.pin` | command | `review.trigger` | pins the artifact: the plan revision, the spec revisions, the commit range or the landing record. It reads `review.opt-in` and passes the harness its arguments: `optIn`, and `preset`, which is `design-audit` when every pinned spec revision is a design or architecture record by the record-kind registry | the pinned SHAs, and the arguments passed, joined to the report's lens-yield keys | `review.lens` | dFairHearing |
| `review.lens` | reviewer, one per lens, within the fan-out bound | `review.pin` | reviews through the lens | a computed join: each finding cites lines that exist in the pinned artifact, and carries its lens and, where one fits, a class from memory's bug-class catalogue (KN-1) | `review.refute` | dFairHearing |
| `review.refute` | skeptic | `review.lens` | tries to refute each finding | a computed join: every finding has one verdict (confirmed, refuted, or unverified, the harness's `uncertain`), and each verdict names its probe and the probe's output | `review.report` | dFairHearing |
| `review.report` | synthesizer | `review.refute` | merges the findings into one report, giving each confirmed finding its left-shift disposition: `class:<slug>`, `new:<slug>`, `gate:<leg>`, or, where `review.unclassed` allows it, `none` with its reason | a computed join: every confirmed finding appears in the report, under the build's `reviews/`, with one disposition. `class:` resolves to a record under `memory/gotchas/`, and `gate:` to a leg in the legs manifest. `new:` names a slug the report claimed at report time, by a compare-and-swap ref on the remote, `refs/gov/class-claims/<slug>`, as `entry.claim` claims a build's slug, so a slug another branch minted is seen; the claim is recorded in the report and re-derivation reads it, or the slug's record carries `from:` this report and finding. `none` carries a reason, and appears only under `reason` or `owner-rules` | `review.dispose`; a `new:` slug claimed elsewhere → re-disposed as `class:` that slug where it fits, or a fresh slug, within `flow.route-backs`; under `owner-rules`, each `none` → an owner item first, resolved as [breakpoint]'s owner gate is (FH1): a class or a gate named, the reason accepted, or the finding returned for a disposition, within `flow.route-backs` | dFairHearing |
| `review.dispose` | command | `review.report` | disposes each confirmed finding by the artifact's state. On an unbuilt spec, the findings go to `review.fold`. On built work, they become new units or asks by `review.findings`. It files each `new:` class with the item that owes its record: `review.fold`'s spec writer on an unbuilt spec, and the fix unit's builder on built work. A finding that becomes an ask carries its `new:` slug, in memory `[asks]`' below-threshold form, which names the record's writer and its acceptance. Each new class carries `from:` its review and finding. It counts each class by its tag (`review.left-shift`), turns an earned gate into a patch-build intake, and files each unverified finding as `review.unverified` says | each disposition joined to its fold, unit or ask, and each `new:` slug to the item or ask that owes its record | unbuilt → `review.fold`; built → released, with a follow-up round as `review.follow-up` says; an unverified finding under `block` → a verification round | dDeclaredLoop |
| `review.fold` | spec writer | `review.dispose` | folds the confirmed findings into the unbuilt specs, the spec-write workflow's disposal stage, and writes the class record of each `new:` disposition | each confirmed finding joined to its fold in the spec at its new SHA, and each `new:` slug to its class record, whose `from:` names this review and finding | the next round as `review.design.rounds` says, or released | dDeclaredLoop |
| `review.cost` | command | `review.report` | records the review's agents and out-tokens in its report, as the harness logs them, extending the harness's `review-shape` line with `shape`, `efforts` and `role-sha` into the shape-run row (systems `[design-role-shapes]`) | the cost field | done | dDeclaredLoop |

- **Classes.** `review.left-shift` counts by class where memory's catalogue tags a finding, and by
  lens where no class fits. The catalogue is core since KN-1, on memory's library side.
- **An unverified finding under `review.unverified: block`.** Its verification round re-runs the
  skeptic with a fresh probe, and counts against `flow.route-backs`. Past that bound it becomes an
  owner item, resolved as the owner gate above is (FH1).
- **Instruction:**
  - the lens views;
  - the reviewer, skeptic and synthesizer schemas;
  - the policies: `review.<stage>`, `review.breakpoints`, `review.blocks`, `review.findings`, `review.left-shift`, `review.unclassed`, `review.follow-up`, `review.unverified`, `review.design.rounds`, `review.design.round-count`, `review.recommendation`, `review.opt-in`, `flow.route-backs` and `run.on-owner-question`.
- **Extension points:** lens packs, which `review.opt-in` fills by swapping a named default lens of a
  preset; a lens, gov's, an expansion's or a repository's, is a catalogue row whose brief is a unit, and
  the harness fills its five slots from that data (the flow and roles adoption, FA-1; revised 2026-10-19,
  the night pass two); the value ledger (observability). The bug-class catalogue is core
  since KN-1.

## [probe] The probe: testing at any boundary

Testing is not a step either (P31). A probe is one program with two ways in:
- **placed** at an item boundary, as a breakpoint is: by `probe.points`, by the owner's request, or owed by
  `probe.observations` when a request claims an observation;
- **raised** by a role as the outcome of its item, under `probe.raise`, as research is routed: the asking item waits,
  and the probe's record returns as its input on re-entry.

Test stays the landing verdict. Only `test.verdict`'s runner-written record gates a landing, and no probe's verdict
feeds `deploy.current`.

- **Its kinds:**
  - a **verification** checks a claim at a pinned SHA: an owner's observation, in the code or on screen;
  - a **reproduction** makes a reported bug red before its fix;
  - an **experiment** compares variants over a pre-registered corpus, and its record is the measured reference that
    later acceptance cites.
- **The driver knows a probe is owed,** because `next` returns the probe's items as the frontier while the asker
  waits (P22).
- **Its verdicts are closed.** A verification or a reproduction is confirmed, refuted, inconclusive or unrunnable, and
  an experiment is measured, within noise, aborted or unrunnable. A claimed or an unrunnable verdict goes to an owner
  item (the closing review's M3).
- **When an observation is verified,** as `probe.observations` says: before `entry.place` places the request; at
  `plan.input` under `verify-at-plan`, though a patch or a repeat build, which never reaches Plan, is verified before
  placement under that value too; and under `on-request` only when the owner asks, through the owner's request (M9).

| Item | Actor | Needs | Does | Proven by | Then | Owner |
|---|---|---|---|---|---|---|
| `probe.trigger` | command | — | records why the probe opened: the boundary `probe.points` names, the owner's request, the observation `probe.observations` owes, or a role item's `probe` outcome under `probe.raise` | the trigger record, keyed by the boundary or the raising return, and by content for a probe before placement, which mints no id | opened → `probe.pin`; not opened → the flow continues | dPlacedRequest |
| `probe.pin` | command | `probe.trigger` | pins the subject by SHA, and records the question, the kind and the losing outcome before anything runs | the probe record's head, its losing outcome committed first | a verification or a reproduction → `probe.design`; an experiment → `probe.experiment` | dPlacedRequest |
| `probe.design` | tester | `probe.pin` | declares the commands that test the claim at the pinned SHA, cold: from the claim and the subject, never from the asker's reasoning | the method's schema check | `probe.run` | dPlacedRequest |
| `probe.experiment` | researcher | `probe.pin` | declares the experiment: the `experiment` shape with its corpus, its variants and its judge | the method's schema check, and the experiment's fan checked against `probe.experiment.authority` | `probe.run`; an experiment beyond its authority → an owner item, resolved as `[breakpoint]`'s owner gate is | dPlacedRequest |
| `probe.run` | executor | `probe.design` or `probe.experiment` | runs the commands at the pinned SHA, or launches the experiment's harness, keeping each output by hash; a visual verification runs through the visual capture adapter | the captured outputs by hash, and an experiment's shape-run rows | `probe.judge`; no capability for the method → `probe.return`, the verdict unrunnable | dPlacedRequest |
| `probe.judge` | command: the executor's re-run, or the experiment's scorer | `probe.run` | compares the outcome with the losing outcome: confirmed, refuted or inconclusive; an experiment measured, within noise or aborted | the re-run's or the scorer's computed verdict; where no command can judge, the verifier's judgment, recorded as claimed | `probe.return` | dPlacedRequest |
| `probe.return` | command, idempotent, through `record` | `probe.judge` | writes the probe record and hands it to the asking item as an input, or to the item after the boundary | the probe record | the asking item's re-entry, or the boundary's next item; a claimed or an unrunnable verdict → an owner item, resolved as `[breakpoint]`'s owner gate is | dPlacedRequest |

- **Against Test and the breakpoint.** A probe gates nothing past the item that asked. A breakpoint disposes its
  findings into folds, units or asks, while a probe hands its record back to the work. `probe.points` names
  boundaries in `review.breakpoints`' grammar.
- **The experiment shape,** dBoundRoles' `experiment` kind, after aScoutedSeam's benchmark, which no chain build
  counts on, with its method since measured (revised 2026-10-19, the night pass two, point 2): a held-out set
  frozen before any tuning, one variable per arm, parsed replies counted before any score, labels rotated per
  case, and the union of arms read as one system:
  - a corpus pinned to a point, with controls and decoys, and blinding at that point;
  - variants sharing one return schema, run in a bounded fan;
  - the scorer factory (dFairHearing) re-deriving every figure from committed raw outputs, paired over the cases every
    variant answered;
  - a blind judge for what no matcher can see;
  - re-runs keyed by variant and effort, and cost as a pinned reading.
- **A visual witness** is a set of deterministic DOM, console and layout assertions that the visual capture adapter
  captured at the pinned SHA and the executor can re-run. An agent's reading of a screenshot is claimed. The owner's
  own observation is an owner disposition. A visual defect worth keeping becomes a deterministic probe, seen red.
- **Roles:** the tester verifies cold; the researcher designs an experiment; the executor runs it; a scorer or a
  blind judge decides it. The tester verifies, as the owner chose (NP-5, 2026-10-18), since one actor acts per
  item (`[rules]`).
- **Instruction:** the probe and tester-return schemas, each verdict set closed; the policies: `probe.points`,
  `probe.raise`, `probe.observations`, `probe.experiment.authority` and `flow.route-backs`.
- **Memory:** writes the trigger, the probe record and an experiment's shape-run rows.
- **Runtime:** the harness adapter's browser capability and the visual capture adapter, dWellOiledMachine's; act
  binding for an experiment's acts.
- **Before the builds it rests on land** (the closing review's H2 and M2). dPlacedRequest builds the program ahead of
  them, so each later part has a stand-in until its build lands:
  - the tester, dWitnessedBar's minimal one first (WK-1), and dBoundRoles' `experiment` shape: until each lands,
    `probe.design` and `probe.experiment` route to an owner item;
  - dBoundRoles' `probe` outcome on the role templates: probes are placed, never raised;
  - dTotalRecall's `record` command: `probe.return` writes the probe record into the build folder, keyed as its kind
    declares;
  - dWellOiledMachine's visual capture adapter: a visual verification is unrunnable.

  The executor's re-run is dDeclaredLoop's own, its witnesses computed rather than typed, and the scorer factory is
  dFairHearing's, an ancestor, so a probe is judged from the start.

## [lifecycle] The owner's controls: pause, resume, withdraw, supersede

Runtime executes the owner's controls (dWellOiledMachine, RT-3). They extend unattended's `--hold`,
`--resume` and `--abort`, and supersede is new. Each control runs as this program:

| Item | Actor | Needs | Does | Proven by | Then | Owner |
|---|---|---|---|---|---|---|
| `life.request` | owner | — | asks to pause, resume, withdraw or supersede the build, or to attend or unattend it, through the guarded command | the command's record | `life.quiesce`; resume → the build's `next`; attend or unattend → the `attendance override` record, scoped by `attendance.scope`, then the build's `next`, announced while attended | dWellOiledMachine |
| `life.quiesce` | executor | `life.request` | dispatches nothing new. Each running act finishes within its ceiling. An open review fan finishes, and a prepared merge is discarded | the executor's record of the acts it let finish | pause → parked; withdraw or supersede → `life.notify`. Once a push is made, the build has landed, and a pause, withdraw or supersede is refused: the build closes through Deploy. One case is not refused: a withdraw or supersede of a landed build waiting at `deploy.released` goes to the release hold's owner item, keyed by (build, landed SHA), which `life.quiesce` opens unless one is open, through the notification adapter: close unreleased, or keep waiting. Once `deploy.unlease` has run, the request is an event wake, and `life.quiesce` runs under its instance's cadence lease (layer-runtime `[schedule]`) | dWellOiledMachine |
| `life.notify` | command, idempotent | `life.quiesce` | posts `withdrawn` or `superseded` to dependents, with the replacement's slug | the mailbox posts | `life.snapshot` | dWellOiledMachine |
| `life.snapshot` | command, idempotent | `life.notify` | commits the card's terminal snapshot | the snapshot commit | `life.unlease` | dWellOiledMachine |
| `life.unlease` | command, idempotent | `life.snapshot` | deletes the leases, closes the mailbox (`[rules]`), and reclaims the build's workspaces | the deleted refs, the mailbox's messages in the folder, and the workspace record | `life.close` | dWellOiledMachine |
| `life.close` | command | `life.unlease` | records the terminal transition: withdrawn, or superseded by its replacement | the transition record | closed | dWellOiledMachine |

- **Attend and unattend stop at the record** (night pass, point 1). They quiesce nothing, since attendance changes no
  item (P4): the next act reads the override and announces itself, or no longer does.
- **A paused build keeps its leases.** The supervisor renews them while it is paused, so
  `leases.expiry-hours` never expires a paused build. Resume enters its `next`.
- **A superseded build's kept work** passes to its replacement through the replacement's
  `design.inventory`.

## [adopt] Repository-level items: adoption and seeding

Retrofit's `adopt` program and `test.seed` run outside any build
(`build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md` `[seed]`). So they are declared here,
beside the owner's lifecycle controls, and the item join reads them (revised 2026-10-17, the
systems and retrofit audit's M3). Distribution's `kits.install` calls the program. Where
distribution is absent, the core's own command runs it.

| Item | Actor | Needs | Does | Proven by | Then | Owner |
|---|---|---|---|---|---|---|
| `adopt.census` | command | — | once in a repository, before its first build, or at the owner's ask: finds the repository's own practices and counts each one's instances, each CI job its own practice | the `census` record | `test.seed` | dLinkedLibrary |
| `test.seed` | command | a check's registration: `adopt.census`, a kit update that brings a new check, or a widened predicate | seeds each registered population that is absent, at that SHA, and after that only a widened predicate's new keys; at adoption, measures the repository's own drain load | the population files, each with its seed SHA and direction | seeded → armed; a failed seed, a timeout, a dead probe or a home the target's hygiene refuses → unarmed, with its reason; under `retrofit.unseeded: refuse`, a check left unseeded refuses the adoption | dWitnessedBar |
| `adopt.practices` | owner | `adopt.census` | rules each practice once: import, translate, keep alongside or retire, largest first, or by keys times reads where observability is installed | the ruling records | each ruling → its practice's migration; until one, as `retrofit.practice-pending` says | dLinkedLibrary |
| `adopt.decisions` | reviewer, as two raters, and the owner where `retrofit.decisions` says | `adopt.census` | routes the decision candidates by the author's rubric | the reconstructed decision records, each `origin: reconstructed@<sha8>` | accepted → `reconstructed`; declined by the owner → kept `rejected`, which the index hides | dLinkedLibrary |
| `adopt.reconstruct` | command | `adopt.census` under `retrofit.reconstruct: at-adoption`, or the owner's ask under `on-ask` | reconstructs records for code no unit touched | the reconstructed records | done; under the default `on-touch` it never runs, and `build.unit-pass` reconstructs on first touch | dLinkedLibrary |

## [transitions] The build's transition table

F-D settled one transition table per level. This is the build's, the draft dDeclaredLoop declares;
the feature and unit tables are owed (`gap-flow-15`). Each state is derived from witnesses (P22), and
the engine refuses any transition the table lacks.

| From | On | To | Witness |
|---|---|---|---|
| none | a placement disposition `new`, from `entry.place`, `entry.place-check` or `entry.place-owner`, its slug claimed by `entry.claim` | planning | the intake record, the disposition and the claim ref |
| none | triage's select of an ask, filing or proposal, its slug claimed by `entry.claim` | planning | the triage record and the claim ref |
| none | a placement disposition `patch`, from any of the three, its slug claimed and its lease taken by `entry.claim` | designing | the patch's derived plan record, the claim ref and the lease record |
| none | a placement disposition `repeat`, from any of the three, its slug claimed and its lease taken by `entry.claim` | designing | the playbook's record, the run's derived plan record, the claim ref and the lease record (the night pass's closing review, H1) |
| planning | `plan.exit` | designing | the transition record |
| planning | triage's defer, retire or refuse | deferred, retired or refused | the triage record |
| planning | the re-placement after `plan.dedupe`: continue, or amend or patch onto the matched build | merged | the placement disposition and the dupes record |
| planning | the re-placement after `plan.dedupe`: ask | deferred | the placement disposition and the filed ask |
| planning | the re-placement after `plan.dedupe`: none | answered | the placement disposition |
| designing | `design.exit` | building | the transition record |
| designing | a fork the goal cannot survive | planning | the plan revision |
| building | `build.exit` | testing | the transition record |
| building | a unit or feature re-entry, or a fix unit | designing | the re-entry record |
| building, testing, or deploying before the push | an amendment admitted at an item boundary | designing | the re-entry record |
| testing | `test.exit` | deploying | the transition record |
| testing | a fix pass, or a conflict to resolve | building | the routing record |
| testing | a new unit through Design | designing | the routing record |
| deploying | a stale verdict | testing | the comparison record |
| deploying | `deploy.land`'s class refused before the push, a race included | testing | the outcome class and the lander's line |
| deploying | `deploy.close` | landed | the transition record, which names the release outcome under `after-release-verifies` |
| any open state | `life.request`: pause | paused | the command's record |
| paused | `life.request`: resume | the state it paused in | the command's record |
| any open state, before the push | `life.close`: withdrawn | withdrawn | the transition record |
| any open state, before the push | `life.close`: superseded | superseded | the transition record |

Landed, withdrawn, superseded, deferred, retired, refused, merged and answered are terminal. A
re-placement after `plan.dedupe` that answers `new` keeps the build, and its claim, in planning: it goes
on to `plan.triage-rule`, which is no transition. A join is owed
beside the table (`gap-flow-15`): every cross-step route in an item's `Then` cell has a row, and every
row is reached by an item, seen red on a planted dropped row.

## [expansions] What the expansions add to the flow

Settled by the expansion round (`build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`).
Expansions meet only through the core (EX-1), so each item below attaches at a core point.
- **Observability's cadence programs, Maintain (`maintain.*`) and the Loop Review (`loop.*`).** They
  register at Runtime's cadence items and read every reading registered at its command adapters:
  each reading's owner is derived, its pin declared, its asks keyed by reading and offender, and
  each event run keyed by event and SHA. A period records a maintenance record, as
  `maintain.record-when` says.
- **Integrations' release program (`release.*`)** fills Deploy's release slot and writes its exit
  record, and its `remote-ci` backend fills Test's verdict-backend registry, read before the landing
  under `verdict: remote-ci` and after it under `GATE_POST_MERGE=ci`.
- **Distribution's `kits.version`** fills the version slot in Test's `test.merge`. Its kit releases
  (`kits.cut`), currency probe (`kits.currency`) and fleet reading (`kits.fleet`) are its own cadence
  programs on `kits.host`, not Maintain's, and its `currency` leg joins Test's leg packs under
  `currency.on-behind: red`.

## [consequences] What the definitions change

- **Core Deploy has no role.** The deployer works only in the expansions: release notes for
  distribution and verify judgment for integrations, so it registers under both. So does the
  maintainer, under observability. Layer 3 sorts the roster by layer.
- **The bug-class checklist** was made an extension point of Build here. Since KN-1 it is core again:
  it rides the builder's work order from memory's library side, as the unit's spec names it, never by the
  unit's write set (revised 2026-10-19, the night pass two, point 6, pending NT-24).
- **Ratification is not an item:**
  - under `plan.ratification: request`, `plan.exit`'s witness carries it;
  - under any other value, it is an owner breakpoint at `plan.exit`.
- **`build.closes`'s two other values exist only with their expansions.** A preset that sets one is
  refused when it is selected on an install without that expansion, so `strict` and `guarded` need
  integrations (the owner's LR-4, `policy.on-missing-expansion`).
- **Three questions were put to the owner** (`[open]`).

## [open] Asked, 2026-10-15

**S-1. "When does a Design spec audit stop running rounds?"**
- Offered:
  - After a round with no HIGH (Recommended);
  - While rounds still find;
  - A fixed number of rounds.
- Answer, in the owner's words: "1 spec review by default, as it is now. This is an owner-adjustable
  setting - until no BLOCKER, no HIGH, or no findings at all, or a set number of rounds."
- Settled: `review.design.rounds`, `one` by default, with `until-no-blocker`, `until-no-high`,
  `until-clean` and `fixed-count` allowed. `review.design.round-count` holds the count, and is read
  only under `fixed-count`.
- **The seam it extends.** The spec audit's round bound already has a carrier: `REVIEW_ROUNDS` in
  `.unattended.conf`, whose kit default of 1 is an owner ruling. The driver also has its loop states:
  CONVERGING, CONVERGED, NON-CONVERGENT and BOUNDED. `review.design.rounds` becomes that bound's one
  carrier, and under the `until-` rules each round counts against `flow.route-backs`.

**S-2. "What happens to a review finding the skeptic can neither confirm nor refute?"**
- Offered:
  - File it as an ask (Recommended);
  - Block until verified;
  - Record only.
- Answer, in the owner's words: "FIle it as an ask by default (what is an 'ask' in this case? build
  unit? backlog item?), the rest are owner-adjustable settings."
- Settled: `review.unverified`, `ask` by default, with `block` and `record` allowed.
- **What an ask is.** An ask is a backlog item, not a unit. Today it is a row in the raising build's
  `BACKLOG.md` (`BACKLOG_MODE = builds`, `memory/HYGIENE.md` `[Backlog layout]`).
  - Today's row carries its id, the date it was filed, and prose. Its status is folded from disposition
    rows, and its severity is a separate `SEV` disposition row.
  - backlog.py's V14 refuses an ask filed since `ASK_CUTOFF` that carries neither `accept` nor a
    `seen … run`, so only recent rows carry an acceptance.
  - The memory layer's design gives the row its own id, a status, a severity, the evidence (the file
    at a SHA, and the command that shows the problem) and an acceptance, the check that says when the
    ask is resolved (LR-5).

  `backlog/<FAMILY>.md` is generated from those rows. A unit belongs to a build's roster and is
  built in that build. An ask waits outside every roster until Plan's triage selects it, as a patch
  build at Design or a unit of a planned build, or retires it.
- **An unverified finding filed as an ask** carries the reviewer's evidence and the skeptic's
  inconclusive verdict. Its acceptance is that a review round confirms or refutes it.
- **For the memory layer:** core flow items file asks. Among them are Test's inherited, mixed,
  contended and dead-probe reds, flake quarantines, scope strays, and unverified findings. So the
  ask register is core memory, even though the owner listed "backlog functionality" among the
  bookkeeping expansions. Its generated index, rotation and labels can stay in the expansion.

**S-3. "Without observability's Maintain, who runs the slower test levels (end-to-end, performance)
that today wait for its cadence?"**
- Offered:
  - Run them at landing (Recommended);
  - Report them unrun;
  - Wait for the expansion.
- Answer, in the owner's words: "Run them at landing by default, other options as owner-adjustable
  settings."
- Settled: `tests.without-cadence`, `run-at-landing` by default, with `report-unrun` and
  `wait-for-expansion` allowed.
- **What the values do without the expansion,** the only case the key governs:
  - `run-at-landing` runs the slower levels in every Test run, within the suite's declared wall-clock
    ceiling, and a breach reds (`[cost]`);
  - `wait-for-expansion` reports them unrun, each with an ask in memory `[asks]`' unrun-level form:
    the level's first green run, once observability's Maintain runs it.

**Presets.** Each preset's values follow its stance:
- `strict` sets rounds until no HIGH, and blocks on an unverified finding;
- `guarded` sets rounds until no BLOCKER;
- `velocity` only records unverified findings, and reports the slower levels unrun.

## [revised] Revised 2026-10-16: the two Tier-2 rounds, folded

Two Tier-2 rounds reviewed this record and `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md`
together, at blobs `43e9cf4b` and `7031c90f`. The comparison record places their findings on 61 defects
(`build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md`, `[map-flow]`), and its map's
`disposition` cells point here for both records. Each defect's fix sits in place, in the sections
named:
- **amend:** this record, or a sibling record, now states the fix;
- **gap:** the owning chain build carries it in the register;
- **fork:** the owner answered it, in the comparison record's `[answers]`;
- **none:** every finding on it was refuted.

Two keys join v2's catalogue: `flow.route-backs` (`[rules]`) and, from LR-4,
`policy.on-missing-expansion` (`[consequences]`).

| Defect | Disposition | Where the fix sits |
|---|---|---|
| `multi-actor-items` | amend | `[rules]`: one actor of one kind per item; every table's actor cells |
| `self-typed-review-witnesses` | amend | `[breakpoint]`: the lens, refute and report items are witnessed by computed joins |
| `exit-witness-all-items` | amend | `[rules]`: an exit's witness covers the items the run reached |
| `breakpoint-placement` | amend | each step's breakpoints; `[breakpoint]`: the flow resumes at the item the breakpoint stands before |
| `autonomy-gates-missing` | amend | `[breakpoint]`: where `autonomy` places the owner's gates; each step's breakpoints say `every-stage`, not `strict` |
| `owner-gate-vs-question` | fork, amend | LR-3; `[breakpoint]`: an owner breakpoint is an owner item |
| `superseded-parent` | amend | `deploy.parents`; `life.notify` |
| `parents-test-decides` | amend | `deploy.parents` under `test-decides` |
| `withdraw-program-missing` | amend, gap | `[lifecycle]`; `[transitions]`; `gap-flow-15` for the feature and unit tables |
| `pause-leases` | amend | `[lifecycle]`: a paused build keeps its leases |
| `review-findings-entry` | amend | `[design]`'s six inputs; `design.input` |
| `landing-review-route` | amend | `[deploy]`: patch builds by the post-close row; `build.core`'s fix unit; layer-flow `[settled]` |
| `deploy-close-reconcile` | amend | `[deploy]`: `deploy.notify`, `deploy.snapshot`, `deploy.release` and `deploy.close`, ordered, each idempotent |
| `red-routes-ignore-policy` | amend | `test.route` and `test.attribute` route by `verdict.blocks` and `verdict.red-route`; layer-flow `[settled]` |
| `unreachable-items` | amend | every table's `Needs` column and routes |
| `ask-acceptance` | fork, amend | LR-5; `[rules]`: every filed ask states its acceptance |
| `first-unwitnessed-item` | amend | `[rules]`: `next` returns the frontier; v2's dDeclaredLoop row too |
| `scope-refusal-stuck` | amend | `build.scope`: a refused stray routes to a revert pass |
| `maintain-superseded-text` | none | refuted |
| `gap-13-14-unstated` | amend | layer-flow `[uncovered]` states `gap-flow-13` and `gap-flow-14` |
| `bar-attribution-unjoined` | amend | `test.verdict` runs `GATE_ATTRIBUTE`, `test.route` routes the computed classes, and `test.attribute` judges OWN and MIXED reds only |
| `lander-rewrites-merge` | amend | `test.merge` is the lander's `--prepare`, and `deploy.land` its `--land` |
| `verdict-tree-build-tip` | amend | `test.merge` and `deploy.current` under `build-tip` |
| `presets-fail-build-closes` | fork, amend | LR-4; `[consequences]`; v2's `policy.on-missing-expansion` |
| `hook-actor-kind` | amend | `entry.intake` is a hook; `test.verdict` is the runner, whose record the pre-push hook reads; layer-flow, v2's contracts, dWitnessedBar's row and flow-roles' Test row too |
| `ask-row-shape` | amend | `[open]` S-2: today's ask row |
| `lease-ref-history` | amend | the lease record replaces "the lease ref's history" |
| `merge-read-as-additions` | amend | `[rules]`: range checks read `--first-parent`, without merges |
| `class-set-undefined` | amend | `[breakpoint]`: classes from memory's catalogue where one fits, the lens otherwise (KN-1) |
| `deployer-producing-role` | amend | layer-flow `[settled]`; `build.recommend` is signals only |
| `reasoning-item-count` | amend | layer-flow `[uncovered]`: four items |
| `audit-b-count` | none | refuted |
| `design-audit-no-fold` | amend | `[breakpoint]`: `review.fold`, and `review.dispose` by the artifact's state |
| `design-rounds-carrier` | amend | `[open]` S-1: the key extends `REVIEW_ROUNDS` and the driver's loop states |
| `review-harness-seam` | amend | `[breakpoint]`: one `tier2-review.js` act, its `uncertain` the unverified verdict |
| `owner-controls-exist` | amend | `[lifecycle]` extends `--hold`, `--resume` and `--abort`; layer-flow `[uncovered]`; `gap-flow-10` |
| `write-set-seams` | amend | `build.unit-lease` and `build.scope` name `--dispatch --writes`, `--check-commit` and check 23 |
| `lander-seams` | amend, gap | `deploy.core` starts or reads the post-merge bar, its verdict keyed by the landed SHA; `deploy.record` reads the marker where one was written; `gap-deploy-02` owes the per-SHA verdict record |
| `tests-without-cadence-dup` | none | refuted |
| `tests-without-cadence-semantics` | amend | `[open]` S-3: what each value does without the expansion |
| `gap-flow-10-owner` | amend | layer-flow `[uncovered]` and `[settled]`: dWellOiledMachine |
| `tag-policy-collision` | amend | the opening: an item's full spelling is `item.<step>.<name>` |
| `policy-lists-incomplete` | amend | each step's policy list |
| `unbounded-loops` | amend | `[rules]`: `flow.route-backs` |
| `intake-hook-crash` | amend, gap | `entry.intake`'s missing route; `gap-rt-14` |
| `intake-owner-scope` | amend | `[entry]`: only an attended-bound session writes intake |
| `intake-secrets` | amend | `[entry]`: the secret scanner and the size cap |
| `lander-exit-classes` | amend, gap | `deploy.land` routes on six outcome classes; `gap-deploy-09` owes the lander's outcome record |
| `owner-disposition-witness` | fork, amend | LR-3; `[breakpoint]`: the disposition record by any channel, or the supervisor's choice |
| `unverified-block-stuck` | amend | `[breakpoint]`: a verification round, bounded by `flow.route-backs` |
| `item-count-readers` | amend | layer-flow `[fit]` points at the items declared here; dated snapshots and research returns keep their counts |
| `mailbox-prune-orphan` | amend | `deploy.release` and `life.release` prune the mailbox; v2 `[open]` |
| `turnstile-not-queue` | amend | `[deploy]`'s landing order; `gap-flow-08` gains the missing queue; v2, the instruction record, flow-roles and the runtime record |
| `reasoning-field-timing` | amend | `[rules]`: the step's `reason` item, after the score |
| `tier-preset-guarded` | amend | `[design]`: owed above the tier under `guarded` |
| `flakes-quarantine-seam` | amend, gap | `test.route` re-runs each red leg and sends a red-then-green leg to `test.flakes`, which acts as `verdict.flakes` says; `gap-test-04` owes the re-run mode |
| `placement-policy-routes` | amend | `[entry]`: `entry.place-check` and `entry.place-owner` |
| `disposition-set-gaps` | amend | `[plan]`: select, defer, retire and refuse |
| `deployer-expansion-mismatch` | amend | `[consequences]`: the deployer registers under distribution and integrations |
| `instruction-tag-examples` | amend | the instruction layer's R-B, in that layer's fold |
| `recommendation-source-mismatch` | none | refuted |

**Revised again, 2026-10-16, after the fold's closing review**
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold.md`). Its confirmed items are fixed in place here:
`test.flakes` on the red route as `verdict.flakes` says, the lander's exit classes and the core
re-check's witness, the transitions the items route, the landing gate before `deploy.mandate`, LR-3's
wording, one mailbox rule, the acceptance forms cited from memory `[asks]`, and `flow.route-backs` in
every step's list. The comparison record's `[closing-review]` names each item and where it went.

**Revised a third time, 2026-10-16, after the follow-up round**
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-followup.md`). Where a fix needs a tool's own
enumeration, the item states the contract and the owning build's gap carries the rest:
`entry.claim` takes the slug claim, `test.route` re-runs red legs (`gap-test-04`), `deploy.land` routes
on outcome classes (`gap-deploy-09`), and `deploy.core` reads a verdict keyed by SHA (`gap-deploy-02`).
The comparison record's `[follow-up]` names each item and where it went.

**Revised 2026-10-16, after the library round's forks LB-1 to LB-4** (layer-library `[settled-lb]`):
`review.report`'s left-shift dispositions, `build.unit-pass`'s reuse line and `deploy.distill`.

**Revised 2026-10-16, after the library round's review** (`reviews/2026-10-16-review-PLAY-dClosedLoop-1-library.md`):
`build.distill` writes the major decisions' rows before Test, and `deploy.distill` confirms them at the
landed SHA; `review.report` gains its `none` arm and its owner route; and each `new:` class record joins
at the item that writes it.

**Revised 2026-10-16, after the expansion round's two reviews**
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-a.md` and `-b.md`) and the owner's RH-1:
`deploy.released` holds the close under `after-release-verifies`, and `build.release-hold` says what
waits; the release slot's exit record is a flow record kind; the version slot moves into `test.merge`;
Test keeps `peer-node` core and reads remote CI before and after the landing; a remote red under `ci`
reaches `refs/gov/bar-red`; and the leg packs gain the lexicon's two signals and the `currency` leg. The
comparison record's `[folded]` (`build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md`)
names each defect and where it went.

**Revised again, 2026-10-16, after the fold's closing review**
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold.md`): `deploy.released` is an event wait
run under its wake's own lease, with a `runtime.hold-ceiling` arm and an owner channel that needs no
mailbox; `deploy.close` mints under the claim ref; unlease closes a mailbox, not a build; the exit
record gains the outcome unverified; `life.quiesce` hands a landed build's withdraw to the release
hold; the core re-check gives `app-only` its arm; and Deploy's Memory bullet reads the exit record.
The comparison record's `[closing-review]` names each item and where it went.

**Revised a third time, 2026-10-16, after the follow-up round** (`reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-followup.md`):
`deploy.close` mints under the claim ref alone; `deploy.released` wakes once per waiting build, and its
ceiling is `build.release-ceiling`, watched by the supervisor's sweep; `life.quiesce` opens the release hold's
owner item itself; and the exit record names the environment that ended the pass. The comparison
record's `[follow-up]` names each item and where it went.

**Revised 2026-10-17, after the debt round's round-3 fold pair**
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-round3-a.md` and `-b.md`): a triage pass runs
outside any build and its select reaches `entry.claim`; the claim is idempotent on the claimant's key;
`test.select` lifts a held leg's hold, `test.flakes` is the flake record's one writer, and its ask is
keyed by the leg; `deploy.land`'s classes are disjoint; and `deploy.core` reads a verdict whatever the
publication did. The debt comparison record's `[fold-fold-round3]` names each defect and where it went.

**Revised 2026-10-17, after the debt round's library pair**
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-library-followup-a.md` and `-b.md`): every raised fork is
joined at Design's witnesses to a fork record with its id, resolver and class; Build's tail is
`build.ratify` under `author-owner-ratifies`, then `build.distill`, then `build.core`, so the core
checks grade the rows; the rows and both joins key on (build, fork id); the reuse line is computed, and
`owner-asks` owes none, as LB-2 offered it; a fix unit's class records are joined at its commit;
`deploy.distill` and a `new:` slug claimed elsewhere each have a route; and Plan reads the library by
build. The debt comparison record's `[fold-library-followup]` names each defect and where it went.

**Revised 2026-10-17, after the debt round's expansion pair**
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-round3-a.md` and `-b.md`):
`life.quiesce` refuses a landed build's pause, withdraw and supersede, save a withdraw or supersede
while the build waits at `deploy.released`; the release hold's owner item has one key, (build, landed
SHA), and every producer opens it only when none is open; a request on a build with no lease is an
event wake; and `deploy.released`'s witness names the build it answered. The debt comparison record's
`[fold-expansions-fold-round3]` names each defect and where it went.
