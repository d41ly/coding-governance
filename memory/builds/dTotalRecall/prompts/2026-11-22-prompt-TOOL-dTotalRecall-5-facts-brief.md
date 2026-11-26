**Serves:** journal TOOL-dTotalRecall-5

# Brief — dTotalRecall: pin the unpinned facts rev-11 of TOOL-dTotalRecall-5 wrote

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 5's pass legs at `6ff99a7ca` read `writing practice (records and
units)` red on the facts its rev-11 fold wrote without a pin; the unit is built and CLOSED.

## The brief

### Goal

Revise the spec in place as a rev-12 bump, with one revision-log line naming this brief by its file stem and saying
the change is a record-only pin to a CLOSED spec, no criterion moved, so
`python tools/playbook/writing_practice.py check pinned-facts` names no line of
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-5.md`.

### Items

1. Run the check and take every red line naming this spec. Pin each fact on its own line: a count a stated search
   gives is DERIVED with that search and the commit it ran at (`17f07b292` for §4 "The fixtures", or the builder's
   pass at `202a354a4` where the fact is the build's), a value set by a decision is PINNED with today's date and the
   mark that set it. A fact nothing on disk supports is cut, never guessed.
2. Keep every claim, criterion and the status header `CLOSED` as they stand; this is a facts pass, not a re-ground.
   Tighten prose only on lines you touch; the spec is over its size ceiling and must not grow by more than the pins.

Before returning, run `python tools/playbook/writing_practice.py check pinned-facts`,
`python tools/check-spec-tokens.py --spec <path>` and
`bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-5`, and fix every finding they
name in this spec. The write grant is the spec file alone; do not commit.

### Acceptance

The pinned-facts check names no line of the spec, and both other commands exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve) · writing practice (records and units)

### Non-goals

No spec but this one. No product code. No change to any criterion.
