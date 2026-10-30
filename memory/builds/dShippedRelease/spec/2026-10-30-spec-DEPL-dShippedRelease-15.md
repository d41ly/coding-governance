# DEPL-dShippedRelease-15 — promotion through environments: the `integrations` kit, the seven `release.*` items and a compare-and-swap on every promote

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 12 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0425@3b7313d6 whole
**Carries:** node:item.release.pick
**Carries:** node:item.release.approve-auto
**Carries:** node:item.release.approve-owner
**Carries:** node:item.release.promote
**Carries:** node:item.release.verify
**Carries:** node:item.release.route
**Carries:** node:item.release.record
**Carries:** node:record-kind.release
**Carries:** node:record-kind.release-exit
**Carries:** node:policy-key.deploy.runs
**Carries:** node:policy-key.deploy.promotion
**Carries:** node:policy-key.deploy.on-verify-fail
**Carries:** node:policy-key.release.environments

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-3-reuse-scout-c.md](../build/2026-10-30-build-DEPL-dShippedRelease-3-reuse-scout-c.md) | research | DEPL-dShippedRelease-3 DEPL-dShippedRelease-6 DEPL-dShippedRelease-8 DEPL-dShippedRelease-19 DEPL-dShippedRelease-22 DEPL-dShippedRelease-26 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |

<!-- /gen:spec-records -->

## 1. Goal

An adopter's release, environments, rollout, rollback and post-deploy verification are not addressed,
and one adopter built all of it outside gov (`gap-deploy-01`). This unit builds promotion after
landing as an integrations extension point: the `integrations` kit with its adapter header, the
release slot, the seven `release.*` items, and the records they write. E's promotion lease is a
cadence lease named `release/<E>` with its epoch, and every engine adapter's promote and rollback is a
compare-and-swap on E's current deployment id read at the pick, so a stale holder's rollback after a
take-over changes nothing. An engine that cannot compare-and-swap declares that gap and runs only
where `deploy.runs` names the operator.

## 2. Scope (IN)

- **S1** — The kit, by `python tools/playbook/core.py new kit integrations --layer layer.integrations`
  (DEPL-dShippedRelease-10 S4): `tools/integrations/kit.toml`, `requires = ["loop", "runtime"]`,
  holding `adapters.py`, `release.py`, `release_fixture.py` and `README.md`. No clause of the 31 names
  the kit and v2's `layer-expansions.md:327` does, so this unit creates it (scout C disagreement 8).
  Observed by AC1.
- **S2** — The header factory (I11). `check_adapter_header(row)` in `tools/integrations/adapters.py`
  returns the reason it refuses a row, or None: `kind` outside `ADAPTER_KINDS`, or an empty `grant`,
  `witness-source`, `probe` or `fallback`; `grant.secret` is the `secret` field, read where
  TOOL-dWellOiledMachine-17 S1 nests it and never copied. A `deploy-engine` row needs `cas`. `python
  adapters.py --check` runs it over every `[[adapter]]` row of `tools/runtime/points.toml` carrying a
  `kind`, and `python adapters.py new <point> <name> --kind <k> …` appends a conforming row and
  refuses a non-conforming one. `ADAPTER_KINDS` opens as `deploy-engine`, `verify` and
  `release-runner`; each later kind joins in its own unit. A probe's failed read is a dead probe,
  never green (`read_held_reds`, `tools/unattended/unattended.sh:10113`, the shape it extracts).
  Observed by AC2.
- **S3** — The slot. A `[[point]]` row `point.flow.release` in `tools/runtime/points.toml`, the spelling
  KICK-dKeptSession-1 §4 and DEPL-dShippedRelease-6 read, its `contract` S5's verbs; the `uses` of
  `layer.integrations` in `tools/playbook/layers.toml` gains it. A `[[adapter]]` row `name =
  "release-runner"`, `kind = "release-runner"`, `run` `python <prefix>/integrations/release.py tick`.
  `run_release_slot(sha, root)` in `tools/loop/deploy_items.py`, on `deploy.core`'s green route, runs
  each `release-runner` row detached and prints `release slot — <n> runner(s)`. A core read of a core
  point, so no core file names this kit, and with no row it prints `0 runner(s)`. Observed by AC3.
- **S4** — The environments. `read_environments(root)` in `release.py` reads
  `read_policy_value("release.environments", root)`, its order the promotion order, and refuses by
  `check_environment_name` a name `git check-ref-format` rejects as a ref segment, which the row's
  regex admits (`a..b`, `x.lock`). Each environment's values are three catalogue pattern rows in
  `tools/policy/catalogue.toml`, `release.env.<environment>.engine`, `.verify` and `.production`
  (§4 "The rows"). A listed name with no `engine` or `verify` refuses naming the key. Environment
  names are policy, never `tools/runtime/points.toml`, which update overwrites (pin C11). An empty
  list runs nothing. Observed by AC4.
- **S5** — The engine contract (I12), every `deploy-engine` row's `run` taking `read-current <E>`,
  `promote <E> <sha> --expect <id>`, `rollback <E> <sha> --expect <id>` and `read-back <E> <sha>`, and
  exiting 0 done, 2 refused, 3 compare-and-swap refused, 4 unreachable. `run_engine_verb(row, verb,
  args)` in `release.py` is the one caller. Observed by AC5.
- **S6** — `release.pick`, `run_release_pick(E, root)`. It takes E's promotion lease by `unattended.sh
  --lease acquire run release <E>`, a `live-holder` refusal printing `release — <E> · skip · held
  elsewhere`, a stale holder taken by `--lease take-over run release <E>` (pin C11). It picks the
  newest landed SHA with a green `read_core_verdict` (DEPL-dShippedRelease-13 S3) that E lacks, walking
  `read_landing` over the default branch's first-parent line; for the second environment on it picks
  only among SHAs verified in the environment before. Under the lease it reads `read-current <E>` and
  writes `<common-dir>/release/<E>.pick`, the SHA, the id and the epoch. None to pick releases the
  lease with no `--as` and prints `nothing`. Observed by AC6.
- **S7** — The approvals. `read_policy_value("deploy.promotion", root)`: `auto-on-green` passes every
  environment through `release.approve-auto`; `owner-approves-each` raises
  `raise_owner_item("release-approval", …)` for every environment, and `owner-approves-prod` for one
  whose `.production` is true, every other passing auto. A refusal is `release.record` with outcome
  `held`. An open item exits 3 and the next tick reads the answer. Observed by AC7.
- **S8** — `release.promote`, `run_release_promote(E, root)`: `promote <E> <sha> --expect <id>` with the
  id read at the pick. Exit 3 prints `release — <E> · stale · compare-and-swap refused`, and it
  records nothing and releases nothing, the stale holder's effect void as a fenced push's is, the
  lease's new holder running E. Exit 2 or 4 retries once, then raises `release-retry`, answered as
  `run.on-owner-question` says: retry again, or `release.record`, outcome `unverified`. A row whose
  `cas` is `none` refuses unless `deploy.runs` is `operator`, naming the gap. Observed by AC5, AC8.
- **S9** — `release.verify`, `run_release_verify(E, root)`: E's `verify` adapter, `<run> <E> <sha>`, exit
  0 green to `release.record`, 1 red to `release.route`, 3 needing judgment, anything else a dead probe
  raising an owner item: verify again, or `release.record`, outcome `unverified`. On 3 the output goes
  to `<common-dir>/release/<E>.verify`, the item prints `needs judgment` and exits 3, and `python
  release.py judge <E> <sha> <answer>` takes `gov-deployer`'s `verify` return (DEPL-dShippedRelease-23
  S4): `real-failure` routes as red, `probe-failure` as a dead probe, `undecided` raises the item.
  Observed by AC9.
- **S10** — `release.route`, `run_release_route(E, root)`, by
  `read_policy_value("deploy.on-verify-fail", root)`, writing a `routing` record. `roll-forward` files
  the ask and ends `rolled-forward`. `rollback-and-ask` reads E's last verified SHA from E's release
  records, runs `rollback <E> <that sha> --expect <current id>`, the same compare-and-swap, re-verifies
  and files the ask, ending `rolled-back`; no verified SHA ends `halted`. `halt-and-alert` ends `halted`
  and raises `release-halted`, and `release.pick` refuses E while that item is open. Each ask is
  `python intake.py file --origin cadence --filer item.release.route` with the text
  `release-verify-failed <sha> <E>`, so its key is that reading and (SHA, E). Observed by AC10.
- **S11** — `release.record`, `run_release_record(E, root)`, idempotent: `write_release(sha, environment,
  fields, root)` writes one record per (SHA, environment) at `derive_release_ref(sha, environment)`,
  then releases E's lease with no `--as`, a hand-over. `verified` goes on to the next environment. A
  `verified` at the last environment, or any other outcome, writes the exit record
  `refs/gov/release-exit/<sha>` by `write_release_exit` (I13), keys `sha`, `outcome`, `environment`
  and `release-id`, the record's commit. `python release.py record <sha> <environment> --outcome <o>` is
  `write_release`'s verb, which DEPL-dShippedRelease-27's publication calls. Observed by AC11.
- **S12** — `deploy.runs`, `read_policy_value("deploy.runs", root)`. `landing-node`: the node's tick
  runs the pass. `adopter-ci`: the node's tick prints `release — adopter-ci` and runs nothing, the
  adopter's job running `release.py tick --ci`, refused under any other value, and the outcome read
  back by SHA through `read_release`. `operator`: `release.promote` raises `release-operator`, the
  owner runs the engine and answers, and `read-back <E> <sha>` confirms before `release.verify`.
  Observed by AC8, AC12.
- **S13** — The wake (§8 F2): S3's slot on a green `deploy.core`, and a `point.cadence-items` row `release`
  (TOOL-dWellOiledMachine-59 S1), `host-key = "run.host"`, `period = "daily"`, `run` the same `tick`, so
  a SHA whose node died, and every pass under the default `at-landing`, is reached with no build
  lease. `run_release_tick(root)` runs one pass per listed environment in order, each under its own
  lease. Observed by AC13.
- **S14** — The items: seven `[[item]]` rows in `tools/loop/loop.toml`, `step = "step.deploy"`, `actor`
  `command:release.<name>`, `owner = "dShippedRelease"`, transcribed from `layer-expansions.md:385-393`,
  their first `needs = []`, so no core item waits on one. Each has a `point.command-adapters` row,
  `class = "idempotent"`. Observed by AC14.
- **S15** — The kinds: `release` and `release-exit` rows in `tools/memory-tree/record-kinds.toml`,
  §4 "The kind rows", `home` the two `refs/gov/` namespaces; the `routing` row gains `release.route` as
  a writer (`layer-memory.md:427`). Observed by AC14.
- **S16** — The keys: the catalogue rows of `deploy.runs`, `deploy.promotion`, `deploy.on-verify-fail`
  and `release.environments` (`tools/policy/catalogue.toml:1016`, `:1022`, `:1028`, `:1101`) gain
  `summary` and `usage`, allowed values and defaults verbatim, and `python tools/policy/policy.py lists
  --write` drains the four names from `tools/policy/unsummarised-keys.txt`. Each is read by the literal
  call this section names. Observed by AC15.
- **S17** — The docs: `tools/integrations/README.md`, the adapter author's unit (the header, the
  dead-probe rule, a secret is named and never written) and `help/release.md` with a row in
  `help/README.md`, stating what a release does, each key and how to list an environment. NOT OBSERVED
  by a criterion: prose, read by the memory hygiene leg at the close.

**Build-run preconditions**: `core.py new kit` (DEPL-dShippedRelease-10), `--lease`
(TOOL-dPlacedRequest-1, -16, -18), `write_gov_ref` (-11), `points.toml` and the grant check
(TOOL-dWellOiledMachine-20, -17), `point.cadence-items` (-59), `raise_owner_item` (-48), `intake.py`
(-4, -27), `read_items` (TOOL-dDeclaredLoop-12), `record-kinds.toml` (TOOL-dTotalRecall-1),
`layers.toml` (PLAY-dOrderedCharter-16), and this build's `read_landing`, `read_core_verdict`, `gov-deployer`.

## 3. Non-goals (OUT)

- A real engine: DEPL-dShippedRelease-6, with `check_engine_runs`, the static cross-key check. This
  unit's fixture ships a stub engine only.
- The wait on an exit record and the hold: DEPL-dShippedRelease-5, which reads `release-exit`.
- A release retry's draw on the rework budget: DEPL-dShippedRelease-30.
- Publications, a `release` record for `artifact:<url>`: DEPL-dShippedRelease-27, through this unit's writer.
- The re-home of `verdict:remote-ci`, `host:cloud-routine` and notification channels into this kit:
  no clause of the 31 carries them.
- Adapter kinds beyond `deploy-engine`, `verify` and `release-runner`, each its own unit's
  (DEPL-dShippedRelease-19, -22).
- A cadence-items row per environment: `release/<E>` is no such row (pin C11, scout C disagreement 6).

### Edges

- **consumes-from** `DEPL-dShippedRelease-23` — `gov-deployer`, the actor of `release.verify`'s judgment, whose `verify` return `release.py judge` takes
- **consumes-from** `DEPL-dShippedRelease-1` — `read_landing`, the landed SHAs `release.pick` walks
- **consumes-from** `DEPL-dShippedRelease-13` — `read_core_verdict`, the green `release.pick` requires
- **hands-off** `DEPL-dShippedRelease-6` — `check_adapter_header`, which grades its row, and `promote`, the engine verbs it implements and `run_engine_verb` calls
- **hands-off** `DEPL-dShippedRelease-19` — `check_adapter_header`, which grades an import's row
- **hands-off** `DEPL-dShippedRelease-22` — `check_adapter_header`, which grades the mirror's row
- **hands-off** `DEPL-dShippedRelease-5` — `release-exit`, the record that wakes its wait
- **hands-off** `DEPL-dShippedRelease-8` — `tools/integrations/kit.toml`, the kit that unit's files, rows and legs join
- **hands-off** `DEPL-dShippedRelease-30` — `run_release_promote`, the retry site that draws `release-retry`
- **hands-off** `DEPL-dShippedRelease-27` — `record-kind.release`, the kind and `write_release`, the writer a publication uses
- **consumes-from** external — the parent units §2 lists, each specced and unbuilt at this base

## 4. Design

### Evidence

Read at `5d1c82ac`; no product file differs from base `f4597719`.

- `CLAIM_NS` (`tools/unattended/unattended.sh:2087`) and the claim's compare-and-swap push (`:2423`) are
  today's lease shapes; the `--lease` verb is TOOL-dPlacedRequest-1's. `read_held_reds` (`:10113`) reads
  anonymously, keys by SHA, bounds its read and never reads a dead probe as green.
- `read_catalogue_row` (`tools/policy/policy.py:219-241`) refuses a key with no row, and a `<word>`
  segment matches one segment, as `roles.effort.<role>` does (`tools/policy/catalogue.toml:296`).
- `check_value` (`tools/policy/policy.py:143`) has a `name` and a `pattern` type, so a free token is
  admitted by a regex and a table row is not needed.
- `release.environments`' `item` regex (`catalogue.toml:1102`) admits `a..b` and `x.lock`, illegal ref
  segments.
- The rows at `:1016`, `:1022`, `:1028` and `:1101` carry no `summary` or `usage`, and each name is on
  `tools/policy/unsummarised-keys.txt` (`:44-46`, `:167`).

### The rows

```toml
# tools/policy/catalogue.toml — new pattern rows, one fact each, no adopter's value
[[key]]
name = "release.env.<environment>.engine"
allowed = { type = "name", item = "[a-z0-9][a-z0-9-]*" }
default = ""
owner = "dShippedRelease"
summary = "The deploy-engine adapter that promotes into this environment."
usage = 'release.env.staging.engine = "compose-systemd"'

[[key]]
name = "release.env.<environment>.verify"   # the same shape: the verify adapter that judges it
[[key]]
name = "release.env.<environment>.production"
allowed = ["true", "false"]                 # read by owner-approves-prod
default = "false"
```

Filled summaries of S16:

| Key | `summary` | `usage` |
|---|---|---|
| `deploy.runs` | Where a release's actors run: the landing node, the adopter's CI, or the operator by hand. | `deploy.runs = "landing-node"` |
| `deploy.promotion` | Who approves promoting a SHA into an environment. | `deploy.promotion = "auto-on-green"` |
| `deploy.on-verify-fail` | What a failed verify does: roll back and ask, halt and alert, or roll forward. | `deploy.on-verify-fail = "roll-forward"` |
| `release.environments` | The environments a landed SHA is promoted through, in order; empty runs no release. | `release.environments = ["staging", "production"]` |

### The records

```
refs/gov/release/<sha>/<environment segment>     gov-release <sha>/<environment>
  sha · environment · outcome · deployment-id · prior-id · engine · epoch · promotion · route · witness
refs/gov/release-exit/<sha>                      gov-release-exit <sha>
  sha · outcome · environment · release-id
```

`outcome` is one of `verified`, `held`, `rolled-forward`, `rolled-back`, `halted` and `unverified`,
`layer-expansions.md:328`'s six. `derive_release_ref(sha, environment)` spells the segment: a legal
ref segment stands as itself, and any other, `artifact:<url>` among them, becomes `env-` and the first
12 hex of its SHA-256, the `environment` key carrying the name. So DEPL-dShippedRelease-27 needs no
second home.

### The kind rows

```toml
[[record-kind]]
name = "release"
tag = "record.release"
layer = "layer.integrations"
home = "refs/gov/release/*"
id-rule = "<sha>/<environment segment>"
schema = { form = "header", source = "tools/integrations/release.py:RELEASE_FIELDS", fields = [
  "sha", "environment", "outcome", "deployment-id", "prior-id", "engine", "epoch", "promotion", "route", "witness"] }
writer = "release.py record"
readers = ["release.py read"]
lifecycle = "append-only"
check = "integrations release"
```

`release-exit` is the same shape, `home = "refs/gov/release-exit/*"`, `id-rule = "<sha>"`, its four keys
from `RELEASE_EXIT_FIELDS`.

### The items

| Item | `outcomes` | Routes |
|---|---|---|
| `item.release.pick` | `skip`, `nothing`, `owed`, `none-owed` | `owed` to approve-owner, `none-owed` to approve-auto |
| `item.release.approve-owner` | `approved`, `refused` | promote; record |
| `item.release.approve-auto` | `pass` | promote |
| `item.release.promote` | `promoted`, `dropped`, `unverified` | verify; ends; record |
| `item.release.verify` | `green`, `red`, `unverified` | record; route; record |
| `item.release.route` | `rolled-forward`, `rolled-back`, `halted` | record |
| `item.release.record` | `next`, `exit` | pick for the next environment; ends |

The pick file is a node-local convenience, never authority. A second node has none, reads the lease
as foreign, takes it over when stale, and picks again under a new epoch, reading a new id.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_adapter_header`, `read_environments`, `check_environment_name`, `run_engine_verb`, `run_release_pick`, `run_release_promote`, `run_release_verify`, `run_release_route`, `run_release_record`, `run_release_tick`, `run_release_slot`, `write_release`, `read_release`, `write_release_exit`, `derive_release_ref` | functions, `adapters.py`, `release.py`, `deploy_items.py` | `py.function`, each OK by `--suggest` at `5d1c82ac` |
| `ADAPTER_KINDS`, `RELEASE_FIELDS`, `RELEASE_EXIT_FIELDS` | module constants | `py.constant`, screaming |
| `refs/gov/release/`, `refs/gov/release-exit/` | ref namespaces | none |
| `release-approval`, `release-retry`, `release-operator`, `release-halted` | `OWNER_ITEM_KINDS` members | none |
| `integrations adapters`, `integrations release` | legs | none |

### Migration

None: no project lists an environment.

### Rollout

Dark: `release.environments` defaults empty, so `tick` prints `release — no environments` and exits 0.
`build.closes: after-release-verifies` with it empty is refused by KICK-dKeptSession-1's `[[selects]]` row.

### Files touched (estimate)

- `tools/integrations/kit.toml` (new), `tools/integrations/adapters.py` (new), `tools/integrations/release.py` (new), `tools/integrations/release_fixture.py` (new), `tools/integrations/README.md` (new)
- `tools/govkit/registry.toml`: the kit's entry, written by `core.py new kit`
- `tools/runtime/points.toml`: S3, S13, S14
- `tools/runtime/owner_items.py`: the four members
- `tools/loop/loop.toml`: S14
- `tools/loop/deploy_items.py`: `run_release_slot`
- `tools/playbook/layers.toml`: S3
- `tools/policy/catalogue.toml` and `tools/policy/unsummarised-keys.txt`: S4, S16
- `tools/memory-tree/record-kinds.toml`: S15
- `tools/memory-tree/HYGIENE.template.md`, rendered to `memory/HYGIENE.md`: the generated region
- `tools/gate-legs.json`: rendered from the kit's two `[[gate_leg]]` rows
- `help/release.md` (new), `help/README.md`: S17

### Alternatives rejected

- **`run_cadence_period` for `release/<E>`.** Rejected by pin C11: `derive_period` cannot produce an
  environment, and a `landed` status reads "already witnessed, run nothing", so a second SHA into E would
  run nothing. Test: TOOL-dWellOiledMachine-13 S6 (scout C disagreement 6).
- **Environment rows in `tools/runtime/points.toml`.** Rejected by pin C11: update overwrites the file
  and a shipped file names no adopter. Test: arm 10, `tools/govkit/govkit.py:3731`.
- **A new `.governance/environments.toml`.** Rejected: a new install location, veto 2, for values a
  pattern row already admits. Test: `read_catalogue_row`'s wildcard match.
- **A tracked `release` record.** Rejected as DEPL-dShippedRelease-1 rejected one: a post-landing
  commit per promotion, each needing a landing, and a program that outlives the build has no lease to
  land under. Test: `unattended.sh:6354-6357`.
- **An eighth item for the role's judgment.** Rejected: v2 lists seven and the packet owns seven. Test:
  `layer-expansions.md:385-393`.

## 5. Production-readiness checklist

- security — deny by default: an empty list runs nothing, a key with no row refuses, an engine with no
  `cas` refuses, and a name illegal as a ref segment refuses at the read. Every adapter runs in its own
  process, a secret by reference resolved into that process alone (TOOL-dWellOiledMachine-17 S4), and
  no record holds a secret: `witness` is a hash of the verify's output, whose file stays node-local.
  This unit adds an outbound surface, each engine's, priced by its Tier-2 review and its `grant`.
- perf / scale — one bounded remote read per environment per tick; a daily row and one slot run per
  green landing.
- error / empty / loading states — nothing to pick, held elsewhere, compare-and-swap refused, dead
  probe and halted each print their own line, and only `verified` goes on.
- observability — one `release — <E> · <what>` line per step; each outcome is on a record a second node reads.
- risks — a daily catch-up leaves a SHA unpromoted for up to a day where its node died. A held-open
  approval holds E's lease, so a later SHA waits: the lease ages to `stale` and the next tick re-picks.
- testing — `release_fixture.py` with a file-backed stub engine and a bare remote.
- migration — none.
- user docs — `help/release.md`, `tools/integrations/README.md`.

## 6. Acceptance criteria

- **AC1** — When `python core.py new kit integrations --layer layer.integrations` has run at the pass, the
  kit's descriptor is tracked and the kit conformance gate of DEPL-dShippedRelease-10 grades it, exit 0.
  Red when: the kit fails the factory's own gate.
- **AC2** — When `python adapters.py --check` runs over a fixture with a row missing each of `kind`,
  `grant`, `witness-source`, `probe` and `fallback`, and a `deploy-engine` row with no `cas`, it exits 1
  naming each; `python adapters.py new` refuses the same rows and writes a conforming one.
  Red when: a row with no probe registers.
- **AC3** — When `python release_fixture.py --case slot` runs `run_release_slot` with one `release-runner`
  row it prints `1 runner(s)` and the stub runs; with none it prints `0 runner(s)`; and `grep -c
  "import.*integrations" deploy_items.py` prints 0.
  Red when: the core depends on this expansion.
- **AC4** — When `python release_fixture.py --case environments` plants `.governance/policy.toml` with
  `release.environments = ["a..b"]`, the tick refuses naming the name; `["staging"]` with no
  `release.env.staging.engine` refuses naming the key; `[]` prints `no environments`.
  Red when: an illegal segment reaches `--lease`, or an empty list runs anything.
- **AC5** — When `python release_fixture.py --case stale-rollback` lets a holder pick on one clone, takes
  the lease over on the other after the planted age, promotes there, and then runs the stale holder's
  `rollback <E> <sha> --expect <old id>`, the engine exits 3, its state is unchanged, the holder prints
  `dropped · compare-and-swap refused`, and no release record names that rollback; `--expect` read at the
  new pick succeeds.
  Red when: the stale rollback changes the deployment, the clause's seen-red case.
- **AC6** — When `python release_fixture.py --case pick` plants three landed SHAs, the newest with no
  green verdict, it picks the middle one; a second environment picks only a SHA verified in the first;
  a lease held live elsewhere prints `skip · held elsewhere`; none left prints `nothing`.
  Red when: a SHA with no green core verdict is picked.
- **AC7** — When `python release_fixture.py --case approvals` plants each of `deploy.promotion` values
  `auto-on-green`, `owner-approves-prod` and `owner-approves-each` over one environment marked production
  and one not, `auto-on-green` raises no item, `owner-approves-prod` raises one, `owner-approves-each`
  raises two; a refusal writes outcome `held`.
  Red when: a production promote passes under `owner-approves-prod` with no answer.
- **AC8** — When `python release_fixture.py --case no-cas` plants an engine row `cas = "none"`, `deploy.runs`
  `landing-node` refuses naming the gap with the engine untouched, and `.governance/policy.toml` planted
  `deploy.runs = "operator"` raises `release-operator` and goes on after a `read-back`.
  Red when: an engine that cannot compare-and-swap runs off the operator.
- **AC9** — When `python release_fixture.py --case verify` plants a verify adapter exiting 0, 1, 3 and 127,
  each routes as S9 says, and `python release.py judge <E> <sha> real-failure` routes a held judgment as red.
  Red when: a dead probe reads as green, or a judged failure is lost.
- **AC10** — When `python release_fixture.py --case on-fail` plants each of `deploy.on-verify-fail` values
  `roll-forward`, `rollback-and-ask` and `halt-and-alert`, the outcomes read `rolled-forward`, `rolled-back`
  with the last verified SHA restored, and `halted` with one `release-halted` item and a later tick
  refusing E; each files one intake, and re-running files none.
  Red when: a rollback passes no compare-and-swap, or a value routes as another.
- **AC11** — When `python release_fixture.py --case record` passes two environments, one `release` ref per
  environment stands, `refs/gov/release-exit/<sha>` reads `verified` naming the second, the lease reads
  `released`, and a re-run writes nothing; `python release.py record <sha> artifact:https://example.invalid/a
  --outcome verified` writes a ref with an `env-` segment.
  Red when: a pass ends with no exit record, or the lease goes terminal.
- **AC12** — When `python release_fixture.py --case runs` plants `deploy.runs = "adopter-ci"`, the node's tick
  prints `adopter-ci` and promotes nothing, `release.py tick --ci` runs the pass, and `--ci` under
  `landing-node` exits 2.
  Red when: both a node and a CI job can promote under one value.
- **AC13** — When `python cadence.py --check` runs at the pass it counts the `release` row; `python
  release_fixture.py --case wake` runs the tick for a build whose lease is a tombstone and the pass completes.
  Red when: the program needs the build's lease, so it cannot outlive an `at-landing` close.
- **AC14** — When `python loop_lib.py --check` and `python record_kinds.py --check` run at the pass, each
  exits 0 with seven `item.release.` rows and the two kinds.
  Red when: a row fails the program check, or a kind's fields differ from its literal.
- **AC15** — When `git grep -cE 'read_policy_value\("(deploy\.runs|deploy\.promotion|deploy\.on-verify-fail|release\.environments)"'`
  runs over `release.py` at the pass it prints at least 4, and `grep -cE '^(deploy\.runs|deploy\.promotion|deploy\.on-verify-fail|release\.environments)$' tools/policy/unsummarised-keys.txt` prints 0.
  Red when: an owned key has no literal reader, or its name stays on the list.

## 7. Gates

`memory hygiene` · `kit/dogfood doc parity` · `policy check` · `policy fixtures` · `unattended kit gate` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `kit version markers` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest`

New arm: tools/integrations/release_fixture.py · covers AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 AC11 AC12 AC13 · each `--case` above with a file-backed stub engine, the failing case `stale-rollback` staged by a stub that ignores `--expect` · none

New arm: tools/integrations/adapters.py · covers AC2 · `--check` over the planted rows, the failing case a row with no `probe` · none

## 8. Open questions

- **F1 — How does an environment get its values?** `read_catalogue_row` refuses a key with no row and
  `release.environments` is a list of bare names (scout C disagreement 7). Options: (a) pattern rows
  `release.env.<environment>.*`, the `roles.effort.<role>` precedent; (b) rows in `points.toml`; (c) a
  new file. (b) is overwritten at update and (c) is a new install location. RESOLVED (agent, 2026-10-30,
  delegated): (a), rung 3, read with DEPL-dShippedRelease-6 §8 F3's rows for the engine's values.
  widens: none · relaxes: none · grants: PLAY-dClosedLoop-3 the three `release.env.<environment>` rows,
  the `integrations` kit and the ref namespaces `refs/gov/release/` and `refs/gov/release-exit/`
- **F2 — What wakes `release.*` after a close under `at-landing`?** Options: (a) the slot on `deploy.core`
  green, and a daily `point.cadence-items` row for what that misses; (b) the walk alone, which ends with
  the build; (c) a new wake on the `landed` event, which TOOL-dWellOiledMachine-59's tick does not read.
  (b) fails "the program outlives the build" (`layer-expansions.md:382`) and (c) is a parent's non-goal.
  RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, scout C's fork 4. widens: none · relaxes: none
- **F3 — Where do `release` records live?** Options: (a) refs, per (SHA, environment); (b) tracked files.
  (b) needs a landing per promotion. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, I13 and pin
  C2's reasoning. widens: none · relaxes: none
- **F4 — Who owns the kit, given no clause names it?** Options: (a) this unit, its first reader, through
  DEPL-dShippedRelease-10's factory; (b) a new unit. The roster is one unit per clause. RESOLVED (agent,
  2026-10-30, delegated): (a), rung 1, pin C1. widens: none · relaxes: none
- **F5 — How does a command item use `gov-deployer`?** Options: (a) the item stays `command`, holds on an
  undecided verify, and takes the role's return through `release.py judge`; (b) an eighth item with a
  role actor. (b) adds a node the packet does not own. RESOLVED (agent, 2026-10-30, delegated): (a),
  rung 3, DEPL-dShippedRelease-23 S4's `verify` return. widens: none · relaxes: none
- **F6 — How is a failed verify's ask filed once the build has closed?** Options: (a) a `cadence` intake
  keyed by the reading's text, whose receipt never ratifies, so `entry.place` routes it to an ask
  (TOOL-dWellOiledMachine-27 S3, S4); (b) a tracked backlog row, needing a landing; (c) an owner item
  alone. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, the flow's "a failed verify filed as an
  ask" (`2026-10-14-build-PLAY-dClosedLoop-1-flow.md:628`). widens: none · relaxes: none
- **F7 — What does a rollback do with no verified SHA in E?** Options: (a) end `halted` and raise the
  item; (b) roll forward. (b) ignores the key's value. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, from the packet's Items 15, `gap-deploy-01`, `layer-expansions.md:296-423`,
  flow-steps:498-503, pins C1 and C11, shared interfaces I11, I12 and I13, and scout C's row and
  disagreements 1, 6, 7, 8 and 17.

## 10. Reuse audit

The seams are `--lease` (TOOL-dPlacedRequest-1, called directly), `read_held_reds`' shape
(`tools/unattended/unattended.sh:10113`), the `[[adapter]]` row of `tools/runtime/points.toml`
(TOOL-dWellOiledMachine-20), and the factory `core.py new kit` (DEPL-dShippedRelease-10). `python
tools/codebase-map/reuse_lookup.py "promote a sha through environments with a compare-and-swap on the current
deployment id"` returned `resolve_compare_base`, `add_deploy_kits` and id helpers, none a promotion, so no
shipped seam fits beyond those. Scout C's row holds at `5d1c82ac`, with one correction to scout C's
interface table: `cas` values are `native`, `built` and `none`, as DEPL-dShippedRelease-6 S7 spells them.
The recall probe's hits were this build's scout record and the night pass's fold of FK-5-6; neither
disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how does an adopter release through environments with rollback" --terms "release environments deployment promotion rollback compare-and-swap engine adapter verify integrations kit"`
