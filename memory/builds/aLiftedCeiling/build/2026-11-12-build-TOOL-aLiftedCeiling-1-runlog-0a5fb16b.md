# Run record

**Serves:** journal TOOL-aLiftedCeiling-1..3

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aLiftedCeiling/RUN.md
- run: 1 of 1
- start: 0a5fb16b75b01e5a044d1c8b92da2921332ba525
- phase: LANDING
- terminal: no
- window: 2026-11-12T18:29:41Z to 2026-11-12T22:05:07Z
- window opened by: git
- window closed by: last-activity
- duration: 12926s · DERIVED from the window
- own commits: 0
- last own commit: -
- merged: -
- units served: 3
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 31 · in-window 0 · post-close 0
- usage main: requests 114 · in 272 · out 86589 · cache-read 77157675 · cache-write 234609
- usage agent: requests 134 · in 278 · out 105794 · cache-read 10956432 · cache-write 456503
- usage workflow: requests 126 · in 258 · out 66422 · cache-read 4714791 · cache-write 451948
- attributed calls: 97 of 367
- values withheld: 0
- commitment: sha256 7e2dedef29d3de19059d01614ad3b1513d75182461ad6927435463b299420b5b · lines 174

## Timeline

- events: 11 · shown 11 · elided 0
- withheld rows: verb 65 · push 21 · push-refused 0 · gate 2 · compact 1 · limit 0 · idle 0 · workflow 5

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-11-12T18:29:41Z | run-state | phase | 768014ca37d5 | RUNNING | - | - |
| 2026-11-12T19:00:53Z | run-state | brief | TOOL-aLiftedCeiling-1 | - | - | - |
| 2026-11-12T19:02:01Z | run-state | dispatch | TOOL-aLiftedCeiling-1 | - | - | - |
| 2026-11-12T19:50:27Z | run-state | brief | TOOL-aLiftedCeiling-2 | - | - | - |
| 2026-11-12T19:51:41Z | run-state | dispatch | TOOL-aLiftedCeiling-2 | - | - | - |
| 2026-11-12T20:50:02Z | run-state | phase | 068fc7304d5b | VERIFYING | - | - |
| 2026-11-12T21:02:37Z | run-state | phase | 60c1eacfca87 | BUILDING | - | - |
| 2026-11-12T21:15:10Z | run-state | brief | TOOL-aLiftedCeiling-3 | - | - | - |
| 2026-11-12T21:17:59Z | run-state | dispatch | TOOL-aLiftedCeiling-3 | - | - | - |
| 2026-11-12T21:26:31Z | run-state | phase | 74f74024d12f | VERIFYING | - | - |
| 2026-11-12T22:05:07Z | run-state | phase | 74f74024d12f | LANDING | - | - |

## Units

- units: 3 · shown 3 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | TOOL-aLiftedCeiling-1 | CLOSED | 0 | 1 | 1 | - |
| 2 | TOOL-aLiftedCeiling-2 | CLOSED | 0 | 1 | 1 | - |
| 3 | TOOL-aLiftedCeiling-3 | CLOSED | 0 | 1 | 1 | - |

## Decisions

- entries: 0 · shown 0 · aggregated no
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 0
- excluded rows: proposal 0 · rescope 2 · dispatch 3 · review 1 · brief 3 · hold 0 · resume 0
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
| 11 | spec-mark | 0 |
| 12 | decision-log | 0 |
| 13 | ledger | 0 |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-11-12T19:18:32Z | CLEAN WITH FIXES | 0 | CONVERGED |

## Conformance

- items: 5 · shown 5 · aggregated no

| # | item | unit | state |
|---|---|---|---|
| 1 | brief-before-build | - | UNJUDGEABLE |
| 2 | phases-walked | - | MET |
| 3 | green-at-close | - | MET |
| 4 | keepalive-reaped | - | MET |
| 5 | review-exited | - | MET |

## Anomalies

- anomalies: 11 · shown 11 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | no-progress | - |
| 2 | out-of-band-edit | - |
| 3 | out-of-band-edit | - |
| 4 | out-of-band-edit | - |
| 5 | out-of-band-edit | - |
| 6 | destructive-git | - |
| 7 | destructive-git | - |
| 8 | destructive-git | - |
| 9 | destructive-git | - |
| 10 | multi-run-session | - |
| 11 | multi-run-session | - |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 0
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 130 | 1 |
| 3 | gates | present | 2 | 0 |
| 4 | pushes | present | 21 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aLiftedCeiling/RUN.md","run":"1 of 1","start":"0a5fb16b75b01e5a044d1c8b92da2921332ba525","phase":"LANDING","terminal":"no","window":"2026-11-12T18:29:41Z to 2026-11-12T22:05:07Z","window opened by":"git","window closed by":"last-activity","duration":"12926s · DERIVED from the window","own commits":"0","last own commit":"-","merged":"-","units served":"3","sources present":"7 of 7","owner turns":"launch 1 · pre-run 31 · in-window 0 · post-close 0","usage main":"requests 114 · in 272 · out 86589 · cache-read 77157675 · cache-write 234609","usage agent":"requests 134 · in 278 · out 105794 · cache-read 10956432 · cache-write 456503","usage workflow":"requests 126 · in 258 · out 66422 · cache-read 4714791 · cache-write 451948","attributed calls":"97 of 367","values withheld":"0","commitment":"sha256 7e2dedef29d3de19059d01614ad3b1513d75182461ad6927435463b299420b5b · lines 174"},"tables":[]},
"Timeline":{"facts":{"events":"11 · shown 11 · elided 0","withheld rows":"verb 65 · push 21 · push-refused 0 · gate 2 · compact 1 · limit 0 · idle 0 · workflow 5"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-11-12T18:29:41Z","run-state","phase","768014ca37d5","RUNNING","-","-"],
["2026-11-12T19:00:53Z","run-state","brief","TOOL-aLiftedCeiling-1","-","-","-"],
["2026-11-12T19:02:01Z","run-state","dispatch","TOOL-aLiftedCeiling-1","-","-","-"],
["2026-11-12T19:50:27Z","run-state","brief","TOOL-aLiftedCeiling-2","-","-","-"],
["2026-11-12T19:51:41Z","run-state","dispatch","TOOL-aLiftedCeiling-2","-","-","-"],
["2026-11-12T20:50:02Z","run-state","phase","068fc7304d5b","VERIFYING","-","-"],
["2026-11-12T21:02:37Z","run-state","phase","60c1eacfca87","BUILDING","-","-"],
["2026-11-12T21:15:10Z","run-state","brief","TOOL-aLiftedCeiling-3","-","-","-"],
["2026-11-12T21:17:59Z","run-state","dispatch","TOOL-aLiftedCeiling-3","-","-","-"],
["2026-11-12T21:26:31Z","run-state","phase","74f74024d12f","VERIFYING","-","-"],
["2026-11-12T22:05:07Z","run-state","phase","74f74024d12f","LANDING","-","-"]]}]},
"Units":{"facts":{"units":"3 · shown 3 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","TOOL-aLiftedCeiling-1","CLOSED","0","1","1","-"],
["2","TOOL-aLiftedCeiling-2","CLOSED","0","1","1","-"],
["3","TOOL-aLiftedCeiling-3","CLOSED","0","1","1","-"]]}]},
"Decisions":{"facts":{"entries":"0 · shown 0 · aggregated no","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 0","excluded rows":"proposal 0 · rescope 2 · dispatch 3 · review 1 · brief 3 · hold 0 · resume 0","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
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
["11","spec-mark","0"],
["12","decision-log","0"],
["13","ledger","0"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-11-12T19:18:32Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"5 · shown 5 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","-","UNJUDGEABLE"],
["2","phases-walked","-","MET"],
["3","green-at-close","-","MET"],
["4","keepalive-reaped","-","MET"],
["5","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"11 · shown 11 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","no-progress","-"],
["2","out-of-band-edit","-"],
["3","out-of-band-edit","-"],
["4","out-of-band-edit","-"],
["5","out-of-band-edit","-"],
["6","destructive-git","-"],
["7","destructive-git","-"],
["8","destructive-git","-"],
["9","destructive-git","-"],
["10","multi-run-session","-"],
["11","multi-run-session","-"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 0","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","130","1"],
["3","gates","present","2","0"],
["4","pushes","present","21","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
