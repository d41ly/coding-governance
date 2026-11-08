# dCountedConsumers — unit 2's builder return and the drift legs

**Serves:** journal TOOL-dCountedConsumers-2

Run wf_f8805af3-37f, summarized from its result.

- Built as `dc4813c40`, with no divergence from the spec.
- `"help"` is now the last entry of `TRACE_GLOBS`, with two comment paragraphs: one says why it was added, the other why `PRODUCT_GLOBS` stays without it. The spec flipped to CLOSED in the same commit.
- Probe B, run before the change, matched the spec's pinned output: the signal read 2, naming TOOL-dCountedConsumers-1.
- After the change:
  - AC1: `help-in-trace yes help-in-product no`.
  - AC2: `pre with value 1 new none`.
  - AC3: `head with value 1 new none`.
  - AC4: `moved TOOL-dCountedConsumers-1 TOOL-dCountedConsumers-2`.
  - AC5: the only product hunks sit within lines 67-76.
  - AC6: the comment counts match.
- The main loop then ran both drift legs.
  - `python tools/drift-audit/drift_report.py --check` exited 0, reading `closed_specs_with_no_product_commit 1 · ok (baseline 1)` with no `new` line.
  - `python tools/drift-audit/selftest.py` exited 0, at 526 executed against a floor of 486.
