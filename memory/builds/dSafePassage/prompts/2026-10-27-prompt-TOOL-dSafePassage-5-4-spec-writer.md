**Serves:** journal TOOL-dSafePassage-5

# gov-spec-writer handoff — TOOL-dSafePassage-5

<!-- gov:handoff role=gov-spec-writer build=dSafePassage unit=TOOL-dSafePassage-5 path=memory/builds/dSafePassage/prompts/2026-10-27-prompt-TOOL-dSafePassage-5-4-spec-writer.md role-sha=06b14b1ac42a task-sha=a390b715170e -->

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

This handoff is for build `dSafePassage`, unit `TOOL-dSafePassage-5`.
Not supplied, optional: `input:spec`.

### brief:goal

Every byte difference the builder measured between a rolled-back tree and release-0 has exactly one disposition in the spec set — a declared output-only or re-derived field normalized in the leg's comparison with its owning record cited, or a defect in the walk or rollback owned by a new unit, ordered before TOOL-dSafePassage-5, that makes the rollback restore it — so unit 5 builds green on the shipped walk and clause `cl-dClosedLoop-0022`'s "down byte-identical" means what it says.

**What the builder measured** at HEAD `41062397` (probe scripts kept at `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dsafepassage-567339/c5f50d22-89c6-41d7-84e5-2382dcd49faa/scratchpad/probe_r0.py`, `probe_walk.py`, `probe_down.py`, `probe_kill.py`; read them):
- **Release-0 now builds.** The pinned clone (`git clone --no-tags`, checked out at `60d90cb7`) applied the rev-7 `kits` line (23 kits) with the rev-7 answers and seeded AGENTS.md: exit 0 in 33 s, a schema-3 receipt, lf_pin notes only.
- **AC1's order** holds only while the clone's `main` is gov's landed ref (`origin/main`); with the clone's own default branch as tip, `agent-cap/fanout-cap-to-agents-in-flight` (29ccb065) walks first.
- **`update --to <HEAD> --write`** exited 0 in 151 s: the schema step applied; the floor and fanout-cap steps were skipped because their witnesses already hold at release-0.
- **(1) `down` (AC3):** after a clean committed up, `update --rollback --to <pin> --write` exits 0 and rolls back all three steps, but the digest differs from release-0 at `.governance/install.json` (every `files` row gains `carry`; five rendered SKILL.md rows re-measured), `.governance/install.sums` (three rendered rows added) and the git index.
- **(2) `kill` (AC7):** killed at the schema step after its first write, the receipt reads schema 4, `steps` [], `gov_commit` = the pin; the rollback from a copy of that state exits 0 having written 0 files ("receipt re-stamped at 60d90cb7") and 38 paths stay at the tip. Killed at the floor step, the rollback walks three downs but leaves install.json, install.sums, a new `.governance/policy.json` and the index different.
- **(3)** `kill` and `fail` never reach the floor and fanout-cap steps' `up`, because their witnesses hold at release-0, so AC7 and AC8 cannot observe them unless the case forces step k's first witness to fail.

### brief:items

1. **Disposition each difference**, reading the code that produced it (`tools/govkit/govkit.py` update/rollback paths, `tools/govkit/upgrade_steps.py` walks, TOOL-dSafePassage-2, -4, -15, -17, -18, -19 specs and DEPL-dCarriedReceipt-9). A field may be normalized ONLY where a record declares it output-only or re-derived per run (cite it, as TOOL-dSafePassage-15 rev-2 did for `carry`); otherwise it is a defect. The killed-walk rollback that writes 0 files with 38 paths at the tip is a defect unless a record says otherwise: the stamp was withheld (TOOL-dSafePassage-2) and the rollback reads vintage from it (TOOL-dSafePassage-4).
2. **For each defect, author a new unit** at the next free ids (TOOL-dSafePassage-62 onward), Tier-2, `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 5`, with `consumes-from` edges so it builds before TOOL-dSafePassage-5, carrying `cl-dClosedLoop-0022` as unit 5 does (use a `part n/m` Carries form if the join needs it, as the 61 split did). One mechanism per spec. Add each to the README's `roster:units` table (`**Derived:**` the build-run divergence). Record nothing in RUN.md; the main loop runs `--rescope`.
3. **Revise TOOL-dSafePassage-5** as a rev bump dated 2026-10-27, still `DEFERRED`: the cases and AC3/AC7/AC12 compare as the dispositions decide; `kill` and `fail` force step k's first witness to fail where the step's witness holds at release-0 (or say why that cannot be done and what the case observes instead); the clone's landed ref is gov's own default branch; `consumes-from` each new unit. One §9 line names this brief.
4. **Cross-read** TOOL-dSafePassage-26 and -61 (consumers of 5); a disagreement in a DEFERRED spec is fixed there. CLOSED specs are read-only: report a contradiction, never edit.
5. **Commit nothing.** Return the files you wrote and, per difference, its disposition and the record or new unit behind it.

### brief:acceptance

- Each of the measured differences (1)-(3) and the landed-ref order has one named disposition.
- No normalization stands without a cited record declaring the field output-only or re-derived.
- Each new unit's spec is conforming (status header, Carries, §6 criteria with a Red-when, §7 gates, §10 reuse), and `bash tools/unattended/unattended.sh --plan dSafePassage --paths` lists it READY once the main loop stages it.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### brief:gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### brief:non-goals

- No product code; no edit of a CLOSED spec; no change to the pin or its adopters.
- No commit, no stage into the real index, no deviation record.
- No normalization that hides a defect.

### task:reuse

each spec's §10 names its seam (tools/govkit/, tools/lib/, tools/push-main.sh).

### card:route

- build: dSafePassage
- unit: TOOL-dSafePassage-5 · spec memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-5.md
- brief: memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-5-build-brief.md

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
