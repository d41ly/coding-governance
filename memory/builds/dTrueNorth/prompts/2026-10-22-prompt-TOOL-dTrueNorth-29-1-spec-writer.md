**Serves:** journal TOOL-dTrueNorth-29

# gov-spec-writer handoff — TOOL-dTrueNorth-29

<!-- gov:handoff role=gov-spec-writer build=dTrueNorth unit=TOOL-dTrueNorth-29 path=memory/builds/dTrueNorth/prompts/2026-10-22-prompt-TOOL-dTrueNorth-29-1-spec-writer.md role-sha=06b14b1ac42a task-sha=16afc900a427 -->

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

This handoff is for build `dTrueNorth`, unit `TOOL-dTrueNorth-29`.
Not supplied, optional: `input:spec`.

### brief:goal

Author TOOL-dTrueNorth-29, one Tier-2 unit whose pass turns each red this build caused green, fixing the cause in code or in the suite's own fixture, never by loosening an assertion. Author only: no product code, no commit, no gate.

### brief:items

1. `spec-tokens self-test`: the six AC6 arms of `tools/check-spec-tokens.test.sh` (the block after its `# AC6 — the staged breaks` comment) write each broken copy of the checker to `$base`, a scratch directory with no `memory-tree` kit beside it. Since TOOL-dTrueNorth-27 S5 inlined `resolve_kit_dir`, such a copy refuses with `REFUSING — the memory-tree kit's design_lib.py does not resolve` before it reaches `CLAIM_CANARY`, so every arm reds. Place the copies where the inlined resolver finds the kit, keeping each arm's stated break. The suite's two `parity:` arms (the measure-legs ceiling of 500 s above the 300 s bound) are red at the base too and are not this unit's.
2. `row-grammar selftest`: the arm `no sibling engine in this kit imports corpus_ids or gen_build_index` finds `deviation_join.py:473`, the `import gen_build_index as gbi` TOOL-dTrueNorth-4 added in `read_population` for the binding classifier and the header grammar. Remove the sibling import (move what it uses to a module both may import, or read it another way the rule allows); the arm is not loosened.
3. `tier2-review self-test`: the arm `spec-audit: a spec that is also a subject is refused` passes `specs: ['s.md']` while the suite's `SPEC` fixture subject is now `memory/builds/dX/spec/s.md` (it was `s.md` at the base), so the harness's exact-path overlap check finds no overlap. Make the arm name the subject's own path; say whether the harness should also match a differently spelled path, and if so, specify it.
4. `unattended-build self-test`: `TN5-AC3 a caller subject with no id is refused naming the field` no longer sees `THROW unattended-build: subject 0's \`id\` is not a unit id`, and the suite executed 342 assertions against its floor of 343. Find whether the substitution the arm stages still matches the roster it edits, or the harness now names another field first, and fix the cause; account for the one unreached assertion.
5. `memory-hygiene self-test`, three findings, each red only at HEAD:
   - `tools/memory-tree/.memory-tree.conf.example` declares none of `DESIGN_BASELINE`, `DESIGN_NODES`, `DESIGN_RECORD`, `DESIGN_VIEW`, which the kit's modules read; declare each, blank, with its meaning, as the example declares the other keys.
   - two check 21 arms (`the audit-pin arm did not count the record an older harness wrote as exempt`, and `a record an older harness wrote, merged after the pinning harness landed, fails check 21`): the writer test no longer exempts the older harness's record in the suite's fixture, after TOOL-dTrueNorth-14, -19, -20 and -27 moved the harness reach to a stand-in resolver and a `harness/` directory. Fix the fixture or the reach so the exemption holds.
   - the partition arm: the unscoped run prints `check 29: coverage off` and `check 30: as-built view: off` lines that no scoped run prints. Make the scoped runs partition the unscoped run's lines again. At the base this arm reds only on the check 26 `cache hits` count, which differs between runs; that half is not this unit's.
6. Not this unit's, and the spec says so in §3: `measure-legs selftest` (red at the base), `pre-push self-test` (green alone at HEAD in a scratch clone; its one red arm, TOOL-aSparedSpawn-33 AC1's bar reuse, ran beside four neighbours), `foreign-prefix parity` (it re-runs every self-test, so it follows the others), and `govkit selftest` unless the base run says otherwise (the main loop adds it if so).
7. The spec carries `**Derived:** PLAY-dClosedLoop-2`, `order 12`, Tier-2, status OPEN, path `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-29.md`, and one AC per item that a pass can observe with a probe on the touched files: the suites themselves are the close's, and a unit runs none of them.
8. Write `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-29-deviation-31.md` for the unit itself: Departs from `dTrueNorth [roster]`, design-to-spec, builder discovery, additive, spec writer under author-recorded, `new unit TOOL-dTrueNorth-29`, Caused-by `PLAY-dClosedLoop-2`.

### brief:acceptance

`python tools/check-spec-tokens.py` prints no hit on the spec; every AC is a probe a pass can run; the record reads with no malformed field under `python tools/memory-tree/deviation_join.py`.

### brief:gates

No gate runs in this pass; the spec's §7 names the five legs and every leg its files trip.

### brief:non-goals

Any other spec; product code; loosening an assertion; a waiver row; the inherited reds of item 6; inside §6, an untracked file named by full path inside a backticked token.

### task:reuse

tools/check-spec-tokens.py (the handoff join's cutoff seam), memory/builds/dClosedLoop/build/*-carries.py, *-deviations.py, *-asbuilt.py as the bootstrap semantics and plant suites, tools/unattended/lib-unattended.sh baseline_units for unit 7; per-spec §10 carries each probe.

### card:route

- build: dTrueNorth
- unit: TOOL-dTrueNorth-27 · spec memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-27.md
- brief: memory/builds/dTrueNorth/prompts/2026-10-21-prompt-TOOL-dTrueNorth-27-build-brief.md

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
