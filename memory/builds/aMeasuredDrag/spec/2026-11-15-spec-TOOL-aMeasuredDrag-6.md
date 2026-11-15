# TOOL-aMeasuredDrag-6 — the index renderer groups the tracked list by build once, instead of scanning it per build

**Status:** CLOSED · rev-1 · 2026-11-15 · node a · Tier-1 · base aebbb4a7 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aMeasuredDrag-6-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-6-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md) | research | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-6-1-builder.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-6-1-builder.md) | journal | — |
| [2026-11-15-review-TOOL-aMeasuredDrag-1-11-closing-diff-round1.md](../reviews/2026-11-15-review-TOOL-aMeasuredDrag-1-11-closing-diff-round1.md) | diff-review | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 |

<!-- /gen:spec-records -->

## 1. Goal

`collect` in `tools/memory-tree/gen_build_index.py` scans the whole tracked memory list once per
build for its specs, up to four times per build for its record kinds, and once per build with a
per-kind test for its documents. This unit groups the tracked list by build slug once, and each build
filters only its own paths. Every rendered artifact stays byte-identical. Finding records-8 of the
2026-11-15 performance review, CONFIRMED at about 3 s of the renderer's wall time. PINNED 2026-11-15

## 2. Scope (IN)

- **S1** — `collect` builds one map from build slug to that build's tracked paths, once, before its
  per-build loop. A path joins the map when it starts with `<MEMORY_ROOT>/builds/` and carries a
  further `/` after the next segment; that segment is its key. Each list keeps `tracked` order.
  Observed by AC1, AC2 and AC3.
- **S2** — inside the loop, the `specs` filter, the `kinds` filter and the `docs` filter read the
  build's own list from that map, an empty list when the slug has none, in place of `tracked`. Each
  predicate is unchanged. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- The refusal branch's own-paths scan at `tools/memory-tree/gen_build_index.py@5a0864b87628:1152`.
  It runs only for a folder with no tracked README, 6 of 218 folders at `6d98c39ca` (PINNED).
- `rosters`, the `slugs` derivation at `:1120`, and any parse or blob cache. A content-keyed cache is
  §5 structural work of the review, not a quick win.
- Any change to what `collect` returns or what any renderer prints.
- The other edits this build makes to the same file. TOOL-aMeasuredDrag-3 memoises
  `read_carries_coverage` at other lines, and the `order` verbs sequence the two passes, so their
  write sets never run at once.
- The kit version. `tools/push-main.sh@c7cd70b96d5b:26-31` mints it at the landing, so a branch owes
  no bump.
- Any help page, and any adopter repository.

## 4. Design

### Evidence

Read at `6d98c39ca`. No file under `tools/` differs between it and the base `aebbb4a7`.

- `tracked` is a list, `git ls-files -- <MEMORY_ROOT>/` in git's order
  (`tools/memory-tree/gen_build_index.py@5a0864b87628:1116`). `slugs` is the sorted set of each
  build path's third segment (`:1120`), so no slug carries a `/`.
- The three per-build scans are `:1179` for `specs`, `:1199-1200` for `kinds` and `:1211-1212` for
  `docs`. Each tests `t.startswith(f"{m}/builds/{slug}/...")` over all of `tracked`.
  `RECORD_KINDS` is four folders (`tools/memory-tree/tree_lib.py@54a65cd4d0c4:409`).
- Both outputs have readers. `docs` feeds `derive_last_record` (`:1932`), and `kinds` feeds the
  record-folder count of the index region (`:1581`).
- Measured by this writer at `6d98c39ca` over 12040 tracked paths (PINNED) and 218 build folders
  (PINNED), the three scans together took 3.15 s of a 11.46 s `collect` (PINNED at `6d98c39ca`).
  The specs scan took 0.27 s, kinds 0.63 s and docs 2.07 s (PINNED at `6d98c39ca`). Building the
  map took 0.007 s (PINNED at `6d98c39ca`), and for every slug the map's list equalled the scan's.
- Why the outputs cannot move: for a slug with no `/`, `t.startswith(f"{m}/builds/{slug}/")` holds
  exactly when `t` starts with `<MEMORY_ROOT>/builds/` and the part after it partitions at its first
  `/` into that slug and a separator. The map holds those paths and only those, in `tracked` order.
  Every filter applied to that sub-list returns the same members, and `sorted` and `any` do not
  depend on what the sub-list leaves out.
- No two slugs in the tree are prefixes of one another at `6d98c39ca`, so AC2 adds a fixture pair.

### The change

Before the loop at `:1139`, in the shape below. Inside the loop, `specs`, `kinds` and `docs` read
`by_slug.get(slug, [])` where they now read `tracked`. No new function is minted.

```python
    # Each build folder's tracked paths, grouped ONCE in `tracked` order (TOOL-aMeasuredDrag-6):
    # the per-build filters below read their own build's list, not the whole tree's.
    in_builds = f"{m}/builds/"
    by_slug: dict = {}
    for p in tracked:
        if p.startswith(in_builds):
            head, sep, _ = p[len(in_builds):].partition("/")
            if sep:
                by_slug.setdefault(head, []).append(p)
```

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`

## 5. Acceptance criteria

Every command runs in Git Bash. `$S` is the session's scratchpad, spelled absolute. The clone sits
under the `md6` folder of `%TEMP%`, because a clone under the scratchpad's long path fails on
Windows. `--write` rewrites tracked files, so it runs only in the clone, never in the worktree. The
clone is made from the worktree root after the pass commit, so its `HEAD` is that commit.

```bash
C="$(cygpath -u "$TEMP")/md6"; G=tools/memory-tree/gen_build_index.py
rm -rf "$C" && git clone -q . "$C" && cd "$C" && B=$(git rev-parse HEAD^)
render() { python "$G" --write 2>&1; echo "rc=$?"; git add -A -- . ":!$G"
           echo "tree $(git write-tree)"; git reset -q --hard; }
render > "$S/md6-write-after.txt"
git show "$B:$G" > "$G"; render > "$S/md6-write-before.txt"
P='import hashlib,json,sys; sys.path.insert(0,"tools/memory-tree"); import gen_build_index as g
r=g.run("git","rev-parse","--show-toplevel").strip(); b=g.collect(r,g.load_conf(r))
print("collect", hashlib.sha256(json.dumps(b,sort_keys=True,default=repr).encode()).hexdigest())'
cp -r memory/builds/aCarriedStop memory/builds/aCarriedStopX
sed -i 's/^slug: aCarriedStop$/slug: aCarriedStopX/' memory/builds/aCarriedStopX/README.md
git add -A && git -c user.name=t -c user.email=t@t commit -qm fixture
PYTHONHASHSEED=0 python -c "$P" > "$S/md6-collect-after.txt" 2>&1
git show "$B:$G" > "$G"; PYTHONHASHSEED=0 python -c "$P" > "$S/md6-collect-before.txt" 2>&1
git checkout -q -- "$G"
```

- **AC1** — When the block runs, `diff "$S/md6-write-before.txt" "$S/md6-write-after.txt"` prints
  nothing. Each file holds the renderer's lines, `rc=0`, and one `tree` line naming the tree the
  render left behind, so equal files mean byte-identical artifacts over the real tree.
  Red when: a filter reads the wrong list, so a build's documents, record folders or units move, a
  rendered region changes, and the `tree` lines differ.
  cost: one render took 59 s at `6d98c39ca` (PINNED), and the block runs two renders and two
  `collect` passes.
- **AC2** — When the block runs, `diff "$S/md6-collect-before.txt" "$S/md6-collect-after.txt"`
  prints nothing, and each file ends in one `collect` line naming the hash of `collect`'s whole return.
  The fixture build `aCarriedStopX` is a copy of `aCarriedStop`, so its slug has a prefix sibling.
  Red when: the key is the slug without its separator, so `aCarriedStop` collects `aCarriedStopX`'s
  paths too and the hashes differ.
  fixture: built by the block in the clone; the tree has no prefix pair of its own.
  figure: the hash is DERIVED at observation. `PYTHONHASHSEED=0` holds it stable; two runs at
  `6d98c39ca` printed one value.
- **AC3** — When `collect` is timed in the clone with each generator, beside 10 runs of
  `/usr/bin/true`, the after time is below the before time, and both go in the acceptance ledger.
  Red when: a per-build scan of `tracked` survives, and the two times stay level.
  figure: the after time is DERIVED at observation. The before figures were measured by this writer
  on node a at `6d98c39ca`:
  11.46 s for `collect` in the worktree, PINNED at `6d98c39ca`.
  0.28 s per 10 runs of `/usr/bin/true`, PINNED at `6d98c39ca`.

  ```bash
  T='import sys,time; sys.path.insert(0,"tools/memory-tree"); import gen_build_index as g
  r=g.run("git","rev-parse","--show-toplevel").strip(); c=g.load_conf(r); t=time.perf_counter()
  g.collect(r,c); print(f"collect {time.perf_counter()-t:.2f} s")'
  python -c "$T" | tail -1; git show "$B:$G" > "$G"; python -c "$T" | tail -1; git checkout -q -- "$G"
  time (for i in 1 2 3 4 5 6 7 8 9 10; do /usr/bin/true; done)
  ```

## 6. Gates

`build-index selftest` · `tier2-review self-test` · `policy fixtures` · `verdict epoch (kit version dates the engine)`

The build-index selftest drives `collect` over its fixture trees. The tier2-review and policy legs
guard this file by name. The epoch leg grades the engine's move at the push boundary, where the
lander's mint dates it. No arm is added or moved: AC1 and AC2 are the equality observations, and a
speed regression has no arm that could fail on it alone.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-15 · initial draft from the build brief `2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief`,
  item 6, grounded at `6d98c39ca`, whose `tools/` tree matches the base `aebbb4a7`. The brief names
  `:1199-1200` and `:1211-1212`; S2 also moves the `specs` filter at `:1179`, the same scan of the
  same list, at no extra line cost.

## 9. Reuse audit

No existing seam fits. `python tools/codebase-map/reuse_lookup.py "group tracked paths by build slug once instead of scanning the whole list per build"`
ranked `tracked` in `tools/govkit/govkit.py` and `build_records` in
`tools/memory-tree/migrate_backlog.py` first, and neither groups paths by build. A grep for
`by_slug` over `tools/memory-tree/` found only `roster_by_slug`, which maps slugs to ids, not to
paths. The edit is in place in `collect`, the function the finding cites. Recall returned the
dFramedEntrypoint round-1 diff review, which priced the same `docs` comprehension when it had no
reader; `derive_last_record` reads it again today.

Recall terms used: `python tools/memory-recall/query.py "how does the build index renderer collect each build's specs, record kinds and documents from the tracked list" --terms "gen_build_index collect tracked ls-files slug record kinds docs inventory renderer scan per build grouping"`
