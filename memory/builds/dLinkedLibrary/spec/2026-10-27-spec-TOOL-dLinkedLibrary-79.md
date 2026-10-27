# TOOL-dLinkedLibrary-79 — the CI census reads the credentials of every block that applies to a job, file-level blocks included

**Status:** OPEN · rev-1 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 31 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-80 |
| [2026-10-27-build-TOOL-dLinkedLibrary-79-deviation-791.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-79-deviation-791.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 65 to 74
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md`) confirmed
finding **id 36 at HIGH**, report item **H5**. No other id shares the item.

`TOOL-dLinkedLibrary-74` S18 widens `TOOL-dLinkedLibrary-63` S3's credential rule to every line of a job,
its `variables:`, an Azure step's `env:`, and GitLab's `secrets:` and `id_tokens:` on a job. It names one
instance where the class is meant: nothing reaches a top-level `variables:` in GitLab or Azure, GitLab's
`default:` (63 S1 applies it to every job, and GitLab admits `id_tokens:` there), or Azure's pipeline- and
stage-level `variables:`. GitHub has the same gap: `TOOL-dLinkedLibrary-51` S5 refuses a `secrets.`
reference on "any line of the job", and a workflow-level `env:` is not one. A file with a top-level
`variables: { TWINE_PASSWORD: $PYPI_TOKEN }` and a job running only `./release.sh` has no credential name
on any line of its own, so it grades `importable`.

This unit names every block that applies to a job in each dialect and reads the credential rule over all
of them. It repairs `TOOL-dLinkedLibrary-74` and builds one step after it (order 31).

## 2. Scope (IN)

- **S1** — The blocks that apply to a job. In `tools/memory-tree/adopt_program.py`'s `ci-job` class, the
  credential rule reads, for each job, its own lines and every block that applies to it:

  | File | Blocks applied to every job, beside the job's own lines |
  |---|---|
  | `.github/workflows/*.yml`, `*.yaml` | the workflow-level `env:` |
  | `.gitlab-ci.yml` | the top-level `variables:`, and `default:` with its `id_tokens:` and `secrets:` |
  | `azure-pipelines.yml` | the pipeline-level `variables:`, and the `variables:` of the stage holding the job |

  Observed by AC1 to AC3.
- **S2** — What is a credential there. In a `variables:` or `env:` block a credential is a variable whose
  NAME matches 63 S3's words (`token`, `secret`, `password`, `passwd`, `key`, `credential`, `auth`,
  ignoring case), or one whose value references such a name in 63 S3's forms; an Azure list item `- name:
  <NAME>` names its variable. For GitHub, a `secrets.` reference other than `secrets.GITHUB_TOKEN` in the
  workflow-level `env:` is read as 51 S5 reads one on a job line. A GitLab `default:` carrying `id_tokens:`
  or `secrets:` is read as 74 S18 reads one on a job. An Azure `variables:` item `- group: <name>`, at any
  level S1 names or on the job, links a variable group whose values live in the forge's library, outside
  the file, so it is a credential the census cannot read, named `group <name>`. Observed by AC1 to AC3.
- **S3** — The refusal. A credential in a block of S1 refuses every job that block applies to, each
  reading `refused: unreadable credentials <NAME>`, `<NAME>` the variable or the key, or for GitHub 51 S5's
  `refused:` reason; a stage-level hit refuses that stage's jobs only. Observed by AC1 to AC4.
- **S4** — The plants, cases of `adopt_program.py --fixture --plant ci-census`, each a scratch tree of its
  own: a GitLab file whose top-level `variables:` maps `TWINE_PASSWORD: $PYPI_TOKEN` beside a job running
  `./release.sh`; a GitLab file whose `default:` carries `id_tokens:` beside a job running `npm test`; an
  Azure file whose pipeline-level `variables:` maps `NUGET_API_KEY: $(nugetKey)` beside a job running
  `./publish.sh`; an Azure file with three stages, the first holding a `variables:` item `- name:
  DEPLOY_TOKEN`, the second a `variables:` item `- group: release-vars` and the third no `variables:`, each
  with a job running `npm test`; a GitHub workflow whose workflow-level `env:` maps `NPM_TOKEN: ${{ secrets.NPM_TOKEN }}` beside a job running `./release.sh`; and a GitLab file whose
  top-level `variables:` maps only `NODE_ENV: test` beside a job running `npm test`. Observed by AC1 to
  AC4.
- **S5** — The page. `help/adopt.md`'s census section carries the sentence "Credentials in a top-level,
  pipeline-level or stage-level `variables:` block, in GitLab's `default:`, or in a workflow-level `env:`
  refuse every job that block applies to." Observed by AC5.

## 3. Non-goals (OUT)

- Reading a forge's protected or masked variable settings: outside the repository, as 63 §4 rejects.
- The indirection keys under `default:`: `TOOL-dLinkedLibrary-76`.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-74` — S18's widened credential rule and AC14's plants, which S1 to S3 extend to every block applying to a job (id 36)

## 4. Design

### Evidence

- 74 S18: the rule reads "every line of a job, `variables:`, an Azure step's `env:`, and GitLab's
  `secrets:` and `id_tokens:`"; AC14 plants only step-level and job-level carriers.
- 63 S1 applies `default:`'s script keys to every GitLab job; 63 S3 matches a reference `$NAME`, `${NAME}`,
  `$(NAME)`, `$env:NAME` or `%NAME%`.
- 51 S5 refuses a `secrets.` reference on "any line of the job", and grants on "it or its workflow", so a
  workflow-level grant is read and a workflow-level secret is not.

### A GitLab file after S1 to S3

```yaml
variables:
  TWINE_PASSWORD: $PYPI_TOKEN    # S2: a credential by name and by reference
release:
  script: ./release.sh           # S3: refused, unreadable credentials TWINE_PASSWORD
```

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4
- `help/adopt.md`: S5

### Alternatives rejected

- **Refusing only a job whose own lines reference the file-level variable.** A release script reads the
  variable from its environment without naming it, which is the case this finding exists for.
- **Refusing every job of a file holding any `variables:` block.** It refuses `NODE_ENV: test`, which names
  no credential; S4's last plant keeps that job `importable`.

## 5. Production-readiness checklist

- security — closes the import of a job whose credentials arrive from a block outside its own lines; deny
  by default.
- perf / scale — each file-level block is read once and applied to its jobs.
- error / empty / loading states — unchanged from 63.
- observability — each refusal names the variable or key.
- risks — a test pipeline with a file-level token variable refuses every job; the owner may rule a job in.
- testing — S4's plants under `adopt_program.py --fixture`.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — `help/adopt.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, the GitLab job
  running `release.sh` beside a top-level `TWINE_PASSWORD` reads `refused: unreadable credentials
  TWINE_PASSWORD`, and the GitLab test job beside a `default:` carrying `id_tokens:` reads `refused:
  unreadable credentials id_tokens`.
  Red when: a credential delivered outside the job's own lines reads `importable`.
- **AC2** — When the same plant runs, the Azure job beside a pipeline-level `NUGET_API_KEY` reads `refused:
  unreadable credentials NUGET_API_KEY`, the job of the stage carrying `DEPLOY_TOKEN` reads `refused:
  unreadable credentials DEPLOY_TOKEN`, the job of the stage linking `release-vars` reads `refused:
  unreadable credentials group release-vars`, and the job of the third stage reads `importable`.
  Red when: a pipeline- or stage-level credential or a variable group passes, or a stage's credential
  reaches another stage's job.
- **AC3** — When the same plant runs, the GitHub job beside a workflow-level `env:` mapping
  `secrets.NPM_TOKEN` reads `refused:`.
  Red when: a workflow-level secret reads `importable`.
- **AC4** — When the same plant runs, the GitLab test job beside a top-level `variables:` mapping only
  `NODE_ENV` reads `importable`.
  Red when: a file-level block naming no credential refuses its jobs.
- **AC5** — When `grep -n 'workflow-level'` runs over the help page `adopt.md` (its path in Files touched)
  at this pass's tip it prints S5's sentence, and over the page as unit 74's pass leaves it, read with
  `git show`, it prints nothing.
  Red when: the page names the job-level carriers alone.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 AC4 · the `ci-census` plant's six file-level, `default:` and stage-level trees, the failing case staged by 74 S18's job-only credential read · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 65 to 74, id 36 (HIGH, item
  H5).

## 10. Reuse audit

The seam extended is 63 S3's credential rule as 74 S18 widens it, and 51 S5's `secrets.` rule, inside
`TOOL-dLinkedLibrary-8`'s `ci-job` class in `tools/memory-tree/adopt_program.py`: one rule, more blocks
read. `python tools/codebase-map/reuse_lookup.py "refuse a ci job whose credentials sit in a file level
variables block"` ranked `CensusRefused`, `ScopeRefused`, `corpus_files` and `ask_filed_in`, none a CI
reader, so no existing seam fits beyond the census being extended.

Recall terms used: `python tools/memory-recall/query.py "how does a census refuse a ci job whose text or credentials come from a block it does not read" --terms "census ci-job refused opaque step credentials default variables block scalar fold header promoted"`
