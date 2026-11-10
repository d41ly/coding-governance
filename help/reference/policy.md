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

## `platforms.provision`
Documented on [help/python-floor.md](../python-floor.md).

## `install.deprecation-window`
Documented on [help/shims.md](../shims.md).

## `install.on-shim-call`
Documented on [help/shims.md](../shims.md).

## `install.retired-edits`
Documented on [help/update-edits.md](../update-edits.md).

## Not yet summarised (242)
- `preset`
- `design.forks`
- `design.reentry`
- `autonomy`
- `attendance`
- `attendance.scope`
- `policy-file.guard`
- `policy-file.proof`
- `floor`
- `hooks.bypass`
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
- `tests.without-cadence`
- `verdict`
- `verdict.blocks`
- `verdict.held`
- `verdict.flakes`
- `verdict.flakes.entry`
- `verdict.flakes.release`
- `tests.product`
- `tests.landing-levels`
- `verdict.tree`
- `verdict.red-route`
- `verdict.remote.trust`
- `verdict.remote.pin-scope`
- `verdict.remote.pin`
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
- `trace.leg-output`
- `trace.rows`
- `runtime.binary`
- `runtime.owner-harness`
- `runtime.act-harness`
- `runtime.act-auth`
- `platforms.supported`
- `platforms.verify`
- `install.steps`
