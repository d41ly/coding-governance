**Serves:** journal TOOL-dBoundRoles-1

# gov-spec-writer handoff — TOOL-dBoundRoles-1

<!-- gov:handoff role=gov-spec-writer build=dBoundRoles unit=- path=memory/builds/dBoundRoles/prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-4-spec-writer.md role-sha=06b14b1ac42a task-sha=c9444dcb3fb1 -->

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

This handoff is for build `dBoundRoles`, and names no single unit.
Not supplied, optional: `card:route`.

### brief:goal

Every unit of dBoundRoles specced and built, so that each of the 26 clauses of its row in v2's `[chain]` (Items) is carried by a spec pinned to its hash and built, each of its 15 owned nodes (Owned nodes) is built, and each of its 22 owned gaps (Gaps) is closed.

### brief:items

Each clause of the row, in its order: its id at its baseline hash, its hash now in the as-built view with the record behind any change, its tokens as `carries.py`'s token arm reads them, and its text.

1. `cl-dClosedLoop-0166@83615023` · now `83615023`, as at the baseline · tokens: none, so the token arm cannot see this clause — the roster sorted by layer: twelve core roles (orientation scout, prompt writer, planner, researcher, reuse scout, architect, spec writer, builder, tester, one reviewer with a lens per step, skeptic, synthesizer), and the deployer and maintainer as expansion roles registered through the distribution, integrations and observability layer contracts, the deployer under both distribution's and integrations', their definitions built by dShippedRelease and dTendedCadence, with the reviewer's maintenance-run and loop lenses
2. `cl-dClosedLoop-0167@0ec2ea97` · now `0ec2ea97`, as at the baseline · tokens: none, so the token arm cannot see this clause — each role's static instructions as structured fields, every limit paired with its enforcer, a ceiling of tools, write classes and gate legs, and a typed return template
3. `cl-dClosedLoop-0168@abfd5f4f` · now `abfd5f4f`, as at the baseline · tokens: none, so the token arm cannot see this clause — the work order rendered per item (the item, its inputs handed as content, its allowance, its return template, its witness), hashed into the spawn marker and bound to its act by task-sha and the session's binding record
4. `cl-dClosedLoop-0169@cdc1b7f9` · now `cdc1b7f9`, as at the baseline · tokens: none, so the token arm cannot see this clause — the prompt writer composing every role's task from the driver's details
5. `cl-dClosedLoop-0170@d33b224b` · now `d33b224b`, as at the baseline · tokens: `roles.retries` — returns through a schema-forced channel, residual failures retried by `roles.retries`
6. `cl-dClosedLoop-0171@efd80f4f` · now `efd80f4f`, as at the baseline · tokens: `role-sha` — the role index and agent files beyond every worker's reach, a tree with no index refused, `role-sha` compared at spawn
7. `cl-dClosedLoop-0172@b73b4974` · now `b73b4974`, as at the baseline · tokens: none, so the token arm cannot see this clause — shell writes held to the allowance
8. `cl-dClosedLoop-0173@a66af889` · now `a66af889`, as at the baseline · tokens: none, so the token arm cannot see this clause — the role-gate arm's field escape explained and closed
9. `cl-dClosedLoop-0174@b2c09e04` · now `b2c09e04`, as at the baseline · tokens: `none`, `review` — the `none` and `review` write classes enforced
10. `cl-dClosedLoop-0175@79a1c7d0` · now `79a1c7d0`, as at the baseline · tokens: `driver.reads`, `prompts.author`, `roles.no-spawn` — `driver.reads`, `prompts.author` and `roles.no-spawn`
11. `cl-dClosedLoop-0176@6a45e0b7` · now `6a45e0b7`, as at the baseline · tokens: `run.on-owner-question` — every fork resolved by the role that meets it and recorded, or held as `run.on-owner-question` says, its options only those the core admits, ranked the most feature-rich first and then the most expandable, its full record naming the admitted options in that ranking and the pick, seen red on a planted fork whose pick lies outside the admitted set and on one whose pick is not the first of its recorded ranking (LR-3)
12. `cl-dClosedLoop-0177@4a09db23` · now `4a09db23`, as at the baseline · tokens: `placement.check` — the orientation scout's return carrying the placement disposition and its reason, the driver recording it and running `placement.check`
13. `cl-dClosedLoop-0178@f3b0d6ea` · now `f3b0d6ea`, as at the baseline · tokens: none, so the token arm cannot see this clause — the trust mechanism (P29): inputs handed as content, each fact keyed and classed by the executor and re-cut fresh at act launch
14. `cl-dClosedLoop-0179@f74e2fff` · now `f74e2fff`, as at the baseline · tokens: `field`, `role` — the `role` and `field` tag namespaces
15. `cl-dClosedLoop-0180@145f826e` · now `145f826e`, as at the baseline · tokens: `always`, `instructions.task-charter` — the role static block carried once per spawn, the single-carry check reading `instructions.task-charter` and the harness kind and refusing `always` on a backend that loads the static block, seen red on a planted `always` there, and the block's budget covering the whole rendered static block, its charter block included, never its base body alone, seen red on a planted charter block that pushes a role over its ceiling (gap-roles-20)
16. `cl-dClosedLoop-0181@6ebedcff` · now `6ebedcff`, as at the baseline · tokens: `FANOUT_CAP`, `experiment`, `panel`, `per-unit`, `roles.effort.*`, `runtime.agents-in-flight`, `single`, `tools/roles/house/policy.toml`, `tools/roles/workflows.toml`, `twin` — the shapes, extending each `tools/roles/workflows.toml` entry with its kind (`single`, `per-unit`, `panel`, `twin`, and `experiment`, whose cases, variants, bounded fan, scorer or blind judge and re-runs keyed by variant and effort come from aScoutedSeam's benchmark, which dFairHearing lands, night pass point 2), fan, checklist, orientation template, merge, twin rule and an agent cap bounded by `runtime.agents-in-flight` (revised by the night pass two, point 7: it was agent-cap's `FANOUT_CAP`), with effort read from the `roles.effort.*` keys first and from `tools/roles/house/policy.toml` by workflow and stage only where no key is set, until dConvergedCharter retires the seed (M7, FA-6, the flow adoption's review), the orientation scout at medium and the builder at high (RS-2), and the registry's readers rewritten in the same unit
17. `cl-dClosedLoop-0182@0cc5ed88` · now `0cc5ed88`, as at the baseline · tokens: `[sites]`, `answers`, `item=`, `test.seed` — every work order carrying its marker with `item=`, and every return naming the work order it `answers`, today's unmarked handoffs and returns a legacy population `test.seed` seeds, so only new ones are refused (the memory plan's `[sites]`)
18. `cl-dClosedLoop-0183@46564bcb` · now `46564bcb`, as at the baseline · tokens: `gov-session` — its own upgrade steps: an adopter's rendered agents renamed as the two reviewer roles merge, and the role index re-rendered (P38, the night pass two's point 4 moving `gov-session`'s retirement to Runtime, the owner's NT-21)
19. `cl-dClosedLoop-0184@923d7266` · now `923d7266`, as at the baseline · tokens: `house/*.md`, `house/policy.toml` — the roles kit's house text files, `house/*.md`, moved into the repository's overlay as level-5 units selecting their role, with their own upgrade step, `house/policy.toml` keeping the route this row's shapes give it (IA-1, P38, the folds' review)
20. `cl-dClosedLoop-0185@ce70dc70` · now `ce70dc70`, as at the baseline · tokens: `BODY_CEILINGS`, `WORKFLOW_NAMES`, `add`, `amends`, `roles.json`, `supersedes`, `workflow`, `workflows.toml` — a repository's roles and workflow entries, in the `workflow` namespace, gov's `workflows.toml` entries tagged in it beside them, each role with its structured fields, typed return and ceiling, declaring the shape kinds it runs in, `BODY_CEILINGS` a role field and `WORKFLOW_NAMES` the workflow registry, never tables closed in code, the matrix arms and the spawn guard reading the composition, a repository role acting in a gov item through a pinned patch of its actor when it returns the item's template, its ceiling covers the item's allowance and it declares the item's shape kind, the role kind's fixed set declared, the matrix arms, each core role's write class and return schema, and the cycle roles, the prompt writer and the driver, whole, its open fields' widening directions declared, tools, write classes and the gate grant widening on `add` and a ceiling as it rises, role and workflow tags joined to dSafePassage's step gate, and the harness paths `roles.json` names resolved in the install, each seen red on a planted role in a shape kind it does not declare, an actor patch whose role lacks the item's template, a harness path the install lacks, a planted patch or widening of a core role's write class or return schema, a planted `supersedes` of the driver, a planted exclusion of a role an active item names as its actor and of a leg a role's gate grant names, each naming the requirer, a planted exclusion leaving a role acting in no item, the role excluded with it or the matrix arm red, a planted role or workflow tag removed with no change record, green on one naming its successor, and an `amends` naming a workflow tag gov does not ship, green on one resolving to a gov workflow entry (FA-1, FA-4, FA-5, the flow adoption's review)
21. `cl-dClosedLoop-0186@e356242a` · now `e356242a`, as at the baseline · tokens: `[effort]`, `[gates]`, `default`, `handoff.py`, `harness-args`, `resolve_stage_efforts`, `roles.effort.<role>`, `roles.effort.<workflow>.<stage>`, `roles.effort.default`, `roles.model.<role>.<harness>`, `stage-efforts` — `roles.effort.<role>`, `roles.effort.<workflow>.<stage>`, `roles.effort.default` and `roles.model.<role>.<harness>`, a stage's effort read from its stage key, then its role's key, then `roles.effort.default`, then the role's declared value, as `resolve_stage_efforts` reads today, a role's model on a harness from its key for that harness, then that harness adapter's equivalent of its declared value, seen red on a planted key for one harness read on another, `default` reserved as a role name, and the gate grant a field of each role's definition, patched in the overlay, `resolve_stage_efforts`, R12, `handoff.py`'s `stage-efforts` and `harness-args` and the gate check re-pointed in the same unit to the keys through dGroundRules's reader and to the grant, the house file's `[effort]` and `[gates]` read only where no key or grant field is set, until dConvergedCharter retires the seed, each seen red on a planted house-file effort that differs from a set key, the key's value read, on a planted role-level effort a stage must inherit, and on a planted house-file `[gates]` row that differs from a role's grant, the grant read (FA-6, the flow adoption's review)
22. `cl-dClosedLoop-0187@5afc67cc` · now `5afc67cc`, as at the baseline · tokens: none, so the token arm cannot see this clause — workflow entries as data: each entry's ordered stages, every stage naming its role, fan, cap, effort and the rows it receives and returns, the five kinds kept as named defaults over them, a stage's cap at or under the repository's agent limit, and a scenario's workflow entries and role rows composed per build, seen on a planted two-stage entry of mixed roles and red on a stage whose cap exceeds the limit (the night pass two, point 1, the owner's NT-8)
23. `cl-dClosedLoop-0188@23b122f8` · now `23b122f8`, as at the baseline · tokens: `.governance/policy.toml`, `roles.effort.*`, `roles.effort.default` — the prompt writer's default frame for a role item, aScoutedSeam's skeleton in order: the role and its job's kind, the material, the boundaries, the population from the item's lister or the needs-then-sketch steps that build it, the upstream rows, the row contract with an escape verdict and proof of search, the added rows, the no-stop line, and the return contract last, every list in the output bounded, its work orders carrying the upstream rows and its returns answering them, and effort the owner's setting under the `roles.effort.*` keys, medium by default with no role declaring less, set below medium only by the owner's explicit authorization in `.governance/policy.toml`, the guarded policy file, and never by an agent, a role's proposal, a scenario or a build's own change, the check reading an effort's provenance from that file alone and refusing a house-file effort below medium while the house file stays a fallback, seen red on a planted effort below medium that no owner write carries, on a role key, a stage key and `roles.effort.default` each, and on a planted house-file effort below medium, and green on a low effort the owner writes to the policy file under its guard and proof, which runs at low (the night pass two, point 2, the owner's NT-10 and NT-12, the answers' review)
24. `cl-dClosedLoop-0189@8d7be499` · now `8d7be499`, as at the baseline · tokens: none, so the token arm cannot see this clause — the prompt writer's framing checked at render, every anchor it points at resolving to a fact the work order hands, seen red on a planted anchor to nothing (the night pass two, point 4)
25. `cl-dClosedLoop-0190@03bbbf1e` · now `03bbbf1e`, as at the baseline · tokens: `tools/hooks/agent-cap.js` — agent-cap's spawn guard and harness admission moved into the roles pack, admission comparing a harness file with its landed blob so an edited harness never runs before the bar has read it, and `tools/hooks/agent-cap.js` retired with an upgrade step once its last rule has moved, its readers inventoried by value, the charter's agent-cap line among them (the night pass two, point 7, the owner's NT-27)
26. `cl-dClosedLoop-0191@66acd199` · now `66acd199`, as at the baseline · tokens: `run.on-owner-question` — the typed refusal return in every role's template, its refusing rule, its remedy and the remedy's actor, who is the refused agent, its producer, the driver, the owner or another build, the outcome table routing a remedy the refused actor cannot perform within its grant at once to that actor and never re-offering the item to the refused agent, and `run.on-owner-question`'s best effort choosing only among endings once a build's budget is spent, seen on a planted refusal of each actor kind (P39, the owner's SL-2 and SL-7)

### brief:acceptance

- At the Design exit, `carries.py --build dBoundRoles --exit` exits 0 over the build's specs: each clause in Items carried whole, or in parts 1/n to n/n, at its hash; each owned node named by a spec; each clause's tokens in its carriers.
- Each clause's own seen-red cases, stated in its text, observed as it states them.
- Every departure from a clause, or from a spec after its first pass, is a deviation record that `deviations.py` joins, and the build's departures report lists it (README rule 4).

### brief:gates

- `packet.py --check dBoundRoles` green before the first pass. A red on a moved instrument blob is a stop, never re-rendered away (README rule 2).
- `carries.py --build dBoundRoles --exit` at the Design exit while it is in service (the execution plan's `[phase-1]` retirement table).
- The close sequence of README rule 4, then the bar the driver owes at `--close`.

### brief:non-goals

- v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: frozen at the baseline, so a change to a clause is a deviation record approved by its risk.
- The 483 clauses of the other 21 chain builds' rows: carrying one needs a `**Moved:** <clause id> to dBoundRoles by <decision>` line.
- Any path outside `memory/builds/dBoundRoles/`, but the product paths a build run's units record with `--dispatch --writes`, an ask row in another build's `BACKLOG.md`, and the shared renders a landing re-renders (README rule 7).
- Another build's packet, the instruments under `memory/builds/dClosedLoop/build/*.py`, and this packet's pin lines: only `packet.py --repin <instrument>`, the owner's, moves a pin.
- The surfaces of dConvergedCharter, which this build's clauses use as stand-ins only (Later builds named).

### input:spec

memory/builds/dBoundRoles/prompts/2026-10-26-prompt-TOOL-dBoundRoles-45-round2-fix-brief.md

### task:reuse

the dWitnessedBar spec run's route (scouts, brief, spec writers, tier2-review.js spec audits); tools/roles/ (render_agents.py, check_roles.py, roles_lib.py, workflows.toml), tools/hooks/agent-cap.js, tools/hooks/scratch-guard.js.

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
