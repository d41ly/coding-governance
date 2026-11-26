# TOOL-dTotalRecall-3 deviation 34 — the lease's offline queue stays in the lease verbs, and no claim or mint queues

**Serves:** deviation TOOL-dTotalRecall-3

- **Departs from:** `TOOL-dPlacedRequest-1@rev-4`
- **Hand-off:** spec-revised
- **Before:** TOOL-dPlacedRequest-1 S10 defines the offline queue, `<git-common-dir>/gov-queue.log` and its flush, in the unattended kit's lease verbs, and its non-goals expect other compare-and-swap mints to apply `leases.offline` through the same queue functions.
- **After:** the queue functions stay in the unattended kit's lease verbs, unchanged; a slug claim or an ask mint by `tools/memory-tree/gov-claim.sh` calls none of them, and offline it writes and queues nothing: `refuse` exits 2, `warn` and `follow-leases` exit 4, the route `--entry-claim` takes over the same namespace.
- **Cause:** external
- **Reason:** the landed `write_gov_queue` refuses `epoch-fence`, drops a queued commit with no `last-fetch:` and reads driver names, so it cannot carry a claim; queueing under `warn` would let two offline clones each scaffold one slug (TOOL-dTotalRecall-3 §8 F7). Deviation 32's move has no second caller to extract for.
- **Evidence:** TOOL-dTotalRecall-3 §2 S6, §8 F2, F3 and F7, AC6; `tools/loop/claim.py#derive_claim_route`; the pass commit of TOOL-dTotalRecall-3 and its acceptance ledger, `2026-11-22-build-TOOL-dTotalRecall-3-1-acceptance-ledger.md`
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer role's rev-4 re-ground of TOOL-dTotalRecall-3 (§8 F7), under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-3
- **Supersedes:** 2026-10-26-build-TOOL-dTotalRecall-3-deviation-32
