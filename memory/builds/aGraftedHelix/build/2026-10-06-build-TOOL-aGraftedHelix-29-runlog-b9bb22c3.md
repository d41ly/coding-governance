# Run record

**Serves:** journal TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-29..41 TOOL-aGraftedHelix-45..47

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aGraftedHelix/RUN.md
- run: 2 of 2
- start: b9bb22c36a189968184ed2359181cac601b842f8
- phase: VERIFYING
- terminal: no
- window: 2026-10-05T17:04:37Z to 2026-10-07T01:28:39Z
- window opened by: git
- window closed by: last-activity
- duration: 116642s
- own commits: 62
- last own commit: 85313733ec9acce7ac17fa66a4d068357f6032ec
- merged: no
- units served: 17
- sources present: 7 of 7
- owner turns: launch 2 · pre-run 7 · in-window 16 · post-close 0
- usage main: requests 901 · in 2006 · out 573265 · cache-read 479599578 · cache-write 6985332
- usage agent: requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0
- usage workflow: requests 8627 · in 17258 · out 7500833 · cache-read 2027929754 · cache-write 45395442
- attributed calls: 4685 of 10611
- values withheld: 0
- commitment: sha256 83d56aba4727675aaf0e858d0cf778eae4b45a913ada64abcaaec45eba409f9c · lines 486

## Timeline

- events: 115 · shown 60 · elided 55
- elided: 55 events from 2026-10-05T21:30:28Z to 2026-10-06T21:39:40Z
- withheld rows: verb 186 · push 56 · push-refused 0 · gate 2 · compact 2 · limit 3 · idle 0 · workflow 81

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
| 2026-10-06T22:17:17Z | git | commit | a9fd99db9e4a | - | - | TOOL-aGraftedHelix-41 |
| 2026-10-06T22:22:56Z | git | merge | d9ed9da3dc76 | - | - | - |
| 2026-10-06T22:29:59Z | git | merge | 1e027341830e | - | - | - |
| 2026-10-06T22:34:53Z | run-state | phase | fff8b6422bdb | HELD | - | - |
| 2026-10-06T22:41:41Z | run-state | phase | e1f4d8c0c6ab | VERIFYING | - | - |
| 2026-10-06T23:11:57Z | git | commit | e5e035fa7abe | - | - | TOOL-aGraftedHelix-45 TOOL-aGraftedHelix-46 TOOL-aGraftedHelix-47 |
| 2026-10-06T23:15:03Z | run-state | brief | TOOL-aGraftedHelix-45 | - | - | - |
| 2026-10-06T23:16:34Z | git | commit | fe49f33d088e | - | - | TOOL-aGraftedHelix-46 |
| 2026-10-06T23:23:45Z | run-state | dispatch | TOOL-aGraftedHelix-45 | - | - | - |
| 2026-10-06T23:37:29Z | run-state | dispatch | TOOL-aGraftedHelix-45 | - | - | - |
| 2026-10-06T23:48:13Z | git | commit | 764b6d8cece5 | - | - | TOOL-aGraftedHelix-45 |
| 2026-10-06T23:56:35Z | git | commit | 4f3270dd624e | - | - | TOOL-aGraftedHelix-45 |
| 2026-10-07T00:05:04Z | git | commit | 928281475211 | - | - | TOOL-aGraftedHelix-45 |
| 2026-10-07T00:11:17Z | run-state | dispatch | TOOL-aGraftedHelix-45 | - | - | - |
| 2026-10-07T00:12:12Z | git | commit | bf3f684805c7 | - | - | TOOL-aGraftedHelix-45 |
| 2026-10-07T00:15:08Z | git | commit | afb3574e83a4 | - | - | TOOL-aGraftedHelix-45 |
| 2026-10-07T00:22:39Z | git | commit | 3bad769b9d1b | - | - | TOOL-aGraftedHelix-3 |
| 2026-10-07T00:24:43Z | run-state | brief | TOOL-aGraftedHelix-46 | - | - | - |
| 2026-10-07T00:26:45Z | run-state | dispatch | TOOL-aGraftedHelix-46 | - | - | - |
| 2026-10-07T00:30:52Z | git | commit | c39267032007 | - | - | TOOL-aGraftedHelix-46 |
| 2026-10-07T00:36:16Z | git | commit | a28075622590 | - | - | TOOL-aGraftedHelix-46 |
| 2026-10-07T00:40:46Z | git | commit | 4fc54f774822 | - | - | TOOL-aGraftedHelix-46 |
| 2026-10-07T00:43:11Z | run-state | brief | TOOL-aGraftedHelix-47 | - | - | - |
| 2026-10-07T00:45:41Z | run-state | dispatch | TOOL-aGraftedHelix-47 | - | - | - |
| 2026-10-07T00:53:28Z | run-state | dispatch | TOOL-aGraftedHelix-47 | - | - | - |
| 2026-10-07T01:22:55Z | run-state | dispatch | TOOL-aGraftedHelix-47 | - | - | - |
| 2026-10-07T01:28:39Z | git | commit | 7d7e957493fc | - | - | TOOL-aGraftedHelix-47 |
| 2026-10-07T01:32:01Z | git | commit | 311cd19af92c | - | - | TOOL-aGraftedHelix-47 |
| 2026-10-07T01:37:46Z | git | commit | 9fcb70037c78 | - | - | TOOL-aGraftedHelix-47 |
| 2026-10-07T01:54:00Z | git | commit | 85313733ec9a | - | - | TOOL-aGraftedHelix-47 |

## Units

- units: 44 · shown 0 · aggregated yes

| # | status | units |
|---|---|---|
| 1 | CLOSED | 44 |

## Decisions

- entries: 154 · shown 0 · aggregated yes
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 1 · agent-before 35 · agent-inside 49
- excluded rows: proposal 0 · rescope 16 · dispatch 26 · review 1 · brief 16 · hold 1 · resume 1
- review rounds: 1 · shown 1 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 4 |
| 2 | abort | 0 |
| 3 | override | 0 |
| 4 | waiver | 0 |
| 5 | handoff | 1 |
| 6 | rescope-retire | 0 |
| 7 | rescope-supersede | 0 |
| 8 | rescope-defer | 0 |
| 9 | review | 1 |
| 10 | trailer | 60 |
| 11 | spec-mark | 85 |
| 12 | decision-log | 0 |
| 13 | ledger | 3 |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-10-06T01:52:42Z | CLEAN WITH FIXES | 0 | CONVERGED |

## Conformance

- items: 20 · shown 20 · aggregated no

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
| 14 | brief-before-build | TOOL-aGraftedHelix-45 | MET |
| 15 | brief-before-build | TOOL-aGraftedHelix-46 | MET |
| 16 | brief-before-build | TOOL-aGraftedHelix-47 | MET |
| 17 | phases-walked | - | UNJUDGEABLE |
| 18 | green-at-close | - | UNJUDGEABLE |
| 19 | keepalive-reaped | - | MET |
| 20 | review-exited | - | MET |

## Anomalies

- anomalies: 43 · shown 0 · aggregated yes

| # | kind | subclass | count |
|---|---|---|---|
| 1 | out-of-band-edit | - | 1 |
| 2 | refusal-loop | - | 1 |
| 3 | destructive-git | - | 32 |
| 4 | multi-run-session | - | 9 |

## Coverage

- journal starts: 2 joined of 3 record-creating
- unjoined starts: 1
- sessions: 2 named · 2 extracted
- idle gaps: judged yes · near an owner turn 0
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 372 | 0 |
| 3 | gates | present | 2 | 0 |
| 4 | pushes | present | 56 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aGraftedHelix/RUN.md","run":"2 of 2","start":"b9bb22c36a189968184ed2359181cac601b842f8","phase":"VERIFYING","terminal":"no","window":"2026-10-05T17:04:37Z to 2026-10-07T01:28:39Z","window opened by":"git","window closed by":"last-activity","duration":"116642s","own commits":"62","last own commit":"85313733ec9acce7ac17fa66a4d068357f6032ec","merged":"no","units served":"17","sources present":"7 of 7","owner turns":"launch 2 · pre-run 7 · in-window 16 · post-close 0","usage main":"requests 901 · in 2006 · out 573265 · cache-read 479599578 · cache-write 6985332","usage agent":"requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0","usage workflow":"requests 8627 · in 17258 · out 7500833 · cache-read 2027929754 · cache-write 45395442","attributed calls":"4685 of 10611","values withheld":"0","commitment":"sha256 83d56aba4727675aaf0e858d0cf778eae4b45a913ada64abcaaec45eba409f9c · lines 486"},"tables":[]},
"Timeline":{"facts":{"events":"115 · shown 60 · elided 55","elided":"55 events from 2026-10-05T21:30:28Z to 2026-10-06T21:39:40Z","withheld rows":"verb 186 · push 56 · push-refused 0 · gate 2 · compact 2 · limit 3 · idle 0 · workflow 81"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
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
["2026-10-06T22:17:17Z","git","commit","a9fd99db9e4a","-","-","TOOL-aGraftedHelix-41"],
["2026-10-06T22:22:56Z","git","merge","d9ed9da3dc76","-","-","-"],
["2026-10-06T22:29:59Z","git","merge","1e027341830e","-","-","-"],
["2026-10-06T22:34:53Z","run-state","phase","fff8b6422bdb","HELD","-","-"],
["2026-10-06T22:41:41Z","run-state","phase","e1f4d8c0c6ab","VERIFYING","-","-"],
["2026-10-06T23:11:57Z","git","commit","e5e035fa7abe","-","-","TOOL-aGraftedHelix-45 TOOL-aGraftedHelix-46 TOOL-aGraftedHelix-47"],
["2026-10-06T23:15:03Z","run-state","brief","TOOL-aGraftedHelix-45","-","-","-"],
["2026-10-06T23:16:34Z","git","commit","fe49f33d088e","-","-","TOOL-aGraftedHelix-46"],
["2026-10-06T23:23:45Z","run-state","dispatch","TOOL-aGraftedHelix-45","-","-","-"],
["2026-10-06T23:37:29Z","run-state","dispatch","TOOL-aGraftedHelix-45","-","-","-"],
["2026-10-06T23:48:13Z","git","commit","764b6d8cece5","-","-","TOOL-aGraftedHelix-45"],
["2026-10-06T23:56:35Z","git","commit","4f3270dd624e","-","-","TOOL-aGraftedHelix-45"],
["2026-10-07T00:05:04Z","git","commit","928281475211","-","-","TOOL-aGraftedHelix-45"],
["2026-10-07T00:11:17Z","run-state","dispatch","TOOL-aGraftedHelix-45","-","-","-"],
["2026-10-07T00:12:12Z","git","commit","bf3f684805c7","-","-","TOOL-aGraftedHelix-45"],
["2026-10-07T00:15:08Z","git","commit","afb3574e83a4","-","-","TOOL-aGraftedHelix-45"],
["2026-10-07T00:22:39Z","git","commit","3bad769b9d1b","-","-","TOOL-aGraftedHelix-3"],
["2026-10-07T00:24:43Z","run-state","brief","TOOL-aGraftedHelix-46","-","-","-"],
["2026-10-07T00:26:45Z","run-state","dispatch","TOOL-aGraftedHelix-46","-","-","-"],
["2026-10-07T00:30:52Z","git","commit","c39267032007","-","-","TOOL-aGraftedHelix-46"],
["2026-10-07T00:36:16Z","git","commit","a28075622590","-","-","TOOL-aGraftedHelix-46"],
["2026-10-07T00:40:46Z","git","commit","4fc54f774822","-","-","TOOL-aGraftedHelix-46"],
["2026-10-07T00:43:11Z","run-state","brief","TOOL-aGraftedHelix-47","-","-","-"],
["2026-10-07T00:45:41Z","run-state","dispatch","TOOL-aGraftedHelix-47","-","-","-"],
["2026-10-07T00:53:28Z","run-state","dispatch","TOOL-aGraftedHelix-47","-","-","-"],
["2026-10-07T01:22:55Z","run-state","dispatch","TOOL-aGraftedHelix-47","-","-","-"],
["2026-10-07T01:28:39Z","git","commit","7d7e957493fc","-","-","TOOL-aGraftedHelix-47"],
["2026-10-07T01:32:01Z","git","commit","311cd19af92c","-","-","TOOL-aGraftedHelix-47"],
["2026-10-07T01:37:46Z","git","commit","9fcb70037c78","-","-","TOOL-aGraftedHelix-47"],
["2026-10-07T01:54:00Z","git","commit","85313733ec9a","-","-","TOOL-aGraftedHelix-47"]]}]},
"Units":{"facts":{"units":"44 · shown 0 · aggregated yes"},"tables":[{"name":"by-status","header":["#","status","units"],"rows":[
["1","CLOSED","44"]]}]},
"Decisions":{"facts":{"entries":"154 · shown 0 · aggregated yes","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 1 · agent-before 35 · agent-inside 49","excluded rows":"proposal 0 · rescope 16 · dispatch 26 · review 1 · brief 16 · hold 1 · resume 1","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","4"],
["2","abort","0"],
["3","override","0"],
["4","waiver","0"],
["5","handoff","1"],
["6","rescope-retire","0"],
["7","rescope-supersede","0"],
["8","rescope-defer","0"],
["9","review","1"],
["10","trailer","60"],
["11","spec-mark","85"],
["12","decision-log","0"],
["13","ledger","3"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-10-06T01:52:42Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"20 · shown 20 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
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
["14","brief-before-build","TOOL-aGraftedHelix-45","MET"],
["15","brief-before-build","TOOL-aGraftedHelix-46","MET"],
["16","brief-before-build","TOOL-aGraftedHelix-47","MET"],
["17","phases-walked","-","UNJUDGEABLE"],
["18","green-at-close","-","UNJUDGEABLE"],
["19","keepalive-reaped","-","MET"],
["20","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"43 · shown 0 · aggregated yes"},"tables":[{"name":"by-kind","header":["#","kind","subclass","count"],"rows":[
["1","out-of-band-edit","-","1"],
["2","refusal-loop","-","1"],
["3","destructive-git","-","32"],
["4","multi-run-session","-","9"]]}]},
"Coverage":{"facts":{"journal starts":"2 joined of 3 record-creating","unjoined starts":"1","sessions":"2 named · 2 extracted","idle gaps":"judged yes · near an owner turn 0","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","372","0"],
["3","gates","present","2","0"],
["4","pushes","present","56","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
