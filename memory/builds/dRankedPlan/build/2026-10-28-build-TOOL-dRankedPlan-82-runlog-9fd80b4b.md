# Run record

**Serves:** journal TOOL-dRankedPlan-82..83

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/dRankedPlan/RUN.md
- run: 1 of 1
- start: 9fd80b4bd2b961b32aa0ac9c2bf87826f943246d
- phase: LANDING
- terminal: no
- window: 2026-10-26T18:52:47Z to 2026-10-28T10:44:49Z
- window opened by: git
- window closed by: last-activity
- duration: 143522s
- own commits: 0
- last own commit: -
- merged: -
- units served: 2
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 0 · in-window 7 · post-close 0
- usage main: requests 747 · in 1856 · out 463875 · cache-read 353472026 · cache-write 2467234
- usage agent: requests 582 · in 1174 · out 359513 · cache-read 46537560 · cache-write 1968938
- usage workflow: requests 3992 · in 7984 · out 3977051 · cache-read 515025103 · cache-write 18326605
- attributed calls: 5262 of 5552
- values withheld: 0
- commitment: sha256 322c73eb4980f27ef0d9eb03e45b2f489750ab20be477d0ff28f557ea20f64d9 · lines 1433

## Timeline

- events: 15 · shown 15 · elided 0
- withheld rows: verb 620 · push 94 · push-refused 0 · gate 5 · compact 1 · limit 0 · idle 0 · workflow 9

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-10-26T18:52:47Z | run-state | phase | 0689e7fa12b5 | RUNNING | - | - |
| 2026-10-27T08:59:24Z | run-state | phase | e501a1f1d65a | HELD | - | - |
| 2026-10-27T12:01:32Z | run-state | phase | 3d57d3f168e5 | RUNNING | - | - |
| 2026-10-27T15:03:31Z | run-state | phase | de997afe9a05 | VERIFYING | - | - |
| 2026-10-27T18:51:14Z | run-state | phase | be042d1e29a7 | HELD | - | - |
| 2026-10-27T21:04:26Z | run-state | phase | ef0ac519801e | BUILDING | - | - |
| 2026-10-27T21:13:52Z | run-state | brief | TOOL-dRankedPlan-82 | - | - | - |
| 2026-10-27T21:23:46Z | run-state | dispatch | TOOL-dRankedPlan-82 | - | - | - |
| 2026-10-27T22:30:58Z | run-state | phase | 448fb3dfca40 | VERIFYING | - | - |
| 2026-10-28T00:55:33Z | run-state | phase | 5232949ca964 | HELD | - | - |
| 2026-10-28T02:26:44Z | run-state | phase | 922d6b94dc88 | BUILDING | - | - |
| 2026-10-28T02:28:10Z | run-state | brief | TOOL-dRankedPlan-83 | - | - | - |
| 2026-10-28T03:07:00Z | run-state | dispatch | TOOL-dRankedPlan-83 | - | - | - |
| 2026-10-28T03:23:42Z | run-state | phase | 3dbf730d02d3 | VERIFYING | - | - |
| 2026-10-28T10:44:49Z | run-state | phase | 3dbf730d02d3 | LANDING | - | - |

## Units

- units: 81 · shown 0 · aggregated yes

| # | status | units |
|---|---|---|
| 1 | DEFERRED | 79 |
| 2 | CLOSED | 2 |

## Decisions

- entries: 175 · shown 0 · aggregated yes
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 87
- excluded rows: proposal 0 · rescope 65 · dispatch 2 · review 8 · brief 2 · hold 3 · resume 3
- review rounds: 8 · shown 8 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 4 |
| 2 | abort | 0 |
| 3 | override | 2 |
| 4 | waiver | 0 |
| 5 | handoff | 3 |
| 6 | rescope-retire | 0 |
| 7 | rescope-supersede | 0 |
| 8 | rescope-defer | 79 |
| 9 | review | 0 |
| 10 | trailer | 0 |
| 11 | spec-mark | 87 |
| 12 | decision-log | 0 |
| 13 | ledger | 0 |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-10-26T21:39:58Z | BLOCKED | 1 | - |
| 2 | 2026-10-27T00:14:02Z | CLEAN | 0 | CONVERGED |
| 3 | 2026-10-27T02:00:02Z | CLEAN | 0 | CONVERGED |
| 4 | 2026-10-27T03:48:14Z | CLEAN | 0 | CONVERGED |
| 5 | 2026-10-27T05:06:09Z | CLEAN | 0 | CONVERGED |
| 6 | 2026-10-27T06:39:39Z | CLEAN | 0 | CONVERGED |
| 7 | 2026-10-27T08:02:23Z | CLEAN | 0 | CONVERGED |
| 8 | 2026-10-27T14:01:18Z | CLEAN | 0 | CONVERGED |

## Conformance

- items: 5 · shown 5 · aggregated no

| # | item | unit | state |
|---|---|---|---|
| 1 | brief-before-build | - | UNJUDGEABLE |
| 2 | phases-walked | - | MET |
| 3 | green-at-close | - | MET |
| 4 | keepalive-reaped | - | MET |
| 5 | review-exited | - | UNMET |

## Anomalies

- anomalies: 12 · shown 12 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | no-progress | - |
| 2 | out-of-band-edit | - |
| 3 | out-of-band-edit | - |
| 4 | out-of-band-edit | - |
| 5 | out-of-band-edit | - |
| 6 | out-of-band-edit | - |
| 7 | refusal-loop | - |
| 8 | killed-verb | - |
| 9 | killed-verb | - |
| 10 | destructive-git | - |
| 11 | destructive-git | - |
| 12 | destructive-git | - |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 3
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 1240 | 1 |
| 3 | gates | present | 5 | 0 |
| 4 | pushes | present | 94 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/dRankedPlan/RUN.md","run":"1 of 1","start":"9fd80b4bd2b961b32aa0ac9c2bf87826f943246d","phase":"LANDING","terminal":"no","window":"2026-10-26T18:52:47Z to 2026-10-28T10:44:49Z","window opened by":"git","window closed by":"last-activity","duration":"143522s","own commits":"0","last own commit":"-","merged":"-","units served":"2","sources present":"7 of 7","owner turns":"launch 1 · pre-run 0 · in-window 7 · post-close 0","usage main":"requests 747 · in 1856 · out 463875 · cache-read 353472026 · cache-write 2467234","usage agent":"requests 582 · in 1174 · out 359513 · cache-read 46537560 · cache-write 1968938","usage workflow":"requests 3992 · in 7984 · out 3977051 · cache-read 515025103 · cache-write 18326605","attributed calls":"5262 of 5552","values withheld":"0","commitment":"sha256 322c73eb4980f27ef0d9eb03e45b2f489750ab20be477d0ff28f557ea20f64d9 · lines 1433"},"tables":[]},
"Timeline":{"facts":{"events":"15 · shown 15 · elided 0","withheld rows":"verb 620 · push 94 · push-refused 0 · gate 5 · compact 1 · limit 0 · idle 0 · workflow 9"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-10-26T18:52:47Z","run-state","phase","0689e7fa12b5","RUNNING","-","-"],
["2026-10-27T08:59:24Z","run-state","phase","e501a1f1d65a","HELD","-","-"],
["2026-10-27T12:01:32Z","run-state","phase","3d57d3f168e5","RUNNING","-","-"],
["2026-10-27T15:03:31Z","run-state","phase","de997afe9a05","VERIFYING","-","-"],
["2026-10-27T18:51:14Z","run-state","phase","be042d1e29a7","HELD","-","-"],
["2026-10-27T21:04:26Z","run-state","phase","ef0ac519801e","BUILDING","-","-"],
["2026-10-27T21:13:52Z","run-state","brief","TOOL-dRankedPlan-82","-","-","-"],
["2026-10-27T21:23:46Z","run-state","dispatch","TOOL-dRankedPlan-82","-","-","-"],
["2026-10-27T22:30:58Z","run-state","phase","448fb3dfca40","VERIFYING","-","-"],
["2026-10-28T00:55:33Z","run-state","phase","5232949ca964","HELD","-","-"],
["2026-10-28T02:26:44Z","run-state","phase","922d6b94dc88","BUILDING","-","-"],
["2026-10-28T02:28:10Z","run-state","brief","TOOL-dRankedPlan-83","-","-","-"],
["2026-10-28T03:07:00Z","run-state","dispatch","TOOL-dRankedPlan-83","-","-","-"],
["2026-10-28T03:23:42Z","run-state","phase","3dbf730d02d3","VERIFYING","-","-"],
["2026-10-28T10:44:49Z","run-state","phase","3dbf730d02d3","LANDING","-","-"]]}]},
"Units":{"facts":{"units":"81 · shown 0 · aggregated yes"},"tables":[{"name":"by-status","header":["#","status","units"],"rows":[
["1","DEFERRED","79"],
["2","CLOSED","2"]]}]},
"Decisions":{"facts":{"entries":"175 · shown 0 · aggregated yes","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 87","excluded rows":"proposal 0 · rescope 65 · dispatch 2 · review 8 · brief 2 · hold 3 · resume 3","review rounds":"8 · shown 8 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","4"],
["2","abort","0"],
["3","override","2"],
["4","waiver","0"],
["5","handoff","3"],
["6","rescope-retire","0"],
["7","rescope-supersede","0"],
["8","rescope-defer","79"],
["9","review","0"],
["10","trailer","0"],
["11","spec-mark","87"],
["12","decision-log","0"],
["13","ledger","0"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-10-26T21:39:58Z","BLOCKED","1","-"],
["2","2026-10-27T00:14:02Z","CLEAN","0","CONVERGED"],
["3","2026-10-27T02:00:02Z","CLEAN","0","CONVERGED"],
["4","2026-10-27T03:48:14Z","CLEAN","0","CONVERGED"],
["5","2026-10-27T05:06:09Z","CLEAN","0","CONVERGED"],
["6","2026-10-27T06:39:39Z","CLEAN","0","CONVERGED"],
["7","2026-10-27T08:02:23Z","CLEAN","0","CONVERGED"],
["8","2026-10-27T14:01:18Z","CLEAN","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"5 · shown 5 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","-","UNJUDGEABLE"],
["2","phases-walked","-","MET"],
["3","green-at-close","-","MET"],
["4","keepalive-reaped","-","MET"],
["5","review-exited","-","UNMET"]]}]},
"Anomalies":{"facts":{"anomalies":"12 · shown 12 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","no-progress","-"],
["2","out-of-band-edit","-"],
["3","out-of-band-edit","-"],
["4","out-of-band-edit","-"],
["5","out-of-band-edit","-"],
["6","out-of-band-edit","-"],
["7","refusal-loop","-"],
["8","killed-verb","-"],
["9","killed-verb","-"],
["10","destructive-git","-"],
["11","destructive-git","-"],
["12","destructive-git","-"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 3","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","1240","1"],
["3","gates","present","5","0"],
["4","pushes","present","94","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
