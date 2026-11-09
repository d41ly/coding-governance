# dOrderedCharter — unit 32's builder return

**Serves:** journal PLAY-dOrderedCharter-32

Runs wf_3b4b7201-e91 and wf_e1ca3eb2-5ae, summarized from their returns.

- The first run handed back a divergence before any write: three seams the spec reused had not landed. Specs 32, 35 and 36 at rev-8
  resolved them, unit 32 landing the `fixed-by` resolver and the `instructions.exclude` reader, and the `policy.adopter.` tag form left to
  dDeclaredLoop.
- Built at rev-8 as pass commit `1da7d1846`.
- What the unit landed:
  - `tools/playbook/overlay.py`: the overlay and exclusion readers, the unit composition, the `fixed-by` resolver and derived classes, the
    overlay writer, and a `check` verb with one plant per acceptance case.
  - The charter render composes unit slots through the overlay, with a selftest arm running the overlay fixture.
  - `fixed-by` read on rows, and only a declared `open` class admitted.
  - The policy kit joins the overlay's policy rows to the catalogue's, and records the overlay among its legacy inputs.
  - `help/overlay.md` and the policy README.
- Observed by probe: AC1 to AC10 through the plants, the overlay check over gov's tree unarmed, and AC8's tag resolution in a scratch repo.
- The main loop regenerated the policy mirror the new legacy input staled, and read its check fresh.
- AC11 is the owner's edit: the deploy answers' comment above `kits` says every kit the repository carries, where it selects the kits gov
  installs and dogfoods.
- The comment above the unit row strings in `instruction_units.py` still omits `fixed-by`.
- Owed at the close: RED then GREEN for the render selftest arm and the overlay check with a planted open gov unit; the tags leg; the
  section-7 legs.
