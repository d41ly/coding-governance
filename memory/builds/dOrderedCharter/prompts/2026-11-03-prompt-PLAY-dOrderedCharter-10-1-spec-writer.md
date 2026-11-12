**Serves:** journal PLAY-dOrderedCharter-10

# gov-spec-writer handoff — PLAY-dOrderedCharter-10

<!-- gov:handoff role=gov-spec-writer build=dOrderedCharter unit=PLAY-dOrderedCharter-10 path=memory/builds/dOrderedCharter/prompts/2026-11-03-prompt-PLAY-dOrderedCharter-10-1-spec-writer.md role-sha=dcd8416ea3d2 task-sha=ec1849562963 -->

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

This handoff is for build `dOrderedCharter`, unit `PLAY-dOrderedCharter-10`.

### brief:goal

Revise spec 10 so registering its namespaces leaves unit 19's `tags` leg green over the tree, and every namespace still
joins both ways.

### brief:items

1. **The `kit.toml` collision.** Decide by M3 between at least: a namespace name that no file name shares; a rule,
   stated in spec 10 and consistent with unit 19's built `SPAN_RE` and `_derive_span_ns`, that excludes a
   file-name-shaped span (a known extension after the namespace) from the citation population; or another mechanism
   you find. Record the loser and the observation that rejected it (M12) in §8, delegated. A choice that edits unit
   19's code is in this unit's Files touched, never a reopening of spec 19.
2. **`owned` against non-core kits.** Say for the `kit` row (and any other namespace whose tags are minted inside a
   non-core kit's tree) either which core-held source mints them, or that the row takes a layer `check_owned` admits,
   or how `owned` treats it; measure the choice over the tree with unit 19's own functions.
3. **The member count.** §4 pins `kit` at 29 members; HEAD holds 18 `tools/*/kit.toml` descriptors and 12
   `tools/govkit/entries/*.kit.toml` files declaring 15 ids. Say which population "each descriptor's id" means and
   derive the count at the pass, never pin it.
4. **Migration and Rollout.** Re-state what the shape check's first run grades, with the count left red over the tree
   (it must be 0) written into §6 from a probe of unit 19's functions.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-03, the status kept `DEFERRED`, and add one §9 line naming this brief.
- Run the spec-token reading on your own revision's §6 and §7 by eye against `tools/check-spec-tokens.py`'s `BAR`
  pattern: no AC observes a suite, a bar or `gov_tag.py check` over the tree.
- Verify every path, count and line you cite against the tree at HEAD; stay under the 47000-byte authored budget.

For the run:

- Writes stay in spec 10 and the files `gen_build_index.py --write` rewrites.
- This is an unattended run and nobody answers a question: a fork no option survives is written as an open §8 item
  with the options and the veto, and said in the return.
- Do not commit and run no check: the main loop re-renders the packet, runs the spec-token check, renders the index
  and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return the new rev, the §8 decisions with their losers, and the red count item 4 measures.

### brief:acceptance

- Spec 10's §6 carries item 4's measured red count, and it is 0.
- The Status line is one rev higher, and §9 holds the new line.

### brief:gates

The spec-token check, run by the main loop before the commit.

### brief:non-goals

No code; no spec but 10; spec 19 stays frozen.

### input:spec

memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-10.md

### task:reuse

each spec's §10 names its seam; recall terms below.

### card:route

- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-10 · spec memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-10.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-10-build-brief.md

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
