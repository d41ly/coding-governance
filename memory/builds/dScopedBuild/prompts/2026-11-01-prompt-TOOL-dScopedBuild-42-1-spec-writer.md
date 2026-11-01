**Serves:** journal TOOL-dScopedBuild-42

# gov-spec-writer handoff — TOOL-dScopedBuild-1

<!-- gov:handoff role=gov-spec-writer build=dScopedBuild unit=- path=memory/builds/dScopedBuild/prompts/2026-11-01-prompt-TOOL-dScopedBuild-42-1-spec-writer.md role-sha=06b14b1ac42a task-sha=c70830e783cc -->

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

This handoff is for build `dScopedBuild`, and names no single unit.
Not supplied, optional: `card:route`.

### brief:goal

Every unit of dScopedBuild specced and built, so that each of the 15 clauses of its row in v2's `[chain]` (Items) is carried by a spec pinned to its hash and built, each of its 23 owned nodes (Owned nodes) is built, and each of its 10 owned gaps (Gaps) is closed.

### brief:items

Each clause of the row, in its order: its id at its baseline hash, its hash now in the as-built view with the record behind any change, its tokens as `carries.py`'s token arm reads them, and its text.

1. `cl-dClosedLoop-0399@182b9f2d` · now `182b9f2d`, as at the baseline · tokens: none, so the token arm cannot see this clause — one exit contract with a history-derived base, refusing a build's exit while a core red its own commits introduced stands
2. `cl-dClosedLoop-0400@d5dcbafa` · now `d5dcbafa`, as at the baseline · tokens: `review.findings` — built specs frozen, a revision of a spec whose unit has landed refused at the commit with or without a deviation record, seen red on a planted in-place edit of a landed unit's spec and green on a status-only edit, and every closing-review finding disposed as new units by `review.findings`
3. `cl-dClosedLoop-0401@e53987d9` · now `e53987d9`, as at the baseline · tokens: none, so the token arm cannot see this clause — scope at the push
4. `cl-dClosedLoop-0402@19e9688b` · now `19e9688b`, as at the baseline · tokens: `review.build.when` — the closing review recorded, run as `review.build.when` says, once per build, per unit or per landing, each value seen on its planted case
5. `cl-dClosedLoop-0403@3c89f2a1` · now `3c89f2a1`, as at the baseline · tokens: none, so the token arm cannot see this clause — a write gate reading derived state
6. `cl-dClosedLoop-0404@f111410c` · now `f111410c`, as at the baseline · tokens: none, so the token arm cannot see this clause — the per-pass checklist's retirement witnessed at Build, a planted pass that calls the lookup by a write set's paths red (the night pass two's review, the owner's NT-24)
7. `cl-dClosedLoop-0405@431edacd` · now `431edacd`, as at the baseline · tokens: none, so the token arm cannot see this clause — the core checks run by the executor at Build's exit
8. `cl-dClosedLoop-0406@c1850071` · now `c1850071`, as at the baseline · tokens: `build.scope`, `build.unit-pass`, `file`, `hunk`, `off`, `retrofit.claim-cap`, `retrofit.claim-on-touch`, `retrofit.drain`, `retrofit.drain-cap` — `build.unit-pass` and `build.scope` draining the legacy a unit touches as `retrofit.drain` says, its changed hunks under `hunk`, every baselined site in each touched file under `file`, both under `retrofit.drain-cap`, and nothing owed under `off`, and claiming the baselined map keys its write set holds (dossiers) under `retrofit.claim-cap`, carrying them with an ask, or neither, as `retrofit.claim-on-touch` says, each value seen on a planted unit
9. `cl-dClosedLoop-0407@b6ab4b28` · now `f551b213` by deviation `2026-11-01-build-TOOL-dScopedBuild-9-deviation-91` · tokens: `build.scope`, `drop_touched_exemptions`, `git diff-tree -U0 --no-merges -M`, `tools/lib` — the touch join as `build.scope`'s one check, graded by its value, over the union of `git diff-tree -U0 --no-merges -M` across the unit's own commits, calling the pure `drop_touched_exemptions` through the map's own CLI, `map_diff.py --paths-from - --drop-affordance-exempt --check`, by subprocess, wherever the map kit homes the function, the map's own writer behind a point, and the claim arm "not installed" where the map is absent, seen on a planted core-only tree (H5)
10. `cl-dClosedLoop-0408@e14d93bc` · now `9fd076d5` by deviation `2026-11-01-build-TOOL-dScopedBuild-10-deviation-101` · tokens: `reproduction` — a red-first reproduction, a confirmed `reproduction` probe record serving the unit, before the first dispatch of any unit whose spec header closes or advances an ask carrying a `seen` clause, the ask being the bug report and the unit its fix, whether or not the build is a patch (night pass, point 2)
11. `cl-dClosedLoop-0409@5b78cbe2` · now `5b78cbe2`, as at the baseline · tokens: none, so the token arm cannot see this clause — a playbook's pieces built as units with piece records joined by hash, and a proposal to amend the playbook filed as an ask (night pass, point 1)
12. `cl-dClosedLoop-0410@dce90a3a` · now `869f06dd` by deviation `2026-11-01-build-TOOL-dScopedBuild-12-deviation-121` · tokens: `build.reuse-check`, `build.reuse-check.second-pass`, `bypassed`, `duplicate`, `flow.route-backs`, `new`, `not-a-unit`, `should-extend` — `build.reuse-check`, per unit before the closing review: the reuse scout at medium over the units the unit's commits add, listed by the ported diff lister `map_diff.py --added-units` with the code record's added definitions joined to it where the record is installed, and capped at sixty with an overflow line, one row per unit (`duplicate`, `should-extend`, `new` or `not-a-unit`, each with its nearest existing symbol or what was searched), added rows for what the lister cannot see, a no-stop line, and one row per MUST seam the unit's spec carried, a `duplicate` or `bypassed` row routing to a fix pass, a second independent pass as `build.reuse-check.second-pass` says, a row the fix pass disputes, with its reason, going to the closing review, re-entries bounded by `flow.route-backs`, and an overflow past sixty never read clean, its remainder taken by a further pass, seen on a planted false `duplicate` and on sixty-one added units whose last is a duplicate, and its acceptance a reproduction of aScoutedSeam's measured figures through gov's own route on its 23 tuning and 12 held-out cases, at least 29 of 35 for the check with the card and 31 of 35 for the system, parsed replies counted first (the night pass two, point 2, the owner's NT-11 and NT-13)
13. `cl-dClosedLoop-0411@78cc90dd` · now `78cc90dd`, as at the baseline · tokens: none, so the token arm cannot see this clause — the closing review handed, beside its range, each unit's acceptance criteria and the MUST seams its spec carried as rows each finder answers, recorded, and gating once a measurement passes (the night pass two, point 4, the owner's NT-10)
14. `cl-dClosedLoop-0412@021fa28b` · now `021fa28b`, as at the baseline · tokens: `build.scope`, `deviation.gate` — the deviation gate under `deviation.gate`: dTrueNorth's joins read at the commit and at the Build exit beside `build.scope`, an unrecorded deviation refused, warned with an ask or reported as the key says, each value seen on its planted case (the owner's FQ-3, P41)
15. `cl-dClosedLoop-0506@2200c4c7` · now `2200c4c7`, as at the baseline · tokens: `build.acceptance`, `test.seen-red` — `build.acceptance` writing the seen-red record: the executor re-running each new or changed gate's planted red beside the unit's acceptance commands, one record per gate keyed by leg and red SHA, which dWitnessedBar's `test.seen-red` reads, a planted red that stays green failing the acceptance, seen red on a planted gate whose red never ran (gap-test-06, the owner's FK-4-12 and FK-5-2)

### brief:acceptance

- At the Design exit, `carries.py --build dScopedBuild --exit` exits 0 over the build's specs: each clause in Items carried whole, or in parts 1/n to n/n, at its hash; each owned node named by a spec; each clause's tokens in its carriers.
- Each clause's own seen-red cases, stated in its text, observed as it states them.
- Every departure from a clause, or from a spec after its first pass, is a deviation record that `deviations.py` joins, and the build's departures report lists it (README rule 4).

### brief:gates

- `packet.py --check dScopedBuild` green before the first pass. A red on a moved instrument blob is a stop, never re-rendered away (README rule 2).
- `carries.py --build dScopedBuild --exit` at the Design exit while it is in service (the execution plan's `[phase-1]` retirement table).
- The close sequence of README rule 4, then the bar the driver owes at `--close`.

### brief:non-goals

- v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: frozen at the baseline, so a change to a clause is a deviation record approved by its risk.
- The 494 clauses of the other 21 chain builds' rows: carrying one needs a `**Moved:** <clause id> to dScopedBuild by <decision>` line.
- Any path outside `memory/builds/dScopedBuild/`, but the product paths a build run's units record with `--dispatch --writes`, an ask row in another build's `BACKLOG.md`, and the shared renders a landing re-renders (README rule 7).
- Another build's packet, the instruments under `memory/builds/dClosedLoop/build/*.py`, and this packet's pin lines: only `packet.py --repin <instrument>`, the owner's, moves a pin.

### input:spec

memory/builds/dScopedBuild/prompts/2026-11-01-prompt-TOOL-dScopedBuild-42-promoted-fix-brief.md

### task:reuse

per-spec §10; scouts over tools/unattended, tools/workflows, tools/memory-tree, tools/hooks, tools/lib.

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
