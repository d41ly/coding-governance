# Pass-leg fix — dSkippedRecord: TOOL-dSkippedRecord-2's one unpinned fact

**Serves:** research TOOL-dSkippedRecord-2

## The prompt

> The `writing practice (records and units)` leg's pinned-facts reader reads one count with no pin on its line in this spec: the section-6 criterion whose Red-when clause names unit 1's section-4 rows, where the section number and the word after it read as a count.

## The brief

### Goal
Clear the one `writing practice (records and units)` hit the bar printed on this spec, changing nothing else.
An earlier inline fix reworded that clause and was taken back out of the red-fix lane, which admits no spec
path, so the clause stands as rev-1 wrote it.

### Items
1. The Red-when clause of the criterion that compares unit 1's spec with its state at this unit's base: spell
   unit 1's section-4 table so no digit sits before the noun, for example "unit 1's mode table", keeping what the
   criterion asserts.
2. Bump the spec to rev-2 with one section-9 line naming this record and the leg.

### Acceptance
`python tools/playbook/writing_practice.py check` prints no `pinned-facts: red` line naming this spec. That run is
the main loop's; the writer confirms with the reader its role admits.

### Gates
`writing practice (records and units)` · `positional (the citation check alone)` · `memory hygiene` ·
`spec tokens (a spec's own names resolve)`

### Non-goals
No change to the spec's meaning, criteria, figures or status (it stays CLOSED), and no other spec. Do not commit
and do not stage.

### Limitations
The spec is CLOSED at rev-1 and built. Its `gen:spec-records` region is the index generator's; leave it alone.
