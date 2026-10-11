# Brief — the held suites still red on the default branch

**Serves:** journal TOOL-aHomedAnchor-22 TOOL-aHomedAnchor-23 TOOL-aHomedAnchor-24 TOOL-aHomedAnchor-25

node a · 2026-10-11 · attended · asks TOOL-aHomedAnchor-8 to -21

## The prompt

```
figure out if they're still failing against the current main, fix what's necessary
```

A later turn of the same session:

```
dont run the unattended shards this time
```

## The brief

### Goal

Establish which of the 14 held suites the close of `aHomedAnchor` filed as red are still red on the
current default branch, and fix the in-tree defects that keep them red.

### Items

1. Decide red or green per suite from the daily held job's latest run on the default branch, at `d006cfc5`, and fix each in-tree cause [planned TOOL-aHomedAnchor-22 TOOL-aHomedAnchor-23 TOOL-aHomedAnchor-24 TOOL-aHomedAnchor-25]

### Acceptance

Each fixed suite's failing arm is observed green under the held job's condition: Python with
`PYTHONUTF8` unset for the encoding class, the arm's own predicate or a slice for the rest.

### Gates

`bash tools/run-gates/run-gates.sh`

### Non-goals

Running the unattended shard suites, by the owner's turn above. Re-designing another build's mechanism.

## Drawn from the session

none

## Owner confirmation

not asked — the brief draws on nothing outside the prompt
