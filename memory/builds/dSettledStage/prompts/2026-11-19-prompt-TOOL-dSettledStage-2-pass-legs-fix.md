# Pass-leg fix — dSettledStage: TOOL-dSettledStage-2's unpinned facts and one positional citation

**Serves:** research TOOL-dSettledStage-2

## The prompt

> pinned-facts: red · memory/builds/dSettledStage/spec/2026-11-19-spec-TOOL-dSettledStage-2.md · unpinned fact `3 files`: pin it on its line (an id, a path:line, PINNED or DERIVED)
> pinned-facts: red · memory/builds/dSettledStage/spec/2026-11-19-spec-TOOL-dSettledStage-2.md · unpinned fact `3 rows`: pin it on its line (an id, a path:line, PINNED or DERIVED)
> pinned-facts: red · memory/builds/dSettledStage/spec/2026-11-19-spec-TOOL-dSettledStage-2.md · unpinned fact `4 files`: pin it on its line (an id, a path:line, PINNED or DERIVED)
> pinned-facts: red · memory/builds/dSettledStage/spec/2026-11-19-spec-TOOL-dSettledStage-2.md · unpinned fact `54 files`: pin it on its line (an id, a path:line, PINNED or DERIVED)
> tags: positional · unlisted · memory/builds/dSettledStage/spec/2026-11-19-spec-TOOL-dSettledStage-2.md · (AC1's fixture file and its line 3) · cite `path#symbol` or a blob-pinned line: positional.py pin memory/builds/dSettledStage/spec/2026-11-19-spec-TOOL-dSettledStage-2.md

## The brief

### Goal
Clear the four `writing practice (records and units)` hits and the one `positional` hit the pass legs printed on
this spec after unit 1's build commit `864d85d42`, before unit 2 is built, changing nothing else.

### Items
1. The counts on lines 24, 100, 352-354 and 411-412 (§1, §3, AC4 and §9): pin each on its own line, the probe's
   counts as `PINNED at 12764ec21`, an expected count as `DERIVED at observation`, as AC4's `figure:` line does.
2. AC1's fixture citation, the file `a.sh` and its line 3 joined by a colon, is a line of a fixture repository the criterion builds: spell it so it is no `path:line`
   citation, for example "lists line 3 of `a.sh`", keeping what the criterion asserts.
3. Bump the spec to rev-2 with one §9 line naming this record and the hits.

### Acceptance
`bash tools/run-gates/pass-legs.sh --base 6daf04180` prints no `pinned-facts` and no `positional` line naming this
spec. That run is the main loop's; the writer confirms with `python tools/playbook/positional.py check` and the
writing-practice reader its role admits.

### Gates
`writing practice (records and units)` · `positional (the citation check alone)` · `memory hygiene` ·
`spec tokens (a spec's own names resolve)`

### Non-goals
No change to the spec's meaning, criteria, figures or status (it stays SPECCED), and no other spec. Do not commit
and do not stage.

### Limitations
The spec is committed at rev-1 and unbuilt.

### Reuse
None: pins and one rewording.

## Drawn from the session

> pinned-facts: RED · 5 red
— agent, the pass legs after 864d85d42

## Owner confirmation

Asked: Ready — say go and I'll start, or adjust any field.
Answer: go, no audit
