# DEPL-dShippedRelease-17 — `kits.install` and `kits.update`: the walk that closes on dSafePassage's outcomes, the attended hooks, the backlog step, and a fresh install in one pass

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 22 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0427@e593e6b1 whole
**Carries:** node:item.kits.install
**Carries:** node:item.kits.update
**Carries:** node:item.kits.install-attended
**Carries:** node:item.kits.update-attended

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-17-deviation-171.md](../build/2026-10-30-build-DEPL-dShippedRelease-17-deviation-171.md) | deviation | — |
| [2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md](../build/2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md) | research | DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-18 DEPL-dShippedRelease-20 DEPL-dShippedRelease-25 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-31 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |

<!-- /gen:spec-records -->

## 1. Goal

`gap-deploy-27`: a fresh install of every kit needs manual steps. This unit gives the Distribution
items their commands: `kits.install` and `kits.update` walk and close on one closed set of outcomes,
each seen on a planted walk; the install and update hooks that call `adopt` and `test.seed` are run
attended by the owner items `kits.install-attended` and `kits.update-attended`; the shards-to-builds
backlog migration becomes an update's upgrade step, attended; and a fresh install of every kit runs in
one pass on an empty repository, its adopters ordered by their declared dependencies.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build, each specced and unbuilt at base
`f4597719`: `run_step_walk`, `derive_pending_steps`, the reclaim and the attended order
(TOOL-dSafePassage-2 S1 to S7); `--rollback` (TOOL-dSafePassage-4 S1, S2); `retired-edited` and
`render-edited` (TOOL-dSafePassage-9 S2, S5); the step grammar `[[upgrade]]` (TOOL-dSafePassage-1 S1);
`instructions.stale` (PLAY-dOrderedCharter-35 S8); the harness adapters' targets
(TOOL-dWellOiledMachine-14); `legacy_ledger.py seed` (TOOL-dWitnessedBar-15 S1); `core.py adopt`
(TOOL-dLinkedLibrary-8 S3); `check_terminal_proof` (TOOL-dDeclaredLoop-2 S5).

- **S1** — One closing word. `derive_walk_outcome(run)` in the new `tools/govkit/kit_walk.py` reads a
  finished run's state and returns one of `KIT_WALK_OUTCOMES`, the eight of §4 "The outcomes". `install`
  and `update --write` print `govkit <verb> — outcome: <word>` as their last line, and each word routes
  as the row says. Observed by AC1.
- **S2** — `kits.install`, the new verb `govkit.py install --target <path> [--kits a,b | --all] [--answer
  key=value ...]`: `cmd_intake` when the target holds no `deploy.toml`, then `cmd_apply` with
  `one_pass=True`, one process. Its selection is `read_kit_rows(root, ids)`, install order, less a row
  whose `installable` reads false, so `--all` omits `lib` and `govkit`. `kits.update` is `update --write`,
  extended by S1 and S4. Observed by AC2 and AC5.
- **S3** — The outcome's `then`. `[[outcome]]` gains one optional key, `then`, `continue` or `attended`,
  only on an `ok = true` row, graded by one `selfcheck` arm beside the arms that read outcome rows (a
  `[[field]]` row of `kit-schema.toml` grades top-level keys only). Under
  `one_pass`, a `continue` stop re-runs that adopter once in the same CONFIGURE, through the one
  `run_target_argv` call `_cmd_apply` already makes (`tools/govkit/govkit.py:8089`), since a gov default
  is all it waited for; an `attended` stop joins `configure_skipped` (`:7999`), so its legs read through
  `exempt_leg` (`:6383`) as held, and it adds one line to the install's attended order. Under plain
  `apply` the key is unread and a stop stays a stop. §4 "The stops" names each row. Observed by AC2
  and AC3.
- **S4** — The hooks. `write_hook_orders(target, verb, receipt)`, called when a walk ends with no
  finding, writes one order through `render_attended_order` for each `read_kit_hooks(verb, …)` row
  (DEPL-dShippedRelease-20 S2), the file named for the hook so a later update rewrites it, and one row
  of the receipt's `orders`, `{"kind": "attended", "id": "hook/<name>", "path": …, "state": "open"}`,
  so `check_orders` grades it. `kits.install` and `kits.update` then close `attended`, routing to the
  owner item. Observed by AC4 and AC5.
- **S5** — `kits.install-attended` and `kits.update-attended`, the owner's verb `govkit.py attend --target
  <path> --build <slug> --unit <id>`, `cmd_attend`. It refuses unless `check_terminal_proof` holds and the
  offer's mode is off: attended means an owner in that session. It walks the receipt's `open` rows of
  kind `attended` and `codex-retrust` in order: a hook's argv, a step's `up` (TOOL-dSafePassage-2 S5's
  attended step, `needs-target = true`), each through `run_target_argv`, and on exit 0 sets the row's
  `state` to `applied` (a step through `set_step_state`). A failed row stops the walk: the receipt names
  the last completed row, the rest stay `open`, and one owner item `step-failed` offers `rerun` or
  `rollback`. A re-run skips each `applied` row. Observed by AC6 and AC7.
- **S6** — The backlog step. One `[[upgrade]]` row `memory-tree/backlog-shards-to-builds` in
  `tools/memory-tree/kit.toml`, program `tools/govkit/steps/backlog_shards_to_builds.py`, §4 "The step",
  `needs-target = true`, so TOOL-dSafePassage-7's `derive_step_mode` makes it attended at every update
  until no tree is left on shards (NP-22). Its witness holds when the target's `.memory-tree.conf` reads
  `BACKLOG_MODE="builds"`, so a tree already moved never sees an order. Observed by AC8.
- **S7** — The order of adopters. `tools/agent-instructions/kit.toml` gains `requires =
  ["playbook-render"]`, the edge `gap-deploy-27` names, so the charter's render precedes its alias
  wiring. Observed by AC2.
- **S8** — The seed `memory/` tolerated. `tools/memory-tree/adopt-memory-tree.sh:505-509` refuses a
  `memory/` with no marker, and the kickoff seed makes one at LAND, before any adopter (scout D
  disagreement 5). The refusal keeps its reason and its branch for a foreign tree, and falls through to
  scaffold when every file under `$M` is a `seed` row of the receipt, `check_seed_only`, which reads
  `.governance/install.json`. Observed by AC3.
- **S9** — The rows: four `[[item]]` rows in `tools/loop/loop.toml`, §4 "The items"; `[[command]]` rows
  `kits.install` and `kits.update` in `tools/govkit/kit.toml` by `new command`; `step-failed` in
  `OWNER_ITEM_KINDS`. Observed by AC9.
- **S10** — The docs. A new page `help/install.md`, linked from `help/README.md`: the install verb, what
  one pass means, each stop and its order, `attend`, and what each outcome word asks. `WIRE-INTO-PROJECT.md`
  points at it; `help/upgrade-steps.md` names the backlog step. Observed by AC10.

## 3. Non-goals (OUT)

- The walk's own moves, the reverse walk, gov first and every refusal they make: TOOL-dSafePassage-2, -4
  and -8. This unit reads their result and names it.
- `kits.offer`: DEPL-dShippedRelease-16. `cmd_attend` refuses under its mode.
- `adopt declarations`: DEPL-dShippedRelease-28. `update`'s report: DEPL-dShippedRelease-29.
- Giving an adopter's conf values gov cannot know: `PROCMON_ROOTS`, a CI file, a project layer. §8 F1.
- Rewriting `migrate_backlog.py`. The step wraps its verbs.
- The runbook: DEPL-dShippedRelease-9 renders from what this unit declares.

### Edges

- **consumes-from** `DEPL-dShippedRelease-10` — `read_kit_rows`, the install order S2 walks
- **consumes-from** `DEPL-dShippedRelease-21` — `installable`, which S2 reads to leave `lib` and `govkit` out of `--all`
- **consumes-from** `DEPL-dShippedRelease-20` — `render_attended_order`, the one order writer, and `KIT_HOOKS`, the rows S4 walks
- **consumes-from** `DEPL-dShippedRelease-27` — `codex-retrust`, the `orders` row S5's walk runs beside the hooks
- **hands-off** `DEPL-dShippedRelease-28` — `kits.update`, whose hook calls `adopt declarations` through S4's row
- **hands-off** `DEPL-dShippedRelease-29` — `kits.update`, whose run prints the report that unit extends
- **consumes-from** external — TOOL-dSafePassage-1, -2, -4, -7 and -9, PLAY-dOrderedCharter-35, TOOL-dWellOiledMachine-14 and -48, TOOL-dWitnessedBar-15, TOOL-dLinkedLibrary-8 and TOOL-dDeclaredLoop-2, each specced and unbuilt at base `f4597719`

## 4. Design

### Evidence

Read at `5d1c82ac0`; no product file differs from base `f4597719`. The empty-repository readings are
scout D's, on two scratch repositories at `f4597719e`, its `apply.out` and `apply2.out`, read again here.

- `derive_install_order` (`tools/govkit/govkit.py:911`) orders by `requires`; its edges are too few and
  no order closes the gap: `memory/` comes from the kickoff seed at LAND, before CONFIGURE.
- Under `playbook_path=docs/charter.template.md` `agent-instructions` exits 2 before the charter exists;
  under `playbook_path=AGENTS.md` it exits 0 and `playbook-render` refuses, template and charter being
  one file. Either way the run ends `govkit: 34 problem(s)` or `36`, PINNED at those runs.
- `process-monitor` exits 1, unclassified, on blank `PROCMON_ROOTS` (`tools/process-monitor/adopt-process-monitor.sh:120`);
  `playbook-render` exits 1, unclassified; `unattended` exits 1, `no-project-layer`, not `ok`
  (`tools/unattended/kit.toml:203-205`); `roles` exits 3, `no-governing-doc`, `ok`
  (`tools/roles/kit.toml:88-92`); `memory-tree` exits 1, `seed-and-stop`, `ok`
  (`tools/memory-tree/kit.toml:141-149`); `codebase-map` is skipped on the hole `map-extractors`.
- A rendered row of a kit `stopped_ok` is reported and not failed (`:8150-8158`); `exempt_leg` excuses a
  red leg only with `red_after_land` and the kit in `configure_skipped` (`:6450`).
- `tools/memory-tree/migrate_backlog.py` carries `--plan`, `--write --as <slug> --signed`, and its
  exit 1 means a human must answer; `.memory-tree.conf:734` holds `BACKLOG_MODE="builds"`.

### The outcomes

| Word | Read from | Route |
|---|---|---|
| `applied` | every step applied, no hook owed | end |
| `attended` | a step stopped `attended`, or an order of S4 is open | `kits.install-attended` or `kits.update-attended` |
| `step-failed` | a step recorded `failed`, the receipt naming step k-1 | one owner item, `rerun` or `rollback` |
| `lock-reclaimed` | the walk re-ran after a dead holder's lock (TOOL-dSafePassage-2 S7) | the word of the re-run, with this printed |
| `downgrade-refused` | `--to` not forward and no recorded rollback (TOOL-dSafePassage-4 S2) | end, exit 2 |
| `held-edits` | a `retired-edited` row or `render-edited` row held; under `install.retired-edits: keep`, reported | end |
| `stale-edge` | `instructions.stale: refuse` held the update, with an ask | end |
| `no-target` | an adapter of `runtime.harnesses` declares no target: nothing installed for it, the core render kept | end |

The set is closed: a run reading none of them is a refusal naming the state, never a default word.

### The stops

| Kit | Exit, today's reading | Row after this unit |
|---|---|---|
| `memory-tree` | 1, `seed-and-stop`, `ok` | `then = "continue"`; the re-run scaffolds through S8 |
| `codebase-map` | 1, `seeded-conf`, `ok`, or the hole `map-extractors` | `then = "continue"` on the outcome; the hole stays a declared skip |
| `roles` | 3, `no-governing-doc`, `ok` | `then = "attended"` |
| `process-monitor` | 1, unclassified | a new row: `code = 1`, `must_exist = ".process-monitor.conf"`, `means = "no-roots"`, `ok = true`, `then = "attended"` |
| `playbook-render` | 1, unclassified | a new row `means = "no-ci-file"`, `ok = true`, `then = "attended"`, its probe the template's presence |
| `agent-instructions` | 2, before the charter | a new row `means = "no-charter"`, `must_not_exist = "AGENTS.md"`, `ok = true`, `then = "attended"` |
| `unattended` | 1, `no-project-layer` | gains `ok = true`, `then = "attended"` |

`continue` is for a stop that only waited for a value gov already defaults. `attended` is for a value
only the owner holds. A `continue` is taken once; a second stop on the re-run is the outcome's own.

### The hooks at the close

`install` owes `test.seed` then `adopt census`; `update` owes `test.seed` then `adopt declarations`. The
order names `<slug>` and `<id>`; `attend` fills them from its flags. `adopt.census` runs once in a
repository, so an install's row is the only one naming it. `test.seed` seeds only an absent population
and is safe to repeat.

### The step

```toml
# tools/memory-tree/kit.toml
[[upgrade]]
id = "memory-tree/backlog-shards-to-builds"
up = ["python", "{gov}/govkit/steps/backlog_shards_to_builds.py", "up", "{target}", "{prefix}"]
down = ["python", "{gov}/govkit/steps/backlog_shards_to_builds.py", "down", "{target}", "{prefix}"]
witness = ["python", "{gov}/govkit/steps/backlog_shards_to_builds.py", "witness", "{target}", "{prefix}"]
surfaces = ["conf-key:.memory-tree.conf#BACKLOG_MODE"]
needs-target = true
```

`up` prints the recipe and exits non-zero: the owner's run is `python <prefix>/memory-tree/migrate_backlog.py
--plan --record <dir>`, then its `--write --as <slug> --signed same-id=<path> --signed triage=<path>`, both
naming signed answers no process can supply. `down` exits 1 naming `git revert` of the switch-over, since
the migration's rows have no before-image.

### The items

```toml
[[item]]
tag = "item.kits.update"
program = "kits"
actor = "command:kits.update"
needs = []
inputs = ["layer.distribution:the receipt and the release"]
allowance = "the target's kit files, its receipt and its outbox"
returns = "record-kind.receipt"
outcomes = ["applied", "attended", "step-failed", "downgrade-refused", "held-edits", "stale-edge", "no-target"]
witness = { class = "history", by = "the receipt and the wiring verdict" }
owner = "dShippedRelease"
[item.routes]
applied = "end"
attended = "item.kits.update-attended"
step-failed = "end"
downgrade-refused = "end"
held-edits = "end"
stale-edge = "end"
no-target = "end"
```

`item.kits.install` is the same with `item.kits.install-attended`. Each attended row is `actor =
"owner"`, `needs` its command, `outcomes = ["applied", "failed"]`, `applied` back to its command, whose
walk resumes past it, `failed` to `end`, the witness "the receipt, each attended step recorded applied".
`lock-reclaimed` is no outcome of a row: the run goes on and closes on another word.

### Inventory

Minted: `tools/govkit/kit_walk.py` with `KIT_WALK_OUTCOMES`, `derive_walk_outcome`, `write_hook_orders`,
its verbs `--fixture`, `--plant`, `--stub`; in `tools/govkit/govkit.py` `cmd_attend` and the verbs
`install`, `attend`; `check_seed_only` in `adopt-memory-tree.sh`; the `[[outcome]]` key `then` with
`continue` and `attended`; the `means` words `no-roots`, `no-ci-file`, `no-charter`; the step
`memory-tree/backlog-shards-to-builds`; the owner-item kind `step-failed`. Naming cells: `py.function`
OK by `python tools/lexicon/lexicon.py --suggest <name> --as py.function` at `5d1c82ac`
(`classify_walk_outcome` was asked first and refused); `sh.function` at the pass.

### Migration

Additive for an installed target: `then` is read only by `install`, and `agent-instructions`' new
`requires` binds a new `apply` and no `update`. An `update` writes the hook orders from its first run.

### Rollout

No switch: `install` is a new verb, and `apply` keeps its stops, so every existing arm reads the same.

### Files touched (estimate)

- `tools/govkit/kit_walk.py` (new): S1, S4
- `tools/govkit/govkit.py`: S2, S3, S5, `parse_args` and USAGE
- `tools/govkit/selftest.py`: the `run_target_argv` count arm at `:16493` moves to four
- `tools/govkit/steps/backlog_shards_to_builds.py` (new): S6
- `tools/memory-tree/kit.toml`, `tools/memory-tree/adopt-memory-tree.sh`: S3, S6, S8
- `tools/agent-instructions/kit.toml`, `tools/process-monitor/kit.toml`, `tools/playbook/kit.toml`,
  `tools/unattended/kit.toml`, `tools/codebase-map/kit.toml`, `tools/roles/kit.toml`: S3, S7
- `tools/govkit/kit.toml`, `tools/loop/loop.toml`, `tools/runtime/owner_items.py`: S9
- `WIRE-INTO-PROJECT.md`, `help/install.md` (new), `help/README.md`, `help/upgrade-steps.md`: S10

### Alternatives rejected

- **Reordering alone.** Scout D measured two empty repositories: `memory/` is made at LAND, and five
  adopters stop for reasons no order changes.
- **A second `apply --resume` documented as the second pass.** Rejected by `gap-deploy-27`, whose words
  are "needs manual steps"; a documented second run is one.
- **Hooks run inside `update`.** `update` then runs `adopt` in every operator's run, and `kits.offer`
  must refuse it, against the clause's "attended".
- **A new receipt list for hooks.** `orders` already holds kinds and `check` already reads it.

## 5. Production-readiness checklist

- security — `attend` runs gov's argv templates at the target's prefix in the owner's session, each
  value through `demand_safe_token`; a terminal proof bars an agent or the offer from it.
- perf / scale — `install --all` is one `apply`, a minute or more; `attend` is one pass over a few rows.
- error / empty / loading states — every stop is declared; an unclassified adopter exit stays a
  problem; a run with no word refuses.
- observability — the closing `outcome:` line, one `CONFIGURE` line per adopter, one order per hook.
- risks — a seeded conf that `continue` renders from defaults is what a person used to review first; the
  closing line names `.memory-tree.conf` as seeded so it is read. `agent-instructions` selected alone
  now needs `playbook-render`.
- testing — the arms of §7, each a scratch gov and target.
- migration — §4 "Migration", and S6's attended step.
- user docs — `help/install.md`, `help/upgrade-steps.md`, `WIRE-INTO-PROJECT.md`.

## 6. Acceptance criteria

- **AC1** — When `python kit_walk.py --fixture --plant outcome-<word>` runs for each of `applied`,
  `attended`, `step-failed`, `lock-reclaimed`, `downgrade-refused`, `held-edits`, `stale-edge` and
  `no-target` over a scratch walk staging that case, the run's last line reads that word, and under
  `step-failed` the receipt names step k-1 and one stubbed `step-failed` item is posted.
  Red when: a planted case closes on another word, or `--plant outcome-unknown` reads a default word.
- **AC2** — When `python kit_walk.py --fixture --plant empty-repo` runs `install --all` over `git init` in a
  scratch directory with `playbook_path` answered under `docs`, it exits 0 in one process,
  no line reads `unclassified`, `playbook-render` precedes `agent-instructions` in the `CONFIGURE` lines,
  `lib` and `govkit` are absent, and the last line reads `outcome: attended`.
  Red when: the run ends with a problem count, or a kit stops with no declared row.
  cost: an `install --all`, a minute or more on a Windows node.
- **AC3** — When the same plant's tree is read after the run, `memory/HYGIENE.md` carries the `gov:kit
  memory-tree@` marker and the install's attended order names `process-monitor`, `playbook-render`,
  `agent-instructions` and `unattended`, each with the value it waits for; and `--plant
  foreign-memory` over a `memory/` holding a file no receipt row names still exits at the refusal.
  Red when: the seed `memory/` is refused, or the foreign tree is overwritten.
- **AC4** — When `--plant hooks-install` and `hooks-update` run, the outbox holds one attended order per
  hook naming its exact command, the receipt's `orders` holds a row per hook with `state` `open`, and a
  second update rewrites those rows and adds none; `python tools/run-gates/check-receipt.py <tree>` counts
  them `open`.
  Red when: a hook has no order, or orders pile up.
- **AC5** — When `--plant no-hooks-run` plants canaries in the target's `core.py` and `legacy_ledger.py`
  and runs `install`, then `update --write`, neither canary exists.
  Red when: `adopt` or `test.seed` runs outside the attended verb, the clause's "attended".
- **AC6** — When `--plant attend-all` runs `attend --build fx --unit fx-1` with `--stub terminal` over a
  target with the two hook orders and a `codex-retrust` row, each canary fires once, each row reads
  `applied`, and a second run spawns nothing; without `--stub terminal`, `attend` exits 2 naming the proof.
  Red when: a non-terminal caller runs it, or an `applied` row runs twice.
- **AC7** — When `--plant attend-fails` makes the second row exit 1, the first row stays `applied`, the
  rest stay `open`, and one stubbed `step-failed` item is posted; a re-run after the fix starts at the
  second row.
  Red when: a failure marks a later row, or the walk restarts from the top.
- **AC8** — When `--plant backlog-step` runs `update --write` over a target whose `.memory-tree.conf`
  reads `BACKLOG_MODE="shards"`, the walk stops `attended` with an order naming `migrate_backlog.py
  --plan` and its `--write` form; over one reading `builds`, the step reads `applied` and no order exists.
  Red when: the step runs with no owner, or a moved tree meets an order.
- **AC9** — When `python loop_lib.py --check` runs, it passes with the four `item.kits.*` rows of this
  unit, each route resolved.
  Red when: an outcome has no route.
- **AC10** — When `grep -c attend install.md` and `grep -c backlog-shards-to-builds upgrade-steps.md` run
  from the `help` directory, each prints at least `1`.
  Red when: a stop or the step is undocumented.

## 7. Gates

`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `policy fixtures` · `agent-instructions self-test` · `codebase-map adopter e2e` · `codebase-map gate coverage` · `codebase-map kit selftest` · `playbook render selftest` · `memory hygiene`

New arm: tools/govkit/kit_walk.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · `--selftest` over every plant, its failing case a planted walk closing on a default word · none
New arm: tools/govkit/selftest.py · covers AC1 · `KIT_WALK_OUTCOMES` compared with the routes of `item.kits.update`, staged by a word with no route · none

## 8. Open questions

- **F1 — What "one pass" means on an empty repository** (scout D fork 6). A strict reading has every
  adopter finish, and `PROCMON_ROOTS`, a CI file and a project layer are values only the owner holds:
  an empty repository has none and gov has no default for them. Options: (a) order alone, measured not
  to close the gap, failing the clause; (b) one process, every kit ending at a declared outcome, a stop
  waiting only on a gov default continued in the run, a stop waiting on an owner's value listed on one
  attended order; (c) invent defaults for those values, which reports a clean tree over a fence that
  matches nothing, the refusal `tools/process-monitor/adopt-process-monitor.sh:121` names. Each option
  fails a bound: (a) and (b) the clause's "every kit", (c) a kit's own deny-by-default. RESOLVED (agent,
  2026-10-30, delegated): (b), rung 6, ER:328, the most capable after relaxing the clause's reading, the bound relaxed the one no
  value could satisfy. widens: none · relaxes: every kit's adopter finishing with no owner's value on an empty repository
- **F2 — Is `then` a key or a new outcome kind?** Options: (a) one optional key on `[[outcome]]`; (b) a
  second table. (a) keeps `classify_outcome` (`tools/govkit/govkit.py:6557`) as the one reader. RESOLVED
  (agent, 2026-10-30, delegated): (a), rung 3. grants: PLAY-dClosedLoop-3 the `[[outcome]]` key `then`.
  widens: none · relaxes: none
- **F3 — Are hooks steps?** Options: (a) `orders` rows of kind `attended`; (b) `[[upgrade]]` rows. A step
  runs once ever by id; a hook recurs at every update. RESOLVED (agent, 2026-10-30, delegated): (a), rung
  3. widens: none · relaxes: none
- **F4 — A verb or a flag for the install?** Options: (a) a verb `install`; (b) `apply --one-pass`. The
  clause names commands, and `intake` then `apply` is the two-step this closes. RESOLVED (agent,
  2026-10-30, delegated): (a), rung 3. grants: PLAY-dClosedLoop-3 the verbs `install` and `attend`.
  widens: none · relaxes: none
- **F5 — How a migration row ends.** "Until no tree is left on shards" names no owner of the check.
  Gov's `adopters` record reads each receipt and no conf, so a count needs a new read. RESOLVED (agent,
  2026-10-30, delegated): the row stays attended, and its retirement is a later unit's by the step
  grammar's `[[retired]]` row, rung 3; nothing here reads a count. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, from the packet's Items 17, layer-expansions:461-462, `gap-deploy-27`,
  scout D's unit 17 row, its disagreement 5 and fork 6, its scratch evidence, and the brief's I18.

## 10. Reuse audit

The seams extended are `derive_install_order` (`tools/govkit/govkit.py:911`) through `read_kit_rows`,
`resolve_selection` (`:1062`, scout D's `:1098` is the `all` arm), `classify_outcome` (`:6557`) and the
`[[outcome]]` table, `configure_skipped` (`:7999`) with `exempt_leg` (`:6383`), the receipt's `orders`,
`_cmd_update` (`:9154`), TOOL-dSafePassage-2's walk and `tools/memory-tree/migrate_backlog.py`. `python
tools/codebase-map/reuse_lookup.py "fresh install of every kit in dependency order on an empty
repository"` ranked `resolve_kit_dir`, `default_kits` and `derive_install_order`, the last the seam; it
found no walk, which agrees with scout D. Where the two disagreed: the gap says ordering closes it and
scout D's measurement says it cannot, and §8 F1 follows the measurement. Recall surfaced
TOOL-dGroundRules-16, which grades the policy leg on a fresh target, and the adopter-instructions
record's row on existing harness files, TOOL-dLinkedLibrary-23's.

Recall terms used: `python tools/memory-recall/query.py "fresh install on an empty repository needs manual steps which adopter stops" --terms "fresh install empty repository derive_install_order requires adopter outcome memory-tree seed intake apply"`
