**Serves:** research DEPL-dShippedRelease-1 DEPL-dShippedRelease-4

# Brief: dShippedRelease's spec 4 re-grounded against the parent specs revised by merge `362790f10`

## The prompt

> If a build has mismatches, write a re-ground brief in its `prompts/`. `gov-spec-writer` agents fold
> the brief, with rev bumps, §9 lines and deviation records as the 2026-10-28 re-grounds did.

— the dClosedLoop session's hand-off to this session, 2026-11-03, relaying the owner's ask for a full
cross-read of dMindYourWords, dShippedRelease, dScopedBuild and dTendedCadence.

## The brief

### Goal

Revise DEPL-dShippedRelease-4 so it cites TOOL-dWellOiledMachine-58 the way that spec reads on
origin/main at `66c5b8dbf`, after its rev-5 (commit `66f7b8d32`, merge `362790f10`). The spec keeps
its own design; only the one stale citation changes.

### Items

Read the cross-check record first,
`memory/builds/dShippedRelease/build/2026-11-03-build-DEPL-dShippedRelease-1-parents-crosscheck.md`.
It has one MISMATCH, its row 10. Group A's section 2 in
`memory/builds/dShippedRelease/build/2026-11-03-build-DEPL-dShippedRelease-1-crosscheck-returns.md`
quotes both sides and states the change. Re-read both sides before you edit. A row the parent's text
does not bear out is not edited: return it as refused, with the line that refutes it.

- **Row 10, §8 F5's line citation.** sr4:397-399 says wm58's "acceptance at `:288` asserts
  `not-closing-verb` for this name". Since wm58 rev-5 added three record rows and two lines to S4,
  wm58:288 is AC3's `not-holder` line, and the `not-closing-verb` assertion for `deploy.unlease` is
  AC4, at wm58:290-295 (the clause at :292-293). Replace `:288` with a section citation, AC4, so the
  next renumbering does not move it again. If any other `:<line>` citation of wm58 or wm6 in this spec
  points at a moved line, correct it the same way and name it in your return as writer-found.

Each revision:

- bumps the **Status:** line to `rev-5` and its date to `2026-11-03`, leaving every other field;
- adds one §9 line in the existing form: `- rev-5 · 2026-11-03 · §8 F5 · <what moved>, by the brief
  prompts/2026-11-03-prompt-DEPL-dShippedRelease-1-parents-reground.md`;
- re-opens no fork and resolves none; F5 stays `RESOLVED` as it is.

### Acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-5`, and §9 holds the new line.
- `grep -n ':288' <spec>` prints no line citing wm58.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your spec staged into it through `GIT_INDEX_FILE`, names nothing of your spec. Delete the copy
  after. Findings that only a `gen_build_index.py --write` render cures belong to the main loop:
  name them and leave them.

### Gates

Only the memory hygiene gate, as the role allows. The main loop runs the rest and renders the index.

### Non-goals

- No file outside DEPL-dShippedRelease-4's spec. No commit, no stage into the real index, no
  deviation record: the main loop writes those.
- No file of dWellOiledMachine, dTotalRecall or dPlacedRequest. A parent spec that looks wrong is a
  line in your return, not an edit.
- No change to what the unit builds.

### Reuse

The parents' specs as the interface; the cross-check record as the map of what moved.
`memory/builds/dWellOiledMachine/prompts/2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-reground.md`
as the precedent for a re-ground revision.
