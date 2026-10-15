# The flow's steps, defined: what goes into each

**Serves:** research PLAY-dClosedLoop-1

The owner, 2026-10-15: "Prior to moving to layer 3, let's review each of the layer 2's steps and
define what exactly goes into them."

This record defines each core step of the flow layer, and the breakpoint, item by item. It draws on:
- the flow record's settlements (FL-*);
- the flow-roles record;
- the item audit (`build/2026-10-15-build-PLAY-dClosedLoop-1-research-flow-items-{a,b}.md`);
- the instruction and flow rounds (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-{instruction,flow}.md`).

The audit's fixes are applied. Each item is the draft that dDeclaredLoop's loop definition declares.
Item tags sit in the `item` namespace, and checklist numbers are retired.

## [rules] What every step shares

- **One actor per item.** Every item the audit found with several actors is split.
- **No witness is typed by the acting agent.** A witness is computed from history, written by a hook,
  or a verifier's verdict. An agent's typed return is evidence that the witness joins.
- **Every item's outcome set is closed, and every outcome routes.** A refusal routes by default: it is
  recorded, and `next` names the first unwitnessed item. Routes are declared explicitly only where a
  policy value refuses.
- **Every work order loads its load set (P27):**
  - the charter's level-0 units;
  - the role's units;
  - the item's scope tags;
  - the step's practice reach;
  - the policy values the item reads.
- **At every item boundary,** the executor reads the build's mailbox (`mailbox.reads`) and updates the
  card's pointers (`card.pointers`).
- **Every step ends in an exit item.** Its witness is the witnesses of all the step's items. A
  breakpoint declared there blocks it until disposed.
- **A recommendation is scored by a command.** Its reasoning is a field in the return of the step's
  producing role. Where the step has no such role, it is signals-only (P7).
- **Items run in dependency order.** Independent items run in parallel within the fan-out bound (P24).

## [entry] Entry: placing a request

The flow's router, before any step.

| Item | Actor | Does | Proven by | Then |
|---|---|---|---|---|
| `entry.intake` | command: the prompt-submit hook | records the owner's prompt verbatim | the hook-written intake entry | `entry.orient` |
| `entry.orient` | orientation scout | composes the session's card: refreshed, or the full kickoff's where no READY card exists | the card written to its stores, its keys recomputing | `entry.place` |
| `entry.place` | orientation scout | returns the disposition from the closed set (continue, amend, new, patch, ask, none), with its reason and evidence | `placement.check` over the return's facts | new → Plan; amend → Design re-entry, or an `intake` message to the session holding the build; patch → Design as a patch build; continue → that build's `next`; ask → filed; none → the answer relayed; a failed check → back to `entry.place` with the refusal |

Other sources enter Plan's triage directly:
- asks, which are core;
- Maintain's filings and the Loop Review's proposals, from observability;
- trackers and adopter feedback, from integrations.

## [plan] Plan: is this worth building, and what exactly?

**Enters** on a `new` disposition, or with an ask, filing or proposal that triage selects.

**Exits** when the plan record is complete and checked, placed and leased:
- under `plan.ratification: request`, the request is the ratification;
- under any other value, ratification is an owner breakpoint at `plan.exit`.

**Takes in** the intake record (the owner's words) or the selected ask. **Hands Design** the ratified
plan record.

| Item | Actor | Does | Proven by | Then |
|---|---|---|---|---|
| `plan.input` | command | pins the intake record, or the selected ask, filing or proposal | its SHA | `plan.dedupe` |
| `plan.dedupe` | command | checks for duplicates and overlaps against live builds, the design index and open asks | the dupes record, keyed by the derived index | none → `plan.triage-rule`; a duplicate or an overlap → `entry.place`, with the finding |
| `plan.triage-rule` | command | applies the declared rules: severity, acceptance, readiness | the triage record naming its rule | ruled → `plan.record`; no rule decides → `plan.triage-judge` |
| `plan.triage-judge` | planner | triages what no rule decides | the schema check over its return | `plan.record` |
| `plan.record` | planner | drafts the plan record: problem, goal, cut-line in and out, acceptance as observations, priority, parents with the interfaces it expects, and each active practice's Plan reach | the plan-record schema check | drafted → `plan.place`; a research request → `plan.research`; an owner question → best effort, recorded (FR-4) |
| `plan.research` | researcher | answers the planner's question | the research record's schema check | `plan.record` |
| `plan.place` | command | regenerates the plan view, the build placed by priority and parents | the placement predicate | placed → `plan.lease`; unplaced → as `plan.unplaced` says |
| `plan.lease` | command | takes the build lease by compare-and-swap | the lease ref's history | held → `plan.recommend`; an overlap → noted on the card and in the other build's mailbox; refused → as `leases` says |
| `plan.recommend` | command | scores the review recommendation, with the planner's reasoning field | the recommendation record | no review → `plan.exit`; a review → the Plan breakpoint |
| `plan.exit` | command | records the transition; the intake record stands as the ratification | the transition record over every witness above | Design; the card is re-rendered and the executor launched where `run.host` says |

- **Roles:** planner and researcher; reviewers at a breakpoint.
- **Instruction:**
  - the practices' Plan reach (for `[yagni]`: is the need real now?);
  - the planning view;
  - the intake and plan-record schemas;
  - the policies: `plan.triage`, `plan.authority`, `plan.ratification`, `autonomy`, `plan.unplaced`, `leases.*`, `review.plan`, `review.recommendation` and `deps.coordination`.
- **Memory:**
  - reads the intake log, the plan view, the design index and the asks;
  - writes the dupes, triage, plan and research records, the lease ref, the recommendation and the
    transition.
- **Runtime:** the prompt-submit hook, the lease engine, the executor's launch.
- **Breakpoints:** none by default. An owner breakpoint at `plan.exit` shows the plan before Design
  starts.
- **Extension points:**
  - intake sources (observability, integrations);
  - the planner's knowledge slot: decisions, and the research library shared across builds;
  - recommendation signals from the value ledger (observability);
  - notifications (integrations).

## [design] Design: how will it be built, and in what pieces?

**Enters** on any of four inputs:
- the ratified plan record;
- an admitted in-goal amendment;
- a ratified plan revision;
- a patch build's derived plan record.

**Exits** when every unit in scope is READY, the roster is recorded and the confirmed interfaces are
posted to dependents. The build moves through Design whole (FL-D1).

| Item | Actor | Does | Proven by | Then |
|---|---|---|---|---|
| `design.input` | command | pins the input and its kind | its SHA and kind | plan record → `design.seams`; amendment → `design.reentry`; plan revision → `design.inventory`; patch → `design.unit-spec`, as a micro-spec |
| `design.reentry` | command | classifies an amendment by a structural diff of the declared interfaces (FL-B4) | the diff record | additive and untriggered → `design.unit-spec` for the new units; breaking, or a `design.reentry` trigger → `design.decompose` for that feature |
| `design.inventory` | architect | after a plan revision, gives each completed unit a verdict (kept, amended by a new unit, or retired) with its reason | the inventory joined to every built unit | `design.decompose` |
| `design.seams` | reuse scout | finds the seams by a tree search over the plan's scope paths and the open asks, adding knowledge's sources where installed | the seams' probe digests, re-derived by the executor | `design.decompose` |
| `design.decompose` | architect | decomposes into features and units: feature designs declaring interfaces structurally (producer, consumers, contract), units with their order and write sets, and feature forks recorded | the roster and interface schema check | decomposed → `design.overlaps`; a fact fork → `design.research`; a fork the goal cannot survive → a plan revision under the mandate (FR-12) |
| `design.research` | researcher | answers a fact fork | the research record's schema check | back to the item that asked |
| `design.overlaps` | command | runs the design index over the roster's write sets, against live builds | the overlap record | `design.unit-spec` |
| `design.unit-spec` | spec writer, one per unit, in parallel within the bound | writes the unit's structured spec: definitions, design, boundaries, interfaces, acceptance as observations with their commands, and each active practice's Design reach; resolves unit forks by `design.forks`; acknowledges the unit's overlaps in its boundaries | the format check on the spec at its SHA; every raised fork joined to its resolution | authored → `design.recommend`; a feature-level fork → `design.decompose` |
| `design.recommend` | command | scores the recommendation, with the architect's reasoning field | the recommendation record | no review → `design.ready`; a review → the Design breakpoint, the spec audit |
| `design.ready` | command | derives READY per unit | derived READY: none MISSING, THIN or FORKED | all READY → `design.exit`; any not → back to that unit's spec writer |
| `design.exit` | command | records the transition, and posts the confirmed interfaces to dependents | the transition record | Build |

- **Roles:** reuse scout, architect, spec writer and researcher; reviewers at a breakpoint.
- **Instruction:**
  - the practices' Design reach;
  - the decomposition and spec-writing views;
  - the feature-design schema, the structured spec and the micro-spec;
  - the policies: `design.forks`, `design.reentry`, `design.overlap`, `design.handoff`, `deps.early-build`, `deps.messaging` and `review.design`.
- **Memory:**
  - reads the plan record, the design index and the parents' confirmed interfaces;
  - writes the roster, the feature designs, the specs, the fork, overlap and research records, the
    transition and the confirmed messages.
- **Runtime:** the fan-out bound, the design index.
- **Breakpoints:** the spec audit at `design.exit`, opt-in by default and owed under `strict`.
  - It runs one round by default.
  - `review.design.rounds` allows four other rules: rounds until no BLOCKER, until no HIGH, until
    clean, or a fixed count (`review.design.round-count`).
- **Extension points:**
  - the map, recall and bug classes for `design.seams`, the lexicon for naming, and the research
    library (knowledge);
  - audit cost (observability);
  - live delivery of confirmed messages (integrations).

## [build] Build: is each unit built to its spec?

**Enters** when every unit is READY and the mandate is active.

**Exits** when:
- every unit is built, with its acceptance recorded;
- the closing review is folded, its findings built as new units;
- no core red stands that the build's own commits introduced.

| Item | Actor | Does | Proven by | Then |
|---|---|---|---|---|
| `build.base` | command | pins the base from history, and the mandate | the base SHA and the intake record | `build.unit-lease` |
| `build.unit-lease` | command | takes each starting unit's lease with its write set | the lease ref's history | held → `build.unit-pass`; an overlap → warned (`leases.overlap`); refused → as `leases` says |
| `build.unit-pass` | builder, one per unit, in declared order; disjoint write sets in parallel; commits queued by the executor | builds and commits one pass, with the unit id and its trailers | the commit, resolved by the executor | committed → `build.acceptance`; spec wrong → the spec writer (unit re-entry); interface change → the architect (feature re-entry if breaking); fork → as `design.forks` says |
| `build.acceptance` | command: the executor | re-runs the spec's acceptance commands on the commit | the executor-written acceptance record | pass → the next pass, or the unit built; fail → a fix pass |
| `build.scope` | command | checks each commit's paths against its unit's write set, from history | the scope report | in scope → onward; stray → warned with an ask, or refused, as `build.scope` says |
| `build.recommend` | command | scores the recommendation, where the closing review is not owed | the recommendation record | `build.core`, or the closing review |
| `build.core` | command: the executor | runs the core checks over the build's range | the executor-written result | clean → `build.exit`; an own red → refused until a new unit fixes it or it is excepted (`core.exceptions`) |
| `build.exit` | command | records the transition | the transition record | Test |

**The closing review** is the breakpoint at `build.core`, owed by default:
- it reviews through the diff lens;
- its findings become new units by `review.findings`, so built specs stay frozen (P19), and those
  units pass through Design and back;
- a follow-up round runs after a HIGH finding (`review.follow-up`).

- **Roles:** builder; the spec writer and the architect on a divergence; reviewers at the closing
  review.
- **Instruction:**
  - the practices' Build reach;
  - the unit-building and divergence views;
  - the trailer and builder-return schemas;
  - the policies: `build.worktree`, `build.scope`, `design.forks`, `design.reentry`, `review.build`, `review.findings`, `review.follow-up`, `core.bypass`, `core.exceptions`, `hooks.bypass` and `resume.partial`.
- **Memory:**
  - reads the specs at their SHAs and the write sets;
  - writes the commits, the acceptance records, the scope reports, the review report, the core result
    and the transition.
- **Runtime:**
  - unit leases;
  - the commit queue in the shared worktree;
  - the executor's acceptance re-runs and core checks;
  - the write gate.
- **Extension points:**
  - the bug-class checklist after each pass, recorded as not applicable without knowledge;
  - the lexicon (knowledge);
  - review cost (observability).

## [test] Test: does the merged result hold?

**Enters** at the Build-to-Test transition.

**Exits** when:
- the verdict for the tree to be landed is recorded;
- no red blocks;
- the verified tree is on the build's lease.

| Item | Actor | Does | Proven by | Then |
|---|---|---|---|---|
| `test.merge` | command | merges the build onto the default branch's current tip, in Test's worktree | the merge SHA and its tree hash | merged → `test.select`; a conflict → Build for a resolution pass, or the architect when an interface clashes |
| `test.select` | command | selects the legs the paths claim, the declared product-test levels (`tests.landing-levels`) and the held legs (`verdict.held`); without observability's Maintain, the levels left to its cadence too, as `tests.without-cadence` says | the selection record | `test.verdict` |
| `test.verdict` | command: the bar, through the hook, on the declared backend | runs the bar; the hook writes the verdict for the tree | the hook-written verdict per tree hash | green → `test.flakes` and `test.seen-red`; red → `test.attribute`; stale → `test.merge` |
| `test.attribute` | tester | classifies each red and names its route | a computed join: every red leg in the verdict has one disposition, and the artifact each disposition names exists | code misses its spec → a fix pass in Build; spec wrong → a new unit through Design; inherited, mixed, contended or a dead probe → an ask |
| `test.flakes` | command | records flakes, and quarantines them past the threshold | the flake record, a flow record kind | a quarantine → an ask |
| `test.seen-red` | command | checks that every gate the build added or changed has a seen-red record | the seen-red records | one missing → a fix pass on the unit that added the gate |
| `test.recommend` | command | scores the recommendation, with the tester's reasoning field | the recommendation record | the gate review where declared, otherwise `test.exit` |
| `test.exit` | command | records the transition, and the verified tree on the build's lease | the transition record and the lease ref's history | Deploy |

- **Roles:** tester; builders and the architect through its routes; reviewers with the gate lens at a
  breakpoint.
- **Instruction:**
  - the practices' Test reach;
  - the bar and attribution views;
  - the tester-return schema, its disposition set closed;
  - the policies: `verdict`, `verdict.tree`, `verdict.blocks`, `verdict.held`, `verdict.red-route`, `verdict.flakes`, `tests.landing-levels`, `tests.product`, `hooks.bypass` and `review.test`.
- **Memory:** writes the merge, selection and attribution records, the hook-written verdict, the flake
  and seen-red records, the transition and the verified tree.
- **Runtime:** Test's worktree, the hook, the verdict backend, leases.
- **Breakpoints:** the gate review, opt-in by default and above-tier under `strict`.
- **Extension points:**
  - verdict backends beyond the local hook: remote CI (integrations);
  - leg packs: gate-lint and the pytest guardrails;
  - product-test runner adapters;
  - the gate-health and flake signals that observability reads.

## [deploy] Deploy: is it landed?

The core runs to the landing, and the build closes there (`build.closes: at-landing`).

**Enters** at the Test-to-Deploy transition, with a current verdict.

**Exits** when:
- the build is landed and recorded;
- its leases are released;
- its dependents are notified;
- the card's terminal snapshot is committed.

| Item | Actor | Does | Proven by | Then |
|---|---|---|---|---|
| `deploy.current` | command | checks that the verdict's tree equals the prepared merge on the current tip | the comparison record | current → `deploy.mandate`; stale → Test |
| `deploy.mandate` | command | checks the landing's authority: the request's mandate under `plan-only`, otherwise an owner breakpoint | the intake record, or the owner's disposition | `deploy.parents` |
| `deploy.parents` | command | holds until every parent has landed (`deps.landing`) | the parents' landing records | landed → `deploy.land`; a parent withdrawn → as `deps.on-parent-withdrawn` says |
| `deploy.land` | command: the lander, through the turnstile | merges `--no-ff` and pushes, reusing the pre-push verdict for the same tree | the pushed merge and the reused verdict | landed → `deploy.core`; the tip moved → Test |
| `deploy.core` | command | runs the core checks on the landed tree (K1) | the core-check result | clean → `deploy.record`; a red → the build cannot close until a new unit fixes it or it is excepted |
| `deploy.record` | command | writes the landing record: SHA, the builds and units carried, the verdict | the landing record | `deploy.recommend` |
| `deploy.recommend` | command | scores the recommendation, signals only, since core Deploy has no producing role | the recommendation record | the landing review where declared, otherwise `deploy.close` |
| `deploy.close` | command | releases the leases, posts `landed` to dependents, commits the card's terminal snapshot, and records the transition | the transition record, the deleted lease refs, the mailbox posts and the snapshot commit | the build is closed |

- **Roles:** none in the core: every item is a command. The deployer works only in the expansions.
- **Instruction:**
  - the practices' Deploy reach;
  - the landing view;
  - the policies: `autonomy`, `plan.ratification`, `verdict.tree`, `landing.order`, `deps.landing`, `deps.on-parent-withdrawn`, `hooks.bypass`, `core.bypass`, `core.exceptions`, `build.closes`, `card.snapshot` and `review.deploy`.
- **Memory:** writes the landing record, the transition, the terminal snapshot and the `landed`
  messages, and deletes the lease refs.
- **Runtime:** the lander, the turnstile queue, the hook, the core checks.
- **Breakpoints:**
  - the landing review, which blocks `deploy.close`, not the push;
  - the owner's landing gate, under `three-gates` and `strict`.
- **Extension points:**
  - versions and release notes (distribution);
  - promotion through environments, each verify recorded per SHA, with `deploy.on-verify-fail`
    (integrations);
  - notifications (integrations).

`build.closes`'s other two values each need an expansion:
- `after-release-verifies` needs integrations' deploy engine;
- `at-landing-maintain-owns` needs observability's Maintain.

## [breakpoint] The breakpoint: review at any boundary

A breakpoint declares three things:
- its position: an item boundary, or a step's exit;
- its disposer: a reviewer lens with its skeptic and synthesizer, or the owner;
- its trigger: owed by policy, a binding recommendation, or the owner's request.

It blocks as `review.blocks` says. An owner breakpoint parks the build until the owner's disposition
is hook-written. A reviewer breakpoint runs this program:

| Item | Actor | Does | Proven by | Then |
|---|---|---|---|---|
| `review.trigger` | command | records why the breakpoint fired | the policy value, the recommendation record, or the hook-written owner intake | fired → `review.pin`; not fired → the flow continues |
| `review.pin` | command | pins the artifact: the plan revision, the spec revisions, the commit range or the landing record | the pinned SHAs | `review.lens` |
| `review.lens` | reviewer, one per lens, within the fan-out bound | reviews through the lens | findings, each tagged with a class from the registered core set | `review.refute` |
| `review.refute` | skeptic | tries to refute each finding | a verdict per finding: confirmed, refuted or unverified | `review.report` |
| `review.report` | synthesizer | merges the findings into one report | the report under the build's `reviews/` | `review.dispose` |
| `review.dispose` | command | disposes each confirmed finding by `review.findings` into new units or asks; counts each class by its tag (`review.left-shift`); turns an earned gate into a patch-build intake; files each unverified finding as `review.unverified` says, an ask by default | each disposition joined to its unit or ask id | disposed → released, with a follow-up round as `review.follow-up` says |
| `review.cost` | command | records the review's cost in its report | the cost field | done |

- **Instruction:**
  - the lens views;
  - the reviewer, skeptic and synthesizer schemas;
  - the policies: `review.<stage>`, `review.breakpoints`, `review.blocks`, `review.findings`, `review.left-shift`, `review.follow-up` and `review.recommendation`.
- **Extension points:** lens packs; the bug-class catalogue (knowledge); the value ledger
  (observability).

## [expansions] What the expansions add to the flow

- **Observability's cadence steps, Maintain and the Loop Review.** They keep the programs walked in
  the flow record's `[maintain]` and `[review]`, with the audit's fixes:
  - a detector register by layer;
  - intakes rendered from keyed readings;
  - event runs keyed by event;
  - a declared home for each report.

  They are defined at observability's review.
- **Distribution's and integrations' Deploy extensions:**
  - kit versions and release notes;
  - promotion through environments, with a verify per SHA and `deploy.on-verify-fail`.

## [consequences] What the definitions change

- **Core Deploy has no role.** The deployer works only in the expansions: release notes and verify
  judgment. So does the maintainer. Layer 3 sorts the roster by layer.
- **The bug-class checklist is now an extension point of Build,** not a core item. Without knowledge it
  records not-applicable.
- **Ratification is not an item:**
  - under `plan.ratification: request`, `plan.exit`'s witness carries it;
  - under any other value, it is an owner breakpoint at `plan.exit`.
- **`build.closes`'s two other values exist only with their expansions,** and the policy check refuses
  them otherwise.
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

**S-2. "What happens to a review finding the skeptic can neither confirm nor refute?"**
- Offered:
  - File it as an ask (Recommended);
  - Block until verified;
  - Record only.
- Answer, in the owner's words: "FIle it as an ask by default (what is an 'ask' in this case? build
  unit? backlog item?), the rest are owner-adjustable settings."
- Settled: `review.unverified`, `ask` by default, with `block` and `record` allowed.
- **What an ask is.** An ask is a backlog item, not a unit. Today it is a row in the raising build's
  `BACKLOG.md` (`BACKLOG_MODE = builds`, `memory/HYGIENE.md` `[Backlog layout]`). The row carries:
  - its own id;
  - a status and a severity;
  - the evidence: the file at a SHA, and the command that shows the problem;
  - an acceptance, the check that says when the ask is resolved.

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

**Presets.** Each preset's values follow its stance:
- `strict` sets rounds until no HIGH, and blocks on an unverified finding;
- `guarded` sets rounds until no BLOCKER;
- `velocity` only records unverified findings, and reports the slower levels unrun.
