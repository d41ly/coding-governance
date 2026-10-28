# TOOL-dSafePassage-53 — the walk's listing handler: an absent directory is the empty population, and only an existing one that cannot be listed is refused

**Status:** CLOSED · rev-2 · 2026-10-28 · node d · Tier-2 · base 3708a705 · streams tooling · order 15 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-53-deviation-99.md](../build/2026-10-23-build-TOOL-dSafePassage-53-deviation-99.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-build-TOOL-dSafePassage-53-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-53-ledger.md) | journal | — |
| [2026-10-28-build-TOOL-dSafePassage-53-deviation-1.md](../build/2026-10-28-build-TOOL-dSafePassage-53-deviation-1.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md) | research | TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-59 |
| [2026-10-26-prompt-TOOL-dSafePassage-53-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-53-build-brief.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-brief.md) | research | TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-5 TOOL-dSafePassage-51 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-59 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |
| [2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md) | diff-review | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-61 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 51 and 52
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-51-52-spec-audit-round1.md`)
confirmed finding **id 22** at BLOCKER, merged with id 7 into its item **B1**. TOOL-dSafePassage-51
S6 and its §4 "The walk, in sequence" list each directory inside `try: ... except OSError: refuse d`.
`FileNotFoundError` is an `OSError`, so a listing of a directory git never creates is a refusal.

This unit's probes on node d, Python 3.14.5 and git 2.54.0.windows.1, 2026-10-23, under `%TEMP%`.
A real `git submodule add` wrote `.git/modules/sub/` holding `HEAD`, `config`, `objects`, `refs` and
six other entries, and no `modules`. `os.scandir` on a missing path raised `FileNotFoundError`, and
on a regular file it raised `NotADirectoryError`. Neither `.git/modules` nor
`.git/worktrees/unattended-dsafepassage-736310/modules` exists in gov's own tree.

This unit is id 22's promotion, the handler's half of B1. It splits the handler by error class, so
the absent class is the empty population and every other listing error stays a refusal. Id 7's
promotion, `TOOL-dSafePassage-54`, makes the trees git itself builds the walk's sound baseline. It
builds at order 15, one above TOOL-dSafePassage-51 (order 14), whose S6 it repairs. Built as
TOOL-51 S6 is written, TOOL-51's own pass would refuse every plant whose submodule git directory
holds no `modules/`, where TOOL-dSafePassage-47 AC1 expects exit 0. So
TOOL-dSafePassage-51's §3 hands-off bullet to this unit names the handler, and that pass builds it
this way.

## 2. Scope (IN)

- **S1** — The absent class. In `read_target_repositories`'s `modules/` walk (TOOL-dSafePassage-30
  S1, rooted by TOOL-dSafePassage-36 S1), `walk(d)` lists `d` with `os.scandir(d)` inside one `try`.
  Its first handler is `except FileNotFoundError: return`: no candidate, no refusal, nothing
  printed. That class covers `<git_dir>/modules/` in a repository with no submodules, and `<c>/modules`
  in a submodule git directory with no nested submodules. Observed by AC1 and AC3.
- **S2** — The refusal's population. The second handler is `except OSError`, a refusal naming `d` and
  the error's class name through TOOL-dSafePassage-24's one `raise Refusal` site. It covers an
  existing path the listing cannot read, such as a `modules` that is a regular file
  (`NotADirectoryError`) or a directory the user may not read (`PermissionError`). The `isolation`
  family gains the plant `submodule-modules-not-a-directory`: `.git/modules/a` is a sound repository
  whose `modules` is a regular file. Observed by AC1 and AC2.
- **S3** — The reading. TOOL-dSafePassage-51 S6's sentence "An `OSError` while listing a directory is
  a refusal naming that directory", and its §4 line `except OSError: refuse d`, are read with S1's
  handler first. TOOL-dSafePassage-47 §5 and TOOL-dSafePassage-36 §5, which say a target with no
  `modules/` yields no candidate, then hold at both positions the walk lists. Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- The sound-baseline plants built by real git and the walk over gov's own tree:
  `TOOL-dSafePassage-54`, id 7's half of B1.
- The link test on the root and on each recursion argument: `TOOL-dSafePassage-56`.
- An existence test before the listing, such as `os.path.lexists(d)`. The handler is the one place
  the absent class is decided, so a path that vanishes between a test and the listing is not a
  second case.
- The report's left-shift gates and checklist entries.

### Edges

- **consumes-from** `TOOL-dSafePassage-51` — S6's listing refusal and §4 "The walk, in sequence", whose handler this unit splits by class; without them there is no handler to correct
- **hands-off** `TOOL-dSafePassage-54` — the walk's sound baseline over the trees git builds, which reads this handler's absent class at the root and at every `c/modules`, finding 7 of the spec audit of units 51 and 52
- **hands-off** `TOOL-dSafePassage-56` — the link test on every path the walk enters, placed before this handler's listing so a dangling link is refused and never read as the absent class, finding 8 of the spec audit of units 51 and 52
- **hands-off** `TOOL-dSafePassage-59` — the listing's population taken from this handler's `os.scandir` with no type filter before the link test, finding 24 of the spec audit of units 51 and 52

## 4. Design

### The handler

```
walk(d):
  try:
    entries = os.scandir(d)
  except FileNotFoundError:      # S1, the absent class
    return
  except OSError as e:           # S2, an existing path the listing cannot read
    refuse d, type(e).__name__
  ...                            # TOOL-dSafePassage-51 §4, from `for c in entries`
```

| Path the walk lists | Listing raises | Outcome |
|---|---|---|
| `<git_dir>/modules/`, no submodules | `FileNotFoundError` | no candidate |
| `<c>/modules`, no nested submodules | `FileNotFoundError` | no nested candidate |
| `<c>/modules` a regular file | `NotADirectoryError` | refused, naming `<c>/modules` |
| a directory the user may not read | `PermissionError` | refused, naming it |

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: the `isolation` plant `submodule-modules-not-a-directory`.
No function, constant, conf key, gate leg or policy key. S2's refusal is TOOL-dSafePassage-24's one
`raise Refusal` site, so `tools/govkit/refusal_join.py`'s `BRANCH_PIN` does not move.

### Migration

None: no step row spawns before this build's walk lands.

### Rollout

Live at landing. It builds at order 15, one above TOOL-dSafePassage-51 (order 14). It shares
`tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py` with `TOOL-dSafePassage-54`, `TOOL-dSafePassage-56` and `TOOL-dSafePassage-59` at order 15, so the build
run sequences those passes by M6's first clause. The driver's id tie-break puts this unit first.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **`if not os.path.lexists(d): return` before the listing.** The report's first form. It decides
  the absent class in a second place beside the handler, and the handler would still refuse a
  `FileNotFoundError` raised after the test.
- **Returning on every `OSError`.** A `modules` that is a regular file, or a directory the user may
  not read, would pass with its configs ungraded.

## 5. Production-readiness checklist

- security: an unreadable or malformed `modules` entry still refuses the step; only a path git never
  created reads as empty.
- perf / scale: unchanged, one listing per directory.
- error / empty / loading states: an absent `modules/` is the empty population; any other listing
  error is a refusal naming the path and the error class, never a traceback.
- observability: the refusal names the path and the error's class name.
- risks: none beyond TOOL-dSafePassage-51's.
- testing: the probes and the plant of §6, through §7's arm.
- migration: none.
- user docs: N/A — `TOOL-dSafePassage-54` S3 writes the page sentence on the sound baseline, and the
  refusal wording is TOOL-dSafePassage-51 S6's.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe walks `tools/govkit/upgrade_steps.py` with `ast`, the `try` whose
  body calls `os.scandir` inside `read_target_repositories`'s walk has two handlers in this order:
  `FileNotFoundError`, whose body returns and raises nothing, then `OSError`, whose body raises
  `Refusal`.
  Red when: the `OSError` handler stands alone or first, so an absent `modules/` is refused.
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-modules-not-a-directory`
  runs, the step is refused naming `.git/modules/a/modules` and `NotADirectoryError`, the output holds
  no `Traceback`, and the run exits 1.
  Red when: the handler returns on every `OSError`, so the plant exits 0.
- **AC3** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path and calls
  `read_target_repositories` over a scratch repository made by `git init` under the run's scratchpad,
  which holds no `.git/modules/`, it returns one row, the target's own git directory, and raises no
  `Refusal`.
  Red when: the absent root is refused.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC2 AC3 · the self-test runs the `submodule-modules-not-a-directory` plant and the walk over a `git init` repository with no `modules/`; its failing cases are staged by a walk copy whose handler is TOOL-dSafePassage-51's single `except OSError` clause, under which the empty repository is refused, and by a walk copy that returns on every `OSError`, under which the plant exits 0 · none

What the check does not cover: a `PermissionError` listing, which node d cannot stage without
changing a directory's ACL, and the trees git itself builds, which `TOOL-dSafePassage-54` walks.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the spec audit of units 51 and 52's id 22
  (BLOCKER, item B1, shared with id 7).
- rev-2 · 2026-10-26 · §7 · the §7 leg line gains `policy fixtures`, whose guard a §4 Files touched path
  trips, per the spec-tokens repair handoff
  `memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-31-1-spec-writer.md`; no
  criterion's meaning moved.

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-51's walk in `read_target_repositories` (TOOL-dSafePassage-30
S1), with TOOL-dSafePassage-24's refusal site, all specced and unbuilt at the base: `git ls-files
tools/govkit` lists no `upgrade_steps.py`. `python tools/codebase-map/reuse_lookup.py "treat a directory that does not exist as an empty listing"`
ranked `note`, `read_id_list`, `declared_list` and `read_id_list_refusals`, name-token matches, none
listing a directory. So no existing seam fits beyond those specs. The recall probe ranked the
report's own appendix row for id 22 and `TOOL-cMendedVintage-19`, the rule that places a promoted
repair one above the unit it repairs, which sets order 15.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's blocker on a walk refusing a missing directory is promoted beside the unit it repairs" --terms "spec audit promoted blocker walk missing directory refusal FileNotFoundError submodule modules junction order"`
