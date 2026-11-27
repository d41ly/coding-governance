# TOOL-dTotalRecall-37 deviation 1020 — a third plant arms the unresolved-token finding

**Serves:** deviation TOOL-dTotalRecall-37

- **Departs from:** `TOOL-dTotalRecall-37@rev-7` [§7 "New arm"]
- **Hand-off:** spec-to-code
- **Before:** the arm stages the plants `generated-glob` and `render-unmarked`, and S2's finding on a rendered `to` whose token does not resolve has no plant.
- **After:** `check_generated_attribute_arms` also stages `render-token`, a `to` spelled with an unknown token, in the run of `generated-glob`.
- **Cause:** builder discovery
- **Reason:** a refusal of the deployer no arm reaches is a gate never seen red; the plant shares a run, so it costs no second selfcheck.
- **Evidence:** the ledger `2026-11-25-build-TOOL-dTotalRecall-37-1-acceptance-ledger.md`, AC3
- **Risk:** additive
- **Approver:** author, under the build's `author-recorded` value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-37
- **Made-by:** owner
