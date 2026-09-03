# TOOL-aProbedToolkit-1 — grade the four knowledge kits against four real repos

**Status:** CLOSED · rev-2 · 2026-09-03 · node a · Tier-1 · base 51444cc1 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-03-build-TOOL-aProbedToolkit-1-graded-findings.md](../build/2026-09-03-build-TOOL-aProbedToolkit-1-graded-findings.md) | journal | — |
| [2026-09-03-build-TOOL-aProbedToolkit-1-measurements.md](../build/2026-09-03-build-TOOL-aProbedToolkit-1-measurements.md) | journal | — |
| [2026-09-03-build-TOOL-aProbedToolkit-1-synthesis.md](../build/2026-09-03-build-TOOL-aProbedToolkit-1-synthesis.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Decide, on measurement rather than on this repo's own green bar, whether `memory-tree`,
`memory-recall`, `lexicon` and `codebase-map` still serve the purpose each was built for, and
whether each is still worth using. The measurement runs every installed verb of each kit inside
scratch clones of the four trees that carry them, and grades the output against ground truth derived
independently of the kit under test.

## 2. Scope (IN)

- Scratch clones under `/tmp/kite`, made with `git clone --local` from `C:/projects/coding-governance`,
  `C:/projects/incms/main`, `C:/projects/incms/main/vendor/nicocares-package` and `C:/projects/swydee`.
- Every installed verb of the four kits in every clone that carries it, with exit code and full
  output captured per run under `/tmp/kite/out/`.
- Ground truth derived first and separately: corpus sizes, file populations by extension, definition
  counts, attribution coverage over source excluding records, and the retrieval answers for
  known-answer questions read out of the corpus before any query is issued.
- Classification of every gap the owner named: invisible, omitted, malformed, duplicated, or a bug
  needing a fix — each with a command that reproduces it from a fresh clone.
- A ranked recommendation list, and a backlog row per defect.

## 3. Non-goals (OUT)

- No change to any kit's source in this unit. A cross-kit fix is Tier 2 by the manifest's tier rule.
- No change to any of the four subject repositories, and no invocation of any kit inside them.
- The other kits — `unattended`, `hooks`, `playbook`, `drift-audit`, `pytest-parallel-guardrails` —
  are out, even where a finding touches their gate legs.
- No re-derivation of adopter-side forks into gov, beyond naming the ones worth carrying back.

## 4. Design

### Inventory

Four subjects, and the fourth is not what the request assumed: `C:/projects/nicocares` is an asset
directory whose `main` is a symlink into `C:/projects/incms/main/vendor/nicocares-package`, which is
its own repository nested inside incms/main's working tree. It is graded as its own subject.

Kit presence and version as installed, measured from each version marker:

| repo | memory-tree | memory-recall | lexicon | codebase-map | install prefix |
|---|---|---|---|---|---|
| coding-governance | 2.55 | 1.4 | 1.1 | 1.3 | `tools/` |
| incms/main | forked, renamed | forked | 1.1 | 1.3 | `scripts/` |
| nicocares-package | 2.49 | 1.4 | 1.1 | 1.3 | `scripts/` |
| swydee | 2.2 | 1.0 | absent | absent | repo root |

### Method

Three passes. The first runs the verbs and records exit codes; the second derives ground truth from
the trees without asking a kit; the third is an adversarial fan of one lens per kit, each prompted
with the measured evidence and the recurring-bug-class checklist, followed by batched skeptics that
must re-run a finding's repro before accepting it.

### Alternatives rejected

Grading the kits inside the real checkouts. Several kits write caches, indexes and rendered
artifacts, and one of them evicts. The measurement is not worth a damaged working tree, and a clone
of the committed tree is also the more honest subject: it grades what an adopter actually receives.

## 5. Production-readiness checklist

Records-only unit. Security, migration, i18n and a11y do not apply. Observability is the captured
output under `/tmp/kite/out/`, which is scratch and is not committed; what lands is the report and
its numbers, each traceable to a named command.

## 6. Acceptance criteria

1. Every kit-and-repo cell carries either a captured run with a verdict or a stated reason it is
   inapplicable. A cell may not be silently absent.
2. Every defect row carries a command that reproduces it from a fresh clone, and that command was
   run.
3. Every reported number is derived by a command, not estimated, and the command is named beside it.
4. Each kit gets a verdict from the closed set KEEP, KEEP-WITH-FIXES, NARROW, RETIRE, with the
   evidence that decides it.
5. The owner's four words — invisible, omitted, malformed, duplicated — are each answered per kit,
   explicitly, including where the answer is "none found".
6. Every confirmed defect leaves a backlog row in its family shard.

## 7. Gates

`bash tools/run-gates/run-gates.sh` over the records this unit adds. The leg set is single-sourced
from `tools/gate-legs.json`; the legs that bind a records-only change are the memory-hygiene,
build-index and declaration legs, and the run is reported by naming every leg the manifest defines
rather than a list typed here.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-03 · opened; scope derived from the kickoff message, subjects corrected after
  measuring that nicocares is a vendored repository rather than a top-level checkout.
- rev-2 · 2026-09-03 · CLOSED. All six acceptance criteria met. Sixteen cells measured, 45 findings
  graded by five skeptics with 44 confirmed, five readings withdrawn under checking and recorded as
  withdrawn, fifteen backlog rows filed. The report is published as an artifact and its working is
  the two journals in this folder.

## 10. Reuse audit

Not required at Tier 1, and recorded anyway because the probe was run. No existing seam fits: this
unit adds no code, and the closest existing instrument, `tools/drift-audit/drift_report.py`, answers
whether THIS repo's records match THIS repo's tree — a different question from whether a kit sees
another repo's tree at all. The evaluation therefore wires through no seam and ships none.
Recall terms used: kit adopter copy-install corpus pin vacuous coverage dossier baseline recall floor
lexicon verb table map inventory.
