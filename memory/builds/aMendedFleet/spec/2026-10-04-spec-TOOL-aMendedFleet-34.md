# TOOL-aMendedFleet-34 — recall measures offline whether an answer was used, from the query log and the worktree's next commit

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · closes TOOL-aWeighedCompass-11 · order 34

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

The recall kit logs every query and the top result ids it returned, and the only outcome signal is
`--opened`, which callers almost never record by hand, plus the hook's inferred first read. This unit
adds an offline measure: `query.py --used` joins each logged query's result ids to the ids the
worktree's NEXT commit cites, in its message or in the lines it adds (a spec it writes included), and
reports how many answers were used and at which rank. No hook changes and nothing is written. It
supersedes the ask to widen the opened hook, as the review's plan says.

## 2. Scope (IN)

- **S1** — `query.py` gains a bare `--used` flag, declared in its closed flag tables and usage block.
  It needs no index, so it runs before the cache is built, and it writes nothing: no log row, no
  cache, no file in the worktree. Observed by AC1, AC4.
- **S2** — ATTRIBUTION. Each `query` row's `worktree` is mapped to that tree's HEAD reflog: the
  admin directory under the common git dir's `worktrees/` whose `gitdir` file names that worktree,
  or the common dir's own `logs/HEAD` when the row names the primary tree. The NEXT commit is the
  first reflog entry whose message opens `commit` and whose timestamp is at or after the row's
  `at`. A row with no reflog to read is UNATTRIBUTED and counted in a bucket of its own, and so is a
  row older than its reflog's FIRST entry: that reflog belongs to a later tree at the same path, or
  was expired past the row, so its next commit is not this row's. Observed by AC1, AC2.
- **S3** — CITATION. The distinct next commits are read in ONE `git log --no-walk` call carrying
  their message and zero-context patch; a commit's cited set is every id the kit's own id grammar
  finds in the message and in its added lines. Observed by AC1.
- **S4** — DE-CONTAMINATION. A result id is not counted as used when the row's own `query` or
  `terms` spell it, or when its slug is one the commit's subject line spells, because both mean the
  caller already held the id before the answer. Observed by AC1.
- **S5** — THE REPORT, three lines on stdout: used of attributable; then the query-row count and
  the three remainders, unattributed, no later commit and no record id among the results, which
  with the attributable count make four disjoint buckets summing to it; then the used-rank
  histogram over ranks 1 to the log's `RESULT_CAP`, saying that a deeper rank is not logged.
  Observed by AC1, AC2.
- **S6** — LIVENESS. An absent log exits 2 naming its path; a log with query rows and NO
  attributable row exits 2 saying the figure was not measured, never `0 of 0` at exit 0. Observed by
  AC3.
- **S7** — `tools/memory-recall/README.md` lists `--used` beside `--export` in its usage block, with
  one sentence on what it joins and that it reads only live reflogs. Observed by AC5.
- **S8** — `memory/map/generated/symbols.json` is regenerated for the new
  definitions. NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at
  the close is its check, and §7 names the leg that reads it.

## 3. Non-goals (OUT)

- Changing `recall-opened.js` or the opened records. The offline join replaces widening the hook.
- Making a dead worktree attributable. Its reflog is deleted with it; the query row would need the
  worktree's HEAD at query time, a new field in the served path. §8 F2 splits that out.
- Reading the session-kickoff orientation cards. They live in another kit's sidecar directory, and
  naming it from this kit is the cross-kit literal the hooks README bans; §8 F1.
- Excluding build-era traffic. `--export` LABELS it by `RECALL_BUILD_QID_CUTOFF`; build-era rows
  are from worktrees long removed, so they land in the unattributed count.
- A gate, a pin or a floor on the figure. It is a report a session runs by hand.

### Edges

- **hands-off** `TOOL-aMendedFleet-82` — the `head` field on the query row that would make a removed
  worktree attributable, split out at §8 F2, and the ancestry arm of `--used` that reads it.

## 4. Design

### Evidence

Read at base `7af5f564`, whose bytes for every file below equal HEAD's at `580dc980e`.

- `log_event` in `tools/memory-recall/query.py` writes `qid`, `at`, `query`, `terms`, `worktree`,
  `results` (the top `RESULT_CAP` = 5 as `set`, `id`, `path`, `line`) and `shown_paths`. `read_log`
  reads the file, `log_path` and `common_git_dir` locate it. `E.ID_RE` in `extract.py` is the id
  grammar built from the conf's families.
- A scratch probe over node a's log on 2026-10-04, PINNED: 438 query rows; 10 carry no record id;
  326 name a worktree whose reflog is gone; 10 have no commit after the query; 92 are attributable,
  and 53 of those were used after S4's two exclusions (55 before). Used ranks: 34 at 1, 13 at 2,
  6 at 3. The probe lacked S2's primary-tree arm, so the 20 rows naming the primary tree sat in the
  unattributed count.
- No branch ref resolves a removed worktree: of the 316 rows whose worktree directory is gone, none
  matched a local or remote `branch/<name>` ref, so a branch-ref arm is not built.

### Mechanism

`measure_answer_used(repo)` runs the steps in order. `resolve_worktree_reflog` normalises both
sides with `os.path.normcase` and `os.path.abspath` before comparing a `gitdir` file's directory to
the row's `worktree`, because the log spells Windows paths with either separator.
`read_cited_ids(repo, shas)` makes the one `git` call, splitting on a sentinel line written by the
format string, which matters on node a where a spawn costs most of a second. Rows sharing a next
commit share its cited set.

```
answer-used: <u> of <a> attributable query row(s) cite a shown record id in the worktree's next commit
  of <n> query rows: <x> unattributed (reflog gone) · <y> no commit after the query · <z> no record id in results
  used at rank: 1:<n> 2:<n> 3:<n> 4:<n> 5:<n> — a deeper rank is not logged
```

### Inventory

- `measure_answer_used`, `resolve_worktree_reflog` and `read_cited_ids` — cell `py.function`; each
  answered OK from `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.
- `--used` — a new member of `KNOWN_FLAGS` and `BARE_FLAGS`.

### Rollout

Units 31, 32 and 33 also write `tools/memory-recall/query.py` or its README and are ordered first;
this unit rebases onto whatever they leave. The memory-recall kit version moves once, at the build's
close.

### Files touched (estimate)

- `tools/memory-recall/query.py`
- `tools/memory-recall/README.md`
- `tools/memory-recall/selftest.py`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Record every corpus read in the opened hook** (the superseded ask). It needs a hook change on
  every node and still infers; a citation in the next commit is the caller's own act.
- **Attribute through `git log --all` by time window alone.** Concurrent worktrees commit in the
  same minutes, so a query would be credited with another session's citation.

## 5. Production-readiness checklist

- security — N/A: reads the local log and the local object store; no new input surface.
- perf / scale — one `git` spawn for all commits plus one file read per live reflog.
- error / empty / loading states — absent log and nothing-attributable both exit 2 with a named
  reason (S6); a malformed log line is skipped, as `read_log` already does.
- observability — the remainder line accounts for every query row, so a thin figure reads as thin.
- risks — reflogs expire with `gc.reflogExpire`, which only moves rows into the unattributed count.
- testing — the fixture repository in AC1 and AC3, and a selftest arm declared in §7.
- migration — N/A: reads existing rows; nothing is written.
- user docs — S7.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-recall/query.py --used` runs inside a fixture repository whose
  linked worktree holds one commit made after three hand-written query rows, where row 1's second
  result id is cited in that commit's added lines, row 2's only cited result id is also in its own
  `terms`, and row 3 names a worktree path with no reflog, it prints `answer-used: 1 of 2`, the
  remainder line with `1 unattributed`, and `2:1` in the rank line.
  Red when: S4 is absent and it prints `2 of 2`, or row 3 is dropped instead of counted.
  fixture: a `git init` plus `git worktree add` under a short `%TEMP%` root; the tree holds none.
- **AC2** — When `python tools/memory-recall/query.py --used` runs on node a's live log, it exits 0
  and its attributable count plus the remainder line's three counts sum to the line's
  `of <n> query rows` figure, which equals the
  number of `"type": "query"` rows in the log under the common git dir.
  Red when: a row is counted twice or in no bucket.
  figure: DERIVED at observation time; the §4 probe read 438 rows and 92 attributable.
- **AC3** — When `python tools/memory-recall/query.py --used` runs in a fixture repository with no
  log, it exits 2 naming the log path; with one query row whose worktree was removed, it exits 2
  saying the figure was not measured.
  Red when: either case prints a zero figure at exit 0.
- **AC4** — When `python tools/memory-recall/query.py --used` runs in the AC1 fixture, the log's
  `sha256sum` is unchanged afterwards and `git status --porcelain` prints nothing.
  Red when: the mode appends a query row through `log_event`.
- **AC5** — When `grep -n -- "--used" tools/memory-recall/README.md` runs, it hits the usage block.
  Red when: the README is unchanged.

## 7. Gates

`memory-recall kit selftest` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-recall/selftest.py · the AC1 fixture, staged red by removing S4's terms exclusion · `SELFTEST_ARMS` moves by the arms added, with its dated `N -> M` provenance line

## 8. Open questions

- **F1 — Do orientation cards count as a citation source?**
  Options: read the session-kickoff card directory under the common git dir; take the card
  directory as an argument; read commits only. The card is the other kit's sidecar, and naming its
  directory here is the cross-kit literal the hooks README bans; an argument adds surface no caller
  exists for. A spec the session writes reaches the next commit's added lines anyway.
  RESOLVED (agent, 2026-10-04, delegated): commits only; cards are a follow-up, not built here.
- **F2 — How does a removed worktree stay attributable?**
  Options: report it as unattributed; match a `branch/<name>` ref, which resolved none of 316 rows;
  log the worktree's HEAD sha on every query row so the next commit is found by ancestry after the
  worktree is gone. The third is a change to the served query path, a second mechanism.
  RESOLVED (agent, 2026-10-04, delegated): split — the HEAD field on the query row moves to a new
  unit the run adds; this unit reports the unattributed count.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#32] and a probe of node a's query
  log and worktree reflogs at base.
- rev-2 · 2026-10-04 · §2 S8 · §4 · §7 · M2 cross-read: the definitions this unit adds
  move `memory/map/generated/symbols.json`, which `TOOL-aMendedFleet-82` and the build's other
  code units regenerate and declare; this spec omitted the write, its Files touched row and the leg.
  §3 Edges also names `TOOL-aMendedFleet-82` for the `head` field, which it called
  `external`, and the §7 arm line moves `SELFTEST_ARMS`, as `TOOL-aMendedFleet-27` S5 does.
- rev-3 · 2026-10-05 · §2 S2 · the build's bug-class checklist named a location join that
  outlives its subject: a worktree path is reused, and a reflog's old entries expire, so S2's
  first-commit-after rule alone credited a row with a later tree's commit. A row older than its
  reflog's first entry is unattributed. S4's "spell" is read as a whole id or slug token, not a
  substring, so an id is not held by a row spelling a longer id that begins with it.

## 10. Reuse audit

The seams extended are `read_log`, `log_path` and `common_git_dir` in
`tools/memory-recall/query.py`, and the id grammar `ID_RE` in `tools/memory-recall/extract.py`;
the flag joins the existing closed tables beside `--export`, the kit's other offline aggregate.
`python tools/codebase-map/reuse_lookup.py "join logged recall query results to ids a later commit
cites"` returned name-stem neighbours such as `measure_commitment` in `tools/runlog/record.py` and
`join_aliases` in `extract.py`, none of which reads a reflog or joins log rows to commits, so no
existing seam fits the attribution step; `_resolve_git_dir` in `tools/codebase-map/reuse_lookup.py`
reads a worktree's `.git` file but sits in another kit and is not importable here. Recall returned
`TOOL-aWeighedCompass-11`, the ask this unit closes, the measurement record that found the opened
signal thin, and `TOOL-aProvenReuse-2`, whose DoD item reads the same log for a different question.
Where the report and the tree disagree: the report counted 379 queries; the log held 438 at the probe.

Recall terms used: `python tools/memory-recall/query.py "how is whether a recall answer was used
measured from the query log" --terms "recall opened inferred in_shown telemetry queries.jsonl qid
shown_paths answer used worktree export"`
