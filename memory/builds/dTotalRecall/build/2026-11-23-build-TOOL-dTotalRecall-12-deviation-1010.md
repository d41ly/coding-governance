# TOOL-dTotalRecall-12 deviation 1010 — the recall adapter's tail held as two segments, a PowerShell command folded before its split, the walk's coverage argument and the slice channel's armed rule

**Serves:** deviation TOOL-dTotalRecall-12

- **Departs from:** `TOOL-dTotalRecall-12@rev-3` [§2 S1, S4, S7; §4 "Data model"]
- **Hand-off:** spec-to-code
- **Before:** §4 spells the read verbs' adapter entry as one path string, the memory-recall kit's directory joined to `query.py`; S1 splits every shell command by `extract_segments`, which reads a backslash as bash's escape; S4 signs `measure_agent_memory(path, memory_root, read_slice)` and sums its walk's torn and unreadable counts onto the window line; S7 grades the slice channel armed or unarmed and states no rule for a population of agents.
- **After:** `tools/runlog/memory_measure.py#RECALL_ADAPTER` holds the tail as its two segments, joined by `/` into its `READ_VERBS` entry and matched as S2 states; `memory_measure.py#derive_read_channel` folds a PowerShell command's backslashes to `/` before `extract_segments` splits it; `memory_measure.py#measure_agent_memory` takes an optional fourth argument `coverage`, handed to `read_records` as that reader takes it; `memory_measure.py#check_slice_armed` reads the channel armed when at least one agent of the window was measured and none read its slice as None; and the fixture sets each planted transcript's write time to its last record, since the population skips a transcript last written before the window opens.
- **Cause:** builder discovery
- **Reason:** the install-prefix ban reds any shipped file spelling a sibling kit's directory joined to one of its files, this module included; bash's escape reading erases each backslash of an unquoted PowerShell path, so a PowerShell read of a Windows memory path would count zero; the three-argument signature cannot return the counts S4 prints; and a per-agent None counted as armed would be the zero-bytes reading S7 and section 8 F2 refuse.
- **Evidence:** the pass commit of TOOL-dTotalRecall-12 and its acceptance ledger, `2026-11-22-build-TOOL-dTotalRecall-12-1-acceptance-ledger.md`
- **Risk:** additive
- **Approver:** author, under the build's `author-recorded` value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-12
- **Made-by:** owner
