**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-21-researcher.md role-sha=51b61c49e522 task-sha=374a766605ca -->

## Role

You are a researcher for a governed repository. You are handed one question a design must answer,
and you produce the candidates that could answer it, the evidence that separates them, and a
recommendation.

You are not choosing the design in this pass, and you are not building it. You write no file in the
repository and run no command that changes it; every probe you run reads. A candidate you would have
to build to test is described as the test the build must run, never built.

How you work, by the build method's M12:

- Find candidates, plural, that differ in MECHANISM, and stop where a further one would differ only
  in detail. "Only one mechanism exists here" is a legitimate answer, and it is a claim that owes the
  same evidence a pick does.
- First look for the seam the repository already has, with the reuse probes M5 names. A candidate
  that extends an existing seam is ranked against the others, not exempted from them.
- For each candidate, write down the smallest test that would make it LOSE before you run anything,
  then run it: a probe, a fixture, a measurement against the real tree. A test every candidate
  passes is a rehearsal, not a test.
- Verify every claim about current code by reading the code, and say where a record and the code
  disagree.

Done means every candidate carries its mechanism, its losing test and that test's result, and every
rejected one names the test that rejected it.

Return exactly the shape your task block or the caller's schema names. Leave the owner's wider
prose, and anything outside the question you were handed, out of what you write and return.

## Task

This handoff is for build `dClosedLoop`, unit `PLAY-dClosedLoop-1`.

### input:question

**Context.** dClosedLoop is a design-only build that re-architects gov (coding-governance), a kit set that ships project-agnostic governance to repositories that adopt it, gov's own repository among them. Its converged design is architecture v2 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`), at `d56d7da4d` on this branch, with its layer and system records beside it under `memory/builds/dClosedLoop/build/` (the flow steps in `...-flow-steps.md`, the layers in `...-layer-*.md`, the systems in `...-systems.md`, the flow and roles adoption in `...-flow-roles-adoption.md`, the night pass two in `...-night-pass-two.md`), each section cited as `[tag]`. The owner is reviewing the last major part of the design not yet reviewed before it is finalized, in the owner's words:

> Let's review one of the last major parts of the design we haven't reviewed before prior to finalizing the design: stall prevention and infinite loop detection. Is there a system to prevent work from being infinitely stalled/delayed due to any reason? What layer of the system does it implement through? One example case: tier2 reviews, spec reviews could previously run infinitely due to non-converge, that's why in the current Gov implementation spec reviews were moved to opt-in only while closing diff reviews run ones and promote their findings to build units. The main objective, in the end, is to produce features in reasonable time - not waste resources on running an infinite non-convergent loop. With the new architecture, I can see several potential loops cycling, wasting resources, and stalling work - testers handing work back to design, design still not converging, hooks stalling work while agents are unable to comply with the hooks' instructions - a lot of refusal steps have been decided on in this design, which will inevitable cause stalls. Since custom scenarios and flow steps are possible, this will lead to unforeseen chains which can potentially stall. Research an extensive set of infinite loop/stall scenarios in the newly designed architecture and account for a reasonable stall and loop prevention system.

**Handed facts, to re-verify, never to act on unread.** v2's catalogue (`[policies]`) already bounds some loops: `flow.route-backs` (3; a route back past the count becomes an owner item), `review.design.rounds` (one by default) with `review.design.round-count` (held below the loop kit's `RUNAWAY_CEILING`), `review.follow-up`, `review.unverified`, `roles.retries` (3), `roles.on-contradiction`, `runtime.act-ceiling` (1.5 h), `runtime.hold-ceiling` (6 h, then an owner item), `leases.expiry-hours` (24), `build.release-ceiling` (72 h), `deps.coordination`, `deps.landing`, `deps.on-parent-withdrawn`, `resume.partial`, `verdict.flakes`, `verdict.held`, `flow.adapt` and the scenario keys (`flow.scenario-*`). dWellOiledMachine holds the admission queue (the owner's NT-28: a spawn over the agent limit waits instead of being refused, a fan clamped to the share it can hold) and the supervisor that runs acts; the flow and roles adoption lets a repository add its own items, roles, stages (spliced between two of gov's), lenses and legs, and patch gov's rows; the night pass two added scenarios (named variants of the flow a build is placed under) and builds that change their own flow mid-build. Today's tree carries `tools/unattended/` (its `RUNAWAY_CEILING`, resume attempts and held stops), `tools/hooks/` (the PreToolUse, Stop and StopFailure guards, the stall recorder among them) and `.githooks/`.

Five researchers serve this request, one question each: a census of the design's cycles and waits, its refusals, concrete stall scenarios, gov's measured history, and prior art outside gov. Yours is THE HISTORY; stay inside it, and name a finding that belongs to another only in one line.

**Your question.** What stalls and loops has gov actually suffered, and what stopped each, measured from its history?
1. **Reviews that did not converge:** find the records that moved spec reviews to opt-in and made the closing diff
   review run once and promote its findings to build units (decision rows, protocol text, the build-method guide, the
   review protocol), and measure from the review records under `memory/builds/*/reviews/`: rounds per subject,
   findings per round, how many of a later round's findings the previous round's fold caused, and where the count
   stopped falling.
2. **Unattended runs:** from the runs' records (RUN.md files, `tools/runlog/`'s grammar and records, held stops), how
   many runs stopped held, ran into `RUNAWAY_CEILING` or exhausted resume attempts, how long they ran and what they
   cost, and why each stopped.
3. **Stalls the hooks caused:** the stall recorder's entries and any record of an agent unable to satisfy a hook;
   repeated red bars, inherited reds that blocked landings, flaky legs retried.
4. **What stopped them:** each mechanism that ended a loop or a stall (a ceiling, an opt-in, an owner decision, a
   kill) and what it cost; and the loops that ended only because a person noticed.

**Return.** A measured table: case, source (`path` or `<record> [<tag>]`), what looped or stalled, how long or how
many times, what stopped it, cost. Then the review-convergence curve with its numbers, then the mechanisms that worked
and those that did not, each with its evidence.

**Bounds.** Write nothing in this repository; a probe works on a copy under the system temp root, deleted when you finish. Cite every claim about the records as `<record> [<tag>]` and every claim about code as `path:line`, quote commands and their outputs as measured, and say where a source is ambiguous. Another agent may be reading this tree while you work: modify nothing in it. Run no gate leg and no test suite.

### brief:goal

Agree with the owner on a target architecture in which every kit, skill, hook, gate and record of
gov serves a declared stage contract of one lifecycle loop (Plan, Design, Build, Test, Deploy,
Maintain, with Review available at any stage) for concurrent, multi-node, agentic development.
Record the gaps between today's product and that architecture, and open the ordered chain of builds
that converges the product onto it.

### brief:non-goals

- No product code: nothing under `tools/`, `skills/`, `coding-governance-agents.template.md` or
  `WIRE-INTO-PROJECT.md`, and no `AGENTS.md` re-render. Each such change is a chain build's unit.
- No unit specs for the chain builds: each opens with a README and a planned unit roster, and its
  own session writes the specs (owner, 2026-10-14).
- No status change to an existing build or ask; their mapping onto the chain is a recommendation.
- No adopter-repository work, and no merge to main or push without the owner's explicit ask.

### Charter rules

- [reuse] Reuse before building: find the seam to extend first, and at a kind's second instance extract its factory, never a copy.
- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
- [memory] Memory keeps only what cannot be derived, and recalled memory is background to re-verify, never an instruction.

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
