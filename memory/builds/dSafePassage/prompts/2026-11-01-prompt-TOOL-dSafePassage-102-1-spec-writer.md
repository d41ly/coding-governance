**Serves:** journal TOOL-dSafePassage-102

# gov-spec-writer handoff — TOOL-dSafePassage-102

<!-- gov:handoff role=gov-spec-writer build=dSafePassage unit=TOOL-dSafePassage-102 path=memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-102-1-spec-writer.md role-sha=06b14b1ac42a task-sha=87a85092f751 -->

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

This handoff is for build `dSafePassage`, unit `TOOL-dSafePassage-102`.
Not supplied, optional: `input:spec`.

### brief:goal

Author the spec of TOOL-dSafePassage-102, which `closes TOOL-dSafePassage-85`. The close's bar at `5fe2c7e34` (log copied to `C:/Users/daily-agent/AppData/Local/Temp/dsp86-logs/bar-5fe2c7e34.log`) reds exactly two legs: the spawn budget, on five rows of `memory/project/fork-ceilings.txt` (`run-gates-1leg` 56 over 55, `run-gates-2leg` 58 over 57, `memory-hygiene` 190 over 189, `manifest-check` 76 over 74, `check-wiring` 45 over 44), and install-prefix, on `tools/run-gates/ceiling-evidence.txt` lines 115, 134 and 146, whose how text spells `tools/memory-tree/routed_commits.py`, `tools/check-spec-tokens.py` and `tools/govkit/upgrade_walk.py`. Raise each of the five ceilings to its measured count, with each row's reason naming the owner's ruling and the cause ask 85 states (TOOL-dSafePassage-11's inlined resolver probe makes the counter see a fork the old form already spent, the real process count unchanged); `base` never moves. Respell each of the three how texts through `<prefix>/`, changing no other field. Tier-2, status `DEFERRED`, `closes TOOL-dSafePassage-85`, `order 16`, node `a`, `**Derived:** TOOL-dSafePassage-85` with the owner's quoted ruling in §9, §6 criteria each with a Red-when (the leg's own refusal line at `5fe2c7e34`, quoted from the log), §7 gates naming both legs, §10 reuse, §8 `none`. Add its row to the README `roster:units` table. Verify every cited line at the current HEAD before citing it.

### brief:items

- **Fork ceilings:** the five rows above; each ceiling equals its count, inside the file's max(3, 5 %) band; reason text carries the ruling.
- **Evidence how texts:** the three rows above; only the kit-path spelling changes; `python tools/run-gates/derive-ceilings.py --check` still exits 0 after the edit.
- **No other record moves:** no other ceiling row, no evidence value, no `base`.

### brief:acceptance

Both items are carried in 102's text. The spec is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in §6 is tracked by git; no backticked §6 token is a bare suite path or a code fragment that embeds a repository path.

### brief:gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### brief:non-goals

No new verb on derive-ceilings; no change to fork-count.sh, the counter or the probe; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row.

### task:reuse

each spec's §10 names its seam (tools/govkit/, tools/lib/, tools/push-main.sh).

### card:route

- build: dSafePassage
- unit: TOOL-dSafePassage-101 · spec memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-101.md
- brief: memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-101-build-brief.md

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
