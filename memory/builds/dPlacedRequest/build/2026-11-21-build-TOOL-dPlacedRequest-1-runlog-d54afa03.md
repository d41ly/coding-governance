# Run record

**Serves:** journal TOOL-dPlacedRequest-1..21 TOOL-dPlacedRequest-23..64 TOOL-dPlacedRequest-95..100

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/dPlacedRequest/RUN.md
- run: 2 of 2
- start: d54afa0314ef243cc5eee195096e69d93a64c882
- phase: LANDING
- terminal: no
- window: 2026-11-19T03:12:10Z to 2026-11-21T11:44:45Z
- window opened by: git
- window closed by: last-activity
- duration: 203555s · DERIVED from the window
- own commits: 0
- last own commit: -
- merged: -
- units served: 69
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 0 · in-window 6 · post-close 0
- usage main: requests 2277 · in 5366 · out 1468706 · cache-read 1063866588 · cache-write 3387859
- usage agent: requests 1739 · in 3540 · out 1726635 · cache-read 257848086 · cache-write 4938761
- usage workflow: requests 9394 · in 18944 · out 7636022 · cache-read 1575520451 · cache-write 27144864
- attributed calls: 12656 of 14653
- values withheld: 0
- commitment: sha256 73670bb3a876f829e55f6d40a21cf667f3be0ce4d36fa2041330862061f3323b · lines 3388

## Timeline

- events: 225 · shown 60 · elided 165
- elided: 165 events from 2026-11-19T12:28:23Z to 2026-11-20T16:15:13Z
- withheld rows: verb 1345 · push 300 · push-refused 0 · gate 99 · compact 5 · limit 8 · idle 1 · workflow 90

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-11-19T03:12:10Z | run-state | phase | 9e21ac760dc0 | RUNNING | - | - |
| 2026-11-19T03:48:35Z | run-state | phase | 15d20d36330b | REVIEWING | - | - |
| 2026-11-19T06:50:21Z | run-state | dispatch | TOOL-dPlacedRequest-11 | - | - | - |
| 2026-11-19T06:51:41Z | run-state | phase | 88f3b4132f3c | BUILDING | - | - |
| 2026-11-19T06:52:34Z | run-state | brief | TOOL-dPlacedRequest-11 | - | - | - |
| 2026-11-19T07:10:11Z | run-state | dispatch | TOOL-dPlacedRequest-11 | - | - | - |
| 2026-11-19T07:11:48Z | run-state | dispatch | TOOL-dPlacedRequest-11 | - | - | - |
| 2026-11-19T07:32:56Z | run-state | dispatch | TOOL-dPlacedRequest-13 | - | - | - |
| 2026-11-19T07:39:45Z | run-state | brief | TOOL-dPlacedRequest-13 | - | - | - |
| 2026-11-19T08:04:18Z | run-state | dispatch | TOOL-dPlacedRequest-1 | - | - | - |
| 2026-11-19T08:07:38Z | run-state | brief | TOOL-dPlacedRequest-1 | - | - | - |
| 2026-11-19T08:55:29Z | run-state | dispatch | TOOL-dPlacedRequest-27 | - | - | - |
| 2026-11-19T08:57:08Z | run-state | brief | TOOL-dPlacedRequest-27 | - | - | - |
| 2026-11-19T09:06:17Z | run-state | dispatch | TOOL-dPlacedRequest-17 | - | - | - |
| 2026-11-19T09:17:21Z | run-state | brief | TOOL-dPlacedRequest-17 | - | - | - |
| 2026-11-19T09:41:29Z | run-state | dispatch | TOOL-dPlacedRequest-23 | - | - | - |
| 2026-11-19T09:43:47Z | run-state | brief | TOOL-dPlacedRequest-23 | - | - | - |
| 2026-11-19T09:53:15Z | run-state | dispatch | TOOL-dPlacedRequest-24 | - | - | - |
| 2026-11-19T10:21:17Z | run-state | brief | TOOL-dPlacedRequest-24 | - | - | - |
| 2026-11-19T10:31:09Z | run-state | dispatch | TOOL-dPlacedRequest-25 | - | - | - |
| 2026-11-19T10:33:59Z | run-state | brief | TOOL-dPlacedRequest-25 | - | - | - |
| 2026-11-19T10:45:59Z | run-state | dispatch | TOOL-dPlacedRequest-16 | - | - | - |
| 2026-11-19T11:15:25Z | run-state | brief | TOOL-dPlacedRequest-16 | - | - | - |
| 2026-11-19T11:16:19Z | run-state | dispatch | TOOL-dPlacedRequest-16 | - | - | - |
| 2026-11-19T11:49:25Z | run-state | dispatch | TOOL-dPlacedRequest-16 | - | - | - |
| 2026-11-19T11:56:24Z | run-state | dispatch | TOOL-dPlacedRequest-16 | - | - | - |
| 2026-11-19T12:03:00Z | run-state | dispatch | TOOL-dPlacedRequest-26 | - | - | - |
| 2026-11-19T12:04:51Z | run-state | brief | TOOL-dPlacedRequest-26 | - | - | - |
| 2026-11-19T12:15:33Z | run-state | dispatch | TOOL-dPlacedRequest-36 | - | - | - |
| 2026-11-19T12:17:28Z | run-state | brief | TOOL-dPlacedRequest-36 | - | - | - |

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-11-20T18:37:56Z | run-state | phase | e267d213c519 | HELD | - | - |
| 2026-11-20T20:55:37Z | run-state | phase | 6277b70848ba | BUILDING | - | - |
| 2026-11-20T21:02:47Z | run-state | dispatch | TOOL-dPlacedRequest-95 | - | - | - |
| 2026-11-20T21:03:51Z | run-state | brief | TOOL-dPlacedRequest-95 | - | - | - |
| 2026-11-20T21:16:21Z | run-state | dispatch | TOOL-dPlacedRequest-95 | - | - | - |
| 2026-11-20T21:27:34Z | run-state | dispatch | TOOL-dPlacedRequest-96 | - | - | - |
| 2026-11-20T21:29:10Z | run-state | brief | TOOL-dPlacedRequest-96 | - | - | - |
| 2026-11-20T21:38:41Z | run-state | dispatch | TOOL-dPlacedRequest-96 | - | - | - |
| 2026-11-20T21:46:37Z | run-state | dispatch | TOOL-dPlacedRequest-97 | - | - | - |
| 2026-11-20T21:48:11Z | run-state | brief | TOOL-dPlacedRequest-97 | - | - | - |
| 2026-11-20T21:58:49Z | run-state | dispatch | TOOL-dPlacedRequest-97 | - | - | - |
| 2026-11-20T22:02:39Z | run-state | dispatch | TOOL-dPlacedRequest-98 | - | - | - |
| 2026-11-20T22:04:11Z | run-state | brief | TOOL-dPlacedRequest-98 | - | - | - |
| 2026-11-20T22:14:42Z | run-state | dispatch | TOOL-dPlacedRequest-98 | - | - | - |
| 2026-11-20T22:21:17Z | run-state | dispatch | TOOL-dPlacedRequest-98 | - | - | - |
| 2026-11-20T22:27:52Z | run-state | dispatch | TOOL-dPlacedRequest-99 | - | - | - |
| 2026-11-20T22:29:24Z | run-state | brief | TOOL-dPlacedRequest-99 | - | - | - |
| 2026-11-20T22:56:49Z | run-state | dispatch | TOOL-dPlacedRequest-99 | - | - | - |
| 2026-11-20T23:10:25Z | run-state | dispatch | TOOL-dPlacedRequest-99 | - | - | - |
| 2026-11-20T23:16:42Z | run-state | dispatch | TOOL-dPlacedRequest-100 | - | - | - |
| 2026-11-20T23:18:57Z | run-state | brief | TOOL-dPlacedRequest-100 | - | - | - |
| 2026-11-20T23:29:01Z | run-state | dispatch | TOOL-dPlacedRequest-100 | - | - | - |
| 2026-11-20T23:32:22Z | run-state | dispatch | TOOL-dPlacedRequest-100 | - | - | - |
| 2026-11-20T23:34:36Z | run-state | dispatch | TOOL-dPlacedRequest-100 | - | - | - |
| 2026-11-21T00:01:25Z | run-state | phase | 2db4a921f14d | VERIFYING | - | - |
| 2026-11-21T02:26:01Z | run-state | phase | 870ddd2b20dc | HELD | - | - |
| 2026-11-21T02:37:25Z | run-state | phase | 8e8230d305b0 | VERIFYING | - | - |
| 2026-11-21T09:12:42Z | run-state | phase | a8bbf1990fb6 | HELD | - | - |
| 2026-11-21T11:07:43Z | run-state | phase | 6b3ebc830841 | VERIFYING | - | - |
| 2026-11-21T11:44:45Z | run-state | phase | 6b3ebc830841 | LANDING | - | - |

## Units

- units: 69 · shown 0 · aggregated yes

| # | status | units |
|---|---|---|
| 1 | CLOSED | 69 |

## Decisions

- entries: 238 · shown 0 · aggregated yes
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 4 · owner-inside 0 · agent-before 139 · agent-inside 88
- excluded rows: proposal 0 · rescope 7 · dispatch 145 · review 6 · brief 69 · hold 3 · resume 3 · refusal 0 · fix-pass 0
- review rounds: 6 · shown 6 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 3 |
| 2 | abort | 0 |
| 3 | override | 1 |
| 4 | waiver | 0 |
| 5 | handoff | 3 |
| 6 | rescope-retire | 0 |
| 7 | rescope-supersede | 0 |
| 8 | rescope-defer | 0 |
| 9 | review | 0 |
| 10 | trailer | 0 |
| 11 | spec-mark | 231 |
| 12 | decision-log | 0 |
| 13 | ledger | 0 |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-11-19T04:43:32Z | CLEAN | 0 | CONVERGED |
| 2 | 2026-11-19T05:52:49Z | CLEAN | 0 | CONVERGED |
| 3 | 2026-11-19T06:46:56Z | CLEAN | 0 | CONVERGED |
| 4 | 2026-11-20T16:29:18Z | CLEAN WITH FIXES | 0 | - |
| 5 | 2026-11-20T16:45:00Z | CLEAN WITH FIXES | 0 | NON-CONVERGENT |
| 6 | 2026-11-20T18:35:01Z | CLEAN | 0 | CONVERGED |

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

- anomalies: 60 · shown 0 · aggregated yes

| # | kind | subclass | count |
|---|---|---|---|
| 1 | no-progress | - | 1 |
| 2 | out-of-band-edit | - | 5 |
| 3 | refusal-loop | - | 3 |
| 4 | killed-verb | - | 11 |
| 5 | destructive-git | - | 39 |
| 6 | idle-gap | - | 1 |

## Coverage

- journal starts: 0 joined of 0 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 2
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 2689 | 0 |
| 3 | gates | present | 99 | 0 |
| 4 | pushes | present | 300 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/dPlacedRequest/RUN.md","run":"2 of 2","start":"d54afa0314ef243cc5eee195096e69d93a64c882","phase":"LANDING","terminal":"no","window":"2026-11-19T03:12:10Z to 2026-11-21T11:44:45Z","window opened by":"git","window closed by":"last-activity","duration":"203555s · DERIVED from the window","own commits":"0","last own commit":"-","merged":"-","units served":"69","sources present":"7 of 7","owner turns":"launch 1 · pre-run 0 · in-window 6 · post-close 0","usage main":"requests 2277 · in 5366 · out 1468706 · cache-read 1063866588 · cache-write 3387859","usage agent":"requests 1739 · in 3540 · out 1726635 · cache-read 257848086 · cache-write 4938761","usage workflow":"requests 9394 · in 18944 · out 7636022 · cache-read 1575520451 · cache-write 27144864","attributed calls":"12656 of 14653","values withheld":"0","commitment":"sha256 73670bb3a876f829e55f6d40a21cf667f3be0ce4d36fa2041330862061f3323b · lines 3388"},"tables":[]},
"Timeline":{"facts":{"events":"225 · shown 60 · elided 165","elided":"165 events from 2026-11-19T12:28:23Z to 2026-11-20T16:15:13Z","withheld rows":"verb 1345 · push 300 · push-refused 0 · gate 99 · compact 5 · limit 8 · idle 1 · workflow 90"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-11-19T03:12:10Z","run-state","phase","9e21ac760dc0","RUNNING","-","-"],
["2026-11-19T03:48:35Z","run-state","phase","15d20d36330b","REVIEWING","-","-"],
["2026-11-19T06:50:21Z","run-state","dispatch","TOOL-dPlacedRequest-11","-","-","-"],
["2026-11-19T06:51:41Z","run-state","phase","88f3b4132f3c","BUILDING","-","-"],
["2026-11-19T06:52:34Z","run-state","brief","TOOL-dPlacedRequest-11","-","-","-"],
["2026-11-19T07:10:11Z","run-state","dispatch","TOOL-dPlacedRequest-11","-","-","-"],
["2026-11-19T07:11:48Z","run-state","dispatch","TOOL-dPlacedRequest-11","-","-","-"],
["2026-11-19T07:32:56Z","run-state","dispatch","TOOL-dPlacedRequest-13","-","-","-"],
["2026-11-19T07:39:45Z","run-state","brief","TOOL-dPlacedRequest-13","-","-","-"],
["2026-11-19T08:04:18Z","run-state","dispatch","TOOL-dPlacedRequest-1","-","-","-"],
["2026-11-19T08:07:38Z","run-state","brief","TOOL-dPlacedRequest-1","-","-","-"],
["2026-11-19T08:55:29Z","run-state","dispatch","TOOL-dPlacedRequest-27","-","-","-"],
["2026-11-19T08:57:08Z","run-state","brief","TOOL-dPlacedRequest-27","-","-","-"],
["2026-11-19T09:06:17Z","run-state","dispatch","TOOL-dPlacedRequest-17","-","-","-"],
["2026-11-19T09:17:21Z","run-state","brief","TOOL-dPlacedRequest-17","-","-","-"],
["2026-11-19T09:41:29Z","run-state","dispatch","TOOL-dPlacedRequest-23","-","-","-"],
["2026-11-19T09:43:47Z","run-state","brief","TOOL-dPlacedRequest-23","-","-","-"],
["2026-11-19T09:53:15Z","run-state","dispatch","TOOL-dPlacedRequest-24","-","-","-"],
["2026-11-19T10:21:17Z","run-state","brief","TOOL-dPlacedRequest-24","-","-","-"],
["2026-11-19T10:31:09Z","run-state","dispatch","TOOL-dPlacedRequest-25","-","-","-"],
["2026-11-19T10:33:59Z","run-state","brief","TOOL-dPlacedRequest-25","-","-","-"],
["2026-11-19T10:45:59Z","run-state","dispatch","TOOL-dPlacedRequest-16","-","-","-"],
["2026-11-19T11:15:25Z","run-state","brief","TOOL-dPlacedRequest-16","-","-","-"],
["2026-11-19T11:16:19Z","run-state","dispatch","TOOL-dPlacedRequest-16","-","-","-"],
["2026-11-19T11:49:25Z","run-state","dispatch","TOOL-dPlacedRequest-16","-","-","-"],
["2026-11-19T11:56:24Z","run-state","dispatch","TOOL-dPlacedRequest-16","-","-","-"],
["2026-11-19T12:03:00Z","run-state","dispatch","TOOL-dPlacedRequest-26","-","-","-"],
["2026-11-19T12:04:51Z","run-state","brief","TOOL-dPlacedRequest-26","-","-","-"],
["2026-11-19T12:15:33Z","run-state","dispatch","TOOL-dPlacedRequest-36","-","-","-"],
["2026-11-19T12:17:28Z","run-state","brief","TOOL-dPlacedRequest-36","-","-","-"]]},
{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-11-20T18:37:56Z","run-state","phase","e267d213c519","HELD","-","-"],
["2026-11-20T20:55:37Z","run-state","phase","6277b70848ba","BUILDING","-","-"],
["2026-11-20T21:02:47Z","run-state","dispatch","TOOL-dPlacedRequest-95","-","-","-"],
["2026-11-20T21:03:51Z","run-state","brief","TOOL-dPlacedRequest-95","-","-","-"],
["2026-11-20T21:16:21Z","run-state","dispatch","TOOL-dPlacedRequest-95","-","-","-"],
["2026-11-20T21:27:34Z","run-state","dispatch","TOOL-dPlacedRequest-96","-","-","-"],
["2026-11-20T21:29:10Z","run-state","brief","TOOL-dPlacedRequest-96","-","-","-"],
["2026-11-20T21:38:41Z","run-state","dispatch","TOOL-dPlacedRequest-96","-","-","-"],
["2026-11-20T21:46:37Z","run-state","dispatch","TOOL-dPlacedRequest-97","-","-","-"],
["2026-11-20T21:48:11Z","run-state","brief","TOOL-dPlacedRequest-97","-","-","-"],
["2026-11-20T21:58:49Z","run-state","dispatch","TOOL-dPlacedRequest-97","-","-","-"],
["2026-11-20T22:02:39Z","run-state","dispatch","TOOL-dPlacedRequest-98","-","-","-"],
["2026-11-20T22:04:11Z","run-state","brief","TOOL-dPlacedRequest-98","-","-","-"],
["2026-11-20T22:14:42Z","run-state","dispatch","TOOL-dPlacedRequest-98","-","-","-"],
["2026-11-20T22:21:17Z","run-state","dispatch","TOOL-dPlacedRequest-98","-","-","-"],
["2026-11-20T22:27:52Z","run-state","dispatch","TOOL-dPlacedRequest-99","-","-","-"],
["2026-11-20T22:29:24Z","run-state","brief","TOOL-dPlacedRequest-99","-","-","-"],
["2026-11-20T22:56:49Z","run-state","dispatch","TOOL-dPlacedRequest-99","-","-","-"],
["2026-11-20T23:10:25Z","run-state","dispatch","TOOL-dPlacedRequest-99","-","-","-"],
["2026-11-20T23:16:42Z","run-state","dispatch","TOOL-dPlacedRequest-100","-","-","-"],
["2026-11-20T23:18:57Z","run-state","brief","TOOL-dPlacedRequest-100","-","-","-"],
["2026-11-20T23:29:01Z","run-state","dispatch","TOOL-dPlacedRequest-100","-","-","-"],
["2026-11-20T23:32:22Z","run-state","dispatch","TOOL-dPlacedRequest-100","-","-","-"],
["2026-11-20T23:34:36Z","run-state","dispatch","TOOL-dPlacedRequest-100","-","-","-"],
["2026-11-21T00:01:25Z","run-state","phase","2db4a921f14d","VERIFYING","-","-"],
["2026-11-21T02:26:01Z","run-state","phase","870ddd2b20dc","HELD","-","-"],
["2026-11-21T02:37:25Z","run-state","phase","8e8230d305b0","VERIFYING","-","-"],
["2026-11-21T09:12:42Z","run-state","phase","a8bbf1990fb6","HELD","-","-"],
["2026-11-21T11:07:43Z","run-state","phase","6b3ebc830841","VERIFYING","-","-"],
["2026-11-21T11:44:45Z","run-state","phase","6b3ebc830841","LANDING","-","-"]]}]},
"Units":{"facts":{"units":"69 · shown 0 · aggregated yes"},"tables":[{"name":"by-status","header":["#","status","units"],"rows":[
["1","CLOSED","69"]]}]},
"Decisions":{"facts":{"entries":"238 · shown 0 · aggregated yes","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 4 · owner-inside 0 · agent-before 139 · agent-inside 88","excluded rows":"proposal 0 · rescope 7 · dispatch 145 · review 6 · brief 69 · hold 3 · resume 3 · refusal 0 · fix-pass 0","review rounds":"6 · shown 6 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","3"],
["2","abort","0"],
["3","override","1"],
["4","waiver","0"],
["5","handoff","3"],
["6","rescope-retire","0"],
["7","rescope-supersede","0"],
["8","rescope-defer","0"],
["9","review","0"],
["10","trailer","0"],
["11","spec-mark","231"],
["12","decision-log","0"],
["13","ledger","0"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-11-19T04:43:32Z","CLEAN","0","CONVERGED"],
["2","2026-11-19T05:52:49Z","CLEAN","0","CONVERGED"],
["3","2026-11-19T06:46:56Z","CLEAN","0","CONVERGED"],
["4","2026-11-20T16:29:18Z","CLEAN WITH FIXES","0","-"],
["5","2026-11-20T16:45:00Z","CLEAN WITH FIXES","0","NON-CONVERGENT"],
["6","2026-11-20T18:35:01Z","CLEAN","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"5 · shown 5 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","-","UNJUDGEABLE"],
["2","phases-walked","-","MET"],
["3","green-at-close","-","MET"],
["4","keepalive-reaped","-","MET"],
["5","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"60 · shown 0 · aggregated yes"},"tables":[{"name":"by-kind","header":["#","kind","subclass","count"],"rows":[
["1","no-progress","-","1"],
["2","out-of-band-edit","-","5"],
["3","refusal-loop","-","3"],
["4","killed-verb","-","11"],
["5","destructive-git","-","39"],
["6","idle-gap","-","1"]]}]},
"Coverage":{"facts":{"journal starts":"0 joined of 0 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 2","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","2689","0"],
["3","gates","present","99","0"],
["4","pushes","present","300","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
