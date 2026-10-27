**Serves:** journal TOOL-dSafePassage-5

# gov-spec-writer handoff — TOOL-dSafePassage-5

<!-- gov:handoff role=gov-spec-writer build=dSafePassage unit=TOOL-dSafePassage-5 path=memory/builds/dSafePassage/prompts/2026-10-27-prompt-TOOL-dSafePassage-5-6-spec-writer.md role-sha=06b14b1ac42a task-sha=573c91b3050a -->

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

TOOL-dSafePassage-5 builds green on the shipped walk: each of the five things its third build pass (`wf_0d024041-1eb`, HEAD `29665dd17`) measured has exactly one disposition in the spec set. The disposition is a spec change in unit 5, a cited normalization, or a defect owned by a new unit ordered before unit 5.

**What the builder measured** over real release-0 trees. The work-in-progress unit is kept at `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dsafepassage-567339/c5f50d22-89c6-41d7-84e5-2382dcd49faa/scratchpad/TOOL-5-wip/`, with case logs `uw5b-*.log` and `uw5-*.log` beside it. Read them. `up`, `isolation`, `shims`, `fail` and `skip` are green. `plants`, `down`, `reup` and `kill` are red:

1. **`edited-render` plant: the adopter's edit is lost.** The pinned `apply` writes every `rendered` row without an `oid` and records only `output_sha256` (pinned govkit.py:8162). `check_render_edited` (`tools/govkit/govkit.py:9382-9393`, TOOL-dSafePassage-9 S5, CLOSED) returns False when a row has no `oid`. So the first `update` re-renders `.claude/skills/lexicon/SKILL.md` over the edit, writes no order, and the edit is gone. That is an adopter-facing defect for every install rendered before `oid` existed. The same root cause makes `down` differ at that file. It also makes `kill`'s re-run differ from `up`, because after a kill the receipt TOOL-dSafePassage-62 writes carries the `oid`.
2. **`derive_first_write` ties.** The fanout-cap step's two writes (`.governance/policy.toml` and its before-image) carry identical `mtime_ns` on this node. The unlinked `.agent-cap.conf`, timed by the root directory's mtime, sorts before both. So the "first write" the kill case applies is really the step's last, and the case reaches a state the step's real write order cannot.
3. **`role` after `down` with `withdraw-one`.** The receipt row `tools/hooks/README.md` reads `retired-edited` where release-0 recorded `engine`.
4. **Plant vocabulary.** The `retired-edited` order appears only when gov's source file is also removed, so `[[gov_plant]]` needs a `remove` edit kind beside append, replace and create.
5. **Index compare.** The receipt's and the sidecar's index entries differ by blob id whenever their contents differ only in S4's normalized fields. The index compare reads those two entries by mode and stage only.

### brief:items

1. **(1) is a defect: author TOOL-dSafePassage-63.** Make it Tier-2, `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 5`, carrying `cl-dClosedLoop-0022` as TOOL-dSafePassage-62 does. Its one mechanism: `check_render_edited` proves an edit from the row's recorded `output_sha256` when `oid` is absent. Read what `output_sha256` measures (raw bytes or cleaned) at today's apply and update writers and at the pinned one, and make the fallback compare like with like. If it cannot prove an edit soundly, say so in §8 as a fork, with the recommendation. Add an acceptance criterion on a planted no-`oid` receipt and a `New arm:` line. TOOL-dSafePassage-9 is CLOSED and read-only, so 63 cites it as the seam it extends. Add 63's row to the README `roster:units` table, with `**Derived:**` set to the build-run divergence.
2. **(2): unit 5 states how the first write is found.** It cannot rely on mtimes alone. Derive the order from something the step's real up determines, read from `tools/govkit/upgrade_steps.py` and the fanout-cap step's up. If nothing does, the kill case may kill by running the step's up in the child walk and stopping it after its first write lands, observed by the walk itself. Pick one, verified against the code, and record why.
3. **(3): disposition by the rev-8 rule.** A field is normalized ONLY where a record declares it output-only or re-derived per run, and that record is cited. Otherwise it is a defect, owned by a new unit at the next free id with the same header as item 1. Read where update's file pass and the step downs set and restore `role` before deciding.
4. **(4) and (5): unit 5's text.** Add `remove` to the `[[gov_plant]]` vocabulary and have the `withdraw-one` plant use it. Make the index compare read the receipt and sidecar entries by mode and stage only, stating why.
5. **Revise TOOL-dSafePassage-5** as rev-9 dated 2026-10-27, still `DEFERRED`, with `consumes-from` on 63 and on any other new unit. AC3, AC5, AC7 and AC12 change only as the dispositions decide. One §9 line names this brief. The spec is already over its 49152-byte warn budget, so add no prose beyond what the dispositions need.
6. **Cross-read** TOOL-dSafePassage-26 and -61, which consume unit 5, and TOOL-dSafePassage-9 and -62. A DEFERRED spec that disagrees is fixed in place, with a rev bump and a §9 line. A CLOSED spec is read-only: report any contradiction in it.
7. **Commit nothing.** Return the files you wrote and, for each of (1) to (5), its disposition and the record or unit behind it.

### brief:acceptance

- Each of (1) to (5) has one named disposition.
- No normalization stands without a cited record.
- TOOL-dSafePassage-63's spec is conforming: status header, Carries, §6 criteria each with a Red-when, §7 gates with a `New arm:` line, and §10 reuse.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### brief:gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### brief:non-goals

- No product code.
- No edit to a CLOSED spec.
- No commit, no stage into the real index, no RUN.md row: the main loop runs `--rescope`.
- No redesign of the green cases.

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
