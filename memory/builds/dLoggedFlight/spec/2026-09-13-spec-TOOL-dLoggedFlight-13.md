# TOOL-dLoggedFlight-13 — drift-audit reports run records left non-terminal after their build merged

**Status:** SPECCED · rev-1 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 |

<!-- /gen:spec-records -->

## 1. Goal

Six of 56 run records say LANDING or BUILDING although their work is on the default branch. So "did it
land?" cannot be answered from the record, and every later run's concurrency report carries them.
Report them from tracked bytes alone, sub-classified by why each stopped, as a drift-audit signal.

## 2. Scope (IN)

- **S1** A new signal, `run_records_nonterminal_but_merged`, built by a new function in
  `tools/drift-audit/drift_report.py` and added to its `SIGNALS` registry. The function reads each
  tracked `memory/builds/*/RUN*.md` at HEAD, takes its `phase:` and `witness:` facts, and counts the
  records whose phase is not terminal and whose witness is an ancestor of the engine's base ref.
  Observed by AC1.
- **S2** Report-only: `gateable` is false. §4 records why a gate here would red the fleet for a
  landing the owner sanctioned. Observed by AC2.
- **S3** Each detail row names the record, phase and witness, and one sub-class from the record's own
  last parked row. The sub-classes are `surfaced-park`, `retired-unit`, `no-rows` and `other`. The
  refused-landing case cannot be told from tracked bytes, because refusals are not recorded there,
  and the row says so. Observed by AC3.
- **S4** Liveness: `live` is true when the population of run records is non-empty, and `of` is that
  population. Observed by AC1.
- **S5** Cost: two git calls in total, one `rev-list` of the base and one `cat-file --batch-check`
  over the witnesses, measured at 0.07 s against 3.4 s for two calls per record. Observed by AC4.
- **S6** The kit version moves from 1.10 to 1.11 across its carriers, with a self-test arm. Observed
  by AC5.

## 3. Non-goals (OUT)

- Repairing the six records. They are the owner's to rule on, and several need `--landed`, which is
  refused for a reason this unit does not reach.
- Reading any machine-local journal. A drift signal must be answerable in a fresh clone.

### Edges

none

## 4. Design

A gate here would red every bar after any worktree landing, and the owner has sanctioned those.
This run is one: it lands from a worktree and ends at LANDING by the owner's choice of 2026-09-13. As
soon as local `main` moves past its witness, the count would rise above any pin, on every node,
through no one's fault. So the signal reports and does not gate. A report-only signal is still judged
against its pin in the table output, so a rising count is visible.

The engine's base ref is resolved the way every other signal resolves it: `--base-ref`, then
`GOV_DEFAULT_BRANCH`, then the local short name of `refs/remotes/origin/HEAD`.

### Data model

`{signal: "run_records_nonterminal_but_merged", value, of, tolerance: 0, gateable: False, live,
unjudgeable, detail: ["<record> <phase> <witness8> <subclass>", ...]}`.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `build_nonterminal_merged_runs` | function | `py.function`, led by the declared `build` |
| `run_records_nonterminal_but_merged` | signal name | drift-audit registry |

### Files touched (estimate)

`tools/drift-audit/{drift_report.py,drift_signals.py,drift_signals.template.py,selftest.py,README.md}`
with the version carriers, and `memory/map/features/` if a dossier claims the signal.

### Alternatives rejected

- Gateable with a pin of 6: rejected by §4.
- Subject-grep for merges: rejected. The evidence reviewer measured that a slug appears in unrelated
  merge subjects, and ancestry is exact.

## 5. Production-readiness checklist

- security — N/A; it reads tracked files and the object store.
- perf / scale — two git calls; S5.
- error / empty / loading states — a record with no `witness:` is `unjudgeable` and counted apart.
  An unresolvable witness is `unjudgeable`, not merged.
- observability — the detail rows.
- risks — none beyond the report being ignored; it is visible in the table on every run.
- testing — a fixture tree per sub-class and one unjudgeable record, each staged, plus the kit's
  existing meta-tests that every signal can move and none hard-codes `live`.
- migration — none.
- user docs — the drift-audit README's signal table.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py` runs on this tree, the new signal reports
  a value of 6 or more, with `of` equal to the tracked run-record count, and `live` true.
  Red when: the signal reads the working tree rather than HEAD, or matches no record.
  figure: 6 was measured on 2026-09-13; the arm asserts the value against a fixture, not against this
  tree.
- **AC2** — When `python tools/drift-audit/drift_report.py --check` runs on this tree, it exits 0
  whatever the signal's value.
  Red when: the signal is gateable.
- **AC3** — When `python tools/drift-audit/selftest.py` builds fixture records for each sub-class, the
  signal names each with its sub-class. A terminal record and an unmerged witness are not counted.
  Red when: a terminal record or an unmerged witness is counted.
- **AC4** — When `tools/drift-audit/selftest.py` counts the git subprocess calls that
  `build_nonterminal_merged_runs` makes over 50 fixture records, it counts two.
  Red when: the function calls git per record.
- **AC5** — When `bash tools/check-kit-versions.sh` runs, drift-audit is green at 1.11, and the
  `drift-audit selftest` leg passes.
  Red when: a carrier still reads 1.10.

## 7. Gates

`drift-audit records` · `drift-audit selftest` · `drift-audit wiring` · `kit version markers` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/drift-audit/selftest.py` · each sub-class and the non-gateable property staged RED · floor raised by the arm count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

The seam is drift-audit's `SIGNALS` registry at `tools/drift-audit/drift_report.py:1749-1755` and its
`Git` helper. `tools/codebase-map/reuse_lookup.py "report run records left non-terminal"` returned the
drift-audit dossier. No signal reads a run-state file today, so the reader is new. The two-call
strategy was measured by the records acquisition probe to agree with the kit's per-record shape on
every row.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
