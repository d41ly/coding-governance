# TOOL-aMendedFleet-57 — shrink-only lists are graded against their low-water mark

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 57

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`shrink_only_lists_not_shrinking` compares each shrink-only list's count today with its count at
the commit that added the file. A list that drained to empty and then grew back reads as shrinking,
because it is still below the count it was seeded at: `memory/project/unarmed-branches.txt` was
seeded at 9, drained to 0, and later held 3, then 15, rows while its seed reading said "shrunk by 6".
This unit grades each list against its LOW-WATER MARK, the smallest count its mainline history ever
recorded, so a list that rises above the lowest point it reached is named as regrown. The seed
reading's one other case, a list that never drained at all, stays an offender.

## 2. Scope (IN)

- **S1** — ONE HISTORY WALK. `derive_low_waters` in `tools/drift-audit/drift_report.py` takes the
  `SHRINK_ONLY` paths and runs ONE `git log --first-parent --diff-merges=first-parent -p --reverse`
  over all of them, replaying the lines each commit adds to and takes from each file, counted only
  when non-blank and not a `#` comment, which is the rule `_entries` already counts by. It returns,
  per path, the
  smallest running count after any commit, or `None` when the path has no history on the first-parent
  line or the replay ever goes negative, which means the replay misread a patch and the row cannot be
  judged. Observed by AC1 and AC4.
- **S2** — THE PREDICATE, as one testable value. `check_shrink_row(seed, low_water, entries)` returns
  `regrown` when `entries` exceeds `low_water`, `never drained` when `seed` is positive and `entries`
  is at least `seed`, and `None` otherwise, so a list seeded empty and still empty is never an
  offender. Observed by AC2 and AC3.
- **S3** — THE SIGNAL. `signal_shrink_only` calls S1 once and S2 per row. Each detail row keeps
  `entries`, `seed` and `shrunk_by` as they are and gains `low_water` and `reason`; the value is the
  number of rows whose `reason` is not `None`; a row whose low-water is `None` is counted in a new
  `unjudgeable` field and never as an offender. `gateable` stays false and the pin is untouched.
  Observed by AC1, AC2 and AC3.
- **S4** — The comment above the predicate in `signal_shrink_only` is rewritten to state both
  reasons and to keep the warning against narrowing the never-drained case, and the drift-audit
  README's row for the signal asks whether a list rose above the lowest count it reached. Observed by
  AC5.
- **S5** — Self-test arms in `tools/drift-audit/selftest.py`: a truth table over S2, and a fixture
  list committed at 2, 1, then 2 entries that reads `regrown` where the seed reading reads shrinking.
  NOT OBSERVED by a criterion here: the suite runs once at the close, and the arms are declared under
  `New arm:` in §7.
- **S6** — `memory/map/generated/symbols.json` is regenerated for the two new definitions.
  NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is
  its check, and §7 names the legs that read it.

## 3. Non-goals (OUT)

- The records-only spec-header declaration that `TOOL-aProbedToolkit-18` asks for. It is a second
  mechanism and §8 F1 splits it out.
- Making the signal gateable or giving it a pin above 0. A list may sit still for a week; the
  signal stays a report.
- Replaying history beyond the first-parent line, or across a rename. A list renamed loses its
  history before the rename, which is the seed reading's limit too.
- Bumping the drift-audit kit version, owed once at the close.

### Edges

- **hands-off** external — the records-only spec-header declaration, a new unit the run adds when it
  performs §8 F1's split.
- **hands-off** external — the drift-audit kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at the worktree HEAD `725b1449`, whose bytes under `tools/drift-audit/` equal base `7af5f564`'s.

- `signal_shrink_only` runs `git log --diff-filter=A` and one `git show` per list, and marks a row
  stalled when `shrunk_by` is at most 0, excluding a list seeded empty and still empty.
- `python tools/drift-audit/drift_report.py --json` reported value 2 of 5 at writing:
  `memory/project/curation-debt.txt` (seed 0, entries 4) and `memory/project/trace-waiver.txt`
  (seed 5, entries 9). PINNED, measured 2026-10-04.
- A scratch replay of one first-parent patch walk over the five lists gave these series. PINNED,
  measured 2026-10-04; S1 re-derives them.

| List | First-parent series | Low-water | Today |
|---|---|---|---|
| `memory/project/id-orphan-waiver.txt` | 4 5 0 1 0 | 0 | 0 |
| `memory/project/curation-debt.txt` | 0 2 5 6 6 6 7 7 4 4 4 5 4 3 4 | 0 | 4 |
| `memory/project/corpus-path-unresolved.txt` | 0 | 0 | 0 |
| `memory/project/unarmed-branches.txt` | 9 0 1 1 1 3 3 3 4 3 11 14 14 14 15 15 0 | 0 | 0 |
| `memory/project/trace-waiver.txt` | 6 7 8 9 10 9 8 9 10 9 | 6 | 9 |

- Each replayed final count equals what `_entries` reads today, so the replay is faithful on this
  tree. The two readings agree on today's value of 2; they part on history, where the unarmed list at
  3 and at 15 rows read "shrunk" by seed and `regrown` by low-water.
- The walk took well under a second on node a, one git spawn for all five lists.

### Inventory

- `derive_low_waters` and `check_shrink_row` — cell `py.function`; answered OK from
  `python tools/lexicon/lexicon.py --suggest derive_low_waters --as py.function`, and the same for
  `check_shrink_row`.
- `low_water`, `reason` and `unjudgeable` — JSON keys of the record; no naming cell grades them.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Walk the full history, merges included.** The full walk interleaves sibling branches by date:
  for `memory/project/curation-debt.txt` it read counts of 8 and 9 that the first-parent line never
  held. A low-water mark is a fact about the line the list lives on.
- **One `git show` per commit per list.** About sixty spawns at this tree's history; at the measured
  cost of a git spawn on node a, tens of seconds for a seconds-tier report.
- **Replace the seed reading outright.** It would lose the never-drained case, which the existing
  comment names as the one case this signal exists for.

## 5. Production-readiness checklist

- security — N/A: reads this repo's own history; no new input.
- perf / scale — one git spawn for every list together, replacing none of the existing ones.
- error / empty / loading states — a path with no first-parent history, or a negative replay, is
  `unjudgeable`, counted and never guessed; a list absent from the tree keeps today's `-1` entries.
- observability — each row names its `low_water` and its `reason`.
- risks — a squash or rewrite on the first-parent line can hide a low point; the reading is then the
  seed reading's at worst.
- testing — AC1 to AC5 here; the arms in S5.
- migration — N/A: nothing stored changes, and the existing JSON keys keep their meaning.
- user docs — the README row in S4.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --json` runs at the worktree root, every
  detail row of the `shrink_only_lists_not_shrinking` record carries `low_water` and `reason`, the
  row for `memory/project/trace-waiver.txt` reads low-water 6 and reason `regrown`, and the row for
  `memory/project/curation-debt.txt` reads low-water 0 and reason `regrown`.
  Red when: a row lacks either key, or a low-water disagrees with the first-parent replay.
  figure: PINNED at writing, 2026-10-04; the §4 replay re-derives it.
- **AC2** — When three non-comment rows are appended to `memory/project/unarmed-branches.txt` in the
  working tree and `python tools/drift-audit/drift_report.py --json` runs, the record's `value` is one
  more than in AC1 and that file's row reads `regrown` with low-water 0, although its `shrunk_by`
  reads 6; restoring the file returns the value.
  Red when: a list that rose above its low-water but stayed under its seed reads as shrinking, which
  is the seed reading's verdict.
- **AC3** — When the same report runs on the unedited tree, the rows for
  `memory/project/corpus-path-unresolved.txt` and `memory/project/id-orphan-waiver.txt` read reason
  null.
  Red when: a list seeded empty and still empty, or one drained to its low-water, is an offender.
- **AC4** — When `grep -n "first-parent" tools/drift-audit/drift_report.py` runs, its only hits sit
  inside `derive_low_waters` on one `git log` call, and the record AC1 printed carries
  `unjudgeable` 0.
  Red when: the walk spawns once per commit or per list, or a faithful replay is reported as
  unjudgeable.
- **AC5** — When `grep -n "shrink_only_lists_not_shrinking" tools/drift-audit/README.md` runs, the
  signal-table row asks about the lowest count a list reached.
  Red when: the README still describes only the seed comparison.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `drift-audit wiring` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/drift-audit/selftest.py` · a truth table over `check_shrink_row`, and a fixture list committed at 2, 1 and 2 entries, staged red by making the predicate compare against the seed · `CHECK_FLOOR` moves by the checks the arms add

## 8. Open questions

- **F1** — The brief's point names two mechanisms: grading shrink-only lists against a low-water
  mark, and a records-only deliverable declared in the spec header (`TOOL-aProbedToolkit-18`).
  The second changes the spec format and signal 6's waiver path, not this signal; its immediate red
  was cleared on 2026-09-20 by a `memory/project/trace-waiver.txt` row, and the header declaration
  it asks for does not exist on this tree.
  RESOLVED (agent, 2026-10-04, delegated): split — the records-only spec-header declaration of
  `TOOL-aProbedToolkit-18` moves to a new unit the run adds; this unit keeps the low-water mark,
  which is the roster row's mechanism.
- **F2** — Which history defines the low-water mark?
  Options: every commit reachable from HEAD, in date order; the first-parent line with merges
  diffed against their first parent. The probe in §4 measured both: the full walk reported counts
  the mainline never held.
  RESOLVED (agent, 2026-10-04, delegated): the first-parent line, per S1.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's drift-audit item 9 ([#57]) and a replay
  of the five lists' first-parent history at base.

## 10. Reuse audit

The seam extended is `signal_shrink_only` in `tools/drift-audit/drift_report.py`, with its
`_entries` counting rule reused for the replay and its `SHRINK_ONLY` declaration in
`tools/drift-audit/drift_signals.py` read unchanged. `python tools/codebase-map/reuse_lookup.py
"grade a shrink-only waiver list against the lowest count it ever reached in history"` returned
`count_never_falls` in `tools/govkit/govkit.py`, a before/after predicate in another kit that a kit
file may not import, whose docstring's lesson S2 follows: the decision is one pure function a truth
table grades. It also returned `scan_history` in `tools/memory-tree/transition_audit.py`, which walks
status transitions, not list counts; no existing seam replays a file's count over history, so the
walk lives beside the signal that reads it. The scan names `.sh` as unscanned; no shell file is
involved. Recall returned `TOOL-aUnmannedHelm-6`, that a floor asserted against the set it is
derived from is vacuous, which is why the low-water comes from history and not from the list, and
`TOOL-dMuffledSentinel-2` on the waiver registries' declared paths. Where the report and the tree
disagree: the report gave no figure for this point; the §4 series are this spec's own measurement.

Recall terms used: `python tools/memory-recall/query.py "how should a shrink-only list be graded
when it drains and then regrows" --terms "shrink_only_lists_not_shrinking SHRINK_ONLY seed shrunk_by
low-water drift-audit waiver curation-debt trace-waiver regrow ratchet"`
