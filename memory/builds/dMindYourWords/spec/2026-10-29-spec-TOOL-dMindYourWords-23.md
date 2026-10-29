# TOOL-dMindYourWords-23 — the `--measure` and `--rebaseline` writers keep the `lexicon-debt` rows they do not measure

**Status:** OPEN · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 |
| [2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-24 TOOL-dMindYourWords-27 TOOL-dMindYourWords-26 TOOL-dMindYourWords-28 TOOL-dMindYourWords-22 TOOL-dMindYourWords-25 TOOL-dMindYourWords-29 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 43 of `reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md`, HIGH, which
shares item H1 with id 1 (TOOL-dMindYourWords-22). TOOL-dMindYourWords-1 makes `--measure > <home>` the
drain edit and has `--measure` print the whole ledger file the tree produces; TOOL-dMindYourWords-11
S8's `--rebaseline` writes the pin to equal the debt population. Both measure the corpus only, so once
TOOL-dMindYourWords-13 seeds tag rows, the first drain edit and every re-baseline delete them, and the
next `--tags` run reds on the live policy keys. This unit makes both writers carry the tag slice
through unchanged.

## 2. Scope (IN)

- **S1** — `--measure` carries the other slice. Its printed ledger is the corpus slice it measured,
  each row keeping the sha and disposition the home already gives it (TOOL-dMindYourWords-1 §4 "The
  registration"), plus every row of the current home whose `derive_ledger_slice` (TOOL-dMindYourWords-22 S1) is
  `tags`, byte for byte, in the row order the factory's `write_rows` gives the merged set. With no home
  there is nothing to carry. Observed by AC1 and AC3.
- **S2** — `--rebaseline <record>` carries the other slice. It writes the corpus slice equal to the debt
  population, each key it gains carrying `widened:<record>` (TOOL-dMindYourWords-11 S8), and keeps every
  `tags` row of the home unchanged; its printed `re-baseline <tag>: debt <old> -> <new>` counts the
  corpus slice only. Observed by AC2.
- **S3** — The carried count. Both writers print one line to stderr, `lexicon: <writer> carried <n>
  row(s) of the tags slice unchanged`, so a carry that matched nothing reads as zero and never as
  silence, and stdout stays the ledger file. Observed by AC1 and AC2.
- **S4** — The docs. The debt-ledger section of `tools/lexicon/README.md` states that the drain edit and
  the re-baseline rewrite the corpus slice and keep the tag rows, which drain by hand on the row the
  `--tags` run prints; `KIT_LEXICON_VERSION` moves once. NOT OBSERVED as behaviour: prose has no grader
  beyond the carriers' own legs.

## 3. Non-goals (OUT)

- Which rows each run compares: TOOL-dMindYourWords-22.
- A `--tags` writer for the tag slice: tag rows are seeded once by unit 13's Migration and drain by the
  printed row, and no clause names a tag writer.
- `--measure`'s line endings and its other stdout lines: review ids 13 and 2, the minors batch
  TOOL-dMindYourWords-29.
- The left-shift lint the report names under H1: a gate is its own unit (BUILD-METHOD M2).

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — the `--measure` writer and `--measure > <home>` as the drain edit; without it there is no writer to make carry
- **consumes-from** `TOOL-dMindYourWords-11` — `--rebaseline <record>`, the second writer of the home
- **consumes-from** `TOOL-dMindYourWords-13` — the tag rows its Migration seeds into the home, the slice both writers carry
- **consumes-from** `TOOL-dMindYourWords-22` — `derive_ledger_slice`, the one predicate deciding which rows a writer carries
- **hands-off** `TOOL-dMindYourWords-29` — `--measure`'s stdout as the ledger file alone, on which the batch routes the tally lines to stderr and sets LF line endings (ids 2, 13)
- **hands-off** `TOOL-dMindYourWords-35` — the `--measure` merge's read of the home, which that unit re-sources from the index copy when stdout is the home (review id 30)
- **hands-off** `TOOL-dMindYourWords-37` — the `--measure` carry and AC1's drain edit, which the minors batch re-observes after the tally lines move to stderr and widens to the drift rows a shallow run holds (review ids 5 and 37)

## 4. Design

### Evidence

- `--measure` today prints the two scalar pins and the `PINS:` rows (`tools/lexicon/lexicon.py:3552-3574`);
  unit 1 S7 makes it print the ledger file instead and calls `--measure > <home>` the drain edit, with
  AC9 requiring the print to equal the home byte for byte.
- Unit 11 S8 writes the pin "so it equals the debt population", the corpus offenders whose grade is
  `debt`; unit 13's Migration says `--rebaseline` grades the corpus only and writes the tag rows
  "beside its run" by hand once (`spec/2026-10-29-spec-TOOL-dMindYourWords-13.md` §4 Migration).
- `run()` is the one mode branch (`lexicon.py:3518-3520`), so both writers share one place to merge.

### The merge

```
home_rows = read_rows(home) if home exists else []
carried   = [r for r in home_rows if derive_ledger_slice(r, reg_rel) == "tags"]
written   = measured_corpus_rows + carried          # write_rows orders the merged set
print(f"lexicon: {writer} carried {len(carried)} row(s) of the tags slice unchanged", file=sys.stderr)
```

### Inventory

Minted: the stderr line `lexicon: <writer> carried`. No function: both writers call
TOOL-dMindYourWords-22's `derive_ledger_slice` and the factory's `read_rows` and `write_rows`.

### Migration

None. A home written before this unit and after unit 13 already holds the tag rows; the next writer
run keeps them.

### Rollout

Live at landing, in the same landing as TOOL-dMindYourWords-13, so no landed tree runs a writer that
drops tag rows.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1, S2, S3, `KIT_LEXICON_VERSION`
- `tools/lexicon/selftest.py`: the arm of §7
- `tools/lexicon/README.md`: S4

### Alternatives rejected

- **Each writer measures every slice**: the tags arrive on stdin from the core's one call per run, so a
  corpus writer has no tag set; carrying is the only form a single-producer writer can take.
- **A refusal when the home holds a row the writer does not measure**: it blocks every drain edit after
  unit 13's landing, the opposite of the drain the ledger exists for.

## 5. Production-readiness checklist

- security — the write path is unchanged: the factory's `write_rows` writes only the registration's
  `home`; this unit adds rows already in that file, never new content.
- perf / scale — one extra read of the home per writer run.
- error / empty / loading states — no home: nothing carried, the line prints 0; a home the factory
  refuses to read is the factory's refusal, never an empty carry.
- observability — S3's stderr line on every writer run.
- risks — a stale tag row is carried until a `--tags` run prints it drained and the operator deletes it,
  which is the ordinary drain of that slice.
- testing — AC1 to AC3 and the arm of §7.
- migration — none.
- user docs — `tools/lexicon/README.md` (S4).

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py --measure` runs in a fixture whose home holds two
  corpus rows and one tag row, stdout carries the tag row byte-identical and stderr prints `carried 1
  row(s) of the tags slice`; redirecting stdout over the home leaves `git diff --exit-code` on the home
  exiting 0 once carriage returns are dropped (`tr -d '\r'`).
  Red when: the tag row is absent from stdout, so the drain edit deletes it.
  fixture: a scratch repository under `%TEMP%`; line endings are the batch's (id 13).
- **AC2** — When `python tools/lexicon/lexicon.py --rebaseline <record>` runs on the same fixture with a
  vocabulary record that reclassifies one corpus offender, `grep -c` for the tag row's key in the home
  prints 1 and the printed `re-baseline` counts move by the corpus change alone.
  Red when: the re-baseline rewrites the home without the tag row.
- **AC3** — When both writers have run, `printf '<the tag>\n' | python tools/lexicon/lexicon.py --tags`
  exits 0 and prints the tag as `debt`.
  Red when: a writer run left the tags slice without its row, so the tags run reds.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest` · `kit version markers`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 · a fixture home holding corpus and tag rows, its failing case the carry cut out of `--measure`, under which AC1's stdout lacks the tag row · none

## 8. Open questions

- **F1 — How does a single-producer writer treat rows another producer owns?** Options: (a) carry them
  unchanged; (b) measure them too; (c) refuse to write. (b) has no tag set to measure and (c) blocks
  every drain. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the report's first route for the
  writers, "the `--measure` and `--rebaseline` writers keep the rows they do not measure". widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 43 (HIGH, item H1) of the round-1 spec
  audit; the comparison half of the item is TOOL-dMindYourWords-22.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 22 to 29
  declare toward this unit (TOOL-dMindYourWords-35, TOOL-dMindYourWords-37); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are the two writers TOOL-dMindYourWords-1 and TOOL-dMindYourWords-11 add to `run()`
(`tools/lexicon/lexicon.py:3518`), the factory's `read_rows` and `write_rows` for the file, and
TOOL-dMindYourWords-22's `derive_ledger_slice` for the partition. `python tools/codebase-map/reuse_lookup.py
"keep the rows another producer owns when rewriting a shared ledger file"` ranked name-stem helpers
(`rows`, `row`, `extract_row`, `owners_of`) and no writer that preserves foreign rows, so no existing
seam fits the carry beyond the factory's own reader and writer, which this unit composes.

Recall terms used: `python tools/memory-recall/query.py "how does the lexicon debt ledger keep its rows when tag findings and corpus findings share one population" --terms "lexicon-debt ledger drain measure rebaseline tags slice check_debt_pin widened shallow provenance"`
