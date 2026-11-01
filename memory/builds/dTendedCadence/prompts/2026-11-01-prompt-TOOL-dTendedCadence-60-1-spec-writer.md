**Serves:** journal TOOL-dTendedCadence-60

# gov-spec-writer handoff — TOOL-dTendedCadence-60

<!-- gov:handoff role=gov-spec-writer build=dTendedCadence unit=TOOL-dTendedCadence-60 path=memory/builds/dTendedCadence/prompts/2026-11-01-prompt-TOOL-dTendedCadence-60-1-spec-writer.md role-sha=06b14b1ac42a task-sha=c110820ca6df -->

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

This handoff is for build `dTendedCadence`, unit `TOOL-dTendedCadence-60`.
Not supplied, optional: `card:route`.

### brief:goal

Every unit of dTendedCadence specced and built, so that each of the 18 clauses of its row in v2's `[chain]` (Items) is carried by a spec pinned to its hash and built, each of its 24 owned nodes (Owned nodes) is built, and each of its 14 owned gaps (Gaps) is closed.

### brief:items

Each clause of the row, in its order: its id at its baseline hash, its hash now in the as-built view with the record behind any change, its tokens as `carries.py`'s token arm reads them, and its text.

1. `cl-dClosedLoop-0442@53466888` · now `d7b64b62` by deviation `2026-11-01-build-TOOL-dTendedCadence-1-deviation-11` · tokens: none, so the token arm cannot see this clause — the Maintain run as its step checklist, `[[item]]` rows in the flow's item schema, launched and leased by the executor's cadence (`run_cadence_period`) and walked in their `needs` order by `tools/drift-audit/maintain.py` until the flow's executor walks a cadence program keyed by (cadence, period), never a recipe-mode playbook
2. `cl-dClosedLoop-0443@06da9bab` · now `06da9bab`, as at the baseline · tokens: `maintain.cadence`, `maintain.events`, `maintain.host`, `release-verify-failed` — the cadence, on Runtime's hosts: Maintain run on `maintain.host` per `maintain.cadence`, and its event runs for the events `maintain.events` names, `release-verify-failed` rendered not installed where integrations is not installed, each value seen on its planted case
3. `cl-dClosedLoop-0444@f4079d73` · now `f4079d73`, as at the baseline · tokens: none, so the token arm cannot see this clause — the safe-fix set
4. `cl-dClosedLoop-0445@768c9f5b` · now `768c9f5b`, as at the baseline · tokens: `maintain.reading-admission: refuse-unowned`, `report-unowned` — detectors with owners, a reading with no derivable owner or no pin refused at registration under `maintain.reading-admission: refuse-unowned` and admitted and reported unowned under `report-unowned`, nothing filed for it until an owner is derived, each value seen on a planted ownerless reading
5. `cl-dClosedLoop-0446@617f13e8` · now `617f13e8`, as at the baseline · tokens: none, so the token arm cannot see this clause — map freshness
6. `cl-dClosedLoop-0447@d34b1bee` · now `d34b1bee`, as at the baseline · tokens: `observability.run-record` — the maintenance record, and the run record the journal reader writes when the journal shows a run closed, as `observability.run-record` says, for every run, for a run with an anomaly or never, each value seen on a planted run
7. `cl-dClosedLoop-0448@6053b724` · now `6053b724`, as at the baseline · tokens: `check-dead-paths.sh`, `memory/` — a detector for dead pointers, owned by Maintain, over both populations it absorbs: drift-audit's dangling-pointer signal over the agent's auto-memory, and `check-dead-paths.sh`'s, the text outside `memory/`, map dossiers and gotcha pages that name a deleted or renamed file, keeping that script's merge-bar leg at Test's leg-pack point (NP-22)
8. `cl-dClosedLoop-0449@503e50af` · now `503e50af`, as at the baseline · tokens: none, so the token arm cannot see this clause — Maintain delivered as a cadence step of the observability expansion, the Loop Review's step registered by dCalibratedLens, detectors registered by layer, patch intakes rendered from keyed detector readings, event runs keyed by event
9. `cl-dClosedLoop-0450@ff08f57f` · now `ff08f57f`, as at the baseline · tokens: `maintain.retrofit-heat`, `off`, `retrofit.cadence: hot-first` — `maintain.retrofit-heat`, filing each period's sweep as a patch build under `retrofit.cadence: hot-first`'s standing ask and sweep asks only under `off`, and the progress cell's share of reads
10. `cl-dClosedLoop-0451@8cb0a7a7` · now `8cb0a7a7`, as at the baseline · tokens: none, so the token arm cannot see this clause — the maintainer's definition, Maintain's filings, registered through dBoundRoles's layer contract
11. `cl-dClosedLoop-0452@6c0e77f7` · now `6c0e77f7`, as at the baseline · tokens: `repeat` — a cyclic playbook's cadence item, filing `repeat` intakes (night pass, point 1)
12. `cl-dClosedLoop-0453@42f1bc0c` · now `42f1bc0c`, as at the baseline · tokens: none, so the token arm cannot see this clause — a detector for bundle members whose code changed while their head line did not (night pass, point 4)
13. `cl-dClosedLoop-0454@ef9a7f8a` · now `3bb6c0f8` by deviation `2026-11-01-build-TOOL-dTendedCadence-13-deviation-131` · tokens: `maintain.security-review` — the recurring security review, a cadence item running dFairHearing's security lens over each period's landed range, from the last reviewed head to the landed tip, as `maintain.security-review` says, weekly by default (NP-19)
14. `cl-dClosedLoop-0455@238dcec0` · now `238dcec0`, as at the baseline · tokens: `maintain.file`, `maintain.fixes`, `maintain.tiers: bands`, `probe.trigger` — readings tiered by their deviation from their pins under `maintain.tiers: bands`, to log, to diagnose read-only or to act within `maintain.fixes`, each reading declaring its band edges beside its pin at registration and admission refusing one without them, the log band a journal line and a count in the maintenance record with nothing filed, the diagnose band a read-only probe through `probe.trigger` with the reading as its observation, its record attached to the ask `maintain.file` files, and the act band routed by its fix, each band seen on its planted reading and a reading registered without edges refused (NP-21, the owner's FK-5-5)
15. `cl-dClosedLoop-0509@9b0389cc` · now `9b0389cc`, as at the baseline · tokens: `file-ask`, `maintain.file`, `maintain.on-breach`, `red-leg`, `report` — `maintain.on-breach`'s three values at `maintain.file`: `file-ask` filing the ask into Plan's triage, `red-leg` filing nothing and registering a leg at Test's leg-pack point that reads the newest maintenance record offline, as distribution's currency leg reads its own record, red while an offender stands over its pin, and `report` filing nothing and sending the maintenance record through the notification adapter, each value seen on its planted offender (the owner's FK-5-5, the whole-design audit's B5-F11)
16. `cl-dClosedLoop-0456@a3633e7f` · now `a3633e7f`, as at the baseline · tokens: `[gates]`, `runtime.act-ceiling` — readings for an act launched with no outcome past `runtime.act-ceiling`, a node's run left unrecorded, a pushed commit missing a required key, over commits from the commit-key leg's registration on, the earlier history outside its population, and a standing directive found in the node's auto-memory and not promoted, a node-scoped reading filed as an ask and never a bar or push leg (P35, the memory plan's `[gates]`)
17. `cl-dClosedLoop-0457@2214ebfb` · now `2214ebfb`, as at the baseline · tokens: `maintain.interpreter-eol` — a detector filing an intake six months before the interpreter floor's end of life, as `maintain.interpreter-eol` says (AP-35)
18. `cl-dClosedLoop-0499@2480b868` · now `2480b868`, as at the baseline · tokens: `closed_specs`, `cutoff_keys_armed`, `gh`, `handkept`, `ledger_rows`, `maintain.dead-after`, `maintain.reading-tree`, `non_terminal_specs` — drift-audit's five gateable drift signals moved to core legs at Test's leg-pack point, each owned by the layer whose records it grades, `ledger_rows` by memory, `non_terminal_specs` and `closed_specs` by flow, and `handkept` and `cutoff_keys_armed` by instruction, so the merge bar reaches none through the observability kit, repo-scoped readings taken as `maintain.reading-tree` says, in a clean checkout at the base SHA or in the node's worktree, each value seen on a planted reading that differs between the two trees, and the remote-CI drift signal registered as a reading with its liveness, dead past `maintain.dead-after` readings and filed to its source, seen on a planted node without `gh`

### brief:acceptance

- At the Design exit, `carries.py --build dTendedCadence --exit` exits 0 over the build's specs: each clause in Items carried whole, or in parts 1/n to n/n, at its hash; each owned node named by a spec; each clause's tokens in its carriers.
- Each clause's own seen-red cases, stated in its text, observed as it states them.
- Every departure from a clause, or from a spec after its first pass, is a deviation record that `deviations.py` joins, and the build's departures report lists it (README rule 4).

### brief:gates

- `packet.py --check dTendedCadence` green before the first pass. A red on a moved instrument blob is a stop, never re-rendered away (README rule 2).
- `carries.py --build dTendedCadence --exit` at the Design exit while it is in service (the execution plan's `[phase-1]` retirement table).
- The close sequence of README rule 4, then the bar the driver owes at `--close`.

### brief:non-goals

- v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: frozen at the baseline, so a change to a clause is a deviation record approved by its risk.
- The 491 clauses of the other 21 chain builds' rows: carrying one needs a `**Moved:** <clause id> to dTendedCadence by <decision>` line.
- Any path outside `memory/builds/dTendedCadence/`, but the product paths a build run's units record with `--dispatch --writes`, an ask row in another build's `BACKLOG.md`, and the shared renders a landing re-renders (README rule 7).
- Another build's packet, the instruments under `memory/builds/dClosedLoop/build/*.py`, and this packet's pin lines: only `packet.py --repin <instrument>`, the owner's, moves a pin.

### input:spec

memory/builds/dTendedCadence/prompts/2026-11-01-prompt-TOOL-dTendedCadence-60-promoted-fix-brief.md

### task:reuse

dMindYourWords' spec-run sequence; seams found per unit by the reuse scouts and recorded in each spec's §10.

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
