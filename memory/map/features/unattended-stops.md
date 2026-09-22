# unattended-stops — how a run pauses, who drives it, and which processes are its own

```toml
feature = "unattended-stops"
title = "The unattended run's stops: HELD, the per-slug lease and the process ledger"
status = "building"
streams = ["tooling"]
decisions = ["TOOL-dDerivedDocket-4", "TOOL-dDerivedDocket-28"]

[claims]
gate-legs = []
kits = []
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
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

Split out of `unattended` when that dossier reached its size cap, so it claims no keys: every key it
touches is claimed there. The split follows the stop contract's seam: that dossier is how a run
proceeds, this one is how it pauses, which session drives it, and which processes it may reap.

## Constraints & why

**A stop the run cannot fix is a PAUSE, not an ending.** `HELD` is non-terminal: entered by
`--hold` with a code, a condition and a witness, left by `--resume` alone. A per-slug LEASE
under the git common dir keys on the session-scoped keepalive id, so a resume tells orientation
from take-over. Every `phase` read routes through `read_derived_phase` or `read_recorded_phase`.
A hold on a review that deferred twice records its Workflow runId (`--pending-run`, fact
`hold-run`), and the take-over prints the relaunch (`TOOL-dDerivedDocket-29`).
See `UNATTENDED-STOPS.md`.

**A process not in the ledger is never killed.** Every command the driver starts through
`run_bounded` is recorded by identity, pid and procfs start token beside the driver's own, in a
per-slug ledger beside the lease, and only a recorded process alive with its token while its driver
is gone is reaped (`TOOL-dDerivedDocket-28`). Only the verbs that hold the lease reap, one orphan at
a time through `PROCMON_CMD --kill-msys <pid>`, and success is read back from the pid rather than
from the reaper's exit. The runner's wrapper carries the repository root as its `$0`, which is what
lets the process-monitor fence admit a tree whose parent is gone. Matching by command line was ruled
out by the run that found five of six same-named processes to be another repository's.

## Shared seams

- `reap.py --kill-msys` — process-monitor's fenced, leaves-first kill, which `PROCMON_CMD` names.
  The driver calls it and reimplements neither the fence nor the walk.
- `resolve_lease_path` — the one derivation of the lease's directory; the ledger's path is derived
  from it, so the two files cannot drift apart.

## Reuse affordance

seam: `run_bounded` — reuse for any project-declared command a verb must bound and be able to reap after its session dies; extend by calling it, which records the process with no code of the caller's.

## Gaps

- **A process the agent starts in its own shell is invisible to the ledger** — a suite run at
  `VERIFYING`, an ad-hoc bar. A session that dies during one leaves it to a person and to the
  process-monitor kit's own sweep.
- **The arms reap MSYS trees only.** A bar whose legs are native processes rests on the reaper's own
  leaves-first walk, which that kit measures and this one does not.
