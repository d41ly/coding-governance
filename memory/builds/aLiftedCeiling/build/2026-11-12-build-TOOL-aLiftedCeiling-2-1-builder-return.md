# aLiftedCeiling — unit 2's builder return

**Serves:** journal TOOL-aLiftedCeiling-2

Run wf_a7b3b17f-d8e, summarized from its return.

- What landed: pass commit `aeb5e0a6b`. The run-gates kit rewrote the instruction-edits leg's evidence row in one reset-and-observe
  call inside a fresh clone of HEAD, its value unchanged and its source now naming the host load and the commit its race ran at; the
  generated file was copied back.
- One deviation, on a `Decided:` trailer: the index generator also added the new ledger's row to the spec's own records table.
- Probes it ran, none a gate: the row's grep and the evidence file's diff against the build's base and against the spec's base.
- The ceiling check was the main loop's, since the role hook refuses it to a builder.
