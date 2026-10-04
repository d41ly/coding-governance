# TOOL-aMendedFleet-7 — a census of the daily held job's red suites by root cause, adding one unit per cause

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-1 · base 7af5f564 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-7-1-held-red-census.md](../build/2026-10-04-build-TOOL-aMendedFleet-7-1-held-red-census.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The owner's goal for the red legs is remote CI green on both jobs, one unit per distinct ROOT CAUSE.
The daily held job reds a different number of suites each day, and several of them visibly share a
cause, so a unit per suite would build the same fix many times and a unit per guess would build the
wrong one. This unit reads the held job's own logs, classifies every red suite by the mechanism that
turns it red, writes that census as a journal, and adds one roster unit per cause no other unit of
this build already owns. It writes no product code: each cause is built by the unit it adds.

## 2. Scope (IN)

- **S1** — The POPULATION is DERIVED at build time and never typed: every job whose name begins
  `held ` and whose conclusion is `failure`, in each of the three most recent COMPLETED scheduled runs
  of the remote CI workflow on `main`, read with `gh run list` and `gh run view --json jobs`. The union
  is the census population, and each suite row records which of the three runs it was red in, so an
  intermittent red is a row with a pattern rather than a suite the newest run happened to miss.
  Observed by AC1.
- **S2** — Each suite row carries its EVIDENCE: the first failing line of that suite's job log, read
  with `gh run view <run> --log-failed` and filtered to the job, plus the file and line the failing
  assertion or traceback names where the log names one. Observed by AC2.
- **S3** — Each suite row carries a CAUSE id `C<n>` and a CLASS, one of `host` (the suite depends on
  a property of the hosted runner that node a's recorded greens do not share: a locale codec, a temp
  root, a clone path, the refs a checkout fetches), `tree` (the suite reds on any host at this tree: a
  stale fixture, a date-relative arm, an inline copy that drifted), `lost` (code a merge dropped) or
  `derived` (the suite reds only because it runs another suite that is red, and its cause is that
  suite's). A suite that cannot be classified from its log and a source read is a row whose cause is
  `UNRESOLVED` with the reason, never a guess. A suite whose log shows more than one mechanism
  carries one cause id per mechanism, each with its own class, so a second cause is never hidden
  behind the first. Observed by AC2.
- **S4** — The CAUSE table: one row per `C<n>`, naming the mechanism in one sentence, every suite it
  explains, and its DISPOSITION — either an EXISTING unit of this build whose write set already
  contains the fix (units 1, 4, 5 and 6 are the candidates the brief names), or a NEW unit. A cause
  is attributed to an existing unit only when that unit's spec names the file the fix lands in; a
  cause that merely resembles one is a new unit. A third disposition, `GREEN-SINCE <run id>`, holds
  only for a cause every one of whose suites passed in the NEWEST census run: it names the commit
  between the two runs' head shas that cleared it where the history names one, and it adds no unit,
  because a unit for a suite already green has no failing case to observe. Observed by AC3.
- **S5** — Each NEW cause is added to the build with
  `bash tools/unattended/unattended.sh --rescope aMendedFleet --act add --item <id> --reason <text>`,
  one call per cause whose reason opens `held-red census cause C<n>`, and a row in the build
  README's authored Units table naming the id, its tier
  and its one-sentence mechanism. The id is the TOOL family's next free sequence at the time of the
  call, derived from the roster and never typed ahead of it. Observed by AC3 and AC4.
- **S6** — The census journal is committed under this build's `build/` folder with the binding line
  `**Serves:** journal TOOL-aMendedFleet-7`, carrying the three run ids and their head shas, the suite
  table of S1 to S3, the cause table of S4, and the liveness line of AC1. Observed by AC1 and AC5.

## 3. Non-goals (OUT)

- Fixing any suite. Every fix is the unit S5 adds, or the existing unit S4 names.
- Running any suite, on this host or any other. Classification reads the CI logs and the source; a
  suite whose class needs a local run to decide is `UNRESOLVED` with that reason, and the unit it
  adds owns the run.
- The three PUSH-bar legs, `transition-audit arms`, `govkit acceptance matrix` and `lexicon wiring`.
  Units 5, 4 and 6 own them, re-observed red on push run 37220352485 at the time of writing.
- Routing the held job's result into the inherited-red HIGH auto-file, which is unit 9, and reporting
  the red streak, which is unit 8.
- Putting any held suite back on the merge bar, which the 2026-08-23 owner ruling forbids.

### Edges

- **consumes-from** external — `gh` authenticated against the public repository, and the scheduled
  runs' logs, which GitHub retains for a bounded period; a run whose log has expired is not a
  census run.
- **consumes-from** `TOOL-aMendedFleet-1` — its spec's files touched, against which S4 attributes a
  cause classed `lost` whose code that unit restores.
- **consumes-from** `TOOL-aMendedFleet-4` — its spec's files touched, against which S4 attributes a
  cause whose fix lands in that unit's matrix module.
- **consumes-from** `TOOL-aMendedFleet-5` — its spec's files touched, for the transition-audit codec
  cause.
- **consumes-from** `TOOL-aMendedFleet-6` — its spec's files touched, for the lexicon conf reader's
  codec cause.
- **hands-off** `TOOL-aMendedFleet-9` — the census journal, as the population that unit's route
  must reach.
- **hands-off** external — each cause S5 adds, whose spec the build's next spec pass authors.

## 4. Design

### Evidence

Read 2026-10-04 at the run's base, PINNED to that date. These are the starting facts a census pass
re-derives, never a substitute for it.

- The remote CI workflow runs on `windows-latest` under Git-Bash, not on Linux: its header says
  every recorded green was earned there. The brief's and the mandate's "Linux" is wrong, and the
  census classes `host` against a hosted Windows runner, not against another OS.
- The red count moves daily. Scheduled run 37196051126 (10-04) red 15 held suites, 37114721791
  (10-03) red 18, and 36996269983 (10-02) red 19. The brief's "18" is the 10-03 figure. The union over
  the three is 19 suite names, which is why S1 takes the union rather than one run.
- The first failing lines of 37196051126 already suggest shared causes, UNVERIFIED as causes:
  - a UTF-8 decode of byte 0x97, the cp1252 em dash, in `codebase-map kit selftest`,
    `govkit selftest`, `row-grammar selftest` and `settings-merge selftest`, and a `charmap` encode
    of a check mark in `runlog selftest`;
  - an inline copy of `resolve_kit_dir` drifted from its canonical source in two memory-tree modules,
    in `python resolver`, which is a tree defect on any host;
  - a cutoff arm in `spec-tokens self-test` whose expected refusal names today's date, and a missing
    conf-example key in `memory-hygiene self-test`;
  - a fixture that cannot clone under the runner's temp root in `manifest-check self-test`, and a
    temp-root exclusion in `process-monitor adopter selftest`;
  - `unattended driver selftest` failing on generated views not re-rendered after an ask is filed,
    which is the function unit 1 restores;
  - `unattended gate selftest shard 2/8` refusing because the clone lacks tips the remote
    advertises, which is the checkout's fetch, a CI configuration fact;
  - `foreign-prefix parity` failing on suites it re-runs, among them `row-grammar selftest` and
    `settings-merge selftest`, which is the `derived` class.

### The census pass

1. Resolve the three run ids: `gh run list --workflow remote-ci.yml --branch main --event schedule
   --status completed --limit 3 --json databaseId,headSha,createdAt`.
2. Per run, list failed held jobs from `gh run view <id> --json jobs` and keep each job's database id.
3. Per run, save `gh run view <id> --log-failed` to the scratchpad, strip CR, and split by the job
   name in its first field. Never read a log through `tail`.
4. Per suite, record the first failing line, then read the source the line names at the run's head
   sha with `git show <sha>:<path>` to decide the mechanism.
5. Group by mechanism into `C<n>` rows and dispose each per S4; for a new cause, run the S5 calls.
6. Write the journal and the roster rows; commit them in one records commit with the unit id in the
   subject and a `Decided:` trailer per attribution to an existing unit.

### Files touched (estimate)

- `memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-7-1-held-red-census.md`
- `memory/builds/aMendedFleet/README.md`
- `memory/builds/aMendedFleet/RUN.md`

## 5. Production-readiness checklist

- security — `gh` reads a public repository's run logs; nothing is written to GitHub and no token
  enters the journal. Logs are quoted one line per suite, which carries no secret the job prints.
- perf / scale — three `gh run view --log-failed` calls, about 800 KB each; seconds.
- error / empty / loading states — an expired log, a run with zero held failures, and a job the log
  does not split out each become a stated line in the journal, never a silent omission.
- observability — the journal is the observation; the roster rows make each cause visible to the run.
- risks — a cause attributed to an existing unit that does not actually fix it leaves a suite red at
  the close; S4's rule that the attributed unit's spec must name the fix's file bounds it.
- testing — AC1 to AC5 are direct reads; no suite runs.
- migration — N/A — no data shape changes.
- user docs — N/A — a build record, not a user-facing feature.

## 6. Acceptance criteria

- **AC1** — When `gh run view <run-id> --repo d41ly/coding-governance --json jobs` runs for each of
  the three run ids the journal names, the number of jobs whose name begins `held ` with conclusion
  `failure` equals the number of suite rows the journal marks red in that run, and the journal's
  liveness line states both numbers for every run.
  Red when: a red suite is missing from the census, the some-not-zero class a bare non-empty check
  passes.
  permission: needs network and an authenticated `gh`.
  figure: DERIVED at observation time from the run's own job list.
- **AC2** — When `git grep -n -E "^\| " -- memory/builds/aMendedFleet/build` runs over the journal's
  suite table, every suite row carries a cause id `C<n>` or `UNRESOLVED` with a reason, a class from
  S3's closed set, and a first failing line quoted from its job log.
  Red when: a row carries no cause, a class outside the set, or an evidence cell that is empty.
- **AC3** — When `grep -c " rescope · item add TOOL-aMendedFleet-[0-9]* · reason held-red census cause " memory/builds/aMendedFleet/RUN.md`
  runs after the pass, it equals the number of cause rows the journal disposes as NEW, and every cause
  row disposed to an existing unit names a file that unit's spec lists under its files touched.
  Red when: a new cause has no unit, or a unit was added for a cause the journal does not list.
- **AC4** — When `git grep -n -F -e <id> -- memory/builds/aMendedFleet/README.md` runs for each id
  the rescope rows of AC3 add, it hits a row inside the authored Units table between the roster
  markers.
  Red when: a cause is recorded in the run-state file and absent from the roster, so no spec pass
  ever reaches it.
- **AC5** — When `python tools/memory-tree/gen_build_index.py --check` runs after the records
  commit, it passes with the journal bound to `TOOL-aMendedFleet-7` by its `**Serves:**` line.
  Red when: the journal is free-named or unbound, which hygiene check 5 or check 21 refuses.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

The census writes records only. The journal path trips the two recall-floor guards, and
`python tools/check-spec-tokens.py --list` over a clone carrying this spec named no other leg.

## 8. Open questions

- **F1** — Does the census decide `host` versus `tree` by running a suite on node a?
  Options: run each red suite locally to see whether it greens here; or classify from the log and a
  source read only, and mark a suite needing a run `UNRESOLVED`.
  RESOLVED (agent, 2026-10-04, delegated): log and source only. The harness forbids any suite inside
  a unit pass, and a suite run here costs hours on node a; the unit a cause adds owns the run.
- **F2** — Is a cause whose mechanism resembles an existing unit's attributed to it?
  RESOLVED (agent, 2026-10-04, delegated): only when that unit's spec names the file the fix lands
  in, per S4. The cp1252 class above spans five kits while unit 4 names one module, so a resemblance
  rule would leave four suites red with their cause marked owned.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft.
- rev-2 · 2026-10-04 · §3 · the Edges handed off to units 1 and 4, both ordered before this one, so
  nothing could be left to them; S4 reads their specs, and those of units 5 and 6, which is a
  consumption. The edges now say so and name all four candidates S4 lists.
- rev-3 · 2026-10-05 · S3, S4 · the census found causes S4's two dispositions could not hold: three
  suites red in the older runs passed in the newest with a clearing commit between, and two suites
  each show two mechanisms. S4 gains `GREEN-SINCE`, which adds no unit, and S3 lets a row carry one
  cause per mechanism. AC3's grep counted every add the run had recorded, fourteen of them before
  this unit, so it could never equal the census's count; it now selects the adds whose reason opens
  `held-red census cause`, the prefix S5's calls write.

## 10. Reuse audit

No existing seam fits: `python tools/codebase-map/reuse_lookup.py "classify failing self-test suites
by root cause from CI logs"` returned name-stem neighbours only (`classify` in the govkit census and
`check-arms.py`, which classify arms and installs, not CI logs). The prior art is a record, not code:
`TOOL-aQuenchedHarness-9` scoped the same per-suite diagnosis on 2026-09-07 and was retired WONTDO to
a backlog row, and `TOOL-dDerivedDocket-76` routes the unattended kit's compensating check to this
held job without noting the job is red. The census reuses the held job's own matrix names as its
suite keys, so no second suite inventory is minted. Where the report and the tree disagree: the
runner is Windows rather than Linux, and the red count is 15, 18 or 19 by day rather than 18.

Recall terms used: `python tools/memory-recall/query.py "how were red held self-test suites triaged
by root cause before" --terms "held suites red triage root cause inherited-red census fixture stale
codec cp1252 remote-ci schedule"`
