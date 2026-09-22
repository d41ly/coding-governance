**Serves:** journal DEPL-dGaugedVintage-7

# Acceptance ledger — DEPL-dGaugedVintage-7, occurrence counting

**Evidences:** DEPL-dGaugedVintage-7

- AC1 — `bash tools/check-install-prefix.sh` — appending ONE line carrying two shipping-prefix
  literals to `tools/gate-lint/README.md` now reports `ROSE tools/gate-lint/README.md 3 -> 5`.
- AC2 — amended rev-3 — NOT MET. S3's identity arm was not built, so a kit path swapped for
  another's at equal occurrence count still passes. Recorded as a surviving hole, and §8 F1 is the
  follow-up.
- AC3 — `bash tools/check-install-prefix.sh` — exits 0 over the unchanged tree against the
  re-measured ledger.
- AC4 — amended rev-3 — RED OBSERVED for the line-counting blind spot only: the same fixture moved
  the count `3 -> 4` under `grep -c`, where two occurrences require `3 -> 5`. The swap case was not
  staged because the arm that would catch it was not built.
- AC5 — `bash tools/check-install-prefix.sh --write-ratchet` — reproduces the committed ledger
  byte-for-byte (`diff -q` reports identical), so the file cannot drift from the counting that
  produced it.
- S2 — `git diff --numstat tools/install-prefix-carried.txt` — 12 of 108 rows moved under the new
  counting, landed in the same change as S1 so the ratchet is never red in between.

## What this ledger does not claim

Half the unit. The line-counting blind spot is closed; the IDENTITY one is not, and a swapped kit
path at equal count remains invisible. Arm 1's `RE` is untouched and keeps its per-line waiver
granularity, deferred in §3 with its reason.
