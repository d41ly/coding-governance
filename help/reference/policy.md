<!-- gov:rendered from tools/playbook/references.toml doc.reference.policy; edit the registry, not this page -->
<!-- unit: unit.policy-schema -->
# Policy

## `charter.override`
<!-- usage: policy:charter.override 0cd8bb7f -->
Which wins when a live instruction conflicts with the charter: the charter unless the owner overrides it in so many words, the live owner instruction, or the charter always; an override taken is recorded in the build's folder.

```text
charter.override = "absolute"
```

## `charter.practices`
Documented on [help/charter.md](../charter.md).

## `core.bypass`
<!-- usage: policy:core.bypass 110702af -->
Whether a permitted bypass skips the core checks with every other leg, its core red reported or blocking after, or never: under never the meta-check reds a core leg that carries a leg guard.

```text
core.bypass = "never"
```

## `core.exceptions`
<!-- usage: policy:core.exceptions d1e9338d -->
Which exception records excuse a core red: any well-formed record a session wrote, only an owner-written one whose expiry is still ahead, or none, every record then red.

```text
core.exceptions = "owner-only-expiring"
```

## `policy-file.on-invalid`
Documented on [help/policy.md](../policy.md).

## `hooks.bypass`
<!-- usage: policy:hooks.bypass c687519d -->
Whether a hook bypass is only recorded or also refused. Under both values each one is recorded as a decision=bypass line in the git common dir's runlog/pushes.log: a landing the pre-push hook never allowed, which the lander reports landed UNGATED, and a pushed pass commit with no Commit-Checked: trailer, which the unattended commit check never saw. Under allowed the push proceeds and the pass-order leg lists such commits as a note. Under refused the pre-push hook refuses them, the pass-order leg reds on them, and the lander and the hook refuse every landing until verdict names an off-node backend, since a hook on the bypassing node cannot refuse its own bypass. Read at the default branch's tip by the hook, at the landed revision by the lander, and at the graded commit by the leg.

```text
hooks.bypass = "refused"
```

## `runtime.agents-in-flight`
Documented on [help/agent-limit.md](../agent-limit.md).

## `instructions.checks`
<!-- usage: policy:instructions.checks 24ae9920 -->
What a render does when a reader's load set lacks a unit its required-by names: refuse the render, render with a missing-unit line the reader sees, or render and record the gap in the prompt record.

```text
instructions.checks = "warn"
```

## `instructions.edit`
<!-- usage: policy:instructions.edit 37b2ab67 -->
Who writes an instruction unit: the owner through the write command with agents only proposing, any caller of it, or only the flow's item.

```text
instructions.edit = "command-for-all"
```

## `instructions.proof`
<!-- usage: policy:instructions.proof 13cf41a9 -->
What shows the write command's caller is the owner: standard error being a terminal, with the signed proof and both refused until that component lands.

```text
instructions.proof = "tty-cli"
```

## `instructions.exclude`
<!-- usage: policy:instructions.exclude 16feadce -->
Which of gov's instruction units and registered rows your repository leaves out: each listed gov tag is absent from the composition and its state reads excluded; a tag no unit or row of gov's holds is refused.

```text
instructions.exclude = ["unit.push-after-review"]
```

## `instructions.stale`
<!-- usage: policy:instructions.stale c32256b2 -->
What update does when gov changed the meaning of a unit your overlay pins: render both texts and write an outbox order, hold the update until you re-pin, or render both and journal the edge with no order.

```text
instructions.stale = "warn"
```

## `review.spec-audit.disposal`
Documented on [help/spec-audit.md](../spec-audit.md).

## `review.spec-audit.chain-stop`
Documented on [help/spec-audit.md](../spec-audit.md).

## `review.spec-audit.chain-ceiling`
Documented on [help/spec-audit.md](../spec-audit.md).

## `bar.inline-red-fixes`
Documented on [help/red-fix-lane.md](../red-fix-lane.md).

## `pass.fast-legs`
Documented on [help/pass-legs.md](../pass-legs.md).

## `memory.staged-render`
Documented on [help/commit-render.md](../commit-render.md).

## `tests.without-cadence`
<!-- usage: policy:tests.without-cadence e2b76654 -->
What a landing does with the product-test levels outside tests.landing-levels where no cadence runs them: runs them at landing anyway, reports them unrun, or waits for a cadence to be set up.

```text
tests.without-cadence = "report-unrun"
```

## `verdict`
<!-- usage: policy:verdict 0427cc96 -->
Which backend's verdict a landing stands on, a name a [[verdict_backend]] row in a kit descriptor declares: local-hook, this node's own hook's full per-tree verdict; peer-node, a second node's verify-peer tag for the commit's own tree; or remote-ci, a push run of the remote CI workflow under verdict.remote.trust. Read at the landed revision by the lander before each landing push, which under any backend but local-hook lands only on GREEN; a value no row declares refuses before any push.

```text
verdict = "peer-node"
```

## `verdict.blocks`
<!-- usage: policy:verdict.blocks 2f0b7c25 -->
Which red of a red bar blocks its landing, by the class the runner's attribution reads each red at: under own-only an OWN or DEAD PROBE red blocks, under own-mixed-contended a MIXED or CONTENDED red blocks too, and under every-red an INHERITED red blocks as well. Read at the default branch's tip by the pre-push hook and the unattended driver; a red bar lands only when every red passes.

```text
verdict.blocks = "own-mixed-contended"
```

## `verdict.held`
<!-- usage: policy:verdict.held dff3fa99 -->
When a held leg runs, read at the default branch's tip: under on-demand it is held at every bar unless GATE_SELFTESTS asks for it; under push-selected the pre-push hook exports GATE_SELFTESTS=changed for its bar when the pusher set nothing, so the held legs the push moved run; under peer-or-cadence it is held at the push and runs elsewhere, a HELD_CI_WORKFLOW in .unattended.conf or a registered peer backend, and the selection refuses where neither is declared.

```text
verdict.held = "push-selected"
```

## `verdict.flakes`
<!-- usage: policy:verdict.flakes cbd3373b -->
What a red bar's flakes do, read by the run-gates kit's `verdict_flow.py flakes` after a bar run under GATE_RERUN=1, which re-runs each red leg once on the same tree: under retry-only nothing is written; under record each such run writes one `flake` record, a row per executed leg with its first rc and its re-run rc; under quarantine it also holds each leg whose flakes reach verdict.flakes.entry and no OPEN held-flaky-leg ask names, and the unattended close files that ask, which holds the leg through the selection's quarantine row: the held leg still runs at least once a day, outside the verdict, so its greens accrue in the flake records, and it is released, its ask closed, after verdict.flakes.release consecutive greens.

```text
verdict.flakes = "record"
```

## `verdict.flakes.entry`
<!-- usage: policy:verdict.flakes.entry abdb1ee4 -->
How many flakes in a leg's last window of verdicts hold it under verdict.flakes quarantine, counted across the tracked flake records, newest first and after the leg's last release: a declared count/window such as 3/10, or measured, the Measured field of the newest gate-health record, and 2/10 until one exists.

```text
verdict.flakes.entry = "3/10"
```

## `verdict.flakes.release`
<!-- usage: policy:verdict.flakes.release 81b1e216 -->
How many consecutive greens release a leg held under verdict.flakes quarantine, read at the default branch's tip by the run-gates kit's `verdict_flow.py select`: the leg's executed rows in the tracked flake records since its held-flaky-leg ask was filed, newest first, must open with this many greens, a red resetting the count; a leg whose manifest row changed since that filing is released too. The unattended close then writes the ask's CLOSED row.

```text
verdict.flakes.release = 5
```

## `tests.product`
<!-- usage: policy:tests.product a994fddb -->
Which product-test legs, the legs carrying a level, the manifest holds: the repository's own declared ones, those plus one leg per level each detected runner adapter declares, or none at all.

```text
tests.product = "declared"
```

## `tests.landing-levels`
<!-- usage: policy:tests.landing-levels a3cbde00 -->
Which product-test levels a landing runs, from unit, integration, e2e and performance, or every level the manifest declares; the slower levels left out are tests.without-cadence's.

```text
tests.landing-levels = ["unit", "integration", "e2e"]
```

## `verdict.tree`
<!-- usage: policy:verdict.tree e2b80358 -->
Which tree Test verifies: the merge `push-main.sh --prepare` makes of the build onto the advertised tip, or the build's own tip pinned with no merge, `--land` then making the landing merge.

```text
verdict.tree = "build-tip"
```

## `verdict.red-route`
<!-- usage: policy:verdict.red-route ad9f8979 -->
Where the tester's judgment of a blocking OWN or MIXED red sends it: under fix-pass-or-design a code-miss goes to a fix pass and a spec-wrong to a new unit through Design, and under always-new-unit both go to a new unit. Read by run-gates' verdict_flow.py judge.

```text
verdict.red-route = "always-new-unit"
```

## `verdict.remote.trust`
<!-- usage: policy:verdict.remote.trust 562844dc -->
What the remote-ci backend does with the source check of its witness rule: under pinned-workflow pinned files that differ from verdict.remote.pin read HELD and an owner item asks to re-pin or to refuse; under owner-reviews-workflow-change the owner item opens at the first differing read and the slot stays HELD until the owner re-pins; under app-only the source check is skipped and a passing run reads GREEN with witness claimed, never witnessed.

```text
verdict.remote.trust = "owner-reviews-workflow-change"
```

## `verdict.remote.pin-scope`
<!-- usage: policy:verdict.remote.pin-scope 48608634 -->
Which files verdict.remote.pin pins for the remote-ci backend: workflow, the declared workflow .github/workflows/remote-ci.yml; or dispatch-closure, that workflow, the run-gates kit's run-gates.sh, the leg manifest and .githooks/gate-env.sh, the files that decide the bar's dispatch, never every script the bar job runs.

```text
verdict.remote.pin-scope = "dispatch-closure"
```

## `verdict.remote.pin`
<!-- usage: policy:verdict.remote.pin fc4016ee -->
The pin the remote-ci backend's source check compares against: one object id, git hash-object --stdin over one &lt;path&gt; &lt;blob id&gt; line per file verdict.remote.pin-scope names, sorted by path, each ending LF, which the run-gates kit's remote_verdict.py pin prints at HEAD. The owner's: set from a terminal or by policy_edit.py set on a live run's branch, and the loop guard refuses an agent's change to it anywhere else. Unset, remote-ci reads HELD, no pin.

```text
verdict.remote.pin = "1fe706824a048fd582f17ef18b4ec6b2d9898d46"
```

## `verdict.peer.signers`
<!-- usage: policy:verdict.peer.signers 6c292dc2 -->
Which node keys may sign a peer-node verdict: one allowed-signers line per node, its node tag, its SSH key type and its base64 public key, with no options field. The peer-node reader reads it at the landed revision, verifies the refs/gov/verdict/&lt;sha&gt; tag with git verify-tag against it, and lets the verdict stand only when the signing key's node tag is the tag's node line and not the reading node's own. The owner's: set from a terminal or by policy_edit.py set on a live run's branch, and the loop guard refuses an agent's change to it anywhere else. Unset, every peer-node read is NONE, no signer table.

```text
verdict.peer.signers = ["b ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIA01XHzWJLfi5hyD6zkT39tg7Apyf1k93ZQ2h2VvlYuK"]
```

## `help.enforce`
Documented on [help/docs-leg.md](../docs-leg.md).

## `budgets.enforce`
Documented on [help/size-caps.md](../size-caps.md).

## `budgets.pinned`
Documented on [help/size-caps.md](../size-caps.md).

## `tags.slice`
Documented on [help/tags.md](../tags.md).

## `tags.retired-cites`
Documented on [help/tags.md](../tags.md).

## `tags.positional`
<!-- usage: policy:tags.positional bc023779 -->
What `gov tag check` does with a positional reference, a file:line citation or a section number: red it unless the positional list holds it, red it listed or not, or only print it.

```text
tags.positional = "report"
```

## `tags.bare-refs`
Documented on [help/tags.md](../tags.md).

## `tags.bundle`
<!-- usage: policy:tags.bundle e4fb27ff -->
What `gov tag bundle` does with a range's content: print the manifest alone and refuse --inline, inline every call under its --bytes budget, or print the manifest and inline on --inline.

```text
tags.bundle = "manifest"
```

## `tags.bundle-rows`
<!-- usage: policy:tags.bundle-rows e1e46026 -->
How many rows `gov tag bundle` prints before it folds rows by their kit directory, the largest group first; --under opens a folded group.

```text
tags.bundle-rows = 80
```

## `instructions.legacy`
<!-- usage: policy:instructions.legacy 9488cebe -->
What the render gate does with the list of instruction files not yet rendered from units: hold it to shrinking, a listed file rendered from units reading as stale, or refuse every listed file.

```text
instructions.legacy = "refuse"
```

## `trace.leg-output`
<!-- usage: policy:trace.leg-output b5f47620 -->
Where a failing leg's output tail lives: kept by its hash in the common dir and named in the verdict under either value, and under `tail-by-hash` also committed as a `leg-tail` record by the run-gates kit's `keep_tails.py`.

```text
trace.leg-output = "node-local"
```

## `platforms.provision`
Documented on [help/python-floor.md](../python-floor.md).

## `install.deprecation-window`
Documented on [help/shims.md](../shims.md).

## `install.on-shim-call`
Documented on [help/shims.md](../shims.md).

## `install.retired-edits`
Documented on [help/update-edits.md](../update-edits.md).

## Not yet summarised (226)
- `preset`
- `design.forks`
- `design.reentry`
- `autonomy`
- `attendance`
- `attendance.scope`
- `policy-file.guard`
- `policy-file.proof`
- `floor`
- `transitions.record`
- `leases`
- `leases.granularity`
- `leases.renewal`
- `leases.expiry-hours`
- `leases.overlap`
- `leases.offline`
- `leases.queued-claim-days`
- `leases.offer-seconds`
- `deps.coordination`
- `deps.early-build`
- `deps.messaging`
- `landing.order`
- `card.follows`
- `placement`
- `placement.check`
- `kickoff.runs`
- `card.store`
- `card.snapshot`
- `actions.free`
- `resume.partial`
- `resume.context`
- `orient.budget`
- `driver.reads`
- `prompts.author`
- `roles.retries`
- `roles.no-spawn`
- `roles.trust`
- `roles.answered-calls`
- `roles.verifier-context`
- `roles.on-contradiction`
- `roles.effort.<role>`
- `roles.effort.<workflow>.<stage>`
- `roles.effort.default`
- `roles.model.<role>.<harness>`
- `roles.harness.<role>`
- `roles.auth.<role>`
- `reuse.delivery`
- `reuse.propose`
- `annotations.grammar`
- `builds.agent-root`
- `asks.acceptance`
- `decisions.major`
- `builds.slug-words`
- `builds.slug-style`
- `builds.slug-date`
- `lexicon.pin`
- `lexicon.forced`
- `lexicon.at-commit`
- `lexicon.drift`
- `lexicon.packs`
- `review.opt-in`
- `runtime.spawn-backend`
- `runtime.relaunch`
- `runtime.act-ceiling`
- `runtime.hold-ceiling`
- `runtime.no-progress`
- `runtime.refusal-repeats`
- `runtime.restarts`
- `runtime.hook-failure`
- `runtime.admission-scope`
- `runtime.attended-judge`
- `runtime.attended-allowance`
- `runtime.harnesses`
- `runtime.journal`
- `runtime.secret-home`
- `runtime.secret-scan`
- `plan.ratification`
- `run.host`
- `notify.owner`
- `notify.channel`
- `notify.owner-items`
- `run.owner-deadline`
- `run.on-owner-silence`
- `run.on-owner-question`
- `deps.landing`
- `mailbox.reads`
- `mailbox.notice`
- `mailbox.fetch-seconds`
- `review.follow-up`
- `prompts.batch`
- `context.on-full`
- `context.threshold`
- `card.pointers`
- `notices.record`
- `review.breakpoints`
- `probe.points`
- `probe.raise`
- `probe.observations`
- `probe.experiment.authority`
- `deps.on-parent-withdrawn`
- `review.design.rounds`
- `review.design.round-count`
- `review.max-rounds`
- `review.design-audit.runs`
- `review.design-audit.seed`
- `review.unverified`
- `review.unclassed`
- `flow.route-backs`
- `flow.rework-budget`
- `flow.on-exhausted`
- `flow.wait-ceiling`
- `flow.scenario-default`
- `flow.scenario-conflict`
- `flow.adapt`
- `flow.promote`
- `policy-file.on-missing-expansion`
- `plan.authority`
- `plan.unplaced`
- `plan.triage`
- `plan.kickoff`
- `design.handoff`
- `design.overlap`
- `design.streams-when`
- `design.coverage`
- `design.coverage.semantic`
- `deviation.gate`
- `deviation.approval`
- `help.explanation`
- `help.atlas`
- `build.scope`
- `build.reuse-check.second-pass`
- `build.worktree`
- `build.push`
- `build.unit-holders`
- `build.spend-cap`
- `deploy.runs`
- `deploy.promotion`
- `deploy.on-verify-fail`
- `deploy.currency`
- `currency.max-behind`
- `currency.on-behind`
- `install.from`
- `install.guards`
- `build.closes`
- `build.release-hold`
- `build.release-ceiling`
- `kits.cadence`
- `kits.host`
- `kits.watch-cadence`
- `release.environments`
- `integrations.tracker`
- `maintain.host`
- `maintain.cadence`
- `maintain.fixes`
- `maintain.on-breach`
- `maintain.events`
- `maintain.reading-tree`
- `maintain.node-readings`
- `maintain.reading-admission`
- `maintain.dead-after`
- `maintain.record-when`
- `maintain.security-review`
- `maintain.tiers`
- `maintain.interpreter-eol`
- `observability.run-record`
- `patch.ratify`
- `review.<stage>`
- `review.<stage>.effort`
- `review.recommendation`
- `review.build.when`
- `review.findings`
- `review.blocks`
- `review.left-shift`
- `review.recommendation.source`
- `review.loop.cadence`
- `review.loop.retire`
- `review.loop.window-days`
- `review.loop.catch-source`
- `budgets.*`
- `annotations.lookup`
- `annotations.resolve-scope`
- `annotations.delivery`
- `instructions.slices`
- `instructions.task-charter`
- `review.twin`
- `roles.shape-enforce`
- `roles.orientation.house-index`
- `memory.default-load`
- `memory.code-budget`
- `memory.code-roles`
- `memory.code-languages`
- `memory.code-enrich`
- `memory.load-budget`
- `memory.item-budget`
- `memory.over-budget`
- `memory.mirror`
- `memory.project-map`
- `memory.map-budget`
- `memory.map-overflow`
- `memory.map-unfold`
- `memory.map-purpose`
- `memory.legacy-anchors`
- `memory.superseded-slices`
- `retrofit.drain`
- `retrofit.drain-cap`
- `retrofit.claim-on-touch`
- `retrofit.claim-cap`
- `retrofit.widen`
- `retrofit.unseeded`
- `retrofit.reconstruct`
- `retrofit.decisions`
- `retrofit.practice-pending`
- `retrofit.cadence`
- `retrofit.slot-bytes`
- `commits.edge-check`
- `commits.squash`
- `trace.identity`
- `trace.cost`
- `trace.rows`
- `runtime.binary`
- `runtime.owner-harness`
- `runtime.act-harness`
- `runtime.act-auth`
- `platforms.supported`
- `platforms.verify`
- `install.steps`
