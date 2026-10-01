# TOOL-aSightedSkeptic-9 — acceptance ledger

**Serves:** journal TOOL-aSightedSkeptic-9

`review_replay.py` scores a review report for recall against a past diff-review round's confirmed
findings, lists the replayable records with `--corpus`, and declares the self-test arms that are the
held leg `review-replay selftest`: 14 at the build, 19 after the round-1 fold (1adf9409, rev-3),
which also amended AC1 and AC6. The readings were first taken on the build's tip, whose `tools/` is
byte-identical to 149e89d6, and every line below was re-read at fe3c29fc except AC8's original run;
`$KIT` is `tools/workflows`. AC8, the live replay, is the main loop's; its evidence is the AC8 line
below, and the run is in this build's live-replay record.

**Evidences:** TOOL-aSightedSkeptic-9
- AC1 — `selftest: 19/19 arms` — `python tools/workflows/review_replay.py --selftest` printed `ok`
  for all 19 arms of the rev-3 §4 table, from `known-legacy-parse` to `appendix-u2028-row` with
  `score-miss` among them, then `selftest: 19/19 arms`, and exited 0. At the build, before the fold,
  it printed 14/14; 1adf9409's message records each of the five new arms RED under a staged break.
- AC2 — `known-liveness-refuses` — a scratch copy under the session scratchpad, with line 157
  `if len(raw) != stated:` replaced by `if False:`, printed
  `FAIL known-liveness-refuses: not refused with both numbers`, then `selftest: 18/19 arms`, and
  exited 1. The copy was not committed. Before the fold the line was 144 and the copy read 13/14.
- AC3 — `round 1` — `--corpus memory/builds` listed 5 records at `round 1`, from aSightedSkeptic,
  dAlignedCarrier, dLoggedFlight, dMendedRecall and dPolishedVitrine, and its summary read scanned
  148, listed 10, refused liveness 110, refused no-count 10, refused no-range 17 and refused
  no-scorable 1. The five listed-and-refused counts sum to 148. The fifth record is this build's own
  closing review, written after the build.
- AC4 — `grep -nE "memory/|tools/" $KIT/review_replay.py` — printed nothing and exited 1.
- AC5 — `git cat-file` — under `GIT_TRACE=1` the same `--corpus` run's trace held exactly 1 line
  naming `git cat-file`, a single `git cat-file --batch-check`, over the 147 records scanned; at
  fe3c29fc it is still exactly 1 line, over 148.
- AC6 — `tools/gate-legs.json` — at fe3c29fc it holds the leg `review-replay selftest` with argv
  `python3 tools/workflows/review_replay.py --selftest`, chunk `selftests`, subject `kit`,
  ceiling 300 and no `guard` key, which 1adf9409 removed under rev-3. `tools/workflows/kit.toml`
  declares the same leg at line 158 with `guard = []`, `memory/map/features/review-harnesses.md`
  claims it at line 15, and `tools/run-gates/selftest-budgets.txt` carries its budget row at 60.
  `python tools/govkit/govkit.py selfcheck` exited 0,
  `python3 tools/codebase-map/check_gate_coverage.py` exited 0, and
  `python tools/check-spec-tokens.py` exited 0 with its guards join examining 137 declared paths in
  11 live specs.
- AC7 — `grep -c "review_replay.py" tools/workflows/README.md` — printed 6, and 6 again at
  fe3c29fc.
- AC8 — `replay: recall` — the main loop ran the new harness over dAlignedCarrier's round-1 record `memory/builds/dAlignedCarrier/reviews/2026-09-30-review-TOOL-dAlignedCarrier-1-closing-diff-round1.md`, range `87c245b3...3c45a567`, then `--known <record> --candidate <report>`, which exited 0 and printed `replay: recall 3/4 = 0.75`. The run and the score are in this build's live-replay record. Re-scoring the same record against the same candidate report with the rev-3 tool at fe3c29fc exited 0 and printed `unit adjudicated-item`, `unscorable 0` on the candidate line, and `replay: recall 3/4 = 0.75` again.
