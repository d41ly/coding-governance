**Serves:** journal TOOL-dTotalRecall-116
**Caused-by:** TOOL-dTotalRecall-116

# Brief — dTotalRecall: TOOL-dTotalRecall-116's first pass diverged, its spec folded as rev-2

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run, resumed on node a on 2026-11-24 by the owner's handoff.

## The brief

### Goal

Fold the divergence of `memory/builds/dTotalRecall/build/2026-11-25-build-TOOL-dTotalRecall-116-1-builder-return.md` into
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-116.md` as rev-2, with one revision-log line naming this
brief by its file stem, so the next pass builds it as written.

### Items

1. Read the return's Why whole and verify its observations over HEAD. §4's path lines and S3 cannot both hold: take the
   return's correction, the path an indexed blob stands at and, for an unindexed blob, the served path it was extracted
   at, and add the criterion that a probe of an id standing in two files reads each file's own path at that file's blob.
2. S2's wording takes the return's MINOR: the path history asked is the served view's, a moved record read at its old
   path's blob being refused, said so.
3. Decide `--literal-pathspecs` on the §4 git call, and say why.
4. Where a sibling spec of TOOL-dTotalRecall-117 to -121 states the same path rule, revise it too, its own rev bump and
   line; where none does, say so.
5. The checks of the spec brief's item 6 over each spec touched.

### Acceptance

The commands name no finding, and S3, §4 and the criteria state one path rule.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No scope beyond the divergence.

### Limitations

The write grant is that spec, and a sibling's under item 4. Do not commit. Run no gate leg.

### Reuse

The draft patch the return names, `TOOL-dTotalRecall-116-draft.patch` in the scratch directory.
