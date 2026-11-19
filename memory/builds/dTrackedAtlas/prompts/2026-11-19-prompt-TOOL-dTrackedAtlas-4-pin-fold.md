# Revision — dTrackedAtlas: TOOL-dTrackedAtlas-4 rev-5 pins its two new figures

**Serves:** research TOOL-dTrackedAtlas-4

## The prompt

> The pass legs after `d8aaf6bff` red the writing-practice leg on two figures spec 4's rev-5 added without a pin.

## The brief

### Goal
`memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-4.md` rev-5 types `149 bytes` and `925 bytes` before a unit word with no pin on their lines, and the `pinned-facts` arm of `writing practice (records and units)` reds both. Pin each on its line.

### Items
1. Put PINNED on the line of each measured figure, or DERIVED where it is computed from another source, or move the figure into a code span that opens and closes on its line.
2. Bump the rev and add one revision-log line naming this record; no other change.

### Acceptance
No line of the spec holds a figure before a unit word without a pin outside a code span; `check-memory-hygiene.sh --only 12 --spec <path>` and `check-spec-tokens.py --spec <path>` are clean; `bash tools/unattended/unattended.sh --check-specs dTrackedAtlas TOOL-dTrackedAtlas-4` prints no refusal.

### Gates
The spec-format and spec-token checks the role allows; no other gate.

### Non-goals
No design change, no status change (the spec stays DEFERRED), no product code, no commit and no index render.
