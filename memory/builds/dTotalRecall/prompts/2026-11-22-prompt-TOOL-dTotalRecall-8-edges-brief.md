**Serves:** journal TOOL-dTotalRecall-8

# Brief — dTotalRecall: unit 8's docs-ledger drain and unit 18's hands-off edge to unit 16

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 16's re-ground
(`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-16-reground-return.md`) found two gaps in
sibling specs it could not edit.

## The brief

### Goal

Revise both specs in place, each as a rev bump with one revision-log line naming this brief by its file stem.

### Items

1. `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-8.md` (DEFERRED, rev-5): its S10 fills the
   `memory.code-languages` catalogue row, which re-renders `help/reference/policy.md`; the `docs` leg then reads the
   `policy:memory.code-languages` row of `memory/project/docs-undocumented.txt` as drained and reds until it is
   removed. Add the drain to S10, add `memory/project/docs-undocumented.txt` and `help/reference/policy.md` to Files
   touched, and add a criterion observing the row gone, as unit 16 rev-3's AC7 does for `memory.map-purpose` (read it
   for the shape). Confirm the row exists at HEAD before writing the claim.
2. `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-18.md` (DEFERRED, rev-5): unit 16 rev-3 consumes
   from unit 18 (the `--layer`, `--lifecycle` and `--readers-none` flags of `record_kinds.py new`), and hygiene check 12
   refuses its `consumes-from TOOL-dTotalRecall-18` edge while spec 18 declares no `hands-off TOOL-dTotalRecall-16`.
   Add that hands-off bullet to spec 18's edges, naming what unit 16 takes. Change nothing else in spec 18.
3. Keep every other claim of both specs as it stands.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-8
TOOL-dTotalRecall-18` and `python tools/check-spec-tokens.py --spec <path>` over each spec, and fix every finding they
name in these two specs. The status headers keep their statuses; the write grant is the two spec files; do not
commit.

### Acceptance

Both commands exit 0 for both specs; each carries its next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec but these two. No product code. No change to any other criterion.
