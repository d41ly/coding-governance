**Serves:** journal PLAY-dOrderedCharter-53

# gov-spec-writer handoff — PLAY-dOrderedCharter-53

<!-- gov:handoff role=gov-spec-writer build=dOrderedCharter unit=PLAY-dOrderedCharter-53 path=memory/builds/dOrderedCharter/prompts/2026-11-03-prompt-PLAY-dOrderedCharter-53-1-spec-writer.md role-sha=dcd8416ea3d2 task-sha=2b74992404ed -->

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

This handoff is for build `dOrderedCharter`, unit `PLAY-dOrderedCharter-53`.

### brief:goal

Revise specs 53, 13, 42 and 12 so each matches the tree at HEAD on every finding below.

### brief:items

1. Fold every finding below into its spec. Re-verify each cited path and line at HEAD before writing it: units may
   have landed since the sweep read the tree.
2. A finding marked NEW MECHANISM is a fork: decide it by M3, and record the loser and the observation that rejected
   it (M12) in §8, delegated.
3. **A new leg's own rows.** Every new leg's rows are written in its own pass, the way unit 26 rev-7 writes
   `tags positional selftest`'s. Those rows are the dossier claim in `memory/map/features/playbook.md` (with
   `memory/map/generated/*`, which the map generator rewrites), the `tools/govkit/subject-pins.tsv` row, and the claiming row.
   - For a leg an adopter cannot carry, the claiming row is an `[[exempt_leg]]` row in `tools/govkit/registry.toml`,
     as units 16, 19 and 28 wrote at `:707`, `:711` and `:715`.
   - Otherwise it is a `[[gate_leg]]` row in the kit's `kit.toml`.
   - Files touched lists those paths, and §7 names the legs they trip. Check them with
     `python tools/check-spec-tokens.py --legs-for <path>`.
4. **`enforces` into `principle.*`.** The main loop decided this across the sweep. Unit 7, at order 11, adds `principle` to the
   `enforces` row's `to` in `tools/playbook/edges.toml` in its own pass. Units 13 and 12 consume that through a §3 Edges line.

In every spec you revise:

- Bump the **Status:** rev by one, dated 2026-11-03, with the status kept `DEFERRED`.
- Add one §9 line naming this brief.
- §7's leg line names every leg whose guard a Files-touched path trips.
- No AC observes a suite, a bar or a gate leg.
- Stay under the 47000-byte authored budget.
- An H1 names another build's unit as "<build>'s unit N", never by its id.

For the run:

- Writes stay in specs 53, 13, 42 and 12 and the files `gen_build_index.py --write` rewrites.
- This is an unattended run and nobody answers a question. A fork that no option survives is written as an open §8 item
  with the options and the veto, and said in the return.
- Do not commit and run no check. The main loop re-renders the packet, renders the index and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return each spec's new rev, each §8 decision with its loser, and any finding you did not fold, with the reason.

**The findings.**

Cross-cutting: (a) new legs in 13 and 12 omit the owed rows (dossier claim memory/map/features/playbook.md + memory/map/generated/, tools/govkit/registry.toml, tools/govkit/subject-pins.tsv; the codebase-map pre-commit hook .githooks/pre-commit:280-292 refuses an unclaimed leg) and the legs those paths trip (recall floor, recall floor arms, govkit selftest, govkit refusal join) — mirror unit 26 rev-7's AC12. tools/run-gates/owed_rows.py is absent at HEAD (unit 50 builds it). (b) 13 and 12 write `principle.*` into a leg's `enforces`; edges.toml:63-70 has to=["unit","practice"]. Main-loop decision: unit 7 (order 11, before both) widens `to` with `principle` in its pass (sweep A 7-2); 13 and 12 consume that and say so in §3 Edges.

**Spec 53.**
- 53-1 S1 reads `git blame --porcelain -M HEAD -- <path>`; naming HEAD blames only the committed version, so AC3's uncommitted x.py:3 gets no attribution (probed: without HEAD the uncommitted line reads sha 0000…). Blame the working tree (drop HEAD); state the all-zero sha counts as inside the descendant set.
- 53-2 §7 says neither leg is in gate-legs.json at base; `tags (the resolver's checks)` is now a leg (registry.toml:711, subject-pins.tsv:146). Unit 26 rev-7 routes positional-* plants to `tags positional selftest` (spec 26 S7 :118-125, New arm :335). Route the three positional-* plants there.
- 53-3 New arm names tools/playbook/adopt-playbook.sh (plant rows in its `run_plant_rows tags` table :258; PLANTS tuple gov_tag.py:317) — not in Files touched. Add it (or drop it once re-routed).

**Spec 13.**
- 13-1 S3/AC3/§4: unit 10 built `level` as level.<name> — namespaces.toml:54-60 (source LEVELS in tools/playbook/instruction_units.py, extractor tag_index:extract_level, purpose-source instruction_units.py#LEVELS); tag_index.py:347-364 extract_level yields level.charter … level.records. Re-point S3/AC3 to level.<name> via extract_level; drop or redefine derive_level_tag(s) — no second extractor.
- 13-2 AC3 says shape `seg` of "S4's grammar"; S4 is ladder-terms; the shape is SEG at tag_index.py:65.
- 13-3 Owed rows/legs for leg `instruction ladder (level is the one term)` — cross-cutting (a).
- 13-4 enforces principle.p13/p11 — cross-cutting (b).
- 13-5 §1/§4 Migration "Nothing in the product spells a level today" is stale; at landing `level` moves pending→graded under the tags leg (unit 22 return lists it pending). Add an AC or §7 note.

**Spec 42.**
- 42-1 S3 cites `deviation_named` (tree_lib.py:491) as stem precedent; that regex matches any `-deviation-\d+.md` name. The stem regex is `deviation_name` :492-493. Generalising :491 reds the six tracked `…-execution-return-plan-2..7.md` under AC6. Cite :492-493 and state the deviation-kind narrowing.
- 42-2 gen_build_index.py anchors: import block :187→:188 (RECORD_KIND_TOKENS :189); cmd_print_bindings :682→:691.
- 42-3 deviation_join.py:238-240 will move when unit 7 (order 11) extracts the factory; cite RECORD_NAME by name.

**Spec 12.**
- 12-1 §10 lines: render() :979→render_playbook.py:1024; check_one_line_regions :667→:698, signature now (text, cap=None) -> list; check-playbook-parity.sh S4 arm 316→:438.
- 12-2 §4 example renderer "playbook-render@1.31"; KIT_PLAYBOOK_RENDER_VERSION = "1.33" (render_playbook.py:1887).
- 12-3 Owed rows/legs for leg `instruction grammar (statement types, provenance lock)` — cross-cutting (a).
- 12-4 enforces principle.p11 — cross-cutting (b).
- 12-5 S4 hash "S7's normaliser" — S7 is the leg; the normaliser is unit 24's derive_pin_hash (tools/memory-tree/design_lib.py:173). Name it.
- 12-6 AC5 runs `render_playbook.py --target . --check`, the playbook render wiring leg's check; restate as the unit's own probe.

### brief:acceptance

- Each finding above is either folded, or listed in the return with the reason it was not.
- Each revised spec's Status line is one rev higher, and its §9 holds the new line.

### brief:gates

The spec-token check, run over the tree by the next `--dispatch`.

### brief:non-goals

- No code.
- No spec outside the four above.
- No finding about another spec.

### input:spec

memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-53.md

### task:reuse

each spec's §10 names its seam; recall terms below.

### card:route

- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-26 · spec memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-26.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-26-build-brief.md

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
