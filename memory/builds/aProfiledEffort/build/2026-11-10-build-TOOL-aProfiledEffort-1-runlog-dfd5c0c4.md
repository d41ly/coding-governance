# Run record

**Serves:** journal TOOL-aProfiledEffort-1..4

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aProfiledEffort/RUN.md
- run: 1 of 1
- start: dfd5c0c4d04c140c218c620c38e9616a85f69ac8
- phase: VERIFYING
- terminal: no
- window: 2026-11-10T02:02:24Z to 2026-11-10T05:35:41Z
- window opened by: git
- window closed by: last-activity
- duration: 12797s
- own commits: 0
- last own commit: -
- merged: -
- units served: 4
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 1 · in-window 0 · post-close 0
- usage main: requests 131 · in 336 · out 76150 · cache-read 38769156 · cache-write 201304
- usage agent: requests 59 · in 128 · out 66542 · cache-read 4943791 · cache-write 483851
- usage workflow: requests 503 · in 1024 · out 615549 · cache-read 60249169 · cache-write 6206956
- attributed calls: 784 of 928
- values withheld: 0
- commitment: sha256 1a913a11e248c0e7e3d30c255005fe6e03e9bb9433d1b9284c596d68c9e218af · lines 228

## Timeline

- events: 19 · shown 19 · elided 0
- withheld rows: verb 106 · push 8 · push-refused 0 · gate 0 · compact 0 · limit 0 · idle 0 · workflow 8

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-11-10T02:02:24Z | run-state | phase | 7c896db61b45 | RUNNING | - | - |
| 2026-11-10T02:03:24Z | run-state | phase | dfd5c0c4d04c | SPECCING | - | - |
| 2026-11-10T03:45:10Z | run-state | phase | e7ac36fe47c3 | BUILDING | - | - |
| 2026-11-10T03:48:27Z | run-state | dispatch | TOOL-aProfiledEffort-1 | - | - | - |
| 2026-11-10T03:48:32Z | run-state | brief | TOOL-aProfiledEffort-1 | - | - | - |
| 2026-11-10T04:03:05Z | run-state | dispatch | TOOL-aProfiledEffort-2 | - | - | - |
| 2026-11-10T04:03:11Z | run-state | brief | TOOL-aProfiledEffort-2 | - | - | - |
| 2026-11-10T04:08:53Z | run-state | dispatch | TOOL-aProfiledEffort-2 | - | - | - |
| 2026-11-10T04:17:26Z | run-state | dispatch | TOOL-aProfiledEffort-3 | - | - | - |
| 2026-11-10T04:17:31Z | run-state | brief | TOOL-aProfiledEffort-3 | - | - | - |
| 2026-11-10T04:20:52Z | run-state | dispatch | TOOL-aProfiledEffort-3 | - | - | - |
| 2026-11-10T04:24:58Z | run-state | phase | 6521bde80fe3 | REVIEWING | - | - |
| 2026-11-10T05:02:03Z | run-state | phase | bd0a38082bb1 | BUILDING | - | - |
| 2026-11-10T05:03:40Z | run-state | brief | TOOL-aProfiledEffort-4 | - | - | - |
| 2026-11-10T05:04:58Z | run-state | dispatch | TOOL-aProfiledEffort-4 | - | - | - |
| 2026-11-10T05:15:00Z | run-state | dispatch | TOOL-aProfiledEffort-4 | - | - | - |
| 2026-11-10T05:18:34Z | run-state | dispatch | TOOL-aProfiledEffort-4 | - | - | - |
| 2026-11-10T05:20:06Z | run-state | dispatch | TOOL-aProfiledEffort-4 | - | - | - |
| 2026-11-10T05:35:41Z | run-state | phase | 06840ba24b09 | VERIFYING | - | - |

## Units

- units: 4 · shown 4 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | TOOL-aProfiledEffort-1 | CLOSED | 0 | 1 | 1 | - |
| 2 | TOOL-aProfiledEffort-2 | CLOSED | 0 | 2 | 1 | - |
| 3 | TOOL-aProfiledEffort-3 | CLOSED | 0 | 2 | 1 | - |
| 4 | TOOL-aProfiledEffort-4 | CLOSED | 0 | 4 | 1 | - |

## Decisions

- entries: 1 · shown 1 · aggregated no
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 1
- excluded rows: proposal 0 · rescope 1 · dispatch 9 · review 1 · brief 4 · hold 0 · resume 0
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
| 9 | review | 0 |
| 10 | trailer | 0 |
| 11 | spec-mark | 1 |
| 12 | decision-log | 0 |
| 13 | ledger | 0 |

| # | source | ref | verdict |
|---|---|---|---|
| 1 | spec-mark | memory/builds/aProfiledEffort/spec/2026-11-10-spec-TOOL-aProfiledEffort-1.md | - |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-11-10T04:34:12Z | CLEAN WITH FIXES | 0 | CONVERGED |

## Conformance

- items: 5 · shown 5 · aggregated no

| # | item | unit | state |
|---|---|---|---|
| 1 | brief-before-build | - | UNJUDGEABLE |
| 2 | phases-walked | - | UNJUDGEABLE |
| 3 | green-at-close | - | UNJUDGEABLE |
| 4 | keepalive-reaped | - | UNJUDGEABLE |
| 5 | review-exited | - | MET |

## Anomalies

- anomalies: 3 · shown 3 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | no-progress | - |
| 2 | refusal-loop | - |
| 3 | destructive-git | - |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 0
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 212 | 1 |
| 3 | gates | present | 0 | 0 |
| 4 | pushes | present | 8 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aProfiledEffort/RUN.md","run":"1 of 1","start":"dfd5c0c4d04c140c218c620c38e9616a85f69ac8","phase":"VERIFYING","terminal":"no","window":"2026-11-10T02:02:24Z to 2026-11-10T05:35:41Z","window opened by":"git","window closed by":"last-activity","duration":"12797s","own commits":"0","last own commit":"-","merged":"-","units served":"4","sources present":"7 of 7","owner turns":"launch 1 · pre-run 1 · in-window 0 · post-close 0","usage main":"requests 131 · in 336 · out 76150 · cache-read 38769156 · cache-write 201304","usage agent":"requests 59 · in 128 · out 66542 · cache-read 4943791 · cache-write 483851","usage workflow":"requests 503 · in 1024 · out 615549 · cache-read 60249169 · cache-write 6206956","attributed calls":"784 of 928","values withheld":"0","commitment":"sha256 1a913a11e248c0e7e3d30c255005fe6e03e9bb9433d1b9284c596d68c9e218af · lines 228"},"tables":[]},
"Timeline":{"facts":{"events":"19 · shown 19 · elided 0","withheld rows":"verb 106 · push 8 · push-refused 0 · gate 0 · compact 0 · limit 0 · idle 0 · workflow 8"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-11-10T02:02:24Z","run-state","phase","7c896db61b45","RUNNING","-","-"],
["2026-11-10T02:03:24Z","run-state","phase","dfd5c0c4d04c","SPECCING","-","-"],
["2026-11-10T03:45:10Z","run-state","phase","e7ac36fe47c3","BUILDING","-","-"],
["2026-11-10T03:48:27Z","run-state","dispatch","TOOL-aProfiledEffort-1","-","-","-"],
["2026-11-10T03:48:32Z","run-state","brief","TOOL-aProfiledEffort-1","-","-","-"],
["2026-11-10T04:03:05Z","run-state","dispatch","TOOL-aProfiledEffort-2","-","-","-"],
["2026-11-10T04:03:11Z","run-state","brief","TOOL-aProfiledEffort-2","-","-","-"],
["2026-11-10T04:08:53Z","run-state","dispatch","TOOL-aProfiledEffort-2","-","-","-"],
["2026-11-10T04:17:26Z","run-state","dispatch","TOOL-aProfiledEffort-3","-","-","-"],
["2026-11-10T04:17:31Z","run-state","brief","TOOL-aProfiledEffort-3","-","-","-"],
["2026-11-10T04:20:52Z","run-state","dispatch","TOOL-aProfiledEffort-3","-","-","-"],
["2026-11-10T04:24:58Z","run-state","phase","6521bde80fe3","REVIEWING","-","-"],
["2026-11-10T05:02:03Z","run-state","phase","bd0a38082bb1","BUILDING","-","-"],
["2026-11-10T05:03:40Z","run-state","brief","TOOL-aProfiledEffort-4","-","-","-"],
["2026-11-10T05:04:58Z","run-state","dispatch","TOOL-aProfiledEffort-4","-","-","-"],
["2026-11-10T05:15:00Z","run-state","dispatch","TOOL-aProfiledEffort-4","-","-","-"],
["2026-11-10T05:18:34Z","run-state","dispatch","TOOL-aProfiledEffort-4","-","-","-"],
["2026-11-10T05:20:06Z","run-state","dispatch","TOOL-aProfiledEffort-4","-","-","-"],
["2026-11-10T05:35:41Z","run-state","phase","06840ba24b09","VERIFYING","-","-"]]}]},
"Units":{"facts":{"units":"4 · shown 4 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","TOOL-aProfiledEffort-1","CLOSED","0","1","1","-"],
["2","TOOL-aProfiledEffort-2","CLOSED","0","2","1","-"],
["3","TOOL-aProfiledEffort-3","CLOSED","0","2","1","-"],
["4","TOOL-aProfiledEffort-4","CLOSED","0","4","1","-"]]}]},
"Decisions":{"facts":{"entries":"1 · shown 1 · aggregated no","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 1","excluded rows":"proposal 0 · rescope 1 · dispatch 9 · review 1 · brief 4 · hold 0 · resume 0","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
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
["1","spec-mark","memory/builds/aProfiledEffort/spec/2026-11-10-spec-TOOL-aProfiledEffort-1.md","-"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-11-10T04:34:12Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"5 · shown 5 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","-","UNJUDGEABLE"],
["2","phases-walked","-","UNJUDGEABLE"],
["3","green-at-close","-","UNJUDGEABLE"],
["4","keepalive-reaped","-","UNJUDGEABLE"],
["5","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"3 · shown 3 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","no-progress","-"],
["2","refusal-loop","-"],
["3","destructive-git","-"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 0","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","212","1"],
["3","gates","present","0","0"],
["4","pushes","present","8","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
