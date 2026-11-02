**Serves:** research TOOL-dTotalRecall-2

# Brief: the owner's pick on TOOL-dTotalRecall-2 §8 F6

## The prompt

> Fix the loose thread you mentioned

— owner, 2026-11-02, on the one fork the 2026-10-29 fork picks left open: TOOL-dWellOiledMachine-58
§8 F5, which follows this spec's §8 F6. The main loop reads it as the 2026-10-29 rule, "take the
recommendations on the forks", applied to F6 and the forks that wait on it; the push waits for the
owner's OK, so the pick can still be turned.

## The brief

### Goal

Mark TOOL-dTotalRecall-2 §8 F6 resolved by the owner to (a), its recommendation, and make the spec read
as F6 now decides. No design change beyond what the pick settles, and the one widening below.

### Items

- tr2 F6 (a): the ask to dPlacedRequest for one read-only holder verb over `read_claims`. Widened by
  one field: the verb prints a lease's `fleet-tag`, `session`, `lease`-mode class (`mine` or foreign)
  and `epoch`, because TOOL-dWellOiledMachine-6 §8 F4, resolved by the owner on 2026-10-29, asks
  dPlacedRequest for a read-only `epoch` verb over `read_claims` and names this one as the best home.
  One ask, filed once in dPlacedRequest's `BACKLOG.md` by this build's run (dTotalRecall builds before
  dWellOiledMachine), serves tr2 S2 and S9, TOOL-dWellOiledMachine-58 S4 (c) and S5,
  TOOL-dWellOiledMachine-41 S2's driver check and TOOL-dWellOiledMachine-6 S6 and S7. Write the ask's
  text into the fork as the row the build run files.
- Every sentence in tr2 that reads the holder verb as asked-but-unpicked, or a rung as waiting on the
  pick ("the pass builds no lease rung before the pick"), states the picked route where it stands.

One writer revises spec 2 only, `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-2.md`.
Write probe copies only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dtruenorth-4cb56e/bc821d4c-b305-40e3-bf2f-7dc1519c57f1/scratchpad/f6/tr/`.
Return: the rev the spec now reads; the fork resolved and its pick; the sections moved; its byte count.

In the spec:

- Bump the **Status:** line's `rev-6` to `rev-7`, dated 2026-11-02, the status kept `DEFERRED`.
- Mark the fork in place: `RESOLVED (owner, 2026-11-02): (a) <the pick in a few words>.` Drop "Open
  for the owner".
- Add one §9 line naming the fork resolved, this brief, and the sections moved.
- Stay under the class cap of 49152 bytes.

### Acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-7` dated 2026-11-02, and §9 holds the new line.
- `grep -n "Open for the owner" <spec>` prints no line of F6.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your spec staged into it through `GIT_INDEX_FILE`, names none of your specs. Findings that only a
  `gen_build_index.py --write` render cures belong to the main loop.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows.

### Non-goals

- No file outside spec 2. No commit, no stage into the real index, no deviation record, no
  `BACKLOG.md` row.
- No fork other than F6, and no other build's spec.
