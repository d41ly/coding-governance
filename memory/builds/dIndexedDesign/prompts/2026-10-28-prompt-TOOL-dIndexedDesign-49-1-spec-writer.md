**Serves:** journal TOOL-dIndexedDesign-49

# gov-spec-writer handoff — TOOL-dIndexedDesign-49

<!-- gov:handoff role=gov-spec-writer build=dIndexedDesign unit=TOOL-dIndexedDesign-49 path=memory/builds/dIndexedDesign/prompts/2026-10-28-prompt-TOOL-dIndexedDesign-49-1-spec-writer.md role-sha=06b14b1ac42a task-sha=244c151c14d3 -->

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

This handoff is for build `dIndexedDesign`, unit `TOOL-dIndexedDesign-49`.
Not supplied, optional: `card:route`.

### brief:goal

Every unit of dIndexedDesign specced and built, so that each of the 16 clauses of its row in v2's `[chain]` (Items) is carried by a spec pinned to its hash and built, each of its 28 owned nodes (Owned nodes) is built, and each of its 13 owned gaps (Gaps) is closed.

### brief:items

Each clause of the row, in its order: its id at its baseline hash, its hash now in the as-built view with the record behind any change, its tokens as `carries.py`'s token arm reads them, and its text.

1. `cl-dClosedLoop-0383@77f2882f` · now `77f2882f`, as at the baseline · tokens: `design.handoff`, `ready-plus-audit` — the Design-to-Build hand-off as `design.handoff` says, derived READY, READY plus a Tier-2 audit, or status and tier, each value seen on its planted case, and a planted `ready-plus-audit` hand-off with no audit seen red
2. `cl-dClosedLoop-0384@372bd58d` · now `372bd58d`, as at the baseline · tokens: `design.overlap`, `refuse` — the design index, an overlap between live designs that neither acknowledges warned at spec-write and kickoff, refused until acknowledged, or shown in the index view only, as `design.overlap` says, each value seen on a planted overlapping roster, an unacknowledged overlap under `refuse` seen red
3. `cl-dClosedLoop-0385@7bdb7329` · now `7bdb7329`, as at the baseline · tokens: none, so the token arm cannot see this clause — design review by policy, its opt-in, effort and audit guard, the stage-exit recommendation being dDeclaredLoop's (AF-1)
4. `cl-dClosedLoop-0386@1f72161f` · now `1f72161f`, as at the baseline · tokens: none, so the token arm cannot see this clause — reuse and alternatives backed by recorded probes
5. `cl-dClosedLoop-0387@f264e3f3` · now `f264e3f3`, as at the baseline · tokens: `experiment` — the research harness, built on dBoundRoles' `experiment` shape (night pass, point 2, and WK-2)
6. `cl-dClosedLoop-0388@deaac21c` · now `deaac21c`, as at the baseline · tokens: none, so the token arm cannot see this clause — agreement and tier checks
7. `cl-dClosedLoop-0389@158d7ac4` · now `158d7ac4`, as at the baseline · tokens: none, so the token arm cannot see this clause — the spec measured, recommendations emitted, and the spec redesigned as a structured, tagged contract
8. `cl-dClosedLoop-0390@a096f77c` · now `a096f77c`, as at the baseline · tokens: `design.forks`, `design.reentry` — the feature level (build, features, units) with each feature's interfaces declared structurally, two-level re-entry by `design.reentry`, additive-versus-breaking interface classification, fork resolution by `design.forks`
9. `cl-dClosedLoop-0391@17b40187` · now `17b40187`, as at the baseline · tokens: none, so the token arm cannot see this clause — spec sections named by tag across tiers
10. `cl-dClosedLoop-0392@c9f3c2f0` · now `c9f3c2f0`, as at the baseline · tokens: `check-playbook` — the playbook record kind: dScriptedRepeat's canon, its declaration block, pieces and sets identified by hash, amendment by proposal, and `check-playbook` as Design's pack (night pass, point 1)
11. `cl-dClosedLoop-0393@c8409a33` · now `c8409a33`, as at the baseline · tokens: none, so the token arm cannot see this clause — the playbook set record and its set check, registered at Test's leg-pack point (night pass, point 1)
12. `cl-dClosedLoop-0394@97e00df6` · now `97e00df6`, as at the baseline · tokens: `decides=`, `design.seams`, `implements=` — the structured spec declaring `implements=` and `decides=` edges, and `design.seams` reading a tag's bundle (night pass, point 4)
13. `cl-dClosedLoop-0395@07a81090` · now `07a81090`, as at the baseline · tokens: none, so the token arm cannot see this clause — the reuse scout's return under aScoutedSeam's M1c contract: needs and a concrete sketch before the search, the anchors resolved, a convention census, at most twelve seams and five MUSTs, a MUST defined as an existing implementation that new code would duplicate, the unmet needs, and its MUST and SHOULD seams handed on as rows (the night pass two, point 2, the owner's NT-10)
14. `cl-dClosedLoop-0396@bf718415` · now `bf718415`, as at the baseline · tokens: none, so the token arm cannot see this clause — the reuse scout's return also naming at most five bug classes by intent, read from the catalogue's one-line index against the unit's needs and sketch, each with its reason, for the unit's spec to carry, armed only once a replay over the closed code reviews, each scout given its unit's spec and the index as they stood before the build and never the review, scores above the anchor ranking's top five with a precision of at least 20%, and retired unarmed if it does not (the night pass two, point 6, the owner's NT-26)
15. `cl-dClosedLoop-0397@155d665e` · now `155d665e`, as at the baseline · tokens: `always`, `design.overlaps`, `design.streams`, `design.streams-when`, `off`, `opt-in` — the planner's `design.streams` item after `design.overlaps`, run as `design.streams-when` says, opt-in by default: a planning workflow, its agents at the planner's effort, medium unless the owner sets another, grouping the roster's units into streams that several node units can take at once, by their declared order, write sets and the overlap record, its stream plan written as dTotalRecall's stream-plan kind, which dWellOiledMachine's pick and a head where one exists read, needing no head, seen red on a planted stream pairing two units whose write sets overlap and on each value of `design.streams-when` planted, `off` running no planning workflow, `always` one on every build and `opt-in` one only where the brief or the owner asks (the owner's CL-3 and FK-3-3, the parked debt's review)
16. `cl-dClosedLoop-0398@f6f6546a` · now `f6f6546a`, as at the baseline · tokens: `design.coverage`, `design.coverage.semantic`, `design.ready`, `implements=` — the design coverage under `design.coverage` and `design.coverage.semantic`: dTrueNorth's join read at each Design exit and at each spec's revision, `design.ready` gaining an UNCARRIED class, `implements=` edges taking a clause target, the design index rendering coverage, and at each Design exit the lens reading each carried clause with the sections it rests on and the owner reading the coverage report, seen red on a planted dropped clause and on a planted carrier that keeps every token and contradicts its clause, which only the lens sees (the owner's FQ-2, P41)

### brief:acceptance

- At the Design exit, `carries.py --build dIndexedDesign --exit` exits 0 over the build's specs: each clause in Items carried whole, or in parts 1/n to n/n, at its hash; each owned node named by a spec; each clause's tokens in its carriers.
- Each clause's own seen-red cases, stated in its text, observed as it states them.
- Every departure from a clause, or from a spec after its first pass, is a deviation record that `deviations.py` joins, and the build's departures report lists it (README rule 4).

### brief:gates

- `packet.py --check dIndexedDesign` green before the first pass. A red on a moved instrument blob is a stop, never re-rendered away (README rule 2).
- `carries.py --build dIndexedDesign --exit` at the Design exit while it is in service (the execution plan's `[phase-1]` retirement table).
- The close sequence of README rule 4, then the bar the driver owes at `--close`.

### brief:non-goals

- v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: frozen at the baseline, so a change to a clause is a deviation record approved by its risk.
- The 493 clauses of the other 21 chain builds' rows: carrying one needs a `**Moved:** <clause id> to dIndexedDesign by <decision>` line.
- Any path outside `memory/builds/dIndexedDesign/`, but the product paths a build run's units record with `--dispatch --writes`, an ask row in another build's `BACKLOG.md`, and the shared renders a landing re-renders (README rule 7).
- Another build's packet, the instruments under `memory/builds/dClosedLoop/build/*.py`, and this packet's pin lines: only `packet.py --repin <instrument>`, the owner's, moves a pin.

### input:spec

memory/builds/dIndexedDesign/prompts/2026-10-28-prompt-TOOL-dIndexedDesign-47-promoted-fix-brief.md

### task:reuse

tools/memory-tree/design_lib.py (binding lines), tools/check-spec-tokens.py (the carries join), tools/unattended/check-playbook.sh (playbook check), .claude/agents/gov-reuse-scout.md (the scout's return); scouts confirm per unit.

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
