# dOrderedCharter — unit 33's later-commit builder return

**Serves:** journal PLAY-dOrderedCharter-33

Run wf_1bb2160e-f88, summarized from its return.

- Built as pass commit `4dd011712`, the later commit spec 33's section 8 F5 deferred until a gov unit row was tracked, which
  PLAY-dOrderedCharter-40's pass `c91c26904` gave.
- What the pass landed:
  - The `unit` class row in `tools/govkit/surface-classes.toml`, its reader, plant and witness in `tools/playbook/pins.py`.
  - The `unit` `[[class]]` row in `tools/govkit/usage.toml`, usage shape `none`, with its `why`.
  - AC7 and AC11 lines in unit 33's acceptance ledger naming this pass.
  - Deviation 336: the unit plant removed nothing on a CRLF checkout, so the step gate read nothing vanished; it now matches the body in
    the file's own line endings and raises naming the tag when the body is absent.
- Observed by probe in scratch clones: the step gate lists the class's members, its plant reds with the fix and passed without it, and
  a plant with a change record naming no successor is witnessed.
- Found for other passes: unit 37's `unit-usage` plant carries the same CRLF defect, and `help/step-gate.md`'s class table lists none
  of the classes the build added; both were folded into unit 37's later-commit brief.
- Owed at the close: RED then GREEN for the `unit` class's plant; the step-gate and docs legs; the layers check and the core
  meta-check, which the builder role may not run.
