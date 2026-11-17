# Revision — aPiecewiseGrade: the owner's answer to TOOL-aPiecewiseGrade-6's F1

**Serves:** research TOOL-aPiecewiseGrade-6

## The prompt

> (b) Deadline or dead owner

The owner's answer, 2026-11-16, to TOOL-aPiecewiseGrade-6's F1, put through the session's question tool: "How is a killed run's lock judged stale?", with options (a) deadline only, the claim-push rule, and (b) deadline or dead owner.

## The brief

### Goal
The owner resolved TOOL-aPiecewiseGrade-6's F1 as (b): the per-slug spec-token lock is also stale once its owner processes are gone, so a killed run's lock breaks at the next dispatch instead of holding the slug's cache off until its deadline. The lock records the driver's pid and the checker's pid, and counts as stale only when its deadline has passed or both are gone.

### Items
1. In `memory/builds/aPiecewiseGrade/spec/2026-11-16-spec-TOOL-aPiecewiseGrade-6.md`, F1 carries `RESOLVED (owner, 2026-11-16): (b) Deadline or dead owner` in its own span, its header gains the ratified pointer, and its rev bumps with a revision-log line naming this record by its file stem.
2. Rewrite the design to (b): what the lock file holds and when each pid is written, how liveness of a pid is judged on this repository's platforms (MSYS on Windows included, where a Windows pid and an MSYS pid differ), and why a lock whose checker outlived its driver is never broken while that checker runs. The claim-push caller of the shared factory keeps its bytes and its behaviour: say how the factory takes the liveness rule without changing claim-push.
3. Criteria and arms observe the dead-owner break at the next dispatch, the surviving-checker case not broken, the deadline break, and claim-push's arms unchanged. Each new arm is one that can be seen red on a staged break.
4. Stage the spec and clear `python tools/check-spec-tokens.py --spec` over it. Do not commit. Return its path and status line, each new or changed criterion's id with one line, any fork with its recommendation, and the checker's final line.

### Acceptance
- TOOL-aPiecewiseGrade-6's F1 reads RESOLVED with the owner's pick, its rev bumped and its log naming this record.
- The design breaks a dead owner's lock at the next dispatch, never a live checker's, and claim-push's bytes and arms do not move.

### Gates
`check-spec-tokens.py --spec` over the spec.

### Non-goals
- Any edit to a CLOSED spec, or to TOOL-aPiecewiseGrade-5's spec.
- Any change to a verdict, a refusal line, the summary line or an exit status of the checker or of `--dispatch`, beyond the busy line the spec already states.
- A row raised in any shrink-only registry.
- Building anything.
