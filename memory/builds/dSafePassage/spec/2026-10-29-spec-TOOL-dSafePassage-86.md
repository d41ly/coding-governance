# TOOL-dSafePassage-86 — release-0's apply runs the pinned clone's own engine, so the walk applies release-0 at every tool root

**Status:** DEFERRED · rev-2 · 2026-10-29 · node a · Tier-2 · base b634d60e · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-prompt-TOOL-dSafePassage-86-1-spec-writer.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-86-1-spec-writer.md) | journal | — |
| [2026-10-29-prompt-TOOL-dSafePassage-86-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-86-spec-brief.md) | research | TOOL-dSafePassage-87 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 closing review's H1 (id 13). `build_release_tree` runs release-0's `apply` from the
pinned clone at HERE's own relative path, and the pin holds only `tools/govkit/govkit.py`. So at
every moved tool root the apply cannot open its engine, the leg exits 2, and the `upgrade-walk` row
of the foreign-prefix parity leg is red. This unit points that one call at the pin's own engine path,
derived from the clone while it sits at the pin, and adds a grader that reds when the path is
HERE-relative again.

## 2. Scope (IN)

- **S1** — The pin's engine path. `tools/govkit/upgrade_walk.py` gains
  `derive_release_engine(clone)`, which returns
  `clone / gk.resolve_prefix_token("{prefix}/govkit/govkit.py", gk.derive_tool_root(clone))`.
  The release-0 `apply` call (`upgrade_walk.py:212`) runs `derive_release_engine(clone)` in place of
  `clone / ctx["govkit"]`. It runs while the clone is checked out at the pin (`:198`), before the
  checkout to the tip (`:234`). `ctx["govkit"]` (`:204`) stays HERE-relative, because its two readers
  (`:483` and `:523`) run against the clone at its tip, which carries HERE's layout. Observed by AC2
  and AC3.
- **S2** — The grader. `check_graders` (`upgrade_walk.py:950`) gains `check_grade_release_engine`,
  run as the `release-engine` row after `fixture-keys` (`:1036`). It lays out three pin-shaped scratch
  trees under its `scratch`, each holding `govkit/registry.toml` and `govkit/govkit.py` under the tool
  root `tools`, `scripts` and the repo root. It requires `derive_release_engine` to return each tree's
  own `govkit/govkit.py`. HERE sits at one tool root, so at least one tree differs from it, and the
  HERE-relative path reds at every prefix the leg runs from. The `check_graders` docstring names
  TOOL-dSafePassage-86 beside 77's S7. Observed by AC1.

## 3. Non-goals (OUT)

- The `[[plant]]` path resolution. At a moved prefix, with S1 alone, the walk applies release-0 and
  then stops at `plant engine-edit: scripts/memory-tree/README.md is absent at release-0`, exit 2.
  That is M7 (id 14), and TOOL-dSafePassage-87 closes it. The review asks the two to land together.
  This unit lands first at order 16 and 87 lands after it, and 87's AC observes the walk past the
  plants at a moved prefix.
- A green `upgrade-walk` row in the foreign-prefix parity leg. That leg is red at `b634d60e5` at
  `scripts/`, and this unit does not turn it green. TOOL-dSafePassage-87's §3 names what still stands
  after both units, measured.
- `ctx["govkit"]` and its two tip-side readers. The skeptic's corrected fix keeps them as they are,
  and so does this unit.
- The review's process gates for H1: a bug-class checklist entry, or a close that refuses a ledger
  marking a parity run owed. The review records that no checklist exists, and a close rule is a
  change to a governance carrier. S2's grader is this unit's gate on the defect class.
- `deploy.toml`'s resolution (`:206-207`) and the policy adopter's kit directory (`:225`). Both
  already read `gk.derive_tool_root(clone)` while the clone is at the pin, and both resolve correctly
  at `scripts/` (§4 "Measured at writing time").

### Edges

- **hands-off** `TOOL-dSafePassage-87` — the `[[plant]]` and arm path resolution against the target's
  install prefix (M7), and the moved-prefix run past the plants that only both fixes together can make
- **hands-off** `TOOL-dSafePassage-89` — the moved-prefix run past `read_steps`, which stops there
  until `derive_tool_root` reads the clone's tree at its tip as well as at the pin

## 4. Design

### The defect, at `b634d60e5`

`build_release_tree` (`tools/govkit/upgrade_walk.py:183`) clones gov, checks the clone out at the pin
(`:198`), and sets `rel = HERE.relative_to(gov_root.resolve()).as_posix()` (`:202`) and
`ctx["govkit"] = f"{rel}/govkit.py"` (`:204`). The release-0 `apply` then runs
`str(clone / ctx["govkit"])` (`:212`). The pin `60d90cb71` (`fixtures/release-0/pin.txt`) holds
`tools/govkit/govkit.py` and `tools/govkit/registry.toml`, and
`git cat-file -e 60d90cb71:scripts/govkit/govkit.py` fails. So at `scripts/`, `vendor/gov/` or the
repo root, `rel` names a file the pin lacks, and `p.returncode` raises the `Stop` at `:215-217`.
`main` prints `nothing measured` and returns 2 (`:1139-1141`). The probe marker at `:1123-1124`
sits after `build_release_tree`, so it never prints, and the parity leg's `run_row` reds on the exit
alone (`tools/run-gates/foreign-prefix.gov.test.sh:574-576`).

### S1: one function, one call site

```python
def derive_release_engine(clone) -> pathlib.Path:
    """The engine release-0's `apply` runs: the pinned clone's own `govkit.py`, at the tool root the
    clone holds at the pin, never HERE's (TOOL-dSafePassage-86). Read while the clone is at the pin."""
    _us, _shims, gk = load_engine()
    return clone / gk.resolve_prefix_token("{prefix}/govkit/govkit.py", gk.derive_tool_root(clone))
```

It sits under the `release-0` banner (`:182`), above `build_release_tree`. At `:212` the argv's
second element becomes `str(derive_release_engine(clone))`. `derive_tool_root(clone)` resolves
`tools` at the pin, because the clone is not gov's own checkout and its one
`*/govkit/registry.toml` is `tools/govkit/registry.toml` (`tools/govkit/govkit.py:205-211`).

The skeptic wrote `clone / f"{gk.derive_tool_root(clone)}/govkit/govkit.py"`. That gives the same
path at this pin. `resolve_prefix_token` (`govkit.py:217-226`) is used instead because at a pin
whose tool root is the repo root, `derive_tool_root` returns `""`, the f-string reads
`/govkit/govkit.py`, and pathlib joins that as an absolute path. Measured: S2's grader reds on the
f-string with `a pin at the repo root derived C:\govkit\govkit.py`.

### S2: the grader

```python
def check_grade_release_engine() -> str:
    for pre in ("tools", "scripts", ""):
        c = scratch / f"pin-{pre or 'root'}"
        for f in ("govkit/registry.toml", "govkit/govkit.py"):
            (c / pre / f).parent.mkdir(parents=True, exist_ok=True)
            (c / pre / f).write_text("x", encoding="utf-8")
        got, want = derive_release_engine(c), c / pre / "govkit" / "govkit.py"
        if got != want:
            return f"a pin at {pre or 'the repo root'} derived {got}, not {want}"
    return ""
```

It needs no git: `derive_tool_root` reads the filesystem. The `scratch` directory is the one
`check_graders` already makes and removes (`:956`, `:1045`). Its row joins the tuple at `:1034-1036`
as `("release-engine", check_grade_release_engine)`.

### Measured at writing time

In a `git clone --no-hardlinks` of `b634d60e5` under the temp root, 2026-10-29. For the moved
prefix, `git mv tools scripts` was committed in the clone, the shape `set_tool_root` makes, without
its declaration rewrite. The walk ran as `FOREIGN_PREFIX_PROBE=1 python scripts/govkit/upgrade_walk.py --case up`,
about 70 seconds per run.

| Observation | At `b634d60e5` | S1 staged |
|---|---|---|
| moved-prefix walk | exit 2, `nothing measured: release-0's apply exited 2: ... can't open file '...\gov\scripts\govkit\govkit.py'` | `release-0 applied by the pinned clone's own apply over the fixture's kits line · exit 0 · receipt schema 3`, then exit 2, `plant engine-edit: scripts/memory-tree/README.md is absent at release-0` |
| `check_graders()` at `tools/`, S1 and S2 staged | — | `grader · release-engine · ok`, `[]` |
| the same, `derive_release_engine` HERE-relative | — | `RED · a pin at scripts derived ...\pin-scripts\tools\govkit\govkit.py`, `['grader release-engine']` |
| the same, the bare f-string | — | `RED · a pin at the repo root derived C:\govkit\govkit.py`, `['grader release-engine']` |

### Inventory

Minted: the function `derive_release_engine`, the nested grader `check_grade_release_engine`, and
the grader row name `release-engine`. `python tools/lexicon/lexicon.py --suggest derive_release_engine --as py.function`
and the same for `check_grade_release_engine` each answered OK on 2026-10-29, leading with the
declared verbs `derive` and `check`. No `Refusal` site, flag, conf key, gate leg or receipt field.

### Migration

None. No stored shape changes.

### Rollout

Live at landing, at order 16. TOOL-dSafePassage-61 holds order 16 and stays DEFERRED, so this unit
does not close the order. It builds before TOOL-dSafePassage-87, which edits `read_fixture_rows` and
`check_grade_tree_clean` in the same file, and the builder of 87 re-reads each cited line by content.

### Files touched (estimate)

- `tools/govkit/upgrade_walk.py`

### Alternatives rejected

- **Repoint `ctx["govkit"]` at the pin's path.** Its readers at `:483` and `:523` run against the
  clone at its tip, which holds HERE's layout, so they would then run the pin's layout. The skeptic
  rejected the finder's fix for this reason.
- **The skeptic's bare f-string.** It reds at a pin whose tool root is the repo root (§4 "S1").
- **Inline the expression at `:212` with no function.** A grader could then only observe it by
  building a release tree, which costs a clone and an apply per run. The function lets the grader
  run on every invocation for milliseconds.
- **A grader that builds only a `scripts` tree.** At a HERE of `scripts/` the HERE-relative mutant
  would read correct there and stay green. Three trees make it red at every prefix.

## 5. Production-readiness checklist

- security: no new write path or spawn. The `apply` argv changes only its engine path, inside the
  scratch clone the leg already owns.
- perf / scale: the grader writes six small files into the scratch directory `check_graders` already
  makes, in milliseconds.
- error / empty / loading states: a clone with no `govkit/registry.toml`, or more than one, raises
  `derive_tool_root`'s `Refusal`. It is not a `Stop`, so it propagates out of `main` as a traceback,
  exit 1, and the parity leg grades that exit red as it grades exit 2. That case is not reachable at
  this pin.
- observability: the grader prints `grader · release-engine · ok` or `RED · <why>` with every other
  grader.
- risks: at a moved prefix the walk still stops after the apply, on M7, until TOOL-dSafePassage-87
  lands.
- testing: §7's New arm, AC2's moved-prefix probe and AC3's greps.
- migration: none.
- user docs: none. `help/upgrade-steps.md:436-437` already says exit 2 means release-0 does not apply
  clean, and this unit makes it apply clean at a moved prefix. No sentence changes.

## 6. Acceptance criteria

- **AC1** — When
  `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import upgrade_walk as u; print(u.check_graders())"`
  runs from the repository root, it prints `upgrade-walk: grader · release-engine · ok` and its last
  line is `[]`.
  Red when: `derive_release_engine` joins the clone with HERE's relative path, so it prints
  `grader · release-engine · RED · a pin at scripts derived` and `['grader release-engine']`.
- **AC2** — When the moved-prefix probe of §4 "Measured at writing time" runs
  `FOREIGN_PREFIX_PROBE=1 python upgrade_walk.py --case up` from the `scripts/govkit` directory of a
  clone of the build head with `git mv tools scripts` committed, it prints
  `upgrade-walk: release-0 applied by the pinned clone's own apply over the fixture's kits line · exit 0`
  and no line holding `release-0's apply exited`.
  Red when: the `apply` call runs `clone / ctx["govkit"]`, so the run prints
  `nothing measured: release-0's apply exited 2` and `can't open file`, as at `b634d60e5`.
  cost: one clone of the repository and one release-0 apply, about 70 seconds.
  fixture: a `git clone --no-hardlinks` of the build head under the temp root, with the move
  committed. The tree holds none today.
- **AC3** — When `git grep -n -F 'clone / ctx["govkit"]' -- tools/govkit/upgrade_walk.py` runs, it
  prints nothing; `git grep -n -F "derive_release_engine(" -- tools/govkit/upgrade_walk.py` prints
  three lines, the definition, the `apply` call and the grader; and
  `git grep -n -F '"govkit": f"{rel}' -- tools/govkit/upgrade_walk.py` prints one line, the
  HERE-relative `ctx["govkit"]` at `:204`.
  Red when: the fix repoints `ctx["govkit"]` at the pin's path, so the third grep prints nothing and
  the tip-side runs at `:483` and `:523` lose HERE's layout.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `upgrade-walk` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/upgrade_walk.py · covers AC1 · the `release-engine` grader of `check_graders`, staged red by a `derive_release_engine` that returns the clone joined with HERE's relative path, which reads the `scripts` tree as `tools` · none

The four `{prefix}/govkit/` legs are the guard join's for `tools/govkit/upgrade_walk.py`; its other
guards are broad. The foreign-prefix parity leg is not on the line. It is red at `b634d60e5` and stays
red after this unit (§3), and a leg line names what the unit keeps green. AC2 observes this unit's
part of that leg's row directly.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-86-1-spec-writer.md` and its
  brief `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-86-spec-brief.md`.
  It closes H1 (id 13) of the round-2 closing diff review,
  `memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-84-closing-diff-round2.md`,
  at the skeptic's corrected fix, with `resolve_prefix_token` in place of its f-string (§4 "S1").
  H1 was reproduced and S1 and S2 were staged and measured in clones of `b634d60e5` (§4 "Measured at
  writing time").
- rev-2 · 2026-10-29 · AC2 AC3 §3 · from the brief
  `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-88-spec-brief.md`. AC2's
  probe runs `upgrade_walk.py` from the moved clone's `scripts/govkit` directory. The walk finds gov
  through its own file (`upgrade_walk.py:1075`), and `--list` run from there on 2026-10-29 printed
  the pin line and the plant paths TOOL-dSafePassage-87's AC8 names. AC3's third grep reads its
  string up to `{rel}`, which still matches only `:204`. The spec-token check read both as
  untracked paths.
  §3 gains the hands-off edge to TOOL-dSafePassage-89, the mirror of its consumes-from.

## 10. Reuse audit

S1 extends govkit's two tool-root primitives, `derive_tool_root` (`tools/govkit/govkit.py:191`) and
`resolve_prefix_token` (`govkit.py:217`), which the same function already uses for `deploy.toml`
(`upgrade_walk.py:206-207`). S2 extends `check_graders` (`upgrade_walk.py:950`), TOOL-dSafePassage-77
S7's frame for the leg's own graders, with its `scratch` directory and its row tuple. No new seam.
`python tools/codebase-map/reuse_lookup.py "derive the engine path release-0's apply runs from the pinned clone's own tool root"`
ranked `derive_tool_root` as a seam at fan-in 8, beside name-stem matches (`run`, `repo_root`,
`engine`, `run_git`) that do not derive an engine path. The recall probe ranked TOOL-dSafePassage-5's
spec, the round-2 review and this brief first, then TOOL-aSweptBar-2 and TOOL-aSparedSpawn-10, the
foreign-prefix probe contract and its sharding, which this unit does not change.

Recall terms used: `python tools/memory-recall/query.py "release-0 apply runs a HERE-relative engine path the pinned clone lacks at a moved prefix" --terms "release-0 pin clone apply tool root prefix derive_tool_root resolve_prefix_token foreign-prefix moved grader upgrade-walk"`
