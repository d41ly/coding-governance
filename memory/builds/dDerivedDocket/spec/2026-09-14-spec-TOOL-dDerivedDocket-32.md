# TOOL-dDerivedDocket-32 — remote CI on every push

**Status:** SPECCED · rev-2 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 32

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-32-spec-audit-g5-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-32-spec-audit-g5-round1.md) | spec-audit | TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-32-spec-audit-g5-round2.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-32-spec-audit-g5-round2.md) | spec-audit | TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

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
  `core.autocrlf false`. Every job runs on `windows-latest` under `shell: bash`. After every
  `actions/checkout` step, `git remote set-head origin main`; in every job, a step asserts that
  `git symbolic-ref refs/remotes/origin/HEAD` resolves before any bar command runs, and the `bar`
  job's plain `git clone` sets the symref itself. Observed by AC1, AC2 and AC7.
- **S2** Job `history-audit`, on every push to the default branch: runs
  `bash tools/memory-tree/check-memory-hygiene.sh` over the full clone, which carries check 9 and the
  transition audit's check 25, with its output `tee`d to a file, then asserts that its output carries
  a line beginning `memory-hygiene: check 25 ` (unit 9 S7), dormant or examined. A job that never
  reached check 25 cannot pass. Observed by AC3.
- **S3** Job `bar`, on every push to the default branch: after the autocrlf step, a plain anonymous
  `git clone` of the repository to `C:/projects/coding-governance` — the path every recorded green was
  earned at and the one the rendered charter records — then `git checkout -B main <sha>`; it runs
  `GATE_FULL=1 bash tools/run-gates/run-gates.sh` there with `GATE_WALL` inside the window AC4
  states, so the runner's wall fires and names the outstanding legs before the platform kills the
  job. The job's conclusion is the per-sha verdict, and its run record is uploaded as S8 states.
  Observed by AC4, AC10 and AC12.
- **S4** Jobs `held-plan` and `held`, on a daily schedule and on `workflow_dispatch`. The plan job
  runs `bash tools/run-gates/run-selftests.sh --list`, the resolved population, and emits one matrix
  entry per suite row: its name, its budget and its full resolved argv. It refuses — red, naming the
  row — when a row does not parse, when the parsed count differs from the `row(s)` figure `--list`
  prints, when `run-selftests.sh --kit "<argv>" --list` selects anything but that one row, or when
  the entries exceed the platform's 256-entry matrix limit. Each `held` job runs
  `bash tools/run-gates/run-selftests.sh --kit "<argv>" --sweep` for its one suite and uploads its
  output as `held-<sha>-<suite name made path-safe>`. Observed by AC5 and AC11.
- **S5** The file's contract, observed before landing by hand and recorded in the unit's journal:
  every checkout carries `fetch-depth: 0`; every `uses:` is an `actions/` action pinned by a 40-hex
  sha; `permissions` grants `contents: read` and nothing more; the bar job's `GATE_WALL` is at least
  the `ceiling_max` that `GATE_FULL=1 bash tools/run-gates/run-gates.sh --print-profile` reports and
  below its `timeout-minutes` in seconds, and `timeout-minutes` is at most 360; every
  `actions/checkout` carries `persist-credentials: false`; the autocrlf step precedes each checkout
  and the `bar` job's clone; every job carries `runs-on: windows-latest` and `shell: bash`; the `bar`
  job's clone URL carries no credential and no `secrets` reference; and every checkout is followed by
  `git remote set-head origin main`. Each observation is a staged break on a scratch copy of the
  file, confirmed to fail, then removed. No permanent gate grades the file (§8 F2). Observed by AC1,
  AC2 and AC4.
- **S6** The declarations the new file owes: `.github/workflows/*.yml` pinned to LF in
  `.gitattributes`, and `yml::dark` added to `LANGS` in `.lexicon.conf`, whose undeclared-extension
  refusal would otherwise red. The file sits outside `tools/govkit/registry.toml`'s declared surface
  and outside every codebase-map inventory, so it owes neither a registry row nor a claim. In the
  same commit, `ratified=` in `.lexicon.conf` is re-stamped with a dated, attributed comment in the
  file's existing re-stamp form, saying it covers only a `dark` `yml` declaration, which refuses to
  extract and so cannot change the population the VERBS seed certifies, and that the seed was not
  re-curated. Observed by AC6, AC7 and AC9.
- **S7** The charter and its answers. `.governance/deploy.toml` drops its `ci_file` answer, so a
  deleted workflow makes the render refuse instead of reviving "none yet". `AGENTS.md`'s rendered
  region is regenerated, and its merge-bar section's sentence calling remote CI a follow-up is
  replaced by one naming the workflow, its jobs, and that it detects after landing and is no
  required check. The headers of `tools/run-gates/run-selftests.sh` and
  `tools/unattended/run-unattended-gates.sh` stop saying nothing runs the held suites automatically,
  and name the daily CI schedule, each beside the compensating-check wording unit 1 S8 leaves there.
  The run-gates and unattended version moves these edits ride are the landing range's single ones,
  NOT OBSERVED by a criterion here: `kit version markers` grades them. Observed by AC8.
- **S8** Every upload names its files and runs after a failure. The `bar` job's `if: always()` step
  copies `<git-dir>/gate-logs/` and, when present, `<git-dir>/gate-last-failure.txt` from the clone
  into the workspace, and the `held` job's sweep output is `tee`d to a workspace file as it runs.
  Every `actions/upload-artifact` step carries `if: always()` and `if-no-files-found: error`.
  Observed by AC10.
- **S9** The plan job prints each suite's derived sweep bound, its budget times the declared
  `sweep-ceiling-factor`, and marks `platform-bounded` every suite whose bound exceeds the held job's
  `timeout-minutes` in seconds. Every held job declares `timeout-minutes: 360` and captures the
  sweep's output to a file as it runs, so a platform cancellation still uploads what ran. Observed by
  AC11.

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

- **consumes-from** `TOOL-dDerivedDocket-1` — both runner headers as its S8 leaves them, and the
  run-gates and unattended version moves (S9) this unit's header edits ride.
- **consumes-from** `TOOL-dDerivedDocket-9` — check 25, the transition audit, inside the unguarded
  `memory hygiene` leg, with its shallow-clone DEAD PROBE. Without it the history-audit job runs
  check 9 alone, and S2's liveness assertion has no line to find. It also takes S7's pinned
  `memory-hygiene: check 25 ` line prefix.
- **consumes-from** `TOOL-dDerivedDocket-27` — `ceiling_max` on the runner's `--print-profile` (S3),
  the lower bound AC4 holds `GATE_WALL` to.

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

The runner is not a node. Every recorded green was also earned in a clone at
`C:/projects/coding-governance`, with an `origin/HEAD` that `git clone` set, on a machine with no job
limit. `PRIMARY_TREE_A` and `WORKTREE_ROOT_A` are `derived` placeholders filled from the parent of
`--git-common-dir`, and an answer overrides one only when its probe finds nothing
(`tools/playbook/render_playbook.py:405-419`), so a bar run from `actions/checkout`'s workspace
renders a different region and the unguarded `playbook render wiring` leg prints DRIFT on every push.
The bar job therefore clones to that path, which `actions/checkout`'s `path` cannot leave the
workspace to reach.

### The three triggers and what each publishes

| Job | Trigger | Runs | Publishes |
|---|---|---|---|
| `history-audit` | push to the default branch | `bash tools/memory-tree/check-memory-hygiene.sh` | the check run on the sha |
| `bar` | push to the default branch | `GATE_FULL=1 bash tools/run-gates/run-gates.sh` in a clone at `C:/projects/coding-governance` | the check run, and the run record as artifact `bar-<sha>` |
| `held-plan`, `held` | daily cron, `workflow_dispatch` | `run-selftests.sh --kit <argv> --sweep` per suite | one artifact `held-<sha>-<suite>` per suite |

The history audit is its own job even though the bar holds the same leg. D11-b names it, it is what
an owner would mark required, and its verdict must not depend on a bar that can red for a host
reason. It costs one engine run per push.

`--sweep` is the right mode for the held run because it issues no cost verdict: the per-suite
budgets in `tools/run-gates/selftest-budgets.txt` were measured on this repo's nodes, and a runner
with a different clock would red them on cost with nothing wrong in the tree. `--sweep` still
bounds each suite by a hang bound derived from its budget, at the budget times the
`sweep-ceiling-factor` the budget file declares. One suite's bound exceeds the hosted job's 21600 s:
`unattended gate selftest`, 13600 s times 2 is 27200 s (PINNED, measured 2026-09-14). For such a
suite the platform, not the sweep, bounds the job, so its cancellation is published as a partial
output rather than as a named kill (S9).

The held population is split by suite because it does not fit one job. `run-selftests.sh --list`
at BASE declares 62 rows and 55710 leg-seconds, with one suite budgeted at 13600 s, against a hosted
job's 360-minute limit. PINNED as measured on 2026-09-14. Deriving one entry per suite from `--list`,
the runner's own resolved output — the budget file's argv column is blank on most rows, which read
their argv from `tools/gate-legs.json`, and `--kit` is a substring filter, so directories do not
partition the population (G5 H4, measured 2026-09-14) — at run time means a new suite joins the
schedule by joining the declaration, with no list typed into the workflow.

### Liveness, in each job

- `history-audit` greps its own output for a line beginning `memory-hygiene: check 25 `. Before the
  switch-over that line is the dormant announcement, and after it the `transitions examined` count;
  either proves the engine reached the check. After the switch-over a shallow clone prints the
  audit's DEAD PROBE and reds, which is design A9 holding in CI; before it, check 25 is dormant on
  shallow and full clones alike, so until unit 34 lands A9 is held by every checkout's
  `fetch-depth: 0` (AC1) and not by the audit.
- `bar` inherits the runner's own liveness: a run with no verdict line is RED at the hook and here.
- `held` reds when its key selects no suite. `run-selftests.sh` already refuses a filter that
  matches nothing, and the plan job refuses any key that selects other than its one row (S4).

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
all once the tree is in builds mode: a checkout that goes shallow then makes the history audit print
its DEAD PROBE and red in CI, which is the design's A9 holding by construction; before the
switch-over check 25 is dormant on a shallow clone too, and every checkout's `fetch-depth: 0` (AC1)
holds A9 until unit 34 lands.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `.github/workflows/remote-ci.yml` | workflow file | `yml::dark` in `.lexicon.conf`; nothing extracts names from it |
| `history-audit`, `bar`, `held-plan`, `held` | job ids | none |

### Files touched (estimate)

`.github/workflows/remote-ci.yml` (new) · `.gitattributes` · `.lexicon.conf` ·
`.governance/deploy.toml` · `AGENTS.md` · `tools/run-gates/run-selftests.sh` (header) ·
`tools/unattended/run-unattended-gates.sh` (header) · this unit's journal under
`memory/builds/dDerivedDocket/build/`.

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
- **Answer-overridable path probes in the renderer.** The playbook kit's surface and another unit's,
  and it changes what `derived` means for every adopter (§8 F5).
- **Directory keys for the held matrix, or an exact selector added to `run-selftests.sh`.**
  Directories do not partition the population under a substring filter, and an exact selector is a
  new run-gates surface and a second version move in this landing range (§8 F6).

## 5. Production-readiness checklist

- security — read-only token, no secrets, no persisted credentials, actions pinned by sha, no
  fork-triggerable event; stated in §4.
- perf / scale — two jobs per push, one of them the full bar on a four-core runner, and a daily
  matrix; all on a public repository's hosted minutes.
- error / empty / loading states — a job that ran nothing reds by its own liveness step; a matrix
  key selecting other than its one suite reds; a shallow clone reds through the audit's DEAD PROBE
  once the tree is in builds mode.
- observability — each sha carries the two check runs; artifacts carry the bar's per-leg logs and
  last-failure file, and each suite's held output, uploaded after a failure too (S8); the wrap-up
  records the first live run.
- risks — the first live runs may red for a host reason on a GitHub runner, such as the temporary
  directory handle class `TOOL-aBoundedVerdict-31` records on Windows. A host red is filed as an ask,
  never suppressed. GitHub disables a public repository's schedule after 60 days without activity,
  which silences the held run; the charter line names the file, and its absence of runs is visible
  on the Actions page. Before landing, only the commands AC12 names were run in a runner-shaped
  clone; an unguarded leg that bakes another node fact shows first on the live run, and is filed as
  an ask. A `platform-bounded` suite on a runner slower than its recorded reading is cancelled by the
  platform; its partial output is published and the cancellation is filed as an ask. The window this
  leaves for `GATE_WALL` runs from `ceiling_max` to just under the hosted job's 21600 s. Whether a
  `GATE_FULL=1` bar at the runner's width finishes inside it is unmeasured before the first live
  run; a wall breach there is filed as an ask naming the choice it raises, a narrower bar or a
  different runner, which is the owner's.
- testing — S5's staged breaks against a scratch copy of the workflow, the history-audit steps run
  by hand in a full clone, a shallow clone and a shallow builds-mode scratch clone, a runner-shaped
  clone at a second path (AC12), and the live run after landing.
- migration — none. Adopters get nothing: the workflow is gov's own.
- user docs — the charter's merge-bar sentence and the rendered CI line are what a session reads.

## 6. Acceptance criteria

- **AC1** — When `grep -c 'fetch-depth: 0'`, `grep -c 'persist-credentials: false'` and
  `grep -c 'actions/checkout@'` run over `remote-ci.yml`, the three counts are equal and non-zero;
  each checkout and the `bar` job's clone step is preceded in its job by the `core.autocrlf false`
  step and each checkout is followed by `git remote set-head origin main`; every job declares
  `runs-on: windows-latest` and `shell: bash`; and the `bar` job's clone URL holds no `secrets.`
  reference. On a scratch copy, one break per property — a deleted `fetch-depth` line, a deleted
  `persist-credentials` line, the autocrlf step moved after a checkout, one job on `ubuntu-latest`,
  one `set-head` step deleted — makes its check fail, and the journal records each reading.
  Red when: only the first job's checkout is full-history or credential-free, so a second job runs
  shallow or leaves the token in the clone's git config, or a job runs on a runner F1 rejected.
- **AC2** — When `grep -nE 'uses:'` runs over the workflow file, every line names `actions/` and
  ends in a 40-hex sha followed by its tag comment; on a scratch copy naming a tag instead, the same
  pattern test fails, and the journal records both.
  Red when: the pin test accepts any hex string, so a short prefix a tag can shadow passes.
- **AC3** — When the history-audit job's steps run by hand in a full clone of the branch,
  `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 and the liveness step finds a line beginning
  `memory-hygiene: check 25 `; in a `git clone --depth 1 file://<clone>` of the same shards-mode
  branch (a plain-path clone ignores `--depth`, so the `file://` form is what makes it shallow,
  confirmed by `git rev-parse --is-shallow-repository` reading `true`) the engine prints check 25's
  dormant line exactly as in the full clone; in a scratch clone of the branch carrying one commit
  that sets `BACKLOG_MODE="builds"`, cloned again the same shallow way, the engine prints check 25's
  DEAD PROBE line naming the shallow clone; and the liveness step run over a captured engine output
  with every check 25 line removed, and over one whose only match is the word `check`, reds both
  times. The journal records the five readings.
  Red when: the liveness step greps for a line the engine does not print, so it can never pass, or
  for the word `check` alone, so it can never fail; or the shallow DEAD PROBE is claimed before the
  flip, where the audit is dormant.
  cost: one engine run in each of three clones, minutes.
- **AC4** — When the `bar` job's `GATE_WALL` and `timeout-minutes` are read out of the workflow
  file, `GATE_WALL` is at least the `ceiling_max` that
  `GATE_FULL=1 bash tools/run-gates/run-gates.sh --print-profile` prints and below `timeout-minutes`
  times 60, `timeout-minutes` is at most 360, and `permissions` reads `contents: read` with no other
  grant; on a scratch copy with `GATE_WALL` below
  `ceiling_max`, and on one with `GATE_WALL` at the timeout, the same comparison fails, and the
  journal records both.
  Red when: the wall sits below the largest leg ceiling the full bar runs, so it kills a healthy leg
  on every push, or at or above the timeout, so the platform kills the job before the runner can
  name a leg.
- **AC5** — When the `held-plan` derivation runs by hand, the union of its entries by row name
  equals the population `bash tools/run-gates/run-selftests.sh --list` prints, with no name twice,
  and each entry's `--kit "<argv>" --list` selects exactly its own row; on a scratch copy of the
  derivation with one entry dropped, and with one key shortened to a bare directory, the union check
  and the one-row check each red, and the journal records both.
  Red when: the derivation reads the budget file's argv column, so the rows that inherit their argv
  are dropped, or a key selects several suites, so the union still matches while suites run twice.
- **AC6** — When `python tools/lexicon/lexicon.py` and `python tools/govkit/govkit.py selfcheck` run
  with the workflow file tracked, both pass.
  Red when: `yml` stays undeclared in `LANGS`, and the lexicon leg refuses the new extension.
- **AC7** — When `git check-attr eol` runs over the workflow file `remote-ci.yml`, it reads `lf`,
  and `git ls-files --eol` shows the index blob as LF.
  Red when: the pin is missing and a Windows checkout commits CRLF bytes.
- **AC8** — When `bash tools/playbook/adopt-playbook.sh --target . --check` runs, the rendered
  charter names the workflow file `remote-ci.yml` and is current, and `AGENTS.md` no longer calls
  remote CI a follow-up; `grep -c '^ci_file' .governance/deploy.toml` prints 0; a scratch render
  with `.github/workflows/` removed refuses naming `CI_FILE`, recorded in the journal; and
  `grep -ci 'nothing runs the self-tests automatically\|nothing runs these automatically'` over both
  runner headers prints 0.
  Red when: the `ci_file` answer is left in place, so deleting the workflow later revives "none
  yet" silently instead of refusing the render; or one runner header still says nothing runs its
  suites automatically after the schedule does.
- **AC9** — When `python tools/drift-audit/drift_report.py --check` runs after the `LANGS` edit, it
  exits 0 with `signal_lexicon_ratified_stale` at its pin; on a scratch copy with the `ratified=`
  line reverted, the same command reds naming that signal, and the journal records both.
  Red when: `yml::dark` lands without the re-stamp, which the unguarded `drift-audit records` leg
  reds on the landing bar and on the CI bar job while every unit-pass observation stays green.
- **AC10** — When `grep -c 'uses: actions/upload-artifact@'` runs over the workflow file, it equals
  the count of `if: always()` lines on those steps and the count of `if-no-files-found: error`, and
  the `bar` job's copy step names `gate-logs`; on a scratch copy with one upload's `if: always()`
  deleted the counts differ, and the journal records both.
  Red when: an upload runs under the default `success()` condition, so a red bar, the one run whose
  record matters, publishes nothing.
- **AC11** — When the plan job's derivation runs by hand, each printed bound equals the suite's
  `--list` budget times the `sweep-ceiling-factor` line of `tools/run-gates/selftest-budgets.txt`,
  and the `platform-bounded` set equals the suites whose bound exceeds 21600 s; every `held` job in
  the workflow declares `timeout-minutes: 360`.
  Red when: a suite whose bound exceeds the job limit is left unmarked, so its platform cancellation
  is read as a hang in the tree, or a held job runs at the platform's default limit.
- **AC12** — When a runner-shaped clone of the branch is made at a second path — `git clone` there,
  then `git remote set-head origin --delete` — `bash tools/playbook/adopt-playbook.sh --target . --check`
  prints DRIFT naming `PRIMARY_TREE_A`, and `python tools/drift-audit/drift_report.py --check` exits 2
  naming the unresolved default branch; after `git remote set-head origin main` the report no longer
  refuses on its base ref. The journal records the three readings, and the
  workflow's `bar` job clones to `C:/projects/coding-governance`.
  Red when: the bar job runs in `actions/checkout`'s workspace, so the per-sha verdict is red on
  every push for a host reason and reads as noise.

## 7. Gates

`playbook render wiring` · `lexicon naming predicates` · `govkit selfcheck` · `charter size` · `memory hygiene` · `line length` · `drift-audit records` · `kit version markers`

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
  instruction stays, because the merge bar still does not run them. The population is
  `run-selftests.sh --list`'s, one matrix entry per suite (F6).
- **F4** — May this unit edit `AGENTS.md`'s authored merge-bar sentence? The unit makes it false,
  and the ratified design lists `AGENTS.md` among the documents this build updates. RESOLVED (agent,
  2026-09-14, delegated): yes, that one sentence; the render and the rest of the charter's backlog
  wording stay with the charter unit.
- **F5 — where the bar runs on the runner.** Options: (a) a clone at the primary-tree path; (b)
  answer-overridable path probes in the renderer. (b) is the playbook kit's surface and changes
  `derived` for every adopter. RESOLVED (agent, 2026-09-14, delegated): (a).
- **F6 — how the held population is partitioned.** Options: (a) an exact selector added to
  `run-selftests.sh`; (b) one matrix entry per suite, keyed by its full resolved argv through the
  existing substring filter, the plan job refusing a key that selects other than one row. (a) is a
  new run-gates surface and a second version move in this landing range. RESOLVED (agent,
  2026-09-14, delegated): (b); (a) is recorded as an ADD candidate.
- The adoption of remote CI, its detection-after-landing timing and its held-suite schedule are
  RESOLVED (owner, 2026-09-13) as D11-b, D11-c and D12-i12, and the push of the workflow file as the
  owner's 2026-09-14 answer that the credential has scope.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft.
- rev-2 · 2026-09-14 · S1 · S2 · S3 · S4 · S5 · S6 · S7 · S8 · S9 · §3 · §4 · §5 · §7 · §8 · AC1 ·
  AC3 · AC4 · AC5 · AC8 · AC9 · AC10 · AC11 · AC12 · folds spec-audit round 1. G5 H2 (50): the bar
  job clones to the primary-tree path, §8 F5, AC12. G5 H3 (51): `set-head` after every checkout and
  an assertion in every job. G5 H4 (1, 48): one matrix entry per suite from
  `run-selftests.sh --list`, AC5's union and one-row checks, §8 F6. G5 H5 (2, 30, 53): AC3 observes the pre-flip
  dormant line, the shallow DEAD PROBE on a builds-mode scratch clone and the liveness step red
  twice. G5 M7 (52, 65): the `ratified=` re-stamp, AC9, `drift-audit records`. G5 M9 (49, 67): S9
  and AC11 mark `platform-bounded` suites. G5 M10 (3): AC4 bounds `GATE_WALL` by `ceiling_max`
  (consumes-from 27) and the timeout by 360 minutes. G5 M11 (4): S8 and AC10 on the uploads. G5 M17
  (5): AC1 reads every S1 property. G5 M18 (6): AC8 greps the `ci_file` answer away and stages the
  refusing render. G5 L1 (73): S7 corrects both runner headers, consumes-from 1, §7 gains
  `kit version markers`. Adds two edges the brief's table does not list, consumes-from units 1 and
  27.

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
