# TOOL-dTotalRecall-119 deviation 1017 — the kit README names the claim cache and a map dossier claims the new gotcha class

**Serves:** deviation TOOL-dTotalRecall-119

- **Departs from:** `TOOL-dTotalRecall-119@rev-1` [§4 "Files touched"; §5 "user docs"]
- **Hand-off:** spec-to-code
- **Before:** the spec's files touched hold neither `tools/memory-tree/README.md` nor a map dossier, and its user-docs row reads N/A.
- **After:** `tools/memory-tree/README.md` says the orphan check's claim root is read from this clone's cache and fetches nothing, and `memory/map/features/memory-tree-hygiene.md`, which claims the causes leg, claims `fixture-plants-a-state-no-writer-makes.md`.
- **Cause:** builder discovery
- **Reason:** the README's orphan paragraph said the root is each build whose claim ref `refs/gov/claims/<slug>` is held, which S1 makes false; and an unclaimed gotcha class is one the coverage leg refuses.
- **Evidence:** the README paragraph before and after (DERIVED 2026-11-25); the ledger `2026-11-25-build-TOOL-dTotalRecall-119-1-acceptance-ledger.md`
- **Risk:** additive
- **Approver:** author, under the build's `author-recorded` value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-119
- **Made-by:** owner
