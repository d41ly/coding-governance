# TOOL-dTotalRecall-3 deviation 32 — the lease's offline queue functions move into the shared ref writer's block

**Serves:** deviation TOOL-dTotalRecall-3

- **Departs from:** `TOOL-dPlacedRequest-1@rev-4`
- **Hand-off:** spec-revised
- **Before:** TOOL-dPlacedRequest-1 S10 defines the offline queue, `<git-common-dir>/gov-queue.log` and its flush, in the unattended kit's lease verbs.
- **After:** the queue functions live in the canonical `gov_ref_sh` block (`tools/lib/gov-ref.sh`), and the lease verbs call them from `unattended.sh`'s inline copy; their behaviour and the log's grammar are unchanged.
- **Cause:** design defect
- **Reason:** TOOL-dPlacedRequest-1's non-goals say other compare-and-swap mints apply `leases.offline` "through the same queue functions when they land"; the ask-family mint is that second caller, in a kit that cannot source the unattended kit, so the functions are extracted at their second instance, never copied.
- **Evidence:** TOOL-dTotalRecall-3 §2 S6 and §8 F3; TOOL-dPlacedRequest-1 S10 and `:139-140`
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer role of dTotalRecall's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-3
