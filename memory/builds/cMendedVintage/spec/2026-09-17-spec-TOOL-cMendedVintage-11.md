# TOOL-cMendedVintage-11 — the census arm resolves its launcher instead of trusting the name

**Status:** SPECCED · rev-1 · 2026-09-17 · node c · Tier-2 · base 859daa67 · streams tooling · order 36

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-prompt-TOOL-cMendedVintage-11-2-build-brief.md](../prompts/2026-09-17-prompt-TOOL-cMendedVintage-11-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`test_live_tree_dies_completely` launches its process tree through a bare `bash`. On node `c` that
name resolves to WSL, whose processes the Windows census cannot enumerate, so the arm walks two
irrelevant rows and reports the tree as surviving. The product is correct — forcing the resolved Git
Bash makes the untouched census walk seven processes, reach the native grandchild and kill all seven.
The arm must resolve its launcher by RUNNING a candidate, as this repo already does for `python`,
and must assert the members it staged rather than a count anything can satisfy.

## 2. Scope (IN)

- **S1** The arm resolves its launcher: each candidate is RUN and accepted only if it answers as the
  POSIX shell whose process the census can see. A name found on `PATH` is not evidence, which is the
  whole lesson `tools/lib/resolve-python.sh` records for a different interpreter. Observed by AC1.
- **S2** An unresolvable launcher is a self-announcing SKIP naming what it looked for, never a pass
  and never a silent green. A node with no such shell cannot run this arm, and saying so is the only
  honest verdict available there. Observed by AC3.
- **S3** The arm asserts the MEMBERS it staged — the nested shell, the sleeps and the native python
  grandchild — rather than a bare count. A `>= 4` threshold is satisfiable by launcher plumbing, and
  a green earned that way is the class this arm exists to disprove. Observed by AC2.
- **S4** The cleanup probe reads the same resolved launcher. Today it shells out through a bare
  `bash` too and cannot see a WSL tree, so the strays it checks for only ever die because tearing
  down the launcher tears down the session. Observed by AC4.

## 3. Non-goals (OUT)

- No change to `tools/process-monitor/census.py`, `scope.py` or `reap.py`. All three are measurably
  correct on this node under a resolved launcher, and the defect is entirely in the fixture.
- No raising of the arm's wait. At twenty seconds it flips green while counting `conhost.exe` and
  `wslhost.exe` with zero members of the staged tree, which is a worse defect than the red it
  replaces and is the reason this unit exists rather than a one-line patch.
- No waiver row. The condition is reproducible, understood and node-local rather than transient, and
  a waiver would retire the only arm that grades the kit's whole reason for existing.
- No new shared resolver in `tools/lib/`. One kit's test fixture is not a second caller of the python
  launcher problem; if a second kit needs this, that is when it becomes a helper.

### Edges

- **hands-off** external — the merge bar stops carrying a red this node can never clear; nothing in
  this build reads the arm.

## 4. Design

The census enumerates Windows processes. A WSL process is not one, so a tree launched under WSL is
invisible to it and the arm's re-read finds nothing to have died. The arm never noticed because it
asserted a COUNT and a count of two is not obviously wrong.

Resolution is by execution, not by lookup. The candidate is run and its answer inspected; a candidate
that is present, answers, and is nevertheless the wrong kind of shell must fail the test. The
recorded precedent is `tools/lib/resolve-python.sh`, which runs each candidate because the MS-Store
`python3` stub answers `command -v` and exits 9009 — the same shape with a different binary.

WHY THE MEMBER ASSERTION IS PART OF THE FIX rather than a tidy-up. With a count, the twenty-second
run is green and wrong; with the members named, that run is red and says which member is missing. The
count is what let a launcher-plumbing green look like a passing test, so replacing it is what stops
the next environment difference doing this again.

## 5. Production-readiness checklist

- security — none. The arm launches and kills processes it created under a name it staged, and the
  resolution narrows which binary it launches rather than widening it.
- perf / scale — one extra candidate execution per arm run, on an arm that already sleeps three
  seconds. No new process in the tree under test.
- error / empty / loading states — a node with no resolvable launcher takes S2's announced skip; a
  node where the tree partially appears now reds naming the missing member instead of passing on a
  count.
- observability — the skip and the red both name what they looked for, which is what makes a green
  row on another node readable rather than assumed.
- risks — the real risk is a resolution that accepts the wrong shell and restores the silent green
  under a new spelling. `AC1` is written against the members, not the resolution, so an accepted
  wrong shell still reds.
- testing — `AC1` to `AC4` are runs of the arm itself on this node, where the failing case is the
  current shipped behaviour and needs no staging.
- migration — none. No shipped product file changes and no adopter receives anything new.
- user docs — none owed. The kit README describes what the monitor does, not how its own arm launches
  a fixture.

## 6. Acceptance criteria

- **AC1** — When `test_live_tree_dies_completely` runs on this node after the change, it reports the
  staged tree walked and killed, with its own report naming every member. Red when: the launcher
  still resolves to WSL, in which case the census walks rows belonging to no staged member and the
  arm's tuple stays `(False, [], [])`.
- **AC2** — When the tree is staged with one member prevented from starting, `the missing member` is
  named in the arm's red. Red when: the assertion is still a bare count, which launcher plumbing
  satisfies — the twenty-second measurement is the evidence that this is reachable.
- **AC3** — When no launcher resolves, the arm prints a line whose head is the literal word `SKIP`
  naming what it looked for, and does not report a pass. Red when: an unresolvable launcher falls
  through to the existing platform skip and reads as coverage.
- **AC4** — When the arm completes, its cleanup probe reports through the resolved launcher and names
  any `stray` it found. Red when: the probe still shells through a bare `bash` and reports clean over
  a tree it cannot see.

## 7. Gates

`process-monitor census selftest` · `process-monitor adopter selftest`

New arm: `tools/process-monitor/selftest.py` · the repaired `test_live_tree_dies_completely`, plus
the member assertion S3 replaces its count with and the announced skip S2 adds · no assertion floor
moves, because the adopter suite beside it gains and loses no assertion.

## 8. Open questions

- **Q1 — should the resolution be shared with the adopter script, which has the same exposure?**
  RESOLVED (agent, 2026-09-17, delegated): not here. The adopter runs on the operator's own shell by
  design and its exposure is a different question from a test fixture staging a tree it must then
  see. §3 records why no `tools/lib/` helper is minted for one caller.

## 9. Revision log

- rev-1 · 2026-09-17 · initial draft, authored mid-build by the main loop after the full bar returned
  RED and a read-only attribution pass measured the leg failing identically at BASE and at HEAD.
  Adopted because the leg blocks this run's own landing, not because the defect belongs to it.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resolve a shell launcher by running the candidate rather than trusting the name"`
returns one seam and it is the right precedent rather than a reusable function:
`tools/lib/resolve-python.sh` resolves a python launcher by RUNNING each candidate, for exactly this
reason, and its header records the MS-Store stub that answers `command -v` and exits 9009. NO
EXISTING SEAM FITS as code — it resolves python, is shell rather than the fixture's own language, and
this repo's kit rule forbids a kit file naming a sibling kit by literal. What it supplies is the
DISCIPLINE, which §4 cites as the precedent.

Recall terms used: process-monitor census winpid live tree WSL Git-Bash launcher resolve candidate
selftest arm green-by-absence node-local.
