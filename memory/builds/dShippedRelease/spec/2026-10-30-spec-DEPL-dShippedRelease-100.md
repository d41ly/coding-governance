# DEPL-dShippedRelease-100 — The ended-leg record holds a deleted path too, so the `[path]` arm reads what the `[leg]` arm reads

**Status:** OPEN · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 3 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-93 DEPL-dShippedRelease-103 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-105 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 30 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, HIGH, item H8. `tools/check-spec-tokens.py` grades each path-shaped
word of a backticked §6 token and hits when it is untracked. Unit 10 S9 takes `tools/check-kit-versions.sh`
and `tools/memory-tree/check-verdict-epoch.sh` out of the tree, and nine foreign live specs name them.
Unit 66 covers the `[leg]` arm only, the SHRINK-ONLY waiver file holds no row for either name, and its
S5 and AC4 forbid that route. Its AC1 asserts only "no `[leg]` hit", so it passes while the leg stays
red.

## 2. Scope (IN)

- **S1** — The row. `memory/project/ended-legs.txt` admits a row whose first cell is a path, told by
  `check_path_shaped`, with the same `<ended-on>` and `<retiring unit>` cells and a `<successor>` that
  is a tracked path or `none`. Unit 10 S9's two scripts get a row each, by the join of §4. Observed by
  AC1.
- **S2** — The arm. `read_ended_legs(root)` returns both kinds, and the path arm at
  `tools/check-spec-tokens.py:1570` counts a word on a path row as held, in a spec whose filename date
  is on or before that row's `ended-on`. A later spec naming the path is a hit. Observed by AC1, AC2.
- **S3** — The line. Every run prints `spec-tokens: ended-path join · <n> token(s) · <m> live spec(s) ·
  <r> row(s)`, held tokens by name under `--list`. Observed by AC1.
- **S4** — The refusals. A path row naming a tracked path, a `<successor>` untracked and not `none`, and
  a row no live spec produces each print as `ENDED` findings and red, as unit 66 S4's do. Observed by
  AC3.

## 3. Non-goals (OUT)

- The waiver file: unit 66 S5 stands, and its SHRINK-ONLY header with it.
- Editing a foreign spec's §6: the brief's rule, kept.
- A rule that any unit deleting a path runs this probe: the audit's left-shift item.

### Edges

- **consumes-from** `DEPL-dShippedRelease-66` — `ended-legs.txt`, `read_ended_legs` and the `ENDED` refusals this unit extends
- **consumes-from** `DEPL-dShippedRelease-10` — S9's two deletions
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 73)

## 4. Design

### Evidence

- `tools/check-spec-tokens.py:1570` hits a path-shaped word not in `git ls-files`, and `:1104` is `check_path_shaped`.
- Unit 10 S9 takes both scripts out, and report id 30's join printed 10 and 2 token hits across 10 specs, nine foreign plus unit 65, which is terminal by the close. PINNED at `f4597719`, and S1 re-derives the population.
- `read_waivers` at `:1216` is the reader's shape, and `memory/project/spec-token-waivers.txt` holds 0 rows for either name.

### The join

For every path S9 ends: every live spec whose §6 holds that word in a backticked token. A path with no such spec needs no row.

### Supersedes

- Unit 66 S1's row population, S2's `:1548` alone and AC1's "no `[leg]` hit", which reads with no `[path]` hit on the retired names beside it.
- Unit 66 §8 F1 stands: this is its record, read by a second arm.

### Files touched (estimate)

- `tools/check-spec-tokens.py`: S2, S3, S4
- `memory/project/ended-legs.txt`: S1
- `tools/check-spec-tokens.test.sh`: the arm of §7
- `memory/map/features/spec-tokens.md`: the arm's sentence

## 5. Production-readiness checklist

- security — N/A — a read over tracked files.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — the join's line on every run, and `--list` naming each held token.
- risks — a path row goes stale when its last live spec closes, and reds until the row goes; the printed remedy names it.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — a repo-root tool; `memory/map/features/spec-tokens.md` states the arm.

## 6. Acceptance criteria

- **AC1** — When `python tools/check-spec-tokens.py --list` runs on a scratch copy with both scripts out
  of the tree and the rows in place, it prints no `[path]` hit and no `[leg]` hit on those names, and
  prints `ended-path join`.
  Red when: a live spec nobody may edit reds on a deleted path, the leg arm's defect left standing.
  cost: 465.2s on node a, `tools/run-gates/ceiling-evidence.txt:133`, under a 940-second ceiling.
- **AC2** — When the same copy holds a spec dated after a row's `ended-on` naming that path in §6, it
  prints a `[path]` hit on that spec.
  Red when: a new spec can lean on the row.
- **AC3** — When `ended-legs.txt` holds a path row naming a tracked file, or a row no live spec names,
  the run prints `ENDED` and exits 1.
  Red when: a stale row hides a live hit.

## 7. Gates

`memory-hygiene self-test` · `kit/dogfood doc parity` · `build-index selftest` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/check-spec-tokens.test.sh · covers AC1 AC2 AC3 · a fixture tree with one path taken out and one row, its failing case the row read for a later spec · none

## 8. Open questions

- **F1 — A row kind, or a second file?** Options: (a) a row whose first cell is path-shaped, in
  `ended-legs.txt`; (b) a second record; (c) a fifth column. (b) is a second reader and a second
  registry row for one rule, and (c) moves every row unit 66 wrote. RESOLVED (agent, 2026-11-01,
  delegated): (a), rung 3, `check_path_shaped` already draws the line. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 30 (HIGH, item H8) of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 125); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `read_ended_legs` (unit 66 S2) and the path arm of `tools/check-spec-tokens.py`, with `check_path_shaped` at `:1104` deciding the row kind.
`python tools/codebase-map/reuse_lookup.py "retire a tracked path and keep older specs resolvable"`
ranked `resolve`, `tracked`, `resolve_kit_dir` and `resolve_caps`, name-stem helpers and no retirement
record. The recall probe surfaced PLAY-dOrderedCharter-26's shrink-only list and TOOL-dWitnessedBar-16,
which agree that a keyed list is the idiom.

Recall terms used:
`python tools/memory-recall/query.py "how does a spec keep resolving a path a later unit deletes" --terms "retired path spec tokens ended-legs waiver SHRINK-ONLY check-kit-versions deleted path arm live spec"`
