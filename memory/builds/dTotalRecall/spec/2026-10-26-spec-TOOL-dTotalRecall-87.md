# TOOL-dTotalRecall-87 — the memory root `resolve_kept_registration` joins is resolved once, normalised to a repo-relative path, and refused when blank, absolute or leaving the tree

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 34 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-88 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 39 at HIGH**, its item **H4**, alone in that item.

`TOOL-dTotalRecall-73` (order 33) builds the registry's home as
`f"{MEMORY_ROOT}/project/{basename}"` with the memory root as the conf spells it. A conf value with a
trailing slash gives `docs/memory//project/…`, a backslash gives a Windows separator, and a blank
value gives `/project/…`. `git show <base>:<that>` fails on such a path: re-probed,
`git show HEAD:memory//HYGIENE.md` exits 128 where `git show HEAD:memory/HYGIENE.md` exits 0. The
census's filesystem join tolerates the same path, so the census reads the registry while
`compare_to_base` reads no home at base, which `TOOL-dTotalRecall-68`'s S4 takes for a first seed.
The shrink-only ratchet then never refuses a gained keep, the split unit 73 exists to close. A blank
root also points the census at an absolute `/project` path outside the repository.

This unit resolves the memory root once, in `tools/memory-tree/tree_lib.py`, the way the sibling
engines already normalise it, and makes the root that cannot name a directory inside the tree a red
finding. `resolve_kept_registration` joins only the resolved root. It repairs
`TOOL-dTotalRecall-73`, at step 34, one above that unit's order.

## 2. Scope (IN)

- **S1** — The resolver. `resolve_memory_root(conf)` in `tools/memory-tree/tree_lib.py` returns the
  kit default `memory` where the conf declares no `MEMORY_ROOT`. Otherwise it strips whitespace, folds
  `\` to `/`, drops empty and `.` segments, and returns the remaining segments joined by `/`. It
  raises `ValueError` naming `MEMORY_ROOT` and the value for a value that is blank after that, that
  starts with `/` or a drive letter, or that holds a `..` segment. Observed by AC1.
  **Readers:** by name: no name retires, the segments S1 drops being bytes of one value. The kit's
  Python readers that spell `MEMORY_ROOT` keep their own reads (§3): `tools/memory-tree/tree_lib.py`,
  `tools/memory-tree/asbuilt_view.py`, `tools/memory-tree/check-arms.py`,
  `tools/memory-tree/corpus_ids.py`, `tools/memory-tree/design_lib.py`,
  `tools/memory-tree/deviation_join.py`, `tools/memory-tree/gen_build_index.py`,
  `tools/memory-tree/gotchas.py`, `tools/memory-tree/merge-rows.py`,
  `tools/memory-tree/migrate_backlog.py`, `tools/memory-tree/routed_commits.py`,
  `tools/memory-tree/row_grammar.py` and `tools/memory-tree/transition_audit.py`, and
  `tools/runlog/runlog_lib.py`'s `resolve_memory_root`, §4's precedent; every other reader in the
  tree is one a git grep -l for the name lists · by value: `resolve_kept_registration`, S2's caller,
  is the one reader of the root S1 returns.
- **S2** — The one caller. `resolve_kept_registration(root)` reads `<root>/.memory-tree.conf` through
  `tree_lib.parse_conf` and joins the home under `resolve_memory_root` of it, and under nothing else.
  A `ValueError` from S1 is a red finding naming `MEMORY_ROOT`, surfaced where unit 73's S1 surfaces
  an absent registration, never a home. Observed by AC2 and AC3.
  **Readers:** by name: READER NOT IN TREE — `resolve_kept_registration` is minted by
  `TOOL-dTotalRecall-73` in this build and is absent at base `462d20f3` · by value:
  `read_kept_path` and `record_causes.py --check`, which read the home it returns.
- **S3** — The plant `kept-home-trailing-root` in `record_causes.py --fixture` builds unit 73's
  `kept-home-rooted` tree with its conf set to `MEMORY_ROOT=docs/memory/`. There `--check` prints one
  home on the census line and the compare line, `docs/memory/project/census-kept-paths.txt`, and the
  compare reads it at base. Observed by AC2.
- **S4** — The plant `kept-root-blank` builds the same tree with `MEMORY_ROOT=` blank. There
  `--check` exits 1 naming `MEMORY_ROOT`, and prints no census line under `/project`. Observed by
  AC3.

## 3. Non-goals (OUT)

- Every other reader of `MEMORY_ROOT` in the kit, such as `tree_lib.read_bindings` at
  `tools/memory-tree/tree_lib.py:489`. Each reads the conf for its own purpose and none joins the
  registry's home.
- Re-rooting the registered home by prefix rather than by basename (item L5, id 20): the batch
  `TOOL-dTotalRecall-88`, which builds on S1.
- Hoisting one memory-root reader into `tools/lib` with a lint against fresh reads: the left-shift
  gate the report suggests, the close's left-shift step (BUILD-METHOD M8).
- Editing unit 73's spec, frozen once its unit builds.

### Edges

- **consumes-from** `TOOL-dTotalRecall-73` — `resolve_kept_registration` and its plant `kept-home-rooted`, whose memory-root join this unit routes through one resolver
- **hands-off** `TOOL-dTotalRecall-88` — `resolve_memory_root`, the resolved root that batch's item for id 20 re-roots the registered home under
- **hands-off** `TOOL-dTotalRecall-92` — its plant `kept-home-trailing-root`, its AC2 answer, its §4 precedent and `resolve_memory_root`, which that batch re-observes on the fixture base, corrects by record and documents (the round-1 audit of units 77 to 88, ids 6, 16, 21)

## 4. Design

### The resolver

```python
def resolve_memory_root(conf: dict) -> str:
    """The memory tree's repo-relative root from a parsed `.memory-tree.conf`: the kit default where
    the key is absent, else the value with `\\` folded to `/` and empty and `.` segments dropped.
    `ValueError` naming the key for a blank, absolute or `..`-holding value."""
    if "MEMORY_ROOT" not in conf:
        return "memory"
    raw = conf["MEMORY_ROOT"]
    value = raw.strip().replace("\\", "/")
    if value.startswith("/") or re.match(r"[A-Za-z]:", value):
        raise ValueError(f"MEMORY_ROOT={raw!r} is absolute, and a memory root is repo-relative")
    parts = [p for p in value.split("/") if p not in ("", ".")]
    if not parts:
        raise ValueError(f"MEMORY_ROOT={raw!r} names no directory")
    if ".." in parts:
        raise ValueError(f"MEMORY_ROOT={raw!r} leaves the repository")
    return "/".join(parts)
```

| Value | Result |
|---|---|
| absent | `memory` |
| `memory` | `memory` |
| `docs/memory/` | `docs/memory` |
| `docs\memory` | `docs/memory` |
| `./docs//memory` | `docs/memory` |
| blank | `ValueError` |
| `/memory` | `ValueError` |
| `../memory` | `ValueError` |

`tools/runlog/runlog_lib.py:393` `resolve_memory_root` is the precedent: it strips slashes and
refuses a value naming no directory or holding `..`. It reads a file of another kit, so a
copy-installed memory-tree kit cannot import it. `deviation_join.py:277` strips slashes and
`design_lib.py:680` folds backslashes, each inline; this resolver states both once for the one
caller that joins a home.

### Inventory

Minted: `resolve_memory_root` in `tools/memory-tree/tree_lib.py`; the fixture plants
`kept-home-trailing-root` and `kept-root-blank` in `record_causes.py --fixture`. Naming cell:
`resolve_memory_root` is asked of the lexicon's `--suggest` under `--as py.function`, which answered
`OK` at writing, led by the declared verb `resolve`.

### Why order 34

The join is unit 73's, built at step 33. Step 34 is the first step after it.
`TOOL-dTotalRecall-74` shares the step and writes only build records.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/record_causes.py`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Strip slashes inline in `resolve_kept_registration`.** It mends the trailing slash and leaves a
  blank root as `/project`, the case that reads outside the repository.
- **A blank value read as the kit default.** `deviation_join.py:277` reads it that way. A declared
  blank is an adopter's mistake that would silently move its registry; runlog's resolver refuses it,
  and the report's fix asks for the refusal.
- **Import `runlog_lib.resolve_memory_root`.** The memory-tree kit is copy-installed and carries no
  other kit's code.

## 5. Production-readiness checklist

- security — narrows a read surface: no root outside the repository is joined.
- perf / scale — one conf read per census run, as before.
- error / empty / loading states — an absent key is the kit default. A blank, absolute or `..` value
  is a red finding naming `MEMORY_ROOT`.
- observability — the census and compare lines print the resolved home.
- risks — an adopter whose conf spells an absolute root now reds where it silently read before; the
  finding names the key and the value.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — none. Gov's `MEMORY_ROOT=memory` resolves to itself.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python -c "import tree_lib; print([tree_lib.resolve_memory_root(c) for c in ({}, {'MEMORY_ROOT': 'docs/memory/'}, {'MEMORY_ROOT': 'docs\\\\memory'}, {'MEMORY_ROOT': './docs//memory'})])"`
  runs from `tools/memory-tree/` at the pass tip, it prints `['memory', 'docs/memory', 'docs/memory', 'docs/memory']`,
  and the same call over `''`, `'/memory'` and `'../memory'` raises `ValueError` naming `MEMORY_ROOT`
  for each.
  Red when: a trailing slash survives, or a blank, absolute or parent root returns a value.
- **AC2** — When `python record_causes.py --fixture --plant kept-home-trailing-root` runs from
  `tools/memory-tree/`, `--check` prints the census line and the compare line, each naming
  the registry's file under `docs/memory/project/` with no doubled slash, and the compare names a
  base sha.
  Red when: either line names `docs/memory//project`, or the compare reads a first seed.
  fixture: the plant's scratch tree, made in a `tempfile.TemporaryDirectory()` the plant removes.
- **AC3** — When `python record_causes.py --fixture --plant kept-root-blank` runs from
  `tools/memory-tree/`, `--check` exits 1 and names `MEMORY_ROOT`, and no line it prints names a home
  starting `/project`.
  Red when: a blank root yields a home.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/record_causes.py · covers AC2 AC3 · the plants `kept-home-trailing-root` and `kept-root-blank`, staged by joining the conf's raw value in `resolve_kept_registration` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 39
  (HIGH, item H4).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-92, each the other end of an edge a
  unit the round-1 spec audit of units 77 to 88 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam is `tree_lib.parse_conf` (`tools/memory-tree/tree_lib.py:135`), the kit's one conf parser,
and the normalisation the sibling engines already apply, `deviation_join.py:277` and
`design_lib.py:680`, with `tools/runlog/runlog_lib.py:393`'s refusals as the precedent.
`python tools/codebase-map/reuse_lookup.py "normalise the memory root read from the conf and refuse a root outside the repository"`
ranked `load_conf`, `parse_conf`, `repo_root` and `read_conf` among its SEAM candidates and no
memory-root resolver in the memory-tree kit; `parse_conf` is the one this unit reads through. The
recall query below found the audit's H4 item, units 73 and 65, and `TOOL-aScouredKit-19`'s ask,
whose conf-line reader `parse_conf_line` became the kit's one parser; none resolves the root a path
is joined under. No existing seam fits inside the kit, so one function is minted for the one join
that needs it.

Recall terms used: `python tools/memory-recall/query.py "how is the memory root from the conf normalised before a path is joined under it" --terms "MEMORY_ROOT trailing slash backslash normalise strip refuse blank absolute parent conf memory-tree registry home"`
