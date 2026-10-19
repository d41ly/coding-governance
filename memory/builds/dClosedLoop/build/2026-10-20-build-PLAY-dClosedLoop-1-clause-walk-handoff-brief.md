# Clause walk handoff brief: run C's walkers

**Serves:** research PLAY-dClosedLoop-1

A run C walker's handoff renders its goal and non-goals from this brief record, through `handoff.py render --input
prompt=<this file>`, as run B's last walker's did from `walk-handoff-brief.md`. The spec-reviewer role reviews the spec
it is handed, so this record names the specs and the lens in the role's own words.

## The prompt

Read the sealed copy's chain clauses for your builds, as the clause walk brief handed as `input:spec` says.

## The brief

### Goal

The specs you review are the `[chain]` clauses of your builds in the sealed copy of dClosedLoop's design, which your
clause walk brief names. The brief, handed to you as `input:spec`, is the lens you review them through and your
instructions, never a spec to review. Read each clause against the records that settle what it builds, as the brief
says. Return exactly the brief's shape: the pre-mortem line, the findings, the clause table, the build verdicts, and
the line naming any read outside the brief's list.

### Non-goals

- Reviewing the clause walk brief, the audit's seal, the walk kit or the scorer. A defect you see in them goes in one
  line at the end of your return, and nowhere else.
- Reading anything outside the brief's list, which leaves out the working tree's records, the other briefs and the
  session's scratch and temp folders.
- Writing anything to the repository.
