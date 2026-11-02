# TOOL-dCalibratedLens-30 — the round-1 spec audit's 41 minors batched: each correction carried by the sibling it lands on, and six arms that hold the classes no sibling owns

**Status:** OPEN · rev-2 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 18 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-30-deviation-301.md](../build/2026-11-02-build-TOOL-dCalibratedLens-30-deviation-301.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 |
| [2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 1 to 17,
`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`, exited CONVERGED with 52
confirmed findings, and `TOOL-dCalibratedLens-19` to `-29` take its 11 HIGH. This unit is BUILD-METHOD
M4's batch of its 30 MEDIUM and 11 LOW by raw id, one scope item per id, in report order, M1 to M28
and then L1 to L11. They land on every one of the seventeen units, so the batch repairs no unit in
particular and builds last, order 18, above every unit of the build. They do not split into two
disjoint write sets: most corrections and every arm below meet in `tools/loop/loop_review.py` or
`tools/loop/measure.py`, so one unit carries them all.

Every id: M1 5, 32; M2 6; M3 7; M4 8; M5 9; M6 10, 46; M7 17; M8 18; M9 25; M10 26; M11 27; M12 28;
M13 29; M14 30; M15 31; M16 33; M17 37; M18 38; M19 39; M20 40; M21 41; M22 42; M23 43; M24 44; M25
45; M26 51; M27 53; M28 54; L1 11; L2 12; L3 13; L4 14; L5 20; L6 21; L7 22; L8 23; L9 24; L10 34;
L11 47.

Each correction was made at the audit's disposal in the text of the unbuilt sibling it lands on: a
rev-2 of that spec, a bullet `- **id <n> · …**` in its §4 "Amendments (round-1 spec audit)" naming
this unit, the superseded S-item or criterion opening `(amended, id <n>)`, and a §9 line naming this
unit and the review record by its stem. Each sibling then builds the corrected design and observes
it through its own amended criterion. This unit adds what no sibling owns: the six arms of §2's S42
to S47, each the class gate the review's left-shift line names, observed over the built loop kit
once every sibling has landed.

## 2. Scope (IN)

- **S1** — id 5, M1, landing on unit 4. S6 reads each cap's cost in-process from `PROVIDERS["cap"]`,
  unit 15's `derive_cap_rows`, the current period's, and names no reader of the view. Observed by
  AC1.
- **S2** — id 32, M1, landing on unit 4. S4 and S6 take the walk's window, so the cost and the evidence
  are one period's. NOT OBSERVED here — the sibling it lands on observes it through its amended
  criterion; AC1 is a spec-text precondition (round-2 id 3).
- **S3** — id 6, M2, landing on units 4 and 16. `read_cap_evidence`, `derive_cap_readings` and
  `read_journal_lines` take the walk's `(start, end, days)` and read no policy value. Observed by AC2;
  AC1 is a spec-text precondition (round-2 id 3).
- **S4** — id 7, M3, landing on unit 14. A scenario proposal carries `kind`, `id`, `action`, `accept`
  and `row`, and AC6 observes it filed. NOT OBSERVED here — the sibling it lands on observes it
  through its amended criterion; AC1 is a spec-text precondition (round-2 id 3).
- **S5** — id 8, M4, landing on units 13 and 10. Unit 13 withdraws the claim that a brief is cited by
  its tag; unit 10's guard and both-ways check reach `tools/workflows/lenses.toml`. NOT OBSERVED
  here — the sibling it lands on observes it through its amended criterion; AC1 is a spec-text
  precondition (round-2 id 3).
- **S6** — id 9, M5, landing on units 2 and 4. The `cost` grammar admits the unit `B`, and unit 4's AC7
  plants `4433344B/212`. Observed by AC3; AC1 is a spec-text precondition (round-2 id 3).
- **S7** — id 10, M6, landing on unit 15. The previous review is the newest committed
  `*-loop-review-*.md` other than this period's, read through `read_loop_records`, never the newest
  commit touching the folder. Observed by AC4; AC1 is a spec-text precondition (round-2 id 3).
- **S8** — id 46, M6, the same defect raised by a second lens, landing on unit 15, closed by S7's rule.
  Observed by AC4; AC1 is a spec-text precondition (round-2 id 3).
- **S9** — id 17, M7, landing on unit 4. AC2's fixture pins `core.autocrlf=false` and asserts a planted
  blob holds a CR. NOT OBSERVED here — the sibling it lands on observes it through its amended
  criterion; AC1 is a spec-text precondition (round-2 id 3).
- **S10** — id 18, M8, landing on unit 16. The act-ceiling row is hours to two decimals, so a `hold` is
  reachable at the default 1.5. Observed by AC5; AC1 is a spec-text precondition (round-2 id 3).
- **S11** — id 25, M9, landing on unit 3. The walk reads its rows through `loop_lib.read_items` and
  takes `check_program`'s refusals; `read_loop_items` is not minted. NOT OBSERVED here — the sibling
  it lands on observes it through its amended criterion; AC1 is a spec-text precondition (round-2 id
  3).
- **S12** — id 26, M10, landing on units 3 and 2. Unit 3's §8 F5 places the rows against
  TOOL-dTendedCadence-1 F1 and ask TOOL-dTendedCadence-25 and states the ask admitting
  `cadence.loop`; unit 2 S9 mirrors it. NOT OBSERVED here — the sibling it lands on observes it
  through its amended criterion; AC1 is a spec-text precondition (round-2 id 3).
- **S13** — id 27, M11, landing on unit 2. The node-journal reds come from `build_leg_yield` through a
  windowed `runlog.py journal --by-leg`, never a second counter. NOT OBSERVED here — the sibling it
  lands on observes it through its amended criterion; AC1 is a spec-text precondition (round-2 id
  3).
- **S14** — id 28, M12, landing on unit 5. `read_finding_units` reads through `review_replay.py
  --confirmed-rows`, so `parse_appendix_rows`' liveness check holds. NOT OBSERVED here — the sibling
  it lands on observes it through its amended criterion; AC1 is a spec-text precondition (round-2 id
  3).
- **S15** — id 29, M13, landing on unit 5. The cited-tag check is PLAY-dOrderedCharter-19's `TAG_RE` and
  `TAG_MAX_BYTES`, its Python copies held by a `PARITY_ROWS` row. NOT OBSERVED here — the sibling it
  lands on observes it through its amended criterion; AC1 is a spec-text precondition (round-2 id
  3).
- **S16** — id 30, M14, landing on units 3, 5, 15, 16 and 17. One reader of earlier records,
  `read_loop_records`, and one Metrics splitter, `read_metrics_lines`, in unit 3; units 5, 6, 15, 16
  and 17 call them (unit 6 added at round 2, id 20). Observed by AC4; AC1 is a spec-text
  precondition (round-2 id 3).
- **S17** — id 31, M15, landing on units 9 and 16. Unit 16 reads acts through `ledgers.py acts` and the
  runtime journal through unit 9's `read_runtime_journal`. NOT OBSERVED here — the sibling it lands
  on observes it through its amended criterion; AC1 is a spec-text precondition (round-2 id 3).
- **S18** — id 33, M16, landing on unit 8. `fill` rewrites the appendix through a new
  `read_appendix_table` in `review_replay.py`, which returns every row. NOT OBSERVED here — the
  sibling it lands on observes it through its amended criterion; AC1 is a spec-text precondition
  (round-2 id 3).
- **S19** — id 37, M17, landing on units 2, 3 and 5. Each registry row carries `unarmed` until its
  first record is tracked, and each unit runs `record_kinds.py --check` after its pass. Observed by
  AC1.
- **S20** — id 38, M18, landing on units 2, 3 and 5. Each row edit is followed by `record_kinds.py
  --write` and `adopt-memory-tree.sh --render`, both HYGIENE copies in one commit. NOT OBSERVED here
  — the sibling it lands on observes it through its amended criterion; AC1 is a spec-text
  precondition (round-2 id 3).
- **S21** — id 39, M19, landing on units 2, 3, 5, 7, 9, 11, 12, 15 and 17. Every `loop_review.py` verb or
  flag on `help/loop-review.md` has its `[[usage]]` row in `tools/govkit/usage.toml`. Observed by AC6;
  AC1 is a spec-text precondition (round-2 id 3).
- **S22** — id 40, M20, landing on unit 13. The `lens` surface class has its `[[class]]` row in
  `usage.toml`, and unit 13's §7 names `docs`. NOT OBSERVED here — the sibling it lands on observes
  it through its amended criterion; AC1 is a spec-text precondition (round-2 id 3).
- **S23** — id 41, M21, landing on unit 10. The held leg `instruction-eval` ships with its budget, pin
  and ceiling-evidence rows. NOT OBSERVED here — the sibling it lands on observes it through its
  amended criterion; AC1 is a spec-text precondition (round-2 id 3).
- **S24** — id 42, M22, landing on units 2, 4 and 13. Each new leg is claimed by a feature dossier,
  names its subject and chunk, and is pinned and, when held, budgeted. NOT OBSERVED here — the
  sibling it lands on observes it through its amended criterion; AC1 is a spec-text precondition
  (round-2 id 3).
- **S25** — id 43, M23, landing on unit 1. The three TOOL-dRankedPlan-6 arms the preset move flips are
  named, and `help/loop.md`'s Plan Review paragraph is rewritten. NOT OBSERVED here — the sibling it
  lands on observes it through its amended criterion; AC1 is a spec-text precondition (round-2 id
  3).
- **S26** — id 44, M24, landing on unit 14. `lens-schema.toml` declares `replay`, admitted on an
  overlay row only. NOT OBSERVED here — the sibling it lands on observes it through its amended
  criterion; AC1 is a spec-text precondition (round-2 id 3).
- **S27** — id 45, M25, the blast-radius lens's copy of H3 (id 2), landing on units 3, 4, 6 and 16. It
  closes with `TOOL-dCalibratedLens-21`'s carrier, whose `id 2` amendments those four specs carry, and
  this item observes them. NOT OBSERVED here — the sibling it lands on observes it through its
  amended criterion; AC1 is a spec-text precondition (round-2 id 3).
- **S28** — id 51, M26, landing on units 9 and 12. `ledgers.py acts --since` filters by file-name date
  and reads the act records in one process; `estimate` stays all-time. NOT OBSERVED here — the
  sibling it lands on observes it through its amended criterion; AC1 is a spec-text precondition
  (round-2 id 3).
- **S29** — id 53, M27, landing on unit 11. The landings are windowed by committer time before any
  `read_landing` fetch. NOT OBSERVED here — the sibling it lands on observes it through its amended
  criterion; AC1 is a spec-text precondition (round-2 id 3).
- **S30** — id 54, M28, landing on unit 16. The kept population is every CLOSED build no earlier
  record's `bound-evidence` lines name. NOT OBSERVED here — the sibling it lands on observes it
  through its amended criterion; AC1 is a spec-text precondition (round-2 id 3).
- **S31** — id 11, L1, landing on units 3, 9 and 17. `searched-none` is an empty source and
  `unread · <reason>` a dead one, everywhere. Observed by AC7; AC1 is a spec-text precondition
  (round-2 id 3).
- **S32** — id 12, L2, landing on units 2 and 3. The snapshot's `writer` names both doors, and unit 3's
  AC6 names the path `record` writes. NOT OBSERVED here — the sibling it lands on observes it
  through its amended criterion; AC1 is a spec-text precondition (round-2 id 3).
- **S33** — id 13, L3, landing on unit 3. The goal counts five rows, unit 5 adding the sixth. Observed
  by AC1.
- **S34** — id 14, L4, landing on unit 13. The `opt-in-unknown` table row and AC5 name the same
  refusal text. NOT OBSERVED here — the sibling it lands on observes it through its amended
  criterion; AC1 is a spec-text precondition (round-2 id 3).
- **S35** — id 20, L5, landing on unit 4. The evidence figure is 4,242 (path, commit) rows over 341
  commits. NOT OBSERVED here — the sibling it lands on observes it through its amended criterion;
  AC1 is a spec-text precondition (round-2 id 3).
- **S36** — id 21, L6, landing on unit 4. The `guide-bytes` example prints `current - (none)`.
  NOT OBSERVED here — the sibling it lands on observes it through its amended criterion; AC1 is a
  spec-text precondition (round-2 id 3).
- **S37** — id 22, L7, landing on unit 15. A full run is every `repo`-subject leg executed, and a held
  size leg reads `unread`. NOT OBSERVED here — the sibling it lands on observes it through its
  amended criterion; AC1 is a spec-text precondition (round-2 id 3).
- **S38** — id 23, L8, landing on unit 12. The `idle` sample rows carry `since` dates before the window.
  NOT OBSERVED here — the sibling it lands on observes it through its amended criterion; AC1 is a
  spec-text precondition (round-2 id 3).
- **S39** — id 24, L9, landing on unit 2. The manifest history figure is 536 across both forms.
  NOT OBSERVED here — the sibling it lands on observes it through its amended criterion; AC1 is a
  spec-text precondition (round-2 id 3).
- **S40** — id 34, L10, landing on unit 15. Its §10 cites `read_git_dirs` as the walk's precedent.
  NOT OBSERVED here — the sibling it lands on observes it through its amended criterion; AC1 is a
  spec-text precondition (round-2 id 3).
- **S41** — id 47, L11, landing on unit 14. `scenario-proposals` is a Metrics line, not a field.
  NOT OBSERVED here — the sibling it lands on observes it through its amended criterion; AC1 is a
  spec-text precondition (round-2 id 3).
- **S42** — The `at-year-back` arm (ids 6, 32, the M2 left-shift): a `--fixture` plant of
  `tools/loop/loop_review.py` that runs `run --dry-run --at` one year before now and reds when any
  reading's printed window, `derive_cap_readings`' and `read_journal_lines`' included, differs from the
  snapshot's `**Window:**`. Observed by AC2.
- **S43** — The `cost-grammar` arm (id 9, the M5 left-shift): `COST_RE`, `^(\d+(\.\d+)?(s|tok|B)/\d+|-)$`,
  in `loop_review.py`, applied by `price` to every provider's `cost` cell, a non-matching cell
  printing `ledger — <kind> · <id> · cost refused · <cell>` and rendering `-`; the plant feeds one cell
  of each unit and the bare `5400`. Observed by AC3.
- **S44** — The `keep-after-review` arm (ids 10, 46, 30, the M6 and M14 left-shift): a plant that commits
  a review, then a keep, then a snapshot, and reds unless `read_loop_records` and unit 15's
  `read_previous_breaches` still answer that review. Observed by AC4.
- **S45** — The `bounds-default` arm (id 18, the M8 left-shift): a plant of `tools/loop/measure.py` that
  runs every `BOUND_EVIDENCE` row over evidence equal to its key's catalogue default and reds unless
  each with an evidence reader prints `hold`. Observed by AC5.
- **S46** — The usage observation (id 39): after every sibling has landed, `python
  tools/govkit/docs_leg.py --list` names a `[[usage]]` row for every `python tools/loop/loop_review.py`
  command line on `help/loop-review.md`, the `propose` and `keep` rows among them. Observed by AC6.
- **S47** — The `dead-sources` arm (id 11, the L1 left-shift): a plant that runs every `METRICS` reader
  with its source killed (no runtime kit, a refused journal, a timed-out command) and reds unless each
  line reads `unread · <reason>`, the `compactions` line and the delivery and pool lines among them.
  Observed by AC7.

## 3. Non-goals (OUT)

- Any of the eleven HIGH findings: `TOOL-dCalibratedLens-19` to `-29`.
- A second reading of any sibling's correction: each lands under its own amended criterion, and this
  unit's AC1 observes only that the amendment is in the sibling's text.
- A lint over spec text for the review's spec-lint left-shift lines (ids 7, 8, 33, 38, 39, 40, 41, 42,
  43, 44, 47, 53). Each names a checker of this repository's spec corpus that no unit of this build
  owns; they are left to the owner's turn, and this unit records them in its §8 F1.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-2` — `price` and the `cost` grammar, which S43's `cost-grammar` arm validates
- **consumes-from** `TOOL-dCalibratedLens-3` — `read_loop_records`, `read_metrics_lines` and the walk's window, which the `keep-after-review` and `at-year-back` arms run
- **consumes-from** `TOOL-dCalibratedLens-4` — `derive_cap_readings` under the walk's window, which the `at-year-back` arm runs
- **consumes-from** `TOOL-dCalibratedLens-5` — the `[[usage]]` rows of `propose` and `keep`, which S46's `docs_leg.py --list` observation reads
- **consumes-from** `TOOL-dCalibratedLens-7` — the `[[usage]]` row of any verb it adds, which S46's `docs_leg.py --list` observation reads
- **consumes-from** `TOOL-dCalibratedLens-9` — the `compactions` reading's dead-source line, which the `dead-sources` arm reads
- **consumes-from** `TOOL-dCalibratedLens-11` — the delivery readings' dead-source lines, which the `dead-sources` arm reads
- **consumes-from** `TOOL-dCalibratedLens-12` — the `[[usage]]` row of any flag it adds, which S46's `docs_leg.py --list` observation reads
- **consumes-from** `TOOL-dCalibratedLens-15` — `read_previous_breaches` over `read_loop_records`, which the `keep-after-review` arm runs
- **consumes-from** `TOOL-dCalibratedLens-16` — `read_journal_lines` under the walk's window and the `BOUND_EVIDENCE` rows, which the `at-year-back` and `bounds-default` arms run
- **consumes-from** `TOOL-dCalibratedLens-17` — the three lines' dead-source answers, which the `dead-sources` arm reads

## 4. Design

### Evidence

- The 41 minors and their fixes are the review record's M1 to M28 and L1 to L11, and its appendix
  rows; every fix the skeptic judged UNSOUND (ids 22, 27, 29 and 51 among the minors) is carried in
  its corrected form, as the record states it.
- The amendments were written into the seventeen sibling specs at the disposal, each at rev-2, the
  HIGH findings' beside the minors'. Spec 7 carries id 39 only, spec 11 ids 53 and 39, and spec 6 id 45
  only through its `id 2` bullet.

### The amendment table AC1 reads

| id | Specs whose §4 "Amendments" carries `- **id <n> · ` |
|---|---|
| 5, 32, 17, 20, 21 | 4 |
| 6 | 4, 16 |
| 7, 44, 47 | 14 |
| 8 | 10, 13 |
| 9 | 2, 4 |
| 10, 46, 22, 34 | 15 |
| 18, 54 | 16 |
| 25, 13 | 3 |
| 26, 12, 37, 38 | 2, 3 (and 5 for 37 and 38) |
| 27, 24 | 2 |
| 28, 29 | 5 |
| 30 | 3, 5, 15, 16, 17 |
| 31 | 9, 16 |
| 33 | 8 |
| 39 | 2, 3, 5, 7, 9, 11, 12, 15, 17 |
| 40, 14 | 13 |
| 41 | 10 |
| 42 | 2, 4, 13 |
| 43 | 1 |
| 45 | 3, 4, 6, 16, through their `id 2` bullet |
| 51 | 9, 12 |
| 53 | 11 |
| 11 | 3, 9, 17 |
| 23 | 12 |

Spec `<n>` is `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-<n>.md`.

### The cost grammar

```python
COST_RE = re.compile(r"^(\d+(\.\d+)?(s|tok|B)/\d+|-)$")   # unit 2 §4 "The row", id 9
```

Unit 2's leg rows (`41.2s/3`), unit 12's item rows (`1840221tok/38`) and unit 15's breach rows
(`4433344B/212`) match; the bare `5400` unit 4's AC7 once planted does not.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `COST_RE` | constant in `loop_review.py` | none |
| `at-year-back`, `cost-grammar`, `keep-after-review`, `dead-sources` | `loop_review.py --fixture` plants | none |
| `bounds-default` | `measure.py --fixture` plant | none |
| `read_loop_records`, `read_metrics_lines` (unit 3), `read_runtime_journal` (unit 9), `read_appendix_table` (unit 8) | functions minted in the siblings by their amendments | `py.function`, each answered OK by `lexicon.py --suggest` at writing |

### Files touched (estimate)

- `tools/loop/loop_review.py` — S42 to S44 and S47, the plants and `COST_RE`
- `tools/loop/measure.py` — S45, the plant

### Alternatives rejected

- **The corrections made in this unit's build pass.** At order 18 every sibling is CLOSED and frozen,
  so a correction could no longer reach the spec its builder reads; the disposal wrote each into the
  unbuilt sibling instead.
- **Two batch units.** The arms share `tools/loop/loop_review.py`, so two halves would not build
  concurrently, the only reason M4 admits a second.

## 5. Production-readiness checklist

- security — `COST_RE` refuses a malformed cell at the pricer's boundary; the plants write only under
  their scratch repositories.
- perf / scale — six plants of seconds each; one `docs_leg.py --list` run.
- error / empty / loading states — a refused cost cell renders `-` with its line; a dead source reads
  `unread`.
- observability — each arm names the reading, the cell or the row it refused.
- risks — a sibling that built its correction differently from its amendment reds an arm here; the
  fix is that sibling's code, made by the main loop.
- testing — the six arms, observed RED and GREEN by the main loop at the close.
- migration — N/A.
- user docs — N/A: every user-facing change is a sibling's, with its own docs line.

## 6. Acceptance criteria

- **AC1** — When `grep -c '^- \*\*id <n> · '` runs over each spec the table of §4 names for id `<n>`,
  every count is at least 1, except id 45 in specs 3, 4, 6 and 16, which their `id 2` bullet carries
  and for which `grep -c '^- \*\*id 2 · '` is read (round-2 id 3).
  Red when: a minor is named here and carried by no sibling's amendment.
  A precondition read at writing: it greps the disposal's text, and nothing this unit builds moves it.
  figure: DERIVED, the table's 41 ids.
- **AC2** — When `python loop_review.py --fixture --plant at-year-back` runs from the loop kit
  directory, every reading's window equals the snapshot's.
  Red when: a reading anchors its window at now.
- **AC3** — When the plant `cost-grammar` runs `price --dry-run`, the `B`, `s` and `tok` cells print as
  planted and `5400` prints `-` with its `cost refused` line.
  Red when: a cell outside the grammar reaches the snapshot.
- **AC4** — When the plant `keep-after-review` runs, `read_loop_records` and `read_previous_breaches`
  both answer the review committed before the keep.
  Red when: a commit that added only a keep or a snapshot is read as the previous review.
- **AC5** — When `python measure.py --fixture --plant bounds-default` runs, each `BOUND_EVIDENCE` key
  with an evidence reader prints `hold` at its default.
  Red when: a rounding or a unit mismatch makes the default unreachable.
- **AC6** — When `python tools/govkit/docs_leg.py --list` runs after the last sibling has landed, it
  names a `[[usage]]` row for every `loop_review.py` command line on the `loop-review.md` help page.
  Red when: a page command has no row, so the `docs` leg reds on `UNROWED`.
- **AC7** — When the plant `dead-sources` runs `gather --dry-run`, every planted dead reader prints
  `unread · <reason>` and none prints `searched-none`.
  Red when: a dead source reads as empty.

## 7. Gates

`docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's legs `loop-review selftest` (TOOL-dCalibratedLens-2 S11) and `loop measure fixtures`
(TOOL-dCalibratedLens-4 S9) are not in the manifest at base and are named here in prose; they run
the arms once those units land.

New arm: tools/loop/loop_review.py · covers AC2 AC3 AC4 AC7 · the plants `at-year-back`, `cost-grammar`, `keep-after-review` and `dead-sources`, staged red by a reading anchored at now, a pricer with no `COST_RE`, a previous-record reader keyed by the newest commit, and a dead reader answering `searched-none` · none
New arm: tools/loop/measure.py · covers AC5 · the `bounds-default` plant, staged red by the act-ceiling row rounded up to whole hours · none

## 8. Open questions

- **F1 — Who builds the spec-lint left-shift lines the review attaches to twelve of these minors?**
  Each names a checker of this repository's spec corpus (a criterion invoking a hook with no payload, a
  spec listing `record-kinds.toml` without both HYGIENE copies, a spec editing `surface-classes.toml`
  without `usage.toml`, and their like). Options: (a) a new checker in `tools/check-spec-tokens.py`,
  shipped by this unit; (b) each class recorded as a `memory/gotchas/` entry by this unit; (c) none
  here, the classes named in this spec for the owner. (a) is a change to a governance carrier, the
  merge bar's spec checker, which veto 2 reserves for the owner; (b) is the M8 left-shift for a class
  that cannot be gated, but each of these can be gated, so a gotcha would stand in for a gate the
  owner has not chosen. Rung 3. RESOLVED (agent, 2026-11-02, delegated): (c); the six arms of S42 to
  S47 are the left-shifts this build can own, and the twelve spec-lint classes stay named in §3 for
  the owner. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from the round-1 spec audit's 30 MEDIUM and 11 LOW,
  batched; the seventeen siblings amended at the disposal (their rev-2).
- rev-2 · 2026-11-02 · §2 S1 to S41 S16 AC1 · amended at the disposal of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`, each `TOOL-dCalibratedLens-41`'s: AC1 reads
  id 45 through the `id 2` bullet and is stated a precondition, and every S-item it alone observed is
  marked NOT OBSERVED here with the sibling's criterion as its observer (id 3); S16's callers gain
  unit 6 (id 20).

## 10. Reuse audit

The seams extended are the siblings' own: unit 3's `--fixture` frame and `read_loop_records`, unit 4's
`measure.py --fixture` and `BOUND_EVIDENCE`, unit 2's row grammar, and `tools/govkit/docs_leg.py --list`,
read at base. `python tools/codebase-map/reuse_lookup.py "isolate each reader so one failure becomes an
unread line, never the walk's exit"`, run once for the set, ranked name stems only; no existing seam
validates a ledger cell or kills a reading's source, so `COST_RE` and the plants are new inside the
loop kit. The recall probe returned TOOL-cMendedVintage-19, the placement ruling this unit's order
follows, and the dFairHearing promoted-fix brief that caps a batch spec's size, which this spec keeps
under.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch loop review record kind"`
