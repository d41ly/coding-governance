**Serves:** journal TOOL-dScopedBuild-1

# gov-spec-writer handoff — TOOL-dScopedBuild-1

<!-- gov:handoff role=gov-spec-writer build=dScopedBuild unit=TOOL-dScopedBuild-1 path=memory/builds/dScopedBuild/prompts/2026-11-03-prompt-TOOL-dScopedBuild-1-2-spec-writer.md role-sha=dcd8416ea3d2 task-sha=fa2609c43d40 -->

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

This handoff is for build `dScopedBuild`, unit `TOOL-dScopedBuild-1`.
Not supplied, optional: `card:route`.

### brief:goal

Revise TOOL-dScopedBuild-1 so its §3 non-goal names the owner of the `build.exit` transition record
the way the parents' specs spell it on origin/main at `66c5b8dbf`. The spec keeps its own design;
only the one mis-attributed owner changes.

### brief:items

Read the cross-check record first,
`memory/builds/dScopedBuild/build/2026-11-03-build-TOOL-dScopedBuild-1-parents-crosscheck.md`. It has
one MISMATCH, its row 1. Section 2 of the return in
`memory/builds/dScopedBuild/build/2026-11-03-build-TOOL-dScopedBuild-1-crosscheck-returns.md` quotes
both sides and states the change. Re-read both sides before you edit. A row the parent's text does not
bear out is not edited: return it as refused, with the line that refutes it.

- **Row 1, the transition record's owner.** sb1:108 says "A file-backed transition record for
  `build.exit`: the executor's (TOOL-dWellOiledMachine-6)." TOOL-dWellOiledMachine-6 names no
  transition record (`grep -ci transition` on it prints 0); its item witness is a `reconcile` row's
  landed effect (wm6:118-119). The writer is TOOL-dDeclaredLoop-3 S5's `write_transition` (dl3:60),
  which dWellOiledMachine's units reach by subprocess through the loop kit's verb `python
  loop_transition.py record` (wm3:60). Re-point the non-goal's owner to TOOL-dDeclaredLoop-3's
  writer, reached through that verb by the `build.exit` command item, and drop the wm6 attribution.
  Keep the bullet a non-goal. If §3's Edges name wm6 for the record too, correct that edge the same
  way.

Each revision:

- bumps the **Status:** line to `rev-4` and its date to `2026-11-03`, leaving every other field;
- adds one §9 line in the existing form: `- rev-4 · 2026-11-03 · §3 · <what moved>, by the brief
  prompts/2026-11-03-prompt-TOOL-dScopedBuild-1-parents-reground.md`;
- re-opens no fork and resolves none.

### brief:acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-4`, and §9 holds the new line.
- `grep -n "the executor's (TOOL-dWellOiledMachine-6)" <spec>` prints nothing.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your spec staged into it through `GIT_INDEX_FILE`, names nothing of your spec. Delete the copy
  after. Findings that only a `gen_build_index.py --write` render cures belong to the main loop:
  name them and leave them.

### brief:gates

Only the memory hygiene gate, as the role allows. The main loop runs the rest and renders the index.

### brief:non-goals

- No file outside TOOL-dScopedBuild-1's spec. No commit, no stage into the real index, no deviation
  record: the main loop writes those.
- No file of dWellOiledMachine or dDeclaredLoop. A parent spec that looks wrong is a line in your
  return, not an edit.
- No change to what the unit builds.

### input:spec

memory/builds/dScopedBuild/spec/2026-11-01-spec-TOOL-dScopedBuild-1.md

### task:reuse

memory/builds/dWellOiledMachine/build/2026-10-28-build-TOOL-dWellOiledMachine-1-parents-crosscheck.md and its prompts (the record and brief shapes); tools/roles/handoff.py render and agents (handoffs and ledger lines); tools/memory-tree/gen_build_index.py --write (indexes).

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
