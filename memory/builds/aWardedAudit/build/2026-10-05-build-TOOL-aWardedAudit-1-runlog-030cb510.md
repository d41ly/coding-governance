# Run record

**Serves:** journal TOOL-aWardedAudit-1..3 TOOL-aWardedAudit-5..6

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aWardedAudit/RUN.md
- run: 1 of 1
- start: 030cb510e2784ea90ea126aa0610f609de20330b
- phase: VERIFYING
- terminal: no
- window: 2026-10-04T22:10:27Z to 2026-10-04T23:12:51Z
- window opened by: git
- window closed by: last-activity
- duration: 3744s
- own commits: 8
- last own commit: 369fabcd7b13f8cb7ac0161b8c4e8d46c01d7a07
- merged: no
- units served: 5
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 0 · in-window 0 · post-close 0
- usage main: requests 200 · in 412 · out 146425 · cache-read 79900014 · cache-write 2218656
- usage agent: requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0
- usage workflow: requests 199 · in 398 · out 178418 · cache-read 24138616 · cache-write 1350053
- attributed calls: 288 of 404
- values withheld: 1
- commitment: sha256 180d03b92243dd342219e31a489cf85463573219f80a97523689a127a6eb76fc · lines 88

## Timeline

- events: 26 · shown 26 · elided 0
- withheld rows: verb 41 · push 3 · push-refused 0 · gate 0 · compact 0 · limit 0 · idle 0 · workflow 1

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-10-04T22:10:27Z | run-state | phase | 856ad8a68562 | RUNNING | - | - |
| 2026-10-04T22:10:59Z | run-state | brief | TOOL-aWardedAudit-1 | - | - | - |
| 2026-10-04T22:11:06Z | run-state | dispatch | TOOL-aWardedAudit-1 | - | - | - |
| 2026-10-04T22:11:33Z | run-state | phase | 030cb510e278 | BUILDING | - | - |
| 2026-10-04T22:15:46Z | git | commit | 1872bdfe527f | - | - | TOOL-aWardedAudit-1 |
| 2026-10-04T22:16:18Z | run-state | brief | TOOL-aWardedAudit-2 | - | - | - |
| 2026-10-04T22:16:26Z | run-state | dispatch | TOOL-aWardedAudit-2 | - | - | - |
| 2026-10-04T22:18:16Z | git | commit | 0268517dc108 | - | - | TOOL-aWardedAudit-2 |
| 2026-10-04T22:19:00Z | run-state | brief | TOOL-aWardedAudit-3 | - | - | - |
| 2026-10-04T22:21:13Z | run-state | dispatch | TOOL-aWardedAudit-2 | - | - | - |
| 2026-10-04T22:21:26Z | git | commit | b7e60ce54a4c | - | - | TOOL-aWardedAudit-2 |
| 2026-10-04T22:21:44Z | git | commit | f28ff537bf89 | - | - | TOOL-aWardedAudit-2 |
| 2026-10-04T22:24:10Z | run-state | dispatch | TOOL-aWardedAudit-3 | - | - | - |
| 2026-10-04T22:26:30Z | run-state | dispatch | TOOL-aWardedAudit-3 | - | - | - |
| 2026-10-04T22:27:06Z | git | commit | 3716c19f05e6 | - | - | TOOL-aWardedAudit-3 |
| 2026-10-04T22:27:56Z | git | commit | 936607ebbd25 | - | - | - |
| 2026-10-04T22:30:18Z | run-state | phase | f70bd40f1d81 | REVIEWING | - | - |
| 2026-10-04T22:47:27Z | run-state | brief | TOOL-aWardedAudit-5 | - | - | - |
| 2026-10-04T22:47:30Z | run-state | brief | TOOL-aWardedAudit-6 | - | - | - |
| 2026-10-04T22:47:42Z | run-state | dispatch | TOOL-aWardedAudit-5 | - | - | - |
| 2026-10-04T22:47:47Z | run-state | phase | aa14e5eb1b1c | BUILDING | - | - |
| 2026-10-04T23:03:14Z | git | commit | c47342a38233 | - | - | TOOL-aWardedAudit-5 |
| 2026-10-04T23:04:11Z | run-state | dispatch | TOOL-aWardedAudit-6 | - | - | - |
| 2026-10-04T23:10:49Z | git | commit | 369fabcd7b13 | - | - | TOOL-aWardedAudit-6 |
| 2026-10-04T23:12:51Z | run-state | phase | 0ee7ce9d8c80 | VERIFYING | - | - |
| 2026-10-04T23:14:57Z | git | merge | 491eee9e1572 | - | - | - |

## Units

- units: 5 · shown 5 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | TOOL-aWardedAudit-1 | CLOSED | 1 | 1 | 1 | 1872bdfe527f |
| 2 | TOOL-aWardedAudit-2 | CLOSED | 3 | 2 | 1 | 0268517dc108 |
| 3 | TOOL-aWardedAudit-3 | CLOSED | 1 | 2 | 1 | 3716c19f05e6 |
| 5 | TOOL-aWardedAudit-5 | CLOSED | 1 | 1 | 1 | c47342a38233 |
| 6 | TOOL-aWardedAudit-6 | CLOSED | 1 | 1 | 1 | 369fabcd7b13 |

## Decisions

- entries: 7 · shown 7 · aggregated no
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 0
- excluded rows: proposal 0 · rescope 2 · dispatch 7 · review 1 · brief 5 · hold 0 · resume 0
- review rounds: 1 · shown 1 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 2 |
| 2 | abort | 0 |
| 3 | override | 0 |
| 4 | waiver | 0 |
| 5 | handoff | 0 |
| 6 | rescope-retire | 0 |
| 7 | rescope-supersede | 0 |
| 8 | rescope-defer | 0 |
| 9 | review | 1 |
| 10 | trailer | 3 |
| 11 | spec-mark | 0 |
| 12 | decision-log | 1 |
| 13 | ledger | 0 |

| # | source | ref | verdict |
|---|---|---|---|
| 1 | decision | memory/builds/aWardedAudit/RUN.md:58 | - |
| 2 | decision | memory/builds/aWardedAudit/RUN.md:60 | - |
| 3 | review | memory/builds/aWardedAudit/reviews/2026-10-05-review-TOOL-aWardedAudit-1-closing-diff-round1.md:17 | CLEAN WITH FIXES |
| 4 | trailer | 1872bdfe527f | - |
| 5 | trailer | 1872bdfe527f | - |
| 6 | trailer | 0268517dc108 | - |
| 7 | decision-log | 936607ebbd25 | - |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-10-04T22:42:18Z | CLEAN WITH FIXES | 0 | CONVERGED |

## Conformance

- items: 9 · shown 9 · aggregated no

| # | item | unit | state |
|---|---|---|---|
| 1 | brief-before-build | TOOL-aWardedAudit-1 | MET |
| 2 | brief-before-build | TOOL-aWardedAudit-2 | MET |
| 3 | brief-before-build | TOOL-aWardedAudit-3 | MET |
| 4 | brief-before-build | TOOL-aWardedAudit-5 | MET |
| 5 | brief-before-build | TOOL-aWardedAudit-6 | MET |
| 6 | phases-walked | - | UNJUDGEABLE |
| 7 | green-at-close | - | UNJUDGEABLE |
| 8 | keepalive-reaped | - | MET |
| 9 | review-exited | - | MET |

## Anomalies

- anomalies: 1 · shown 1 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | destructive-git | - |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 0
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 82 | 0 |
| 3 | gates | present | 0 | 0 |
| 4 | pushes | present | 3 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aWardedAudit/RUN.md","run":"1 of 1","start":"030cb510e2784ea90ea126aa0610f609de20330b","phase":"VERIFYING","terminal":"no","window":"2026-10-04T22:10:27Z to 2026-10-04T23:12:51Z","window opened by":"git","window closed by":"last-activity","duration":"3744s","own commits":"8","last own commit":"369fabcd7b13f8cb7ac0161b8c4e8d46c01d7a07","merged":"no","units served":"5","sources present":"7 of 7","owner turns":"launch 1 · pre-run 0 · in-window 0 · post-close 0","usage main":"requests 200 · in 412 · out 146425 · cache-read 79900014 · cache-write 2218656","usage agent":"requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0","usage workflow":"requests 199 · in 398 · out 178418 · cache-read 24138616 · cache-write 1350053","attributed calls":"288 of 404","values withheld":"1","commitment":"sha256 180d03b92243dd342219e31a489cf85463573219f80a97523689a127a6eb76fc · lines 88"},"tables":[]},
"Timeline":{"facts":{"events":"26 · shown 26 · elided 0","withheld rows":"verb 41 · push 3 · push-refused 0 · gate 0 · compact 0 · limit 0 · idle 0 · workflow 1"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-10-04T22:10:27Z","run-state","phase","856ad8a68562","RUNNING","-","-"],
["2026-10-04T22:10:59Z","run-state","brief","TOOL-aWardedAudit-1","-","-","-"],
["2026-10-04T22:11:06Z","run-state","dispatch","TOOL-aWardedAudit-1","-","-","-"],
["2026-10-04T22:11:33Z","run-state","phase","030cb510e278","BUILDING","-","-"],
["2026-10-04T22:15:46Z","git","commit","1872bdfe527f","-","-","TOOL-aWardedAudit-1"],
["2026-10-04T22:16:18Z","run-state","brief","TOOL-aWardedAudit-2","-","-","-"],
["2026-10-04T22:16:26Z","run-state","dispatch","TOOL-aWardedAudit-2","-","-","-"],
["2026-10-04T22:18:16Z","git","commit","0268517dc108","-","-","TOOL-aWardedAudit-2"],
["2026-10-04T22:19:00Z","run-state","brief","TOOL-aWardedAudit-3","-","-","-"],
["2026-10-04T22:21:13Z","run-state","dispatch","TOOL-aWardedAudit-2","-","-","-"],
["2026-10-04T22:21:26Z","git","commit","b7e60ce54a4c","-","-","TOOL-aWardedAudit-2"],
["2026-10-04T22:21:44Z","git","commit","f28ff537bf89","-","-","TOOL-aWardedAudit-2"],
["2026-10-04T22:24:10Z","run-state","dispatch","TOOL-aWardedAudit-3","-","-","-"],
["2026-10-04T22:26:30Z","run-state","dispatch","TOOL-aWardedAudit-3","-","-","-"],
["2026-10-04T22:27:06Z","git","commit","3716c19f05e6","-","-","TOOL-aWardedAudit-3"],
["2026-10-04T22:27:56Z","git","commit","936607ebbd25","-","-","-"],
["2026-10-04T22:30:18Z","run-state","phase","f70bd40f1d81","REVIEWING","-","-"],
["2026-10-04T22:47:27Z","run-state","brief","TOOL-aWardedAudit-5","-","-","-"],
["2026-10-04T22:47:30Z","run-state","brief","TOOL-aWardedAudit-6","-","-","-"],
["2026-10-04T22:47:42Z","run-state","dispatch","TOOL-aWardedAudit-5","-","-","-"],
["2026-10-04T22:47:47Z","run-state","phase","aa14e5eb1b1c","BUILDING","-","-"],
["2026-10-04T23:03:14Z","git","commit","c47342a38233","-","-","TOOL-aWardedAudit-5"],
["2026-10-04T23:04:11Z","run-state","dispatch","TOOL-aWardedAudit-6","-","-","-"],
["2026-10-04T23:10:49Z","git","commit","369fabcd7b13","-","-","TOOL-aWardedAudit-6"],
["2026-10-04T23:12:51Z","run-state","phase","0ee7ce9d8c80","VERIFYING","-","-"],
["2026-10-04T23:14:57Z","git","merge","491eee9e1572","-","-","-"]]}]},
"Units":{"facts":{"units":"5 · shown 5 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","TOOL-aWardedAudit-1","CLOSED","1","1","1","1872bdfe527f"],
["2","TOOL-aWardedAudit-2","CLOSED","3","2","1","0268517dc108"],
["3","TOOL-aWardedAudit-3","CLOSED","1","2","1","3716c19f05e6"],
["5","TOOL-aWardedAudit-5","CLOSED","1","1","1","c47342a38233"],
["6","TOOL-aWardedAudit-6","CLOSED","1","1","1","369fabcd7b13"]]}]},
"Decisions":{"facts":{"entries":"7 · shown 7 · aggregated no","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 0","excluded rows":"proposal 0 · rescope 2 · dispatch 7 · review 1 · brief 5 · hold 0 · resume 0","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","2"],
["2","abort","0"],
["3","override","0"],
["4","waiver","0"],
["5","handoff","0"],
["6","rescope-retire","0"],
["7","rescope-supersede","0"],
["8","rescope-defer","0"],
["9","review","1"],
["10","trailer","3"],
["11","spec-mark","0"],
["12","decision-log","1"],
["13","ledger","0"]]},
{"name":"entries","header":["#","source","ref","verdict"],"rows":[
["1","decision","memory/builds/aWardedAudit/RUN.md:58","-"],
["2","decision","memory/builds/aWardedAudit/RUN.md:60","-"],
["3","review","memory/builds/aWardedAudit/reviews/2026-10-05-review-TOOL-aWardedAudit-1-closing-diff-round1.md:17","CLEAN WITH FIXES"],
["4","trailer","1872bdfe527f","-"],
["5","trailer","1872bdfe527f","-"],
["6","trailer","0268517dc108","-"],
["7","decision-log","936607ebbd25","-"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-10-04T22:42:18Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"9 · shown 9 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","TOOL-aWardedAudit-1","MET"],
["2","brief-before-build","TOOL-aWardedAudit-2","MET"],
["3","brief-before-build","TOOL-aWardedAudit-3","MET"],
["4","brief-before-build","TOOL-aWardedAudit-5","MET"],
["5","brief-before-build","TOOL-aWardedAudit-6","MET"],
["6","phases-walked","-","UNJUDGEABLE"],
["7","green-at-close","-","UNJUDGEABLE"],
["8","keepalive-reaped","-","MET"],
["9","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"1 · shown 1 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","destructive-git","-"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 0","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","82","0"],
["3","gates","present","0","0"],
["4","pushes","present","3","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
