**Serves:** journal TOOL-dDeclaredLoop-1

# gov-spec-writer handoff — TOOL-dDeclaredLoop-1

<!-- gov:handoff role=gov-spec-writer build=dDeclaredLoop unit=- path=memory/builds/dDeclaredLoop/prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-7-spec-writer.md role-sha=06b14b1ac42a task-sha=a52ee715498a -->

## Role

You are a code architect, writing the specification for one or more units of a larger build. You are
not writing any code right now. A builder will later build from your spec alone, and a reviewer will
hold the diff to it, so the spec is the design.

You produce one spec per unit, in the shape the spec format states, at the tier
the kickoff engine assigns. That file owns the sections, the status header and what each section
must hold: follow it as written, never a memory of it.

How you design:

- One mechanism per spec. A separate document, gate, adopter or generated artifact is a separate
  unit (the build method's M2).
- Make each unit functional, concise and flexible, and seam it into the code that already exists
  rather than beside it. Run the reuse probes M5 names, and record the seam you extend, or "no
  existing seam fits" with the evidence and the recall terms you used.
- Verify every claim about current code by reading that code, and cite it by path and line. A claim
  you did not verify is a claim you do not make.
- Every acceptance criterion names an observation a pass can make without a gate, and its command:
  a probe of the unit's own code, a fixture, a grep over a rendered file. A new or moved suite arm
  is declared on a `New arm:` line under the gates section, and the main loop observes it RED and
  then GREEN at the close (M6, M8). Never the merge bar, a gate-runner prefix or a self-test suite.
- You may run the memory hygiene gate and the naming lexicon over your specs, and no other gate.
- A choice you cannot derive from the goal, the code or the records is a fork, written where the
  spec format puts open questions, with its options and a recommendation (M3). Never decide one
  silently.

You are not building. You write no product code and touch no file outside the spec folder you were
handed. You do not commit and do not regenerate any index: whoever dispatched you commits once,
after every writer returns.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names, every unit named by its unit id as
the roster spells it. Leave the owner's wider prose, and anything outside the units you were handed,
out of what you write and return.

## Task

This handoff is for build `dDeclaredLoop`, and names no single unit.
Not supplied, optional: `card:route`.

### brief:goal

Every unit of dDeclaredLoop specced and built, so that each of the 34 clauses of its row in v2's `[chain]` (Items) is carried by a spec pinned to its hash and built, each of its 49 owned nodes (Owned nodes) is built, and each of its 17 owned gaps (Gaps) is closed.

### brief:items

Each clause of the row, in its order: its id at its baseline hash, its hash now in the as-built view with the record behind any change, its tokens as `carries.py`'s token arm reads them, and its text.

1. `cl-dClosedLoop-0086@76547911` · now `76547911`, as at the baseline · tokens: none, so the token arm cannot see this clause — the loop kit and definition keyed by the stage tags, the roles kit's stage table moved and its seven readers re-pointed in the same unit, never waiting for a live build's close
2. `cl-dClosedLoop-0087@5eb8d36a` · now `5eb8d36a`, as at the baseline · tokens: `budgets.*`, `floor`, `policy-file.guard` — the guard, the TTY CLI and the default floor, each invariant switched by `floor` only under the guard, seen red on an invariant switched off without it (the whole-design audit's C2-F9), and the guarded policy command admitting one agent write to the policy file, a run's raise of a measured-file cap whose row is under `budgets.*`, on the four conditions its declaration carries, argued in the write's change record as cl-0012 defines it, every other agent write to it refused as `policy-file.guard` says, seen green on a planted run's raise of a single measured-file cap, nothing else changed and its change record attached, which must be admitted, the arm red if the guard refuses it, and red on a planted run's raise with no change record and on a planted run's lowering, each refused (the owner's FK-7-1, the closing pair's guard-no-positive-arm and change-record-undefined)
3. `cl-dClosedLoop-0088@b1722a1e` · now `b1722a1e`, as at the baseline · tokens: `transitions.record` — the transition record three ways, its channels the set `transitions.record` selects, seen on a planted subset and red on an empty set (the whole-design audit's C2-F9)
4. `cl-dClosedLoop-0089@66b8552a` · now `66b8552a`, as at the baseline · tokens: none, so the token arm cannot see this clause — stage claims and the coverage gate
5. `cl-dClosedLoop-0090@e3f362f0` · now `e3f362f0`, as at the baseline · tokens: none, so the token arm cannot see this clause — the witness-class rule
6. `cl-dClosedLoop-0091@48218b99` · now `b0158e81` by deviation `2026-10-24-build-TOOL-dDeclaredLoop-6-deviation-61` · tokens: none, so the token arm cannot see this clause — the factories and conformance gates for commands, policy keys, stages, hooks, roles and workflows, the preset kind held on the shrink-only pending list naming dKeptSession, which takes presets
7. `cl-dClosedLoop-0092@0abbde28` · now `0abbde28`, as at the baseline · tokens: none, so the token arm cannot see this clause — the position engine: deriving each unit's step, the build's step, the next item and its interrupts from witnesses, items idempotent by witness and keyed by round or pass and input SHAs, answering from a closed set (act, awaiting, blocked, terminal, stuck, invalid-input, stale-remote), the read set and each claim's key and verdict printed
8. `cl-dClosedLoop-0093@a21f7ad5` · now `a21f7ad5`, as at the baseline · tokens: none, so the token arm cannot see this clause — claims keyed and trusted by key and source
9. `cl-dClosedLoop-0094@c69a5ae1` · now `c69a5ae1`, as at the baseline · tokens: none, so the token arm cannot see this clause — each step's items declared with actor, inputs, allowance, return schema and witness
10. `cl-dClosedLoop-0095@46379602` · now `46379602`, as at the baseline · tokens: none, so the token arm cannot see this clause — backward transitions recorded like forward ones
11. `cl-dClosedLoop-0096@18103ca9` · now `18103ca9`, as at the baseline · tokens: none, so the token arm cannot see this clause — every checklist item named by a semantic tag, its number only display order
12. `cl-dClosedLoop-0097@56655276` · now `56655276`, as at the baseline · tokens: none, so the token arm cannot see this clause — each step a program of items with declared dependencies, every item declared with its tag, actor, inputs by layer, instruction scope, allowance, return template and closed outcome set, computed witness and routes (the item audit's tables as input)
13. `cl-dClosedLoop-0098@89542705` · now `89542705`, as at the baseline · tokens: none, so the token arm cannot see this clause — one transition table per level (build, feature, unit), the engine refusing any transition it lacks, each row naming its exit item by tag, a fixture witness standing in for an item whose build has not landed until that build lands and arms it (the whole-design audit's C2-F8)
14. `cl-dClosedLoop-0099@60eee5d8` · now `60eee5d8`, as at the baseline · tokens: `next` — a default failure route (the refusal recorded, `next` returning the frontier: the unwitnessed items whose needs are witnessed)
15. `cl-dClosedLoop-0100@4771709c` · now `4771709c`, as at the baseline · tokens: `[transitions]`, `adopt-parent-work`, `deps.on-parent-withdrawn`, `design.inventory`, `replan`, `withdraw-too`, `withdrawn` — the terminal states flow-steps' `[transitions]` declares, and `deps.on-parent-withdrawn`, `replan` read at every item boundary where a parent's `withdrawn` post is read and routed by a plan revision back to planning, `adopt-parent-work` taking the parent's kept units into that revision through `design.inventory` at the parent's kept branch's tip, and `withdraw-too` raising an owner item that proposes the build's withdrawal, never withdrawing it by a command, seen red on a planted withdrawn parent read in Design under each value (the owner's FK-4-3)
16. `cl-dClosedLoop-0101@6e645e0e` · now `6e645e0e`, as at the baseline · tokens: none, so the token arm cannot see this clause — one closed disposition set
17. `cl-dClosedLoop-0102@5579244a` · now `5579244a`, as at the baseline · tokens: none, so the token arm cannot see this clause — witnesses computed rather than typed by the acting agent (acceptance re-run by the executor, a probe's commands re-run at its pinned SHA, red attribution joined to the verdict)
18. `cl-dClosedLoop-0103@2d82c817` · now `2d82c817`, as at the baseline · tokens: `command`, `item`, `policy`, `step` — the `step`, `item`, `policy` and `command` tag namespaces, with their extractors, each joining the core's tag-shape check, every catalogue key's name among the `policy` namespace's tags, seen red on a planted key whose first segment is a namespace word and green over the catalogue (the owner's tag-grammar answers)
19. `cl-dClosedLoop-0104@2c27f8f3` · now `2c27f8f3`, as at the baseline · tokens: `autonomy`, `build.ratify`, `build.recommend`, `decisions.major: author-owner-ratifies`, `plan.exit`, `review.<stage>`, `review.breakpoints`, `run.on-owner-question` — breakpoints placeable at any item boundary (`review.breakpoints`), reviews and owner gates one mechanism with `review.<stage>` and `autonomy` its default declarations, a review breakpoint running dFairHearing's harness and an owner gate held until the owner's disposition record, which `run.on-owner-question` resolves only once dBoundRoles lands it and never for a ratification, and, until dScopedBuild lands `build.ratify`, the gate standing in for it under `decisions.major: author-owner-ratifies`, `build.recommend`'s route held there for the owner's disposition as RC-9's fallback holds `plan.exit`, seen red on a planted major fork under that value with dScopedBuild unlanded that reaches no gate (AF-1, DA-H1, the owner's FK-9-1)
20. `cl-dClosedLoop-0105@cab8e16c` · now `cab8e16c`, as at the baseline · tokens: `review.blocks`, `review.cost`, `review.dispose`, `review.findings`, `review.fold`, `review.left-shift`, `review.trigger`, `review.unverified` — the breakpoint program's own items, `review.trigger`, `review.dispose`, `review.fold` and `review.cost`, with `review.blocks`, `review.unverified`, `review.left-shift` and `review.findings`, which `review.dispose` reads (AF-1, FM4)
21. `cl-dClosedLoop-0106@90aa01b6` · now `90aa01b6`, as at the baseline · tokens: `REVIEW_ROUNDS`, `RUNAWAY_CEILING`, `check-unattended.sh`, `review.design.round-count`, `review.design.rounds`, `review.follow-up`, `review.max-rounds`, `unattended.sh` — follow-up closing-review rounds by `review.follow-up`, and the design audit's rounds by `review.design.rounds` and `review.design.round-count`, `REVIEW_ROUNDS` retired in the same unit with its own upgrade step moving an adopter's value into `review.design.round-count`, its readers derived by key value over code, confs and kit.toml key lists and each re-pointed, the runaway ceiling, `RUNAWAY_CEILING`, made the policy key `review.max-rounds` in the same unit with `unattended.sh` and `check-unattended.sh` re-pointed to it, and a planted round count above it refused and one equal to it admitted, still red with `unattended.sh` deleted in a scratch clone (AF-1, DA-M8, FM7, FM10, P38, the whole-design audit's C2-F3)
22. `cl-dClosedLoop-0107@a606d808` · now `a606d808`, as at the baseline · tokens: `review.recommendation`, `review.recommendation.source` — the stage-exit recommendation: every step's recommend and reason items, the score computed and the reasoning returned by the step's producing role, as `review.recommendation` and `review.recommendation.source` say (AF-1, DA-H2)
23. `cl-dClosedLoop-0108@df656363` · now `df656363`, as at the baseline · tokens: `Decided:`, `Gov-Act`, `Gov-Item`, `Gov-Session`, `Gov-Unit`, `Pass:`, `Pass: <id>`, `Pass: none`, `[sites]`, `commit`, `made-by`, `read_attribution_tokens`, `read_git_range`, `routed_commits.py`, `runs-in`, `serves` — the commit node and its kind, the `commit` native-id class registered with it: the trailer keys `Gov-Unit`, `Gov-Item` and `Pass:` mapped to `serves`, `Gov-Act` to `made-by` and `Gov-Session` to `runs-in`, `Pass:` and `Decided:` registered with one reader that offers both views today's readers answer, the union of subject and trailer ids `routed_commits.py` reads and the trailer replacing the subject that unattended's `read_attribution_tokens` reads, each consumer naming its view, runlog's `read_git_range` re-pointed to it for `Decided:`, the three re-pointed in one unit, `routed_commits.py`'s AC2 arms and unattended's commit check run on planted `Pass: none`, `Pass: <id>` and subject-id-with-`Pass: none` commits reading the same before and after, and the position engine reading them (the memory plan's `[sites]`)
24. `cl-dClosedLoop-0109@48e119fc` · now `48e119fc`, as at the baseline · tokens: `item`, `needs`, `review.breakpoints`, `supersedes` — the `item` kind in the kinds register with its factory, a repository's items composed with the loop definition at the landed revision, every check reading the composition: the needs graph acyclic with every need resolving, each input an item declares produced by an item it needs at its record kind's version, that version bumped whenever an output's meaning changes, and the floor, a gov item's `needs` and routes changed only by a pinned patch, the item kind's fixed set declared, every floor item and every step's exit item whole and in any gov item its tag, step, witness and outcome set, its open fields' widening directions declared, `needs` a constraint set, and item tags joined to dSafePassage's step gate, each seen red on a planted repository item, a planted patch of a gov item's witness or outcome set, a planted `supersedes` of a floor item and of an exit item, a planted exclusion of an item another active item needs, naming the requirer, and of an item `review.breakpoints` names, naming the key, and a planted item tag removed with no change record, green on one naming its successor (FA-1, FA-2, FA-5, the flow adoption's review)
25. `cl-dClosedLoop-0110@c46e726a` · now `c46e726a`, as at the baseline · tokens: `item.adopter.<stage>.<name>`, `review.breakpoints`, `step.adopter.<name>` — a repository's own stages, each spliced between two adjacent gov stages by pinned rows of the build's transition table, gov's five kept whole and in order, a repository stage tagged `step.adopter.<name>` and its items `item.adopter.<stage>.<name>`, the splice row an overlay kind, stage tags joined to dSafePassage's step gate, a gov stage's rename beside a splice re-pointing its transition rows, a repository stage's items and exit item witnessed as a gov step's are, its boundaries reviewed through `review.breakpoints`, seen red on a planted stage that removes, reorders or replaces a gov stage, one before Plan, one after Deploy, a splice whose rows join two non-adjacent gov stages and a stage tag removed with no change record, and green on one spliced between Test and Deploy and on a gov rename beside a splice (FA-3, P20, the flow adoption's review)
26. `cl-dClosedLoop-0111@313dbc9c` · now `313dbc9c`, as at the baseline · tokens: none, so the token arm cannot see this clause — a build's composition pinned per step: the transition record into a step carrying the composition's revision, position derived from it inside the step, the build moving at its next step boundary with its witnesses carried by the change records' successors, an item retired under it filing an order, and every policy value that names a renamed boundary re-pointed, seen on a planted rename under a build positioned on the renamed item (FA-7)
27. `cl-dClosedLoop-0112@de8c6c54` · now `de8c6c54`, as at the baseline · tokens: `declared-order`, `flow.scenario-conflict`, `flow.scenario-default`, `refuse`, `scenario` — the `scenario` kind in the kinds register and its namespace: gov's shipped scenarios, feature, amendment, patch, playbook-run and design-only, and a repository's in its overlay, each naming the scenario it extends, its admission predicate over a request's facts, its entry, and the rows of registered kinds it activates, each later build admitting its own kind's rows, a build's composition being gov's packs, the repository's overlay, the scenarios it was placed under in their declared order and its own recorded changes, pinned in its claim and in each step's transition record, two scenarios setting one field differently resolved as `flow.scenario-conflict` says, a switch of scenario only at a step boundary, in-build sequencing by a scenario naming the one that takes over at a step's exit, and `flow.scenario-default` when none admits the request, seen on two builds pinned to different scenarios positioned at once, red on a planted scenario that removes, reorders or replaces a gov stage, red on two conflicting scenarios placed together under `refuse`, and under `declared-order` settled by the declared order and recorded (the night pass two, point 1, the owner's NT-1, NT-6 and NT-7, each value's arm added by its review)
28. `cl-dClosedLoop-0113@11f77a79` · now `11f77a79`, as at the baseline · tokens: `additive-recorded`, `flow.adapt`, `off`, `owner-approves` — a build's recorded changes: rows a role proposes for its own build, applied at its next step boundary as `flow.adapt` says, a change that only adds items, roles, stages or stricter values applying unattended and recorded, one that removes, reorders or loosens waiting for the owner while the build carries on under its pinned composition, every change kept in the build folder, and at each step boundary the build's witnessed path compared with its pinned composition, a deviation filing an order, seen on a planted unrecorded skip and on a planted additive change, applied under `additive-recorded`, held for the owner under `owner-approves` and refused under `off` (the night pass two, point 1, the owner's NT-4, each value's arm added by its review)
29. `cl-dClosedLoop-0114@f3e34c2f` · now `f3e34c2f`, as at the baseline · tokens: `bypassed`, `not-applicable`, `upstream`, `used` — an item's `upstream` field naming the items whose commitments it must answer, each commitment handed as a row its return answers `used`, `bypassed` or `not-applicable` with a reason, the join computed at the return, a `bypassed` row also a finding that routes, the rows recorded on every edge and gating only on an edge whose measurement passed, the reuse edge the first to gate once a later build arms it, seen red on a planted return that drops a row on a gating edge (the night pass two, point 2, the owner's NT-10)
30. `cl-dClosedLoop-0115@cc7f99e5` · now `cc7f99e5`, as at the baseline · tokens: `flow.on-exhausted`, `flow.rework-budget`, `flow.route-backs` — the rework budget: one per build in its transition record, `flow.rework-budget`'s base plus its per-unit share for each unit frozen at Design's exit, the base alone before that freeze and for a build with no units, keyed to the build so units a loop mints cannot reset it, every repetition drawing on it, a route back, a fix pass, a review round after the first, a re-dispatch of an unwitnessed instance after a refusal, a voided witness or a lost SubagentStop, and a research or probe round trip, contention never drawing on it, a verdict staled or a merge conflicted by another build's landing re-verified in its turn, and `flow.route-backs` the per-item early limit past which that item's loop ends non-converging, a blocking item's open work promoted to a new unit while the budget remains and then ending as `flow.on-exhausted` says, and a non-blocking item's going to asks, seen red on a planted loop that mints a new unit each lap and on a planted loop before Design's exit that spends the base, and green on a planted stale verdict that draws nothing, and a closed build's record re-opened for a patch build's draw alone, each draw an appended row naming the patch build, the build's terminal state never moved by a draw, seen on a planted draw on a closed build whose state stays terminal (P39, the owner's SL-1, FK-1-5 and FK-4-5, the parked debt's review)
31. `cl-dClosedLoop-0116@d75a79f0` · now `d75a79f0`, as at the baseline · tokens: `best-effort-ending`, `close-incomplete`, `flow.on-exhausted`, `incomplete`, `park-for-owner`, `parked` — `flow.on-exhausted`: a build whose budget is spent ends and never laps again, under `best-effort-ending` the driver taking the ending its evidence supports and recording it for the owner, landing what is witnessed green with every open finding filed as an ask, or descoping the failing units to asks and landing the rest, a unit already in Test's tree reverted through a testing-to-building row that draws nothing, being an ending and not a lap (the owner's FK-4-13), or closing the build incomplete with its branch and records kept, `park-for-owner` and `close-incomplete` the other values, each ending a row of the build's transition table, any open state to `incomplete`, a terminal, on the exhaustion record, and any open state to `parked`, left only by the owner's disposition, each ending planted from those rows, a best-effort choice to lap again refused, and raising the budget the owner's alone (P39, the owner's SL-2, the whole-design audit's C2-F2)
32. `cl-dClosedLoop-0117@166df103` · now `166df103`, as at the baseline · tokens: `flow.on-exhausted`, `flow.route-backs`, `review.max-rounds`, `until-*`, `while-*` — the convergence routing: every `until-*` and `while-*` value, spec audits, closing-review follow-ups and fix passes against one acceptance red ending at a NON-CONVERGENT round, whose findings are promoted, to units while budget remains and to asks after, never folded into another round, a CEILING round's open findings promoted the same way, and every review loop, the closing review's included, held to `review.max-rounds` rounds and ended at whichever of it and `flow.route-backs` it reaches first, both promoting its open findings the same way, a blocking item's open work past `flow.route-backs` promoted to a new unit while budget remains and then ending as `flow.on-exhausted` says, and a non-blocking item's going to asks, seen red on a planted flat follow-up sequence that runs another round and on a planted sequence whose blocker and high count falls every round past `review.max-rounds`, the round after the limit refused and the report reading CEILING, and on a planted acceptance red that never greens, which must reach a terminal (P39, the owner's SL-3, keeping FR-9, the parked debt's review, the owner's FK-4-5)
33. `cl-dClosedLoop-0118@4c8ef789` · now `4c8ef789`, as at the baseline · tokens: `flow.adapt`, `flow.wait-ceiling` — the static termination check on every composition, gov's packs with the overlay, the scenarios and a build's recorded changes, at the push and at each step boundary a build moves: every state reaching a terminal and every item reachable, every cycle of the build and item transition tables passing a counted edge, every wait declaring an outcome and a deadline, a value or a key such as `flow.wait-ceiling`, scenario successor chains acyclic, a raise of a loop bound read as a loosening that waits for the owner under `flow.adapt` and is named as a widening in the overlay's update report, and every approval item that would loosen a value recommending the decline, seen red on a planted repository stage routing back into itself with an exit, which only the counted-edge rule catches, a stage with no path to a terminal, an item no transition reaches, an empty state set, which never passes, a wait declaring no deadline, a scenario successor cycle, an unattended raise of the budget, of a round count, of a retry count and of a deadline, each its own planted case, and an approval item recommending a loosening (P39, the parked debt's review, the whole-design audit's C2-F13)
34. `cl-dClosedLoop-0119@a9b53abc` · now `a9b53abc`, as at the baseline · tokens: `deviation.approval` — the deviation approval route under `deviation.approval`: by its risk, an editorial deviation its author's by dOrderedCharter's classifier, an additive or stricter one the spec writer's with the changed sections re-audited at the new revision, a loosening or a breaking one the owner's, and an owner's ruling quoted, each value seen on its planted case and red on an approver below the risk (the owner's FQ-3, P41)

### brief:acceptance

- At the Design exit, `carries.py --build dDeclaredLoop --exit` exits 0 over the build's specs: each clause in Items carried whole, or in parts 1/n to n/n, at its hash; each owned node named by a spec; each clause's tokens in its carriers.
- Each clause's own seen-red cases, stated in its text, observed as it states them.
- Every departure from a clause, or from a spec after its first pass, is a deviation record that `deviations.py` joins, and the build's departures report lists it (README rule 4).

### brief:gates

- `packet.py --check dDeclaredLoop` green before the first pass. A red on a moved instrument blob is a stop, never re-rendered away (README rule 2).
- `carries.py --build dDeclaredLoop --exit` at the Design exit while it is in service (the execution plan's `[phase-1]` retirement table).
- The close sequence of README rule 4, then the bar the driver owes at `--close`.

### brief:non-goals

- v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: frozen at the baseline, so a change to a clause is a deviation record approved by its risk.
- The 475 clauses of the other 21 chain builds' rows: carrying one needs a `**Moved:** <clause id> to dDeclaredLoop by <decision>` line.
- Any path outside `memory/builds/dDeclaredLoop/`, but the product paths a build run's units record with `--dispatch --writes`, an ask row in another build's `BACKLOG.md`, and the shared renders a landing re-renders (README rule 7).
- Another build's packet, the instruments under `memory/builds/dClosedLoop/build/*.py`, and this packet's pin lines: only `packet.py --repin <instrument>`, the owner's, moves a pin.
- The surfaces of dBoundRoles, dScopedBuild, which this build's clauses use as stand-ins only (Later builds named).

### input:spec

memory/builds/dDeclaredLoop/prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md

### task:reuse

dOrderedCharter's and dFairHearing's spec runs (3ca963bb6..ed497191d) as the procedure; seams per unit come from the reuse scouts' records.

### Charter rules

- [yagni] YAGNI: build what this unit needs now, never scaffolding for later, and delete rather than disable.
- [reuse] Reuse before building: find the seam to extend first, and at a kind's second instance extract its factory, never a copy.
- [core] One shared core with thin adapters, so logic and authorization live once; data changes additively, with defaults and an upgrade step.
- [contract] A contract two parties share lands first, as one source with generated copies and a parity gate against a live re-derivation; deployables sharing one artifact release together.
- [derive] Derive over author: status, counts, inventories and indexes are generated or declared and checked both ways, never typed beside what they describe.
- [one-fact] One fact in one place: a document points at the source that owns a value, or a gate compares the two.
- [spec] Spec before code: every product-code unit commits its spec first, a micro-spec for a mechanical change and a full design pass for a substantive one.
- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [gate] A gate never seen red is not a gate: observe its failing case, state what it does not check, and never read a skip, an unmovable probe, an exemption or an empty population as coverage.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
- [small] Work in small units, one stream each, merged to local main often; risky behaviour lands dark behind a default-off switch.
- [docs] A user-facing change is not done until its page under `help/` is current.
- [security] Security first: validate once at the write boundary, deny by default, give automation the narrowest grant, and keep secrets out of files, memory and chat.

### Protocols — read the one whose trigger holds

<!-- one-line -->
- A build of more than one pass: `memory/guides/BUILD-METHOD.md`.
- Writing a spec, or adding a write path or surface: `memory/TEMPLATE-SPEC.md`.
- Any record, index or id under `memory/`: `memory/HYGIENE.md`.
- Any review or `Workflow` fan-out: `memory/guides/REVIEW-PROTOCOL.md`.
- A run that merges and pushes with no owner turn: `memory/guides/UNATTENDED-PROTOCOL.md`.
<!-- /one-line -->

### Facts

- **Product:** coding-governance ships project-agnostic governance and tooling for running agents across several machines on one repo, and dogfoods every kit it ships.
- **Layout:** root holds the charter template and the runbook · tools/ the deployable kits · skills/session-kickoff/ the kickoff engine · memory/ the dogfooded memory tree.
- **Product context:** README.md, plus memory/DECISIONS.md for why anything is the way it is.
- **Commands:** bash tools/run-gates/run-gates.sh (the bar) · GATE_JOBS=1 for the serial rollback · GATE_FULL=1 to ignore every leg guard · bash tools/push-main.sh (the lander).
- **The merge bar:** `bash tools/run-gates/run-gates.sh`, wired into remote CI at `.github/workflows/remote-ci.yml`; the legs are single-sourced from tools/gate-legs.json; read that, never a list typed elsewhere.
- **Ids and records:** families playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL; streams playbook kickoff tooling deployer; Tier-2 reviews persist under `memory/builds/<slug>/reviews/`.
- **Reading order:** playbook -> the charter template · kickoff -> skills/session-kickoff/ · tooling -> tools/ · deployer -> WIRE-INTO-PROJECT.md.
- **Streams:** no fixed ownership — a solo tooling repo, one stream per work-unit.
- **Worktrees:** none yet — worktrees are created by hand under .claude/worktrees/.
- **Kinds:** kits are the kind: each is a directory under tools/ with a kit.toml descriptor and its own adopter. Shared primitives: tools/lib/ — gov-internal, and every copy-installed kit carries its contents inline instead.
- **Toolchain:** bash + python3 resolved by tools/lib/resolve-python.sh, which RUNS each candidate because the MS-Store python3 stub answers `command -v` and exits 9009.
- **Commit trailer:** every agent commit ends with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
