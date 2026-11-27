**Serves:** journal TOOL-dTotalRecall-8

# Brief — dTotalRecall: TOOL-dTotalRecall-8 and -37 carried forward DEFERRED, not retired

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Retiring unit 8 `WONTDO` (its §8 F1 loss route) left
`cl-dClosedLoop-0219` and its owned nodes `record-kind.code` and `policy-key.memory.code-languages` with no live
carrier, and hygiene check 29 then refuses every INPROGRESS spec of the build; a node has no release line. The main
loop recorded `--rescope --act defer` for units 8 and 37 against owner ask TOOL-dTotalRecall-109 in
`memory/builds/dTotalRecall/BACKLOG.md`, and corrected
`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-8-deviation-83.md`.

## The brief

### Goal

Revise specs 8 and 37 in place, each as a rev bump with one revision-log line naming this brief by its file stem.

### Items

1. `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-8.md` (WONTDO, rev-7): set the status to
   `DEFERRED` with the header's `advances` naming TOOL-dTotalRecall-109 (keep `advances TOOL-dTotalRecall-27`
   beside it if the header grammar admits two, else name 109 alone), and drop the WONTDO reason segment. Keep the
   `**Carries:**` lines byte-identical. Keep §8 F1 and its loss line, and add one line saying the loss route's
   `WONTDO` was superseded by a deferral to ask TOOL-dTotalRecall-109 for the check-29 reason above. Every other
   rev-7 change stays.
2. `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-37.md` (WONTDO, rev-4): the same, deferred to
   TOOL-dTotalRecall-109, its §8 F4 kept with one line saying the retirement became a deferral beside unit 8's.
3. Change nothing else.

Before returning, run `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec <path>` over both,
`bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-8 TOOL-dTotalRecall-37` and
`python tools/check-spec-tokens.py --spec <path>` over both, and fix every finding they name in these two specs. The
write grant is the two spec files; do not commit.

### Acceptance

Every command exits 0 for both specs; each carries its next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec but these two. No product code. No new design for the code record.
