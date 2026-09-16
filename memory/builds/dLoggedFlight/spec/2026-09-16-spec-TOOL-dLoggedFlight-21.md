# TOOL-dLoggedFlight-21 — the commitment is a digest and a line count, and `verify` recomputes it from the time-ordered prefix of the run's journal lines

**Status:** SPECCED · rev-2 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling · order 21

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md) | journal | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 |
| [2026-09-16-review-TOOL-dLoggedFlight-21-spec-audit-round1.md](../reviews/2026-09-16-review-TOOL-dLoggedFlight-21-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dLoggedFlight-20` at rev-1 rendered the commitment as its digest and line count, never a line's
time, and named nothing that reads the two fields it dropped. `COMMITMENT_RE`
(`tools/runlog/record.py:115`) requires `first (\S+) · last (\S+)` after the count. `check_commitment`
(`record.py:993`) refuses a line that does not fullmatch it, then passes `first` to
`measure_commitment` as the floor it recomputes from (`record.py:1035`, the floor at `:961-964`) and
compares all four fields (`:1036`). Every record rendered after unit 20 would therefore fail `verify`
with exit 2, and `test_record_ac5_verify` would red. The spec audit of units 14, 16 and 20, round 1,
confirmed this as B1, a BLOCKER, and the loop promoted it here.

Redefine the commitment and `verify` together. The committed line carries the digest and the line
count only. `verify` hashes the first that-many of the run's journal lines in time order, with no
floor. `TOOL-dLoggedFlight-9` S5's "first and last timestamps" clause, and the commitment shape its
AC5 arm asserts, are superseded here by name.

Every code line cited here was read at `ba3bd9fd` on the run branch. The `base` above is the
default-branch sha the format asks for, and `tools/runlog` does not exist there yet.

## 2. Scope (IN)

- **S1** The template. The Summary `commitment` fact's templates in `RECORD_SCHEMA`
  (`record.py:199`) become `none` and `sha256 {digest} · lines {int}`. `COMMITMENT_RE` becomes
  `sha256 ([0-9a-f]{64}) · lines ([0-9]+)`. `build_summary_facts` (`record.py:661-668`) renders the
  two fields and reads no time from the commitment. Observed by AC1.
- **S2** The measure. `measure_commitment(model, journal_root, count=None)` returns `sha256` and
  `lines` and no time. It picks the model's `journal_lines` and sorts them by time, producer rank and
  line number, as today (`record.py:936-960`). With `count` it keeps the first `count` of them. The
  `first` parameter and the floor filter (`record.py:961-964`) are removed. Observed by AC1 and AC2.
- **S3** Verify. `check_commitment` parses the two fields with `COMMITMENT_RE`, rebuilds the model as
  today, calls `measure_commitment(model, journal_root, count=<committed lines>)`, and compares
  `sha256` and `lines`, naming each field that differs. The `none` path, the check that the markdown and
  Data copies agree, and the exit-2 refusal on a machine holding no journal of the run are unchanged.
  Observed by AC2.
- **S4** The anchor's cases, stated. A journal line written after the render carries a time at or
  after the moment the render read the journal, so it sorts past the committed prefix and changes
  nothing. An edited or deleted hashed line changes the digest. A line the rebuilt model attributes
  whose time precedes a hashed line shifts the prefix and reads `mismatch`, whether it was inserted into
  the journal later or is attributed at verify and was not at render. The last case is
  `TOOL-dLoggedFlight-18` S5's line earlier than the old floor. Under this anchor it is an insertion
  into the hashed prefix, and it is reported, never absorbed. Observed by AC2.
- **S5** The pair arm. `record.py` declares `TEMPLATE_PARSERS`, a map from each Summary fact label
  whose value a parser in this kit reads back to that parser. `commitment` to `COMMITMENT_RE` is its one
  entry today. One self-test arm renders the class model's record, parses each mapped fact's rendered
  value with its parser in both the markdown and the Data twin, and reds naming the label the parser
  cannot fullmatch. Observed by AC3.
- **S6** The docs. The commitment paragraph of `tools/runlog/README.md` (`tools/runlog/README.md:313-318`), its
  residue bullet "A line inserted before the committed first time" (`tools/runlog/README.md:435-437`), the module
  docstring's commitment paragraph (`tools/runlog/record.py:34-38`) and the map dossier's sentence
  (`memory/map/features/runlog.md:125-127`) state S3 and S4, and none of them names a committed first
  time. Observed by AC4.

## 3. Non-goals (OUT)

- Which journal lines the model attributes to the run. `TOOL-dLoggedFlight-8` owns `journal_lines`,
  and this unit reads it unchanged.
- Every other rendered time. `TOOL-dLoggedFlight-20`, `-22`, `-23` and `-24` own them.
- A committed position as a floor, such as the first hashed line's producer and line number. §4
  records why it lost.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-8` — `build_run_model` and the `journal_lines` it attributes,
  which `verify` rebuilds and hashes.
- **consumes-from** `TOOL-dLoggedFlight-9` — S5's commitment, `measure_commitment`,
  `check_commitment` and the AC5 arm, whose first and last timestamps this unit supersedes.
- **hands-off** `TOOL-dLoggedFlight-20` — its rev-1 S3 commitment clause, which moved here.
- **hands-off** `TOOL-dLoggedFlight-22` — the commitment with no time, which must land before the
  owner-time refusal retires.
- **hands-off** `TOOL-dLoggedFlight-23` — the commitment line, which carries no time token for the
  population arm to grade.

## 4. Design

The floor did one job the count could not. It kept out a line earlier than the render's first hashed
line that the rebuilt model attributes. The README already records that such a line is invisible to
`verify` today. The owner's ruling of 2026-09-16 forbids committing the floor, because it is a journal
time. The count still does what an append needs, since a line written after the render sorts after
every line the render hashed. What remains is the earlier line, and reading it as the insertion it is
serves an integrity check better than absorbing it.

S5 is the left-shift for B1's class. A template and the parser that reads it back were changed in one
spec and not the other. The pair arm makes that disagreement red in code whatever the specs say.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `TEMPLATE_PARSERS` | constant | none |

`COMMITMENT_RE`, `measure_commitment` and `check_commitment` change shape and keep their names.

### Files touched (estimate)

`tools/runlog/{record.py,selftest.py,README.md}` and `memory/map/features/runlog.md`.

### Alternatives rejected

- Keep `first` and `last`, `TOOL-dLoggedFlight-18` §4's position that "`first` is the verify floor":
  rejected by the owner's ruling of 2026-09-16, since both are journal times. S4 answers the floor's
  one job: the earlier line reads `mismatch`, the safe direction for an integrity check.
- Commit the first hashed line's producer and line number as a positional floor: rejected. It is a new
  committed field that restores only the absorbed earlier-line case S4 reports, and the journals are
  shared by every run of the clone, so a line number also counts other runs' lines.
- Drop the commitment: rejected, since `TOOL-dLoggedFlight-9` S5's edit detection keeps its purpose
  with no time in it.
- Coarsen `first` and `last` to a day: rejected by `TOOL-dLoggedFlight-20` §3, since a bucket is still
  a clock time.

## 5. Production-readiness checklist

- security — the last journal time leaves the committed record, and edit detection stays.
- perf / scale — one sort and one slice, as today; no git call is added.
- error / empty / loading states — a run with no journal line still commits `none`; a malformed
  two-field line exits 2 naming the shape, as a malformed four-field line does today.
- observability — a mismatch names the differing field, `sha256` or `lines`.
- risks — a line attributed at verify that precedes a hashed line reads `mismatch`, by S4's design; a
  journal write racing the render's read can do the same.
- testing — each AC staged RED on its fixture; the commitment in every arm is the one
  `measure_commitment` makes, the production shape.
- migration — no run record is committed in this tree, so no four-field line needs reading.
- user docs — the kit README's commitment paragraph and residue list.

## 6. Acceptance criteria

- **AC1** — When `render_record` renders the class model with the commitment `measure_commitment`
  makes, the Summary `commitment` fact reads `sha256` followed by 64 hex characters and `lines` followed
  by the count, in the markdown and in the Data twin, and `COMMITMENT_RE` fullmatches it.
  Red when: the line carries `first`, `last` or any `utc` token, or `COMMITMENT_RE` does not fullmatch
  it.
- **AC2** — When `python <kit>/runlog.py verify` reads the live run's record in the rotation fixture of
  `test_record_ac5_verify`, it exits 0 reading `match` on the untouched journal and on one with the
  run's later lines appended, and 1 naming `sha256` on one with a hashed line edited. With a line of the
  run inserted between two hashed lines by time, it exits 1 naming `mismatch`, and the rebuilt model's
  `journal_lines` holds the inserted line. The arm's commitment-shape assertion (`selftest.py:4433`)
  ends at the count.
  Red when: an append reads `mismatch`, an edit or the insertion reads `match`, or a well-formed
  two-field record exits 2 as not the schema's shape.
- **AC3** — When the pair arm reads `TEMPLATE_PARSERS`, every mapped fact renders and parses in both
  copies. On a copy of `RECORD_SCHEMA` whose `commitment` template gains a third field while
  `COMMITMENT_RE` is left, it reds naming `commitment`.
  Red when: the staged copy passes, or `TEMPLATE_PARSERS` is empty.
- **AC4** — When `grep -n "committed first" tools/runlog/README.md tools/runlog/record.py memory/map/features/runlog.md`
  runs, it finds nothing, and the README's commitment paragraph names the time-ordered prefix.
  Red when: any file still describes a committed first time.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · AC2's inserted line and AC3's widened template, each staged on a copy · floor raised by the arm count

## 8. Open questions

- **F1** What anchors `verify`'s recompute once `first` leaves the commitment? Options: the time-ordered
  prefix of `count` lines with no floor; a committed positional floor; dropping the commitment.
  RESOLVED (agent, 2026-09-16, delegated): the time-ordered prefix. It is the only option that commits
  no time and no new field and still detects an edit, a deletion and an insertion. §4 records why the
  other two lost.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, promoted from B1 of the spec audit of units 14, 16 and 20,
  round 1, at the loop's BOUNDED exit. It takes `TOOL-dLoggedFlight-20` rev-1 S3's commitment clause
  and supersedes `TOOL-dLoggedFlight-9` S5's first and last timestamps and its AC5 arm's commitment
  shape.
- rev-2 · 2026-09-16 · S6 · the three code citations name their kit path, so the spec-token checker
  reads `tools/runlog/README.md` and `tools/runlog/record.py` rather than the root README. Spelling
  only, made in the main loop while the spec audit of units 21 to 24 read rev-1; no design moved.

## 10. Reuse audit

The seams are `measure_commitment`, `check_commitment`, `COMMITMENT_RE` and `RECORD_SCHEMA` in
`tools/runlog/record.py`, all this build's. `tools/codebase-map/reuse_lookup.py "recompute an
integrity digest over a counted prefix of journal lines"` returned name-stem candidates only: this
kit's `read_journal`, `parse_line` and `render_line`, and memory-recall's `alias_digest`. None hashes a
prefix, so the change stays inside `measure_commitment`. The recall query returned this build's own
records, unit 9 S5, unit 18 S4 and the map dossier's commitment sentence, which S6 rewrites.

Recall terms used: commitment verify floor first last journal lines sha256 count record schema template owner time
