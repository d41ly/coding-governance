# Run record

**Serves:** journal TOOL-aHeardState-1..8

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aHeardState/RUN.md
- run: 1 of 1
- start: dd96ba886c7bab7f9c592579800fdb2d63895a2c
- phase: VERIFYING
- terminal: no
- window: 2026-10-12T16:27:06Z to 2026-10-12T22:15:16Z
- window opened by: git
- window closed by: last-activity
- duration: 20890s
- own commits: 0
- last own commit: -
- merged: -
- units served: 8
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 2 · in-window 3 · post-close 0
- usage main: requests 201 · in 406 · out 154909 · cache-read 121231860 · cache-write 1266382
- usage agent: requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0
- usage workflow: requests 169 · in 338 · out 162253 · cache-read 14600662 · cache-write 986053
- attributed calls: 456 of 518
- values withheld: 0
- commitment: sha256 e6310d9ef6de8110ef2abdd3828e196bd8a579b8b94b40975c1cb6b763722872 · lines 116

## Timeline

- events: 30 · shown 30 · elided 0
- withheld rows: verb 52 · push 6 · push-refused 0 · gate 0 · compact 0 · limit 0 · idle 0 · workflow 1

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-10-12T16:27:06Z | run-state | phase | 6b32af422bc2 | RUNNING | - | - |
| 2026-10-12T16:33:00Z | run-state | brief | TOOL-aHeardState-1 | - | - | - |
| 2026-10-12T16:33:44Z | run-state | brief | TOOL-aHeardState-2 | - | - | - |
| 2026-10-12T16:41:17Z | run-state | phase | dd96ba886 | BUILDING | - | - |
| 2026-10-12T16:46:25Z | run-state | dispatch | TOOL-aHeardState-1 | - | - | - |
| 2026-10-12T17:06:38Z | run-state | dispatch | TOOL-aHeardState-1 | - | - | - |
| 2026-10-12T19:45:28Z | run-state | dispatch | TOOL-aHeardState-1 | - | - | - |
| 2026-10-12T20:01:45Z | run-state | phase | 12cb2e1b8d96 | HELD | - | - |
| 2026-10-12T21:27:56Z | run-state | phase | b1ff2069a18f | BUILDING | - | - |
| 2026-10-12T21:28:24Z | run-state | dispatch | TOOL-aHeardState-2 | - | - | - |
| 2026-10-12T21:30:08Z | run-state | dispatch | TOOL-aHeardState-2 | - | - | - |
| 2026-10-12T21:34:52Z | run-state | dispatch | TOOL-aHeardState-2 | - | - | - |
| 2026-10-12T21:53:05Z | run-state | brief | TOOL-aHeardState-3 | - | - | - |
| 2026-10-12T21:53:07Z | run-state | brief | TOOL-aHeardState-4 | - | - | - |
| 2026-10-12T21:53:09Z | run-state | brief | TOOL-aHeardState-5 | - | - | - |
| 2026-10-12T21:53:11Z | run-state | brief | TOOL-aHeardState-6 | - | - | - |
| 2026-10-12T21:53:12Z | run-state | brief | TOOL-aHeardState-7 | - | - | - |
| 2026-10-12T21:53:13Z | run-state | brief | TOOL-aHeardState-8 | - | - | - |
| 2026-10-12T21:54:30Z | run-state | dispatch | TOOL-aHeardState-3 | - | - | - |
| 2026-10-12T21:56:37Z | run-state | dispatch | TOOL-aHeardState-4 | - | - | - |
| 2026-10-12T21:58:04Z | run-state | dispatch | TOOL-aHeardState-4 | - | - | - |
| 2026-10-12T22:01:08Z | run-state | dispatch | TOOL-aHeardState-5 | - | - | - |
| 2026-10-12T22:02:01Z | run-state | dispatch | TOOL-aHeardState-6 | - | - | - |
| 2026-10-12T22:02:20Z | run-state | dispatch | TOOL-aHeardState-6 | - | - | - |
| 2026-10-12T22:03:10Z | run-state | dispatch | TOOL-aHeardState-7 | - | - | - |
| 2026-10-12T22:05:16Z | run-state | dispatch | TOOL-aHeardState-7 | - | - | - |
| 2026-10-12T22:06:35Z | run-state | dispatch | TOOL-aHeardState-8 | - | - | - |
| 2026-10-12T22:11:56Z | run-state | dispatch | TOOL-aHeardState-8 | - | - | - |
| 2026-10-12T22:12:51Z | run-state | phase | 9ea947136 | VERIFYING | - | - |
| 2026-10-12T22:14:46Z | run-state | dispatch | TOOL-aHeardState-3 | - | - | - |

## Units

- units: 8 · shown 8 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | TOOL-aHeardState-1 | CLOSED | 0 | 3 | 1 | - |
| 2 | TOOL-aHeardState-2 | CLOSED | 0 | 3 | 1 | - |
| 3 | TOOL-aHeardState-3 | CLOSED | 0 | 2 | 1 | - |
| 4 | TOOL-aHeardState-4 | CLOSED | 0 | 2 | 1 | - |
| 5 | TOOL-aHeardState-5 | CLOSED | 0 | 1 | 1 | - |
| 6 | TOOL-aHeardState-6 | CLOSED | 0 | 2 | 1 | - |
| 7 | TOOL-aHeardState-7 | CLOSED | 0 | 2 | 1 | - |
| 8 | TOOL-aHeardState-8 | CLOSED | 0 | 2 | 1 | - |

## Decisions

- entries: 7 · shown 7 · aggregated no
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 5 · agent-inside 1
- excluded rows: proposal 0 · rescope 6 · dispatch 17 · review 1 · brief 8 · hold 1 · resume 1
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
| 11 | spec-mark | 6 |
| 12 | decision-log | 0 |
| 13 | ledger | 0 |

| # | source | ref | verdict |
|---|---|---|---|
| 1 | decision | memory/builds/aHeardState/RUN.md:52 | - |
| 2 | spec-mark | memory/builds/aHeardState/spec/2026-10-11-spec-TOOL-aHeardState-1.md | - |
| 3 | spec-mark | memory/builds/aHeardState/spec/2026-10-11-spec-TOOL-aHeardState-1.md | - |
| 4 | spec-mark | memory/builds/aHeardState/spec/2026-10-11-spec-TOOL-aHeardState-1.md | - |
| 5 | spec-mark | memory/builds/aHeardState/spec/2026-10-11-spec-TOOL-aHeardState-1.md | - |
| 6 | spec-mark | memory/builds/aHeardState/spec/2026-10-11-spec-TOOL-aHeardState-2.md | - |
| 7 | spec-mark | memory/builds/aHeardState/spec/2026-10-11-spec-TOOL-aHeardState-2.md | - |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-10-12T21:49:01Z | CLEAN WITH FIXES | 0 | CONVERGED |

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

- anomalies: 2 · shown 2 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | no-progress | - |
| 2 | killed-verb | - |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 1
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 104 | 0 |
| 3 | gates | present | 0 | 0 |
| 4 | pushes | present | 6 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aHeardState/RUN.md","run":"1 of 1","start":"dd96ba886c7bab7f9c592579800fdb2d63895a2c","phase":"VERIFYING","terminal":"no","window":"2026-10-12T16:27:06Z to 2026-10-12T22:15:16Z","window opened by":"git","window closed by":"last-activity","duration":"20890s","own commits":"0","last own commit":"-","merged":"-","units served":"8","sources present":"7 of 7","owner turns":"launch 1 · pre-run 2 · in-window 3 · post-close 0","usage main":"requests 201 · in 406 · out 154909 · cache-read 121231860 · cache-write 1266382","usage agent":"requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0","usage workflow":"requests 169 · in 338 · out 162253 · cache-read 14600662 · cache-write 986053","attributed calls":"456 of 518","values withheld":"0","commitment":"sha256 e6310d9ef6de8110ef2abdd3828e196bd8a579b8b94b40975c1cb6b763722872 · lines 116"},"tables":[]},
"Timeline":{"facts":{"events":"30 · shown 30 · elided 0","withheld rows":"verb 52 · push 6 · push-refused 0 · gate 0 · compact 0 · limit 0 · idle 0 · workflow 1"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-10-12T16:27:06Z","run-state","phase","6b32af422bc2","RUNNING","-","-"],
["2026-10-12T16:33:00Z","run-state","brief","TOOL-aHeardState-1","-","-","-"],
["2026-10-12T16:33:44Z","run-state","brief","TOOL-aHeardState-2","-","-","-"],
["2026-10-12T16:41:17Z","run-state","phase","dd96ba886","BUILDING","-","-"],
["2026-10-12T16:46:25Z","run-state","dispatch","TOOL-aHeardState-1","-","-","-"],
["2026-10-12T17:06:38Z","run-state","dispatch","TOOL-aHeardState-1","-","-","-"],
["2026-10-12T19:45:28Z","run-state","dispatch","TOOL-aHeardState-1","-","-","-"],
["2026-10-12T20:01:45Z","run-state","phase","12cb2e1b8d96","HELD","-","-"],
["2026-10-12T21:27:56Z","run-state","phase","b1ff2069a18f","BUILDING","-","-"],
["2026-10-12T21:28:24Z","run-state","dispatch","TOOL-aHeardState-2","-","-","-"],
["2026-10-12T21:30:08Z","run-state","dispatch","TOOL-aHeardState-2","-","-","-"],
["2026-10-12T21:34:52Z","run-state","dispatch","TOOL-aHeardState-2","-","-","-"],
["2026-10-12T21:53:05Z","run-state","brief","TOOL-aHeardState-3","-","-","-"],
["2026-10-12T21:53:07Z","run-state","brief","TOOL-aHeardState-4","-","-","-"],
["2026-10-12T21:53:09Z","run-state","brief","TOOL-aHeardState-5","-","-","-"],
["2026-10-12T21:53:11Z","run-state","brief","TOOL-aHeardState-6","-","-","-"],
["2026-10-12T21:53:12Z","run-state","brief","TOOL-aHeardState-7","-","-","-"],
["2026-10-12T21:53:13Z","run-state","brief","TOOL-aHeardState-8","-","-","-"],
["2026-10-12T21:54:30Z","run-state","dispatch","TOOL-aHeardState-3","-","-","-"],
["2026-10-12T21:56:37Z","run-state","dispatch","TOOL-aHeardState-4","-","-","-"],
["2026-10-12T21:58:04Z","run-state","dispatch","TOOL-aHeardState-4","-","-","-"],
["2026-10-12T22:01:08Z","run-state","dispatch","TOOL-aHeardState-5","-","-","-"],
["2026-10-12T22:02:01Z","run-state","dispatch","TOOL-aHeardState-6","-","-","-"],
["2026-10-12T22:02:20Z","run-state","dispatch","TOOL-aHeardState-6","-","-","-"],
["2026-10-12T22:03:10Z","run-state","dispatch","TOOL-aHeardState-7","-","-","-"],
["2026-10-12T22:05:16Z","run-state","dispatch","TOOL-aHeardState-7","-","-","-"],
["2026-10-12T22:06:35Z","run-state","dispatch","TOOL-aHeardState-8","-","-","-"],
["2026-10-12T22:11:56Z","run-state","dispatch","TOOL-aHeardState-8","-","-","-"],
["2026-10-12T22:12:51Z","run-state","phase","9ea947136","VERIFYING","-","-"],
["2026-10-12T22:14:46Z","run-state","dispatch","TOOL-aHeardState-3","-","-","-"]]}]},
"Units":{"facts":{"units":"8 · shown 8 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","TOOL-aHeardState-1","CLOSED","0","3","1","-"],
["2","TOOL-aHeardState-2","CLOSED","0","3","1","-"],
["3","TOOL-aHeardState-3","CLOSED","0","2","1","-"],
["4","TOOL-aHeardState-4","CLOSED","0","2","1","-"],
["5","TOOL-aHeardState-5","CLOSED","0","1","1","-"],
["6","TOOL-aHeardState-6","CLOSED","0","2","1","-"],
["7","TOOL-aHeardState-7","CLOSED","0","2","1","-"],
["8","TOOL-aHeardState-8","CLOSED","0","2","1","-"]]}]},
"Decisions":{"facts":{"entries":"7 · shown 7 · aggregated no","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 5 · agent-inside 1","excluded rows":"proposal 0 · rescope 6 · dispatch 17 · review 1 · brief 8 · hold 1 · resume 1","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
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
["11","spec-mark","6"],
["12","decision-log","0"],
["13","ledger","0"]]},
{"name":"entries","header":["#","source","ref","verdict"],"rows":[
["1","decision","memory/builds/aHeardState/RUN.md:52","-"],
["2","spec-mark","memory/builds/aHeardState/spec/2026-10-11-spec-TOOL-aHeardState-1.md","-"],
["3","spec-mark","memory/builds/aHeardState/spec/2026-10-11-spec-TOOL-aHeardState-1.md","-"],
["4","spec-mark","memory/builds/aHeardState/spec/2026-10-11-spec-TOOL-aHeardState-1.md","-"],
["5","spec-mark","memory/builds/aHeardState/spec/2026-10-11-spec-TOOL-aHeardState-1.md","-"],
["6","spec-mark","memory/builds/aHeardState/spec/2026-10-11-spec-TOOL-aHeardState-2.md","-"],
["7","spec-mark","memory/builds/aHeardState/spec/2026-10-11-spec-TOOL-aHeardState-2.md","-"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-10-12T21:49:01Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"5 · shown 5 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","-","UNJUDGEABLE"],
["2","phases-walked","-","UNJUDGEABLE"],
["3","green-at-close","-","UNJUDGEABLE"],
["4","keepalive-reaped","-","UNJUDGEABLE"],
["5","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"2 · shown 2 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","no-progress","-"],
["2","killed-verb","-"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 1","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","104","0"],
["3","gates","present","0","0"],
["4","pushes","present","6","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
