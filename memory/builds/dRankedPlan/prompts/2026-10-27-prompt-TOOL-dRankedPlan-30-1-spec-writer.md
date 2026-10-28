**Serves:** journal TOOL-dRankedPlan-30

# gov-spec-writer handoff — TOOL-dRankedPlan-30

<!-- gov:handoff role=gov-spec-writer build=dRankedPlan unit=TOOL-dRankedPlan-30 path=memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-30-1-spec-writer.md role-sha=06b14b1ac42a task-sha=5d2eea8dfd86 -->

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

This handoff is for build `dRankedPlan`, unit `TOOL-dRankedPlan-30`.
Not supplied, optional: `card:route`.

### brief:goal

Every unit of dRankedPlan specced and built, so that each of the 16 clauses of its row in v2's `[chain]` (Items) is carried by a spec pinned to its hash and built, each of its 18 owned nodes (Owned nodes) is built, and each of its 10 owned gaps (Gaps) is closed.

### brief:items

Each clause of the row, in its order: its id at its baseline hash, its hash now in the as-built view with the record behind any change, its tokens as `carries.py`'s token arm reads them, and its text.

1. `cl-dClosedLoop-0369@9f2afd12` · now `9f2afd12`, as at the baseline · tokens: `parents:` — priority beside `parents:` and the generated plan view
2. `cl-dClosedLoop-0370@23b0ac8f` · now `23b0ac8f`, as at the baseline · tokens: `owner-orders`, `plan.authority`, `planner-drafts-owner-ratifies`, `planner-within-themes` — the planner and triager role and Plan workflow, the plan's order set as `plan.authority` says: drafted by the planner and binding once the owner ratifies it, the planner adding but never reordering between ratifications, under `planner-drafts-owner-ratifies`, ordered by the planner within the themes and priorities the owner sets under `planner-within-themes`, and written by the owner, agents only proposing, under `owner-orders`, each value seen on its planted case (R2.4)
3. `cl-dClosedLoop-0371@3ec4f25f` · now `3ec4f25f`, as at the baseline · tokens: `archive-legacy`, `owner-batches`, `plan.triage`, `plan.triage-rule`, `rules` — triage as `plan.triage` says: by `plan.triage-rule`'s declared rules, the planner judging what no rule decides, under `rules`, drafted and held for the owner to ratify in batches at an owner breakpoint under `owner-batches`, and the legacy backlog archived with only new asks triaged under `archive-legacy`, each value seen on its planted case
4. `cl-dClosedLoop-0372@5c733981` · now `5c733981`, as at the baseline · tokens: none, so the token arm cannot see this clause — dormancy disposal
5. `cl-dClosedLoop-0373@70fb5631` · now `f1eb8c00` by deviation `2026-10-26-build-TOOL-dRankedPlan-5-deviation-51` · tokens: none, so the token arm cannot see this clause — the mapping's population is every build the plan view lists at the build run's base, less the 22 chain builds of v2's `[chain]` table, derived by TOOL-dRankedPlan-5 §8 F1's probe; at `0689e7fa1` that is v1's 24 rows plus `aScoutedSeam` and `dClosedLoop`, each of the two recorded `kept` since v1 names no chain build for it.
6. `cl-dClosedLoop-0374@c6143eda` · now `c6143eda`, as at the baseline · tokens: `review.pin` — Plan Review, run until dCalibratedLens's Plan lenses land with the lenses of the preset `review.pin` passes from dFairHearing's catalogue, seen on a tree that holds no Plan lens
7. `cl-dClosedLoop-0375@33084fbd` · now `33084fbd`, as at the baseline · tokens: `advisory`, `binding`, `offer-next`, `plan.kickoff` — kickoff using the plan as `plan.kickoff` says: offering the plan's next item under `offer-next`, holding the session to the plan's next item under `binding`, and showing the plan as advice beside the session's own choice under `advisory`, each value seen on its planted case, and attended briefs gated
8. `cl-dClosedLoop-0376@f1c33063` · now `f1c33063`, as at the baseline · tokens: `kickoff.runs` — the full kickoff only where `kickoff.runs` says
9. `cl-dClosedLoop-0377@fd363a7f` · now `a78b3ac9` by deviation `2026-10-26-build-TOOL-dRankedPlan-9-deviation-91` · tokens: `entry.intake`, `plan.ratification` — the session's intake log, which `entry.intake`'s prompt-submit hook writes once dWellOiledMachine lands it and which until then is dPlacedRequest's request record and its `.typed` line, its owner-origin intake alone read as the request's ratification by `plan.ratification`, every witness read from the stand-in marked `log stand-in` in place of a `[[stand-in]]` row
10. `cl-dClosedLoop-0378@ed811c10` · now `ed811c10`, as at the baseline · tokens: `plan.exit`, `plan.ratification: request` — until the intake kind lands and the harness's adapter declares the prompt-submit event in its capability table, `plan.exit` under `plan.ratification: request` falls back to dDeclaredLoop's owner gate, held for the owner's disposition, its witness recorded as "intake not installed", the fallback kept for every harness whose adapter does not declare the event whichever of this build and dWellOiledMachine lands first, seen on a planted Codex-shaped adapter that reaches Plan's exit through it (RC-9, AF-1, DA-H1)
11. `cl-dClosedLoop-0379@f1807fe1` · now `f1807fe1`, as at the baseline · tokens: `id#tag` — each role item's memory read set sized at Plan, as `id#tag` keys
12. `cl-dClosedLoop-0380@1e2f59a7` · now `1e2f59a7`, as at the baseline · tokens: `plan.record` — `plan.record` declaring the probes owed before Design (night pass, point 2)
13. `cl-dClosedLoop-0381@634c7b47` · now `634c7b47`, as at the baseline · tokens: `code` — the plan record's intent fields: the affected systems derived from the `code` record and checked, and the open questions as fork tags (night pass, point 6)
14. `cl-dClosedLoop-0382@182ba9ba` · now `182ba9ba`, as at the baseline · tokens: none, so the token arm cannot see this clause — the plan record's scenario field, set from the placement and revisable by the planner at Plan with its reason, a later re-pick only at a step boundary through a plan revision (the night pass two, point 1, the owner's NT-2)
15. `cl-dClosedLoop-0497@2b8de50e` · now `2b8de50e`, as at the baseline · tokens: none, so the token arm cannot see this clause — the plan revision record: a fork the goal cannot survive moving the build from designing back to planning, the planner recording what the revision changes in the ratified plan and why, ratified as the plan is, and Design re-entered on the ratified revision, seen on a planted fork the goal cannot survive whose revision Design receives
16. `cl-dClosedLoop-0498@e9d43f26` · now `e9d43f26`, as at the baseline · tokens: none, so the token arm cannot see this clause — the artifact levels declared as the owner confirmed them in the flow round: the card at the session's level above the plan, one plan record per build holding its concrete details, and the brief derived from the plan, the spec and the stage's facts and never authored, each fact with one home that a lower level renders and never restates, seen red on a planted brief that types a plan field

### brief:acceptance

- At the Design exit, `carries.py --build dRankedPlan --exit` exits 0 over the build's specs: each clause in Items carried whole, or in parts 1/n to n/n, at its hash; each owned node named by a spec; each clause's tokens in its carriers.
- Each clause's own seen-red cases, stated in its text, observed as it states them.
- Every departure from a clause, or from a spec after its first pass, is a deviation record that `deviations.py` joins, and the build's departures report lists it (README rule 4).

### brief:gates

- `packet.py --check dRankedPlan` green before the first pass. A red on a moved instrument blob is a stop, never re-rendered away (README rule 2).
- `carries.py --build dRankedPlan --exit` at the Design exit while it is in service (the execution plan's `[phase-1]` retirement table).
- The close sequence of README rule 4, then the bar the driver owes at `--close`.

### brief:non-goals

- v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: frozen at the baseline, so a change to a clause is a deviation record approved by its risk.
- The 493 clauses of the other 21 chain builds' rows: carrying one needs a `**Moved:** <clause id> to dRankedPlan by <decision>` line.
- Any path outside `memory/builds/dRankedPlan/`, but the product paths a build run's units record with `--dispatch --writes`, an ask row in another build's `BACKLOG.md`, and the shared renders a landing re-renders (README rule 7).
- Another build's packet, the instruments under `memory/builds/dClosedLoop/build/*.py`, and this packet's pin lines: only `packet.py --repin <instrument>`, the owner's, moves a pin.
- The surfaces of dWellOiledMachine, dCalibratedLens, which this build's clauses use as stand-ins only (Later builds named).

### input:spec

memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-30-promoted-fix-brief.md

### task:reuse

the parents' specs (dDeclaredLoop, dTotalRecall, dBoundRoles) cited by id and section; seams from the two reuse-scout records.

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
