# Run record

**Serves:** journal TOOL-aQueuedIndex-1..3

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aQueuedIndex/RUN.md
- run: 1 of 1
- start: 0b9c7ce9b8a45c5cefd6106dbc1166ec81fc0fd7
- phase: LANDING
- terminal: no
- window: 2026-11-12T14:03:12Z to 2026-11-12T17:44:52Z
- window opened by: git
- window closed by: last-activity
- duration: 13300s · DERIVED from the window
- own commits: 0
- last own commit: -
- merged: -
- units served: 3
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 30 · in-window 0 · post-close 0
- usage main: requests 132 · in 318 · out 93839 · cache-read 98078019 · cache-write 177759
- usage agent: requests 142 · in 302 · out 135062 · cache-read 14074154 · cache-write 780853
- usage workflow: requests 299 · in 614 · out 190094 · cache-read 13242663 · cache-write 1173332
- attributed calls: 132 of 579
- values withheld: 0
- commitment: sha256 41d3e02c315ede473476dd5586f906d3cce298b71ed91199f43b2eb4fb3f4507 · lines 189

## Timeline

- events: 10 · shown 10 · elided 0
- withheld rows: verb 74 · push 20 · push-refused 0 · gate 1 · compact 0 · limit 0 · idle 0 · workflow 6

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-11-12T14:03:12Z | run-state | phase | d084590b612e | RUNNING | - | - |
| 2026-11-12T14:50:25Z | run-state | dispatch | TOOL-aQueuedIndex-1 | - | - | - |
| 2026-11-12T14:50:54Z | run-state | brief | TOOL-aQueuedIndex-1 | - | - | - |
| 2026-11-12T15:23:30Z | run-state | dispatch | TOOL-aQueuedIndex-1 | - | - | - |
| 2026-11-12T16:22:30Z | run-state | brief | TOOL-aQueuedIndex-2 | - | - | - |
| 2026-11-12T16:23:39Z | run-state | dispatch | TOOL-aQueuedIndex-2 | - | - | - |
| 2026-11-12T16:56:17Z | run-state | brief | TOOL-aQueuedIndex-3 | - | - | - |
| 2026-11-12T16:57:27Z | run-state | dispatch | TOOL-aQueuedIndex-3 | - | - | - |
| 2026-11-12T17:07:35Z | run-state | phase | 8439558dd735 | VERIFYING | - | - |
| 2026-11-12T17:44:52Z | run-state | phase | 8439558dd735 | LANDING | - | - |

## Units

- units: 3 · shown 3 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | TOOL-aQueuedIndex-1 | CLOSED | 0 | 2 | 1 | - |
| 2 | TOOL-aQueuedIndex-2 | CLOSED | 0 | 1 | 1 | - |
| 3 | TOOL-aQueuedIndex-3 | CLOSED | 0 | 1 | 1 | - |

## Decisions

- entries: 1 · shown 1 · aggregated no
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 1
- excluded rows: proposal 0 · rescope 2 · dispatch 4 · review 2 · brief 3 · hold 0 · resume 0
- review rounds: 2 · shown 2 · aggregated no

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
| 9 | review | 0 |
| 10 | trailer | 0 |
| 11 | spec-mark | 1 |
| 12 | decision-log | 0 |
| 13 | ledger | 0 |

| # | source | ref | verdict |
|---|---|---|---|
| 1 | spec-mark | memory/builds/aQueuedIndex/spec/2026-11-12-spec-TOOL-aQueuedIndex-1.md | - |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-11-12T15:38:35Z | BLOCKED | 2 | - |
| 2 | 2026-11-12T16:38:54Z | CLEAN WITH FIXES | 0 | CONVERGED |

## Conformance

- items: 5 · shown 5 · aggregated no

| # | item | unit | state |
|---|---|---|---|
| 1 | brief-before-build | - | UNJUDGEABLE |
| 2 | phases-walked | - | UNMET |
| 3 | green-at-close | - | MET |
| 4 | keepalive-reaped | - | MET |
| 5 | review-exited | - | MET |

## Anomalies

- anomalies: 14 · shown 14 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | no-progress | - |
| 2 | out-of-band-edit | - |
| 3 | destructive-git | - |
| 4 | destructive-git | - |
| 5 | destructive-git | - |
| 6 | destructive-git | - |
| 7 | destructive-git | - |
| 8 | destructive-git | - |
| 9 | destructive-git | - |
| 10 | destructive-git | - |
| 11 | destructive-git | - |
| 12 | destructive-git | - |
| 13 | destructive-git | - |
| 14 | multi-run-session | - |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 0
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 148 | 1 |
| 3 | gates | present | 1 | 0 |
| 4 | pushes | present | 20 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aQueuedIndex/RUN.md","run":"1 of 1","start":"0b9c7ce9b8a45c5cefd6106dbc1166ec81fc0fd7","phase":"LANDING","terminal":"no","window":"2026-11-12T14:03:12Z to 2026-11-12T17:44:52Z","window opened by":"git","window closed by":"last-activity","duration":"13300s · DERIVED from the window","own commits":"0","last own commit":"-","merged":"-","units served":"3","sources present":"7 of 7","owner turns":"launch 1 · pre-run 30 · in-window 0 · post-close 0","usage main":"requests 132 · in 318 · out 93839 · cache-read 98078019 · cache-write 177759","usage agent":"requests 142 · in 302 · out 135062 · cache-read 14074154 · cache-write 780853","usage workflow":"requests 299 · in 614 · out 190094 · cache-read 13242663 · cache-write 1173332","attributed calls":"132 of 579","values withheld":"0","commitment":"sha256 41d3e02c315ede473476dd5586f906d3cce298b71ed91199f43b2eb4fb3f4507 · lines 189"},"tables":[]},
"Timeline":{"facts":{"events":"10 · shown 10 · elided 0","withheld rows":"verb 74 · push 20 · push-refused 0 · gate 1 · compact 0 · limit 0 · idle 0 · workflow 6"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-11-12T14:03:12Z","run-state","phase","d084590b612e","RUNNING","-","-"],
["2026-11-12T14:50:25Z","run-state","dispatch","TOOL-aQueuedIndex-1","-","-","-"],
["2026-11-12T14:50:54Z","run-state","brief","TOOL-aQueuedIndex-1","-","-","-"],
["2026-11-12T15:23:30Z","run-state","dispatch","TOOL-aQueuedIndex-1","-","-","-"],
["2026-11-12T16:22:30Z","run-state","brief","TOOL-aQueuedIndex-2","-","-","-"],
["2026-11-12T16:23:39Z","run-state","dispatch","TOOL-aQueuedIndex-2","-","-","-"],
["2026-11-12T16:56:17Z","run-state","brief","TOOL-aQueuedIndex-3","-","-","-"],
["2026-11-12T16:57:27Z","run-state","dispatch","TOOL-aQueuedIndex-3","-","-","-"],
["2026-11-12T17:07:35Z","run-state","phase","8439558dd735","VERIFYING","-","-"],
["2026-11-12T17:44:52Z","run-state","phase","8439558dd735","LANDING","-","-"]]}]},
"Units":{"facts":{"units":"3 · shown 3 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","TOOL-aQueuedIndex-1","CLOSED","0","2","1","-"],
["2","TOOL-aQueuedIndex-2","CLOSED","0","1","1","-"],
["3","TOOL-aQueuedIndex-3","CLOSED","0","1","1","-"]]}]},
"Decisions":{"facts":{"entries":"1 · shown 1 · aggregated no","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 1","excluded rows":"proposal 0 · rescope 2 · dispatch 4 · review 2 · brief 3 · hold 0 · resume 0","review rounds":"2 · shown 2 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","0"],
["2","abort","0"],
["3","override","0"],
["4","waiver","0"],
["5","handoff","0"],
["6","rescope-retire","0"],
["7","rescope-supersede","0"],
["8","rescope-defer","0"],
["9","review","0"],
["10","trailer","0"],
["11","spec-mark","1"],
["12","decision-log","0"],
["13","ledger","0"]]},
{"name":"entries","header":["#","source","ref","verdict"],"rows":[
["1","spec-mark","memory/builds/aQueuedIndex/spec/2026-11-12-spec-TOOL-aQueuedIndex-1.md","-"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-11-12T15:38:35Z","BLOCKED","2","-"],
["2","2026-11-12T16:38:54Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"5 · shown 5 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","-","UNJUDGEABLE"],
["2","phases-walked","-","UNMET"],
["3","green-at-close","-","MET"],
["4","keepalive-reaped","-","MET"],
["5","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"14 · shown 14 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","no-progress","-"],
["2","out-of-band-edit","-"],
["3","destructive-git","-"],
["4","destructive-git","-"],
["5","destructive-git","-"],
["6","destructive-git","-"],
["7","destructive-git","-"],
["8","destructive-git","-"],
["9","destructive-git","-"],
["10","destructive-git","-"],
["11","destructive-git","-"],
["12","destructive-git","-"],
["13","destructive-git","-"],
["14","multi-run-session","-"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 0","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","148","1"],
["3","gates","present","1","0"],
["4","pushes","present","20","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
