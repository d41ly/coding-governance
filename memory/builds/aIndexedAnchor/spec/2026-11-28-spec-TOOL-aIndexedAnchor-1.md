# TOOL-aIndexedAnchor-1 — the anchor gate resolves each anchor at the index

**Status:** CLOSED · rev-1 · 2026-11-28 · node a · Tier-1 · base 229f1dde · streams tooling · closes TOOL-dTotalRecall-127

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-28-build-TOOL-aIndexedAnchor-1-1-acceptance-ledger.md](../build/2026-11-28-build-TOOL-aIndexedAnchor-1-1-acceptance-ledger.md) | log | — |
| [2026-11-28-build-TOOL-aIndexedAnchor-1-acceptance-1.md](../build/2026-11-28-build-TOOL-aIndexedAnchor-1-acceptance-1.md) | acceptance | — |
| [2026-11-28-build-TOOL-aIndexedAnchor-1-agent-ledger.md](../build/2026-11-28-build-TOOL-aIndexedAnchor-1-agent-ledger.md) | log | TOOL-aIndexedAnchor-2 |
| [2026-11-28-build-TOOL-aIndexedAnchor-1-red-fix-1.md](../build/2026-11-28-build-TOOL-aIndexedAnchor-1-red-fix-1.md) | red-fix | — |
| [2026-11-28-prompt-TOOL-aIndexedAnchor-1-1-spec-writer.md](../prompts/2026-11-28-prompt-TOOL-aIndexedAnchor-1-1-spec-writer.md) | log | — |
| [2026-11-28-prompt-TOOL-aIndexedAnchor-1-2-builder.md](../prompts/2026-11-28-prompt-TOOL-aIndexedAnchor-1-2-builder.md) | log | — |
| [2026-11-28-prompt-TOOL-aIndexedAnchor-1-brief.md](../prompts/2026-11-28-prompt-TOOL-aIndexedAnchor-1-brief.md) | research | — |
| [2026-11-28-review-TOOL-aIndexedAnchor-2-closing-diff-round1.md](../reviews/2026-11-28-review-TOOL-aIndexedAnchor-2-closing-diff-round1.md) | diff-review | TOOL-aIndexedAnchor-2 |

<!-- /gen:spec-records -->

## 1. Goal

The anchor gate resolves each `[paths].symbols` key at the index, the tree the next commit carries.
A merge commit's pre-commit then grades the merge and not the branch's old tip, so an honest merge
of a main that anchored a new definition is no longer refused.

## 2. Scope (IN)

- **S1** — `tools/codebase-map/map_diff.py#read_unheld_anchors`, a new reader taking
  `(root, tree, map_rel)`. It answers a sorted list of `<feature>: <key>` rows, one per anchor whose
  index blob defines no such name, or None on a shallow clone. Observed by AC1 and AC2.
- **S2** — The gate in `tools/codebase-map/test_codebase_map.py` and its byte-identical twin
  `tools/codebase-map/test_codebase_map.template.py` asserts on that reader. It is renamed from
  `test_anchor_resolves_at_head` to `test_anchor_resolves_at_index`, in its definition and in the
  `__main__` runner list of both files, and `memory/map/generated/symbols.json` is regenerated.
  Observed by AC3.
  **Readers:**
  by name: `tools/codebase-map/test_codebase_map.py`, `tools/codebase-map/test_codebase_map.template.py`,
  `memory/map/generated/symbols.json`.
  by value: NO VALUE READERS — the name is a runner-list entry and a symbol id; nothing compares,
  counts or derives from it.
- **S3** — A selftest arm in `tools/codebase-map/selftest.py`, registered in that file's `main`,
  reproducing the merge case over a real git fixture. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- `map_diff.py --stale-dossiers`, whose unheld-anchor exit in `tools/codebase-map/map_diff.py#main`
  keeps reading at HEAD, as does its README sentence.
- `map_lib.load_map_tree`, which keeps reading the working-tree dossiers.
- The pre-commit hook, and any lexicon or aTemperedLane file.
- Reading the dossiers themselves from the index. The brief offers it as an alternative and the
  index read of the definitions already removes the mismatch.

### Edges

none

## 4. Design

`tools/codebase-map/map_diff.py#read_anchor_hashes` already takes the rev as `head` and builds each
`git cat-file --batch` request as `f"{rev}:{path}"`. An empty rev makes that `:<path>`, which git
reads as the index's stage-0 blob. Probed 2026-11-28 in this worktree: `:tools/codebase-map/map_diff.py`
answered `e05714d3… blob 24711`, and `:nope.py` answered `:nope.py missing`, the shape the reader's
existing `missing` branch already maps to "defines nothing".

The new reader is the gate's current body moved into the kit:

```python
def read_unheld_anchors(root: Path, tree, map_rel: str) -> list[str] | None:
    read = read_commit_paths(root, None)
    if read is None:
        return None
    anchors = read_anchor_hashes(root, read[0], tree, map_rel, head="")  # "" = the index
    return [f"{feature}: {key}" for feature, (now, _then) in sorted(anchors.items())
            for key, digest in sorted(now.items()) if digest is None]
```

The docstring of `read_anchor_hashes` gains one clause: `head` is a rev, or `""` for the index.

The gate keeps its early return for a map with no anchors. It then calls the reader, asserts it is
not None with the existing shallow-clone message, and asserts it is empty with the existing remedy,
"HEAD" reworded to "the index". Its docstring's Not-checked list keeps the dossier no commit
reachable from HEAD carries, and adds a conflicted path, which the index holds at no stage 0 and so
reads as undefined. Under pre-commit the index is the tree being committed. On a clean checkout,
which is every CI run, the index equals HEAD, so the gate's verdict there does not move.

The selftest arm, `test_anchor_reads_the_index_mid_merge(tmp)`, copies the fixture setup of
`tools/codebase-map/selftest.py#test_anchored_dossier_staleness`: the isolated `env`, `run_git`,
`write_commit`, and a `MapTree` built from `DOSSIER` with a parsed foundation. Its steps:

1. The base commit carries `a.py` defining `f`, and `map/features/x.md` whose `[paths]` claims
   `a.py` and anchors `a.py::f`.
2. `git checkout -qb side` commits `def h` into `a.py` and adds the key `a.py::h` to the dossier.
3. `git checkout -qb tip <base>` commits an unrelated `c.py`, then runs
   `git merge --no-ff --no-commit side`.
4. The tree is parsed from the working-tree `map/features/x.md`, so it anchors both keys.
   `md.read_unheld_anchors(tmp, tree, "map")` answers `[]`.
5. `a.py` is rewritten with `h` renamed to `h2` and staged. The reader answers `["x: a.py::h"]`.
6. `git commit -q --no-edit` completes the merge. The reader still answers `["x: a.py::h"]`.

It is registered in `main` beside the anchored-staleness arm, inside its own
`tempfile.TemporaryDirectory()`, as
`stale dossiers: a merge in progress resolves its anchors at the index (aIndexedAnchor-1)`.

Step 4 is the red half. With the reader's rev at `"HEAD"`, the branch's old tip defines no `h` and
the reader answers `["x: a.py::h"]`. Steps 5 and 6 answer the same row at either rev, which is the
rename regression the brief keeps.

### Files touched (estimate)

- `tools/codebase-map/map_diff.py`
- `tools/codebase-map/test_codebase_map.py`
- `tools/codebase-map/test_codebase_map.template.py`
- `tools/codebase-map/selftest.py`
- `memory/map/generated/symbols.json` — regenerated by `python tools/codebase-map/gen_map.py --write`,
  never hand-edited.

## 5. Acceptance criteria

- **AC1** — When `cd tools/codebase-map && python3 -c "import tempfile, pathlib, selftest as s; s.test_anchor_reads_the_index_mid_merge(pathlib.Path(tempfile.mkdtemp()))"`
  runs, it exits 0.
  Red when: `read_unheld_anchors` passes `head="HEAD"`, so step 4 answers `["x: a.py::h"]` for an
  anchor the merge being committed defines.
- **AC2** — When AC1's command runs, the arm's steps 5 and 6 each assert the reader answers
  `["x: a.py::h"]`, before and after `git commit -q --no-edit` completes the merge.
  Red when: the reader stops reporting an anchor whose definition a staged rename took away, so
  either assertion reads `[]`.
- **AC3** — When `cd tools/codebase-map && python3 -c "import test_codebase_map as t; t.test_anchor_resolves_at_index()"`
  runs over this tree, it exits 0, and `grep -c test_anchor_resolves_at_head tools/codebase-map/test_codebase_map.py tools/codebase-map/test_codebase_map.template.py memory/map/generated/symbols.json`
  prints 0 for each file.
  Red when: a key a committed dossier anchors names a definition the index does not hold, or the old
  name survives in either gate file or in the generated symbol list.
  cost: about ten seconds, the full-history `git log` the reader reads (measured 2026-11-28 on the
  current gate, PINNED).

## 6. Gates

`codebase-map coverage + freshness` · `codebase-map gate coverage` · `codebase-map kit selftest` · `codebase-map adopter e2e` · `recall floor` · `recall floor arms`

New arm: `tools/codebase-map/selftest.py` · covers AC1 AC2 · the reader's rev set to `"HEAD"` reds step 4 · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-28 · initial draft.

## 9. Reuse audit

The seam is `tools/codebase-map/map_diff.py#read_anchor_hashes`, which already parameterises the rev;
the new reader passes `""` for the index and adds no blob reader of its own. The lookup also surfaced
`tools/memory-tree/tree_lib.py#read_blobs_at`, which belongs to a separately installed kit that the
codebase-map kit cannot import, and reads no definitions.

Recall terms used: `reuse_lookup.py "read anchored symbol definitions from the index blob git cat-file staged tree resolve dossier anchor unheld"`
