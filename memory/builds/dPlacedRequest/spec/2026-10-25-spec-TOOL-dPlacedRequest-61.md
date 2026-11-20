# TOOL-dPlacedRequest-61 — the round-6 promotions' minors: a two-way oracle inventory, one run-fact reader, a claim reader that keeps its normalisation, honest orders, and criteria that can fail

**Status:** CLOSED · rev-6 · 2026-11-20 · node a · Tier-2 · base c63aabbb · streams tooling · order 33 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-61-deviation-611.md](../build/2026-10-25-build-TOOL-dPlacedRequest-61-deviation-611.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-61-deviation-612.md](../build/2026-10-25-build-TOOL-dPlacedRequest-61-deviation-612.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-build-TOOL-dPlacedRequest-61-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dPlacedRequest-61-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-12-pass-red-fix-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-12-pass-red-fix-brief.md) | research | TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-63 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-59-orders-31-36-reground-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-59-orders-31-36-reground-brief.md) | research | TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-review-TOOL-dPlacedRequest-60-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-60-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-60 |
| [2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-63 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-6 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-57-spec-audit.md`)
exited CONVERGED with 21 confirmed findings. Its one high, finding 16, is unit 60. This unit is the
batch `doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it`
makes of the rest: 11 MEDIUM and 9 LOW findings by raw id, one scope item per id, each naming its
finding and, in brackets, the review item holding it (M1 to M7, L1 to L9). Two review items hold
more than one id (M1: 1, 9, 17 and 18; M2: 2 and 15). L3, finding 6, restates H1's defect, which
unit 60 closes at HIGH. It sits at order 33, after unit 59 at 31.

| Item | Finding | Severity | Lands on |
|---|---|---|---|
| S1 to S4 | 1, 9, 17, 18 (M1) | MEDIUM | units 54, 59 |
| S5, S6 | 2, 15 (M2) | MEDIUM | unit 59 |
| S7 | 3 (M3) | MEDIUM | units 56, 57, 58, 59 |
| S8 | 7 (M4) | MEDIUM | unit 57 |
| S9 | 10 (M5) | MEDIUM | units 48, 50, 56, 59 |
| S10 | 14 (M6) | MEDIUM | units 44, 57 |
| S11 | 20 (M7) | MEDIUM | unit 59 |
| S12 | 4 (L1) | LOW | unit 59 |
| S13 | 5 (L2) | LOW | units 44, 54, 59 |
| S14 | 6 (L3) | LOW | unit 57 |
| S15 | 8 (L4) | LOW | units 54, 59 |
| S16 | 11 (L5) | LOW | unit 59 |
| S17 | 12 (L6) | LOW | unit 59 |
| S18 | 13 (L7) | LOW | unit 57 |
| S19 | 21 (L8) | LOW | unit 57 |
| S20 | 22 (L9) | LOW | units 44, 59 |

Units 44, 48, 50, 54, 56, 57 and 58 are CLOSED, and the charter's P19 keeps built work out of
in-place rewrites; unit 59 is DEFERRED, and a builder writes no spec. Re-grounded on 2026-11-20
against the tree at `8a52e8e3b` by
`2026-11-20-prompt-TOOL-dPlacedRequest-59-orders-31-36-reground-brief`, each item is one of three
kinds. The scope ids are kept so the siblings that cite them still resolve, and criterion ACn
observes item Sn.

| Kind | Items |
|---|---|
| observes the text unit 59's rev-7 carries, the fold of this unit's order | S1, S3 to S6, S11 to S13, S15 to S17, S20 |
| observes a closed unit's text by a probe | S10, S18 |
| closed by a landed unit, or resolved in §4 as text a closed spec froze | S2, S7 to S9, S14, S19 |

Narrowed from rev-5: no item edits a spec, no order moves, and this unit builds nothing. The CR
strip, the loose trim and the split count land in unit 59's own function and criteria (F4, F5), the
inventory is unit 59's live sweep, and the oracle's head lives whole in unit 59's §4.

## 2. Scope (IN)

"Extracted" means read by unit 59 §4's readers: `bullet` for an S or AC bullet, joined to one line,
and `sec` for a `###` or `##` section, from the line after its heading to the next `##` or `###`
heading (unit 62's narrowing and 63's join, made in 59 at its rev-7). A `<unit>` operand names that
unit's spec.

- **S1** — finding 1 (M1). Made in 59's rev-7 (F4): spec 54 is CLOSED and carries no inventory, so
  59's S3 makes the inventory the live sweep of its §4, and its AC2 and AC21, which run the oracle in
  spec 55's fixture, each name the fixture's base. Left, its observation. Observed by AC1.
- **S2** — finding 9 (M1). Closed by 59's rev-7: no inventory table is written, so no row stands for
  a range, and the sweep prints each bullet whole. NOT OBSERVED here: spec text.
- **S3** — finding 17 (M1). Made in 59's AC3: the sweep's hits are compared with the empty set, the
  criterion reading nothing printed, and its red names a scratch copy that prints one bullet. Left,
  its observation. Observed by AC3.
- **S4** — finding 18 (M1). Made in 59's §4 sweep: it matches `oracle[^.]*(runs|run |prints|exits)`
  and runs the reverse direction in the same pass, each hit naming `RUN.md` or the fixture's base.
  Left, its observation. Observed by AC4.
- **S5** — finding 2 (M2), the skeptic's corrected fix. Made in 59's AC7: its count over the driver
  prints one line inside `CLAIM_KV_AWK`'s text, the pattern widened to the split 59's §4 writes.
  Left, its observation. Observed by AC5.
- **S6** — finding 15 (M2), the skeptic's corrected fix. Made in 59's AC7: a scratch copy of the
  driver whose walk adds `p = index(s, ": ")` makes the count print two lines. Left, its
  observation. Observed by AC6.
- **S7** — finding 3 (M3). Resolved in §4: units 56, 57 and 58 are CLOSED and their passes ran, so no
  order moves; this spec's F1, §5 risks line and last Alternatives bullet are restated from the
  driver, the folds of 63's S10 and 64's S1. NOT OBSERVED here: record text.
- **S8** — finding 7 (M4). Resolved in §4: spec 57 is CLOSED, and its Evidence names the subject
  test and the ancestor test each refusing the run's own base. NOT OBSERVED here: spec text.
- **S9** — finding 10 (M5). Resolved in §4: units 48 and 50 are CLOSED with their order-25 passes run,
  and spec 56 carries no AC5. NOT OBSERVED here: spec text.
- **S10** — finding 14 (M6). Satisfied by 57 rev-5: its S1 reads the base by the library's filter
  `tools/unattended/lib-unattended.sh#extract_run_facts`. Left, its observation. Observed by AC10.
- **S11** — finding 20 (M7). Made in 59's S7 and §4: `read_kv` strips a trailing CR itself and
  declares its locals. Left, its observation. Observed by AC11.
- **S12** — finding 4 (L1). Made in 59's sweep: the base alternation is
  `RUN\.md|fixture's( later)? base`, which no bare `base` substring matches. Left, its observation.
  Observed by AC12.
- **S13** — finding 5 (L2). Made in 59's rev-7: the oracle's head lives in 59 §4's block alone, and
  59's AC13 reads 54's and 52's frozen sections by `sec`. Left, its observation. Observed by AC13.
- **S14** — finding 6 (L3). Closed by 57 rev-5: its AC2 reads 54's AC1 by unit 60's bounded form,
  and 34's AC59 is frozen. NOT OBSERVED here: unit 60's AC1 observed it.
- **S15** — finding 8 (L4). Made in 59's S1: the merge found on the real tree was a foreign landing
  the subject test refused. Left, its observation. Observed by AC15.
- **S16** — finding 11 (L5). Made in 59's S7: the trim is loose mode's alone, which only the walk's
  keys reach, and strict mode keeps a trailing blank. Left, its observation. Observed by AC16.
- **S17** — finding 12 (L6). Made in 59's §1, which reads "Four review items". Observed by AC17.
- **S18** — finding 13 (L7). Satisfied by 57 rev-5, whose §5 claims no line count of the run-state
  file. Left, its observation. Observed by AC18.
- **S19** — finding 21 (L8). Resolved in §4: 57's Evidence cites
  `tools/unattended/unattended.sh#fact` and `extract_run_facts` by symbol and measured a CRLF file
  holding `base:<sha>` with no space. NOT OBSERVED here: spec text.
- **S20** — finding 22 (L9). Made in 59's §4 block: the short-circuits keep their own `if`, and the
  captured ancestor case runs only after them. Left, its observation. Observed by AC20.

## 3. Non-goals (OUT)

- No edit to any spec, and no code: the folds are made in 59's rev-7, and the closed specs are
  resolved in §4 (F3, F4).
- No second mechanism for the high: unit 60 owns finding 16.
- No order moves, and no sequencing in the run that builds this unit (F1).
- No new gate leg, no lint over spec criteria and no new bug-class record: the closing review's
  left-shift decides any (`doc.build-method#m8-closing-the-build`).

### Edges

- **consumes-from** `TOOL-dPlacedRequest-59` — S1, S3, S7, S21, §1, §4's readers, sweep, key reader and block, AC3, AC7 and AC13 as its rev-7 leaves them, the folds of this unit's items, which every criterion but AC10 and AC18 reads
- **consumes-from** `TOOL-dPlacedRequest-57` — S1, §4 Evidence and §5, frozen, which S8, S10, S18 and S19 observe or resolve
- **consumes-from** `TOOL-dPlacedRequest-60` — the bounded read, frozen in 57's AC2, which S14 records
- **consumes-from** `TOOL-dPlacedRequest-54` — §4 and its Evidence, frozen, which S1, S13 and S15 resolve through unit 59
- **consumes-from** `TOOL-dPlacedRequest-44` — AC1 and §4's oracle, frozen and superseded, which S10, S13 and S20 resolve through unit 59
- **consumes-from** `TOOL-dPlacedRequest-56` — the header order and the absence of AC5, frozen, which S7 and S9 resolve
- **consumes-from** `TOOL-dPlacedRequest-58` — the header order, frozen, which S7 resolves
- **consumes-from** `TOOL-dPlacedRequest-48` — the Files touched sequence sentence, frozen, which S9 resolves
- **consumes-from** `TOOL-dPlacedRequest-50` — the Files touched sequence sentence, frozen, which S9 resolves
- **hands-off** `TOOL-dPlacedRequest-62` — §2's "Extracted", which that unit's narrowing made in unit 59 and observes there
- **hands-off** `TOOL-dPlacedRequest-63` — §8 F1, §5 and the Alternatives, restated here from the driver as that unit's item for finding 14 ordered, which it observes
- **hands-off** `TOOL-dPlacedRequest-64` — §5's risks line and F1, which that unit's item for finding 1 observes

## 4. Design

### The folds into unit 59 (F4)

| This unit's items | Made in 59's rev-7 |
|---|---|
| S1, S3, S4, S12 | S3, §4's live sweep and AC3 |
| S5, S6 | AC7's split count and its scratch red |
| S11, S16 | S7 and §4's shared key reader |
| S13, S20 | S21, §4's one version oracle and AC13 |
| S15 | S1 and §4's closed-text paragraph |
| S17 | §1's count of review items |

Unit 59 is built before this one, at order 31, and `--dispatch` refuses this unit while 59 is
neither CLOSED nor WONTDO, so every criterion here reads text and code 59's pass has landed.

### The closed specs' text (S2, S7 to S9, S14, S19)

The closing mechanism is P19: a CLOSED spec is a frozen record, so its text stands as built, and the
fact each finding asked for stands here or in unit 59.

- S2: no inventory table exists; 59's sweep prints each bullet it grades.
- S7: units 56 and 57 shared order 29, 57 consuming from 56. The workflow sorts its roster by order,
  then by id (`tools/workflows/unattended-build.js#ordered`), and dispatches strictly in sequence,
  so 56 ran first; `--dispatch` refuses a consumer whose producer is neither CLOSED nor WONTDO, fail
  49 in `tools/unattended/unattended.sh#verb_dispatch`. Both are CLOSED, 58 with them, and their
  orders stand as built; unit 59 at 31 shares no step.
- S8: 57's Evidence records fact 1 returning the run's own base, subject
  `merge: dDeclaredLoop — land onto origin/main at c1f80c00`, which the subject test and the
  ancestor test each refuse.
- S9: the order-25 passes of 48 and 50 ran and closed; 56's S5 resolves the sentence, and 56 carries
  no AC5.
- S14: 57's AC2 reads 54's AC1 through the closers next bullet, heading or blank line.
- S19: 57's Evidence names `fact` and `extract_run_facts` by symbol and the CRLF no-space shape.

### Evidence

- `memory/builds/dPlacedRequest/RUN.md` held 133 lines on 2026-10-25, the figure finding 13 read.
- Measured 2026-11-20: `RUN.md` held 447 lines, PINNED at that date, and 57's §5 perf line reads
  "one filter over the run-state file, once at the close".
- `tools/unattended/lib-unattended.sh#extract_run_facts` scopes the `## Run facts` section by a
  fixed-prefix `index() == 1` test, and `tools/unattended/check-pass-order.sh` and
  `tools/unattended/check-brief-recorded.sh` read `base` through it. Read 2026-11-20.
- `tools/workflows/unattended-build.js#ordered` sorts by `order`, then by id, and the file's header
  says dispatch is strictly sequential within a shared order. Read 2026-11-20.
- `verb_dispatch`'s fail 49 message, `neither CLOSED nor WONTDO, so the consumer would build`, is
  asserted by the dispatch rows of `tools/unattended/unattended.test.sh`. Read 2026-11-20 at blob
  `9e03d5ed`.

### Files touched (estimate)

None: every item's text is made in unit 59's rev-7 or resolved here, and the code is unit 59's.

### Alternatives rejected

- **Renumber 56 to 30, 58 to 31 and 59 to 32 (rev-5's S7).** Units 56 and 58 are CLOSED, and moving
  59 alone moves it past no unit.
- **A gate refusing a shared order over intersecting write sets (finding 3's left-shift).**
  `--dispatch`'s fail 49 already refuses a consumer while its producer is open, at any order, and
  that refusal is the seam such a gate would extend; the closing review's left-shift decides more.
- **Build the CR strip and the trim at this pass (rev-5's S11 and S16).** Unit 59 builds the
  function whole, and a second pass over it is a copy of the same edit.
- **A trim in strict mode too (finding 11's first form).** It would let `status: live ` pass the
  strict reader's status test, which refuses it today.

## 5. Production-readiness checklist

- security — none: a read of spec text and of a closed unit's record.
- perf / scale — one `awk` per read, over one file.
- error / empty / loading states — a label or heading that names nothing prints nothing, which fails
  the clause that reads it.
- observability — each read prints the text it graded.
- risks — `--dispatch` refuses this unit with fail 49 while unit 59 is open, so a read of 59's text
  never runs ahead of its pass.
- testing — the probes of §6.
- migration — none: spec text.
- user docs — none: spec text.

## 6. Acceptance criteria

`bullet`, `sec` and `entries` are unit 59 §4's readers, a `<unit>` operand naming that unit's spec.

- **AC1** — When `sec 59 '### The live sweep'` is read, it holds
  `grep -L -E '^\*\*Status:\*\* (CLOSED|WONTDO)'`, and `bullet 59 AC2` and `bullet 59 AC21` each
  name `fixture's`.
  Red when: a criterion of the batch that walks history is left out of the sweep's population.
- **AC3** — When `bullet 59 AC3` is read, it names `prints nothing` and a scratch copy that prints
  one bullet.
  Red when: the sweep's result is compared with nothing.
- **AC4** — When `sec 59 '### The live sweep'` is read, it holds `oracle[^.]*(runs|run |prints|exits)`
  and `RUN\.md|fixture's( later)? base`.
  Red when: a criterion worded with prints is never swept, or a swept bullet is never asked its base.
- **AC5** — When `bullet 59 AC7` is read, it holds `index\([^,)]*, *(s|": "|":")\)` and
  `CLAIM_KV_AWK='`.
  Red when: the count admits a split under another variable name.
- **AC6** — When `bullet 59 AC7` is read, it names `p = index(s, ": ")` and `two lines`.
  Red when: a second split of the grammar is invisible to the count.
- **AC10** — When `bullet 57 S1` is read, it names `extract_run_facts`, and piped to
  `grep -c '/\^## Run facts/'` it prints 0.
  Red when: a criterion keeps its own reader of the Run facts grammar.
- **AC11** — When `sec 59 '### The shared key reader'` is read, it holds `sub(/\r$/, "", line)` and
  `loose,   s, p, k, x)`, and `bullet 59 S7` names `61's S11`.
  Red when: the shared reader keeps a CR the record read stripped.
- **AC12** — When `printf 'the merge-base\n'` is piped to `grep -cE "RUN\.md|fixture's( later)? base"`,
  it prints 0, and `sec 59 '### The live sweep'` holds that alternation.
  Red when: a substring of `merge-base` satisfies a base clause.
- **AC13** — When `bullet 59 AC13` is read, it names `### The oracle's head` and
  `neither CLOSED nor WONTDO`, and `bullet 59 S21` names `61's S13 and S20`.
  Red when: the head is stated in two specs.
- **AC15** — When `bullet 59 S1` is read, it names `subject test` and `61's S15`.
  Red when: the evidence names the wrong test as the one that refused.
- **AC16** — When `sec 59 '### The shared key reader'` is read, it holds
  `if (loose) { sub(/^[[:blank:]]+/`, and `sec 59 "### The suite's rows"` names `live |5`.
  Red when: a trim widens what the strict reader admits.
- **AC17** — When `grep -c 'Four review items'` runs over 59's spec, it prints 1, and
  `grep -c 'Five review items'` prints 0.
  Red when: a stated count disagrees with its list.
- **AC18** — When `grep -c 'under a hundred lines'` runs over 57's spec, it prints 0, and
  `sec 57 '## 5.'` names `one filter over the run-state file`.
  Red when: a size claim is false.
- **AC20** — When `sec 59 '### The one version oracle'` is read, the first line holding
  `[ "$own" = 0 ]` comes before the first holding `merge-base --is-ancestor`, and over a scratch copy
  of 59 with those two lines swapped the order inverts.
  Red when: the short-circuits are lost in a swap of the `if`.
  fixture: the scratch copy is made under the run's scratch directory.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

No new arm: every criterion is a read of spec text, and unit 59's arm carries the rows.

## 8. Open questions

- **F1 — How is finding 3 closed when this unit is built after units 56 and 57 (S7)?** (a) Renumber
  56 to 30, 58 to 31 and 59 to 32, the skeptic's corrected fix; (b) keep the orders, the roster
  sorted by order and then by id (`tools/workflows/unattended-build.js#ordered`), which reaches 56
  before 57, and `--dispatch` refusing a consumer with fail 49 while its producer is open; (c) a gate
  refusing a shared order over intersecting write sets, whose existing seam is that fail-49 refusal.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3. The index and any later plan read true.
  widens: none · relaxes: none. Overtaken at rev-6: units 56, 57 and 58 are CLOSED, 57 consuming from
  56 and built after it, so no order moves (F3), and (b) is the account of what ran.
- **F2 — Where does the value trim live (S16)?** (a) Inside the function, for the walk's keys only;
  (b) inside the function for every caller; (c) in each caller. (b) widens the strict reader. (c)
  is the second reader S7 of unit 59 takes away. RESOLVED (agent, 2026-10-25, delegated): (a), rung
  3. widens: none · relaxes: none. Made in 59's S7 as its loose mode (F4).
- **F3 — What becomes of an item that edits or re-orders a CLOSED spec?** (a) Resolved in §4 naming
  P19, the closed spec untouched; (b) the closed spec edited with a rev bump; (c) dropped unrecorded.
  (b) rewrites built work; (c) loses the fact. Recommendation: (a). RESOLVED (agent, 2026-11-20,
  delegated): (a), rung 3; P19 freezes units 44, 48, 50, 54, 56, 57 and 58, and §1's kinds table
  sorts each item by what the tree holds. widens: none · relaxes: none
- **F4 — Are this unit's amendments to spec 59 made at this pass or now?** (a) Now, once, in 59's
  rev-7, this unit reduced to observing that text; (b) at this unit's pass, by a builder. (b) has a
  builder write a spec, which no builder does. Recommendation: (a). RESOLVED (agent, 2026-11-20,
  delegated): (a), rung 3; spec 59 is DEFERRED, so each amendment is a spec act the re-grounding
  makes once, as the brief's fold rule names. widens: none · relaxes: none
- **F5 — Who builds the CR strip and the trim (S11, S16)?** (a) Unit 59, inside the function it
  builds; (b) this unit, at its pass over 59's function. (b) is a second edit of code built whole a
  pass earlier. Recommendation: (a). RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; the
  amendment is to 59's design, so it lands where 59 builds. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, the batch of the spec audit of the round-6 promotions' 11
  MEDIUM and 9 LOW findings.
- rev-2 · 2026-10-25 · §3 · the disposal of the spec audit of the round-7 promotions: the hands-off edges to `TOOL-dPlacedRequest-62` and `TOOL-dPlacedRequest-63`, mirroring their consumes-from.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-8 promotions: the hands-off edge to `TOOL-dPlacedRequest-64`, mirroring its consumes-from.
- rev-4 · 2026-11-19 · §3 · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit`: finding 2 (H1), the claim that unit 34 sits
  under 48128 is re-pinned on the disposal's dated measurement, 47885 bytes at its rev-12, PINNED 2026-11-19 (a figure
  rev-5 corrected). §7 also
  names `scratch-guard self-test` and `tier2-review self-test`, the legs the spec-token guard join names
  for `tools/unattended/unattended.sh` in Files touched.
- rev-5 · 2026-11-19 · §3 · §4 Files touched · §7 · §9 rev-4 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: findings 1, 6 and 13 (M1), unit 34 measured
  47885 bytes at rev-12, PINNED 2026-11-19, 243 under 48128; finding 17 (M8), this unit's own pass regenerates
  `memory/map/generated/`, named in Files touched, and §7 names its leg.
- rev-6 · 2026-11-20 · §1 · §2 S1 to S20 · §3 · §4 · §5 · §6 AC1 to AC20 · §7 · §8 F1 to F5 · §10 ·
  re-grounded by `2026-11-20-prompt-TOOL-dPlacedRequest-59-orders-31-36-reground-brief`: the items
  landing on spec 59 made in its rev-7 (F4, F5), so each reduces to observing that text; the closed
  specs' items resolved in §4 (F3), no order moving; the narrowing `TOOL-dPlacedRequest-62` ordered
  to AC13 and AC20 made in §2's "Extracted" and in 59's AC13, and 63's restatement of F1, §5 and the
  Alternatives from the driver made here; Files touched now none, and §7 loses the legs its code
  owed; line citations swapped for symbol citations and a blob pin, and the build method's section
  for its alias tag.

## 10. Reuse audit

The seams extended: unit 59 §4's readers `bullet` and `sec` for every read of a sibling's text;
`tools/unattended/lib-unattended.sh#extract_run_facts` for S10's observation; and `--dispatch`'s
fail-49 refusal in `tools/unattended/unattended.sh#verb_dispatch` for S7's account. The brief's
named seam, the governance-ref factory `tools/unattended/unattended.sh#write_gov_ref`, writes refs,
and this unit writes none. `python tools/codebase-map/reuse_lookup.py "read a labelled criterion
bullet or a markdown section of a sibling spec"`, run 2026-11-20, ranked `read_text`, `read`,
`read_bytes` and `read_git`, name stems only, none a spec-section reader: no existing seam fits
beyond unit 59's readers. `python tools/memory-recall/query.py "re-ground a deferred minors batch
whose amendments to sibling specs fold into one spec and whose target specs are closed"` with the
terms below returned the minors batches of dKeptSession and aDistilledCharter and unit 56's
re-grounding; none disagrees with source.

Recall terms used: re-ground deferred minors batch fold closed spec P19 frozen observe extract_run_facts verb_dispatch fail 49
