**Serves:** journal TOOL-dWitnessedBar-53

# Brief — dWitnessedBar: TOOL-dWitnessedBar-53's one unpinned fact

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. The rev-5 re-ground of TOOL-dWitnessedBar-53 left one numeric fact
that `writing_practice.py check pinned-facts` reds, and the pass legs would red on it.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem, so
`python tools/playbook/writing_practice.py check pinned-facts` reports no red for it.

### Items

1. The checker printed, on 2026-11-19 at `da9345429`: `unpinned fact `6 rows`: pin it on its line (an id, a
   path:line, PINNED or DERIVED)`. The fact sits in §2's probe paragraph, on the line that begins "After the commit,
   with those homes removed"; its PINNED mark wrapped onto the next line. Put a pin on the fact's own line, or rewrap
   the sentence so the existing mark lands on it.
2. Change nothing else. The status header keeps its status; bump only the rev.

Before returning, run `python tools/playbook/writing_practice.py check pinned-facts`,
`bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-53` and
`python tools/check-spec-tokens.py --spec <path>`, and fix every finding about this spec they name.

### Acceptance

The three commands report nothing against this spec; the spec carries the next rev and one revision-log line naming
this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-53. No product code.

### Limitations

The write grant is `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-53.md` alone.

### Reuse

None needed: a wrap of one sentence.
