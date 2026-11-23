# TOOL-dQuietDisk-4 — routed-commits reads only the commits its store does not already hold

**Status:** CLOSED · rev-4 · 2026-11-22 · node d · Tier-2 · base 40def53f · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 |
| [2026-11-22-build-TOOL-dQuietDisk-4-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-4-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dQuietDisk-4-red-fix-13.md](../build/2026-11-22-build-TOOL-dQuietDisk-4-red-fix-13.md) | red-fix | — |
| [2026-11-22-build-TOOL-dQuietDisk-4-red-fix-5.md](../build/2026-11-22-build-TOOL-dQuietDisk-4-red-fix-5.md) | red-fix | — |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task.md) | research | TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 |
| [2026-11-22-prompt-TOOL-dQuietDisk-4-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-4-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-4-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-4-build-brief.md) | journal | — |
| [2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md](../reviews/2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md) | diff-review | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-tree/routed_commits.py` reads every commit of HEAD's history on every run. It makes
one `git log --name-only` per population, so a push reads the history twice, RANGE and WHOLE. A
commit's log record never changes once its id exists. This unit keeps the parsed records in
TOOL-dQuietDisk-1's history verdict store, as 256 items each keyed by the commits it holds, and
logs only the commits the store does not hold. The leg's rc and every line it prints stay
byte-identical, the deviation join's lines included.

What the unit saves was measured at the re-ground. The analysis's row G3
(`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`) gives the leg
1,761 s [PINNED] on the loaded disk. It names a `git log --raw --numstat` over all commits, but at
the base that argv is the red-fix limits read, over the `Red-fix:` commits alone
(`tools/memory-tree/routed_commits.py#check_red_fix_limits`). The whole-history read is the one
`git log --name-only` of `read_commits`. With a warm page cache that log took 1.8 s over 10,983
commits and printed 7.5 MB, and the limits read took 0.7 s over 216 commits [PINNED, both measured
2026-11-22 at `8688cdbba`, whose `tools/` tree equals the base's]. So the saving is the pack reads
of the log pass, which a loaded disk makes slow. It is not a process saving: the store's resolve
adds 8 git processes per run in a fixture and 9 in gov's tree (section 8, F1). TOOL-dQuietDisk-19
records the before and after.

## 2. Scope (IN)

- **S1** — `read_routed_commits` gains a third parameter, `held`, a dict that
  `check_routed_commits` creates once per run and passes to each population's read. With `held`
  given and the store on, the population's order comes from one `git rev-list` over its revision
  arguments, and each commit's record from the run's record map. A WHOLE population reuses the
  fill's order and runs no second `rev-list`. With `held` absent the read is today's. That keeps the
  three other callers on today's read: `tools/memory-tree/build_records.py#write_red_fix`,
  `tools/memory-tree/build_records.py#check_red_fix_join` and
  `tools/memory-tree/deviation_join.py#measure_fixture`. Observed by AC1 and AC7.
- **S2** — The record map is filled once per run, over the WHOLE order `git rev-list HEAD`, since
  every run grades WHOLE. The fill takes five steps, each in section 4: group by id prefix, read the
  buckets, recover a moved bucket's old members through the tip, log the lack, write. Observed by
  AC1, AC3 and AC4.
- **S3** — The store is opened once per run, at the first fill, with
  `resolve_store(repo, "routed-commits", code_paths)` from the memory-tree kit's copy,
  `tools/memory-tree/history_store.py`. The code paths are the kit's `routed_commits.py`,
  `commit_trailers.py` and `tree_lib.py`, by absolute path, and the trailer key table's path where
  `read_key_table` returns one. The leg calls `read_key_table` before the fill, inside the `try`
  that maps a ValueError or LookupError to `the commit log cannot be read`. So a table that does not
  parse refuses with today's words, and an edit to any code path moves every key. Observed by AC2.
- **S4** — A bucket's body is a JSON array of the reader's own dicts, sorted by id. Each dict holds
  exactly `sha`, `parents`, `date`, `subject`, `trailers` and `paths`, and its `trailers` holds
  exactly the two keys the leg asks for. The body is rendered with sorted keys and compact
  separators, so two writers write the same bytes. A body that does not parse, a record of another
  shape, or a set of ids other than the bucket's members is a miss, never a record. Observed by
  AC5.
- **S5** — The truncation refusal keeps its words and its counts. The assembled list skips a
  commit no record holds, so a short log yields a short list, and the existing comparison against
  `rev-list --count` refuses at exit 2. A fill that leaves any commit without a record writes
  nothing. Observed by AC5.
- **S6** — With the store off, the read is today's: one `read_commits` per population over its
  revision arguments, no `rev-list` for the order, nothing written. The store is off when
  `tests.history-verdicts` reads `regraded` or when the store cannot resolve. Observed by AC6.
- **S7** — `run_selftest` replaces the module's `resolve_store` name with one that returns an off
  store for every existing arm, so each keeps today's read and its spawn count. Only the new arm
  restores the real one. Observed by AC9, and by the `New arm:` line in section 7.
- **S8** — The module docstring gains one paragraph naming the store, what an item holds, what a
  warm run still spawns, and the switch. Observed by AC8.

## 3. Non-goals (OUT)

- No stored verdict. A commit's verdict reads HEAD's id map, `no spec defines it at HEAD`, which
  moves on every spec commit. So this unit stores the commit's record and grades it each run.
- No change to `deviation_join.py`. Its per-row pickaxes are dTrueNorth's join and a separate
  mechanism; TOOL-aMeasuredDrag-1's findings record measured them at about 219 s [PINNED] per bar.
- No change to `commit_trailers.py`, which three kits carry as one reader, and no change to the
  red-fix limits read, whose one `git log` runs over `Red-fix:` commits only.
- No change to `read_newest_unit`, the `--newest-unit` verb's own range read
  (`tools/memory-tree/routed_commits.py#read_newest_unit`).
- No use of the store's `BatchReader`. The leg's object reads are already one `cat-file --batch`
  and one `cat-file --batch-check` each, and a record is a log record, not an object.
- No change to TOOL-dQuietDisk-1's store. A gap in it is that unit's deviation, named in section 8.
- No change to the reuse cache's history key, and no change to what is graded.

### Edges

- **consumes-from** `TOOL-dQuietDisk-1` — the history verdict store, through the memory-tree kit's
  copy of its module, and its policy key. Without them the leg reads its whole population as today.

## 4. Design

### The read at the base

All citations are read at `40def53f7`. The leg's blob is `e699ef01c1c1`, the reader's
`c70e65b653b1` and the kit library's `32b948d8b50b`.

`check_routed_commits` loops over one or two populations
(`tools/memory-tree/routed_commits.py@e699ef01c1c1:421`) and calls `read_routed_commits` for each
(`:422`). That calls `read_commits` (`tools/memory-tree/commit_trailers.py#read_commits`). Its one
`git log -z --root --no-renames --name-only` over the revision arguments is the whole-history read.
`read_commits` first calls `read_key_table` and raises a ValueError for a requested key the table
does not register (`tools/memory-tree/commit_trailers.py@c70e65b653b1:194`). The leg then checks the
count against `rev-list --count` (`tools/memory-tree/routed_commits.py@e699ef01c1c1:424`). The
records feed the grading loop and `check_deviation_join`. Past the two fields `read_routed_commits`
derives, `trailer` and `red_fix`, nothing mutates a record, so the two populations may share one.

Three other callers pass two arguments: `build_records.py` with `["-1", <sha>]` and `["HEAD"]`
(`tools/memory-tree/build_records.py@431265189bb5:558`, `:595`), and the deviation join's fixture
measure (`tools/memory-tree/deviation_join.py@bdb5a3d1bab8:1315`).

dWitnessedBar changed this file at `79a4f9c20` (TOOL-dWitnessedBar-29, a path for
`--newest-unit`) and `c1eed311c` (the self-test's remover). It changed the reader at `c8727978d`
(TOOL-dWitnessedBar-2, `Commit-Checked` among the floor keys) and through TOOL-dWitnessedBar-108 to
110 (the attribution check). None of them touches the leg's read. Each moved the reader's bytes,
which is why the reader is a code path of the key.

### The store as built

From `tools/lib/history_store.py#resolve_store`, byte-identical in the memory-tree kit's copy:

| Call | What this unit uses it for |
|---|---|
| `resolve_store(repo, leg, code_paths)` | the run's `HistoryStore`, `stored` False under `regraded` or when no git dir resolves |
| `HistoryStore.read(fields)` | a bucket's body, or None on a miss, a torn or foreign item, or the store off |
| `HistoryStore.write(fields, body)` | a bucket whose key missed; an item already holding the body is left as it is |
| `HistoryStore.read_tip()`, `write_tip(sha)` | this worktree's last filled HEAD |
| `HistoryStore.remove_aged()` | the 30-day prune, at most once a day, which the CLI's `store` verb runs and the Python face leaves to its caller |

The layout is `<git common dir>/history-verdicts/v1/routed-commits/items/<key[0:2]>/<key>`, beside
`tips/<scope>`. The key is the sha256 of the schema, the leg, the code digest and the fields. The
code digest hashes each code path's WORKING bytes. A code path inside the repository is named
relative to it, so an adopter's worktrees share their items, and a path outside it is named
absolute.

### Why a stored record is the same record

`read_commits` builds each dict from one log record of one commit id. The fields are the commit's
own immutable data, rendered by a format string and a parse that live in `commit_trailers.py`. A
requested key the table lacks is a ValueError before anything is read. So the key holds the reader
and the table through the code digest, and the leg and its git runner, `tree_lib.build_git_env`,
through the same digest. A change to any of them misses every bucket, and the next run is cold.

`git log` and `git rev-list` over the same revision arguments list commits in the same default
order. So the stored records, taken in `rev-list` order, are the list the single log pass gave. A
record logged with `--no-walk=unsorted <id>...` is the record the walked log gives for that id,
since both runs pass `--root`, `--no-renames` and `--name-only` and show a merge with no paths.

### The fill

```python
def read_routed_commits(repo, rev_args, held=None) -> list:
    if held is None: return today's read                         # S1: the other callers
    if not held: fill(held)                                      # once per run
    if not held["store"].stored: return today's read             # S6
    order = held["order"] if rev_args == ["HEAD"] else rev-list(rev_args)
    return [derive(held["records"][sha]) for sha in order if sha in held["records"]]   # S5

def fill(held):
    read_key_table()                                             # S3: today's refusal, the table path
    store = resolve_store(repo, "routed-commits", code_paths)
    order = rev-list HEAD
    buckets = group order by sha[:RECORD_BUCKET_HEX]             # 256 buckets
    fields(members) = [prefix, sha256("\n".join(sorted(members)))]
    records = every record of each bucket that hits             # S4 rejects a malformed body
    missed = the buckets that did not hit
    tip = store.read_tip()
    if missed and tip and tip != HEAD:                           # recover the old members
        old = rev-list tip (may fail: then no old)
        read the bucket of old's members under each missed prefix into records
    lack = [sha for sha in order if sha not in records]
    if len(lack) > LOG_BATCH_BOUND: log = read_commits(["HEAD"])
    elif lack:                      log = read_commits(["--no-walk=unsorted", *lack])
    records.update(log)
    if every sha of order is in records:                         # S5: no write after a short log
        write each missed bucket; write_tip(HEAD) when it moved; store.remove_aged()
```

`LOG_BATCH_BOUND` is 500. At 41 bytes an id, 500 ids hold the log's argv near 21 KB [DERIVED],
under the 32,767-character command line of Windows. A cold run passes the bound and runs today's log.

A bucket holds 43 records at the base and about 29 KB [DERIVED: 10,980 commits and 7.5 MB over 256
buckets]. A new commit moves only its own bucket's key, so a run after k new commits writes at most
k buckets and logs only those k commits. Two bars writing one bucket write the same bytes, which
the store's tmp-then-rename lands once.

### The warm-run bound

Today, a WHOLE run over a fixture with the four DESIGN_* keys blank and no `Red-fix:` commit made 8
git processes [PINNED, measured 2026-11-22 over a 32-commit fixture built by `build_fixture`]. They
are the top-level `rev-parse`, the shallow test, the `ls-tree`, the spec `cat-file --batch`, the
`rev-parse HEAD`, the `log`, the `rev-list --count` and the first-parent `cat-file --batch-check`.

After the unit, a warm run replaces the `log` with one `rev-list`, and adds the store's resolve. The
resolve costs 7 processes for the switch's `policy.py get` and 1 `rev-parse` in that fixture, and 8
plus 1 in gov's tree [PINNED, measured 2026-11-22]. The bound promised, PINNED and observed by AC3:

| Run | Git processes | `log --name-only` |
|---|---|---|
| warm, no new commit | today's count plus 8 in a fixture, plus 9 in gov's tree | none |
| warm, k new commits, k at most 500 | today's count plus 10, plus 11 in gov's tree | one, naming exactly the k ids |
| cold | today's count plus 9, plus 10 in gov's tree | today's one, over `HEAD` |

A RANGE run swaps its RANGE `log` for one `rev-list` as well, so the same deltas hold beside RANGE.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `LOG_BATCH_BOUND` | module constant, 500 | none | AC4 |
| `RECORD_BUCKET_HEX` | module constant, 2 | none | AC3 |
| `routed-commits` | the store's leg name, the leg's own `SAY` | none; the store's `LEG_RE` admits it | AC7 |
| a bucket's fields | the prefix, then the sha256 of its sorted member ids | none; the store's schema owns the key | AC5 |

No verb, flag, conf key, policy key, refusal number or column-0 function is minted.

### Files touched (estimate)

`tools/memory-tree/routed_commits.py`

### What the pass does not write

The fill and its steps sit inside `read_routed_commits` as nested functions, so the file gains no
column-0 function. The codebase map's generated symbol index, `memory/map/generated/symbols.json`,
which lists every column-0 function of this file, is not regenerated. The module's usage lines do
not change, and the path is not on the kickoff manifest's `watch:` line.

### Paths shared with order-2 units

None. Units 2, 3, 5, 7 and 8 name no path of this unit's. TOOL-dQuietDisk-9, at order 6, edits
`tools/memory-tree/commit_trailers.py`, a code path of this unit's key. That shares no file; its
landing makes the next run cold once.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| One item per commit, rev-3's design | 10,980 file creates on the cold run and again on each edit of a code path, which four paths took in 43 commits over the 30 days to 2026-11-22 [PINNED]. A warm run opens 10,980 files. The build's goal is fewer file creates. |
| One item per tip, holding the whole population | 7.5 MB written on each run that has a new commit, each copy kept 30 days by the store's prune. |
| A chain of delta items from the tip | An item would name its base inside its body, so one key could hold two bodies across worktrees, against the store's rule that an item is immutable per key. |
| Store each commit's verdict | The verdict reads HEAD's id map, so a spec added at HEAD flips an old commit's `no spec defines it at HEAD`; the key would need the whole map. |
| Grade only `<last>..HEAD` and carry the old counts | The summary counts and the deviation join read the whole population, and a stale waiver is judged over all of it. |
| A `--stdin` id list to `git log` | `read_commits` takes revision arguments and no stdin, and three kits share it as one reader. |

## 5. Production-readiness checklist

- security: records come from the repository's own history into the store under its git common
  dir. Nothing is pushed or rendered, and a forged item needs write access to the git dir, which is
  the store's stated limit.
- perf / scale: a warm run reads 256 items, about 7.5 MB, and runs no whole-history log. It
  spawns 8 or 9 more git processes than today (section 4). A cold run, and the first run after a
  code path's edit, costs today's log plus 256 creates; old items age out at 30 days.
- error / empty / loading states: a missing, torn, malformed or foreign item is logged again. A
  short log refuses at exit 2 and writes nothing (S5). A tip that no longer names a commit gives no
  old members, so that bucket's members are logged.
- observability: the summary lines are unchanged; the store prints its own stderr line only when it
  cannot resolve or the switch does not read.
- risks: git's trailer parse depends on the git version and on `trailer.*` config, and no key holds
  either. A git upgrade that parses a trailer differently keeps the old parse until the items age
  out or a code path moves. The deviation join's self-test calls `check_routed_commits` in-process,
  so it pays the resolve on each of those calls.
- testing: the equivalence corpus (AC1), the key moves (AC2), the counts (AC3), the planted red
  (AC4), the torn items and the short log (AC5), the switch (AC6), the adopter copy (AC7).
- migration: none; the first run is cold, and the switch restores today's read.
- user docs: the module docstring (S8). `help/reference/policy.md` already documents
  `tests.history-verdicts`, and no page under `help/` describes this read.

## 6. Acceptance criteria

The pass's probes run over a hermetic fixture repository F, built under `%TEMP%/<short-name>` with
`tools/memory-tree/routed_commits.py#build_fixture` and `#set_fixture_conf`. Both are called by
import, never through the module's `--selftest`. F holds at least 600 commits [PINNED], so a cold
run passes the 500 bound. It also holds:

- two specs, and routed commits naming their units;
- one routed commit that names no unit, so both legs exit 1;
- two `Red-fix:` commits, with `LEG_MANIFEST` naming a committed leg manifest;
- three merge commits of side branches, and one commit before the cutoff;
- a `main` branch at HEAD, so the switch's policy read answers in F.

F2 is F plus one commit that vendors the unit's memory-tree kit, the policy kit and the playbook
kit's `edges.toml` at the prefix `scripts/`. It mirrors the install an adopter gets from
`tools/govkit/fixtures/release-0/deploy.toml`, which lists `memory-tree` among its kits.

"Old" is the leg at `40def53f7`, run by path from a `git clone --shared` of this repository checked
out there under `%TEMP%`. "New" is the unit's leg, run by path from the build worktree. Both run
with the fixture as the working directory, and their stdout and stderr are compared together. A
reading over the real tree is the gate's own population, which a role agent may not run
(scratch-guard row G1). Each such reading below is owed to the main loop at the close.

- **AC1** — When old and new each run over F, the outputs and exit codes are byte-identical at each
  of five points: cold; warm at an unmoved HEAD; warm after one commit naming a unit; warm after a
  merge commit of a three-commit side branch; and with `GATE_PUSH_BASE` set to a commit 20 behind
  HEAD, cold and then warm. When the main loop runs `python tools/memory-tree/routed_commits.py`
  from the clone at `40def53f7` and from the build worktree, over one scratch `git clone --shared`
  of the real tree at the commit the bar runs on, the two are byte-identical there too, cold and
  warm.
  Red when: a record assembled from the store differs from the logged one, or the order moves.
  cost: about 30 minutes per real-tree run; the leg ceiling is 3,540 s [PINNED], `tools/gate-legs.json`.
  permission: the real-tree corpus is owed to the main loop; the pass makes the fixture comparison.
  fixture: the real-tree clone under `%TEMP%` with its own `TEMP`, taken at the merge commit the bar
  grades, never before it (`memory/gotchas/history-leg-graded-before-the-reconcile-commit.md`).
- **AC2** — When F2's vendored copy of `tools/playbook/edges.toml` gains one `[[trailer]]` row,
  the next run of F2's vendored new leg, under `GIT_TRACE2_EVENT=<dir>`, holds one `log` event whose
  argv carries `--name-only` over `HEAD`, and prints what the vendored old leg prints. The same
  holds when one comment line is appended to F2's vendored copy of `tools/memory-tree/tree_lib.py`.
  Red when: a bucket stored under the old table or the old library is reused.
- **AC3** — When new runs warm over F with no new commit and the four DESIGN_* keys blank, under
  `GIT_TRACE2_EVENT=<dir>`, the directory holds at most 8 files [PINNED] more than old's run over
  the same F, and no event's argv carries `--name-only`. When one commit is added and new runs
  again, it holds at most 10 files [PINNED] more than old's run, and one `--name-only` log names
  exactly that commit's id. When the main loop takes the warm count over the real-tree clone of AC1,
  with the four DESIGN_* keys blanked in that clone's working `.memory-tree.conf`, it holds at most
  9 files [PINNED] more than old's and no `--name-only` log.
  Red when: the whole-history log survives on the warm path, or the count grows with the commits.
  figure: 8, 9 and 10 are PINNED as the promise from section 4's counts, measured 2026-11-22.
  permission: the real-tree count is owed to the main loop.
- **AC4** — When a commit touching a path under `ROUTED_PATHS` that names no unit is added to F
  past the stored tip, both legs exit 1 and print the same violation line for it. New's trace holds
  one `--name-only` log naming that id, and the store's `items/` gains at most one file. When 501
  commits are added and new runs, its one `--name-only` log is over `HEAD`, as `LOG_BATCH_BOUND`
  states.
  Red when: the new commit is not read, it reads green, or a bucket it did not move is rewritten.
- **AC5** — When one bucket item under F's `history-verdicts/v1/routed-commits/items/` is truncated
  to half its bytes, the next run logs exactly that bucket's members and its output equals old's.
  The same holds when a bucket is rewritten with a valid header and a JSON body naming an id outside
  its members. When `read_commits` is patched, by import, in both old and new to drop the last
  record it parses, both exit 2 over a cold F with the same truncation refusal, and new's `items/`
  holds no file after.
  Red when: a torn or foreign body is trusted, or a short stream reads clean or writes.
- **AC6** — When F commits a `.governance/policy.toml` whose `[tests]` table holds
  `history-verdicts = "regraded"`, `python tools/policy/policy.py get tests.history-verdicts` in F
  prints `regraded`. New's next run then holds one `--name-only` log over `HEAD`, no `rev-list`
  without `--count`, and an unchanged `items/`, and its output equals old's.
  Red when: the switch at `regraded` still reads or writes the store.
- **AC7** — When F2's vendored new leg runs cold then warm, its output equals F2's vendored old leg
  at the same prefix, and the store's `items/` under F2's git dir is non-empty. When a
  `git worktree add --detach` of F2 at HEAD runs the vendored new leg, its trace holds no
  `--name-only` log, since the code paths are named relative to the repository. When
  `python tools/govkit/govkit.py check --target C:/projects/incms/main` and the same with
  `C:/projects/nicocares/main` run read-only from the clone at `40def53f7` and from the build
  worktree, each pair prints the same bytes and exit code.
  Red when: the store does not resolve beside a renamed kit dir, a second worktree misses every
  item, or either check reads differently.
  permission: read-only against the adopters' main checkouts, never their `gov-upgrade` worktrees.
  fixture: the adopters reach the change only after a minted version and their own `govkit update`.
- **AC8** — When `grep -c 'history verdict store' tools/memory-tree/routed_commits.py` runs, it
  prints 1 or more, and the paragraph names `tests.history-verdicts`.
  Red when: the docstring does not name the store and its switch.
- **AC9** — When `grep -n 'resolve_store' tools/memory-tree/routed_commits.py` runs, it prints the
  import, the fill's call, and a line inside `run_selftest` that replaces the name with an off store.
  Red when: the existing arms run the store, so their spawn counts move.

## 7. Gates

`routed commits name a specced unit` · `routed-commits selftest` · `policy fixtures` · `line length` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)` · `codebase-map coverage + freshness`

New arm: tools/memory-tree/routed_commits.py · covers AC4 AC5 · a `--selftest` arm over one fixture holding a lane commit, a merge and an unattributed routed commit, which compares the store-on read with the module's own store-off read, cold, warm, after one added commit and after one torn bucket; its failing case is staged by a fill that reads the buckets without logging the lack, and the arm patches `LOG_BATCH_BOUND` to 2 to cross it cheaply · none

The arm's oracle is the module's own store-off read, never the module at a literal sha
(`memory/gotchas/test-oracle-read-from-a-historical-sha.md`). The existing spawn arms keep holding,
since S7 runs them with the store off. The main loop observes the arm RED and then GREEN at the
close; a role agent runs no `--selftest` (scratch-guard row G3). The leg's budget row, 500 s [PINNED]
against 330 s [PINNED] measured (`tools/run-gates/selftest-budgets.txt`), absorbs one arm.

## 8. Open questions

- **F1 — The store's resolve costs 8 git processes per run in a fixture and 9 in gov's tree.**
  `resolve_store` reads `tests.history-verdicts` through `policy.py get`, which spawns 7 git
  processes in a fixture and 8 in gov's tree, and then one `rev-parse` for the git dir
  (`tools/lib/history_store.py#read_policy_mode`). The leg's warm run therefore spawns more git
  processes than today, while it saves the whole-history log's pack reads.
  - (a) Take the cost. Section 4's bound counts it, and the main loop files the ask against
    TOOL-dQuietDisk-1 for one mode read per leg run, the ask TOOL-dQuietDisk-2's F1 makes.
  - (b) Build the `HistoryStore` in the leg without `resolve_store`. That is a second resolver
    beside the one unit 1 gated byte-identical across its copies.
  - Recommendation: (a). It is bounded and does not grow with the commit count.
  RESOLVED (agent, 2026-11-22, delegated): (a), under the re-ground task's rule that a consuming
  unit follows the store as built.
- **F2 — An item that is hit is never refreshed.** `HistoryStore.write` skips a body it already
  holds, and `remove_aged` drops items by mtime after 30 days. The 256 buckets of a cold run share
  one write date, so the leg's run 30 days later is cold.
  - (a) Take the monthly cold run. It costs today's log once, and the main loop files the ask
    against TOOL-dQuietDisk-1 to touch an item on a hit, the ask TOOL-dQuietDisk-2's F3 makes.
  - (b) Rewrite hit items from the leg. The store skips an identical body, so this changes nothing.
  - Recommendation: (a).
  RESOLVED (agent, 2026-11-22, delegated): (a), under the same rule.

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.
- rev-2 · 2026-11-22 · S2 · section 6 · under `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task`.
  S2 spells the store's opener `resolve_store`, as TOOL-dQuietDisk-1 rev-3 renames it. Section 6 no
  longer has the pass run the leg over the real tree: AC1 to AC5 run old and new over a hermetic
  fixture built by the module's own `build_fixture`, and the real-tree corpus of AC1 and the
  real-tree count of AC3 are owed to the main loop at the close. The spec's own minted constant,
  `LOG_BATCH_BOUND`, sits in no lexicon cell, so nothing of its own needed a rename.
- rev-3 · 2026-11-22 · section 1 · section 3 · section 4 · section 6 · section 10 · wording only,
  under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. The analysis's commit count and wall time,
  TOOL-aMeasuredDrag-1's measured pickaxe cost, the fixture's commit floor, AC3's warm bound and
  dWitnessedBar's changed-line count are marked PINNED. Design, scope and acceptance unchanged.
- rev-4 · 2026-11-22 · section 1 · S1 to S8 · section 3 · section 4 · section 5 · AC1 to AC9 ·
  section 7 · section 8 · re-grounded at 40def53f7 (order 1 built, dWitnessedBar landed), under
  `2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task`. What moved: every citation re-pinned to the
  base's blobs; the store as built keeps one file per item and costs 8 or 9 git processes to
  resolve, so the design stores 256 buckets keyed by their members instead of one item per commit,
  whose 10,980 creates per cold run and per code edit the build's goal forbids; three callers pass
  two arguments, so `held` is a new optional parameter (S1); the existing self-test arms run with
  the store off (S7). Section 1 now says the analysis's 1,761 s [PINNED] is the leg's wall time on
  the loaded disk, and that the log pass measured 1.8 s with a warm cache. Acceptance gains AC6 (the switch),
  AC7 (the adopter copy, which the spec brief requires) and AC9; AC3's bound becomes a delta over
  the old leg's count, since the store's resolve adds a fixed 8. Section 8 names the store's two
  gaps. dWitnessedBar did none of this unit's work. The goal does not move.

## 10. Reuse audit

The seam extended is `read_routed_commits`
(`tools/memory-tree/routed_commits.py#read_routed_commits`), the leg's one log pass, through
TOOL-dQuietDisk-1's store as built (`tools/memory-tree/history_store.py#resolve_store`).
TOOL-aMeasuredDrag-1's findings record proposed a per-commit cache for history legs
(`memory/builds/aMeasuredDrag/build/2026-11-15-build-TOOL-aMeasuredDrag-1-findings-gate.md`, row
legs-1 and the routing note under it). Where the brief says to key each commit's verdict, this spec
keys its record, for the reason section 3 gives. The chain build owning the area is dWitnessedBar
(Test: gate health), with dScopedBuild (Build: the history-derived exit base). A grep of
dWitnessedBar's specs and `git log 59e882afd..fb6f1a74c` over the leg, the reader and `tree_lib.py`
found no cache of this read; its changes to these files are listed in section 4.

`python tools/codebase-map/reuse_lookup.py "group cached records into buckets keyed by their member set"`
returned name-token neighbours only (`key`, `records`, `read_records`, `derive_key`). No existing
seam fits beyond the leg's own reader and the store. Recall returned TOOL-dScopedBuild-1's second
caller of `read_routed_commits`, TOOL-aNimbleMend-10's limits pass, TOOL-dDeclaredLoop-40's floor
keys and TOOL-dTrueNorth-4, the deviation join. The source agreed with each, and the second caller
is why `held` is optional.

Recall terms used: routed_commits read_routed_commits read_commits history_store resolve_store history-verdicts log pass whole range deviation join commit_trailers incremental bucket
