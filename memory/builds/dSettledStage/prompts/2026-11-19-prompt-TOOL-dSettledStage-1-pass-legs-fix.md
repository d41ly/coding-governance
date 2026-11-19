# Pass-leg fix — dSettledStage: TOOL-dSettledStage-1's one unpinned-fact hit

**Serves:** research TOOL-dSettledStage-1

## The prompt

> pinned-facts: red · memory/builds/dSettledStage/spec/2026-11-19-spec-TOOL-dSettledStage-1.md · unpinned fact `2 records`: pin it on its line (an id, a path:line, PINNED or DERIVED)

## The brief

### Goal
Clear the one `writing practice (records and units)` hit the pass legs printed on this spec after unit 1's build
commit `864d85d42`, changing nothing else.

### Items
1. §3's line 56, "there, unit 2 records it as a follow-up.", reads "2 records" as a count. It is not a fact:
   reword it so no number sits before a counted noun, for example "TOOL-dSettledStage-2 registers it as a
   follow-up", keeping its meaning.
2. Bump the spec to rev-2 with one §9 line naming this record and the hit.

### Acceptance
`bash tools/run-gates/pass-legs.sh --base 6daf04180` prints no `pinned-facts` line naming this spec. That run is
the main loop's; the writer confirms with the writing-practice reader its role admits.

### Gates
`writing practice (records and units)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

### Non-goals
No change to any other section's meaning, the status, the date or any other spec. Do not commit and do not stage.

### Limitations
The spec is CLOSED and built at `864d85d42`; the rev bump records the wording change only.

### Reuse
None: a one-line rewording.

## Drawn from the session

> pinned-facts: RED · 5 red
— agent, the pass legs after 864d85d42

## Owner confirmation

Asked: Ready — say go and I'll start, or adjust any field.
Answer: go, no audit
