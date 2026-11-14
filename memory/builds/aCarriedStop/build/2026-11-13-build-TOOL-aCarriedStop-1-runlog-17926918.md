# Run record

**Serves:** journal TOOL-aCarriedStop-1..3 TOOL-aCarriedStop-9..10

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aCarriedStop/RUN.md
- run: 1 of 1
- start: 17926918815023997468c5021f974d2d6160ed9f
- phase: LANDING
- terminal: no
- window: 2026-11-13T11:19:21Z to 2026-11-14T09:43:18Z
- window opened by: git
- window closed by: last-activity
- duration: 80637s · DERIVED from the window
- own commits: 0
- last own commit: -
- merged: -
- units served: 5
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 0 · in-window 2 · post-close 0
- usage main: requests 430 · in 1016 · out 229231 · cache-read 113426742 · cache-write 1039462
- usage agent: requests 302 · in 624 · out 309825 · cache-read 28836718 · cache-write 1061523
- usage workflow: requests 99 · in 208 · out 128469 · cache-read 3951248 · cache-write 697137
- attributed calls: 839 of 921
- values withheld: 0
- commitment: sha256 1b07d5ce4bdb8acbea1d3a00342622f7d60372874b6f8f7c519ed6f532625ba9 · lines 416

## Timeline

- events: 25 · shown 25 · elided 0
- withheld rows: verb 189 · push 20 · push-refused 0 · gate 6 · compact 3 · limit 0 · idle 0 · workflow 1

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-11-13T11:19:21Z | run-state | phase | d646814e4a6a | SPECCING | - | - |
| 2026-11-13T11:45:32Z | run-state | brief | TOOL-aCarriedStop-1 | - | - | - |
| 2026-11-13T11:46:03Z | run-state | brief | TOOL-aCarriedStop-1 | - | - | - |
| 2026-11-13T11:47:24Z | run-state | dispatch | TOOL-aCarriedStop-1 | - | - | - |
| 2026-11-13T12:02:27Z | run-state | phase | 0dd449637fb3 | BUILDING | - | - |
| 2026-11-13T13:01:26Z | run-state | phase | cfda7001d79d | VERIFYING | - | - |
| 2026-11-13T13:04:06Z | run-state | brief | TOOL-aCarriedStop-2 | - | - | - |
| 2026-11-13T13:05:21Z | run-state | dispatch | TOOL-aCarriedStop-2 | - | - | - |
| 2026-11-13T13:13:34Z | run-state | dispatch | TOOL-aCarriedStop-2 | - | - | - |
| 2026-11-13T13:13:35Z | run-state | phase | a484dc6c96ee | BUILDING | - | - |
| 2026-11-13T13:17:27Z | run-state | brief | TOOL-aCarriedStop-3 | - | - | - |
| 2026-11-13T13:18:41Z | run-state | dispatch | TOOL-aCarriedStop-3 | - | - | - |
| 2026-11-13T13:57:09Z | run-state | phase | 41015d329ec2 | VERIFYING | - | - |
| 2026-11-13T18:39:30Z | run-state | phase | 4bf57cb7626b | HELD | - | - |
| 2026-11-14T02:00:52Z | run-state | phase | 5e2451f22100 | VERIFYING | - | - |
| 2026-11-14T02:02:40Z | run-state | brief | TOOL-aCarriedStop-9 | - | - | - |
| 2026-11-14T02:04:10Z | run-state | dispatch | TOOL-aCarriedStop-9 | - | - | - |
| 2026-11-14T02:09:26Z | run-state | phase | 4cb4b39fa5e8 | BUILDING | - | - |
| 2026-11-14T02:16:36Z | run-state | phase | 60a6d0d79abd | VERIFYING | - | - |
| 2026-11-14T05:06:32Z | run-state | brief | TOOL-aCarriedStop-9 | - | - | - |
| 2026-11-14T05:29:52Z | run-state | phase | 1f732d9ba8a3 | BUILDING | - | - |
| 2026-11-14T05:33:36Z | run-state | brief | TOOL-aCarriedStop-10 | - | - | - |
| 2026-11-14T05:34:54Z | run-state | dispatch | TOOL-aCarriedStop-10 | - | - | - |
| 2026-11-14T05:44:52Z | run-state | phase | 3d8689eaa | VERIFYING | - | - |
| 2026-11-14T09:43:18Z | run-state | phase | 3d8689eaa | LANDING | - | - |

## Units

- units: 5 · shown 5 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 2 | TOOL-aCarriedStop-2 | CLOSED | 0 | 2 | 1 | - |
| 3 | TOOL-aCarriedStop-3 | CLOSED | 0 | 1 | 1 | - |
| 4 | TOOL-aCarriedStop-9 | CLOSED | 0 | 1 | 2 | - |
| 5 | TOOL-aCarriedStop-10 | CLOSED | 0 | 1 | 1 | - |
| 5 | TOOL-aCarriedStop-1 | CLOSED | 0 | 1 | 2 | - |

## Decisions

- entries: 2 · shown 2 · aggregated no
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 2
- excluded rows: proposal 0 · rescope 4 · dispatch 6 · review 1 · brief 7 · hold 1 · resume 1
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
| 11 | spec-mark | 2 |
| 12 | decision-log | 0 |
| 13 | ledger | 0 |

| # | source | ref | verdict |
|---|---|---|---|
| 1 | spec-mark | memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-1.md | - |
| 2 | spec-mark | memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-1.md | - |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-11-13T12:34:52Z | CLEAN WITH FIXES | 0 | CONVERGED |

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

- anomalies: 20 · shown 20 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | no-progress | - |
| 2 | out-of-band-edit | - |
| 3 | out-of-band-edit | - |
| 4 | out-of-band-edit | - |
| 5 | out-of-band-edit | - |
| 6 | out-of-band-edit | - |
| 7 | out-of-band-edit | - |
| 8 | out-of-band-edit | - |
| 9 | refusal-loop | - |
| 10 | killed-verb | - |
| 11 | killed-verb | - |
| 12 | killed-verb | - |
| 13 | killed-verb | - |
| 14 | killed-verb | - |
| 15 | killed-verb | - |
| 16 | killed-verb | - |
| 17 | killed-verb | - |
| 18 | destructive-git | - |
| 19 | destructive-git | - |
| 20 | destructive-git | - |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 1
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 370 | 1 |
| 3 | gates | present | 6 | 0 |
| 4 | pushes | present | 20 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aCarriedStop/RUN.md","run":"1 of 1","start":"17926918815023997468c5021f974d2d6160ed9f","phase":"LANDING","terminal":"no","window":"2026-11-13T11:19:21Z to 2026-11-14T09:43:18Z","window opened by":"git","window closed by":"last-activity","duration":"80637s · DERIVED from the window","own commits":"0","last own commit":"-","merged":"-","units served":"5","sources present":"7 of 7","owner turns":"launch 1 · pre-run 0 · in-window 2 · post-close 0","usage main":"requests 430 · in 1016 · out 229231 · cache-read 113426742 · cache-write 1039462","usage agent":"requests 302 · in 624 · out 309825 · cache-read 28836718 · cache-write 1061523","usage workflow":"requests 99 · in 208 · out 128469 · cache-read 3951248 · cache-write 697137","attributed calls":"839 of 921","values withheld":"0","commitment":"sha256 1b07d5ce4bdb8acbea1d3a00342622f7d60372874b6f8f7c519ed6f532625ba9 · lines 416"},"tables":[]},
"Timeline":{"facts":{"events":"25 · shown 25 · elided 0","withheld rows":"verb 189 · push 20 · push-refused 0 · gate 6 · compact 3 · limit 0 · idle 0 · workflow 1"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-11-13T11:19:21Z","run-state","phase","d646814e4a6a","SPECCING","-","-"],
["2026-11-13T11:45:32Z","run-state","brief","TOOL-aCarriedStop-1","-","-","-"],
["2026-11-13T11:46:03Z","run-state","brief","TOOL-aCarriedStop-1","-","-","-"],
["2026-11-13T11:47:24Z","run-state","dispatch","TOOL-aCarriedStop-1","-","-","-"],
["2026-11-13T12:02:27Z","run-state","phase","0dd449637fb3","BUILDING","-","-"],
["2026-11-13T13:01:26Z","run-state","phase","cfda7001d79d","VERIFYING","-","-"],
["2026-11-13T13:04:06Z","run-state","brief","TOOL-aCarriedStop-2","-","-","-"],
["2026-11-13T13:05:21Z","run-state","dispatch","TOOL-aCarriedStop-2","-","-","-"],
["2026-11-13T13:13:34Z","run-state","dispatch","TOOL-aCarriedStop-2","-","-","-"],
["2026-11-13T13:13:35Z","run-state","phase","a484dc6c96ee","BUILDING","-","-"],
["2026-11-13T13:17:27Z","run-state","brief","TOOL-aCarriedStop-3","-","-","-"],
["2026-11-13T13:18:41Z","run-state","dispatch","TOOL-aCarriedStop-3","-","-","-"],
["2026-11-13T13:57:09Z","run-state","phase","41015d329ec2","VERIFYING","-","-"],
["2026-11-13T18:39:30Z","run-state","phase","4bf57cb7626b","HELD","-","-"],
["2026-11-14T02:00:52Z","run-state","phase","5e2451f22100","VERIFYING","-","-"],
["2026-11-14T02:02:40Z","run-state","brief","TOOL-aCarriedStop-9","-","-","-"],
["2026-11-14T02:04:10Z","run-state","dispatch","TOOL-aCarriedStop-9","-","-","-"],
["2026-11-14T02:09:26Z","run-state","phase","4cb4b39fa5e8","BUILDING","-","-"],
["2026-11-14T02:16:36Z","run-state","phase","60a6d0d79abd","VERIFYING","-","-"],
["2026-11-14T05:06:32Z","run-state","brief","TOOL-aCarriedStop-9","-","-","-"],
["2026-11-14T05:29:52Z","run-state","phase","1f732d9ba8a3","BUILDING","-","-"],
["2026-11-14T05:33:36Z","run-state","brief","TOOL-aCarriedStop-10","-","-","-"],
["2026-11-14T05:34:54Z","run-state","dispatch","TOOL-aCarriedStop-10","-","-","-"],
["2026-11-14T05:44:52Z","run-state","phase","3d8689eaa","VERIFYING","-","-"],
["2026-11-14T09:43:18Z","run-state","phase","3d8689eaa","LANDING","-","-"]]}]},
"Units":{"facts":{"units":"5 · shown 5 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["2","TOOL-aCarriedStop-2","CLOSED","0","2","1","-"],
["3","TOOL-aCarriedStop-3","CLOSED","0","1","1","-"],
["4","TOOL-aCarriedStop-9","CLOSED","0","1","2","-"],
["5","TOOL-aCarriedStop-10","CLOSED","0","1","1","-"],
["5","TOOL-aCarriedStop-1","CLOSED","0","1","2","-"]]}]},
"Decisions":{"facts":{"entries":"2 · shown 2 · aggregated no","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 2","excluded rows":"proposal 0 · rescope 4 · dispatch 6 · review 1 · brief 7 · hold 1 · resume 1","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
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
["11","spec-mark","2"],
["12","decision-log","0"],
["13","ledger","0"]]},
{"name":"entries","header":["#","source","ref","verdict"],"rows":[
["1","spec-mark","memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-1.md","-"],
["2","spec-mark","memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-1.md","-"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-11-13T12:34:52Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"5 · shown 5 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","-","UNJUDGEABLE"],
["2","phases-walked","-","MET"],
["3","green-at-close","-","MET"],
["4","keepalive-reaped","-","MET"],
["5","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"20 · shown 20 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","no-progress","-"],
["2","out-of-band-edit","-"],
["3","out-of-band-edit","-"],
["4","out-of-band-edit","-"],
["5","out-of-band-edit","-"],
["6","out-of-band-edit","-"],
["7","out-of-band-edit","-"],
["8","out-of-band-edit","-"],
["9","refusal-loop","-"],
["10","killed-verb","-"],
["11","killed-verb","-"],
["12","killed-verb","-"],
["13","killed-verb","-"],
["14","killed-verb","-"],
["15","killed-verb","-"],
["16","killed-verb","-"],
["17","killed-verb","-"],
["18","destructive-git","-"],
["19","destructive-git","-"],
["20","destructive-git","-"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 1","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","370","1"],
["3","gates","present","6","0"],
["4","pushes","present","20","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
