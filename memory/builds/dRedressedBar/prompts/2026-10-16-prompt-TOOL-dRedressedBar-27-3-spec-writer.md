**Serves:** journal TOOL-dRedressedBar-27

# gov-spec-writer handoff — TOOL-dRedressedBar-27

<!-- gov:handoff role=gov-spec-writer build=dRedressedBar unit=TOOL-dRedressedBar-27 path=memory/builds/dRedressedBar/prompts/2026-10-16-prompt-TOOL-dRedressedBar-27-3-spec-writer.md role-sha=06b14b1ac42a task-sha=386d1cca7292 -->

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

### brief:goal

DIVERGENCE: spec 27 §4 "The six revision entries" gives the build pass five spec writes, as do S4, §3's second non-goal, §4 Files touched, AC4 and AC5. Each is one appended revision entry plus the status header's rev and date, in TOOL-aSparedSpawn-11 (rev-4), TOOL-aSparedSpawn-13 (rev-6), TOOL-aSparedSpawn-32 (rev-5), TOOL-aOrientedCast-22 (rev-2) and TOOL-dRedressedBar-18 (rev-9). The scratch-guard hook refused all five edits. .claude/roles.json lets only gov-spec-writer write a spec, and a gov-builder may move only the status and date cells of its own routed spec. The repo's precedent agrees: a records-fix revision to another spec is written by the unit's spec-writer pass (spec 18 rev-5 to rev-8, spec 9 rev-5 to rev-7).

What §4 would have to say: TOOL-dRedressedBar-27's spec-writer pass writes the five entries and header moves, and re-renders the three build READMEs' generated rows with gen_build_index.py --write, before the build pass. The build pass then writes only the eight ledgers, the re-collected returns record, the 37 foreign lines and this unit's own ledger. AC4's spec half and AC5's entry lookup would then grade the spec-writer commit.

Without those entries, the five U lines would cite revisions that do not exist, so I committed nothing. Every path this pass changed is restored, and the work is saved for the redispatch.

### brief:items

1. **TOOL-dRedressedBar-27 — revise to rev-2, and run `<w27>` in this same pass.** Restructure as the builder states above: the five revision entries and header moves (TOOL-aSparedSpawn-11 rev-4, -13 rev-6, -32 rev-5, TOOL-aOrientedCast-22 rev-2, TOOL-dRedressedBar-18 rev-9) are this unit's spec-writer pass `<w27>`, and you write them now, in this pass, with the exact text the builder saved under `HANDOFF.txt` in `memory/builds/dRedressedBar/build/2026-10-16-build-TOOL-dRedressedBar-27-1-set-aside-work.md`. Date each entry and header 2026-10-16. The main loop commits your spec-27 revision and the five entries together as `<w27>` and re-renders the three build READMEs' generated rows with `gen_build_index.py --write`. The build pass then writes only the eight ledgers, the re-collected returns record, the 37 foreign ledger lines and its own ledger, restoring them from that set-aside record and changing them only where this revision requires; AC4's spec half and AC5's entry lookup grade the `<w27>` commit.
2. **The builder's seven spec facts, each corrected:** (1) aSparedSpawn-8/AC11's template token is `skipped — <id> · <why>` as spec 8 spells it; (2) aSparedSpawn-4/AC12's literal is the wrapper at `989e9234b:tools/hooks/agent-cap.test.sh:72`; (3) aSparedSpawn-3/AC7's before-runner is `286b839a`; (4) aSparedSpawn-16/AC12's instrument base is `f53211e6c`, with the file spelled `age.${heldkeys[$i]}`; (5) AC5's `git grep -F` lookup is satisfied by the owning spec for the tokens the builder lists; (6) Files touched adds the generated records rows the eight new ledgers add to specs 2, 4, 5, 7, 9, 11, 18 and 20; (7) AC4's pinned date is 2026-10-16.

### brief:acceptance

`git diff` shows spec 27 at rev-2 and the five owning specs each with one appended revision entry and their header rev and date moved, nothing else. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades unit 27 READY.

### brief:gates

`memory hygiene`

### brief:non-goals

- No code. No edit beyond spec 27 and the five revision entries with their header moves. No status change; no index regeneration; no commit.

### input:spec

memory/builds/dRedressedBar/spec/2026-10-15-spec-TOOL-dRedressedBar-27.md

### task:reuse

precedent memory/builds/aSweptBar/; each spec's §10.

### card:route

- build: dRedressedBar
- unit: TOOL-dRedressedBar-27 · spec memory/builds/dRedressedBar/spec/2026-10-15-spec-TOOL-dRedressedBar-27.md
- brief: memory/builds/dRedressedBar/prompts/2026-10-15-prompt-TOOL-dRedressedBar-27-brief.md

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
