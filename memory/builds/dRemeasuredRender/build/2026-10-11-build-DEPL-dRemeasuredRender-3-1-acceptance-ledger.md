# Acceptance ledger — DEPL-dRemeasuredRender-3

**Serves:** journal DEPL-dRemeasuredRender-3

Built on `0fa8463e`. The new arm ran through the scratch runner beside unit 2's block, once against
this tree's `govkit.py` and once against `bac1a4fb`'s, the tip the closing review read. Here both
assertions held. At `bac1a4fb` the row was re-stamped although the regenerate exited 3 without
touching the file, which is the review's HIGH (round 1, id 4) reproduced.

**Evidences:** DEPL-dRemeasuredRender-3
- AC1 — `stopped at accepted outcome` — the fixture regenerate exited 3 through a declared `ok = true` outcome `not-rendered-here`, the file kept its v1 bytes, the row equalled its pre-update record, and the run printed `receipt: KEPT [rendered] docs/out.md — its render stopped at accepted outcome 'not-rendered-here' without rendering`; red at bac1a4fb
- AC2 — `its render was refused` — unit 2's refused-render arm, whose regenerate exits 5 with no outcome accepting it, still printed that reason after this change
