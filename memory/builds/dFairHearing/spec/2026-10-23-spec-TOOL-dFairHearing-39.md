# TOOL-dFairHearing-39 — a criterion quoting an error text its tool never emits, carried into the bug-class catalogue a spec commit selects

**Status:** CLOSED · rev-3 · 2026-11-04 · node d · Tier-2 · base 3708a705 · streams tooling · order 27 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-39-deviation-391.md](../build/2026-10-23-build-TOOL-dFairHearing-39-deviation-391.md) | deviation | — |
| [2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md) | journal | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-40 TOOL-dFairHearing-43 |
| [2026-11-04-build-TOOL-dFairHearing-39-1-acceptance-ledger.md](../build/2026-11-04-build-TOOL-dFairHearing-39-1-acceptance-ledger.md) | journal | — |
| [2026-11-04-build-TOOL-dFairHearing-39-1-builder-return.md](../build/2026-11-04-build-TOOL-dFairHearing-39-1-builder-return.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-38-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-38-promoted-fix-brief.md) | research | TOOL-dFairHearing-38 TOOL-dFairHearing-40 |
| [2026-10-23-prompt-TOOL-dFairHearing-39-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-39-1-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFairHearing-39-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFairHearing-39-build-brief.md) | research | — |
| [2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief.md) | research | TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-35 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-40 |
| [2026-11-04-prompt-TOOL-dFairHearing-39-1-spec-writer.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-39-1-spec-writer.md) | journal | — |
| [2026-11-04-prompt-TOOL-dFairHearing-39-fix-brief.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-39-fix-brief.md) | research | — |
| [2026-11-04-review-TOOL-dFairHearing-1-40-diff-review.md](../reviews/2026-11-04-review-TOOL-dFairHearing-1-40-diff-review.md) | diff-review | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-40 |

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
`criterion-asserts-what-its-own-command-cannot-show`, which `gotchas.py --for-diff` already hands to
a commit touching a spec: `TOOL-dGroundRules-42` (commit `8fa309e89`) backticked `memory/builds/` in
the record's body, and that directory anchor reaches every spec under a build's `spec/` folder (§4,
§8 F1). This unit adds no anchor.

## 2. Scope (IN)

- **S1** — The form. `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` gains an
  eighth bullet under its Symptom, "The tool does not say that": a criterion quotes an error text or
  an exit status that the named tool never produces, often borrowed from a library the tool does not
  use. The Symptom's lead sentence, "Seven ways" at `678d0e91d`, reads "Eight ways". Observed by AC2.
- **S2** — Where it bit. The record's Where it bit section gains this instance: unit 37 AC4, the
  round-5 spec audit's ids 1 and 11, the `--for-diff` branch of the bug-class tool's `main` reading one
  argument at `3708a705` (lines 1335 to 1339), and the repair in unit 38. The tool is named in prose
  there, as the bug-class tool, and never as a backticked path or basename, so the record derives no
  anchor on the tool itself and is not selected for every change to it. Observed by AC2.
- **S3** — The check. The record's fix section gains one rule, in these words: a criterion that quotes
  a tool's error text or exit status cites the line of that tool that emits it at the spec's base, or
  the scope item that adds it. Observed by AC2.
- **S4** — The description and the index. The record's front-matter `description` ends ", or an error
  text its tool never emits", the "or" before its current last clause dropping to a comma, and
  `memory/gotchas/INDEX.md` is regenerated with `python tools/memory-tree/gotchas.py --write`. The
  record's `memory/builds/` anchor stays, and no new backticked path-like token enters its body, so
  the class's anchor count does not move. Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- No repair of unit 37 AC4: that is id 1's mechanism, `TOOL-dFairHearing-38`; the two units share no
  file.
- No machine gate and no new class. The record's own Its gate section states why the class has none,
  and this form is the same defect one shape further.
- No change to `gotchas.py`, its anchor harvest or its selection.
- No new anchor: `memory/builds/`, set by `TOOL-dGroundRules-42`, already selects the class for a
  spec path (§4, §8 F1).
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

### The anchor is already there

rev-2 measured on 2026-10-23 that a spec path did not select the class, and gave it a `/spec/`
anchor. The next day `TOOL-dGroundRules-42` (CLOSED, rev-2, its S4) backticked `memory/builds/` in
the record's body in commit `8fa309e89`, whose trailer records `--for-diff b9f7b5c4e~1..b9f7b5c4e`
naming the record 0 times before and once after, by its directory anchor.

Measured on 2026-11-04 at `678d0e91d`: the record's anchors, harvested by `ANCHOR_RE`
(`tools/memory-tree/gotchas.py:65`) over its body (`:281`), are `memory/builds/`,
`tools/check-spec-tokens.py` and `tools/check-testsuite-counts.sh`, and its row in
`memory/gotchas/INDEX.md` (`:58`) shows 3. `gotchas.py --for-paths` over
`memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-37.md` lists the class at the
`(directory)` tier, because `selectable` (`tools/memory-tree/gotchas.py:340`) admits a path that
holds an anchor as a substring. Every spec under a build's `spec/` folder holds `memory/builds/`, so
a `/spec/` anchor would reach no spec path the class does not already reach, and rev-2's AC1 parent
half, "run at this unit's parent, it does not", is red on today's tree. §8 F1 records the choice.

The same tool over `tools/memory-tree/gotchas.py` lists no line of the class today: none of the
three anchors is a substring of that path or shares its basename. That is the state S2's prose
naming keeps, and AC2 reads it.

The `--for-diff` branch S2 cites at `3708a705` (lines 1335 to 1339) sits at
`tools/memory-tree/gotchas.py:1461-1465` at `678d0e91d`, still reading only `argv[2]`. The record
cites it at the pinned base, so the line drift does not reach the record.

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
- risks — the existing `memory/builds/` anchor over-selects every record under a build, not only
  specs; the catalogue's derivation is recall-biased by design (`tools/memory-tree/gotchas.py`, its
  module docstring). This unit adds no anchor, so it widens nothing.
- testing — AC1 to AC3 by direct runs of the tool and the record.
- migration — none.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --for-paths memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-37.md`
  runs at this unit's commit, it lists `criterion-asserts-what-its-own-command-cannot-show`. It lists
  it at the parent too, since the anchor is `TOOL-dGroundRules-42`'s (§4): this criterion checks that
  the unit's edit keeps the anchor, and AC2 observes what the unit adds.
  Red when: the edit drops or respells the record's `memory/builds/` token, so no anchor a spec path
  reaches survives.
- **AC2** — When `grep -c "unrecognized arguments" memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
  runs, it prints a number above 0. Over the same record, `grep -c "TOOL-dFairHearing-37"` prints a
  number above 0, `grep -c "the line of that tool that emits it"` prints a number above 0 and
  `grep -c "Eight ways"` prints 1; each of the four prints 0 at `678d0e91d`. And
  `python tools/memory-tree/gotchas.py --for-paths tools/memory-tree/gotchas.py` prints no line
  naming `criterion-asserts-what-its-own-command-cannot-show`; AC1's run of the same tool over a spec
  path is its liveness twin.
  Red when: the form, its instance, its check or the moved count is absent, or the record cites the
  tool by a backticked path or basename that derives an anchor on it.
- **AC3** — When `python tools/memory-tree/gotchas.py --check` runs at this unit's commit, it exits 0;
  `grep -c "an error text its tool never emits" memory/gotchas/INDEX.md` prints 1; and the class's
  row in that file shows the anchor count the same row shows at the unit's parent, read with
  `git show <commit>~1:memory/gotchas/INDEX.md`, `<commit>` being this unit's commit.
  Red when: the index was not regenerated after the description moved, or the edit added an anchor.
  figure: the anchor count is DERIVED from the parent's row, 3 at `678d0e91d`, and never typed here.

## 7. Gates

`gotchas selftest` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No new arm: the change is a catalogue record, observed directly by §6.

## 8. Open questions

- **F1 — Does S4 still add the `/spec/` anchor, now that `TOOL-dGroundRules-42` anchored the class
  to `memory/builds/`?** (a) Drop S4's `/spec/` anchor and AC1's parent half; AC1 keeps its commit
  half as the check that the edit keeps the existing anchor, and AC3 reads the anchor count from the
  parent's row rather than typing one. (b) Keep the `/spec/` anchor as rev-2 specced it, with AC1's
  parent half and AC3's typed 3. (b) fails AC1 as written on today's tree, since the parent already
  lists the class by its directory anchor (§4), and its AC3 count would read 4 against the typed 3,
  so veto 1 discards it. (a) meets every criterion and leaves no follow-up: the goal's outcome, a
  spec commit's checklist naming the class, already holds. Recommendation (a). Rung 3. RESOLVED
  (agent, 2026-11-04, delegated): (a), the run's resolution in fix brief
  2026-11-04-prompt-TOOL-dFairHearing-39-fix-brief, verified against the record at `678d0e91d` and
  commit `8fa309e89`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 11 (item H1, HIGH, shared with id 1) of the
  round-5 spec audit of specs 33 to 37.
- rev-2 · 2026-11-03 · header order · §3 Edges · the header's order 25 to 27: its §3 consumes from
  unit 37, now at 26 (fix brief 2026-11-03-prompt-TOOL-dFairHearing-25-reorder-fix-brief, item 2).
- rev-3 · 2026-11-04 · §1 · §3 · §4 · the `memory/builds/` anchor `TOOL-dGroundRules-42` set in
  `8fa309e89` stated, with the record's three derived anchors measured at `678d0e91d` (fix brief
  2026-11-04-prompt-TOOL-dFairHearing-39-fix-brief, item 1).
- rev-3 · 2026-11-04 · §8 F1 · the `/spec/` anchor dropped, option (b) discarded by M3's veto 1
  (fix brief 2026-11-04-prompt-TOOL-dFairHearing-39-fix-brief, item 2).
- rev-3 · 2026-11-04 · §2 S4 · §5 risks · AC1 · AC3 · S4 adds no anchor; AC1 loses its parent half
  and reds on a dropped anchor; AC3 reads the description clause and the parent row's count (fix
  brief 2026-11-04-prompt-TOOL-dFairHearing-39-fix-brief, item 3).
- rev-3 · 2026-11-04 · §2 S1 · S3 · AC2 · the form is the eighth bullet, the record holding seven at
  `678d0e91d`, and the lead count moves; AC2 greps the check's words and the count, and reads the
  tool's own selection over its path in place of a grep that a prose mention of the path would red
  (fix brief 2026-11-04-prompt-TOOL-dFairHearing-39-fix-brief, item 4).
- rev-3 · 2026-11-04 · §4 · §10 · the `--for-diff` branch located at :1461-1465 at `678d0e91d` and
  `selectable` confirmed at :340; §10's seam names the `memory/builds/` anchor in place of the
  `/spec/` convention (fix brief 2026-11-04-prompt-TOOL-dFairHearing-39-fix-brief, item 4).

## 10. Reuse audit

The seam extended is the catalogue class `criterion-asserts-what-its-own-command-cannot-show`
(`memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`) and the `memory/builds/`
anchor `TOOL-dGroundRules-42` gave it, which this unit keeps and does not extend. `python tools/codebase-map/reuse_lookup.py
"record a recurring bug class a review keeps finding in specs"` ranked `records` in
`tools/memory-tree/gotchas.py` first, the catalogue reader this record feeds, and no second catalogue.
The recall query returned that class record and `memory/gotchas/INDEX.md` in its top four, beside
`TOOL-dTieredTribunal-24`'s ask for greps over a spec's criteria, which the alternatives above weigh.

Recall terms used: `python tools/memory-recall/query.py "a spec criterion quotes an error message the tool never prints" --terms "criterion asserts command cannot show error text quoted tool emits gotchas class left-shift spec audit"`
