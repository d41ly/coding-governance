# TOOL-dTrackedAtlas-1 — one chain build-state derivation, read by the schedule and the Atlas

**Status:** CLOSED · rev-3 · 2026-11-19 · node d · Tier-1 · base 9e21ac76 · streams tooling · ratified 2026-11-19 · records-only · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py](../build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py) | research | — |
| [2026-11-19-build-TOOL-dTrackedAtlas-1-ledger.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-1-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dTrackedAtlas-1-rewrite-map.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-1-rewrite-map.md) | research | — |
| [2026-11-19-build-TOOL-dTrackedAtlas-1-runlog-27295082.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-1-runlog-27295082.md) | journal | TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-10 TOOL-dTrackedAtlas-11 TOOL-dTrackedAtlas-12 TOOL-dTrackedAtlas-18 |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-1-1-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-1-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-1-2-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-2-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-1-3-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-3-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-1-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-brief.md) | research | TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-1-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-build-brief.md) | research | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-1-f2-fold.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-f2-fold.md) | research | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-1-pin-fold.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-pin-fold.md) | research | TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-1-spec-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-spec-brief.md) | research | — |
| [2026-11-19-review-TOOL-dTrackedAtlas-1-2-3-4-diff-review-round1.md](../reviews/2026-11-19-review-TOOL-dTrackedAtlas-1-2-3-4-diff-review-round1.md) | diff-review | TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 |
| [2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md](../reviews/2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md) | diff-review | TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-10 TOOL-dTrackedAtlas-11 |

<!-- /gen:spec-records -->

## 1. Goal

One derivation, read from the tree at a git ref, states every dClosedLoop chain build's actual
state: its spec run, its build run and the merge that landed it, its units, forks, revisions,
deviation records, claim and whether its next run can start. The schedule script's `tree_state`
stops being a second answer and reads it, so the schedule and the Atlas print one landed set, six
at `9e21ac760` where the schedule prints four today.

## 2. Scope (IN)

- **S1** — A new instrument, `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py`,
  whose `derive` returns the state document §4 "Interface" defines, for every build of v2's
  `[chain]`, in row order. Observed by AC2, AC3 and AC4.
- **S2** — The build-run predicate of §4 "The landed predicate": a build run has landed at a ref
  when a run record of that build reads as a build run by README rule 1 at its own `base:` and a
  first-parent merge of the ref carried it. A DEFERRED unit of a landed build run is a carried
  unit, never an unbuilt one. Observed by AC1, AC2 and AC4.
- **S3** — The landing merges of each run, newest one as `landing`, with sha and subject. Observed
  by AC2 and AC4.
- **S4** — The next run of each build under the schedule's Policy J, and its state against the
  cached run claim: done, running, held, stale, startable or waiting. Observed by AC2, AC4 and AC5.
- **S5** — Every read is at the ref through git, bounded, and never the working tree. Observed by
  AC6.
- **S6** — The schedule script reads the derivation: `tree_state`, the `[chain]` parse in `chain`,
  the claim-cache parse in `claims` and the Policy J predecessor lists in `graph` call it, its
  printed output keeps its shape, and `tree_state(ref, ids)` keeps the signature and the
  `(spec done, build done)` tuples
  `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py#derive_sources`
  reads. Observed by AC1, AC4 and AC7.
- **S7** — A CLI, `--ref <rev>` (default `HEAD`) and `--claims cache|none` (default `cache`),
  printing the state document as JSON. Observed by AC2.

## 3. Non-goals (OUT)

- Rendering anything: the Atlas page, its views and its "today" side are `TOOL-dTrackedAtlas-2`'s.
- The page's generation commit, input digest and `--check`, beyond the document's `commit` field.
- Regenerating the page after a landing.
- `tools/policy/check_policy.py#derive_landed_owners`, which carries the same DEFERRED miscount: it
  is under `tools/`, and the build files it as an ask.
- Re-pinning the schedule instrument in `tools/chain-packet.py#INSTRUMENT_BLOBS` or in the chain
  packets: this unit moves that pin, as §7 F2 resolved, and the re-pins are an ask the main loop
  files at the close.
- Any other dClosedLoop instrument, v2's text, any chain build's specs, and the design map.
- Refreshing the claim cache: `unattended.sh --claims` fills it, and this unit only reads it.
- A gate, a suite arm or a self-test: the instrument is a build-folder record, checked by its
  fixture observations.

### Edges

- **hands-off** `TOOL-dTrackedAtlas-2` — renders the state document; this unit renders nothing.
- **hands-off** `TOOL-dTrackedAtlas-3` — the page's commit and input digest; this unit supplies the
  resolved `commit` only.
- **hands-off** external — the ask for `derive_landed_owners` and the one ask for both re-pins §7
  F2's resolution leaves owing, filed by the main loop at the close, outside this unit's write set.

## 4. Design

### Interface

The module is loaded by path, the way dClosedLoop's instruments load each other, because its file
name is not an importable module name:

```python
spec = importlib.util.spec_from_file_location("build_state", <path of S1>)
STATE = importlib.util.module_from_spec(spec); spec.loader.exec_module(STATE)
```

It reads git in `root` (default `.`, a worktree root, as every dClosedLoop instrument is run) and
loads the code it reuses from the repository its own file sits in.

| Name | Kind | Value or signature |
|---|---|---|
| `ROOT` | constant | `"dTrueNorth"`, moved from the schedule |
| `WHOLE` | constant | `frozenset({"dTrueNorth"})`, moved from the schedule |
| `STATUS`, `CARRY` | constants | the schedule's two header patterns, moved unchanged |
| `RUN_STATES` | constant | `("landed", "landed-carrying", "not-landed")` |
| `NEXT_STATES` | constant | `("done", "running", "held", "stale", "startable", "waiting")` |
| `GIT_TIMEOUT` | constant | `120`, seconds, on each git call this file makes |
| `DERIVE_BOUND` | constant | `900`, seconds, the CLI's wall bound |
| `ChainError` | exception | v2's `[chain]` does not hold 22 builds and 509 clauses |
| `StateError` | exception | the ref does not resolve, a git call fails or times out, or a needed conf key is absent |
| `read_chain(ref, root=".")` | function | `{"names", "stage", "parents", "clauses", "rows"}` |
| `derive_predecessors(build, parents)` | function | `{"spec": [...], "build": [...]}`, or `{"build": [...]}` for a `WHOLE` build |
| `read_claims(ref, names, root=".", now=None)` | function | `{slug: claim}` for each slug of `names` the cache holds |
| `derive(ref="HEAD", root=".", claims=True, detail=True)` | function | the state document |

`read_chain` returns `names` as v2's row order, `stage` and `parents` per build as the schedule
parses them today, `clauses` as each row's `cl-` ids, and `rows` as the `[chain]` section text. It
raises `ChainError` carrying the schedule's current message, word for word.

`derive_predecessors` returns run keys, `(kind, slug)` tuples with kind `"spec"` or `"build"`, exactly the
lists the schedule's `graph` builds today: a spec run waits on `("build", ROOT)`, each parent's spec
run (a `WHOLE` parent's build run) and each grandparent's build run; a build run waits on its own
spec run and each parent's build run. A `WHOLE` build has the one key `"build"`, holding the spec
run's list.

A claim is `{"status": str, "node": str | None, "beat_utc": str | None, "stale": bool | None}`,
read from the commit message of `refs/gov/remote/runs/<slug>` as the schedule's `claims` reads it
today. `stale` is `True` or `False` for a `live` claim whose `beat-utc` parses, judged against
`RESUME_STALE_BOUND` in `.unattended.conf` at the ref, and `None` otherwise. A ref the cache does
not hold is absent from the map. `StateError` when the conf at the ref declares no bound.

### Data model

`derive` returns one JSON-serialisable dict, printed by the CLI as `json.dumps(doc, indent=1)`:

| Field | Value |
|---|---|
| `schema` | `1` |
| `ref` | the ref as passed |
| `commit` | the 40-hex commit it resolved to |
| `subject` | that commit's subject line |
| `claims_read` | `true` when the claim cache was read |
| `builds` | one build entry per `[chain]` row, in row order |
| `landed` | slugs whose `build_run.state` is not `not-landed`, in row order |
| `ready` | slugs whose `next.waiting_on` is empty and whose `next.state` is not `done` |
| `startable` | slugs whose `next.state` is `startable` |
| `running` | slugs whose `next.state` is `running` or `held` |

A build entry:

| Field | Value |
|---|---|
| `slug`, `stage`, `parents`, `whole` | from `read_chain`; `whole` is membership of `WHOLE` |
| `spec_run` | `{"done": bool}`, the schedule's current spec-phase rule, moved unchanged |
| `build_run` | `{"state": one of RUN_STATES, "carried": [{"unit", "verb", "ask"}]}` |
| `runs` | one entry per run record at the ref, by first landing, a run with none last: `{"record", "kind", "base", "phase", "landings"}` |
| `landing` | `{"sha", "subject"}` of the newest landing of the newest build-kind run, else `null` |
| `counts` | `{token: n}` over the build's spec headers, `NONE` for a spec with no header |
| `units` | the number of spec files |
| `revisions` | `{unit id: header rev}`; `null` when `detail` is false |
| `forked` | the unit ids whose spec the driver's `plan_state` grades FORKED; `null` when `detail` is false |
| `deviations` | `[{"id", "path", "hand", "risk", "cause"}]`; `null` when `detail` is false |
| `claim` | the build's claim, or `null` when absent or `claims` is false |
| `next` | `{"run": "spec" or "build" or "whole" or null, "waiting_on": ["<kind> <slug>"], "state": one of NEXT_STATES}` |

`carried` lists each DEFERRED spec of a landed build run with the `closes` or `advances` verb its
header tail carries and that verb's id, or `null` for both. `build_run.state` is `landed-carrying`
when that list is not empty.

`next.state` is decided in this order: `done` when the build run has landed; `running` for a `live`
claim with `stale` not `True`; `held` for a `held` claim; `stale` for a `live` claim with `stale`
`True`; `startable` when `waiting_on` is empty; `waiting` otherwise. A claim of any other status
names a past run and decides nothing.

### The landed predicate

A run record is `memory/builds/<slug>/RUN.md` or a rotated `RUN.LANDED.<blob8>.md` beside it, read
at the ref. Its `base:` and `phase:` lines come from its `## Run facts` section. Its `kind` is
README rule 1 at that `base:`, through
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py#derive_run_kind`,
which is the test `tools/unattended/unattended.sh#check_spec_run` applies: an open ask of the build
and a roster unit with no spec at `base:` make a spec run, anything else a build run.

A run's `landings` are the merge commits on the ref's first-parent history whose diff against their
first parent touches the build's `RUN.md` and whose `RUN.md` carries that run's `base:`. One
`git log --first-parent --merges --format=%H%x09%s <ref> -- memory/builds/<slug>/RUN.md` per build
lists the candidates, and one `tools/memory-tree/tree_lib.py#read_blobs_at` batch reads their
`RUN.md` blobs.

The build run has landed when a build-kind record has at least one landing. A build-kind `RUN.md`
on a run branch that never merged has none, so it reads `not-landed`.

Measured at `9e21ac760` on 2026-11-19 with a scratch probe of `derive_run_kind` over all 27 run
records (PINNED): exactly six builds hold a build-kind record, the six that landed. Their newest
landing merges are `2511c1181` dTrueNorth, `3c0318d95` dGroundRules, `3ada42ab1` dSafePassage,
`9760fb746` dOrderedCharter, `0a760477e` dFairHearing and `9e21ac760` dDeclaredLoop, whose earlier
landing `c1f80c002` carries the same `base:`. The other 16 hold only a spec-kind `RUN.md`. The
first-parent history also holds non-merge commits touching `RUN.md`, such as `622a4a9af`, which the
`--merges` filter excludes.

### Reads and bounds

- Spec, run-record and deviation blobs at the ref: one `git ls-tree -r --name-only <ref>
  memory/builds/<slug>/` per build and one `tools/memory-tree/tree_lib.py#read_blobs_at` batch for
  all of them.
- The memory-tree conf at the ref: `tools/memory-tree/gen_build_index.py#read_conf_at_rev`, from
  which the family prefixes, `MEMORY_ROOT` and `FORK_ITEM_CUTOFF` are read. `RESUME_STALE_BOUND` is
  read from `.unattended.conf` at the ref, as the schedule reads it.
- Unit ids: `tools/memory-tree/tree_lib.py#parse_spec_h1`. Header revisions:
  `tools/memory-tree/tree_lib.py#HDR_RE`. Deviation fields:
  `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py#read_record`
  over each `*-deviation-*.md` blob of the build's `build/` folder.
- Forks: each non-terminal spec's blob is written under one `tempfile.TemporaryDirectory`, keeping
  its file name because `plan_state` dates it by name, and graded in one bash run of
  `tools/loop/breakpoints.py#run_sourced`, which sources the unattended driver and has its own
  900 s timeout (tools/loop/breakpoints.py@418b3e8e3a13cfc57e9f248dcc052186d03e9b9c:330).
  A CLOSED or WONTDO spec is not graded: hygiene check 12 already refuses an unresolved §8 there.
- Every git call this file makes passes `timeout=GIT_TIMEOUT` and raises `StateError` naming the
  call when it expires. The reused readers spawn git without a timeout, so the CLI arms a
  `threading.Timer` of `DERIVE_BOUND` seconds that prints `build-state: no answer within 900 s` to
  stderr and exits 2. A library caller such as the schedule arms no timer.

CLI exits: 0 with the document on stdout; 1 on `ChainError`; 2 on `StateError` or the wall bound,
one `build-state: <reason>` line on stderr.

What it does not check: that a merge touching `RUN.md` with a run's `base:` is that run's own
landing, rather than a merge of its branch for another reason; a run record rotated outside the
driver; the open forks of a terminal spec; and claims newer than the last `unattended.sh --claims`.

### The schedule's edit

`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py` loads the
derivation by a path relative to its own file and then:

- binds `ROOT`, `WHOLE`, `STATUS` and `CARRY` to the derivation's objects, because `packet.py` and
  `open.py` read `schedule.WHOLE` and `tools/chain-packet.test.sh` cites
  `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py#CARRY`;
- `chain(ref)` calls `read_chain`, prints the `ChainError` message and exits 1 as it does today;
- `tree_state(ref, ids)` returns `{b: (spec_run.done, build_run.state != "not-landed")}` for each
  `b` of `ids`, from `derive(ref, claims=False, detail=False)`;
- `claims(ref, names)` builds its `(held, other, stale)` from `read_claims`, with its fleet-tag map,
  its messages and its two exits unchanged;
- `graph` takes each run's predecessor list from `derive_predecessors`;
- its docstring's INPUTS paragraph names the derivation as the build-phase rule.

`EXTRA`, `SPEC_ONLY`, `NODES`, `SURFACES`, `git` and the simulation stay where they are.

### Files touched (estimate)

`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py`
`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-ledger.md`

### Alternatives rejected

The build-run predicates weighed are §7 F1. A per-build reader inside the schedule alone was
rejected because the Atlas would then hold a second answer, the defect this unit exists to remove.

## 5. Acceptance criteria

The commands run from a worktree root, with these names set:

```bash
. tools/lib/resolve-python.sh && PY=$(resolve_python)
STATE=memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py
SCHED=memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py
```

- **AC1** — When `"$PY" "$SCHED" --ref 9e21ac760` runs, its first line ends
  `specs done 22, builds landed 6`, the table rows for dSafePassage and dDeclaredLoop read `done`
  in both run columns, and no entry of "runs the owner starts" names either build.
  Red when: `tree_state` keeps the CLOSED-or-WONTDO rule; observed before the change on
  2026-11-19 as `builds landed 4`, with dDeclaredLoop's build run at `a 0-23` and dSafePassage's at
  `d 20-29`.
  figure: PINNED at `9e21ac760`.
- **AC2** — When `"$PY" "$STATE" --ref 9e21ac760 --claims none` runs, it exits 0 and its JSON
  `landed` is dTrueNorth, dGroundRules, dSafePassage, dOrderedCharter, dFairHearing, dDeclaredLoop;
  their `landing.sha` values begin `2511c1181`, `3c0318d95`, `3ada42ab1`, `9760fb746`, `0a760477e`
  and `9e21ac760`; dDeclaredLoop's build-kind run lists `c1f80c002` then `9e21ac760`; and
  `startable` and `ready` are both dPlacedRequest, dWitnessedBar.
  Red when: the predicate is any rejected candidate of §7 F1, for instance `CENSUS_TERMINAL`, which
  reads all 22 landed and none startable.
  figure: PINNED at `9e21ac760`.
- **AC3** — When the same JSON is read, dSafePassage's `counts` is 98 CLOSED, 1 DEFERRED and 1
  WONTDO with `build_run.state` `landed-carrying` and `carried` naming `TOOL-dSafePassage-61`
  `advances` `TOOL-dSafePassage-14`; dDeclaredLoop's is 101, 1 and 1, carrying `TOOL-dDeclaredLoop-34`
  `advances` `TOOL-dDeclaredLoop-35`; dWitnessedBar's is 88 DEFERRED, dPlacedRequest's 63 DEFERRED
  and dTrueNorth's 30 CLOSED; and each build's `deviations` length equals
  `git ls-tree -r --name-only 9e21ac760 memory/builds/<slug>/build/ | grep -c -- '-deviation-'`.
  Red when: a DEFERRED unit of a landed build run is counted as unbuilt, or `carried` drops its verb.
  figure: PINNED at `9e21ac760`.
- **AC4** — When a scratch clone at `%TEMP%/ta1fx` is checked out at `9e21ac760` and a branch that
  rotates `memory/builds/dWitnessedBar/RUN.md` to `RUN.LANDED.00000001.md` and writes a new `RUN.md`
  whose `## Run facts` read `phase: LANDING` and `base: <9e21ac760's full sha>` is merged with
  `git merge --no-ff`, then `"$PY" <worktree>/"$STATE" --ref HEAD --claims none` run in the clone
  names seven `landed` builds, dWitnessedBar's `landing.sha` is that merge, and `startable` is
  dPlacedRequest alone; and `"$PY" <worktree>/"$SCHED" --ref HEAD` there prints
  `builds landed 7`.
  Red when: the same two commands at the clone's `9e21ac760`, before the merge, print six landed
  and two startable, and the schedule `builds landed 6`.
  fixture: the clone is planted by the pass and removed after; the real repository's refs are never
  written.
- **AC5** — When the clone of AC4, before the merge, gets
  `git update-ref refs/gov/remote/runs/dPlacedRequest <commit>` with a message of `status: live`,
  a `node:` line and a `beat-utc:` of now, then `"$PY" <worktree>/"$STATE" --ref HEAD` reads
  dPlacedRequest's `next.state` as `running`, it leaves `startable` while staying in `ready`, and a
  `beat-utc:` older than `RESUME_STALE_BOUND` reads `stale`.
  Red when: `--claims none` over the same clone, which reads it `startable`.
- **AC6** — When a spec of the clone's working tree is edited and left uncommitted, for instance
  `TOOL-dDeclaredLoop-34`'s status flipped to `OPEN`, the JSON of `--ref 9e21ac760 --claims none`
  compares equal under `cmp` to the one taken before the edit.
  Red when: a reader reads the working tree, which a staged swap of one `git show` for a file read
  shows by moving `counts`.
- **AC7** — When the call shape of `derive_sources` in
  `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py` is made directly,
  loading `"$SCHED"` and calling `tree_state("9e21ac760", {"dDeclaredLoop": [], "dWitnessedBar": []})`, it returns
  exactly those two keys, `(True, True)` and `(True, False)`.
  Red when: `tree_state` returns the derivation's document, or keys outside the `ids` it was given.

## 6. Gates

The close runs the plain bar once, which holds the guarded legs of the `selftests` chunk below as
on-demand legs, so they do not run there. Because §7 F2 resolved to editing the schedule in place,
`chain-packet self-test` will red its CP3, CP4 and CP5 arms on the next bar run with
`GATE_SELFTESTS=1` until the door's constant and the owner's `packet.py --repin` re-pin the schedule,
the one ask the main loop files at the close.

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `chain-packet self-test` · `policy fixtures`

## 7. Open questions

- **FACT-QUESTION · F1 — Which predicate says a chain build's build run has landed?** Probe: each
  candidate evaluated over the 22 chain builds at `9e21ac760`. Deciding observation: the candidate
  reads exactly the six landed build runs. Liveness: the probe can produce a negative, as the
  candidates below that fail it show.
  (a) Every spec CLOSED or WONTDO, the schedule's `tree_state` today. Rejected: it reads four,
  missing dSafePassage and dDeclaredLoop, whose one DEFERRED unit each was carried forward.
  (b) `tools/memory-tree/tree_lib.py#CENSUS_TERMINAL`, DEFERRED counted done. Rejected: it reads all
  22, because a spec run carries every unit forward as DEFERRED (PLAY-dClosedLoop-2).
  (c) Every DEFERRED spec carries a `closes` or `advances` verb. Rejected: dWitnessedBar's 88
  spec-run carries all carry `advances`, so all 22 read landed.
  (d) At least one CLOSED spec. Rejected: dWellOiledMachine holds one and dRankedPlan two, built
  inside their spec runs, so eight read landed.
  (e) A `-departures-build.md` report in the build folder. Rejected: only dGroundRules and dTrueNorth
  hold one.
  (f) The `phase:` of the live `RUN.md`. Rejected: dSafePassage's landed build run reads `LANDING`,
  and so do the 16 spec runs.
  (g) A build-kind run record by README rule 1 with a first-parent landing merge. Reads exactly the
  six, with the merges §4 lists.
  RESOLVED (agent, 2026-11-19, delegated): (g), the observation above.
- **F2 — The schedule edit moves the schedule instrument's pinned blob. Which way does the unit
  take?** `tools/chain-packet.py#INSTRUMENT_BLOBS` pins the schedule at
  `5aa5421e265b02ba4478f8860ad9a4f5fea94500`, and every chain packet pins it too
  (`memory/builds/dWitnessedBar/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md` is one).
  Any byte change moves it. `tools/chain-packet.test.sh@6b7a4d274a6ffe0ea97b2caa1516ec57b4a2c43b:28`
  says CP3, CP4 and CP5 then fail; the door falls back to the instrument, slower and with the same
  output. `packet.py --check` reds each packet's pin arm, and
  `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py@cab3bff165a1bb61a5854f58d350912e79a7b34b:46`
  says the `--repin` that clears it admits only an owner at a console inside a chain run.
  (a) Edit the schedule as §4 states. The owner's acceptance, "the schedule script prints builds
  landed 6", holds. The main loop files one ask at the close for both re-pins: the door's constant,
  with its reliance points re-read because `tree_state` stops calling `schedule.git` per path, and
  the owner's `packet.py --repin` of the schedule instrument.
  (b) Leave the schedule's bytes alone and run its `main` through a door in this unit's file that
  rebinds `tree_state`, as `tools/chain-packet.py` rebinds `schedule.git`. No pin moves, but the
  schedule run directly still prints `builds landed 4`, which fails the owner's acceptance, and
  `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py#derive_sources`
  keeps reading parents as unbuilt.
  (c) Edit the schedule and re-pin both in this build. Refused: the door is under `tools/`, which
  owes a `GATE_SELFTESTS=1` bar the owner ruled out for this run, and the packet re-pin is the
  owner's.
  (a) is the only option that meets the owner's acceptance inside the build's rules; it trips none
  of M3's vetoes, since the schedule is an instrument, not a governance carrier, and nothing under
  `tools/` moves; its cost is one owner re-pin and one ask.
  RESOLVED (agent, 2026-11-19, delegated): (a), the only option meeting the owner's acceptance; the
  re-pins are filed as one ask at the close.

## 8. Revision log

- rev-1 · 2026-11-19 · initial draft.
- rev-2 · 2026-11-19 · §3 · §6 · §7 · F2 resolved to (a), the schedule edited in place, under the
  mandate's delegated authority; folded from 2026-11-19-prompt-TOOL-dTrackedAtlas-1-f2-fold.
- rev-3 · 2026-11-19 · §2 · §4 · §5 · §7 · §9 · the pass legs' reds after `390c2bc05`, folded from
  2026-11-19-prompt-TOOL-dTrackedAtlas-1-3-spec-writer: the interface function `predecessors` is
  renamed `derive_predecessors`, whose leading token is a declared verb, in the interface table,
  its prose and the schedule's edit, and the built code is renamed by the main loop's inline red fix
  in the same commit; the breakpoints timeout figure is pinned on its line; and each symbol cited
  by a bare basename now gives its repository-relative path. No other design change.

## 9. Reuse audit

The seams extended: the schedule's own `tree_state`, `chain`, `claims` and `graph`, whose rules move
into the derivation.
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py#derive_run_kind`
answers the run kind, the test `tools/unattended/unattended.sh#check_spec_run` applies.
`tools/memory-tree/tree_lib.py#read_blobs_at` reads every blob at the ref.
`tools/memory-tree/gen_build_index.py#read_conf_at_rev` reads the conf at the ref.
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py#read_record`
parses deviation records, and `tools/loop/breakpoints.py#run_sourced` runs the driver's `plan_state`.
`python tools/codebase-map/reuse_lookup.py "derive whether a build run landed from run records at a git ref"`
ranked only name-stem helpers (`run`, `git`, `build`, `records`, `run_git`), no reader of a chain
build's state. Seams read and not taken: `tools/unattended/lib-unattended.sh#read_landing_commit`
derives a landing from HEAD's working copy, not at a ref; `tools/loop/position.py` derives one build's step inside
its own run; `DEPL-dShippedRelease-49` specs a parent-landed reading for a chain build not yet built.
The recall probe returned PLAY-dClosedLoop-2 (a spec run carries every unit forward), the ask
PLAY-dClosedLoop-37 and TOOL-dTrueNorth-7, the unit behind `check_spec_run`.

Recall terms used: `python tools/memory-recall/query.py "how is a chain build's build run known to have landed when a unit is carried forward DEFERRED" --terms "dClosedLoop schedule tree_state landed DEFERRED carry-forward spec-run build-run run-kind RUN.LANDED rotation landing-merge"`
