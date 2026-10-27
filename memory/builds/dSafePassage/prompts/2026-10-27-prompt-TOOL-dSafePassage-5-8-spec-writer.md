**Serves:** journal TOOL-dSafePassage-5

# gov-spec-writer handoff — TOOL-dSafePassage-5

<!-- gov:handoff role=gov-spec-writer build=dSafePassage unit=TOOL-dSafePassage-5 path=memory/builds/dSafePassage/prompts/2026-10-27-prompt-TOOL-dSafePassage-5-8-spec-writer.md role-sha=06b14b1ac42a task-sha=21116f4e31d2 -->

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

TOOL-dSafePassage-5 builds green: each of the four things its fourth pass measured has one disposition in the spec set. A disposition is a spec change in unit 5, a cited normalization, or a defect owned by a new unit ordered before unit 5.

**What the builder measured.** The pass built rev-9 whole from the kept work. `up`, `plants`, `skip`, `fail`, `shims` and `isolation` are green, and `reup`'s digest equals `up`'s. Everything is kept at `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dsafepassage-567339/c5f50d22-89c6-41d7-84e5-2382dcd49faa/scratchpad/TOOL-5-wip4/`: `tool5-pass4.patch`, `files/`, `probe_up.py`, `probe_down.py`, `rdiff.py` and `logs-pass4/`. Read them.

1. **`down` is red at `.governance/install.json`.** The `withdraw-one` row `tools/hooks/README.md` reads `retired-edited`, where release-0 recorded `engine`. TOOL-dSafePassage-64's re-resolution does not fire, because `_cmd_update` reads descriptors from the gov checkout's working tree (`read_descriptors(root, ...)` at `tools/govkit/govkit.py:9521`, `resolve_entry(root, ...)` at `:10145`), not at `--to`. S2 keeps the clone at the tip, where the gov plant removed the rule. Measured: the same up tree, rolled back with the clone checked out at HEAD and no gov plants, matched release-0 exactly. Decide from the code and the records (`help/`, the update and rollback specs, DEPL records) which is true:
   - (a) A rollback is documented as run from a gov checkout at the pin. Then S2's clone handling is the spec's error: unit 5 checks the clone out at the pin for each `down`.
   - (b) `update --to` promises the `--to` revision's descriptors. Then reading the working tree is a defect owned by a new unit.
   - (c) TOOL-dSafePassage-64 §4's assumption is simply wrong, and unit 5's expectation changes.
2. **The held kit's exit.** Since TOOL-dSafePassage-63, the `edited-render` plant is `ordered`. Every walk's `update` then holds the lexicon kit back, exits 1 with "1 problem(s)", and withholds the stamp (`gov_commit` stays at the pin). §4 "The cases" and S6 must say how the cases read that exit and the withheld stamp. The patch carries the builder's measurement-only `check_walk_exit`. Weigh it, along with the alternative of running the `edited-render` plant in its own case so the walk cases stay exit 0.
3. **`kill` is red for all three steps** at `install.json`, `install.sums`, and the bytes and index of `tools/lexicon/adopt-lexicon.sh`. The held kit's writes are rolled back only in update's verify phase (`govkit.py` ~`:12626`), after the step walk (~`:11781`). TOOL-dSafePassage-62's receipt, written before the first step, records them at the tip. So a walk killed inside a step leaves a held kit's files at the tip, and its rollback cannot return them. This is gotcha class `verdict-printed-before-the-step-that-reverts-it`. It is a defect unless a record says otherwise. If item 2 takes the held kit out of the kill case's tree, say whether the defect still reaches adopters, and own it in a new unit either way.
4. **AC14's grep** also prints three local `build_target` helpers that already exist: `tools/govkit/upgrade_steps.py:2419`, `tools/govkit/fixtures/retired_edits.py:152`, and `tools/govkit/selftest.py:1252` and `:2408`. The kept patch had bound two of them to the factory's name, so they recursed. Say whether AC14 counts them, or rename them in the Files touched.

### brief:items

1. **Disposition each of (1) to (4)** by the rev-8 rule. A field is normalized only where a record declares it output-only or re-derived and that record is cited. Otherwise it is a defect.
2. **Each defect gets a new unit** at the next free id, TOOL-dSafePassage-65 onward. Each is Tier-2, `DEFERRED`, `advances TOOL-dSafePassage-14` and `order 5`, `**Derived:** TOOL-dSafePassage-5` as -63 and -64 are, with one mechanism, a `New arm:` line and a README `roster:units` row.
3. **Revise TOOL-dSafePassage-5** as rev-10, dated 2026-10-27 and still `DEFERRED`, with `consumes-from` on each new unit. One §9 line names this brief. Add only the prose the dispositions need: the spec is 59 KB, over its 49152-byte warn budget.
4. **Cross-read** TOOL-dSafePassage-26 and -61 (consumers of 5) and TOOL-dSafePassage-2, -62, -63 and -64. Fix a DEFERRED spec in place, with a rev bump and a §9 line. A CLOSED spec is read-only: report any contradiction in it.
5. **Commit nothing.** Return the files you wrote and each item's disposition.

### brief:acceptance

- Each of (1) to (4) has one named disposition, backed by code lines or a cited record.
- Each new unit's spec is conforming: status header, `**Derived:**` line, §6 criteria each with a Red-when, §7 gates with a `New arm:` line, §10 reuse.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### brief:gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### brief:non-goals

- No product code, and no edit to a CLOSED spec.
- No commit, no stage into the real index, and no RUN.md row: the main loop runs `--rescope`.
- No redesign of the cases that are already green.

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
