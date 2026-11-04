# PLAY-dConvergedCharter-8 deviation 81 — review-protocol parity narrowed to its four harness pairs, not retired with its last document

**Serves:** deviation PLAY-dConvergedCharter-8

- **Departs from:** `cl-dClosedLoop-0482@c8b56d3a`
- **Hand-off:** design-to-spec
- **Before:** the remaining renderers absorbed, each retired with its last document: kit/dogfood doc parity, review-protocol parity, each kit's skill wiring `--check` and govkit's placeholder render
- **After:** the remaining renderers absorbed, each retired with its last document: kit/dogfood doc parity, review-protocol parity's document pair, each kit's skill wiring `--check` and govkit's placeholder render, review-protocol parity kept as the check of the workflows kit's four harness pairs, which render no document
- **Cause:** design defect
- **Reason:** review-protocol parity holds one document pair, `REVIEW-PROTOCOL.md`, and four `.js` harness pairs. Its last document leaves with unit 7, and retiring the leg then drops the check of the four harness pairs, which the fates table keeps ("four harness checks … parity | STAYS"). Keeping the leg fails the clause's word for this leg, so every option fails a strongest-tier bound and the fork rule's rung 6 relaxes the weaker one (execution plan lines 924-946, PLAY-dConvergedCharter-8 §8 F3). The clause's bound is the one written about renderers of documents, and once the document pair leaves the leg renders none, so the clause's word is the bound relaxed for this one leg.
- **Evidence:** the clause, `memory/builds/dConvergedCharter/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md:28`; the pairs, `tools/workflows/check-protocol-parity.test.sh:94-98`; the fates rows, `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md:98` and `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-research-tool-fates.md:68`; scout B finding 6, `memory/builds/dConvergedCharter/build/2026-11-03-build-PLAY-dConvergedCharter-6-reuse-scout-b.md:16`; rung 6, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:924`
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer stage of the harness's spec run for dConvergedCharter, citing ER:328, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0482@c8b56d3a
- **Caused-by:** PLAY-dConvergedCharter-8
- **Bound:** the clause's "each retired with its last document" for `review-protocol parity (kit vs dogfood)`
- **Tier:** strongest, a bound the carried clause states in its text
