**Serves:** journal TOOL-aShelvedLeg-3

# gov-spec-writer handoff — TOOL-aShelvedLeg-3

<!-- gov:handoff role=gov-spec-writer build=aShelvedLeg unit=TOOL-aShelvedLeg-3 path=memory/builds/aShelvedLeg/prompts/2026-11-11-prompt-TOOL-aShelvedLeg-3-2-spec-writer.md role-sha=dcd8416ea3d2 task-sha=d7a2b7667766 -->

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

This handoff is for build `aShelvedLeg`, unit `TOOL-aShelvedLeg-3`.
Not supplied, optional: `input:spec`.

### brief:goal

The MEDIUM and LOW the closing review of TOOL-aShelvedLeg-2 confirmed are fixed in one batch unit, as M4 promotes them, and each is left-shifted. The findings are in `memory/builds/aShelvedLeg/reviews/2026-11-11-review-TOOL-aShelvedLeg-2-closing-diff-round1.md`. The spec is written with status DEFERRED: by the owner's ruling of 2026-11-11 units 1 and 2 land first and this unit lands later on its own. Its §3 declares **consumes-from** `TOOL-aShelvedLeg-2` and no edge to unit 1.

### brief:items

1. **The every-bar comments S1 missed (MEDIUM, ids 2 and 3).** `tools/unattended/lib-unattended.sh:2389` says `read_spec_audit_ids` exists "because check 2 runs on every bar", and `tools/unattended/unattended.sh:2997` rests an owner-accepted cost on check 9 asserting the same facts "on the bar". Both checks are `check-unattended.sh`'s, which TOOL-aShelvedLeg-1 held off every automatic bar. Re-derive the population by grep over every script in `tools/unattended/`, not a named-file list, and reword each sentence; where a sentence's argument rested on the bar running the leg, say what bounds it now.
2. **The changed-mode sentence drops its other arms (LOW, ids 1 and 4).** `tools/unattended/README.md:424-426`, `tools/unattended/kit.toml:263-265` and `memory/gotchas/changed-mode-selection-ignores-doc-reads.md` say the leg is selected by the kit's shipped sources "only" or "alone". `run-gates.sh:3071-3077` also runs a held leg with no, unreadable, non-ancestor or foreign last-run record, or one more than `GATE_SELFTESTS_MAX_LAG` commits behind HEAD. Point at that comment rather than restating the rule.
3. **Left-shift.** One `memory/gotchas/` entry for the new class `restated-rule-drops-its-other-arms`; the other two findings' classes exist.

### brief:acceptance

1. A grep over every file in `tools/unattended/` for every-bar or merge-bar wording on a line about `check-unattended`, check 2, check 9 or the kit gate prints only lines that describe a different leg. At BASE it prints `lib-unattended.sh:2389` and `unattended.sh:2997`.
2. No changed-mode sentence in the three files says "only" or "alone" about the selection.
3. The new gotchas entry passes memory hygiene.

### brief:gates

memory hygiene · spec tokens · docs · kit version markers · kit epoch · lexicon naming predicates · routed commits name a specced unit · brief-recorded; then the full bar at the lander.

### brief:non-goals

Behaviour of any script. The changed-mode selection itself.

### task:reuse

run-gates' existing hold (`subject == kit` OR `chunk == selftests`, run by `GATE_SELFTESTS=1`); `aBenchedProbe` held a descriptor leg the same way for cost.

### card:route

- build: aShelvedLeg
- unit: TOOL-aShelvedLeg-2 · spec memory/builds/aShelvedLeg/spec/2026-11-10-spec-TOOL-aShelvedLeg-2.md
- brief: memory/builds/aShelvedLeg/prompts/2026-11-10-prompt-TOOL-aShelvedLeg-2-brief.md

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
