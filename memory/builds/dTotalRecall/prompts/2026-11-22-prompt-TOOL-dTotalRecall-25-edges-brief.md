**Serves:** journal TOOL-dTotalRecall-25

# Brief — dTotalRecall: unit 25's edges to units 16 and 18, declared both ways

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 25's re-ground
(`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-25-reground-return.md`) found that unit 25
consumes from units 16 and 18, and neither spec declares a hands-off to it, so hygiene check 12 refused the edges.

## The brief

### Goal

Revise specs 16, 18 and 25 in place, each as a rev bump with one revision-log line naming this brief by its file stem,
so every edge between them is declared both ways.

### Items

1. `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-18.md` (DEFERRED, rev-6): add a
   `hands-off TOOL-dTotalRecall-25` bullet naming what unit 25 takes from it (the required columns and the `--layer`,
   `--lifecycle` and `--readers-none` flags of `record_kinds.py new`, as spec 25 rev-5's S1 reads them).
2. `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-16.md` (DEFERRED, rev-4): add a
   `hands-off TOOL-dTotalRecall-25` bullet naming what unit 25 takes from it (the `purpose` cell and `new`'s
   `--purpose`).
3. `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-25.md` (DEFERRED, rev-5): add the two matching
   `consumes-from` bullets, and delete the §3 non-goal text that stands in for them.
4. Change nothing else in any of the three.

Before returning, run `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec <path>` over each of the three
specs, `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-16 TOOL-dTotalRecall-18
TOOL-dTotalRecall-25` and `python tools/check-spec-tokens.py --spec <path>` over each, and fix every finding they name
in these three. The status headers keep their statuses; the write grant is the three spec files; do not commit.

### Acceptance

Every command exits 0 for the three specs; each carries its next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec but these three. No product code. No change to any criterion.
