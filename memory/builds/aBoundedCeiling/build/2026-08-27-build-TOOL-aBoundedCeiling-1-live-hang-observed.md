# A live `--close` hang, observed on node `a` while speccing the fix for it

**Serves:** research TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5 TOOL-aBoundedCeiling-6

Observed 2026-08-27 01:45 local, node `a`, while this build's own commits were running slowly.
Nothing here was staged or reproduced: it was already running.

## What was found

Six abandoned processes, from an ADOPTER repository on this machine, not from `coding-governance`.
The tell is the path — `scripts/unattended/` and `scripts/gate.sh`, where gov's own spellings are
`tools/unattended/` and `tools/run-gates/run-gates.sh`.

| pid | command | age | CPU | parent |
|---|---|---|---|---|
| 22220 | `scripts/unattended/unattended.sh --close dPinnedVintage` | 3h19m | 16.9 s | **GONE** |
| 25480 | same, child of 22220 | 3h18m | **0 s** | 22220 |
| 28664 | `scripts/gate.sh` | 3h18m | 6.5 s | 30344 |
| 26040 | `scripts/gate.sh`, child of 28664 | 2h35m | **0 s** | 28664 |
| 2812 | `scripts/unattended/unattended.test.sh` | 2h35m | 45.6 s | 3904 |

Read the CPU column before anything else. Two of the five have accumulated **zero** CPU across more
than two and a half hours. They are not slow. They are blocked, and they will stay blocked until the
machine reboots, because nothing in the chain has a deadline and the session that started the top one
is gone.

`Get-CimInstance Win32_Process` is what produced the table; `Get-Process` alone gives CPU but not the
command line or the parent, and the command line is the only thing that identifies whose repo this is.

## Why this is decisive for this build

**It is the owner's prompt, running.** The prompt said the self-check gates "often hang" and that
they "separately exist on `unattended.sh --close` execution". This is that, with a stopwatch on it.

**And it refutes a scope this build nearly shipped.** `TOOL-aBoundedCeiling-1` bounds each leg of
`tools/run-gates/run-gates.sh`. The hung tree above never reaches that runner — it invokes
`scripts/gate.sh`, which is a different project's own gate command. A per-leg ceiling inside gov's
runner is invisible to it. So a solution that stops at unit 1 would have left the exact failure the
prompt names untouched in the exact place it was observed.

What binds every adopter regardless of which runner they use is a bound on the DoD gate invocation
ITSELF, in `tools/unattended/unattended.sh`, where `$GATE_CMD` is expanded. That is
`TOOL-aBoundedCeiling-6`, added to this build's roster by `--rescope` on the strength of this
observation.

## It is not only the adopter's

Fifteen minutes later, in THIS repository, `tools/memory-tree/check-memory-hygiene.sh` (pid 19064,
started 01:43:44, no `--staged`) was found running with its parent already GONE. Nothing in this run
started a full-tree hygiene check at that moment, and no reader for its output exists any more.

That matters for the diagnosis in a way the adopter's tree cannot show. The adopter's hang is one
project's `--close`; this is gov's own checker, orphaned during ordinary use, on the machine that
authored the rule. It is the gotcha's own sentence — orphans accumulate during ordinary use and not
just after an interrupt — reproduced on this node while writing the spec that cites it.

The measurement it explains: this build's `git commit` hook (pid 30596,
`check-memory-hygiene.sh --staged`) had accumulated **33.5 seconds of CPU across 15 minutes of wall
clock**, which is 3.7% busy. It was never hung. It was starved, alongside 66 resident `bash.exe`
processes, several of them abandoned.

## The class it belongs to

`memory/gotchas/bounded-through-a-pipe-is-unbounded.md`, third bullet of "Where it bit", which
already records the harness half of this: killed or completed runs leaving leg children orphaned,
holding scratch subtrees, and every later suite then "produced ZERO bytes for twenty minutes and read
as a hang in the code under test". Its stated diagnostic applies exactly — a process emitting nothing
at all, rather than stopping partway, is a machine symptom and not a logic one.

The contention is measurable from this side too: 66 `bash.exe` processes were resident while these
six held on, and this build's own `git commit` hook, which normally costs about seven minutes on the
memory-hygiene leg, was still running at twelve.

## What was deliberately NOT done

**The processes were not killed.** They belong to another repository and another session, this run
has no owner turn in which to ask, and an abandoned process can still be holding a scratch directory
or an index someone intends to inspect. Killing another project's work is outside anything this
build's mandate authorizes. It is parked in this run's record instead, with the pids, so the owner
can decide in one glance.

The remedy, when the owner wants it, is the one the gotcha records: kill by command line, then
re-run. After the equivalent clean-up in the incident that gotcha describes, the hygiene engine
finished in 42 seconds green, having previously read as a hang for twenty minutes.
