# TOOL-dTotalRecall-116 — a blob-pinned record read returns a key only where the blob is that record's

**Status:** CLOSED · rev-2 · 2026-11-25 · node d · Tier-2 · base acbb74bb · streams tooling · order 44

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-dTotalRecall-116-1-builder-return.md](../build/2026-11-25-build-TOOL-dTotalRecall-116-1-builder-return.md) | journal | — |
| [2026-11-25-build-TOOL-dTotalRecall-116-2-acceptance-ledger.md](../build/2026-11-25-build-TOOL-dTotalRecall-116-2-acceptance-ledger.md) | log | — |
| [2026-11-25-build-TOOL-dTotalRecall-116-2-builder-return.md](../build/2026-11-25-build-TOOL-dTotalRecall-116-2-builder-return.md) | journal | — |
| [2026-11-25-build-TOOL-dTotalRecall-116-widen-29.md](../build/2026-11-25-build-TOOL-dTotalRecall-116-widen-29.md) | widen | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-116-build-2-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-116-build-2-brief.md) | journal | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-116-build-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-116-build-brief.md) | journal | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-116-divergence-fold-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-116-divergence-fold-brief.md) | journal | — |
| [2026-11-25-review-TOOL-dTotalRecall-115-closing-diff-review-round2.md](../reviews/2026-11-25-review-TOOL-dTotalRecall-115-closing-diff-review-round2.md) | diff-review | TOOL-dTotalRecall-115 TOOL-dTotalRecall-117 TOOL-dTotalRecall-118 TOOL-dTotalRecall-119 TOOL-dTotalRecall-120 TOOL-dTotalRecall-121 TOOL-dTotalRecall-21 |

<!-- /gen:spec-records -->

## 1. Goal

H2 of the closing review (findings 2 and 6): `record show`, `record budget`, the edge grammar's `id#tag` form and a
work order's `--read` all certify `<key>@<blob>` without testing that the blob holds the key. An unknown key returns
any blob whole, and a superseded record's text passes under another key. This unit refuses what it cannot verify.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/record_find.py#read_section`, given a blob: a key with no row of the served view and no
  indexed record row at that blob is refused, naming the key. Observed by AC1.
- **S2** — Given a blob and a known key: the index's record row of the key at that blob, else a row the blob's own text
  defines, else the file-name key of a path of the served view that git's history holds that blob at, through the new
  `check_blob_path`; with none, a FindError naming the key and the blob. The whole-blob fallback goes (§4). Observed by
  AC2 and AC3.
- **S3** — The returned `path` is the path the row was read at: for a blob the index holds under the key, a path the index
  holds that blob at, the served view's own first; for any other, the served path its row was extracted at; never
  the empty string (§4). Observed by AC3 and AC6.
- **S4** — Three plants of `record_find.py`, `blob-unknown-key`, `blob-foreign-text` and `blob-foreign-record`, each
  expecting exit 2, and their arms in `tools/memory-tree/check-memory-hygiene.test.sh` beside `unheld-blob`, which stays
  green. The module docstring says what an unverified blob is refused for. Observed by AC4.
- **S5** — The suite's `FLOOR_ASSERTIONS` rises by the assertions S4 adds, and its `shell-role` row takes the measured
  count through `ratchet.py widen`, unit `TOOL-dTotalRecall-116`. Observed by AC5.

## 3. Non-goals (OUT)

- The containment of `#<tag>` in its record, M5, which is `TOOL-dTotalRecall-121`'s.
- A key whose record left the tree, addressed at an old blob no index row holds: it is refused as unknown. Today's
  fallback answered it with whatever the blob held.
- A moved record read by its file name at an unindexed blob only its old path held: the history asked is the served
  view's path alone, so it is refused. A move that kept the bytes is read, its blob indexed at the new path.
- A change of the address grammar, the supersession read or the budget.

### Edges

- **consumes-from** external — the closing review's report and the landed units whose code it read
- **consumes-from** `TOOL-dTotalRecall-115` — its bytes of the symbol map, the shell-role rows, edited after it
- **hands-off** `TOOL-dTotalRecall-117` — this unit's bytes of the symbol map, the shell-role rows, the hygiene suite and its floor
- **hands-off** `TOOL-dTotalRecall-118` — this unit's bytes of the symbol map
- **hands-off** `TOOL-dTotalRecall-119` — this unit's bytes of the symbol map, the shell-role rows, the hygiene suite and its floor
- **hands-off** `TOOL-dTotalRecall-120` — this unit's bytes of the symbol map, the shell-role rows, the hygiene suite and its floor
- **hands-off** `TOOL-dTotalRecall-121` — this unit's bytes of the symbol map, the shell-role rows, the hygiene suite and its floor, the record finder
- **hands-off** external — the close's next bar, the held suites and the landing, each the main loop's

## 4. Design

Read at `acbb74bb` on 2026-11-25 and run over this worktree: `read_section('.', …)` returned `NO-SUCH-KEY` with path
`''` over lines 1 to 121 of `README.md` (DERIVED, that blob), and `TOOL-dTotalRecall-114` over a widen record's
whole blob, lines 1 to 8 (DERIVED, that blob).

**The report is wrong on one point.** Its fix asks the extraction of the blob's text for a record row of the key. For a
key that is a file's stem that test passes every blob: `tools/playbook/record_extract.py#extract_record` emits the
stem's row from the path alone, so the builder-return's stem over `README.md`'s blob yielded its row over two planted
lines (DERIVED 2026-11-25, that call). A row keyed by an id comes from the text, and the test holds there. So the stem
case asks git where the blob has been.

### The blob branch

```python
sha, text = read_git_blob(root, blob)
held = con.execute(…).fetchone()                     # the index's record row, as today
secs = [...]                                         # as today
path = next((r["path"] for r in rows if r["blob"] == sha), "")   # S3: where the served view holds this blob
if held is not None and not path:                    # S3: a blob another tree of this node holds
    got = [p for (p,) in con.execute("SELECT DISTINCT path FROM path_row WHERE blob=? AND kind='record'", (sha,))]
    if not got:
        raise FindError(f"blob {sha} stands at no path the index holds")
    path = min(got, key=lambda p: (pathlib.PurePosixPath(p).stem != key, p))
if held is None and not rows:                        # S1
    raise FindError(f"key {key} names no record of the served view, and blob {sha} holds no indexed row of it")
if held is None:                                     # S2: the index does not hold the blob under this key
    _ti, rx = load_tag_index()
    for cand in dict.fromkeys(r["path"] for r in rows):
        found = [(r[2], r[3]) for r in rx.extract_record(ctx, cand, text) if r[1] == "record" and r[4] == key]
        stem = pathlib.PurePosixPath(cand).stem == key
        if found and (not stem or check_blob_path(root, sha, cand)):
            held, path = found[0], cand
            secs = [(r[0], r[2], r[3]) for r in rx.extract_section(ctx, cand, text)]
            break
    if held is None:
        raise FindError(f"blob {sha} is no version of {key}")
```

**The path rule, one rule for every answer.** A key stands in several files as a rule: 1284 of 16160 (DERIVED 2026-11-25, the
first pass's read of the index). `rows[0]` names the first of them whatever blob was asked, so `TOOL-cSpliceWarden-6` at
the blob of `memory/DECISIONS.md` and at its `BACKLOG.md`'s came back under its spec's path with the other file's line
(DERIVED 2026-11-25, `read_section` over HEAD), a path `resolve_edge` and `gov_tag.py show` print as `path:line`. So an indexed
blob answers with a path that holds it. An unindexed one answers with the served path its row was extracted at, which
is the key's file today and no claim that the blob stood there: an id key at another record's old blob is admitted
below, and the archive's old blob of an id that `memory/DECISIONS.md` defines too reads `memory/DECISIONS.md`. The empty `got` is
not reachable while `tag_index.py#remove_unheld_rows` drops path and blob rows together; it refuses and never
answers empty.

`check_blob_path(root, sha, path)` is true where `git --literal-pathspecs log --all --reflog -m -1 --format=%H
--find-object=<sha> -- <path>` prints a commit: the blob stood at that path in some commit this clone holds, an amended one included. It ran
in about 2 s over this repository's whole history (PINNED 2026-11-25, node d), and only a stem key at an unindexed
blob reaches it. A refused git is a FindError naming it, never a yes. `--literal-pathspecs` is in the call because the
path is a file's name and never a pattern: a record name holding `*`, `?` or `[` would otherwise match its neighbours and
certify a blob only a neighbour held. It is git's own option, so it stands before the verb, as `design_lib.py` spells it.

An id key needs no such read: another record's blob that defines the id is a version of that id's text, which is
what the address asks for.

### The plants

Each runs over the fixture's `deviation-1` record. `blob-unknown-key`: `show NO-SUCH-KEY@<its blob>`.
`blob-foreign-text`: its stem at the blob of the fixture's `memory/README.md`, no record. `blob-foreign-record`: its
stem at a second deviation's blob, which the index holds under that record's own key. Each prints `refused show:` and
exits 2. On today's code each exits 0.

### Inventory

Minted: `check_blob_path` in `record_find.py` (python-function, verb `check`); three plant names.

### Files touched (estimate)

- `tools/memory-tree/record_find.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `memory/project/shell-role.txt`
- `memory/map/generated/`
- `memory/builds/dTotalRecall/build/` (the widen record and this unit's ledger)

### Alternatives rejected

- **The report's extraction test alone.** It certifies a stem key over any blob, as above; its own second plant, a
  known key with another record's blob, would stay at exit 0.
- **`git ls-tree` for the path.** A blob the current tree holds at a record's path is already an index row; a blob no
  tree holds is in no `ls-tree`.
- **Refusing a stem key at any unindexed blob.** It ends the unheld-blob read spec `TOOL-dTotalRecall-9` S5 asks for.

## 5. Production-readiness checklist

- security — deny by default: an address that names nothing verifiable is refused.
- perf / scale — one history read, about 2 s (PINNED 2026-11-25, node d), for a stem key at an unindexed blob alone.
- error / empty / loading states — a blob git lacks, an unknown key and a foreign blob are three named refusals.
- observability — the refusal names the key and the blob's full sha.
- risks — a clone whose reflog has expired refuses an amended-away blob it still holds; the address cannot be
  verified there.
- testing — AC1 to AC6 by the pass; §7's arms by the main loop.
- migration — none: the tree's pinned addresses are read through the same branch, and an address that was right stays.
- user docs — N/A, no page states the fallback.

## 6. Acceptance criteria

- **AC1** — When `python record_find.py --fixture --plant blob-unknown-key` runs from `tools/memory-tree/`, it prints a
  `refused show: key NO-SUCH-KEY` line and `fixture blob-unknown-key · exit 2`.
  Red when: the blob is returned under the key. Today it exits 0.
- **AC2** — When `--plant blob-foreign-text` and `--plant blob-foreign-record` run there, each prints `is no version of`
  and `exit 2`.
  Red when: a stem key takes the row its path alone gives. Today each exits 0.
- **AC3** — When `--plant unheld-blob` runs there, it prints `the second`, never `the third`, and `exit 0`; and a probe
  calling `read_section` on that address reads a `path` ending `deviation-1.md`.
  Red when: `check_blob_path` reads the branches alone, so the amended-away blob is refused, or the path is empty.
- **AC4** — When a probe over this worktree calls `read_section` with `NO-SUCH-KEY` and with
  `2026-11-25-build-TOOL-dTotalRecall-114-1-builder-return` at the blob of `README.md`, each raises `FindError`, and the
  second at its own file's blob returns its text.
  Red when: either foreign address is certified.
  cost: one index read, minutes on a cold cache.
- **AC5** — When `grep -c 'run_find_plant blob-' tools/memory-tree/check-memory-hygiene.test.sh` runs, it prints 3 (DERIVED,
  S4), the suite's `FLOOR_ASSERTIONS` stands above its value at `acbb74bb` by the assertions added, and its `shell-role`
  row holds the measured count of `python tools/gate-lint/sh_hygiene.py --shell-role --measure . ':!memory/'`.
  Red when: an arm lands and the floor or the row stands.
- **AC6** — When a probe over a fixture repository whose `DEC-tFix-1` is defined in `memory/DECISIONS.md` and in an archived
  decisions file calls `read_section` with the id at each file's own blob, each returned `path` is that file and each
  `line` is that file's; and once the archived file is edited and committed, the id at its former blob reads the path
  `memory/DECISIONS.md` and the former text.
  Red when: the path is `rows[0]`'s whatever blob was asked. Today both blobs return one path.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `encoding posture (text IO names its encoding)` · `python reads (a name never bound, an import outside its guard)` · `portability (shell lines only shrink)` · `recall floor` · `recall floor arms` · `ratchet (never gains)` · `ratchet (both ways)` · `memory-hygiene self-test` · `edges (every declared edge parses, is registered and resolves)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC2 · the three plants, red on today's fallback, and `blob-foreign-record` red on `check_blob_path` cut · `FLOOR_ASSERTIONS` by the assertions added

## 8. Open questions

- **F1 — Which binding line does a unit the closing review added carry?** The carries join reds a chain spec carrying
  nothing and derived from nothing. Options: (a) `**Derived:**` naming `PLAY-dClosedLoop-2`, the ruling that a chain run
  carries the units it adds, as `TOOL-dTotalRecall-114` §8 F1; (b) a part of another unit's clause, which the parts join
  reds. RESOLVED (agent, 2026-11-25, delegated): (a), the one survivor. widens: none · relaxes: none
- **F2 — How is a file-stem key verified against a blob the index does not hold?** Options: (a) the history of its path,
  `git log --find-object`; (b) the report's extraction, which any blob passes; (c) always refused, which ends a read
  a landed spec states. RESOLVED (agent, 2026-11-25, delegated): (a), the one option that tells the two apart.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft, from the closing review's H2.
- rev-2 · 2026-11-25 · S2 S3 §3 §4 AC6 · the first pass's divergence folded: one path rule, an indexed blob's own path and
  an unindexed blob's served one, the moved record's refusal, `--literal-pathspecs`; from
  `2026-11-25-prompt-TOOL-dTotalRecall-116-divergence-fold-brief`.

## 10. Reuse audit

The seams, each read at `acbb74bb`: `record_find.py#read_git_blob` and `record_find.py#scan_records`;
`tools/playbook/record_extract.py#extract_record`, its stem row and its id rows; the index's `path_row` and
`blob_row` tables; `record_find.py#run_fixture`'s plant table. `python tools/codebase-map/reuse_lookup.py "read a record
addressed by key and blob"` ranked generic readers alone: no existing seam fits the path-history read. The task's
build-folder walks and `id_grammar.py#read_kept_reason` read no blob.

Recall terms used: `python tools/memory-recall/query.py "record read by key and blob" --terms "blob pinned record show unknown key read budget FindError supersession"`
