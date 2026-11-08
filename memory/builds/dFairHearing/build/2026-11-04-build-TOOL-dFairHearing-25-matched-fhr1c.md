# TOOL-dFairHearing-25 — replay 1 run 1's matched list, attempt `fhr1c`

**Serves:** research TOOL-dFairHearing-25

**Adjudicator:** the build pass's main loop of 2026-11-04, as spec 1 §4 "Scoring" assigns it

Run 1's second attempt; its first, `fhr1b`, is void (its synthesizer read a path outside the clone and the
scratchpad). The report is the clone's `memory/builds/dFairHearing/reviews/` record under `%TEMP%/fhr1c`.
Each row is one of its confirmed findings that the main loop placed on a known row after reading the
finding's claim beside the known set (`2026-11-03-build-TOOL-dFairHearing-1-known-set`) and the defect's
`what` in the comparison record's `[map]`, taking the `address-match` lines as candidates and pairing
only where the finding's ref cites the row's tag: 39 pairs over 27 tags.

| candidate | tag |
|---|---|
| 1 | relaunch-replay |
| 15 | relaunch-replay |
| 48 | relaunch-replay |
| 19 | driver-schema |
| 20 | calls-per-act |
| 4 | merge-back |
| 10 | chain-overlap |
| 32 | chain-overlap |
| 8 | executor-map |
| 6 | renewal-keys |
| 2 | hidden-spawns |
| 16 | hidden-spawns |
| 39 | hidden-spawns |
| 16 | inflight-count |
| 39 | inflight-count |
| 12 | unfailing-fixtures |
| 49 | unfailing-fixtures |
| 35 | fail-closed-policy |
| 50 | supervisor-host |
| 22 | dispatcher-latency |
| 28 | fanout-carrier |
| 14 | reap-key |
| 29 | reap-key |
| 27 | resume-tick-seed |
| 34 | hookspath |
| 30 | core-sweep |
| 31 | hook-fragments |
| 3 | catalogue-duplicates |
| 5 | catalogue-duplicates |
| 24 | catalogue-duplicates |
| 25 | catalogue-duplicates |
| 40 | relaunch-cap |
| 44 | relaunch-cap |
| 40 | hold-bound |
| 38 | fencing |
| 11 | instance-witness |
| 18 | headless-workflow |
| 26 | owner-rulings |
| 45 | act-ceiling |
