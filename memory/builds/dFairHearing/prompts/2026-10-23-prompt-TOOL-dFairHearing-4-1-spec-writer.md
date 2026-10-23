**Serves:** journal TOOL-dFairHearing-4

# gov-spec-writer handoff — TOOL-dFairHearing-4

<!-- gov:handoff role=gov-spec-writer build=dFairHearing unit=TOOL-dFairHearing-4 path=memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-4-1-spec-writer.md role-sha=06b14b1ac42a task-sha=9de8dd98d5fd -->

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

This handoff is for build `dFairHearing`, unit `TOOL-dFairHearing-4`.
Not supplied, optional: `card:route`.

### brief:goal

Every unit of dFairHearing specced and built, so that each of the 18 clauses of its row in v2's `[chain]` (Items) is carried by a spec pinned to its hash and built, each of its 10 owned nodes (Owned nodes) is built, and each of its 13 owned gaps (Gaps) is closed.

### brief:items

Each clause of the row, in its order: its id at its baseline hash, its hash now in the as-built view with the record behind any change, its tokens as `carries.py`'s token arm reads them, and its text.

1. `cl-dClosedLoop-0068@b4e6c04e` · now `d09495d0` by deviation `2026-10-23-build-TOOL-dFairHearing-1-deviation-11` · tokens: `review_replay.py` — the owed replays first: the design-audit preset run blind at blob 767187aa, from a bundle of the history to 6cfd21619 cloned outside the repository, scored by `review_replay.py` against a known-set file of 65 rows, the 59 defects the two baseline rounds confirmed with `escaped` `no` and the 6 escapes with `escaped` `yes`, each with its address and grade, counting each matched defect once, at 45 of the 59 reviewed rows, 4 of the 6 escaped rows and 7 of the 8 high rows in each run, a miss keeping the unit-spec preset for design records, the verify stage with batches by address, the synthesis with twins shown, and aRoutedQuill #23's fix re-judged by class
2. `cl-dClosedLoop-0069@a762d009` · now `a762d009`, as at the baseline · tokens: `preset` — the design-audit preset of the spec-audit kind for design and architecture records, chosen by a `preset` argument that Design's breakpoint passes when every pinned spec revision is one (RV-1) (coherence, grounding flagging untested assumptions, reuse held to precedent, failure-envelope extended to trust boundaries, and alternatives-and-cost in place of blast-radius)
3. `cl-dClosedLoop-0070@00ce4e3c` · now `00ce4e3c`, as at the baseline · tokens: `optIn`, `preset`, `review.opt-in`, `review.pin`, `review.trigger` — opt-in lenses (security, alternatives, cost, portability, adopter migration, topology), each swapped for a named default lens of its preset in the five-element literal, passed as per-run `optIn` and `preset` arguments that `review.pin` maps from `review.opt-in` and the pinned revisions' record kind, checked once at the argument boundary, and each shipping on its losing test, `review.pin` run directly with its pin arguments, a stand-in until dDeclaredLoop's `review.trigger` lands (the whole-design audit's C2-F6)
4. `cl-dClosedLoop-0071@8d3a19dc` · now `8d3a19dc`, as at the baseline · tokens: none, so the token arm cannot see this clause — skeptic batches sorted by cited address
5. `cl-dClosedLoop-0072@4afd6a04` · now `4afd6a04`, as at the baseline · tokens: none, so the token arm cannot see this clause — duplicates counted as merged confirmations, with the orphan check on both kinds
6. `cl-dClosedLoop-0073@242e109b` · now `242e109b`, as at the baseline · tokens: none, so the token arm cannot see this clause — items carrying a grade per id, ranked by the highest
7. `cl-dClosedLoop-0074@51869353` · now `51869353`, as at the baseline · tokens: none, so the token arm cannot see this clause — refuted claims and same-address twins handed to the synthesizer to flag
8. `cl-dClosedLoop-0075@8c43970c` · now `8c43970c`, as at the baseline · tokens: `class:`, `gate:`, `new:`, `none`, `review.dispose`, `review.report`, `review.unclassed` — fix verdicts judged by class, and every confirmed finding given one disposition from `review.report`'s grammar (`class:`, `new:`, `gate:`, or `none` under `review.unclassed`), against the leg manifest and the class slugs the harness hands over, the report's dispositions written to the review record, a stand-in until dDeclaredLoop's `review.dispose` lands and routes them (the whole-design audit's C2-F6)
9. `cl-dClosedLoop-0076@8bf57ee9` · now `8bf57ee9`, as at the baseline · tokens: none, so the token arm cannot see this clause — portability, topology and adopter migration as bug-class checklist entries anchored to their paths, never universal, and lens notes passed by the callers, derived per preset after a swap
10. `cl-dClosedLoop-0077@58d0099e` · now `58d0099e`, as at the baseline · tokens: `tools/roles/agents/gov-synthesizer.agent.md`, `tools/workflows/REVIEW-PROTOCOL.template.md`, `tools/workflows/tier2-review.template.js` — the review records brought back in line with the code at their sources (`tools/workflows/REVIEW-PROTOCOL.template.md`'s lens list, lens count and skeptic default, agent-cap's lens comment, `tools/workflows/tier2-review.template.js`, and `tools/roles/agents/gov-synthesizer.agent.md`'s input line), each live copy re-rendered
11. `cl-dClosedLoop-0078@ed5e83ae` · now `ed5e83ae`, as at the baseline · tokens: `review.twin` — the panel's internals, every agent the harness spawns typed and declared in a stage, seen red on a planted untyped spawn (gap-review-13, the whole-design audit's C2-F16), and the twin merge a review step runs when the owner's `review.twin` opts it in (RS-1)
12. `cl-dClosedLoop-0079@d8e61ab6` · now `d8e61ab6`, as at the baseline · tokens: `b0fe68f30`, `review_replay.py` — the scorer factory: one deterministic scorer that re-derives every figure from committed raw outputs, pairs the cases every variant answered and refuses a partial population, extracted from `review_replay.py` with aScoutedSeam's grader as its second instance, its grader, cases, results and judge taken by blob from commit `b0fe68f30`, since merged into the default branch with the later results the night pass two cites, never waited on, the second instance proven over the committed results, which need no corpus, a factory test refusing when only `review_replay.py`'s instance is present, and a conformance arm red on a second scorer, code outside the factory that pairs variants with cases (night pass, point 2)
13. `cl-dClosedLoop-0080@8c9e5de7` · now `8c9e5de7`, as at the baseline · tokens: none, so the token arm cannot see this clause — the lens catalogue as data in the review kit, the harness's five-slot literal filled from it, and the merge bar's harness check counting slots, never names, where agent-cap counted them until the night pass two's point 7, seen red on a planted sixth slot and green on a catalogue row added as data (FA-1)
14. `cl-dClosedLoop-0081@3ad56b8f` · now `3ad56b8f`, as at the baseline · tokens: none, so the token arm cannot see this clause — the experiment shape's method, from aScoutedSeam's measurements: cases with objective evidence, a held-out set frozen before any tuning and never read to change a prompt, one variable per arm, parsed replies counted before any score is read, one blind judge per case with labels rotated, and the arms' union read as one system, its held-out cases joining the benchmark's replay (the night pass two, point 2)
15. `cl-dClosedLoop-0082@8ac81dad` · now `8ac81dad`, as at the baseline · tokens: none, so the token arm cannot see this clause — the review's bug-class checklist selected by the pinned range and ordered by anchors, the cut of fully gated classes left to dLinkedLibrary's derived status (the night pass two's review), and a replay with the checklist and without it over the known-defect corpus deciding whether review keeps that selection or takes every ungated class, the lookup's charter line retired as the harness hands the checklist itself (the night pass two, point 6, the owner's NT-25)
16. `cl-dClosedLoop-0083@bd47ee4e` · now `bd47ee4e`, as at the baseline · tokens: `check-review-join.sh` — agent-cap's review rules moved to the review kit: the verifier total and the loop markers to the merge bar's harness checks, the ref-keyed join ban to `check-review-join.sh` alone, and the spec-audit opt-in to a review-kit pack on Workflow calls, each seen red on its planted case before agent-cap stops carrying it (the night pass two, point 7, the owner's NT-27)
17. `cl-dClosedLoop-0084@5c5896a3` · now `b793fdd5` by deviation `2026-10-23-build-TOOL-dFairHearing-17-deviation-171` · tokens: none, so the token arm cannot see this clause — each round's state in the review report, CONVERGED, NON-CONVERGENT, BOUNDED or CEILING, or CONVERGING on a round with blockers or highs standing that is the first or falls below the round before, while under its caller's limit or when its caller passes none, computed against the round before from its blocker and high count at the round limit its caller passes, seen red on a planted flat sequence and an oscillating one, and on a strictly falling sequence that reaches its caller's limit, read BOUNDED, and one run past it, read CEILING (P39, the owner's SL-3, the parked debt's review)
18. `cl-dClosedLoop-0085@796d40aa` · now `796d40aa`, as at the baseline · tokens: `[tag]`, `review.design-audit.runs`, `review.design-audit.seed` — the whole-design walk as a preset of the design audit: walkers sliced by scenario and by step under `review.design-audit.runs`, each returning its findings and a walk table of every item and scenario with its actor, needs, witness, route and verdict, a synthesis red on an empty cell, skeptics refuting a sample of clean cells, the replay scorer reading `[tag]` addresses, and recall graded on seeded past escapes as `review.design-audit.seed` says, seen red on a planted gap the walk misses and on an empty cell (the owner's FQ-1)

### brief:acceptance

- At the Design exit, `carries.py --build dFairHearing --exit` exits 0 over the build's specs: each clause in Items carried whole, or in parts 1/n to n/n, at its hash; each owned node named by a spec; each clause's tokens in its carriers.
- Each clause's own seen-red cases, stated in its text, observed as it states them.
- Every departure from a clause, or from a spec after its first pass, is a deviation record that `deviations.py` joins, and the build's departures report lists it (README rule 4).

### brief:gates

- `packet.py --check dFairHearing` green before the first pass. A red on a moved instrument blob is a stop, never re-rendered away (README rule 2).
- `carries.py --build dFairHearing --exit` at the Design exit while it is in service (the execution plan's `[phase-1]` retirement table).
- The close sequence of README rule 4, then the bar the driver owes at `--close`.

### brief:non-goals

- v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: frozen at the baseline, so a change to a clause is a deviation record approved by its risk.
- The 491 clauses of the other 21 chain builds' rows: carrying one needs a `**Moved:** <clause id> to dFairHearing by <decision>` line.
- Any path outside `memory/builds/dFairHearing/`, but the product paths a build run's units record with `--dispatch --writes`, an ask row in another build's `BACKLOG.md`, and the shared renders a landing re-renders (README rule 7).
- Another build's packet, the instruments under `memory/builds/dClosedLoop/build/*.py`, and this packet's pin lines: only `packet.py --repin <instrument>`, the owner's, moves a pin.
- The surfaces of dDeclaredLoop, which this build's clauses use as stand-ins only (Later builds named).

### input:spec

memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-4-edge-fix-brief.md

### task:reuse

the dTrueNorth spec-brief shape (memory/builds/dTrueNorth/prompts/2026-10-21-prompt-TOOL-dTrueNorth-1-spec-brief.md); tools/workflows/unattended-build.js and tier2-review.js for the passes; each spec's §10 records its own seam.

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
