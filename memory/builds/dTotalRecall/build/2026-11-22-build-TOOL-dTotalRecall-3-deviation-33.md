# TOOL-dTotalRecall-3 deviation 33 — the `gov_ref_sh` block refuses deleting a claim ref and carries no offline queue

**Serves:** deviation TOOL-dTotalRecall-3

- **Departs from:** `TOOL-dPlacedRequest-11@rev-3`
- **Hand-off:** spec-revised
- **Before:** TOOL-dPlacedRequest-11 S1 and S2 put `write_gov_ref`, `build_gov_commit` and `remove_gov_ref` in the canonical `gov_ref_sh` block of `tools/lib/gov-ref.sh`; `remove_gov_ref` pushes the deletion of any ref it is named, and the block holds no offline queue.
- **After:** `tools/lib/gov-ref.sh#remove_gov_ref` returns 2 for any ref under `refs/gov/claims/`, `GOVREF_WHY` naming the rule, before it reaches the push; the block holds no offline queue, which stays in the unattended kit's lease verbs; its inline copies follow through the `gov_ref_sh` parity row, and `tools/memory-tree/gov-claim.sh` joins them as a third carrier.
- **Cause:** external
- **Reason:** cl-0214 requires slug claim refs never pruned, and `remove_gov_ref` is the one deletion form every caller reaches. The landed queue drops a claim and reads driver names, so the spec's rev-4 re-ground queues nothing (§8 F7) and the queue half of deviation 31 describes no change this unit makes.
- **Evidence:** TOOL-dTotalRecall-3 §2 S5 and S6, §8 F3 and F7; the pass commit of TOOL-dTotalRecall-3 and its acceptance ledger, `2026-11-22-build-TOOL-dTotalRecall-3-1-acceptance-ledger.md`
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role's rev-4 re-ground of TOOL-dTotalRecall-3 (§8 F7), under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-3
- **Supersedes:** 2026-10-26-build-TOOL-dTotalRecall-3-deviation-31
