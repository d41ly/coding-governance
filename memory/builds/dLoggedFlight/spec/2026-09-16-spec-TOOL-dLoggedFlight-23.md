# TOOL-dLoggedFlight-23 — one self-test arm holds every time-bearing token a render writes to a public source, over classes and slots read from the schema and a fixture that reaches every conditional slot

**Status:** SPECCED · rev-2 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling · order 28

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md) | journal | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-24 TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-26 TOOL-dLoggedFlight-27 TOOL-dLoggedFlight-28 TOOL-dLoggedFlight-29 TOOL-dLoggedFlight-30 |
| [2026-09-16-review-TOOL-dLoggedFlight-21-spec-audit-round1.md](../reviews/2026-09-16-review-TOOL-dLoggedFlight-21-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-24 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dLoggedFlight-20` at rev-1 gave every `utc` and `duration` slot a declared source, then checked
the rendered text by reading `utc` tokens only. The schema's `duration` shape, `[0-9]{1,12}s`
(`tools/runlog/record.py:142`), is not a `utc` token, and a rendered start plus a rendered duration
recovers an end. That is the recovery the first closing review recorded as its B1, and the class
`memory/gotchas/withheld-value-recovered-from-a-derived-one.md` names (H1). The same check read only
the slots its fixture happened to fill. The Timeline `elided` fact renders only once the kept rows pass
twice `TIMELINE_EDGE` (`record.py:78`, `:710`), and no criterion read it (H2). The spec audit of units
14, 16 and 20, round 1, confirmed both as HIGH, and the loop promoted them here together, since both
are the population of one arm.

Make that arm read its token classes and its slot list from the schema's own declaration, grade every
token of those classes plus every encoding of each sentinel whatever class carries it, and assert that
every declared slot rendered. A new time-bearing slot, class or conditional row then joins the check
without an edit, and a slot the fixture failed to reach reds instead of passing silent.

Every code line cited here was read at `ba3bd9fd` on the run branch. The `base` above is the
default-branch sha the format asks for, and `tools/runlog` does not exist there yet.

## 2. Scope (IN)

- **S1** The declaration it reads. The arm takes the time-bearing classes from
  `RECORD_SCHEMA["time_classes"]` and the slot list from `scan_time_slots(RECORD_SCHEMA)`, both of which
  `TOOL-dLoggedFlight-20` S1 declares. It holds no typed list of classes or slots. Observed by AC3 and
  AC4.
- **S2** The fixture. `build_sentinel_model` builds a model from the landed fixture, through
  `build_run_model`, and extends it:
  - every journal and transcript event, and the model `window`'s start and end, carries a sentinel
    second;
  - the kept rows pass twice `TIMELINE_EDGE`, with journal events interleaved among them, so an elided
    range read from the unfiltered timeline differs from the kept one;
  - it carries a commitment made by `measure_commitment`, one anomaly of each member of `ANOMALY_KINDS`,
    one review round row, and events from `driver`, `gates`, `pushes` and `transcripts`.

  Each sentinel differs from every commit time and run-state row time in the fixture, and from each
  such time plus any difference of two such times, plus zero or one second, and its clock time differs
  from every public time's. No difference of two sentinels, and no sentinel less a public time, equals
  a non-negative difference of two public times, since the renderer computes `duration` as end less start
  (`tools/runlog/record.py:624`) and S3's duration rule accepts any public difference. The arm asserts
  that choice before it grades, so a coincidence in the fixture cannot fail it. Observed by AC1 and AC3.
- **S3** The token rule. Over the markdown and the Data twin, where a public time is a fixture commit's
  committer time or a run-state row's time:
  - every `utc` token equals a public time;
  - every `duration` token equals a non-negative difference of two public times;
  - no `utc` token plus a `duration` token, nor that sum plus one second, equals a sentinel;
  - whatever class carries it, no sentinel's ISO form, its epoch second as a whole integer token, or its
    `HH:MM:SS` appears anywhere in the text.

  Observed by AC1.
- **S4** The elided fact. The Timeline `elided` fact's two times equal the times of the first and last
  kept rows the shown tables omit. Observed by AC2.
- **S5** Liveness. Every slot `scan_time_slots` returns rendered at least one token in the fixture's
  record, red naming the slot that rendered nothing. Every `shaped` class of `RECORD_SCHEMA` that
  fullmatches the rendered form of a public time or of a difference of two is in `time_classes`, red
  naming the class that is not. The sentinel set is non-empty, and the model the arm rendered carries
  each sentinel. Observed by AC3 and AC4.

## 3. Non-goals (OUT)

- Which slots exist and which sources they declare. `TOOL-dLoggedFlight-20` S1, `-21`, `-22` and `-24`
  own them, and this arm grades what they leave.
- Grading committed records on the bar. `TOOL-dLoggedFlight-20` S7 gives the schema leg its source rule;
  this is a self-test arm over a fixture.
- The local model, which keeps every time.
- A render-time refusal. `TOOL-dLoggedFlight-22` retires the one that existed, and a sentinel is
  knowledge only a fixture holds.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-9` — `render_record`, `RECORD_SCHEMA` and `TIMELINE_EDGE`.
- **consumes-from** `TOOL-dLoggedFlight-20` — `time_classes`, `TIME_SOURCES` and `scan_time_slots`.
- **consumes-from** `TOOL-dLoggedFlight-21` — the commitment line, which carries no time token.
- **consumes-from** `TOOL-dLoggedFlight-22` — the kept Timeline rows and the tables with no time
  column.
- **consumes-from** `TOOL-dLoggedFlight-24` — the Summary `window` and `duration` facts, rendered from
  commit times.
- **consumes-from** `TOOL-dLoggedFlight-25` — the `window closed by` fact and the closing bound at each
  render placement, which a terminal placement renders from the last record commit's time.

## 4. Design

The owner-time class ended four times at a population narrower than the leak: first the row kinds, then
the `utc` slots, then `utc` tokens over whatever a fixture rendered. Each check enumerated one level
below the thing it guarded. This arm reads every population it grades from the declaration the render
also reads, and it adds two checks no declaration can narrow. The class-blind sentinel scan catches a
time in a class nobody declared. The per-slot liveness catches a slot the fixture never reached.

Differences of public times are public, because each operand is. A sum of a rendered time and a
rendered duration is the recovery path, so the rule grades sums against sentinels rather than trying to
enumerate which sums are legitimate.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `build_sentinel_model` | function | `py.function`, led by `build` |
| `test_record_time_population` | function | `py.function`, led by `test` |

### Files touched (estimate)

`tools/runlog/{selftest.py,README.md}` and `memory/map/features/runlog.md`.

### Alternatives rejected

- `TOOL-dLoggedFlight-20` rev-1 S6, `utc` tokens only, over whatever the fixture renders: rejected by
  H1 and H2.
- A typed pair of time classes and a typed list of slots: rejected, since a typed population is how the
  class kept escaping, and it is H1's left-shift.
- `TOOL-dLoggedFlight-19`'s owner-act classes over `utc` slots: superseded with that unit by the owner's
  ruling of 2026-09-16. Its schema-derived slot enumeration is kept, as `scan_time_slots`, and widened
  to every class `time_classes` names.

## 5. Production-readiness checklist

- security — every time-bearing token of a render is held to a public source by one arm.
- perf / scale — one render of one fixture; no git call beyond the fixture's model build.
- error / empty / loading states — a slot that rendered nothing reds by name rather than passing empty.
- observability — each failure names the slot, the class or the token's line.
- risks — a sentinel chosen near a public sum or difference would make a staged break invisible or fail
  the arm, which S2's pre-check refuses first.
- testing — each AC staged RED on a copy of the fixture model or of the schema.
- migration — N/A — test code only.
- user docs — the kit README's record section names the arm.

## 6. Acceptance criteria

- **AC1** — When `test_record_time_population` renders S2's fixture through `render_record`, every token
  obeys S3's rule in both copies.
  Red when: any token breaks it. Staged RED five ways, each on a copy: a renderer whose Summary
  `duration` reads the model's journal-bounded `window`, a model whose one kept `commit` row carries a
  journal event's time, a model whose `run` count is a sentinel epoch second, and two copies each
  carrying one sentinel encoding no `utc` token covers, its `HH:MM:SS` and its ISO form. No kept class
  but `utc` admits a colon (`record.py:117-152`), so those two ride a ledger entry `ref` on a schema copy
  whose `ref` class is widened to admit that encoding. Before its verdict, every staged RED asserts that
  its broken token reached the text and lies outside the set S3 accepts, and it reds as a dead probe
  otherwise.
- **AC2** — When the fixture's kept rows pass twice `TIMELINE_EDGE`, the `elided` fact renders, and its
  two times equal the first and last omitted kept rows' times, neither a sentinel.
  Red when: the fact does not render, or either time differs; staged RED by a renderer copy whose elided
  range is read from the model's unfiltered timeline.
- **AC3** — When the arm enumerates `scan_time_slots(RECORD_SCHEMA)`, every slot rendered a token. With
  the fixture's review round removed, it reds naming the Decisions `rounds` table's `UTC` column. With
  the kept rows cut to `TIMELINE_EDGE`, it reds naming the Timeline `elided` fact. Enumerating a copy of
  `RECORD_SCHEMA` that declares one extra `utc` slot the fixture's record never fills, it reds naming
  that slot.
  Red when: any staged fixture or copy passes, or the arm's slot list is typed.
- **AC4** — When the arm runs over a copy of `RECORD_SCHEMA` whose `time_classes` omits `duration`, it
  reds naming `duration` as a class that matched a rendered difference of public times.
  Red when: the copy passes.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · AC1's five copies, AC2's renderer copy, AC3's two cut fixtures and extra-slot schema copy, and AC4's schema copy · floor raised by the arm count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, promoted from H1 and H2 of the spec audit of units 14, 16 and
  20, round 1, at the loop's BOUNDED exit. It takes `TOOL-dLoggedFlight-20` rev-1 S6 and AC1's sentinel
  arm.
- rev-2 · 2026-09-16 · S2 · AC1 · AC3 · §3 · §5 · §7 · folded M3 and M4 of the spec audit of units 21 to 24,
  round 1. M3: AC3 stages a schema copy with one extra `utc` slot and reds on a typed slot list, and AC1
  stages the `HH:MM:SS` and ISO encodings on a widened `ref` class, since no kept class but `utc` admits
  a colon. M4: S2's pre-check refuses a sentinel difference, or a sentinel less a public time, that
  equals a public difference, and every staged RED asserts its break lies outside the accepted set
  before its verdict. §3 gains the edge to `TOOL-dLoggedFlight-25`, promoted by the same audit. The
  order moves from 25 to 28.

## 10. Reuse audit

The seams are `render_record` and `RECORD_SCHEMA` in `tools/runlog/record.py`, `scan_time_slots`, which
`TOOL-dLoggedFlight-20` S1 adds, and the landed fixture of `tools/runlog/selftest.py`, all this build's.
`tools/codebase-map/reuse_lookup.py "derive a test's population from a declared schema"` returned
name-stem candidates only, `derive_scope` and `population` among them, and none derives a test
population from a schema. The recall query returned `TOOL-dLoggedFlight-19` S1's slot enumeration,
which S1 reuses through unit 20, and the first closing review's B1, which S3's sum rule answers.

Recall terms used: owner turn time leak derived slot sentinel population fixture elided duration utc class gate arm
