**Serves:** journal TOOL-dGroundRules-88

# gov-spec-writer handoff — TOOL-dGroundRules-88

<!-- gov:handoff role=gov-spec-writer build=dGroundRules unit=TOOL-dGroundRules-88 path=memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-88-1-spec-writer.md role-sha=06b14b1ac42a task-sha=173909c5e6a2 -->

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

This handoff is for build `dGroundRules`, unit `TOOL-dGroundRules-88`.
Not supplied, optional: `input:spec`.

### brief:goal

Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-88.md`, a Tier-2 spec at order 34, status `DEFERRED`, in the shape `memory/TEMPLATE-SPEC.md` gives, that makes `--repin` (and only `--repin`: a first render stays refused inside a chain run) admit the owner while a chain run is live and refuse every agent and unattended caller. Author only: no product code, no commit, no gate beyond memory hygiene.

### brief:items

1. Reuse first: find how this repository already tells an owner's invocation from an agent's (the scratch-guard hook's `agent_type`, the unattended kit's owner-only verbs, `tools/check-template-size.sh`, `tools/run-gates/run-gates.sh`, any other seam a grep for owner/agent finds) and run `reuse_lookup.py` on the behaviour; spec the caller test on the seam that exists, or say with evidence why none fits. Deny by default: a caller the test cannot classify is refused.
2. Name what the guard records when it admits an owner repin inside a live chain run (where, in what shape, read by whom), so the repin is visible on the record rather than silent.
3. Keep every existing refusal and fixture plant meaning what it means today for an agent caller, and add the plant(s) that observe the owner path admitted and an agent or unattended caller refused with a live chain run; a `New arm:` line per added plant.
4. State the owner action this unit leaves: after its build commit, `packet.py --repin` of `packet.py` itself (and any other instrument this unit touches) by the owner, admitted by the new guard, before the close's bar; the close's spec tokens leg reds on the stale pin until then.
5. Each acceptance criterion is a command the pass may run (`packet.py --fixture --plant <case>`, a direct call of the guard), never the bar or a self-test suite, and carries `Red when:` with a staged break that reds it by name. §6 names the legs the touched file owes through `derive_guarded_legs`.
6. §7 "Open questions" reads exactly `none`, with no bullet under it, unless a fork genuinely needs the owner; any follow-up goes in the revision log as prose. No line anywhere in §5 starts at column 0 with `AC<n>` other than the bullets themselves; every AC bullet carries `Red when:`; keep every acceptance code span on one line and free of a `|` the bar pattern reads as a pipe; no retirement word in §2; an untracked path sits in a fenced block; never write a probe copy of a spec inside the spec folder.

### brief:acceptance

`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### brief:gates

Memory hygiene only.

### brief:non-goals

`carries.py` and its batching (ask TOOL-dGroundRules-112); the first-render refusal; the pin arm's grading; any other instrument.

### task:reuse

each unit's §10 names its seam: read_policy_key/resolve_read in tools/lib and tools/hooks/agent-cap.js, tools/gate-legs.json, tools/govkit/registry.toml.

### card:route

- build: dGroundRules
- unit: TOOL-dGroundRules-84 · spec memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-84.md
- unit: TOOL-dGroundRules-85 · spec memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-85.md
- unit: TOOL-dGroundRules-86 · spec memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-86.md
- brief: memory/builds/dGroundRules/README.md

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
