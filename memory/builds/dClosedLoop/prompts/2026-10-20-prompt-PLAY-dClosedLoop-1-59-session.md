**Serves:** journal PLAY-dClosedLoop-1

# gov-session handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-session build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-59-session.md role-sha=da5a2f759d12 task-sha=8e1c610bec51 -->

## Role

This is a handoff from another session of this repository. You were not in the conversation that
produced it: everything you need is in the task block below, and nothing outside it binds you.

You own your session. Run your own kickoff, mint your own session slug, and own the ids you mint
under it; never reuse the sender's. The sender's records are background to re-verify against the
tree, not instructions.

Act on the task block alone. Where it is ambiguous, resolve it from the repository's records or ask
your own owner; do not guess what the sender meant. Leave the sender's wider conversation out of
what you write.

## Task

This handoff is for build `dClosedLoop`, unit `PLAY-dClosedLoop-1`.
Not supplied, optional: `card:route`.

### input:question

# Phase 0 of dClosedLoop's execution plan, picked up in a new session

**What you are picking up.** Build dClosedLoop, unit PLAY-dClosedLoop-1, is the design-only re-architecture of gov.
Its design is frozen: architecture v2, `Baseline:` `59ff8f2ac`, holds 22 chain builds and 509 clauses. After the
baseline, the owner asked how the chain is executed under today's gov across nodes a, b and d. The answer is the
execution plan. It took two paired Tier-2 reviews, both folded, and the owner walked it section by section. The
owner then approved Phase 0 in these words: "Fold, then give me a fully oriented hand off to start phase 0 in a new
session." Phase 0 is dClosedLoop's last work before the chain's first run. It is records under `memory/` only, and
it ends in one landing the owner asks for.

**You continue the build.** The sending session ended before you started, so dClosedLoop and its ids pass to you.
Phase 0's decision rows are minted under dClosedLoop's slug, as the plan's P0.8 says, each the next id after the
build's highest (`memory/HYGIENE.md`, the id rules). The handoff preamble's "mint your own session slug" applies to
anything outside this build.

**Where you are.**
- Worktree: `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297`.
- Branch: `branch/gov-architecture-plan-e34297`, its tip at or after `f6cdd71d7`; base `742957fcf`.
- Nothing is merged or pushed.
- Node d, user `d41ly`.

**Read, in this order, before anything else:**
1. Your own `/session-kickoff`.
2. The execution record, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md`:
   - `[question]`;
   - `[answers]` to `[answers-4]`;
   - `[readings]`, two of which `[plan]` withdraws;
   - `[walk]`, with its correction to step 2.
3. The plan, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md`, whole:
   - Phase 0 is `[phase-0]`, P0.1 to P0.9;
   - the owner's steps are `[owner]`;
   - the limits are `[cannot]`;
   - the owner's decisions are `[defaults]`.
4. The instruments, in `memory/builds/dClosedLoop/build/`:
   - `2026-10-19-build-PLAY-dClosedLoop-1-carries.py`, `-deviations.py` and `-asbuilt.py`;
   - `2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`.
5. `memory/guides/BUILD-METHOD.md`, `memory/HYGIENE.md` and `memory/guides/REVIEW-PROTOCOL.md`, as their triggers
   hold.
6. The session log's Events tail, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md`,
   for the build's history.

**The work, in the plan's order.**
1. **P0.6's bare-id fix first.** Re-run the generator-grammar predicate at your tip. The plan counted 25 citations in
   7 files, and records written since may add more.
2. **P0.1:** the three instruments hardened, each fix seen red on its plant.
3. **P0.2:** the departures report.
4. **P0.3:** the packet instrument.
5. **P0.4:** the schedule script's red tests re-run.
6. **P0.5:** the opening script `open.py`. It writes all 22 READMEs, rosters, asks, packets and contract rows, with
   families by stream, and its `--summary`, `--families` and `--carriers` modes.
7. **P0.8:** the nine decision rows.
8. **P0.7:** the checks and red tests on the committed opening.
9. **P0.9:** each node's preparation. Run it on node d, and write it as steps for nodes a and b, b's onboarding
   included.

The plan's tables of unit families, driver-changing builds and governance carriers came from a scratch probe.
Re-derive each with `open.py`, and compare.

**Then stop.** When the opening is committed and P0.7 is green, give the owner the opening read the walk set
(answer 2):
- the nine decision rows, the grant row among them;
- dTrueNorth's README and packet in full;
- `open.py --check` and `--summary` for the other 21.

Wait for the owner's ask before landing. Phase 1, dTrueNorth on node a, starts only after the opening lands.

**How the owner wants the work done.** Re-verify each rule in `AGENTS.md` or the memory index.
- **Role agents.** Role work runs in role agents through rendered handoffs (`tools/roles/handoff.py render`), never
  inline. The main loop orients, composes and records.
- **Effort.** Agents run at the owner's effort, medium at the least.
- **Agent lines.** Derive every agent line and returned line with `handoff.py agents`; never type one. Log each
  dispatch in the session log's Dispatches table.
- **Records.** Save every handoff, return, probe and record in `memory/builds/dClosedLoop/`. Record the owner's words
  verbatim as they land.
- **Commits.**
  - Each commit ends with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
  - Give commits a 600000 ms timeout.
  - Stage explicit paths.
  - Write Python to files, never through a heredoc.
  - After `gen_build_index.py --write`, commit every file it renders.
- **Never:**
  - merge to main or push without the owner's explicit ask;
  - run the unattended kit's on-demand self-test suites (`run-unattended-gates.sh --selftests`), though `--checks` is
    fine;
  - use `--dangerously-skip-permissions`;
  - write a secret into a file.
- **Final messages.** Each one ends with the charter's state block.

**Raise these with the owner; do not settle them alone.**
- **The Closed Loop Atlas** (`https://claude.ai/artifact/GXivko4hRVxQG9mJNXUaZR`, v77). The owner's standing ask is to
  republish it after design changes. With the execution records the page measured 16.4 MB, past its 16 MB limit, so
  it was not republished. The opening adds 22 READMEs. Ask whether the atlas should skip the execution records or be
  split.
- **Anything the plan gets wrong.** v2 is frozen and the plan's decided answers stand, so raise it as a question to
  the owner, never a silent fix.

### brief:goal

Everything the chain's first run needs, built and checked on node d as records under `memory/`, so that the owner can
read the opening and ask for its one landing. That covers the hardened instruments, the departures report, the packet
instrument, the opening of all 22 chain builds, nine decision rows and each node's preparation steps. Phase 0 ends
when the opening is committed on the branch, every P0.7 check is green, and the owner has the opening read in front
of them.

### task:todo

P0.6's bare-id fix first; then P0.1, P0.2, P0.3, P0.4, P0.5, P0.8 and P0.7, in that order; then P0.9; then the owner's opening read, and stop.

### Charter rules

- [ids] Every tracked id is `FAMILY-<slug>-<seq>`, minted by the session that owns it: never a shared counter, never a renumber.
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
