# Research: the integrations expansion, run A

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 53's return, verbatim. Its question is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-20-researcher.md`, which dispatch 54 ran
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`.

---

## 1. Verdict

Integrations should be a set of adapters, each registered at the core point that owns its slot, with all of them sharing one adapter header: name, kind, grant, secret reference, liveness probe and absence fallback. A single integrations registry loses its test (§4). Runtime already declares the host and notification points. Test's verdict backend and the command-adapter point carry remote CI. Deploy needs one new core point, a per-SHA release program, run as `release.*` items after the landing. Trackers can be argued away for now: the in-repo ask backlog holds 521 rows and no code names an outside tracker. Grants live on the shared header. The binding secret check is a value-fingerprint scan, not a shape scan. Without the layer, the core falls back to the local hook, the terminal, the node tick and close-at-landing.

## 2. Today

| Part | What it does | Measured use | file:line |
|---|---|---|---|
| `remote-ci.yml` | `history-audit` and `bar` run on every push to main; `held-plan` and `held` run daily and on dispatch | Only `contents: read`. Its own comment says it "blocks nothing". Triggers only on main (`push: branches: [main]`) | `.github/workflows/remote-ci.yml:11,31-38,86-122` |
| What CI publishes | One check run per SHA from the `github-actions` app (id 15368), plus an artifact `bar-<sha>` | The check run is readable anonymously. The artifact download returns **HTTP 401** without a credential and expires after 90 days. Of the last 40 push runs, **22 failed and 18 passed**. The latest run (2026-10-16, `9b46ae0fa`) had a green `history-audit` and a red `bar` step after 21 minutes | API output below |
| `post-merge.sh` | Runs the full bar on a landed SHA, publishes a red as `refs/gov/bar-red` with a lease, and keeps one last-verdict file | Gov's remote holds 17 `refs/gov/runs/*` refs and **no** `bar-red` | `tools/run-gates/post-merge.sh:13-16,249,272` |
| `GATE_POST_MERGE=ci` | The lander starts nothing under it, and pre-push still reads only `bar-red` | **A dead path.** Nothing turns a CI result into `bar-red`. Gov's `gate-env.sh` does not declare the key at all | `tools/push-main.sh:431-437`; `.githooks/pre-push:1621,1919-1936` |
| govkit `[gate_runner.ci]` | Validates the declaration and accepts only `github-actions` | **No workflow is ever emitted**: 0 hits for `.github/workflows` in govkit.py and 0 in any kit.toml | `tools/govkit/govkit.py:5745-5748` |
| Owner notification | The micro-formats in the final message, plus park lines appended to files | **No push channel.** 0 code hits for PushNotification, ntfy, Slack, webhook or toast (all "slack" hits mean margin). No `Notification` hook is wired | `coding-governance-agents.template.md:58-74`; `tools/unattended/unattended.sh:12416`; `.claude/settings.json:3,32,65,85` |
| Host | Session hooks, plus the unattended skill's in-session `CronCreate` | `cloud-routine`, `run.host` and `maintain.host` have 0 code hits; `RemoteTrigger` has 0 | `.claude/skills/unattended/SKILL.md:16` |
| Tracker | The derived ask backlog | 521 rows across 4 shards, generated from 126 `BACKLOG.md` files. **0** hits for gh issue, Jira, Linear, Trello or Asana | `memory/backlog/TOOL.md:1-5` |
| Credentials | The lander's push rides the ambient Git Credential Manager | `credential.helper=manager` comes from the system gitconfig. **0** credential or push-scope hits in push-main.sh and govkit.py | `C:/Program Files/Git/etc/gitconfig` |
| Secret shapes | Runlog's redaction table (20 classes) and `scan_secrets` | Used only by `runlog_lib.py`. **No leg** in gate-legs.json scans for secrets | `tools/runlog/redaction.tsv`; `tools/runlog/runlog_lib.py:447,522` |
| Deploy engine and release | Nothing | `deploy.runs`, `deploy.promotion`, `deploy.on-verify-fail` and `build.closes` have 0 code hits each. All staging, canary and promote hits are the guard canary or unit promotion | — |

The commands behind the CI rows:
```
$ curl -s .../actions/runs?per_page=40&event=push → last 40 push runs: {'failure': 22, 'success': 18}
$ curl -s .../commits/9b46ae0f.../check-runs → check-run: bar failure app: github-actions 15368
$ curl -s .../runs/38898108320/jobs → step 6 "the merge bar…" failure 12:05:48→12:26:25
$ curl -s -o /dev/null -w %{http_code} <artifact zip> → anonymous download HTTP 401
$ git ls-remote origin 'refs/gov/*' → 17 refs/gov/runs (no bar-red)
```

**Where the records and the code disagree**
- The handed fact says remote CI has been "unavailable since 2026-10-14". The service is up: runs fired on 10-14, 10-15 and 10-16, and each ran the bar. What is missing is a **green** verdict. The bar reds on the hosted runner, and the cause is unread because the logs need authentication.
- research-deploy:48,94 says "CI cannot publish a verdict". It cannot write a ref, but GitHub publishes a check run keyed by SHA that anyone can read anonymously.
- flow-steps:331 (K1) says "under `ci`, the remote CI's result … is the witness". No code reads that result.
- layer-runtime:748-749 says a key that selects an extension takes registered names, "never … a literal enumeration". The catalogue nonetheless gives `verdict`, `run.host` and `maintain.host` literal value lists.

## 3. Attach points

| Attach point | Declared at | What the layer fills | Core without the layer |
|---|---|---|---|
| Verdict backends | flow-steps:259 (`test.verdict` "on the declared backend") and :291-292 | A remote-CI verdict adapter | `verdict: local-hook`, as P3 settles |
| The core re-check's witness under `ci` (K1) | flow-steps:316,331 | The check-run reader for the landed SHA | `post-merge.sh` on the node |
| Command adapters | layer-runtime:739 | Each verdict, engine and secret-check command, with its witness and probe | — |
| Host adapters | layer-runtime:700,744 | `cloud-routine` | The node tick: requesting-node or os-scheduler |
| Notification adapters | layer-runtime:745 | Push channels | The terminal |
| Deploy's promotion extension | flow-steps:360-361, prose only | The release program | Closes at landing |
| `build.closes: after-release-verifies` | flow-steps:365 | Holds `deploy.close` until the release verifies | `at-landing` |

**Points no core layer declares yet:**

| Missing point | What is missing | Proposed owner |
|---|---|---|
| (a) An item slot for the release program | flow-steps:360 names the extension but declares no item, record kind or route into it | Flow |
| (b) A grant field on adapter rows | The command-adapter row (layer-runtime:739) carries a witness and a probe, but no grant or secret reference | Runtime |
| (c) A tracker point | None anywhere | Not needed under the pick, because the tracker is argued away (§8 fork 4) |

## 4. Candidates

| # | Mechanism | Smallest losing test | Result |
|---|---|---|---|
| **A** | One integrations registry, a new extension point with a `kind` field and its own dispatcher | It loses if core already declares points for the kinds it would hold, because then it double-registers them and P28 forbids an expansion-owned point | **LOSES.** `layer-runtime:744-745` already declares host and notification adapters, and `:739` declares command adapters. A second registry for the same kinds duplicates them |
| **B (pick)** | Each adapter registers at the core point that owns its slot, all sharing one header (name, kind, grant, secret-ref, probe, fallback). Remote verdicts are read as a platform check run keyed by SHA | It loses if no remote witness exists that the pusher cannot write, or if a kind fits no core point | **PASSES, with conditions.** The check run comes from app 15368 and is keyed by `head_sha`. But `remote-ci.yml` is tracked in the pushed tree (`git ls-files .github/workflows` → `remote-ci.yml`; last edited `ca46f313d`), so a pusher could swap the job for `exit 0`. The reader must therefore pin the workflow blob. Gaps (a) and (b) above must be declared |
| **C** | CI as the bus: govkit emits workflows, every integration is a CI job, and gov reads check runs (research-deploy pick B, generalised) | It loses if CI cannot yield a usable verdict, or cannot serve the host or notification kinds | **LOSES.** 22 of the last 40 push runs are red, and the newest bar is red. CI fires only on main (`remote-ci.yml:31-32`), so it gives Test no pre-landing verdict. A CI job can neither reach an attended owner nor host the supervisor |
| **D** | Outbox orders: gov emits an order, an operator executes it, and gov reads the result back | It loses if the result is typed rather than computed (P2) | **LOSES as the primary mechanism.** No code grades orders (gap-deploy-05). The operator's "done" is typed. It survives only as `deploy.runs: operator`, and only when an engine probe backs it |

**The secret-check sub-question** has two candidates:
- **Shape scan** with `scan_secrets` over the tracked tree. **Loses as a binding gate.** The command run in §2 found 4,646 files with spans in 22 of them, all fixture or example text (for example `memory/builds/aScouredKit/reviews/…-lens-security.md:187-191`). A gate would need an allowlist, and an allowlist is state shared with what it guards.
- **Value-fingerprint scan.** At runtime the adapter hashes the secret value it holds and searches the tracked tree, `memory/` and the session transcripts that runlog already reads for that exact value. It cannot hit a fixture. **Passes by construction**; the build must prove it with a planted-value fixture that reds.

## 5. The contract, filled

| Field | Integrations |
|---|---|
| Tag and definition | `integrations`, expansion: adapters to outside services. Every adapter carries one header and registers at a core-declared point |
| Instruction units | The adapter header schema; the release view (a level-5 work-order slot); the grant rule "least scope, secret by reference"; and a rewrite of the `up —` format so it carries `pw-where` only, never a value |
| Engine kits | `tools/integrations/`: the header library, plus `verdict-gh-checks`, `host-cloud-routine`, `notify-<channel>`, `secret-fingerprint` and the release runner. Each adopter's engine adapter is dShippedRelease's unit. It reuses `post-merge.sh` publication, govkit's `[gate_runner.ci]` validator and runlog's `scan_secrets` |
| Record kinds | `release`, keyed per SHA; `remote-verdict` (key, source, workflow blob, conclusion, run id); `delivery` (notification sent, adapter receipt); `grant` (the adapter's declared scope, probed) |
| Extension points | **Declares:** deploy-engine adapters, owned by the release program. **Uses:** verdict backends (Test), command adapters, host adapters, notification adapters (Runtime), and the release item slot and adapter grant field once Flow and Runtime declare them |
| Policies and gates | The keys in §6. Gates: secret-fingerprint, adapter registration (each header complete and its probe live) and remote-verdict trust (workflow blob pinned) |

## 6. Items and policies

The release is its own program, keyed by SHA. It opens when a landing record exists and `release.environments` is non-empty. Under the default `build.closes: at-landing` it outlives the build.

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `release.open` | command | Opens the release record for the landed SHA, with the declared environments in order | The release record row, written through `record` | → `release.promote(env₁)` |
| `release.promote` | command: the engine adapter for the environment | Promotes the SHA once the prior environment has verified and the `deploy.promotion` gate is met | The engine's deployment id, plus the engine probe's report of the SHA live in that environment | Deployed → `release.verify`. Awaiting approval → an owner item. Engine unreachable → supervisor retry, then an owner item. Refused → an ask |
| `release.verify` | command: the engine's verify, or the declared smoke command | Verifies the (SHA, environment) pair | A runner-written verdict keyed by (SHA, environment, source) | Green → the next environment, or `release.close`. Red → `release.on-fail` |
| `release.on-fail` | command | Acts on `deploy.on-verify-fail` | The rollback's deployment id and its re-verify, or the halt record, or the filed ask | `roll-forward`: an ask as new work, with the environment flagged red. `rollback-and-ask`: the engine rolls back to the last verified SHA, re-verifies, then files an ask. `halt-and-alert`: stops this and every later SHA in that environment, and notifies the owner through the notification adapter |
| `release.close` | command | Records each environment's terminal state. Under `after-release-verifies`, it unblocks `deploy.close` | The transition record | Closed |
| `deploy.core` (filled) | command | Under `GATE_POST_MERGE=ci`, reads the check run for the landed SHA | A `remote-verdict` record whose app id, job name and workflow blob all match | Red → also published as `refs/gov/bar-red` by the node, which closes the dead path |
| `deploy.notify` (filled) | command | Also sends `notify.owner` events through the selected adapter | A `delivery` record | — |

**The release record:** `id rel-<sha12>`, `sha`, `landing` (link to the landing record), `builds[]`, then one row per environment: {`env`, `engine`, `deploy_ref`, `approval` (witness ref or `auto`), `verify` {verdict, key, source}, `outcome` (verified, red, rolled-back or halted), `rollback_to`, `asks[]`}. One writer: `record`.

**Naming `deploy.release` apart from the release.** `deploy.release` appears 6 times in flow-steps and has 0 hits in code. I recommend renaming it to `deploy.unlease`, because its job is to delete lease refs and close the mailbox. That leaves "release" for the per-SHA program.

| Key | Allowed values | Default | Why |
|---|---|---|---|
| `release.environments` | An ordered list of registered environments | `[]` | An empty list means no release program runs, so the core alone still lands |
| `verdict.remote.trust` | `workflow-pinned`, `app-only` | `workflow-pinned` | The workflow file sits in the pushed tree |
| `notify.channel` | Registered adapter names | `terminal` | The only channel today |
| `integrations.secret-home` | `os-keychain`, `env-injected`, `ci-store` | `os-keychain` | The `manager` credential helper is already present on the node |
| `integrations.secret-check` | `fingerprint`, `fingerprint+shape-report` | `fingerprint+shape-report` | The shape scan alone reds on fixtures |
| `tracker` | `none`, `mirror-out` | `none` | 0 trackers are in use |

**Grants.** Every adapter header declares `grant = {service, scopes[]}` and `secret = <ref name>`, never a value. Registration probes the scope it declared, for example a read of the check runs. The secret is injected only into the adapter's own process environment.

## 7. Gaps

**Closed by the pick**

| Gap | How it closes |
|---|---|
| `gap-deploy-01` | The release program and the engine adapter point. The adopter's engine adapter itself is still dShippedRelease's unit |
| `gap-deploy-02` | The `remote-verdict` and `release` records are keyed by SHA, replacing the single last-verdict file. The `ci` path becomes bound |
| `gap-deploy-03` | Partly: the emitted workflow becomes an optional adapter, and govkit's validator (govkit.py:5745) is its seam |
| `gap-deploy-05` | Under `operator`, an order counts as done only on the engine probe's witness |

**New gaps the pick exposes**

| New gap | Evidence |
|---|---|
| No adapter declares a grant, and no check covers secrets | 0 credential hits in push-main.sh and govkit.py; 0 secret legs; the redaction table is read only by runlog |
| `up —` invites a password into chat | `coding-governance-agents.template.md:64` (`pw <pw-or-where-it-lives>`) |
| `GATE_POST_MERGE=ci` binds nothing | push-main.sh:434 starts nothing; pre-push:1919-1936 reads only `bar-red`, which only post-merge.sh:249 writes |
| A CI green can be forged by the pusher | `remote-ci.yml` is tracked in the tree it judges |
| The hosted bar is red | 22 of 40 push runs failed; `9b46ae0fa` ran 21 minutes and went red |
| The release has no item slot, and the adapter row has no grant field | flow-steps:360 (prose only); layer-runtime:739 |
| Selection keys are typed as literals | `verdict` and `run.host` against layer-runtime:748-749 |

## 8. Forks

| Fork | Options | Recommendation |
|---|---|---|
| 1. Naming | (a) rename the item to `deploy.unlease` and keep `release.*` for the program; (b) keep `deploy.release` and call the program `promote.*` | (a). The per-SHA process is what adopters call a release |
| 2. Trust in a remote verdict | (a) workflow blob pinned to an owner-ratified blob; (b) app id only; (c) a required check, which is a repository setting | (a) now. (c) is the owner's repository setting, and it still needs (a) |
| 3. Reach of remote CI | (a) post-landing only, filling `deploy.core` under `ci`; (b) also pre-landing, through a staging ref and the lander | (a). The hosted bar is red, and P3 keeps the local hook binding |
| 4. Trackers | (a) argue them away: the ask backlog is the tracker; (b) a one-way `mirror-out` reader of the ask record kind; (c) two-way sync | (a), with (b) as a later adapter. (c) breaks the one-door `record` rule |
| 5. Where secrets live | os-keychain, env-injected, or ci-store | os-keychain, with ci-store only for emitted CI |
| 6. Read the hosted bar's red before any `ci` default | (a) a diagnostic unit in dWitnessedBar; (b) leave it | (a). The logs need an authenticated read, which only the owner can grant |

Files relevant to this answer:
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/.github/workflows/remote-ci.yml`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/run-gates/post-merge.sh`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/push-main.sh`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/.githooks/pre-push`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/govkit/govkit.py`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/runlog/redaction.tsv`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/runlog/runlog_lib.py`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/coding-governance-agents.template.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`
