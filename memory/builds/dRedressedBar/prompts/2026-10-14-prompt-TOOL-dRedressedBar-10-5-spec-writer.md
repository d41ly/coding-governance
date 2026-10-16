**Serves:** journal TOOL-dRedressedBar-10

# gov-spec-writer handoff — TOOL-dRedressedBar-10

<!-- gov:handoff role=gov-spec-writer build=dRedressedBar unit=TOOL-dRedressedBar-10 path=memory/builds/dRedressedBar/prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-5-spec-writer.md role-sha=06b14b1ac42a task-sha=5219072b3c88 -->

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

This handoff is for build `dRedressedBar`, unit `TOOL-dRedressedBar-10`.

### brief:goal

DIVERGENCE: the spec requires one commit that no single role can make. §2 S24, §4 "The sibling rev bumps" and its Files touched, and §6 AC19 put the eight sibling-spec corrections into this unit's own build-pass commit. Those are specs 1 and 3 to 9: S1-S3's revision line, S5, S8, S9, S14, S16 and S22's spec-9 half. AC19 then reads them at `<p10>~1..<p10>`. scratch-guard blocks that write. Under `.claude/roles.json` only gov-spec-writer may write spec files, and a gov-builder may change only the status and date cells of the spec it is routed to. So the one commit AC19 reads cannot be made by either role. The spec would have to say one of two things. Option one: the sibling corrections are a separate gov-spec-writer pass with its own commit (M6's "a review's fixes folded in"); this unit's build pass writes only `tools/govkit/entries/settings-merge.kit.toml`, `tools/govkit/matrix.py` and the acceptance ledger; and AC19, plus S24's "in this pass", reads the spec-writer's commit instead of `<p10>`. Option two: split the unit into a product unit and a spec-correction unit.

The builder's further findings, for the same revision: unit 20 shifted every `govkit.py` line after about 870 by +3 (`EPOCH_ROLES` now at :12938; §4's cites 1450-1456, 5913-5917, 6313-6324, 7740-7764 and 11104-11126 are each +3); spec 4's §5 migration line "once unit 7 bumps the two kits" is the same false fact S8 corrects but S8 names only three addresses; and S9's list "1 to 6, 8 and 9" omits unit 20, also ordered before unit 7.

### brief:items

1. **Take option one, and do the folding now, in this pass.** Apply every sibling-spec correction unit 10 owns to specs 1 and 3 to 9, each as a rev bump with its §9 line naming report id and unit 10. Include the spec-4 §5 migration line and S9's list with unit 20 added. CLOSED specs take the correction as a records fix with their status unchanged.
2. **Revise spec 10** to a new rev: S24 and §4 say the sibling corrections landed in this spec-writer pass, by its commit; §4's Files touched for the build pass lists only `tools/govkit/entries/settings-merge.kit.toml`, `tools/govkit/matrix.py` and the acceptance ledger; AC19 reads the spec-writer pass's commit, named as `<s10>`, not `<p10>`; the govkit.py line cites move by +3.
3. **Apply the same check to specs 13, 17 and 19.** For each S-item or AC that requires the builder's own commit to edit another spec, do the same: fold those sibling corrections now in this pass, and revise the unit so its build pass writes only product files and its AC reads this pass's commit. Name each moved item in the unit's §9 line. A unit with no such item is left alone, and the report says so.

### brief:acceptance

`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades units 10, 13, 17 and 19 READY. No READY unit's build pass names a spec file other than its own in Files touched. `bash tools/memory-tree/check-memory-hygiene.sh --staged` over the staged specs prints no check 12 or 25 line for them.

### brief:gates

`memory hygiene` · `kit epoch`

### brief:non-goals

- No code: the product half of unit 10 stays for its builder.
- No status change to any spec.
- No merge to local main and no push without the owner's ask.

### input:spec

memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md

### task:reuse

precedent memory/builds/aSweptBar/; each spec's §10.

### card:route

- build: dRedressedBar
- unit: TOOL-dRedressedBar-10 · spec memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md
- brief: memory/builds/dRedressedBar/prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-2-revision.md

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
