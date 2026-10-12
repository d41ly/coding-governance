# Brief — aSparedHolder: the resume tick spares a live session

**Serves:** journal TOOL-aSparedHolder-1

## The prompt

> On 2026-10-10, unattended run aFrugalTurnstile (worktree .claude/worktrees/awesome-cannon-44b2b1, session c43608a7-c8e7-4081-be42-83f438359a45) was killed and relaunched 7 times between 04:39Z and 18:30Z. Each was a `resume-tick run-resumed aFrugalTurnstile attempt N` line in the host health log. The first one killed the live interactive session (pid 34476). The OS did not reboot (last boot 2026-10-04).
>
> 1. The liveness verdict ignores live background work. [...] It should count a live signal: a running `run-gates.sh` whose turnstile beacon names this worktree, a registered task heartbeat, or the gate-logs mtime. Or it should refuse to kill a live pid and only report it.
> 2. The idle-wake keepalive never delivered. [...] Find out why [...] Then either fix the delivery or stop the protocol from depending on it as the liveness signal.
> 3. The relaunch is `claude -p`, which can't wait on background work. [...] Fix one of two ways: make the stop-guard refuse a turn end in a -p session while its own background tasks run, or give the resumed payload a rule to wait in the foreground (no background spawns).
>
> Acceptance: A staged failing case is observed RED, then GREEN, for each defect, in resume-tick.test.sh and unattended.test.sh fixtures. A live pid with a running bar must not be killed, and a -p session with a running background task must not be allowed to stop. The PROTOCOL template and memory/guides/UNATTENDED-PROTOCOL.md stay byte-identical. Watch the protocol size row in tools/template-size-limits.txt. Don't touch the aFrugalTurnstile build. It is closing in its own session.

## The brief

### Goal
Stop the resume tick from killing a live session it did not launch, and let a resumed headless
session keep its background work alive through a turn end.

### Items
1. A live recorded pid the tick did not launch is reported, never killed or relaunched over.
2. The idle-wake's silence is recorded as measured, and a resumed session reaps the jobs it inherits.
3. The resumed `claude -p` waits for its background Workflows and agents.

### Acceptance
Each item's arm in `resume-tick.test.sh` is observed RED against the tick at BASE, then GREEN.

### Gates
`unattended kit gate` · `kit version markers` · `memory hygiene` · the held `resume-tick.test.sh`.

### Non-goals
The aFrugalTurnstile build. The liveness verdict's arithmetic, which every other reader shares.

### Limitations
The protocol template is at its size ceiling, so its edits are byte-neutral.

### Reuse
The kill and launch paths already exist in `resume-tick.sh`; the unit narrows one and adds one
environment line to the other. No new helper.

## Drawn from the session

> Background tasks still running 10m after the last turn (workflow "Builds exactly ONE unit of an unattended build, in a sidecha"); stopping them. Set CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0 to wait indefinitely.
— agent, the first line of every resumed aFrugalTurnstile session's `.out` file, 2026-10-10

## Owner confirmation

Asked: none; the owner's prompt names the three defects and their acceptance.
Answer: none.
