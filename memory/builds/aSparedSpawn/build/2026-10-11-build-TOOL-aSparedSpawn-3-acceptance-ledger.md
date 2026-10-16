# Acceptance ledger — TOOL-aSparedSpawn-3

**Serves:** journal TOOL-aSparedSpawn-3

Node `a`, 2026-10-12, bash 5.3 under MSYS, beside other sessions' work: a fixture `sleep 20` leg took
26.8 s, so every reading below is ordered by run-record rows and never by a clock. The pass ran no
bar, no suite, no held leg and no slice of a suite. Every observation drove the real runner over a
hand-built fixture repository through the instrument committed beside this ledger,
`2026-10-12-build-TOOL-aSparedSpawn-3-direct-checks.sh`, once against the base runner at `286b839a`
(the "before" runs) and once against the working tree's (the "after" runs). `bash -n` passed on the
five changed shell files and the instrument. Every suite arm this unit adds or moves is OWED at
VERIFYING and says so.

**Evidences:** TOOL-aSparedSpawn-3
- AC1 — `direct-checks.sh ac1` — before: the retry's `1.retry.leg` started 20 s after the sleeper's
  `0.leg` ended and the sleeper found no marker in the work dir; after: the retry started 10 s before
  the sleeper ended and the sleeper, listing the work dir as it ended, found `1.defer`. The canary's
  9k arm is OWED at VERIFYING.
- AC2 — `direct-checks.sh ac1` — after: the bar's `GATE` and `----` lines are the base bar's line for
  line, the reworded deferral apart: `GATE ok    sleeper`, the deferral, the pending chunk line,
  `GATE ok    once  (retried after timeout)`, `---- retry: green  (1 retried, 0 failed)`, `----`.
  The canary's 9k byte-equality arm is OWED at VERIFYING.
- AC3 — `direct-checks.sh ac3` — after, a 30 s ceiling under a 50 s wall: under `GATE_WALL=50` the
  breach printed `still running at the wall: stall (its serial retry)` and no `GATE ok` or
  `GATE FAIL` line for the leg. A first draft at a 10 s ceiling and an 18 s wall named only the sleeper, because the release
  came 10 to 14 s after the first attempt's end on this host; both arms now carry the wider window.
  The canary's 9l arm is OWED at VERIFYING.
- AC4 — `direct-checks.sh ac4` — after: one FAIL line for the leg, reading
  "`timed out after 3s, again on its serial retry`" with the serial attempt's HOST note; the
  set-aside `1.tail.leg` reads `timeout` and started before the sleeper ended, and `1.retry.leg`
  started after it. Its first run read a floor an earlier case had written to the shared floor path,
  which the instrument and the canary's 9m arm now remove first. The 9m arm is OWED at VERIFYING.
- AC5 — `direct-checks.sh ac5` — before: the header's `dispatch` key read `0 1 2`; after: `1 2 0`.
  The evidence suite's AC5 arm is OWED at VERIFYING.
- AC6 — `direct-checks.sh ac6` — before: `0 1 2 3`; after: `0 1 3 2`, the ledger placing `a` and a
  40 s ceiling over the median ratio 10 placing `d` between `b` and `c`. The evidence suite's AC6 arm
  is OWED at VERIFYING.
- AC7 — `direct-checks.sh ac7` — before: on the base runner at 286b839a, whose ledger merge is the
  `NR == FNR` program the criterion names (spelled `NR==FNR` there), a second bar that reused its
  one leg left `gate-ledger.tsv` with 0 rows; after: 1 row. The canary's 9d assertion is OWED at
  VERIFYING.

Checked as well, none of them a bar leg over the tree: `check-arms.py --check` reports the same six
unarmed `run-gates.sh` exit sites as before this pass; `sh_hygiene.py --spawn-idioms` over the leg's
pathspecs exited 0 once the three new canary reads took a here-string instead of a pipe;
`lexicon.py` exited 0; `check-spec-tokens.py` reported nothing for this spec; `gen_map.py --write`
added `run_tail_retry`.

## Announced gaps

- The suites this unit edits ran in no form: `run-gates.test.sh`, `run-gates.evidence.test.sh`,
  `profile_bar.test.sh` and `foreign-prefix.gov.test.sh`. The ceiling-prior sort now orders a
  ledgerless fixture by its legs' ceilings, so an existing arm that relied on manifest dispatch order
  among ceiling-bearing legs would surface there.
- A python heredoc meant to edit `profile_bar.test.sh` was passed the file as its first argument,
  and the launcher started that suite with bash; it died at startup on a cygwin signal-pipe fault,
  wrote nothing and left no process. The edit was then made with the Edit tool.
