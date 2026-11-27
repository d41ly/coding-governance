**Serves:** journal TOOL-dTotalRecall-16

# Brief — dTotalRecall: unit 16 declares its consumes-from edge to unit 18

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Spec 18 rev-6 now declares `hands-off TOOL-dTotalRecall-16` (S10's
`--layer`, `--lifecycle` and `--readers-none` flags of `record_kinds.py new`, S2's view columns and S11's pipe escape,
which unit 16's S8 reads), and hygiene check 12 refuses it while spec 16 declares no matching edge back.

## The brief

### Goal

Revise `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-16.md` in place as a rev-4 bump, with one
revision-log line naming this brief by its file stem.

### Items

1. Add a `- **consumes-from** `TOOL-dTotalRecall-18`` bullet to the spec's edges naming what it takes, matching spec
   18 rev-6's hands-off bullet to this unit (read it), and delete the §3 sentence saying spec 18 declares no
   hands-off to this unit, so no edge is declared.
2. Change nothing else.

Before returning, run `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec <spec 16 path>` and the same
over spec 18's path, `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-16
TOOL-dTotalRecall-18` and `python tools/check-spec-tokens.py --spec <path>` over spec 16, and fix every finding they
name in spec 16. The status header keeps `DEFERRED`; the write grant is spec 16 alone; do not commit.

### Acceptance

All four commands exit 0; spec 16 carries rev-4 and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec but spec 16. No product code. No change to any criterion.
