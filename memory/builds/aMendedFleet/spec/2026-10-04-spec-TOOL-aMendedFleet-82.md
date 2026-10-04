# TOOL-aMendedFleet-82 — each recall query row carries the worktree's HEAD, so `--used` attributes a query after its worktree is gone

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 82

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Unit 34's `query.py --used` finds the commit after a recall query through the worktree's HEAD
reflog, which `git worktree remove` deletes, so 326 of 438 logged queries on node a could not be
attributed at its probe. This unit, split from unit 34 at its F2, writes the worktree's HEAD sha
into every query row at query time, and teaches `--used` to find the next commit by ancestry from
that sha when the reflog is gone: a commit whose parents include it, committed at or after the
query. Rows already logged carry no such field and stay unattributed; every row written from now on
survives its worktree.

## 2. Scope (IN)

- **S1** — THE FIELD. A new reader in `tools/memory-recall/query.py`, `read_worktree_head(repo)`,
  runs one `git rev-parse --verify --quiet HEAD` without `check`, and returns the sha, or `None` on
  an unborn HEAD or any git failure. The query row `main` hands to `log_event` gains `"head"` with
  that value. Nothing else in the row moves, and a failure never fails the query, which is
  `log_event`'s existing contract. Observed by AC1, AC2.
- **S2** — THE ANCESTRY ARM. In `--used`, a query row whose worktree reflog cannot be read and which
  carries a non-null `head` is attributed by ancestry: its next commit is a commit reachable from any
  ref whose parents include `head` and whose committer time is at or after the row's `at`. Exactly
  one such commit attributes the row; none puts it in the existing "no commit after the query"
  bucket; more than one leaves it unattributed and counts it as AMBIGUOUS, because two worktrees
  started from one tip would otherwise credit one another's citations. A row the reflog attributes
  is never re-attributed by `head`. Observed by AC3, AC4.
- **S3** — ONE CALL. The parent map comes from a single `git log --all --format` call printing each
  commit's sha, parents and committer time, made only when at least one row needs the arm, and the
  cited set of every chosen commit joins unit 34's one `git log --no-walk` read. Observed by AC3.
- **S4** — THE REPORT gains a fourth line, `  attributed by head ancestry: <h> · ambiguous head:
  <m>`, below unit 34's three. The head-attributed rows count inside the first line's attributable
  figure, and the ambiguous ones inside the remainder line's unattributed figure, so unit 34's four
  buckets still sum to the query-row count. Observed by AC3, AC4.
- **S5** — `tools/memory-recall/README.md` names the `head` field where it describes the query row,
  and says `--used` reads it when a worktree's reflog is gone. Observed by AC5.
- **S6** — `memory/map/generated/symbols.json` is regenerated for the new definition. NOT OBSERVED
  by a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is its check,
  and §7 names the legs that read it.
- **S7** — Self-test arms in `tools/memory-recall/selftest.py`: the AC3 fixture and the AC4 fixture.
  NOT OBSERVED by a criterion here: the suite runs once at the close, and the arms are declared
  under `New arm:` in §7.

## 3. Non-goals (OUT)

- Back-filling `head` into rows already logged. Their HEAD at query time is not recoverable for a
  removed worktree, which is the problem.
- Logging a branch name. Branch refs are deleted at landing, so a name outlives its target no
  better than a reflog does; the sha is what ancestry needs.
- Adding `head` to `opened` rows. They join to a query by `qid` and need no second sha.
- Changing `--export`, the opened hook, or cache eviction. None reads the new key.
- A gate on the attributed figure. `--used` stays a report a session runs by hand.
- Bumping the memory-recall kit version, owed once at the close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-34` — the `--used` mode, its reflog attribution, its cited-id
  read and its three report lines; S2 to S4 extend them and have nothing to extend without them.
- **hands-off** external — the memory-recall kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at the worktree HEAD `fee9f62b`, whose bytes under `tools/` equal base `7af5f564`'s.

- `main` in `tools/memory-recall/query.py` builds the query row with `type`, `query`, `terms`,
  `rewritten`, `k`, `budget`, `bytes_emitted`, `worktree`, `n_hits`, `n_shown`, `results` and
  `shown_paths`, and `log_event` adds `qid` and `at`. The module's `git` helper calls
  `subprocess.run` with `check=True`, so S1 does not reuse it: an unborn HEAD would raise.
- Node a's log held 450 query rows at this probe, and no row carries a HEAD sha. PINNED, measured
  2026-10-04; unit 34's probe read 438 and 326 of them unattributable.
- One `git rev-parse --verify --quiet HEAD` spawn cost 0.021 s on node a, mean of five. PINNED,
  measured 2026-10-04 on an idle host; a contended host has measured far slower, so S1 makes one
  spawn and no more.

### Mechanism

`head` is read at log time, after the hits print, so the sha is the tree the caller is about to
commit on. The next commit after a query in a live worktree is a child of that sha unless the
caller reset or rebased first, which the reflog arm still covers while the worktree exists. When it
does not, ancestry finds the commit wherever it now lives: on a deleted branch it survives only as
far as some ref reaches it, and a commit merged with `--no-ff` stays reachable from the default
branch. A commit no ref reaches reads as "no commit after the query", which is honest.

### Inventory

- `read_worktree_head` — cell `py.function`; answered OK from
  `python tools/lexicon/lexicon.py --suggest read_worktree_head --as py.function`.
- `head` — a new key of the query row; no naming cell grades JSON keys.

### Rollout

Unit 34 builds `--used` and is ordered first; this unit rebases onto it. Units 31, 32 and 33 also
write `tools/memory-recall/query.py` or its README and are ordered first too.

### Files touched (estimate)

- `tools/memory-recall/query.py`
- `tools/memory-recall/README.md`
- `tools/memory-recall/selftest.py`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Read HEAD from the files under the git dir.** It saves a spawn and re-implements ref
  resolution: loose refs, `packed-refs`, a detached HEAD, and the reftable format, which stores
  neither file. One `rev-parse` is correct on all of them.
- **Fold the read into `common_git_dir`'s `rev-parse`.** That helper raises on failure and serves
  the cache and log paths, so an unborn HEAD would fail the query it exists to log.
- **Attribute by the first commit after `at` on any branch.** Concurrent worktrees commit in the
  same minutes, which is why unit 34 rejected time-only attribution; ancestry from `head` is the
  discriminator.

## 5. Production-readiness checklist

- security — N/A: a commit sha is already public to anyone reading the log's own repository.
- perf / scale — one spawn per query; `--used` adds one `git log --all` only when a row needs it.
- error / empty / loading states — a failed read logs `"head": null` and the query answers as
  before; a row with a null or absent `head` falls through to unit 34's buckets unchanged.
- observability — the fourth line says how many rows ancestry recovered and how many it refused.
- risks — a rebased or reset worktree's next commit is not a child of `head`; it reads as "no commit
  after the query", never as a wrong attribution.
- testing — AC1 to AC5 here; the arms in S7.
- migration — N/A: an additive key; rows without it are read as before.
- user docs — S5.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-recall/query.py "how are recall queries logged" --terms
  "recall queries.jsonl query log worktree head qid results shown_paths log_event"` runs at the
  worktree root, the last `"type": "query"` row of the log under `git rev-parse --git-common-dir`
  carries a `head` equal to what `git rev-parse HEAD` prints.
  Red when: the row has no `head`, or it names another tree's sha.
- **AC2** — When `python -c` imports `query` from `tools/memory-recall` and calls
  `read_worktree_head` on a freshly `git init`-ed fixture with no commit, it prints `None` and raises
  nothing.
  Red when: an unborn HEAD raises, which would cost the query its log row.
  fixture: a `git init` under a short `%TEMP%` root; the tree holds none.
- **AC3** — When `python tools/memory-recall/query.py --used` runs in a fixture repository whose
  linked worktree recorded one hand-written query row carrying that worktree's `head`, then made a
  commit citing the row's first result id, then was removed with `git worktree remove`, it prints
  `answer-used: 1 of 1` and `attributed by head ancestry: 1`.
  Red when: the row lands in the unattributed count, which is unit 34's behaviour without this arm.
  fixture: built under a short `%TEMP%` root; the tree holds none.
- **AC4** — When that fixture instead holds two commits, on two branches, each a child of the row's
  `head` and each made after its `at`, `python tools/memory-recall/query.py --used` prints
  `ambiguous head: 1` and counts the row unattributed.
  Red when: either commit is credited with the query.
- **AC5** — When `grep -n "head" tools/memory-recall/README.md` runs, it hits the sentence that
  describes the query row and the `--used` entry.
  Red when: the log gains a field its README does not name.

## 7. Gates

`memory-recall kit selftest` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/memory-recall/selftest.py` · the AC3 fixture staged red by deleting the row's `head`, and the AC4 two-child fixture · none

## 8. Open questions

- **F1** — What does `--used` do when more than one commit is a child of `head` after the query?
  Options: credit the earliest; credit every one; count the row ambiguous. The earliest is often a
  sibling worktree that started from the same tip, and crediting every one inflates the figure.
  RESOLVED (agent, 2026-10-04, delegated): ambiguous, counted on its own line and inside the
  unattributed bucket, per S2 and S4.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, split from unit 34 at its F2, from a probe of node a's query
  log and the query row's assembly at base.

## 10. Reuse audit

The seams extended are the query row assembled in `main` and written by `log_event` in
`tools/memory-recall/query.py`, and unit 34's `--used` mode with its `resolve_worktree_reflog` and
`read_cited_ids`, which do not exist at base and are cited from unit 34's spec.
`python tools/codebase-map/reuse_lookup.py "record the worktree HEAD sha on each logged recall
query"` returned name-stem neighbours in `tools/runlog/record.py`, such as `write_record` and
`derive_short_sha`, which write and shorten run-record shas for another kit, so no existing seam
fits the field; the module's own `git` helper raises on failure, so S1 adds a non-raising reader
beside it rather than reusing it. Recall returned unit 34's spec, which names this split,
`TOOL-aProvenReuse-2`, whose `reuse-probed` item reads the same log by `worktree`, and
`TOOL-aQuenchedHarness-12`, on worktrees the index cannot see. Where the report and the tree
disagree: the log grew from unit 34's 438 query rows to 450 at this probe.

Recall terms used: `python tools/memory-recall/query.py "is a recall query row attributable to the
commit after it once the worktree is gone" --terms "recall queries.jsonl query log worktree head sha
reflog ancestry answer used attribution"`
