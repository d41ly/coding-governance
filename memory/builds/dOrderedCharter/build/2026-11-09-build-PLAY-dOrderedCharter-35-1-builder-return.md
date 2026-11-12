# dOrderedCharter — unit 35's builder return

**Serves:** journal PLAY-dOrderedCharter-35

Runs wf_ce437813-e35 and wf_087fa988-524, summarized from their returns.

- The first run handed back a divergence before any write: the naming lexicon refused the composer's names, and four gaps sat beside it.
  Spec 35 rev-9 renamed the composer `derive_row_composition` and `set_row_patch` across this build's specs and closed the gaps.
- Built at rev-9 as pass commit `8c8cd7bf6`, with the policy mirror regenerated in `43a54f6a2`.
- What the unit landed:
  - `tools/playbook/overlay_rows.py`: the overlay's row reader, the shared kind-schema reader, the adopter-seat check, the composer and
    its patch, and the canonical form.
  - `tools/playbook/fixtures/row_kind.py`, one plant per acceptance case, and a render selftest block running it.
  - The overlay record's `tables` field, filled from the one parse its reader already makes.
  - `help/overlay-rows.md`, and the `instructions.exclude` catalogue row's summary and usage.
- Decided in the pass: the canonical form leaves out origin and source; an exclusion is refused only for a tag in the kind's namespace no
  gov row holds; a rename record is marked editorial.
- Observed by probe: every plant against AC1 to AC11 and AC13, the selftest block alone, and four plants red with a function stubbed
  broken; AC12's catalogue probe.
- Refusal sites with no arm asserting their text, in the schema reader, the row reader and the composer, are listed in the run's return.
- The overlay module's docstring still lists only unit and policy rows; refused for edit once the spec was CLOSED.
- AC14's pathspec is unit 49's to correct.
- Owed at the close: RED then GREEN for the row-kind block; the tags leg; the section-7 legs.
