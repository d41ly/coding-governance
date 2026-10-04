# Run record

**Serves:** journal TOOL-aBatchedMinors-2..4 TOOL-aBatchedMinors-6

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aBatchedMinors/RUN.md
- run: 1 of 1
- start: dc0cf1f91311246b155ad0ed9ca74c887061741b
- phase: VERIFYING
- terminal: no
- window: 2026-10-04T15:32:41Z to 2026-10-04T16:59:02Z
- window opened by: git
- window closed by: last-activity
- duration: 5181s
- own commits: 8
- last own commit: 75a935fb01a97f62e26c71215eb01b5dc33ec9fc
- merged: no
- units served: 4
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 0 · in-window 0 · post-close 0
- usage main: requests 127 · in 256 · out 100990 · cache-read 40724471 · cache-write 208697
- usage agent: requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0
- usage workflow: requests 179 · in 358 · out 144407 · cache-read 21679188 · cache-write 1202187
- attributed calls: 285 of 311
- values withheld: 0
- commitment: sha256 e5782c947a319a5c21550062b0076724b3aee7488a01e675787c6fd004e677a9 · lines 48

## Timeline

- events: 23 · shown 23 · elided 0
- withheld rows: verb 23 · push 1 · push-refused 0 · gate 0 · compact 0 · limit 0 · idle 0 · workflow 1

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-10-04T15:32:41Z | run-state | phase | 5ba0fc4fcdab | RUNNING | - | - |
| 2026-10-04T15:37:23Z | git | commit | 01b0603b568e | - | - | TOOL-aBatchedMinors-1 TOOL-aBatchedMinors-2 TOOL-aBatchedMinors-3 TOOL-aBatchedMinors-4 |
| 2026-10-04T15:37:23Z | run-state | phase | dc0cf1f91311 | SPECCING | - | - |
| 2026-10-04T15:37:52Z | run-state | brief | TOOL-aBatchedMinors-2 | - | - | - |
| 2026-10-04T15:37:55Z | run-state | brief | TOOL-aBatchedMinors-3 | - | - | - |
| 2026-10-04T15:37:58Z | run-state | brief | TOOL-aBatchedMinors-4 | - | - | - |
| 2026-10-04T15:38:02Z | git | commit | 3c1195040152 | - | - | TOOL-aBatchedMinors-2 TOOL-aBatchedMinors-3 TOOL-aBatchedMinors-4 |
| 2026-10-04T15:38:27Z | run-state | phase | 3c1195040152 | BUILDING | - | - |
| 2026-10-04T15:38:49Z | run-state | dispatch | TOOL-aBatchedMinors-2 | - | - | - |
| 2026-10-04T15:54:28Z | git | commit | 131537ae4856 | - | - | TOOL-aBatchedMinors-2 |
| 2026-10-04T15:55:09Z | run-state | dispatch | TOOL-aBatchedMinors-3 | - | - | - |
| 2026-10-04T16:12:35Z | git | commit | ef2277f21ded | - | - | TOOL-aBatchedMinors-3 |
| 2026-10-04T16:14:11Z | run-state | dispatch | TOOL-aBatchedMinors-4 | - | - | - |
| 2026-10-04T16:16:16Z | run-state | dispatch | TOOL-aBatchedMinors-4 | - | - | - |
| 2026-10-04T16:17:32Z | git | commit | 6d1ae3a63d03 | - | - | TOOL-aBatchedMinors-4 |
| 2026-10-04T16:23:36Z | run-state | phase | 92847e1858b6 | REVIEWING | - | - |
| 2026-10-04T16:34:57Z | git | commit | a8571c6420f1 | - | - | TOOL-aBatchedMinors-6 |
| 2026-10-04T16:35:31Z | run-state | brief | TOOL-aBatchedMinors-6 | - | - | - |
| 2026-10-04T16:35:38Z | git | commit | adaea26441a3 | - | - | TOOL-aBatchedMinors-6 |
| 2026-10-04T16:35:38Z | run-state | phase | a8571c6420f1 | BUILDING | - | - |
| 2026-10-04T16:36:17Z | run-state | dispatch | TOOL-aBatchedMinors-6 | - | - | - |
| 2026-10-04T16:52:34Z | git | commit | 75a935fb01a9 | - | - | TOOL-aBatchedMinors-6 |
| 2026-10-04T16:59:02Z | run-state | phase | 75a935fb01a9 | VERIFYING | - | - |

## Units

- units: 5 · shown 5 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | TOOL-aBatchedMinors-1 | WONTDO | 1 | 0 | 0 | - |
| 2 | TOOL-aBatchedMinors-2 | CLOSED | 3 | 1 | 1 | 131537ae4856 |
| 3 | TOOL-aBatchedMinors-3 | CLOSED | 3 | 1 | 1 | ef2277f21ded |
| 4 | TOOL-aBatchedMinors-4 | CLOSED | 3 | 2 | 1 | 6d1ae3a63d03 |
| 6 | TOOL-aBatchedMinors-6 | CLOSED | 3 | 1 | 1 | 75a935fb01a9 |

## Decisions

- entries: 15 · shown 15 · aggregated no
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 0
- excluded rows: proposal 0 · rescope 1 · dispatch 5 · review 1 · brief 4 · hold 0 · resume 0
- review rounds: 1 · shown 1 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 0 |
| 2 | abort | 0 |
| 3 | override | 0 |
| 4 | waiver | 0 |
| 5 | rescope-retire | 1 |
| 6 | rescope-supersede | 0 |
| 7 | review | 1 |
| 8 | trailer | 13 |
| 9 | spec-mark | 0 |
| 10 | decision-log | 0 |
| 11 | ledger | 0 |

| # | source | ref | verdict |
|---|---|---|---|
| 1 | rescope-retire | memory/builds/aBatchedMinors/RUN.md:34 | - |
| 2 | review | memory/builds/aBatchedMinors/reviews/2026-10-04-review-TOOL-aBatchedMinors-2-closing-diff-round1.md:15 | CLEAN WITH FIXES |
| 3 | trailer | 01b0603b568e | - |
| 4 | trailer | 01b0603b568e | - |
| 5 | trailer | 131537ae4856 | - |
| 6 | trailer | 131537ae4856 | - |
| 7 | trailer | ef2277f21ded | - |
| 8 | trailer | ef2277f21ded | - |
| 9 | trailer | 6d1ae3a63d03 | - |
| 10 | trailer | 6d1ae3a63d03 | - |
| 11 | trailer | a8571c6420f1 | - |
| 12 | trailer | a8571c6420f1 | - |
| 13 | trailer | 75a935fb01a9 | - |
| 14 | trailer | 75a935fb01a9 | - |
| 15 | trailer | 75a935fb01a9 | - |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-10-04T16:33:46Z | CLEAN WITH FIXES | 0 | CONVERGED |

## Conformance

- items: 8 · shown 8 · aggregated no

| # | item | unit | state |
|---|---|---|---|
| 1 | brief-before-build | TOOL-aBatchedMinors-2 | MET |
| 2 | brief-before-build | TOOL-aBatchedMinors-3 | MET |
| 3 | brief-before-build | TOOL-aBatchedMinors-4 | MET |
| 4 | brief-before-build | TOOL-aBatchedMinors-6 | MET |
| 5 | phases-walked | - | UNJUDGEABLE |
| 6 | green-at-close | - | UNJUDGEABLE |
| 7 | keepalive-reaped | - | UNJUDGEABLE |
| 8 | review-exited | - | MET |

## Anomalies

- anomalies: 0 · shown 0 · aggregated no

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 0
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 46 | 0 |
| 3 | gates | present | 0 | 0 |
| 4 | pushes | present | 1 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aBatchedMinors/RUN.md","run":"1 of 1","start":"dc0cf1f91311246b155ad0ed9ca74c887061741b","phase":"VERIFYING","terminal":"no","window":"2026-10-04T15:32:41Z to 2026-10-04T16:59:02Z","window opened by":"git","window closed by":"last-activity","duration":"5181s","own commits":"8","last own commit":"75a935fb01a97f62e26c71215eb01b5dc33ec9fc","merged":"no","units served":"4","sources present":"7 of 7","owner turns":"launch 1 · pre-run 0 · in-window 0 · post-close 0","usage main":"requests 127 · in 256 · out 100990 · cache-read 40724471 · cache-write 208697","usage agent":"requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0","usage workflow":"requests 179 · in 358 · out 144407 · cache-read 21679188 · cache-write 1202187","attributed calls":"285 of 311","values withheld":"0","commitment":"sha256 e5782c947a319a5c21550062b0076724b3aee7488a01e675787c6fd004e677a9 · lines 48"},"tables":[]},
"Timeline":{"facts":{"events":"23 · shown 23 · elided 0","withheld rows":"verb 23 · push 1 · push-refused 0 · gate 0 · compact 0 · limit 0 · idle 0 · workflow 1"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-10-04T15:32:41Z","run-state","phase","5ba0fc4fcdab","RUNNING","-","-"],
["2026-10-04T15:37:23Z","git","commit","01b0603b568e","-","-","TOOL-aBatchedMinors-1 TOOL-aBatchedMinors-2 TOOL-aBatchedMinors-3 TOOL-aBatchedMinors-4"],
["2026-10-04T15:37:23Z","run-state","phase","dc0cf1f91311","SPECCING","-","-"],
["2026-10-04T15:37:52Z","run-state","brief","TOOL-aBatchedMinors-2","-","-","-"],
["2026-10-04T15:37:55Z","run-state","brief","TOOL-aBatchedMinors-3","-","-","-"],
["2026-10-04T15:37:58Z","run-state","brief","TOOL-aBatchedMinors-4","-","-","-"],
["2026-10-04T15:38:02Z","git","commit","3c1195040152","-","-","TOOL-aBatchedMinors-2 TOOL-aBatchedMinors-3 TOOL-aBatchedMinors-4"],
["2026-10-04T15:38:27Z","run-state","phase","3c1195040152","BUILDING","-","-"],
["2026-10-04T15:38:49Z","run-state","dispatch","TOOL-aBatchedMinors-2","-","-","-"],
["2026-10-04T15:54:28Z","git","commit","131537ae4856","-","-","TOOL-aBatchedMinors-2"],
["2026-10-04T15:55:09Z","run-state","dispatch","TOOL-aBatchedMinors-3","-","-","-"],
["2026-10-04T16:12:35Z","git","commit","ef2277f21ded","-","-","TOOL-aBatchedMinors-3"],
["2026-10-04T16:14:11Z","run-state","dispatch","TOOL-aBatchedMinors-4","-","-","-"],
["2026-10-04T16:16:16Z","run-state","dispatch","TOOL-aBatchedMinors-4","-","-","-"],
["2026-10-04T16:17:32Z","git","commit","6d1ae3a63d03","-","-","TOOL-aBatchedMinors-4"],
["2026-10-04T16:23:36Z","run-state","phase","92847e1858b6","REVIEWING","-","-"],
["2026-10-04T16:34:57Z","git","commit","a8571c6420f1","-","-","TOOL-aBatchedMinors-6"],
["2026-10-04T16:35:31Z","run-state","brief","TOOL-aBatchedMinors-6","-","-","-"],
["2026-10-04T16:35:38Z","git","commit","adaea26441a3","-","-","TOOL-aBatchedMinors-6"],
["2026-10-04T16:35:38Z","run-state","phase","a8571c6420f1","BUILDING","-","-"],
["2026-10-04T16:36:17Z","run-state","dispatch","TOOL-aBatchedMinors-6","-","-","-"],
["2026-10-04T16:52:34Z","git","commit","75a935fb01a9","-","-","TOOL-aBatchedMinors-6"],
["2026-10-04T16:59:02Z","run-state","phase","75a935fb01a9","VERIFYING","-","-"]]}]},
"Units":{"facts":{"units":"5 · shown 5 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","TOOL-aBatchedMinors-1","WONTDO","1","0","0","-"],
["2","TOOL-aBatchedMinors-2","CLOSED","3","1","1","131537ae4856"],
["3","TOOL-aBatchedMinors-3","CLOSED","3","1","1","ef2277f21ded"],
["4","TOOL-aBatchedMinors-4","CLOSED","3","2","1","6d1ae3a63d03"],
["6","TOOL-aBatchedMinors-6","CLOSED","3","1","1","75a935fb01a9"]]}]},
"Decisions":{"facts":{"entries":"15 · shown 15 · aggregated no","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 0","excluded rows":"proposal 0 · rescope 1 · dispatch 5 · review 1 · brief 4 · hold 0 · resume 0","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","0"],
["2","abort","0"],
["3","override","0"],
["4","waiver","0"],
["5","rescope-retire","1"],
["6","rescope-supersede","0"],
["7","review","1"],
["8","trailer","13"],
["9","spec-mark","0"],
["10","decision-log","0"],
["11","ledger","0"]]},
{"name":"entries","header":["#","source","ref","verdict"],"rows":[
["1","rescope-retire","memory/builds/aBatchedMinors/RUN.md:34","-"],
["2","review","memory/builds/aBatchedMinors/reviews/2026-10-04-review-TOOL-aBatchedMinors-2-closing-diff-round1.md:15","CLEAN WITH FIXES"],
["3","trailer","01b0603b568e","-"],
["4","trailer","01b0603b568e","-"],
["5","trailer","131537ae4856","-"],
["6","trailer","131537ae4856","-"],
["7","trailer","ef2277f21ded","-"],
["8","trailer","ef2277f21ded","-"],
["9","trailer","6d1ae3a63d03","-"],
["10","trailer","6d1ae3a63d03","-"],
["11","trailer","a8571c6420f1","-"],
["12","trailer","a8571c6420f1","-"],
["13","trailer","75a935fb01a9","-"],
["14","trailer","75a935fb01a9","-"],
["15","trailer","75a935fb01a9","-"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-10-04T16:33:46Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"8 · shown 8 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","TOOL-aBatchedMinors-2","MET"],
["2","brief-before-build","TOOL-aBatchedMinors-3","MET"],
["3","brief-before-build","TOOL-aBatchedMinors-4","MET"],
["4","brief-before-build","TOOL-aBatchedMinors-6","MET"],
["5","phases-walked","-","UNJUDGEABLE"],
["6","green-at-close","-","UNJUDGEABLE"],
["7","keepalive-reaped","-","UNJUDGEABLE"],
["8","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"0 · shown 0 · aggregated no"},"tables":[]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 0","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","46","0"],
["3","gates","present","0","0"],
["4","pushes","present","1","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
