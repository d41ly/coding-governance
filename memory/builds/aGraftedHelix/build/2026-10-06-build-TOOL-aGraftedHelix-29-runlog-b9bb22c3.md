# Run record

**Serves:** journal TOOL-aGraftedHelix-29..41

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aGraftedHelix/RUN.md
- run: 2 of 2
- start: b9bb22c36a189968184ed2359181cac601b842f8
- phase: VERIFYING
- terminal: no
- window: 2026-10-05T17:04:37Z to 2026-10-06T22:21:58Z
- window opened by: git
- window closed by: last-activity
- duration: 105441s
- own commits: 47
- last own commit: a9fd99db9e4ae567e27aaaa2e7c423a63b368a21
- merged: no
- units served: 13
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 4 · in-window 9 · post-close 0
- usage main: requests 293 · in 648 · out 217362 · cache-read 119657232 · cache-write 3580384
- usage agent: requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0
- usage workflow: requests 4344 · in 8688 · out 4167383 · cache-read 1256370107 · cache-write 23684059
- attributed calls: 4031 of 5178
- values withheld: 0
- commitment: sha256 97b2aea5e8c44c42c1ab486c5b228576b0b5396b4a87d2838564911e93f02f4a · lines 326

## Timeline

- events: 85 · shown 60 · elided 25
- elided: 25 events from 2026-10-05T21:30:28Z to 2026-10-06T05:08:51Z
- withheld rows: verb 123 · push 40 · push-refused 0 · gate 0 · compact 1 · limit 3 · idle 0 · workflow 23

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-10-05T17:04:37Z | run-state | phase | 018b5675727d | RUNNING | - | - |
| 2026-10-05T17:05:33Z | run-state | phase | b9bb22c36a18 | SPECCING | - | - |
| 2026-10-05T17:38:58Z | git | commit | 43bdf3aef8c1 | - | - | TOOL-aGraftedHelix-29 |
| 2026-10-05T17:40:36Z | git | commit | 1b53b54b8fca | - | - | TOOL-aGraftedHelix-30 TOOL-aGraftedHelix-31 TOOL-aGraftedHelix-32 |
| 2026-10-05T17:42:10Z | run-state | phase | 7dca26485330 | BUILDING | - | - |
| 2026-10-05T17:43:49Z | run-state | brief | TOOL-aGraftedHelix-29 | - | - | - |
| 2026-10-05T17:49:32Z | run-state | dispatch | TOOL-aGraftedHelix-29 | - | - | - |
| 2026-10-05T17:52:05Z | git | commit | f5ee092858da | - | - | TOOL-aGraftedHelix-29 |
| 2026-10-05T18:07:47Z | git | commit | d52f0edea3c9 | - | - | TOOL-aGraftedHelix-29 |
| 2026-10-05T18:10:31Z | git | commit | f7a0f089948d | - | - | TOOL-aGraftedHelix-29 |
| 2026-10-05T18:12:21Z | git | commit | 65b4548763c1 | - | - | TOOL-aGraftedHelix-29 |
| 2026-10-05T18:18:18Z | run-state | brief | TOOL-aGraftedHelix-30 | - | - | - |
| 2026-10-05T18:19:16Z | run-state | dispatch | TOOL-aGraftedHelix-30 | - | - | - |
| 2026-10-05T18:32:20Z | git | commit | 99b5dac28334 | - | - | TOOL-aGraftedHelix-30 |
| 2026-10-05T18:37:30Z | git | commit | c54278c13129 | - | - | TOOL-aGraftedHelix-30 |
| 2026-10-05T18:41:49Z | run-state | brief | TOOL-aGraftedHelix-31 | - | - | - |
| 2026-10-05T18:43:22Z | run-state | dispatch | TOOL-aGraftedHelix-31 | - | - | - |
| 2026-10-05T19:22:39Z | git | commit | d65ee07d8958 | - | - | TOOL-aGraftedHelix-31 |
| 2026-10-05T19:24:58Z | git | commit | 744fd3560dc1 | - | - | TOOL-aGraftedHelix-31 |
| 2026-10-05T19:38:59Z | run-state | brief | TOOL-aGraftedHelix-32 | - | - | - |
| 2026-10-05T19:40:52Z | run-state | dispatch | TOOL-aGraftedHelix-32 | - | - | - |
| 2026-10-05T20:23:32Z | git | commit | 28f063c242e5 | - | - | TOOL-aGraftedHelix-32 |
| 2026-10-05T20:34:57Z | git | commit | a6de788a259f | - | - | TOOL-aGraftedHelix-32 |
| 2026-10-05T20:37:37Z | git | commit | 525079d4ed38 | - | - | TOOL-aGraftedHelix-32 |
| 2026-10-05T20:41:41Z | git | commit | bdc93251c03d | - | - | TOOL-aGraftedHelix-32 |
| 2026-10-05T21:08:08Z | git | commit | 0bc5f0f87c56 | - | - | TOOL-aGraftedHelix-33 |
| 2026-10-05T21:09:13Z | run-state | brief | TOOL-aGraftedHelix-33 | - | - | - |
| 2026-10-05T21:09:48Z | run-state | dispatch | TOOL-aGraftedHelix-33 | - | - | - |
| 2026-10-05T21:25:51Z | git | commit | 843d5c0b3495 | - | - | TOOL-aGraftedHelix-33 |
| 2026-10-05T21:27:13Z | git | commit | 4b21bbd7a885 | - | - | TOOL-aGraftedHelix-33 |

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-10-06T05:13:18Z | git | commit | 897f1ecf42be | - | - | TOOL-aGraftedHelix-37 |
| 2026-10-06T05:16:49Z | git | commit | 071c32bce76b | - | - | TOOL-aGraftedHelix-37 |
| 2026-10-06T05:19:15Z | run-state | phase | 071c32bce76b | VERIFYING | - | - |
| 2026-10-06T10:57:31Z | git | commit | 7db5d7a8b2d5 | - | - | TOOL-aGraftedHelix-38 |
| 2026-10-06T10:58:56Z | run-state | brief | TOOL-aGraftedHelix-38 | - | - | - |
| 2026-10-06T10:59:44Z | run-state | dispatch | TOOL-aGraftedHelix-38 | - | - | - |
| 2026-10-06T11:06:45Z | run-state | dispatch | TOOL-aGraftedHelix-38 | - | - | - |
| 2026-10-06T11:17:04Z | git | commit | 333160ad3655 | - | - | TOOL-aGraftedHelix-38 |
| 2026-10-06T11:30:24Z | run-state | dispatch | TOOL-aGraftedHelix-38 | - | - | - |
| 2026-10-06T11:30:30Z | git | commit | bc3f3ab0cb01 | - | - | TOOL-aGraftedHelix-38 |
| 2026-10-06T11:43:58Z | git | commit | 693c58df808c | - | - | TOOL-aGraftedHelix-38 |
| 2026-10-06T12:12:18Z | git | commit | b32773b58e73 | - | - | TOOL-aGraftedHelix-39 |
| 2026-10-06T12:13:45Z | run-state | brief | TOOL-aGraftedHelix-39 | - | - | - |
| 2026-10-06T12:14:27Z | run-state | dispatch | TOOL-aGraftedHelix-39 | - | - | - |
| 2026-10-06T12:20:34Z | run-state | dispatch | TOOL-aGraftedHelix-39 | - | - | - |
| 2026-10-06T12:51:39Z | git | commit | 838bb8238356 | - | - | TOOL-aGraftedHelix-39 |
| 2026-10-06T12:54:43Z | git | commit | b04ab0da05b7 | - | - | TOOL-aGraftedHelix-39 |
| 2026-10-06T19:48:38Z | git | commit | 9323a3ef55d1 | - | - | TOOL-aGraftedHelix-40 TOOL-aGraftedHelix-41 |
| 2026-10-06T20:00:45Z | run-state | brief | TOOL-aGraftedHelix-40 | - | - | - |
| 2026-10-06T20:02:11Z | run-state | dispatch | TOOL-aGraftedHelix-40 | - | - | - |
| 2026-10-06T20:05:15Z | run-state | dispatch | TOOL-aGraftedHelix-40 | - | - | - |
| 2026-10-06T20:15:23Z | git | merge | c849b65e10e9 | - | - | - |
| 2026-10-06T20:20:56Z | git | commit | d6d50bf0f00f | - | - | TOOL-aGraftedHelix-40 |
| 2026-10-06T20:26:14Z | git | commit | 62dc8a6c5346 | - | - | TOOL-aGraftedHelix-40 |
| 2026-10-06T20:28:39Z | run-state | brief | TOOL-aGraftedHelix-41 | - | - | - |
| 2026-10-06T20:30:05Z | run-state | dispatch | TOOL-aGraftedHelix-41 | - | - | - |
| 2026-10-06T21:31:37Z | git | commit | 183047ecbbfd | - | - | TOOL-aGraftedHelix-41 |
| 2026-10-06T21:37:23Z | run-state | dispatch | TOOL-aGraftedHelix-41 | - | - | - |
| 2026-10-06T21:39:40Z | git | commit | a0aa627ecfde | - | - | TOOL-aGraftedHelix-41 |
| 2026-10-06T22:17:17Z | git | commit | a9fd99db9e4a | - | - | TOOL-aGraftedHelix-41 |

## Units

- units: 41 · shown 0 · aggregated yes

| # | status | units |
|---|---|---|
| 1 | CLOSED | 41 |

## Decisions

- entries: 132 · shown 0 · aggregated yes
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 1 · agent-before 35 · agent-inside 44
- excluded rows: proposal 0 · rescope 13 · dispatch 19 · review 1 · brief 13 · hold 0 · resume 0
- review rounds: 1 · shown 1 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 2 |
| 2 | abort | 0 |
| 3 | override | 0 |
| 4 | waiver | 0 |
| 5 | handoff | 0 |
| 6 | rescope-retire | 0 |
| 7 | rescope-supersede | 0 |
| 8 | rescope-defer | 0 |
| 9 | review | 1 |
| 10 | trailer | 47 |
| 11 | spec-mark | 80 |
| 12 | decision-log | 0 |
| 13 | ledger | 2 |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-10-06T01:52:42Z | CLEAN WITH FIXES | 0 | CONVERGED |

## Conformance

- items: 17 · shown 17 · aggregated no

| # | item | unit | state |
|---|---|---|---|
| 1 | brief-before-build | TOOL-aGraftedHelix-29 | MET |
| 2 | brief-before-build | TOOL-aGraftedHelix-30 | MET |
| 3 | brief-before-build | TOOL-aGraftedHelix-31 | MET |
| 4 | brief-before-build | TOOL-aGraftedHelix-32 | MET |
| 5 | brief-before-build | TOOL-aGraftedHelix-33 | MET |
| 6 | brief-before-build | TOOL-aGraftedHelix-34 | MET |
| 7 | brief-before-build | TOOL-aGraftedHelix-35 | MET |
| 8 | brief-before-build | TOOL-aGraftedHelix-36 | MET |
| 9 | brief-before-build | TOOL-aGraftedHelix-37 | MET |
| 10 | brief-before-build | TOOL-aGraftedHelix-38 | MET |
| 11 | brief-before-build | TOOL-aGraftedHelix-39 | MET |
| 12 | brief-before-build | TOOL-aGraftedHelix-40 | MET |
| 13 | brief-before-build | TOOL-aGraftedHelix-41 | MET |
| 14 | phases-walked | - | UNJUDGEABLE |
| 15 | green-at-close | - | UNJUDGEABLE |
| 16 | keepalive-reaped | - | MET |
| 17 | review-exited | - | MET |

## Anomalies

- anomalies: 10 · shown 10 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | out-of-band-edit | - |
| 2 | refusal-loop | - |
| 3 | destructive-git | - |
| 4 | destructive-git | - |
| 5 | destructive-git | - |
| 6 | destructive-git | - |
| 7 | destructive-git | - |
| 8 | destructive-git | - |
| 9 | destructive-git | - |
| 10 | destructive-git | - |

## Coverage

- journal starts: 2 joined of 3 record-creating
- unjoined starts: 1
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 1
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 246 | 0 |
| 3 | gates | present | 0 | 0 |
| 4 | pushes | present | 40 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aGraftedHelix/RUN.md","run":"2 of 2","start":"b9bb22c36a189968184ed2359181cac601b842f8","phase":"VERIFYING","terminal":"no","window":"2026-10-05T17:04:37Z to 2026-10-06T22:21:58Z","window opened by":"git","window closed by":"last-activity","duration":"105441s","own commits":"47","last own commit":"a9fd99db9e4ae567e27aaaa2e7c423a63b368a21","merged":"no","units served":"13","sources present":"7 of 7","owner turns":"launch 1 · pre-run 4 · in-window 9 · post-close 0","usage main":"requests 293 · in 648 · out 217362 · cache-read 119657232 · cache-write 3580384","usage agent":"requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0","usage workflow":"requests 4344 · in 8688 · out 4167383 · cache-read 1256370107 · cache-write 23684059","attributed calls":"4031 of 5178","values withheld":"0","commitment":"sha256 97b2aea5e8c44c42c1ab486c5b228576b0b5396b4a87d2838564911e93f02f4a · lines 326"},"tables":[]},
"Timeline":{"facts":{"events":"85 · shown 60 · elided 25","elided":"25 events from 2026-10-05T21:30:28Z to 2026-10-06T05:08:51Z","withheld rows":"verb 123 · push 40 · push-refused 0 · gate 0 · compact 1 · limit 3 · idle 0 · workflow 23"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-10-05T17:04:37Z","run-state","phase","018b5675727d","RUNNING","-","-"],
["2026-10-05T17:05:33Z","run-state","phase","b9bb22c36a18","SPECCING","-","-"],
["2026-10-05T17:38:58Z","git","commit","43bdf3aef8c1","-","-","TOOL-aGraftedHelix-29"],
["2026-10-05T17:40:36Z","git","commit","1b53b54b8fca","-","-","TOOL-aGraftedHelix-30 TOOL-aGraftedHelix-31 TOOL-aGraftedHelix-32"],
["2026-10-05T17:42:10Z","run-state","phase","7dca26485330","BUILDING","-","-"],
["2026-10-05T17:43:49Z","run-state","brief","TOOL-aGraftedHelix-29","-","-","-"],
["2026-10-05T17:49:32Z","run-state","dispatch","TOOL-aGraftedHelix-29","-","-","-"],
["2026-10-05T17:52:05Z","git","commit","f5ee092858da","-","-","TOOL-aGraftedHelix-29"],
["2026-10-05T18:07:47Z","git","commit","d52f0edea3c9","-","-","TOOL-aGraftedHelix-29"],
["2026-10-05T18:10:31Z","git","commit","f7a0f089948d","-","-","TOOL-aGraftedHelix-29"],
["2026-10-05T18:12:21Z","git","commit","65b4548763c1","-","-","TOOL-aGraftedHelix-29"],
["2026-10-05T18:18:18Z","run-state","brief","TOOL-aGraftedHelix-30","-","-","-"],
["2026-10-05T18:19:16Z","run-state","dispatch","TOOL-aGraftedHelix-30","-","-","-"],
["2026-10-05T18:32:20Z","git","commit","99b5dac28334","-","-","TOOL-aGraftedHelix-30"],
["2026-10-05T18:37:30Z","git","commit","c54278c13129","-","-","TOOL-aGraftedHelix-30"],
["2026-10-05T18:41:49Z","run-state","brief","TOOL-aGraftedHelix-31","-","-","-"],
["2026-10-05T18:43:22Z","run-state","dispatch","TOOL-aGraftedHelix-31","-","-","-"],
["2026-10-05T19:22:39Z","git","commit","d65ee07d8958","-","-","TOOL-aGraftedHelix-31"],
["2026-10-05T19:24:58Z","git","commit","744fd3560dc1","-","-","TOOL-aGraftedHelix-31"],
["2026-10-05T19:38:59Z","run-state","brief","TOOL-aGraftedHelix-32","-","-","-"],
["2026-10-05T19:40:52Z","run-state","dispatch","TOOL-aGraftedHelix-32","-","-","-"],
["2026-10-05T20:23:32Z","git","commit","28f063c242e5","-","-","TOOL-aGraftedHelix-32"],
["2026-10-05T20:34:57Z","git","commit","a6de788a259f","-","-","TOOL-aGraftedHelix-32"],
["2026-10-05T20:37:37Z","git","commit","525079d4ed38","-","-","TOOL-aGraftedHelix-32"],
["2026-10-05T20:41:41Z","git","commit","bdc93251c03d","-","-","TOOL-aGraftedHelix-32"],
["2026-10-05T21:08:08Z","git","commit","0bc5f0f87c56","-","-","TOOL-aGraftedHelix-33"],
["2026-10-05T21:09:13Z","run-state","brief","TOOL-aGraftedHelix-33","-","-","-"],
["2026-10-05T21:09:48Z","run-state","dispatch","TOOL-aGraftedHelix-33","-","-","-"],
["2026-10-05T21:25:51Z","git","commit","843d5c0b3495","-","-","TOOL-aGraftedHelix-33"],
["2026-10-05T21:27:13Z","git","commit","4b21bbd7a885","-","-","TOOL-aGraftedHelix-33"]]},
{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-10-06T05:13:18Z","git","commit","897f1ecf42be","-","-","TOOL-aGraftedHelix-37"],
["2026-10-06T05:16:49Z","git","commit","071c32bce76b","-","-","TOOL-aGraftedHelix-37"],
["2026-10-06T05:19:15Z","run-state","phase","071c32bce76b","VERIFYING","-","-"],
["2026-10-06T10:57:31Z","git","commit","7db5d7a8b2d5","-","-","TOOL-aGraftedHelix-38"],
["2026-10-06T10:58:56Z","run-state","brief","TOOL-aGraftedHelix-38","-","-","-"],
["2026-10-06T10:59:44Z","run-state","dispatch","TOOL-aGraftedHelix-38","-","-","-"],
["2026-10-06T11:06:45Z","run-state","dispatch","TOOL-aGraftedHelix-38","-","-","-"],
["2026-10-06T11:17:04Z","git","commit","333160ad3655","-","-","TOOL-aGraftedHelix-38"],
["2026-10-06T11:30:24Z","run-state","dispatch","TOOL-aGraftedHelix-38","-","-","-"],
["2026-10-06T11:30:30Z","git","commit","bc3f3ab0cb01","-","-","TOOL-aGraftedHelix-38"],
["2026-10-06T11:43:58Z","git","commit","693c58df808c","-","-","TOOL-aGraftedHelix-38"],
["2026-10-06T12:12:18Z","git","commit","b32773b58e73","-","-","TOOL-aGraftedHelix-39"],
["2026-10-06T12:13:45Z","run-state","brief","TOOL-aGraftedHelix-39","-","-","-"],
["2026-10-06T12:14:27Z","run-state","dispatch","TOOL-aGraftedHelix-39","-","-","-"],
["2026-10-06T12:20:34Z","run-state","dispatch","TOOL-aGraftedHelix-39","-","-","-"],
["2026-10-06T12:51:39Z","git","commit","838bb8238356","-","-","TOOL-aGraftedHelix-39"],
["2026-10-06T12:54:43Z","git","commit","b04ab0da05b7","-","-","TOOL-aGraftedHelix-39"],
["2026-10-06T19:48:38Z","git","commit","9323a3ef55d1","-","-","TOOL-aGraftedHelix-40 TOOL-aGraftedHelix-41"],
["2026-10-06T20:00:45Z","run-state","brief","TOOL-aGraftedHelix-40","-","-","-"],
["2026-10-06T20:02:11Z","run-state","dispatch","TOOL-aGraftedHelix-40","-","-","-"],
["2026-10-06T20:05:15Z","run-state","dispatch","TOOL-aGraftedHelix-40","-","-","-"],
["2026-10-06T20:15:23Z","git","merge","c849b65e10e9","-","-","-"],
["2026-10-06T20:20:56Z","git","commit","d6d50bf0f00f","-","-","TOOL-aGraftedHelix-40"],
["2026-10-06T20:26:14Z","git","commit","62dc8a6c5346","-","-","TOOL-aGraftedHelix-40"],
["2026-10-06T20:28:39Z","run-state","brief","TOOL-aGraftedHelix-41","-","-","-"],
["2026-10-06T20:30:05Z","run-state","dispatch","TOOL-aGraftedHelix-41","-","-","-"],
["2026-10-06T21:31:37Z","git","commit","183047ecbbfd","-","-","TOOL-aGraftedHelix-41"],
["2026-10-06T21:37:23Z","run-state","dispatch","TOOL-aGraftedHelix-41","-","-","-"],
["2026-10-06T21:39:40Z","git","commit","a0aa627ecfde","-","-","TOOL-aGraftedHelix-41"],
["2026-10-06T22:17:17Z","git","commit","a9fd99db9e4a","-","-","TOOL-aGraftedHelix-41"]]}]},
"Units":{"facts":{"units":"41 · shown 0 · aggregated yes"},"tables":[{"name":"by-status","header":["#","status","units"],"rows":[
["1","CLOSED","41"]]}]},
"Decisions":{"facts":{"entries":"132 · shown 0 · aggregated yes","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 1 · agent-before 35 · agent-inside 44","excluded rows":"proposal 0 · rescope 13 · dispatch 19 · review 1 · brief 13 · hold 0 · resume 0","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","2"],
["2","abort","0"],
["3","override","0"],
["4","waiver","0"],
["5","handoff","0"],
["6","rescope-retire","0"],
["7","rescope-supersede","0"],
["8","rescope-defer","0"],
["9","review","1"],
["10","trailer","47"],
["11","spec-mark","80"],
["12","decision-log","0"],
["13","ledger","2"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-10-06T01:52:42Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"17 · shown 17 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","TOOL-aGraftedHelix-29","MET"],
["2","brief-before-build","TOOL-aGraftedHelix-30","MET"],
["3","brief-before-build","TOOL-aGraftedHelix-31","MET"],
["4","brief-before-build","TOOL-aGraftedHelix-32","MET"],
["5","brief-before-build","TOOL-aGraftedHelix-33","MET"],
["6","brief-before-build","TOOL-aGraftedHelix-34","MET"],
["7","brief-before-build","TOOL-aGraftedHelix-35","MET"],
["8","brief-before-build","TOOL-aGraftedHelix-36","MET"],
["9","brief-before-build","TOOL-aGraftedHelix-37","MET"],
["10","brief-before-build","TOOL-aGraftedHelix-38","MET"],
["11","brief-before-build","TOOL-aGraftedHelix-39","MET"],
["12","brief-before-build","TOOL-aGraftedHelix-40","MET"],
["13","brief-before-build","TOOL-aGraftedHelix-41","MET"],
["14","phases-walked","-","UNJUDGEABLE"],
["15","green-at-close","-","UNJUDGEABLE"],
["16","keepalive-reaped","-","MET"],
["17","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"10 · shown 10 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","out-of-band-edit","-"],
["2","refusal-loop","-"],
["3","destructive-git","-"],
["4","destructive-git","-"],
["5","destructive-git","-"],
["6","destructive-git","-"],
["7","destructive-git","-"],
["8","destructive-git","-"],
["9","destructive-git","-"],
["10","destructive-git","-"]]}]},
"Coverage":{"facts":{"journal starts":"2 joined of 3 record-creating","unjoined starts":"1","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 1","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","246","0"],
["3","gates","present","0","0"],
["4","pushes","present","40","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
