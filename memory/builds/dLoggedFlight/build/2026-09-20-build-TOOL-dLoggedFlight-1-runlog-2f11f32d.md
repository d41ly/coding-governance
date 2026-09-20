# Run record

**Serves:** journal TOOL-dLoggedFlight-1..14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20..30

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/dLoggedFlight/RUN.md
- run: 1 of 1
- start: 2f11f32dbfd9feb92daef3226d10d8b248e46f25
- phase: LANDING
- terminal: no
- window: 2026-09-13T11:05:47Z to 2026-09-20T21:27:54Z
- window opened by: git
- window closed by: last-activity
- duration: 642127s
- own commits: 92
- last own commit: 09e75cefce6f1d79722e5f039fa404c053049c28
- merged: no
- units served: 26
- sources present: 4 of 7
- owner turns: launch 1 · pre-run 1 · in-window 6 · post-close 0
- usage main: requests 639 · in 1342 · out 849013 · cache-read 321613326 · cache-write 7583660
- usage agent: requests 367 · in 734 · out 279340 · cache-read 112646783 · cache-write 794452
- usage workflow: requests 9643 · in 19286 · out 11621801 · cache-read 2392090163 · cache-write 43812336
- attributed calls: 8898 of 12183
- values withheld: 0
- commitment: sha256 bbb7c3282663f60a3fdb888a88bdcfda26430e3b50919d088a19fe121ea5076f · lines 253

## Timeline

- events: 163 · shown 60 · elided 103
- elided: 103 events from 2026-09-13T20:46:46Z to 2026-09-20T12:52:35Z
- withheld rows: verb 123 · push - · push-refused - · gate 7 · compact 2 · limit 103 · idle 2 · workflow 44

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-09-13T11:05:47Z | run-state | phase | a4007553c89f | RUNNING | - | - |
| 2026-09-13T11:58:19Z | git | commit | 1dd6f3da2c12 | - | - | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 |
| 2026-09-13T11:58:19Z | run-state | phase | 2f11f32dbfd9 | SPECCING | - | - |
| 2026-09-13T13:26:12Z | git | commit | b21c5dd3f769 | - | - | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 |
| 2026-09-13T13:26:12Z | run-state | phase | 1dd6f3da2c12 | REVIEWING | - | - |
| 2026-09-13T13:28:05Z | git | commit | f698f6e601cb | - | - | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 |
| 2026-09-13T14:51:45Z | git | commit | 04a4e5af58c0 | - | - | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 |
| 2026-09-13T14:52:51Z | git | commit | e1e83acfb8b6 | - | - | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 |
| 2026-09-13T16:04:26Z | git | commit | d93167b542f5 | - | - | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 |
| 2026-09-13T16:18:49Z | git | commit | 89b00392dab4 | - | - | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 |
| 2026-09-13T16:19:26Z | git | commit | 8730066b6ba4 | - | - | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 |
| 2026-09-13T16:20:11Z | run-state | phase | 8730066b6ba4 | BUILDING | - | - |
| 2026-09-13T16:31:59Z | run-state | dispatch | TOOL-dLoggedFlight-1 | - | - | - |
| 2026-09-13T16:32:03Z | run-state | brief | TOOL-dLoggedFlight-1 | - | - | - |
| 2026-09-13T17:01:43Z | run-state | dispatch | TOOL-dLoggedFlight-1 | - | - | - |
| 2026-09-13T17:02:04Z | git | commit | 03ae473c0c87 | - | - | TOOL-dLoggedFlight-1 |
| 2026-09-13T17:04:20Z | run-state | dispatch | TOOL-dLoggedFlight-1 | - | - | - |
| 2026-09-13T17:06:39Z | git | commit | 9ac609eccebe | - | - | TOOL-dLoggedFlight-1 |
| 2026-09-13T17:28:20Z | run-state | dispatch | TOOL-dLoggedFlight-2 | - | - | - |
| 2026-09-13T17:28:24Z | run-state | brief | TOOL-dLoggedFlight-2 | - | - | - |
| 2026-09-13T17:29:24Z | run-state | dispatch | TOOL-dLoggedFlight-2 | - | - | - |
| 2026-09-13T17:55:58Z | run-state | dispatch | TOOL-dLoggedFlight-2 | - | - | - |
| 2026-09-13T18:28:14Z | git | commit | 796c148ac1bd | - | - | TOOL-dLoggedFlight-2 |
| 2026-09-13T18:39:43Z | git | commit | 83e6024df944 | - | - | TOOL-dLoggedFlight-2 |
| 2026-09-13T18:53:50Z | run-state | dispatch | TOOL-dLoggedFlight-3 | - | - | - |
| 2026-09-13T18:53:54Z | run-state | brief | TOOL-dLoggedFlight-3 | - | - | - |
| 2026-09-13T19:25:44Z | run-state | dispatch | TOOL-dLoggedFlight-3 | - | - | - |
| 2026-09-13T20:13:27Z | git | commit | 33f1db946cc9 | - | - | TOOL-dLoggedFlight-3 |
| 2026-09-13T20:25:00Z | git | commit | 78d97a4824c4 | - | - | TOOL-dLoggedFlight-3 |
| 2026-09-13T20:46:42Z | run-state | dispatch | TOOL-dLoggedFlight-4 | - | - | - |

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-09-20T12:54:50Z | git | commit | af725942ea17 | - | - | TOOL-dLoggedFlight-22 |
| 2026-09-20T13:04:16Z | run-state | dispatch | TOOL-dLoggedFlight-27 | - | - | - |
| 2026-09-20T13:04:21Z | run-state | brief | TOOL-dLoggedFlight-27 | - | - | - |
| 2026-09-20T13:15:48Z | git | commit | 6588fee2b1cd | - | - | TOOL-dLoggedFlight-27 |
| 2026-09-20T13:19:52Z | git | commit | 717656323142 | - | - | TOOL-dLoggedFlight-27 |
| 2026-09-20T13:20:57Z | git | commit | 1cb1960f27f4 | - | - | TOOL-dLoggedFlight-27 |
| 2026-09-20T13:29:50Z | run-state | dispatch | TOOL-dLoggedFlight-20 | - | - | - |
| 2026-09-20T13:29:55Z | run-state | brief | TOOL-dLoggedFlight-20 | - | - | - |
| 2026-09-20T13:44:14Z | git | commit | 9fb8b7853689 | - | - | TOOL-dLoggedFlight-20 |
| 2026-09-20T13:48:21Z | git | commit | 5136bc5e0691 | - | - | TOOL-dLoggedFlight-20 |
| 2026-09-20T13:59:40Z | run-state | dispatch | TOOL-dLoggedFlight-23 | - | - | - |
| 2026-09-20T13:59:46Z | run-state | brief | TOOL-dLoggedFlight-23 | - | - | - |
| 2026-09-20T14:17:02Z | git | commit | 506c0181c70e | - | - | TOOL-dLoggedFlight-23 |
| 2026-09-20T14:19:11Z | git | commit | cb1629ea0934 | - | - | TOOL-dLoggedFlight-23 |
| 2026-09-20T14:30:10Z | run-state | dispatch | TOOL-dLoggedFlight-28 | - | - | - |
| 2026-09-20T14:30:15Z | run-state | brief | TOOL-dLoggedFlight-28 | - | - | - |
| 2026-09-20T14:40:18Z | git | commit | 99cbf16a4eb5 | - | - | TOOL-dLoggedFlight-28 |
| 2026-09-20T14:42:17Z | git | commit | a7351d71dc36 | - | - | TOOL-dLoggedFlight-28 |
| 2026-09-20T14:46:48Z | run-state | dispatch | TOOL-dLoggedFlight-29 | - | - | - |
| 2026-09-20T14:46:52Z | run-state | brief | TOOL-dLoggedFlight-29 | - | - | - |
| 2026-09-20T14:58:47Z | git | commit | 964fed81f71a | - | - | TOOL-dLoggedFlight-29 |
| 2026-09-20T15:01:27Z | git | commit | 1a44ef335060 | - | - | TOOL-dLoggedFlight-29 |
| 2026-09-20T15:03:29Z | git | commit | da9d25f70db4 | - | - | TOOL-dLoggedFlight-29 |
| 2026-09-20T15:04:40Z | git | commit | 62c4d5593bb3 | - | - | TOOL-dLoggedFlight-29 |
| 2026-09-20T15:12:04Z | run-state | dispatch | TOOL-dLoggedFlight-30 | - | - | - |
| 2026-09-20T15:12:09Z | run-state | brief | TOOL-dLoggedFlight-30 | - | - | - |
| 2026-09-20T15:20:00Z | git | commit | fbfd04675674 | - | - | TOOL-dLoggedFlight-30 |
| 2026-09-20T15:24:09Z | git | commit | 2db0cb093fc9 | - | - | TOOL-dLoggedFlight-30 |
| 2026-09-20T15:28:21Z | git | commit | 09e75cefce6f | - | - | TOOL-dLoggedFlight-30 |
| 2026-09-20T16:14:27Z | run-state | phase | 5d472fdd | VERIFYING | - | - |

## Units

- units: 30 · shown 0 · aggregated yes

| # | status | units |
|---|---|---|
| 1 | CLOSED | 26 |
| 2 | WONTDO | 4 |

## Decisions

- entries: 184 · shown 0 · aggregated yes
- trailer near-misses: 37
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 16
- excluded rows: proposal 0 · rescope 17 · dispatch 32 · review 10 · brief 26
- review rounds: 10 · shown 10 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 4 |
| 2 | abort | 0 |
| 3 | override | 1 |
| 4 | waiver | 0 |
| 5 | rescope-retire | 0 |
| 6 | rescope-supersede | 4 |
| 7 | review | 9 |
| 8 | trailer | 80 |
| 9 | spec-mark | 16 |
| 10 | decision-log | 0 |
| 11 | ledger | 70 |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-09-13T13:09:10Z | BLOCKED | 4 | - |
| 2 | 2026-09-13T14:39:51Z | BLOCKED | 1 | - |
| 3 | 2026-09-13T16:03:12Z | CLEAN | 0 | CONVERGED |
| 4 | 2026-09-14T07:59:08Z | BLOCKED | 1 | - |
| 5 | 2026-09-16T12:24:19Z | BLOCKED | 1 | - |
| 6 | 2026-09-16T12:24:19Z | BLOCKED | 1 | NON-CONVERGENT |
| 7 | 2026-09-16T12:54:38Z | BLOCKED | 1 | - |
| 8 | 2026-09-16T14:07:07Z | BLOCKED | 2 | - |
| 9 | 2026-09-16T16:35:03Z | BLOCKED | 1 | - |
| 10 | 2026-09-20T10:32:43Z | BLOCKED | 1 | - |

## Conformance

- items: 30 · shown 0 · aggregated yes

| # | item | state | count |
|---|---|---|---|
| 1 | brief-before-build | MET | 26 |
| 2 | phases-walked | MET | 1 |
| 3 | green-at-close | MET | 1 |
| 4 | keepalive-reaped | MET | 1 |
| 5 | review-exited | UNMET | 1 |

## Anomalies

- anomalies: 25 · shown 0 · aggregated yes

| # | kind | subclass | count |
|---|---|---|---|
| 1 | out-of-band-edit | - | 1 |
| 2 | refusal-loop | - | 2 |
| 3 | red-behind-zero | - | 4 |
| 4 | destructive-git | - | 16 |
| 5 | idle-gap | - | 2 |

## Coverage

- journal starts: 0 joined of 0 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 2
- anomaly kinds: judged 11 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | partial | 246 | 0 |
| 3 | gates | partial | 7 | 0 |
| 4 | pushes | absent | 0 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/dLoggedFlight/RUN.md","run":"1 of 1","start":"2f11f32dbfd9feb92daef3226d10d8b248e46f25","phase":"LANDING","terminal":"no","window":"2026-09-13T11:05:47Z to 2026-09-20T21:27:54Z","window opened by":"git","window closed by":"last-activity","duration":"642127s","own commits":"92","last own commit":"09e75cefce6f1d79722e5f039fa404c053049c28","merged":"no","units served":"26","sources present":"4 of 7","owner turns":"launch 1 · pre-run 1 · in-window 6 · post-close 0","usage main":"requests 639 · in 1342 · out 849013 · cache-read 321613326 · cache-write 7583660","usage agent":"requests 367 · in 734 · out 279340 · cache-read 112646783 · cache-write 794452","usage workflow":"requests 9643 · in 19286 · out 11621801 · cache-read 2392090163 · cache-write 43812336","attributed calls":"8898 of 12183","values withheld":"0","commitment":"sha256 bbb7c3282663f60a3fdb888a88bdcfda26430e3b50919d088a19fe121ea5076f · lines 253"},"tables":[]},
"Timeline":{"facts":{"events":"163 · shown 60 · elided 103","elided":"103 events from 2026-09-13T20:46:46Z to 2026-09-20T12:52:35Z","withheld rows":"verb 123 · push - · push-refused - · gate 7 · compact 2 · limit 103 · idle 2 · workflow 44"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-09-13T11:05:47Z","run-state","phase","a4007553c89f","RUNNING","-","-"],
["2026-09-13T11:58:19Z","git","commit","1dd6f3da2c12","-","-","TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9"],
["2026-09-13T11:58:19Z","run-state","phase","2f11f32dbfd9","SPECCING","-","-"],
["2026-09-13T13:26:12Z","git","commit","b21c5dd3f769","-","-","TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9"],
["2026-09-13T13:26:12Z","run-state","phase","1dd6f3da2c12","REVIEWING","-","-"],
["2026-09-13T13:28:05Z","git","commit","f698f6e601cb","-","-","TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9"],
["2026-09-13T14:51:45Z","git","commit","04a4e5af58c0","-","-","TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9"],
["2026-09-13T14:52:51Z","git","commit","e1e83acfb8b6","-","-","TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4"],
["2026-09-13T16:04:26Z","git","commit","d93167b542f5","-","-","TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9"],
["2026-09-13T16:18:49Z","git","commit","89b00392dab4","-","-","TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4"],
["2026-09-13T16:19:26Z","git","commit","8730066b6ba4","-","-","TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9"],
["2026-09-13T16:20:11Z","run-state","phase","8730066b6ba4","BUILDING","-","-"],
["2026-09-13T16:31:59Z","run-state","dispatch","TOOL-dLoggedFlight-1","-","-","-"],
["2026-09-13T16:32:03Z","run-state","brief","TOOL-dLoggedFlight-1","-","-","-"],
["2026-09-13T17:01:43Z","run-state","dispatch","TOOL-dLoggedFlight-1","-","-","-"],
["2026-09-13T17:02:04Z","git","commit","03ae473c0c87","-","-","TOOL-dLoggedFlight-1"],
["2026-09-13T17:04:20Z","run-state","dispatch","TOOL-dLoggedFlight-1","-","-","-"],
["2026-09-13T17:06:39Z","git","commit","9ac609eccebe","-","-","TOOL-dLoggedFlight-1"],
["2026-09-13T17:28:20Z","run-state","dispatch","TOOL-dLoggedFlight-2","-","-","-"],
["2026-09-13T17:28:24Z","run-state","brief","TOOL-dLoggedFlight-2","-","-","-"],
["2026-09-13T17:29:24Z","run-state","dispatch","TOOL-dLoggedFlight-2","-","-","-"],
["2026-09-13T17:55:58Z","run-state","dispatch","TOOL-dLoggedFlight-2","-","-","-"],
["2026-09-13T18:28:14Z","git","commit","796c148ac1bd","-","-","TOOL-dLoggedFlight-2"],
["2026-09-13T18:39:43Z","git","commit","83e6024df944","-","-","TOOL-dLoggedFlight-2"],
["2026-09-13T18:53:50Z","run-state","dispatch","TOOL-dLoggedFlight-3","-","-","-"],
["2026-09-13T18:53:54Z","run-state","brief","TOOL-dLoggedFlight-3","-","-","-"],
["2026-09-13T19:25:44Z","run-state","dispatch","TOOL-dLoggedFlight-3","-","-","-"],
["2026-09-13T20:13:27Z","git","commit","33f1db946cc9","-","-","TOOL-dLoggedFlight-3"],
["2026-09-13T20:25:00Z","git","commit","78d97a4824c4","-","-","TOOL-dLoggedFlight-3"],
["2026-09-13T20:46:42Z","run-state","dispatch","TOOL-dLoggedFlight-4","-","-","-"]]},
{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-09-20T12:54:50Z","git","commit","af725942ea17","-","-","TOOL-dLoggedFlight-22"],
["2026-09-20T13:04:16Z","run-state","dispatch","TOOL-dLoggedFlight-27","-","-","-"],
["2026-09-20T13:04:21Z","run-state","brief","TOOL-dLoggedFlight-27","-","-","-"],
["2026-09-20T13:15:48Z","git","commit","6588fee2b1cd","-","-","TOOL-dLoggedFlight-27"],
["2026-09-20T13:19:52Z","git","commit","717656323142","-","-","TOOL-dLoggedFlight-27"],
["2026-09-20T13:20:57Z","git","commit","1cb1960f27f4","-","-","TOOL-dLoggedFlight-27"],
["2026-09-20T13:29:50Z","run-state","dispatch","TOOL-dLoggedFlight-20","-","-","-"],
["2026-09-20T13:29:55Z","run-state","brief","TOOL-dLoggedFlight-20","-","-","-"],
["2026-09-20T13:44:14Z","git","commit","9fb8b7853689","-","-","TOOL-dLoggedFlight-20"],
["2026-09-20T13:48:21Z","git","commit","5136bc5e0691","-","-","TOOL-dLoggedFlight-20"],
["2026-09-20T13:59:40Z","run-state","dispatch","TOOL-dLoggedFlight-23","-","-","-"],
["2026-09-20T13:59:46Z","run-state","brief","TOOL-dLoggedFlight-23","-","-","-"],
["2026-09-20T14:17:02Z","git","commit","506c0181c70e","-","-","TOOL-dLoggedFlight-23"],
["2026-09-20T14:19:11Z","git","commit","cb1629ea0934","-","-","TOOL-dLoggedFlight-23"],
["2026-09-20T14:30:10Z","run-state","dispatch","TOOL-dLoggedFlight-28","-","-","-"],
["2026-09-20T14:30:15Z","run-state","brief","TOOL-dLoggedFlight-28","-","-","-"],
["2026-09-20T14:40:18Z","git","commit","99cbf16a4eb5","-","-","TOOL-dLoggedFlight-28"],
["2026-09-20T14:42:17Z","git","commit","a7351d71dc36","-","-","TOOL-dLoggedFlight-28"],
["2026-09-20T14:46:48Z","run-state","dispatch","TOOL-dLoggedFlight-29","-","-","-"],
["2026-09-20T14:46:52Z","run-state","brief","TOOL-dLoggedFlight-29","-","-","-"],
["2026-09-20T14:58:47Z","git","commit","964fed81f71a","-","-","TOOL-dLoggedFlight-29"],
["2026-09-20T15:01:27Z","git","commit","1a44ef335060","-","-","TOOL-dLoggedFlight-29"],
["2026-09-20T15:03:29Z","git","commit","da9d25f70db4","-","-","TOOL-dLoggedFlight-29"],
["2026-09-20T15:04:40Z","git","commit","62c4d5593bb3","-","-","TOOL-dLoggedFlight-29"],
["2026-09-20T15:12:04Z","run-state","dispatch","TOOL-dLoggedFlight-30","-","-","-"],
["2026-09-20T15:12:09Z","run-state","brief","TOOL-dLoggedFlight-30","-","-","-"],
["2026-09-20T15:20:00Z","git","commit","fbfd04675674","-","-","TOOL-dLoggedFlight-30"],
["2026-09-20T15:24:09Z","git","commit","2db0cb093fc9","-","-","TOOL-dLoggedFlight-30"],
["2026-09-20T15:28:21Z","git","commit","09e75cefce6f","-","-","TOOL-dLoggedFlight-30"],
["2026-09-20T16:14:27Z","run-state","phase","5d472fdd","VERIFYING","-","-"]]}]},
"Units":{"facts":{"units":"30 · shown 0 · aggregated yes"},"tables":[{"name":"by-status","header":["#","status","units"],"rows":[
["1","CLOSED","26"],
["2","WONTDO","4"]]}]},
"Decisions":{"facts":{"entries":"184 · shown 0 · aggregated yes","trailer near-misses":"37","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 16","excluded rows":"proposal 0 · rescope 17 · dispatch 32 · review 10 · brief 26","review rounds":"10 · shown 10 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","4"],
["2","abort","0"],
["3","override","1"],
["4","waiver","0"],
["5","rescope-retire","0"],
["6","rescope-supersede","4"],
["7","review","9"],
["8","trailer","80"],
["9","spec-mark","16"],
["10","decision-log","0"],
["11","ledger","70"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-09-13T13:09:10Z","BLOCKED","4","-"],
["2","2026-09-13T14:39:51Z","BLOCKED","1","-"],
["3","2026-09-13T16:03:12Z","CLEAN","0","CONVERGED"],
["4","2026-09-14T07:59:08Z","BLOCKED","1","-"],
["5","2026-09-16T12:24:19Z","BLOCKED","1","-"],
["6","2026-09-16T12:24:19Z","BLOCKED","1","NON-CONVERGENT"],
["7","2026-09-16T12:54:38Z","BLOCKED","1","-"],
["8","2026-09-16T14:07:07Z","BLOCKED","2","-"],
["9","2026-09-16T16:35:03Z","BLOCKED","1","-"],
["10","2026-09-20T10:32:43Z","BLOCKED","1","-"]]}]},
"Conformance":{"facts":{"items":"30 · shown 0 · aggregated yes"},"tables":[{"name":"by-state","header":["#","item","state","count"],"rows":[
["1","brief-before-build","MET","26"],
["2","phases-walked","MET","1"],
["3","green-at-close","MET","1"],
["4","keepalive-reaped","MET","1"],
["5","review-exited","UNMET","1"]]}]},
"Anomalies":{"facts":{"anomalies":"25 · shown 0 · aggregated yes"},"tables":[{"name":"by-kind","header":["#","kind","subclass","count"],"rows":[
["1","out-of-band-edit","-","1"],
["2","refusal-loop","-","2"],
["3","red-behind-zero","-","4"],
["4","destructive-git","-","16"],
["5","idle-gap","-","2"]]}]},
"Coverage":{"facts":{"journal starts":"0 joined of 0 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 2","anomaly kinds":"judged 11 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","partial","246","0"],
["3","gates","partial","7","0"],
["4","pushes","absent","0","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
