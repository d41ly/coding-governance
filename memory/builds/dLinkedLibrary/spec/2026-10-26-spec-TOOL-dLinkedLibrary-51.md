# TOOL-dLinkedLibrary-51 — the CI census reads every workflow file, every line a job runs, and refuses a job that publishes, pushes or holds a write grant

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 21 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 |
| [2026-10-26-build-TOOL-dLinkedLibrary-51-deviation-511.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-51-deviation-511.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
finding **id 67 at HIGH**, report item **R15**. No other id shares the item.

`TOOL-dLinkedLibrary-8` §4 "The census" reads only `.github/workflows/*.yml`, parses jobs by indentation
with no rule for block scalars, and refuses on six substrings (`CI_REFUSE_PATTERNS`). A `.yaml` workflow
is missed, a `run: |` block's later lines are unread, and `git -C x push`, `yarn publish`, `pnpm publish`,
`cargo publish` and `terraform apply` match no pattern. An owner ruling `import` on such a job hands
dShippedRelease a job that pushes or publishes as a gate leg, defeating the deny-by-default rule at the
one place unit 8's §5 prices it.

This unit makes the census read every workflow file and every line a job runs, normalise the verbs it
matches, refuse the publish and apply verbs of common package managers and infrastructure tools, and
refuse any job holding a write grant or reading a secret. It repairs `TOOL-dLinkedLibrary-8` and builds
one step after it (order 21).

## 2. Scope (IN)

- **S1** — The files. The `ci-job` class reads `.github/workflows/*.yml` and `.github/workflows/*.yaml`,
  beside `.gitlab-ci.yml` and `azure-pipelines.yml` as before. Observed by AC1.
- **S2** — The lines a job runs. Each job's text is every line of its `steps`, every line of a block
  scalar (`run: |`, `run: >`, with or without a chomping indicator) up to the first line indented no
  deeper than its key, and every job-level and step-level `uses:`. Observed by AC2.
- **S3** — Normalisation before matching. A command's leading options are folded before its verb is
  matched: `git -C <dir> push`, `git -c <k>=<v> push` and `git --git-dir=<d> push` read as `git push`;
  `npx`, `pnpm dlx` and `yarn dlx` prefixes are stripped. Observed by AC3.
- **S4** — The refusal list. `CI_REFUSE_PATTERNS` (`tools/memory-tree/adopt_program.py`) holds, beside its
  six: `yarn publish`, `yarn npm publish`, `pnpm publish`, `cargo publish`, `gem push`, `poetry publish`,
  `mvn deploy`, `gradle publish`, `helm push`, `terraform apply`, `pulumi up`, `kubectl apply`,
  `aws s3 cp` and `aws s3 sync`. Observed by AC3.
- **S5** — Grants and secrets. A job refuses, `refused: <why>`, when it or its workflow grants
  `permissions: write-all`, or any `<scope>: write` under `permissions:`, or when any line of the job
  references `secrets.` other than `secrets.GITHUB_TOKEN` under a read-only grant. Observed by AC4.
- **S6** — The plants, cases of `adopt_program.py --fixture --plant ci-census` (`TOOL-dLinkedLibrary-8`
  S11): a `.yaml` workflow whose job runs `npm publish`; a `run: |` block holding `npm publish` on its third
  line; a `yarn publish` job; a `git -C x push` job; a job with `permissions: contents: write`; a job
  reading `secrets.NPM_TOKEN`; each `refused`; and a plain test job, `importable`. Observed by AC1 to AC5.

## 3. Non-goals (OUT)

- A YAML library: the census stays a text reader, as `TOOL-dLinkedLibrary-8` §5 prices it; S2 states the
  block-scalar rule the indentation reader lacked.
- Importing a job as a leg: dShippedRelease's.
- A complete list of every publishing tool: the list is a table this unit owns and extends, and S5's
  grant and secret rules refuse a publishing job whose verb the list misses but whose credentials it
  needs.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-8` — `scan_practices`, the `ci-job` class and `CI_REFUSE_PATTERNS`, which S1 to S5 widen, and its `--fixture` plants, which S6 extends (id 67)
- **hands-off** `TOOL-dLinkedLibrary-63` — S2's block-scalar reader, S3's normalisation and `CI_REFUSE_PATTERNS`, which unit 63 extends to GitLab and Azure (id 27 of the spec audit of units 37 to 53)
- **hands-off** `TOOL-dLinkedLibrary-64` — S5's grant and secret rules, which unit 64 completes for an absent `permissions:` key (id 28 of the spec audit of units 37 to 53)

## 4. Design

### Evidence

- `TOOL-dLinkedLibrary-8` §4 "The census": `ci-job` reads "each job of `.github/workflows/*.yml`,
  `.gitlab-ci.yml` and `azure-pipelines.yml`, read by indentation without a YAML library; `refused` when a
  step's `run` or `uses` matches `CI_REFUSE_PATTERNS` (`git push`, `npm publish`, `twine upload`, `docker
  push`, `gh release`, `deploy`)".
- The skeptic's note: `gh release create` and `actions/deploy-pages` already match `gh release` and
  `deploy`.
- This repository's own workflow, `.github/workflows/remote-ci.yml`, is the one tracked `ci-job` source at
  base.

### A job's text after S2 and S3

```yaml
release:
  permissions:
    contents: write          # S5: refused, a write grant
  steps:
    - run: |
        npm ci
        npm test
        npm publish          # S2: read; S4: refused
    - run: git -C dist push  # S3: read as `git push`
```

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S6
- `help/adopt.md`: the census section's refusal rules

### Alternatives rejected

- **Refusing every job that reads any secret.** A test job reading a read-only token for a private
  registry is common; S5 refuses the write grant and named secrets, the credentials a publish needs.
- **A YAML parser.** It is a new dependency in a kit that ships none (veto 2).

## 5. Production-readiness checklist

- security — closes the import of a publishing or pushing job; the census still executes nothing.
- perf / scale — one more glob and the block-scalar lines, read once per job.
- error / empty / loading states — a workflow file that does not read as jobs is listed `refused:
  unreadable`, never `importable`.
- observability — each refused job names the matched verb, grant or secret.
- risks — a verb neither on the list nor needing a grant or secret stays importable; the owner's ruling
  is still required to import any job.
- testing — S6's plants under `adopt_program.py --selftest`.
- migration — none: a census record already written keeps its state; a re-run at a new SHA re-reads.
- user docs — `help/adopt.md`'s census section names the refusal rules.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, the job of the
  `.yaml` workflow reads `refused: npm publish`.
  Red when: a `.yaml` workflow is not censused.
- **AC2** — When the same plant runs, the job whose `run: |` block holds `npm publish` on its third line
  reads `refused: npm publish`.
  Red when: a block scalar's later lines are not read.
- **AC3** — When the same plant runs, the `yarn publish` job and the `git -C x push` job each read
  `refused` naming `yarn publish` and `git push`.
  Red when: an option-prefixed or unlisted publish verb reads `importable`.
- **AC4** — When the same plant runs, the job granted `contents: write` and the job reading
  `secrets.NPM_TOKEN` each read `refused` naming the grant or the secret.
  Red when: a job holding write credentials reads `importable`.
- **AC5** — When the same plant runs, its plain test job reads `importable`.
  Red when: the widened rules refuse a job that neither publishes, pushes nor holds a write grant.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 AC4 AC5 · the `ci-census` plant's seven jobs, the failing case staged by the rev-1 reader, `*.yml` only, first line of a block, six patterns · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, id 67
  (HIGH, item R15), on the skeptic's corrected fix.
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-63, TOOL-dLinkedLibrary-64, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

The seam extended is `TOOL-dLinkedLibrary-8`'s `scan_practices` and its `CI_REFUSE_PATTERNS` table in
`tools/memory-tree/adopt_program.py`; `tools/govkit/census.py:1-26` shows the read-only census shape that
unit keeps. `python tools/codebase-map/reuse_lookup.py "refuse a workflow job that publishes or pushes"`
ranked `load_workflows` (`tools/roles/roles_lib.py`, the roles kit's workflow entries, not CI files) and
three refusal classes, none a CI reader, so no existing seam fits beyond the census being repaired.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`
