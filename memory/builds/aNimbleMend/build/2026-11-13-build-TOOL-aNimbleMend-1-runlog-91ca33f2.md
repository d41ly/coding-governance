# Run record

**Serves:** journal TOOL-aNimbleMend-1..15 TOOL-aNimbleMend-27

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aNimbleMend/RUN.md
- run: 1 of 1
- start: 91ca33f20859846d021d304c837b08e14b5c8766
- phase: LANDING
- terminal: no
- window: 2026-11-12T13:23:26Z to 2026-11-13T07:40:01Z
- window opened by: git
- window closed by: last-activity
- duration: 65795s · DERIVED from the window
- own commits: 64
- last own commit: 0071491ade5c8b07912711a33a471432f00ff48c
- merged: yes
- units served: 16
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 0 · in-window 3 · post-close 0
- usage main: requests 729 · in 1772 · out 474026 · cache-read 380370115 · cache-write 1661981
- usage agent: requests 58 · in 116 · out 111909 · cache-read 7654524 · cache-write 394584
- usage workflow: requests 1323 · in 2718 · out 1687046 · cache-read 180723468 · cache-write 9521779
- attributed calls: 2142 of 2772
- values withheld: 1
- commitment: sha256 48bf9c7aebf1fe103ae56f89ce7617afccec63b8f6185dd37e5d398eb73e8886 · lines 1000

## Timeline

- events: 134 · shown 60 · elided 74
- elided: 74 events from 2026-11-12T15:38:07Z to 2026-11-12T21:15:32Z
- withheld rows: verb 452 · push 38 · push-refused 0 · gate 20 · compact 1 · limit 6 · idle 0 · workflow 34

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-11-12T13:23:26Z | run-state | phase | 1265772cc365 | RUNNING | - | - |
| 2026-11-12T14:18:08Z | git | commit | 0ab43cad1f8a | - | - | TOOL-aNimbleMend-1 TOOL-aNimbleMend-12 |
| 2026-11-12T14:18:08Z | run-state | phase | 91ca33f20859 | SPECCING | - | - |
| 2026-11-12T14:21:46Z | git | commit | ec74d7006e46 | - | - | TOOL-aNimbleMend-11 |
| 2026-11-12T14:29:06Z | git | commit | 72a9a7a8cc97 | - | - | TOOL-aNimbleMend-12 TOOL-aNimbleMend-2 TOOL-aNimbleMend-4 |
| 2026-11-12T14:33:04Z | git | commit | 5484178a6056 | - | - | TOOL-aNimbleMend-1 TOOL-aNimbleMend-12 |
| 2026-11-12T14:33:04Z | run-state | phase | 72a9a7a8cc97 | BUILDING | - | - |
| 2026-11-12T14:35:41Z | run-state | dispatch | TOOL-aNimbleMend-1 | - | - | - |
| 2026-11-12T14:35:43Z | run-state | brief | TOOL-aNimbleMend-1 | - | - | - |
| 2026-11-12T14:38:27Z | run-state | dispatch | TOOL-aNimbleMend-1 | - | - | - |
| 2026-11-12T14:40:04Z | git | commit | 75115e9af8d6 | - | - | TOOL-aNimbleMend-1 |
| 2026-11-12T14:42:23Z | run-state | dispatch | TOOL-aNimbleMend-1 | - | - | - |
| 2026-11-12T14:43:16Z | git | commit | 2121531db238 | - | - | TOOL-aNimbleMend-1 |
| 2026-11-12T14:46:22Z | run-state | dispatch | TOOL-aNimbleMend-1 | - | - | - |
| 2026-11-12T14:46:24Z | git | commit | 27cd3a9da12c | - | - | TOOL-aNimbleMend-1 |
| 2026-11-12T14:48:24Z | git | commit | a4a3b4ed0619 | - | - | TOOL-aNimbleMend-2 |
| 2026-11-12T14:50:52Z | run-state | dispatch | TOOL-aNimbleMend-2 | - | - | - |
| 2026-11-12T14:50:54Z | run-state | brief | TOOL-aNimbleMend-2 | - | - | - |
| 2026-11-12T14:58:51Z | run-state | dispatch | TOOL-aNimbleMend-2 | - | - | - |
| 2026-11-12T14:59:08Z | git | commit | d4eb74047106 | - | - | TOOL-aNimbleMend-2 |
| 2026-11-12T15:02:10Z | git | commit | a02ce85edcd1 | - | - | TOOL-aNimbleMend-4 |
| 2026-11-12T15:05:16Z | run-state | dispatch | TOOL-aNimbleMend-4 | - | - | - |
| 2026-11-12T15:05:18Z | run-state | brief | TOOL-aNimbleMend-4 | - | - | - |
| 2026-11-12T15:13:03Z | git | commit | 0ea161c39cbe | - | - | TOOL-aNimbleMend-4 |
| 2026-11-12T15:20:40Z | git | commit | 88efda1367dc | - | - | TOOL-aNimbleMend-4 |
| 2026-11-12T15:22:54Z | run-state | dispatch | TOOL-aNimbleMend-4 | - | - | - |
| 2026-11-12T15:25:06Z | git | commit | 729762c56740 | - | - | TOOL-aNimbleMend-4 |
| 2026-11-12T15:32:20Z | git | commit | eccda329df8d | - | - | TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-4 |
| 2026-11-12T15:34:33Z | git | commit | a49837d4c0df | - | - | TOOL-aNimbleMend-3 |
| 2026-11-12T15:38:05Z | run-state | dispatch | TOOL-aNimbleMend-3 | - | - | - |

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-11-12T21:28:48Z | run-state | dispatch | TOOL-aNimbleMend-15 | - | - | - |
| 2026-11-12T21:29:54Z | git | commit | a56828506d77 | - | - | TOOL-aNimbleMend-15 |
| 2026-11-12T21:41:12Z | git | commit | 64439c8ddda5 | - | - | TOOL-aNimbleMend-15 |
| 2026-11-12T21:49:28Z | run-state | dispatch | TOOL-aNimbleMend-15 | - | - | - |
| 2026-11-12T21:49:31Z | git | commit | c46ec725e784 | - | - | TOOL-aNimbleMend-15 |
| 2026-11-12T21:57:46Z | git | commit | f9d6d6bebbef | - | - | TOOL-aNimbleMend-15 |
| 2026-11-12T22:02:21Z | run-state | dispatch | TOOL-aNimbleMend-15 | - | - | - |
| 2026-11-12T22:08:53Z | git | commit | 685c0bf2f9c6 | - | - | TOOL-aNimbleMend-15 |
| 2026-11-12T22:19:49Z | run-state | dispatch | TOOL-aNimbleMend-15 | - | - | - |
| 2026-11-12T22:20:53Z | git | commit | 7e785ac21389 | - | - | TOOL-aNimbleMend-15 |
| 2026-11-12T23:12:53Z | run-state | dispatch | TOOL-aNimbleMend-15 | - | - | - |
| 2026-11-12T23:16:18Z | git | commit | 8ed4b1d5636a | - | - | TOOL-aNimbleMend-15 |
| 2026-11-12T23:16:18Z | run-state | phase | 7e785ac21389 | VERIFYING | - | - |
| 2026-11-12T23:42:07Z | run-state | dispatch | TOOL-aNimbleMend-15 | - | - | - |
| 2026-11-12T23:46:19Z | git | commit | 369e6922c7f7 | - | - | TOOL-aNimbleMend-15 |
| 2026-11-13T01:22:44Z | run-state | dispatch | TOOL-aNimbleMend-15 | - | - | - |
| 2026-11-13T01:23:48Z | git | commit | df037bd306a3 | - | - | TOOL-aNimbleMend-15 |
| 2026-11-13T03:13:01Z | git | commit | eeadcf9046db | - | - | TOOL-aNimbleMend-10 TOOL-aNimbleMend-12 TOOL-aNimbleMend-14 TOOL-aNimbleMend-2 |
| 2026-11-13T03:18:28Z | git | commit | aef875cbdc2e | - | - | - |
| 2026-11-13T03:54:45Z | git | commit | 0071491ade5c | - | - | TOOL-aNimbleMend-15 |
| 2026-11-13T03:58:15Z | git | merge | e3fedd1eaef3 | - | - | - |
| 2026-11-13T04:01:14Z | git | merge | 6f50dab916b3 | - | - | - |
| 2026-11-13T05:05:09Z | run-state | dispatch | TOOL-aNimbleMend-15 | - | - | - |
| 2026-11-13T05:10:24Z | run-state | dispatch | TOOL-aNimbleMend-15 | - | - | - |
| 2026-11-13T06:30:45Z | run-state | brief | TOOL-aNimbleMend-27 | - | - | - |
| 2026-11-13T06:32:02Z | run-state | phase | 602f89528e4c | BUILDING | - | - |
| 2026-11-13T06:37:06Z | run-state | dispatch | TOOL-aNimbleMend-27 | - | - | - |
| 2026-11-13T06:50:27Z | run-state | dispatch | TOOL-aNimbleMend-27 | - | - | - |
| 2026-11-13T07:01:21Z | run-state | phase | 148920512962 | VERIFYING | - | - |
| 2026-11-13T07:40:01Z | run-state | phase | 148920512962 | LANDING | - | - |

## Units

- units: 16 · shown 16 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | TOOL-aNimbleMend-1 | CLOSED | 6 | 4 | 1 | 2121531db238 |
| 2 | TOOL-aNimbleMend-2 | CLOSED | 5 | 2 | 1 | d4eb74047106 |
| 3 | TOOL-aNimbleMend-4 | CLOSED | 6 | 2 | 1 | 0ea161c39cbe |
| 4 | TOOL-aNimbleMend-3 | CLOSED | 2 | 1 | 1 | 82e4bddd25cf |
| 5 | TOOL-aNimbleMend-5 | CLOSED | 2 | 1 | 1 | 910734ec6319 |
| 6 | TOOL-aNimbleMend-6 | CLOSED | 2 | 1 | 1 | a88517562223 |
| 7 | TOOL-aNimbleMend-7 | CLOSED | 2 | 2 | 1 | bde79f210f27 |
| 8 | TOOL-aNimbleMend-8 | CLOSED | 2 | 2 | 1 | 93bb9b87a31d |
| 8 | TOOL-aNimbleMend-13 | CLOSED | 6 | 3 | 1 | cb1ee1c519d3 |
| 9 | TOOL-aNimbleMend-9 | CLOSED | 4 | 3 | 1 | 25f552c45d75 |
| 10 | TOOL-aNimbleMend-10 | CLOSED | 3 | 1 | 1 | cf44617fde10 |
| 11 | TOOL-aNimbleMend-11 | CLOSED | 5 | 3 | 1 | de6e03312064 |
| 12 | TOOL-aNimbleMend-12 | CLOSED | 9 | 5 | 1 | 679697d7c8e6 |
| 14 | TOOL-aNimbleMend-14 | CLOSED | 7 | 1 | 1 | 227f840eb5d5 |
| 15 | TOOL-aNimbleMend-15 | CLOSED | 14 | 10 | 1 | a56828506d77 |
| 16 | TOOL-aNimbleMend-27 | CLOSED | 0 | 2 | 1 | - |

## Decisions

- entries: 122 · shown 0 · aggregated yes
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 13
- excluded rows: proposal 0 · rescope 4 · dispatch 43 · review 1 · brief 16 · hold 0 · resume 0
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
| 10 | trailer | 101 |
| 11 | spec-mark | 13 |
| 12 | decision-log | 1 |
| 13 | ledger | 6 |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-11-12T20:20:13Z | CLEAN WITH FIXES | 0 | CONVERGED |

## Conformance

- items: 19 · shown 19 · aggregated no

| # | item | unit | state |
|---|---|---|---|
| 1 | brief-before-build | TOOL-aNimbleMend-1 | MET |
| 2 | brief-before-build | TOOL-aNimbleMend-10 | MET |
| 3 | brief-before-build | TOOL-aNimbleMend-11 | MET |
| 4 | brief-before-build | TOOL-aNimbleMend-12 | MET |
| 5 | brief-before-build | TOOL-aNimbleMend-13 | MET |
| 6 | brief-before-build | TOOL-aNimbleMend-14 | MET |
| 7 | brief-before-build | TOOL-aNimbleMend-15 | MET |
| 8 | brief-before-build | TOOL-aNimbleMend-2 | MET |
| 9 | brief-before-build | TOOL-aNimbleMend-3 | MET |
| 10 | brief-before-build | TOOL-aNimbleMend-4 | MET |
| 11 | brief-before-build | TOOL-aNimbleMend-5 | MET |
| 12 | brief-before-build | TOOL-aNimbleMend-6 | MET |
| 13 | brief-before-build | TOOL-aNimbleMend-7 | MET |
| 14 | brief-before-build | TOOL-aNimbleMend-8 | MET |
| 15 | brief-before-build | TOOL-aNimbleMend-9 | MET |
| 16 | phases-walked | - | MET |
| 17 | green-at-close | - | MET |
| 18 | keepalive-reaped | - | MET |
| 19 | review-exited | - | MET |

## Anomalies

- anomalies: 10 · shown 10 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | nonterminal-merged | other |
| 2 | out-of-band-edit | - |
| 3 | out-of-band-edit | - |
| 4 | out-of-band-edit | - |
| 5 | out-of-band-edit | - |
| 6 | refusal-loop | - |
| 7 | destructive-git | - |
| 8 | destructive-git | - |
| 9 | destructive-git | - |
| 10 | destructive-git | - |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 0
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 904 | 1 |
| 3 | gates | present | 20 | 0 |
| 4 | pushes | present | 38 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aNimbleMend/RUN.md","run":"1 of 1","start":"91ca33f20859846d021d304c837b08e14b5c8766","phase":"LANDING","terminal":"no","window":"2026-11-12T13:23:26Z to 2026-11-13T07:40:01Z","window opened by":"git","window closed by":"last-activity","duration":"65795s · DERIVED from the window","own commits":"64","last own commit":"0071491ade5c8b07912711a33a471432f00ff48c","merged":"yes","units served":"16","sources present":"7 of 7","owner turns":"launch 1 · pre-run 0 · in-window 3 · post-close 0","usage main":"requests 729 · in 1772 · out 474026 · cache-read 380370115 · cache-write 1661981","usage agent":"requests 58 · in 116 · out 111909 · cache-read 7654524 · cache-write 394584","usage workflow":"requests 1323 · in 2718 · out 1687046 · cache-read 180723468 · cache-write 9521779","attributed calls":"2142 of 2772","values withheld":"1","commitment":"sha256 48bf9c7aebf1fe103ae56f89ce7617afccec63b8f6185dd37e5d398eb73e8886 · lines 1000"},"tables":[]},
"Timeline":{"facts":{"events":"134 · shown 60 · elided 74","elided":"74 events from 2026-11-12T15:38:07Z to 2026-11-12T21:15:32Z","withheld rows":"verb 452 · push 38 · push-refused 0 · gate 20 · compact 1 · limit 6 · idle 0 · workflow 34"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-11-12T13:23:26Z","run-state","phase","1265772cc365","RUNNING","-","-"],
["2026-11-12T14:18:08Z","git","commit","0ab43cad1f8a","-","-","TOOL-aNimbleMend-1 TOOL-aNimbleMend-12"],
["2026-11-12T14:18:08Z","run-state","phase","91ca33f20859","SPECCING","-","-"],
["2026-11-12T14:21:46Z","git","commit","ec74d7006e46","-","-","TOOL-aNimbleMend-11"],
["2026-11-12T14:29:06Z","git","commit","72a9a7a8cc97","-","-","TOOL-aNimbleMend-12 TOOL-aNimbleMend-2 TOOL-aNimbleMend-4"],
["2026-11-12T14:33:04Z","git","commit","5484178a6056","-","-","TOOL-aNimbleMend-1 TOOL-aNimbleMend-12"],
["2026-11-12T14:33:04Z","run-state","phase","72a9a7a8cc97","BUILDING","-","-"],
["2026-11-12T14:35:41Z","run-state","dispatch","TOOL-aNimbleMend-1","-","-","-"],
["2026-11-12T14:35:43Z","run-state","brief","TOOL-aNimbleMend-1","-","-","-"],
["2026-11-12T14:38:27Z","run-state","dispatch","TOOL-aNimbleMend-1","-","-","-"],
["2026-11-12T14:40:04Z","git","commit","75115e9af8d6","-","-","TOOL-aNimbleMend-1"],
["2026-11-12T14:42:23Z","run-state","dispatch","TOOL-aNimbleMend-1","-","-","-"],
["2026-11-12T14:43:16Z","git","commit","2121531db238","-","-","TOOL-aNimbleMend-1"],
["2026-11-12T14:46:22Z","run-state","dispatch","TOOL-aNimbleMend-1","-","-","-"],
["2026-11-12T14:46:24Z","git","commit","27cd3a9da12c","-","-","TOOL-aNimbleMend-1"],
["2026-11-12T14:48:24Z","git","commit","a4a3b4ed0619","-","-","TOOL-aNimbleMend-2"],
["2026-11-12T14:50:52Z","run-state","dispatch","TOOL-aNimbleMend-2","-","-","-"],
["2026-11-12T14:50:54Z","run-state","brief","TOOL-aNimbleMend-2","-","-","-"],
["2026-11-12T14:58:51Z","run-state","dispatch","TOOL-aNimbleMend-2","-","-","-"],
["2026-11-12T14:59:08Z","git","commit","d4eb74047106","-","-","TOOL-aNimbleMend-2"],
["2026-11-12T15:02:10Z","git","commit","a02ce85edcd1","-","-","TOOL-aNimbleMend-4"],
["2026-11-12T15:05:16Z","run-state","dispatch","TOOL-aNimbleMend-4","-","-","-"],
["2026-11-12T15:05:18Z","run-state","brief","TOOL-aNimbleMend-4","-","-","-"],
["2026-11-12T15:13:03Z","git","commit","0ea161c39cbe","-","-","TOOL-aNimbleMend-4"],
["2026-11-12T15:20:40Z","git","commit","88efda1367dc","-","-","TOOL-aNimbleMend-4"],
["2026-11-12T15:22:54Z","run-state","dispatch","TOOL-aNimbleMend-4","-","-","-"],
["2026-11-12T15:25:06Z","git","commit","729762c56740","-","-","TOOL-aNimbleMend-4"],
["2026-11-12T15:32:20Z","git","commit","eccda329df8d","-","-","TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-4"],
["2026-11-12T15:34:33Z","git","commit","a49837d4c0df","-","-","TOOL-aNimbleMend-3"],
["2026-11-12T15:38:05Z","run-state","dispatch","TOOL-aNimbleMend-3","-","-","-"]]},
{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-11-12T21:28:48Z","run-state","dispatch","TOOL-aNimbleMend-15","-","-","-"],
["2026-11-12T21:29:54Z","git","commit","a56828506d77","-","-","TOOL-aNimbleMend-15"],
["2026-11-12T21:41:12Z","git","commit","64439c8ddda5","-","-","TOOL-aNimbleMend-15"],
["2026-11-12T21:49:28Z","run-state","dispatch","TOOL-aNimbleMend-15","-","-","-"],
["2026-11-12T21:49:31Z","git","commit","c46ec725e784","-","-","TOOL-aNimbleMend-15"],
["2026-11-12T21:57:46Z","git","commit","f9d6d6bebbef","-","-","TOOL-aNimbleMend-15"],
["2026-11-12T22:02:21Z","run-state","dispatch","TOOL-aNimbleMend-15","-","-","-"],
["2026-11-12T22:08:53Z","git","commit","685c0bf2f9c6","-","-","TOOL-aNimbleMend-15"],
["2026-11-12T22:19:49Z","run-state","dispatch","TOOL-aNimbleMend-15","-","-","-"],
["2026-11-12T22:20:53Z","git","commit","7e785ac21389","-","-","TOOL-aNimbleMend-15"],
["2026-11-12T23:12:53Z","run-state","dispatch","TOOL-aNimbleMend-15","-","-","-"],
["2026-11-12T23:16:18Z","git","commit","8ed4b1d5636a","-","-","TOOL-aNimbleMend-15"],
["2026-11-12T23:16:18Z","run-state","phase","7e785ac21389","VERIFYING","-","-"],
["2026-11-12T23:42:07Z","run-state","dispatch","TOOL-aNimbleMend-15","-","-","-"],
["2026-11-12T23:46:19Z","git","commit","369e6922c7f7","-","-","TOOL-aNimbleMend-15"],
["2026-11-13T01:22:44Z","run-state","dispatch","TOOL-aNimbleMend-15","-","-","-"],
["2026-11-13T01:23:48Z","git","commit","df037bd306a3","-","-","TOOL-aNimbleMend-15"],
["2026-11-13T03:13:01Z","git","commit","eeadcf9046db","-","-","TOOL-aNimbleMend-10 TOOL-aNimbleMend-12 TOOL-aNimbleMend-14 TOOL-aNimbleMend-2"],
["2026-11-13T03:18:28Z","git","commit","aef875cbdc2e","-","-","-"],
["2026-11-13T03:54:45Z","git","commit","0071491ade5c","-","-","TOOL-aNimbleMend-15"],
["2026-11-13T03:58:15Z","git","merge","e3fedd1eaef3","-","-","-"],
["2026-11-13T04:01:14Z","git","merge","6f50dab916b3","-","-","-"],
["2026-11-13T05:05:09Z","run-state","dispatch","TOOL-aNimbleMend-15","-","-","-"],
["2026-11-13T05:10:24Z","run-state","dispatch","TOOL-aNimbleMend-15","-","-","-"],
["2026-11-13T06:30:45Z","run-state","brief","TOOL-aNimbleMend-27","-","-","-"],
["2026-11-13T06:32:02Z","run-state","phase","602f89528e4c","BUILDING","-","-"],
["2026-11-13T06:37:06Z","run-state","dispatch","TOOL-aNimbleMend-27","-","-","-"],
["2026-11-13T06:50:27Z","run-state","dispatch","TOOL-aNimbleMend-27","-","-","-"],
["2026-11-13T07:01:21Z","run-state","phase","148920512962","VERIFYING","-","-"],
["2026-11-13T07:40:01Z","run-state","phase","148920512962","LANDING","-","-"]]}]},
"Units":{"facts":{"units":"16 · shown 16 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","TOOL-aNimbleMend-1","CLOSED","6","4","1","2121531db238"],
["2","TOOL-aNimbleMend-2","CLOSED","5","2","1","d4eb74047106"],
["3","TOOL-aNimbleMend-4","CLOSED","6","2","1","0ea161c39cbe"],
["4","TOOL-aNimbleMend-3","CLOSED","2","1","1","82e4bddd25cf"],
["5","TOOL-aNimbleMend-5","CLOSED","2","1","1","910734ec6319"],
["6","TOOL-aNimbleMend-6","CLOSED","2","1","1","a88517562223"],
["7","TOOL-aNimbleMend-7","CLOSED","2","2","1","bde79f210f27"],
["8","TOOL-aNimbleMend-8","CLOSED","2","2","1","93bb9b87a31d"],
["8","TOOL-aNimbleMend-13","CLOSED","6","3","1","cb1ee1c519d3"],
["9","TOOL-aNimbleMend-9","CLOSED","4","3","1","25f552c45d75"],
["10","TOOL-aNimbleMend-10","CLOSED","3","1","1","cf44617fde10"],
["11","TOOL-aNimbleMend-11","CLOSED","5","3","1","de6e03312064"],
["12","TOOL-aNimbleMend-12","CLOSED","9","5","1","679697d7c8e6"],
["14","TOOL-aNimbleMend-14","CLOSED","7","1","1","227f840eb5d5"],
["15","TOOL-aNimbleMend-15","CLOSED","14","10","1","a56828506d77"],
["16","TOOL-aNimbleMend-27","CLOSED","0","2","1","-"]]}]},
"Decisions":{"facts":{"entries":"122 · shown 0 · aggregated yes","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 13","excluded rows":"proposal 0 · rescope 4 · dispatch 43 · review 1 · brief 16 · hold 0 · resume 0","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","0"],
["2","abort","0"],
["3","override","0"],
["4","waiver","0"],
["5","handoff","0"],
["6","rescope-retire","0"],
["7","rescope-supersede","0"],
["8","rescope-defer","0"],
["9","review","1"],
["10","trailer","101"],
["11","spec-mark","13"],
["12","decision-log","1"],
["13","ledger","6"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-11-12T20:20:13Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"19 · shown 19 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","TOOL-aNimbleMend-1","MET"],
["2","brief-before-build","TOOL-aNimbleMend-10","MET"],
["3","brief-before-build","TOOL-aNimbleMend-11","MET"],
["4","brief-before-build","TOOL-aNimbleMend-12","MET"],
["5","brief-before-build","TOOL-aNimbleMend-13","MET"],
["6","brief-before-build","TOOL-aNimbleMend-14","MET"],
["7","brief-before-build","TOOL-aNimbleMend-15","MET"],
["8","brief-before-build","TOOL-aNimbleMend-2","MET"],
["9","brief-before-build","TOOL-aNimbleMend-3","MET"],
["10","brief-before-build","TOOL-aNimbleMend-4","MET"],
["11","brief-before-build","TOOL-aNimbleMend-5","MET"],
["12","brief-before-build","TOOL-aNimbleMend-6","MET"],
["13","brief-before-build","TOOL-aNimbleMend-7","MET"],
["14","brief-before-build","TOOL-aNimbleMend-8","MET"],
["15","brief-before-build","TOOL-aNimbleMend-9","MET"],
["16","phases-walked","-","MET"],
["17","green-at-close","-","MET"],
["18","keepalive-reaped","-","MET"],
["19","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"10 · shown 10 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","nonterminal-merged","other"],
["2","out-of-band-edit","-"],
["3","out-of-band-edit","-"],
["4","out-of-band-edit","-"],
["5","out-of-band-edit","-"],
["6","refusal-loop","-"],
["7","destructive-git","-"],
["8","destructive-git","-"],
["9","destructive-git","-"],
["10","destructive-git","-"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 0","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","904","1"],
["3","gates","present","20","0"],
["4","pushes","present","38","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
