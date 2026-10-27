# TOOL-dLinkedLibrary-63 — the CI census reads the lines a GitLab or Azure job runs, and refuses one whose credentials it cannot read

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 22 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 |
| [2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-build-TOOL-dLinkedLibrary-63-deviation-631.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-63-deviation-631.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 37 to 53
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md`) confirmed
finding **id 27 at HIGH**, report item **H7**. No other id shares the item.

`TOOL-dLinkedLibrary-51` S1 keeps `.gitlab-ci.yml` and `azure-pipelines.yml` in the `ci-job` census, but
its S2 defines a job's text by GitHub keys alone, `steps`, `run: |`, `run: >` and `uses:`, and its S5's
`permissions:` and `secrets.` rules are GitHub's. GitLab's `script:`, `before_script:` and
`after_script:`, and Azure's `script:`, `bash:` and `pwsh:`, are never read, and unit 8's census row
reads only a step's `run` or `uses`. So `npm publish` in a GitLab `script:` reads `importable`, the
defect unit 51 exists to close, and 51's §3 fallback, catching an unlisted publish verb through its
credentials, does not exist for either dialect. All seven of 51's plants are GitHub-shaped.

This unit names the line keys of each dialect, states each dialect's credential rule, and plants one
case per dialect per refusal rule. It repairs `TOOL-dLinkedLibrary-51` and builds one step after it
(order 22).

## 2. Scope (IN)

- **S1** — The line keys per dialect. In `tools/memory-tree/adopt_program.py`'s `ci-job` class
  (`TOOL-dLinkedLibrary-8` S11, as unit 51 widens it), a job's text is every line under its dialect's keys:

  | File | Keys whose lines a job runs |
  |---|---|
  | `.github/workflows/*.yml`, `*.yaml` | `steps[].run`, `uses` (unit 51's S2, unchanged) |
  | `.gitlab-ci.yml` | `script`, `before_script`, `after_script`, and `default:`'s same three, applied to every job |
  | `azure-pipelines.yml` | `script`, `bash`, `pwsh`, `powershell` |

  Each key is read as a scalar, a list of scalars, or a block scalar (`|`, `>`, with or without a
  chomping indicator) up to the first line indented no deeper than the key; unit 51's S3 normalisation
  and S4 refusal list run over every line read. Observed by AC1 and AC2.
- **S2** — The opaque step. A GitLab `trigger:` or `include:` inside a job, and an Azure `task:` or
  `template:` step, run text the census does not hold; the job reads `refused: opaque step <key> <value>`.
  Observed by AC3.
- **S3** — The credential rule per dialect. GitLab and Azure jobs carry no grant the census can read, so a
  job of either dialect any of whose lines references a variable whose name matches `token`, `secret`,
  `password`, `passwd`, `key`, `credential` or `auth`, ignoring case, in the forms `$NAME`, `${NAME}`,
  `$(NAME)`, `$env:NAME` or `%NAME%`, reads `refused: unreadable credentials <NAME>`. Observed by AC3.
- **S4** — The plants, cases of `adopt_program.py --fixture --plant ci-census`: a `.gitlab-ci.yml` job
  whose `script:` list runs `npm publish` as its second item; an `azure-pipelines.yml` step `bash: |` whose
  block holds `cargo publish`; a GitLab job whose `script:` runs `./release.sh` with `$CI_DEPLOY_TOKEN`;
  an Azure step `task: NuGetCommand@2`; each `refused`; and a GitLab job running `npm ci` and `npm test`,
  `importable`. Observed by AC1 to AC4.
- **S5** — The page. `help/adopt.md`'s census section, which unit 51 writes, names each dialect's keys,
  the opaque-step refusal and the credential rule. Observed by AC5.

## 3. Non-goals (OUT)

- GitHub's rules: `TOOL-dLinkedLibrary-51`'s, unchanged, and a GitHub workflow with no `permissions:` key
  is id 28 of the same audit, a minor in `TOOL-dLinkedLibrary-64`.
- A YAML library: the census stays a text reader, as unit 8 §5 prices it.
- Other CI dialects: the census reads the three files unit 51's S1 names, and an unlisted file is not a
  `ci-job` source.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-51` — S2's block-scalar reader, S3's normalisation, S4's `CI_REFUSE_PATTERNS` and the `ci-census` plant, which S1 to S4 extend to the two other dialects (id 27)
- **hands-off** `TOOL-dLinkedLibrary-71` — S2's opaque-step refusal and the `ci-census` plant, which unit 71 extends to GitLab's inheritance and include keys (id 15 of the spec audit of units 54 to 64)
- **hands-off** `TOOL-dLinkedLibrary-72` — S2's opaque-step refusal and the `ci-census` plant, which unit 72 extends to Azure's stage, job and pipeline templates (id 40 of the spec audit of units 54 to 64)
- **hands-off** `TOOL-dLinkedLibrary-73` — S1's block-scalar rule, whose extent unit 73 restates (id 39 of the spec audit of units 54 to 64)
- **hands-off** `TOOL-dLinkedLibrary-74` — S3's credential rule and the `ci-census` plant, which unit 74 completes (id 41 of the spec audit of units 54 to 64)

## 4. Design

### Evidence

- `TOOL-dLinkedLibrary-51` S1 keeps both files; S2 names `steps`, `run: |`, `run: >` and `uses:` only;
  S5 names `permissions:` and `secrets.`; S6's seven plants are GitHub workflows.
- `TOOL-dLinkedLibrary-8` §4 "The census": `refused` when "a step's `run` or `uses`" matches.
- This repository tracks no `.gitlab-ci.yml` and no `azure-pipelines.yml` (`git ls-files`), so the plants
  are the only population either dialect has here.

### A GitLab job after S1 and S3

```yaml
release:
  script:
    - npm ci
    - npm publish            # S1: read; unit 51 S4: refused
deploy:
  script: ./release.sh "$CI_DEPLOY_TOKEN"   # S3: refused, unreadable credentials
```

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4
- `help/adopt.md`: S5

### Alternatives rejected

- **Refusing every GitLab and Azure job.** It refuses a plain test job, which unit 51's AC5 keeps
  importable for GitHub; the dialects are read, not banned.
- **Reading GitLab's protected-variable settings.** They live in the forge's settings, outside the
  repository the census reads.

## 5. Production-readiness checklist

- security — closes the import of a publishing GitLab or Azure job; the census executes nothing, and an
  opaque step or an unreadable credential is refused rather than guessed.
- perf / scale — the same text read, with two more key sets.
- error / empty / loading states — a file that does not read as jobs is `refused: unreadable`, as unit 51
  states.
- observability — each refusal names the matched verb, the opaque key or the variable.
- risks — a test job that reads a variable named like a credential is refused; the owner may still rule it
  in, as for any refused job.
- testing — S4's plants under `adopt_program.py --fixture`.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — `help/adopt.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, the GitLab
  job whose `script:` list runs `npm publish` second reads `refused: npm publish`.
  Red when: a GitLab `script:` list is not read.
- **AC2** — When the same plant runs, the Azure step whose `bash: |` block holds `cargo publish` reads
  `refused: cargo publish`.
  Red when: an Azure block scalar is not read.
- **AC3** — When the same plant runs, the GitLab job reading `$CI_DEPLOY_TOKEN` reads `refused: unreadable
  credentials CI_DEPLOY_TOKEN`, and the Azure `task: NuGetCommand@2` step reads `refused: opaque step task
  NuGetCommand@2`.
  Red when: a job whose credentials or step text the census cannot read is `importable`.
- **AC4** — When the same plant runs, the GitLab test job reads `importable`.
  Red when: the dialect rules refuse a job that neither publishes nor reads a credential.
- **AC5** — When `grep -n "before_script\|unreadable credentials\|opaque step"` runs over the help page
  `adopt.md` (its path in Files touched), it prints the census section's lines for each.
  Red when: the page states the GitHub rules alone.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 AC4 · the `ci-census` plant's five GitLab and Azure jobs, the failing case staged by unit 51's GitHub-only key set · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — What does the census do with a step whose text it cannot hold?** Options: (a) refuse it as
  opaque; (b) read it as `importable` and leave it to the owner. (b) widens what an import can carry past
  what unit 8 §5 priced (veto 3). RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, deny by default.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 37 to 53, id 27 (HIGH, item
  H7).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-71, TOOL-dLinkedLibrary-72, TOOL-dLinkedLibrary-73, TOOL-dLinkedLibrary-74, promoted from the spec audit of units 54 to 64; nothing else moved.

## 10. Reuse audit

The seam extended is `TOOL-dLinkedLibrary-8`'s `ci-job` class in `tools/memory-tree/adopt_program.py`,
with unit 51's block-scalar reader, normalisation and `CI_REFUSE_PATTERNS`, each read over the new keys
rather than re-implemented. `python tools/codebase-map/reuse_lookup.py "refuse a ci job that publishes
from a gitlab script list"` ranked `CensusRefused` and `ScopeRefused` (`tools/process-monitor/`, a
process census) and `read_id_list`, none a CI reader, so no existing seam fits beyond the census being
extended.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding repair a spec-audited unit at the next order step" --terms "spec-audit promoted high finding repairs order inline parity block tree-kill witness before-image"`
