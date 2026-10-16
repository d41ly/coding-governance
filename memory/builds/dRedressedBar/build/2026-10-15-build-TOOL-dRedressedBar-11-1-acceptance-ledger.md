# TOOL-dRedressedBar-11 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-11

Written by TOOL-dRedressedBar-27 on 2026-10-15, after the unit closed with no ledger, from what its
builder recorded. Nothing was re-run for it. The unit was built against spec 11 rev-3 in the one
pass commit `b65688cde`. Spec 11's rev-4, rev-5 and rev-6 are records fixes that move no criterion
text, so the readings answer the criteria as they stand. The readings are the builder's, from that
commit's body and from its return in `2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`,
under the heading `2026-10-14T18:29:21 · gov-builder · wf_551a7d53-a85/aabed9b0e2ce4380b` at line
5180. The builder ran the `<p10>` halves over unit 10's block at `07feb3b38`. No merge bar, no
self-test suite and no gate leg ran in the build pass, and the section 7 legs were owed to the
close.

**Evidences:** TOOL-dRedressedBar-11
- AC1 — `must_not_resolve` — the descriptor's code-2 block read back with all five parts, and
  `("must_exist", True)` no longer appears in `tools/govkit/govkit.py`. The grep for
  `must_not_resolve` printed the `OUTCOME_PROBE_KEYS` line and the docstring, plus a third line,
  the `if key != "must_not_resolve"` branch the evaluation needs; the builder noted that AC1's red
  condition does not cover that line.
- AC2 — `refusing to wire` — an in-process program got the expected verdict in all seven states.
  The adopter's stderr carried `cannot read` in the receipt row and `refusing to wire` with no
  receipt. The same program over unit 10's block, from `git show 07feb3b38`, read ACCEPTED on the
  receipt row, the red half.
- AC3 — `govkit: kit 'settings-merge'` — on fixture A, by the CLI under `%TEMP%`, the second apply
  exited 1 with exactly one such line, carrying `cannot read` and `settings.json`, and no
  `no-agent-cap-to-wire` anywhere. Over a clone at `07feb3b38`, fixture A exited 0 with
  `[accepted stop]`.
- AC4 — `gov_commit` — on fixture B, `update --write` exited 1, printed the same single line, and
  `gov_commit` stayed at `24f39915`. Over the `07feb3b38` clone it exited 0, re-stamped the receipt
  and printed the accepted line. Spec 11's rev-5 records that the criterion's "Before the commit"
  was inexact and that `TOOL-dRedressedBar-13`'s AC15 observed its corrected form.
- AC5 — `[accepted stop]` — fixture A-absent exited 0 and printed it. The record names no re-run
  of unit 9's AC2 program at the tip.
- AC6 — `must_not_resolves` — with `check` replaced by a recorder, every label read true: 19
  key-rule labels (18 blocks plus unit 9's), the liveness label, exactly the two `lexicon ` labels,
  and six settings-merge rows. With `must_not_resolve` renamed to `must_not_resolves`, exactly two
  labels went false: the settings-merge key-rule label and the receipt-only row. Spec 11's rev-5
  records the halves of this criterion that `TOOL-dRedressedBar-13`'s AC7 and AC9 observed in
  their corrected form.
- AC7 — `scan_text_io` — `git diff 07feb3b38 b65688cd -- tools/govkit/` changed no `def` or
  `class` line. `scan_text_io` counted 36 subprocess sites in `govkit.py`, none in `matrix.py`, and
  24 subprocess plus 1 file-io in `selftest.py`, matching the registry.
