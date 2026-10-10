# Run record

**Serves:** journal TOOL-aHomedAnchor-1..7

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aHomedAnchor/RUN.md
- run: 1 of 1
- start: 5ac5d61bfc6ac9c31741e2d72975838e176d4e9c
- phase: VERIFYING
- terminal: no
- window: 2026-10-09T01:45:00Z to 2026-10-09T05:41:21Z
- window opened by: git
- window closed by: last-activity
- duration: 14181s
- own commits: 12
- last own commit: 51518b1637d20a20dffd5bea19ede9264abca5fd
- merged: no
- units served: 7
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 0 · in-window 0 · post-close 0
- usage main: requests 239 · in 484 · out 176021 · cache-read 94512595 · cache-write 350985
- usage agent: requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0
- usage workflow: requests 255 · in 510 · out 232245 · cache-read 26904120 · cache-write 1326109
- attributed calls: 479 of 519
- values withheld: 0
- commitment: sha256 445cdc0522920abdcb0b12f7fdc79a815a09db4bbba1d4bed25677d8249370fb · lines 88

## Timeline

- events: 31 · shown 31 · elided 0
- withheld rows: verb 38 · push 7 · push-refused 0 · gate 0 · compact 0 · limit 0 · idle 0 · workflow 1

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-10-09T01:45:00Z | run-state | phase | 11224126c2e4 | RUNNING | - | - |
| 2026-10-09T01:58:32Z | git | commit | dc8591f4ae91 | - | - | TOOL-aHomedAnchor-1 |
| 2026-10-09T01:58:32Z | run-state | phase | 5ac5d61bfc6a | SPECCING | - | - |
| 2026-10-09T02:07:46Z | run-state | dispatch | TOOL-aHomedAnchor-1 | - | - | - |
| 2026-10-09T02:32:05Z | run-state | dispatch | TOOL-aHomedAnchor-1 | - | - | - |
| 2026-10-09T02:32:26Z | git | commit | 59c9719a835e | - | - | TOOL-aHomedAnchor-1 |
| 2026-10-09T02:32:26Z | run-state | phase | dc8591f4ae91 | BUILDING | - | - |
| 2026-10-09T02:46:49Z | git | commit | 337b5b644f7e | - | - | TOOL-aHomedAnchor-1 |
| 2026-10-09T02:53:06Z | run-state | dispatch | TOOL-aHomedAnchor-1 | - | - | - |
| 2026-10-09T02:53:24Z | git | commit | 026f5eecf08a | - | - | TOOL-aHomedAnchor-1 |
| 2026-10-09T02:58:36Z | run-state | dispatch | TOOL-aHomedAnchor-2 | - | - | - |
| 2026-10-09T03:31:05Z | run-state | dispatch | TOOL-aHomedAnchor-2 | - | - | - |
| 2026-10-09T03:39:12Z | run-state | dispatch | TOOL-aHomedAnchor-2 | - | - | - |
| 2026-10-09T03:39:46Z | git | commit | 40a976d9eceb | - | - | TOOL-aHomedAnchor-2 |
| 2026-10-09T04:23:45Z | git | commit | 71a299b2a5e3 | - | - | TOOL-aHomedAnchor-3 |
| 2026-10-09T04:23:45Z | run-state | phase | 40a976d9eceb | SPECCING | - | - |
| 2026-10-09T04:28:05Z | run-state | dispatch | TOOL-aHomedAnchor-3 | - | - | - |
| 2026-10-09T04:28:57Z | git | commit | 4c80fedddcba | - | - | TOOL-aHomedAnchor-3 |
| 2026-10-09T04:28:57Z | run-state | phase | 71a299b2a5e3 | BUILDING | - | - |
| 2026-10-09T04:32:43Z | run-state | dispatch | TOOL-aHomedAnchor-5 | - | - | - |
| 2026-10-09T04:33:05Z | git | commit | 87f19159c426 | - | - | TOOL-aHomedAnchor-5 |
| 2026-10-09T04:35:22Z | run-state | dispatch | TOOL-aHomedAnchor-4 | - | - | - |
| 2026-10-09T04:36:06Z | git | commit | d3b545f675fb | - | - | TOOL-aHomedAnchor-4 |
| 2026-10-09T04:39:08Z | run-state | dispatch | TOOL-aHomedAnchor-6 | - | - | - |
| 2026-10-09T04:45:27Z | run-state | dispatch | TOOL-aHomedAnchor-6 | - | - | - |
| 2026-10-09T04:45:29Z | git | commit | 2d5f232c0b44 | - | - | TOOL-aHomedAnchor-6 |
| 2026-10-09T04:48:05Z | run-state | dispatch | TOOL-aHomedAnchor-7 | - | - | - |
| 2026-10-09T04:50:37Z | git | commit | dd043ee71461 | - | - | TOOL-aHomedAnchor-7 |
| 2026-10-09T04:59:26Z | run-state | phase | dd043ee71461 | VERIFYING | - | - |
| 2026-10-09T05:32:15Z | run-state | dispatch | TOOL-aHomedAnchor-7 | - | - | - |
| 2026-10-09T05:32:17Z | git | commit | 51518b1637d2 | - | - | TOOL-aHomedAnchor-7 |

## Units

- units: 7 · shown 7 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | TOOL-aHomedAnchor-1 | CLOSED | 4 | 3 | 0 | 59c9719a835e |
| 2 | TOOL-aHomedAnchor-2 | CLOSED | 1 | 3 | 0 | 40a976d9eceb |
| 3 | TOOL-aHomedAnchor-3 | CLOSED | 2 | 1 | 0 | 4c80fedddcba |
| 3 | TOOL-aHomedAnchor-5 | CLOSED | 1 | 1 | 0 | 87f19159c426 |
| 4 | TOOL-aHomedAnchor-4 | CLOSED | 1 | 1 | 0 | d3b545f675fb |
| 5 | TOOL-aHomedAnchor-6 | CLOSED | 1 | 2 | 0 | 2d5f232c0b44 |
| 5 | TOOL-aHomedAnchor-7 | CLOSED | 2 | 2 | 0 | dd043ee71461 |

## Decisions

- entries: 11 · shown 11 · aggregated no
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 1
- excluded rows: proposal 0 · rescope 5 · dispatch 13 · review 1 · brief 0 · hold 0 · resume 0
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
| 9 | review | 1 |
| 10 | trailer | 8 |
| 11 | spec-mark | 1 |
| 12 | decision-log | 1 |
| 13 | ledger | 0 |

| # | source | ref | verdict |
|---|---|---|---|
| 1 | review | memory/builds/aHomedAnchor/reviews/2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md:9 | CLEAN WITH FIXES |
| 2 | trailer | dc8591f4ae91 | - |
| 3 | trailer | dc8591f4ae91 | - |
| 4 | trailer | 59c9719a835e | - |
| 5 | trailer | 40a976d9eceb | - |
| 6 | trailer | 71a299b2a5e3 | - |
| 7 | trailer | 71a299b2a5e3 | - |
| 8 | trailer | 2d5f232c0b44 | - |
| 9 | trailer | 2d5f232c0b44 | - |
| 10 | spec-mark | memory/builds/aHomedAnchor/spec/2026-10-09-spec-TOOL-aHomedAnchor-1.md | - |
| 11 | decision-log | 337b5b644f7e | - |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-10-09T04:12:49Z | CLEAN WITH FIXES | 0 | CONVERGED |

## Conformance

- items: 11 · shown 11 · aggregated no

| # | item | unit | state |
|---|---|---|---|
| 1 | brief-before-build | TOOL-aHomedAnchor-1 | UNMET |
| 2 | brief-before-build | TOOL-aHomedAnchor-2 | UNMET |
| 3 | brief-before-build | TOOL-aHomedAnchor-3 | UNMET |
| 4 | brief-before-build | TOOL-aHomedAnchor-4 | UNMET |
| 5 | brief-before-build | TOOL-aHomedAnchor-5 | UNMET |
| 6 | brief-before-build | TOOL-aHomedAnchor-6 | UNMET |
| 7 | brief-before-build | TOOL-aHomedAnchor-7 | UNMET |
| 8 | phases-walked | - | UNJUDGEABLE |
| 9 | green-at-close | - | UNJUDGEABLE |
| 10 | keepalive-reaped | - | MET |
| 11 | review-exited | - | MET |

## Anomalies

- anomalies: 2 · shown 2 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | killed-verb | - |
| 2 | killed-verb | - |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 0
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 74 | 0 |
| 3 | gates | present | 0 | 0 |
| 4 | pushes | present | 7 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aHomedAnchor/RUN.md","run":"1 of 1","start":"5ac5d61bfc6ac9c31741e2d72975838e176d4e9c","phase":"VERIFYING","terminal":"no","window":"2026-10-09T01:45:00Z to 2026-10-09T05:41:21Z","window opened by":"git","window closed by":"last-activity","duration":"14181s","own commits":"12","last own commit":"51518b1637d20a20dffd5bea19ede9264abca5fd","merged":"no","units served":"7","sources present":"7 of 7","owner turns":"launch 1 · pre-run 0 · in-window 0 · post-close 0","usage main":"requests 239 · in 484 · out 176021 · cache-read 94512595 · cache-write 350985","usage agent":"requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0","usage workflow":"requests 255 · in 510 · out 232245 · cache-read 26904120 · cache-write 1326109","attributed calls":"479 of 519","values withheld":"0","commitment":"sha256 445cdc0522920abdcb0b12f7fdc79a815a09db4bbba1d4bed25677d8249370fb · lines 88"},"tables":[]},
"Timeline":{"facts":{"events":"31 · shown 31 · elided 0","withheld rows":"verb 38 · push 7 · push-refused 0 · gate 0 · compact 0 · limit 0 · idle 0 · workflow 1"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-10-09T01:45:00Z","run-state","phase","11224126c2e4","RUNNING","-","-"],
["2026-10-09T01:58:32Z","git","commit","dc8591f4ae91","-","-","TOOL-aHomedAnchor-1"],
["2026-10-09T01:58:32Z","run-state","phase","5ac5d61bfc6a","SPECCING","-","-"],
["2026-10-09T02:07:46Z","run-state","dispatch","TOOL-aHomedAnchor-1","-","-","-"],
["2026-10-09T02:32:05Z","run-state","dispatch","TOOL-aHomedAnchor-1","-","-","-"],
["2026-10-09T02:32:26Z","git","commit","59c9719a835e","-","-","TOOL-aHomedAnchor-1"],
["2026-10-09T02:32:26Z","run-state","phase","dc8591f4ae91","BUILDING","-","-"],
["2026-10-09T02:46:49Z","git","commit","337b5b644f7e","-","-","TOOL-aHomedAnchor-1"],
["2026-10-09T02:53:06Z","run-state","dispatch","TOOL-aHomedAnchor-1","-","-","-"],
["2026-10-09T02:53:24Z","git","commit","026f5eecf08a","-","-","TOOL-aHomedAnchor-1"],
["2026-10-09T02:58:36Z","run-state","dispatch","TOOL-aHomedAnchor-2","-","-","-"],
["2026-10-09T03:31:05Z","run-state","dispatch","TOOL-aHomedAnchor-2","-","-","-"],
["2026-10-09T03:39:12Z","run-state","dispatch","TOOL-aHomedAnchor-2","-","-","-"],
["2026-10-09T03:39:46Z","git","commit","40a976d9eceb","-","-","TOOL-aHomedAnchor-2"],
["2026-10-09T04:23:45Z","git","commit","71a299b2a5e3","-","-","TOOL-aHomedAnchor-3"],
["2026-10-09T04:23:45Z","run-state","phase","40a976d9eceb","SPECCING","-","-"],
["2026-10-09T04:28:05Z","run-state","dispatch","TOOL-aHomedAnchor-3","-","-","-"],
["2026-10-09T04:28:57Z","git","commit","4c80fedddcba","-","-","TOOL-aHomedAnchor-3"],
["2026-10-09T04:28:57Z","run-state","phase","71a299b2a5e3","BUILDING","-","-"],
["2026-10-09T04:32:43Z","run-state","dispatch","TOOL-aHomedAnchor-5","-","-","-"],
["2026-10-09T04:33:05Z","git","commit","87f19159c426","-","-","TOOL-aHomedAnchor-5"],
["2026-10-09T04:35:22Z","run-state","dispatch","TOOL-aHomedAnchor-4","-","-","-"],
["2026-10-09T04:36:06Z","git","commit","d3b545f675fb","-","-","TOOL-aHomedAnchor-4"],
["2026-10-09T04:39:08Z","run-state","dispatch","TOOL-aHomedAnchor-6","-","-","-"],
["2026-10-09T04:45:27Z","run-state","dispatch","TOOL-aHomedAnchor-6","-","-","-"],
["2026-10-09T04:45:29Z","git","commit","2d5f232c0b44","-","-","TOOL-aHomedAnchor-6"],
["2026-10-09T04:48:05Z","run-state","dispatch","TOOL-aHomedAnchor-7","-","-","-"],
["2026-10-09T04:50:37Z","git","commit","dd043ee71461","-","-","TOOL-aHomedAnchor-7"],
["2026-10-09T04:59:26Z","run-state","phase","dd043ee71461","VERIFYING","-","-"],
["2026-10-09T05:32:15Z","run-state","dispatch","TOOL-aHomedAnchor-7","-","-","-"],
["2026-10-09T05:32:17Z","git","commit","51518b1637d2","-","-","TOOL-aHomedAnchor-7"]]}]},
"Units":{"facts":{"units":"7 · shown 7 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","TOOL-aHomedAnchor-1","CLOSED","4","3","0","59c9719a835e"],
["2","TOOL-aHomedAnchor-2","CLOSED","1","3","0","40a976d9eceb"],
["3","TOOL-aHomedAnchor-3","CLOSED","2","1","0","4c80fedddcba"],
["3","TOOL-aHomedAnchor-5","CLOSED","1","1","0","87f19159c426"],
["4","TOOL-aHomedAnchor-4","CLOSED","1","1","0","d3b545f675fb"],
["5","TOOL-aHomedAnchor-6","CLOSED","1","2","0","2d5f232c0b44"],
["5","TOOL-aHomedAnchor-7","CLOSED","2","2","0","dd043ee71461"]]}]},
"Decisions":{"facts":{"entries":"11 · shown 11 · aggregated no","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 1","excluded rows":"proposal 0 · rescope 5 · dispatch 13 · review 1 · brief 0 · hold 0 · resume 0","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","0"],
["2","abort","0"],
["3","override","0"],
["4","waiver","0"],
["5","handoff","0"],
["6","rescope-retire","0"],
["7","rescope-supersede","0"],
["8","rescope-defer","0"],
["9","review","1"],
["10","trailer","8"],
["11","spec-mark","1"],
["12","decision-log","1"],
["13","ledger","0"]]},
{"name":"entries","header":["#","source","ref","verdict"],"rows":[
["1","review","memory/builds/aHomedAnchor/reviews/2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md:9","CLEAN WITH FIXES"],
["2","trailer","dc8591f4ae91","-"],
["3","trailer","dc8591f4ae91","-"],
["4","trailer","59c9719a835e","-"],
["5","trailer","40a976d9eceb","-"],
["6","trailer","71a299b2a5e3","-"],
["7","trailer","71a299b2a5e3","-"],
["8","trailer","2d5f232c0b44","-"],
["9","trailer","2d5f232c0b44","-"],
["10","spec-mark","memory/builds/aHomedAnchor/spec/2026-10-09-spec-TOOL-aHomedAnchor-1.md","-"],
["11","decision-log","337b5b644f7e","-"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-10-09T04:12:49Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"11 · shown 11 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","TOOL-aHomedAnchor-1","UNMET"],
["2","brief-before-build","TOOL-aHomedAnchor-2","UNMET"],
["3","brief-before-build","TOOL-aHomedAnchor-3","UNMET"],
["4","brief-before-build","TOOL-aHomedAnchor-4","UNMET"],
["5","brief-before-build","TOOL-aHomedAnchor-5","UNMET"],
["6","brief-before-build","TOOL-aHomedAnchor-6","UNMET"],
["7","brief-before-build","TOOL-aHomedAnchor-7","UNMET"],
["8","phases-walked","-","UNJUDGEABLE"],
["9","green-at-close","-","UNJUDGEABLE"],
["10","keepalive-reaped","-","MET"],
["11","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"2 · shown 2 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","killed-verb","-"],
["2","killed-verb","-"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 0","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","74","0"],
["3","gates","present","0","0"],
["4","pushes","present","7","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
