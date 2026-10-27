# TOOL-dLinkedLibrary-82 — the CI census refuses the jobs an Azure variables template applies to, at every level

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 32 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 |
| [2026-10-27-build-TOOL-dLinkedLibrary-82-deviation-821.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-82-deviation-821.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-86 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 75 to 80
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md`) confirmed
finding **id 34 at HIGH**, report item **H1**. Id 13 shares the item and is its own unit,
`TOOL-dLinkedLibrary-81`.

`TOOL-dLinkedLibrary-79` S2 names `- group: <name>` as the one `variables:` item whose values live outside
the file. A `- template: <path>` item under `variables:` does the same: Azure reads the variables from
that file, at pipeline, stage or job level. No unit reads it. `TOOL-dLinkedLibrary-72` S1 refuses `-
template:` only under `stages:` or `jobs:`, 72 S2 only a top-level `extends:`, and
`TOOL-dLinkedLibrary-63` S2 only a step-level `template:`. So a pipeline-level `variables: [ - template:
release-vars.yml ]` whose file maps a token, beside a job running `./publish.sh`, grades `importable`.

This unit refuses every job a variables template applies to, as 79 refuses a variable group, and plants
it at each level. It repairs `TOOL-dLinkedLibrary-79` and builds one step after it (order 32).

## 2. Scope (IN)

- **S1** — The item. In `tools/memory-tree/adopt_program.py`'s `ci-job` class, an `azure-pipelines.yml`
  list item `- template: <path>` whose parent key is `variables:`, at the pipeline, a stage or a job, is
  an unreadable credential source, as 79 S2 reads `- group: <name>`. Observed by AC1 to AC3.
- **S2** — The refusal. It refuses every job its `variables:` block applies to, scoped as 79 S3 scopes a
  hit: a pipeline-level item every job, a stage-level item that stage's jobs, a job-level item that job.
  Each reads `refused: unreadable credentials template <path>`, `<path>` the item's value as written.
  Observed by AC1 to AC3.
- **S3** — What is unchanged. A `- template:` item whose parent key is `stages:` or `jobs:` keeps 72 S1's
  `opaque step template` row, and a step-level `template:` keeps 63 S2's refusal; the parent key alone
  decides which rule reads the item. Observed by AC4.
- **S4** — The plants, cases of `adopt_program.py --fixture --plant ci-census`, each a scratch tree of
  its own: an Azure file whose pipeline-level `variables:` list holds `- template: release-vars.yml`
  beside two plain jobs, `publish` running `./publish.sh` and `test` running `npm test`; an Azure file
  with two stages, the first holding a stage-level `variables:` item `- template: stage-vars.yml` and the
  second none, each stage holding the same two jobs; and an Azure file whose job `publish` holds a
  job-level `variables:` item `- template: job-vars.yml` beside the plain job `test`. Observed by AC1 to
  AC3.

## 3. Non-goals (OUT)

- Every other item form outside `- name:` and `- group:`: `TOOL-dLinkedLibrary-81` (id 13), whose fallback
  refuses a `- template:` item too until this unit lands.
- Fetching or reading the template file: the census stays a text reader, as 72 §3 keeps it.
- Stage and job templates under `stages:` and `jobs:`: 72 S1, unchanged.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-79` — S2's `- group:` reading and S3's scoping, which S1 and S2 extend to a `- template:` item under `variables:` (id 34)
- **hands-off** `TOOL-dLinkedLibrary-87` — S2's `unreadable credentials template <path>` reason, which unit 87's template tree reads (id 1)
- **hands-off** `TOOL-dLinkedLibrary-91` — S2's template reason and §7's `covers` list, which unit 91's S3 names on the page and S5 completes with AC4 at this unit's pass (ids 7, 11)

## 4. Design

### Evidence

- 79 S2 (`2026-10-27-spec-TOOL-dLinkedLibrary-79.md:50-53`) reads `- group: <name>` as a credential the
  census cannot read and names no other item form.
- 72 S1 (`2026-10-27-spec-TOOL-dLinkedLibrary-72.md`, S1) reads `- template:` under `stages:` or `jobs:`;
  63 S2 reads a step-level `template:`; neither names a `variables:` parent.
- `git ls-files` lists no `azure-pipelines.yml` at base, so S4's plants are the whole population.

### An Azure file after S1 and S2

```yaml
variables:
- template: release-vars.yml   # S1: values from outside the file
jobs:
- job: publish
  steps:
  - script: ./publish.sh       # S2: refused, unreadable credentials template release-vars.yml
```

### Rollout

Order 32 beside `TOOL-dLinkedLibrary-81`. Both write `adopt_program.py`, so BUILD-METHOD M6's clause 1
sequences the passes; 81 S3 holds the template item refused in either order.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4

### Alternatives rejected

- **72's `opaque step template` form for the item.** That form names a census row the template supplies;
  a variables template supplies values to jobs that are rows already, which is 79's credential reading.
- **Refusing only a job whose own lines reference a variable.** A release script reads its token from the
  environment without naming it, the case 79 exists for.

## 5. Production-readiness checklist

- security — closes the import of a job whose credentials arrive from a variables template; deny by
  default.
- perf / scale — one more item form per `variables:` block.
- error / empty / loading states — a `- template:` with an empty value refuses with an empty `<path>`.
- observability — each refusal names the template path.
- risks — a pipeline that keeps harmless variables in a template refuses its jobs; the owner may rule a
  job in.
- testing — S4's plants under `adopt_program.py --fixture`.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — none under `help/` from this unit: 79 S5's sentence already says credentials in a
  pipeline-level or stage-level `variables:` block refuse every job it applies to, and a template is one
  such source.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, both jobs of the
  tree whose pipeline-level list holds `- template: release-vars.yml` read `refused: unreadable credentials
  template release-vars.yml`.
  Red when: a pipeline-level variables template leaves a job `importable`.
- **AC2** — When the same plant runs, both jobs of the stage holding `- template: stage-vars.yml` read
  `refused: unreadable credentials template stage-vars.yml`, and both jobs of the second stage read
  `importable`.
  Red when: a stage-level template misses one of its stage's jobs, or reaches another stage.
- **AC3** — When the same plant runs, the job `publish` holding `- template: job-vars.yml` reads `refused:
  unreadable credentials template job-vars.yml` and the job `test` beside it reads `importable`.
  Red when: a job-level template passes, or refuses a job it does not apply to.
- **AC4** — When the same plant runs, 72's stage-template and job-template rows still read `refused:
  opaque step template` with their values.
  Red when: the parent-key test reads a `stages:` or `jobs:` template as a variables template.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 · the `ci-census` plant's three variables-template trees, the failing case staged by 79's `- group:`-only outside-source read · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 75 to 80, id 34 (HIGH, item
  H1, which id 13 shares).
- rev-2 · 2026-10-27 · §3 · the hands-off edges to units 87 and 91, the mirrors of the consumes-from
  edges their specs declare, promoted from the spec audit of units 81 to 86; no scope or criterion moved.

## 10. Reuse audit

The seam extended is 79 S2's `- group:` reading and S3's scoping inside `TOOL-dLinkedLibrary-8`'s `ci-job`
class in `tools/memory-tree/adopt_program.py`: one more outside-source item, the same refusal. `python
tools/codebase-map/reuse_lookup.py "refuse an azure job whose variables come from a template file"` ranked
`CensusRefused`, `ScopeRefused`, `corpus_files` and `ask_filed_in`, none a CI reader, so no existing seam
fits beyond the census being extended.

Recall terms used: `python tools/memory-recall/query.py "how does the census read an azure variables list item it does not know" --terms "census ci-job azure variables group template item expression refused credentials deny-by-default"`
