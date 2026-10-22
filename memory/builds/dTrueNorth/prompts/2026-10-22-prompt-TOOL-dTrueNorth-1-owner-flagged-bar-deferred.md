**Serves:** research TOOL-dTrueNorth-1

# Owner instruction — the flagged bar is deferred past this landing

## The prompt

> Omit the flagged bar this time, we will run it later

— owner, 2026-10-22, in the run's session while TOOL-dTrueNorth-29's builder was running, after the run
estimated the landing at four to five hours, three of them two flagged bars.

## How the run applies it

- No `GATE_FULL=1 GATE_SELFTESTS=1` bar runs for this landing: neither the confirming bar before the close
  nor the one the VERIFYING notice owes into `--close`. The close runs its own bar without
  `GATE_SELFTESTS`, so the self-test legs read held, and the kit Definition-of-Done item that owes the
  flagged bar is overridden citing this record.
- TOOL-dTrueNorth-29 is still verified: the five suites its fixes target run once, standalone, after its
  commit.
- The RED-then-GREEN observation of the `New arm:` lines on the suites the flagged bar runs
  (`check-memory-hygiene.test.sh`, `check-verdict-epoch.test.sh`, `check-spec-tokens.test.sh`,
  `tier2-review.test.sh`, `unattended-build.test.sh`) is owed with the later flagged bar, listed in the
  wrap-up as owed. The `gen_build_index.py`, `routed_commits.py`, `deviation_join.py` and
  `asbuilt_view.py` arm lines were observed RED before this instruction and are recorded in their ledgers.
- The flagged bar at e583a7f42 found the reds `2026-10-22-build-TOOL-dTrueNorth-29-flagged-bar.md`
  excerpts; its inherited reds (measure-legs, govkit, foreign-prefix parity, the spec-tokens parity arms,
  pre-push's bar-reuse arm under load) are the later bar's to read.
