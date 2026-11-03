**Serves:** research TOOL-dCalibratedLens-20

# Brief: unit 20's §3 gains the two hands-off edges units 5 and 19 now consume

## The prompt

> go with (b) for row 9, rest with recommendations

— the owner, 2026-11-03. The disposal of the cross-check folds' spec audit, item M6, gave units 5
and 19 a `consumes-from` edge on `TOOL-dCalibratedLens-20`. Hygiene check 12 now reds because unit 20
declares no matching `hands-off` edge back.

## The brief

### Goal

Add to `TOOL-dCalibratedLens-20`'s §3 Edges the two `hands-off` edges that pair with the
`consumes-from` edges units 5 and 19 declare. After the edit, hygiene check 12 names neither pair.

### Items

- Read unit 5's and unit 19's §3 `consumes-from` `TOOL-dCalibratedLens-20` lines. They are the
  disposal of item M6 in
  `memory/builds/dCalibratedLens/reviews/2026-11-04-review-TOOL-dCalibratedLens-1-crosscheck-spec-audit.md`.
- Add one **hands-off** `TOOL-dCalibratedLens-5` line and one **hands-off** `TOOL-dCalibratedLens-19`
  line to unit 20's §3 Edges, in the form its existing edges take. Each says what unit 20 hands over:
  the `**Serves:**` binding of the keep record (unit 5) and of the three-homes plant's records
  (unit 19). Spell it as the two consuming lines spell it.
- Bump the **Status:** line by one rev, with date `2026-11-04`.
- Add one §9 line in the spec's existing form: `- rev-<n> · 2026-11-04 · §3 · the hands-off edges to
  units 5 and 19 that pair the edges the audit disposal gave them, by the brief
  prompts/2026-11-04-prompt-TOOL-dCalibratedLens-20-edge-join.md`.

Return, in this shape and nothing else:

1. The two lines added, verbatim.
2. The spec's new rev and byte count.
3. The hygiene run's command and what it printed for check 12.

### Acceptance

- `bash tools/memory-tree/check-memory-hygiene.sh` names neither unit 5's nor unit 19's
  `consumes-from` `TOOL-dCalibratedLens-20` under check 12. Run it over a copy of the index with unit
  20's spec staged into it through `GIT_INDEX_FILE`, and delete the copy after.

### Gates

Only the memory hygiene gate. The main loop renders the index.

### Non-goals

- No file other than unit 20's spec. No commit, no stage into the real index, no deviation record.
- No change to unit 20 beyond the two edges, the rev bump and the §9 line.
