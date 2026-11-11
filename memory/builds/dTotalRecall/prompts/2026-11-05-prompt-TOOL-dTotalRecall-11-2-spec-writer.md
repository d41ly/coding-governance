**Serves:** journal TOOL-dTotalRecall-11

# gov-spec-writer handoff — TOOL-dTotalRecall-11

<!-- gov:handoff role=gov-spec-writer build=dTotalRecall unit=TOOL-dTotalRecall-11 path=memory/builds/dTotalRecall/prompts/2026-11-05-prompt-TOOL-dTotalRecall-11-2-spec-writer.md role-sha=dcd8416ea3d2 task-sha=a6510724d5d0 -->

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

This handoff is for build `dTotalRecall`, unit `TOOL-dTotalRecall-11`.
Not supplied, optional: `card:route`.

### brief:goal

Revise TOOL-dTotalRecall-11 and -25 so what they say of dDeclaredLoop's `review.cost` row and of TOOL-dTotalRecall-2 S9's door agrees with those specs as they stand. Neither unit's build changes.

### brief:items

Read the cross-check record first, `memory/builds/dTotalRecall/build/2026-11-05-build-TOOL-dTotalRecall-1-parents-crosscheck.md`. Its rows name each MISMATCH; the readers' returns in `memory/builds/dTotalRecall/build/2026-11-05-build-TOOL-dTotalRecall-1-crosscheck-returns.md` quote both sides and state the change. The specs are read at the branch tip, which holds the owner's fork picks of 2026-11-05 merged after the readers ran: re-read both sides of every row before you edit, against today's text. A row the parent's text does not bear out, or that a fork pick already settled, is not edited: return it as refused, with the line that refutes it. Cite a parent by section, not by line, wherever you touch a cite.

One writer per group below. The spec your task block's `input:spec` names leads one group: revise every spec of that group and no other.

#### Group A, led by spec 11: specs 11 and 25

- **Row 7, tr11 §3, the writers of `new shape-run`.** tr11 §3 names TOOL-dDeclaredLoop-20's `review.cost` act row as a caller of `gov_record.py new shape-run`; dl20 S3 limits `review.cost` to the shape line's four fields and no dDeclaredLoop spec calls the verb. §3 stops naming dl20 as a caller; it states that no parent spec owns the review-act writer yet, a later unit or an ask does, and that TOOL-dWellOiledMachine-19 calls the `--act` form.
- **Rows 10 and 11, tr25 §8 F2 and the §3 non-goal, the `fence` row's writer.** Both say tr2's door replaces the `stream-plan` row's `hand` writer when the planner lands. Since TOOL-dTotalRecall-1 rev-5, tr2 S9 moves only `fields`-form `hand` rows and names the owner of every other row's door in its pass's `Decided:` trailer. F2 (resolved as it stands, its pick untouched) and the non-goal say the `fence` row keeps `hand` through tr2 S9, that trailer names dIndexedDesign's planner as the door's owner, and the writer cell moves when that planner lands its own verb, not through tr2's door.

### brief:acceptance

- `wc -c` of every spec you revise is under 49152.
- Each revised spec's **Status:** line carries its next rev and the date `2026-11-05`, every other
  field kept, and its §9 holds one new line in the existing form: `- rev-<n> · 2026-11-05 · <sections>
  · <what moved>, by the brief prompts/2026-11-05-prompt-TOOL-dTotalRecall-1-parents-reground.md`.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your
  specs staged into it through `GIT_INDEX_FILE`, names nothing of your specs. Delete the copy after.
  Findings that only a `gen_build_index.py --write` render cures belong to the main loop: name them and
  leave them.

### brief:gates

Only the memory hygiene gate, as the role allows. The main loop runs the rest and renders the index.

### brief:non-goals

- No file outside the specs your group names. No commit, no stage into the real index, no deviation
  record: the main loop writes those.
- No file of another build. A parent spec that looks wrong is a line in your return, not an edit.
- No fork opened or re-opened; a fork the owner's picks resolved stays resolved as written.
- No change to what a unit builds beyond what an item states.

### input:spec

memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-11.md

### task:reuse

the 2026-11-03 crosscheck records and briefs in memory/builds/dShippedRelease/build/ and prompts/ as the template; tools/roles/handoff.py render/agents; tools/memory-tree/gen_build_index.py.

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
