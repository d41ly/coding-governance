# unattended-stops — how a run pauses, who drives it, and which processes are its own

```toml
feature = "unattended-stops"
title = "The unattended run's stops: HELD, the lease and the process ledger"
status = "building"
streams = ["tooling"]
decisions = ["TOOL-dDerivedDocket-4", "TOOL-dDerivedDocket-28"]

[claims]
gate-legs = []
kits = []
git-hooks = []
harness-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = ["liveness-negative-from-another-population.md"]
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/unattended/unattended.sh",
  "tools/unattended/STOPS.template.md",
  "memory/guides/UNATTENDED-STOPS.md",
  ".unattended.conf",
]
```

Split out of `unattended` when that dossier reached its size cap, so the keys it touches are
claimed there, save the one gotcha class that arrived with the cap already reached: a probe of
aborted records whose liveness negative came from another population. The split follows the stop
contract's seam: that dossier is how a run proceeds, this one is how it pauses, which session
drives it, and which processes it may reap.

## Constraints & why

**A stop the run cannot fix is a PAUSE, not an ending.** `HELD` is non-terminal: entered by `--hold`
with a code, a condition and a witness, left by `--resume` alone. The LEASE is the run-state file's
facts, judged fresh by `--liveness`, which reads `HELD` as its own verdict, so a resume tells
orientation from take-over. Every `phase` read routes through `read_derived_phase` or
`read_recorded_phase`. A hold on a review that deferred twice records its Workflow runId
(`--pending-run`, fact `hold-run`), and the take-over prints the relaunch
(`TOOL-dDerivedDocket-29`). See `UNATTENDED-STOPS.md`.

**One worktree answers for a slug.** The record is one tracked copy per worktree and every clock
belongs to the calling one, so the worktree whose HEAD is the run's branch — `run-branch`, else
`branch-ref`, the gate-guard's key — is the only one that acts: git checks a branch out in one
worktree at most. Elsewhere `--liveness` reads `ELSEWHERE`, second after `TERMINAL`; the tick skips it
by name, the stop-guard allows, and the matrix's HELD and working rows refuse a leased record at check
58, naming where the run is driven from (`TOOL-dDerivedDocket-62`). A record naming no branch is
graded where it is read, and the tick acts on none of its copies.

**The holder keeps its own `--replaces`.** The matrix reads `--replaces` above the same-session row,
and that row takes only a caller under a pid the record does not name, because a restart is a new
process. The holder's own process, or a sub-agent inside it, carries both the recorded session and
the recorded pid, so its new id meets the clock rows: refused at 58 while the clock is fresh or
unknown, taken over as `presumed-stopped` once stale (`TOOL-dDerivedDocket-63`).

**A process not in the ledger is never killed.** Every command the driver starts through
`run_bounded` is recorded by identity, pid and procfs start token beside the driver's own, in a
per-slug ledger, and only a recorded process alive with its token while its driver is gone is reaped
(`TOOL-dDerivedDocket-28`). Only the verbs that hold the lease reap, one orphan at a time through
`PROCMON_CMD --kill-msys <pid>`, and success is read back from the pid rather than from the reaper's
exit. The runner's wrapper carries the repository root as its `$0`, which is what lets the
process-monitor fence admit a tree whose parent is gone. Matching by command line was ruled out by
the run that found five of six same-named processes to be another repository's.

## Shared seams

- `reap.py --kill-msys` — process-monitor's fenced, leaves-first kill, which `PROCMON_CMD` names.
  The driver calls it and reimplements neither the fence nor the walk.
- `resolve_landed_log` — the one derivation of the log's directory; the ledger's path is derived
  from it, so the two files cannot drift apart.

## Reuse affordance

seam: `run_bounded` — reuse for any project-declared command a verb must bound and be able to reap after its session dies; extend by calling it, which records the process with no code of the caller's.

## Gaps

- **A process the agent starts in its own shell is invisible to the ledger** — a suite run at
  `VERIFYING`, an ad-hoc bar. A session that dies during one leaves it to a person and to the
  process-monitor kit's own sweep.
- **The arms reap MSYS trees only.** A bar whose legs are native processes rests on the reaper's own
  leaves-first walk, which that kit measures and this one does not.
