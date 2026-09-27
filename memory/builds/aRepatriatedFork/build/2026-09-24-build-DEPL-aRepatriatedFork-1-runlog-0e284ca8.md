# Run record

**Serves:** journal DEPL-aRepatriatedFork-1 DEPL-aRepatriatedFork-13..14 DEPL-aRepatriatedFork-17 DEPL-aRepatriatedFork-20..21 TOOL-aRepatriatedFork-2..12 TOOL-aRepatriatedFork-15..16 TOOL-aRepatriatedFork-18..19 TOOL-aRepatriatedFork-21

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aRepatriatedFork/RUN.md
- run: 1 of 1
- start: 0e284ca80ec395abc47b79e527a9808b05e85e31
- phase: LANDED
- terminal: yes
- window: 2026-09-23T18:02:01Z to 2026-09-24T18:34:27Z
- window opened by: git
- window closed by: terminal-pending
- duration: 88346s
- own commits: 83
- last own commit: c9ae923fdb50b8ca750b47ee068381ec8b0da509
- merged: yes
- units served: 22
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 2 · in-window 2 · post-close 0
- usage main: requests 371 · in 842 · out 304567 · cache-read 233720989 · cache-write 3272978
- usage agent: requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0
- usage workflow: requests 4173 · in 8346 · out 3118530 · cache-read 932461660 · cache-write 13200714
- attributed calls: 5003 of 5027
- values withheld: 1
- commitment: sha256 98427c772bf45d35823edab7177efb78bf0c389ce26862f0498019336298d44d · lines 425

## Timeline

- events: 202 · shown 60 · elided 142
- elided: 142 events from 2026-09-23T20:17:23Z to 2026-09-24T07:49:42Z
- withheld rows: verb 210 · push 1 · push-refused 0 · gate 4 · compact 0 · limit 0 · idle 0 · workflow 38

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-09-23T18:02:01Z | run-state | phase | 004f1bc0c9db | RUNNING | - | - |
| 2026-09-23T18:05:43Z | run-state | phase | 31cdaa009da5 | BUILDING | - | - |
| 2026-09-23T18:08:18Z | run-state | dispatch | DEPL-aRepatriatedFork-1 | - | - | - |
| 2026-09-23T18:08:23Z | run-state | brief | DEPL-aRepatriatedFork-1 | - | - | - |
| 2026-09-23T18:24:11Z | run-state | dispatch | DEPL-aRepatriatedFork-1 | - | - | - |
| 2026-09-23T18:25:57Z | run-state | dispatch | DEPL-aRepatriatedFork-1 | - | - | - |
| 2026-09-23T18:29:30Z | git | commit | b858ce1a0de3 | - | - | DEPL-aRepatriatedFork-1 |
| 2026-09-23T18:29:30Z | run-state | dispatch | DEPL-aRepatriatedFork-1 | - | - | - |
| 2026-09-23T18:32:14Z | run-state | dispatch | TOOL-aRepatriatedFork-10 | - | - | - |
| 2026-09-23T18:32:19Z | run-state | brief | TOOL-aRepatriatedFork-10 | - | - | - |
| 2026-09-23T18:57:54Z | run-state | dispatch | TOOL-aRepatriatedFork-10 | - | - | - |
| 2026-09-23T19:01:16Z | git | commit | d91357b9b391 | - | - | TOOL-aRepatriatedFork-10 |
| 2026-09-23T19:02:48Z | git | commit | 653646443c89 | - | - | TOOL-aRepatriatedFork-10 |
| 2026-09-23T19:05:21Z | run-state | dispatch | TOOL-aRepatriatedFork-16 | - | - | - |
| 2026-09-23T19:05:27Z | run-state | brief | TOOL-aRepatriatedFork-16 | - | - | - |
| 2026-09-23T19:19:22Z | run-state | dispatch | TOOL-aRepatriatedFork-16 | - | - | - |
| 2026-09-23T19:20:40Z | run-state | dispatch | TOOL-aRepatriatedFork-16 | - | - | - |
| 2026-09-23T19:21:53Z | git | commit | 5d9be3fc2b3c | - | - | TOOL-aRepatriatedFork-16 |
| 2026-09-23T19:23:25Z | git | commit | 85fcb90f7c64 | - | - | TOOL-aRepatriatedFork-16 |
| 2026-09-23T19:28:22Z | run-state | brief | TOOL-aRepatriatedFork-3 | - | - | - |
| 2026-09-23T19:29:47Z | run-state | dispatch | TOOL-aRepatriatedFork-3 | - | - | - |
| 2026-09-23T19:39:03Z | git | commit | d50ac91d9af9 | - | - | TOOL-aRepatriatedFork-3 |
| 2026-09-23T19:42:29Z | git | commit | 424c67d8a2dd | - | - | TOOL-aRepatriatedFork-16 |
| 2026-09-23T19:43:04Z | git | commit | 468f39970432 | - | - | TOOL-aRepatriatedFork-3 |
| 2026-09-23T19:45:05Z | run-state | dispatch | TOOL-aRepatriatedFork-4 | - | - | - |
| 2026-09-23T19:45:07Z | run-state | brief | TOOL-aRepatriatedFork-4 | - | - | - |
| 2026-09-23T19:52:19Z | run-state | dispatch | TOOL-aRepatriatedFork-4 | - | - | - |
| 2026-09-23T19:53:29Z | git | commit | a1ea53455442 | - | - | TOOL-aRepatriatedFork-4 |
| 2026-09-23T19:59:14Z | run-state | dispatch | TOOL-aRepatriatedFork-5 | - | - | - |
| 2026-09-23T19:59:20Z | run-state | brief | TOOL-aRepatriatedFork-5 | - | - | - |

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-09-24T08:15:15Z | run-state | dispatch | DEPL-aRepatriatedFork-13 | - | - | - |
| 2026-09-24T08:18:32Z | git | commit | e665485d07fb | - | - | TOOL-aRepatriatedFork-18 |
| 2026-09-24T08:18:53Z | git | commit | 1f6e2be554bd | - | - | TOOL-aRepatriatedFork-11 |
| 2026-09-24T08:19:14Z | git | commit | 66f09cad4154 | - | - | DEPL-aRepatriatedFork-17 |
| 2026-09-24T08:19:37Z | git | commit | 98eec7cf73a1 | - | - | DEPL-aRepatriatedFork-14 |
| 2026-09-24T08:19:59Z | git | commit | 4b7f5be39daa | - | - | TOOL-aRepatriatedFork-7 |
| 2026-09-24T08:20:20Z | git | commit | 87c35469a309 | - | - | DEPL-aRepatriatedFork-13 |
| 2026-09-24T08:50:08Z | run-state | dispatch | TOOL-aRepatriatedFork-2 | - | - | - |
| 2026-09-24T08:50:14Z | run-state | brief | TOOL-aRepatriatedFork-2 | - | - | - |
| 2026-09-24T09:02:21Z | run-state | dispatch | TOOL-aRepatriatedFork-2 | - | - | - |
| 2026-09-24T09:02:28Z | git | commit | 3717ee866f1b | - | - | TOOL-aRepatriatedFork-2 |
| 2026-09-24T09:04:23Z | run-state | dispatch | TOOL-aRepatriatedFork-5 | - | - | - |
| 2026-09-24T09:06:12Z | git | commit | d5e280e17dd0 | - | - | TOOL-aRepatriatedFork-5 |
| 2026-09-24T09:07:31Z | git | commit | a5b0124aa1ba | - | - | TOOL-aRepatriatedFork-2 |
| 2026-09-24T09:24:12Z | run-state | dispatch | TOOL-aRepatriatedFork-8 | - | - | - |
| 2026-09-24T09:24:18Z | run-state | brief | TOOL-aRepatriatedFork-8 | - | - | - |
| 2026-09-24T09:27:39Z | git | commit | 201af720f7d4 | - | - | TOOL-aRepatriatedFork-8 |
| 2026-09-24T09:30:32Z | git | commit | 6cd239fc3c6c | - | - | TOOL-aRepatriatedFork-6 |
| 2026-09-24T09:35:26Z | run-state | dispatch | TOOL-aRepatriatedFork-8 | - | - | - |
| 2026-09-24T09:35:33Z | git | commit | 2ffc74ecf9b8 | - | - | TOOL-aRepatriatedFork-10 |
| 2026-09-24T09:38:26Z | run-state | dispatch | TOOL-aRepatriatedFork-8 | - | - | - |
| 2026-09-24T09:38:44Z | git | commit | 6526e331d5d2 | - | - | TOOL-aRepatriatedFork-10 |
| 2026-09-24T09:39:31Z | git | commit | d1d71c380457 | - | - | TOOL-aRepatriatedFork-6 |
| 2026-09-24T09:43:32Z | git | commit | 386f168b4b3e | - | - | DEPL-aRepatriatedFork-14 |
| 2026-09-24T16:13:03Z | run-state | dispatch | TOOL-aRepatriatedFork-8 | - | - | - |
| 2026-09-24T16:13:18Z | git | commit | 526d43cc9677 | - | - | TOOL-aRepatriatedFork-8 |
| 2026-09-24T16:19:38Z | run-state | dispatch | TOOL-aRepatriatedFork-8 | - | - | - |
| 2026-09-24T16:20:49Z | git | commit | c9ae923fdb50 | - | - | TOOL-aRepatriatedFork-8 |
| 2026-09-24T18:34:27Z | run-state | phase | d393c445005d | LANDING | - | - |
| 2026-09-24T18:35:06Z | git | merge | 2bd14f4bf03a | - | - | - |

## Units

- units: 22 · shown 0 · aggregated yes

| # | status | units |
|---|---|---|
| 1 | BLOCKED | 1 |
| 2 | CLOSED | 21 |

## Decisions

- entries: 191 · shown 0 · aggregated yes
- trailer near-misses: 7
- decision-log rows the owner's: 0
- spec marks: owner-before 53 · owner-inside 0 · agent-before 0 · agent-inside 7
- excluded rows: proposal 0 · rescope 2 · dispatch 80 · review 2 · brief 34
- review rounds: 2 · shown 2 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 3 |
| 2 | abort | 0 |
| 3 | override | 1 |
| 4 | waiver | 0 |
| 5 | rescope-retire | 0 |
| 6 | rescope-supersede | 0 |
| 7 | review | 2 |
| 8 | trailer | 123 |
| 9 | spec-mark | 60 |
| 10 | decision-log | 0 |
| 11 | ledger | 2 |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-09-24T03:27:33Z | BLOCKED | 1 | - |
| 2 | 2026-09-24T05:41:59Z | CLEAN WITH FIXES | 0 | CONVERGED |

## Conformance

- items: 25 · shown 0 · aggregated yes

| # | item | state | count |
|---|---|---|---|
| 1 | brief-before-build | MET | 21 |
| 2 | phases-walked | MET | 1 |
| 3 | green-at-close | MET | 1 |
| 4 | keepalive-reaped | MET | 1 |
| 5 | review-exited | MET | 1 |

## Anomalies

- anomalies: 26 · shown 0 · aggregated yes

| # | kind | subclass | count |
|---|---|---|---|
| 1 | refusal-loop | - | 2 |
| 2 | killed-verb | - | 1 |
| 3 | red-behind-zero | - | 2 |
| 4 | destructive-git | - | 21 |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 0
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 419 | 0 |
| 3 | gates | present | 4 | 0 |
| 4 | pushes | present | 1 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aRepatriatedFork/RUN.md","run":"1 of 1","start":"0e284ca80ec395abc47b79e527a9808b05e85e31","phase":"LANDED","terminal":"yes","window":"2026-09-23T18:02:01Z to 2026-09-24T18:34:27Z","window opened by":"git","window closed by":"terminal-pending","duration":"88346s","own commits":"83","last own commit":"c9ae923fdb50b8ca750b47ee068381ec8b0da509","merged":"yes","units served":"22","sources present":"7 of 7","owner turns":"launch 1 · pre-run 2 · in-window 2 · post-close 0","usage main":"requests 371 · in 842 · out 304567 · cache-read 233720989 · cache-write 3272978","usage agent":"requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0","usage workflow":"requests 4173 · in 8346 · out 3118530 · cache-read 932461660 · cache-write 13200714","attributed calls":"5003 of 5027","values withheld":"1","commitment":"sha256 98427c772bf45d35823edab7177efb78bf0c389ce26862f0498019336298d44d · lines 425"},"tables":[]},
"Timeline":{"facts":{"events":"202 · shown 60 · elided 142","elided":"142 events from 2026-09-23T20:17:23Z to 2026-09-24T07:49:42Z","withheld rows":"verb 210 · push 1 · push-refused 0 · gate 4 · compact 0 · limit 0 · idle 0 · workflow 38"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-09-23T18:02:01Z","run-state","phase","004f1bc0c9db","RUNNING","-","-"],
["2026-09-23T18:05:43Z","run-state","phase","31cdaa009da5","BUILDING","-","-"],
["2026-09-23T18:08:18Z","run-state","dispatch","DEPL-aRepatriatedFork-1","-","-","-"],
["2026-09-23T18:08:23Z","run-state","brief","DEPL-aRepatriatedFork-1","-","-","-"],
["2026-09-23T18:24:11Z","run-state","dispatch","DEPL-aRepatriatedFork-1","-","-","-"],
["2026-09-23T18:25:57Z","run-state","dispatch","DEPL-aRepatriatedFork-1","-","-","-"],
["2026-09-23T18:29:30Z","git","commit","b858ce1a0de3","-","-","DEPL-aRepatriatedFork-1"],
["2026-09-23T18:29:30Z","run-state","dispatch","DEPL-aRepatriatedFork-1","-","-","-"],
["2026-09-23T18:32:14Z","run-state","dispatch","TOOL-aRepatriatedFork-10","-","-","-"],
["2026-09-23T18:32:19Z","run-state","brief","TOOL-aRepatriatedFork-10","-","-","-"],
["2026-09-23T18:57:54Z","run-state","dispatch","TOOL-aRepatriatedFork-10","-","-","-"],
["2026-09-23T19:01:16Z","git","commit","d91357b9b391","-","-","TOOL-aRepatriatedFork-10"],
["2026-09-23T19:02:48Z","git","commit","653646443c89","-","-","TOOL-aRepatriatedFork-10"],
["2026-09-23T19:05:21Z","run-state","dispatch","TOOL-aRepatriatedFork-16","-","-","-"],
["2026-09-23T19:05:27Z","run-state","brief","TOOL-aRepatriatedFork-16","-","-","-"],
["2026-09-23T19:19:22Z","run-state","dispatch","TOOL-aRepatriatedFork-16","-","-","-"],
["2026-09-23T19:20:40Z","run-state","dispatch","TOOL-aRepatriatedFork-16","-","-","-"],
["2026-09-23T19:21:53Z","git","commit","5d9be3fc2b3c","-","-","TOOL-aRepatriatedFork-16"],
["2026-09-23T19:23:25Z","git","commit","85fcb90f7c64","-","-","TOOL-aRepatriatedFork-16"],
["2026-09-23T19:28:22Z","run-state","brief","TOOL-aRepatriatedFork-3","-","-","-"],
["2026-09-23T19:29:47Z","run-state","dispatch","TOOL-aRepatriatedFork-3","-","-","-"],
["2026-09-23T19:39:03Z","git","commit","d50ac91d9af9","-","-","TOOL-aRepatriatedFork-3"],
["2026-09-23T19:42:29Z","git","commit","424c67d8a2dd","-","-","TOOL-aRepatriatedFork-16"],
["2026-09-23T19:43:04Z","git","commit","468f39970432","-","-","TOOL-aRepatriatedFork-3"],
["2026-09-23T19:45:05Z","run-state","dispatch","TOOL-aRepatriatedFork-4","-","-","-"],
["2026-09-23T19:45:07Z","run-state","brief","TOOL-aRepatriatedFork-4","-","-","-"],
["2026-09-23T19:52:19Z","run-state","dispatch","TOOL-aRepatriatedFork-4","-","-","-"],
["2026-09-23T19:53:29Z","git","commit","a1ea53455442","-","-","TOOL-aRepatriatedFork-4"],
["2026-09-23T19:59:14Z","run-state","dispatch","TOOL-aRepatriatedFork-5","-","-","-"],
["2026-09-23T19:59:20Z","run-state","brief","TOOL-aRepatriatedFork-5","-","-","-"]]},
{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-09-24T08:15:15Z","run-state","dispatch","DEPL-aRepatriatedFork-13","-","-","-"],
["2026-09-24T08:18:32Z","git","commit","e665485d07fb","-","-","TOOL-aRepatriatedFork-18"],
["2026-09-24T08:18:53Z","git","commit","1f6e2be554bd","-","-","TOOL-aRepatriatedFork-11"],
["2026-09-24T08:19:14Z","git","commit","66f09cad4154","-","-","DEPL-aRepatriatedFork-17"],
["2026-09-24T08:19:37Z","git","commit","98eec7cf73a1","-","-","DEPL-aRepatriatedFork-14"],
["2026-09-24T08:19:59Z","git","commit","4b7f5be39daa","-","-","TOOL-aRepatriatedFork-7"],
["2026-09-24T08:20:20Z","git","commit","87c35469a309","-","-","DEPL-aRepatriatedFork-13"],
["2026-09-24T08:50:08Z","run-state","dispatch","TOOL-aRepatriatedFork-2","-","-","-"],
["2026-09-24T08:50:14Z","run-state","brief","TOOL-aRepatriatedFork-2","-","-","-"],
["2026-09-24T09:02:21Z","run-state","dispatch","TOOL-aRepatriatedFork-2","-","-","-"],
["2026-09-24T09:02:28Z","git","commit","3717ee866f1b","-","-","TOOL-aRepatriatedFork-2"],
["2026-09-24T09:04:23Z","run-state","dispatch","TOOL-aRepatriatedFork-5","-","-","-"],
["2026-09-24T09:06:12Z","git","commit","d5e280e17dd0","-","-","TOOL-aRepatriatedFork-5"],
["2026-09-24T09:07:31Z","git","commit","a5b0124aa1ba","-","-","TOOL-aRepatriatedFork-2"],
["2026-09-24T09:24:12Z","run-state","dispatch","TOOL-aRepatriatedFork-8","-","-","-"],
["2026-09-24T09:24:18Z","run-state","brief","TOOL-aRepatriatedFork-8","-","-","-"],
["2026-09-24T09:27:39Z","git","commit","201af720f7d4","-","-","TOOL-aRepatriatedFork-8"],
["2026-09-24T09:30:32Z","git","commit","6cd239fc3c6c","-","-","TOOL-aRepatriatedFork-6"],
["2026-09-24T09:35:26Z","run-state","dispatch","TOOL-aRepatriatedFork-8","-","-","-"],
["2026-09-24T09:35:33Z","git","commit","2ffc74ecf9b8","-","-","TOOL-aRepatriatedFork-10"],
["2026-09-24T09:38:26Z","run-state","dispatch","TOOL-aRepatriatedFork-8","-","-","-"],
["2026-09-24T09:38:44Z","git","commit","6526e331d5d2","-","-","TOOL-aRepatriatedFork-10"],
["2026-09-24T09:39:31Z","git","commit","d1d71c380457","-","-","TOOL-aRepatriatedFork-6"],
["2026-09-24T09:43:32Z","git","commit","386f168b4b3e","-","-","DEPL-aRepatriatedFork-14"],
["2026-09-24T16:13:03Z","run-state","dispatch","TOOL-aRepatriatedFork-8","-","-","-"],
["2026-09-24T16:13:18Z","git","commit","526d43cc9677","-","-","TOOL-aRepatriatedFork-8"],
["2026-09-24T16:19:38Z","run-state","dispatch","TOOL-aRepatriatedFork-8","-","-","-"],
["2026-09-24T16:20:49Z","git","commit","c9ae923fdb50","-","-","TOOL-aRepatriatedFork-8"],
["2026-09-24T18:34:27Z","run-state","phase","d393c445005d","LANDING","-","-"],
["2026-09-24T18:35:06Z","git","merge","2bd14f4bf03a","-","-","-"]]}]},
"Units":{"facts":{"units":"22 · shown 0 · aggregated yes"},"tables":[{"name":"by-status","header":["#","status","units"],"rows":[
["1","BLOCKED","1"],
["2","CLOSED","21"]]}]},
"Decisions":{"facts":{"entries":"191 · shown 0 · aggregated yes","trailer near-misses":"7","decision-log rows the owner's":"0","spec marks":"owner-before 53 · owner-inside 0 · agent-before 0 · agent-inside 7","excluded rows":"proposal 0 · rescope 2 · dispatch 80 · review 2 · brief 34","review rounds":"2 · shown 2 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","3"],
["2","abort","0"],
["3","override","1"],
["4","waiver","0"],
["5","rescope-retire","0"],
["6","rescope-supersede","0"],
["7","review","2"],
["8","trailer","123"],
["9","spec-mark","60"],
["10","decision-log","0"],
["11","ledger","2"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-09-24T03:27:33Z","BLOCKED","1","-"],
["2","2026-09-24T05:41:59Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"25 · shown 0 · aggregated yes"},"tables":[{"name":"by-state","header":["#","item","state","count"],"rows":[
["1","brief-before-build","MET","21"],
["2","phases-walked","MET","1"],
["3","green-at-close","MET","1"],
["4","keepalive-reaped","MET","1"],
["5","review-exited","MET","1"]]}]},
"Anomalies":{"facts":{"anomalies":"26 · shown 0 · aggregated yes"},"tables":[{"name":"by-kind","header":["#","kind","subclass","count"],"rows":[
["1","refusal-loop","-","2"],
["2","killed-verb","-","1"],
["3","red-behind-zero","-","2"],
["4","destructive-git","-","21"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 0","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","419","0"],
["3","gates","present","4","0"],
["4","pushes","present","1","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
