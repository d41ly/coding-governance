# Run record

**Serves:** journal DEPL-aLevelledCopy-1 TOOL-aLevelledCopy-1..3 TOOL-aLevelledCopy-7..9

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aLevelledCopy/RUN.md
- run: 1 of 1
- start: 9380159bf91df98cac62925862565d5d1dc46d7a
- phase: LANDING
- terminal: no
- window: 2026-10-08T22:44:27Z to 2026-10-10T01:18:18Z
- window opened by: git
- window closed by: last-activity
- duration: 95631s
- own commits: 18
- last own commit: 669816ae7e72b035e7cf7566b839b3b0afd99f42
- merged: yes
- units served: 7
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 0 · in-window 6 · post-close 0
- usage main: requests 299 · in 676 · out 154428 · cache-read 150799438 · cache-write 4457419
- usage agent: requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0
- usage workflow: requests 891 · in 1782 · out 812371 · cache-read 139626926 · cache-write 6624366
- attributed calls: 1076 of 1291
- values withheld: 0
- commitment: sha256 14f9867ffdbd7bfa8f800eec269898eb85705ac813d25c3ee1c6bda2d24d124e · lines 391

## Timeline

- events: 49 · shown 49 · elided 0
- withheld rows: verb 150 · push 51 · push-refused 0 · gate 9 · compact 0 · limit 0 · idle 4 · workflow 12

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-10-08T22:44:27Z | run-state | phase | ce9192c0ba18 | RUNNING | - | - |
| 2026-10-08T23:24:58Z | git | commit | 6e7b81081d4c | - | - | DEPL-aLevelledCopy-1 TOOL-aLevelledCopy-1 |
| 2026-10-08T23:29:09Z | run-state | phase | 6e7b81081d4c | SPECCING | - | - |
| 2026-10-08T23:33:05Z | run-state | phase | f405a8368e11 | BUILDING | - | - |
| 2026-10-08T23:41:01Z | run-state | dispatch | DEPL-aLevelledCopy-1 | - | - | - |
| 2026-10-08T23:42:10Z | run-state | brief | DEPL-aLevelledCopy-1 | - | - | - |
| 2026-10-09T00:17:36Z | run-state | dispatch | DEPL-aLevelledCopy-1 | - | - | - |
| 2026-10-09T00:18:16Z | git | commit | 7ab080afd903 | - | - | DEPL-aLevelledCopy-1 |
| 2026-10-09T00:25:29Z | git | commit | 53a8cc080cda | - | - | DEPL-aLevelledCopy-1 |
| 2026-10-09T00:33:36Z | run-state | brief | TOOL-aLevelledCopy-1 | - | - | - |
| 2026-10-09T00:40:31Z | run-state | dispatch | TOOL-aLevelledCopy-1 | - | - | - |
| 2026-10-09T00:52:21Z | git | commit | 961a1cbb7d11 | - | - | TOOL-aLevelledCopy-1 |
| 2026-10-09T00:58:49Z | git | commit | 5eac1decfbda | - | - | TOOL-aLevelledCopy-1 |
| 2026-10-09T01:05:20Z | git | commit | ff49508faf93 | - | - | TOOL-aLevelledCopy-1 |
| 2026-10-09T01:17:17Z | run-state | dispatch | TOOL-aLevelledCopy-2 | - | - | - |
| 2026-10-09T01:18:12Z | run-state | brief | TOOL-aLevelledCopy-2 | - | - | - |
| 2026-10-09T01:57:51Z | run-state | dispatch | TOOL-aLevelledCopy-2 | - | - | - |
| 2026-10-09T01:58:13Z | git | commit | c82936e23438 | - | - | TOOL-aLevelledCopy-2 |
| 2026-10-09T02:05:18Z | git | commit | 33a15c879a11 | - | - | TOOL-aLevelledCopy-2 |
| 2026-10-09T02:11:59Z | run-state | brief | TOOL-aLevelledCopy-3 | - | - | - |
| 2026-10-09T02:14:43Z | run-state | dispatch | TOOL-aLevelledCopy-3 | - | - | - |
| 2026-10-09T02:48:35Z | run-state | dispatch | TOOL-aLevelledCopy-3 | - | - | - |
| 2026-10-09T02:55:52Z | run-state | dispatch | TOOL-aLevelledCopy-3 | - | - | - |
| 2026-10-09T03:01:25Z | run-state | dispatch | TOOL-aLevelledCopy-3 | - | - | - |
| 2026-10-09T03:01:44Z | git | commit | 788a74b79c8e | - | - | TOOL-aLevelledCopy-3 |
| 2026-10-09T03:10:44Z | git | commit | bb6178eab4ef | - | - | TOOL-aLevelledCopy-3 |
| 2026-10-09T03:21:24Z | run-state | phase | bb6178eab4ef | REVIEWING | - | - |
| 2026-10-09T04:11:53Z | git | commit | 4f0eec36de8e | - | - | TOOL-aLevelledCopy-7 TOOL-aLevelledCopy-8 TOOL-aLevelledCopy-9 |
| 2026-10-09T04:19:16Z | git | commit | 176005b62ce6 | - | - | TOOL-aLevelledCopy-9 |
| 2026-10-09T04:26:05Z | run-state | dispatch | TOOL-aLevelledCopy-7 | - | - | - |
| 2026-10-09T04:26:34Z | run-state | brief | TOOL-aLevelledCopy-7 | - | - | - |
| 2026-10-09T04:40:54Z | git | commit | 7779b08e7ed4 | - | - | TOOL-aLevelledCopy-7 |
| 2026-10-09T04:42:57Z | git | commit | dae09ec1f1ce | - | - | TOOL-aLevelledCopy-7 |
| 2026-10-09T04:47:58Z | run-state | brief | TOOL-aLevelledCopy-9 | - | - | - |
| 2026-10-09T04:52:36Z | run-state | dispatch | TOOL-aLevelledCopy-9 | - | - | - |
| 2026-10-09T05:02:14Z | git | commit | b9a11b433a2c | - | - | TOOL-aLevelledCopy-9 |
| 2026-10-09T05:05:05Z | git | commit | 0a09d7a09e55 | - | - | TOOL-aLevelledCopy-9 |
| 2026-10-09T05:09:54Z | run-state | dispatch | TOOL-aLevelledCopy-8 | - | - | - |
| 2026-10-09T05:10:13Z | run-state | brief | TOOL-aLevelledCopy-8 | - | - | - |
| 2026-10-09T05:40:18Z | git | commit | 41331dbceb3a | - | - | TOOL-aLevelledCopy-8 |
| 2026-10-09T05:44:56Z | git | commit | 669816ae7e72 | - | - | TOOL-aLevelledCopy-8 |
| 2026-10-09T06:08:39Z | run-state | phase | 79126924852f | VERIFYING | - | - |
| 2026-10-09T06:16:57Z | git | merge | c79047d89f43 | - | - | - |
| 2026-10-09T13:34:41Z | git | merge | 82fe6eb763d3 | - | - | - |
| 2026-10-09T13:50:10Z | git | merge | 5a836bf0fc94 | - | - | - |
| 2026-10-09T14:44:25Z | git | merge | 295e6bee4df9 | - | - | - |
| 2026-10-09T15:47:14Z | git | merge | 3459008235d8 | - | - | - |
| 2026-10-09T23:18:49Z | git | merge | c41dcd03951d | - | - | - |
| 2026-10-10T01:18:18Z | run-state | phase | 79126924852f | LANDING | - | - |

## Units

- units: 7 · shown 7 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | DEPL-aLevelledCopy-1 | CLOSED | 3 | 2 | 1 | 7ab080afd903 |
| 1 | TOOL-aLevelledCopy-1 | CLOSED | 4 | 1 | 1 | 961a1cbb7d11 |
| 1 | TOOL-aLevelledCopy-2 | CLOSED | 2 | 2 | 1 | c82936e23438 |
| 2 | TOOL-aLevelledCopy-3 | CLOSED | 2 | 4 | 1 | 788a74b79c8e |
| 3 | TOOL-aLevelledCopy-7 | CLOSED | 3 | 1 | 1 | 7779b08e7ed4 |
| 3 | TOOL-aLevelledCopy-9 | CLOSED | 4 | 1 | 1 | b9a11b433a2c |
| 4 | TOOL-aLevelledCopy-8 | CLOSED | 3 | 1 | 1 | 41331dbceb3a |

## Decisions

- entries: 37 · shown 0 · aggregated yes
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 14
- excluded rows: proposal 0 · rescope 3 · dispatch 12 · review 1 · brief 7 · hold 0 · resume 1
- review rounds: 1 · shown 1 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 0 |
| 2 | abort | 0 |
| 3 | override | 0 |
| 4 | waiver | 0 |
| 5 | handoff | 0 |
| 6 | rescope-retire | 0 |
| 7 | rescope-supersede | 0 |
| 8 | rescope-defer | 0 |
| 9 | review | 1 |
| 10 | trailer | 22 |
| 11 | spec-mark | 14 |
| 12 | decision-log | 0 |
| 13 | ledger | 0 |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-10-09T03:40:59Z | CLEAN WITH FIXES | 0 | CONVERGED |

## Conformance

- items: 11 · shown 11 · aggregated no

| # | item | unit | state |
|---|---|---|---|
| 1 | brief-before-build | DEPL-aLevelledCopy-1 | MET |
| 2 | brief-before-build | TOOL-aLevelledCopy-1 | MET |
| 3 | brief-before-build | TOOL-aLevelledCopy-2 | MET |
| 4 | brief-before-build | TOOL-aLevelledCopy-3 | MET |
| 5 | brief-before-build | TOOL-aLevelledCopy-7 | MET |
| 6 | brief-before-build | TOOL-aLevelledCopy-8 | MET |
| 7 | brief-before-build | TOOL-aLevelledCopy-9 | MET |
| 8 | phases-walked | - | MET |
| 9 | green-at-close | - | UNMET |
| 10 | keepalive-reaped | - | MET |
| 11 | review-exited | - | MET |

## Anomalies

- anomalies: 37 · shown 0 · aggregated yes

| # | kind | subclass | count |
|---|---|---|---|
| 1 | nonterminal-merged | refused-landing | 1 |
| 2 | out-of-band-edit | - | 6 |
| 3 | refusal-loop | - | 2 |
| 4 | killed-verb | - | 21 |
| 5 | destructive-git | - | 3 |
| 6 | idle-gap | - | 4 |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 0
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 280 | 0 |
| 3 | gates | present | 9 | 0 |
| 4 | pushes | present | 51 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aLevelledCopy/RUN.md","run":"1 of 1","start":"9380159bf91df98cac62925862565d5d1dc46d7a","phase":"LANDING","terminal":"no","window":"2026-10-08T22:44:27Z to 2026-10-10T01:18:18Z","window opened by":"git","window closed by":"last-activity","duration":"95631s","own commits":"18","last own commit":"669816ae7e72b035e7cf7566b839b3b0afd99f42","merged":"yes","units served":"7","sources present":"7 of 7","owner turns":"launch 1 · pre-run 0 · in-window 6 · post-close 0","usage main":"requests 299 · in 676 · out 154428 · cache-read 150799438 · cache-write 4457419","usage agent":"requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0","usage workflow":"requests 891 · in 1782 · out 812371 · cache-read 139626926 · cache-write 6624366","attributed calls":"1076 of 1291","values withheld":"0","commitment":"sha256 14f9867ffdbd7bfa8f800eec269898eb85705ac813d25c3ee1c6bda2d24d124e · lines 391"},"tables":[]},
"Timeline":{"facts":{"events":"49 · shown 49 · elided 0","withheld rows":"verb 150 · push 51 · push-refused 0 · gate 9 · compact 0 · limit 0 · idle 4 · workflow 12"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-10-08T22:44:27Z","run-state","phase","ce9192c0ba18","RUNNING","-","-"],
["2026-10-08T23:24:58Z","git","commit","6e7b81081d4c","-","-","DEPL-aLevelledCopy-1 TOOL-aLevelledCopy-1"],
["2026-10-08T23:29:09Z","run-state","phase","6e7b81081d4c","SPECCING","-","-"],
["2026-10-08T23:33:05Z","run-state","phase","f405a8368e11","BUILDING","-","-"],
["2026-10-08T23:41:01Z","run-state","dispatch","DEPL-aLevelledCopy-1","-","-","-"],
["2026-10-08T23:42:10Z","run-state","brief","DEPL-aLevelledCopy-1","-","-","-"],
["2026-10-09T00:17:36Z","run-state","dispatch","DEPL-aLevelledCopy-1","-","-","-"],
["2026-10-09T00:18:16Z","git","commit","7ab080afd903","-","-","DEPL-aLevelledCopy-1"],
["2026-10-09T00:25:29Z","git","commit","53a8cc080cda","-","-","DEPL-aLevelledCopy-1"],
["2026-10-09T00:33:36Z","run-state","brief","TOOL-aLevelledCopy-1","-","-","-"],
["2026-10-09T00:40:31Z","run-state","dispatch","TOOL-aLevelledCopy-1","-","-","-"],
["2026-10-09T00:52:21Z","git","commit","961a1cbb7d11","-","-","TOOL-aLevelledCopy-1"],
["2026-10-09T00:58:49Z","git","commit","5eac1decfbda","-","-","TOOL-aLevelledCopy-1"],
["2026-10-09T01:05:20Z","git","commit","ff49508faf93","-","-","TOOL-aLevelledCopy-1"],
["2026-10-09T01:17:17Z","run-state","dispatch","TOOL-aLevelledCopy-2","-","-","-"],
["2026-10-09T01:18:12Z","run-state","brief","TOOL-aLevelledCopy-2","-","-","-"],
["2026-10-09T01:57:51Z","run-state","dispatch","TOOL-aLevelledCopy-2","-","-","-"],
["2026-10-09T01:58:13Z","git","commit","c82936e23438","-","-","TOOL-aLevelledCopy-2"],
["2026-10-09T02:05:18Z","git","commit","33a15c879a11","-","-","TOOL-aLevelledCopy-2"],
["2026-10-09T02:11:59Z","run-state","brief","TOOL-aLevelledCopy-3","-","-","-"],
["2026-10-09T02:14:43Z","run-state","dispatch","TOOL-aLevelledCopy-3","-","-","-"],
["2026-10-09T02:48:35Z","run-state","dispatch","TOOL-aLevelledCopy-3","-","-","-"],
["2026-10-09T02:55:52Z","run-state","dispatch","TOOL-aLevelledCopy-3","-","-","-"],
["2026-10-09T03:01:25Z","run-state","dispatch","TOOL-aLevelledCopy-3","-","-","-"],
["2026-10-09T03:01:44Z","git","commit","788a74b79c8e","-","-","TOOL-aLevelledCopy-3"],
["2026-10-09T03:10:44Z","git","commit","bb6178eab4ef","-","-","TOOL-aLevelledCopy-3"],
["2026-10-09T03:21:24Z","run-state","phase","bb6178eab4ef","REVIEWING","-","-"],
["2026-10-09T04:11:53Z","git","commit","4f0eec36de8e","-","-","TOOL-aLevelledCopy-7 TOOL-aLevelledCopy-8 TOOL-aLevelledCopy-9"],
["2026-10-09T04:19:16Z","git","commit","176005b62ce6","-","-","TOOL-aLevelledCopy-9"],
["2026-10-09T04:26:05Z","run-state","dispatch","TOOL-aLevelledCopy-7","-","-","-"],
["2026-10-09T04:26:34Z","run-state","brief","TOOL-aLevelledCopy-7","-","-","-"],
["2026-10-09T04:40:54Z","git","commit","7779b08e7ed4","-","-","TOOL-aLevelledCopy-7"],
["2026-10-09T04:42:57Z","git","commit","dae09ec1f1ce","-","-","TOOL-aLevelledCopy-7"],
["2026-10-09T04:47:58Z","run-state","brief","TOOL-aLevelledCopy-9","-","-","-"],
["2026-10-09T04:52:36Z","run-state","dispatch","TOOL-aLevelledCopy-9","-","-","-"],
["2026-10-09T05:02:14Z","git","commit","b9a11b433a2c","-","-","TOOL-aLevelledCopy-9"],
["2026-10-09T05:05:05Z","git","commit","0a09d7a09e55","-","-","TOOL-aLevelledCopy-9"],
["2026-10-09T05:09:54Z","run-state","dispatch","TOOL-aLevelledCopy-8","-","-","-"],
["2026-10-09T05:10:13Z","run-state","brief","TOOL-aLevelledCopy-8","-","-","-"],
["2026-10-09T05:40:18Z","git","commit","41331dbceb3a","-","-","TOOL-aLevelledCopy-8"],
["2026-10-09T05:44:56Z","git","commit","669816ae7e72","-","-","TOOL-aLevelledCopy-8"],
["2026-10-09T06:08:39Z","run-state","phase","79126924852f","VERIFYING","-","-"],
["2026-10-09T06:16:57Z","git","merge","c79047d89f43","-","-","-"],
["2026-10-09T13:34:41Z","git","merge","82fe6eb763d3","-","-","-"],
["2026-10-09T13:50:10Z","git","merge","5a836bf0fc94","-","-","-"],
["2026-10-09T14:44:25Z","git","merge","295e6bee4df9","-","-","-"],
["2026-10-09T15:47:14Z","git","merge","3459008235d8","-","-","-"],
["2026-10-09T23:18:49Z","git","merge","c41dcd03951d","-","-","-"],
["2026-10-10T01:18:18Z","run-state","phase","79126924852f","LANDING","-","-"]]}]},
"Units":{"facts":{"units":"7 · shown 7 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","DEPL-aLevelledCopy-1","CLOSED","3","2","1","7ab080afd903"],
["1","TOOL-aLevelledCopy-1","CLOSED","4","1","1","961a1cbb7d11"],
["1","TOOL-aLevelledCopy-2","CLOSED","2","2","1","c82936e23438"],
["2","TOOL-aLevelledCopy-3","CLOSED","2","4","1","788a74b79c8e"],
["3","TOOL-aLevelledCopy-7","CLOSED","3","1","1","7779b08e7ed4"],
["3","TOOL-aLevelledCopy-9","CLOSED","4","1","1","b9a11b433a2c"],
["4","TOOL-aLevelledCopy-8","CLOSED","3","1","1","41331dbceb3a"]]}]},
"Decisions":{"facts":{"entries":"37 · shown 0 · aggregated yes","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 14","excluded rows":"proposal 0 · rescope 3 · dispatch 12 · review 1 · brief 7 · hold 0 · resume 1","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","0"],
["2","abort","0"],
["3","override","0"],
["4","waiver","0"],
["5","handoff","0"],
["6","rescope-retire","0"],
["7","rescope-supersede","0"],
["8","rescope-defer","0"],
["9","review","1"],
["10","trailer","22"],
["11","spec-mark","14"],
["12","decision-log","0"],
["13","ledger","0"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-10-09T03:40:59Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"11 · shown 11 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","DEPL-aLevelledCopy-1","MET"],
["2","brief-before-build","TOOL-aLevelledCopy-1","MET"],
["3","brief-before-build","TOOL-aLevelledCopy-2","MET"],
["4","brief-before-build","TOOL-aLevelledCopy-3","MET"],
["5","brief-before-build","TOOL-aLevelledCopy-7","MET"],
["6","brief-before-build","TOOL-aLevelledCopy-8","MET"],
["7","brief-before-build","TOOL-aLevelledCopy-9","MET"],
["8","phases-walked","-","MET"],
["9","green-at-close","-","UNMET"],
["10","keepalive-reaped","-","MET"],
["11","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"37 · shown 0 · aggregated yes"},"tables":[{"name":"by-kind","header":["#","kind","subclass","count"],"rows":[
["1","nonterminal-merged","refused-landing","1"],
["2","out-of-band-edit","-","6"],
["3","refusal-loop","-","2"],
["4","killed-verb","-","21"],
["5","destructive-git","-","3"],
["6","idle-gap","-","4"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 0","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","280","0"],
["3","gates","present","9","0"],
["4","pushes","present","51","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
