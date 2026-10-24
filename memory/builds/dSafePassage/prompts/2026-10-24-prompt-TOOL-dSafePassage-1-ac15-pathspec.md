**Serves:** research TOOL-dSafePassage-1

# Brief: TOOL-dSafePassage-1's AC15 can never pass, because its grep finds the step's own files

## The prompt

> Do this task here: “dSafePassage: fix spec 1 AC15 and stale Carries pins”

— owner, 2026-10-24, in the session that landed the re-ground at 1769e08cc. The stale-pins half needs no
edit. `python tools/check-spec-tokens.py`, the bar's carries join, reads each clause's hash in the
as-built view and finds 0 stale pins. The bootstrap instrument
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py` hashes v2's baseline
text instead, and re-pinning to it reds the bar. That is what
`2026-10-23-prompt-TOOL-dSafePassage-1-carries-repin.md` undid.

## The brief

### Goal

Make AC15 of `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-1.md` passable on a
correct build and still red on a reader S8 failed to dispose of.

### Items

1. AC15 runs `git grep -l -F 'template-size-limits' -- ':!memory/builds' ':!memory/ledger'
   ':!memory/backlog'`. On a correct build it always prints the step's own files:
   - `tools/govkit/steps.toml`, whose row's `id` (`govkit/template-size-limits-to-budgets`) and
     `surfaces` (`file:{prefix}/template-size-limits.txt`) spell the name;
   - the step program `tools/govkit/steps/template_size_limits.py`, which must name the file it
     migrates.
2. Exclude exactly those two paths from AC15's grep, and no others. Say in the criterion why each is
   excluded: they are the step itself, and any path the step does not own is still a red. If another
   file this unit writes must spell the name on a correct build, exclude it the same way, with its
   reason. If you find none, say so in your return.
3. Keep S7's by-name readers paragraph consistent with the criterion, but only where it states the
   same grep.

### Acceptance

- AC15's grep carries the two exclusions, each with its reason.
- **Status:** reads `rev-8`, dated 2026-10-24, still `DEFERRED`, and §9 holds one line naming AC15 and
  this brief.
- `wc -c` of the spec stays under 48900, which leaves room for the records rows the index render
  adds. Trim wording elsewhere in the same criterion if you must.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only the
  spec staged through `GIT_INDEX_FILE`, names it only for findings a `gen_build_index.py --write`
  render cures. Delete the copy after.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows.

### Non-goals

- No other criterion, section or spec. Re-pin no **Carries:** line. Leave fork F12 open.
- No commit, no stage into the real index, no deviation record: the main loop writes those.
