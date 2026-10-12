# Run record

**Serves:** journal DEPL-dRemeasuredRender-1..4 TOOL-dRemeasuredRender-1

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/dRemeasuredRender/RUN.md
- run: 1 of 1
- start: c922c7e2a5ca7b4e59cf46aeb57e2f444d725450
- phase: LANDED
- terminal: yes
- window: 2026-10-11T09:12:00Z to 2026-10-11T14:57:57Z
- window opened by: git
- window closed by: terminal-pending
- duration: 20757s
- own commits: 8
- last own commit: 180db356e7211c4b42c4dfdd358ffda827a36fa2
- merged: yes
- units served: 5
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 0 · in-window 1 · post-close 0
- usage main: requests 245 · in 508 · out 154839 · cache-read 111703617 · cache-write 787522
- usage agent: requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0
- usage workflow: requests 165 · in 330 · out 109035 · cache-read 12885290 · cache-write 927982
- attributed calls: 364 of 429
- values withheld: 0
- commitment: sha256 9caffa241e3eba286ac4e060f0f65fd345ab13095b46bec71a3b37acdc87455c · lines 109

## Timeline

- events: 31 · shown 31 · elided 0
- withheld rows: verb 49 · push 5 · push-refused 0 · gate 1 · compact 0 · limit 0 · idle 0 · workflow 1

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-10-11T09:12:00Z | run-state | phase | 17472e212ffd | RUNNING | - | - |
| 2026-10-11T09:12:43Z | run-state | brief | TOOL-dRemeasuredRender-1 | - | - | - |
| 2026-10-11T09:14:52Z | run-state | dispatch | TOOL-dRemeasuredRender-1 | - | - | - |
| 2026-10-11T09:16:46Z | run-state | dispatch | TOOL-dRemeasuredRender-1 | - | - | - |
| 2026-10-11T09:17:41Z | run-state | dispatch | TOOL-dRemeasuredRender-1 | - | - | - |
| 2026-10-11T09:18:01Z | run-state | dispatch | TOOL-dRemeasuredRender-1 | - | - | - |
| 2026-10-11T09:18:07Z | git | commit | 7a474babe03f | - | - | TOOL-dRemeasuredRender-1 |
| 2026-10-11T09:18:07Z | run-state | phase | c922c7e2a5ca | BUILDING | - | - |
| 2026-10-11T09:20:23Z | run-state | brief | DEPL-dRemeasuredRender-1 | - | - | - |
| 2026-10-11T09:23:56Z | run-state | dispatch | DEPL-dRemeasuredRender-1 | - | - | - |
| 2026-10-11T09:24:21Z | git | commit | 473d2bbcd39d | - | - | DEPL-dRemeasuredRender-1 |
| 2026-10-11T09:24:46Z | run-state | brief | DEPL-dRemeasuredRender-2 | - | - | - |
| 2026-10-11T09:26:57Z | run-state | dispatch | DEPL-dRemeasuredRender-2 | - | - | - |
| 2026-10-11T09:27:08Z | git | commit | c38059b5a050 | - | - | DEPL-dRemeasuredRender-2 |
| 2026-10-11T09:28:49Z | git | commit | bac1a4fb5f9f | - | - | TOOL-dRemeasuredRender-1 |
| 2026-10-11T09:40:38Z | git | commit | 0fa8463e1e5f | - | - | DEPL-dRemeasuredRender-3 DEPL-dRemeasuredRender-4 |
| 2026-10-11T09:40:38Z | run-state | phase | bac1a4fb5f9f | REVIEWING | - | - |
| 2026-10-11T09:41:01Z | run-state | brief | DEPL-dRemeasuredRender-3 | - | - | - |
| 2026-10-11T09:41:01Z | run-state | brief | DEPL-dRemeasuredRender-4 | - | - | - |
| 2026-10-11T09:42:12Z | run-state | dispatch | DEPL-dRemeasuredRender-3 | - | - | - |
| 2026-10-11T09:42:16Z | git | commit | 57a98c4fcbfb | - | - | DEPL-dRemeasuredRender-3 |
| 2026-10-11T09:42:16Z | run-state | phase | 0fa8463e1e5f | BUILDING | - | - |
| 2026-10-11T09:47:02Z | run-state | dispatch | DEPL-dRemeasuredRender-4 | - | - | - |
| 2026-10-11T09:47:49Z | run-state | dispatch | DEPL-dRemeasuredRender-4 | - | - | - |
| 2026-10-11T09:47:53Z | git | commit | b41d79bc66e7 | - | - | DEPL-dRemeasuredRender-4 |
| 2026-10-11T09:49:04Z | run-state | phase | b41d79bc66e7 | VERIFYING | - | - |
| 2026-10-11T09:50:18Z | git | merge | 90244ce16979 | - | - | - |
| 2026-10-11T09:50:55Z | git | merge | 81b937f4aa7f | - | - | - |
| 2026-10-11T11:29:53Z | git | commit | 180db356e721 | - | - | DEPL-dRemeasuredRender-4 |
| 2026-10-11T11:30:15Z | git | merge | 692632c12a79 | - | - | - |
| 2026-10-11T14:57:57Z | run-state | phase | 9b37cb4757b7 | HELD | - | - |

## Units

- units: 5 · shown 5 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | TOOL-dRemeasuredRender-1 | CLOSED | 2 | 4 | 1 | 7a474babe03f |
| 2 | DEPL-dRemeasuredRender-1 | CLOSED | 1 | 1 | 1 | 473d2bbcd39d |
| 3 | DEPL-dRemeasuredRender-2 | CLOSED | 1 | 1 | 1 | c38059b5a050 |
| 4 | DEPL-dRemeasuredRender-3 | CLOSED | 2 | 1 | 1 | 57a98c4fcbfb |
| 5 | DEPL-dRemeasuredRender-4 | CLOSED | 3 | 2 | 1 | b41d79bc66e7 |

## Decisions

- entries: 19 · shown 19 · aggregated no
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 0
- excluded rows: proposal 0 · rescope 2 · dispatch 9 · review 1 · brief 5 · hold 1 · resume 0
- review rounds: 1 · shown 1 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 1 |
| 2 | abort | 0 |
| 3 | override | 0 |
| 4 | waiver | 0 |
| 5 | handoff | 1 |
| 6 | rescope-retire | 0 |
| 7 | rescope-supersede | 0 |
| 8 | rescope-defer | 0 |
| 9 | review | 1 |
| 10 | trailer | 16 |
| 11 | spec-mark | 0 |
| 12 | decision-log | 0 |
| 13 | ledger | 0 |

| # | source | ref | verdict |
|---|---|---|---|
| 1 | decision | memory/builds/dRemeasuredRender/RUN.md:83 | - |
| 2 | handoff | memory/builds/dRemeasuredRender/RUN.md:85 | - |
| 3 | review | memory/builds/dRemeasuredRender/reviews/2026-10-11-review-TOOL-dRemeasuredRender-1-closing-diff-round1.md:12 | CLEAN WITH FIXES |
| 4 | trailer | 7a474babe03f | - |
| 5 | trailer | 7a474babe03f | - |
| 6 | trailer | 7a474babe03f | - |
| 7 | trailer | 473d2bbcd39d | - |
| 8 | trailer | 473d2bbcd39d | - |
| 9 | trailer | 473d2bbcd39d | - |
| 10 | trailer | c38059b5a050 | - |
| 11 | trailer | c38059b5a050 | - |
| 12 | trailer | bac1a4fb5f9f | - |
| 13 | trailer | 0fa8463e1e5f | - |
| 14 | trailer | 0fa8463e1e5f | - |
| 15 | trailer | 0fa8463e1e5f | - |
| 16 | trailer | 57a98c4fcbfb | - |
| 17 | trailer | b41d79bc66e7 | - |
| 18 | trailer | b41d79bc66e7 | - |
| 19 | trailer | 180db356e721 | - |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-10-11T09:38:45Z | CLEAN WITH FIXES | 0 | CONVERGED |

## Conformance

- items: 9 · shown 9 · aggregated no

| # | item | unit | state |
|---|---|---|---|
| 1 | brief-before-build | DEPL-dRemeasuredRender-1 | MET |
| 2 | brief-before-build | DEPL-dRemeasuredRender-2 | MET |
| 3 | brief-before-build | DEPL-dRemeasuredRender-3 | MET |
| 4 | brief-before-build | DEPL-dRemeasuredRender-4 | MET |
| 5 | brief-before-build | TOOL-dRemeasuredRender-1 | MET |
| 6 | phases-walked | - | MET |
| 7 | green-at-close | - | UNJUDGEABLE |
| 8 | keepalive-reaped | - | MET |
| 9 | review-exited | - | MET |

## Anomalies

- anomalies: 5 · shown 5 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | out-of-band-edit | - |
| 2 | out-of-band-edit | - |
| 3 | killed-verb | - |
| 4 | killed-verb | - |
| 5 | destructive-git | - |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 0
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 98 | 0 |
| 3 | gates | present | 1 | 0 |
| 4 | pushes | present | 5 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/dRemeasuredRender/RUN.md","run":"1 of 1","start":"c922c7e2a5ca7b4e59cf46aeb57e2f444d725450","phase":"LANDED","terminal":"yes","window":"2026-10-11T09:12:00Z to 2026-10-11T14:57:57Z","window opened by":"git","window closed by":"terminal-pending","duration":"20757s","own commits":"8","last own commit":"180db356e7211c4b42c4dfdd358ffda827a36fa2","merged":"yes","units served":"5","sources present":"7 of 7","owner turns":"launch 1 · pre-run 0 · in-window 1 · post-close 0","usage main":"requests 245 · in 508 · out 154839 · cache-read 111703617 · cache-write 787522","usage agent":"requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0","usage workflow":"requests 165 · in 330 · out 109035 · cache-read 12885290 · cache-write 927982","attributed calls":"364 of 429","values withheld":"0","commitment":"sha256 9caffa241e3eba286ac4e060f0f65fd345ab13095b46bec71a3b37acdc87455c · lines 109"},"tables":[]},
"Timeline":{"facts":{"events":"31 · shown 31 · elided 0","withheld rows":"verb 49 · push 5 · push-refused 0 · gate 1 · compact 0 · limit 0 · idle 0 · workflow 1"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-10-11T09:12:00Z","run-state","phase","17472e212ffd","RUNNING","-","-"],
["2026-10-11T09:12:43Z","run-state","brief","TOOL-dRemeasuredRender-1","-","-","-"],
["2026-10-11T09:14:52Z","run-state","dispatch","TOOL-dRemeasuredRender-1","-","-","-"],
["2026-10-11T09:16:46Z","run-state","dispatch","TOOL-dRemeasuredRender-1","-","-","-"],
["2026-10-11T09:17:41Z","run-state","dispatch","TOOL-dRemeasuredRender-1","-","-","-"],
["2026-10-11T09:18:01Z","run-state","dispatch","TOOL-dRemeasuredRender-1","-","-","-"],
["2026-10-11T09:18:07Z","git","commit","7a474babe03f","-","-","TOOL-dRemeasuredRender-1"],
["2026-10-11T09:18:07Z","run-state","phase","c922c7e2a5ca","BUILDING","-","-"],
["2026-10-11T09:20:23Z","run-state","brief","DEPL-dRemeasuredRender-1","-","-","-"],
["2026-10-11T09:23:56Z","run-state","dispatch","DEPL-dRemeasuredRender-1","-","-","-"],
["2026-10-11T09:24:21Z","git","commit","473d2bbcd39d","-","-","DEPL-dRemeasuredRender-1"],
["2026-10-11T09:24:46Z","run-state","brief","DEPL-dRemeasuredRender-2","-","-","-"],
["2026-10-11T09:26:57Z","run-state","dispatch","DEPL-dRemeasuredRender-2","-","-","-"],
["2026-10-11T09:27:08Z","git","commit","c38059b5a050","-","-","DEPL-dRemeasuredRender-2"],
["2026-10-11T09:28:49Z","git","commit","bac1a4fb5f9f","-","-","TOOL-dRemeasuredRender-1"],
["2026-10-11T09:40:38Z","git","commit","0fa8463e1e5f","-","-","DEPL-dRemeasuredRender-3 DEPL-dRemeasuredRender-4"],
["2026-10-11T09:40:38Z","run-state","phase","bac1a4fb5f9f","REVIEWING","-","-"],
["2026-10-11T09:41:01Z","run-state","brief","DEPL-dRemeasuredRender-3","-","-","-"],
["2026-10-11T09:41:01Z","run-state","brief","DEPL-dRemeasuredRender-4","-","-","-"],
["2026-10-11T09:42:12Z","run-state","dispatch","DEPL-dRemeasuredRender-3","-","-","-"],
["2026-10-11T09:42:16Z","git","commit","57a98c4fcbfb","-","-","DEPL-dRemeasuredRender-3"],
["2026-10-11T09:42:16Z","run-state","phase","0fa8463e1e5f","BUILDING","-","-"],
["2026-10-11T09:47:02Z","run-state","dispatch","DEPL-dRemeasuredRender-4","-","-","-"],
["2026-10-11T09:47:49Z","run-state","dispatch","DEPL-dRemeasuredRender-4","-","-","-"],
["2026-10-11T09:47:53Z","git","commit","b41d79bc66e7","-","-","DEPL-dRemeasuredRender-4"],
["2026-10-11T09:49:04Z","run-state","phase","b41d79bc66e7","VERIFYING","-","-"],
["2026-10-11T09:50:18Z","git","merge","90244ce16979","-","-","-"],
["2026-10-11T09:50:55Z","git","merge","81b937f4aa7f","-","-","-"],
["2026-10-11T11:29:53Z","git","commit","180db356e721","-","-","DEPL-dRemeasuredRender-4"],
["2026-10-11T11:30:15Z","git","merge","692632c12a79","-","-","-"],
["2026-10-11T14:57:57Z","run-state","phase","9b37cb4757b7","HELD","-","-"]]}]},
"Units":{"facts":{"units":"5 · shown 5 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","TOOL-dRemeasuredRender-1","CLOSED","2","4","1","7a474babe03f"],
["2","DEPL-dRemeasuredRender-1","CLOSED","1","1","1","473d2bbcd39d"],
["3","DEPL-dRemeasuredRender-2","CLOSED","1","1","1","c38059b5a050"],
["4","DEPL-dRemeasuredRender-3","CLOSED","2","1","1","57a98c4fcbfb"],
["5","DEPL-dRemeasuredRender-4","CLOSED","3","2","1","b41d79bc66e7"]]}]},
"Decisions":{"facts":{"entries":"19 · shown 19 · aggregated no","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 0","excluded rows":"proposal 0 · rescope 2 · dispatch 9 · review 1 · brief 5 · hold 1 · resume 0","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","1"],
["2","abort","0"],
["3","override","0"],
["4","waiver","0"],
["5","handoff","1"],
["6","rescope-retire","0"],
["7","rescope-supersede","0"],
["8","rescope-defer","0"],
["9","review","1"],
["10","trailer","16"],
["11","spec-mark","0"],
["12","decision-log","0"],
["13","ledger","0"]]},
{"name":"entries","header":["#","source","ref","verdict"],"rows":[
["1","decision","memory/builds/dRemeasuredRender/RUN.md:83","-"],
["2","handoff","memory/builds/dRemeasuredRender/RUN.md:85","-"],
["3","review","memory/builds/dRemeasuredRender/reviews/2026-10-11-review-TOOL-dRemeasuredRender-1-closing-diff-round1.md:12","CLEAN WITH FIXES"],
["4","trailer","7a474babe03f","-"],
["5","trailer","7a474babe03f","-"],
["6","trailer","7a474babe03f","-"],
["7","trailer","473d2bbcd39d","-"],
["8","trailer","473d2bbcd39d","-"],
["9","trailer","473d2bbcd39d","-"],
["10","trailer","c38059b5a050","-"],
["11","trailer","c38059b5a050","-"],
["12","trailer","bac1a4fb5f9f","-"],
["13","trailer","0fa8463e1e5f","-"],
["14","trailer","0fa8463e1e5f","-"],
["15","trailer","0fa8463e1e5f","-"],
["16","trailer","57a98c4fcbfb","-"],
["17","trailer","b41d79bc66e7","-"],
["18","trailer","b41d79bc66e7","-"],
["19","trailer","180db356e721","-"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-10-11T09:38:45Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"9 · shown 9 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","DEPL-dRemeasuredRender-1","MET"],
["2","brief-before-build","DEPL-dRemeasuredRender-2","MET"],
["3","brief-before-build","DEPL-dRemeasuredRender-3","MET"],
["4","brief-before-build","DEPL-dRemeasuredRender-4","MET"],
["5","brief-before-build","TOOL-dRemeasuredRender-1","MET"],
["6","phases-walked","-","MET"],
["7","green-at-close","-","UNJUDGEABLE"],
["8","keepalive-reaped","-","MET"],
["9","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"5 · shown 5 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","out-of-band-edit","-"],
["2","out-of-band-edit","-"],
["3","killed-verb","-"],
["4","killed-verb","-"],
["5","destructive-git","-"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 0","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","98","0"],
["3","gates","present","1","0"],
["4","pushes","present","5","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
