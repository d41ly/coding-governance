# dOrderedCharter — unit 41's builder return

**Serves:** journal PLAY-dOrderedCharter-41

Run wf_49a2f8e7-6aa, summarized from its return.

- Built at rev-6 as pass commit `4a8349f9c`.
- What the unit landed:
  - The rule comment above `TEMPLATE_MAJOR` and a `help/charter.md` paragraph: a template a major behind gets the reseed note, one at the engine's major gets none.
  - A selftest arm in `run_selftest` rendering gov's template and a seeded v4.4 template, each with and without the `cross-os` drop, in scratch repositories committed on `main`.
  - The wiring guide's paragraph and its `when:cross-os` bullet.
- Observed by probe: AC1 to AC6, and the new arm cut out and run alone, green on the shipped row and red on a legacy mark.
- No divergence.
- Owed at the close: RED then GREEN for the new arm, the section-7 legs, and the tags leg.
