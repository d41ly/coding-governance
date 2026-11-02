**Serves:** journal TOOL-dSafePassage-41

# gov-spec-writer handoff — TOOL-dSafePassage-41

<!-- gov:handoff role=gov-spec-writer build=dSafePassage unit=TOOL-dSafePassage-41 path=memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-41-2-spec-writer.md role-sha=06b14b1ac42a task-sha=cf250da8c773 -->

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

This handoff is for build `dSafePassage`, unit `TOOL-dSafePassage-41`.
Not supplied, optional: `input:spec`.

### brief:goal

AC2 observes the `ac-order` join grading a non-empty live population on the real tree. It does not depend on specs that the unattended harness flips straight from DEFERRED to CLOSED.

**What the builder measured.**
- The join grades only the specs that `LIVE` matches (`tools/check-spec-tokens.py:331`: OPEN, SPECCED, INPROGRESS, BLOCKED). The module docstring counts a DEFERRED spec as terminal.
- Under the build run, every dSafePassage spec is CLOSED or DEFERRED. The one exception is the unit being built, which is INPROGRESS during its pass.
- No other build has a live spec dated 2026-10-23 or later: dDeclaredLoop's are DEFERRED, and dClosedLoop's is dated 2026-10-20.
- A probe of the join's own predicate over the tree, run with this spec at INPROGRESS (`C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dsafepassage-567339/c5f50d22-89c6-41d7-84e5-2382dcd49faa/scratchpad/ao41_pred.py`), graded 1 of 37 live specs, this one, with 0 out of order.
- Once the pass commit flips this spec to CLOSED, the count is 0. That is AC2's own red case, and the empty population the `[gate]` rule forbids reading as coverage.
- AC1 is buildable as written. The builder's join patch is kept at `scratchpad/TOOL-dSafePassage-41-join.patch`, and its fixture runs are recorded in the hand-back.

**The main loop's disposition.**
- AC2 is observed during the pass, with this spec at INPROGRESS: the join's run line grades at least 1 live spec dated on or after the key, and finds 0 out of order.
- AC2 states that the same line at the close may grade 0, because the harness closes every spec. Under `[gate]`, that 0 is not coverage. Coverage is AC1's fixture plus this pass-time observation.
- Cite hygiene check 29's identical note: "under the unattended harness a spec goes OPEN to CLOSED in its build commit, so this check grades attended builds only".
- Do not widen `LIVE`, and do not move the key. Both are non-goals, and TOOL-dSafePassage-34's.

### brief:items

1. **Revise TOOL-dSafePassage-41** as a rev bump dated 2026-10-28, still `DEFERRED`:
   - restate AC2 and its Red-when as above;
   - correct §1's and §4's order-table claim that the join grades specs dated 2026-10-23 or later, so it says which of those are live and when;
   - add one §9 line naming this brief.
2. **Cross-read** TOOL-dSafePassage-34 §4's "a join seen grading nothing is not a gate", and TOOL-dSafePassage-46 and -42, which read 41's join. Fix a DEFERRED disagreement in place. CLOSED specs are read-only.
3. **Commit nothing.** Return the files you wrote.

### brief:acceptance

- AC2 names the INPROGRESS observation, the close-time 0, and check 29's note.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### brief:gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### brief:non-goals

- No product code.
- No change to `LIVE` or to the key.
- No edit to a CLOSED spec.
- No commit, and no stage into the real index.

### task:reuse

each spec's §10 names its seam (tools/govkit/, tools/lib/, tools/push-main.sh).

### card:route

- build: dSafePassage
- unit: TOOL-dSafePassage-41 · spec memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-41.md
- brief: memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-41-build-brief.md

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
