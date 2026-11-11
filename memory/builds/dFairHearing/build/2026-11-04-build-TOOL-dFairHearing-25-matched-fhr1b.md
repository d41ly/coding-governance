# TOOL-dFairHearing-25 — replay 1 run 1's matched list, attempt `fhr1b`

**Serves:** research TOOL-dFairHearing-25

**Adjudicator:** the build pass's main loop of 2026-11-04, as spec 1 §4 "Scoring" assigns it

Run 1's report is the clone's `memory/builds/dFairHearing/reviews/` record under `%TEMP%/fhr1b`. Each row is one of
its confirmed findings that the main loop placed on a known row after reading the finding's claim beside
the known set (`2026-11-03-build-TOOL-dFairHearing-1-known-set`) and the defect's `what` in the
comparison record's `[map]`, taking the `address-match` lines as candidates and pairing only where the
finding's ref cites the row's tag: 34 pairs over 24 tags.

| candidate | tag |
|---|---|
| 5 | relaunch-replay |
| 14 | relaunch-replay |
| 17 | calls-per-act |
| 2 | merge-back |
| 12 | chain-overlap |
| 9 | executor-map |
| 8 | renewal-keys |
| 7 | fixture-2-population |
| 4 | hidden-spawns |
| 15 | hidden-spawns |
| 32 | hidden-spawns |
| 15 | inflight-count |
| 40 | inflight-count |
| 46 | inflight-count |
| 35 | cli-binary |
| 22 | supervisor-host |
| 23 | dispatcher-latency |
| 49 | dispatcher-latency |
| 24 | fanout-carrier |
| 47 | fanout-carrier |
| 13 | reap-key |
| 25 | reap-key |
| 30 | hookspath |
| 28 | parallel-cleared |
| 1 | catalogue-duplicates |
| 26 | catalogue-duplicates |
| 41 | relaunch-cap |
| 45 | relaunch-cap |
| 48 | deferral-fixtures |
| 42 | next-answers |
| 3 | cycle-spawns |
| 19 | user-guards |
| 31 | deferral-seam |
| 41 | limit-hold |
