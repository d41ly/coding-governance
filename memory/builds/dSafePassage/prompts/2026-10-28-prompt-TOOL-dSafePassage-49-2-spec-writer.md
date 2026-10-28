**Serves:** journal TOOL-dSafePassage-49

# gov-spec-writer handoff — TOOL-dSafePassage-49

<!-- gov:handoff role=gov-spec-writer build=dSafePassage unit=TOOL-dSafePassage-49 path=memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-49-2-spec-writer.md role-sha=06b14b1ac42a task-sha=2d624ea50972 -->

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

This handoff is for build `dSafePassage`, unit `TOOL-dSafePassage-49`.
Not supplied, optional: `input:spec`.

### brief:goal

Every criterion of TOOL-dSafePassage-49 can go green against HEAD's code plus this unit's own writes.

**What the builder measured.**
1. **AC14 is red by construction.** It asserts that `--plant subsection-password-space` prints no substring of `se cret` longer than 2 characters. Every refused step prints TOOL-dSafePassage-24's fixed refusal from `run_step_isolated` (`tools/govkit/upgrade_steps.py`): "...declares what git runs as a program or sends as a credential, <entries>, so nothing was spawned". ` credential` contains `cre` and ` cr`, both pieces of `se cret`, so the assertion is red even when the redaction is correct. That lead text is pinned by the `[dSP-24]` needles in `tools/govkit/selftest.py`. The TOOL-45 and TOOL-38 plants escaped this only by luck.
2. **AC2 / S4 / §8 F1(a).** F1(a) RESOLVED that the build run's sweep moves TOOL-dSafePassage-4 to order 3 and -18/-19 to order 4 before the roster is handed out. That never happened. TOOL-4, -7, -18, -19 and -43 are now CLOSED. The run built them in consumes-from topological order, which is recorded in RUN.md's dispatch rows. Their headers still read 4 at order 2 and 18/19 at order 3, so AC2 ("TOOL-4's order is greater than TOOL-43's and TOOL-7's") is red, and a CLOSED spec's header is not this unit's to edit.
3. **For the rebuild (not divergences):**
   - AC12: `not refused` and `ssh://` sit on adjacent lines 71 and 72 of `help/upgrade-steps.md`, so one sentence needs reflowing.
   - AC5: "exactly one `startswith(DOWN_STOP_PREFIXES)` call" also needs the rollback fixture's own check at `upgrade_steps.py:4405` to compare through `test_step_row`.
   - AC3: the `rolled-back-witness-holds` plant cannot reach the walk through `derive_reverse_steps`, which drops `rolled-back` rows. The plant must record s2 `rolled-back` after the rows are derived, for example in the reverse child before `run_reverse_walk`.
   - S6/AC7 and AC8's data already hold.

**The main loop's recommendations.**
- **(1)** Make AC14 grade only the refusal's named entries, the text after TOOL-dSafePassage-24's fixed lead, for any 3-character piece of the password. Also grade the whole output for the full password and for each space-separated half. This is the class fix: any future password is graded the same way. Name the trap in AC14's Red-when.
- **(2)** Strike F1(a)'s sweep and AC2. The order relation it protected was dispatch order, and the run already honoured it by consumes-from. Record that in §8 F1 as re-resolved, citing RUN.md's dispatch sequence. S4 shrinks to whatever residual remains, or is struck.
- **(3)** Fold the rebuild notes into the criteria they touch.

Take each recommendation unless the code shows it breaks a written criterion. Record a rejected one in §8 with its reason.

### brief:items

1. **Revise TOOL-dSafePassage-49** as a rev bump dated 2026-10-28, still `DEFERRED`, with one §9 line naming this brief.
2. **Cross-read** TOOL-dSafePassage-45 (its AC6 no-substring assertion has the same latent class; it is CLOSED, so report it) and every DEFERRED spec that cites F1(a)'s sweep or TOOL-49's AC2. CLOSED specs are read-only.
3. **Commit nothing.** Return the files you wrote.

### brief:acceptance

- AC14 names the graded span and the fixed-lead trap. AC2 and the sweep are struck or re-resolved, citing RUN.md.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### brief:gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### brief:non-goals

- No product code.
- No edit to a CLOSED spec.
- No commit, and no stage into the real index.

### task:reuse

each spec's §10 names its seam (tools/govkit/, tools/lib/, tools/push-main.sh).

### card:route

- build: dSafePassage
- unit: TOOL-dSafePassage-49 · spec memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-49.md
- brief: memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-49-build-brief.md

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
