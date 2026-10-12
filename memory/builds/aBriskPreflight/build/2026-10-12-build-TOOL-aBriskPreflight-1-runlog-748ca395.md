# Run record

**Serves:** journal TOOL-aBriskPreflight-1..7 TOOL-aBriskPreflight-10 TOOL-aBriskPreflight-12

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aBriskPreflight/RUN.md
- run: 1 of 1
- start: 748ca3956581fe459933715d6b2292cd4fcd1fb0
- phase: HELD
- terminal: no
- window: 2026-10-11T01:34:39Z to 2026-10-12T05:28:39Z
- window opened by: git
- window closed by: last-activity
- duration: 100440s
- own commits: 0
- last own commit: -
- merged: -
- units served: 9
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 0 · in-window 1 · post-close 0
- usage main: requests 277 · in 596 · out 202939 · cache-read 151131981 · cache-write 5502126
- usage agent: requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0
- usage workflow: requests 1944 · in 3888 · out 1924802 · cache-read 446403051 · cache-write 17268788
- attributed calls: 1885 of 2395
- values withheld: 0
- commitment: sha256 554196f8cf92ac5dc2524d3cb4a50425f9adfdcc992eb752ede6f9d8c1feafd0 · lines 270

## Timeline

- events: 27 · shown 27 · elided 0
- withheld rows: verb 126 · push 16 · push-refused 0 · gate 2 · compact 0 · limit 15 · idle 0 · workflow 13

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-10-11T01:34:39Z | run-state | phase | 271a90045723 | RUNNING | - | - |
| 2026-10-11T03:18:05Z | run-state | phase | 748ca3956581 | SPECCING | - | - |
| 2026-10-11T03:32:06Z | run-state | phase | 5ecd06dcf6c1 | BUILDING | - | - |
| 2026-10-11T03:40:27Z | run-state | dispatch | TOOL-aBriskPreflight-1 | - | - | - |
| 2026-10-11T03:41:11Z | run-state | brief | TOOL-aBriskPreflight-1 | - | - | - |
| 2026-10-11T05:59:29Z | run-state | dispatch | TOOL-aBriskPreflight-1 | - | - | - |
| 2026-10-11T05:59:38Z | run-state | brief | TOOL-aBriskPreflight-1 | - | - | - |
| 2026-10-11T06:39:36Z | run-state | dispatch | TOOL-aBriskPreflight-5 | - | - | - |
| 2026-10-11T06:39:51Z | run-state | brief | TOOL-aBriskPreflight-5 | - | - | - |
| 2026-10-11T07:28:52Z | run-state | dispatch | TOOL-aBriskPreflight-6 | - | - | - |
| 2026-10-11T07:29:00Z | run-state | brief | TOOL-aBriskPreflight-6 | - | - | - |
| 2026-10-11T08:09:46Z | run-state | dispatch | TOOL-aBriskPreflight-2 | - | - | - |
| 2026-10-11T08:09:56Z | run-state | brief | TOOL-aBriskPreflight-2 | - | - | - |
| 2026-10-11T10:07:31Z | run-state | dispatch | TOOL-aBriskPreflight-4 | - | - | - |
| 2026-10-11T10:08:05Z | run-state | brief | TOOL-aBriskPreflight-4 | - | - | - |
| 2026-10-11T13:58:36Z | run-state | dispatch | TOOL-aBriskPreflight-3 | - | - | - |
| 2026-10-11T14:00:18Z | run-state | brief | TOOL-aBriskPreflight-3 | - | - | - |
| 2026-10-11T15:02:48Z | run-state | brief | TOOL-aBriskPreflight-10 | - | - | - |
| 2026-10-11T15:27:11Z | run-state | dispatch | TOOL-aBriskPreflight-10 | - | - | - |
| 2026-10-11T19:05:19Z | run-state | dispatch | TOOL-aBriskPreflight-7 | - | - | - |
| 2026-10-11T19:06:10Z | run-state | brief | TOOL-aBriskPreflight-7 | - | - | - |
| 2026-10-11T20:19:31Z | run-state | phase | feb305b0bb10 | REVIEWING | - | - |
| 2026-10-11T22:27:48Z | run-state | phase | bb38838401eb | SPECCING | - | - |
| 2026-10-11T22:41:23Z | run-state | dispatch | TOOL-aBriskPreflight-12 | - | - | - |
| 2026-10-11T22:42:03Z | run-state | brief | TOOL-aBriskPreflight-12 | - | - | - |
| 2026-10-11T23:41:34Z | run-state | dispatch | TOOL-aBriskPreflight-12 | - | - | - |
| 2026-10-12T03:32:43Z | run-state | phase | 7d98741e3baa | VERIFYING | - | - |

## Units

- units: 10 · shown 10 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | TOOL-aBriskPreflight-1 | CLOSED | 0 | 2 | 2 | - |
| 1 | TOOL-aBriskPreflight-5 | CLOSED | 0 | 1 | 1 | - |
| 1 | TOOL-aBriskPreflight-6 | CLOSED | 0 | 1 | 1 | - |
| 1 | TOOL-aBriskPreflight-10 | CLOSED | 0 | 1 | 1 | - |
| 2 | TOOL-aBriskPreflight-2 | CLOSED | 0 | 1 | 1 | - |
| 2 | TOOL-aBriskPreflight-4 | CLOSED | 0 | 1 | 1 | - |
| 3 | TOOL-aBriskPreflight-3 | CLOSED | 0 | 1 | 1 | - |
| 4 | TOOL-aBriskPreflight-7 | CLOSED | 0 | 1 | 1 | - |
| 6 | TOOL-aBriskPreflight-11 | SPECCED | 0 | 0 | 0 | - |
| 6 | TOOL-aBriskPreflight-12 | CLOSED | 0 | 2 | 1 | - |

## Decisions

- entries: 20 · shown 20 · aggregated no
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 17
- excluded rows: proposal 0 · rescope 3 · dispatch 11 · review 1 · brief 10 · hold 1 · resume 0
- review rounds: 1 · shown 1 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 2 |
| 2 | abort | 0 |
| 3 | override | 0 |
| 4 | waiver | 0 |
| 5 | handoff | 1 |
| 6 | rescope-retire | 0 |
| 7 | rescope-supersede | 0 |
| 8 | rescope-defer | 0 |
| 9 | review | 0 |
| 10 | trailer | 0 |
| 11 | spec-mark | 17 |
| 12 | decision-log | 0 |
| 13 | ledger | 0 |

| # | source | ref | verdict |
|---|---|---|---|
| 1 | decision | memory/builds/aBriskPreflight/RUN.md:91 | - |
| 2 | decision | memory/builds/aBriskPreflight/RUN.md:97 | - |
| 3 | handoff | memory/builds/aBriskPreflight/RUN.md:101 | - |
| 4 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-4.md | - |
| 5 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-4.md | - |
| 6 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-4.md | - |
| 7 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-4.md | - |
| 8 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-6.md | - |
| 9 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md | - |
| 10 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md | - |
| 11 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md | - |
| 12 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md | - |
| 13 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md | - |
| 14 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md | - |
| 15 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-11.md | - |
| 16 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-12.md | - |
| 17 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-12.md | - |
| 18 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-12.md | - |
| 19 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-12.md | - |
| 20 | spec-mark | memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-12.md | - |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-10-11T21:19:28Z | CLEAN WITH FIXES | 0 | CONVERGED |

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

- anomalies: 23 · shown 0 · aggregated yes

| # | kind | subclass | count |
|---|---|---|---|
| 1 | no-progress | - | 1 |
| 2 | out-of-band-edit | - | 2 |
| 3 | refusal-loop | - | 2 |
| 4 | killed-verb | - | 16 |
| 5 | destructive-git | - | 2 |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 0
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 236 | 0 |
| 3 | gates | present | 2 | 0 |
| 4 | pushes | present | 16 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aBriskPreflight/RUN.md","run":"1 of 1","start":"748ca3956581fe459933715d6b2292cd4fcd1fb0","phase":"HELD","terminal":"no","window":"2026-10-11T01:34:39Z to 2026-10-12T05:28:39Z","window opened by":"git","window closed by":"last-activity","duration":"100440s","own commits":"0","last own commit":"-","merged":"-","units served":"9","sources present":"7 of 7","owner turns":"launch 1 · pre-run 0 · in-window 1 · post-close 0","usage main":"requests 277 · in 596 · out 202939 · cache-read 151131981 · cache-write 5502126","usage agent":"requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0","usage workflow":"requests 1944 · in 3888 · out 1924802 · cache-read 446403051 · cache-write 17268788","attributed calls":"1885 of 2395","values withheld":"0","commitment":"sha256 554196f8cf92ac5dc2524d3cb4a50425f9adfdcc992eb752ede6f9d8c1feafd0 · lines 270"},"tables":[]},
"Timeline":{"facts":{"events":"27 · shown 27 · elided 0","withheld rows":"verb 126 · push 16 · push-refused 0 · gate 2 · compact 0 · limit 15 · idle 0 · workflow 13"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-10-11T01:34:39Z","run-state","phase","271a90045723","RUNNING","-","-"],
["2026-10-11T03:18:05Z","run-state","phase","748ca3956581","SPECCING","-","-"],
["2026-10-11T03:32:06Z","run-state","phase","5ecd06dcf6c1","BUILDING","-","-"],
["2026-10-11T03:40:27Z","run-state","dispatch","TOOL-aBriskPreflight-1","-","-","-"],
["2026-10-11T03:41:11Z","run-state","brief","TOOL-aBriskPreflight-1","-","-","-"],
["2026-10-11T05:59:29Z","run-state","dispatch","TOOL-aBriskPreflight-1","-","-","-"],
["2026-10-11T05:59:38Z","run-state","brief","TOOL-aBriskPreflight-1","-","-","-"],
["2026-10-11T06:39:36Z","run-state","dispatch","TOOL-aBriskPreflight-5","-","-","-"],
["2026-10-11T06:39:51Z","run-state","brief","TOOL-aBriskPreflight-5","-","-","-"],
["2026-10-11T07:28:52Z","run-state","dispatch","TOOL-aBriskPreflight-6","-","-","-"],
["2026-10-11T07:29:00Z","run-state","brief","TOOL-aBriskPreflight-6","-","-","-"],
["2026-10-11T08:09:46Z","run-state","dispatch","TOOL-aBriskPreflight-2","-","-","-"],
["2026-10-11T08:09:56Z","run-state","brief","TOOL-aBriskPreflight-2","-","-","-"],
["2026-10-11T10:07:31Z","run-state","dispatch","TOOL-aBriskPreflight-4","-","-","-"],
["2026-10-11T10:08:05Z","run-state","brief","TOOL-aBriskPreflight-4","-","-","-"],
["2026-10-11T13:58:36Z","run-state","dispatch","TOOL-aBriskPreflight-3","-","-","-"],
["2026-10-11T14:00:18Z","run-state","brief","TOOL-aBriskPreflight-3","-","-","-"],
["2026-10-11T15:02:48Z","run-state","brief","TOOL-aBriskPreflight-10","-","-","-"],
["2026-10-11T15:27:11Z","run-state","dispatch","TOOL-aBriskPreflight-10","-","-","-"],
["2026-10-11T19:05:19Z","run-state","dispatch","TOOL-aBriskPreflight-7","-","-","-"],
["2026-10-11T19:06:10Z","run-state","brief","TOOL-aBriskPreflight-7","-","-","-"],
["2026-10-11T20:19:31Z","run-state","phase","feb305b0bb10","REVIEWING","-","-"],
["2026-10-11T22:27:48Z","run-state","phase","bb38838401eb","SPECCING","-","-"],
["2026-10-11T22:41:23Z","run-state","dispatch","TOOL-aBriskPreflight-12","-","-","-"],
["2026-10-11T22:42:03Z","run-state","brief","TOOL-aBriskPreflight-12","-","-","-"],
["2026-10-11T23:41:34Z","run-state","dispatch","TOOL-aBriskPreflight-12","-","-","-"],
["2026-10-12T03:32:43Z","run-state","phase","7d98741e3baa","VERIFYING","-","-"]]}]},
"Units":{"facts":{"units":"10 · shown 10 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","TOOL-aBriskPreflight-1","CLOSED","0","2","2","-"],
["1","TOOL-aBriskPreflight-5","CLOSED","0","1","1","-"],
["1","TOOL-aBriskPreflight-6","CLOSED","0","1","1","-"],
["1","TOOL-aBriskPreflight-10","CLOSED","0","1","1","-"],
["2","TOOL-aBriskPreflight-2","CLOSED","0","1","1","-"],
["2","TOOL-aBriskPreflight-4","CLOSED","0","1","1","-"],
["3","TOOL-aBriskPreflight-3","CLOSED","0","1","1","-"],
["4","TOOL-aBriskPreflight-7","CLOSED","0","1","1","-"],
["6","TOOL-aBriskPreflight-11","SPECCED","0","0","0","-"],
["6","TOOL-aBriskPreflight-12","CLOSED","0","2","1","-"]]}]},
"Decisions":{"facts":{"entries":"20 · shown 20 · aggregated no","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 17","excluded rows":"proposal 0 · rescope 3 · dispatch 11 · review 1 · brief 10 · hold 1 · resume 0","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","2"],
["2","abort","0"],
["3","override","0"],
["4","waiver","0"],
["5","handoff","1"],
["6","rescope-retire","0"],
["7","rescope-supersede","0"],
["8","rescope-defer","0"],
["9","review","0"],
["10","trailer","0"],
["11","spec-mark","17"],
["12","decision-log","0"],
["13","ledger","0"]]},
{"name":"entries","header":["#","source","ref","verdict"],"rows":[
["1","decision","memory/builds/aBriskPreflight/RUN.md:91","-"],
["2","decision","memory/builds/aBriskPreflight/RUN.md:97","-"],
["3","handoff","memory/builds/aBriskPreflight/RUN.md:101","-"],
["4","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-4.md","-"],
["5","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-4.md","-"],
["6","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-4.md","-"],
["7","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-4.md","-"],
["8","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-6.md","-"],
["9","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md","-"],
["10","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md","-"],
["11","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md","-"],
["12","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md","-"],
["13","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md","-"],
["14","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md","-"],
["15","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-11.md","-"],
["16","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-12.md","-"],
["17","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-12.md","-"],
["18","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-12.md","-"],
["19","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-12.md","-"],
["20","spec-mark","memory/builds/aBriskPreflight/spec/2026-10-12-spec-TOOL-aBriskPreflight-12.md","-"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-10-11T21:19:28Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"5 · shown 5 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","-","UNJUDGEABLE"],
["2","phases-walked","-","UNJUDGEABLE"],
["3","green-at-close","-","UNJUDGEABLE"],
["4","keepalive-reaped","-","MET"],
["5","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"23 · shown 0 · aggregated yes"},"tables":[{"name":"by-kind","header":["#","kind","subclass","count"],"rows":[
["1","no-progress","-","1"],
["2","out-of-band-edit","-","2"],
["3","refusal-loop","-","2"],
["4","killed-verb","-","16"],
["5","destructive-git","-","2"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 0","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","236","0"],
["3","gates","present","2","0"],
["4","pushes","present","16","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
