# TOOL-aHastenedSweep-2 — `selectable` computes each basename once, and `walk` derives its roots once

**Status:** CLOSED · rev-1 · 2026-11-15 · node a · Tier-2 · base f25308f0 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aHastenedSweep-2-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aHastenedSweep-2-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-prompt-TOOL-aHastenedSweep-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aHastenedSweep-1-brief.md) | research | TOOL-aHastenedSweep-1 TOOL-aHastenedSweep-3 TOOL-aHastenedSweep-4 |
| [2026-11-16-review-TOOL-aHastenedSweep-1-2-3-4-diff-review-round1.md](../reviews/2026-11-16-review-TOOL-aHastenedSweep-1-2-3-4-diff-review-round1.md) | diff-review | TOOL-aHastenedSweep-1 TOOL-aHastenedSweep-3 TOOL-aHastenedSweep-4 |

<!-- /gen:spec-records -->

## 1. Goal

Two Python delegates of the hygiene shell repeat pure work once per item. `gotchas.selectable`
calls `os.path.basename` on the anchor and on every tracked path for every anchor, and
`corpus_ids.walk` rebuilds the set of top-level directories from the whole tracked set for every
citation it judges. This unit computes each path's basename once per process, the anchor's once per
call, and the roots once per walk, with every predicate unchanged. The analysis measured
`gotchas.py --check` at 227 s shipped against 34.5 s with both memos, output identical, PINNED
2026-11-15 on node a (the build's brief, item 2).

## 2. Scope (IN)

- **S1** — `selectable` in `tools/memory-tree/gotchas.py` computes `os.path.basename(anchor)` once
  per call, and reads each path's basename from a module-level dict `_BASENAMES`, filled by
  `os.path.basename` on a path's first lookup. The catalogue's self-exclusion, the two substring
  tests and their order are kept, so the function returns the same set for every input. Observed
  by AC1 and AC3.
- **S2** — `walk` in `tools/memory-tree/corpus_ids.py` binds `roots = _roots(tracked_set)` once,
  right after `tracked_set` is built, and the citation test reads `roots`. `_roots` itself is kept
  as it is. Observed by AC2 and AC3.
- **S3** — `gotchas.py --check` and `corpus_ids.py --check` print byte-identical output with the
  same exit codes as the shipped modules on the live tree. Observed by AC3.

## 3. Non-goals (OUT)

- Any change to what `selectable` admits, to `derive_anchor_tier`, to `normalise_paths`, or to a
  caller of `selectable`.
- Any change to `_roots`, to the citation rules of check 15, or to `ask_shell`. The index set the
  shell hands down, and the one shared walk, are other units of this build.
- A memo of `walk` itself, or any cache that outlives the process.
- The memory-tree kit version constant `KIT_MEMORY_TREE_VERSION`. This unit does not move it.
- The R5 commit recipe, the render stamp, R6, and the spec-writer prompt's hygiene scope. The owner
  holds those.
- `memory/builds/dDeclaredLoop/`, the worktree `unattended-declared-loop-d56bf0`, its branch and
  its run-state file.

### Edges

- **hands-off** external — the memory-tree kit version: this unit leaves `KIT_MEMORY_TREE_VERSION`
  as it is, and the build's brief places its one move in the build's last unit, which the verdict
  epoch leg holds owed at the lander.
- **hands-off** external — the live-tree A/B of AC3 and the close's legs of §7. Both are the main
  loop's, at the close, recorded in this unit's acceptance ledger under a `Pass: none` commit.

## 4. Design

### Evidence

Read at f25308f0.

| Fact | Where |
|---|---|
| `selectable` returns `{p for p in paths if not p.startswith(skip) and (anchor in p or p in anchor or os.path.basename(p) == os.path.basename(anchor))}`. | `tools/memory-tree/gotchas.py#selectable`, the predicate at `tools/memory-tree/gotchas.py@0cb445ff:347-350` |
| Its callers are `inert_only`, `scan_dead_anchors`, the `--for-paths` checklist and `derive_moved_invariants`. | `tools/memory-tree/gotchas.py@0cb445ff:379`, `:392`, `:751`, `:756`, `:785` and `:823` |
| `normalise_paths` brings caller paths to the repo-relative POSIX shape before they reach `selectable`. | `tools/memory-tree/gotchas.py#normalise_paths` |
| No code in `gotchas.py` rebinds `os.path` or patches `os.path.basename`. | `grep -n "posixpath\|ntpath\|setattr" tools/memory-tree/gotchas.py` finds one docstring line |
| `walk` builds `tracked_set = set(tracked)` once and never adds to it or takes from it. | `tools/memory-tree/corpus_ids.py@d5bd676f:455-456` |
| The citation test calls `_roots(tracked_set)` inside the per-token loop. | `tools/memory-tree/corpus_ids.py@d5bd676f:569` |
| `_roots` is `{p.split("/", 1)[0] + "/" for p in tracked_set if "/" in p}`, a pure function of its argument, and line 569 is its only caller. | `tools/memory-tree/corpus_ids.py#_roots` |
| `gotchas.py --check` reaches `walk` through `load_defined_ids` when the catalogue holds an invariant. | `tools/memory-tree/gotchas.py@0cb445ff:185` and `tools/memory-tree/gotchas.py@0cb445ff:596` |

The analysis profiled, PINNED 2026-11-15 on node a: `selectable` at 1,349 calls making 33M
`ntpath.basename` calls, 78% of the module's profile (PINNED); and `_roots` at 3,889 rebuilds over
about 12.6k paths, about 37% of the `corpus_ids.py --check` profile (PINNED).

### Why each memo is exact

A path's basename is a pure function of the path string within one process, since `os.path` is
fixed at import and nothing here rebinds it. A dict keyed by that string therefore returns what the
call would. A backslash path is keyed by its own spelling, so it keeps the platform's answer. The
anchor's basename is computed per call and never kept, so a later call with another anchor cannot
read it. `_roots` reads only `tracked_set`, which the loop never changes, so one call before the
loop returns what every call inside it returned.

### S1: the selection predicate

```python
_BASENAMES: dict = {}   # path -> os.path.basename(path), once per process (TOOL-aHastenedSweep-2 S1)


def selectable(anchor: str, paths, m: str) -> set:
    """<docstring unchanged>"""
    skip = f"{m}/gotchas/"
    base = os.path.basename(anchor)
    out = set()
    for p in paths:
        if p.startswith(skip):
            continue
        if anchor in p or p in anchor:
            out.add(p)
            continue
        b = _BASENAMES.get(p)
        if b is None:
            b = _BASENAMES[p] = os.path.basename(p)
        if b == base:
            out.add(p)
    return out
```

The docstring keeps "THE ONE COPY of the selection predicate" and gains one sentence naming the
memo. The order of tests matches the shipped expression's short-circuit order, so a path that a
substring test admits is never looked up. An empty basename is stored as the empty string, which
`get` returns as itself and not as `None`.

### S2: the roots

In `walk`, right after `tracked_set = set(tracked)`:

```python
    roots = _roots(tracked_set)   # once per walk: _roots is pure and the loop never changes tracked_set (TOOL-aHastenedSweep-2 S2)
```

and the test at `tools/memory-tree/corpus_ids.py@d5bd676f:569` reads
`if cited.split("/", 1)[0] + "/" not in roots:`. The case-1 and case-2 comment above it stays.
`_walk_continues` derives its obligations from the AST, so adding a statement moves no
reachability arm.

### What this does not check

- That a memo stays small. `_BASENAMES` holds one entry per distinct path the process saw, which is
  the tracked set plus fixture paths, and it is freed with the process.
- Speed. AC3 records each side's wall time, and no gate holds a figure.

### Inventory

One module-level dict, `_BASENAMES`, in `tools/memory-tree/gotchas.py`, and one local, `roots`, in
`walk`. The lexicon declares the cells `py.function` and `py.type` for Python and no `py.constant`
cell (`python tools/lexicon/lexicon.py --suggest _BASENAMES --as py.constant` says so), and it
grades no local, so neither name has a cell to answer in. No function, flag, key, leg or file is
minted.

### Migration

None. An adopter receives both modules on its next kit update, and no verdict moves.

### Rollout

No switch. The pass runs `python -m py_compile` over both modules, then AC1 and AC2, then
`python tools/codebase-map/gen_map.py --write`, and commits whatever that rewrites with the code.

### Files touched (estimate)

- `tools/memory-tree/gotchas.py`
- `tools/memory-tree/corpus_ids.py`
- `memory/builds/aHastenedSweep/build/2026-11-15-build-TOOL-aHastenedSweep-2-1-acceptance-ledger.md`

### Alternatives rejected

- **`functools.lru_cache` around `os.path.basename`.** Equally exact, but it adds a wrapper call on
  every pair, and the brief names a dict.
- **Precomputing every path's basename per call.** It pays the full basename cost once per anchor,
  which is the cost being cut.
- **Passing `roots` into `walk` from the caller.** No caller holds it, and the walk is the one place
  that builds `tracked_set`.

## 5. Production-readiness checklist

- security — No input boundary moves. Both memos read only strings the modules already hold.
- perf / scale — PINNED 2026-11-15, node a, contended: `gotchas.py --check` measured 227 s
  shipped and 34.5 s with both memos (PINNED), and 115 s inside a traced full run, against an
  expected 20 s to 35 s (PINNED).
- error / empty / loading states — An empty path list returns an empty set on both paths. An empty
  basename is a stored value, not a miss.
- observability — None owed. The output is byte-identical, so nothing new is printed.
- risks — A memo keyed by anything but the full path string would merge two paths. §4 keys it by
  the path, and AC1 calls two anchors in turn over one list so that a kept anchor value shows.
- testing — AC1 and AC2 compare the changed functions with the shipped ones over hand-built inputs.
  AC3 compares the two CLIs on the live tree. The modules' selftest arms run at the close.
- migration — None (§4, "Migration").
- user docs — No page under `help/` describes either module's cost, and no behaviour a user sees
  moves.

## 6. Acceptance criteria

- **AC1** — When a probe imports `selectable` from the changed `tools/memory-tree/gotchas.py` and
  from the shipped copy, and calls each with five anchors over one path list, in order and then in
  reverse, every pair of returned sets is equal. The anchors, written here unquoted because they
  name fixture paths and not tracked ones, are other/some-gate.sh, `INDEX.md`, deep/nested/,
  `nested` and deep/nested/some-gate.sh. The paths are tools/some-gate.sh,
  deep/nested/some-gate.sh, the same path spelled with backslashes, docs/INDEX.md,
  `memory/gotchas/INDEX.md` and `memory/README.md`. The other/some-gate.sh call admits by basename
  alone: it returns the two forward-slash some-gate.sh paths, plus the backslash one where
  `os.path` is `ntpath`. The `INDEX.md` call returns docs/INDEX.md alone.
  Red when: the anchor's basename is kept across calls, so the `INDEX.md` call also admits the
  some-gate.sh paths; or the self-exclusion test moves behind the substring tests, and
  `memory/gotchas/INDEX.md` is admitted.
  fixture: the probe is a script under the run's scratchpad. The shipped copy is
  `git archive f25308f0 tools` unpacked there and loaded by path through `importlib.util`.
- **AC2** — When a probe builds one fixture repository with the changed module's `_scratch`, with
  `DEAD_PATH_PIN` set to `0`, then `checks(walk(root, conf))` from the changed module and from the
  shipped copy return equal lists. The fixture adds a tracked file tools/kit/check.sh, and a
  `memory/HYGIENE.md` that cites three tokens: kit/check.sh, a real file written at the wrong
  prefix; tools/gone/never.sh, a dead path under a real root; and nosuchroot/x.md, which has no
  root and no tracked tail. Both lists name the first two tokens, and neither names the third.
  Red when: the roots are derived from anything but the whole tracked set, such as the memory
  corpus alone, so `tools/` is no root and tools/gone/never.sh is skipped as unrooted.
  fixture: the repository goes under %TEMP% at a short name such as `hs2fx`, because it is a git
  repository. The tree holds none today.
- **AC3** — When `python tools/memory-tree/gotchas.py --check` and
  `python tools/memory-tree/corpus_ids.py --check` run on the live tree at one commit, each beside
  the same command from the shipped copy, each pair's outputs are `cmp`-identical with the same exit
  code, and the acceptance ledger records the four wall times and each output's line count.
  Red when: a path or citation is admitted on one side and not the other, or a line's order moves.
  cost: the shipped `gotchas.py --check` measured 227 s, PINNED 2026-11-15 by the analysis.
  permission: the main loop observes this at the close, as the build's brief assigns.
  figure: the four wall times are DERIVED at the observation.

## 7. Gates

`memory hygiene` · `gotchas selftest` · `corpus-ids selftest` · `verdict epoch (kit version dates the engine)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `playbook render selftest` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

The close's bar runs these once, after the last unit. The `gotchas selftest` leg carries the arms
the analysis names: check 19's dead anchor and the `--report` dead anchor at
`tools/memory-tree/gotchas.py@0cb445ff:1044-1049`, the inert anchor at
`tools/memory-tree/gotchas.py@0cb445ff:1028`, and the `selectable` arms for the directory anchor,
the basename arm and the catalogue's self-exclusion at
`tools/memory-tree/gotchas.py@0cb445ff:1078-1086`. The `corpus-ids selftest` leg carries the
dead-citation arms that the roots gate, at `tools/memory-tree/corpus_ids.py@d5bd676f:1452`,
`:1473`, `:1484` and `:1505`, and the read-path arm at `tools/memory-tree/corpus_ids.py@d5bd676f:1558`.
Each was seen red when written. The `verdict epoch` leg reads an engine move with no version move
as owed at the lander, not as a red off the push boundary.

This unit adds no arm and moves none. AC1 and AC2 are its direct observations of the classes those
arms guard.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.

## 10. Reuse audit

No existing seam fits beyond the two this unit edits. `python tools/codebase-map/reuse_lookup.py
"memoize the basename of a tracked path when an anchor selects paths"` and
`python tools/codebase-map/reuse_lookup.py "derive the top-level directories of the tracked set"`
returned `tracked` in `tools/govkit/govkit.py`, `anchor_at` and other name-stem neighbours, none of
them a basename memo or a roots derivation. The seams are `gotchas.selectable`, the one copy of the
selection predicate, and `corpus_ids.walk` with its `_roots`. The recall probe returned the brief,
the build README, TOOL-dTotalRecall-23's scout on the shell's Python delegations, and the
2026-10-08 `aMeteredSweep` suites research on `ask_shell`. None of them names either memo. The
probes and source agree.

Recall terms used: `hygiene check 25 by-name readers test_whole_token corpus_ids walk gotchas selectable print-index-set INDEX_SET ask_shell`
