# Run record

**Serves:** journal TOOL-dWellOiledMachine-127

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/dWellOiledMachine/RUN.md
- run: 1 of 1
- start: 0487772d4525a0a7f0459d9ed6fdc73b1636a9dc
- phase: LANDING
- terminal: no
- window: 2026-10-26T18:51:09Z to 2026-10-28T05:50:40Z
- window opened by: git
- window closed by: last-activity
- duration: 125971s
- own commits: 0
- last own commit: -
- merged: -
- units served: 1
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 0 · in-window 6 · post-close 0
- usage main: requests 723 · in 1804 · out 470284 · cache-read 323831169 · cache-write 1642383
- usage agent: requests 488 · in 978 · out 300412 · cache-read 67174309 · cache-write 3065938
- usage workflow: requests 5086 · in 10172 · out 5400117 · cache-read 867635202 · cache-write 25348535
- attributed calls: 6259 of 6494
- values withheld: 0
- commitment: sha256 b53af49674f1371abb1e43e3175b34353c3024d3145dd8d12cd7bf925ac04f05 · lines 1453

## Timeline

- events: 8 · shown 8 · elided 0
- withheld rows: verb 664 · push 61 · push-refused 0 · gate 3 · compact 2 · limit 0 · idle 0 · workflow 10

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-10-26T18:51:09Z | run-state | phase | 0689e7fa12b5 | SPECCING | - | - |
| 2026-10-26T22:31:55Z | run-state | phase | 05478df909e0 | REVIEWING | - | - |
| 2026-10-27T12:27:41Z | run-state | phase | 5962b630365e | VERIFYING | - | - |
| 2026-10-27T16:32:56Z | run-state | phase | b5eca851ada7 | HELD | - | - |
| 2026-10-27T21:13:39Z | run-state | brief | TOOL-dWellOiledMachine-127 | - | - | - |
| 2026-10-27T21:29:03Z | run-state | phase | 0075cd1c4cd9 | VERIFYING | - | - |
| 2026-10-27T21:38:34Z | run-state | dispatch | TOOL-dWellOiledMachine-127 | - | - | - |
| 2026-10-28T05:50:40Z | run-state | phase | 0075cd1c4cd9 | LANDING | - | - |

## Units

- units: 126 · shown 0 · aggregated yes

| # | status | units |
|---|---|---|
| 1 | DEFERRED | 125 |
| 2 | CLOSED | 1 |

## Decisions

- entries: 309 · shown 0 · aggregated yes
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 179
- excluded rows: proposal 0 · rescope 65 · dispatch 1 · review 8 · brief 1 · hold 1 · resume 1
- review rounds: 8 · shown 8 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 2 |
| 2 | abort | 0 |
| 3 | override | 2 |
| 4 | waiver | 0 |
| 5 | handoff | 1 |
| 6 | rescope-retire | 0 |
| 7 | rescope-supersede | 0 |
| 8 | rescope-defer | 125 |
| 9 | review | 0 |
| 10 | trailer | 0 |
| 11 | spec-mark | 179 |
| 12 | decision-log | 0 |
| 13 | ledger | 0 |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-10-26T23:11:43Z | BLOCKED | 1 | - |
| 2 | 2026-10-27T02:14:00Z | CLEAN | 0 | CONVERGED |
| 3 | 2026-10-27T04:03:06Z | CLEAN | 0 | CONVERGED |
| 4 | 2026-10-27T05:39:31Z | CLEAN | 0 | CONVERGED |
| 5 | 2026-10-27T07:38:34Z | CLEAN | 0 | CONVERGED |
| 6 | 2026-10-27T08:32:19Z | BLOCKED | 1 | - |
| 7 | 2026-10-27T10:40:12Z | CLEAN | 0 | CONVERGED |
| 8 | 2026-10-27T11:50:34Z | CLEAN | 0 | CONVERGED |

## Conformance

- items: 5 · shown 5 · aggregated no

| # | item | unit | state |
|---|---|---|---|
| 1 | brief-before-build | - | UNJUDGEABLE |
| 2 | phases-walked | - | UNMET |
| 3 | green-at-close | - | MET |
| 4 | keepalive-reaped | - | MET |
| 5 | review-exited | - | UNMET |

## Anomalies

- anomalies: 4 · shown 4 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | no-progress | - |
| 2 | out-of-band-edit | - |
| 3 | out-of-band-edit | - |
| 4 | out-of-band-edit | - |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 1
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 1328 | 1 |
| 3 | gates | present | 3 | 0 |
| 4 | pushes | present | 61 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/dWellOiledMachine/RUN.md","run":"1 of 1","start":"0487772d4525a0a7f0459d9ed6fdc73b1636a9dc","phase":"LANDING","terminal":"no","window":"2026-10-26T18:51:09Z to 2026-10-28T05:50:40Z","window opened by":"git","window closed by":"last-activity","duration":"125971s","own commits":"0","last own commit":"-","merged":"-","units served":"1","sources present":"7 of 7","owner turns":"launch 1 · pre-run 0 · in-window 6 · post-close 0","usage main":"requests 723 · in 1804 · out 470284 · cache-read 323831169 · cache-write 1642383","usage agent":"requests 488 · in 978 · out 300412 · cache-read 67174309 · cache-write 3065938","usage workflow":"requests 5086 · in 10172 · out 5400117 · cache-read 867635202 · cache-write 25348535","attributed calls":"6259 of 6494","values withheld":"0","commitment":"sha256 b53af49674f1371abb1e43e3175b34353c3024d3145dd8d12cd7bf925ac04f05 · lines 1453"},"tables":[]},
"Timeline":{"facts":{"events":"8 · shown 8 · elided 0","withheld rows":"verb 664 · push 61 · push-refused 0 · gate 3 · compact 2 · limit 0 · idle 0 · workflow 10"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-10-26T18:51:09Z","run-state","phase","0689e7fa12b5","SPECCING","-","-"],
["2026-10-26T22:31:55Z","run-state","phase","05478df909e0","REVIEWING","-","-"],
["2026-10-27T12:27:41Z","run-state","phase","5962b630365e","VERIFYING","-","-"],
["2026-10-27T16:32:56Z","run-state","phase","b5eca851ada7","HELD","-","-"],
["2026-10-27T21:13:39Z","run-state","brief","TOOL-dWellOiledMachine-127","-","-","-"],
["2026-10-27T21:29:03Z","run-state","phase","0075cd1c4cd9","VERIFYING","-","-"],
["2026-10-27T21:38:34Z","run-state","dispatch","TOOL-dWellOiledMachine-127","-","-","-"],
["2026-10-28T05:50:40Z","run-state","phase","0075cd1c4cd9","LANDING","-","-"]]}]},
"Units":{"facts":{"units":"126 · shown 0 · aggregated yes"},"tables":[{"name":"by-status","header":["#","status","units"],"rows":[
["1","DEFERRED","125"],
["2","CLOSED","1"]]}]},
"Decisions":{"facts":{"entries":"309 · shown 0 · aggregated yes","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 179","excluded rows":"proposal 0 · rescope 65 · dispatch 1 · review 8 · brief 1 · hold 1 · resume 1","review rounds":"8 · shown 8 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","2"],
["2","abort","0"],
["3","override","2"],
["4","waiver","0"],
["5","handoff","1"],
["6","rescope-retire","0"],
["7","rescope-supersede","0"],
["8","rescope-defer","125"],
["9","review","0"],
["10","trailer","0"],
["11","spec-mark","179"],
["12","decision-log","0"],
["13","ledger","0"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-10-26T23:11:43Z","BLOCKED","1","-"],
["2","2026-10-27T02:14:00Z","CLEAN","0","CONVERGED"],
["3","2026-10-27T04:03:06Z","CLEAN","0","CONVERGED"],
["4","2026-10-27T05:39:31Z","CLEAN","0","CONVERGED"],
["5","2026-10-27T07:38:34Z","CLEAN","0","CONVERGED"],
["6","2026-10-27T08:32:19Z","BLOCKED","1","-"],
["7","2026-10-27T10:40:12Z","CLEAN","0","CONVERGED"],
["8","2026-10-27T11:50:34Z","CLEAN","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"5 · shown 5 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","-","UNJUDGEABLE"],
["2","phases-walked","-","UNMET"],
["3","green-at-close","-","MET"],
["4","keepalive-reaped","-","MET"],
["5","review-exited","-","UNMET"]]}]},
"Anomalies":{"facts":{"anomalies":"4 · shown 4 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","no-progress","-"],
["2","out-of-band-edit","-"],
["3","out-of-band-edit","-"],
["4","out-of-band-edit","-"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 1","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","1328","1"],
["3","gates","present","3","0"],
["4","pushes","present","61","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
