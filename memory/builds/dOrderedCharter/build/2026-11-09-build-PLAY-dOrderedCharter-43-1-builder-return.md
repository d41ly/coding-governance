# dOrderedCharter — unit 43's builder return

**Serves:** journal PLAY-dOrderedCharter-43

Run wf_04afe0c0-018, summarized from its return.

- Built at rev-4 as pass commit `37bbf6d36`, with S1, S2, S3 and S5.
- What the unit landed:
  - The charter renderer's `--card` switch, off by default: in pointer mode the entry-files scope writes `CLAUDE.md` with the card import
    as its second line and a new `.gemini/settings.json` listing both files; a one-line pointer is rewritten without `--force`.
  - `check_card_import` under `--check-render --card`, failing a pointer without the import and printing a `card — not delivered:` line
    for each alias with no native import and for Codex.
  - The agent-instructions adopter passes `--card` through and holds no card logic.
- S4 is held by the spec's own rollout: `--card` on gov's two render legs and gov's `CLAUDE.md` second line land only once unit 8's live
  compaction fixture is recorded green, which it is not. AC5 and AC7 are owed with it.
- Observed by probe: AC1 to AC4 and AC6 over committed scratch repositories.
- The packet's instrument pins were not checked in the pass: its probe hit its bound.
- Owed at the close: S4 with AC5 and AC7 after unit 8's live fixture; RED then GREEN for the scope arms and the adopter's thirteenth arm;
  the tags leg.
