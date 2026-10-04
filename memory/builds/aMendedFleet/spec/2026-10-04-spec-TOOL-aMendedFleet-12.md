# TOOL-aMendedFleet-12 — LIVE.md carries each build's last record date and splits ACTIVE from DORMANT

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 12

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`memory/LIVE.md` lists every build with a non-terminal unit, and nothing in it says which of them
anyone is still working on: 20 of its 23 rows carry no record dated within 21 days of the newest
record in the tree, PINNED, measured 2026-10-04 by the probe in §10. This unit adds a `Last record`
column, derived from dates the build's own tracked records already carry, and an `Activity` column
that reads `active` or `dormant` against a declared `LIVE_DORMANT_DAYS`, with active rows first, so a
reader of the one generated work-state file can tell live work from parked work.

## 2. Scope (IN)

- **S1** — A build's last record date is the newest of four dates the generator already reads: every
  unit's spec status-header date, the leading date of every tracked record filename under
  the build's record folders, the `filed` date of every ask whose home is the build's `BACKLOG.md`
  under `BACKLOG_MODE=builds`, and the front matter's `opened`. No git history, no clock and no file
  read beyond what the generator reads today. Observed by AC1, AC2 and AC3.
- **S2** — The anchor is the newest last record date across EVERY build, terminal ones included. A
  build is `dormant` when its last record date is more than `LIVE_DORMANT_DAYS` days before the
  anchor, and `active` otherwise, the boundary day itself counting as active. Observed by AC3.
- **S3** — With `LIVE_DORMANT_DAYS` set, `LIVE.md` stays ONE table, gains two trailing columns,
  `Last record` and `Activity`, orders its rows active first and then dormant, each by slug, and opens
  with one sentence naming the threshold, the anchor date and the build that set it. Observed by AC1
  and AC6.
- **S4** — `LIVE_DORMANT_DAYS` blank, or undeclared, renders `LIVE.md` byte-identical to today's
  render. A value that is not a positive integer is refused with a named error before any artifact
  is written. Observed by AC4 and AC5.
- **S5** — This repo declares `LIVE_DORMANT_DAYS="21"` in `.memory-tree.conf`, the kit's
  `.memory-tree.conf.example` declares it blank with a comment saying blank renders today's file, and
  `memory/LIVE.md` is re-rendered. Observed by AC1 and AC7.
- **S6** — The generator's module docstring, whose third source is the tracked file list "for the
  ROSTER only", says the list now also dates the build, and the kit README's row for the generator
  names the two columns and the key. Observed by AC7.
- **S7** — Three `--selftest` arms in the generator: the commit-date fixture pair, the four-build
  boundary fixture and the blank-key byte comparison. Observed by AC2, AC3 and AC4.
- **S8** — `memory/map/generated/symbols.json` is regenerated for the new
  definitions. NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at
  the close is its check, and §7 names the leg that reads it.

## 3. Non-goals (OUT)

- Git history as a source. §4's alternatives record the two git candidates and the tests that
  rejected them.
- The run-state file `RUN.md` and any record outside the build's record folders. An unattended run
  writes dated recordings with every pass, so its activity reaches S1 without them.
- The month shards under `memory/ledger/`; they keep today's columns. Unit 22 owns their shape.
- A drift signal over the same reading. `live_builds_without_activity` is unit 54's.
- The LANDED-UNCLOSED column, which is `TOOL-aMendedFleet-13`.
- Retiring, deferring or otherwise acting on a dormant build. The column reports; it decides nothing.
- The memory-tree kit version bump, owed once at this build's close after the last move.

### Edges

- **hands-off** `TOOL-aMendedFleet-13` — the column it appends goes after the two this unit adds.
- **hands-off** `TOOL-aMendedFleet-54` — a drift signal for live builds without activity, which may
  read the dormant rule this unit renders rather than defining a second one.
- **hands-off** external — the memory-tree kit version bump, owed once by this build's close.

## 4. Design

### Evidence

Read at base `7af5f564`, re-verified 2026-10-04 at `6a88fbf7`, whose `tools/` bytes equal base.

- `render_live` in `tools/memory-tree/gen_build_index.py` renders one table, `| Build | Status |
  Node | Opened | Streams | Ids (n) |`, over the builds whose derived status is not terminal, in
  `collect` order.
- `collect` already holds every input S1 names: each unit's parsed header carries `date`; each build's
  `docs` list is its tracked record files; `read_backlog` parses every ask with its `filed` date; and
  `fm["opened"]` is required front matter. S1 therefore costs no spawn and no read.
- The module docstring states FOUR SOURCES and "No git history and no mtimes", and gives the reason:
  a source the renderer does not read cannot make the render drift. S1 keeps that sentence true.
- One reader parses `LIVE.md`: `skills/session-kickoff/manifest-check.sh` counts table rows that are
  not separator rows and subtracts one header. A second table would add a header and miscount, which
  is why S3 keeps one table. No code reads the columns by position; `git grep` over `tools/`,
  `skills/` and `.githooks/` finds no other reader.

### Data model

```
| Build | Status | Node | Opened | Streams | Ids (n) | Last record | Activity |
| [<slug>](builds/<slug>/README.md) | <status> | <node> | <opened> | <streams> | <n> | <last-touch date> | active|dormant |
```

The opening sentence, rendered only with the key set: `Dormant: no record dated within <N> days of
<anchor>, the newest record date in this tree (<slug>).` The anchor's slug is the alphabetically
first build carrying that date, so the sentence is a pure function of the tree.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `derive_last_record` | function: a build and its asks in, a date out | `py.function`, verb `derive` |
| `LIVE_DORMANT_DAYS` | conf key, `.memory-tree.conf` | conf key; blank means off |

`render_live` gains the conf and the backlog reading as parameters; `plan` already holds both. A name
the lexicon leg refuses is replaced with its `--suggest` answer at build time, and this table is
amended with a rev bump.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/README.md`
- `tools/memory-tree/.memory-tree.conf.example`
- `.memory-tree.conf`
- `memory/LIVE.md`
- `memory/map/generated/symbols.json`

### Rollout

Dark by key. An adopter's `LIVE.md` is unchanged until it declares `LIVE_DORMANT_DAYS`; this repo
declares it in the same commit that re-renders its `LIVE.md`.

### Alternatives rejected

Three candidates differing in mechanism were tested against the live tree on 2026-10-04 with the two
scratch probes §10 names.

- **C1, the report's: one `git log --name-only` pass over the build folders, excluding sweep commits
  that touch more than K build folders.** Lost on two tests. Truth: at K=3, four of the 23 live rows
  take their date from a commit of another build or of the kit, among them `bConvergentLodestar`
  dated 2026-09-22 by a dGatedProse commit and `aWeighedCanon` dated 2026-09-05 by an aJoinedCanon
  one. At K=2 both of those remain, the first from a one-folder commit no K can exclude, and at K=7
  ten rows move to 2026-09-22. Three rows had no non-sweep touch at all. Consistency: the generator renders BEFORE the commit it rides
  in exists, so a render that reads the log cannot see that commit and `--check` reds on the next
  commit touching a build. Repairing it needs a pending-change rule, a second spawn, author dates
  rather than committer dates, and still reds across midnight and on partial staging.
- **C2: C1 counting only commits whose subject names the slug.** Excludes the foreign sweeps, and
  loses the consistency test outright: the render cannot read the subject of a commit not yet
  written.
- **C3, chosen: the dates the build's own records carry.** Passes both tests. Its blind spot is an
  edit that moves no dated field, which the spec header rule already forbids for a material change.
  On every other row C1 dated, C3 agreed within one day.
- **A wall-clock anchor.** `LIVE.md` would go stale with no commit as a build crossed the threshold,
  and the freshness check would red a tree nobody touched.
- **Two tables, Active and Dormant.** Miscounts the kickoff card's row reader by one header.

## 5. Production-readiness checklist

- security — N/A — a read-only render over tracked records.
- perf / scale — no spawn and no file read added; one pass over values already in memory.
- error / empty / loading states — a build with no dated record falls back to `opened`, which is
  required front matter, so the cell is never empty; a tree with no live build renders today's
  `*No live build.*` line and no sentence.
- observability — the opening sentence names the threshold, the anchor and the build that set it, so
  a mistyped future date is visible on the first line it distorts.
- risks — a mistyped future date in one record moves the anchor and marks every other build dormant;
  the sentence names the build that set it. A record dated in the past, such as a backfilled review,
  can make a build read as dormant while it is worked; the next pass's spec header date corrects it.
- testing — the three `--selftest` arms of S7 and direct calls on the live tree.
- migration — N/A — a rendered file; `--write` regenerates it.
- user docs — the kit README's generator row and the example conf comment, S5 and S6.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --write` runs on the live tree and
  `memory/LIVE.md` is read, its header row ends `| Last record | Activity |`, every build row carries a
  date and `active` or `dormant`, no `dormant` row precedes an `active` one, and the
  `aMendedFleet` row reads `active`.
  Red when: a row lacks either cell, the order interleaves, or this build reads dormant on its own
  opening day.
  figure: the active and dormant counts are DERIVED at observation time; at writing, 3 and 20.
- **AC2** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, an arm renders two
  fixture trees holding the same tracked bytes, committed with author and committer dates a year
  apart, and asserts their two `LIVE.md` renders are identical.
  Red when: the render reads git history or the clock.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, an arm over a fixture
  of four builds with `LIVE_DORMANT_DAYS` 21 asserts: the anchor is the newest date among a spec
  header, a record filename and an ask's `filed` date, each the newest in one build; a build exactly
  21 days older reads `active`; a build 22 days older reads `dormant`; and a build with no dated
  record shows its `opened` date.
  Red when: a date source is ignored, the boundary is off by one, or a cell is empty.
- **AC4** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, an arm over a fixture
  with `LIVE_DORMANT_DAYS` blank asserts the `LIVE.md` render equals the render of today's
  `render_live` for the same builds, byte for byte.
  Red when: a blank key changes one byte of the file.
- **AC5** — When `LIVE_DORMANT_DAYS` in `.memory-tree.conf` is staged as `abc`, then as `0`, and
  `python tools/memory-tree/gen_build_index.py --check` runs after each, each exits non-zero with a
  line naming the key and writes nothing; restoring the value restores the clean run. These two
  edits are the staged breaks for S4's refusal.
  Red when: either value renders a file or exits 0.
- **AC6** — When `awk '/^\|/ && !/^\|[-|: ]*$/ {n++} END{print n-1}' memory/LIVE.md` runs, the
  kickoff card's own row arithmetic, it prints the number of rows `grep -c '](builds/' memory/LIVE.md`
  counts.
  Red when: the render adds a second header row or a second table.
- **AC7** — When `grep -n "LIVE_DORMANT_DAYS" tools/memory-tree/README.md tools/memory-tree/.memory-tree.conf.example .memory-tree.conf tools/memory-tree/gen_build_index.py`
  runs, each file reports at least one hit, the example conf's value is blank and this repo's is 21,
  and the generator's docstring line for the tracked-file source no longer reads "for the ROSTER
  only" alone.
  Red when: a carrier omits the key, or the docstring still claims the list feeds the roster only.

## 7. Gates

`build-index selftest` · `build README slot contract` · `memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py --selftest · two fixture trees a year apart in commit dates, and a four-build boundary fixture · none

## 8. Open questions

- **F1** — Which dates make a build's last touch?
  Options: C1, git log with a sweep cut at K; C2, git log keyed on the subject; C3, the dates the
  build's records carry. §4 records the two tests and the rows each candidate got wrong.
  RESOLVED (agent, 2026-10-04, delegated): C3. It is the only candidate that passes both tests, and
  it keeps the generator's no-history contract.
- **F2** — What is the dormancy measured against?
  Options: the wall clock; the HEAD commit's date; the newest record date in the tree. The first goes
  stale untouched, the second needs a spawn and reds across the commit it rides in.
  RESOLVED (agent, 2026-10-04, delegated): the newest record date across every build.
- **F3** — What value does this repo declare?
  Options: 14, 21 or 28 days. On 2026-10-04 every value from 13 to 28 splits the 23 rows the same
  way, 3 active and 20 dormant, and 21 is more than twice the 9.1-day p90 the report measured from a
  build's opening to its last real touch.
  RESOLVED (agent, 2026-10-04, delegated): 21.
- **F4** — One table or two?
  Options: an Active table and a Dormant table; one table with an `Activity` column, active rows
  first. Two tables miscount the kickoff card's reader.
  RESOLVED (agent, 2026-10-04, delegated): one table.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `render_live`, `collect` and the three-candidate probe on
  the live tree.
- rev-2 · 2026-10-04 · §2 S8 · §4 · §7 · M2 cross-read: the definitions this unit adds
  move `memory/map/generated/symbols.json`, which `TOOL-aMendedFleet-82` and the build's other
  code units regenerate and declare; this spec omitted the write, its Files touched row and the leg.
  §5 testing also says three self-test arms, as S7 does; it said two.

## 10. Reuse audit

The seam extended is `render_live` in `tools/memory-tree/gen_build_index.py`, fed by values `collect`
and `read_backlog` already hold: each unit's header `date`, each build's `docs`, each ask's `filed`.
`python tools/codebase-map/reuse_lookup.py "derive when a build was last worked on and mark idle
builds dormant"` returned name-stem neighbours only and no recency helper, so no existing seam
computes a last-touch date; the derivation is new and sits beside the render. Recall returned the
report rows and `TOOL-aFoldedQuarry-4`, the decision that made build status a derived render, which
this unit extends rather than reopens. The candidate test used two scratch probes over the live tree:
one `git log --no-renames --name-only` pass over `memory/builds/` with K varied over 2, 3 and 7, and a
read of the four record date sources. Where the report and the tree disagree: the report's "about 15
of 22 rows idle 29 days or more" is now 20 of 23 dormant at 21 days by record dates, and its proposed
mechanism, the git log pass, misdates five rows at its own K.

Recall terms used: `python tools/memory-recall/query.py "was a last-touch or dormant column for
LIVE.md or idle builds considered before" --terms "LIVE.md last-touch dormant idle builds
gen_build_index render_live git log mtimes generated index status derived"`
