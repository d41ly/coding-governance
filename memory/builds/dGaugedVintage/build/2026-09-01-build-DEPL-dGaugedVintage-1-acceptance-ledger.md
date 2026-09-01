**Serves:** journal DEPL-dGaugedVintage-1

# Acceptance ledger — DEPL-dGaugedVintage-1, the shipping assertion

**Evidences:** DEPL-dGaugedVintage-1

- AC1 — `python tools/govkit/govkit.py selfcheck` — exits 0 at HEAD. Every versioned entry lands
  the file its `version_from` names, which §4 predicted by measurement before the arm was written.
- AC2 — `python tools/govkit/govkit.py selfcheck` — with `check-wiring.sh` removed from its own
  `[[files]]` include on a staged fixture, the run reds naming both the entry and the path:
  `declares its version constant in 'tools/check-wiring.sh', which its own [[files]] rules do not
  land`.
- AC3 — `tools/govkit/govkit.py` — the ten `version_from.none` entries never reach the arm: check 5
  `continue`s on the `none` branch several lines above it, so the arm has no opinion about them.
- AC4 — `python tools/govkit/govkit.py selfcheck` — RED OBSERVED, which is the whole point: the arm
  is GREEN over today's tree, so without a staged break it would be an assertion about nothing. The
  break was restored from a file copy rather than `git checkout --`, which had already reverted an
  unstaged change once in this build.

## What this ledger does not claim

The arm asks whether the constant's file is LANDED, not whether the constant is readable once it
lands — that is `DEPL-dGaugedVintage-5`'s marker. Sentinel paths are out of scope per §8 F1, and the
seven entries declaring one were not measured.
