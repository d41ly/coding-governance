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
- **Every route back is bounded.** A route back, a review round included, counts in the build's
  transition record. Past `flow.route-backs` returns to the same item, the loop becomes an owner item,
  resolved as `run.on-owner-question` says.
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

## [entry] Entry: placing a request

The flow's router, before any step.

| Item | Actor | Needs | Does | Proven by | Then |
|---|---|---|---|---|---|
| `entry.intake` | hook: prompt-submit, in an attended-bound session only | — | records the owner's prompt, its secrets redacted and its size capped | the hook-written intake entry, carrying the session binding it came from, keyed by its session and content, so it mints no id | `entry.orient`; no intake, because the hook crashed or never fired → `entry.orient` records it absent, and no request mandate exists |
| `entry.orient` | orientation scout | `entry.intake` | composes the session's card: refreshed, or the full kickoff's where no READY card exists | the card written to its stores, its keys recomputing | `entry.place`, `entry.place-check` or `entry.place-owner`, as `placement` says |
| `entry.place` | orientation scout, under `placement: agent-places` | `entry.orient` | returns the disposition from the closed set (continue, amend, new, patch, ask, none), with its reason and evidence | `placement.check` over the return's facts | new → `entry.claim`, then Plan, or `plan.triage-rule` on a re-placement after `plan.dedupe`; amend → Design re-entry, or an `intake` message to the session holding the build; patch → `entry.claim`, then Design as a patch build; continue → that build's `next`; ask → filed; none → the answer relayed; a failed check → back to `entry.place` with the refusal |
| `entry.place-check` | command, under `placement: declared-checked` | `entry.orient` | checks the placement the request declares | `placement.check` over the declared placement | as `entry.place`'s outcomes; a failed check → the request returned with the refusal |
| `entry.place-owner` | owner, under `placement: owner-places` | `entry.orient` | places the request | the owner's disposition record | as `entry.place`'s outcomes |
| `entry.claim` | command | a `new` or `patch` disposition from any of the three placing items, or triage's select | mints the build's slug as memory `[names]` says, and claims it by a compare-and-swap push that creates `refs/gov/claims/<slug>` on the remote, the way unattended claims `refs/gov/runs/<slug>`; `check_slug_claimed` is only its local pre-check. On `patch` it also takes the build's lease, which a patch build never reaches `plan.lease` to take | the claim ref on the remote; on `patch`, the lease record too | claimed → Plan, or Design on `patch`; the slug claimed elsewhere → a fresh slug, within `flow.route-backs`; the lease refused → as `leases` says |

- **Whose prompt is intake.** Only a session whose binding record says "attended" writes intake. An
  act session is bound to its act, and a `claude -p` an attended model runs from its shell is unbound,
  so neither writes intake (Runtime's session binding).
- **What intake keeps.** The prompt passes the secret scanner runlog ships (`scan_secrets` and its
  closed class list), which moves into the core with runlog's journal grammar. A match is redacted in
  the record and reported to the owner. A prompt over the record's size cap keeps its first bytes, its
  length and its hash.
- **The hook is Runtime's.** Its event joins Runtime's enforcement surface, with a witness its reader
  checks (`gap-rt-14`).
- **Policies:** `placement`, `placement.check`, `builds.slug-*`, `leases.*` and `flow.route-backs`.

Other sources enter Plan's triage directly:
- asks, which are core;
- Maintain's filings and the Loop Review's proposals, from observability;
- trackers and adopter feedback, from integrations.

## [plan] Plan: is this worth building, and what exactly?

**Enters** on a `new` disposition, or on a pass of the triage over the open asks, filings and proposals,
which selects one into a build. Either way the build's slug is claimed first, by `entry.claim`.

**Exits** when the plan record is complete and checked, placed and leased:
- under `plan.ratification: request`, the request is the ratification;
- under any other value, ratification is an owner breakpoint at `plan.exit`.

**Takes in** the intake record (the owner's words) or the selected ask. **Hands Design** the ratified
plan record.

| Item | Actor | Needs | Does | Proven by | Then |
|---|---|---|---|---|---|
| `plan.input` | command | — | pins the intake record, or the selected ask, filing or proposal | its SHA | `plan.dedupe` |
| `plan.dedupe` | command | `plan.input` | checks for duplicates and overlaps against live builds, the design index and open asks | the dupes record, keyed by the derived index | none → `plan.triage-rule`; a duplicate or an overlap → `entry.place`, with the finding |
| `plan.triage-rule` | command | `plan.dedupe` | applies the declared rules: severity, acceptance, readiness | the triage record naming its rule | select → `plan.record`; defer → filed as an ask, with its acceptance; retire → the ask retired, with the rule; refuse → out of scope, and the requester told; no rule decides → `plan.triage-judge` |
| `plan.triage-judge` | planner | `plan.triage-rule` | triages what no rule decides, choosing select, defer, retire or refuse | the schema check over its return, its choice joined to the triage record | as `plan.triage-rule`'s outcomes |
| `plan.record` | planner | a select | drafts the plan record: problem, goal, cut-line in and out, acceptance as observations, priority, parents with the interfaces it expects, and each active practice's Plan reach | the plan-record schema check | drafted → `plan.place`; a research request → `plan.research`; an owner question → an owner item, resolved as `run.on-owner-question` says |
| `plan.research` | researcher | the request of `plan.record` | answers the planner's question | the research record's schema check | `plan.record` |
| `plan.place` | command | `plan.record` | regenerates the plan view, the build placed by priority and parents | the placement predicate | placed → `plan.lease`; unplaced → as `plan.unplaced` says |
| `plan.lease` | command | `plan.place` | takes the build lease by compare-and-swap | the lease record the lease engine writes at each take | held → `plan.recommend`; an overlap → noted on the card and in the other build's mailbox; refused → as `leases` says |
| `plan.recommend` | command | `plan.lease` | scores the review recommendation | the recommendation record | `plan.reason`, or under `signals-only`: no review → `plan.exit`, a review → the Plan breakpoint |
| `plan.reason` | planner | `plan.recommend` | answers the step's one question, the score handed | the schema check, its answer joined to the recommendation record | no review → `plan.exit`; a review → the Plan breakpoint |
| `plan.exit` | command | every item the run reached | records the transition; under `plan.ratification: request`, the intake record stands as the ratification | the transition record over the reached items' witnesses | Design; the card is re-rendered and the executor launched where `run.host` says |

- **Roles:** planner and researcher; reviewers at a breakpoint.
- **Instruction:**
  - the practices' Plan reach (for `[yagni]`: is the need real now?);
  - the planning view;
  - the intake and plan-record schemas;
  - the policies: `plan.triage`, `plan.authority`, `plan.ratification`, `autonomy`, `plan.unplaced`, `leases.*`, `run.host`, `run.on-owner-question`, `review.plan`, `review.recommendation`, `review.recommendation.source`, `deps.coordination` and `flow.route-backs`.
- **Memory:**
  - reads the intake log, the plan view, the design index, the asks, and the research view and the
    decision log by the plan's scope tags;
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

**Enters** on any of six inputs:
- the ratified plan record;
- an admitted in-goal amendment;
- a ratified plan revision;
- a patch build's derived plan record, its slug claimed and its lease taken by `entry.claim`;
- a review finding disposed into a new unit;
- a fix unit, for a red whose spec is wrong or a core red the build's own commits introduced.

**Exits** when every unit in scope is READY, the roster is recorded and the confirmed interfaces are
posted to dependents. The build moves through Design whole (FL-D1).

| Item | Actor | Needs | Does | Proven by | Then |
|---|---|---|---|---|---|
| `design.input` | command | — | pins the input and its kind | its SHA and kind | plan record → `design.seams`; amendment → `design.reentry`; plan revision → `design.inventory`; patch → `design.unit-spec`, as a micro-spec; finding or fix unit → `design.unit-spec` for its new unit, or `design.decompose` when it changes an interface |
| `design.reentry` | command | `design.input` | classifies an amendment by a structural diff of the declared interfaces (FL-B4) | the diff record | additive and untriggered → `design.unit-spec` for the new units; breaking, or a `design.reentry` trigger → `design.decompose` for that feature |
| `design.inventory` | architect | `design.input` | after a plan revision, gives each completed unit a verdict (kept, amended by a new unit, or retired) with its reason | the inventory joined to every built unit | `design.decompose` |
| `design.seams` | reuse scout | `design.input` | finds the seams by a tree search over the plan's scope paths and the open asks, adding the map's and recall's sources where installed | the seams' probe digests, re-derived by the executor | `design.decompose` |
| `design.decompose` | architect | `design.seams`, `design.inventory` or `design.reentry` | decomposes into features and units: feature designs declaring interfaces structurally (producer, consumers, contract), units with their order and write sets, and feature forks recorded | the roster and interface schema check | decomposed → `design.overlaps`; a fact fork → `design.research`; a fork the goal cannot survive → a plan revision under the mandate (FR-12) |
| `design.research` | researcher | the asking item | answers a fact fork | the research record's schema check | back to the item that asked |
| `design.overlaps` | command | `design.decompose` | runs the design index over the roster's write sets, against live builds | the overlap record | `design.unit-spec` |
| `design.unit-spec` | spec writer, one per unit, in parallel within the bound | `design.overlaps`, or the input's unit | writes the unit's structured spec: definitions, design, boundaries, interfaces, acceptance as observations with their commands, and each active practice's Design reach; resolves unit forks by `design.forks`; acknowledges the unit's overlaps in its boundaries | the format check on the spec at its SHA; every raised fork joined to its resolution | authored → `design.recommend`; a feature-level fork → `design.decompose` |
| `design.recommend` | command | every unit's `design.unit-spec` | scores the recommendation | the recommendation record | `design.reason`, or under `signals-only`: no review → `design.ready`, a review → the spec audit |
| `design.reason` | architect | `design.recommend` | answers the step's one question, the score handed | the schema check, its answer joined to the recommendation record | no review → `design.ready`; a review → the spec audit |
| `design.ready` | command | `design.recommend`, and the spec audit where it ran | derives READY per unit | derived READY: none MISSING, THIN or FORKED | all READY → `design.exit`; any not → back to that unit's spec writer |
| `design.exit` | command | `design.ready` | records the transition, and posts the confirmed interfaces to dependents | the transition record | Build |

- **Roles:** reuse scout, architect, spec writer and researcher; reviewers at a breakpoint.
- **Instruction:**
  - the practices' Design reach;
  - the decomposition and spec-writing views;
  - the feature-design schema, the structured spec and the micro-spec;
  - the policies: `design.forks`, `design.reentry`, `design.overlap`, `design.handoff`, `deps.early-build`, `deps.messaging`, `review.design`, `review.design.rounds`, `review.design.round-count`, `review.recommendation.source` and `flow.route-backs`.
- **Memory:**
  - reads the plan record, the design index and the parents' confirmed interfaces;
  - writes the roster, the feature designs, the specs, the fork records, each resolved fork with its
    decision and its declared class, the overlap and research records, the transition and the
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

| Item | Actor | Needs | Does | Proven by | Then |
|---|---|---|---|---|---|
| `build.base` | command | — | pins the base from history, and the mandate | the base SHA and the intake record | `build.unit-lease` |
| `build.unit-lease` | command | `build.base` | takes each starting unit's lease with its write set, declared as the driver's `--dispatch --pass <id> --writes <path>` declares one | the lease record | held → `build.unit-pass`; an overlap → warned (`leases.overlap`); refused → as `leases` says |
| `build.unit-pass` | builder, one per unit, in declared order; disjoint write sets in parallel | `build.unit-lease` | builds and commits one pass, with the unit id and its trailers; the executor queues its commits | the commit, resolved by the executor. Each unit `reuse.propose` selects carries its reuse line, `proposed <tag>` or `none` with its reason: under `new-seam`, a unit whose spec's reuse audit records a new seam; under `every-unit`, every unit; under `owner-asks`, a unit that builds a feature an owner-filed reuse ask names. A fix unit carries the class records its findings' `new:` dispositions owe, in its write set | committed → `build.acceptance`; spec wrong → the spec writer (unit re-entry); interface change → the architect (feature re-entry if breaking); fork → as `design.forks` says |
| `build.acceptance` | executor | `build.unit-pass` | re-runs the spec's acceptance commands on the commit | the executor-written acceptance record | pass → `build.scope`; fail → a fix pass |
| `build.scope` | command | `build.acceptance` | checks the commit's paths against its unit's write set, from history, as the driver's `--check-commit` and check 23 already grade a pass | the scope report | in scope → the unit's next pass, or, its last pass done, the unit built; stray → as `build.scope` says: warned with an ask, reported, or refused. A refused stray routes to a revert pass on the unit, and a stray the range later reverts passes |
| `build.recommend` | command | every unit built | scores the recommendation, signals only: Build runs a builder per unit, so it has no single producing role | the recommendation record | the closing review where owed; otherwise `build.core` |
| `build.core` | executor | `build.recommend`, and the closing review where it ran | runs the core checks over the build's range | the executor-written result | clean → `build.distill`; an own red → a fix unit through Design, or excepted (`core.exceptions`) |
| `build.distill` | command, idempotent | `build.core` | appends to the decision log, in the build's own branch, a row for each of its resolved forks whose class is major, as `decisions.major` says: its date, its build, the decision, a pointer to its rationale, and the reuse entry it created, if any. Under `owner-only`, only a fork the owner resolved may be major. A row already present, keyed by build and fork, is skipped | a one-to-one join between the build's resolved forks, each with its class declared, and a row for each major one; a fork with no class, or a second row for one key, is red | `build.exit`; under `author-owner-ratifies`, the owner's ratification comes first, an owner item: ratified → the row; rejected → the fork re-classed as not major, kept in the build's records only; held → as `run.on-owner-question` says |
| `build.exit` | command | `build.distill` | records the transition | the transition record | Test |

**The closing review** is the breakpoint between `build.recommend` and `build.core`, owed by default:
- it reviews through the diff lens;
- its findings become new units by `review.findings`, so built specs stay frozen (P19), and those
  units pass through Design and back;
- a follow-up round runs after a HIGH finding (`review.follow-up`);
- `build.core` then runs over the range, the findings' units included.

- **Roles:** builder; the spec writer and the architect on a divergence; reviewers at the closing
  review.
- **Instruction:**
  - the practices' Build reach;
  - the unit-building and divergence views;
  - the trailer and builder-return schemas;
  - the policies: `build.worktree`, `build.scope`, `leases.*`, `design.forks`, `design.reentry`, `review.build`, `review.findings`, `review.follow-up`, `reuse.propose`, `decisions.major`, `core.bypass`, `core.exceptions`, `hooks.bypass`, `resume.partial` and `flow.route-backs`.
- **Memory:**
  - reads the specs at their SHAs, the write sets, and the bug classes those write sets select;
  - writes the commits, the acceptance records, the scope reports, the review report, the core result,
    the reuse lines and proposals, the fix units' class records, the decision-log rows and the
    transition.
- **Runtime:**
  - unit leases;
  - the commit queue in the shared worktree;
  - the executor's acceptance re-runs and core checks;
  - the write gate.
- **Breakpoints:** the closing review; the owner's ratification of major decisions before `build.distill`
  under `decisions.major: author-owner-ratifies`; the owner's gate at `build.exit` under `every-stage`.
- **Extension points:**
  - the lexicon, an optional memory component (KN-1). The bug-class checklist left this list at KN-1:
    bug classes are core, on memory's library side, and ride the builder's work order by its unit's
    write set;
  - review cost (observability).

## [test] Test: does the merged result hold?

**Enters** at the Build-to-Test transition.

**Exits** when:
- the verdict for the tree to be landed is recorded;
- no red blocks: each blocking red is fixed or excepted;
- the verified tree is on the build's lease record.

| Item | Actor | Needs | Does | Proven by | Then |
|---|---|---|---|---|---|
| `test.merge` | command: the lander's `--prepare` | — | under `verdict.tree: prepared-merge`, prepares the landing merge in Test's worktree: the build merged onto the default branch's tip, kit versions minted where distribution fills the version slot, otherwise the announced skip, and outputs regenerated into it. Under `build-tip`, it pins the build's tip | the prepared merge's SHA and tree hash, or the tip's | prepared → `test.select`; a conflict → Build for a resolution pass, or the architect when an interface clashes; refused → an ask naming the lander's refusal |
| `test.select` | command | `test.merge` | selects the legs the paths claim, the declared product-test levels (`tests.landing-levels`) and the held legs (`verdict.held`); without observability's Maintain, the levels left to its cadence too, as `tests.without-cadence` says | the selection record | `test.verdict` |
| `test.verdict` | command: the bar's runner, on the declared backend | `test.select` | runs the bar with attribution (`GATE_ATTRIBUTE`); the runner writes the verdict record for the tree, which the pre-push hook reads | the runner-written verdict per tree hash, each red classed OWN, INHERITED, MIXED, CONTENDED or DEAD PROBE | green → `test.seen-red`; red → `test.route`; stale → `test.merge` |
| `test.route` | command | `test.verdict` | re-runs each red leg once on the same tree, under `test.verdict`'s env, then routes each red by its computed class, as `verdict.blocks` says. A leg red then green is nondeterministic | every red joined to one route, with its re-run's verdict | a nondeterministic leg → `test.flakes`; an OWN or MIXED red → `test.attribute`; a blocking CONTENDED red → a re-run on a quiet host; a blocking DEAD PROBE → the probe repaired, or an owner exception (`core.exceptions`); a blocking INHERITED red → a fix unit through Design, or an owner exception; a red that does not block → an ask |
| `test.attribute` | tester | the OWN and MIXED reds of `test.route` | judges each such red: the code misses its spec, or the spec is wrong | a computed join: every such red has one judgment, and the artifact its route names exists | as `verdict.red-route` says: under `fix-pass-or-design`, a code miss → a fix pass in Build and a wrong spec → a new unit through Design; under `always-new-unit`, both → a new unit through Design |
| `test.flakes` | command | the nondeterministic reds of `test.route` | records each nondeterministic leg as the flake record, except under `retry-only`, and acts as `verdict.flakes` says | the flake record, a flow record kind; under `retry-only`, the re-entry's routing record | under `quarantine`, a leg past the threshold `verdict.flakes` declares is held, an ask is filed in the held-flaky-leg form, and the run re-enters `test.select`, which applies the hold, while a leg below it goes as under `record`; under `record`, the flake is recorded and the run re-enters `test.verdict`; under `retry-only`, the run re-enters `test.verdict` and nothing is recorded. Each re-entry counts against `flow.route-backs` |
| `test.seen-red` | command | `test.verdict` | checks that every gate the build added or changed has a seen-red record | the seen-red records | all present → `test.recommend`; one missing → a fix pass on the unit that added the gate |
| `test.recommend` | command | `test.seen-red` | scores the recommendation | the recommendation record | `test.reason`, or under `signals-only`: the gate review where declared, otherwise `test.exit` |
| `test.reason` | tester | `test.recommend` | answers the step's one question, the score handed | the schema check, its answer joined to the recommendation record | the gate review where declared, otherwise `test.exit` |
| `test.exit` | command | `test.recommend`, and the gate review where it ran | records the transition, and the verified tree on the build's lease record | the transition record and the lease record | Deploy |

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

| Item | Actor | Needs | Does | Proven by | Then |
|---|---|---|---|---|---|
| `deploy.current` | command | — | checks that the verdict's tree equals the prepared merge on the current tip, or under `verdict.tree: build-tip`, the build's tip | the comparison record | current → `deploy.mandate`; stale → Test |
| `deploy.mandate` | command | `deploy.current` | checks the landing's authority: the request's mandate under `plan-only`; under `three-gates` and `every-stage`, the disposition of the owner's landing gate, the breakpoint before this item | the intake record, or the gate's witness | `deploy.parents` |
| `deploy.parents` | command | `deploy.mandate` | reads each parent's state, as `deps.landing` says | the parents' records | every parent landed → `deploy.land`; under `test-decides`, the build's own verdict green without the parents' unlanded work → `deploy.land`; a parent unlanded or paused → holds; a parent withdrawn, or ended in planning without landing (deferred, retired, refused or answered) → as `deps.on-parent-withdrawn` says; a parent superseded or merged → the link moves to its replacement, or to the build it merged into, and the hold reads that |
| `deploy.land` | command: the lander's `--land`, run with `GOV_PUSH_MAIN_MAX_RETRIES=1` | `deploy.parents` | pushes HEAD of the prepared merge, gated by the pre-push bar for that tree. On a race it re-prepares onto the new tip and exits without a second push | the outcome class, from the lander's exit, the pre-push hook's allow and bar records, and a probe of the remote's default branch; a landing is the remote holding the pushed SHA, and the lander's marker is optional | landed and gated, the allow record naming the SHA and the bar record a real bar → `deploy.core`; landed ungated, no allow record naming the SHA or a bar record reading a stub → `deploy.core`, the landing recorded ungated until its bar is green; nothing pushed, the remote already holding the SHA → `deploy.core`, the landing recorded as already held; refused before the push, a race included → Test, which grades the merge `--land` re-prepared, or an ask for a carried commit; the remote unreachable, a failed probe included → the supervisor's retry, then an owner item; an argument → an ask on the adapter |
| `deploy.core` | command | `deploy.land` | starts the post-merge bar on the landed SHA unless a run for that SHA already shows, and reads its verdict keyed by that SHA (K1), as `GATE_POST_MERGE` declares | the bar's verdict for the landed SHA, copied into the landing record when read | green → `deploy.record`; red → a patch build through the entry-point table's post-close row, and the close waits for its filing; refused → one re-run after a fetch, then an owner item; still running → waits, within the act's ceiling; no verdict past it → an owner item |
| `deploy.record` | command | `deploy.core` | writes the landing record: SHA, the builds and units carried, the outcome class, the pre-push verdict or ungated, the core re-check's verdict, and the `build.closes` value in force. It reads the lander's marker where one was written, otherwise the pushed SHA and the remote tip | the landing record | `deploy.distill` |
| `deploy.distill` | command, idempotent | `deploy.record` | confirms that the decision-log rows `build.distill` wrote are in the log at the landed SHA | the rows at the landed SHA, joined one to one to the build's major forks | `deploy.recommend` |
| `deploy.recommend` | command | `deploy.distill` | scores the recommendation, signals only, since core Deploy has no producing role | the recommendation record | the landing review where declared, otherwise `deploy.notify` |
| `deploy.notify` | command, idempotent | `deploy.recommend`, and the landing review where it ran | posts `landed` to dependents, keyed by the landing SHA, so a repeated post is a no-op | the mailbox posts | `deploy.released` and `deploy.snapshot` |
| `deploy.released` | command | `deploy.notify` | reads `build.closes`. Under `after-release-verifies`, it is an event wait: the release slot's exit record for the landed SHA, or for a later SHA that contains it, wakes it, once for each waiting build whose landed SHA it contains, and the supervisor runs each under that wake's own run lease, since under `close-only` the build's lease is gone by then. Under the other two values, it passes at once | the slot's exit record, keyed by SHA, with its outcome; under the other two values, the landing record's `build.closes` value | verified, or a pass → `deploy.close`, once `deploy.unlease` is done; held, rolled forward, rolled back, halted or unverified → an owner item through the owner's notification adapter, since the build's mailbox may be closed, resolved as `run.on-owner-question` says: close unreleased, the outcome on the transition, or wait for a later release; no exit record within `build.release-ceiling`, which the supervisor's sweep watches → the same owner item; `release.environments` emptied, or integrations removed, after the landing → as `policy.on-missing-expansion` says |
| `deploy.snapshot` | command, idempotent | `deploy.notify`, and under `build.release-hold: whole-close`, `deploy.released` | commits the card's terminal snapshot; an equal snapshot is a no-op | the snapshot commit | `deploy.unlease` |
| `deploy.unlease` | command, idempotent | `deploy.snapshot` | deletes the build's lease refs, a missing ref counting as done, and closes its mailbox (`[rules]`) | the deleted refs, and the mailbox's messages in the folder | `deploy.close`, once `deploy.released` has passed |
| `deploy.close` | command | `deploy.unlease` and `deploy.released` | records the transition, with the release outcome under `after-release-verifies`, minted under the build's claim ref, which is never pruned (layer-memory `[contract]`) | the transition record | the build is closed |

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
  - `post-merge.sh` answers green, red or REFUSED, and a red is also published as `refs/gov/bar-red`.
    REFUSED re-runs once after a fetch, then becomes an owner item;
  - the bar is the full bar (`GATE_FULL=1`), which covers the core checks.
- **The lander's outcomes are classes, not exit codes.** `deploy.land` routes on landed and gated,
  landed ungated, nothing pushed, refused before the push, the remote unreachable, and an argument.
  Today the adapter derives them from the lander's exit, the pre-push hook's allow and bar records and
  a probe of the remote's default branch, since one exit code covers several, and a failed probe
  counts as unreachable. The lander's own outcome record is owed (`gap-deploy-09`).
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

**An owner breakpoint is an owner item,** held or resolved as `run.on-owner-question` says (LR-3): the
supervisor's recorded choice under `best-effort-recorded`, the item or the build parked under
`park-item` or `park-build`, and the run stopped under `stop-run`. Its witness is one of two:
- the owner's disposition record, written by whichever channel carried it: the mailbox, a terminal
  command or a prompt;
- under `best-effort-recorded`, the supervisor's recorded choice.

`autonomy` places the owner's gates:
- `plan-only` places the Plan ratification, unless the request ratifies;
- `three-gates` adds the design go at `design.exit` and the landing gate before `deploy.mandate`;
- `every-stage` adds a gate at every step's exit.

**A reviewer breakpoint runs this program.** Its lens, refute and report items are one harness act,
`tools/workflows/tier2-review.js` (finders, skeptic batches, one synthesis), which Runtime runs as one
multi-agent act. The items are its witnessed stages:

| Item | Actor | Needs | Does | Proven by | Then |
|---|---|---|---|---|---|
| `review.trigger` | command | — | records why the breakpoint fired | the policy value, the recommendation record, or the owner's request record | fired → `review.pin`; not fired → the flow continues |
| `review.pin` | command | `review.trigger` | pins the artifact: the plan revision, the spec revisions, the commit range or the landing record | the pinned SHAs | `review.lens` |
| `review.lens` | reviewer, one per lens, within the fan-out bound | `review.pin` | reviews through the lens | a computed join: each finding cites lines that exist in the pinned artifact, and carries its lens and, where one fits, a class from memory's bug-class catalogue (KN-1) | `review.refute` |
| `review.refute` | skeptic | `review.lens` | tries to refute each finding | a computed join: every finding has one verdict (confirmed, refuted, or unverified, the harness's `uncertain`), and each verdict names its probe and the probe's output | `review.report` |
| `review.report` | synthesizer | `review.refute` | merges the findings into one report, giving each confirmed finding its left-shift disposition: `class:<slug>`, `new:<slug>`, `gate:<leg>`, or, where `review.unclassed` allows it, `none` with its reason | a computed join: every confirmed finding appears in the report, under the build's `reviews/`, with one disposition. `class:` resolves to a record under `memory/gotchas/`, and `gate:` to a leg in the legs manifest. `new:` names a slug that no record held at the report's pinned SHA, or whose record carries `from:` this report and finding. `none` carries a reason, and appears only under `reason` or `owner-rules` | `review.dispose`; under `owner-rules`, each `none` → an owner item first, resolved as `run.on-owner-question` says: a class or a gate named, the reason accepted, or the finding returned for a disposition, within `flow.route-backs` |
| `review.dispose` | command | `review.report` | disposes each confirmed finding by the artifact's state. On an unbuilt spec, the findings go to `review.fold`. On built work, they become new units or asks by `review.findings`. It files each `new:` class with the item that owes its record: `review.fold`'s spec writer on an unbuilt spec, and the fix unit's builder on built work. A finding that becomes an ask carries its `new:` slug, and the ask is accepted once the class record exists. Each new class carries `from:` its review and finding. It counts each class by its tag (`review.left-shift`), turns an earned gate into a patch-build intake, and files each unverified finding as `review.unverified` says | each disposition joined to its fold, unit or ask, and each `new:` slug to the item or ask that owes its record | unbuilt → `review.fold`; built → released, with a follow-up round as `review.follow-up` says; an unverified finding under `block` → a verification round |
| `review.fold` | spec writer | `review.dispose` | folds the confirmed findings into the unbuilt specs, the spec-write workflow's disposal stage, and writes the class record of each `new:` disposition | each confirmed finding joined to its fold in the spec at its new SHA, and each `new:` slug to its class record, whose `from:` names this review and finding | the next round as `review.design.rounds` says, or released |
| `review.cost` | command | `review.report` | records the review's agents and out-tokens in its report, as the harness logs them | the cost field | done |

- **Classes.** `review.left-shift` counts by class where memory's catalogue tags a finding, and by
  lens where no class fits. The catalogue is core since KN-1, on memory's library side.
- **An unverified finding under `review.unverified: block`.** Its verification round re-runs the
  skeptic with a fresh probe, and counts against `flow.route-backs`. Past that bound it becomes an
  owner item, resolved as `run.on-owner-question` says.
- **Instruction:**
  - the lens views;
  - the reviewer, skeptic and synthesizer schemas;
  - the policies: `review.<stage>`, `review.breakpoints`, `review.blocks`, `review.findings`, `review.left-shift`, `review.unclassed`, `review.follow-up`, `review.unverified`, `review.design.rounds`, `review.design.round-count`, `review.recommendation`, `flow.route-backs` and `run.on-owner-question`.
- **Extension points:** lens packs; the value ledger (observability). The bug-class catalogue is core
  since KN-1.

## [lifecycle] The owner's controls: pause, resume, withdraw, supersede

Runtime executes the owner's controls (dWellOiledMachine, RT-3). They extend unattended's `--hold`,
`--resume` and `--abort`, and supersede is new. Each control runs as this program:

| Item | Actor | Needs | Does | Proven by | Then |
|---|---|---|---|---|---|
| `life.request` | owner | — | asks to pause, resume, withdraw or supersede the build, through the guarded command | the command's record | `life.quiesce`; resume → the build's `next` |
| `life.quiesce` | executor | `life.request` | dispatches nothing new. Each running act finishes within its ceiling. An open review fan finishes, and a prepared merge is discarded | the executor's record of the acts it let finish | pause → parked; withdraw or supersede → `life.notify`; a push already made → a pause is refused: the build has landed. A withdraw or supersede of a landed build waiting at `deploy.released` opens that item's owner item itself, unless one is open, through the notification adapter and keyed by (build, request): close unreleased, or keep waiting. Once `deploy.unlease` has run, `life.*` runs under the request's own run lease |
| `life.notify` | command, idempotent | `life.quiesce` | posts `withdrawn` or `superseded` to dependents, with the replacement's slug | the mailbox posts | `life.snapshot` |
| `life.snapshot` | command, idempotent | `life.notify` | commits the card's terminal snapshot | the snapshot commit | `life.unlease` |
| `life.unlease` | command, idempotent | `life.snapshot` | deletes the leases, closes the mailbox (`[rules]`), and reclaims the build's workspaces | the deleted refs, the mailbox's messages in the folder, and the workspace record | `life.close` |
| `life.close` | command | `life.unlease` | records the terminal transition: withdrawn, or superseded by its replacement | the transition record | closed |

- **A paused build keeps its leases.** The supervisor renews them while it is paused, so
  `leases.expiry-hours` never expires a paused build. Resume enters its `next`.
- **A superseded build's kept work** passes to its replacement through the replacement's
  `design.inventory`.

## [transitions] The build's transition table

F-D settled one transition table per level. This is the build's, the draft dDeclaredLoop declares;
the feature and unit tables are owed (`gap-flow-15`). Each state is derived from witnesses (P22), and
the engine refuses any transition the table lacks.

| From | On | To | Witness |
|---|---|---|---|
| none | a placement disposition `new`, from `entry.place`, `entry.place-check` or `entry.place-owner`, its slug claimed by `entry.claim` | planning | the intake record, the disposition and the claim ref |
| none | triage's select of an ask, filing or proposal, its slug claimed by `entry.claim` | planning | the triage record and the claim ref |
| none | a placement disposition `patch`, from any of the three, its slug claimed and its lease taken by `entry.claim` | designing | the patch's derived plan record, the claim ref and the lease record |
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
  it rides the builder's work order from memory's library side, by the unit's write set.
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
