# TOOL-aSightedSkeptic-9 — acceptance ledger

**Serves:** journal TOOL-aSightedSkeptic-9

`review_replay.py` scores a review report for recall against a past diff-review round's adjudicated
items, lists the replayable records with `--corpus`, and declares 14 self-test arms that are the held
leg `review-replay selftest`. Every reading below was taken on the build's tip, whose `tools/` is
byte-identical to 149e89d6; `$KIT` is `tools/workflows`. AC8, the live replay, is the main loop's and
is not evidenced in this record yet.

**Evidences:** TOOL-aSightedSkeptic-9
- AC1 — `selftest: 14/14 arms` — `python tools/workflows/review_replay.py --selftest` printed `ok`
  for all 14 arms, from `known-legacy-parse` to `candidate-only` with `score-miss` among them, then
  `selftest: 14/14 arms`, and exited 0.
- AC2 — `known-liveness-refuses` — a scratch copy under the session scratchpad, with line 144
  `if len(raw) != stated:` replaced by `if False:`, printed
  `FAIL known-liveness-refuses: not refused with both numbers`, then `selftest: 13/14 arms`, and
  exited 1. The copy was not committed.
- AC3 — `round 1` — `--corpus memory/builds` listed 4 records at `round 1`, from dAlignedCarrier,
  dLoggedFlight, dMendedRecall and dPolishedVitrine, and its summary read scanned 147, listed 9,
  refused liveness 110, refused no-count 10, refused no-range 17 and refused no-scorable 1. The five
  listed-and-refused counts sum to 147.
- AC4 — `grep -nE "memory/|tools/" $KIT/review_replay.py` — printed nothing and exited 1.
- AC5 — `git cat-file` — under `GIT_TRACE=1` the same `--corpus` run's trace held exactly 1 line
  naming `git cat-file`, a single `git cat-file --batch-check`, over the 147 records scanned.
- AC6 — `tools/gate-legs.json` — it holds the leg `review-replay selftest` with argv
  `python3 tools/workflows/review_replay.py --selftest`, chunk `selftests`, subject `kit`, guard
  `tools/workflows/` and ceiling 300. `tools/workflows/kit.toml` declares the same leg at line 156,
  `memory/map/features/review-harnesses.md` claims it at line 15, and
  `tools/run-gates/selftest-budgets.txt` carries its budget row at 60. NOT observed here:
  `govkit.py selfcheck` and `check_gate_coverage.py` were outside the commands this pass could run;
  they run at the close.
- AC7 — `grep -c "review_replay.py" tools/workflows/README.md` — printed 6.

## What this ledger does not evidence

AC8, the live replay of one round-1 record through the `Workflow` tool, was still running in the
main loop when this record was written. Its line, with the record path, the range and the
`replay: recall` line, is the main loop's to add.
