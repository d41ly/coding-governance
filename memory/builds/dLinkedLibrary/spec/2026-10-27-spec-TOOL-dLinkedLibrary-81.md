# TOOL-dLinkedLibrary-81 — the CI census reads an Azure `variables:` list as a closed set of item forms, refusing any other

**Status:** OPEN · rev-4 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 32 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-81-deviation-811.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-81-deviation-811.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-86 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 75 to 80
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md`) confirmed
finding **id 13 at HIGH**, report item **H1**. Id 34 shares the item and is its own unit,
`TOOL-dLinkedLibrary-82`.

`TOOL-dLinkedLibrary-79` S2 reads an Azure `variables:` list by two item forms, `- name:` and `- group:`.
Every other form is read by nothing: `- template: <file>`, which id 34 names, and the template-expression
items Azure also admits there, a conditional insertion `- ${{ if <cond> }}:` or an `- ${{ each ... }}:`
loop, whose nested items the reader never reaches. A form outside the two the reader knows is an
import it cannot read, and today it grades the jobs it applies to `importable`.

This unit turns the item read into a closed set: the forms the census reads are listed, and any item
outside the list refuses the jobs its block applies to. Id 34's unit gives `- template:` its own
reason; this unit makes the class deny by default, so the next unlisted form cannot pass either. It
repairs `TOOL-dLinkedLibrary-79` and builds one step after it (order 32).

## 2. Scope (IN)

- **S1** — The known forms. In `tools/memory-tree/adopt_program.py`'s `ci-job` class, an
  `azure-pipelines.yml` `variables:` block at any level 79 S1 names, and on a job, is read as one of two
  shapes. A list: each item at the list's own indentation opens with `- name:` (its `value:` and
  `readonly:` keys read as 79 S2 states), `- group:` (79 S2) or `- template:` (`TOOL-dLinkedLibrary-82`).
  A block mapping: each key a plain variable name, read as 79 S2 reads a name. Observed by AC1 and AC3.
- **S2** — Every other form refuses. A list item opening with any other key, or with `${{`, and a
  mapping key opening with `${{`, refuses every job its block applies to, scoped as 79 S3 scopes a hit:
  a pipeline-level hit refuses every job, a stage-level hit that stage's jobs, a job-level hit that job.
  Each reads `refused: unreadable variables item <form>`, `<form>` being `expression` for an item or key
  opening `${{` and the item's first key otherwise. A `variables:` whose value is a scalar on its own
  line, `variables: ${{ parameters.vars }}` say, refuses the same way with `<form>` `expression`.
  Observed by AC1 and AC2.
- **S3** — Precedence. `- group:` keeps 79 S2's reason. A `- template:` item keeps the reason unit 82
  gives it where unit 82 has landed, and reads S2's `refused: unreadable variables item template`
  until then, so the item never reads `importable` in either order of the two passes. Observed by
  AC3.
- **S4** — The plants, cases of `adopt_program.py --fixture --plant ci-census`, each a scratch tree of
  its own with two plain jobs, `publish` running `./publish.sh` and `test` running `npm test`, one
  before and one after the block where YAML allows: an Azure file whose pipeline-level `variables:` list
  holds `- ${{ if eq(variables['Build.SourceBranchName'], 'main') }}:` over a nested `- group:
  release-vars`; an Azure file whose pipeline-level `variables:` mapping holds a key `${{ if
  eq(parameters.release, true) }}:` over a nested `NUGET_API_KEY: $(nugetKey)`; an Azure file with two
  stages, the first holding a stage-level `variables:` item `- ${{ each v in parameters.vars }}:` and the
  second none, each stage holding the two plain jobs; and an Azure file whose pipeline-level `variables:` list holds only `- name:
  BUILD_CONFIGURATION` with `value: Release`. Observed by AC1 to AC3.

## 3. Non-goals (OUT)

- The `- template:` item's own reason: `TOOL-dLinkedLibrary-82` (id 34).
- Evaluating a template expression or a condition: the census stays a text reader, as 63 §3 keeps it.
- GitLab's and GitHub's variable blocks: 79 S1's rows for them are unchanged.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-79` — S1's Azure levels, S2's `- name:` and `- group:` reads and S3's scoping, which S1 and S2 close over every other item form (id 13)
- **hands-off** `TOOL-dLinkedLibrary-87` — S2's unknown-key and scalar branches and S3's interim template refusal, which unit 87 plants and stages red (id 1)
- **hands-off** `TOOL-dLinkedLibrary-88` — S1's closed set and S2's `unreadable variables item <form>` reason, which unit 88 extends to a flow-style value and item (id 27)
- **hands-off** `TOOL-dLinkedLibrary-91` — S4's plant trees, S3's "Observed by" claim, §5's user docs, its Rollout and §4's 79 cite, which unit 91's S1 to S5 and S30 correct at this unit's pass (ids 2, 28, 7, 25, 11, 17)
- **hands-off** `TOOL-dLinkedLibrary-94` — S1's list and mapping reading and S2's scalar branch, which unit 94 applies to a `variables:` value on the line after its key (id 22)
- **hands-off** `TOOL-dLinkedLibrary-99` — S1's item reading at the list's own indentation and S3's precedence keeping 79 S2's `- group:` reason, which unit 99 feeds from 94's locator for a list at the key's own indentation (id 24)

## 4. Design

### Evidence

- 79 S2 (`2026-10-27-spec-TOOL-dLinkedLibrary-79.md:46-53`): an Azure list item `- name: <NAME>` names its
  variable, and `- group: <name>` is an unreadable credential; no other form is stated.
- 72 S1 refuses `- template:` only under `stages:` or `jobs:`; 63 S2 refuses a step-level `template:`;
  neither reads an item of a `variables:` list.
- Azure's YAML schema admits a `variables:` list of `name`/`value`, `group` and `template` items, and
  template expressions `${{ if }}`, `${{ elseif }}`, `${{ else }}` and `${{ each }}` as list items or
  mapping keys at any of those levels.

### An Azure file after S1 and S2

```yaml
variables:
- ${{ if eq(variables['Build.SourceBranchName'], 'main') }}:   # S2: refused, item form expression
  - group: release-vars
jobs:
- job: publish
  steps:
  - script: ./publish.sh       # refused: unreadable variables item expression
```

### Rollout

Order 32 beside `TOOL-dLinkedLibrary-82`. Both write `adopt_program.py`, so BUILD-METHOD M6's clause 1
sequences the passes; S3 holds for either order, and neither unit's criteria read the other's plant.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4

### Alternatives rejected

- **Listing `- template:` as the one missing form.** It closes the instance and leaves the class: the
  next form Azure admits, or the expression items already admitted, passes unread.
- **Descending into an expression item and reading its nested items.** Which branch applies depends on
  the condition, which the census cannot evaluate, so the read would be a guess.

## 5. Production-readiness checklist

- security — closes the import of a job whose variables arrive through an item form the census does not
  read; deny by default.
- perf / scale — one test per `variables:` item, as before.
- error / empty / loading states — an empty `variables:` block refuses nothing.
- observability — each refusal names the item form.
- risks — a pipeline using a conditional variable item refuses its jobs; the owner may rule a job in.
- testing — S4's plants under `adopt_program.py --fixture`.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — none under `help/` from this unit: 79 S5's sentence names the blocks read, and the closed
  item set is the census's own reading of them.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, both jobs of the
  tree whose pipeline-level list holds the `${{ if }}` item, and both jobs of the tree whose mapping holds
  the `${{ if }}` key, read `refused: unreadable variables item expression`.
  Red when: 79's two-form read leaves an expression item unread and a job reads `importable`.
- **AC2** — When the same plant runs, the jobs of the stage holding the `${{ each }}` item read `refused:
  unreadable variables item expression`, and both jobs of the second stage read `importable`.
  Red when: a stage-level hit reaches another stage's job, or misses one of its own.
- **AC3** — When the same plant runs, both jobs of the tree holding only `- name: BUILD_CONFIGURATION`
  read `importable`, and no job anywhere in the plant reads `importable` beside a `variables:` item whose
  first key is not `name`, `group` or `template`.
  Red when: the closed set refuses a known form, or an unknown form passes.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 · the `ci-census` plant's four `variables:` item-form trees, the failing case staged by 79's `- name:`/`- group:`-only read · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 75 to 80, id 13 (HIGH, item
  H1, which id 34 shares).
- rev-2 · 2026-10-27 · §3 · the hands-off edges to units 87, 88 and 91, the mirrors of the consumes-from
  edges their specs declare, promoted from the spec audit of units 81 to 86; no scope or criterion moved.
- rev-3 · 2026-10-27 · §3 · the hands-off edge to unit 94, the mirror of the
  consumes-from edge its spec declares, promoted from the spec audit of units 87 to 91;
  no scope or criterion moved.
- rev-4 · 2026-10-27 · §3 · the hands-off edge to unit 99, the mirror of the
  consumes-from edge its spec declares, promoted from the spec audit of units 92 to 96;
  no scope or criterion moved.

## 10. Reuse audit

The seam extended is 79 S2's Azure `variables:` item read inside `TOOL-dLinkedLibrary-8`'s `ci-job` class
in `tools/memory-tree/adopt_program.py`, with 79 S3's scoping reused for the refusal. `python
tools/codebase-map/reuse_lookup.py "refuse an azure job whose variables list holds an item the reader does
not know"` ranked `read`, `read_text`, `note` and `read_conf`, none a CI reader, so no existing seam fits
beyond the census being extended.

Recall terms used: `python tools/memory-recall/query.py "how does the census read an azure variables list item it does not know" --terms "census ci-job azure variables group template item expression refused credentials deny-by-default"`
