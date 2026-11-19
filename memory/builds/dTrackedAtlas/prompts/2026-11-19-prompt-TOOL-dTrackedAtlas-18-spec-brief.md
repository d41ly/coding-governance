**Serves:** research TOOL-dTrackedAtlas-18

# Spec brief — TOOL-dTrackedAtlas-18: re-pin the schedule instrument, packets and door

You author the spec of `TOOL-dTrackedAtlas-18` and write no product code. The owner, 2026-11-19: "Rewrite the branch
to drop the four Red-fix trailers, re-pin the schedule, approve unit 4's loop.toml row then land it". This unit is
the re-pin; it closes ask `TOOL-dTrackedAtlas-6` in `memory/builds/dTrackedAtlas/BACKLOG.md`. Read first, whole:
the build README, that ask, the CLOSED spec of `TOOL-dTrackedAtlas-1` (its fork F2 is why the pin moved),
`memory/TEMPLATE-SPEC.md`, and `memory/guides/BUILD-METHOD.md` at
`doc.build-method#m2-the-spec-set-decompose-detect-classify-act`.

## The unit

- **The packets.** `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py` `--repin` sets the
  schedule instrument's pin to its blob at HEAD in every chain build's packet and re-renders each. Read `cmd_repin`
  and its guard: it admits any caller when no chain run is live at the tree it reads, and only an owner at a console
  otherwise. State which holds at this branch, and what the builder does if the guard refuses.
- **The door.** `tools/chain-packet.py` pins the schedule at `INSTRUMENT_BLOBS["schedule"]` with reliance points:
  the door rebinds `schedule.git` to answer the two git calls `tree_state` made per build. Unit 1 moved those reads
  into `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py`, so re-read every
  reliance point against the schedule as it stands, say which still hold, and specify what the door changes so its
  answer stays byte-identical to the instrument's, or that it falls back to the instrument where it can no longer
  answer. Then re-pin the constant.
- Acceptance: `packet.py --check <slug>` green on every chain build's packet (its pin arm included); a direct run of
  the door against the instrument on one build, compared byte for byte; each red observed first on the current
  tree. No gate, suite or bar: the `chain-packet self-test` leg is held and runs only under `GATE_SELFTESTS`, which
  this run leaves unset.

## Constraints

- A shipped kit edit (`tools/chain-packet.py`), so tier it as the kickoff engine assigns one; status header `order 11`.
- Every new function name leads with a verb `.lexicon.conf` declares; every figure typed before a unit word carries a
  pin on its line or sits in a code span on that line; every citation is `<repository path>#<symbol>` or blob-pinned.
- The packets live in other chain builds' `prompts/` folders; the re-pin verb is the one door that writes them.
  dWitnessedBar and dPlacedRequest hold live run claims on their own branches; say what the re-pin means for them.
