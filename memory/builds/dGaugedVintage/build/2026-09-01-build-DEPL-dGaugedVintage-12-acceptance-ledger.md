**Serves:** journal DEPL-dGaugedVintage-12

# Acceptance ledger — DEPL-dGaugedVintage-12, ratchet identity

**Evidences:** DEPL-dGaugedVintage-12

- AC1 — `bash tools/check-install-prefix.sh` — exchanging one `tools/gate-lint/ps-hygiene.py` for
  `tools/lexicon/lexicon.py` at an unchanged count of 3 now exits 1 and prints
  `SWAPPED tools/gate-lint/README.md 3: kits gate-lint -> gate-lint,lexicon`.
- AC2 — `bash tools/check-install-prefix.sh` — RED OBSERVED: the identical swap at HEAD before this
  unit exited 0. The count held and nothing looked.
- AC3 — `bash tools/check-install-prefix.sh` — exits 0 over the unchanged tree against the
  re-measured ledger.
- AC4 — `bash tools/check-install-prefix.sh` — adding a literal for a kit the file ALREADY names
  reports `ROSE tools/gate-lint/README.md 3 -> 4`, not `SWAPPED`, so the two verdicts stay
  distinguishable rather than one swallowing the other.
- AC5 — `bash tools/check-install-prefix.sh --write-ratchet` — reproduces the committed ledger
  byte-for-byte (`diff -q` identical), so the file cannot drift from the emitter.

## What this ledger does not claim

Arm 1's `RE` is untouched and keeps its per-line waiver granularity, deferred by
`DEPL-dGaugedVintage-7` §3. The kit set is built from a SORTED intermediate stream so the row is
deterministic; an unsorted join would churn the ledger between runs on an unchanged tree.
