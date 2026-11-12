# dOrderedCharter — unit 8's builder return

**Serves:** journal PLAY-dOrderedCharter-8

Run wf_0268c19b-53f, summarized from its return.

- Built as pass commit `06d9f5678`.
- What the unit landed:
  - The kickoff card engine writes the stored card into the session tree's ignored `.claude` card file in its level-1 envelope after
    every write, replay and append, adding the exclude line once, and a failure prints one `card-file — skipped:` line.
  - `tools/lib/envelope.sh`, the shell twin of the envelope helper, inlined in the card engine under a parity row and a byte-compare part.
  - The `doc.orientation-card` registry row, untracked: the envelope gate checks it where it exists, passes it absent, and fails it tracked.
  - The scratch guard's subagent context and the handoff's `## Card` block wrapped in the card's envelope.
  - `skills/session-kickoff/card-compaction.fixture.sh`, the live fixture for AC1.
- Deviations 82 (the charter re-render) and 83 (no line printed on a written card file).
- Observed by probe: AC2 to AC4 and AC8 to AC11 in scratch clones and by direct calls; AC1 only against a stub CLI.
- The main loop pinned the live fixture's four exit sites in `memory/project/unarmed-branches.txt`, since no suite can stage them offline.
- `AGENTS.md` measures 23279 bytes against its 23161 row.
- The python resolver leg's guard reads `tools/` and `.githooks/` but not `skills/`, so a parity copy in the card engine can drift unread.
- Owed at the close: AC1 live (two headless sessions and a compaction), which keeps unit 43's card import dark until green; RED then
  GREEN for the card-file arms, the scratch guard arms, the envelope parity row and part, and the three card plants; the tags leg; the
  envelope gate with and without a card file.
