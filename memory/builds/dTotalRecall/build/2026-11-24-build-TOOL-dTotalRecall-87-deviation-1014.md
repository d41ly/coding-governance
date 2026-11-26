# TOOL-dTotalRecall-87 deviation 1014 — the precedent paragraph of the memory root resolver states a third way the runlog reader diverges

**Serves:** deviation TOOL-dTotalRecall-87

- **Departs from:** `TOOL-dTotalRecall-87@rev-3` [§4 The resolver]
- **Hand-off:** spec-revised
- **Before:** the precedent paragraph says of `tools/runlog/runlog_lib.py#resolve_memory_root`: "It diverges from this one in two ways."
- **After:** it diverges in a third way too: `runlog_lib` keeps an inner empty or `.` segment and outer whitespace as spelled, where `tree_lib.resolve_memory_root` folds them away, so `./docs//memory`, a root with outer spaces and `.` each read two ways, the last refused by `tree_lib`; the fold is deliberate, one root being one path in the kit, and agrees with the backslash fold of `tools/memory-tree/design_lib.py#main`
- **Cause:** review finding
- **Reason:** item M8 of the round-1 spec audit of units 77 to 88, report id 16, asked the precedent sentence to state its divergence whole, and rev-3 states the two refusals and leaves the third way out.
- **Evidence:** the six rows of TOOL-dTotalRecall-92 §4 "The precedent", read again at this pass by both resolvers over one conf value (DERIVED 2026-11-24); `2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1`; the ledger `2026-11-24-build-TOOL-dTotalRecall-92-1-acceptance-ledger.md`; `audit-77 id 16 s10`
- **Risk:** editorial
- **Approver:** author, the pass of TOOL-dTotalRecall-92, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTotalRecall-92
- **Caused-by:** TOOL-dTotalRecall-92
- **Made-by:** lease-dTotalRecall
