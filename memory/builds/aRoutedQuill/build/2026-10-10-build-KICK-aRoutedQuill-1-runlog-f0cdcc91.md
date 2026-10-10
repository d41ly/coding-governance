# Run record

**Serves:** journal KICK-aRoutedQuill-1 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-1..5 TOOL-aRoutedQuill-7 TOOL-aRoutedQuill-9..12

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aRoutedQuill/RUN.md
- run: 1 of 1
- start: f0cdcc911ee0b074cfcc5fcb27c61cc2ae0943d7
- phase: VERIFYING
- terminal: no
- window: 2026-10-09T16:38:17Z to 2026-10-10T04:18:02Z
- window opened by: git
- window closed by: last-activity
- duration: 41985s
- own commits: 0
- last own commit: -
- merged: -
- units served: 12
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 0 · in-window 0 · post-close 0
- usage main: requests 226 · in 486 · out 136518 · cache-read 79137847 · cache-write 1425335
- usage agent: requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0
- usage workflow: requests 1739 · in 3478 · out 1395631 · cache-read 342828610 · cache-write 11681820
- attributed calls: 1586 of 2141
- values withheld: 0
- commitment: sha256 2dd04e25adf88539fecdc9f9be35ff1aa2c976137c7cd29a59418a049306325e · lines 229

## Timeline

- events: 33 · shown 33 · elided 0
- withheld rows: verb 100 · push 16 · push-refused 0 · gate 1 · compact 0 · limit 0 · idle 0 · workflow 18

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-10-09T16:38:17Z | run-state | phase | 5a836bf0fc94 | RUNNING | - | - |
| 2026-10-09T17:31:43Z | run-state | dispatch | TOOL-aRoutedQuill-1 | - | - | - |
| 2026-10-09T17:32:27Z | run-state | brief | TOOL-aRoutedQuill-1 | - | - | - |
| 2026-10-09T18:18:55Z | run-state | phase | 06071f441392 | BUILDING | - | - |
| 2026-10-09T18:26:38Z | run-state | dispatch | KICK-aRoutedQuill-1 | - | - | - |
| 2026-10-09T18:27:10Z | run-state | brief | KICK-aRoutedQuill-1 | - | - | - |
| 2026-10-09T19:17:37Z | run-state | dispatch | KICK-aRoutedQuill-1 | - | - | - |
| 2026-10-09T19:25:16Z | run-state | dispatch | KICK-aRoutedQuill-1 | - | - | - |
| 2026-10-09T19:44:24Z | run-state | dispatch | TOOL-aRoutedQuill-2 | - | - | - |
| 2026-10-09T19:45:09Z | run-state | brief | TOOL-aRoutedQuill-2 | - | - | - |
| 2026-10-09T20:26:55Z | run-state | brief | TOOL-aRoutedQuill-3 | - | - | - |
| 2026-10-09T20:51:48Z | run-state | dispatch | TOOL-aRoutedQuill-3 | - | - | - |
| 2026-10-09T21:16:55Z | run-state | dispatch | TOOL-aRoutedQuill-3 | - | - | - |
| 2026-10-09T21:37:58Z | run-state | brief | TOOL-aRoutedQuill-4 | - | - | - |
| 2026-10-09T21:53:14Z | run-state | dispatch | TOOL-aRoutedQuill-4 | - | - | - |
| 2026-10-09T22:42:04Z | run-state | dispatch | PLAY-aRoutedQuill-1 | - | - | - |
| 2026-10-09T22:42:24Z | run-state | brief | PLAY-aRoutedQuill-1 | - | - | - |
| 2026-10-09T23:13:32Z | run-state | brief | TOOL-aRoutedQuill-5 | - | - | - |
| 2026-10-09T23:17:00Z | run-state | dispatch | TOOL-aRoutedQuill-5 | - | - | - |
| 2026-10-09T23:35:39Z | run-state | dispatch | TOOL-aRoutedQuill-5 | - | - | - |
| 2026-10-10T00:55:22Z | run-state | dispatch | TOOL-aRoutedQuill-7 | - | - | - |
| 2026-10-10T00:55:34Z | run-state | brief | TOOL-aRoutedQuill-7 | - | - | - |
| 2026-10-10T02:20:55Z | run-state | phase | ff0b3dc32751 | REVIEWING | - | - |
| 2026-10-10T02:57:36Z | run-state | brief | TOOL-aRoutedQuill-9 | - | - | - |
| 2026-10-10T03:03:10Z | run-state | dispatch | TOOL-aRoutedQuill-9 | - | - | - |
| 2026-10-10T03:11:54Z | run-state | dispatch | TOOL-aRoutedQuill-10 | - | - | - |
| 2026-10-10T03:11:57Z | run-state | brief | TOOL-aRoutedQuill-10 | - | - | - |
| 2026-10-10T03:20:55Z | run-state | brief | TOOL-aRoutedQuill-11 | - | - | - |
| 2026-10-10T03:21:49Z | run-state | dispatch | TOOL-aRoutedQuill-11 | - | - | - |
| 2026-10-10T03:32:04Z | run-state | brief | TOOL-aRoutedQuill-12 | - | - | - |
| 2026-10-10T03:32:54Z | run-state | dispatch | TOOL-aRoutedQuill-12 | - | - | - |
| 2026-10-10T03:43:47Z | run-state | dispatch | TOOL-aRoutedQuill-12 | - | - | - |
| 2026-10-10T04:16:46Z | run-state | phase | 31257756bb5d | VERIFYING | - | - |

## Units

- units: 13 · shown 13 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | TOOL-aRoutedQuill-1 | CLOSED | 0 | 1 | 1 | - |
| 2 | KICK-aRoutedQuill-1 | CLOSED | 0 | 3 | 1 | - |
| 3 | TOOL-aRoutedQuill-2 | CLOSED | 0 | 1 | 1 | - |
| 4 | TOOL-aRoutedQuill-3 | CLOSED | 0 | 2 | 1 | - |
| 4 | TOOL-aRoutedQuill-4 | CLOSED | 0 | 1 | 1 | - |
| 5 | PLAY-aRoutedQuill-1 | CLOSED | 0 | 1 | 1 | - |
| 5 | TOOL-aRoutedQuill-5 | CLOSED | 0 | 2 | 1 | - |
| 6 | TOOL-aRoutedQuill-6 | DEFERRED | 0 | 0 | 0 | - |
| 6 | TOOL-aRoutedQuill-7 | CLOSED | 0 | 1 | 1 | - |
| 6 | TOOL-aRoutedQuill-9 | CLOSED | 0 | 1 | 1 | - |
| 6 | TOOL-aRoutedQuill-10 | CLOSED | 0 | 1 | 1 | - |
| 6 | TOOL-aRoutedQuill-11 | CLOSED | 0 | 1 | 1 | - |
| 6 | TOOL-aRoutedQuill-12 | CLOSED | 0 | 2 | 1 | - |

## Decisions

- entries: 30 · shown 0 · aggregated yes
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 21 · owner-inside 0 · agent-before 0 · agent-inside 6
- excluded rows: proposal 0 · rescope 4 · dispatch 17 · review 2 · brief 12 · hold 0 · resume 0
- review rounds: 2 · shown 2 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 2 |
| 2 | abort | 0 |
| 3 | override | 0 |
| 4 | waiver | 0 |
| 5 | handoff | 0 |
| 6 | rescope-retire | 0 |
| 7 | rescope-supersede | 0 |
| 8 | rescope-defer | 1 |
| 9 | review | 0 |
| 10 | trailer | 0 |
| 11 | spec-mark | 27 |
| 12 | decision-log | 0 |
| 13 | ledger | 0 |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-10-10T02:20:35Z | BLOCKED | 1 | - |
| 2 | 2026-10-10T02:30:08Z | BLOCKED | 1 | NON-CONVERGENT |

## Conformance

- items: 5 · shown 5 · aggregated no

| # | item | unit | state |
|---|---|---|---|
| 1 | brief-before-build | - | UNJUDGEABLE |
| 2 | phases-walked | - | UNJUDGEABLE |
| 3 | green-at-close | - | UNJUDGEABLE |
| 4 | keepalive-reaped | - | MET |
| 5 | review-exited | - | MET |

## Anomalies

- anomalies: 17 · shown 17 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | no-progress | - |
| 2 | out-of-band-edit | - |
| 3 | out-of-band-edit | - |
| 4 | out-of-band-edit | - |
| 5 | refusal-loop | - |
| 6 | refusal-loop | - |
| 7 | killed-verb | - |
| 8 | killed-verb | - |
| 9 | killed-verb | - |
| 10 | killed-verb | - |
| 11 | killed-verb | - |
| 12 | destructive-git | - |
| 13 | destructive-git | - |
| 14 | destructive-git | - |
| 15 | destructive-git | - |
| 16 | destructive-git | - |
| 17 | destructive-git | - |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 0
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 196 | 0 |
| 3 | gates | present | 1 | 0 |
| 4 | pushes | present | 16 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aRoutedQuill/RUN.md","run":"1 of 1","start":"f0cdcc911ee0b074cfcc5fcb27c61cc2ae0943d7","phase":"VERIFYING","terminal":"no","window":"2026-10-09T16:38:17Z to 2026-10-10T04:18:02Z","window opened by":"git","window closed by":"last-activity","duration":"41985s","own commits":"0","last own commit":"-","merged":"-","units served":"12","sources present":"7 of 7","owner turns":"launch 1 · pre-run 0 · in-window 0 · post-close 0","usage main":"requests 226 · in 486 · out 136518 · cache-read 79137847 · cache-write 1425335","usage agent":"requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0","usage workflow":"requests 1739 · in 3478 · out 1395631 · cache-read 342828610 · cache-write 11681820","attributed calls":"1586 of 2141","values withheld":"0","commitment":"sha256 2dd04e25adf88539fecdc9f9be35ff1aa2c976137c7cd29a59418a049306325e · lines 229"},"tables":[]},
"Timeline":{"facts":{"events":"33 · shown 33 · elided 0","withheld rows":"verb 100 · push 16 · push-refused 0 · gate 1 · compact 0 · limit 0 · idle 0 · workflow 18"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-10-09T16:38:17Z","run-state","phase","5a836bf0fc94","RUNNING","-","-"],
["2026-10-09T17:31:43Z","run-state","dispatch","TOOL-aRoutedQuill-1","-","-","-"],
["2026-10-09T17:32:27Z","run-state","brief","TOOL-aRoutedQuill-1","-","-","-"],
["2026-10-09T18:18:55Z","run-state","phase","06071f441392","BUILDING","-","-"],
["2026-10-09T18:26:38Z","run-state","dispatch","KICK-aRoutedQuill-1","-","-","-"],
["2026-10-09T18:27:10Z","run-state","brief","KICK-aRoutedQuill-1","-","-","-"],
["2026-10-09T19:17:37Z","run-state","dispatch","KICK-aRoutedQuill-1","-","-","-"],
["2026-10-09T19:25:16Z","run-state","dispatch","KICK-aRoutedQuill-1","-","-","-"],
["2026-10-09T19:44:24Z","run-state","dispatch","TOOL-aRoutedQuill-2","-","-","-"],
["2026-10-09T19:45:09Z","run-state","brief","TOOL-aRoutedQuill-2","-","-","-"],
["2026-10-09T20:26:55Z","run-state","brief","TOOL-aRoutedQuill-3","-","-","-"],
["2026-10-09T20:51:48Z","run-state","dispatch","TOOL-aRoutedQuill-3","-","-","-"],
["2026-10-09T21:16:55Z","run-state","dispatch","TOOL-aRoutedQuill-3","-","-","-"],
["2026-10-09T21:37:58Z","run-state","brief","TOOL-aRoutedQuill-4","-","-","-"],
["2026-10-09T21:53:14Z","run-state","dispatch","TOOL-aRoutedQuill-4","-","-","-"],
["2026-10-09T22:42:04Z","run-state","dispatch","PLAY-aRoutedQuill-1","-","-","-"],
["2026-10-09T22:42:24Z","run-state","brief","PLAY-aRoutedQuill-1","-","-","-"],
["2026-10-09T23:13:32Z","run-state","brief","TOOL-aRoutedQuill-5","-","-","-"],
["2026-10-09T23:17:00Z","run-state","dispatch","TOOL-aRoutedQuill-5","-","-","-"],
["2026-10-09T23:35:39Z","run-state","dispatch","TOOL-aRoutedQuill-5","-","-","-"],
["2026-10-10T00:55:22Z","run-state","dispatch","TOOL-aRoutedQuill-7","-","-","-"],
["2026-10-10T00:55:34Z","run-state","brief","TOOL-aRoutedQuill-7","-","-","-"],
["2026-10-10T02:20:55Z","run-state","phase","ff0b3dc32751","REVIEWING","-","-"],
["2026-10-10T02:57:36Z","run-state","brief","TOOL-aRoutedQuill-9","-","-","-"],
["2026-10-10T03:03:10Z","run-state","dispatch","TOOL-aRoutedQuill-9","-","-","-"],
["2026-10-10T03:11:54Z","run-state","dispatch","TOOL-aRoutedQuill-10","-","-","-"],
["2026-10-10T03:11:57Z","run-state","brief","TOOL-aRoutedQuill-10","-","-","-"],
["2026-10-10T03:20:55Z","run-state","brief","TOOL-aRoutedQuill-11","-","-","-"],
["2026-10-10T03:21:49Z","run-state","dispatch","TOOL-aRoutedQuill-11","-","-","-"],
["2026-10-10T03:32:04Z","run-state","brief","TOOL-aRoutedQuill-12","-","-","-"],
["2026-10-10T03:32:54Z","run-state","dispatch","TOOL-aRoutedQuill-12","-","-","-"],
["2026-10-10T03:43:47Z","run-state","dispatch","TOOL-aRoutedQuill-12","-","-","-"],
["2026-10-10T04:16:46Z","run-state","phase","31257756bb5d","VERIFYING","-","-"]]}]},
"Units":{"facts":{"units":"13 · shown 13 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","TOOL-aRoutedQuill-1","CLOSED","0","1","1","-"],
["2","KICK-aRoutedQuill-1","CLOSED","0","3","1","-"],
["3","TOOL-aRoutedQuill-2","CLOSED","0","1","1","-"],
["4","TOOL-aRoutedQuill-3","CLOSED","0","2","1","-"],
["4","TOOL-aRoutedQuill-4","CLOSED","0","1","1","-"],
["5","PLAY-aRoutedQuill-1","CLOSED","0","1","1","-"],
["5","TOOL-aRoutedQuill-5","CLOSED","0","2","1","-"],
["6","TOOL-aRoutedQuill-6","DEFERRED","0","0","0","-"],
["6","TOOL-aRoutedQuill-7","CLOSED","0","1","1","-"],
["6","TOOL-aRoutedQuill-9","CLOSED","0","1","1","-"],
["6","TOOL-aRoutedQuill-10","CLOSED","0","1","1","-"],
["6","TOOL-aRoutedQuill-11","CLOSED","0","1","1","-"],
["6","TOOL-aRoutedQuill-12","CLOSED","0","2","1","-"]]}]},
"Decisions":{"facts":{"entries":"30 · shown 0 · aggregated yes","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 21 · owner-inside 0 · agent-before 0 · agent-inside 6","excluded rows":"proposal 0 · rescope 4 · dispatch 17 · review 2 · brief 12 · hold 0 · resume 0","review rounds":"2 · shown 2 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","2"],
["2","abort","0"],
["3","override","0"],
["4","waiver","0"],
["5","handoff","0"],
["6","rescope-retire","0"],
["7","rescope-supersede","0"],
["8","rescope-defer","1"],
["9","review","0"],
["10","trailer","0"],
["11","spec-mark","27"],
["12","decision-log","0"],
["13","ledger","0"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-10-10T02:20:35Z","BLOCKED","1","-"],
["2","2026-10-10T02:30:08Z","BLOCKED","1","NON-CONVERGENT"]]}]},
"Conformance":{"facts":{"items":"5 · shown 5 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","-","UNJUDGEABLE"],
["2","phases-walked","-","UNJUDGEABLE"],
["3","green-at-close","-","UNJUDGEABLE"],
["4","keepalive-reaped","-","MET"],
["5","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"17 · shown 17 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","no-progress","-"],
["2","out-of-band-edit","-"],
["3","out-of-band-edit","-"],
["4","out-of-band-edit","-"],
["5","refusal-loop","-"],
["6","refusal-loop","-"],
["7","killed-verb","-"],
["8","killed-verb","-"],
["9","killed-verb","-"],
["10","killed-verb","-"],
["11","killed-verb","-"],
["12","destructive-git","-"],
["13","destructive-git","-"],
["14","destructive-git","-"],
["15","destructive-git","-"],
["16","destructive-git","-"],
["17","destructive-git","-"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 0","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","196","0"],
["3","gates","present","1","0"],
["4","pushes","present","16","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
