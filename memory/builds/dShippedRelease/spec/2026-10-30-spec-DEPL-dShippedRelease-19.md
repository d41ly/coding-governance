# DEPL-dShippedRelease-19 — the integrations `import` of an adopter's CI jobs as legs: only a job ruled `import`, test jobs only, each through an adapter row

**Status:** OPEN · rev-2 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 29 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0429@78bd7623 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-3-reuse-scout-c.md](../build/2026-10-30-build-DEPL-dShippedRelease-3-reuse-scout-c.md) | research | DEPL-dShippedRelease-3 DEPL-dShippedRelease-6 DEPL-dShippedRelease-8 DEPL-dShippedRelease-15 DEPL-dShippedRelease-22 DEPL-dShippedRelease-26 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md](../reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-10 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-31 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-13 DEPL-dShippedRelease-4 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-6 DEPL-dShippedRelease-27 DEPL-dShippedRelease-5 DEPL-dShippedRelease-30 DEPL-dShippedRelease-3 DEPL-dShippedRelease-25 DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-20 DEPL-dShippedRelease-17 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-18 DEPL-dShippedRelease-24 DEPL-dShippedRelease-8 DEPL-dShippedRelease-26 DEPL-dShippedRelease-22 DEPL-dShippedRelease-9 |

<!-- /gen:spec-records -->

## 1. Goal

An adopter's own CI jobs are a practice the owner rules on, and nothing turns a ruling into a leg. This
unit imports a job as a leg only when its ruling record says `import`, only when it is a test job, and
only through an adapter row carrying its grant and secret reference. A job that deploys, publishes or
pushes is refused, and a registration check keeps all of that true after the import. It owns no node.
It reads `record-kind.census`, `record-kind.ruling` and `point.flow.leg-pack`.

## 2. Scope (IN)

Build-run preconditions, specced and DEFERRED at base `f4597719`: TOOL-dLinkedLibrary-8 (`census` and
`ruling`, the `ci-job` class, `scan_practices`, `CI_REFUSE_PATTERNS`), TOOL-dLinkedLibrary-51 and -63 (the
reader and the patterns they widen), TOOL-dWitnessedBar-6 (`read_remote_verdict`, `fetch_api`),
TOOL-dWitnessedBar-11 and -28 (the leg factory and overlay `[[gate-leg]]` rows), TOOL-dWellOiledMachine-17
(`check_adapter_grant`, `read_secret_ref`) and PLAY-dOrderedCharter-15 and -46 (the overlay's write door).

- **S1** — The ruling read. `read_job_ruling(root, job)` in `tools/integrations/ci_import.py` returns the
  `Ruling` value of the `ruling` record whose `Subject` is that job's `census` record of class `ci-job`,
  or `None`. It reads records through the record kit's own reader, never by parsing their prose here.
  Observed by AC1 and AC2.
- **S2** — The plan. `python ci_import.py plan` prints one line per `ci-job` census record, in rank order,
  `import` or `skipped · <why>`, and writes nothing. A job is `import` only when all four hold, tested in
  this order: its steps at HEAD match no `CI_REFUSE_PATTERNS` entry and its census `State` is `importable`;
  its ruling is `import`; `check_test_job(steps)` holds; and its file is a GitHub workflow. Observed by
  AC1, AC2, AC3, AC4, AC9 and AC10.
- **S3** — The test-job predicate. `check_test_job(steps)` holds when at least one step's `run` matches
  `CI_TEST_PATTERNS`, a closed table of test runners in this module, and no step fails S2's first test.
  A job it cannot place is `skipped · not a test job`, so the rule denies by default. Observed by AC4.
- **S4** — The adapter row. Each imported job is one `[[adapter]]` row of `.governance/ci-imports.toml`,
  `point = "point.flow.ci-imports"`, with the header `check_adapter_header` grades: `kind = "ci-job"`, its
  `grant` with the `secret` reference nested in it, `witness-source`, `probe` and `fallback`, and two fields
  of its own, `workflow` and `job`. `ci-job` joins `ADAPTER_KINDS` in `tools/integrations/adapters.py`,
  whose list DEPL-dShippedRelease-15 S2 leaves to each later kind. The `[[point]]` row goes in
  `tools/runtime/points.toml`, and the word joins `declares` of `layer.flow` and `uses` of
  `layer.integrations` in `tools/playbook/layers.toml`. An adopter's rows stay in the adopter's file
  because `update` overwrites `points.toml` and shipped files name no adopter. Observed by AC5.
- **S5** — The import. `python ci_import.py import <job>` refuses unless the plan reads `import`. It writes
  S4's row, runs `check_adapter_header` and `check_adapter_grant` on it, and writes the leg as an overlay
  `[[gate-leg]]` row with `pack = "adopter"`, tag `leg.adopter.ci-<job>` and argv `python
  {prefix}/integrations/ci_import.py leg <job>`, through the overlay's write door
  (PLAY-dOrderedCharter-15 S2, PLAY-dOrderedCharter-46 S4). A refused row leaves neither file changed.
  Observed by AC5.
- **S6** — The leg. `python ci_import.py leg <job>` reads the job's remote conclusion through
  `read_job_conclusion(row, sha)`, at HEAD and then at each first-parent ancestor up to `JOB_WALK`, stopping
  at the first SHA holding a run. It maps the read to `GREEN`, `RED`, `NONE` or `DEAD PROBE`, the secret
  resolved into this process alone by `read_secret_ref`, and exits 0 only on `GREEN`, naming the SHA and how
  far behind it sits. It runs nothing of the job's. `--rows <file>` reads saved rows in place of the
  network. Observed by AC7.
- **S7** — The registration check, `python ci_import.py check`, the leg `ci import registration` of
  `tools/integrations/kit.toml`. It reds, both ways: a planted deploy job, meaning an imported job whose
  steps at HEAD now match a refuse pattern; an imported leg with no adapter row; a row with no grant; a row
  whose job no `import` ruling names; and a row with no leg. Observed by AC6 and AC8.
- **S8** — The docs. `help/ci-import.md`, with its row in `help/README.md`, states the order: census, ruling,
  `plan`, `import`, and what a leg reads. Observed by AC11.

## 3. Non-goals (OUT)

- The census, its `ci-job` class, the ruling verbs and the refusal at `adopt practices --rule`:
  TOOL-dLinkedLibrary-8's. This unit reads them and re-checks at HEAD, because a job can gain a step.
- Running a job's steps on a node (§8 F2).
- `translate`, `alongside` and every other ruling. Each reads `skipped`, and `test.seed` owns what a ruling
  other than `import` does.
- CI systems other than GitHub Actions (§8 F4), though the census lists them.
- Emitting CI: DEPL-dShippedRelease-8's.

### Edges

- **consumes-from** `DEPL-dShippedRelease-15` — `check_adapter_header`, which grades S4's row; without it no import can register
- **consumes-from** external — TOOL-dLinkedLibrary-8's records and `CI_REFUSE_PATTERNS`, TOOL-dWitnessedBar-6's `fetch_api`, TOOL-dWitnessedBar-28's overlay legs and TOOL-dWellOiledMachine-17's grant check; without them `plan` has nothing to read and `import` nowhere to write
- **hands-off** `DEPL-dShippedRelease-78` — the job reader and its leg, which the minors batch repairs (review ids 13, 51, 62, 63, 107)

## 4. Design

### One job's path

```text
adopt.census → census record, State importable | refused: <why>
adopt.practices (owner) → ruling record: import | translate | alongside | ...
ci_import.py plan → import | skipped · <why>
ci_import.py import <job> → .governance/ci-imports.toml row + overlay [[gate-leg]] row
the bar → ci_import.py leg <job> → the job's remote conclusion
ci_import.py check → the two files, the rulings and HEAD's steps agree, both ways
```

### Why a remote conclusion

A leg reads the conclusion the job already reached on the host. `read_held_runs` and `read_remote_verdict`
are the shape: a bounded GET, keyed by SHA, whose failed read is a dead probe and never green. The grant
and the secret reference exist for exactly this read, and the header's `witness-source` and `probe` have
no meaning on a local re-run. The cost is timing: a prepared merge has no run yet, so the leg walks back to
the nearest SHA that has one and names how far. A job red on the default branch therefore holds a landing,
and a job's verdict on the SHA being landed arrives after it, as `deploy.core` reads a post-landing verdict.

`fetch_api` carries no credential (TOOL-dWitnessedBar-6 S7). The build adds a `token=None` keyword to it,
used by this reader alone, so the one bounded GET stays one and its other callers keep their bytes.

### Data model

```toml
# .governance/ci-imports.toml
[[adapter]]
point = "point.flow.ci-imports"
name = "unit-tests"
kind = "ci-job"
tenancy = "project"
retention = "none"
region = "local"
grant = { service = "github", scopes = ["actions:read"], secret = "ci-read" }
witness-source = "github-actions run by head_sha, the workflow and job below"
probe = ["python", "{prefix}/integrations/ci_import.py", "probe", "unit-tests"]
fallback = "the job stays in CI, alongside"
workflow = ".github/workflows/test.yml"
job = "unit-tests"
```

### The test table

`CI_TEST_PATTERNS` is a closed tuple of command prefixes, seeded with `pytest`, `python -m pytest`,
`python -m unittest`, `npm test`, `npm run test`, `pnpm test`, `yarn test`, `go test`, `cargo test`, `dotnet
test`, `mvn test`, `gradle test` and `bundle exec rspec`. A runner it lacks reads `skipped`, and its remedy
is one row here, or `translate`. This is the same shape as `CI_REFUSE_PATTERNS`, and it deliberately sits
beside the import that uses it rather than in the census, which classes practices and not tests.

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `ci_import.py`, `plan`, `import`, `leg`, `probe`, `check` | module and verbs | `tools/integrations/` |
| `read_job_ruling`, `check_test_job`, `read_job_conclusion`, `check_import_registration`, `render_import_row` | functions | `ci_import.py` |
| `CI_TEST_PATTERNS`, `JOB_WALK` | constants | `ci_import.py` |
| `.governance/ci-imports.toml` | adopter-owned file | an adopter's tree |
| `point.flow.ci-imports`, kind `ci-job` | point and adapter kind | `tools/runtime/points.toml`, `ci_import.py` |
| `ci import registration` | gate leg | `tools/integrations/kit.toml` |

`lexicon.py --suggest <name> --as py.function` printed OK for `read_job_ruling`, `check_test_job`,
`read_job_conclusion`, `check_import_registration` and `render_import_row` on 2026-10-30. `JOB_WALK` is 32
commits, PINNED here as a design choice.

### Migration

Additive. No file exists until an owner's ruling and an `import`.

### Rollout

Dark: gov's tree holds no adoption build, so `plan` prints `0 ci-job census records` and the leg reads the
empty file as `searched-empty`. Every adopter stays there until its owner rules.

### Files touched (estimate)

- `tools/integrations/ci_import.py`
- `tools/integrations/adapters.py`
- `tools/integrations/kit.toml`
- `tools/runtime/points.toml`
- `tools/playbook/layers.toml`
- `tools/run-gates/remote_verdict.py`, the `token` keyword of `fetch_api`
- `tools/gate-legs.json`, rendered from the kit's `[[gate_leg]]` rows by `leg_factory.py --write`
- `help/ci-import.md`
- `help/README.md`

### Alternatives rejected

- **Re-running a job's `run` lines at the bar.** The test: a workflow's `uses:` steps and `${{ }}` expressions
  have no local meaning, and a resolved secret would reach adopter step text on a node. That widens a
  surface (veto 3) and fails the header's `witness-source` (§8 F2).
- **Deciding "test job" by the job's name.** The test: a job named `test-and-publish` passes a name test, and
  the census's own class is by steps, so the predicate reads steps.
- **Adapter rows in `tools/runtime/points.toml`.** The test: the brief's pin C11 states that update
  overwrites that file, and `tools/govkit/govkit.py:3731`'s arm 10 refuses an adopter's name in a shipped file.

## 5. Production-readiness checklist

- security: denied by default at four points, re-checked at HEAD by a leg. The secret is a reference, resolved
  into one process, sent only to the fixed API host under `fetch_api`'s no-redirect GET, and never logged. The
  grant is read-only. An import writes one adopter file and one overlay row through its door.
- perf / scale: one bounded GET per SHA walked, at most `JOB_WALK`, per imported leg per bar.
- error / empty / loading states: no census is `0 ci-job census records` and no leg. A failed read is `DEAD
  PROBE`, a red leg, never green. A walk finding no run is `NONE` and red, naming the walk.
- observability: `plan`'s one line per job with its reason, and the leg's line naming the state, SHA and distance.
- risks: an imported leg depends on a host being up, so an outage reds the adopter's bar until it clears. That
  is the owner's trade at the ruling, stated on the help page. The leg's verdict lags the SHA being landed.
- testing: the probes of §6 and the module's in-file arms (§7).
- migration: §4 "### Migration".
- user docs: `help/ci-import.md`, S8.

## 6. Acceptance criteria

- **AC1** — When `python ci_import.py plan --root <fixture>` runs on planted `census` and `ruling` records and a
  workflow, a job ruled `import` whose step runs `pytest` prints `import`.
  Red when: no path reaches `import`, which would make every other criterion pass by refusing all.
  fixture: a scratch repository under `%TEMP%` with the two records, after TOOL-dLinkedLibrary-8 is built.
- **AC2** — When `python ci_import.py plan --root <fixture>` runs with one job ruled `alongside` and one
  unruled, each prints `skipped` with its reason, and the fixture holds no `ci-imports.toml`.
  Red when: a job is imported on anything but an `import` ruling.
- **AC3** — When `python ci_import.py plan --root <fixture>` runs with a job ruled `import` whose workflow then
  gained a `docker push` step, it prints `skipped · refused`, and `python ci_import.py import <job>` exits 1.
  Red when: the census's old `State` is trusted over the steps at HEAD.
- **AC4** — When `python ci_import.py plan --root <fixture>` runs with a job ruled `import` whose only step runs
  `eslint .`, it prints `skipped · not a test job`.
  Red when: a lint or build job imports, the clause's "test jobs only".
- **AC5** — When `python ci_import.py import <job>` runs on AC1's job, the row passes `check_adapter_header` and
  the overlay holds a `[[gate-leg]]` row whose tag is `leg.adopter.ci-<job>`. With the row's `secret` planted as
  a credential-shaped value rather than a reference, it exits 1 and neither file changes.
  Red when: a secret value reaches a tracked file, or a half-written import survives a refusal.
- **AC6** — When `python ci_import.py check --root <fixture>` runs on AC5's result with a `git push` step planted
  in the job, it exits 1 naming the job and the pattern.
  Red when: a registration check passes a planted deploy job, the clause's seen-red case.
- **AC7** — When `python ci_import.py leg <job> --rows <file>` runs on planted rows, a `success` conclusion exits 0
  naming the SHA; `failure` exits 1; a dead read exits 1 printing `DEAD PROBE`; and no run within `JOB_WALK`
  exits 1 printing `NONE`. A run one commit behind HEAD exits 0 and prints `1 behind`.
  Red when: a dead probe or an absent run reads green, or the walk stops at HEAD.
- **AC8** — When `python ci_import.py check --root <fixture>` runs with the leg row kept and the adapter row
  deleted, then the reverse, then with the ruling record's value changed, each exits 1 naming the job.
  Red when: an imported leg with no grant row passes, retrofit's stated case.
- **AC9** — When `python ci_import.py plan --root <fixture>` runs on a job of `.gitlab-ci.yml` ruled `import`, it
  prints `skipped · host not registered`.
  Red when: a job on a host with no reader imports and then reads a dead probe forever.
- **AC10** — When a grep of `ci_import.py` for `CI_REFUSE_PATTERNS` runs after the build, every hit reads the
  table through `adopt_program.py`, and none spells a pattern.
  Red when: the refusal list is copied, so a widening by TOOL-dLinkedLibrary-51 misses the import.
  fixture: the tree after the build.
- **AC11** — When `grep -n 'ci-import.md' help/README.md` runs, it prints the page's row.
  Red when: an owner has no page for the order.

## 7. Gates

`measure-legs selftest` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `govkit acceptance matrix` · `playbook render selftest`

New arm: tools/integrations/ci_import.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 · planted census and ruling records, a workflow with each kind of job, a deleted row, saved conclusions of each state · none

The leg `ci import registration` is new and is named here rather than on the leg line above, which reads names
the manifest already holds. What these do not check: that a test runner's name in a step means it tests
anything, that a job's verdict covers the SHA being landed, or any host but GitHub.

## 8. Open questions

- **F1 — How is "test job" decided (scout C F7)?** The census classes only `refused`, so a lint or build job can be
  ruled `import` (dLinkedLibrary-8:246). Options: (a) a closed table of test commands over the job's steps; (b) the
  job's name; (c) the owner's ruling alone. (b) passes `test-and-publish`, and (c) fails the clause's "test jobs
  only", which it states apart from the ruling. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, denied by
  default, as retrofit:350 states CI jobs are. widens: none · relaxes: none
- **F2 — Does a leg re-run the job or read its remote conclusion (scout C F6)?** Options: (a) a local re-run of its
  `run` lines; (b) the conclusion by SHA through the adapter row. (a) runs step text with a resolved secret on a node
  (veto 3), and `uses:` steps have no local meaning. RESOLVED (agent, 2026-10-30, delegated): (b), rung 3, with the
  walk of S6 because a prepared merge has no run. widens: none · relaxes: none
- **F3 — Where do an adopter's adapter rows live?** Options: (a) `tools/runtime/points.toml`, which `update` overwrites;
  (b) `.governance/ci-imports.toml`; (c) overlay rows, whose composition knows no `[[adapter]]` table. RESOLVED
  (agent, 2026-10-30, delegated): (b), rung 3. widens: none · relaxes: none
- **F4 — Which hosts?** The census reads three, and the validator states GitHub Actions is the only grammar ever
  measured (`tools/govkit/govkit.py:6003`). RESOLVED (agent, 2026-10-30, delegated): GitHub Actions, the others read
  `skipped · host not registered`, rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft.
- rev-2 · 2026-10-30 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (units 78); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is TOOL-dLinkedLibrary-8's `ci-job` census class and `ruling` kind, not built, reused for job
discovery and rulings, with `CI_REFUSE_PATTERNS` reached through `resolve_kit_dir("memory-tree", "adopt_program.py",
here)` and no copy. `reuse_lookup.py "import a foreign CI job as a gate leg with a grant"` ranked `legs`, `leg`,
`check_gate_wall` and `parse_grants`, each a name-stem neighbour, and none is an import seam; at HEAD
`tools/govkit/census.py` answers a different question, as dLinkedLibrary-8 says, and nothing exists for this. Scout
C's disagreement 10 is §8 F1, and its retrofit:354 citation reads true at `2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md:355`:
an imported leg with no grant row reds, which AC8 observes. The scout's `read_job_ruling(census_record, job)` is
spelled `read_job_ruling(root, job)` here, because the census record is what it finds. Candidates rejected and their
tests are under §4 "### Alternatives rejected".

Recall terms used: `python tools/memory-recall/query.py "how are an adopter's CI jobs imported as gate legs" --terms "ci-job census ruling import legs grant secret refused deploy publish push registration check"`
