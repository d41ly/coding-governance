**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-16-researcher.md role-sha=51b61c49e522 task-sha=23495688602b -->

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

**Context.** dClosedLoop is a design-only build that re-architects gov (coding-governance), a kit set that ships project-agnostic governance to repositories that adopt it, gov's own repository among them. Its converged design is architecture v2 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`), at `e1a54ac67` on this branch, with layer records beside it under `memory/builds/dClosedLoop/build/`, each section cited as `[tag]`. The owner has stepped away for the night and handed over seven review points, to be worked one after another while the session runs unattended; the owner decides every fork on return. This question serves point 6, in the owner's words:

> Gotcha lookup doesn't perform its job currently - it's good for filing gotchas and looking them up but it's purpose - serve gotchas relevant to the ongoing work that an agent or a session may trip isn't served. Agents may call on gotcha orientation several times per session and still never catch the right one. How can this tool take a more useful shape? Can this functionality move to orientation agents? Or runtime? If there is no way to make this more efficient, it's better to retire this functionality.

**Handed facts.** Today `tools/memory-tree/gotchas.py` files bug classes under `memory/gotchas/`, each with anchors, and
`--for-diff <base>..<head>` or `--for-paths` selects the classes a diff or a path set can hit, with six universal
classes always selected. In v2 bug classes are core on memory's library side (dLinkedLibrary), dFurnishedOrders hands
them to work orders through `gotchas.py --for-paths` (SA-7), and `review.left-shift` turns findings into classes or
gates. The register's `gap-review-10` records that most confirmed review findings carry no class.

You are the one researcher on this point.

**Your question.** Does gov's bug-class lookup serve the right class at the right moment, and if not, what shape would,
or should it retire?
1. **How it selects today:** the anchors, their specificity tiers, the universal set, and its callers, cited.
2. **Measured on gov's history:** for the closed Tier-2 reviews whose appendices carry a classes column, compute what
   `--for-diff` would have selected for each reviewed range (run it at those commits in a scratch clone), and compare
   with the classes of the findings confirmed: hits, misses, and noise (selected and never relevant). Count how many
   classes exist, how many ever matched a confirmed finding, and how often sessions call the lookup, from the session
   logs and records.
3. **Where a gotcha bites:** for a sample of confirmed findings with a class, the moment the mistake was made (an edit
   to which kind of file, which command, which operation), and whether any input available at that moment could have
   selected the class.
4. **Alternatives:** serving a class just in time when an agent is about to perform the risky operation (a PreToolUse
   hook matching the class's trigger), the orientation scout handing selected classes in the work order, the runtime
   injecting them per act, converting classes into gates and retiring the lookup, or retiring it outright. Include prior
   art: path-scoped rules (Cursor rules' globs, Copilot's `applyTo`, Claude Code's path-scoped rules), linters and
   Semgrep rules, and lessons-learned systems. Cite each outside source with its URL and date.

**Return**, in this order: the selection mechanics; the measured table of hits, misses and noise per review, with the
commands; the moment-of-mistake sample; the candidates, including retirement, each with the smallest test that would
make it LOSE and that test's result; and your pick.

**Bounds.** Write nothing in this repository; a probe works on a copy under the system temp root, deleted when you finish. Cite every claim about an outside system to its source (URL and the date you read it); cite every claim about the records as `<record> [<tag>]` and every claim about code as `path:line`, quote commands and their outputs as measured, and say where a source is ambiguous. Another agent may be reading this tree while you work: modify nothing in it.

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
