# TOOL-dLinkedLibrary-72 — the CI census refuses an Azure job a template supplies at any level

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 23 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-72-deviation-721.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-72-deviation-721.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-74 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 54 to 64
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md`) confirmed
finding **id 40 at HIGH**, report item **H5**. Id 15 shares the item and is its own unit,
`TOOL-dLinkedLibrary-71`.

`TOOL-dLinkedLibrary-63` S2 refuses an Azure `template:` only as a step. Azure Pipelines also pulls whole
stages and jobs from a template (`- template:` under `stages:` or `jobs:`), and a top-level `extends:
template:` hands the entire pipeline to another file. None of those is read or refused, so a pipeline
whose publishing job sits in a stage or job template reads with no publishing line, and an
`extends:`-based pipeline grades its local stub. That contradicts 63's F2, deny by default, on the
security surface 63 §5 prices.

This unit refuses each Azure template reference outside a step, and the top-level `extends:`, as opaque.
It repairs `TOOL-dLinkedLibrary-63` and builds one step after it (order 23).

## 2. Scope (IN)

- **S1** — Stage and job templates. In `tools/memory-tree/adopt_program.py`'s `ci-job` class, an
  `azure-pipelines.yml` list item `- template: <value>` under `stages:` or `jobs:` is a census row of its
  own, named `template <value>`, reading `refused: opaque step template <value>`. Observed by AC1.
- **S2** — The top-level `extends:`. An `azure-pipelines.yml` holding a top-level `extends:` refuses every
  job and every template row in the file, each reading `refused: opaque step extends <template value>`.
  Observed by AC2.
- **S3** — What stays readable. An Azure file with no `template:` outside a step and no top-level
  `extends:` is graded as 63 S1 to S3 state, and 63's step-level `template:` refusal is unchanged.
  Observed by AC3.
- **S4** — The plants, cases of `adopt_program.py --fixture --plant ci-census`: an Azure file whose
  `jobs:` list holds `- template: publish-job.yml` beside a plain job; one whose `stages:` holds `-
  template: release-stage.yml`; and a third scratch tree whose `azure-pipelines.yml` opens with `extends:
  template: base.yml` and defines one plain job. Observed by AC1 and AC2.
- **S5** — The page. `help/adopt.md`'s census section names the Azure template refusals. Observed by AC4.

## 3. Non-goals (OUT)

- GitLab's indirection keys: `TOOL-dLinkedLibrary-71` (id 15).
- The block-scalar reader: `TOOL-dLinkedLibrary-73` (id 39).
- Fetching or reading a template file, local or remote: the census stays a text reader of the three
  files unit 51 names, as 63 §3 keeps it.
- Azure step `env:` credentials: `TOOL-dLinkedLibrary-74`'s item for id 41.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-63` — S2's opaque-step refusal and the `ci-census` plant, which S1 and S2 extend to Azure's stage, job and pipeline templates (id 40)
- **hands-off** `TOOL-dLinkedLibrary-80` — S5's page paragraph, which unit 80 completes (id 16 of the spec audit of units 65 to 74)

## 4. Design

### Evidence

- 63 S2 names an Azure `task:` or `template:` step only; 63 S1 reads Azure jobs by `script`, `bash`,
  `pwsh` and `powershell`.
- `git ls-files` lists no `azure-pipelines.yml` at base, so S4's plants are the only population.

### An Azure file after S1

```yaml
stages:
- template: release-stage.yml     # S1: refused, opaque step template release-stage.yml
- stage: test
  jobs:
  - job: unit
    steps:
    - script: npm test            # graded as 63 states
```

### Rollout

Order 23 beside `TOOL-dLinkedLibrary-71` and `TOOL-dLinkedLibrary-73`. All three write
`adopt_program.py`, so BUILD-METHOD M6's clause 1 sequences the passes; each owns its own keys and none
reads another's output.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4
- `help/adopt.md`: S5

### Alternatives rejected

- **Reading a local template file the census can find in the tree.** A template may take parameters and
  conditional insertion, so its text is not the job's text, and a remote one is not in the tree at all.
- **Refusing only the plain job beside a stage template.** The template row itself is what may publish,
  so it is the row that must appear refused.

## 5. Production-readiness checklist

- security — closes the import of a publishing Azure job a template supplies; deny by default.
- perf / scale — one more key test per list item.
- error / empty / loading states — unchanged from 63.
- observability — each refusal names the key and the template.
- risks — every `extends:`-based pipeline is refused whole; the owner may rule a job in.
- testing — S4's plants under `adopt_program.py --fixture`.
- migration — none.
- user docs — `help/adopt.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, the rows
  `template publish-job.yml` and `template release-stage.yml` read `refused: opaque step template`.
  Red when: a job or stage template reads `importable` or has no row.
- **AC2** — When the same plant runs, the plain job of the tree whose file opens `extends:` reads
  `refused: opaque step extends base.yml`.
  Red when: a job under a top-level `extends:` reads `importable`.
- **AC3** — When the same plant runs, the plain job beside the job template, and 63's Azure rows, read as
  63's AC2 and AC3 state.
  Red when: the template refusal spreads to a job that names no template in a file with no `extends:`.
- **AC4** — When `grep -n "template\|extends"` runs over the help page `adopt.md` (its path in Files
  touched), it prints the census section's Azure lines.
  Red when: the page states the step-level `template:` alone.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 · the `ci-census` plant's three Azure template trees, the failing case staged by 63's step-only `template:` rule · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 54 to 64, id 40 (HIGH, item
  H5).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-80, promoted from the spec
  audit of units 65 to 74; nothing else moved.

## 10. Reuse audit

The seam extended is 63 S2's opaque-step refusal inside `TOOL-dLinkedLibrary-8`'s `ci-job` class in
`tools/memory-tree/adopt_program.py`, one more set of keys on the same rule. `python
tools/codebase-map/reuse_lookup.py "refuse a ci job that inherits its script through extends or an
anchor"` ranked `anchors`, `anchor_at`, `CensusRefused`, `ScopeRefused` and `ReapRefused`, none a CI
reader, so no existing seam fits beyond the census being extended.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding of a spec audit repair a unit at the next order step" --terms "spec-audit promoted high finding repairs order staged break conf reader row grammar census indirection"`
