# TOOL-dLoggedFlight-20 — the committed record carries no time a journal or transcript produced

**Status:** CLOSED · rev-4 · 2026-09-20 · node d · Tier-2 · base 4cf0944d · streams tooling · order 27

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md) | journal | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-26 TOOL-dLoggedFlight-27 TOOL-dLoggedFlight-28 TOOL-dLoggedFlight-29 TOOL-dLoggedFlight-30 |
| [2026-09-16-review-TOOL-dLoggedFlight-20-spec-audit-round1.md](../reviews/2026-09-16-review-TOOL-dLoggedFlight-20-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 |

<!-- /gen:spec-records -->

## 1. Goal

Five review rounds found an owner turn's clock time recoverable from the committed record through a
new derived path each time: an idle gap's end, a stale extract, a killed verb's END, a killed bar's
`NONE` line, a compaction row, the commitment's last line time. Each fold closed the path it was shown,
and the next round found one the rule did not enumerate. The owner ruled on 2026-09-16 that the
committed record carries no time a journal or a transcript produced. Every time it keeps comes from a
source that is already public in git: a commit, or a row of the committed run-state file. Every other
time stays in the machine-local model and the runlog Skill's answers. That closes the class by
construction, and it supersedes `TOOL-dLoggedFlight-15`, `-17`, `-18` and `-19`.

The spec audit of units 14, 16 and 20, round 1, moved four halves of this unit out. The commitment went
to `TOOL-dLoggedFlight-21` (B1). The journal rows, the time columns and the refusal, with every arm that
reads them, went to `TOOL-dLoggedFlight-22` (B2). The population arm went to `TOOL-dLoggedFlight-23` (H1,
H2). The Summary window, its duration and its provenance facts went to `TOOL-dLoggedFlight-24` (H3, with
M1). What this unit still owns is the declaration every time slot's source is read from, the schema
leg's source rule, the Skill's routing and the class record.

## 2. Scope (IN)

- **S1** Declared sources. `RECORD_SCHEMA` in `tools/runlog/record.py` gains `time_classes`, the
  shaped classes that carry a time, `("utc", "duration")`, and `TIME_SOURCES`, `("git", "run-state")`.
  `scan_time_slots(schema)` returns every slot of a class in `time_classes`: each placeholder of a fact
  template, keyed by section, label and position; each Timeline row layout's column, keyed by row kind;
  and each column of any other table, keyed by section, table and header. It holds no typed list of
  slots. `RECORD_SCHEMA["sources"]` maps each such key to the non-empty set of sources its value may
  come from, since the Timeline `elided` fact reads a `commit` row or a `dispatch` row alike. Then
  `check_time_sources` refuses, naming the slot, a key `scan_time_slots` returns with no entry, a source
  outside `TIME_SOURCES`, and an entry keyed to no slot. Observed by AC1.
- **S2** Moved to `TOOL-dLoggedFlight-22` S1. NOT OBSERVED here: that unit's AC1 observes it.
- **S3** Moved. The commitment went to `TOOL-dLoggedFlight-21` S1 to S4, the window and the duration to
  `TOOL-dLoggedFlight-24` S1 and S2, and the two provenance facts on to `TOOL-dLoggedFlight-25` S1. NOT
  OBSERVED here: unit 21's AC1 to AC4, unit 24's AC1 and AC4, and unit 25's AC1, AC2 and AC5 observe it.
- **S4** Moved to `TOOL-dLoggedFlight-22` S2. NOT OBSERVED here: that unit's AC2 observes it.
- **S5** Moved to `TOOL-dLoggedFlight-22` S3. NOT OBSERVED here: that unit's AC3 observes it.
- **S6** Moved to `TOOL-dLoggedFlight-23` S1 to S5. NOT OBSERVED here: that unit's AC1 to AC4 observe
  it.
- **S7** The schema leg. `check-records` refuses, under a rule of its own in `RECORD_RULES` named
  `source`, a committed record whose Timeline row renders a time beside a source `sources` does not
  declare that slot may be filled from, naming the record, the line and that rule. A row that renders
  a time with its source cell `-` is refused too: an unattributed time is the class itself. The rule
  reaches a row that STATES a source; a fact's time and the Decisions `rounds` column state none in
  the record's bytes, and `check_time_sources` is what binds those. The clause about a layout
  carrying a time column `TOOL-dLoggedFlight-22` S2 removed is DISCHARGED, not implemented — rev-4's
  section 9 says by what. Observed by AC5.
- **S8** The Skill. `tools/runlog/SKILL.template.md` says the committed record carries no event times.
  Its question table's row for what a run did between two times reads first from the local `model`
  timeline (`SKILL.template.md:61`). Its `description` (`SKILL.template.md:4-7`) no longer sends a
  question about a time to the committed record first. `.claude/skills/runlog/SKILL.md` is re-rendered
  by `tools/runlog/adopt-runlog.sh --scaffold`. Observed by AC7.
- **S9** The class record. The fix section of
  `memory/gotchas/withheld-value-recovered-from-a-derived-one.md`, which says `tools/runlog/record.py`
  refuses the whole record on an owner-second match (line 46), is rewritten to the source rule: no
  committed time comes from a journal or a transcript, held by `check_time_sources`, `check-records` and
  `TOOL-dLoggedFlight-23`'s population arm. Observed by AC8.

## 3. Non-goals (OUT)

- The local model. It keeps every time it has, for the Skill's answers on this machine.
- Count correctness. `TOOL-dLoggedFlight-14` and `TOOL-dLoggedFlight-16` own which sources the counts
  rest on.
- Coarsening times into buckets. A bucket is still a clock time, and the ruling withholds the source,
  not the precision.
- The commitment, the retired rows and columns with their readers, the population arm, and the Summary
  window block. `TOOL-dLoggedFlight-21`, `-22`, `-23` and `-24` own them.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-8` — the model's timeline, with each event's source.
- **consumes-from** `TOOL-dLoggedFlight-9` — `RECORD_SCHEMA` and the renderer, whose slots S1 declares.
- **consumes-from** `TOOL-dLoggedFlight-10` — the schema leg this unit gives the source rule.
- **consumes-from** `TOOL-dLoggedFlight-12` — the Skill's description and its question table, whose
  time routing S8 changes.
- **consumes-from** `TOOL-dLoggedFlight-14` — the counts the record keeps in place of the times.
- **consumes-from** `TOOL-dLoggedFlight-21` — the commitment with no time, so S1 declares no slot for
  it.
- **consumes-from** `TOOL-dLoggedFlight-22` — the kept rows and columns, so every slot S1 declares has a
  public source.
- **consumes-from** `TOOL-dLoggedFlight-24` — the Summary window and duration, rendered from commit
  times.
- **hands-off** `TOOL-dLoggedFlight-23` — `time_classes`, `TIME_SOURCES` and `scan_time_slots`, which
  the population arm reads.

## 4. Design

The defect class was enumeration: each withholding rule ran over a narrower population than the leak.
This unit changes what is withheld from values to sources. A source either is already public or is not,
and that is decidable per slot, so there is no population to enumerate beyond the schema's own slots,
and `scan_time_slots` reads those from the schema rather than from a list.
`TOOL-dLoggedFlight-23` then checks the rendered text against the same classes and slots, `duration`
included, so a slot that escapes the declaration still fails.

Commit times and run-state row times can sit near an owner turn, because an agent often commits right
after the owner answers. They add nothing a reader cannot already get from `git log` on the public
remote, and that is why they are the kept sources.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `TIME_SOURCES` | constant | none |
| `time_classes` | schema key | `RECORD_SCHEMA` |
| `sources` | schema key | `RECORD_SCHEMA` |
| `scan_time_slots` | function | `py.function`, led by `scan` |
| `check_time_sources` | function | `py.function`, led by `check` |

### Files touched (estimate)

`tools/runlog/{record.py,runlog.py,selftest.py,README.md,SKILL.template.md}`,
`.claude/skills/runlog/SKILL.md`, `memory/gotchas/withheld-value-recovered-from-a-derived-one.md`,
`memory/map/features/runlog.md` and the regenerated map.

### Alternatives rejected

- Continue the per-path holds of `TOOL-dLoggedFlight-15` to `-19`: rejected by the owner's ruling,
  after five rounds in which each audit widened the surface.
- Coarsen every rendered time to a bucket: rejected by §3.
- Drop the Timeline section: rejected, since commits and run-state rows are public and give the record
  its sequence.

## 5. Production-readiness checklist

- security — closes the owner-time class by source, not by path.
- perf / scale — the declaration is read once per check; no git call is added.
- error / empty / loading states — a time slot added with no declared source is refused by name.
- observability — a refusal names the slot and the rule.
- risks — a reader of the committed record loses the order of journal events; the local model keeps it.
- testing — each AC staged RED on its fixture or on a copy of the schema.
- migration — records committed before this unit are re-rendered by their next placement.
- user docs — the kit README's record section, the runlog Skill and the class record.

## 6. Acceptance criteria

- **AC1** — When `check_time_sources` reads `RECORD_SCHEMA`, every key `scan_time_slots` returns has an
  entry whose sources are all in `TIME_SOURCES`, and it refuses nothing. On a copy with `driver` added to
  the Summary `window` slot's sources, and on a copy with the Decisions `rounds` table's `UTC` entry
  removed from `sources`, it refuses naming that slot.
  Red when: either staged copy passes, or a time slot has no entry.
- **AC5** — When `check-records` reads a fixture record carrying a kept `commit` row whose `source` cell
  reads `driver`, it exits 1 naming the record, the line and the source rule. `driver` is a member of the
  `source` vocabulary and `commit` keeps its layout, so no rule but the source rule can refuse that row.
  Red when: the record is accepted, or the refusal names a rule other than the source rule.
- **AC7** — When `grep -n 'no event times' .claude/skills/runlog/SKILL.md` runs, it finds the sentence,
  the question table's between-two-times row names the model's `timeline` as its first source, and the
  description's routing does not put the committed record first for a question about a time.
  Red when: the sentence is absent, the row still names the record's Timeline first, or the description
  still routes a time question to the committed record first; staged RED against the current Skill with
  the sentence added and the row and description left.
- **AC8** — When `grep -n 'refuses the whole record' memory/gotchas/withheld-value-recovered-from-a-derived-one.md`
  runs, it finds nothing, and the fix section names `check_time_sources`.
  Red when: the gotcha still describes the refusal as present.

## 7. Gates

`runlog selftest` · `runlog record schema` · `runlog skill wiring` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arms: `tools/runlog/selftest.py` · AC1's three schema copies and AC7's half-amended Skill, plus
AC5's `source` variant inside the schema leg's own refusal arm · floor raised to 1422 by 18

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, from the owner's ruling of 2026-09-16; supersedes
  `TOOL-dLoggedFlight-15`, `-17`, `-18` and `-19`.
- rev-2 · 2026-09-16 · §1 · §3 · §4 · S1 S2 S3 S4 S5 S6 S8 S9 · AC1 AC2 AC3 AC4 AC6 AC7 AC8 · the
  disposal of the spec audit of units 14, 16 and 20, round 1. Promoted: B1 to `TOOL-dLoggedFlight-21`,
  which takes S3's commitment clause; B2 to `-22`, which takes S2, S4 and S5 with AC2, AC4 and AC6; H1
  and H2 to `-23`, which takes S6 and AC1's sentinel arm; H3 to `-24`, which takes S3's window and
  duration with AC3. S1 now spells `time_classes`, `sources` and `scan_time_slots`, which `-23` reads, so
  AC1 observes the declaration itself. Folded: M1, the provenance facts S3 neither retired nor
  redefined, is decided in `-24` S3 against that unit's window, as the audit asked, since the facts
  describe it. M2: S8 and AC7 re-route the description and the question table as well as adding the
  sentence, with a consumes-from edge to `TOOL-dLoggedFlight-12`. L1: S9 and AC8 rewrite the gotcha's fix
  section, and Files touched names it. The order moves from 20 to 24, so `-21`, `-24` and `-22` land
  first.
- rev-3 · 2026-09-16 · AC5 · S3 · folded M5 of the spec audit of units 21 to 24, round 1, whose subjects did
  not include this unit. `TOOL-dLoggedFlight-22` removes the `verb` layout, and `check_table_row` refuses a
  row whose kind has no layout under rule `cell` before any class check (`tools/runlog/record.py:1141-1145`
  at `f7bf9d2f`), so a verb row could not tell the source rule from that refusal. AC5's fixture is a kept
  `commit` row sourced `driver`, and its Red-when names the rule. The order moves from 24 to 27, after
  `TOOL-dLoggedFlight-25`, `-26` and `-27` are inserted before it. Because this rev moved by a review
  that did not audit this unit, the spec is unreviewed again under BUILD-METHOD M4. S3's pointer names
  where the provenance facts went once `TOOL-dLoggedFlight-25` took them from unit 24.

- rev-4 · 2026-09-20 · S7 · §7 · the build pass, written before the code it changes. THE SECOND
  CLAUSE OF S7 IS DISCHARGED BY WHAT UNITS 22 AND 20 ALREADY LAND, and writing a third rule for it
  would be a second answer to one question. A record whose Anomalies or Coverage table carries a time
  column `TOOL-dLoggedFlight-22` S2 removed does not match any header that section declares, so
  `check_record_lines` refuses it at the header line under `cell` before a row is read
  (`tools/runlog/record.py` at `6f481d31`, the `a table header section … declares no table for`
  branch); and a time column RE-ADDED to the schema is a slot `scan_time_slots` returns with no
  entry, which `check_time_sources` refuses by AC1. This is rev-3's own finding one step on: that rev
  moved AC5's fixture off a `verb` row for the same reason, a retired layout being refused under
  `cell` before any class check. So the source rule is written once, over the Timeline rows that
  state a source, and S7 now says what it does not reach. §7's new-arm line: AC1 stages THREE copies
  of the declaration rather than two, the third an entry keyed to no slot, since the checker refuses
  three things; AC5's arm is a variant inside `test_schema_ac2_refusals`, because that arm holds
  `RECORD_RULES` in both directions and a new rule nobody staged would red it; the floor moves by 18,
  to 1422.

## 10. Reuse audit

The seams are `RECORD_SCHEMA` and `render_record` in `tools/runlog/record.py`, and the schema leg
`check-records` in `tools/runlog/runlog.py`, all this build's.
`tools/codebase-map/reuse_lookup.py "declare a source for every rendered time"` returned name-stem
candidates only. Outside this kit they are codebase-map's `derive_source_paths`, memory-recall's
`extract_declarations` and lexicon's `parse_ts_source`, unrelated name matches, and none declares a
source per rendered time. `scan_time_slots` reuses the slot enumeration `TOOL-dLoggedFlight-19` S1
specified before that unit was superseded, widened from `utc` to every class in `time_classes`.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
