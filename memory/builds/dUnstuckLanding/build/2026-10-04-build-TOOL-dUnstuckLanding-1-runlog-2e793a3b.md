# Run record

**Serves:** journal TOOL-dUnstuckLanding-1..2 TOOL-dUnstuckLanding-12

Rendered from the run model by the runlog kit's `record` command. Every value below is drawn from a closed schema, so no line carries free text. Re-render it rather than edit it.

## Summary

- run-state: memory/builds/dUnstuckLanding/RUN.md
- run: 1 of 1
- start: 2e793a3bc6b7762083020a4812687af9e3513a05
- phase: VERIFYING
- terminal: no
- window: 2026-10-04T08:52:38Z to 2026-10-04T09:40:16Z
- window opened by: git
- window closed by: last-activity
- duration: 2858s
- own commits: 4
- last own commit: 28b23d7a7773afb13fe062ef8bba25b17ed06c68
- merged: no
- units served: 3
- sources present: 7 of 7
- owner turns: launch 1 · pre-run 0 · in-window 0 · post-close 0
- usage main: requests 94 · in 190 · out 139200 · cache-read 34808507 · cache-write 264811
- usage agent: requests 5 · in 10 · out 4695 · cache-read 1022123 · cache-write 23147
- usage workflow: requests 261 · in 522 · out 311022 · cache-read 34946769 · cache-write 1612241
- attributed calls: 392 of 395
- values withheld: 0
- commitment: sha256 def3cb164c7d4393e80e56096acf45e77249c8ef2bde638911e7f03ec6ed8ae1 · lines 42

## Timeline

- events: 12 · shown 12 · elided 0
- withheld rows: verb 19 · push 2 · push-refused 0 · gate 0 · compact 0 · limit 0 · idle 0 · workflow 1

| UTC | source | event | value | phase | rc | more |
|---|---|---|---|---|---|---|
| 2026-10-04T08:52:38Z | run-state | phase | 0c16a66b53c9 | RUNNING | - | - |
| 2026-10-04T08:58:35Z | run-state | brief | TOOL-dUnstuckLanding-1 | - | - | - |
| 2026-10-04T08:59:10Z | git | commit | ac7e375fa3df | - | - | TOOL-dUnstuckLanding-1 |
| 2026-10-04T08:59:10Z | run-state | phase | 2e793a3bc6b7 | RESEARCHING | - | - |
| 2026-10-04T09:07:01Z | run-state | brief | TOOL-dUnstuckLanding-2 | - | - | - |
| 2026-10-04T09:07:44Z | git | commit | 04ebf84abd13 | - | - | TOOL-dUnstuckLanding-2 |
| 2026-10-04T09:07:44Z | run-state | phase | ac7e375fa3df | TESTING | - | - |
| 2026-10-04T09:08:43Z | run-state | phase | 04ebf84abd13 | REVIEWING | - | - |
| 2026-10-04T09:28:32Z | git | commit | 162cb20d3b95 | - | - | TOOL-dUnstuckLanding-12 |
| 2026-10-04T09:31:54Z | run-state | brief | TOOL-dUnstuckLanding-12 | - | - | - |
| 2026-10-04T09:32:37Z | git | commit | 28b23d7a7773 | - | - | TOOL-dUnstuckLanding-12 |
| 2026-10-04T09:38:52Z | run-state | phase | 3b93b1a159a6 | VERIFYING | - | - |

## Units

- units: 3 · shown 3 · aggregated no

| order | unit | status | commits | dispatched | briefed | built |
|---|---|---|---|---|---|---|
| 1 | TOOL-dUnstuckLanding-1 | CLOSED | 1 | 0 | 1 | - |
| 2 | TOOL-dUnstuckLanding-2 | CLOSED | 1 | 0 | 1 | - |
| 3 | TOOL-dUnstuckLanding-12 | CLOSED | 2 | 0 | 1 | - |

## Decisions

- entries: 10 · shown 10 · aggregated no
- trailer near-misses: 0
- decision-log rows the owner's: 0
- spec marks: owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 0
- excluded rows: proposal 0 · rescope 1 · dispatch 0 · review 1 · brief 3 · hold 0 · resume 0
- review rounds: 1 · shown 1 · aggregated no

| # | source | entries |
|---|---|---|
| 1 | decision | 3 |
| 2 | abort | 0 |
| 3 | override | 0 |
| 4 | waiver | 0 |
| 5 | rescope-retire | 0 |
| 6 | rescope-supersede | 0 |
| 7 | review | 1 |
| 8 | trailer | 6 |
| 9 | spec-mark | 0 |
| 10 | decision-log | 0 |
| 11 | ledger | 0 |

| # | source | ref | verdict |
|---|---|---|---|
| 1 | decision | memory/builds/dUnstuckLanding/RUN.md:46 | - |
| 2 | decision | memory/builds/dUnstuckLanding/RUN.md:48 | - |
| 3 | decision | memory/builds/dUnstuckLanding/RUN.md:50 | - |
| 4 | review | memory/builds/dUnstuckLanding/reviews/2026-10-04-review-TOOL-dUnstuckLanding-1-2-closing-diff-round1.md:9 | CLEAN WITH FIXES |
| 5 | trailer | ac7e375fa3df | - |
| 6 | trailer | 04ebf84abd13 | - |
| 7 | trailer | 04ebf84abd13 | - |
| 8 | trailer | 04ebf84abd13 | - |
| 9 | trailer | 162cb20d3b95 | - |
| 10 | trailer | 28b23d7a7773 | - |

| # | UTC | verdict | blockers | exit |
|---|---|---|---|---|
| 1 | 2026-10-04T09:25:49Z | CLEAN WITH FIXES | 0 | CONVERGED |

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

- anomalies: 2 · shown 2 · aggregated no

| # | kind | subclass |
|---|---|---|
| 1 | out-of-band-edit | - |
| 2 | destructive-git | - |

## Coverage

- journal starts: 1 joined of 1 record-creating
- unjoined starts: 0
- sessions: 1 named · 1 extracted
- idle gaps: judged yes · near an owner turn 0
- anomaly kinds: judged 12 of 12

| # | source | state | lines | bad |
|---|---|---|---|---|
| 1 | run-state | present | - | - |
| 2 | driver | present | 38 | 0 |
| 3 | gates | present | 0 | 0 |
| 4 | pushes | present | 2 | 0 |
| 5 | git | present | - | - |
| 6 | transcripts | present | - | - |
| 7 | build-folder | present | - | - |

## Data

```json
{"schema":1,"sections":{
"Summary":{"facts":{"run-state":"memory/builds/dUnstuckLanding/RUN.md","run":"1 of 1","start":"2e793a3bc6b7762083020a4812687af9e3513a05","phase":"VERIFYING","terminal":"no","window":"2026-10-04T08:52:38Z to 2026-10-04T09:40:16Z","window opened by":"git","window closed by":"last-activity","duration":"2858s","own commits":"4","last own commit":"28b23d7a7773afb13fe062ef8bba25b17ed06c68","merged":"no","units served":"3","sources present":"7 of 7","owner turns":"launch 1 · pre-run 0 · in-window 0 · post-close 0","usage main":"requests 94 · in 190 · out 139200 · cache-read 34808507 · cache-write 264811","usage agent":"requests 5 · in 10 · out 4695 · cache-read 1022123 · cache-write 23147","usage workflow":"requests 261 · in 522 · out 311022 · cache-read 34946769 · cache-write 1612241","attributed calls":"392 of 395","values withheld":"0","commitment":"sha256 def3cb164c7d4393e80e56096acf45e77249c8ef2bde638911e7f03ec6ed8ae1 · lines 42"},"tables":[]},
"Timeline":{"facts":{"events":"12 · shown 12 · elided 0","withheld rows":"verb 19 · push 2 · push-refused 0 · gate 0 · compact 0 · limit 0 · idle 0 · workflow 1"},"tables":[{"name":"events","header":["UTC","source","event","value","phase","rc","more"],"rows":[
["2026-10-04T08:52:38Z","run-state","phase","0c16a66b53c9","RUNNING","-","-"],
["2026-10-04T08:58:35Z","run-state","brief","TOOL-dUnstuckLanding-1","-","-","-"],
["2026-10-04T08:59:10Z","git","commit","ac7e375fa3df","-","-","TOOL-dUnstuckLanding-1"],
["2026-10-04T08:59:10Z","run-state","phase","2e793a3bc6b7","RESEARCHING","-","-"],
["2026-10-04T09:07:01Z","run-state","brief","TOOL-dUnstuckLanding-2","-","-","-"],
["2026-10-04T09:07:44Z","git","commit","04ebf84abd13","-","-","TOOL-dUnstuckLanding-2"],
["2026-10-04T09:07:44Z","run-state","phase","ac7e375fa3df","TESTING","-","-"],
["2026-10-04T09:08:43Z","run-state","phase","04ebf84abd13","REVIEWING","-","-"],
["2026-10-04T09:28:32Z","git","commit","162cb20d3b95","-","-","TOOL-dUnstuckLanding-12"],
["2026-10-04T09:31:54Z","run-state","brief","TOOL-dUnstuckLanding-12","-","-","-"],
["2026-10-04T09:32:37Z","git","commit","28b23d7a7773","-","-","TOOL-dUnstuckLanding-12"],
["2026-10-04T09:38:52Z","run-state","phase","3b93b1a159a6","VERIFYING","-","-"]]}]},
"Units":{"facts":{"units":"3 · shown 3 · aggregated no"},"tables":[{"name":"units","header":["order","unit","status","commits","dispatched","briefed","built"],"rows":[
["1","TOOL-dUnstuckLanding-1","CLOSED","1","0","1","-"],
["2","TOOL-dUnstuckLanding-2","CLOSED","1","0","1","-"],
["3","TOOL-dUnstuckLanding-12","CLOSED","2","0","1","-"]]}]},
"Decisions":{"facts":{"entries":"10 · shown 10 · aggregated no","trailer near-misses":"0","decision-log rows the owner's":"0","spec marks":"owner-before 0 · owner-inside 0 · agent-before 0 · agent-inside 0","excluded rows":"proposal 0 · rescope 1 · dispatch 0 · review 1 · brief 3 · hold 0 · resume 0","review rounds":"1 · shown 1 · aggregated no"},"tables":[{"name":"by-source","header":["#","source","entries"],"rows":[
["1","decision","3"],
["2","abort","0"],
["3","override","0"],
["4","waiver","0"],
["5","rescope-retire","0"],
["6","rescope-supersede","0"],
["7","review","1"],
["8","trailer","6"],
["9","spec-mark","0"],
["10","decision-log","0"],
["11","ledger","0"]]},
{"name":"entries","header":["#","source","ref","verdict"],"rows":[
["1","decision","memory/builds/dUnstuckLanding/RUN.md:46","-"],
["2","decision","memory/builds/dUnstuckLanding/RUN.md:48","-"],
["3","decision","memory/builds/dUnstuckLanding/RUN.md:50","-"],
["4","review","memory/builds/dUnstuckLanding/reviews/2026-10-04-review-TOOL-dUnstuckLanding-1-2-closing-diff-round1.md:9","CLEAN WITH FIXES"],
["5","trailer","ac7e375fa3df","-"],
["6","trailer","04ebf84abd13","-"],
["7","trailer","04ebf84abd13","-"],
["8","trailer","04ebf84abd13","-"],
["9","trailer","162cb20d3b95","-"],
["10","trailer","28b23d7a7773","-"]]},
{"name":"rounds","header":["#","UTC","verdict","blockers","exit"],"rows":[
["1","2026-10-04T09:25:49Z","CLEAN WITH FIXES","0","CONVERGED"]]}]},
"Conformance":{"facts":{"items":"5 · shown 5 · aggregated no"},"tables":[{"name":"items","header":["#","item","unit","state"],"rows":[
["1","brief-before-build","-","UNJUDGEABLE"],
["2","phases-walked","-","UNJUDGEABLE"],
["3","green-at-close","-","UNJUDGEABLE"],
["4","keepalive-reaped","-","MET"],
["5","review-exited","-","MET"]]}]},
"Anomalies":{"facts":{"anomalies":"2 · shown 2 · aggregated no"},"tables":[{"name":"anomalies","header":["#","kind","subclass"],"rows":[
["1","out-of-band-edit","-"],
["2","destructive-git","-"]]}]},
"Coverage":{"facts":{"journal starts":"1 joined of 1 record-creating","unjoined starts":"0","sessions":"1 named · 1 extracted","idle gaps":"judged yes · near an owner turn 0","anomaly kinds":"judged 12 of 12"},"tables":[{"name":"sources","header":["#","source","state","lines","bad"],"rows":[
["1","run-state","present","-","-"],
["2","driver","present","38","0"],
["3","gates","present","0","0"],
["4","pushes","present","2","0"],
["5","git","present","-","-"],
["6","transcripts","present","-","-"],
["7","build-folder","present","-","-"]]}]}}}
```
