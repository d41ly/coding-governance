# Walk handoff brief: the whole-design walk's walkers

**Serves:** research PLAY-dClosedLoop-1

A walker's handoff renders its goal and non-goals from this brief record, through `handoff.py render --input
prompt=<this file>`. The build's own brief names the design pass's goal, and the spec-reviewer role reviews the spec it
is handed. Handed their walk brief as `input:spec`, four of run B's walkers reviewed the brief instead of walking, one
of them twice. This record names the specs and the lens in the role's own words.

## The prompt

Walk the sealed copy of dClosedLoop's design, as the walk brief handed as `input:spec` says.

## The brief

### Goal

The specs you review are the design records in the sealed copy of dClosedLoop that your walk brief names. The walk
brief, handed to you as `input:spec`, is the lens you review them through and your instructions, never a spec to
review. Walk your slice's items through its scenarios as the brief says. Return exactly the brief's shape: the
pre-mortem line, the findings, the walk table, the build and principle verdicts, and the line naming any read outside
the brief's list.

### Non-goals

- Reviewing the walk brief, the audit's seal, the walk kit or the scorer. A defect you see in them goes in one line at
  the end of your return, and nowhere else.
- Reading anything outside the brief's list, which leaves out the working tree's records, the other briefs and the
  session's scratch and temp folders.
- Writing anything to the repository.
