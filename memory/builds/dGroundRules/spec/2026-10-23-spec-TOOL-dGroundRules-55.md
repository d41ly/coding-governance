# TOOL-dGroundRules-55 — the criterion bug class gains the side read: a criterion observes its scope item by running the check, never by reading what the check reads

**Status:** CLOSED · rev-2 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 17 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-55-deviation-43.md](../build/2026-10-23-build-TOOL-dGroundRules-55-deviation-43.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-55-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-55-ledger.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-53-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-task.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-56 TOOL-dGroundRules-57 |
| [2026-10-23-prompt-TOOL-dGroundRules-55-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-55-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-55-1-spec-reviewer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-55-1-spec-reviewer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-55-2-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-55-2-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-55-probe-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-55-probe-fix-brief.md) | research | — |
| [2026-10-24-prompt-TOOL-dGroundRules-55-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-55-staleness-probe-brief.md) | research | TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-64 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of the spec run, round 1
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`),
confirmed finding **id 12 at HIGH** under item **H1**, which it shares with ids 5, 9, 14 and 19.
Id 12 is H1 seen from verification. Its literal defect, `TRAP_SH` sourcing the library by a bare
file name and printing `127` where `TOOL-dGroundRules-44` AC2 expects `1`, is repaired in
`TOOL-dGroundRules-44`'s own text: from rev-4 its `TRAP_SH` sources
`tools/unattended/lib-unattended.sh` and prints `1` (§4 Evidence). What verification owes beyond
the literal is the item's checklist half, which the review's left-shift gate names: "criterion
reads the fixture, never runs the check". Unit 44's AC3 read the arm's table in Python and never ran
the row check it was written to observe, and the class record
`memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` names no such form.

The record reaches a spec commit through `gotchas.py --for-diff` only because
`TOOL-dGroundRules-42` S4 gave it the `memory/builds/` anchor. That unit sits at order 13, before
this one, and is built (§4 Evidence); before it the record's anchors were two kit paths, and a
commit touching only specs did not select it. This unit is id 12's promotion as that checklist half,
as the round before gave its own item's id 1 to `TOOL-dGroundRules-47`: the record gains the
side-read form, where it bit and its fix. It repairs `TOOL-dGroundRules-44`, which sits at order 14,
so it builds at order 17.

## 2. Scope (IN)

- **S1** — The symptom. The record's Symptom list gains a form headed
  `It reads what the check reads, and never runs the check.`: a criterion that names a scope item
  observes it through a side probe of the table, fixture or file the check grades, so the item is
  certified while the check's own code never runs. A side probe that misreads the input's spelling
  prints nothing, and the criterion still reads as an observation. The sentence that introduces the
  list counts its forms, and its count word rises by one. Observed by AC1.
- **S2** — Where it bit. A paragraph in "Where it bit" names this review's H1:
  `TOOL-dGroundRules-44` AC3 read `OVERLAP_PAIRS` in Python, through `TRAP_PROBE`, to certify the
  row check of its S2, and never ran the check. It records why that read printed nothing on the
  built tree, in the words `closing quote`: the table is one single-quoted shell string, so its
  last line ends in the word `disjoint` with the string's closing quote attached, and a probe that
  blanked no single quote matched no row. The respelled staging was not the cause. It names `TOOL-dGroundRules-44`'s revised
  `TRAP_PROBE`, which blanks the single quote and lists the row, and says a probe that lists the row
  still never runs the check; `TOOL-dGroundRules-56`, which runs the row check itself, is the
  repair. Observed by AC1.
- **S3** — The fix. "The fix" gains: a criterion that names a scope item runs the shipped check on
  a staged break, whether the checker on a fixture, a suite function run alone or a `--selftest`
  flag, and names the suite on a `New arm:` line; a side read of the check's input never runs the
  check, so it may sit beside that observation and never stands in for it. Observed by AC1.
- **S4** — The index row holds. No paragraph S1 to S3 adds changes the record's front-matter
  `description` or backticks a path-like token, so the record's derived anchors, the selection
  `gotchas.py --for-diff` makes and its row in `memory/gotchas/INDEX.md` stay as
  `TOOL-dGroundRules-42` left them. Observed by AC2.

## 3. Non-goals (OUT)

- A gate. Whether a criterion's probe runs the check or only reads its input needs the criterion's
  intent, which the record's own "Its gate" section says no text join reaches.
- The review's other left-shift, a join that every path operand in a §6 fenced literal resolves or
  is declared created (§4 Alternatives rejected, where its measurement is recorded).
- A new class record. The side read is a form of the class this record already holds.
- The literal repairs: `TOOL-dGroundRules-44`'s own `TRAP_SH` and `TRAP_PROBE`, and
  `TOOL-dGroundRules-56`'s run of the row check.

### Edges

- **consumes-from** `TOOL-dGroundRules-44` — AC3, its `TRAP_PROBE` and the quote that left it reading nothing, the instance S2 records; without it the form has no measured case
- **consumes-from** `TOOL-dGroundRules-42` — the record's respelled-input form and its fenced-literal fix, which S1 and S3 sit beside, and its S4 `memory/builds/` anchor, through which `gotchas.py --for-diff` hands the record to a spec commit
- **consumes-from** `TOOL-dGroundRules-47` — the record's verbatim re-run rule, which S3's fix follows in "The fix"

## 4. Design

### Evidence

Every line below was read or run on 2026-10-24 at 8fa309e89, from the repository root.

- The record's Symptom list holds five forms, introduced by "Five ways, and a spec set usually has
  more than one". `TOOL-dGroundRules-42`, built at 8fa309e89, added the fifth, the input respelled
  to pass a join; `TOOL-dGroundRules-47`, at order 14, adds the re-run to "The fix" and no form.
  None names a criterion that reads the check's input instead of running the check.
- The record's derived anchors at 8eab342e0, by `ANCHOR_RE` of `tools/memory-tree/gotchas.py`, were
  `tools/check-spec-tokens.py` and `tools/check-testsuite-counts.sh` only, so `selectable` gave a
  spec path neither. At 8fa309e89 they are three, `memory/builds/` among them:
  `python tools/memory-tree/gotchas.py --for-diff a2aaa9ab2~1..a2aaa9ab2`, a commit touching only
  specs, names the record, and its `memory/gotchas/INDEX.md` row's Anchors cell reads `3`.
- The record's "Its gate" section says deciding whether a criterion can fail needs the criterion's
  intent, so no text join reaches its forms.
- `TOOL-dGroundRules-44` AC3 runs `TRAP_PROBE`, a Python read of the suite's table, and its S2 names
  AC3 as its only observation (review id 14). Its rev-4 `TRAP_SH` sources
  `tools/unattended/lib-unattended.sh`, and run from the root it printed `1`.
- `OVERLAP_PAIRS` sits in the arm headed by the comment naming `TOOL-dGroundRules-32` S9 and
  `TOOL-dGroundRules-40` in `tools/check-spec-tokens.test.sh`: one single-quoted string of two rows,
  the `disjoint` row last, so that line's last word carries the closing quote. The rev-4
  `TRAP_PROBE`, which blanks double quotes and parentheses only, printed nothing; the same probe
  with the single quote blanked too printed the trap row, its raw prefix answer `True` and its
  containment answer `False`.
- `python tools/memory-tree/gotchas.py --check` exited 0.

### The paragraphs

S1, S2 and S3 each add one paragraph or bullet to the record, in its Symptom, "Where it bit" and
"The fix" sections. None backticks a path-like token, so the anchors `TOOL-dGroundRules-42` set,
and the selection `gotchas.py --for-diff` makes from them, are unchanged. The count word S1 raises
is whatever the list's introducing sentence holds when this unit builds, `Five` at 8fa309e89.

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
- observability — `gotchas.py --for-diff` hands the record to every spec commit, through the
  `memory/builds/` anchor `TOOL-dGroundRules-42` S4 built.
- risks — none beyond the record's wording.
- testing — AC1 and AC2.
- migration — none; the generated index row is unchanged.
- user docs — N/A: a gov-internal record.

## 6. Acceptance criteria

Every command runs from the repository root.

- **AC1** — When
  `grep -c "never runs the check" memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
  runs, it prints `2` or more;
  `grep -c "TOOL-dGroundRules-44" memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
  prints `1` or more; and
  `grep -c "closing quote" memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
  prints `1` or more. At 8fa309e89 each prints `0`, so this is red before this unit.
  Red when: the record names neither the side-read form nor its fix, names the form without the
  instance it was measured on, or names the instance without the quote that emptied its read.
  figure: PINNED, the symptom head and the fix each carry the first phrase once.
- **AC2** — When `python tools/memory-tree/gotchas.py --check` runs, it exits 0, and
  `grep -c "| class | 3 |  | an acceptance criterion names" memory/gotchas/INDEX.md` prints `1`.
  Both hold at 8fa309e89, after `TOOL-dGroundRules-42`, so this is green before this unit. The
  staged break that reds it is a new paragraph that backticks a path-like token, which raises the
  record's derived anchors to four: left unregenerated, `--check` exits non-zero naming check 17's
  stale index, and regenerated with `--write`, the grep prints `0`.
  Red when: a paragraph this unit adds moves the record's anchors or its description, so the
  selection `gotchas.py --for-diff` makes and the index row move with it.
  figure: PINNED, the Anchors cell `3` read at 8fa309e89.

## 7. Gates

`gotchas selftest` · `memory hygiene` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 12 (HIGH, item H1) of the closing diff
  review round 1 as the item's checklist half, its literal carried by `TOOL-dGroundRules-53`, with
  the record and the review's candidate arm measured on 2026-10-23.
- rev-2 · 2026-10-24 · §1 S1 S2 S4 §3 §4 §5 AC1 AC2 §9 · disagreements, from a read-only probe of
  steps 15 to 20 at e1c7051cb, restated at 8fa309e89: §1 and §3 had `TOOL-dGroundRules-53` repair
  `TRAP_SH`, and S2 and §3 had `TOOL-dGroundRules-57` repair the staging, both since closed WONTDO,
  while `TOOL-dGroundRules-44` rev-4's own `TRAP_SH` sources `tools/unattended/lib-unattended.sh`
  and prints `1`; S1 and S2 blamed the respelled `NOT_A_TRAP` staging for the empty read, where at
  HEAD the cause is the table's last word carrying the string's closing quote; §1 and §5 said
  `gotchas.py --for-diff` already handed the record to every spec commit, where its anchors at
  8eab342e0 were two kit paths; §4 Evidence read the tree at 7810198ad; AC2 did not say it was green
  before this unit. Ruled: §1 names `TOOL-dGroundRules-44`'s own text as the literal repair and no
  closed unit; S2 records the quote as the cause and `TOOL-dGroundRules-44`'s revised `TRAP_PROBE`
  as stripping it, with `TOOL-dGroundRules-56` the repair that runs the check; §1, §3 Edges, §4 and
  §5 say the record reaches a spec commit only through `TOOL-dGroundRules-42`'s `memory/builds/`
  anchor, at order 13 before this unit and built at 8fa309e89 since the ruling. The ruling named
  that unit's S2; its spec places the anchor in S4, so S4 is cited. S4 and AC2 hold the Anchors
  cell, AC1 gains the quote clause and states it is red before this unit, AC2 is restated green
  before this unit with its staged break, and Evidence is re-read at 8fa309e89, every citation by
  symbol or AC id. No criterion consumes a literal of a closed unit.

## 10. Reuse audit

The seam extended is the record `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`,
which `TOOL-dGroundRules-42` widened and `TOOL-dGroundRules-47` widens before this unit; no new
record is written. `python tools/codebase-map/reuse_lookup.py "run one suite function alone on a
staged row to observe its refusal line"` ranks code seams and none of record shape, so the record
was found by listing `memory/gotchas/`. The recall probe returned `TOOL-dGroundRules-42` and
`TOOL-dGroundRules-47`, both widening this record; both agree with widening it again rather than
minting one.

Recall terms used: `python tools/memory-recall/query.py "how is a criterion that reads a fixture
instead of running the check repaired" --terms "acceptance criterion fixture side read never runs
check stripped literal respelled trap row overlap arm suite function"`
