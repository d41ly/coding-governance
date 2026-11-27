# TOOL-dTotalRecall-17 deviation 1009 — the map instance's five helpers, its constants, and the CLI refusing --instance map-replay

**Serves:** deviation TOOL-dTotalRecall-17

- **Departs from:** TOOL-dTotalRecall-17@rev-3 [§4 Inventory, S1]
- **Hand-off:** spec-to-code
- **Before:** §4's inventory mints measure_map_experiment, extract_item_findings, measure_existence_searches, measure_bytes_before_act and derive_map_verdict, and S1 reads the runs as measure_replay_experiment does; neither names a helper beside them, a constant, or what --instance map-replay does.
- **After:** tools/workflows/replay_scorer.py#read_run_reports is the run-case subject read, extracted from #measure_replay_experiment at its second caller; #read_map_known reads every known set before any transcript, so AC1's refusals need no runlog kit; #resolve_runlog_extract is runlog's import at use; #read_transcript_calls is the one transcript reader both measures share; #measure_call_searches is the per-call search count #measure_bytes_before_act also reads to except a shell search; ITEM_HEADING, SEARCH_TOOLS, SEARCH_PROGRAMS, GIT_SEARCHES, RECALL_MARGIN and SEARCH_FLOOR are module constants; #main refuses --instance map-replay as a usage error.
- **Cause:** builder discovery
- **Reason:** a second copy of the run-case read would be a second pairing of reports with subjects, the charter's reuse rule; a known-set read callable alone lets the map-known arm run without runlog, which only map-transcript may skip on; one transcript reader keeps the two measures on one parse; and --instance map-replay would otherwise call derive_map_verdict with two texts and raise.
- **Evidence:** the pass commit of TOOL-dTotalRecall-17 and its acceptance ledger, 2026-11-22-build-TOOL-dTotalRecall-17-1-acceptance-ledger.md
- **Risk:** additive
- **Approver:** author, under the build's author-recorded value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-17
- **Made-by:** owner
