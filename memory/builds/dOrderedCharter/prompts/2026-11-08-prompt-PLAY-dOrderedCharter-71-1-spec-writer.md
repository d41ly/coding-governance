**Serves:** journal PLAY-dOrderedCharter-71

# gov-spec-writer handoff — PLAY-dOrderedCharter-71

<!-- gov:handoff role=gov-spec-writer build=dOrderedCharter unit=PLAY-dOrderedCharter-71 path=memory/builds/dOrderedCharter/prompts/2026-11-08-prompt-PLAY-dOrderedCharter-71-1-spec-writer.md role-sha=07ad6a5d06b8 task-sha=80a217b6f32a -->

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

This handoff is for build `dOrderedCharter`, unit `PLAY-dOrderedCharter-71`.
Not supplied, optional: `input:spec`.

### brief:goal

Write unit 71's spec, so `python tools/govkit/govkit.py selfcheck` reports no problem over this tree, with a fix for the class.

### brief:items

1. **The red.** `govkit selfcheck` fails twice: `tools/playbook/positional-refs.txt` names the adopters NicoCares and inCMS.
   - Unit 70 set `tools/playbook/kit.toml`'s gov-only lists to `role = "project-owned"`.
   - `tools/govkit/govkit.py` defines that role as "the target authors it — gov supplies no bytes for this source, ever".
   - The adopter-name ban in `tools/govkit/govkit.py#selfcheck` still builds its population from every survivor's `src`, every role included.
     Its comment says "an adopter receives a `project-owned` seed as surely as an engine", which the role's own definition contradicts.
2. **The fix.** The ban's population leaves out `project-owned` rows, and its comment says why and what it does not check.
   - Read how `resolve_entry` reports a survivor's role, and how unit 70's `check_source_rows` treats the same rows, so one reading serves both.
   - The ban must still red on a shipped file naming an adopter.
3. **The arm.** One `tools/govkit/selftest.py` arm, by the suite's own conventions:
   - a `project-owned` source naming an adopter passes;
   - the same file under a shipping role reds.
4. **Owed by unit 70.** Three new helpers are lexicon verb offenders, taking the pin from 1209 to 1212. Rename each to a declared verb, and list
   both files in Files touched:
   - `fold` in `tools/memory-tree/merge-rows.py`;
   - `split_known` and `warn_grown_file` in `tools/run-gates/owed_rows.py`.
5. **Not this unit:** the content of `positional-refs.txt`, which stays as it is.

In the spec:

- Follow `memory/TEMPLATE-SPEC.md`, at `memory/builds/dOrderedCharter/spec/2026-11-08-spec-PLAY-dOrderedCharter-71.md`.
- Status `DEFERRED`, rev-1, dated 2026-11-08, base `9f41230b5`, streams tooling, `order 17`, advancing PLAY-dOrderedCharter-38, Tier-2.
- Declare the new arm on a `New arm:` line, and each leg it moves in section 7.
- New text cites code as `path#symbol`, outside the acceptance bullets. An acceptance bullet spells a plain tracked path, with no `#` and no
  `HEAD:` prefix. New text names a section in words, and names a check by what it checks.
- Any retirement word in section 2 owes its Readers clause.
- Run the hygiene spec checks (`--only 12,25`) after the file is tracked, since they read `git ls-files`: stage it first.

### brief:acceptance

- The spec exists, its acceptance includes `govkit selfcheck` exiting 0 over the tree and `lexicon OK` at the pin of 1209.

### brief:gates

Memory hygiene, as your role runs it.

### brief:non-goals

- No code. No edit to another spec.

### task:reuse

each spec's section 10 names its seam; recall terms below.

### card:route

- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-70 · spec memory/builds/dOrderedCharter/spec/2026-11-05-spec-PLAY-dOrderedCharter-70.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-05-prompt-PLAY-dOrderedCharter-70-build-brief.md

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
