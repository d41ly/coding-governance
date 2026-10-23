# TOOL-dGroundRules-55 — the criterion bug class gains the side read: a criterion observes its scope item by running the check, never by reading what the check reads

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-55-deviation-43.md](../build/2026-10-23-build-TOOL-dGroundRules-55-deviation-43.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-53-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-task.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-56 TOOL-dGroundRules-57 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of the spec run, round 1
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`),
confirmed finding **id 12 at HIGH** under item **H1**, which it shares with ids 5, 9, 14 and 19.
Id 12 is H1 seen from verification. Its literal defect, `TRAP_SH` printing `127` where
`TOOL-dGroundRules-44` AC2 expects `1`, is the one `TOOL-dGroundRules-53` repairs for ids 5 and 12
together. What verification owes beyond the literal is the item's checklist half, which the
review's left-shift gate names: "criterion reads the fixture, never runs the check". Unit 44's AC3
read the arm's table in Python and never ran the row check it was written to observe, and the class
record `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`, which
`gotchas.py --for-diff` hands to every spec commit, names no such form. This unit is id 12's
promotion as that checklist half, as the round before gave its own item's id 1 to
`TOOL-dGroundRules-47`: the record gains the side-read form, where it bit and its fix. It repairs
`TOOL-dGroundRules-44`, which sits at order 14, so it builds at order 17.

## 2. Scope (IN)

- **S1** — The symptom. The record's Symptom list gains a form headed
  `It reads what the check reads, and never runs the check.`: a criterion that names a scope item
  observes it through a side probe of the table, fixture or file the check grades, so the item is
  certified while the check's own code never runs, and a respelled input leaves the side probe
  reading nothing. The sentence that introduces the list counts its forms, and its count word rises
  by one. Observed by AC1.
- **S2** — Where it bit. A paragraph names this review's H1: `TOOL-dGroundRules-44` AC3 read
  `OVERLAP_PAIRS` in Python to certify the row check of its S2, and its respelled `NOT_A_TRAP`
  staging left that read printing nothing. It names `TOOL-dGroundRules-56` and
  `TOOL-dGroundRules-57` as the repair. Observed by AC1.
- **S3** — The fix. "The fix" gains: a criterion that names a scope item runs the shipped check on
  a staged break, whether the checker on a fixture, a suite function run alone or a `--selftest`
  flag, and names the suite on a `New arm:` line; a side read of the check's input never runs the
  check, so it may sit beside that observation and never stands in for it. Observed by AC1.
- **S4** — The index stays current. This unit leaves the record's front-matter `description` as it
  finds it, so `memory/gotchas/INDEX.md` needs no new row text. Observed by AC2.

## 3. Non-goals (OUT)

- A gate. Whether a criterion's probe runs the check or only reads its input needs the criterion's
  intent, which the record's own "Its gate" section says no text join reaches.
- The review's other left-shift, a join that every path operand in a §6 fenced literal resolves or
  is declared created (§4 Alternatives rejected, where its measurement is recorded).
- A new class record. The side read is a form of the class this record already holds.
- The literal repairs: `TOOL-dGroundRules-53`, `TOOL-dGroundRules-56` and `TOOL-dGroundRules-57`.

### Edges

- **consumes-from** `TOOL-dGroundRules-44` — AC3 and its `NOT_A_TRAP` staging, the instance S2 records; without it the form has no measured case
- **consumes-from** `TOOL-dGroundRules-42` — the record's respelled-input form and its fenced-literal fix, which S1 and S3 sit beside
- **consumes-from** `TOOL-dGroundRules-47` — the record's verbatim re-run rule, which S3's fix follows in "The fix"

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `7810198ad`.

- The record's Symptom list holds four forms, introduced by "Four ways, and a spec set usually has
  more than one". `TOOL-dGroundRules-42` S1 adds a fifth, the input respelled to pass a join, and
  changes the front-matter `description` for it; `TOOL-dGroundRules-47` adds the re-run to "The
  fix". Neither names a criterion that reads the check's input instead of running the check.
- The record's "Its gate" section says deciding whether a criterion can fail needs the criterion's
  intent, so no text join reaches its forms.
- `TOOL-dGroundRules-44` AC3 runs `TRAP_PROBE`, a Python read of the suite's table, and S2 names
  AC3 as its only observation (review id 14).
- `python tools/memory-tree/gotchas.py --check` exited 0.

### The paragraphs

S1, S2 and S3 each add one paragraph or bullet to the record, in its Symptom, "Where it bit" and
"The fix" sections. No anchor changes, so the selection `gotchas.py --for-diff` makes, which
`TOOL-dGroundRules-42` AC1 observes, is unchanged. The count word S1 raises is whatever the list's
introducing sentence holds when this unit builds, after `TOOL-dGroundRules-42`.

### Files touched (estimate)

- `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`

### Alternatives rejected

- **The review's spec-tokens arm: every path operand in a §6 fenced literal resolves against the
  tree or is declared created by a named unit.** Measured on 2026-10-23 over every live spec's §6
  fenced blocks, before this disposal's specs: 59 path-shaped operands carrying a `/`, 38 of them
  unresolved, in 12 specs (PINNED, scratch script). Every one is a scratch-repository path, a
  fixture string, a file a unit creates, or a fragment of a glob or a regex. None is one of H1's
  stripped literals, which are bare names carrying no `/` at all. The arm would red 38 legitimate
  operands and catch none of the class. `TOOL-dGroundRules-46` already gates the bare-name source.
- **A new record.** The record's class is a criterion whose command cannot answer it; a side read
  that never runs the check is that class.

## 5. Production-readiness checklist

- security — N/A: a memory record.
- perf / scale — N/A: prose.
- error / empty / loading states — N/A: no code path.
- observability — `gotchas.py --for-diff` hands the record to every spec commit.
- risks — none beyond the record's wording.
- testing — AC1 and AC2.
- migration — none; the generated index row is unchanged.
- user docs — N/A: a gov-internal record.

## 6. Acceptance criteria

Every command runs from the repository root.

- **AC1** — When
  `grep -c "never runs the check" memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
  runs, it prints `2` or more, and
  `grep -c "TOOL-dGroundRules-44" memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
  prints `1` or more.
  Red when: the record names neither the side-read form nor its fix, or names the form without the
  instance it was measured on.
  figure: PINNED, the symptom head and the fix each carry the phrase once.
- **AC2** — When `python tools/memory-tree/gotchas.py --check` runs, it exits 0.
  Red when: the record's edit leaves the generated index stale.

## 7. Gates

`gotchas selftest` · `memory hygiene` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 12 (HIGH, item H1) of the closing diff
  review round 1 as the item's checklist half, its literal carried by `TOOL-dGroundRules-53`, with
  the record and the review's candidate arm measured on 2026-10-23.

## 10. Reuse audit

The seam extended is the record `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`,
which `TOOL-dGroundRules-42` and `TOOL-dGroundRules-47` widen before this unit; no new record is
written. `python tools/codebase-map/reuse_lookup.py "run one suite function alone on a staged row to
observe its refusal line"` ranks code seams and none of record shape, so the record was found by
listing `memory/gotchas/`. The recall probe returned `TOOL-dGroundRules-42` and
`TOOL-dGroundRules-47`, both widening this record; both agree with widening it again rather than
minting one.

Recall terms used: `python tools/memory-recall/query.py "how is a criterion that reads a fixture
instead of running the check repaired" --terms "acceptance criterion fixture side read never runs
check stripped literal respelled trap row overlap arm suite function"`
