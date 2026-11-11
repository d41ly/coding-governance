**Serves:** research TOOL-dScopedBuild-1

# Brief: dScopedBuild's spec 1 re-grounded against its parents' specs

## The prompt

> If a build has mismatches, write a re-ground brief in its `prompts/`. `gov-spec-writer` agents fold
> the brief, with rev bumps, §9 lines and deviation records as the 2026-10-28 re-grounds did.

— the dClosedLoop session's hand-off to this session, 2026-11-03, relaying the owner's ask for a full
cross-read of dMindYourWords, dShippedRelease, dScopedBuild and dTendedCadence.

## The brief

### Goal

Revise TOOL-dScopedBuild-1 so its §3 non-goal names the owner of the `build.exit` transition record
the way the parents' specs spell it on origin/main at `66c5b8dbf`. The spec keeps its own design;
only the one mis-attributed owner changes.

### Items

Read the cross-check record first,
`memory/builds/dScopedBuild/build/2026-11-03-build-TOOL-dScopedBuild-1-parents-crosscheck.md`. It has
one MISMATCH, its row 1. Section 2 of the return in
`memory/builds/dScopedBuild/build/2026-11-03-build-TOOL-dScopedBuild-1-crosscheck-returns.md` quotes
both sides and states the change. Re-read both sides before you edit. A row the parent's text does not
bear out is not edited: return it as refused, with the line that refutes it.

- **Row 1, the transition record's owner.** sb1:108 says "A file-backed transition record for
  `build.exit`: the executor's (TOOL-dWellOiledMachine-6)." TOOL-dWellOiledMachine-6 names no
  transition record (`grep -ci transition` on it prints 0); its item witness is a `reconcile` row's
  landed effect (wm6:118-119). The writer is TOOL-dDeclaredLoop-3 S5's `write_transition` (dl3:60),
  which dWellOiledMachine's units reach by subprocess through the loop kit's verb `python
  loop_transition.py record` (wm3:60). Re-point the non-goal's owner to TOOL-dDeclaredLoop-3's
  writer, reached through that verb by the `build.exit` command item, and drop the wm6 attribution.
  Keep the bullet a non-goal. If §3's Edges name wm6 for the record too, correct that edge the same
  way.

Each revision:

- bumps the **Status:** line to `rev-4` and its date to `2026-11-03`, leaving every other field;
- adds one §9 line in the existing form: `- rev-4 · 2026-11-03 · §3 · <what moved>, by the brief
  prompts/2026-11-03-prompt-TOOL-dScopedBuild-1-parents-reground.md`;
- re-opens no fork and resolves none.

### Acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-4`, and §9 holds the new line.
- `grep -n "the executor's (TOOL-dWellOiledMachine-6)" <spec>` prints nothing.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your spec staged into it through `GIT_INDEX_FILE`, names nothing of your spec. Delete the copy
  after. Findings that only a `gen_build_index.py --write` render cures belong to the main loop:
  name them and leave them.

### Gates

Only the memory hygiene gate, as the role allows. The main loop runs the rest and renders the index.

### Non-goals

- No file outside TOOL-dScopedBuild-1's spec. No commit, no stage into the real index, no deviation
  record: the main loop writes those.
- No file of dWellOiledMachine or dDeclaredLoop. A parent spec that looks wrong is a line in your
  return, not an edit.
- No change to what the unit builds.

### Reuse

The parents' specs as the interface; the cross-check record as the map of what moved.
`memory/builds/dWellOiledMachine/prompts/2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-reground.md`
as the precedent for a re-ground revision.
