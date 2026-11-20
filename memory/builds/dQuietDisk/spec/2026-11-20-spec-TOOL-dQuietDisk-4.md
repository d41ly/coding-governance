# TOOL-dQuietDisk-4 — routed-commits reads only the commits its store does not already hold

**Status:** SPECCED · rev-1 · 2026-11-20 · node d · Tier-2 · base 609cd40b · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-tree/routed_commits.py` reads every commit of HEAD's history with one
`git log --name-only` per run, about 9,900 commits, measured at 1,761 s by the analysis
(`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`, row G3), and on a
push it reads them twice, RANGE and WHOLE. A commit's log record never changes once its id exists.
This unit keeps each commit's parsed record in TOOL-dQuietDisk-1's history verdict store, keyed by
its id and the reader's code, and logs only the commits the store does not hold. The leg's rc and
every line it prints stay byte-identical, the deviation join's lines included.

## 2. Scope (IN)

- **S1** — `read_routed_commits` derives the population's order from one `git rev-list` over the
  same revision arguments, then takes each commit's record from the store. It logs only the commits
  the store lacks, through the same `read_commits` reader and the same trailer keys. Observed by AC1
  and AC3.
- **S2** — The leg opens the store once with `open_store` from the memory-tree kit's copy of the
  module, `tools/memory-tree/history_store.py`. Its code paths are `routed_commits.py`,
  `commit_trailers.py`, `tree_lib.py` and the trailer key table `read_key_table` resolves, so a
  change to any of them moves every key. A stored record is the reader's own dict for one commit:
  `sha`, `parents`, `date`, `subject`, `trailers` and `paths`. Its id fields are the commit id and
  the requested trailer keys. Observed by AC2.
- **S3** — Every grading step after the read runs as today over the assembled list: the cutoff, the
  routed-path test, the attribution union, the first-parent batch check, the red-fix lane and its
  limits, the waiver and stale rules, and the deviation join. Nothing graded is stored. Observed by
  AC1 and AC4.
- **S4** — The truncation refusal keeps its meaning: the assembled list must hold exactly the
  commits `rev-list` named, and every logged commit must parse, or the leg refuses at exit 2 naming
  the counts as today. Observed by AC5.
- **S5** — When the commits the store lacks exceed a bound, 500, the reader logs the population with
  today's revision arguments in one call rather than a list of ids, so a cold run's argv stays
  short. Observed by AC3.
- **S6** — A run that ends without a Refusal writes every newly logged record and the new tip, each
  tmp-then-rename. A missing, unreadable, partial or foreign-version record is logged again, never
  trusted. The policy key `tests.history-verdicts` at `regraded` restores today's single log pass.
  Observed by AC2 and AC5.
- **S7** — The module docstring gains one paragraph naming the store, what it holds, and the
  switch. Observed by AC6.

## 3. Non-goals (OUT)

- No stored verdict. A commit's verdict reads HEAD's id map, `no spec defines it at HEAD`, which
  moves on every spec commit, so this unit stores the commit's record and grades it each run.
- No change to `deviation_join.py`. Its per-row pickaxes, which TOOL-aMeasuredDrag-1's findings
  record measured at about 219 s per bar, are dTrueNorth's join and a separate mechanism.
- No change to `commit_trailers.py`, which three kits carry as one reader.
- No change to the red-fix limits pass, whose one `git log` runs only over `Red-fix:` commits.
- No change to the reuse cache's history key, and no change to what is graded.

### Edges

- **consumes-from** `TOOL-dQuietDisk-1` — the history verdict store, through the memory-tree kit's
  copy of its module, and its policy key. Without them the leg logs its whole population as today.

## 4. Design

### The read today

All citations are read at `609cd40b1`.

`check_routed_commits` (`tools/memory-tree/routed_commits.py#check_routed_commits`) loops over one or
two populations and calls `read_routed_commits` for each
(`tools/memory-tree/routed_commits.py@609cd40b1:421`). That calls `read_commits`
(`tools/memory-tree/commit_trailers.py#read_commits`), whose one `git log -z --root --no-renames
--name-only` over the revision arguments is the 1,761 s. Its count is then checked against
`rev-list --count` (`tools/memory-tree/routed_commits.py@609cd40b1:423`). The records feed both the
grading loop and `check_deviation_join`, which reads `sha`, `parents`, `date`, `trailer` and `paths`
(`tools/memory-tree/deviation_join.py#read_first_passes`).

### Why a stored record is the same record

`read_commits` builds each dict from one log record of one commit id. The fields are the commit's own
immutable data, rendered by a format string and a parse that live in `commit_trailers.py`. The trailer
values also depend on which keys the table registers, since a key the table lacks is a ValueError
before anything is read. So the key holds the commit id, the reader's blob ids, the requested keys and
the table's blob id. A change to any of them misses every stored record, and the next run is cold.

`git log` and `git rev-list` over the same revision arguments list commits in the same default order.
So assembling the stored records in `rev-list` order gives the list the single log pass gave.

### The read after

```python
def read_routed_commits(repo, rev_args: list) -> list:
    order = rev-list over rev_args                 # one process, no diffs
    held = the store's records for order, under this reader's key
    lack = [sha for sha in order if sha not in held]
    if len(lack) > 500:  fresh = read_commits(repo, rev_args, ...)       # today's call
    elif lack:           fresh = read_commits(repo, ["--no-walk=unsorted", *lack], ...)
    else:                fresh = []
    # S4: every sha in lack parsed, and len(assembled) == len(order), or Refusal
    return [held.get(sha) or fresh_by_sha[sha] for sha in order]
```

The `total` check in `check_routed_commits` keeps reading `rev-list --count`, so the refusal reads as
today. The RANGE and WHOLE populations share one store, so a push's WHOLE half reads what its RANGE
half just logged.

### The warm-run bound

With the four DESIGN_* keys blank the deviation join makes no git call
(`tools/memory-tree/routed_commits.py#check_deviation_join`). A warm WHOLE run with no new commit
then makes the shallow test, the `ls-tree -r HEAD`, the spec `cat-file --batch`, `rev-parse HEAD`,
one `rev-list`, the `rev-list --count`, the first-parent `cat-file --batch-check` and the red-fix
limits log. The bound promised is **at most 12 git processes** and **no `git log --name-only` over
more than the NEW commits**, PINNED as a promise and observed by AC3. The cold run's time is DERIVED
at observation.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `LOG_BATCH_BOUND` | module constant, 500 | none | AC3 |
| the record key fields | store item fields | none; the store's schema owns them | the store's reader |

No verb, flag, conf key, policy key or refusal number is minted.

### Files touched (estimate)

`tools/memory-tree/routed_commits.py`

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| Store each commit's verdict, keyed by its id and the grading code | The verdict reads HEAD's id map, so a spec added at HEAD flips an old commit's `no spec defines it at HEAD`; the key would need the whole map and would move on every spec commit. |
| Grade only `<last>..HEAD` and carry the old counts | The summary counts and the deviation join read the whole population, and a stale waiver is judged over all of it. |
| A `--stdin` id list to `git log` | `read_commits` takes revision arguments and no stdin, and it is one reader shared by three kits. |

## 5. Production-readiness checklist

- security: N/A — records are read from the repository's own history into the store under its git
  common dir; nothing is pushed or rendered.
- perf / scale: a warm run logs only NEW commits (AC3); a cold run costs today's log plus one store
  write.
- error / empty / loading states: a missing or foreign record is logged again; a log that parses short
  refuses at exit 2 (S4).
- observability: the summary lines are unchanged.
- risks: a reader change the key misses would carry stale records; S2's key holds the reader's blobs
  and the key table's, and AC2 plants the table move.
- testing: the equivalence corpus (AC1), the key moves (AC2), the count (AC3), the planted red (AC4).
- migration: none; the first run is cold.
- user docs: the module docstring (S7); `help/` holds no page for this leg.

## 6. Acceptance criteria

- **AC1** — When the old leg, `python tools/memory-tree/routed_commits.py` at `609cd40b1`, and the new
  leg run over one scratch `git clone --shared` of the real tree at the build's base, the store cold
  and then warm, and again with `GATE_PUSH_BASE` set to a commit 20 behind HEAD, all outputs and exit
  codes are byte-identical, the deviation join's lines included.
  Red when: a record assembled from the store differs from the logged one, or the order moves.
  cost: about 30 minutes per cold run, measured 1,761 s by the analysis.
  fixture: a clone under `%TEMP%` with its own `TEMP`.
- **AC2** — When the trailer key table `tools/playbook/edges.toml` gains one row in the clone, the
  next run logs the whole population again and prints what the old leg prints.
  Red when: a record stored under the old table is reused.
- **AC3** — When the new leg runs warm with no new commit and the four DESIGN_* keys blank, under
  `GIT_TRACE2_EVENT=<dir>`, the directory holds at most 12 files and no `log` event names
  `--name-only` over more than the NEW commits.
  Red when: the whole-history log survives on the warm path.
  figure: 12 is PINNED as the promise.
- **AC4** — When a `git commit` touching a path under `ROUTED_PATHS` that names no unit is added past
  the stored tip, both legs exit 1 and print the same violation line for it.
  Red when: the new commit is not read, or reads green.
- **AC5** — When a stored record is truncated to half its bytes, the next run logs that commit again
  and its output equals the old leg's. When a planted `read_commits` stub drops one logged commit, the
  leg exits 2 with the truncation refusal.
  Red when: a partial record is trusted, or a short stream reads clean.
- **AC6** — When `grep -c 'history verdict store' tools/memory-tree/routed_commits.py` runs, it prints
  1 or more.
  Red when: the docstring does not name the store and its switch.

## 7. Gates

`routed commits name a specced unit` · `routed-commits selftest` · `policy fixtures` · `line length` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC4 AC5 · a `--selftest` arm whose fixture stores records, then adds an unattributed routed commit and truncates one record; its failing case is staged by reading the store without logging the commits it lacks · none

The arm sits in the leg's own `--selftest`, which already counts spawns per run. The main loop
observes it at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.

## 10. Reuse audit

The seam extended is `read_routed_commits`
(`tools/memory-tree/routed_commits.py#read_routed_commits`), the leg's one log pass, through
TOOL-dQuietDisk-1's store. TOOL-aMeasuredDrag-1's findings record proposed a per-commit cache for
history legs (`memory/builds/aMeasuredDrag/build/2026-11-15-build-TOOL-aMeasuredDrag-1-findings-gate.md`,
row legs-1 and the routing note under it). Where the brief says to key each commit's verdict, this
spec keys its record, for the reason section 3 gives. The chain build owning the area is dWitnessedBar
(Test: gate health), with dScopedBuild (Build: the history-derived exit base); dWitnessedBar changes
this file by 3 lines at `609cd40b1`.

`python tools/codebase-map/reuse_lookup.py "cache parsed commit log records by commit id across runs"`
returned name-token neighbours only (`run`, `parse`, `parse_args`, `records`). No existing seam fits
beyond the leg's own reader and the store. Recall returned TOOL-aRoutedQuill-10, the WHOLE-beside-
RANGE rule, TOOL-aNimbleMend-10's limits pass, TOOL-dDeclaredLoop-23 and -40, the one trailer reader,
and TOOL-dTrueNorth-4, the deviation join. The source agreed with each.

Recall terms used: routed_commits read_routed_commits log pass whole range deviation join commit_trailers read_commits numstat incremental
