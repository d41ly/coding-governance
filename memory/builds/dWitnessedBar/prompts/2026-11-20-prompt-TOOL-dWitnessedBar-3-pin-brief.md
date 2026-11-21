**Serves:** journal TOOL-dWitnessedBar-3

# Brief — dWitnessedBar: TOOL-dWitnessedBar-3's one unpinned count

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. The rev-7 re-ground of TOOL-dWitnessedBar-3 left one numeric fact
`writing_practice.py check pinned-facts` reds: the count of files that read the retired key.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem, so
`python tools/playbook/writing_practice.py check pinned-facts` reports no red for it.

### Items

1. Put a pin on the line that carries the count of readers the re-ground re-derived (an id, a path:line, PINNED or
   DERIVED), or rewrap the sentence so an existing mark lands on that line. Change nothing else; the status header
   keeps its status.

Before returning, run `python tools/playbook/writing_practice.py check pinned-facts`,
`bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-3` and
`python tools/check-spec-tokens.py --spec <path>`, and fix every finding about this spec they name.

### Acceptance

The three commands report nothing against this spec; the spec carries the next rev and one revision-log line naming
this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-3. No product code.

### Limitations

The write grant is `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-3.md` alone.

### Reuse

None needed: one line.
