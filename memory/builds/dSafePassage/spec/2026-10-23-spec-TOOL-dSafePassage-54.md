# TOOL-dSafePassage-54 — the walk's sound baseline: a plain submodule git built and gov's own tree, each walked to exit 0 with no refusal

**Status:** CLOSED · rev-2 · 2026-10-28 · node d · Tier-2 · base 3708a705 · streams tooling · order 15 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-54-deviation-100.md](../build/2026-10-23-build-TOOL-dSafePassage-54-deviation-100.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-build-TOOL-dSafePassage-54-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-54-ledger.md) | journal | — |
| [2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md) | research | TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-59 |
| [2026-10-26-prompt-TOOL-dSafePassage-54-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-54-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 51 and 52
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-51-52-spec-audit-round1.md`)
confirmed finding **id 7** at BLOCKER, merged with id 22 into its item **B1**. TOOL-dSafePassage-51
§4 "The walk, in sequence" calls `walk(c/modules)` for every listed candidate and lists
`<git_dir>/modules/` with no thought for whether git created either. Git creates neither in the
common case. Every plant the walk's specs mint is hand-shaped, so none of them carries the tree git
actually writes, and the defect was reachable only by reading the design against git.

This unit's probes on node d, git 2.54.0.windows.1, 2026-10-23. In a scratch superproject under
`%TEMP%`, `git submodule add ../sub sub` wrote `.git/modules/sub/` with `HEAD`, `config`,
`description`, `hooks`, `index`, `info`, `logs`, `objects`, `packed-refs` and `refs`, and no
`modules`. In gov's own tree `git rev-parse --git-dir` printed
`C:/projects/coding-governance/.git/worktrees/unattended-dsafepassage-736310`, and neither that
directory nor the common `.git` holds a `modules` directory. TOOL-dSafePassage-8 walks every step on
gov's own tree first.

This unit is id 7's promotion, the baseline's half of B1. It makes the trees git itself builds a
sound baseline the walk must pass, and states which paths the walk enters. Id 22's promotion,
`TOOL-dSafePassage-53`, splits the listing handler so the absent class is empty. This unit builds at
order 15, one above TOOL-dSafePassage-51 (order 14), whose S6 it repairs, and after
`TOOL-dSafePassage-53` by the driver's id tie-break. TOOL-dSafePassage-51's §3 hands-off bullet to
this unit names the baseline, so that pass may run it too.

## 2. Scope (IN)

- **S1** — The plant git builds. The `isolation` family of `python3 "tools/govkit/upgrade_steps.py" fixture`
  gains `submodule-sound-no-nested`. It is made by running git, never by writing directories: a
  scratch repository with one commit, then `git -c protocol.file.allow=always submodule add` of it into
  a scratch superproject. No config of either sets a key the refused-key table names. The walk lists
  `.git/modules/<name>` and the step is not refused. Observed by AC1.
- **S2** — Gov's own tree. `read_target_repositories` called on the repository root of gov's own
  tree returns exactly one row, the git directory `git rev-parse --absolute-git-dir` prints, and
  raises no `Refusal`. This is the tree TOOL-dSafePassage-8's gov-first walk enters. Observed by AC2.
- **S3** — The paths the walk enters. The walk enters `<git_dir>/modules/` and, for each candidate
  `c`, `<c>/modules`. Either may be absent, and an absent one is the empty population that
  `TOOL-dSafePassage-53`'s handler returns. TOOL-dSafePassage-51 S6 and its §4 are read with that
  sentence, and the "What a step can reach" section of `help/upgrade-steps.md` says that a target
  with no submodules, or whose submodules have none nested, passes the walk with no refusal.
  Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- The handler's error classes and the `submodule-modules-not-a-directory` plant:
  `TOOL-dSafePassage-53`.
- A git-built plant for each hand-shaped plant the walk already carries. The baseline is the two
  sound trees; the hand-shaped plants stay as their units mint them.
- The report's left-shift gates and checklist entries.

### Edges

- **consumes-from** `TOOL-dSafePassage-53` — the listing handler whose first clause returns the empty population on `FileNotFoundError`; without it both baseline trees are refused
- **consumes-from** `TOOL-dSafePassage-51` — S6, §4 "The walk, in sequence" and §4 "The section probe", which S3 reads and AC3 runs

## 4. Design

### The baseline

| Tree | Made by | Paths the walk enters | Outcome |
|---|---|---|---|
| `submodule-sound-no-nested` | `git init`, `git commit`, `git submodule add` | `.git/modules/`, `.git/modules/<name>/modules` (absent) | `<name>` listed, exit 0 |
| gov's own tree | the checkout itself | `<git_dir>/modules/` (absent) | the target's own row only |

The plant needs `protocol.file.allow=always`. Without it, git 2.54.0.windows.1 on node d,
2026-10-23, printed `fatal: transport 'file' not allowed` and exited 128 on the same
`submodule add`. The fixture sets it on that one command line, never in a config file.

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: the `isolation` plant `submodule-sound-no-nested`. No
function, constant, conf key, gate leg or policy key.

### Migration

None: no step row spawns before this build's walk lands.

### Rollout

Live at landing. It builds at order 15, after `TOOL-dSafePassage-53`, and shares
`tools/govkit/upgrade_steps.py`, `tools/govkit/selftest.py` and `help/upgrade-steps.md` with that unit,
`TOOL-dSafePassage-56` and `TOOL-dSafePassage-59` at order 15, so the build run sequences the passes
by M6's first clause.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **A hand-written `.git/modules/<name>/` with `HEAD`, `objects/` and `refs/`.** It carries the tree
  its author imagines, which is how S6's defect passed every plant. Git's own `submodule add` writes
  the tree the walk meets.
- **Running the baseline over the superproject of an adopter.** No adopter tree is on node d, and
  gov's own tree is the one TOOL-dSafePassage-8 walks first.

## 5. Production-readiness checklist

- security: N/A — a fixture and a reading; the refusals are unchanged.
- perf / scale: one scratch clone per self-test run.
- error / empty / loading states: an absent `modules/` at either position is the empty population.
- observability: the plant prints the population it listed.
- risks: the plant depends on git's `submodule add` layout, which is what it exists to track.
- testing: the plant and the probe of §6, through §7's arm.
- migration: none.
- user docs: the "What a step can reach" section of `help/upgrade-steps.md`, S3.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-sound-no-nested`
  runs, its population holds the superproject's row and one row for `.git/modules/<name>`, it prints
  no refusal and no `Traceback`, and the run exits 0.
  Red when: the walk refuses `.git/modules/<name>/modules`, which git never created.
- **AC2** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path and calls
  `read_target_repositories` on gov's own repository root, it returns one row whose git directory
  equals `git rev-parse --absolute-git-dir`, and raises no `Refusal`.
  Red when: the absent `<git_dir>/modules/` is refused, so every gov-first walk stops.
- **AC3** — When TOOL-dSafePassage-51's §4 "The section probe" runs over `help/upgrade-steps.md`, its
  output holds a line saying that a target with no submodules, or whose submodules have none nested,
  passes with no refusal.
  Red when: the section says nothing of the sound baseline.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the self-test runs the `submodule-sound-no-nested` plant and the walk over gov's own tree as the sound baseline; its failing case is staged by a walk copy whose listing handler is TOOL-dSafePassage-51's single `except OSError` clause, under which both are refused · none

What the check does not cover: a submodule layout another git version writes, and a nested
submodule git built, whose `modules/` exists and which TOOL-dSafePassage-30's `submodule-nested`
plant covers by hand.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the spec audit of units 51 and 52's id 7
  (BLOCKER, item B1, shared with id 22).
- rev-2 · 2026-10-26 · §7 · the §7 leg line gains `policy fixtures`, whose guard a §4 Files touched path
  trips, per the spec-tokens repair handoff
  `memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-31-1-spec-writer.md`; no
  criterion's meaning moved.

## 10. Reuse audit

The seams extended are TOOL-dSafePassage-30's `read_target_repositories` and its `isolation`
fixture family, with TOOL-dSafePassage-51's walk, all specced and unbuilt at the base.
`python tools/codebase-map/reuse_lookup.py "treat a directory that does not exist as an empty listing"`
ranked `note`, `read_id_list` and `declared_list`, name-token matches, none a fixture that builds a
repository with git. So no existing seam fits beyond those specs. The plant's layout was measured
against git on node d, not taken from a record.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's blocker on a walk refusing a missing directory is promoted beside the unit it repairs" --terms "spec audit promoted blocker walk missing directory refusal FileNotFoundError submodule modules junction order"`
