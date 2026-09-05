# TOOL-dTracedLattice-7 — a merge-bar substrate whose score depends on the hash seed

**Status:** SPECCED · rev-2 · 2026-09-05 · node d · Tier-2 · base 22d75b31 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-dTracedLattice-1-baseline_ranks.py](../build/2026-09-05-build-TOOL-dTracedLattice-1-baseline_ranks.py) | research | TOOL-dTracedLattice-1 |
| [2026-09-05-build-TOOL-dTracedLattice-1-build_scen3.py](../build/2026-09-05-build-TOOL-dTracedLattice-1-build_scen3.py) | research | TOOL-dTracedLattice-1 |
| [2026-09-05-build-TOOL-dTracedLattice-1-grade.py](../build/2026-09-05-build-TOOL-dTracedLattice-1-grade.py) | research | TOOL-dTracedLattice-1 |
| [2026-09-05-build-TOOL-dTracedLattice-1-harness.py](../build/2026-09-05-build-TOOL-dTracedLattice-1-harness.py) | research | TOOL-dTracedLattice-1 |
| [2026-09-05-build-TOOL-dTracedLattice-1-harvest.py](../build/2026-09-05-build-TOOL-dTracedLattice-1-harvest.py) | research | TOOL-dTracedLattice-1 |
| [2026-09-05-build-TOOL-dTracedLattice-1-meas-cost-and-regression.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-meas-cost-and-regression.md) | research | TOOL-dTracedLattice-1 |
| [2026-09-05-build-TOOL-dTracedLattice-1-meas-memory-recall-recall.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-meas-memory-recall-recall.md) | research | TOOL-dTracedLattice-1 |
| [2026-09-05-build-TOOL-dTracedLattice-1-meas-reuse-lookup-recall.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-meas-reuse-lookup-recall.md) | research | TOOL-dTracedLattice-1 |
| [2026-09-05-build-TOOL-dTracedLattice-1-meas-shared-mechanism.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-meas-shared-mechanism.md) | research | TOOL-dTracedLattice-1 |
| [2026-09-05-build-TOOL-dTracedLattice-1-recall-report.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-recall-report.md) | research | TOOL-dTracedLattice-1 |
| [2026-09-05-build-TOOL-dTracedLattice-1-resolver.py](../build/2026-09-05-build-TOOL-dTracedLattice-1-resolver.py) | research | TOOL-dTracedLattice-1 |
| [2026-09-05-build-TOOL-dTracedLattice-1-scen-adversarial-seams.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-scen-adversarial-seams.md) | research | TOOL-dTracedLattice-1 |

<!-- /gen:spec-records -->

## 1. Goal

`bench.run_rm3` selects its expansion terms through `Counter.most_common`, whose ties break on
insertion order, and that order comes from iterating a `set` — so it depends on `PYTHONHASHSEED`.
`rm3` is a legal `RECALL_FLOOR` substrate, so a repository that pins its floor to `rm3` today gets a
gate whose verdict changes between runs on an unchanged tree.

## 2. Scope (IN)

- **S1** Make the expansion-term selection deterministic in `tools/memory-recall/bench.py`: the term
  set feeding `df` is ordered before it is counted, and `most_common`'s tie-break is made explicit
  rather than inherited from insertion order.
- **S2** Re-pin `bench.py` in `tools/memory-recall/verbatim.json`, since the file is byte-pinned and
  `selftest.py` asserts the pin. The re-pin lands in the same commit as the change, because a pin
  updated later is a window in which the assertion passes against the wrong bytes.
- **S3** An arm that runs the same query under several `PYTHONHASHSEED` values and fails on any
  disagreement. It must be observed RED against the current implementation before the fix lands.
- **S4** State in the kit README which substrates are seed-stable, so a project choosing a
  `RECALL_FLOOR` substrate is choosing with that knowledge rather than discovering it from a flaky
  gate.

## 3. Non-goals (OUT)

- No change to what `rm3` RETRIEVES beyond removing the nondeterminism. This unit makes the
  substrate reproducible; it does not try to make it better.
- No change to `RECALL_FLOOR`, to the declared floor value, or to which substrate this repository
  pins. Those are the adopting project's.
- No change to `fts5`, `fts5w` or `grep`, which were measured byte-identical across seeds.
- Not the recall SHORTFALL on harvested questions — §8 carries it as the separate unit it is.

## 4. Design

### Data model

`run_rm3` builds a `Counter` over the terms of its seed documents and takes `most_common`. Counts are
order-independent; the SELECTION among equal counts is not. Ordering the per-document term set before
`df.update`, and giving `most_common` an explicit key, makes the chosen expansion terms a function of
the corpus alone.

### Migration

`bench.py` is byte-pinned in `verbatim.json` and the memory-recall dossier records why: the floor gate
IMPORTS bench's scoring functions rather than extending them, so the pin is what stops the graded
substrate drifting away from the served one. S2 is therefore not bookkeeping — it is the half that
keeps that guarantee true.

### Alternatives rejected

Pinning `RECALL_FLOOR` to `rm3` and accepting the variance. Measured: eight free-seed runs give a
control `r@5` in `{0.6667, 0.75}` while `fts5` is byte-identical across all fourteen runs. A gate
that flips on an unchanged tree teaches its readers to re-run it until it passes.

Also rejected: removing `rm3` from `bench.LEXICAL`. It is a legitimate substrate and the defect is
three lines; deleting a measurement because it is noisy loses the measurement and keeps the noise
everywhere else the same idiom appears.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — one `sorted()` over a bounded per-document term list; no new scan.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — an empty seed already returns early and stays that way.
- observability — S4 is the observability item.
- risks — the re-pin is the risk. A change landed without S2 leaves `selftest.py` asserting stale
  bytes, which is a green gate over a file nobody is checking.
- testing + left-shift gates — S3 is the left-shift, and it generalises: the arm asks whether a
  substrate is seed-stable, so a future substrate inherits the question.
- migration / rollback — a project whose floor is pinned to `rm3` may see its measured score move
  once, to a stable value. S4 tells them before they meet it.
- user docs — `tools/memory-recall/README.md`, per S4.

## 6. Acceptance criteria

- **AC1** — When the same query is scored under at least three distinct `PYTHONHASHSEED` values,
  `run_rm3` returns identical rankings, and this arm is observed RED against the current
  implementation before the fix lands.
- **AC2** — When `python tools/memory-recall/selftest.py` runs after the change, the `verbatim.json`
  pin for `bench.py` matches the new bytes, so the assertion is against what ships.
- **AC3** — When `bash tools/run-gates/run-gates.sh` runs the `recall floor` leg twice on an
  unchanged tree, both runs report the same score.
- **AC4** — When `tools/memory-recall/README.md` is read, it names which substrates are seed-stable
  and which are not.

## 7. Gates

`memory-recall kit selftest` · `recall floor` · `recall floor arms` ·
`harness arms (fail branches armed or pinned)`.

The kit-subject legs are HELD on a plain bar; verifying this unit needs
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`. The runner names every held leg, so they are
announced rather than silent.

## 8. Open questions

- **Q1 — the floor's coverage, which is a bigger finding than this unit.** `records:fts5:r@5` holds
  its declared floor at `0.8333` over the shipped 12-question fixture and scores `0.3012` over 83
  questions harvested from the corpus, against a ceiling of `1.0000` — so the shortfall is retrieval,
  not unreachable targets, and 50 of 95 questions return nothing at any k. Widening the fixture would
  make the floor describe the corpus rather than twelve curated questions, and it would also almost
  certainly fail on the day it landed.

  **It does not need its own spec: three already exist.** `TOOL-aTunedCompass-2` makes the graded set
  send the query shape a session actually sends, since the fixture carries no terms while `query.py`
  refuses a query without them and all 148 live queries supplied them. `TOOL-aTunedCompass-3` makes
  the floor grade the two-set ensemble the CLI serves rather than the one set it grades today.
  `TOOL-aTunedCompass-9` builds a set that can tell the ensemble from its `records` half at all.
  RESOLVED (agent, 2026-09-05, delegated): this unit files nothing and points instead.

  The 83-question figure measured here is EVIDENCE FOR `-9` rather than a competing finding, and the
  two readings need reconciling by whoever builds it: `-9` reports `records:fts5` scoring recall
  1.000 by itself with terms at k=20, while this measurement reports 0.3012 at r@5 over 83 harvested
  questions against a ceiling of 1.0000. Different k, different question set, and nobody has run
  them against each other.

## 9. Revision log

- rev-2 · 2026-09-05 · Q1 resolved by pointing: `TOOL-aTunedCompass-2`, `-3` and `-9` already own
  the fixture and floor question this unit had parked, and the 83-question figure is re-framed as
  evidence for `-9` with the k and question-set difference named.
- rev-1 · 2026-09-05 · initial draft, from the scenario-based recall measurement, which found the
  defect while establishing a control for the substrate comparison.

## 10. Reuse audit

No existing seam fits, and the evidence is that the defect is three lines inside one function:
`python tools/codebase-map/reuse_lookup.py "make a ranking reproducible across interpreter runs"`
returns no seam above the threshold, which is the honest answer here rather than a weak one — this
tree has no shared determinism helper, and `sorted()` is the stdlib. The ranking that produced that
answer is itself under repair by `TOOL-dTracedLattice-1`, so the probe was corroborated by reading
`tools/memory-recall/bench.py:182-190` directly. Verified against source at writing time: `run_rm3`
calls `df.update` over a `set` at `:188` and `most_common` at `:189`, and `verbatim.json` carries
`bench.py`.

Recall terms used: memory-recall bench rm3 substrate expansion terms hash seed determinism verbatim
pin recall floor selftest counter most_common
