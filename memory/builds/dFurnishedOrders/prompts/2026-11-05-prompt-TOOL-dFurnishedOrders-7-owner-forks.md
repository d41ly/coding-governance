**Serves:** research TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-46

# Brief: the owner's picks on dFurnishedOrders's open forks

## The prompt

> resolve all forks with recommendations - record it

— owner, 2026-11-05, on the 47 forks the 2026-11-05 verification found open across the dClosedLoop
chain's landed specs; 5 of them are this build's, listed below. Every pick is the option
the fork's own text recommends.

## The brief

### Goal

Mark each fork below resolved by the owner to the option its own spec recommends, and make each spec
read as its fork now decides. No spec's design changes beyond what the pick settles.

### Items

- TOOL-dFurnishedOrders-7 §8 F9: (a), the option the fork itself recommends.
- TOOL-dFurnishedOrders-11 §8 F5: (a), the option the fork itself recommends.
- TOOL-dFurnishedOrders-14 §8 F8: (a), the option the fork itself recommends.
- TOOL-dFurnishedOrders-29 §8 F6: (a), the option the fork itself recommends.
- TOOL-dFurnishedOrders-46 §8 F7: (a), the option the fork itself recommends.

Where a pick names an ask another build's unit must answer, the spec states the ask as the one its
build run files in the target build's `BACKLOG.md`, with the ask's text as the fork gives it. Where a
pick names an act of the owner at a later boundary, the spec states that act as ruled, at that
boundary. One writer revises specs 7, 11, 14, 29, 46 of this build, the files:

- `memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-7.md`
- `memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-11.md`
- `memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-14.md`
- `memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-29.md`
- `memory/builds/dFurnishedOrders/spec/2026-10-27-spec-TOOL-dFurnishedOrders-46.md`

Write probe copies only under `C:/Users/d41ly/AppData/Local/Temp/claude/abaae6cd36b7dece/bc821d4c-b305-40e3-bf2f-7dc1519c57f1/scratchpad/forks/dFurnishedOrders/`, and delete nothing else there. Return, per spec: the
rev it now reads; each fork resolved and its pick; the sections moved; and its byte count.

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-11-05, the status kept `DEFERRED`.
- Mark each fork in place: `RESOLVED (owner, 2026-11-05): (<letter>) <the pick in a few words>.` Drop
  "Open for the owner" from that fork.
- Replace each sentence that points at the fork as open, or at a route as waiting on the owner's pick,
  with the picked route, where it stands.
- Add one §9 line naming the forks resolved, this brief, and the sections moved.
- Stay under the class cap of 49152 bytes; a spec already over it grows by no more than its fork marks.

### Acceptance

- `wc -c <spec>` is under 49152, or grew by no more than the fork marks where it was already over.
- The **Status:** line reads `rev-<N+1>` dated 2026-11-05, and §9 holds the new line.
- `grep -n "Open for the owner" <spec>` prints no line of a fork this brief names.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your specs staged into it through `GIT_INDEX_FILE`, names none of your specs. Findings that only a
  `gen_build_index.py --write` render cures belong to the main loop.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows.

### Non-goals

- No file outside the specs listed. No commit, no stage into the real index, no deviation record, no
  `BACKLOG.md` row.
- No fork other than those named, no fork already RESOLVED, and no other build's spec.
