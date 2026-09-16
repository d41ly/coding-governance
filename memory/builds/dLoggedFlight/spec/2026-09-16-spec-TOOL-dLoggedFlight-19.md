# TOOL-dLoggedFlight-19 — every UTC slot of the record schema is classed against owner acts, and one arm reads every time a production render writes

**Status:** SPECCED · rev-1 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling · order 19

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dLoggedFlight-15` at rev-1 offered a class gate as what stops a third fold of one class: every
timed kind the renderer emits would sit in exactly one of two sets. Its population was the Timeline
events table's row kinds. The schema carries times that have no row kind: the Summary's `window` and
`commitment` facts, the Timeline's `elided` fact, and the `utc` columns of the `rounds`, `anomalies`
and `sources` tables. The held times of unit 15 leaked through exactly those slots, as H1 and H2 (H3).
The spec audit of units 14 and 15, round 1, confirmed H3 as HIGH, and the loop promoted it here. Take
the gate's population from `RECORD_SCHEMA`'s own `utc` shape, so a new timed slot reds until it is
classed, and prove the classes with one arm that scans every UTC token a production render writes.

Every code line cited here was read at `a6f9d52e` on the run branch. The `base` above is the
default-branch sha the format asks for, and `tools/runlog` does not exist there yet.

## 2. Scope (IN)

- **S1** The population. `scan_time_slots(schema)` in `tools/runlog/record.py` returns every
  `utc`-shaped slot of the schema it is handed, `RECORD_SCHEMA` (`record.py:130`) in production:
  - each `{utc}` placeholder of a fact's templates, keyed by section, label and its position in the
    template that carries it;
  - each `utc` entry of a table keyed by row kind, one slot per kind, keyed by section, table and kind,
    which is the Timeline events table;
  - each `utc` column of any other table, keyed by section and table. Where that table also carries a
    column whose class is a vocabulary named `*-kind`, the slot expands to one per member of that
    vocabulary, which is the Anomalies table through `ANOMALY_KINDS`.

  Nothing in it is a typed list of slots. Observed by AC1.
- **S2** The classes. `OWNER_TIME_CLASSES` in `tools/runlog/record.py` maps every slot key to exactly
  one class, each key with a one-line comment giving its reason:
  - `held` — the slot's row is kept off the record near an owner turn. These are the Timeline `idle`
    row and the `idle-gap` anomaly, held by `derive_idle_gaps` at `IDLE_OWNER_GUARD_S`, and the rows
    and anomalies of `TOOL-dLoggedFlight-15`'s `OWNER_CAUSED_KINDS`, held at `OWNER_ACT_BAND_S`;
  - `derived` — the slot's value is computed from other events, which never supply a held line's time.
    These are the `window` end and the `commitment`'s first and last, under `TOOL-dLoggedFlight-18`,
    and the `elided` fact's two times, which are rendered rows' own cells;
  - `independent` — no owner act sets the slot within a producer's latency. Every other slot is here,
    among them the `window` start, a verb row, and the `rounds` and `sources` times. An agent's act
    that follows an owner turn is the agent's, the trade closing review round 2 recorded as O2.

  Observed by AC2.
- **S3** The class gate arm. A self-test arm requires every slot `scan_time_slots(RECORD_SCHEMA)`
  returns to be keyed in `OWNER_TIME_CLASSES` exactly once, and every key to name a slot it returns.
  It also requires the kinds of the `held` slots to equal `OWNER_CAUSED_KINDS` together with `idle` and
  `idle-gap`, in both directions. Before the arm lands, its failing case is observed twice. A schema
  copy with one added `{utc}` fact label reds as an unclassed slot. A copy with the `rounds` table's
  `utc` column removed reds as a dead key. Observed by AC2 and AC3.
- **S4** The whole-record band arm. It renders a non-terminal fixture through `render_record`, with
  the commitment `measure_commitment` makes from the fixture's journals. The fixture holds an
  interrupt owner turn, an unclean END 10 ms later, a `verdict=NONE` gate line as the run's last event,
  and a manual compaction 100 s after the turn. Every other event lies outside `OWNER_ACT_BAND_S` of
  the turn. The arm scans every UTC token of the markdown and of its Data twin, with no list of rows or
  facts to consult. It asserts that none lies within `OWNER_ACT_BAND_S` of the turn, and that the scan
  found at least one token outside the band. It is observed RED three times: with
  `TOOL-dLoggedFlight-18`'s `shown_end` reverted, with its commitment rule reverted, and with
  `TOOL-dLoggedFlight-15`'s held rows rendered. Observed by AC4.

## 3. Non-goals (OUT)

- The hold predicates themselves. `TOOL-dLoggedFlight-8` S6, and units 15, 17 and 18, own them.
- A band on `independent` slots. Round 2's O2 recorded why that trades a leak for evidence loss.
- The committed record's schema. This unit reads `RECORD_SCHEMA` and changes no template, column or
  vocabulary.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-8` — `derive_idle_gaps`, which holds the idle slots.
- **consumes-from** `TOOL-dLoggedFlight-9` — `RECORD_SCHEMA` and `render_record`, the population and
  the render the arms read.
- **consumes-from** `TOOL-dLoggedFlight-15` — `OWNER_CAUSED_KINDS` and `OWNER_ACT_BAND_S`, the held
  set the gate reconciles and the band the whole-record arm measures.
- **consumes-from** `TOOL-dLoggedFlight-17` — the idle row's refusal at `IDLE_OWNER_GUARD_S`.
- **consumes-from** `TOOL-dLoggedFlight-18` — the derived slots' rule and the commitment the whole-record
  arm renders with.

## 4. Design

Three findings of one audit had one cause: a correct rule applied to fewer slots than the leak runs
through. Unit 15's gate asked "is every row kind classed?" when the question was "is every time the
record carries classed?". The schema already answers the second, because every value it admits
declares its class, and `utc` is one class. So the population is read from the schema's shape, and the
only authored input is the class of each slot. An authored list of slots beside the schema would be a
second answer to the question the schema already owns.

The gate proves every slot has a class, and it cannot prove the class is right. The whole-record arm
covers that half by behaviour: it reads the text a production render writes, the way the refusal
does, so a slot classed `derived` whose derivation still reads a held line reds there. The two arms
are one mechanism. A population with no behavioural arm certifies labels, and a behavioural arm with
no population covers only the slots its fixture happens to exercise.

`derived` is its own class rather than a part of `held`, because its slot is never kept off the record.
Its value is rendered, and what the class promises is that the derivation skips held lines.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `scan_time_slots` | function | `py.function`, led by `scan` |
| `OWNER_TIME_CLASSES` | constant | none |

### Files touched (estimate)

`tools/runlog/{record.py,selftest.py,README.md}` and `memory/map/features/runlog.md`.

### Alternatives rejected

- Enumerate the Timeline's row kinds, unit 15 rev-1's population: rejected by H3.
- A typed list of timed slots beside `RECORD_SCHEMA`: rejected, since it is a second answer to what the
  schema declares, and a slot added to one is invisible to the other.
- The whole-record arm alone: rejected, since it grades only the slots its fixture exercises, and a
  new slot the fixture never fills passes it.

## 5. Production-readiness checklist

- security — a timed slot added to the record schema cannot land without a class, and the classes are
  checked against a production render.
- perf / scale — N/A at runtime; both arms run in the runlog self-test only.
- error / empty / loading states — a slot with no class and a key naming no slot each red, naming the
  key.
- observability — the arm's refusal names the unclassed slot or the dead key.
- risks — a slot classed `independent` wrongly passes the gate; the whole-record arm catches it only
  where its fixture fills that slot in band.
- testing — S3's two staged schema copies and S4's three staged reverts.
- migration — none.
- user docs — the kit README's record section gains the class table's reading rule.

## 6. Acceptance criteria

- **AC1** — When `scan_time_slots` reads `RECORD_SCHEMA`, its slots before the `*-kind` expansion
  number exactly as many as a plain count of `{utc}` placeholders across fact templates and `utc`
  entries across column tuples. After the expansion, the Anomalies slot contributes one slot per member
  of `ANOMALY_KINDS`. The result holds the `window`, `commitment` and `elided` slots, one Timeline slot
  per member of `TIMELINE_EVENTS`, and the `rounds` and `sources` slots.
  Red when: a named slot is missing, or either count differs.
  figure: DERIVED — both counts are computed from the schema at observation time, never typed.
- **AC2** — When the class gate arm reads `OWNER_TIME_CLASSES`, every slot is keyed exactly once,
  every key names a returned slot, and the `held` slots' kinds equal `OWNER_CAUSED_KINDS` with `idle`
  and `idle-gap`.
  Red when: a slot is unkeyed or keyed twice, a key is dead, or the held kinds differ in either
  direction.
- **AC3** — When the class gate arm runs over a copy of `RECORD_SCHEMA` with one added `{utc}` fact
  label, and over a copy with the `rounds` table's `utc` column removed, it reds each time, naming the
  unclassed slot and the dead key.
  Red when: either copy passes.
- **AC4** — When the whole-record band arm renders its fixture with a real commitment, no UTC token in
  the markdown or its Data twin lies within `OWNER_ACT_BAND_S` of the turn, and at least one token lies
  outside it.
  Red when: a token lies within the band, or no token was scanned; observed RED with
  `TOOL-dLoggedFlight-18`'s `shown_end` reverted, with its commitment rule reverted, and with
  `TOOL-dLoggedFlight-15`'s held rows rendered.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · staged schema copies and staged reverts · floor raised by the arm count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, promoted from H3 of the spec audit of units 14 and 15, round 1,
  at the loop's BOUNDED exit. It takes `TOOL-dLoggedFlight-15` S5 and AC5, and the whole-record band
  arm that audit gave as the left-shift of H1 and H2.

## 10. Reuse audit

The seam is `RECORD_SCHEMA` in `tools/runlog/record.py`, whose declared classes are the population,
and `derive_table` and `derive_fact_templates` beside it, which already read the schema by section.
`tools/codebase-map/reuse_lookup.py "classify every time slot a rendered record carries against owner
acts"` returned `render_record`, `build_record_doc` and `build_record_parts` among this build's
candidates, and no candidate enumerates a schema's slots by class. `UTC_TOKEN_RE`, which
`scan_owner_times` already uses, is the whole-record arm's token reader. The recall query returned
only this build's own records.

Recall terms used: owner turn idle gap held near_owner refusal commitment verify window end stale extract coverage transcripts
