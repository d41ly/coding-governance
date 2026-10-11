# Acceptance ledger — DEPL-dRemeasuredRender-2

**Serves:** journal DEPL-dRemeasuredRender-2

Built on `473d2bbc`. The two new arms ran through the same scratch runner as unit 2, beside the
`[aHI-1]` block they share a generator with, once against this tree's `govkit.py` and once against
base `17472e21`'s. Here every assertion held, `[aHI-1 S3]`'s `is undischarged (probe exit 3)` line
included: it is now printed by the re-probe. At base the `hp` fixture printed
`HOLE demo: 'demo-hole' is undischarged (probe exit 1)` for a hole its own render then discharged,
which is the false red this unit closes, and neither fixture printed the early-line wording.

**Evidences:** DEPL-dRemeasuredRender-2
- AC1 — `is discharged after the render` — over the `hp` fixture, whose probe greps the rendered file for `v2`, the run printed `probes undischarged before the render` and `is discharged after the render; the early verdict does not stand`, and no `is undischarged` line; red at 17472e21, which printed `is undischarged (probe exit 1)`
- AC2 — `is undischarged (probe exit` — over the `hf` fixture, whose probe exits 3, that line printed after the early line and no discharged line printed; red at 17472e21, which printed no early line
