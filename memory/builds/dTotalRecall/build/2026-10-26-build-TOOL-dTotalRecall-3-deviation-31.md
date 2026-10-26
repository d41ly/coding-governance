# TOOL-dTotalRecall-3 deviation 31 — the `gov_ref_sh` block refuses deleting a claim ref and carries the offline queue

**Serves:** deviation TOOL-dTotalRecall-3

- **Departs from:** `TOOL-dPlacedRequest-11@rev-3`
- **Hand-off:** spec-revised
- **Before:** TOOL-dPlacedRequest-11 S1 and S2 put `write_gov_ref` and `build_gov_commit` in the canonical `gov_ref_sh` block of `tools/lib/gov-ref.sh`; an empty `<src>` pushes any ref's deletion, and the block holds no offline queue.
- **After:** the block also refuses, rc 2, an empty `<src>` for any ref under `refs/gov/claims/`, and holds TOOL-dPlacedRequest-1 S10's offline queue functions, moved there; its inline copies follow through the `gov_ref_sh` parity row, and `tools/memory-tree/gov-claim.sh` joins them as a third copy.
- **Cause:** design defect
- **Reason:** cl-0214 requires slug claim refs never pruned, and the one writer of every governance ref is the one place a deletion can be refused for all callers. The ask-family mint is the queue's second caller, and memory-tree cannot source the unattended kit, so the queue moves into the shared block rather than being copied.
- **Evidence:** TOOL-dTotalRecall-3 §2 S5 and S6, §8 F1 and F3; TOOL-dPlacedRequest-11 S1, S2, S8; TOOL-dPlacedRequest-1 S10 and its non-goal at `:139-140`
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dTotalRecall's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-3
