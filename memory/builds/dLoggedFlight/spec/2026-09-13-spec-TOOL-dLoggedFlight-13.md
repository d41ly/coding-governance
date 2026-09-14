# TOOL-dLoggedFlight-13 — drift-audit reports run records left non-terminal after their build merged

**Status:** SPECCED · rev-5 · 2026-09-14 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 |
| [2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md](../prompts/2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md) | journal | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 |

<!-- /gen:spec-records -->

## 1. Goal

Six tracked run records say LANDING or BUILDING although their work is on the default branch. So "did
it land?" cannot be answered from the record, and every later run's concurrency report carries them.
Report them from tracked bytes alone, sub-classified by why each stopped, as a drift-audit signal, and
name the one whose witness cannot say.

## 2. Scope (IN)

- **S1** A new signal, `run_records_nonterminal_but_merged`, built by a new function in
  `tools/drift-audit/drift_report.py` and added to its `SIGNALS` registry. The function reads each
  tracked run-state file under the engine's `ctx.memory_root`, at HEAD and never the working tree, and
  takes its `phase:`, `witness:` and `base:` facts. The population is every `RUN.md` and every rotated
  `RUN.<phase>.<blob8>.md` in a build folder, the two globs the driver's own single-live check reads.
  It counts a record as merged when three conditions hold:
  - its phase is not terminal;
  - its witness is an ancestor of the engine's base ref;
  - its witness is neither equal to nor an ancestor of its own recorded `base:`.

  A witness at or behind its base is `unjudgeable`, with the reason `witness not re-written since
  preflight`, counted apart and printed in its detail row. The witness is HEAD at the last verb that
  writes one, and `--close` writes none, so such a record may have built and landed, as dRatifiedSeam
  did. Judging it needs the run's own commits, which three git calls cannot read, and
  `TOOL-dLoggedFlight-8` judges it from them. Observed by AC1 and AC3.

  The witness is read first. A missing witness, one that is not a sha, and one that does not resolve
  are each `unjudgeable` with their own reason. A witness that resolves and is not an ancestor of the
  base ref is not merged, and is neither counted nor unjudgeable. For a merged witness, a missing,
  non-sha or unresolvable `base:` is `unjudgeable`, and so is a base the base ref does not reach,
  since one rev-list cannot relate the witness to a commit outside it. A record with no `phase:` fact
  is `unjudgeable` too.
- **S2** Report-only: `gateable` is false. §4 records why a gate here would red the fleet for a
  landing the owner sanctioned. Observed by AC2.
- **S3** Each counted record gets exactly one sub-class, decided from its own last parked row by this
  table, first match wins. The act of a `rescope` row is the first word of its item field, as the
  driver writes it: `rescope · item <act> <unit>`. Observed by AC3.

  | the record's last parked row | sub-class |
  |---|---|
  | a `rescope` row whose act is `retire` or `supersede` | `retired-unit` |
  | a `decision`, `abort`, `override` or `waiver` row | `surfaced-park` |
  | no parked row at all | `no-rows` |
  | any other row: `review`, `dispatch`, `brief`, `proposal`, or a `rescope` whose act is `add` | `other` |

  A retire or supersede row is matched before the owed-kind rule because it is the more specific cause.
  The refused-landing case cannot be told from tracked bytes, because refusals are not recorded
  there, and the detail row says so. `TOOL-dLoggedFlight-8` cites this table rather than restating it.
  The table's kinds and acts are the driver's `PARK_KINDS_OWED`, `PARK_ACTS_OWED` and `PARK_KINDS`,
  and the terminal set is its `PHASES_TERMINAL`. A row whose kind is outside `PARK_KINDS` is not a
  parked row. An arm of the withheld `tools/drift-audit/selftest.py` extracts all four from the
  driver's source where that file is present and compares both directions, and announces its skip
  where it is not. It reaches the driver by a path derived from its own kit directory, as its siblings
  reach the workflow and recall kits. The carried-prefix predicate does not match that form, so no
  carried row is owed, and the count was taken with the gate's own pattern. Observed by AC6.
- **S4** Each detail row names the record, phase, witness, the witness's relation to its base, and the
  sub-class, so a vacuous case is visible on every run. Liveness: `live` is true when the population
  of run records is non-empty, and `of` is that population. With no run record and no
  `.unattended.conf` at the root the signal is NOT ASKED rather than DEAD, since that repo does not
  adopt what it reads. With the conf and no record it is DEAD. Observed by AC1.
- **S5** Cost: three git calls in total, whatever the record count. They are one `ls-tree -r HEAD`
  over the build folders to enumerate, one `rev-list --parents` of the base ref, and one
  `cat-file --batch` held open for one conversation. That stream returns each record's content by
  the blob id `ls-tree` named at HEAD, then tests each witness and base with `<sha>^{commit}`. The
  witness-to-base test walks the parent graph `rev-list` printed and adds no call, because the set of
  commits alone cannot order two of its members. Observed by AC4.
- **S6** The kit version moves from 1.10 to 1.11 across its carriers, with a self-test arm. Observed
  by AC5.

## 3. Non-goals (OUT)

- Repairing the records. They are the owner's to rule on, and several need `--landed`, which is
  refused for a reason this unit does not reach.
- Reading any machine-local journal. A drift signal must be answerable in a fresh clone.

### Edges

none

## 4. Design

A gate here would red every bar after any worktree landing, and the owner has sanctioned those. As soon
as local `main` moves past such a run's witness, the count would rise above any pin, on every node,
through no one's fault. So the signal reports and does not gate. A report-only signal is still judged
against its pin in the table output, so a rising count is visible. This repo's project layer pins it
at the measured 5, so the table reads `ok` at that value and `over pin` above it. The pin takes no
RATCHETS row: a rise is nobody's fault, as above, so raising it needs no reason.

The engine's base ref is resolved the way every other signal resolves it: `--base-ref`, then
`GOV_DEFAULT_BRANCH`, then the local short name of `refs/remotes/origin/HEAD`. The kit's existing
at-sha reader, `_read_defs_at_sha`, spends an `ls-tree` plus a `cat-file --batch`; this function
follows the same pattern and adds the witness test to the batch rather than a fourth call. The
witnesses are known only once the records are read, so the batch is one process held open: the
record blobs go first, then each `<sha>^{commit}` query. `cat-file` flushes after every object, so
the conversation cannot deadlock on a buffer.

### Real-population measurement

Measured on this tree on 2026-09-13 when rev-4 was written. Seven records are non-terminal at HEAD. Six
of them are merged, each with own commits on `origin/main` after its start commit. Five have a witness
beyond their base and are counted. dRatifiedSeam's witness equals its base, because its run went from
preflight to `--close`, which writes no witness, although its three own commits are merged. So the
signal reports it `unjudgeable`. The seventh is this run, whose witness is not on `origin/main`.
Re-measured at the build pass on 2026-09-14 against local `main`, which the engine resolves here, and
the seven split the same way. The rotated archives join the population and are all terminal.

### Data model

`{signal: "run_records_nonterminal_but_merged", value, of, tolerance: 0, gateable: False, live,
unjudgeable, detail: ["<record> <phase> <witness8> <ahead|equal|behind> <subclass>", ...]}`.

An unjudgeable row puts `unjudgeable — <reason>` where the sub-class goes, and `unknown` for a
relation it could not read. The last detail row is the refused-landing note S3 names.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `build_nonterminal_merged_runs` | function | `py.function`, led by the declared `build` |
| `_parse_run_record` · `_derive_run_subclass` · `_check_run_ancestor` | functions | `py.function`, led by `parse`, `derive` and `check` |
| `test_nonterminal_merged_runs` · `test_park_sets_match_the_driver` · `test_version_carriers_agree` | self-test arms | `py.function`, led by the reserved `test` |
| `run_records_nonterminal_but_merged` | signal name | drift-audit registry |

### Files touched (estimate)

`tools/drift-audit/{drift_report.py,drift_signals.py,drift_signals.template.py,selftest.py,README.md,adopt-drift-audit.sh}`
and the two drift workflow harnesses, which carry the version. No dossier claims a drift-audit key,
so `memory/map/features/` is untouched, and `memory/map/generated/` re-renders because the symbol
index lists the new public functions. No carried-prefix row moves (S3).

### Alternatives rejected

- Gateable with a pin: rejected by §4.
- Subject-grep for merges: rejected. The evidence reviewer measured that a slug appears in unrelated
  merge subjects, and ancestry is exact.
- Two git calls: rejected, since `cat-file --batch-check` returns no content and the records must be
  read at HEAD.

## 5. Production-readiness checklist

- security — N/A; it reads tracked files and the object store.
- perf / scale — three git calls; S5.
- error / empty / loading states — a record with no `phase:`, `witness:` or `base:` is `unjudgeable`
  and counted apart, and so is a witness at or behind its base (S1). An unresolvable or non-sha
  witness is `unjudgeable`, not merged, and so is a merged witness whose base the base ref does not
  reach. A failed `cat-file` or `rev-list` reports DEAD with a note, never a clean 0, and a repo with
  no run record and no `.unattended.conf` is NOT ASKED (S4).
- observability — the detail rows, which print the witness-to-base relation.
- risks — none beyond the report being ignored; it is visible in the table on every run.
- testing — one fixture per table row and per alternative in it, one record with its witness equal
  to its base and one with its witness behind it, and one record per other unjudgeable reason, each
  staged, plus the kit's existing meta-tests that every signal can move and none hard-codes `live`.
  One more arm holds every version carrier the kit owns to the engine's constant (S6).
- migration — none.
- user docs — the drift-audit README's signal table.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py` runs on this tree, the new signal reports a
  value of 5 or more, with `of` equal to the tracked run-record count, and `live` true, and its detail
  rows print each witness's relation to its base. In the self-test, a fixture RUN.md edited in the
  working tree to a non-terminal phase that HEAD does not carry is not counted.
  Red when: the signal reads the working tree rather than HEAD, or matches no record.
  figure: 5 was measured on 2026-09-13; the arm asserts the value against a fixture, not against this
  tree.
- **AC2** — When `python tools/drift-audit/drift_report.py --check` runs on this tree, it exits 0
  whatever the signal's value.
  Red when: the signal is gateable.
- **AC3** — When `python tools/drift-audit/selftest.py` builds fixture records for the S3 table, the
  signal names each with its sub-class. `rescope` retire, supersede and add rows are separate fixtures,
  reading `retired-unit`, `retired-unit` and `other`, and a rescope item whose second word is `retire`
  reads `other`. A record left as preflight and `--close` leave it, witness equal to base, reads
  `unjudgeable` with its reason and is not counted, and so does one whose witness is strictly behind its
  base. A terminal record and an unmerged witness are not counted.
  Red when: a table row or one of its alternatives maps to the wrong sub-class, a stale witness is
  counted, or a terminal record is counted.
- **AC4** — When `tools/drift-audit/selftest.py` counts the git subprocess calls that
  `build_nonterminal_merged_runs` makes over fixture trees of 5 and of 50 records, it counts three for
  both.
  Red when: the function calls git per record.
- **AC5** — When `bash tools/check-kit-versions.sh` runs, drift-audit is green at 1.11, and the
  `drift-audit selftest` leg passes.
  Red when: a carrier still reads 1.10.
- **AC6** — When `python tools/drift-audit/selftest.py` runs where `tools/unattended/unattended.sh` is
  present, the S3 table's kind and act sets equal the driver's `PARK_KINDS_OWED`, `PARK_ACTS_OWED` and
  `PARK_KINDS` in both directions, and the terminal set equals its `PHASES_TERMINAL`. Where the driver
  is absent, the arm prints its skip.
  Red when: the driver gains an owed kind the table lacks and the arm stays green.

## 7. Gates

`drift-audit records` · `drift-audit selftest` · `drift-audit wiring` · `kit version markers` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/drift-audit/selftest.py` · each table row, the base test, the HEAD-not-worktree read and the non-gateable property staged RED · the suite had no assertion floor to raise, so it gains one at its executed-check count, compared only on a run where no arm skipped

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · S1 S5 · §4 · AC1 AC4 · folded round-1 spec audit M12 (three git calls, constant in
  the record count, and an arm whose working tree differs from HEAD).
- rev-3 · 2026-09-13 · S1 S3 S4 S5 · §1 · §4 · AC1 AC3 · folded round-2 spec audit H4 (a witness at or
  behind its recorded base is `no-progress` and uncounted, TOOL-cFinalBerth-2, so the measured value is
  five, not six) and M6 (the sub-classes are a first-match table over the last parked row, with a
  place for `supersede`).
- rev-4 · 2026-09-13 · S1 S3 · §1 · §4 · §5 · AC3 AC6 · folded round-3 spec audit H1 (a witness at or
  behind its base is `unjudgeable`, since `--close` writes none and dRatifiedSeam built and landed), M7
  (each alternative of a table row is its own fixture), M11 (the table's sets are held to the driver's
  source) and M12 (the root is `ctx.memory_root`).
- rev-5 · 2026-09-14 · S1 S3 S4 S5 · §4 · §5 · §7 · AC6 · the build pass, before its code. S5's
  witness-to-base test cannot use the `rev-list` set, which holds no order between two of its members,
  so it walks the `--parents` graph. The batch is one process held open, since the witnesses are read
  from the records it returns. S1 names the rotated archives and every unjudgeable reason. S3 holds
  the terminal set to the driver too, and reaches the driver by a derived path, so no carried row is
  owed. S4 adds NOT ASKED for a repo with no runs and no conf. §4 pins the measured 5 and spells the
  unjudgeable row. §5's testing line still said `no-progress`, rev-3's name for what rev-4 made
  `unjudgeable`, and now names each fixture by reason. §7's suite had no floor to raise.

## 10. Reuse audit

The seam is drift-audit's `SIGNALS` registry at `tools/drift-audit/drift_report.py:1749-1755` and its
`Git` helper, with `_read_defs_at_sha` as the at-sha read pattern. `tools/codebase-map/reuse_lookup.py
"report run records left non-terminal"` returned the drift-audit dossier. No signal reads a run-state
file today, so the reader is new.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
