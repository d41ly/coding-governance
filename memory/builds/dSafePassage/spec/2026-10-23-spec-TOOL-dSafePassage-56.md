# TOOL-dSafePassage-56 — the walk tests for a link on every path it enters, the root and each `modules/` it recurses into, before listing it

**Status:** DEFERRED · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 15 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-56-deviation-102.md](../build/2026-10-23-build-TOOL-dSafePassage-56-deviation-102.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-prompt-TOOL-dSafePassage-56-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-56-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 51 and 52
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-51-52-spec-audit-round1.md`)
confirmed finding **id 8** at HIGH, its item **H3**. The same defect was found at MEDIUM as id 23,
item M6, which is batched by its own id in `TOOL-dSafePassage-59`.

TOOL-dSafePassage-51 S6 says the walk never follows a symlink or a junction. Its §4 "The walk, in
sequence" tests `islink(c) or isjunction(c)` only on the children of a listed directory. The root
`<git_dir>/modules/` and each path passed to `walk(c/modules)` are listed with no link test. This
unit's probe on node d, Python 3.14.5, 2026-10-23, made a junction `m/a/modules -> m` with
`mklink /J`. `os.path.islink` read False, `os.path.isjunction` read True, and `os.scandir` listed
`['a']` through it, silently and at every depth. So a `c/modules` junction back to `.git/modules`
recurses until a path-length `OSError`, and one to a directory outside `.git/modules` is walked and
its configs read.

This unit is id 8's promotion. The link test runs at the top of `walk(d)`, before the listing, so
every path the walk enters gets the test a listed child gets. It builds at order 15, one above
TOOL-dSafePassage-51 (order 14), whose S6 it repairs, and after `TOOL-dSafePassage-53` by the
driver's id tie-break. TOOL-dSafePassage-51's §3 hands-off bullet to this unit names the rule, so
that pass may build it.

## 2. Scope (IN)

- **S1** — The test, once. `test_path_linked(path)` in `tools/govkit/upgrade_steps.py` returns True
  when `path` is a symlink or a junction, by the test TOOL-dSafePassage-51 S6 names. It takes no
  `stat` that follows a link. An absent path reads False. TOOL-dSafePassage-51 S6's child test is
  read as a call of it. Observed by AC1.
- **S2** — Every path entered. `walk(d)` calls `test_path_linked(d)` first, before
  `TOOL-dSafePassage-53`'s listing. A hit is a refusal naming `d`, through TOOL-dSafePassage-24's one
  `raise Refusal` site. So the root `<git_dir>/modules/` and every `<c>/modules` get the test each
  listed child gets. Because the test precedes the listing, a dangling link at `<c>/modules` is
  refused and never read as the handler's absent class. Observed by AC2 and AC4.
- **S3** — The plants. The `isolation` family gains `submodule-modules-link-nested`:
  `.git/modules/a` is a sound repository whose `modules` links back to `.git/modules`. It also gains
  `submodule-modules-link-outside`: `.git/modules/a/modules` links to a scratch directory outside
  `.git/modules` that holds a sound repository whose config sets `filter.canary.clean`. On Windows
  each link is a junction made with `cmd /c mklink /J`, and on POSIX a directory symlink.
  Observed by AC2 and AC3.
- **S4** — The claim it makes true. TOOL-dSafePassage-51 §5's "S6 stops the walk leaving the
  target's `.git/modules/` through a link" is read as holding over every path the walk enters.
  Observed by AC3.

## 3. Non-goals (OUT)

- The test's form on Python 3.11, where `os.path.isjunction` does not exist: finding 18, batched in
  `TOOL-dSafePassage-59`.
- A plant with a link at `<git_dir>/modules` itself, and the name-segment reading of
  `submodule-modules-link-loop`: finding 23, batched in `TOOL-dSafePassage-59`.
- Reparse points other than symlinks and junctions, which TOOL-dSafePassage-51 §3 leaves out.
- The report's left-shift gates and checklist entries.

### Edges

- **consumes-from** `TOOL-dSafePassage-51` — S6's link rule, its child test, the `submodule-modules-link-loop` plant and §5's claim, which S1 names once and S2 applies to every path entered
- **consumes-from** `TOOL-dSafePassage-53` — the listing handler this unit's test precedes, so a dangling link is refused before `os.scandir` can read it as absent
- **hands-off** `TOOL-dSafePassage-59` — `test_path_linked`'s form without `os.path.isjunction` for the 3.11 floor, a plant linking `<git_dir>/modules` itself, and the `os.scandir` population tested before any type filter, findings 18, 23 and 24 of the spec audit of units 51 and 52

## 4. Design

### The walk's entry

```
walk(d):
  if test_path_linked(d): refuse d                # S2, the root and every c/modules
  try: entries = os.scandir(d)                    # TOOL-dSafePassage-53's handler
  except FileNotFoundError: return
  except OSError as e: refuse d, type(e).__name__
  for c in entries:
    if test_path_linked(c): refuse c              # TOOL-dSafePassage-51 S6, through S1
    ...                                           # TOOL-dSafePassage-51 §4, from the shape test
      list c; walk(c/modules)                     # entered through S2's test
```

| Plant | Link at | Refusal names |
|---|---|---|
| `submodule-modules-link-loop` | `.git/modules/a/loop`, a listed child | `.git/modules/a/loop` |
| `submodule-modules-link-nested` | `.git/modules/a/modules`, a recursion argument | `.git/modules/a/modules` |
| `submodule-modules-link-outside` | `.git/modules/a/modules`, pointing outside | `.git/modules/a/modules` |

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: `test_path_linked`, cell `py.function`, verb `test`
(`python tools/lexicon/lexicon.py --suggest test_path_linked --as py.function` printed OK on
2026-10-23), and the `isolation` plants `submodule-modules-link-nested` and
`submodule-modules-link-outside`. No constant, conf key, gate leg or policy key. S2's refusal is
TOOL-dSafePassage-24's one `raise Refusal` site, so `tools/govkit/refusal_join.py`'s `BRANCH_PIN`
does not move.

### Migration

None: no step row spawns before this build's walk lands.

### Rollout

Live at landing. It builds at order 15, after `TOOL-dSafePassage-53`, and shares
`tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py` with that unit,
`TOOL-dSafePassage-54` and `TOOL-dSafePassage-59` at order 15, so the build run sequences the passes
by M6's first clause.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Testing each child and also each `c/modules` before the recursive call.** Two call sites for one
  rule, and the root would still need a third. One test at the top of `walk(d)` covers every path the
  walk enters.
- **Bounding the recursion depth.** A depth cap ends the loop but still walks and reads a junction to
  a directory outside `.git/modules`.

## 5. Production-readiness checklist

- security: the walk never leaves the target's `.git/modules/` through a link at any position, so
  no config outside it is read or listed.
- perf / scale: one `lstat` per path entered, beside the one per listed child.
- error / empty / loading states: a link at any position is a refusal naming that path, never a
  path-length `OSError`, a `RecursionError` or a silent loop.
- observability: the refusal names the linked path.
- risks: none beyond TOOL-dSafePassage-51's.
- testing: the probe and the plants of §6, through §7's arm.
- migration: none.
- user docs: N/A — TOOL-dSafePassage-51 S6 writes the page's link-refusal sentence, which this unit
  makes true at more positions without changing its words.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path and calls
  `test_path_linked` on a scratch junction or directory symlink, a plain directory and an absent path,
  it prints True, False and False.
  Red when: a junction reads False, as `os.path.islink` alone reads it.
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-modules-link-nested`
  runs, the step is refused naming `.git/modules/a/modules`, the output holds no `Traceback`, and the
  run exits 1 within 60 seconds.
  Red when: the walk lists through the junction, so it loops to a path-length `OSError` naming a
  deeper path, or to a `RecursionError`.
- **AC3** — When the same family runs with `--plant submodule-modules-link-outside`, the step is
  refused naming `.git/modules/a/modules`, the output never names `filter.canary.clean`, and the run
  exits 1.
  Red when: the walk enters the outside directory and grades its repository's config.
- **AC4** — When a `python -c` probe walks `tools/govkit/upgrade_steps.py` with `ast`, inside
  `read_target_repositories`'s walk a call `test_path_linked(d)` on the walk's own argument sits on a
  line before the `os.scandir(d)` call.
  Red when: the walk lists `d` before it tests `d`.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the self-test runs `test_path_linked` over a junction or symlink, and the `submodule-modules-link-nested` and `submodule-modules-link-outside` plants; its failing case is staged by a walk copy that tests only listed children, under which the nested plant ends in an `OSError` naming a deeper path and the outside plant names `filter.canary.clean` · none

What the check does not cover: a reparse point that is neither a symlink nor a junction, and a link
a POSIX host makes that Windows cannot, since every job this repo runs is Windows.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the spec audit of units 51 and 52's id 8
  (HIGH, item H3).

## 10. Reuse audit

The seams extended are TOOL-dSafePassage-51's walk and its child link test, with
`TOOL-dSafePassage-53`'s handler and TOOL-dSafePassage-24's refusal site, all specced and unbuilt at
the base. `python tools/codebase-map/reuse_lookup.py "refuse a path that is a symlink or junction before listing it"`
ranked `before`, `CensusRefused`, `ScopeRefused` and `build_spec_path_re`, name-token matches, none a
link test. `read_plain_stat` in `tools/run-gates/measure_legs.py:1373` refuses any `st_reparse_tag`
on each component. It lives in the run-gates kit, from which no `tools/govkit/*.py` imports
anything (`grep -n "measure_legs" tools/govkit/*.py` printed nothing on 2026-10-23), and
`TOOL-dSafePassage-59` names it in TOOL-dSafePassage-51's alternatives. So no existing seam fits
beyond those specs.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's blocker on a walk refusing a missing directory is promoted beside the unit it repairs" --terms "spec audit promoted blocker walk missing directory refusal FileNotFoundError submodule modules junction order"`
