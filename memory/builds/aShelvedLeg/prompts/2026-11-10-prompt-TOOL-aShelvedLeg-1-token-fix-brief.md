# Brief — aShelvedLeg: spec 1's acceptance clears the spec-token check

**Serves:** research TOOL-aShelvedLeg-1

## The brief

### Goal
`python tools/check-spec-tokens.py` prints four `[bar]` hits on spec 1's §6, all of them a runner script named in backticks inside an acceptance criterion: `run-selftests.sh --check` (AC3), `tools/unattended/run-unattended-gates.sh` (AC4 and AC6) and `run-unattended-gates.sh --checks` (AC5). Each criterion observes a file by grep or awk, not by running the runner, so re-point each witness at what it observes (the file read, the row matched or the gate leg's name) so that no backticked token in §6 names a runner. Change nothing else, as a rev-1 to rev-2 bump with one revision-log line.

### Items
1. AC3, AC4, AC5 and AC6 each observe the same fact with no backticked token naming `run-selftests.sh` or `run-unattended-gates.sh`. The file a criterion greps may be named in prose without backticks, or through the gate leg the manifest is keyed on.

### Acceptance
`python tools/check-spec-tokens.py` prints no line naming `memory/builds/aShelvedLeg/spec/`, and `bash tools/memory-tree/check-memory-hygiene.sh --only 12` prints no `check 12 FAILED` line naming it.

### Gates
spec tokens · memory hygiene.

### Non-goals
Any change to the spec's scope, design, files touched, budget or forks, or to what any criterion observes.

### Limitations
`memory/project/spec-token-waivers.txt` is shrink-only: no waiver row.

### Reuse
The spec's own §10 stands.
