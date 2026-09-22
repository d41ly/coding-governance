**Serves:** journal DEPL-dGaugedVintage-8

# Acceptance ledger — DEPL-dGaugedVintage-8, the stamp guard

**Evidences:** DEPL-dGaugedVintage-8

- AC1 — `python tools/govkit/govkit.py update --write` — over a scratch target whose receipt carried
  one `evidence: "unattributed"` row, exit 0, `gov_commit` unchanged at `3e11f259`, and the run
  printed `The receipt is NOT re-stamped: 1 row(s) carry evidence: "unattributed" …` naming both the
  `adopt --re-adopt --write` remedy and the `--allow-ungraded` override.
- AC2 — `python tools/govkit/govkit.py update --write --allow-ungraded` — same fixture, exit 0,
  `gov_commit` advanced `3e11f259 -> b263d5b9`, and the closing line read
  `receipt re-stamped at b263d5b9 over 1 ungraded row(s), --allow-ungraded`.
- AC3 — `python tools/govkit/govkit.py update --write` — over a fixture whose single row was a
  well-formed `vintage-match` (real `gov_oid`, `commit` and `sha256`), exit 0, stamp advanced, and
  the output carried NO new line: byte-identical to the pre-guard message. The first attempt at this
  arm used a `vintage-match` row with no `gov_oid` and exited 2 on an unrelated provenance refusal —
  a malformed fixture, not a finding, and it is recorded here because a red that proves nothing is
  the thing this build keeps catching.
- AC4 — `python tools/govkit/govkit.py update` — read-only, exit 0, no stamp movement and no guard
  line, over both populations. The guard sits after the `if not write` return by construction.
- AC5 — RED OBSERVED. `git show HEAD:tools/govkit/govkit.py` written back into `tools/govkit/` (so
  `repo_root()` resolves) and run against the AC1 fixture: exit 0, `gov_commit` advanced
  `3e11f259 -> b263d5b9`, printing the ordinary `receipt re-stamped at b263d5b9` with no mention of
  the ungraded row. That is the defect, reproduced on the pre-fix binary. The first attempt ran the
  old binary from a temp directory and exited 2 on `no tools/govkit/registry.toml above …` — it
  proved nothing, and the arm was re-run from inside the tree.
- S3 — `python tools/govkit/selftest.py` — five permanent arms added beside the existing update
  block, all `ok`, and the suite closes `govkit-selftest: all arms held`. They reuse the file's own
  `stale_target()` fixture rather than a hand-built receipt.

## What this ledger does not claim

The guard is scoped to `_cmd_update`'s stamp. It does not re-attribute anything, and it does not
change which rows `update` writes bytes for. `adopt --write` is deliberately unguarded (§8 F2).
