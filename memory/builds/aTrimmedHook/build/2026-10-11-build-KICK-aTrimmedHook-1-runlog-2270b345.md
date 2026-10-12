# Run record

**Serves:** journal KICK-aTrimmedHook-1 TOOL-aTrimmedHook-1..7

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aTrimmedHook/RUN.md
- run: 1 of 1
- start: 2270b34596f3e04e14d456cdf8f8b50bf869f4ae
- phase: VERIFYING
- terminal: no
- window: 2026-10-11T02:34:07Z to 2026-10-11T09:24:26Z
- window opened by: git
- window closed by: last-activity
- duration: 24619s
- own commits: 0
- last own commit: -
- merged: -
- units served: 8
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 2 · in-window 1 · post-close 0
- usage main: requests 273 · in 580 · out 227819 · cache-read 168471023 · cache-write 902527
- usage agent: requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0
- usage workflow: requests 264 · in 528 · out 230148 · cache-read 30118215 · cache-write 1285540
- attributed calls: 416 of 563
- values withheld: 0
- commitment: sha256 bfec9c3090ee9061531f0e0bb557ba315afbeb68c5d98e134965684a4b7da778 · lines 123

## Timeline

- events: 22 · shown 22 · elided 0
- withheld rows: verb 58 · push 5 · push-refused 0 · gate 0 · compact 0 · limit 13 · idle 0 · workflow 1

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-10-11T02:34:07Z | run-state | phase | 2785323db4e7 | SPECCING | - | - |
| 2026-10-11T03:26:05Z | run-state | brief | TOOL-aTrimmedHook-1 | - | - | - |
| 2026-10-11T03:46:33Z | run-state | dispatch | TOOL-aTrimmedHook-1 | - | - | - |
| 2026-10-11T05:57:40Z | run-state | dispatch | TOOL-aTrimmedHook-1 | - | - | - |
| 2026-10-11T05:58:22Z | run-state | phase | 22f32233e43f | BUILDING | - | - |
| 2026-10-11T06:00:06Z | run-state | dispatch | TOOL-aTrimmedHook-3 | - | - | - |
| 2026-10-11T06:00:11Z | run-state | brief | TOOL-aTrimmedHook-3 | - | - | - |
| 2026-10-11T06:03:47Z | run-state | dispatch | KICK-aTrimmedHook-1 | - | - | - |
| 2026-10-11T06:04:01Z | run-state | brief | KICK-aTrimmedHook-1 | - | - | - |
| 2026-10-11T06:16:17Z | run-state | dispatch | TOOL-aTrimmedHook-2 | - | - | - |
| 2026-10-11T06:16:22Z | run-state | brief | TOOL-aTrimmedHook-2 | - | - | - |
| 2026-10-11T06:19:07Z | run-state | dispatch | TOOL-aTrimmedHook-2 | - | - | - |
| 2026-10-11T07:22:02Z | run-state | phase | 704b37056ee0 | REVIEWING | - | - |
| 2026-10-11T07:42:34Z | run-state | dispatch | TOOL-aTrimmedHook-4 | - | - | - |
| 2026-10-11T07:42:55Z | run-state | brief | TOOL-aTrimmedHook-4 | - | - | - |
| 2026-10-11T07:54:16Z | run-state | brief | TOOL-aTrimmedHook-5 | - | - | - |
| 2026-10-11T07:57:08Z | run-state | dispatch | TOOL-aTrimmedHook-6 | - | - | - |
| 2026-10-11T07:57:14Z | run-state | brief | TOOL-aTrimmedHook-6 | - | - | - |
| 2026-10-11T08:00:20Z | run-state | dispatch | TOOL-aTrimmedHook-5 | - | - | - |
| 2026-10-11T08:04:18Z | run-state | dispatch | TOOL-aTrimmedHook-7 | - | - | - |
| 2026-10-11T08:04:27Z | run-state | brief | TOOL-aTrimmedHook-7 | - | - | - |
| 2026-10-11T08:19:39Z | run-state | phase | f492cf2655c0 | VERIFYING | - | - |

## Units

- units: 8 · shown 8 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | KICK-aTrimmedHook-1 | CLOSED | 0 | 1 | 1 | - |
| 1 | TOOL-aTrimmedHook-1 | CLOSED | 0 | 2 | 1 | - |
| 1 | TOOL-aTrimmedHook-3 | CLOSED | 0 | 1 | 1 | - |
| 2 | TOOL-aTrimmedHook-2 | CLOSED | 0 | 2 | 1 | - |
| 3 | TOOL-aTrimmedHook-4 | CLOSED | 0 | 1 | 1 | - |
| 3 | TOOL-aTrimmedHook-6 | CLOSED | 0 | 1 | 1 | - |
| 4 | TOOL-aTrimmedHook-5 | CLOSED | 0 | 1 | 1 | - |
| 5 | TOOL-aTrimmedHook-7 | CLOSED | 0 | 1 | 1 | - |

## Decisions

- entries: 1 · shown 1 · aggregated no
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 0
- excluded rows: proposal 0 · rescope 4 · dispatch 10 · review 1 · brief 8 · hold 0 · resume 0
- review rounds: 1 · shown 1 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 1 |
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

| # | source | ref | verdict |
|---|---|---|---|
| 1 | decision | memory/builds/aTrimmedHook/RUN.md:82 | - |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-10-11T07:19:50Z | CLEAN WITH FIXES | 0 | CONVERGED |

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

- anomalies: 11 · shown 11 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | no-progress | - |
| 2 | refusal-loop | - |
| 3 | killed-verb | - |
| 4 | killed-verb | - |
| 5 | killed-verb | - |
| 6 | destructive-git | - |
| 7 | destructive-git | - |
| 8 | destructive-git | - |
| 9 | destructive-git | - |
| 10 | destructive-git | - |
| 11 | destructive-git | - |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 0
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 113 | 0 |
| 3 | gates | present | 0 | 0 |
| 4 | pushes | present | 5 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aTrimmedHook/RUN.md","run":"1 of 1","start":"2270b34596f3e04e14d456cdf8f8b50bf869f4ae","phase":"VERIFYING","terminal":"no","window":"2026-10-11T02:34:07Z to 2026-10-11T09:24:26Z","window opened by":"git","window closed by":"last-activity","duration":"24619s","own commits":"0","last own commit":"-","merged":"-","units served":"8","sources present":"7 of 7","owner turns":"launch 1 · pre-run 2 · in-window 1 · post-close 0","usage main":"requests 273 · in 580 · out 227819 · cache-read 168471023 · cache-write 902527","usage agent":"requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0","usage workflow":"requests 264 · in 528 · out 230148 · cache-read 30118215 · cache-write 1285540","attributed calls":"416 of 563","values withheld":"0","commitment":"sha256 bfec9c3090ee9061531f0e0bb557ba315afbeb68c5d98e134965684a4b7da778 · lines 123"},"tables":[]},
"Timeline":{"facts":{"events":"22 · shown 22 · elided 0","withheld rows":"verb 58 · push 5 · push-refused 0 · gate 0 · compact 0 · limit 13 · idle 0 · workflow 1"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-10-11T02:34:07Z","run-state","phase","2785323db4e7","SPECCING","-","-"],
["2026-10-11T03:26:05Z","run-state","brief","TOOL-aTrimmedHook-1","-","-","-"],
["2026-10-11T03:46:33Z","run-state","dispatch","TOOL-aTrimmedHook-1","-","-","-"],
["2026-10-11T05:57:40Z","run-state","dispatch","TOOL-aTrimmedHook-1","-","-","-"],
["2026-10-11T05:58:22Z","run-state","phase","22f32233e43f","BUILDING","-","-"],
["2026-10-11T06:00:06Z","run-state","dispatch","TOOL-aTrimmedHook-3","-","-","-"],
["2026-10-11T06:00:11Z","run-state","brief","TOOL-aTrimmedHook-3","-","-","-"],
["2026-10-11T06:03:47Z","run-state","dispatch","KICK-aTrimmedHook-1","-","-","-"],
["2026-10-11T06:04:01Z","run-state","brief","KICK-aTrimmedHook-1","-","-","-"],
["2026-10-11T06:16:17Z","run-state","dispatch","TOOL-aTrimmedHook-2","-","-","-"],
["2026-10-11T06:16:22Z","run-state","brief","TOOL-aTrimmedHook-2","-","-","-"],
["2026-10-11T06:19:07Z","run-state","dispatch","TOOL-aTrimmedHook-2","-","-","-"],
["2026-10-11T07:22:02Z","run-state","phase","704b37056ee0","REVIEWING","-","-"],
["2026-10-11T07:42:34Z","run-state","dispatch","TOOL-aTrimmedHook-4","-","-","-"],
["2026-10-11T07:42:55Z","run-state","brief","TOOL-aTrimmedHook-4","-","-","-"],
["2026-10-11T07:54:16Z","run-state","brief","TOOL-aTrimmedHook-5","-","-","-"],
["2026-10-11T07:57:08Z","run-state","dispatch","TOOL-aTrimmedHook-6","-","-","-"],
["2026-10-11T07:57:14Z","run-state","brief","TOOL-aTrimmedHook-6","-","-","-"],
["2026-10-11T08:00:20Z","run-state","dispatch","TOOL-aTrimmedHook-5","-","-","-"],
["2026-10-11T08:04:18Z","run-state","dispatch","TOOL-aTrimmedHook-7","-","-","-"],
["2026-10-11T08:04:27Z","run-state","brief","TOOL-aTrimmedHook-7","-","-","-"],
["2026-10-11T08:19:39Z","run-state","phase","f492cf2655c0","VERIFYING","-","-"]]}]},
"Units":{"facts":{"units":"8 · shown 8 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","KICK-aTrimmedHook-1","CLOSED","0","1","1","-"],
["1","TOOL-aTrimmedHook-1","CLOSED","0","2","1","-"],
["1","TOOL-aTrimmedHook-3","CLOSED","0","1","1","-"],
["2","TOOL-aTrimmedHook-2","CLOSED","0","2","1","-"],
["3","TOOL-aTrimmedHook-4","CLOSED","0","1","1","-"],
["3","TOOL-aTrimmedHook-6","CLOSED","0","1","1","-"],
["4","TOOL-aTrimmedHook-5","CLOSED","0","1","1","-"],
["5","TOOL-aTrimmedHook-7","CLOSED","0","1","1","-"]]}]},
"Decisions":{"facts":{"entries":"1 · shown 1 · aggregated no","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 0","excluded rows":"proposal 0 · rescope 4 · dispatch 10 · review 1 · brief 8 · hold 0 · resume 0","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","1"],
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
{"name":"entries","header":["#","source","ref","verdict"],"rows":[
["1","decision","memory/builds/aTrimmedHook/RUN.md:82","-"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-10-11T07:19:50Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"5 · shown 5 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","-","UNJUDGEABLE"],
["2","phases-walked","-","UNJUDGEABLE"],
["3","green-at-close","-","UNJUDGEABLE"],
["4","keepalive-reaped","-","MET"],
["5","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"11 · shown 11 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","no-progress","-"],
["2","refusal-loop","-"],
["3","killed-verb","-"],
["4","killed-verb","-"],
["5","killed-verb","-"],
["6","destructive-git","-"],
["7","destructive-git","-"],
["8","destructive-git","-"],
["9","destructive-git","-"],
["10","destructive-git","-"],
["11","destructive-git","-"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 0","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","113","0"],
["3","gates","present","0","0"],
["4","pushes","present","5","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
