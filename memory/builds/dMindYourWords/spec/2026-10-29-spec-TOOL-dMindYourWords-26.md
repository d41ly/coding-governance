# TOOL-dMindYourWords-26 — a `widened:<record>` ledger row is admitted only when the branch adds its record

**Status:** OPEN · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 6

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 |
| [2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-24 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-25 TOOL-dMindYourWords-29 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 44 of `reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md`, HIGH, item
H4. TOOL-dMindYourWords-11 S8 has `check_debt_pin` green a `gained` or `raised` row whose disposition is
`widened:<record>` under `lexicon.pin = shrink-only` whenever `<record>` is a tracked vocabulary
record, and TOOL-dMindYourWords-1's `absorb` arm greens one whenever `<record>` is a tracked path. Only
the commit hook asks that the record be new, so a branch committed with the hook bypassed, in a clone
with no `core.hooksPath`, or arriving through CI, adds debt rows citing any old record and passes the
merge bar. This unit makes the bar ask what the hook asks: the branch added the record.

## 2. Scope (IN)

- **S1** — The added set. `read_branch_added_paths(root, base)` in `tools/lexicon/lexicon.py` returns the
  repo-relative paths `git diff -M --diff-filter=A --name-only -z <base> HEAD` lists, `base` the compare
  base `check_debt_pin` already resolves for its base half (`resolve_compare_base`, carried by the kit's
  `tools/lexicon/coverage_join.py`). One spawn per run, computed only when a widened row is judged. A
  record the branch renamed is not added, so an old record moved under a new name admits nothing.
  Observed by AC1 and AC3.
- **S2** — The `shrink-only` admission. A `gained` or `raised` row whose disposition is
  `widened:<record>` greens only when `<record>` is in S1's set AND is a vocabulary record by
  `read_vocabulary_record`'s predicate on that one path (TOOL-dMindYourWords-11 S1); otherwise it reds
  naming the row and why, `record not added by this branch` or `not a vocabulary record`. Observed by
  AC1 and AC2.
- **S3** — The `absorb` admission. A `gained` or `raised` row whose disposition is `widened:<record>`
  greens only when `<record>` is in S1's set; otherwise it reds naming the row and `record not added by
  this branch`. Observed by AC3.
- **S4** — No base, no admission to judge. With no resolvable base the base half is not computed
  (TOOL-dMindYourWords-1 §4 "The verdict table", "no ledger at the base"), so no `gained` row exists and
  S1 is never asked. Observed by AC4.
- **S5** — The docs. The debt-ledger section of `tools/lexicon/README.md` states that a widened row is
  admitted at the bar only for a record its branch adds; `KIT_LEXICON_VERSION` moves once. NOT OBSERVED
  as behaviour: prose has no grader beyond the carriers' own legs.

## 3. Non-goals (OUT)

- The commit hook's own check, which already asks for a record the index adds (TOOL-dMindYourWords-11
  S3 and S4).
- Comparing a record's `Before` and `After` with the change it admits: review id 52, the minors batch
  TOOL-dMindYourWords-29.
- The bug-class checklist entry the report names as H4's left-shift gate: a gate is its own unit
  (BUILD-METHOD M2), and no clause of this build names it.

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — `check_debt_pin`'s base half, its compare base and its `absorb` arm; without it there is no admission to narrow
- **consumes-from** `TOOL-dMindYourWords-11` — S8's `shrink-only` admission of a `widened:<record>` row and `read_vocabulary_record`'s predicate on one path
- **hands-off** `TOOL-dMindYourWords-29` — the narrowed admission, against which the batch re-observes unit 1's AC3 with a non-vocabulary record the branch adds (id 11)
- **hands-off** `TOOL-dMindYourWords-37` — `read_branch_added_paths` and its fixture, which the minors batch walks by first parent, parses with the shared `-z` reader and fixtures with a remote and a cleared environment (review ids 9, 14, 19 and 33)

## 4. Design

### Evidence

- Unit 11 S8: "a `gained` or `raised` row whose disposition is `widened:<record>` greens under
  `lexicon.pin` `shrink-only` when `<record>` is a tracked vocabulary record (S1's predicate on that one
  path)" (`spec/2026-10-29-spec-TOOL-dMindYourWords-11.md` S8). Unit 1's table: under `absorb`, "green
  when `<record>` is a tracked path, else red" (`spec/2026-10-29-spec-TOOL-dMindYourWords-1.md` §4).
- Unit 11 S3 requires, at commit, "a record of that tag the index adds", and its non-goals rely on the
  bar to see a bypassed commit's effect (`spec/2026-10-29-spec-TOOL-dMindYourWords-11.md` §3).
- Unit 5 rejects the same pointer design for suppressions, because it "proves a record exists, never
  that the row's own change carried one" (`spec/2026-10-29-spec-TOOL-dMindYourWords-5.md:170-172`, as the
  report quotes it).
- The compare base is the one the factory's base half already reads, carried inline as
  `tools/lexicon/coverage_join.py` (unit 1 S3), so the added set and the `gained` finding are computed
  over one base.

### The admission

| `lexicon.pin` | `widened:<record>`, record added by the branch | added, not a vocabulary record | not added |
|---|---|---|---|
| `shrink-only` | green when a vocabulary record | red, `not a vocabulary record` | red, `record not added by this branch` |
| `absorb` | green | green | red, `record not added by this branch` |
| `no-gate` | printed | printed | printed |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_branch_added_paths` | function, `tools/lexicon/lexicon.py` | `py.function`; `lexicon.py --suggest read_branch_added_paths --as py.function` answered `OK` at writing |
| `record not added by this branch`, `not a vocabulary record` | refusal reasons | none |

### Migration

None in gov at this order: no widened row exists before TOOL-dMindYourWords-11's first re-baseline,
which lands its record in the same branch.

### Rollout

Live at landing, one order after TOOL-dMindYourWords-11, so no landed tree admits a widened row by an
old record.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1 to S4, `KIT_LEXICON_VERSION`
- `tools/lexicon/selftest.py`: the arm of §7
- `tools/lexicon/README.md`: S5

### Alternatives rejected

- **The record's adding commit read from blame of the ledger row**: blame names the commit that last
  wrote the row, not the one that carried the record, and needs a full history; the base diff answers
  the question asked, "did this branch add it".
- **Requiring the record and the row in one commit**: a branch may write its record and re-baseline in
  two commits, and the merge bar grades the branch, not each commit.

## 5. Production-readiness checklist

- security — deny by default: a widened row is red unless its record is shown added; a renamed old record
  admits nothing.
- perf / scale — one `git diff` spawn per run, only when a widened row is judged.
- error / empty / loading states — no base: no `gained` row, nothing to admit (S4); a failed `git diff`
  reds `cannot judge widened rows — <why>`, never an admission.
- observability — each refused row prints its key and the reason.
- risks — a squash merge carries the record in the same commit as the row, so the base diff still lists it.
- testing — AC1 to AC4 and the arm of §7.
- migration — none.
- user docs — `tools/lexicon/README.md` (S5).

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py` runs in a fixture repository with no `core.hooksPath`,
  whose branch adds an offender and its ledger row `widened:<record>` naming a vocabulary record already
  on the base, it exits 1 naming the row and `record not added by this branch`.
  Red when: an old vocabulary record admits the row, the bypass the finding names.
  fixture: a scratch repository under `%TEMP%` with a base commit on its default branch.
- **AC2** — When the same branch instead adds a new vocabulary record and cites it, the run exits 0; when
  it adds and cites a new file that is not a vocabulary record, it exits 1 naming `not a vocabulary
  record`.
  Red when: a record the branch adds is refused, or any added file admits under `shrink-only`.
- **AC3** — When the fixture commits `.governance/policy.toml` setting `lexicon.pin = "absorb"`, a row
  citing a path already on the base exits 1 naming `record not added by this branch`, and one citing a
  path the branch adds exits 0; a base record the branch renames with `git mv` and cites still exits 1.
  Red when: `absorb` admits by a tracked old path, or by a renamed one.
- **AC4** — When the fixture has no resolvable base, the run prints the base half as unresolved and makes
  no `git diff` call for the added set.
  Red when: the admission is judged against a guessed base.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest` · `kit version markers`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC4 · a fixture with a base commit holding a vocabulary record, its failing case the added-set test cut out of the admission, under which AC1's row citing the base record greens · none

## 8. Open questions

- **F1 — What proves a widened row's record belongs to its change, at the bar?** Options: (a) the record
  is in the set of paths the branch adds over the compare base, rename-aware; (b) the record is newer
  than the row's commit by blame; (c) the record and the row share one commit. (b) needs a full history
  and answers a different question; (c) refuses a branch that writes them in two commits. RESOLVED
  (agent, 2026-10-29, delegated): (a), rung 3, the report's fix and the most capable survivor.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 44 (HIGH, item H4) of the round-1 spec
  audit.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 22 to 29
  declare toward this unit (TOOL-dMindYourWords-37); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are TOOL-dMindYourWords-1's `check_debt_pin`, whose base half already resolves the
compare base through the kit's `coverage_join` copy of `resolve_compare_base`
(`tools/lib/compare_base.py:15-50`), and TOOL-dMindYourWords-11 S1's `read_vocabulary_record`
predicate. `python tools/codebase-map/reuse_lookup.py "keep the rows another producer owns when
rewriting a shared ledger file"` ranked no admission or added-path helper, and `git grep -n
'diff-filter=A' -- tools` is the evidence that the added-path read is a one-line `git diff` each caller
spells for its own population; no existing seam fits the added set itself.

Recall terms used: `python tools/memory-recall/query.py "how does the lexicon debt ledger keep its rows when tag findings and corpus findings share one population" --terms "lexicon-debt ledger drain measure rebaseline tags slice check_debt_pin widened shallow provenance"`
