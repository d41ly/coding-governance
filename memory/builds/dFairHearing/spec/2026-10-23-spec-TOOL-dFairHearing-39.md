# TOOL-dFairHearing-39 — a criterion quoting an error text its tool never emits, carried into the bug-class catalogue a spec commit selects

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 25 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-39-deviation-391.md](../build/2026-10-23-build-TOOL-dFairHearing-39-deviation-391.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-38-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-38-promoted-fix-brief.md) | research | TOOL-dFairHearing-38 TOOL-dFairHearing-40 |
| [2026-10-23-prompt-TOOL-dFairHearing-39-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-39-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-5 spec audit's finding id 11 (item H1, HIGH, shared with id 1,
`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md`) is
closed. Id 11 is the grounding lens's reading of the defect id 1 names: `TOOL-dFairHearing-37` AC4
quotes argparse's `unrecognized arguments` for a tool that reads its arguments by hand, so the text has
no emitting line and the criterion can neither pass on a correct build nor tell a shipped flag from an
absent one. The instance is repaired in `TOOL-dFairHearing-38`. A finding fixed and not left-shifted
returns (BUILD-METHOD M8), and the report names no gate for it: deciding which tool emits a quoted
text needs the criterion's intent. This unit adds the form to the catalogue class it belongs to,
`criterion-asserts-what-its-own-command-cannot-show`, and gives that class the anchor that makes
`gotchas.py --for-diff` select it for a commit touching a spec, which today it does not.

## 2. Scope (IN)

- **S1** — The form. `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` gains a
  fifth bullet under its Symptom, "The tool does not say that": a criterion quotes an error text or an
  exit status that the named tool never produces, often borrowed from a library the tool does not use.
  Observed by AC2.
- **S2** — Where it bit. The record's Where it bit section gains this instance: unit 37 AC4, the
  round-5 spec audit's ids 1 and 11, the `--for-diff` branch of the bug-class tool's `main` reading one
  argument at `3708a705` (lines 1335 to 1339), and the repair in unit 38. The tool is named in plain
  text there, not as a backticked path, so the record derives no anchor on the tool itself and is not
  selected for every change to it. Observed by AC2.
- **S3** — The check. The record's fix section gains one rule: a criterion that quotes a tool's error
  text or exit status cites the line of that tool that emits it at the spec's base, or the scope item
  that adds it. Observed by AC2.
- **S4** — The anchor. The record's body carries the backticked token `/spec/`, the anchor
  `observed-by-claim-no-arm-discharges` already uses, so a range or a path set that touches a spec
  under any build's `spec/` folder selects the class. Its description gains the clause "or an error
  text its tool never emits", and `memory/gotchas/INDEX.md` is regenerated with
  `python tools/memory-tree/gotchas.py --write`, its anchor count for the class moving from 2 to 3.
  Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- No repair of unit 37 AC4: that is id 1's mechanism, `TOOL-dFairHearing-38`; the two units share no
  file.
- No machine gate and no new class. The record's own Its gate section states why the class has none,
  and this form is the same defect one shape further.
- No change to `gotchas.py`, its anchor harvest or its selection.
- No MEDIUM or LOW finding of the same audit: those 35 are `TOOL-dFairHearing-40`'s.
- No help page: `help/` covers neither the bug-class catalogue nor the review harness.

### Edges

- **consumes-from** `TOOL-dFairHearing-37` — AC4's wording at rev-1, the instance S2 cites; without it the record names no place the form bit

## 4. Design

### Why the existing class and not a new one

The class already lists the forms of a criterion whose command cannot answer it, and its first form,
"the command does not print that", is this defect's nearest neighbour. A second record would split one
lens brief over two checklist lines. The form joins the list and the description names it, so a
reviewer reading only the checklist line sees it.

### Why the anchor

Measured on 2026-10-23: `gotchas.py --for-paths` over
`memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-37.md` lists
`observed-by-claim-no-arm-discharges` and not this class. The class's two derived anchors today are
`tools/check-testsuite-counts.sh` and `tools/check-spec-tokens.py`, so the spec audit's checklist, the
`--for-diff` output over a spec commit, never hands it to a lens. The `/spec/` token selects by
substring (`selectable`, `tools/memory-tree/gotchas.py:340`), as it does for the sibling class.

### Files touched (estimate)

- `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
- `memory/gotchas/INDEX.md`

`INDEX.md` changes only through `gotchas.py --write`, never by hand.

### Alternatives rejected

- **A new class record for this form.** One defect over two checklist lines, and the existing record
  already says criteria of this shape are written by someone who just read the code.
- **A gate that greps each quoted error text in a criterion against its tool's source.** It cannot tell
  a text the unit's own scope item adds from one the tool must already emit, which is the intent the
  record's Its gate section names.

## 5. Production-readiness checklist

- security — N/A: a catalogue record and its generated index; no code and no write path.
- perf / scale — one more line in the checklist of a commit that touches a spec.
- error / empty / loading states — N/A: no runtime behaviour.
- observability — the class appears in `--for-diff` and `--for-paths` output for spec paths.
- risks — the anchor over-selects for any path holding `/spec/`; the catalogue's derivation is
  recall-biased by design (`tools/memory-tree/gotchas.py`, its module docstring).
- testing — AC1 to AC3 by direct runs of the tool and the record.
- migration — none.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --for-paths memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-37.md`
  runs at this unit's commit, it lists `criterion-asserts-what-its-own-command-cannot-show`. Run at
  this unit's parent, it does not.
  Red when: the record derives no anchor a spec path reaches.
- **AC2** — When `grep -c "unrecognized arguments" memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
  runs, it prints a number above 0, and `grep -n "TOOL-dFairHearing-37"` over the same record prints the
  Where it bit line. `grep -c "tools/memory-tree/gotchas.py" <the record>` prints 0.
  Red when: the form, its instance or its check is absent, or the tool is cited as an anchor.
- **AC3** — When `python tools/memory-tree/gotchas.py --check` runs at this unit's commit, it exits 0,
  and the class's row in `memory/gotchas/INDEX.md` shows 3 anchors.
  Red when: the index was not regenerated after the anchor or the description moved.
  figure: 3 is DERIVED, the 2 anchors counted on 2026-10-23 plus `/spec/`.

## 7. Gates

`gotchas selftest` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No new arm: the change is a catalogue record, observed directly by §6.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 11 (item H1, HIGH, shared with id 1) of the
  round-5 spec audit of specs 33 to 37.

## 10. Reuse audit

The seam extended is the catalogue class `criterion-asserts-what-its-own-command-cannot-show`
(`memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`) and the `/spec/` anchor
convention `observed-by-claim-no-arm-discharges` set. `python tools/codebase-map/reuse_lookup.py
"record a recurring bug class a review keeps finding in specs"` ranked `records` in
`tools/memory-tree/gotchas.py` first, the catalogue reader this record feeds, and no second catalogue.
The recall query returned that class record and `memory/gotchas/INDEX.md` in its top four, beside
`TOOL-dTieredTribunal-24`'s ask for greps over a spec's criteria, which the alternatives above weigh.

Recall terms used: `python tools/memory-recall/query.py "a spec criterion quotes an error message the tool never prints" --terms "criterion asserts command cannot show error text quoted tool emits gotchas class left-shift spec audit"`
