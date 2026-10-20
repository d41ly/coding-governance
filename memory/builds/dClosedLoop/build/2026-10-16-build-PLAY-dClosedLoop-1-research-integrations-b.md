# Research: the integrations expansion, run B

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 54's return, verbatim, except that its title line is demoted to keep one H1 per
record. Its question is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-20-researcher.md`, which dispatch 53 ran
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`.

---

**Integrations layer: research return (PLAY-dClosedLoop-1, question 20)**

## 1. Verdict

Integrations is a set of adapter kinds that share one adapter header: a name, a grant, a secret reference, a witness source and a probe. Each kind registers at the extension point of the core layer it serves.

- Today it has one live seam: an anonymous GitHub reader keyed by SHA (`unattended.sh:9972`). It is the factory to extract.
- Remote CI already publishes a per-SHA verdict as a check-run that anyone can read. That witness is untrusted until the workflow file is pinned.
- The release is its own per-SHA process with `release.*` items. The core item `deploy.release` should be renamed `deploy.unlease`.
- Trackers get no kind of their own. An outbound mirror registers as a journal reader.
- A secret stays out of files, memory and chat by a value scan that only the adapter's runner can run.

## 2. Today

| Part | What it does | Measured use | file:line |
|---|---|---|---|
| `remote-ci.yml` | `bar` and `history-audit` on every push to main; `held` daily | 77 runs since 2026-09-29. Push: 18 green, 42 red. Schedule: 17 of 17 red. Last green push 2026-10-13 13:29 (`2a9d8191`). The 2026-10-16 bar went red after 21 min. | `.github/workflows/remote-ci.yml:30-38, 86-122` |
| Its check-runs | One per job, keyed by `head_sha`, `app.slug=github-actions`, readable without a credential | 4 check-runs on `9b46ae0f`; `bar` failure; commit statuses 0 | (GitHub API, below) |
| `read_held_reds` | Anonymous read of the latest scheduled run, files one HIGH ask per red held suite | `HELD_CI_WORKFLOW="remote-ci.yml"` at `.unattended.conf:221`; 53 asks filed across 8 builds' BACKLOG.md | `tools/unattended/unattended.sh:9948-10070` |
| `post-merge.sh` | Full bar on the landed SHA, pushes `refs/gov/bar-red` | `GATE_POST_MERGE` declared 0 times in gov; remote `refs/gov/*` = 17 `runs/`, 0 `bar-red` | `tools/run-gates/post-merge.sh:13-16, 249` |
| `run_post_merge` (`ci` branch) | Prints "remote CI runs it; nothing started here" | Nothing reads CI afterwards | `tools/push-main.sh:427-438` |
| pre-push post-merge read | `git ls-remote` of `refs/gov/bar-red` only | — | `.githooks/pre-push:1913-1971` |
| `[gate_runner.ci]` | Validated as `github-actions` only, then never emitted | Its only reference is the validator | `tools/govkit/govkit.py:5745-5748` |
| Owner channel | Turn micro-formats, enforced at Stop; parked rows; stall records written to disk | Hook events wired: PreToolUse, SessionStart, PostToolUse, Stop, StopFailure, SubagentStart. No Notification hook, 0 push channels | `coding-governance-agents.template.md:52-64`; `tools/hooks/format-guard.js:1-15`; `tools/unattended/stall-recorder.js:1-14` |
| Tracker | None. The asks in BACKLOG.md are the internal tracker | 0 hits for `gh issue`, jira, linear or tracker in tools, skills, `.githooks`, `.github` | — |
| Secrets | runlog's redaction table, applied to transcripts when they are read | 19 classes; 0 gate legs scan for secrets | `tools/runlog/redaction.tsv:1-12`; `tools/runlog/runlog_lib.py:415-421` |
| Catalogued keys | `notify.owner`, `deploy.promotion`, `deploy.on-verify-fail`, `deploy.runs`, `run.host`, `cloud-routine`, `peer-node` | 0 code readers for each | — |

The measuring commands, shortened:

```
$ git ls-remote origin 'refs/gov/*' | awk '{print $2}' | sed 's#/[^/]*$##' | sort | uniq -c
     17 refs/gov/runs
$ grep -n GATE_POST_MERGE .githooks/gate-env.sh          # (no output)
$ curl -s .../actions/runs?per_page=100 | python -c '...Counter((event,conclusion))'
runs 77 first 2026-09-29T15:59:34Z  {('push','failure'):42, ('push','success'):18, ('schedule','failure'):17}
$ curl -s .../commits/9b46ae0f.../check-runs
total 4 | bar failure 9b46ae0f github-actions github | history-audit success ... ; statuses 0
$ curl -s .../actions/runs/38898108320  -> .github/workflows/remote-ci.yml 9b46ae0f push d41ly d41ly
$ grep -rh "on the daily held job" memory/builds/*/BACKLOG.md | wc -l   -> 53
```

**Where the records and the code disagree:**

- **CI publishes a per-SHA verdict.** The Deploy research (`research-deploy.md:94, 135`) and `gap-deploy-02` say CI "cannot publish". It cannot write a ref (`permissions: contents: read`, remote-ci.yml:37-38). It does publish a per-SHA check-run that anyone can read.
- **`ci` has no witness.** flow-steps `[deploy]` (`flow-steps.md:331`) says "under `ci`, the remote CI's result for the landed SHA is the witness". No code reads it: push-main starts nothing (`push-main.sh:434`), and pre-push reads only `bar-red`.
- **CI is red, not absent.** The handed fact says remote CI has been unavailable since 2026-10-14. The service still runs: there were push and schedule runs on 10-14, 10-15 and 10-16. What is missing is a usable verdict: every run since 2026-10-13 14:03 is red.

## 3. Attach points

| Attach point | Declared at | What integrations registers | Core without it |
|---|---|---|---|
| Verdict backends | Test's extension points, in prose only (`flow-steps.md:291-292`). **Not among Runtime's nine** (`layer-runtime.md:736-746`) | `remote-ci`, `peer-node` | `verdict: local-hook` (P3); pre-push decides |
| `deploy.core` witness under `GATE_POST_MERGE=ci` | `flow-steps.md:325-337` | The check-run reader | Local `post-merge.sh` keyed by SHA |
| Host adapters | `layer-runtime.md:744, 697-701` | `cloud-routine` | `requesting-node` / `os-scheduler` (the node tick) |
| Notification adapters | `layer-runtime.md:745` | Push channels | Terminal: turn micro-formats and parked rows |
| Promotion through environments | Deploy's extension points, prose only (`flow-steps.md:360-361, 484-487`). **No items, no registry** | Deploy engines, verify adapters, the `release.*` program | No release; the build closes at landing (`flow-steps.md:299`) |
| `build.closes: after-release-verifies` | `flow-steps.md:364-365` | The release record's final-environment verify | Value refused under `policy.on-missing-expansion: refuse` |
| Command adapters | `layer-runtime.md:739` | Each adapter's callable form, with its idempotence probe | — |
| Journal readers | `layer-runtime.md:746` | Tracker mirror (outbound) | Asks in BACKLOG.md only |
| Hook packs | `layer-runtime.md:742` | Secret-echo guard | No guard |
| CI emission into adopters | **Undeclared.** The validator alone exists (`govkit.py:5745`) | `ci-emit:github-actions` | No adopter CI job (`gap-deploy-03`) |
| Grant / secret provider | **Undeclared anywhere** | Grant record, secret resolver | Anonymous reads only |

Three points have no core declaration. Each must be declared by the core layer named, or the layer cannot attach under P28:

1. **Verdict backends:** Flow, in Test, as a registry.
2. **Environments, deploy engines and verify adapters:** Flow, in Deploy.
3. **Grants:** Runtime.

## 4. Candidates

### A. Kind per core point, with one shared adapter header (the pick)

**Mechanism.** Every adapter declares one header: name, kind, grant, `secret_ref`, witness source, probe, and DEAD PROBE semantics. It registers at the point of the core layer it serves. The header is a factory extracted from `read_held_reds`, which already has a SHA-shaped key, a literal host, no redirects, a 30 s and 4 MiB bound, and DEAD PROBE that never reads as green (`unattended.sh:9958-10015`).

**Losing test.**

- (a) Some adapter kind has no core fallback, so its slot would render empty.
- (b) No existing outside-service code fits the header, so the factory would be invented rather than extracted.

**Result: passes both.**

- (a) Every kind in §3 has a named fallback.
- (b) `read_held_reds` fits every header field, and it is live: 53 asks filed.

### B. Everything at Runtime's command-adapter point

**Mechanism.** Every adapter is a command that items call, and integrations declares no other point.

**Losing test.** Some kind is not a command an item calls.

**Result: LOSES.** Runtime's settled `[extend]` separates host adapters ("where the supervisor and its sessions run") and notification adapters from command adapters (`layer-runtime.md:739, 744-745`). Test's witness is "the runner-written verdict per tree, read by the pre-push hook" (`flow-steps.md:259`), not a command's exit code.

### C. Adopter CI as the single engine for verdict, release and schedule (Deploy research's pick B)

**Mechanism.** govkit emits one CI job that runs the bar, promotes and verifies. The core reads CI only.

**Losing test.** In gov, CI gives a green verdict that can be used for most landings.

**Result: LOSES as the mechanism.** 18 of 60 push runs were green and 0 of 17 scheduled runs (curl tally above). P3 already makes the local hook the verdict. C survives as one registered backend and as the `ci-emit` adapter.

### D. Every outside outcome published as a ref under `refs/gov/`

**Mechanism.** Extend `bar-red`: each runner pushes `refs/gov/<kind>/<sha>`, and the core reads refs only.

**Losing test.** Who writes the ref is a principal the certified pusher does not control.

**Result: LOSES.**

- `post-merge.sh` pushes `bar-red` from the landing node (`post-merge.sh:13, 249`).
- The 17 `refs/gov/runs/*` refs are written by agents' nodes.
- No signature exists (Test research C, `research-test.md:129-131`).

Refs stay as an index and a lease, never as a witness.

**The trust test applied to A's remote-CI backend.** It asks whether the source can be forged by the pusher.

- On a `push` event, GitHub runs the workflow definition from the pushed commit itself. This is platform behaviour, read from the docs and not measured here.
- `remote-ci.yml:15-16` says "no permanent gate grades this file's text". It has 4 commits on main.
- So a landing that edits `remote-ci.yml` certifies itself.

A therefore owes a workflow pin. The verdict counts only if the blob of `remote-ci.yml` at `head_sha` equals the pinned blob. Otherwise the change routes to the owner.

**What a remote verdict must carry to stand as a witness:**

| Field | Check |
|---|---|
| Key | `head_sha` equals the landed SHA, and that SHA's `^{tree}` equals `verdict.tree` |
| Writer | `app.slug=github-actions`; the run's `path` is the declared workflow; `event=push`; the job name is the declared name (`bar`) |
| Source trust | The workflow blob at `head_sha` equals the pinned blob |
| Liveness | The job's bar step concluded (not skipped), and the artifact `bar-<sha>` exists |
| Read failure | Any failed read is DEAD PROBE and counts as no verdict, never as green |

## 5. The contract, filled (pick A)

| Field | Integrations |
|---|---|
| Tag and definition | `layer.integrations`: adapters to outside services, each with a header (grant, `secret_ref`, witness source, probe), registered at a core point |
| Instruction units | The adapter-author unit (header fields, DEAD PROBE rule); the grant rule ("a secret is named, never written"); the release view; the deployer role's release instruction (the deployer "works only in the expansions", `flow-steps.md:346`) |
| Engine kits | `integrations` kit: the adapter registry and the header factory. Adapters: `verdict:remote-ci` (extracted from `read_held_reds`), `verdict:peer-node`, `host:cloud-routine`, `notify:<channel>`, `ci-emit:github-actions` (from `govkit.py:5745`), and deploy engines and verify adapters (dShippedRelease) |
| Record kinds | `remote-verdict` (a reading of a check-run: sha, tree, source, run id, workflow blob, conclusion); `release` (schema in §6); `notify-receipt`; `grant` (declared scopes, no values); `secret-scan` (counts and salted ids only) |
| Extension points declared | Environments (each with an engine and a verify adapter); grant providers (OS credential store, CI secret store) |
| Extension points used | Test's verdict backends; Deploy's promotion point; Runtime's host adapters, notification adapters, command adapters, journal readers (tracker mirror) and hook packs (secret-echo guard) |
| Policies and gates | Keys in §6. Gates: registry validation (names, not literals, `layer-runtime.md:748`); grant-scope probe; the workflow pin; the secret value scan |

## 6. Items and policies

### The release process

The release runs per SHA, per environment, after `deploy.core` is green. It is not the build's program unless `build.closes: after-release-verifies` holds.

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `release.pick` | command | Picks the newest landed SHA with a green `deploy.core` not yet in environment E, then takes E's promotion lease | The landing record and the per-SHA core verdict | `release.approve` |
| `release.approve` | owner, or command | Under `owner-approves-prod` (E = prod) or `owner-approves-each`, the owner disposes; else auto | The disposition record, or `auto-on-green` | Approve → `release.promote`; refuse → the release is closed as `held` |
| `release.promote` | command: E's engine adapter | Promotes the SHA into E; idempotent (already at the SHA counts as done) | The engine's own deployment id, read from the source keyed by (sha, env) | Promoted → `release.verify`; refused or unreachable → retry, then an owner item |
| `release.verify` | command: E's verify adapter | Verifies the SHA in E | The runner-written verify verdict keyed by (sha, env) | Green → `release.record`; red → `release.route`; DEAD PROBE → an owner item |
| `release.route` | command | Applies `deploy.on-verify-fail` | The routing record | `roll-forward` → an ask filed and E marked red at the SHA; `rollback-and-ask` → `release.promote` of E's last verified SHA, then an ask; `halt-and-alert` → E's lease frozen and an owner request sent through the notification adapter |
| `release.record` | command, through `record` | Writes the release record | The record | The next environment, under `auto-on-green`; at the final environment, the build's `deploy.close` when `after-release-verifies` |

**The release record schema.**

- **Id and home:** id `<sha8>-<env>-<n>`. Home: a per-SHA trail outside any build folder, because a release carries several builds.
- **Fields:** `sha`, `tree`, `env`, `env_order`, `from_sha`, `builds[]` (from the landing records between `from_sha` and `sha`), `core_verdict`, `approval`, `engine{adapter, version, deployment_id, source}`, `promote_outcome`, `verify{adapter, verdict, source, run_id}`, `route`, `ask`, `node`, `started`, `finished`.
- **Lifecycle:** `open → promoted → verified | red → rolled-back | rolled-forward | halted`.
- **Check:** each witness is re-read from its source.

**Naming apart.** The core's `deploy.release` deletes lease refs and closes the mailbox (`flow-steps.md:322`). Rename it `deploy.unlease`. "Release" then names only the promotion process (`release.*`, the `release` record).

### Notification adapters

A notification adapter is send-only. Its witness is the service's receipt id, kept in `notify-receipt`. The owner's answer always returns through `next` and the owner's controls, never through the channel. That keeps out an inbound path that would need a secret, and keeps out a message being read as consent.

### Policy keys

| Key | Allowed values | Default | Why |
|---|---|---|---|
| `verdict.remote.trust` (new) | `pinned-workflow`, `owner-reviews-workflow-change` | `pinned-workflow` | The pushed commit's workflow certifies itself otherwise (§4) |
| `notify.channel` (new) | Registered names | `terminal` | Validated against the registry, not a literal list |
| `secrets.scan` (new) | `value-gate`, `value-gate+shape-report`, `shape-report` | `value-gate+shape-report` | A shape scan reds on examples (§7) |
| `integrations.reads` (new) | `anonymous-only`, `granted` | `anonymous-only` | Today's only live reader needs no credential |
| Catalogued keys | `verdict`, `run.host`, `maintain.host`, `notify.owner`, `deploy.runs`, `deploy.promotion`, `deploy.on-verify-fail`, `build.closes` | As catalogued | Integrations is the reader of the `remote-ci`, `peer-node`, `cloud-routine`, release and push-notification values |

### Grants and secrets

- **Declaration.** The header carries `[grant] service`, `scopes[]`, `secret_ref` (a name, such as `cred:gov/github-deploy` or `env:DEPLOY_TOKEN`), and `anonymous = true|false`. The value never appears there.
- **Where the secret lives.** It lives in the node's OS credential store, or in the CI secret store for adapters that run in CI. It is resolved just in time into the adapter process's environment only.
- **Scope probe.** The adapter calls the service once and compares the granted scopes with the declared ones, for example GitHub's `X-OAuth-Scopes`. Wider than declared is refused.
- **Proof the secret is absent.** The adapter's runner, the one principal holding the value, scans for the literal value and its URL-encoded and base64 forms. It covers tracked files, `memory/`, the journal and the session transcripts runlog reads. It records only a hit count and a salted id. Zero hits is the witness.
- **The early report.** A shape scan with runlog's table reports, and does not gate.

## 7. Gaps

**Closed by the pick:**

- **`gap-deploy-01`:** the `release.*` program, environments, engines and verify adapters.
- **`gap-deploy-02`:** the remote-verdict record keyed by SHA, a reader for `GATE_POST_MERGE=ci`, and the release record per (sha, env).
- **`gap-deploy-03`:** the `ci-emit` adapter at a declared point.
- **`gap-deploy-05`:** each outbox order becomes a release item with a witness. It is graded by `release.record`, not by prose.

**New gaps exposed:**

| New gap | Evidence |
|---|---|
| `GATE_POST_MERGE=ci` has no witness. The flow record says it does. | `push-main.sh:434`; pre-push reads only `bar-red` (`:1919-1936`); `flow-steps.md:331` |
| A remote verdict's source is self-certifying | Push workflows run the pushed definition; no gate grades `remote-ci.yml` (`:15-16`) |
| No secret check exists | 0 legs. The shape scan over 4,650 tracked files found 58 hits in 22 files, all of them examples or fixtures (for example `https://u:p@`, `sk-ant-api03-XXXX`). Value hits: 0. |
| No channel reaches the owner outside a session | 0 Notification hooks, 0 channel code; settings hook events listed in §2 |
| The verdict-backend, environment and grant points are undeclared | `layer-runtime.md:736-746`; `flow-steps.md:291-292, 360-361` are prose only |
| An integration is buried in the unattended kit | `read_held_reds` (`unattended.sh:9972`) has no registration. The `deploy.core` CI reader would be the second instance, so extract the factory. |

The secret-scan measurement:

```
$ git ls-files -z | python -I -c '<compile redaction.tsv rows, finditer over every text file>'
scanned 4650 files; total hits 58 in 22 files
url-userinfo 20/14 · env-assign 18/10 · json-secret 12/2 · ... ; memory/ files hit: 10
```

## 8. Forks

| Fork | Options | Recommendation |
|---|---|---|
| Does remote CI become a pre-landing backend? | (a) post-landing witness only (for `deploy.core`); (b) also pre-landing, through a staging-ref trigger; (c) neither | (a). CI is red on every run since 2026-10-13 14:03, P3 stands, and (b) adds a lander staging step |
| How the remote verdict is trusted | `pinned-workflow` vs `owner-reviews-workflow-change` | `pinned-workflow` |
| Naming | Rename `deploy.release` to `deploy.unlease`, or keep it and call the process `promote` | Rename; "release" is the process the owner's words name |
| Trackers | (a) no kind, an outbound mirror as a journal reader; (b) a tracker kind with inbound intake | (a). 0 tracker use, asks are the record (P30), and an issue is not consent |
| Where secrets live | OS credential store, CI secret store, or both by host | Both, chosen by the adapter's host; never a file in the repository |
| Where the three missing points are declared | Verdict backends and environments in Flow, grants in Runtime, or all three in Runtime's registry | Flow for the first two (its items consume them), Runtime for grants |

These are the files I read or measured:

- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/.github/workflows/remote-ci.yml`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/unattended/unattended.sh`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/push-main.sh`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/run-gates/post-merge.sh`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/.githooks/pre-push`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/govkit/govkit.py`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/runlog/redaction.tsv`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`
