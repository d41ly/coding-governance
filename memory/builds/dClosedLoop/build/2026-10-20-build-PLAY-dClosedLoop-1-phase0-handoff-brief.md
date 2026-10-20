# Phase 0 handoff brief: dClosedLoop's last work before the chain's first run, in a new session

**Serves:** research PLAY-dClosedLoop-1

The new session's handoff renders its goal, items, acceptance, gates and non-goals from this brief record, through
`handoff.py render --role gov-session --input prompt=<this file>`. The owner approved the execution plan after
walking it, and asked for Phase 0 to start in a new session: "Fold, then give me a fully oriented hand off to start
phase 0 in a new session." (`build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md` `[walk]`).

## The prompt

Run Phase 0 of dClosedLoop's execution plan: harden the deviation instruments, add the departures report, build the
packet instrument, commit the schedule script's checks, write the opening of all 22 chain builds with the decision
rows the owner's answers ratify, and prepare the nodes, then bring the opening to the owner to read before its one
landing.

## The brief

### Goal

Everything the chain's first run needs, built and checked on node d as records under `memory/`, so that the owner can
read the opening and ask for its one landing. That covers the hardened instruments, the departures report, the packet
instrument, the opening of all 22 chain builds, nine decision rows and each node's preparation steps. Phase 0 ends
when the opening is committed on the branch, every P0.7 check is green, and the owner has the opening read in front
of them.

### Items

P0.1 to P0.9 of `build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` `[phase-0]`, in its order, with the
owner's walk folded in.

### Acceptance

- Each P0 item's acceptance and red tests hold as the plan states them, each red seen before its green.
- P0.7's checks are green on the committed opening, the generator-grammar bare-id predicate printing nothing.
- The owner's opening read is ready as the walk's answer 2 sets it. It covers the decision rows, the grant row,
  dTrueNorth's README and packet in full, and the opening script's check output and per-build summary for the other
  21.
- Every record, return and probe is in the build folder, and every commit is on `branch/gov-architecture-plan-e34297`.

### Gates

Per commit: the pre-commit hook's staged hygiene, and `gen_build_index.py --write` with every file it renders
committed. Before the opening is offered: P0.7's checks and red tests, and the full bar `bash
tools/run-gates/run-gates.sh` on a quiescent tree. The unattended kit's own suites are on no leg of it, and none
is run.

### Non-goals

- No product code: nothing under `tools/`, `skills/`, `coding-governance-agents.template.md` or
  `WIRE-INTO-PROJECT.md`, and no `AGENTS.md` re-render. Phase 0 is records under `memory/` only.
- No chain build's run, spec or code: the opening writes READMEs, rosters, packets and asks, never a unit spec.
- No merge to main and no push, and no landing of the opening, without the owner's explicit ask.
- No change to v2, the audit's records or the execution plan's decided answers. A needed change is a question to the
  owner.
- No run of the unattended kit's on-demand self-test suites, `run-unattended-gates.sh --selftests` (the owner's
  standing instruction; `--checks` is fine).
