**Serves:** journal TOOL-aGuardedEffort-1

# gov-spec-writer handoff — TOOL-aGuardedEffort-1

<!-- gov:handoff role=gov-spec-writer build=aGuardedEffort unit=TOOL-aGuardedEffort-1 path=memory/builds/aGuardedEffort/prompts/2026-11-10-prompt-TOOL-aGuardedEffort-1-1-spec-writer.md role-sha=dcd8416ea3d2 task-sha=78790034cc38 -->

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

This handoff is for build `aGuardedEffort`, unit `TOOL-aGuardedEffort-1`.
Not supplied, optional: `input:spec`, `card:route`.

### brief:goal

The hooks kit's spawn guard, `tools/hooks/agent-cap.js`, refuses a direct role spawn whose effort, and a harness call whose `efforts`, differ from the levels the effort policy gives the session's model, so a session that forgets the model argument is stopped at the tool call instead of shown on the `agent` line afterwards. This discharges ask `TOOL-aProfiledEffort-6`.

### brief:items

1. The guard learns the model a call will run on: an `Agent` call's own `model` argument where it carries one, else the `message.model` of the last main-chain assistant entry of the transcript the payload's `transcript_path` names. [planned TOOL-aGuardedEffort-1]
2. The guard learns the levels from the role index `.claude/roles.json`, which `render_agents.py` extends with the default role and stage levels and each profile's match words and resolved levels; the hook spawns no interpreter. [planned TOOL-aGuardedEffort-1]
3. An `Agent` call rule 6 admits is refused when the level it will run at, its `effort` argument or, with none, its role's default level, is not the level the model's profile gives that role. [planned TOOL-aGuardedEffort-1]
4. A `Workflow` call rule 6 admits is refused when, for any stage key of a workflow that harness runs, the level it will run at, the `args.efforts` value or, with none, the stage's default level, is not the profile's. [planned TOOL-aGuardedEffort-1]
5. The refusal names the role or stage, the level seen, the level expected, the model, and the `handoff.py role-efforts --model` or `stage-efforts --model` call that prints the right value. [planned TOOL-aGuardedEffort-1]
6. Where no model can be read, the call is admitted and one stderr line says the level was not checked and why. [planned TOOL-aGuardedEffort-1]
7. The hook's header, the roles README sentence `The spawn guard reads no`, the codebase-map dossier and the `help/` page say what the guard now checks and what it does not. [planned TOOL-aGuardedEffort-1]

### brief:acceptance

1. A payload whose transcript's last assistant model is `claude-fable-5-2` and whose `Agent` call for `gov-builder` carries no `effort`, or `effort: high`, exits 2 naming `medium`; the same call with `effort: medium` exits 0.
2. With a model no profile matches, the same call with no `effort` exits 0, and with an `effort` that is not the role's default exits 2.
3. A `Workflow` call for the unit harness on a Fable transcript exits 2 with no `efforts` and with `{"builder":"high"}`, and 0 with `{"builder":"medium"}`.
4. An `Agent` call carrying `model: fable` on a transcript of another model is graded against the `fable` profile.
5. A payload with no `transcript_path`, an unreadable one, or one with no assistant entry exits 0 and prints the not-checked line.
6. The word match in the hook and `roles_lib.resolve_profile` agree over one shared list of model ids, the non-matching `affable-1` among them, in a parity arm.
7. `render_agents.py --check` reds on a role index whose effort section differs from the policy's.
8. Every arm above is in `tools/hooks/agent-cap.test.sh` or the roles adopter self-test, and each was seen red before green.

### brief:gates

harness arms · roles catalogue · roles render wiring · roles render selftest · roles adopter self-test · hook destinations · codebase-map coverage + freshness · docs · kit/dogfood doc parity · lexicon naming predicates · kit epoch · kit version markers · memory hygiene · spec tokens; then the bar once at the close.

### brief:non-goals

The agents a running harness spawns through its own `agent()`, which no hook sees. The `committer` and `probe` stages, which take no level (ask `TOOL-aProfiledEffort-5`). Any change to a level, a profile, or the resolver's rules. A second matching rule: the hook's match is the resolver's, proved by parity. A refusal when the model cannot be read. Reading the model from anywhere but the call and the transcript.

### task:reuse

agent-cap.js rule 6 checkHandoffSpawn and checkHarnessCall; format-guard.js transcript read; render_agents.py role index; roles_lib.resolve_profile.

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
