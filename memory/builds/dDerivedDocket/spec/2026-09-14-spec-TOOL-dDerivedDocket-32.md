# TOOL-dDerivedDocket-32 — remote CI on every push

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 32

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

Every layer of the straggler guard runs on some node's hooks, and a `--no-verify` push skips all of
them. Remote CI is the one layer no node can skip (design §18r.2 L7), and the owner ruled that it
runs the transition audit and check 9 on every push to main (D11-b), detecting after landing because
landing stays a direct push (D11-c). It also carries a scheduled run of the held suites and a per-sha
bar verdict (D12-i12), which is the periodic signal a held suite has never had. The owner confirmed
the push credential has `workflow` scope, so the workflow file is committed and pushed in this build.

## 2. Scope (IN)

- **S1** One workflow file, `.github/workflows/remote-ci.yml`, so the charter's CI placeholder
  derives exactly one path. Workflow-level `permissions: contents: read`. Only GitHub-owned
  `actions/*` actions, each pinned by a full 40-hex commit sha with its tag in a comment. Every
  checkout uses `fetch-depth: 0` and `persist-credentials: false`, after a step setting
  `core.autocrlf false`. Every job runs on `windows-latest` under `shell: bash`. Observed by AC1,
  AC2 and AC7.
- **S2** Job `history-audit`, on every push to the default branch: runs
  `bash tools/memory-tree/check-memory-hygiene.sh` over the full clone, which carries check 9 and the
  transition audit's check 25, and then asserts that its output carries check 25's line, dormant or
  examined. A job that never reached check 25 cannot pass. Observed by AC3.
- **S3** Job `bar`, on every push to the default branch: runs the full bar,
  `GATE_FULL=1 bash tools/run-gates/run-gates.sh`, with `GATE_WALL` set below the job's own timeout,
  so the runner's wall fires and names the outstanding legs before the platform kills the job. The
  job's conclusion is the per-sha verdict, and the run record under the git dir is uploaded as an
  artifact named by the sha. Observed by AC4.
- **S4** Jobs `held-plan` and `held`, on a daily schedule and on `workflow_dispatch`: the plan job
  derives the kit directories from the argv column of `tools/run-gates/selftest-budgets.txt`, and a
  matrix job per directory runs `bash tools/run-gates/run-selftests.sh --kit <dir> --sweep`,
  uploading its output as an artifact named by the sha and the directory. The job is red when a
  suite fails or when its directory selected no suite. Observed by AC5.
- **S5** The file's contract, observed before landing by hand and recorded in the unit's journal:
  every checkout carries `fetch-depth: 0`; every `uses:` is an `actions/` action pinned by a 40-hex
  sha; `permissions` grants `contents: read` and nothing more; and the bar job's `GATE_WALL` is below
  its timeout. Each observation is a staged break on a scratch copy of the file, confirmed to fail,
  then removed. No permanent gate grades the file (§8 F2). Observed by AC1, AC2 and AC4.
- **S6** The declarations the new file owes: `.github/workflows/*.yml` pinned to LF in
  `.gitattributes`, and `yml::dark` added to `LANGS` in `.lexicon.conf`, whose undeclared-extension
  refusal would otherwise red. The file sits outside `tools/govkit/registry.toml`'s declared surface
  and outside every codebase-map inventory, so it owes neither a registry row nor a claim.
  Observed by AC6 and AC7.
- **S7** The charter and its answers. `.governance/deploy.toml` drops its `ci_file` answer, so a
  deleted workflow makes the render refuse instead of reviving "none yet". `AGENTS.md`'s rendered
  region is regenerated, and its merge-bar section's sentence calling remote CI a follow-up is
  replaced by one naming the workflow, its jobs, and that it detects after landing and is no
  required check. The header of `tools/run-gates/run-selftests.sh` stops saying nothing runs the
  held suites automatically. Observed by AC8.

## 3. Non-goals (OUT)

- No GitHub setting. Marking a job as a required check and disallowing squash and rebase merges are
  the owner's acts (D11-b), and the brief rules settings out of this build.
- No blocking before landing. Landing stays a direct push (D11-c); a `--no-verify` push lands and CI
  reds after it, which is design §18r.6 hole 2 as the owner accepted it.
- No consumer of the published verdicts. Pointing red attribution at a per-sha CI verdict instead of
  a local re-run at the remote tip is a later change to that unit.
- No pull-request trigger and no feature-branch trigger. Neither is in D11-b's scope.
- No third-party action and no installed tool beyond what the runner image carries. `bash`, `git`,
  `node` and a Python the repo's resolver can run are all on `windows-latest`.
- No change to the kickoff manifest. Remote CI is not a command a session runs, and none of the files
  this unit touches is in its `watch:` list.
- No permanent gate over the workflow file's text. A new gate is a separate unit under the build
  method's decomposition rule, and this spec cannot mint one; §8 F2 records it as an ADD candidate.
- The first live run happens after this build lands, because a push to the default branch is its
  only trigger besides the schedule. The wrap-up records that run's URL and conclusion; no criterion
  here depends on it.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-9` — check 25, the transition audit, inside the unguarded
  `memory hygiene` leg, with its shallow-clone DEAD PROBE. Without it the history-audit job runs
  check 9 alone, and S2's liveness assertion has no line to find.

## 4. Design

### Why one file, and why `windows-latest`

`tools/playbook/render_playbook.py`'s `derive_ci_file` returns the first `.yml` under
`.github/workflows/` in sorted order, so a single file is the one layout the charter line describes
exactly. Measured at BASE, this repo carries no `.github/` directory at all, and `.governance/deploy.toml`
supplies "none yet" as the override the probe falls back to.

Every node in the registry runs Windows with Git-Bash. A search of the build records for Linux,
Ubuntu and macOS found adopter nodes and portability findings, and no record of this repo's bar
completing on Linux. A Linux runner would be the bar's first contact with a new environment, on a
leg whose reds land after the fact, so its first failures would be the host's rather than the
tree's. That candidate loses on that observation; `windows-latest` with `shell: bash` is the
environment every recorded green was earned in. The price is the platform's process-creation cost, which the runner's profile
row absorbs: a four-core runner resolves to the `modest` row in `tools/run-gates/gate-profiles.txt`.

### The three triggers and what each publishes

| Job | Trigger | Runs | Publishes |
|---|---|---|---|
| `history-audit` | push to the default branch | `bash tools/memory-tree/check-memory-hygiene.sh` | the check run on the sha |
| `bar` | push to the default branch | `GATE_FULL=1 bash tools/run-gates/run-gates.sh` | the check run, and the run record as artifact `bar-<sha>` |
| `held-plan`, `held` | daily cron, `workflow_dispatch` | `run-selftests.sh --kit <dir> --sweep` per directory | one artifact `held-<sha>-<dir>` per directory |

The history audit is its own job even though the bar holds the same leg. D11-b names it, it is what
an owner would mark required, and its verdict must not depend on a bar that can red for a host
reason. It costs one engine run per push.

`--sweep` is the right mode for the held run because it issues no cost verdict: the per-suite
budgets in `tools/run-gates/selftest-budgets.txt` were measured on this repo's nodes, and a runner
with a different clock would red them on cost with nothing wrong in the tree. `--sweep` still
bounds each suite by a hang bound derived from its budget, so a suite slower than that on the runner
is published as killed, which is a host fact the published output keeps.

The held population is split by directory because it does not fit one job. `run-selftests.sh --list`
at BASE declares 62 rows and 55710 leg-seconds, with one suite budgeted at 13600 s, against a hosted
job's 360-minute limit. PINNED as measured on 2026-09-14. Deriving the directories from the budget
declaration at run time means a new suite joins the schedule by joining the declaration, with no list
typed into the workflow.

### Liveness, in each job

- `history-audit` greps its own output for check 25's line. Before the switch-over that line is the
  dormant announcement, and after it the `transitions examined` count; either proves the engine
  reached the check. A shallow clone would print the audit's DEAD PROBE and red, which is the design's
  A9 property holding in CI.
- `bar` inherits the runner's own liveness: a run with no verdict line is RED at the hook and here.
- `held` reds when its directory selected no suite. `run-selftests.sh` already refuses a filter that
  matches nothing, and the plan job derives only directories the declaration names.

### Security

The token GitHub issues to the jobs is read-only and is not left in the clone's git config. No job
uses a secret, writes to the repository, or runs on an event a fork can trigger. Pinning each action
by commit sha makes a moved tag unable to change what runs. These are the only GitHub-owned actions
used, `actions/checkout` and `actions/upload-artifact`, and they are part of the Actions platform the
owner authorized; any other action would be a new external dependency, which S5's observation
refuses before landing.

### Why the pre-landing checks are staged breaks and not a gate

The first live run happens after the landing, and the unit must close before it. So each property
S5 names is observed on a scratch copy of the file: the break is staged, the observing command is
run and seen to fail, and the copy is discarded. The property that matters most needs no gate at
all: a checkout that goes shallow makes the history audit print its DEAD PROBE and red in CI, which
is the design's A9 holding by construction.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `.github/workflows/remote-ci.yml` | workflow file | `yml::dark` in `.lexicon.conf`; nothing extracts names from it |
| `history-audit`, `bar`, `held-plan`, `held` | job ids | none |

### Files touched (estimate)

`.github/workflows/remote-ci.yml` (new) · `.gitattributes` · `.lexicon.conf` ·
`.governance/deploy.toml` · `AGENTS.md` · `tools/run-gates/run-selftests.sh` (header) · this unit's
journal under `memory/builds/dDerivedDocket/build/`.

### Alternatives rejected

- **`ubuntu-latest`.** Rejected above: no record of this repo's bar completing on Linux, so its first
  reds would measure the host.
- **One job for the whole held population.** Rejected by the measured budget against the hosted
  job limit.
- **No pre-landing check of the file.** Every criterion would then wait for the first live run, after
  landing, which a unit that must close before the landing cannot wait for.
- **A permanent contract gate over the file.** A new gate is a separate unit under M2, which this
  spec cannot mint (§8 F2).
- **Pushing the run branch to trigger CI before landing.** It needs a branch trigger outside D11-b's
  scope and a CLI session with GitHub authentication that this run cannot assume.

## 5. Production-readiness checklist

- security — read-only token, no secrets, no persisted credentials, actions pinned by sha, no
  fork-triggerable event; stated in §4.
- perf / scale — two jobs per push, one of them the full bar on a four-core runner, and a daily
  matrix; all on a public repository's hosted minutes.
- error / empty / loading states — a job that ran nothing reds by its own liveness step; a matrix
  directory selecting nothing reds; a shallow clone reds through the audit's DEAD PROBE.
- observability — each sha carries the two check runs; artifacts carry the run record and the held
  output; the wrap-up records the first live run.
- risks — the first live runs may red for a host reason on a GitHub runner, such as the temporary
  directory handle class `TOOL-aBoundedVerdict-31` records on Windows. A host red is filed as an ask,
  never suppressed. GitHub disables a public repository's schedule after 60 days without activity,
  which silences the held run; the charter line names the file, and its absence of runs is visible
  on the Actions page.
- testing — S5's staged breaks against a scratch copy of the workflow, the history-audit steps run
  by hand in a full and a shallow clone, and the live run after landing.
- migration — none. Adopters get nothing: the workflow is gov's own.
- user docs — the charter's merge-bar sentence and the rendered CI line are what a session reads.

## 6. Acceptance criteria

- **AC1** — When `grep -c 'fetch-depth: 0'` and `grep -c 'actions/checkout@'` run over the workflow
  file `remote-ci.yml`, the two counts are equal and non-zero; on a scratch copy with one
  `fetch-depth` line deleted they differ, and the journal records both readings.
  Red when: only the first job's checkout is full-history, so a second job runs shallow.
- **AC2** — When `grep -nE 'uses:'` runs over the workflow file, every line names `actions/` and
  ends in a 40-hex sha followed by its tag comment; on a scratch copy naming a tag instead, the same
  pattern test fails, and the journal records both.
  Red when: the pin test accepts any hex string, so a short prefix a tag can shadow passes.
- **AC3** — When the history-audit job's steps are run by hand in a full clone of the branch,
  `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 and the liveness step finds check 25's
  line; in a `git clone --depth 1` of the same branch the audit exits 1 as a DEAD PROBE.
  Red when: the liveness step greps for a line the engine does not print, so it can never pass, or
  for the word `check` alone, so it can never fail.
  cost: one engine run in each clone, minutes.
- **AC4** — When the `bar` job's `GATE_WALL` and `timeout-minutes` are read out of the workflow
  file, the wall is below the timeout expressed in seconds, and `permissions` reads
  `contents: read` with no other grant.
  Red when: the wall equals or exceeds the timeout, so the platform kills the job before the runner
  can name a leg.
- **AC5** — When the `held-plan` step's derivation runs by hand over
  `tools/run-gates/selftest-budgets.txt`, it prints every directory that the argv column names and no
  other, and `bash tools/run-gates/run-selftests.sh --kit <dir> --list` selects at least one suite
  for each.
  Red when: a directory typed into the workflow instead of derived drops a suite added later.
- **AC6** — When `python tools/lexicon/lexicon.py` and `python tools/govkit/govkit.py selfcheck` run
  with the workflow file tracked, both pass.
  Red when: `yml` stays undeclared in `LANGS`, and the lexicon leg refuses the new extension.
- **AC7** — When `git check-attr eol` runs over the workflow file `remote-ci.yml`, it reads `lf`,
  and `git ls-files --eol` shows the index blob as LF.
  Red when: the pin is missing and a Windows checkout commits CRLF bytes.
- **AC8** — When `bash tools/playbook/adopt-playbook.sh --target . --check` runs, the rendered
  charter names the workflow file `remote-ci.yml` and is current, and `AGENTS.md` no longer calls
  remote CI a follow-up.
  Red when: the `ci_file` answer is left in place, so deleting the workflow later revives "none
  yet" silently instead of refusing the render.

## 7. Gates

`playbook render wiring` · `lexicon naming predicates` · `govkit selfcheck` · `charter size` · `memory hygiene` · `line length`

No new gate arm. The file's contract is observed by staged breaks recorded in the journal (S5), and
its liveness in CI is the history audit's own DEAD PROBE on a shallow clone.

## 8. Open questions

- **F1** — Which runner? Options: `ubuntu-latest`; `windows-latest` under `shell: bash`. The first
  would be this repo's bar's first recorded contact with Linux, on a leg whose reds land after the
  fact.
  RESOLVED (agent, 2026-09-14, delegated): `windows-latest`.
- **F2** — How is the workflow observed before its first live run? Options: (a) not at all; (b) a
  permanent repo-subject contract gate; (c) staged breaks on a scratch copy, recorded in the
  journal; (d) a branch push that triggers CI before landing. (a) leaves every criterion waiting on
  a run after the unit must close. (b) is a new gate, which M2 makes a separate unit with its own
  id, and a spec writer mints none. (d) needs a trigger outside D11-b and an authenticated GitHub CLI.
  RESOLVED (agent, 2026-09-14, delegated): (c), with (b) recorded as an ADD candidate for the
  orchestrator under M2's amendment acts.
- **F3** — Does the held run include the unattended kit's suites? The session instruction runs them
  only on the owner's ask, and its recorded prune condition is a bar running them automatically.
  D12-i12 is the owner asking for a scheduled run of the held suites, and the design names it the
  periodic half of the baseline unit, which covers those suites. RESOLVED (agent, 2026-09-14,
  delegated): yes, the whole population `tools/run-gates/selftest-budgets.txt` declares. The session
  instruction stays, because the merge bar still does not run them.
- **F4** — May this unit edit `AGENTS.md`'s authored merge-bar sentence? The unit makes it false,
  and the ratified design lists `AGENTS.md` among the documents this build updates. RESOLVED (agent,
  2026-09-14, delegated): yes, that one sentence; the render and the rest of the charter's backlog
  wording stay with the charter unit.
- The adoption of remote CI, its detection-after-landing timing and its held-suite schedule are
  RESOLVED (owner, 2026-09-13) as D11-b, D11-c and D12-i12, and the push of the workflow file as the
  owner's 2026-09-14 answer that the credential has scope.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft.

## 10. Reuse audit

Nothing here builds a gate engine: every job runs a command the bar already owns. The history audit is
`tools/memory-tree/check-memory-hygiene.sh` as the `memory hygiene` leg runs it; the per-sha verdict is
`tools/run-gates/run-gates.sh` with `GATE_FULL=1` and its existing `GATE_WALL` override at
`run-gates.sh:422`; the held run is `tools/run-gates/run-selftests.sh --sweep`, whose usage text
already states that it answers only whether any suite failed. The charter line is derived by
`derive_ci_file` in `tools/playbook/render_playbook.py`. `python tools/codebase-map/reuse_lookup.py
"run the merge bar and the history audit on a remote CI runner for every push to main"` returned
name-stem neighbours only, `run` and `merge` among them, and it reports `.sh` as an unscanned layer;
no seam in the tree talks to a CI service, and none needs to. Recall returned `TOOL-aBoundedCeiling-10`,
whose candidates name "a scheduled run of the held population" as the periodic signal, and the
owner's D11-b and credential answers in this build's own records.

Where DR and the source disagree at BASE: DR's L7 speaks of REQUIRED checks, and making a check
required is a repository setting this build may not change, so the unit ships the checks and leaves
the setting to the owner. DR does not name a runner, a trigger set or an artifact shape; §4 decides
them. M12's candidates and the observation that rejected each are in §4, Alternatives rejected.

Recall terms used: `remote CI GitHub workflow scoped push required checks history audit check 9
held suites schedule fetch-depth shallow direct push`
