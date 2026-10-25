# TOOL-dGroundRules-47 — the criterion bug class's fix gains the re-run: a literal is run verbatim from the root before its spec commits, and a restated one is re-run, never copied

**Status:** CLOSED · rev-2 · 2026-10-24 · node d · Tier-1 · base 3708a705 · streams tooling · order 14 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-47-deviation-35.md](../build/2026-10-23-build-TOOL-dGroundRules-47-deviation-35.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-47-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-47-ledger.md) | journal | — |
| [2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md](../build/2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md) | journal | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 TOOL-dGroundRules-72 TOOL-dGroundRules-73 TOOL-dGroundRules-74 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 TOOL-dGroundRules-80 TOOL-dGroundRules-81 TOOL-dGroundRules-82 TOOL-dGroundRules-83 TOOL-dGroundRules-84 TOOL-dGroundRules-85 TOOL-dGroundRules-86 |
| [2026-10-23-prompt-TOOL-dGroundRules-47-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-47-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-47-1-spec-reviewer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-47-1-spec-reviewer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-47-2-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-47-2-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-47-probe-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-47-probe-fix-brief.md) | research | — |
| [2026-10-24-prompt-TOOL-dGroundRules-47-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-47-staleness-probe-brief.md) | research | TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md](../reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 35 to 43
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md`)
exited BOUNDED with finding **id 1 at HIGH**, which shares item **H1** with ids 10
(`TOOL-dGroundRules-46`) and 20 (`TOOL-dGroundRules-45`). Id 1 is H1 seen from coherence:
`TOOL-dGroundRules-40` promised its probes "restated whole" and copied the stripped `PAIRS_SH` of
`TOOL-dGroundRules-34` AC16 instead, and `TOOL-dGroundRules-43` AC1 inherited it; the skeptic's
corrected fix ends "re-run the literal from the repository root before committing the spec".
The rule to spell a literal whole in a fenced block is `TOOL-dGroundRules-42` S3, which widens the
record `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` at order 13, before
this unit. At HEAD the record does not hold it yet: its fix section names no fenced block. S3 does
not say to run the literal, and a whole-looking literal copied from a corrupted source is still
corrupted. This unit is id 1's promotion and the item's checklist half: the record's fix gains the
re-run rule after the paragraph S3 writes, and its "Where it bit" gains this round. It repairs
`TOOL-dGroundRules-40`, which sits at order 13, so it builds at order 14.

## 2. Scope (IN)

- **S1** — The re-run. "The fix" of
  `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` gains: every literal a
  spec's acceptance section spells that only reads is run verbatim from the repository root before
  the spec's commit, and its output is compared with what the criterion expects; a literal restated
  from another spec is re-run in the same way and never copied on trust, because a copy carries its
  source's corruption. Observed by AC1.
- **S2** — Where it bit. A paragraph in "Where it bit" names this audit's H1 (review ids 1, 10 and
  20): `TOOL-dGroundRules-40` restated `TOOL-dGroundRules-34` AC16's stripped literal while promising
  it whole, one round after `TOOL-dGroundRules-42` recorded the respelled form. Observed by AC2.
- **S3** — The index row holds. The record's front-matter `description` is unchanged, and neither
  new paragraph backticks a path-like token, so the record's derived anchors and its row in
  `memory/gotchas/INDEX.md` stay as `TOOL-dGroundRules-42` leaves them. NOT OBSERVED: a row this
  unit leaves as it was reads the same before the unit as after it, so no criterion can red on it;
  the `memory hygiene` leg in §6 runs `gotchas.py --check`, whose check 17 reds a stale index.

## 3. Non-goals (OUT)

- A gate that runs spec literals. `TOOL-dGroundRules-46` §4 says why a gate does not execute spec
  text, and gates the one form a text join can see.
- A new class record. The copied literal is the fifth form `TOOL-dGroundRules-42` adds, met again.
- The arm and probe repairs: `TOOL-dGroundRules-44` and `TOOL-dGroundRules-45`.

### Edges

- **consumes-from** `TOOL-dGroundRules-42` — the record's fifth form and its S3 fenced-block fix, which S1 extends with the re-run and S2 with this round's instance

## 4. Design

`TOOL-dGroundRules-42` S1 to S3 add the respelled input to the record's Symptom list, its "Where it
bit" and its fix, and its S4 backticks `memory/builds/` so `gotchas.py --for-diff` hands the record
to every spec commit. This unit adds two paragraphs to the same record, one in "The fix" after the
paragraph `TOOL-dGroundRules-42` S3 writes, and one in "Where it bit". The fix paragraph is the
skeptic's own wording for id 1, generalised from `PAIRS_SH` to any read-only literal.

Neither paragraph backticks a path-like token. In `tools/memory-tree/gotchas.py`, `ANCHOR_RE`
harvests a record's anchors from backticked tokens carrying a `/` or a listed file extension,
`build_record` keeps them, and `render` prints their count in the record's index row. A new anchor
would move that count, leave the index stale for check 17 in `cmd_check`, and widen which diffs
`selectable` hands the record to. The paragraphs name a unit id, a constant such as PAIRS_SH and
the review in plain text, as the record's existing "Where it bit" paragraphs do.

### Files touched (estimate)

- `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`

## 5. Acceptance criteria

- **AC1** — When
  `sed -n '/^## The fix/,/^## Related/p' memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md | grep -c "verbatim from the repository root"`
  runs, it prints `1` or more, and the same command with `grep -c "never copied"` in place of the
  last stage prints `1` or more. Both print `0` at commit 9bcca652 (measured 2026-10-24, PINNED).
  Red when: "The fix" lacks the re-run of a literal from the root (the first count), or lacks the
  rule that a restated literal is re-run rather than copied (the second count).
- **AC2** — When
  `sed -n '/^## Where it bit/,/^## The fix/p' memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md | grep -c "TOOL-dGroundRules-40"`
  runs, it prints `1` or more. It prints `0` at commit 9bcca652 (measured 2026-10-24, PINNED).
  Red when: "Where it bit" does not name this round's copied literal, including when the paragraph
  lands in another section of the record.

## 6. Gates

`gotchas selftest` · `memory hygiene` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 1 (HIGH, item H1) of the round-1 spec
  audit of units 35 to 43 as the item's checklist half, from the skeptic's corrected fix, with the
  record's fix section and unit 42's scope read on 2026-10-23.
- rev-2 · 2026-10-24 · the staleness probe against HEAD found four disagreements, and the run ruled
  on each. §1 said the record already holds the fenced-block fix; the ruling states it is
  `TOOL-dGroundRules-42` S3, built at order 13 before this unit, and absent from the record at HEAD.
  §4 credited S1 to S3 of that unit with the anchors; the ruling cites its S4. AC2 ran
  `gotchas.py --check`, green before this unit; the ruling replaces it with a section-scoped count
  that prints `0` at HEAD, AC1 is scoped to "The fix" the same way, and S3 is `NOT OBSERVED` with
  its reason, after reading that `render` counts anchors in the index row. Code is cited by symbol,
  never by line number.

## 9. Reuse audit

The seam extended is the record `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`,
which `TOOL-dGroundRules-42` widens to the respelled input; no new record is written.
`python tools/codebase-map/reuse_lookup.py "flag a shell library sourced by a bare file name in a
spec acceptance literal"` ranks code seams and none of record shape, so the record was found by
listing `memory/gotchas/`. The recall probe returned `TOOL-dGroundRules-42` and the open ask
`TOOL-aKeyedAnnotation-9`; both agree with widening the record rather than minting one.

Recall terms used: `python tools/memory-recall/query.py "how is a stripped criterion literal repaired
and kept from being respelled" --terms "acceptance criterion literal stripped respelled fenced block
root re-run paths join spec-tokens table"`
