# TOOL-dUnstuckLanding-15 — drift-audit reports ABORTED run records whose work landed anyway

**Status:** INPROGRESS · rev-1 · 2026-10-04 · node d · Tier-2 · base 98926870 · streams tooling · order 3 · closes TOOL-dUnstuckLanding-5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md) | journal | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md) | journal | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 |

<!-- /gen:spec-records -->

## 1. Goal

Unit 14's `--settle` writes `work-landed-at` onto a legacy ABORTED record whose work the content
predicate reads landed. Nothing yet reports the records still waiting for that write, or the later
ABORTED records whose work landed although ABORTED had come to mean discard. Add two report-only
drift-audit signals that read both populations from tracked bytes. Their liveness is drawn from the
population the predicate acts on, so a predicate that cannot say no reads DEAD PROBE and never a clean
zero.

## 2. Scope (IN)

- **S1 — the population and its dating.** A new reader in `tools/drift-audit/drift_report.py` takes
  every tracked run-state file at HEAD whose `phase:` fact reads `ABORTED`. That covers the live
  `RUN.md` and every rotated `RUN.<phase>.<blob8>.md`, the two globs the sibling signal
  `run_records_nonterminal_but_merged` already reads. It reuses that signal's single `ls-tree` and its
  held-open `cat-file --batch`. Each record is dated by the kit library's "first committed" rule, the
  rule `read_first_commit_date` in `tools/unattended/lib-unattended.sh` implements: the oldest add along
  `--follow`, floored for a live `RUN.md` at the newest first touch of an archived sibling in the same
  folder. A record dated before `HANDOFF_CUTOFF` is LEGACY, and one dated on or after it is POST-CUTOFF.
  `HANDOFF_CUTOFF` is read from `.unattended.conf` as committed at HEAD, through the engine's own conf
  parser. Observed by AC3, AC5 and AC8.
- **S2 — the content predicate, consumed and never redefined.** Each ABORTED record is judged by the
  three clauses of `check_work_landed`, the library function unit 14 owns, with the engine's base ref
  standing for unit 14's advertised tip: (i) the witness is not an ancestor of the record's `base`, and
  `base..witness` holds at least one commit attributable to the run, by its slug in the subject or by a
  path under its own build folder; (ii) every attributable commit is an ancestor of the base ref;
  (iii) no commit in `rev-list --first-parent <base ref> ^<witness>` carries a
  `This reverts commit <sha>` line naming one of them. The verdict is `landed`, or `not-landed` naming
  the first clause that failed, or `unjudgeable` with a reason wherever unit 14's function returns
  undecidable. The pure verdict half is a Python function of gathered facts, also named
  `check_work_landed`, so it can be run over controls with no git call. Observed by AC3, AC4 and AC8.
- **S3 — two signals over one read.** `aborted_work_landed` counts LIVE LEGACY records, each a build's
  `RUN.md`, whose verdict is `landed` and which carry no upheld `work-landed-at`. A fact is UPHELD when
  its first field names the record's own witness and the predicate reads `landed` today. A rotated
  archive is listed with its verdict and is not counted, because `--settle` never edits an archive
  (unit 14's F1), and a count no verb can lower would never reach zero. `discarded_work_landed` counts
  POST-CUTOFF records, live and archived, whose verdict is `landed`, whatever facts they carry, because
  no verb clears that class. Each signal's `of` is the population it counts from. The read runs once
  per report and both builders take its result. Observed by AC3, AC5 and AC11.
- **S4 — report-only.** Both signals carry `gateable: False`, so `--check` and `--offenders` never red
  on them. Observed by AC2.
- **S5 — liveness from the population.** A module constant holds four CONTROL fact sets, each shaped
  like a member of the ABORTED population: a witness equal to its base, a foreign witness whose
  `base..witness` holds no attributable commit, attributable work merged and then reverted, and
  attributable work merged and not reverted. Every report runs the verdict half over them first. The
  first three must read `not-landed` and the fourth `landed`. Any other reading makes both signals
  DEAD, with a note naming the control. A signal is live only when its dated population is non-empty
  and every control reads as stated. A repo with no tracked run record and no `.unattended.conf` reads
  NOT ASKED. A blank `HANDOFF_CUTOFF` reads every ABORTED record as LEGACY, and `discarded_work_landed`
  then reads NOT ASKED, naming the blank key. `aborted_work_landed` still counts under a blank key,
  because the record still contradicts git. Its detail then carries a note that `--settle` refuses every
  ABORTED record until the key is dated, which is unit 14's F2. Observed by AC5, AC6 and AC7.
- **S6 — the detail rows.** One row per ABORTED record:
  `<record> <halt-code> <witness8> <first-commit date> <legacy|post-cutoff> <verdict>`. The verdict
  field is one of `landed`, `landed (archived)`, `settled`, `fact-not-upheld`,
  `not-landed (i|ii|iii)` or `unjudgeable — <reason>`. `fact-not-upheld` is shown and not counted, because hygiene check 15
  grades that fact and unit 14 owns that arm. Observed by AC3.
- **S7 — the cost.** Four git calls shared by both signals, whatever the population: the `ls-tree`
  and the `cat-file --batch` above, one `rev-list --parents` of the base ref, and one first-parent
  `log --grep` of the base ref for revert lines. Per ABORTED record, at most two more: one `log` of
  `base..witness` with subjects and paths, and one `--follow` dating walk. A live `RUN.md` adds one
  more per archived sibling, for the floor. A revert line naming an attributable commit is excluded
  when it is an ancestor of the witness, read from the parent graph when the witness is on the base
  ref and by one `merge-base --is-ancestor` otherwise. That call happens only for such a revert, so it
  is zero in the common case. Nothing scales with the length of history. Observed by AC9.
- **S8 — the project layer and the docs.** Gov's `tools/drift-audit/drift_signals.py` pins
  `aborted_work_landed` at the value AC1 measures, so the table reads `ok` at that value. The kit's
  `tools/drift-audit/drift_signals.template.py` carries both names as commented example pins, with the
  instruction to seed at the measured value. The kit README's signal table gains both rows. Observed
  by AC1 and AC10.
- **S9 — parity with the driver.** A self-test arm sources the unattended kit's library where it is
  present, by the path the arm derives from its own kit directory, as `test_park_sets_match_the_driver`
  already does. Over the same fixture records, the library's content predicate and its first-commit
  dating must agree with this engine's in both directions. Where the library is absent, the arm prints
  its skip. Observed by AC8.

## 3. Non-goals (OUT)

- Writing any record. `--settle` is unit 14's writer, and this unit only reads.
- Gating either signal. A post-cutoff landed discard has no verb that clears it, so a gate on it would
  be a permanent red. That is the class unit 16 removes, and this unit must not add a new member.
- Redefining the predicate. A disagreement between this engine and the driver is a red parity arm,
  and the fix lands in whichever implementation contradicts unit 14's spec.
- Non-terminal records that `--settle` marks `abandoned`. They stay in the sibling signal
  `run_records_nonterminal_but_merged`, which counts them still. Teaching that signal to read the
  `abandoned` marker is a follow-up for the owner. It is reported in this unit's return and not
  built here.
- Reading inCMS or NicoCares. The engine reads one repository, and ask 11 carries the kit there.
- The drift-audit kit version and its "Migrating" paragraph. The orchestrator bumps once, at
  VERIFYING.

### Edges

- **consumes-from** `TOOL-dUnstuckLanding-14` — `check_work_landed`, the `work-landed-at` fact's shape,
  and the rule that `--settle` reaches no archive. Without them, S2 has no owner, S3 has no clearing
  verb, and S9's parity arm has nothing to compare against.
- **consumes-from** `TOOL-dUnstuckLanding-13` — the `HANDOFF_CUTOFF` key in `.unattended.conf`. Without
  it, every record reads LEGACY and `discarded_work_landed` reads NOT ASKED.
- **hands-off** external — the drift-audit version move and its README "Migrating" paragraph, to the
  orchestrator at VERIFYING.

## 4. Design

### Data model

Each signal returns the engine's usual shape:
`{signal, value, of, tolerance: 0, gateable: False, live, unjudgeable, detail: [...]}`.
`not_asked: True` marks the NOT ASKED cases in S5, as `_build_not_asked` already does. A DEAD return
carries a first detail row beginning `DEAD PROBE — `, naming the control or the empty population.

The gathered facts per record, which the verdict half reads and nothing else:

| fact | meaning |
|---|---|
| `witness_is_base_ancestor` | the witness equals the base or is an ancestor of it |
| `attributable` | the commits of `base..witness` that name the slug or touch the build folder |
| `on_base_ref` | the subset of `attributable` reachable from the base ref |
| `reverted` | the subset of `attributable` named by a revert line on the first-parent line |
| `why_unjudgeable` | empty, or the reason clause (i) could not be decided |

### The shared read

`read_aborted_verdicts(ctx)` runs the reads S7 counts and caches its result on the context, so the two
builders cost one read. The base ref's parent graph places a witness against its base without a call
per record, as `_check_run_ancestor` does. A base the base ref does not reach is `unjudgeable`, the
sibling signal's rule. The revert set comes from one `log --first-parent --grep='This reverts commit'`
over the base ref, parsed for every named sha.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `build_aborted_work_landed` · `build_discarded_work_landed` | functions | `py.function`, led by `build` |
| `read_aborted_verdicts` · `read_first_commit_date` | functions | `py.function`, led by `read` |
| `check_work_landed` | function | `py.function`, led by `check` |
| `parse_conf_text` | function, extracted from `load_conf` | `py.function`, led by `parse` |
| `_WORK_LANDED_CONTROLS` | module constant | not graded |
| `test_aborted_work_landed` · `test_work_landed_matches_the_driver` | self-test arms | `py.function`, led by `test` |
| `aborted_work_landed` · `discarded_work_landed` | signal names | the drift-audit registry |

`parse_conf_text` is the body of `load_conf` with the file read lifted out. `load_conf` calls it, so the
existing bash-parity arm `test_conf_parser_matches_bash` keeps grading the one parser that both
callers use.

### Known limits

- The revert clause reads the first-parent line only, as design §2 states. A revert that lands on a
  side branch and merges in is not seen, so such work reads `landed`. The clause is unit 14's, and
  this limit is reported to that unit's builder rather than fixed here.
- The engine's base ref is the remote-tracking ref, not a fresh `ls-remote`. A report run on a stale
  clone judges against what that clone last fetched, and its header prints that ref and its sha.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/drift_signals.py`
- `tools/drift-audit/drift_signals.template.py`
- `tools/drift-audit/README.md`
- `memory/map/generated/symbols.json`, re-rendered because the symbol index lists the new functions

### Alternatives rejected

- **The implementation in the project layer**, as the design's owes list words it. The engine owns
  every signal implementation, and the template's own header says so. The project file is a `seed`
  in the kit descriptor, copied once at adoption, so a signal living there never reaches an existing
  adopter. The project layer keeps what is repo-shaped: the pin.
- **Shelling out to the driver's predicate.** It would name a sibling kit's file by literal inside a
  shipped engine file, which the kit-literal ban refuses. It would also make the report need bash
  where the drift kit runs without the unattended kit.
- **One signal with two sub-classes.** The two classes differ in remedy: one clears by `--settle`, the
  other by nothing. Two values let each carry its own pin.
- **Liveness from a free-standing sha.** That is the `liveness-negative-from-another-population`
  class. The controls are record-shaped, and the self-test feeds real fixture records.

## 5. Production-readiness checklist

- security — N/A. It reads tracked files and the object store, and writes nothing.
- perf / scale — S7. Four shared calls, at most two per ABORTED record, plus the floor's per-sibling
  call. Gov holds twelve ABORTED records at this unit's base.
- error / empty / loading states — S5's NOT ASKED and DEAD forms, and S6's `unjudgeable` reasons. A
  failed `cat-file` or `rev-list` reads DEAD with the stage named, never a clean zero.
- observability — S6's detail rows, which print each record's dating class and verdict.
- risks — the parity arm is the only thing holding two implementations of one predicate together.
  If the library is absent the arm skips, and it says so.
- testing — `test_aborted_work_landed` and `test_work_landed_matches_the_driver`, with the fixtures AC3
  to AC9 name. The executed-check floor `CHECK_FLOOR` in `tools/drift-audit/selftest.py` rises by the
  new checks, with its `<old> -> <new>` comment line.
- migration — none. Both signals are additive and report-only.
- user docs — the drift-audit README's signal table.

## 6. Acceptance criteria

Each arm named below runs ALONE: import `tools/drift-audit/selftest.py` and call the one function on an
empty scratch directory, then read the module's `FAILS` list. No criterion runs the whole suite.

- **AC1** — When `python tools/drift-audit/drift_report.py --json` runs on this tree after units 13 and
  14 have landed, both signals are present, `aborted_work_landed` is live with `of` equal to the
  LEGACY ABORTED count, and every detail row carries a verdict. The builder records the value and the
  HEAD sha in this unit's acceptance ledger.
  Red when: either signal is absent, or `aborted_work_landed` reads DEAD over a tree that tracks
  ABORTED records.
  figure: DERIVED at observation; this spec pins no count, because rev-1 of the design counted
  records that reached main rather than work that landed.
- **AC2** — When `python tools/drift-audit/drift_report.py --check` runs on a fixture where both
  signals read non-zero, it exits 0.
  Red when: either signal is gateable.
- **AC3** — When `test_aborted_work_landed` builds a fixture repository holding one LEGACY record per
  negative shape and one positive, the witness-equals-base, foreign-witness and merged-then-reverted
  records each read `not-landed` and are not counted, and the positive is counted once. Adding an upheld
  `work-landed-at` to the positive moves it to `settled`. A `work-landed-at` naming another witness
  leaves it counted. The same fact on a negative record reads `fact-not-upheld` and is not counted.
  The positive record, rotated to an archive name, reads `landed (archived)` and is not counted.
  Red when: a negative shape is counted, a fact that names the wrong witness clears a record, or an
  archive is counted where no verb can clear it.
- **AC4** — When the same arm rebuilds the merged-then-reverted record with its revert commit removed,
  `aborted_work_landed` lists it.
  Red when: the record stays uncounted, which would mean the revert clause never decided it.
- **AC5** — When the arm dates a positive record on or after the fixture's `HANDOFF_CUTOFF`, it is
  counted in `discarded_work_landed` and not in `aborted_work_landed`. An upheld `work-landed-at` on it
  does not clear it. With the fixture's `HANDOFF_CUTOFF` blank, the same record is LEGACY, it is
  counted in `aborted_work_landed` with the note naming the blank key, and `discarded_work_landed`
  reads NOT ASKED.
  Red when: a post-cutoff record is cleared by a fact, or a blank key reads a clean zero.
  fixture: `.unattended.conf` carrying `HANDOFF_CUTOFF`, and records whose first commits fall on both
  sides of it.
- **AC6** — When the arm replaces `_WORK_LANDED_CONTROLS` with four fact sets that each describe landed
  work, both signals read DEAD and the note names the first control that misread. Pointing the positive
  control at reverted work does the same.
  Red when: a control set that cannot read negative, or cannot read positive, leaves either signal
  live.
- **AC7** — When the arm reads a fixture with no run record and no `.unattended.conf`, both signals read
  NOT ASKED. With the conf present and no ABORTED record, both read DEAD, naming the empty population.
  Red when: either empty state prints a clean zero.
- **AC8** — When `test_work_landed_matches_the_driver` runs where `tools/unattended/lib-unattended.sh`
  is present, it sources that file and runs `check_work_landed` and `read_first_commit_date` over AC3's
  and AC5's fixture records, the base ref standing for the tip. Every verdict and every date equals this engine's. A rotated
  archive is dated by its first add and not by the rotation, and a live `RUN.md` is floored at its
  archived sibling. Where the library is absent, the arm prints its skip.
  Red when: one fixture reads differently in the two implementations and the arm stays green.
  fixture: `check_work_landed`, which unit 14 ships in the library.
- **AC9** — When the arm counts git subprocesses during `read_aborted_verdicts` over fixtures of three
  and of six ABORTED records with no archived siblings, the two counts differ by three times the
  per-record constant. Adding fifty unrelated commits to the base ref moves neither count.
  Red when: the read calls git per commit, or per record beyond the two S7 allows.
- **AC10** — When `grep -c "_work_landed" tools/drift-audit/README.md` runs, it finds both signal rows
  in the signal table. `drift_signals.py` pins `aborted_work_landed` at AC1's measured value.
  Red when: a signal ships with no README row, or the pin differs from the measured value.
- **AC11** — When a scratch clone of this repository at AC1's sha runs `--settle` on every slug whose
  live record `aborted_work_landed` lists, and commits what each settle staged, the signal then reads
  0 in that clone, and each formerly counted row reads `settled`.
  Red when: a settled record stays counted, or the value cannot reach 0 because an uncounted class
  leaked into it.
  cost: one `--settle` per listed slug and one commit, in a clone under `%TEMP%`.
  permission: needs unit 14's `--settle`, so it is observed after that unit is built.

## 7. Gates

`drift-audit records` · `drift-audit selftest` · `drift-audit wiring` · `kit version markers` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene` · `kit epoch (shipped bytes move, the version moves)` · `recall floor` · `recall floor arms`

New arm: `tools/drift-audit/selftest.py` `test_aborted_work_landed` · each negative shape, the revert removed, a post-cutoff record, a blank cutoff and a misread control, each staged RED · `CHECK_FLOOR` rises by the arm's executed checks
New arm: `tools/drift-audit/selftest.py` `test_work_landed_matches_the_driver` · a fixture on which the engine's verdict is flipped by hand · `CHECK_FLOOR` rises by the arm's executed checks

## 8. Open questions

- **F1 — where does the signal's code live?** The design's owes list names the kit template and gov's
  project layer, and says the engine only loads it. The engine has no hook that loads a project-layer
  signal, and the template is a `seed`, so an adopter never receives a later change to it. Option (a)
  puts the code in the engine and the pin in the project layer. Option (b) adds a project-layer signal
  hook to the engine and puts the code in the template. Option (c) puts the code in gov's project
  layer alone. RESOLVED (agent, 2026-10-04, delegated): (a). It satisfies every ask criterion, it
  reaches every adopter on the next kit carry, and it follows the precedent of
  `run_records_nonterminal_but_merged`. Option (b) adds a public surface (veto 2), and (c) reaches no
  adopter.
- **F2 — gateable or report-only?** A gate on `discarded_work_landed` would red a bar that no verb can
  clear. A gate on `aborted_work_landed` alone would red when a legacy record's work lands late,
  through nobody's fault. RESOLVED (agent, 2026-10-04, delegated): report-only for both, with gov
  pinning the measured value, the precedent the sibling signal set.
- **F3 — what is live when a dated population is empty?** The kit rule says an empty population is a
  DEAD PROBE. A repo with no post-cutoff abort would then show DEAD on `discarded_work_landed`
  until one happens. RESOLVED (agent, 2026-10-04, delegated): DEAD, with the note naming the empty
  population. The value means nothing until a record exists, and the kit's rule is that a zero which
  means nothing is printed as DEAD. The signal is report-only, so DEAD reds nothing.
- **F4 — how are archived ABORTED records counted?** Unit 14 resolved that `--settle` never edits an
  archive, and handed this question here. (a) Count them in `aborted_work_landed`, which then never
  reaches zero in gov, where four ABORTED records are archived. (b) Leave them out of the population.
  (c) List them with their verdict and count them in neither value, except a post-cutoff archive,
  which `discarded_work_landed` counts because nothing clears that class anyway. RESOLVED (agent,
  2026-10-04, delegated): (c). It keeps every contradiction visible, and it keeps the ask's "zero after
  a `--settle` pass" observable. Option (a) fails that criterion and (b) hides drift.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from design §2 (c3) at rev-2 and ask 5.

## 10. Reuse audit

The seam is `build_nonterminal_merged_runs` in `tools/drift-audit/drift_report.py`, with its record
parser `_parse_run_record`, its ancestry walk `_check_run_ancestor` and the `SIGNALS` registry. This
unit reuses that signal's `ls-tree`, its held-open `cat-file --batch` and its parent-graph walk, and it
extends the record parser to read `halt-code` and `work-landed-at`. The dating rule is
`read_first_commit_date` in `tools/unattended/lib-unattended.sh`, ported rather than called, and held to
it by S9's parity arm. `python tools/codebase-map/reuse_lookup.py "report aborted run records whose
work landed on the default branch"` ranked `build_nonterminal_merged_runs` among its run candidates,
and nothing else that reads a run-state file. Its top seams, `run` and `report`, are self-test
helpers and do not fit. The recall probe's top hits were this build's own ask 5, the design's (c3)
paragraph and the `liveness-negative-from-another-population` gotcha. That gotcha is why S5's controls
are record-shaped.

Recall terms used: ABORTED witness drift-audit signal liveness DEAD PROBE run-state RUN.md landed-derived ancestor base fixture report-only
