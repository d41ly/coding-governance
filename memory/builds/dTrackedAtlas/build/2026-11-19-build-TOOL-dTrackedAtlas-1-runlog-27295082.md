# Run record

**Serves:** journal TOOL-dTrackedAtlas-1..4 TOOL-dTrackedAtlas-8..12 TOOL-dTrackedAtlas-18

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/dTrackedAtlas/RUN.md
- run: 1 of 1
- start: 2729508280d9ddec4f70626339b7c1a2e3a1ec79
- phase: LANDING
- terminal: no
- window: 2026-11-19T03:06:25Z to 2026-11-19T14:33:18Z
- window opened by: git
- window closed by: last-activity
- duration: 41213s · DERIVED from the window
- own commits: 0
- last own commit: -
- merged: -
- units served: 10
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 0 · in-window 1 · post-close 0
- usage main: requests 480 · in 1128 · out 292207 · cache-read 287740452 · cache-write 622904
- usage agent: requests 177 · in 358 · out 141977 · cache-read 11890325 · cache-write 486685
- usage workflow: requests 1422 · in 2850 · out 1367375 · cache-read 128773798 · cache-write 7327064
- attributed calls: 1780 of 2235
- values withheld: 0
- commitment: sha256 92c26654ee5c22d663ad01fe91634eaed4ef4382df4678211e5c4c37e3873e80 · lines 621

## Timeline

- events: 42 · shown 42 · elided 0
- withheld rows: verb 273 · push 24 · push-refused 0 · gate 27 · compact 0 · limit 0 · idle 0 · workflow 20

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-11-19T03:06:25Z | run-state | phase | 6547d032070a | RUNNING | - | - |
| 2026-11-19T03:10:27Z | run-state | phase | 695c1f7e0f0b | SPECCING | - | - |
| 2026-11-19T03:56:09Z | run-state | brief | TOOL-dTrackedAtlas-1 | - | - | - |
| 2026-11-19T03:56:29Z | run-state | dispatch | TOOL-dTrackedAtlas-1 | - | - | - |
| 2026-11-19T03:56:51Z | run-state | phase | 20ca97bea95e | BUILDING | - | - |
| 2026-11-19T04:27:34Z | run-state | brief | TOOL-dTrackedAtlas-2 | - | - | - |
| 2026-11-19T04:27:58Z | run-state | dispatch | TOOL-dTrackedAtlas-2 | - | - | - |
| 2026-11-19T04:49:03Z | run-state | brief | TOOL-dTrackedAtlas-3 | - | - | - |
| 2026-11-19T04:49:28Z | run-state | dispatch | TOOL-dTrackedAtlas-3 | - | - | - |
| 2026-11-19T04:55:48Z | run-state | brief | TOOL-dTrackedAtlas-3 | - | - | - |
| 2026-11-19T04:56:45Z | run-state | dispatch | TOOL-dTrackedAtlas-3 | - | - | - |
| 2026-11-19T05:17:01Z | run-state | brief | TOOL-dTrackedAtlas-4 | - | - | - |
| 2026-11-19T05:17:25Z | run-state | dispatch | TOOL-dTrackedAtlas-4 | - | - | - |
| 2026-11-19T05:25:47Z | run-state | brief | TOOL-dTrackedAtlas-4 | - | - | - |
| 2026-11-19T05:26:39Z | run-state | dispatch | TOOL-dTrackedAtlas-4 | - | - | - |
| 2026-11-19T06:05:09Z | run-state | phase | 2e5147a2ef43 | REVIEWING | - | - |
| 2026-11-19T06:22:50Z | run-state | phase | 18af33dafb40 | SPECCING | - | - |
| 2026-11-19T06:43:34Z | run-state | brief | TOOL-dTrackedAtlas-8 | - | - | - |
| 2026-11-19T06:43:58Z | run-state | dispatch | TOOL-dTrackedAtlas-8 | - | - | - |
| 2026-11-19T06:44:16Z | run-state | phase | 5c2d5b5af190 | BUILDING | - | - |
| 2026-11-19T06:52:35Z | run-state | brief | TOOL-dTrackedAtlas-9 | - | - | - |
| 2026-11-19T06:52:59Z | run-state | dispatch | TOOL-dTrackedAtlas-9 | - | - | - |
| 2026-11-19T07:07:50Z | run-state | brief | TOOL-dTrackedAtlas-10 | - | - | - |
| 2026-11-19T07:08:18Z | run-state | dispatch | TOOL-dTrackedAtlas-10 | - | - | - |
| 2026-11-19T07:19:41Z | run-state | brief | TOOL-dTrackedAtlas-11 | - | - | - |
| 2026-11-19T07:20:05Z | run-state | dispatch | TOOL-dTrackedAtlas-11 | - | - | - |
| 2026-11-19T07:31:39Z | run-state | phase | e818d4faf8f3 | REVIEWING | - | - |
| 2026-11-19T07:40:04Z | run-state | phase | 812bd05192c4 | SPECCING | - | - |
| 2026-11-19T07:59:50Z | run-state | brief | TOOL-dTrackedAtlas-12 | - | - | - |
| 2026-11-19T08:00:17Z | run-state | dispatch | TOOL-dTrackedAtlas-12 | - | - | - |
| 2026-11-19T08:00:35Z | run-state | phase | 3b741f6ad35d | BUILDING | - | - |
| 2026-11-19T08:15:40Z | run-state | phase | 3f298cfaba83 | VERIFYING | - | - |
| 2026-11-19T08:45:31Z | run-state | phase | 15c462a7dd7a | HELD | - | - |
| 2026-11-19T09:36:04Z | run-state | phase | c942b173d3b6 | VERIFYING | - | - |
| 2026-11-19T09:46:43Z | run-state | phase | 92959104c9aa | SPECCING | - | - |
| 2026-11-19T09:47:25Z | run-state | brief | TOOL-dTrackedAtlas-4 | - | - | - |
| 2026-11-19T09:47:51Z | run-state | dispatch | TOOL-dTrackedAtlas-4 | - | - | - |
| 2026-11-19T09:48:09Z | run-state | phase | 8229afe6d412 | BUILDING | - | - |
| 2026-11-19T10:31:26Z | run-state | brief | TOOL-dTrackedAtlas-18 | - | - | - |
| 2026-11-19T10:31:56Z | run-state | dispatch | TOOL-dTrackedAtlas-18 | - | - | - |
| 2026-11-19T13:32:08Z | run-state | phase | bb214a89ded3 | VERIFYING | - | - |
| 2026-11-19T14:33:18Z | run-state | phase | bb214a89ded3 | LANDING | - | - |

## Units

- units: 10 · shown 10 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | TOOL-dTrackedAtlas-1 | CLOSED | 0 | 1 | 1 | - |
| 2 | TOOL-dTrackedAtlas-2 | CLOSED | 0 | 1 | 1 | - |
| 3 | TOOL-dTrackedAtlas-3 | CLOSED | 0 | 2 | 2 | - |
| 4 | TOOL-dTrackedAtlas-4 | CLOSED | 0 | 3 | 3 | - |
| 5 | TOOL-dTrackedAtlas-8 | CLOSED | 0 | 1 | 1 | - |
| 6 | TOOL-dTrackedAtlas-9 | CLOSED | 0 | 1 | 1 | - |
| 7 | TOOL-dTrackedAtlas-10 | CLOSED | 0 | 1 | 1 | - |
| 8 | TOOL-dTrackedAtlas-11 | CLOSED | 0 | 1 | 1 | - |
| 9 | TOOL-dTrackedAtlas-12 | CLOSED | 0 | 1 | 1 | - |
| 11 | TOOL-dTrackedAtlas-18 | CLOSED | 0 | 1 | 1 | - |

## Decisions

- entries: 7 · shown 7 · aggregated no
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 1 · agent-before 0 · agent-inside 2
- excluded rows: proposal 0 · rescope 6 · dispatch 13 · review 2 · brief 13 · hold 1 · resume 1 · refusal 0 · fix-pass 0
- review rounds: 2 · shown 2 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 2 |
| 2 | abort | 0 |
| 3 | override | 0 |
| 4 | waiver | 0 |
| 5 | handoff | 1 |
| 6 | rescope-retire | 0 |
| 7 | rescope-supersede | 0 |
| 8 | rescope-defer | 1 |
| 9 | review | 0 |
| 10 | trailer | 0 |
| 11 | spec-mark | 3 |
| 12 | decision-log | 0 |
| 13 | ledger | 0 |

| # | source | ref | verdict |
|---|---|---|---|
| 1 | decision | memory/builds/dTrackedAtlas/RUN.md:74 | - |
| 2 | rescope-defer | memory/builds/dTrackedAtlas/RUN.md:76 | - |
| 3 | decision | memory/builds/dTrackedAtlas/RUN.md:113 | - |
| 4 | handoff | memory/builds/dTrackedAtlas/RUN.md:115 | - |
| 5 | spec-mark | memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-4.md | - |
| 6 | spec-mark | memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-4.md | - |
| 7 | spec-mark | memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-4.md | - |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-11-19T06:20:59Z | CLEAN WITH FIXES | 0 | - |
| 2 | 2026-11-19T07:39:14Z | CLEAN WITH FIXES | 0 | CONVERGED |

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

- anomalies: 24 · shown 0 · aggregated yes

| # | kind | subclass | count |
|---|---|---|---|
| 1 | no-progress | - | 1 |
| 2 | out-of-band-edit | - | 4 |
| 3 | refusal-loop | - | 1 |
| 4 | destructive-git | - | 18 |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 1
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 546 | 0 |
| 3 | gates | present | 27 | 0 |
| 4 | pushes | present | 24 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/dTrackedAtlas/RUN.md","run":"1 of 1","start":"2729508280d9ddec4f70626339b7c1a2e3a1ec79","phase":"LANDING","terminal":"no","window":"2026-11-19T03:06:25Z to 2026-11-19T14:33:18Z","window opened by":"git","window closed by":"last-activity","duration":"41213s · DERIVED from the window","own commits":"0","last own commit":"-","merged":"-","units served":"10","sources present":"7 of 7","owner turns":"launch 1 · pre-run 0 · in-window 1 · post-close 0","usage main":"requests 480 · in 1128 · out 292207 · cache-read 287740452 · cache-write 622904","usage agent":"requests 177 · in 358 · out 141977 · cache-read 11890325 · cache-write 486685","usage workflow":"requests 1422 · in 2850 · out 1367375 · cache-read 128773798 · cache-write 7327064","attributed calls":"1780 of 2235","values withheld":"0","commitment":"sha256 92c26654ee5c22d663ad01fe91634eaed4ef4382df4678211e5c4c37e3873e80 · lines 621"},"tables":[]},
"Timeline":{"facts":{"events":"42 · shown 42 · elided 0","withheld rows":"verb 273 · push 24 · push-refused 0 · gate 27 · compact 0 · limit 0 · idle 0 · workflow 20"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-11-19T03:06:25Z","run-state","phase","6547d032070a","RUNNING","-","-"],
["2026-11-19T03:10:27Z","run-state","phase","695c1f7e0f0b","SPECCING","-","-"],
["2026-11-19T03:56:09Z","run-state","brief","TOOL-dTrackedAtlas-1","-","-","-"],
["2026-11-19T03:56:29Z","run-state","dispatch","TOOL-dTrackedAtlas-1","-","-","-"],
["2026-11-19T03:56:51Z","run-state","phase","20ca97bea95e","BUILDING","-","-"],
["2026-11-19T04:27:34Z","run-state","brief","TOOL-dTrackedAtlas-2","-","-","-"],
["2026-11-19T04:27:58Z","run-state","dispatch","TOOL-dTrackedAtlas-2","-","-","-"],
["2026-11-19T04:49:03Z","run-state","brief","TOOL-dTrackedAtlas-3","-","-","-"],
["2026-11-19T04:49:28Z","run-state","dispatch","TOOL-dTrackedAtlas-3","-","-","-"],
["2026-11-19T04:55:48Z","run-state","brief","TOOL-dTrackedAtlas-3","-","-","-"],
["2026-11-19T04:56:45Z","run-state","dispatch","TOOL-dTrackedAtlas-3","-","-","-"],
["2026-11-19T05:17:01Z","run-state","brief","TOOL-dTrackedAtlas-4","-","-","-"],
["2026-11-19T05:17:25Z","run-state","dispatch","TOOL-dTrackedAtlas-4","-","-","-"],
["2026-11-19T05:25:47Z","run-state","brief","TOOL-dTrackedAtlas-4","-","-","-"],
["2026-11-19T05:26:39Z","run-state","dispatch","TOOL-dTrackedAtlas-4","-","-","-"],
["2026-11-19T06:05:09Z","run-state","phase","2e5147a2ef43","REVIEWING","-","-"],
["2026-11-19T06:22:50Z","run-state","phase","18af33dafb40","SPECCING","-","-"],
["2026-11-19T06:43:34Z","run-state","brief","TOOL-dTrackedAtlas-8","-","-","-"],
["2026-11-19T06:43:58Z","run-state","dispatch","TOOL-dTrackedAtlas-8","-","-","-"],
["2026-11-19T06:44:16Z","run-state","phase","5c2d5b5af190","BUILDING","-","-"],
["2026-11-19T06:52:35Z","run-state","brief","TOOL-dTrackedAtlas-9","-","-","-"],
["2026-11-19T06:52:59Z","run-state","dispatch","TOOL-dTrackedAtlas-9","-","-","-"],
["2026-11-19T07:07:50Z","run-state","brief","TOOL-dTrackedAtlas-10","-","-","-"],
["2026-11-19T07:08:18Z","run-state","dispatch","TOOL-dTrackedAtlas-10","-","-","-"],
["2026-11-19T07:19:41Z","run-state","brief","TOOL-dTrackedAtlas-11","-","-","-"],
["2026-11-19T07:20:05Z","run-state","dispatch","TOOL-dTrackedAtlas-11","-","-","-"],
["2026-11-19T07:31:39Z","run-state","phase","e818d4faf8f3","REVIEWING","-","-"],
["2026-11-19T07:40:04Z","run-state","phase","812bd05192c4","SPECCING","-","-"],
["2026-11-19T07:59:50Z","run-state","brief","TOOL-dTrackedAtlas-12","-","-","-"],
["2026-11-19T08:00:17Z","run-state","dispatch","TOOL-dTrackedAtlas-12","-","-","-"],
["2026-11-19T08:00:35Z","run-state","phase","3b741f6ad35d","BUILDING","-","-"],
["2026-11-19T08:15:40Z","run-state","phase","3f298cfaba83","VERIFYING","-","-"],
["2026-11-19T08:45:31Z","run-state","phase","15c462a7dd7a","HELD","-","-"],
["2026-11-19T09:36:04Z","run-state","phase","c942b173d3b6","VERIFYING","-","-"],
["2026-11-19T09:46:43Z","run-state","phase","92959104c9aa","SPECCING","-","-"],
["2026-11-19T09:47:25Z","run-state","brief","TOOL-dTrackedAtlas-4","-","-","-"],
["2026-11-19T09:47:51Z","run-state","dispatch","TOOL-dTrackedAtlas-4","-","-","-"],
["2026-11-19T09:48:09Z","run-state","phase","8229afe6d412","BUILDING","-","-"],
["2026-11-19T10:31:26Z","run-state","brief","TOOL-dTrackedAtlas-18","-","-","-"],
["2026-11-19T10:31:56Z","run-state","dispatch","TOOL-dTrackedAtlas-18","-","-","-"],
["2026-11-19T13:32:08Z","run-state","phase","bb214a89ded3","VERIFYING","-","-"],
["2026-11-19T14:33:18Z","run-state","phase","bb214a89ded3","LANDING","-","-"]]}]},
"Units":{"facts":{"units":"10 · shown 10 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","TOOL-dTrackedAtlas-1","CLOSED","0","1","1","-"],
["2","TOOL-dTrackedAtlas-2","CLOSED","0","1","1","-"],
["3","TOOL-dTrackedAtlas-3","CLOSED","0","2","2","-"],
["4","TOOL-dTrackedAtlas-4","CLOSED","0","3","3","-"],
["5","TOOL-dTrackedAtlas-8","CLOSED","0","1","1","-"],
["6","TOOL-dTrackedAtlas-9","CLOSED","0","1","1","-"],
["7","TOOL-dTrackedAtlas-10","CLOSED","0","1","1","-"],
["8","TOOL-dTrackedAtlas-11","CLOSED","0","1","1","-"],
["9","TOOL-dTrackedAtlas-12","CLOSED","0","1","1","-"],
["11","TOOL-dTrackedAtlas-18","CLOSED","0","1","1","-"]]}]},
"Decisions":{"facts":{"entries":"7 · shown 7 · aggregated no","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 1 · agent-before 0 · agent-inside 2","excluded rows":"proposal 0 · rescope 6 · dispatch 13 · review 2 · brief 13 · hold 1 · resume 1 · refusal 0 · fix-pass 0","review rounds":"2 · shown 2 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","2"],
["2","abort","0"],
["3","override","0"],
["4","waiver","0"],
["5","handoff","1"],
["6","rescope-retire","0"],
["7","rescope-supersede","0"],
["8","rescope-defer","1"],
["9","review","0"],
["10","trailer","0"],
["11","spec-mark","3"],
["12","decision-log","0"],
["13","ledger","0"]]},
{"name":"entries","header":["#","source","ref","verdict"],"rows":[
["1","decision","memory/builds/dTrackedAtlas/RUN.md:74","-"],
["2","rescope-defer","memory/builds/dTrackedAtlas/RUN.md:76","-"],
["3","decision","memory/builds/dTrackedAtlas/RUN.md:113","-"],
["4","handoff","memory/builds/dTrackedAtlas/RUN.md:115","-"],
["5","spec-mark","memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-4.md","-"],
["6","spec-mark","memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-4.md","-"],
["7","spec-mark","memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-4.md","-"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-11-19T06:20:59Z","CLEAN WITH FIXES","0","-"],
["2","2026-11-19T07:39:14Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"5 · shown 5 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","-","UNJUDGEABLE"],
["2","phases-walked","-","MET"],
["3","green-at-close","-","MET"],
["4","keepalive-reaped","-","MET"],
["5","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"24 · shown 0 · aggregated yes"},"tables":[{"name":"by-kind","header":["#","kind","subclass","count"],"rows":[
["1","no-progress","-","1"],
["2","out-of-band-edit","-","4"],
["3","refusal-loop","-","1"],
["4","destructive-git","-","18"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 1","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","546","0"],
["3","gates","present","27","0"],
["4","pushes","present","24","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
