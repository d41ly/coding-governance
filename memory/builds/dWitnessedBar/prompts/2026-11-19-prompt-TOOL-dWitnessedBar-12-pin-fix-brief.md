**Serves:** journal TOOL-dWitnessedBar-12

# Brief — dWitnessedBar: TOOL-dWitnessedBar-12's one unpinned count, pinned

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. Unit 12's pass legs read one unpinned fact in its spec.

## The brief

### Goal

Pin the one unpinned count the writing-practice leg reds in the spec named here, as a rev bump with one revision-log
line naming this brief by its file stem.

### Items

1. The pass legs over unit 12 printed `pinned-facts: red` for the spec's `70 rows`: the descriptor list's lead-in
   carries `DERIVED` on the line above the count, so the count's own line has no marker. Put the marker on the count's
   line, changing no fact.

Before returning, run `python tools/playbook/writing_practice.py check pinned-facts` and
`python tools/check-spec-tokens.py --spec <path>`, and fix every finding about this spec either names.

### Acceptance

The pinned-facts check names no line of this spec; the spec carries the next rev and one revision-log line naming this
brief.

### Gates

memory hygiene · writing practice (records and units)

### Non-goals

No other change to the spec. No product code.

### Limitations

The status header keeps its status. The write grant is
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-12.md` alone.

### Reuse

None needed: a one-line marker.
