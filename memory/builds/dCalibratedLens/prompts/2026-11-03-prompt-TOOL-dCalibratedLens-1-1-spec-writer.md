**Serves:** journal TOOL-dCalibratedLens-1

# gov-spec-writer handoff — TOOL-dCalibratedLens-1

<!-- gov:handoff role=gov-spec-writer build=dCalibratedLens unit=- path=memory/builds/dCalibratedLens/prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-1-spec-writer.md role-sha=dcd8416ea3d2 task-sha=e8869d92e027 -->

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
after every writer returns. At a spec audit's disposal, a correction to an unbuilt sibling's spec
rewrites that sibling's text, with a rev bump and a revision-log line naming the repair unit and
the review record by its file stem, and a CLOSED sibling stays frozen.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names, every unit named by its unit id as
the roster spells it. Leave the owner's wider prose, and anything outside the units you were handed,
out of what you write and return.

## Task

This handoff is for build `dCalibratedLens`, and names no single unit.
Not supplied, optional: `card:route`.

### brief:goal

Every unit of dCalibratedLens specced and built, so that each of the 17 clauses of its row in v2's `[chain]` (Items) is carried by a spec pinned to its hash and built, each of its 15 owned nodes (Owned nodes) is built, and each of its 13 owned gaps (Gaps) is closed.

### brief:items

Each clause of the row, in its order: its id at its baseline hash, its hash now in the as-built view with the record behind any change, its tokens as `carries.py`'s token arm reads them, and its text.

1. `cl-dClosedLoop-0458@5429e502` · now `5429e502`, as at the baseline · tokens: `review.<stage>.effort` — each stage review's lenses and effort: lenses for Plan, Test, Deploy and Maintain, drawn from dFairHearing's catalogue, run at `review.<stage>.effort` through dDeclaredLoop's breakpoints (AF-1)
2. `cl-dClosedLoop-0459@facc646b` · now `facc646b`, as at the baseline · tokens: none, so the token arm cannot see this clause — the shared value ledger
3. `cl-dClosedLoop-0460@401ecbd8` · now `401ecbd8`, as at the baseline · tokens: `review.loop.cadence` — the Loop Review, registered as a cadence step of the observability expansion and run as `review.loop.cadence` says, weekly, monthly or every n landings, its lease keyed by the selected period, each value seen on its planted case
4. `cl-dClosedLoop-0461@ea09b304` · now `ea09b304`, as at the baseline · tokens: `budgets.*` — caps re-derived from evidence and review cost, the `budgets.*` values
5. `cl-dClosedLoop-0462@cad135ef` · now `cad135ef`, as at the baseline · tokens: none, so the token arm cannot see this clause — instruction effectiveness measured from returns and findings that cite unit tags, the Loop Review pruning units that bear no load and tightening those broken often, and proposing a charter amendment for a rule whose override records recur, so a standing override becomes an amendment rather than a habit (foundations, step 1, the owner's FK-11-1)
6. `cl-dClosedLoop-0463@33710e39` · now `33710e39`, as at the baseline · tokens: `measured`, `memory.item-budget` — each role's `memory.item-budget` derived from its p90 over 30 sliced work orders under `measured`, through the guarded policy command, the owner's own setting for a role winning (MS-2)
7. `cl-dClosedLoop-0464@b1127f93` · now `b1127f93`, as at the baseline · tokens: `review.cost` — the value ledger's shape rows, priced from the shape-run rows `review.cost` writes for review acts and the journal reconcile writes for every other
8. `cl-dClosedLoop-0465@4003d147` · now `f1db8527` by deviation `2026-11-02-build-TOOL-dCalibratedLens-8-deviation-81` · tokens: `code`, `review.dispose` — the not-in-view cause added to `review.dispose`'s record, computed from the authors' committed work orders, the handoff files under the build's `prompts/` folder whose marker names an authoring role, every tracked path they spell being the view, a work order rendering the slices, the `map` slot and the `code` slot it hands, so the three inputs are read where they were handed rather than from a separate manifest (night pass, point 3), and the Loop Review's reading of its share, proposing the map's retirement if it does not fall by 15 points over 38 confirmed findings
9. `cl-dClosedLoop-0466@f36d2aed` · now `f36d2aed`, as at the baseline · tokens: none, so the token arm cannot see this clause — probe cost priced in the value ledger, and compactions counted per item kind as a sizing signal (night pass, points 2 and 5)
10. `cl-dClosedLoop-0467@58bd6ee5` · now `0bd9d49f` by deviation `2026-11-02-build-TOOL-dCalibratedLens-10-deviation-101` · tokens: none, so the token arm cannot see this clause — instruction evals: a replay suite of recorded items with known outcomes, scored through dFairHearing's scorer factory, its scoring re-run as a held leg when an instruction unit changes, the leg red on each case whose replay the change made owed until the replay is recorded, a confirmed finding whose cause is an instruction adding a case (night pass, point 6)
11. `cl-dClosedLoop-0468@8f541e2a` · now `b4b68e80` by deviation `2026-11-02-build-TOOL-dCalibratedLens-11-deviation-111` · tokens: none, so the token arm cannot see this clause — the Loop Review's delivery metrics: lead time, from the first commit adding the build's README to the landing commit, each a committer time every node reads from git and the landing read from the landing record DEPL-dShippedRelease-1 writes, landing frequency, change failure rate, time to restore, first-pass verdict rate, route-backs per build and scope drift (night pass, point 6), and the owner queue's depth, read with no bound (NP-18)
12. `cl-dClosedLoop-0469@653feb80` · now `653feb80`, as at the baseline · tokens: none, so the token arm cannot see this clause — the Loop Review pricing cost per item kind from trace rows (P35)
13. `cl-dClosedLoop-0470@dfafc75a` · now `dfafc75a`, as at the baseline · tokens: `lens`, `review.opt-in` — the `lens` kind and namespace, gov's lenses tagged in it and their briefs made units, a repository's lenses from its overlay, chosen by `review.opt-in`, the lens kind's fixed set declared, the five lens slots among it, and lens tags joined to dSafePassage's step gate, seen on a planted repository lens swapped into a run, and red on a planted patch adding a sixth slot, a planted exclusion of a lens `review.opt-in` names, naming the key, and a planted lens tag removed with no change record, green on one naming its successor (FA-1, FA-5, the flow adoption's review)
14. `cl-dClosedLoop-0471@453f9872` · now `453f9872`, as at the baseline · tokens: `flow.promote`, `instructions.edit`, `off`, `owner-only`, `promoted-from` — lens removal by a swap or by excluding a default lens, its slot then filled by an opt-in, a repository lens recording a replay result when one ran and never owing one, and scenario promotion as `flow.promote` says: the Loop Review proposing a scenario from a recorded change two or more builds carried, the owner ratifying it through `instructions.edit` with `promoted-from` edges to those changes, builds in flight moving to it only at a step boundary and only if they comply, a declined proposal recorded, keyed by the change's content, and not proposed again until a build carries a changed form, under `owner-only` no proposal raised and the owner promoting through `instructions.edit` alone, and under `off` any promotion refused, each value seen on its planted case, a declined proposal the next review does not raise among them (the night pass two, point 1, the owner's NT-5 and NT-9, the decline and each value's arm added by the night pass two's review)
15. `cl-dClosedLoop-0472@bf8d8ee5` · now `bf8d8ee5`, as at the baseline · tokens: none, so the token arm cannot see this clause — each size breach priced in the value ledger by its bytes and its reads, and the Loop Review raising an owner item for a breach that persists or grows across reviews, counting only new or grown breaches, so an advisory cap keeps a brake (the night pass two, point 5, the owner's NT-23)
16. `cl-dClosedLoop-0473@17126ed2` · now `17126ed2`, as at the baseline · tokens: none, so the token arm cannot see this clause — the stall and loop classes Runtime journals, no progress, a repeat, a budget spent, a deadline passed, a breaker open and a cycle across builds, trended per scenario, item and rule, and the rework budget, the deadlines and the thresholds re-derived from that evidence once 30 builds have run under them, seen red on a planted class journaled and left out of the trend (P39, P9, the parked debt's review)
17. `cl-dClosedLoop-0474@b1852db0` · now `b1852db0`, as at the baseline · tokens: `trace.cost` — the node beats and the pools' ledgers trended, and the reservation estimate per item kind re-derived from `trace.cost` (P40, P9)

### brief:acceptance

- At the Design exit, `carries.py --build dCalibratedLens --exit` exits 0 over the build's specs: each clause in Items carried whole, or in parts 1/n to n/n, at its hash; each owned node named by a spec; each clause's tokens in its carriers.
- Each clause's own seen-red cases, stated in its text, observed as it states them.
- Every departure from a clause, or from a spec after its first pass, is a deviation record that `deviations.py` joins, and the build's departures report lists it (README rule 4).

### brief:gates

- `packet.py --check dCalibratedLens` green before the first pass. A red on a moved instrument blob is a stop, never re-rendered away (README rule 2).
- `carries.py --build dCalibratedLens --exit` at the Design exit while it is in service (the execution plan's `[phase-1]` retirement table).
- The close sequence of README rule 4, then the bar the driver owes at `--close`.

### brief:non-goals

- v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: frozen at the baseline, so a change to a clause is a deviation record approved by its risk.
- The 492 clauses of the other 21 chain builds' rows: carrying one needs a `**Moved:** <clause id> to dCalibratedLens by <decision>` line.
- Any path outside `memory/builds/dCalibratedLens/`, but the product paths a build run's units record with `--dispatch --writes`, an ask row in another build's `BACKLOG.md`, and the shared renders a landing re-renders (README rule 7).
- Another build's packet, the instruments under `memory/builds/dClosedLoop/build/*.py`, and this packet's pin lines: only `packet.py --repin <instrument>`, the owner's, moves a pin.

### input:spec

memory/builds/dCalibratedLens/prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-departures-brief.md

### task:reuse

the seams the scout names, recorded per spec §10.

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
