# TOOL-dTotalRecall-87 — the memory root `resolve_kept_home` joins is resolved once, normalised to a repo-relative path, and refused when blank, absolute or leaving the tree

**Status:** DEFERRED · rev-3 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 34 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-87-deviation-871.md](../build/2026-10-26-build-TOOL-dTotalRecall-87-deviation-871.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-11 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-53 TOOL-dTotalRecall-59 TOOL-dTotalRecall-62 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-81 TOOL-dTotalRecall-88 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 |
| [2026-11-24-prompt-TOOL-dTotalRecall-87-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-87-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-87-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-87-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-88 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 39 at HIGH**, its item **H4**, alone in that item.

`TOOL-dTotalRecall-73` (order 33) gives the census keep registry one home, `resolve_kept_home(root)`,
the memory root joined to `project` and the registry's filename. Its rev-3 strips whitespace and the
slashes at both ends, so a trailing slash already reads one home. Four readings are left:

- A backslash, a `.` segment or a doubled inner slash stays as spelled. Git resolves no such path at a
  revision: `git cat-file -e HEAD:memory//HYGIENE.md` exits 128 (DERIVED 2026-11-24, that command). The
  factory's compare of a home registered in that spelling so reads no file at its base.
- A backslash root also builds unit 66's row domain, which then admits no tracked path, since git lists
  paths with `/`.
- A `..` segment or a drive letter opens a registry outside the repository. At HEAD
  `tree_lib.py#read_kept_rows` answered the row of one under each (DERIVED 2026-11-24, one probe over a
  scratch repository with a registry beside it).
- A declared blank, or a bare `/`, silently reads the kit default.

This unit resolves the memory root once, in `tools/memory-tree/tree_lib.py`, and makes a root that
cannot name a directory inside the tree a red finding. `resolve_kept_home` joins only the resolved
root. It repairs `TOOL-dTotalRecall-73`, at step 34, one above that unit's order.

## 2. Scope (IN)

- **S1** — The resolver. `resolve_memory_root(conf)` in `tools/memory-tree/tree_lib.py` returns the
  kit default `memory` where the conf declares no `MEMORY_ROOT`. Otherwise it strips whitespace, folds
  `\` to `/`, drops empty and `.` segments, and returns the remaining segments joined by `/`. It
  raises `ValueError` naming `MEMORY_ROOT` and the value for a value that is blank after that, that
  starts with `/` or a drive letter, or that holds a `..` segment. Observed by AC1.
  **Readers:** by name: no name retires, the segments S1 drops being bytes of one value. The kit's
  Python readers that spell `MEMORY_ROOT` keep their own reads (§3):
  `tools/memory-tree/asbuilt_view.py`, `tools/memory-tree/build_records.py`,
  `tools/memory-tree/check-arms.py`, `tools/memory-tree/corpus_ids.py`,
  `tools/memory-tree/design_lib.py`, `tools/memory-tree/deviation_join.py`,
  `tools/memory-tree/gen_build_index.py`, `tools/memory-tree/gotchas.py`,
  `tools/memory-tree/gov_record.py`, `tools/memory-tree/id_grammar.py`,
  `tools/memory-tree/merge-rows.py`, `tools/memory-tree/migrate_backlog.py`,
  `tools/memory-tree/ratchet.py`, `tools/memory-tree/record_causes.py`,
  `tools/memory-tree/record_find.py`, `tools/memory-tree/record_kinds.py`,
  `tools/memory-tree/routed_commits.py`, `tools/memory-tree/row_grammar.py`,
  `tools/memory-tree/seen_red.py`, `tools/memory-tree/shape_run.py`,
  `tools/memory-tree/transition_audit.py` and `tools/memory-tree/tree_lib.py` (DERIVED 2026-11-24,
  a git grep -l for the name over the kit's Python files); every other reader in the tree is one a
  git grep -l for the name lists · by value: `resolve_kept_home`, S2's caller, is the one reader of the
  root S1 returns.
- **S2** — The one caller. `resolve_kept_home(root)` joins the home under `resolve_memory_root` of
  `design_lib.read_design_conf(root)`, and under nothing else. A refused root is one red finding of the
  writer census, naming `MEMORY_ROOT`, through the catch it makes around `read_kept_rows`.
  `check_kept_home(root)` catches the same error, prints one line naming it in place of its own lines,
  and adds no second red and no refusal (§8 F3). Observed by AC3 and AC4.
  **Readers:** by name: READER NOT IN TREE — `resolve_kept_home` and `check_kept_home` are minted by
  `TOOL-dTotalRecall-73` in this build and are absent at base `462d20f3` · by value:
  `read_kept_rows`, which opens the home and takes unit 66's row domain from it, `read_kept_path` and
  both censuses through it, and `check_kept_home`, which prints and compares it.
- **S3** — The plant `kept-home-trailing-root` in `record_causes.py --fixture` builds unit 73's
  `kept-home-rooted` tree with its conf set to `MEMORY_ROOT="docs/memory/"` and its registration naming
  the file under that root's `project` folder. There the writer census prints one home on its `read at`
  line and its `registered at` line, and no red. Observed by AC2.
- **S4** — The plant `kept-root-blank` builds the plain tree with `MEMORY_ROOT=""`. There the writer
  census exits 1 with one red naming `MEMORY_ROOT`, and prints no `read at` line. Observed by AC3.

## 3. Non-goals (OUT)

- Every other reader of `MEMORY_ROOT` in the kit, such as `tools/memory-tree/tree_lib.py#read_bindings`
  and the two the censuses walk by, `record_causes.py#read_conf` and `record_kinds.py#read_memory_root`.
  Each reads the conf for its own purpose and none joins the registry's home.
- `memory-recall`'s read of the key. It refuses a blank, and it resolves no id under a trailing slash,
  so `record_causes.py --check` is red or refused there for a reason of its own (§8 F2).
- Re-rooting the registered home by prefix rather than by basename (item L5, id 20): the batch
  `TOOL-dTotalRecall-88`. Unit 73 rev-3 re-roots no registration.
- Hoisting one memory-root reader into `tools/lib` with a lint against fresh reads: the left-shift
  gate the report suggests, the close's left-shift step (BUILD-METHOD M8).
- Editing unit 73's spec, frozen once its unit builds.

### Edges

- **consumes-from** `TOOL-dTotalRecall-73` — `resolve_kept_home` and its plant `kept-home-rooted`, whose memory-root join this unit routes through one resolver
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

| Value | At unit 73's tip | Result |
|---|---|---|
| absent | `memory` | `memory` |
| `memory` | `memory` | `memory` |
| `docs/memory/` | `docs/memory` | `docs/memory` |
| `docs\memory` | as spelled | `docs/memory` |
| `./docs//memory` | as spelled | `docs/memory` |
| blank, or `/` | `memory` | `ValueError` |
| `/memory` | `memory` | `ValueError` |
| `../memory`, `C:/memory` | as spelled | `ValueError` |

`tools/runlog/runlog_lib.py#resolve_memory_root` is the precedent: it strips slashes and refuses a
value naming no directory or holding `..`. It diverges from this one in two ways. It strips a leading
slash, where this one refuses an absolute root. It refuses any backslash or `:`, where this one folds a
backslash and refuses a leading drive only. No criterion asks the two to agree. It reads a file of
another kit, so a copy-installed memory-tree kit cannot import it.
`tools/memory-tree/deviation_join.py#read_population` strips slashes and
`tools/memory-tree/design_lib.py#main` folds backslashes, each inline; this resolver states both once
for the one caller that joins a home.

### The caller

`resolve_kept_home` keeps its signature and its call-time import, and its body becomes:

```python
    return f"{resolve_memory_root(read_design_conf(root))}/project/{CENSUS_KEPT_REGISTRY}"
```

`read_kept_rows` lets the `ValueError` pass, and the catch each census makes around it turns it into one
red opening `cause-writer MEMORY_ROOT=` or `alias-compare MEMORY_ROOT=`, the walk reading every hit
unkept, as a malformed registry's does. Unit 66's `read_pinned_rows` answers `[]` there.
`check_kept_home` begins:

```python
    try:
        home = tree_lib.resolve_kept_home(root)
    except ValueError as exc:   # read_kept_rows' catch is the red
        return [f"cause-writer · keep registry · read nowhere: {exc}"], []
```

A `..` or drive root that leaves the repository reaches that line only where the build-folder walk's own
git read of it does not refuse the census first, as it does for `..` at HEAD
(`record_causes.py#read_build_code_paths`). Either way no registry is opened.

### The plants

`main`'s `--cause-writers` branch becomes `run_cause_writers(root)`, answering `(lines, exit)`, and
`main` and `run_fixture` both call it. `run_fixture` takes it in place of `run_check` for the two plants
of this unit (§8 F2). Each plant's conf is rewritten after the seed, as the view plants rewrite theirs,
so the seed runs under the root the tree is built at: `docs/memory` for the first, `memory` for the
second.

### Inventory

Minted: `resolve_memory_root` in `tools/memory-tree/tree_lib.py`; `run_cause_writers` in
`tools/memory-tree/record_causes.py`; the fixture plants `kept-home-trailing-root` and
`kept-root-blank`. Naming cells: both functions answer `OK` under `py.function`
(`python tools/lexicon/lexicon.py --suggest <name> --as py.function`, 2026-11-24), led by the declared
verbs `resolve` and `run`; a plant has none.

### Why order 34

The join is unit 73's, built at step 33. Step 34 is the first step after it.
`TOOL-dTotalRecall-74` shares the step and writes only build records.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/record_causes.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Leave the inline strip of `resolve_kept_home`, as unit 73 builds it.** It mends the trailing slash
  and leaves a `..` root, the case that reads outside the repository.
- **A blank value read as the kit default.** `deviation_join.py#read_population` and unit 73 read it
  that way. A declared blank is an adopter's mistake that would silently move its registry; runlog's
  resolver refuses it, and the report's fix asks for the refusal.
- **Import `runlog_lib.resolve_memory_root` or `loop_lib.resolve_memory_root`.** The memory-tree kit is
  copy-installed and carries no other kit's code. `tools/loop/loop_lib.py#resolve_memory_root` also
  answers the unattended driver's records root, from a second conf this one does not read.

## 5. Production-readiness checklist

- security — narrows a read surface: no root outside the repository is joined.
- perf / scale — one conf read per home read, as before.
- error / empty / loading states — an absent key is the kit default. A blank, absolute or `..` value
  is a red finding naming `MEMORY_ROOT`.
- observability — the census prints the resolved home, or the refusal in its place.
- risks — an adopter whose conf spells a leading slash or a blank now reds where the registry's reader
  fell back before, while the kit's other readers still fall back; the finding names the key and the
  value.
- testing — AC1 to AC4 by the pass; the arm of §7 at the close.
- migration — none. Gov's `MEMORY_ROOT=memory` resolves to itself.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python -c "import tree_lib; print([tree_lib.resolve_memory_root(c) for c in ({}, {'MEMORY_ROOT': 'docs/memory/'}, {'MEMORY_ROOT': 'docs\\\\memory'}, {'MEMORY_ROOT': './docs//memory'})])"`
  runs from `tools/memory-tree/` at the pass tip, it prints `['memory', 'docs/memory', 'docs/memory', 'docs/memory']`,
  and the same call over `''`, `'/memory'`, `'../memory'` and `'C:/memory'` raises `ValueError` naming
  `MEMORY_ROOT` for each.
  Red when: a trailing slash survives, or a blank, absolute or parent root returns a value.
- **AC2** — When `python record_causes.py --fixture --plant kept-home-trailing-root` runs from
  `tools/memory-tree/`, it exits 0 with no `record causes: RED ` line, and its `read at` and
  `registered at` lines each name the registry's file under the `project` folder of `docs/memory`, with
  no doubled slash. With the conf's raw value joined in a probe process, the `read at` line names a
  doubled slash.
  Red when: either line names `docs/memory//project`, or the two name two homes.
  fixture: the plant's scratch tree, made and removed under the system temp directory as every plant's
  is.
- **AC3** — When `python record_causes.py --fixture --plant kept-root-blank` runs from
  `tools/memory-tree/`, it exits 1 with one `record causes: RED ` line, naming `MEMORY_ROOT`, and prints
  the `read nowhere` line and no `read at` line. With the blank refusal skipped in a probe process and
  the kit default returned, the same plant exits 0.
  Red when: a blank root yields a home, or the refusal is two reds or an exit 2.
- **AC4** — When the probe below runs from `tools/memory-tree/` at the pass tip, it prints the registry's
  path under the `project` folder of `docs/memory` three times, then `MEMORY_ROOT` twice.
  `python record_causes.py --cause-writers` there prints every line as at the pass base.

  ```bash
  python - <<'PROBE'
  import os, pathlib, sys, tempfile
  sys.path.insert(0, os.getcwd())
  import tree_lib
  with tempfile.TemporaryDirectory(prefix="kh") as d:
      for v in ("docs/memory/", "docs" + chr(92) + "memory", "./docs//memory", "", "../memory"):
          pathlib.Path(d, ".memory-tree.conf").write_text(f'MEMORY_ROOT="{v}"\n', encoding="utf-8")
          try:
              print(tree_lib.resolve_kept_home(d))
          except ValueError as exc:
              print(str(exc).split("=")[0])
  PROBE
  ```

  Red when: the home joins the conf's raw value, which at the base of this pass prints the second and
  third as spelled and a home for the last two, or gov's own lines move.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `record causes (causes and orphans over the legacy population)` · `record-kinds` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 AC3 · the plants `kept-home-trailing-root` and `kept-root-blank`, staged by joining the conf's raw value in `resolve_kept_home` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Which run do the two plants grade?** Options: (a) `--check`, as rev-2 states; (b) the writer
  census alone, as `--cause-writers` prints it. Probed over one fixture per value at HEAD (DERIVED
  2026-11-24, `run_check` and `check_cause_writers`): a blank root makes `--check` refuse in
  `memory-recall`'s id read, before any census runs. A trailing slash reds it, one record
  causeless, since the id that record names does not resolve. (a) fails AC2 and AC3; veto 1 discards
  it. RESOLVED (agent, 2026-11-24, delegated): (b), the one survivor, per
  `2026-11-24-prompt-TOOL-dTotalRecall-87-reground-brief`. widens: none · relaxes: none
- **F3 — Where does a refused root surface, which unit 73 §4 leaves to this unit?** Options: (a) one red
  through the census's catch, `check_kept_home` naming it on a line; (b) the error left uncaught in
  `check_kept_home`, so the census refuses with exit 2; (c) a red from both. (b) and (c) fail AC3; veto 1
  discards both. RESOLVED (agent, 2026-11-24, delegated): (a), the one survivor, per
  `2026-11-24-prompt-TOOL-dTotalRecall-87-reground-brief`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 39
  (HIGH, item H4).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-92, each the other end of an edge a
  unit the round-1 spec audit of units 77 to 88 promoted wrote; nothing else moved.
- rev-3 · 2026-11-24 · §1 S1 S2 S3 S4 §3 §4 §5 AC1 AC2 AC3 AC4 §7 §8 §10 · re-grounded at HEAD `db95ebf86`
  per `2026-11-24-prompt-TOOL-dTotalRecall-87-reground-brief`, over unit 73 rev-3: the join is
  `resolve_kept_home`, no compare line stands, and a trailing slash already reads one home. The plants
  grade the writer census (F2), a refused root is one red (F3), AC4 is new, the arm sits in the hygiene
  suite, the precedent paragraph states where it diverges, and citations name symbols.

## 10. Reuse audit

The seam is `tools/memory-tree/design_lib.py#read_design_conf`, the conf's one reader over
`tools/memory-tree/tree_lib.py#parse_conf`, and the normalisation the sibling engines already apply,
`tools/memory-tree/deviation_join.py#read_population` and `tools/memory-tree/design_lib.py#main`, with
`tools/runlog/runlog_lib.py#resolve_memory_root`'s refusals as the precedent.
`python tools/codebase-map/reuse_lookup.py "normalise the memory root read from the conf and refuse a root outside the repository"`
ranked `read_design_conf`, `parse_conf` and `resolve_memory_root` among its SEAM candidates, the last in
the loop, memory-recall and runlog kits and none in the memory-tree kit (DERIVED 2026-11-24, that
command). The recall query below found the audit's H4 item, unit 73, `TOOL-dDeclaredLoop-72` and
`TOOL-dDeclaredLoop-116`, which route the loop kit's readers through its own resolver, and
`TOOL-aScouredKit-19`'s ask, whose conf-line reader `parse_conf_line` became the kit's one parser; none
resolves the root a path of this kit is joined under. No existing seam fits inside the kit, so one
function is minted for the one join that needs it.

Recall terms used: `python tools/memory-recall/query.py "how is the memory root from the conf normalised before a path is joined under it" --terms "MEMORY_ROOT trailing slash backslash normalise strip refuse blank absolute parent conf memory-tree registry home"`
