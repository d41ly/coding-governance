# TOOL-dLinkedLibrary-89 — the CI census reads GitLab's `spec:` header document and refuses a job an `inputs` interpolation reaches

**Status:** OPEN · rev-3 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 26 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-89-deviation-891.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-89-deviation-891.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-87-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-87-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 81 to 86
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md`) confirmed
finding **id 30 at HIGH**, report item **H3**. No other id shares the item.

`TOOL-dLinkedLibrary-84` S1 names the class "every top-level block that reaches every job" and lists eight
global blocks, leaving out GitLab's header keyword `spec:`. Its `inputs:` defaults reach a job's text
through the interpolation `$[[ inputs.<name> ]]`, and no census spec reads `inputs` or `$[[`. So a header
`spec: inputs: cmd: default: npm publish`, then `---`, then a job running `"$[[ inputs.cmd ]]"`, runs `npm
publish` while its text holds no refusal substring, no indirection token and no credential name: the job
grades `importable`.

This unit adds the header document to the class, as a block that is never a job, and refuses every job
an interpolation reaches, deny by default. It repairs `TOOL-dLinkedLibrary-84` and builds one step after
it (order 26).

## 2. Scope (IN)

- **S1** — The header document. In `tools/memory-tree/adopt_program.py`'s `ci-job` class, a
  `.gitlab-ci.yml` whose lines before its first column-0 `---` line hold a top-level `spec:` key has a
  header document: none of those lines is a job, a census row or a block whose script lines 84 S3 applies,
  and the jobs are read from the lines after that `---`. A top-level `spec:` with no `---` after it joins
  84 S1's class of job-wide blocks, never a job. Observed by AC3.
- **S2** — The interpolation in a job. A line of a job, its key line included, holding `$[[` refuses that
  job, reading `refused: opaque step inputs <name>`: `<name>` is the text after `inputs.` up to the first
  whitespace, `|` or `]]`, or the trimmed text between `$[[` and `]]` when it does not open `inputs.`.
  Observed by AC1.
- **S3** — The interpolation outside a job. A `$[[` on any other line after the header, in a block of 84
  S1 or elsewhere, refuses every job in the file through `TOOL-dLinkedLibrary-71` S2's one file-wide
  function, as 84 S2 routes its hits, each job reading the same reason. Observed by AC2.
- **S4** — What stays readable. A header whose `inputs:` no line after the `---` interpolates leaves the
  file's plain jobs graded as 63 S1 to S3, 79 and 84 state: a default reaches a job only through `$[[`.
  Observed by AC3.
- **S5** — The page. `help/adopt.md`'s census section carries the sentence "A GitLab `$[[ ... ]]`
  interpolation refuses the job whose lines hold it, and every job in the file when it sits outside a
  job, because its value comes from the pipeline's `spec:` header or from its caller." Observed by AC5.
- **S6** — The plants, cases of `adopt_program.py --fixture --plant ci-census`, each a scratch tree of its
  own: a header whose `spec:` `inputs:` gives `cmd` the default `npm publish`, then `---`, a job `release`
  whose `script:` runs `"$[[ inputs.cmd ]]"` and a plain job `test` running `npm test`; the same header,
  then `---`, a top-level `variables:` mapping `DEPLOY_CMD: $[[ inputs.cmd ]]` beside two plain jobs,
  `release` running `./release.sh` and `test` running `npm test`; and a header whose input `stage` has the
  default `test`, then `---`, the same two plain jobs and no `$[[`. Observed by AC1 to AC4.

## 3. Non-goals (OUT)

- Resolving an input's default or a caller's value: the census stays a text reader, as 63 §3 keeps it.
- An `include:` with `inputs:`: `TOOL-dLinkedLibrary-71` S2 already refuses every job of a file holding
  `include:`.
- The other job-wide blocks: 84 S1 to S3, unchanged.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-84` — S1's class of job-wide top-level blocks and S2's file-wide refusal path, which S1 and S3 extend to the `spec:` header and to an interpolation outside a job (id 30)
- **hands-off** `TOOL-dLinkedLibrary-96` — S1 to S3 and S6, which unit 96's S14, S15, S18 and S21 settle and plant at this unit's pass, S3's call into 71 S2's file-wide function, which unit 96's S20 lists among 91 S17's call sites, and the map re-render, by S12 (ids 26, 5, 15, 27, 20, 11)
- **hands-off** `TOOL-dLinkedLibrary-102` — this unit's pass and ledger, where unit 102's S19 narrows 96 S20's line to 71 S2's function and 96's pass adds the 91 S17 line (ids 7, 6)

## 4. Design

### Evidence

- 84 S1 (`2026-10-27-spec-TOOL-dLinkedLibrary-84.md`, S1) lists `default:`, `variables:`, `workflow:`,
  `image:`, `services:`, `cache:`, `before_script:` and `after_script:`; 84 §4 cites only GitLab's global
  keywords.
- GitLab's CI/CD YAML syntax reference lists `spec` under "Header keywords", in a header section separated
  from the pipeline by `---`, with `spec:inputs` interpolated into the pipeline as `$[[ inputs.<name> ]]`.
- A census-spec grep for `inputs` or `$[[` over units 51, 63 and 70 to 86 finds no reading of either.

### A GitLab file after S1 and S2

```yaml
spec:
  inputs:
    cmd:
      default: npm publish
---
release:
  script: ["$[[ inputs.cmd ]]"]   # S2: refused, opaque step inputs cmd
test:
  script: [npm test]              # importable
```

### Rollout

Order 26, one step after `TOOL-dLinkedLibrary-84`, whose class and file-wide path S1 and S3 extend. It
writes `adopt_program.py` and `help/adopt.md`, which unit 8 S12 created at order 20.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4, S6
- `help/adopt.md`: S5

### Alternatives rejected

- **Refusing only `$[[ inputs.` tokens.** GitLab interpolates other contexts the same way, and a
  closed reading of one prefix leaves the next; S2 refuses any `$[[`.
- **Reading the header's defaults into each job.** A caller overrides a default, so the text a job runs
  is not in the file.
- **Refusing every job of a file holding a header.** It refuses the third plant, whose input no job reads.

## 5. Production-readiness checklist

- security — closes the import of a job whose text arrives by a header input; deny by default.
- perf / scale — one substring test per line.
- error / empty / loading states — a header with no `---` after it is a job-wide block, never a job; a
  `$[[` with no closing `]]` takes `<name>` to the end of the line.
- observability — each refusal names the input.
- risks — a pipeline interpolating a harmless input refuses the jobs it reaches; the owner may rule a
  job in.
- testing — S6's plants under `adopt_program.py --fixture`.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — `help/adopt.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, the job
  `release` of the tree whose script runs `"$[[ inputs.cmd ]]"` reads `refused: opaque step inputs cmd`,
  and the job `test` beside it reads `importable`.
  Red when: the interpolation holds no refusal substring and `release` reads `importable`.
- **AC2** — When the same plant runs, both plain jobs of the tree whose top-level `variables:` maps
  `DEPLOY_CMD: $[[ inputs.cmd ]]` read `refused: opaque step inputs cmd`.
  Red when: an interpolation in a job-wide block reaches no job.
- **AC3** — When the same plant runs, both plain jobs of the tree with no `$[[` read `importable`, and no
  tree has a census row named `spec` or `inputs`.
  Red when: the header refuses jobs no input reaches, or is graded as a job.
- **AC4** — When a scratch copy of `adopt_program.py` without S2's and S3's `$[[` test runs the same plant
  by `python -I`, the job `release` of AC1's tree prints `importable`.
  Red when: the staged break leaves the job refused, so the plant does not discriminate the test.
- **AC5** — When `grep -n 'interpolation refuses'` runs over the help page `adopt.md` (its path in Files
  touched) at this tip, it prints S5's sentence, and over the page at this pass's start, read with `git
  show`, it prints nothing.
  Red when: the refusal ships with no line on the page.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 · the `ci-census` plant's three header-document trees, the failing case staged by 84's eight-block class with no `$[[` test · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 81 to 86, id 30 (HIGH, item
  H3).
- rev-2 · 2026-10-27 · §3 · the hands-off edge to unit 96, the mirror of the
  consumes-from edge its spec declares, promoted from the spec audit of units 87 to 91;
  no scope or criterion moved.
- rev-3 · 2026-10-27 · §3 · the hands-off edge to unit 102, the mirror of the
  consumes-from edge its spec declares, promoted from the spec audit of units 92 to 96;
  no scope or criterion moved.

## 10. Reuse audit

The seam extended is 84 S1's class of job-wide blocks and its file-wide refusal, which is 71 S2's one
function, inside `TOOL-dLinkedLibrary-8`'s `ci-job` class in `tools/memory-tree/adopt_program.py`.
`python tools/codebase-map/reuse_lookup.py "read a gitlab header document spec inputs before the
separator"` ranked `read`, `read_text`, `before` and `read_conf`, none a CI reader, so no existing seam
fits beyond the census being extended.

Recall terms used: `python tools/memory-recall/query.py "how does a gitlab pipeline header spec inputs reach a job" --terms "census ci-job gitlab spec inputs header document interpolation job-wide refused opaque"`
