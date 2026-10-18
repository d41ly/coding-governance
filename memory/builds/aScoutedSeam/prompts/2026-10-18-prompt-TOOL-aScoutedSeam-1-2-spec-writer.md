**Serves:** journal TOOL-aScoutedSeam-1

# gov-spec-writer handoff — TOOL-aScoutedSeam-1

<!-- gov:handoff role=gov-spec-writer build=aScoutedSeam unit=TOOL-aScoutedSeam-1 path=memory/builds/aScoutedSeam/prompts/2026-10-18-prompt-TOOL-aScoutedSeam-1-2-spec-writer.md role-sha=06b14b1ac42a task-sha=c82d6c6f805a -->

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

This handoff is for build `aScoutedSeam`, unit `TOOL-aScoutedSeam-1`.
Not supplied, optional: `input:spec`, `task:reuse`, `card:route`.

### brief:goal

Record the owner's 2026-10-18 rulings on the nine open §8 forks of the five aScoutedSeam specs, and change each spec where a ruling departs from what it was written to. Specs only: no product code, no commit.

### brief:items

1. TOOL-aScoutedSeam-1 F1, RULED: the design lens runs ONLY when the code lens's framing finds a UI need, against the recommendation.
   - Rework S2, S3, the §4 flow and the data model so the harness runs `codeLens` first. It spawns `designLens` only when the code lens's return marks a UI need: add a boolean `uiNeed` to the return contract, which the code lens sets.
   - The two passes are now serial, so the wall is the sum of the two; state it in §5. The section's `scout` line still reports `lenses <live>/<run>`, and a non-UI request reads `lenses 1/1`.
   - Liveness: a design lens not run because `uiNeed` is false is announced on the scout line as `design skipped (no UI)`, never read as dead.
   - Criteria: adjust any criterion that assumed both lenses always run (AC1, AC3, AC10), and add one. When the code lens returns `uiNeed: false`, the stub records no design spawn and the scout line says the design pass was skipped. Red when a skipped design pass reads as a dead lens, or when the design lens is spawned anyway.
2. TOOL-aScoutedSeam-1 F2, RULED: `medium`, as recommended. Close it.
3. TOOL-aScoutedSeam-1 F4, RULED: option (a), as recommended. Close it.
4. KICK-aScoutedSeam-1 F1, RULED: leave the gov default blank, as recommended. Close it.
5. KICK-aScoutedSeam-1 F2, RULED: product code only, as recommended. Close it.
6. TOOL-aScoutedSeam-2 F1, RULED: the author's reason, read at approval, as recommended. Close it.
7. TOOL-aScoutedSeam-3 F1, RULED: per unit, as recommended. Close it.
8. TOOL-aScoutedSeam-3 F2, NOT CLOSED: the owner asked to measure the diff mode at `high` first, and for a hypothesis on why `medium` lost cases. Mark F2 "measurement owed (owner, 2026-10-18)". Change nothing else about the effort in this pass.
9. DEPL-aScoutedSeam-1 F1, RULED: the superproject rung FIRST, against the recommendation.
   - Reorder S1's resolution ladder: `git rev-parse --show-superproject-working-tree`, then `GOV_REUSE_HOSTS`, then `.unattended.conf REUSE_HOST_TREES`, then `hosts: none`.
   - State what that costs: a node that checks the package out away from its host, while the package is still a submodule, cannot override the superproject with the env variable.
   - Adjust the criterion that observes the ladder order.
10. Every spec: each resolved fork keeps its question and records `RESOLVED (owner, 2026-10-18): <ruling>`, as TOOL-1 F3 already does. One §9 revision line per spec names every section, scope item and criterion moved.

### brief:acceptance

Each of the five specs carries a §9 line for this pass. Every ruled fork reads RESOLVED with the ruling, and TOOL-3 F2 reads as a measurement owed. `python tools/check-spec-tokens.py`, `python tools/memory-tree/gen_build_index.py --check` and `--check-format` pass after the main loop re-renders the indexes. TOOL-aScoutedSeam-1 stays under the 49152-byte ceiling after the re-render, which adds records rows. It is 48925 bytes now, so item 1's additions are paid for by cuts elsewhere in that spec, such as shortening resolved forks to their ruling.

### brief:gates

memory hygiene · spec tokens (a spec's own names resolve) · build README slot contract

### brief:non-goals

- No product code and nothing under `tools/`, `skills/` or `.claude/`.
- No change to unit ids, order or titles.
- No commit, which is the main loop's.
- No change to TOOL-aScoutedSeam-3's effort or prompt in this pass: that waits on the measurement.

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
