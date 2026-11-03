# dOrderedCharter — unit 63's builder return

**Serves:** journal PLAY-dOrderedCharter-63

Run wf_bec9fd19-bd4, summarized from its return.

- Built at rev-1 as pass commit `4264cdde2`: `tools/check-spec-tokens.py` gains `STATUS_HEAD` and `check_live_header`,
  and the population loop reads a spec's liveness from its first `**Status:**` line outside any fence instead of
  `LIVE.search` over the whole text. Three arms in `tools/check-spec-tokens.test.sh` (`deferred-fenced`,
  `fence-above-header`, `live-fenced-closed`); `FLOOR_ASSERTIONS` 215 → 218.
- Observed by probe: AC1 to AC5 as the ledger records; against the unchanged checker the first two plants read
  `2 live spec(s)` and exited 1; over the tree one spec flips, TOOL-dIndexedDesign-12.
- Owed at the close: RED then GREEN for the three `New arm:` lines (AC1 with `LIVE.search` restored, AC2 under a
  first-status-line read ignoring fences, AC3 under a read taking a fenced status as the header); the suite's 218
  assertions through `check-testsuite-counts.sh`; the §7 legs.
