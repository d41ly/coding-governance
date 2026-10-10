# TOOL-aRoutedQuill-9 — the routed-commits leg reads green in WHOLE mode at the tip that lands

**Status:** SPECCED · rev-1 · 2026-10-10 · node a · Tier-1 · base e6585db4 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-10-prompt-TOOL-aRoutedQuill-9-spec-brief.md](../prompts/2026-10-10-prompt-TOOL-aRoutedQuill-9-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The routed-commits leg (`tools/memory-tree/routed_commits.py`) is red in WHOLE mode at head
4edeb467, because the reconcile merge 8f493d467 of origin/main e6585db4 brought in three cutoff-day
mints that touch `ROUTED_PATHS`, name no unit and are not in `ROUTED_COMMIT_WAIVED`. This unit makes
the waiver set exactly the set the leg names, records how that set is derived so the close re-derives
it after its last reconcile, and files the bug class that let the B1 fix certify a green it did not
have.

## 2. Scope (IN)

- **S1** — `ROUTED_COMMIT_WAIVED` in `.memory-tree.conf` gains the three shas the leg names at head:
  `d6aae9d18478`, `22efab659eaf` and `670436cd5f16`. The value then lists exactly the violations the
  leg reports with the value blank, no more and no fewer, so the leg exits 0 in WHOLE mode at the
  pass commit. Observed by AC1 and AC2.
- **S2** — The comment above `ROUTED_COMMIT_WAIVED` names the new group: three version mints from
  other sessions, committed on the cutoff day, that reached this branch by the reconcile of
  origin/main e6585db4. It also states the derivation in one sentence: blank the value, run the leg
  with `GATE_PUSH_BASE` unset, and list exactly the shas it names under FAILED. The value is
  re-derived that way after every reconcile, never copied from a review or a list. Observed by AC3.
- **S3** — A new `memory/gotchas/` class record,
  `history-leg-graded-before-the-reconcile-commit.md`, for "a history-wide leg graded before the
  reconcile commit is graded on the wrong history". `gotchas.py --write` re-renders
  `memory/gotchas/INDEX.md`. Observed by AC4.
- **S4** — The record's inventory key is claimed under `gotcha-classes` in
  `memory/map/features/memory-tree-hygiene.md`, the dossier that owns the leg, and
  `gen_map.py --write` regenerates the map artifacts in the same commit. Observed by AC5.
- **S5** — The kickoff manifest's `last-audit` in `memory/guides/SESSION-KICKOFF.md` is re-stamped,
  because `.memory-tree.conf` is in its `watch:` list, with the delta line in the commit message as
  the B1 fix commit 5b4f964d5 did. Observed by AC6.

## 3. Non-goals (OUT)

- No change to `routed_commits.py`, its grading, its WHOLE/RANGE split or its waiver semantics. A
  waiver keyed on something other than a listed sha, such as ancestry of a merge's second parent, is
  a gate-semantics change and is out of scope for a Tier-1 data unit.
- No change to which mode the landing push grades. That the push grades RANGE only, so remote CI sees
  a WHOLE-mode red the push never ran, is `TOOL-aRoutedQuill-10`'s mechanism (closing review H1).
- No re-derivation at the landing tip inside this unit. The run reconciles origin/main once more
  before landing, which may bring in more cutoff-day mints from sessions that do not yet know the
  rule. The close re-derives the value by S2's sentence at that tip; this unit cannot observe a tip
  that does not exist yet.
- No change to `ROUTED_COMMIT_CUTOFF`. See §4 Alternatives rejected.

## 4. Design

S1 is a data edit. The prefixes are 12 hex characters, the length the eight existing entries use,
and each is taken with `git rev-parse --short=12` from the full sha, never typed by hand. The leg
matches a waiver by prefix and reds a listed sha that is not a violation as stale, so the set must be
exact: a fourth sha "just in case" is a red, not a margin.

S2's derivation is the one procedure that cannot drift from the leg, because the leg is the oracle.
With the value blanked in the working copy, `env -u GATE_PUSH_BASE python
tools/memory-tree/routed_commits.py` prints every violation as an indented line opening with its
8-character prefix. That list is the waiver set. The conf is restored with the derived value
before anything is committed.

S3's record follows the class shape the catalogue already uses, with front matter `name`,
`description` and `kind: class`, and the sections Symptom, Where it bit, The fix, What it is not and
The gate. It must carry these facts:

- **Symptom.** A leg that grades HISTORY rather than files was observed green, the waiver or fix
  was committed, and the leg is red at the commit. Between the observation and the commit a
  reconcile merge was committed, which touched none of the fix's files but added commits to the
  population the leg grades.
- **Where it bit.** aRoutedQuill on node a, 2026-10-10. Commit 5b4f964d5 says the leg "now exits 0
  (graded 39, 8 waived)". At that commit it grades 45 and fails on three shas the reconcile 8f493d467
  brought in. Closing review round 2 confirmed it with all three lenses.
- **The fix.** A history-graded observation names the tip it was taken at. It is re-taken after the
  LAST merge, at the commit that ships it. A waiver set for such a leg is derived from the leg's own
  output at that tip, never from a review's list.
- **What it is not.** It is not `observation-before-the-last-fold-of-the-same-commit`. That class's
  remedy is to re-run the observations that count over the files the last fold touched. A reconcile
  merge touches none of those files, so the remedy selects nothing here: the population is the
  commit graph, not a file set.
- **The gate.** No machine gate exists in this unit. The documented check is S2's derivation at the
  final tip. `TOOL-aRoutedQuill-10` is the unit that would make the landing push grade the leg as
  remote CI does. The record names it as the gate to point at only once that unit is CLOSED.

Its anchors are the backticked paths `tools/memory-tree/routed_commits.py` and
`.memory-tree.conf`, so `gotchas.py --for-paths` selects it for either. Anchors are derived from the
body, so no `anchors:` field is written.

### Files touched (estimate)

`.memory-tree.conf`
`history-leg-graded-before-the-reconcile-commit.md` (new, under `memory/gotchas/`)
`memory/gotchas/INDEX.md`
`memory/map/features/memory-tree-hygiene.md`
`memory/map/generated/MAP.md`
`memory/map/generated/inventories.json`
`memory/map/generated/CARDS.md`
`memory/guides/SESSION-KICKOFF.md`

### Alternatives rejected

- **Move `ROUTED_COMMIT_CUTOFF` to 2026-10-10.** This would excuse every cutoff-day commit at once,
  with no list to maintain. It loses on a probe: `git log --no-merges --format='%cs %s'
  5a836bf0f..HEAD` restricted to `ROUTED_PATHS` holds 3 of this build's own product commits dated
  2026-10-09 (PINNED, measured 2026-10-10 at 4edeb467). Moving the cutoff would stop grading the very
  build that introduced the leg.
- **Waive the three by a pattern such as the `mint:` subject prefix.** That is a new waiver grammar in
  `routed_commits.py`, which is gate semantics and violates §3's first non-goal. It would also excuse
  every future unattributed mint, which is the population the leg exists to grade.

## 5. Acceptance criteria

- **AC1** — When `env -u GATE_PUSH_BASE python tools/memory-tree/routed_commits.py` runs at the pass
  commit, it exits 0. Its summary line shows a waived count equal to the number of tokens in
  `ROUTED_COMMIT_WAIVED`, and no `FAILED` line is printed.
  Red when: any of `d6aae9d18478`, `22efab659eaf` or `670436cd5f16` is missing, which prints FAILED
  naming it and exits 1. It is also red when a listed sha is not a violation, which prints the stale
  line and exits 1.
  figure: DERIVED. The waived count is read from the conf value at the commit graded, and it is 11 at
  this unit's pass only if no further reconcile precedes the pass.
- **AC2** — When `ROUTED_COMMIT_WAIVED` is blanked in the working copy and
  `env -u GATE_PUSH_BASE python tools/memory-tree/routed_commits.py` runs, the set of 8-character
  prefixes on its indented FAILED lines equals the set of the first 8 characters of each token in the
  committed value. `git checkout -- .memory-tree.conf` then restores the file and the leg exits 0 again.
  Red when: the two sets differ in either direction, meaning a violation is unwaived or a waiver
  hides nothing.
- **AC3** — When `grep -n -B10 '^ROUTED_COMMIT_WAIVED=' .memory-tree.conf` runs, the comment names
  the e6585db4 reconcile group and carries the derivation sentence, including the words
  `GATE_PUSH_BASE` and `re-derived`.
  Red when: the shas were added with no comment for their group, or the comment omits how the value
  is derived.
- **AC4** — When `python tools/memory-tree/gotchas.py --check` runs, it exits 0. When
  `python tools/memory-tree/gotchas.py --for-paths tools/memory-tree/routed_commits.py` runs, its
  checklist includes `history-leg-graded-before-the-reconcile-commit`.
  Red when: `INDEX.md` was not re-rendered, which `--check` reports as stale. It is also red when the
  record names no gate and does not say it has none (check 18), or when no backticked anchor selects
  it for the leg's path.
- **AC5** — When `python tools/codebase-map/gen_map.py --check` runs, it exits 0, and
  `grep -n 'history-leg-graded-before-the-reconcile-commit.md' memory/map/generated/MAP.md` prints a
  row naming `memory-tree-hygiene`.
  Red when: the key is claimed but the artifacts were not regenerated, which makes `--check` exit 1.
  It is also red when the key is unclaimed, so the MAP.md row is absent.
- **AC6** — When `bash skills/session-kickoff/manifest-check.sh` runs at the pass commit, it exits 0.
  Red when: `.memory-tree.conf` changed with no `last-audit` re-stamp and delta line, which the
  ratchet reports as an unaudited watch-touching commit.

## 6. Gates

`routed commits name a specced unit` · `memory hygiene` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms`

The pass verifies with AC1 to AC6 only. The listed legs run once, at the close, after the last unit
is terminal.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-10 · initial draft, from the spec brief
  `2026-10-10-prompt-TOOL-aRoutedQuill-9-spec-brief.md`.

## 9. Reuse audit

`tools/codebase-map/reuse_lookup.py "waive landed commits a history-wide leg reds on after a
reconcile merge"` returned only name-stem neighbours, such as `merge`, `legs` and `read_history_range`
in `tools/unattended/lib-unattended.sh`, and none of them waives a graded commit. No existing seam
fits beyond the one this unit edits in place, the `ROUTED_COMMIT_WAIVED` key that
`routed_commits.py` already reads in WHOLE mode. The recall probe returned round 1's B1 and round 2's
B1-r2 for this exact defect, and `TOOL-aSealedCaravan-1`, a line-keyed waiver that reds on a merge.
That one is a different keying fault and needs no action here. The catalogue's nearest class,
`observation-before-the-last-fold-of-the-same-commit.md`, was read whole. Its remedy selects by the
files a fold touched, which a reconcile does not touch, so S3 adds a sibling class rather than
amending it. §4 states the difference in the record's "What it is not" section.

Recall terms used: `python tools/memory-recall/query.py "how is a whole-history gate leg kept green
when a reconcile merge brings in commits graded before the waiver count" --terms "routed-commits
ROUTED_COMMIT_WAIVED WHOLE reconcile merge cutoff waiver stale history leg gotcha observation fold"`
