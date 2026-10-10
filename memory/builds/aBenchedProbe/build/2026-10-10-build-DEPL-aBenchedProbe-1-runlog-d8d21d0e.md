# Run record

**Serves:** journal DEPL-aBenchedProbe-1..4 TOOL-aBenchedProbe-1..2

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/aBenchedProbe/RUN.md
- run: 1 of 1
- start: d8d21d0e94d2d6c6037b8cf45eaf1cc4d5d7c138
- phase: LANDING
- terminal: no
- window: 2026-10-09T17:08:32Z to 2026-10-10T07:28:56Z
- window opened by: git
- window closed by: last-activity
- duration: 51624s
- own commits: 8
- last own commit: a656e35ff1e0d5be17c16fd8b4d98c0449ee7271
- merged: no
- units served: 6
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 0 · in-window 4 · post-close 0
- usage main: requests 191 · in 408 · out 110350 · cache-read 79063342 · cache-write 1911653
- usage agent: requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0
- usage workflow: requests 710 · in 1420 · out 483364 · cache-read 101485387 · cache-write 3820057
- attributed calls: 835 of 979
- values withheld: 0
- commitment: sha256 f3a410fa50834b35475279bb195a6afd9eb644df04302568129af4cb1b22de8e · lines 238

## Timeline

- events: 35 · shown 35 · elided 0
- withheld rows: verb 88 · push 32 · push-refused 0 · gate 1 · compact 0 · limit 0 · idle 1 · workflow 9

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-10-09T17:08:32Z | run-state | phase | 2b26f187f03c | RUNNING | - | - |
| 2026-10-09T17:50:30Z | git | commit | a8023bd7f752 | - | - | DEPL-aBenchedProbe-1 TOOL-aBenchedProbe-1 |
| 2026-10-09T18:06:41Z | run-state | dispatch | TOOL-aBenchedProbe-1 | - | - | - |
| 2026-10-09T18:07:43Z | run-state | brief | TOOL-aBenchedProbe-1 | - | - | - |
| 2026-10-09T18:17:22Z | run-state | dispatch | TOOL-aBenchedProbe-1 | - | - | - |
| 2026-10-09T18:21:35Z | run-state | dispatch | TOOL-aBenchedProbe-1 | - | - | - |
| 2026-10-09T18:26:40Z | git | commit | 894952cb63a0 | - | - | TOOL-aBenchedProbe-1 |
| 2026-10-09T18:26:40Z | run-state | phase | de219c587207 | BUILDING | - | - |
| 2026-10-09T18:35:28Z | run-state | dispatch | TOOL-aBenchedProbe-2 | - | - | - |
| 2026-10-09T18:37:10Z | run-state | brief | TOOL-aBenchedProbe-2 | - | - | - |
| 2026-10-09T19:13:56Z | run-state | dispatch | TOOL-aBenchedProbe-2 | - | - | - |
| 2026-10-09T19:14:16Z | git | commit | e0448998f39e | - | - | TOOL-aBenchedProbe-2 |
| 2026-10-09T19:23:07Z | run-state | dispatch | DEPL-aBenchedProbe-1 | - | - | - |
| 2026-10-09T19:23:41Z | run-state | brief | DEPL-aBenchedProbe-1 | - | - | - |
| 2026-10-09T19:34:30Z | git | commit | 1696d09d4a62 | - | - | DEPL-aBenchedProbe-1 |
| 2026-10-09T19:47:46Z | run-state | dispatch | DEPL-aBenchedProbe-2 | - | - | - |
| 2026-10-09T19:48:14Z | run-state | brief | DEPL-aBenchedProbe-2 | - | - | - |
| 2026-10-09T19:59:36Z | git | commit | 91c34abf72cf | - | - | DEPL-aBenchedProbe-2 |
| 2026-10-09T20:20:49Z | run-state | phase | 91c34abf72cf | REVIEWING | - | - |
| 2026-10-09T23:39:44Z | git | commit | 76ee1a1c257d | - | - | DEPL-aBenchedProbe-3 |
| 2026-10-09T23:46:05Z | run-state | brief | DEPL-aBenchedProbe-3 | - | - | - |
| 2026-10-09T23:47:33Z | run-state | dispatch | DEPL-aBenchedProbe-3 | - | - | - |
| 2026-10-10T01:49:17Z | run-state | phase | 76ee1a1c257d | BUILDING | - | - |
| 2026-10-10T01:55:17Z | run-state | dispatch | DEPL-aBenchedProbe-3 | - | - | - |
| 2026-10-10T04:04:38Z | run-state | dispatch | DEPL-aBenchedProbe-3 | - | - | - |
| 2026-10-10T04:04:39Z | git | commit | bc5e5cf2ad5d | - | - | DEPL-aBenchedProbe-3 |
| 2026-10-10T05:57:51Z | run-state | brief | DEPL-aBenchedProbe-4 | - | - | - |
| 2026-10-10T05:58:30Z | run-state | dispatch | DEPL-aBenchedProbe-4 | - | - | - |
| 2026-10-10T06:00:51Z | run-state | dispatch | DEPL-aBenchedProbe-4 | - | - | - |
| 2026-10-10T06:01:37Z | run-state | dispatch | DEPL-aBenchedProbe-4 | - | - | - |
| 2026-10-10T06:01:38Z | git | commit | a656e35ff1e0 | - | - | DEPL-aBenchedProbe-4 |
| 2026-10-10T06:09:45Z | run-state | phase | a590c95f6bd5 | VERIFYING | - | - |
| 2026-10-10T06:12:10Z | git | merge | dae442565304 | - | - | - |
| 2026-10-10T06:17:39Z | git | merge | c6f40988342f | - | - | - |
| 2026-10-10T07:28:56Z | run-state | phase | a590c95f6bd5 | LANDING | - | - |

## Units

- units: 6 · shown 6 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | TOOL-aBenchedProbe-1 | CLOSED | 2 | 3 | 1 | 894952cb63a0 |
| 1 | TOOL-aBenchedProbe-2 | CLOSED | 1 | 2 | 1 | e0448998f39e |
| 2 | DEPL-aBenchedProbe-1 | CLOSED | 2 | 1 | 1 | 1696d09d4a62 |
| 3 | DEPL-aBenchedProbe-2 | CLOSED | 1 | 1 | 1 | 91c34abf72cf |
| 4 | DEPL-aBenchedProbe-3 | CLOSED | 2 | 3 | 1 | bc5e5cf2ad5d |
| 5 | DEPL-aBenchedProbe-4 | CLOSED | 1 | 3 | 1 | a656e35ff1e0 |

## Decisions

- entries: 20 · shown 20 · aggregated no
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 8
- excluded rows: proposal 0 · rescope 2 · dispatch 13 · review 1 · brief 6 · hold 0 · resume 4
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
| 10 | trailer | 11 |
| 11 | spec-mark | 8 |
| 12 | decision-log | 0 |
| 13 | ledger | 0 |

| # | source | ref | verdict |
|---|---|---|---|
| 1 | review | memory/builds/aBenchedProbe/reviews/2026-10-09-review-TOOL-aBenchedProbe-1-closing-diff-round1.md:14 | CLEAN WITH FIXES |
| 2 | trailer | a8023bd7f752 | - |
| 3 | trailer | a8023bd7f752 | - |
| 4 | trailer | 894952cb63a0 | - |
| 5 | trailer | e0448998f39e | - |
| 6 | trailer | 1696d09d4a62 | - |
| 7 | trailer | 91c34abf72cf | - |
| 8 | trailer | 76ee1a1c257d | - |
| 9 | trailer | bc5e5cf2ad5d | - |
| 10 | trailer | bc5e5cf2ad5d | - |
| 11 | trailer | a656e35ff1e0 | - |
| 12 | trailer | a656e35ff1e0 | - |
| 13 | spec-mark | memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-1.md | - |
| 14 | spec-mark | memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-2.md | - |
| 15 | spec-mark | memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-2.md | - |
| 16 | spec-mark | memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-3.md | - |
| 17 | spec-mark | memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-3.md | - |
| 18 | spec-mark | memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-3.md | - |
| 19 | spec-mark | memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-4.md | - |
| 20 | spec-mark | memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-4.md | - |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-10-09T20:18:02Z | CLEAN WITH FIXES | 0 | CONVERGED |

## Conformance

- items: 10 · shown 10 · aggregated no

| # | item | unit | state |
|---|---|---|---|
| 1 | brief-before-build | DEPL-aBenchedProbe-1 | MET |
| 2 | brief-before-build | DEPL-aBenchedProbe-2 | MET |
| 3 | brief-before-build | DEPL-aBenchedProbe-3 | MET |
| 4 | brief-before-build | DEPL-aBenchedProbe-4 | MET |
| 5 | brief-before-build | TOOL-aBenchedProbe-1 | MET |
| 6 | brief-before-build | TOOL-aBenchedProbe-2 | MET |
| 7 | phases-walked | - | MET |
| 8 | green-at-close | - | MET |
| 9 | keepalive-reaped | - | MET |
| 10 | review-exited | - | MET |

## Anomalies

- anomalies: 12 · shown 12 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | out-of-band-edit | - |
| 2 | out-of-band-edit | - |
| 3 | out-of-band-edit | - |
| 4 | out-of-band-edit | - |
| 5 | refusal-loop | - |
| 6 | killed-verb | - |
| 7 | killed-verb | - |
| 8 | killed-verb | - |
| 9 | destructive-git | - |
| 10 | destructive-git | - |
| 11 | destructive-git | - |
| 12 | idle-gap | - |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 1
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 173 | 0 |
| 3 | gates | present | 1 | 0 |
| 4 | pushes | present | 32 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/aBenchedProbe/RUN.md","run":"1 of 1","start":"d8d21d0e94d2d6c6037b8cf45eaf1cc4d5d7c138","phase":"LANDING","terminal":"no","window":"2026-10-09T17:08:32Z to 2026-10-10T07:28:56Z","window opened by":"git","window closed by":"last-activity","duration":"51624s","own commits":"8","last own commit":"a656e35ff1e0d5be17c16fd8b4d98c0449ee7271","merged":"no","units served":"6","sources present":"7 of 7","owner turns":"launch 1 · pre-run 0 · in-window 4 · post-close 0","usage main":"requests 191 · in 408 · out 110350 · cache-read 79063342 · cache-write 1911653","usage agent":"requests 0 · in 0 · out 0 · cache-read 0 · cache-write 0","usage workflow":"requests 710 · in 1420 · out 483364 · cache-read 101485387 · cache-write 3820057","attributed calls":"835 of 979","values withheld":"0","commitment":"sha256 f3a410fa50834b35475279bb195a6afd9eb644df04302568129af4cb1b22de8e · lines 238"},"tables":[]},
"Timeline":{"facts":{"events":"35 · shown 35 · elided 0","withheld rows":"verb 88 · push 32 · push-refused 0 · gate 1 · compact 0 · limit 0 · idle 1 · workflow 9"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-10-09T17:08:32Z","run-state","phase","2b26f187f03c","RUNNING","-","-"],
["2026-10-09T17:50:30Z","git","commit","a8023bd7f752","-","-","DEPL-aBenchedProbe-1 TOOL-aBenchedProbe-1"],
["2026-10-09T18:06:41Z","run-state","dispatch","TOOL-aBenchedProbe-1","-","-","-"],
["2026-10-09T18:07:43Z","run-state","brief","TOOL-aBenchedProbe-1","-","-","-"],
["2026-10-09T18:17:22Z","run-state","dispatch","TOOL-aBenchedProbe-1","-","-","-"],
["2026-10-09T18:21:35Z","run-state","dispatch","TOOL-aBenchedProbe-1","-","-","-"],
["2026-10-09T18:26:40Z","git","commit","894952cb63a0","-","-","TOOL-aBenchedProbe-1"],
["2026-10-09T18:26:40Z","run-state","phase","de219c587207","BUILDING","-","-"],
["2026-10-09T18:35:28Z","run-state","dispatch","TOOL-aBenchedProbe-2","-","-","-"],
["2026-10-09T18:37:10Z","run-state","brief","TOOL-aBenchedProbe-2","-","-","-"],
["2026-10-09T19:13:56Z","run-state","dispatch","TOOL-aBenchedProbe-2","-","-","-"],
["2026-10-09T19:14:16Z","git","commit","e0448998f39e","-","-","TOOL-aBenchedProbe-2"],
["2026-10-09T19:23:07Z","run-state","dispatch","DEPL-aBenchedProbe-1","-","-","-"],
["2026-10-09T19:23:41Z","run-state","brief","DEPL-aBenchedProbe-1","-","-","-"],
["2026-10-09T19:34:30Z","git","commit","1696d09d4a62","-","-","DEPL-aBenchedProbe-1"],
["2026-10-09T19:47:46Z","run-state","dispatch","DEPL-aBenchedProbe-2","-","-","-"],
["2026-10-09T19:48:14Z","run-state","brief","DEPL-aBenchedProbe-2","-","-","-"],
["2026-10-09T19:59:36Z","git","commit","91c34abf72cf","-","-","DEPL-aBenchedProbe-2"],
["2026-10-09T20:20:49Z","run-state","phase","91c34abf72cf","REVIEWING","-","-"],
["2026-10-09T23:39:44Z","git","commit","76ee1a1c257d","-","-","DEPL-aBenchedProbe-3"],
["2026-10-09T23:46:05Z","run-state","brief","DEPL-aBenchedProbe-3","-","-","-"],
["2026-10-09T23:47:33Z","run-state","dispatch","DEPL-aBenchedProbe-3","-","-","-"],
["2026-10-10T01:49:17Z","run-state","phase","76ee1a1c257d","BUILDING","-","-"],
["2026-10-10T01:55:17Z","run-state","dispatch","DEPL-aBenchedProbe-3","-","-","-"],
["2026-10-10T04:04:38Z","run-state","dispatch","DEPL-aBenchedProbe-3","-","-","-"],
["2026-10-10T04:04:39Z","git","commit","bc5e5cf2ad5d","-","-","DEPL-aBenchedProbe-3"],
["2026-10-10T05:57:51Z","run-state","brief","DEPL-aBenchedProbe-4","-","-","-"],
["2026-10-10T05:58:30Z","run-state","dispatch","DEPL-aBenchedProbe-4","-","-","-"],
["2026-10-10T06:00:51Z","run-state","dispatch","DEPL-aBenchedProbe-4","-","-","-"],
["2026-10-10T06:01:37Z","run-state","dispatch","DEPL-aBenchedProbe-4","-","-","-"],
["2026-10-10T06:01:38Z","git","commit","a656e35ff1e0","-","-","DEPL-aBenchedProbe-4"],
["2026-10-10T06:09:45Z","run-state","phase","a590c95f6bd5","VERIFYING","-","-"],
["2026-10-10T06:12:10Z","git","merge","dae442565304","-","-","-"],
["2026-10-10T06:17:39Z","git","merge","c6f40988342f","-","-","-"],
["2026-10-10T07:28:56Z","run-state","phase","a590c95f6bd5","LANDING","-","-"]]}]},
"Units":{"facts":{"units":"6 · shown 6 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","TOOL-aBenchedProbe-1","CLOSED","2","3","1","894952cb63a0"],
["1","TOOL-aBenchedProbe-2","CLOSED","1","2","1","e0448998f39e"],
["2","DEPL-aBenchedProbe-1","CLOSED","2","1","1","1696d09d4a62"],
["3","DEPL-aBenchedProbe-2","CLOSED","1","1","1","91c34abf72cf"],
["4","DEPL-aBenchedProbe-3","CLOSED","2","3","1","bc5e5cf2ad5d"],
["5","DEPL-aBenchedProbe-4","CLOSED","1","3","1","a656e35ff1e0"]]}]},
"Decisions":{"facts":{"entries":"20 · shown 20 · aggregated no","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 8","excluded rows":"proposal 0 · rescope 2 · dispatch 13 · review 1 · brief 6 · hold 0 · resume 4","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","0"],
["2","abort","0"],
["3","override","0"],
["4","waiver","0"],
["5","handoff","0"],
["6","rescope-retire","0"],
["7","rescope-supersede","0"],
["8","rescope-defer","0"],
["9","review","1"],
["10","trailer","11"],
["11","spec-mark","8"],
["12","decision-log","0"],
["13","ledger","0"]]},
{"name":"entries","header":["#","source","ref","verdict"],"rows":[
["1","review","memory/builds/aBenchedProbe/reviews/2026-10-09-review-TOOL-aBenchedProbe-1-closing-diff-round1.md:14","CLEAN WITH FIXES"],
["2","trailer","a8023bd7f752","-"],
["3","trailer","a8023bd7f752","-"],
["4","trailer","894952cb63a0","-"],
["5","trailer","e0448998f39e","-"],
["6","trailer","1696d09d4a62","-"],
["7","trailer","91c34abf72cf","-"],
["8","trailer","76ee1a1c257d","-"],
["9","trailer","bc5e5cf2ad5d","-"],
["10","trailer","bc5e5cf2ad5d","-"],
["11","trailer","a656e35ff1e0","-"],
["12","trailer","a656e35ff1e0","-"],
["13","spec-mark","memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-1.md","-"],
["14","spec-mark","memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-2.md","-"],
["15","spec-mark","memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-2.md","-"],
["16","spec-mark","memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-3.md","-"],
["17","spec-mark","memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-3.md","-"],
["18","spec-mark","memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-3.md","-"],
["19","spec-mark","memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-4.md","-"],
["20","spec-mark","memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-4.md","-"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-10-09T20:18:02Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"10 · shown 10 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","DEPL-aBenchedProbe-1","MET"],
["2","brief-before-build","DEPL-aBenchedProbe-2","MET"],
["3","brief-before-build","DEPL-aBenchedProbe-3","MET"],
["4","brief-before-build","DEPL-aBenchedProbe-4","MET"],
["5","brief-before-build","TOOL-aBenchedProbe-1","MET"],
["6","brief-before-build","TOOL-aBenchedProbe-2","MET"],
["7","phases-walked","-","MET"],
["8","green-at-close","-","MET"],
["9","keepalive-reaped","-","MET"],
["10","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"12 · shown 12 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","out-of-band-edit","-"],
["2","out-of-band-edit","-"],
["3","out-of-band-edit","-"],
["4","out-of-band-edit","-"],
["5","refusal-loop","-"],
["6","killed-verb","-"],
["7","killed-verb","-"],
["8","killed-verb","-"],
["9","destructive-git","-"],
["10","destructive-git","-"],
["11","destructive-git","-"],
["12","idle-gap","-"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 1","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","173","0"],
["3","gates","present","1","0"],
["4","pushes","present","32","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
