# dOrderedCharter — unit 5's builder return

**Serves:** journal PLAY-dOrderedCharter-5

Run wf_1f762b51-e68, summarized from its return.

- Built at rev-6 as pass commit `02a980cf4`.
- What the unit landed:
  - Ranked agent files: the charter blocks first inside the charter's level-0 envelope, then the role text, all inside the file's level-5
    envelope; with no playbook kit the render is unranked with one note, and an unreadable registry refuses by name.
  - Ranked handoffs: the role part at level 5, the task part's practices block first at level 0 and the rest at level 6.
  - The charter carried once: the `charter-blocks` slot left the work-order template, and the practices slot leads the task.
  - `handoff.py#check_envelope_order`, failing an unclosed envelope or a level that drops inside a part.
- Deviation 53: both work-order cases were already red from unit 27's `input:code` key, and both were re-pinned.
- Deviation 54: the dispatch verb refused the agent files beside their generator, so the main loop re-rendered the nine agent files after
  the pass, read the render check green and unit 3's envelope check at 31 covered, 1 held, 0 red, and committed them with these records.
- Unit 3's third criterion read no charter envelope in an agent file; this unit's ranked render now carries one by design.
- Observed by probe: AC1 to AC4 and both work-order cases by hand.
- Owed at the close: RED then GREEN for the ranked arms in the roles render selftest, which also cover the two new refusal sites; the
  section-7 legs; the tags leg.
