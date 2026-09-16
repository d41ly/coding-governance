# TOOL-dLoggedFlight-22 — the journal rows, the time columns and the owner-time refusal retire, with every arm, vocabulary and floor that reads them rewritten by name

**Status:** SPECCED · rev-2 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling · order 23

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md) | journal | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 |
| [2026-09-16-review-TOOL-dLoggedFlight-21-spec-audit-round1.md](../reviews/2026-09-16-review-TOOL-dLoggedFlight-21-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dLoggedFlight-20` at rev-1 stopped rendering the journal and transcript rows of the Timeline
(S2), removed the Anomalies and Coverage time columns (S4) and deleted `scan_owner_times` (S5). It
named none of the arms that read those things. `test_record_ac10_unknown_counts` asserts a `--close`
verb row's `rc` cell, and `TOOL-dLoggedFlight-16` AC4 requires that arm to pass unedited.
`test_record_ac9_owner_times` calls `scan_owner_times`. `test_record_ac4_classes` and
`test_schema_ac1_render_then_grade` require every `gate-verdict` and `push-decision` member in the
rendered cells, which only the retired row layouts carry. Unit 16 AC4 and unit 20 AC2 were owed to the
same bar run and could not both pass. The spec audit of units 14, 16 and 20, round 1, confirmed this as
B2, a BLOCKER, and the loop promoted it here.

This unit performs the three retirements, and in the same unit rewrites or retires every reader they
break, each named with its replacement. It re-declares the assertion floor with a reason, and it
restates unit 16's pin so that "unedited" covers only the half of the AC10 arm this unit leaves.

Every code line cited here was read at `ba3bd9fd` on the run branch. The `base` above is the
default-branch sha the format asks for, and `tools/runlog` does not exist there yet.

## 2. Scope (IN)

- **S1** The rows. The Timeline row layouts in `RECORD_SCHEMA` (`tools/runlog/record.py:208-222`) keep
  `phase`, `commit`, `merge`, `dispatch` and `brief`, whose times come from git or the run-state file.
  `verb`, `push`, `push-refused`, `gate`, `compact`, `limit`, `idle` and `workflow` leave the layouts
  and `TIMELINE_EVENTS` (`record.py:103`), and join a new constant, `RETIRED_EVENTS`.
  `build_timeline_rows` (`record.py:524-536`) drops an event of a retired kind before a row is built
  and counts it. The Timeline gains the fact `withheld rows`, whose template reads each member of
  `RETIRED_EVENTS` followed by its count. `derive_timeline_values` loses the retired kinds' branches,
  and `derive_clean_rc` (`record.py:488-492`), whose only callers were the `verb` and `push` branches,
  retires. The `events` fact counts kept rows, and the `elided` fact's times are read from the kept rows
  it omits (`record.py:707-711`). Observed by AC1.
- **S2** The columns. The Anomalies `anomalies` table drops its `UTC` column (`record.py:268`) and the
  Coverage `sources` table drops its `epoch` column (`record.py:285`). `build_anomaly_rows` and
  `build_coverage_rows` (`record.py:587-604`) stop reading `t` and `epoch`. Both tables still lead each
  row with its ordinal, and the model keeps both values. Observed by AC2.
- **S3** The refusal. `scan_owner_times`, `UTC_TOKEN_RE` and `TWIN_ROW_RE` (`record.py:304-309` and
  `:830-875`) are removed, with the refusal branch of `render_record` (`record.py:890-896`). The prose
  that describes the refusal goes with them: the module docstring's paragraph and clause
  (`record.py:28-32` and `:47-48`), the README's "No time in an owner turn's second" paragraph
  (`tools/runlog/README.md:285-291`) and the map dossier's bullet
  (`memory/map/features/runlog.md:217-220`). It retires in this unit and not earlier: by this step
  `TOOL-dLoggedFlight-21` and `-24` have taken the commitment's and the Summary window's journal times
  out, and S1 and S2 take the rest. The gotcha that describes the refusal,
  `memory/gotchas/withheld-value-recovered-from-a-derived-one.md`, is `TOOL-dLoggedFlight-20` S9's to
  rewrite, a later step. Observed by AC3.
- **S4** The vocabularies and classes no render reaches. `RECORD_SCHEMA["vocab"]` drops `gate-verdict`
  and `push-decision`, and its `event` vocabulary becomes the kept kinds. `RECORD_SCHEMA["shaped"]`
  drops `verb`, `checks` and `label`, whose only slots were the retired layouts. The constants
  `GATE_VERDICTS` and `PUSH_DECISIONS` (`record.py:95-100`) retire with them. The comment on
  `RECORD_SCHEMA["forbidden"]` (`record.py:291-296`) keeps its reason, and names a path class's file
  segment as the class that admits a lowercase UUID in place of `label`. Observed by AC4.
- **S5** The readers. Each arm of `tools/runlog/selftest.py` that reads what S1 to S4 retire changes as
  the table below says. Observed by AC5.

  | arm or builder | what it reads that retires | after this unit |
  |---|---|---|
  | `build_class_model` (`:4221`) | appended `push`, `push-refused`, `gate`, `idle`, `workflow`, `compact`, `limit` and `verb` events, to reach every vocabulary member | appends the kept kinds, plus one event of each retired kind so the `withheld rows` fact counts one of each |
  | `test_record_ac4_classes` (`:4289`) | a typed vocabulary list (`:4297-4300`) and a shaped-value map naming `verb`, `checks`, `label` and an idle row's `960s` (`:4302-4305`) | both lists are read from `RECORD_SCHEMA["vocab"]` and `RECORD_SCHEMA["shaped"]`, never typed, so a vocabulary or class no render reaches reds; the `duration` value is the Summary's |
  | `test_schema_ac1_render_then_grade` (`:4822`) | a typed vocabulary list (`:4837-4842`), and a workflow label as the UUID carrier of `TOOL-dLoggedFlight-10` S5 (`:4843-4865`) | the list is read from `RECORD_SCHEMA["vocab"]`; the UUID rides a ledger entry `ref` whose file segment is a lowercase UUID, which the `ref` class admits |
  | `test_schema_ac2_refusals` (`:4866`) | a driver `verb` row carrying the `cell` variant, and a `workflow` row carrying the `uuid` and `data escape` variants (`:4883-4893`) | the `cell` variant rides a kept `commit` row; `uuid` and `data escape` ride the ledger entry `ref` above; the rule set it stages is unchanged |
  | `build_big_model` for `test_record_ac6_cap` (`:4335`, `:4375`) | 500 rows seeded from every non-owner event, journal kinds included, widened through `verb` names and `workflow` labels | seeds kept kinds only, so the `500 · shown 60 · elided 440` fact still holds; widens the `commit` rows' units cell until the widest record's overflow at the nominal bounds (`:4404-4411`) is still observed |
  | `test_record_model_fields` (`:4491`) | the rendered workflow row and the anomaly's rendered time (`:4526-4532`) | the model-side assertions (`:4515-4525`) stand; the render assertion reads `workflow 1` in `withheld rows` and an `out-of-band-edit` anomaly row with no time |
  | `test_record_copied_sets` (`:4534`) | `PUSH_DECISIONS` against the pre-push hook (`:4544-4551`) | that half retires with the constant; the status-token and verdict halves stand |
  | `test_record_ac9_owner_times` (`:4601`) | `scan_owner_times` and the refusal | retires whole; the model keeping idle gaps away from owner turns stays observed by `test_model_ac19_idle` |
  | `test_record_ac10_unknown_counts` (`:4689`) | its `--close` verb row's `rc` cell (`:4732-4739`) | that loop retires with the verb rows; every count assertion above it stands unedited |
  | `test_record_ac3_shape` (`:4189`) | table rows led by a timestamp | kept `commit` and `phase` rows still lead with one, so it stands unedited; UNVERIFIED until the build runs it |

- **S6** The floor. `ASSERTION_FLOOR` (`selftest.py:114`) is re-declared to the assertion count the suite
  prints once S5 is built. Its comment names this unit and each retired arm or half, in the shape of the
  floor's existing RAISED comments. Observed by AC5.
- **S7** The closed specs. `TOOL-dLoggedFlight-9` gains a rev line recording that S4's journal-sourced
  row layouts and time columns, S4's owner-time refusal with AC9, the `rc` half of AC10, and the members
  of AC4 no render reaches are superseded here. `TOOL-dLoggedFlight-10` gains one recording that its S5
  UUID carrier and its AC1 and AC2 fixture carriers move as S5's table says. `TOOL-dLoggedFlight-16`
  S4 and AC4 are restated at its rev-2, so that "unedited" names the count assertions of
  `test_record_ac10_unknown_counts` only. NOT OBSERVED: these are spec edits made in the disposal that
  promoted this unit, recorded in each spec's revision log, and no build step changes them.

## 3. Non-goals (OUT)

- The local model. It keeps every row, column and time, for the runlog Skill's answers.
- Which sources a slot may declare, and the schema leg's source rule. `TOOL-dLoggedFlight-20` S1 and S7
  own them.
- The whole-render population arm over time tokens. `TOOL-dLoggedFlight-23` owns it.
- Rewriting the gotcha that describes the refusal. `TOOL-dLoggedFlight-20` S9 owns it.
- A gate over specs that retire a name without naming its readers, which the audit's left-shift for B2
  proposed. It would be a new check of `memory/HYGIENE.md`, a governance carrier, so M3's second veto
  makes it the owner's. S5's schema-derived lists are the half this kit can carry.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-9` — the Timeline layouts, the Anomalies and Coverage tables,
  the refusal and the arms of AC4, AC6, AC9 and AC10, which this unit retires or rewrites.
- **consumes-from** `TOOL-dLoggedFlight-10` — the fixture carriers of AC1, AC2 and S5, which move.
- **consumes-from** `TOOL-dLoggedFlight-16` — AC4's pin on the AC10 arm, restated to its counts half.
- **consumes-from** `TOOL-dLoggedFlight-21` — the commitment with no time, which must land before the
  refusal retires.
- **consumes-from** `TOOL-dLoggedFlight-24` — the Summary window with no journal time, which must land
  before the refusal retires.
- **hands-off** `TOOL-dLoggedFlight-20` — its rev-1 S2, S4 and S5, which moved here, and the gotcha
  that still describes the refusal.
- **hands-off** `TOOL-dLoggedFlight-23` — the kept rows and columns whose time tokens the population
  arm grades.

## 4. Design

The retirement and its readers are one mechanism. Retiring a row while leaving the arm that asserts it
is a red suite, and editing the arm in a later unit is the pair of criteria that cannot both pass that
B2 found. So both halves land in one pass, and the table in S5 is the inventory B2 asked for.

The two typed vocabulary lists are the reason this retirement needed an inventory at all. Reading them
from `RECORD_SCHEMA` makes the schema the one list the renderer, the leg and the arms share, so the
next retirement of a vocabulary cannot leave an arm naming its members.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `RETIRED_EVENTS` | constant | none |
| `withheld rows` | Timeline fact label | `RECORD_SCHEMA` fact template |

`scan_owner_times`, `derive_clean_rc`, `UTC_TOKEN_RE`, `TWIN_ROW_RE`, `GATE_VERDICTS` and
`PUSH_DECISIONS` are removed.

### Files touched (estimate)

`tools/runlog/{record.py,selftest.py,README.md}` and `memory/map/features/runlog.md`.

### Alternatives rejected

- Retire the rows in unit 20 and rewrite the arms in a later unit: rejected, since the suite is red
  between the two and unit 16 AC4 fails in the one bar run that observes both.
- Keep `gate-verdict`, `push-decision`, `verb`, `checks` and `label` in the schema with no slot:
  rejected, since a class no render can reach is a schema member no arm can observe, and the derived
  lists of S5 would red on it.
- Keep `scan_owner_times` as a second line of defence: rejected, since every rendered time is then
  public, and a refusal of a public commit time sharing an owner turn's second blocks a record for a
  coincidence, which the README already concedes.

## 5. Production-readiness checklist

- security — no journal or transcript row, column or refusal residue reaches the committed record.
- perf / scale — the render does less; the per-kind count is one counter.
- error / empty / loading states — a run with no retired events renders `withheld rows` with every
  count `0`.
- observability — the `withheld rows` fact says what happened per kind in place of the rows.
- risks — a reader of the committed record loses the journal rows' order; the local model keeps it.
- testing — each AC staged RED on its fixture; S5's rewritten arms are observed passing and each derived
  list observed red on a schema copy.
- migration — no run record is committed in this tree.
- user docs — the kit README's record section.

## 6. Acceptance criteria

- **AC1** — When `render_record` renders `build_class_model`'s model, the Timeline holds only `phase`,
  `commit`, `merge`, `dispatch` and `brief` rows, and the `withheld rows` fact reads a count of 1 for
  each member of `RETIRED_EVENTS`.
  Red when: a row of a retired kind renders, or a retired kind's count is missing or wrong.
- **AC2** — When `render_record` renders the same model, the Anomalies `anomalies` table's header is
  `#`, `kind`, `subclass` and the Coverage `sources` table's header holds no `epoch`.
  Red when: either table carries a time column.
- **AC3** — When `grep -rn "scan_owner_times\|UTC_TOKEN_RE\|TWIN_ROW_RE" tools/runlog memory/map/features/runlog.md`
  runs, it finds nothing, and a render whose commit time falls in an owner turn's second writes its
  record.
  Red when: any name remains, or the render refuses.
- **AC4** — When the rewritten `test_record_ac4_classes` reads a copy of `RECORD_SCHEMA` that keeps
  `push-decision`, it reds naming the unreached members; on the real schema it passes.
  Red when: the copy passes, or the arm's lists are typed.
- **AC5** — When `ASSERTION_FLOOR` in the runlog kit's self-test module is read after S5, its comment names
  `TOOL-dLoggedFlight-22`, the file defines no `test_record_ac9_owner_times`, and each arm in S5's table
  is edited as the table says. The suite run that grades those arms is this spec's `New arm:` line.
  Red when: the floor falls with no comment naming this unit, `test_record_ac9_owner_times` is still
  defined, or an arm still reads a retired row, column, vocabulary or function.

## 7. Gates

`runlog selftest` · `runlog record schema` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · AC1's retired-kind rows and AC4's schema copy keeping `push-decision` · floor re-declared by S6

## 8. Open questions

- **F1** Where does the arm rewrite land, which is B2's fix? Options: a scope item in unit 20 that lists
  the arms; a unit of its own that retires and rewrites together; an edge from unit 16 ordering the
  edit. RESOLVED (agent, 2026-09-16, delegated): a unit of its own taking unit 20's S2, S4 and S5, since
  M4 promotes a BLOCKER to a unit whose mechanism closes it, and one pass is the only shape in which the
  suite is never red between the retirement and its readers.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, promoted from B2 of the spec audit of units 14, 16 and 20,
  round 1, at the loop's BOUNDED exit. It takes `TOOL-dLoggedFlight-20` rev-1 S2, S4 and S5 with their
  AC2, AC4 and AC6, and restates `TOOL-dLoggedFlight-16` AC4's pin.
- rev-2 · 2026-09-16 · AC5 · the spec-token checker refuses a suite run as an acceptance observation.
  AC5 now reads the floor's comment and the file's definitions directly, and the suite stays under
  `New arm:`. Made in the main loop while the spec audit of units 21 to 24 read rev-1; no design moved.

## 10. Reuse audit

The seams are `RECORD_SCHEMA`, `build_timeline_rows`, `build_anomaly_rows`, `build_coverage_rows` and
`render_record` in `tools/runlog/record.py`, and the arms of `tools/runlog/selftest.py`, all this
build's. `tools/codebase-map/reuse_lookup.py "retire a rendered row kind and every test reading it"`
returned name-stem candidates only, `read_text` and `read_journal` among them, and none inventories a
retirement's readers. S5's table was built by a probe over `selftest.py` that listed each arm reading a
retired row kind, the refusal, the commitment or a typed vocabulary, and every row was then read at its
cited line. The recall query returned this build's own records.

Recall terms used: owner turn time leak derived slot sentinel population fixture elided duration utc class gate arm
