**Serves:** journal PLAY-dOrderedCharter-20

# gov-spec-writer handoff — PLAY-dOrderedCharter-20

<!-- gov:handoff role=gov-spec-writer build=dOrderedCharter unit=PLAY-dOrderedCharter-20 path=memory/builds/dOrderedCharter/prompts/2026-11-04-prompt-PLAY-dOrderedCharter-20-1-spec-writer.md role-sha=07ad6a5d06b8 task-sha=563047fbafea -->

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
- Verify every claim about current code by reading that code, and cite it by `path#symbol` or the
  blob-pinned line `<path>@<oid>:<n>`. A claim you did not verify is a claim you do not make.
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

This handoff is for build `dOrderedCharter`, unit `PLAY-dOrderedCharter-20`.

### brief:goal

Revise spec 20 so each conflict below is resolved and its builder can build it as written.

### brief:items

1. **The kind's factory name.** S9, AC9 and section 4's Inventory say `core.py new unit`. `core.py new <kind>` looks up the
   row `kind.<kind>`, and the row is `kind.instruction-unit`, so that command refuses and exits 2. An alias would break
   unit 65's rule that a kind's name is never a namespace word. Say `core.py new instruction-unit`, in the row's factory
   too.
2. **The gate leg's principles.** S9 makes the schema leg the kind's gate and takes the kind off `core-pending.txt`.
   S10 fixes that leg's `enforces` at p11 and p13, but `kind.instruction-unit` binds p13 and p16, and
   `tools/playbook/core.py#check_kind_row` requires the gate leg to enforce every bound tag. Add `principle.p16` to the
   leg, or rule that the binds change. Decide by the fork rule.
3. **Reading change records before unit 15.** S3 reads them through the record factory as the kind unit 15 registers,
   but unit 15 builds after this unit: `tools/memory-tree/build_records.py` holds the kind as pending, and reading it
   raises. `derive_status` over passed-in records is buildable, but the tree reads behind S2's active, S3's render arm
   and S8 are not. Say what they read until unit 15 lands, or move the work. Options include: no records, every unit
   active with an unarmed line, unit 15 wiring the reader; or this unit registering the kind. Decide by the fork rule.
4. **Kit dependencies.** The adopters will depend on `render_playbook.py`, but `tools/agent-instructions/kit.toml` has
   `requires = []`, `tools/roles/kit.toml` does not require `playbook-render`, and the agent-instructions adopter's
   header claims no hard dependencies. The section 5 risk that an adopter renders with the old renderer cannot hold
   under AC5. Rule on `requires`, and rewrite that risk.
5. **Files touched and section 7.**
   - `tools/roles/adopt-roles.test.sh` copies only the roles kit into its fixture, so `render_playbook.py` is unreachable
     there.
   - Section 7 omits the `roles adopter self-test` leg.
   - `tools/roles/kit.toml` needs its `[[generated]]` generator changed.
   - `help/roles.md` and `tools/govkit/usage.toml` still name `render_agents.py --write`; that writer must go or it
     writes with no lock row.
6. **The selftest fold.** S6 does not say whether `roles render selftest` keeps its `render_agents.py --selftest` argv or
   moves to `render_playbook.py`. Say which.
7. **A stale pending row.** `python tools/playbook/core.py meta-check` is red at HEAD:
   - The row `principle.p11` in `tools/playbook/core-pending.txt` is stale, because units 12 and 13 now enforce it.
   - Add its deletion to this unit's scope, since S9 already edits that file.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-04, with the status kept `DEFERRED`.
- Add one history line naming this brief, with the S and AC ids it touched.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`.
- New text names a section in words. It never uses the section-sign form, the method-rule form or the hygiene
  check-number form, and it adds no `path:line`.
- An item that retires a name carries a `**Readers:**` clause. Its by-name half names readers by plain tracked path.
- A consumes-from or hands-off edge you add or change has its mirror on the other spec. List any such edge in the
  return; do not edit another spec.
- Stay under the 47000-byte authored budget.

For the run:

- No unit is building, so edit the spec in the tree.
- Writes stay in spec 20. A fork no option survives is written open in the fork record and said in the return.
- Do not commit and run no gate.
- Return the new rev, each fork decision with its loser, and any edge needing a mirror.

### brief:acceptance

- Every item above is folded, or listed in the return with the reason it was not.

### brief:gates

The memory-hygiene hook, at the main loop's commit.

### brief:non-goals

- No code.
- No other spec.

### input:spec

memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md

### task:reuse

each spec's section 10 names its seam; recall terms below.

### card:route

- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-20 · spec memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-20-build-brief.md

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
