**Serves:** journal TOOL-dGroundRules-10

# gov-spec-writer handoff — TOOL-dGroundRules-10

<!-- gov:handoff role=gov-spec-writer build=dGroundRules unit=TOOL-dGroundRules-10 path=memory/builds/dGroundRules/prompts/2026-10-24-prompt-TOOL-dGroundRules-10-2-spec-writer.md role-sha=06b14b1ac42a task-sha=c95a7d916ce4 -->

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

This handoff is for build `dGroundRules`, unit `TOOL-dGroundRules-10`.

### brief:goal

Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md` to the run's rulings. Author only: no product code, no commit, no gate.

### brief:items

1. **The stranded citations, rung 5 (ER:388).** The two `[cite]` hits are waived in `memory/project/spec-token-waivers.txt`, one row each, keyed on the cited token, reason naming the other build's live spec and that this unit's retirements moved the lines; the registry is shrink-only, so this is a `relaxes:` departure (the count 34 to 36) recorded in a deviation record carrying `**Bound:**`, `**Tier:**` and `**Reason:**` per `memory/HYGIENE.md` "Deviation records"; and an ask row in this build's `BACKLOG.md` asks TOOL-aOrientedCast-28 and TOOL-dFairHearing-22 to re-cite `agent-cap.js` by symbol, which retires the two rows. Editing another build's spec is refused by this build's README rule (outside writes are ask rows only); keeping `agent-cap.js` padded to its old length is refused as dead bytes. S4 states this, §4's files touched adds the waiver registry, `BACKLOG.md` and the deviation record, and §7 adds the `spec tokens` leg. Cite ER:388 in the §8 mark and say the commit's `Decided:` trailer carries `relaxes: spec-token-waivers shrink-only count` and `widens: none`.
2. **Readers S4/§4 must name**, each with what changes: `tools/workflows/check-review-join.test.sh` (its environment-refusal arm sets `AGENT_CAP=7`; under `--only=join` it needs a stub predicate); `tools/roles/adopt-roles.test.sh` (arms 6 and 11 run gov's hook in a fixture with no settings, so they take a hook copy with no `policy` kit beside it, as the rule-6 section does); `.lexicon.conf` (`VERB_OFFENDER_PIN` 1213 to 1204, nine offenders leaving with the retired code); `help/policy.md` (the sentence "No gate or hook reads a value through it yet" goes stale); `tools/policy/README.md` (the CLI list gains the `settings` verb and `--live`). §7 adds `roles adopter self-test` and any leg those paths trip (`python tools/check-spec-tokens.py --list`).
3. **The kit version.** No version marker moves on the branch, following the build brief (the lander mints versions at landing); S4's `2.0` becomes "the major bump the retirements owe, minted at landing", the `gov:kit agent-cap@` markers in `tools/hooks/format-guard.js` and `tools/hooks/scratch-guard.js` stay unchanged, and §7 names `kit version markers` and `kit epoch` as legs the close grades.
4. The status header's rev rises by one, with a §9 line naming what disagreed and each ruling.

### brief:acceptance

`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); every `**Carries:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line; the spec stays under 49152 bytes.

### brief:gates

No gate runs in this pass.

### brief:non-goals

Any other spec; product code; the status cell, which stays `DEFERRED`.

### input:spec

memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md

### task:reuse

each unit's §10 names its seam: read_policy_key/resolve_read in tools/lib and tools/hooks/agent-cap.js, tools/gate-legs.json, tools/govkit/registry.toml.

### card:route

- build: dGroundRules
- unit: TOOL-dGroundRules-66 · spec memory/builds/dGroundRules/spec/2026-10-24-spec-TOOL-dGroundRules-66.md
- unit: TOOL-dGroundRules-7 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-7.md
- unit: TOOL-dGroundRules-8 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-8.md
- unit: TOOL-dGroundRules-10 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md
- unit: TOOL-dGroundRules-9 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-9.md
- unit: TOOL-dGroundRules-15 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-15.md
- unit: TOOL-dGroundRules-17 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-17.md
- unit: TOOL-dGroundRules-18 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-18.md
- unit: TOOL-dGroundRules-20 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-20.md
- unit: TOOL-dGroundRules-21 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-21.md
- unit: TOOL-dGroundRules-22 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-22.md
- unit: TOOL-dGroundRules-23 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-23.md
- unit: TOOL-dGroundRules-25 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-25.md
- unit: TOOL-dGroundRules-29 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-29.md
- unit: TOOL-dGroundRules-27 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-27.md
- unit: TOOL-dGroundRules-30 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-30.md
- unit: TOOL-dGroundRules-31 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-31.md
- unit: TOOL-dGroundRules-32 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-32.md
- unit: TOOL-dGroundRules-33 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-33.md
- unit: TOOL-dGroundRules-34 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-34.md
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
