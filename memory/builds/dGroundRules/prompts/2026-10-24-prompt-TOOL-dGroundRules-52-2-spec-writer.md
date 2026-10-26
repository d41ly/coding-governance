**Serves:** journal TOOL-dGroundRules-52

# gov-spec-writer handoff — TOOL-dGroundRules-52

<!-- gov:handoff role=gov-spec-writer build=dGroundRules unit=TOOL-dGroundRules-52 path=memory/builds/dGroundRules/prompts/2026-10-24-prompt-TOOL-dGroundRules-52-2-spec-writer.md role-sha=06b14b1ac42a task-sha=0ba9fb5b5554 -->

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

This handoff is for build `dGroundRules`, unit `TOOL-dGroundRules-52`.

### brief:goal

Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-52.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### brief:items

1. §1: drop the claim that order 16 sits above every unit; state its actual order.
2. S1, S5's AC3 half and S10 (findings 3, 12, 25) are restated as closed by TOOL-dGroundRules-43 rev-5 (6e8863f43), whose `EVIDENCE` reads the build README whole; S7 and S17 (findings 14 and 7) as closed by -43 rev-5's `ORDER_SHIFT` (AC6).
3. S4 and AC4: `derive_parallel_step` is built by TOOL-dGroundRules-25 (b663756ca) in `tools/memory-tree/gen_build_index.py`, and the steps hold more than two units; restate the edge and the criterion, or drop them if nothing remains.
4. S6 and AC6: `derive_guardable_reads` already sends bytes (TOOL-dGroundRules-36, cc4b4e53b); the unbuilt parts are `-z`, `fsencode` and the matched count, and AC6 observes those.
5. S8 and S23 are built (`os.fsdecode` in `check_guard_trace`'s helper, TOOL-dGroundRules-33, eb67e2cc8); S25's suppress half is built (TOOL-dGroundRules-35, 764a8a282) and only the `unmapped` line is new; the module set is `SOURCE_READS` and `kept` is a local of `check_guard_trace`.
6. S9: `check_guard_lines` is built (7a600abf5), called by `run_fixture`, and TOOL-dGroundRules-43 rev-5 AC8, AC9, AC11 and AC12 rest on it; S9 keeps it and takes out no part of it, and its Readers line names `run_fixture`.
7. S13 and AC11 observe through TOOL-dGroundRules-41's `INSTALL_LINES` and `HELP_LEGS` (rev-4, built at 277c9e37f); -48 rev-2 defines no `INSTALL_LINES_WHOLE`; update the consumes-from edges to name -41.
8. S21: `check_writes_intersect` is already graded by TOOL-dGroundRules-40's arm over `OVERLAP_PAIRS`; restate what this unit adds, if anything.
9. AC5: -43 rev-5 AC1 observes through TOOL-dGroundRules-40's `PAIRS_PY`/`PAIRS_SH`; AC5 names those, or -45's `PAIRS_TABLE` only with the precondition that -45 is built.
10. Every staging into `build_fresh_target` (`PLANT_TWO`, `PLANT_NONASCII`, `PLANT_BYTES`, `PLANT_REFUSED`) names `run_fresh_target`, the case runner in `tools/policy/check_policy.py`.
11. S18 and AC15: the deny branch is built by TOOL-dGroundRules-38 (8b50fc8bb); `NO_GIT` staging targets `policy.run_git` callers, so restate AC15 as green before this unit or drop it.
12. Every bare `check_policy.py` in a literal (`GUARD_LINES_GONE`, `PREFIXED`, `COLD_WRITING`, AC3, AC10) is spelled `tools/policy/check_policy.py`, and the §6 preamble's claim about -43 is restated.
13. Units 1 to 41 are built (HEAD 8eab342e0); TOOL-dGroundRules-51, -53, -54, -57, -58 and -59 are retired WONTDO, so no criterion may consume a literal of theirs.
14. Re-cite every moved line by symbol or AC id, not line number.
15. Drop any claim that the policy legs or `tools/policy/check_policy.py` do not exist or cannot run; `policy fixtures` is a leg in `tools/gate-legs.json`.
16. The status header's rev rises by one, with a revision-log line (§9 in a Tier-2 spec, §8 in a Tier-1 one) naming the disagreements and the rulings. Keep the file under 48600 bytes measured with its records region; every acceptance-section code span stays on one line; every acceptance bullet keeps a `Red when:` clause, and no line in the acceptance section starts at column 0 with `AC<n>`, wrapped prose included; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token; an untracked or fixture-relative path sits inside a fenced block or carries its target placeholder; every command a criterion runs is spelled so it runs from the repository root; a criterion that is green before this unit is restated as such, with the staged break or later observation that can red.

### brief:acceptance

`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); every `**Carries:**`/`**Derived:**` line, the H1 and the RESOLVED marks of the open-questions section survive; every acceptance-section code span sits on one line.

### brief:gates

No gate runs in this pass.

### brief:non-goals

Any other spec; product code; the status cell, which stays `DEFERRED`.

### input:spec

memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-52.md

### task:reuse

each unit's §10 names its seam: read_policy_key/resolve_read in tools/lib and tools/hooks/agent-cap.js, tools/gate-legs.json, tools/govkit/registry.toml.

### card:route

- build: dGroundRules
- unit: TOOL-dGroundRules-41 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-41.md
- unit: TOOL-dGroundRules-42 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-42.md
- unit: TOOL-dGroundRules-43 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md
- unit: TOOL-dGroundRules-44 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-44.md
- unit: TOOL-dGroundRules-45 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-45.md
- unit: TOOL-dGroundRules-46 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-46.md
- unit: TOOL-dGroundRules-47 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-47.md
- unit: TOOL-dGroundRules-48 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-48.md
- unit: TOOL-dGroundRules-49 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-49.md
- unit: TOOL-dGroundRules-50 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-50.md
- unit: TOOL-dGroundRules-51 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-51.md
- unit: TOOL-dGroundRules-52 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-52.md
- unit: TOOL-dGroundRules-53 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-53.md
- unit: TOOL-dGroundRules-54 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-54.md
- unit: TOOL-dGroundRules-55 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-55.md
- unit: TOOL-dGroundRules-56 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-56.md
- unit: TOOL-dGroundRules-57 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-57.md
- unit: TOOL-dGroundRules-58 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-58.md
- unit: TOOL-dGroundRules-59 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-59.md
- unit: TOOL-dGroundRules-60 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-60.md
- unit: TOOL-dGroundRules-61 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-61.md
- unit: TOOL-dGroundRules-62 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-62.md
- unit: TOOL-dGroundRules-63 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-63.md
- unit: TOOL-dGroundRules-64 · spec memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-64.md
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
