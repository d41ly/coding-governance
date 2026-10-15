**Serves:** journal TOOL-dRedressedBar-27

# gov-spec-writer handoff — TOOL-dRedressedBar-27

<!-- gov:handoff role=gov-spec-writer build=dRedressedBar unit=TOOL-dRedressedBar-27 path=memory/builds/dRedressedBar/prompts/2026-10-15-prompt-TOOL-dRedressedBar-27-1-spec-writer.md role-sha=06b14b1ac42a task-sha=b00f1c671065 -->

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

This handoff is for build `dRedressedBar`, unit `TOOL-dRedressedBar-27`.
Not supplied, optional: `input:spec`.

### brief:goal

A full `bash tools/memory-tree/check-memory-hygiene.sh` at the build tip reds check 23 in three arms. (1) A CLOSED unit numbers an acceptance criterion no journal record evidences: TOOL-dRedressedBar-2, -4, -5, -7, -9, -11, -18 and -20 wrote no acceptance ledger. (2) An acceptance-ledger line is in neither legal form: TOOL-aSparedSpawn-10/AC9, -11/AC10, -13/AC11, -6/AC6, -6/AC8, -8/AC10, -8/AC6, -32/AC12. (3) A ledger answer shares no backticked token with its criterion: TOOL-aOrientedCast-22/AC7 and 29 aSparedSpawn entries. Arms 2 and 3 are byte-identical at the base `ebce889c7` (`prompts/2026-10-15-prompt-TOOL-dRedressedBar-1-4-researcher.md`), so the base bar's `memory hygiene` leg was red on them too. Make check 23 pass with no waiver, by evidence.

### brief:items

1. **TOOL-dRedressedBar-27 — a records-only unit, order after unit 26.** No product code moves. Spec it as Tier-1 (records), with a scope item and an AC per arm.
   - **Arm 1:** one acceptance ledger per listed dRedressedBar unit, under `memory/builds/dRedressedBar/build/`, carrying `**Serves:** journal <unit id>`, one line per criterion in the OBSERVED or AMENDED form check 23 accepts. The readings come from what each unit's builder recorded: its commit body, its `Decided:` trailers and its return in `build/2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`. A criterion its builder did not observe is written as such (an AMENDED or an owed-at-close line in the legal form), never as an invented reading. Units 18's criteria are the rev the builder built against.
   - **Arms 2 and 3:** rewrite each listed foreign ledger line in place so it is in a legal form and shares a backticked token with its criterion, keeping its reading true to what that unit observed: read the unit's spec criterion and the ledger's own evidence before changing a word. A line whose observation cannot be reconstructed from the record is converted to the honest legal form check 23 accepts for an unobserved criterion, not given a token it did not earn. List every foreign line changed, before and after.
   - The check's legal forms, the token rule and any cutoff or grandfather keys are read from `tools/memory-tree/check-memory-hygiene.sh` check 23 and `.memory-tree.conf`; the spec cites them.
2. **The record:** the unit's own ledger evidences its ACs as usual.

### brief:acceptance

`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades unit 27 READY, ordered after unit 26. The spec names each of the 8 + 38 targets and an AC whose red half is today's check 23 output for that arm.

### brief:gates

`memory hygiene`

### brief:non-goals

- No product code, no checker change, no waiver or grandfather row added to make check 23 pass.
- No edit to any other part of the aSparedSpawn or aOrientedCast builds beyond the listed ledger lines.
- No merge to local main and no push without the owner's ask.

### task:reuse

precedent memory/builds/aSweptBar/; each spec's §10.

### card:route

- build: dRedressedBar
- unit: TOOL-dRedressedBar-26 · spec memory/builds/dRedressedBar/spec/2026-10-15-spec-TOOL-dRedressedBar-26.md
- brief: memory/builds/dRedressedBar/prompts/2026-10-15-prompt-TOOL-dRedressedBar-25-brief.md

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
