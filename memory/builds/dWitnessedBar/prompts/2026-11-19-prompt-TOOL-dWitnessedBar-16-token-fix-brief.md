**Serves:** journal TOOL-dWitnessedBar-16

# Brief — dWitnessedBar: TOOL-dWitnessedBar-16's carried clause token restored

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. The rev-8 re-ground blob-pinned the line that names
cl-dClosedLoop-0354's carried token, so the build's coverage reds on that token.

## The brief

### Goal

Restore the carried token in the spec named here, as a rev bump with one revision-log line naming this brief by its
file stem.

### Items

1. The amended text of cl-dClosedLoop-0354 carries the token
   `memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews-instruments.md:1087-1090`, and
   the coverage join matches it byte for byte. The rev-8 re-ground respelled it with a blob pin in the population
   rule's sentence. Restore the exact token there, in backticks; a `.md` line citation is a document line the
   positional check does not ban. Leave the other blob pins as they are.

Before returning, run `python tools/memory-tree/gen_build_index.py --check-coverage` and
`python tools/check-spec-tokens.py --spec <path>`, and fix every finding about this spec either names.

### Acceptance

The coverage check names no red token for dWitnessedBar; the spec carries the next rev and one revision-log line
naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other change to the spec. No product code.

### Limitations

The status header keeps its status. The write grant is
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-16.md` alone.

### Reuse

None needed: one restored token.
