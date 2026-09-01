**Serves:** journal DEPL-dGaugedVintage-6

# Acceptance ledger — DEPL-dGaugedVintage-6, the install block

**Evidences:** DEPL-dGaugedVintage-6

- AC1 — followed the block literally in a scratch dir: `mkdir -p <t>/tools` then
  `cp -r <gov>/tools/drift-audit <t>/tools/drift-audit`, and line 3's
  `tools/drift-audit/adopt-drift-audit.sh` RESOLVES. The old block was run for contrast in the same
  scratch dir and its tree does not carry that path at all, which is the defect reproduced.
- AC2 — `bash tools/check-install-prefix.sh` exits 0 and the carried-ledger row
  `tools/drift-audit/README.md` is unchanged at 3. The repair adds no shipping-prefix literal:
  `<target-repo>/tools/drift-audit` names a directory, and `re_ship` matches only a path ending in a
  file with an extension.
- AC3 — S2's sweep ran over every `tools/*/README.md`. Exactly ONE carries a `cp -r` install line,
  `tools/drift-audit/README.md` itself, so no sibling shares the shape. A clean sweep, recorded here
  so it is distinguishable from a sweep that never ran.

## What this ledger does not claim

Nothing about the steps AFTER the install block. `RATCHET_LOOKBACK`, `PRODUCT_GLOBS` and the
`.memory-tree.conf` dependency were not exercised.
