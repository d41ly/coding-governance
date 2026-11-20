**Serves:** journal TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-3

# Brief — dWitnessedBar: the unit 3 to unit 5 edge pair, and spec 5's one unpinned count

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. Spec 5's rev-6 re-ground found that unit 5 adds a verb to
`tools/run-gates/verdict_flow.py`, which unit 3 (order 20) creates, and named that dependency in prose (§8 F4) because
a one-way edge fails the hygiene edge check. Unit 4's pass legs also red spec 5 on one numeric fact with no pin on its
line.

## The brief

### Goal

Revise the two specs named here in place, each as a rev bump with one revision-log line naming this brief by its
file stem, so the dependency is a declared edge pair and spec 5 carries no unpinned fact.

### Items

1. Add `consumes-from TOOL-dWitnessedBar-3` to TOOL-dWitnessedBar-5's §3 Edges, naming what it consumes, and the
   mirroring `hands-off TOOL-dWitnessedBar-5` to TOOL-dWitnessedBar-3's §3 Edges. Restate spec 5's §8 F4 to point at
   the edge instead of the prose dependency.
2. In spec 5, put a pin on the line that carries the count `python tools/playbook/writing_practice.py check
   pinned-facts` names, or rewrap the sentence so its existing mark lands on that line.
3. Change nothing else; each status header keeps its status.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5`,
`python tools/check-spec-tokens.py --spec <path>` over each spec, `python tools/playbook/writing_practice.py check
pinned-facts` and `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec <path>` over each, and fix every
finding about these specs they name.

### Acceptance

The commands report nothing against either spec; each carries the next rev and one revision-log line naming this
brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-3 and TOOL-dWitnessedBar-5. No product code.

### Limitations

The write grant is `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-3.md` and
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-5.md`.

### Reuse

The Edges blocks of any two specs this build already pairs, as the shape to copy.
