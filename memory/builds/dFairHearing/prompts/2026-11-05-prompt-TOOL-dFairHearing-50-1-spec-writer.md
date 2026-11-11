**Serves:** journal TOOL-dFairHearing-50

# gov-spec-writer handoff — TOOL-dFairHearing-50

<!-- gov:handoff role=gov-spec-writer build=dFairHearing unit=TOOL-dFairHearing-50 path=memory/builds/dFairHearing/prompts/2026-11-05-prompt-TOOL-dFairHearing-50-1-spec-writer.md role-sha=dcd8416ea3d2 task-sha=902617dd893d -->

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
after every writer returns. At a spec audit's disposal, a correction to an unbuilt sibling's spec
rewrites that sibling's text, with a rev bump and a revision-log line naming the repair unit and
the review record by its file stem, and a CLOSED sibling stays frozen.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names, every unit named by its unit id as
the roster spells it. Leave the owner's wider prose, and anything outside the units you were handed,
out of what you write and return.

## Task

This handoff is for build `dFairHearing`, unit `TOOL-dFairHearing-50`.
Not supplied, optional: `input:spec`.

### brief:goal

Write the spec for `TOOL-dFairHearing-50` at `memory/builds/dFairHearing/spec/2026-11-05-spec-TOOL-dFairHearing-50.md`. It repairs every red below, so each suite named exits 0. Commit nothing; the main loop commits.

### brief:items

Every line here is the main loop's reading of a suite log. Re-ground each one on today's tree and say so where it is wrong. A log line is quoted as the suite printed it.

1. `tools/workflows/tier2-review.test.sh`, `the args header documents all 31 fields read off a` — missing `length`. Its field regex at :451 takes `twinFigures.a.length` at `tools/workflows/tier2-review.js:3235` for a read of the args alias, because `\b` holds after a dot. Fix the arm's regex.
2. `tools/workflows/tier2-review.test.sh`, `FH23 AC27 the real stdout cut inside its item list` — the fixture's real stdout has one item, so cutting it leaves no `- ` line, and the harness reports `no bug class selected` where its head lines state one class. The arm has never run before. The defect is the harness's: the `cut` computation at the checklist acquisition (`tools/workflows/tier2-review.template.js` and its render) runs only when a `- ` line exists. A return whose head line states more than zero classes and holds no item is a cut, so it must be a `checklistError`. A genuine zero-selection return stays `no bug class selected`.
3. `tools/workflows/check-review-join.test.sh:386`, `harness: the verifier count is bounded`, greps `Math.ceil(allFindings.length / MAX_VERIFIERS)`; the harness spells `verifyOrder.length`. Fix the needle.
4. `tools/workflows/check-review-join.test.sh`, `discovery: an empty population is still not a pass` and `the empty refusal does not name both directories`. Unit 16 dropped `agent-cap.js` from `SELF_EXCLUDE` on purpose, so the `$E` and `$H4` fixtures' hook copy under the kit prefix makes the population non-empty. Move each fixture's hook copy to the `.claude/hooks/` fallback the gate already reads, outside the population. Keep the exclusion as it is.
5. `tools/workflows/check-verifier-fanout.sh`, six arms (`AC3`, `AC5`, `FH27 AC1`, `AC25` twice, `AC26`): the `--slots` call hands node `"$f:$_l"`, and MSYS does not convert an absolute path with a suffix, so node reads ENOENT and the gate exits 2. Fix the gate, not the arms: give node a spelling it can open, with no new spawn on a relative path, and fall back cleanly where `cygpath` is absent. Say which spelling a Linux run sees.
6. `tools/check-playbook-parity.test.sh`, `S1 an empty kit derivation reds before reporting coverage`: unit 27 planted a third kit in the fixture and the arm's staging at :492 still removes two. Add the third.
7. `tools/workflows/unattended-build.test.sh`, `MT zero confirmed and 48 unverified` (:1098) and `MT20 the callee ran over the measured shape` (:1120): the needles predate unit 5's `merged` key. Read the real output first, then fix the needles.
8. `tools/workflows/unattended-build.test.sh`, `DGR74 LIVENESS`, `DGR74 ...after a stderr notice` and `DGR83 a hook that denies printing nothing`: unit 16 moved `WRITER_MARK` from the hook to `tools/workflows/check-verifier-fanout.js`, so the `sed` staging at :2301 and its liveness grep stage nothing. Read `tools/workflows/check-protocol-parity.test.sh:706` to `:733` and decide whether the writer-split question still reaches a stub hook. If it does not, the arms, the notice's wording, or the gate is wrong: say which, from the code.
9. `tools/workflows/unattended-build.test.sh`, `RA6-1 ...and its check-verifier-fanout.sh once` (got 2) and `RA6-1 ...and the tool root plus gov's home for them nowhere` (got 6). This one may be a real gap: a renamed kit's rendered review protocol still spells the old kit home. Find which lines of `tools/workflows/REVIEW-PROTOCOL.template.md` the render's kit-cite pass misses, and fix the render or the template. The first count may be a legitimate new cite: then the arm's number moves, and the spec says why.
10. `tools/check-spec-tokens.test.sh`, `parity: a manifest suite invocation BAR does not match`: `measure-legs selftest` carries a 500 s ceiling and is not declared exempt. This red is inherited from base `8bec4cefd`. Declare it exempt the way its siblings are, in the same list.
11. Unit 48's two leftovers. Its builder could not fix the two docstrings in `tools/check-spec-tokens.py` (about :936 and :995) that call `read_carries_specs` the WONTDO filter's one home, now false, nor a header the generator's grammar refuses being graded here but set apart by the carries join. State the true filter homes. Then check whether `tools/workflows/README.md`, `memory/guides/UNATTENDED-VERBS.md`, `memory/guides/UNATTENDED-STOPS.md` or `memory/guides/REVIEW-PROTOCOL.md` list the harness's stop exits; if one does, `walk-red` joins that list.

12. Clear the traps this close has already hit:
    - Header: Tier-1 unless item 2, 5, 8 or 9 turns out to change behaviour past a mechanical fix, then Tier-2 with reasons. `order 33`, no ask clause, status `OPEN`.
    - List every path: renders beside templates, `memory/LIVE.md`, the build README, `memory/map/generated/symbols.json` if a definition moves, and any kit version marker a move owes.
    - `--dispatch` refuses a generated file declared beside its generator. Staging `tools/gate-legs.json` needs the kickoff manifest's `last-audit` re-stamp and delta line in the same commit.
    - A test floor counted by hand is not a run: say the floors move, and leave them to the close.
    - Acceptance sweep: split every backticked span on whitespace. Each word holding a `/` must be a tracked path exactly, or lead with `$`, `<`, a quote or `~`. Check the `BAR` pattern at `tools/check-spec-tokens.py:419` to `:424`, and put no `python -c` probe in the Acceptance section.
    - Every change-log line names a section, a scope id or an acceptance id. New text cites no check, section or method rule by a bare number.
    - `tools/gate-legs.json` legs for every file touched go on the Gates leg line, or the guards join reds.

The main loop may add items from a bar running now. Leave the spec open to one revision.

### brief:acceptance

A spec conforming to `memory/TEMPLATE-SPEC.md`, one criterion per item. Each criterion names the suite and the arm label, so the close's run is what observes it. A pass runs no suite, so each criterion also names a probe the builder can run: a grep, a fixture or a direct call of the changed code.

### brief:gates

None you run.

### brief:non-goals

No code, and no other spec. No new gate beyond what an item needs. Not touching `tools/run-gates/run-gates.sh`, since a run that edits the grader cannot land itself.

### task:reuse

each unit's spec §10 names its seam; the review harness tools/workflows/tier2-review.template.js and tools/hooks/agent-cap.js are the main seams.

### card:route

- build: dFairHearing
- unit: TOOL-dFairHearing-48 · spec memory/builds/dFairHearing/spec/2026-11-05-spec-TOOL-dFairHearing-48.md
- brief: memory/builds/dFairHearing/prompts/2026-11-05-prompt-TOOL-dFairHearing-48-build-brief.md

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
