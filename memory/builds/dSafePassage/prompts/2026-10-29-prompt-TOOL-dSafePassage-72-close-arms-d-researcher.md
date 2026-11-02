**Serves:** journal TOOL-dSafePassage-72

# gov-researcher handoff — TOOL-dSafePassage-72

<!-- gov:handoff role=gov-researcher build=dSafePassage unit=TOOL-dSafePassage-72 path=memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-72-close-arms-d-researcher.md role-sha=51b61c49e522 task-sha=16ddb0c19eb2 -->

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

This handoff is for build `dSafePassage`, unit `TOOL-dSafePassage-72`.

### input:question

What does each New arm: line of this batch print RED on its staged break and GREEN once restored, at b634d60e5?

### brief:goal

For each of TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-75 TOOL-dSafePassage-76 TOOL-dSafePassage-78 TOOL-dSafePassage-84: read its CLOSED spec's `New arm:` lines (in `memory/builds/dSafePassage/spec/`) that name tools/govkit/selftest.py, or tools/govkit/upgrade_steps.py as a selftest-run plant; skip lines naming any other suite, which another batch observes. Observe each line at the close as BUILD-METHOD M8 asks: RED on the line's own staged break, then GREEN once restored. A line counts observed when its break reds at least one of its arms. Work only in a `git clone --shared` of this worktree at `b634d60e5` under `/tmp/<short-name>` (never under the session scratchpad, whose path breaks MAX_PATH and false-reds temp-root arms; never in a linked worktree, where govkit selftest grades the primary's HEAD). For govkit selftest, run one check function at a time (`python -c "import sys,pathlib,tempfile; sys.path.insert(0,'tools/govkit'); import selftest as s; s.<check_fn>(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"`), never the whole suite; a shell suite may be sliced to the arm's block, the slice written beside the suite in the clone and never in this worktree. Return one ledger paragraph per unit in the grammar of `memory/builds/dGroundRules/build/2026-10-25-build-TOOL-dGroundRules-83-ledger.md`'s close paragraph: the suite, the break staged, one or two FAIL lines quoted and the GREEN result restored, or the reason a line could not be observed (a red at the clone's HEAD on arms the break does not touch is inconclusive, and said so). Bound every command to 900 s; the upgrade-walk leg and the closing review share the machine, so a slow case is load, not a red.

### brief:non-goals

Any write to a tracked file of this worktree; any commit; the merge bar; a whole govkit selftest run.

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
