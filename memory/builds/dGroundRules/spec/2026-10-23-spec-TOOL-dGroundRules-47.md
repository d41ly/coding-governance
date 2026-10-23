# TOOL-dGroundRules-47 — the criterion bug class's fix gains the re-run: a literal is run verbatim from the root before its spec commits, and a restated one is re-run, never copied

**Status:** DEFERRED · rev-1 · 2026-10-23 · node d · Tier-1 · base 3708a705 · streams tooling · order 14 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-47-deviation-35.md](../build/2026-10-23-build-TOOL-dGroundRules-47-deviation-35.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 35 to 43
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md`)
exited BOUNDED with finding **id 1 at HIGH**, which shares item **H1** with ids 10
(`TOOL-dGroundRules-46`) and 20 (`TOOL-dGroundRules-45`). Id 1 is H1 seen from coherence:
`TOOL-dGroundRules-40` promised its probes "restated whole" and copied the stripped `PAIRS_SH` of
`TOOL-dGroundRules-34` AC16 instead, and `TOOL-dGroundRules-43` AC1 inherited it; the skeptic's
corrected fix ends "re-run the literal from the repository root before committing the spec". The
record `TOOL-dGroundRules-42` widens already says to spell a literal whole in a fenced block; it does
not say to run it, and a whole-looking literal copied from a corrupted source is still corrupted.
This unit is id 1's promotion and the item's checklist half: the record's fix gains the re-run rule
and its "Where it bit" gains this round. It repairs `TOOL-dGroundRules-40`, which sits at order 13, so
it builds at order 14.

## 2. Scope (IN)

- **S1** — The re-run. "The fix" of
  `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` gains: every literal a
  spec's acceptance section spells that only reads is run verbatim from the repository root before
  the spec's commit, and its output is compared with what the criterion expects; a literal restated
  from another spec is re-run in the same way and never copied on trust, because a copy carries its
  source's corruption. Observed by AC1.
- **S2** — Where it bit. A paragraph names this audit's H1 (review ids 1, 10 and 20):
  `TOOL-dGroundRules-40` restated `TOOL-dGroundRules-34` AC16's stripped literal while promising it
  whole, one round after `TOOL-dGroundRules-42` recorded the respelled form. Observed by AC1.
- **S3** — The index stays current. The record's front-matter `description` is unchanged, so
  `memory/gotchas/INDEX.md` needs no new row text. Observed by AC2.

## 3. Non-goals (OUT)

- A gate that runs spec literals. `TOOL-dGroundRules-46` §4 says why a gate does not execute spec
  text, and gates the one form a text join can see.
- A new class record. The copied literal is the fifth form `TOOL-dGroundRules-42` adds, met again.
- The arm and probe repairs: `TOOL-dGroundRules-44` and `TOOL-dGroundRules-45`.

### Edges

- **consumes-from** `TOOL-dGroundRules-42` — the record's fifth form and its fenced-block fix, which S1 extends with the re-run and S2 with this round's instance

## 4. Design

`TOOL-dGroundRules-42` S1 to S3 add the respelled input to the record's Symptom list and its fix,
and anchor the record so `gotchas.py --for-diff` hands it to every spec commit. This unit adds two
paragraphs to the same record, one in "The fix" and one in "Where it bit", and changes no anchor, so
the selection `TOOL-dGroundRules-42` AC1 observes is unchanged. The fix paragraph is the skeptic's
own wording for id 1, generalised from `PAIRS_SH` to any read-only literal.

### Files touched (estimate)

- `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`

## 5. Acceptance criteria

- **AC1** — When
  `grep -c "verbatim from the repository root" memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
  runs, it prints `1` or more, and `grep -c "TOOL-dGroundRules-40"` over the same record prints `1`
  or more.
  Red when: the record names the stripped form without the re-run that would have caught the copy.
- **AC2** — When `python tools/memory-tree/gotchas.py --check` runs, it exits 0.
  Red when: the record's edit leaves the generated index stale.

## 6. Gates

`gotchas selftest` · `memory hygiene` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 1 (HIGH, item H1) of the round-1 spec
  audit of units 35 to 43 as the item's checklist half, from the skeptic's corrected fix, with the
  record's fix section and unit 42's scope read on 2026-10-23.

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
