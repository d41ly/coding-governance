**Serves:** research TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-58

# Brief: the owner's pick on TOOL-dWellOiledMachine-58 §8 F5, through TOOL-dTotalRecall-2 §8 F6

## The prompt

> Fix the loose thread you mentioned

— owner, 2026-11-02, on the one fork the 2026-10-29 fork picks left open: TOOL-dWellOiledMachine-58
§8 F5, which follows TOOL-dTotalRecall-2 §8 F6. The main loop reads it as the 2026-10-29 rule, "take
the recommendations on the forks", applied to F6 and the forks that wait on it; the push waits for the
owner's OK, so the pick can still be turned.

## The brief

### Goal

Mark TOOL-dWellOiledMachine-58 §8 F5 resolved by the owner through TOOL-dTotalRecall-2 §8 F6's pick,
and make units 6, 41 and 58 read the picked route wherever they wait on it. No design change beyond
what the pick settles.

### Items

- The pick, written into TOOL-dTotalRecall-2 §8 F6 by its own writer in the same pass: (a), one
  read-only holder verb over `read_claims` asked of dPlacedRequest, printing a lease's `fleet-tag`,
  `session`, `lease`-mode class (`mine` or foreign) and `epoch`. dTotalRecall's build run files the one
  ask in dPlacedRequest's `BACKLOG.md`; this build files no row for it.
- wm58 F5: `RESOLVED (owner, 2026-11-02): TOOL-dTotalRecall-2 §8 F6 (a), the holder verb; S4 (c) and S5
  read the holder through it.` Drop "Open for the owner, through F6" and "waits on F6's pick"; S2 (the
  live-lease sentence at about line 76) states the picked route.
- wm41: S2's driver check, and the sentences at about lines 51, 168, 232 and 238, read the lease holder
  through that holder verb as picked, not as open or awaited.
- wm6 F4: already resolved (owner, 2026-10-29) to an ask for a read-only `epoch` verb, naming F6's
  holder verb as its best home. State that the holder verb now prints `epoch`, so the one ask serves
  F4 and this build files no separate epoch row; S6 and S7 read the epoch through it.

One writer revises specs 6, 41 and 58, the files
`memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-<n>.md`. Write probe
copies only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dtruenorth-4cb56e/bc821d4c-b305-40e3-bf2f-7dc1519c57f1/scratchpad/f6/wm/`.
Return, per spec: the rev it now reads; the fork resolved or the sentences moved; the sections moved;
its byte count.

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-11-02, the status kept `DEFERRED`.
- Mark F5 in place as above. Leave wm6 F4's existing RESOLVED mark and add the one sentence.
- Add one §9 line naming the fork or sentences moved, this brief, and the sections moved.
- Stay under the class cap of 49152 bytes.

### Acceptance

- `wc -c <spec>` is under 49152.
- Each **Status:** line moved one rev, dated 2026-11-02, and §9 holds the new line.
- `grep -n "Open for the owner" <spec 58>` prints no line of F5, and
  `grep -nE "F6's (open|pick)|waits on (TOOL-dTotalRecall-2 §8 )?F6" <spec>` prints nothing in 6, 41 or 58.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your specs staged into it through `GIT_INDEX_FILE`, names none of your specs. Findings that only a
  `gen_build_index.py --write` render cures belong to the main loop.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows.

### Non-goals

- No file outside specs 6, 41 and 58. No commit, no stage into the real index, no deviation record,
  no `BACKLOG.md` row.
- No fork other than those named, and no other build's spec.
