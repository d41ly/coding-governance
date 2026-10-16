# Layer review: the expansion layers, observability, integrations and distribution

The core's five layers are designed, reviewed and folded. This round designs the three expansions that
architecture v2 `[layers]` names. Each is researched twice, independently, and the design rests on what
both runs of a layer agree on.

## [words] The owner's words, 2026-10-16

> let's move on to the expansion layers - launch a concurrent set of research agents each targeting
> their own expansion layer design given their fit into the new architectural design. Run each of
> them twice at medium effort. Then, base your own design against what the agents agree on.

## [scope] What this round designs

- **The three expansions**, as v2 `[layers]` defines them:
  - `observability`: signals about the loop and the runtime, and the cadence steps that act on them,
    Maintain and the Loop Review;
  - `integrations`: adapters to outside services: remote CI, notifications, cloud hosts, trackers,
    and deploy engines that promote a landed tree through environments;
  - `distribution`: the product's delivery: govkit, the adopt scripts, overlays, the install of the
    render targets Runtime's harness adapters define, and currency.
- **What each fills.** Each fills the layer contract P28 names, attaches only at extension points a
  core layer declares, and leaves the core whole when it is absent, its optional slots rendering the
  core's fallback.
- **What the core rounds left to this one:**
  - Maintain and the Loop Review as items: a detector register by layer, intakes rendered from keyed
    readings, event runs keyed by event, and a declared home for each report (flow-steps
    `[expansions]`);
  - Deploy's extensions: kit versions and release notes from distribution, and promotion through
    environments with a verify per SHA from integrations (flow-steps `[expansions]`);
  - `runtime.journal`, left open because the run record is observability's (layer-runtime
    `[policies]`).
- **The method.** One handoff per layer, run twice from identical text by `gov-researcher` at medium
  effort, as the owner asked. Where a layer's two returns agree, the design takes it. Where they
  split, the split is measured or put to the owner as a fork.

## [research] Dispatched, 2026-10-16

| Dispatch | Layer | Run | Handoff | Returned, and filed as |
|---|---|---|---|---|
| 51 | observability | A | `prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-19-researcher.md` | 8m26s, 37.8k out; `build/2026-10-16-build-PLAY-dClosedLoop-1-research-observability-a.md` |
| 52 | observability | B | the same | 10m01s, 45.2k out; `build/2026-10-16-build-PLAY-dClosedLoop-1-research-observability-b.md` |
| 53 | integrations | A | `prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-20-researcher.md` | 6m08s, 33.0k out; `build/2026-10-16-build-PLAY-dClosedLoop-1-research-integrations-a.md` |
| 54 | integrations | B | the same | 6m14s, 30.5k out; `build/2026-10-16-build-PLAY-dClosedLoop-1-research-integrations-b.md` |
| 55 | distribution | A | `prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-21-researcher.md` | 6m24s, 34.7k out; `build/2026-10-16-build-PLAY-dClosedLoop-1-research-distribution-a.md` |
| 56 | distribution | B | the same | 6m11s, 34.4k out; `build/2026-10-16-build-PLAY-dClosedLoop-1-research-distribution-b.md` |

- **Why the sixth run went later.** The agent-cap hook gives a prompt five direct spawns, and a slot
  frees 45 minutes after its claim (`tools/hooks/agent-cap.js`, the slot ledger). Dispatches 51 to 55
  claimed all five at 16:43 +03:00, so dispatch 56 was held for the first slot. Once all five had
  returned, the hook admitted it at 17:00. Its budget had reset on the returns' notifications, the
  defect `gap-rt-05` already records. No more than five ran at once.
- **What every handoff hands over.** The same settled facts: the layer table, P28 and the layer
  contract, the optional slot, the item and record rules, and Runtime's nine extension points. Each
  layer's part adds that layer's settled decisions, its policy keys and the register's gaps it
  touches. The design records each run may read are named in its part.
- **The return shape**, the same for all six: verdict, today, attach points, candidates with their
  losing tests, the contract filled, items and policies, gaps, and forks.

## [agreement] What each layer's two runs agree on

Each table sets a layer's run A beside its run B, question by question. "Both runs" holds only what
each found on its own. A claim one run made, which the design uses, was re-measured here first, and
the row says so. The returns are filed verbatim as `research-<layer>-a.md` and `-b.md` in `build/`.

### [agree-observability] Observability, dispatches 51 and 52

| Question | Both runs | Where they differ | The design takes |
|---|---|---|---|
| The line | A signal that decides a position is a core witness; one that only files work is an observability reading. B's test: a change under grading causes it, and committed history reproduces it | — | both |
| The 7 gateable drift signals | they are change-caused witnesses, run today by a core leg that calls this expansion's kit (`tools/gate-legs.json:1034`), so they move into core gates | A moves them to Test's legs; B into each owning core layer's gates | core gate legs on the bar, each owned by the layer whose records it grades |
| The detector register | one entry per detector, carrying its owner, pin, scope (repo, node, outside), events, fix and liveness; an entry without an owner or a pin is refused | A: 44 detectors, a tie broken by the writer of the offending row, a dead probe filed to its source; B: 40 detectors, the owner derived from the memory contract's writer field, a probe dead after 10 readings | the union of both entries; the owner rule is in `[design-observability]` |
| Where a detector registers | as a command adapter at Runtime's point, with its witness contract and idempotence probe | A declares one point of its own, `detectors`; B declares four: detectors, safe fixes, metric sources, events | see `[cross]`: a detector is registered at a core point, so any layer can add one |
| Node-scoped detectors | read on every node, never by one lease holder for all | A leases them per (period, node) under `maintain.node-detectors`; B reads them on the node that runs | every node, under a (period, node) lease |
| Readings | not a tracked record kind of their own, because they are re-derivable and they vary | A keeps them as a section of the maintenance record; B as journal lines, and measured 14 of 108 repeated (head, base, signal) groups varying in value or denominator, re-measured here with the same count | journal lines; the maintenance record lists what was checked, fixed and filed; repo-scope readings are taken in a clean checkout at the base SHA |
| Maintain's items | the period or event lease, a read per detector, the direct actions (reap, prune landed), a patch build at Design for a fix that changes tracked content, an ask keyed by (detector, offender key) that a recurrence never duplicates, the held legs and slower levels, the record, the lease released; event runs keyed by event | B adds a currency item and one item per event | as both, with the release cut and the currency probe moved to distribution (`[cross]`) |
| The Loop Review | lease, gather from committed sources, price the value ledger, propose, file into Plan under `review.loop.retire`, record | A tags the items `loop.*` and proposes by a role; B tags them `review.loop.*` and proposes by a command | `loop.*`, so items stay apart from the `review.loop.*` keys; proposals derived by a command, and judged at the owner's breakpoint (P24) |
| The value ledger | a generated view, never typed: kind, id, cost, catches, last catch, window, state | A keeps it in the Loop Review record; B as a library view | a library view, regenerated; each Loop Review record keeps the snapshot it priced |
| Catches | must come from committed verdict records, and none exist: Test's verdict record has to carry each leg's reds with their attribution | — | both: a new gap for dWitnessedBar |
| The run record | runlog's run record becomes a record kind this layer declares, written through `record` | B adds `observability.run-record` | both |
| `runtime.journal` | — | A: a selector of registered journal readers; B: retention in days | retention: readers already select themselves by registering, and "nothing prunes the journals" (`tools/runlog/README.md:568`) |
| A period that finds nothing | — | A: the lease witness only; B: a committed record every period | put to the owner (`[forks]`) |
| Gaps | close `gap-maint-01`, 02, 05, 06, 07 and 08; 03 in part, blocked on catch history; 04 not closed | — | both |

### [agree-integrations] Integrations, dispatches 53 and 54

| Question | Both runs | Where they differ | The design takes |
|---|---|---|---|
| The shape | each adapter registers at the core point that owns its slot, and all share one header; a single integrations registry loses | A also rejects outbox orders as the mechanism; B also rejects "every adapter a command" and refs as witnesses | both |
| The header | name, kind, grant, secret reference, probe | A adds the absence fallback; B adds the witness source and the dead-probe rule, under which a failed read never counts as green | the union of both |
| Today's seam | — | B found one live outside reader, `read_held_reds` (`tools/unattended/unattended.sh:9972`), which files an ask per red held suite; 53 such asks exist, verified here | the factory the header is extracted from (`[reuse]`) |
| Remote CI | it runs and it is red, not absent. It publishes one check run per SHA that anyone can read, cannot write a ref, and nothing reads it under `GATE_POST_MERGE=ci` (`tools/push-main.sh:434`), verified here | A: 22 of the last 40 push runs red; B: 42 of 60 push runs and 17 of 17 scheduled runs red since 2026-09-29 | a `remote-ci` verdict backend, after the landing only, for `deploy.core` under `ci` |
| Trusting a remote verdict | the workflow file sits in the tree it judges, so a pusher can certify itself; the verdict counts only at a pinned workflow blob | the alternative values offered | `verdict.remote.trust`, default `pinned-workflow` |
| The release | its own program per SHA and environment, after `deploy.core` is green: pick, approve, promote, verify, route a red as `deploy.on-verify-fail` says, record | A: one record per SHA, a row per environment; B: one record per (SHA, environment), kept outside any build folder | one record per (SHA, environment); the per-SHA view derived |
| Naming | rename the core item `deploy.release`, which deletes lease refs, to `deploy.unlease` | — | both |
| Notifications | send-only adapters at Runtime's point, the terminal by default, a receipt as witness | B: the owner's answer returns only through `next`, never through a channel | both |
| Trackers | no adapter kind: the ask backlog is the tracker, with an optional one-way mirror | A: a `tracker` key; B: the mirror registers as a journal reader | both |
| Grants and secrets | a grant (service, scopes) and a secret named by reference on the header; scopes probed at registration; the secret resolved into the adapter's process only; a value scan, run by the adapter's runner, binds; a shape scan only reports | key names | `integrations.secret-scan`, default `value-gate+shape-report` |
| Missing core points | a release slot with its environments in Flow's Deploy, and a grant field on Runtime's adapter rows; no tracker point is needed | B also: a verdict-backend registry in Flow's Test, prose only today | all three (`[cross]`) |
| Keys typed as literals | a key that selects an extension takes registered names | — | `verdict`, `run.host`, `maintain.host` and `notify.channel` take registered names |
| Gaps | close `gap-deploy-01`, 02, 03 (A: in part) and 05 | — | both |
| One run only | — | A: the `up —` micro-format asks for a password value in chat (`AGENTS.md:61`), verified here | a new gap |

### [agree-distribution] Distribution, dispatches 55 and 56

| Question | Both runs | Where they differ | The design takes |
|---|---|---|---|
| The line | moving bytes and versions across a repository boundary is distribution's; rendering, checking, the bar and the lander on bytes already in the tree are core; the adopt scripts' render and check halves are core, and only their install half is distribution's | A holds the descriptor schema core; B lists the descriptor's layer rows as a point distribution declares | core: the core reads descriptors today (`tools/run-gates/regen.py`, the gate legs in kit packs), so it cannot take their schema from an expansion |
| The mechanism | govkit installs by copy at a tagged release; a pinned reference or vendoring loses | A: a reference install loses on 13 adopter-written rows inside kit homes; B: vendoring loses on 28 of 92 rows landing outside the kit, and the hand `cp -r` path ignores 31 withheld rows and writes no receipt | copy at a release tag; the hand-copy path retires, and the runbook is generated from the descriptors |
| Versions | `deploy.version` mints in the lander's prepare and fills Deploy's version slot; every kit must declare a version | A counts 10 of 29 entries unversioned; B 9 | 10, re-measured here with `govkit epoch` |
| Releases | one annotated product tag per release, its notes generated from the landing records and version deltas, with no changelog file; none has ever been cut | A: `release/<date>`, cut by a cadence item of distribution's own; B: `gov/v<date>.<n>`, cut by Maintain as the handoff said | `gov/v<date>.<n>`, which orders several releases a day and leaves the word "release" to integrations; cut by distribution's own cadence program (EX-1) |
| The receipt | it must name the release it installed and where that came from | A: `gov_source` is a local path (`tools/govkit/govkit.py:8020`), verified here; B: 31 core files read the receipt, yet no layer declares it | schema 4 carries the release tag and the source remote, and the receipt is distribution's declared record kind |
| Currency | the adopter compares its receipt with gov's remote tag list and needs no gov checkout; gov reads each adopter's committed receipt for the fleet view; an unreachable remote is unverified, never green | A also runs the adopter's comparison as a bar leg | a cadence program, not a bar leg: the bar makes no network call for a value it does not grade (`tools/drift-audit/drift_report.py:3387-3389`) |
| The fleet register | `adopters.toml` grows into it: key, remote, default branch, cadence | — | both |
| Descriptors | they gain layers, the points they declare and use, record kinds and policies, each joined to its registry, and a required version | field names | `layers`, `declares`, `uses`, `records`, `policies`, `units` and `version_from` |
| Conformance | one gate: fields present, every name resolving in its registry, a version required, `requires` closed over the siblings the code resolves, render destinations named by kind | A: owned by dOrderedCharter; B: the kit factory's, which v2's chain gives dShippedRelease | one core gate; its owner is the chain re-cut's |
| Wiring and versions | one in-tree wiring verdict that iterates the descriptors as one bar leg, and one version check; `gap-tool-02` undercounts both | A: three wiring judges and five lockstep checks; B: all 11 `[check]` argvs duplicate their own gate legs | both |
| Inline copies | generated from `tools/lib/`, never hand-kept | B: in-tree by a regen stage, tracked and drift-gated, and the class spans 16 primitives and 254 markers | in-tree by regen; 261 markers over 17 names, re-measured here |
| Render targets | Claude Code's paths are hard-coded: 8 descriptor rows write under `.claude/` | A: distribution declares target kinds; B: a field on Runtime's harness adapters | an install-target field on each harness adapter (`[core-points]`) |
| The overlay | — | A: a repository's own rules render inside the charter's one block, not a separate one (`AGENTS.md:1-177`, its section 2 at line 84), verified; B: gov's overlay says it selects every kit, yet selects 22 of 29 (`.governance/deploy.toml:11,18-26`), verified | one new gap for both |
| Gov's own receipt (P8) | — | A: a source-mode receipt, so gov runs the same checks; B: none, so gov's tree stays the standing fixture of the core without distribution | put to the owner (DI-1) |
| Keys | `currency.max-behind`, default 2 releases | A adds `currency.on-behind`, default owner-item; B adds `install.from`, default release-tag | all three |
| Gaps | close `gap-deploy-04`, `gap-deploy-06` (its review stays a role's), `gap-deploy-08` in part, `gap-tool-02` and `gap-tool-04`, and only the version half of `gap-deploy-07` | — | both |
| The deploy-governance Skill | both slim it to an operator order | — | it retires, as the memory round's tooling map already says (`gap-tool-05`: no reader, 0 loads); neither run was handed that verdict |
| One run only | — | B: govkit's usage text omits the `contribute` verb it dispatches (`tools/govkit/govkit.py:13212` against `:13713`) | noted in `[open]`, too small to register |

## [cross] What runs on different layers found in common

Some findings came from runs on different layers, each working alone. They shape all three designs.

| Finding | Found by | Evidence | The design takes |
|---|---|---|---|
| The scheduler has no point where a layer registers a cadence program | observability A and B, distribution A | layer-runtime `[schedule]` runs "the cadence items that their layers declare", yet none of `[extend]`'s nine points takes one | Runtime declares a tenth point, cadence items |
| Records that belong to no build have no home | observability A and B, integrations B | maintenance and Loop Review records are keyed by period, release records by SHA and environment; `memory/HYGIENE.md:17-35` has no such home, and `project/` holds waiver registries "and nothing else" | the memory contract declares one, asked as `[forks]` EX-2 |
| One expansion attaching to another breaks P28 | observability B, distribution A | Maintain cutting gov's release makes observability carry distribution's work; observability reading remote CI needs an integrations adapter | expansions meet only through core points and records, asked as EX-1 |
| Remote CI is red, not absent | integrations A and B; observability A and B found its drift signal dead | both integrations runs read every run since 2026-10-13 14:03 as red through the public API. `remote_ci_red_streak` shells to `gh`, which is absent on this node, and is not asked under `--check` (`tools/drift-audit/drift_report.py:3333-3341,3385-3390`), verified here | the signal retires, and integrations' remote-verdict records replace it; reading the red runs' logs needs an authenticated read |
| No catch history is committed | observability A and B | both runs counted 78 bars in this node's journal, and A set them against 361 landings on main; the gate ledger keeps only each leg's last state | Test's verdict record names each leg's reds |
| A key that selects an extension is typed as a literal list | integrations A and B | `verdict`, `run.host` and `maintain.host` list values, against layer-runtime `[extend]`'s rule that such keys take registered names | they take registered names |

**Expansions meet only through the core.** Each expansion registers only at points a core layer
declares. One expansion uses another's output only as records it reads through memory, and when the
other is absent it renders the core's fallback. Under this rule:
- gov's tagged release and the adopter currency probe are distribution's own cadence programs, not
  Maintain's items, so FL-DP2's "Maintain's run cuts a tagged release" changes its cutter, not its
  mechanism;
- observability reads distribution's currency observations and integrations' remote verdicts as
  records, and registers nothing of theirs;
- Maintain's report channel and its cloud host use Runtime's notification and host points, which
  integrations fills, so without integrations they fall back to the terminal and the node tick.

**Three senses of "release".** Integrations' runs both rename the core item `deploy.release`, which
deletes lease refs, to `deploy.unlease`, and give `release.*` to promoting a landed SHA through
environments. Both distribution runs use "release" for cutting gov's tagged kit release. The design
names the three apart:
- `deploy.unlease`, the core item that deletes a build's lease refs and closes its mailbox;
- `release.*` and the `release` record, integrations' promotion of a landed SHA through environments;
- `kits.*`, the `kit-release` record and the `gov/v<date>.<n>` tags, distribution's delivery of gov's
  kits.

## [design] The expansions, as proposed

Each design takes what its layer's two runs agree on, resolves a split by the measurement named in
`[agreement]`, and leaves the rest to `[forks]`.

### [core-points] What the core declares so the expansions can attach

P28 lets an expansion attach only where a core layer declares a point. The runs found eight points
missing. Each lands in the core layer named, and its chain build is in `[gaps-proposed]`.

| Point | Core layer | What registers there | Used by |
|---|---|---|---|
| cadence items: a program with its host key, period, lease and events | Runtime, as its tenth extension point | Maintain and the Loop Review; gov's kit release and the currency probe | observability, distribution |
| reading and fix classes on command adapters: a reading carries its scope (repo, node, outside), pin, events, fix and liveness, and its owner derived from the memory contract | Runtime's command adapters | each layer's own detectors and safe fixes | observability runs them; any layer registers its own |
| a grant on every adapter row: the service, its scopes, and its secret by reference | Runtime's adapter rows | every outside adapter | integrations |
| verdict backends, as a registry | Flow, in Test | `local-hook` (built in), `peer-node`, `remote-ci` | integrations |
| the release slot after the landing, with its environments, each naming an engine and a verify adapter | Flow, in Deploy | the `release.*` program and its engines | integrations |
| homes for record kinds keyed by period, SHA or adopter rather than by build | Memory's contract | maintenance and Loop Review records, release records, fleet rows and currency observations | all three |
| the version slot in the landing's prepare | Flow, in Deploy | `deploy.version`, which mints each kit whose shipped bytes moved | distribution |
| install targets on each harness adapter: where a rendered Skill, agent, rule, hook or settings fragment lands | Runtime's harness adapters | each adapter's paths, read by the install | distribution |

### [design-observability] Observability

**What it is.** `observability` reads signals about the loop and the runtime, never typed, and acts on
them only through the flow, by its two cadence programs, Maintain and the Loop Review.

**The line with the core.** A signal that decides a position is a core witness: a verdict, a lease, a
transition, a return record, `refs/gov/bar-red`. A signal that only files work is a reading, and
observability's. The seven gateable drift signals are change-caused witnesses, so they leave
drift-audit for core gate legs, each owned by the layer whose records it grades: `ledger_rows` by
memory, `non_terminal_specs` and `closed_specs` by flow, and `handkept`, the two lexicon signals and
`cutoff_keys_armed` by instruction (observability B's table).

**A reading's owner is derived, never typed.** It is the layer the memory contract declares for the
record kind whose rows the offenders are. Node state (processes, worktrees, journals) is Runtime's. A
tie goes to the layer that wrote the offending row. A probe dead for `maintain.dead-after` readings is
filed to the layer that feeds it its input. A reading with no derivable owner, or no pin, is refused
at registration.

| Contract field | Observability's entry |
|---|---|
| tag and definition | `layer.observability`, as above |
| instruction units | Maintain's run rules (only declared fixes are applied, and everything else is filed); the admission rule (no reading without an owner and a pin); the Loop Review's proposal rule; the card cells' texts |
| engine kits | drift-audit's report-only half; runlog's reader half and its run record, its journal grammar moved into Runtime; branch-reconcile as the prune fix; process-monitor's census as a node reading, its reaping staying Runtime's; codebase-map's stale-dossier reading; the two cadence programs; the value-ledger generator (dCalibratedLens) |
| record kinds | the maintenance record, per period or event run; the Loop Review record, per period, with the ledger snapshot it priced; the run record, per run; the value ledger, a generated library view |
| extension points declared | none: readings, fixes and cadence programs all register at core points (`[core-points]`) |
| extension points used | Runtime's cadence items, command adapters, journal readers, hook packs (the session-start breach), host and notification adapters; Flow's Plan intake, the patch-build entry at Design and the breakpoints; Memory's record kinds through `record`; the card's optional slots |
| policies | `maintain.*`, `review.loop.*` and the new keys below |
| gates | reading admission (owner, pin, scope, liveness); the maintenance record's schema; every applied fix inside `maintain.fixes`; the value ledger derived, never typed |

**Maintain**, a cadence program keyed by period, or by event and SHA:

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `maintain.lease` | executor | takes the lease for the period, or the event and SHA, and for each node-scoped reading the (period, node) lease | the lease, through `record`; a closed witness for the key means done | held elsewhere → skip; done → nothing; taken → `maintain.read` |
| `maintain.read` | command: each registered reading | reads repo-scoped readings in a clean checkout at the base SHA, and node-scoped ones on this node | journal lines: reading, SHA, value, denominator, offender key | in pin → nothing; over pin → `maintain.direct`, `maintain.patch` or `maintain.file`, by its fix; dead past `maintain.dead-after` → `maintain.file`, to its source |
| `maintain.direct` | command: the reading's fix, where it changes no tracked content (reap, prune landed) | applies the fix | the next reading shows the set gone | a survivor → `maintain.file` |
| `maintain.patch` | command | opens a patch build at Design for a fix that changes tracked content, its intake rendered from the reading | the intake, keyed by (reading, offender key) | Design, as `patch.ratify` says |
| `maintain.file` | command, through `record` | files an ask for the owner, with a severity and the acceptance "back under its pin"; a recurrence adds a `seen` row to the open ask | the ask, keyed by (reading, offender key) | Plan's triage, as `maintain.on-breach` says |
| `maintain.levels` | command: the bar's held profile | runs the slower test levels and the held legs assigned to Maintain | the verdict record | a red → `maintain.file`, owned by Test |
| `maintain.record` | command, through `record` | records what was checked, fixed and filed, and releases the lease | the maintenance record, or the lease witness alone, as `maintain.record` says | closed |

An event run carries only the readings whose events name it. Its events are `default-branch-red`
(produced by the core's `refs/gov/bar-red`), `release-verify-failed` (by integrations' release
record, when installed) and `session-start-breach` (by the card's cells).

**The Loop Review**, a cadence program keyed by ISO week:

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `loop.lease` | executor | takes the week's lease | the lease | `loop.gather` |
| `loop.gather` | command | gathers the metrics from committed records: cycle times from transitions, yield from review records, catches from Test's verdict records, cost from the ceiling evidence, flakes from retries, records overhead and surface size from git | the metric set, each value with its source; a missing source renders searched-none | `loop.price` |
| `loop.price` | command | regenerates the value ledger: kind, id, since, cost, catches, false reds, last catch, window, state | the ledger blob | `loop.propose` |
| `loop.propose` | command | proposes retiring or merging each row with no catch in `review.loop.window-days`, and re-derives the caps | the proposal list | `loop.file` |
| `loop.file` | command, through `record` | files each proposal into Plan's triage with its ledger row | one ask per proposal | the owner's breakpoint, as `review.loop.retire` says |
| `loop.record` | command, through `record` | writes the Loop Review record | the record | closed |

**New keys:**

| Key | Allowed values | Default | Why |
|---|---|---|---|
| `runtime.journal` | days, or `all` | 60, at least `review.loop.window-days` | journal retention; nothing prunes the journals today |
| `maintain.reading-tree` | clean-base, worktree | clean-base | 14 of 108 repeated readings varied with the tree they were taken in |
| `maintain.node-readings` | every-node, lease-holder | every-node | a node-scoped reading sees only its own node |
| `maintain.detector-admission` | refuse-unowned, report-unowned | refuse-unowned | 0 of the 27 drift signals carry an owner |
| `maintain.dead-after` | a count of readings | 10 | drift-report's existing limit |
| `maintain.record` | every-period, on-finding | every-period | EX-3: both values built, the default the owner's |
| `observability.run-record` | per-run, on-anomaly, none | per-run | today's behaviour; on-anomaly eases `gap-maint-04` |
| `review.loop.catch-source` | verdict-records, node-journal | verdict-records | another node cannot see a node's journal |

**Absent.** The core lands builds unchanged. The card's `drift —` and `health —` cells render "not
installed: observability". No cadence program runs Maintain or the Loop Review, so asks and patch
builds come from requests alone (P6). A stage review keeps its cost in its own record, and the ledger
slot renders not installed. The seven gateable signals still gate, because they are core now.
Reaping happens only at Runtime's act ceiling.

### [design-integrations] Integrations

**What it is.** `integrations` holds the adapters to outside services. Each adapter registers at the
core point that owns its slot, and every adapter carries the same header:

| Header field | What it holds |
|---|---|
| name and kind | a registered name, and its kind: verdict backend, host, notification, deploy engine, verify |
| grant | the service, and the scopes the adapter needs |
| secret | a reference to where the secret lives, never its value; `anonymous` when it needs none |
| witness source | where its outcome is read back from, keyed by SHA or receipt |
| probe | a liveness and scope probe; a failed read is a dead probe and never counts as green |
| fallback | the core's behaviour without it |

The header is extracted from `read_held_reds` (`tools/unattended/unattended.sh:9972`), today's one
live outside reader, which already reads anonymously, keys by SHA, bounds its read and never reads a
dead probe as green.

| Kind | Registers at | Core fallback |
|---|---|---|
| verdict backend: `remote-ci`, `peer-node` | Flow's verdict backends, in Test | `local-hook` (P3) |
| host: `cloud-routine` | Runtime's host adapters | the node tick |
| notification channel | Runtime's notification adapters | the terminal |
| deploy engine and verify, per environment | Flow's release slot, in Deploy | no release; the build closes at landing |
| tracker | none: the ask backlog is the tracker. An optional one-way mirror registers as a journal reader | the ask backlog |

| Contract field | Integrations' entry |
|---|---|
| tag and definition | `layer.integrations`, as above |
| instruction units | the adapter author's unit (the header, the dead-probe rule); the grant rule: a secret is named, never written; the release view; the deployer role's release instruction |
| engine kits | the `integrations` kit: the header factory and the registry check; `verdict:remote-ci`, extracted from `read_held_reds`; `verdict:peer-node`; `host:cloud-routine`; notification channels; the release runner. Each adopter's engine adapter is a dShippedRelease unit |
| record kinds | `remote-verdict` (SHA, tree, writer, run id, workflow blob, conclusion); `release` (one per SHA and environment); `delivery` (a notification and its receipt); `grant` (declared scopes, never values) |
| extension points declared | none: every kind registers at a core point (`[core-points]`) |
| extension points used | Flow's verdict backends and release slot; Runtime's command, host, notification and journal-reader points, and the grant field on adapter rows |
| policies | the new keys below, and the catalogue's `verdict`, `run.host`, `maintain.host`, `notify.owner`, `deploy.runs`, `deploy.promotion`, `deploy.on-verify-fail` and `build.closes` |
| gates | every adapter's header complete and its probe live; the granted scopes no wider than declared; the remote verdict's workflow blob pinned; the secret value scan |

**A remote verdict stands as a witness only when every field holds:**
- **key:** its `head_sha` is the landed SHA, and that SHA's tree is the verdict's tree;
- **writer:** the platform's own app, the declared workflow path, a push event and the declared job;
- **source:** the workflow blob at `head_sha` equals the pinned blob;
- **liveness:** the bar step concluded, and was not skipped;
- **a failed read:** a dead probe, which is no verdict and never green.

Remote CI is read after the landing only, as `deploy.core`'s witness under `GATE_POST_MERGE=ci`. The
local hook stays the verdict before the landing (P3).

**The release**, a program per SHA and environment, opened when `deploy.core` is green and
`release.environments` is not empty. Under the default `build.closes: at-landing` it outlives the
build. The core item `deploy.release` is renamed `deploy.unlease`.

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `release.pick` | command | takes the newest landed SHA with a green core verdict that environment E lacks, and E's promotion lease | the landing record and the SHA's core verdict | `release.approve` |
| `release.approve` | the owner, or a command | asks the owner where `deploy.promotion` says so, and otherwise passes on green | the disposition, or `auto-on-green` | approved → `release.promote`; refused → the release closes as held |
| `release.promote` | command: E's engine adapter | promotes the SHA into E; already there counts as done | the engine's deployment id, read back by (SHA, E) | promoted → `release.verify`; refused or unreachable → retry, then an owner item |
| `release.verify` | command: E's verify adapter | verifies the SHA in E | a runner-written verdict keyed by (SHA, E) | green → `release.record`; red → `release.route`; dead probe → an owner item |
| `release.route` | command | acts as `deploy.on-verify-fail` says: roll forward with an ask filed; roll back to E's last verified SHA, re-verify and file an ask; or halt E and notify the owner | the routing record | as its value says |
| `release.record` | command, through `record` | writes the release record for (SHA, E) | the record | the next environment; at the last, `deploy.close` under `after-release-verifies` |

**Grants and secrets.** A secret lives in the node's credential store, or in the CI secret store for
an adapter that runs in CI, and is resolved into the adapter's own process only. Registration
probes the scopes granted, and refuses wider than declared. The adapter's runner, the one principal
holding the value, scans tracked files, `memory/`, the journal and the transcripts for the value and
its encodings, and records a count and a salted id only. Zero is the witness. Runlog's shape scan
reports, and gates nothing, because it reds on examples and fixtures.

**New keys:**

| Key | Allowed values | Default | Why |
|---|---|---|---|
| `release.environments` | an ordered list of registered environments | none | none means no release program runs, so the core alone still lands |
| `verdict.remote.trust` | pinned-workflow, owner-reviews-workflow-change, app-only | pinned-workflow | the workflow file sits in the tree it judges |
| `notify.channel` | registered channel names | terminal | the only channel today |
| `integrations.secret-home` | os-keychain, env-injected | os-keychain | for node adapters; a CI-hosted adapter reads the CI store |
| `integrations.secret-scan` | value-gate, value-gate+shape-report | value-gate+shape-report | a shape scan alone reds on fixtures |
| `integrations.tracker` | none, mirror-out | none | no tracker is in use |

`verdict`, `run.host`, `maintain.host` and `notify.channel` take registered names, validated against
the registry, with today's values as the built-ins.

**Absent.** The verdict is the local hook, the host is the node tick, the owner hears through the
terminal, and a build closes at landing with no release. `build.closes: after-release-verifies` is
refused, or falls back with a report, as `policy.on-missing-expansion` says.

### [design-distribution] Distribution

**What it is.** `distribution` moves kits and their versions across a repository boundary: it
installs a release of kits into a repository, keeps the release current there, and measures how far
behind each repository is. What runs on bytes already in the tree stays core: the render and its
`--check`, the bar, the lander, and the descriptor schema the core reads.

**The mechanism.** govkit installs by copy at a release tag, and the receipt names that release and
the remote it came from. A pinned reference or vendoring loses on rows that land outside the kit or
that an adopter writes inside it. The hand `cp -r` path retires, because it ignores withheld rows and
writes no receipt, and the runbook is generated from the descriptors.

| Contract field | Distribution's entry |
|---|---|
| tag and definition | `layer.distribution`, as above |
| instruction units | the operator order for install and update, in the runbook generated from the descriptors; the release-note and currency views. The deploy-governance Skill retires, as the tooling map says (`gap-tool-05`) |
| engine kits | govkit, with check-wiring's install arms and check-placeholders folded in; the install half of each adopt script; the inline-copy generator; `adopters.toml`, grown into the fleet register |
| record kinds | `receipt` (`.governance/install.json`, schema 4: per-kit versions, the release tag, the source remote; gov's own in source mode, DI-1); `kit-release` (an annotated `gov/v<date>.<n>` tag, its notes generated from the landing records and version deltas); `currency` (an adopter's releases behind, keyed by its HEAD SHA); `fleet` (gov's reading of each adopter, per release); the fleet register's rows; outbox orders, as today |
| extension points declared | none: the descriptor schema, the version slot and the install targets are core points (`[core-points]`) |
| extension points used | Flow's version slot in Deploy; Runtime's cadence items, command adapters, harness adapters' install targets and notification adapters |
| policies | `release.cadence`, `deploy.currency`, `runtime.harnesses`, and the new keys below |
| gates | one wiring verdict, in-tree, iterating the descriptors as one bar leg; one version check; kit conformance, core; receipt integrity |

**The descriptor fields P28 needs**, each joined to its registry by the conformance gate: `layers`,
`declares`, `uses`, `records`, `policies`, `units`, and a required `version_from`, with `none` refused
unless the kit ships no bytes.

**Items:**

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `deploy.version` | command: `govkit mint`, in the lander's prepare | mints each kit whose shipped bytes moved, filling Deploy's version slot | the version check's verdict at the push boundary | minted or clean → the landing goes on; refused → Test; govkit absent → the announced skip |
| `kits.cut` | command, a cadence program per `release.cadence` | cuts the annotated tag `gov/v<date>.<n>`, its notes generated since the previous tag; under `owner-cut`, an owner item | the tag on the remote, and its notes blob | nothing landed since the last tag → skip, announced; cut → done; refused by the remote → an owner item |
| `kits.currency` | command, a cadence program in each adopter | joins the receipt's rows to gov's remote tag list: releases behind, per kit | the currency record, keyed by HEAD SHA; unreachable → unverified, never green | within `currency.max-behind` → done; over → as `currency.on-behind` says |
| `kits.fleet` | command, a cadence program in gov | reads each register row's committed receipt at its remote tip | the fleet record, per release | `pull-and-watch` → reported; `push-branches` → `kits.offer` |
| `kits.offer` | command | under `push-branches`, runs the update in a worktree and pushes `gov/update-<release>` to the adopter | the pushed ref on the adopter's remote | pushed → the adopter lands it with its own lander; refused → an outbox order |
| `kits.install`, `kits.update` | the owner, or a command | applies or updates a release, installing each render target where the adapters in `runtime.harnesses` say | the receipt, and the wiring verdict | an adapter that declares no target → its slot renders not installed, the core render kept |

**New keys:**

| Key | Allowed values | Default | Why |
|---|---|---|---|
| `currency.max-behind` | a count of releases | 2 | it turns a measurement into an owner item; 990 commits behind went unseen because nothing set a bar |
| `currency.on-behind` | note, owner-item, red | owner-item | a red would block an adopter's own landings on gov's cadence |
| `install.from` | release-tag, any-commit | release-tag | the receipt then names one release, so "releases behind" is defined |

**Absent.** The lander mints nothing, says so, and lands. `check-receipt` skips with "no receipt", and
kit resolution probes beside the kit. The currency slot renders "not installed: no receipt, currency
unmeasured". A preset that names `release.cadence` or `deploy.currency` is refused under
`policy.on-missing-expansion: refuse`. The render and `--check` of `AGENTS.md` and its aliases still
run, because they are core.

## [gaps-proposed] Gaps to register once the forks settle

Each row is a distance both runs of a layer measured, or one run measured and this round re-measured.
Its id is the next free in its stage, and its owner is the chain build whose stage holds it. Two
findings join existing gaps instead of adding one: the undeclared release slot is `gap-deploy-01`'s,
and the verdict-backend registry is `gap-test-02`'s.

| Proposed id | Stage | Sev | What is missing | Evidence | Owner |
|---|---|---|---|---|---|
| `gap-maint-09` | Maintain | MED | The seven gateable drift signals are change-caused witnesses, yet the core bar reaches them through this expansion's kit. | `tools/gate-legs.json:1034-1049`; observability A and B | dTendedCadence |
| `gap-maint-10` | Maintain | LOW | A reading varies with the tree it is taken in: 14 of 108 repeated (head, base, signal) groups differ in value or denominator. | `.git/drift-history.tsv`, re-measured here | dTendedCadence |
| `gap-maint-11` | Maintain | LOW | The remote-CI drift signal is dead: it shells to `gh`, absent on this node, and is not asked under `--check`. | `tools/drift-audit/drift_report.py:3333-3341,3385-3390` | dTendedCadence |
| `gap-test-10` | Test | HIGH | No catch history is committed. The gate ledger keeps each leg's last state, gate reds live in one node's journal, and no bug class carries a catch field, so nothing can price a gate. | `tools/run-gates/run-gates.sh:5214-5256`; observability A and B | dWitnessedBar |
| `gap-test-11` | Test | MED | A remote verdict certifies itself: the workflow that produces it is part of the tree it judges, and nothing grades the workflow's text. | `.github/workflows/remote-ci.yml:15-16`; integrations A and B | dWitnessedBar |
| `gap-test-12` | Test | MED | The hosted bar has been red on every run since 2026-10-13 14:03, and reading why needs an authenticated read of its logs. | integrations A and B, through the public API | dWitnessedBar |
| `gap-test-13` | Test | LOW | The one live outside reader, the held-CI reader, sits inside the unattended kit with no adapter registration. | `tools/unattended/unattended.sh:9972`; `.unattended.conf:221` | dWitnessedBar |
| `gap-rt-15` | Runtime | HIGH | The scheduler runs "the cadence items that their layers declare", but no extension point takes one, so Maintain, the Loop Review, the kit release and the currency probe have nowhere to register. | layer-runtime `[schedule]` and `[extend]`; observability A and B, distribution A | dWellOiledMachine |
| `gap-rt-16` | Runtime | MED | Nothing prunes the journals, and six node-local grammars sit beside runlog's. | `tools/runlog/README.md:568`; observability B | dWellOiledMachine |
| `gap-rt-17` | Runtime | MED | No adapter declares a grant, and no check covers secrets: the lander's push rides an ambient credential, and no gate leg scans for a secret. | `credential.helper=manager` from the system gitconfig; 0 of 140 legs scan for one; verified here | dWellOiledMachine |
| `gap-rt-18` | Runtime | MED | No channel reaches the owner outside a session: no notification hook is wired, and no channel code exists. | `.claude/settings.json`; integrations A and B | dWellOiledMachine |
| `gap-mem-16` | Memory | MED | Records that belong to no build have no home: maintenance and Loop Review records are keyed by period, release records by SHA and environment, currency observations by adopter. | `memory/HYGIENE.md:17-35`; observability A and B, integrations B | dTotalRecall |
| `gap-deploy-10` | Deploy | MED | `GATE_POST_MERGE=ci` binds nothing: the lander starts no bar under it, and the pre-push hook reads only `refs/gov/bar-red`, though flow-steps names the CI result as the witness. | `tools/push-main.sh:434`; `.githooks/pre-push:1919-1936`, verified here | dShippedRelease |
| `gap-spine-07` | Spine | LOW | Keys that select an extension are typed as literal lists (`verdict`, `run.host`, `maintain.host`), against the rule that they take registered names. | v2 `[policies]`; layer-runtime `[extend]` | dDeclaredLoop |
| `gap-found-18` | Foundation | MED | The `up —` micro-format asks for a password value, inviting a secret into chat. | `AGENTS.md:61`; `coding-governance-agents.template.md:64`, verified here | dOrderedCharter |
| `gap-deploy-11` | Deploy | MED | No release has ever been cut: no release tag, no changelog, and 10 of 29 kit entries declare no version. | `git tag`; `govkit epoch`, re-measured here; distribution A and B | dShippedRelease |
| `gap-deploy-12` | Deploy | MED | A receipt records gov's source as a local path, so an adopter cannot resolve where its install came from. | `tools/govkit/govkit.py:8020`, verified here | dShippedRelease |
| `gap-rt-19` | Runtime | MED | Harness adapters declare no install targets: 8 descriptor rows write to Claude Code's `.claude/` paths. | `tools/*/kit.toml` and `tools/govkit/entries/`, verified here; layer-runtime `[harness]` | dWellOiledMachine |
| `gap-tool-07` | Tooling | MED | Kit descriptors declare no layers, extension points, record kinds or policies, and nothing validates their keys. | 0 of 29 descriptors carry `layers`, verified here; distribution A and B | dShippedRelease |
| `gap-found-19` | Foundation | MED | No overlay is a separate project block: a repository's own rules render inside the charter's one block, and gov's own overlay says it selects every kit, yet selects 22 of 29. | `AGENTS.md:1-177`; `.governance/deploy.toml:11,18-26`, verified here | dOrderedCharter |

Two existing gaps grow instead of adding rows. `gap-tool-02` gains B's finding that all 11 `[check]`
argvs duplicate their own gate legs. `gap-tool-04` widens from `resolve_python`'s 73 copies to 261
inline markers over 17 primitives, re-measured here.

## [forks] Asked, 2026-10-16

Each fork is a decision the runs could not make for the owner: a split between a layer's runs, or a
choice the agreed design leaves open. Every option offered becomes an allowed value or a recorded
decision, and the recommended one is marked.

**EX-1. "How do the expansions meet each other?"**
- **Only through the core (Recommended).** Each registers only at core points. One reads another's
  output only as records through memory, and when the other is absent it renders the core's fallback.
  Gov's kit release and the currency probe become distribution's own cadence programs, so FL-DP2's
  release changes its cutter from Maintain, not its mechanism.
- **An expansion may declare points another fills.** Each must still degrade on its own when the
  other is absent, and P28 gains that exception.

**EX-2. "Where do records that belong to no build live?"**
- **Under `memory/<layer>/<kind>/`, each kind's home declared in the memory contract (Recommended).**
  The layer's tag names the home, so it is derived rather than chosen.
- **A standing build folder per program,** such as `builds/maintain/`. A build would then never close
  at landing.
- **Refs only,** with no committed record: the witness is a ref, and the record exists nowhere.

**EX-3. "A Maintain period that finds nothing: what does it leave?"** The two observability runs
split here.
- **The lease witness only (Recommended),** keyed by the period and visible on every node, with a
  maintenance record only when something was fixed or filed. Observability A, and `gap-maint-04`'s
  weight of records.
- **A committed maintenance record every period.** Observability B, at about 30 records a month.

**DI-1. "Does gov carry its own install receipt?"** P8 says every adopter is an adopter, gov included.
The two distribution runs split here.
- **A source-mode receipt (Recommended).** Gov records itself as the source of its own install, so the
  receipt's readers, the wiring verdict and the currency probe run in gov as they do in an adopter,
  and currency reads "source, 0 behind". Distribution A, and the charter's "dogfoods every kit it
  ships".
- **No receipt.** Gov's tree stays the standing fixture of the core without distribution, and a
  self-receipt would only hash the source against itself. Distribution B.

## [settled] What EX-1 to EX-3 and DI-1 settled, 2026-10-16

The owner's answers, verbatim:
- **EX-1:** "Only through the core (Recommended)". Expansions meet only through the core. P28 says so, gov's kit
  release and the currency probe are distribution's own cadence programs, and Maintain no longer
  cuts the release.
- **EX-2:** "memory/<layer>/<kind>/ (Recommended)". A record that belongs to no build lives under
  `memory/<layer>/<kind>/`, its home declared in the memory contract (layer-memory
  `[revised-expansions]`).
- **EX-3:** "A record every period by default, owner-switchable. Both options built.". `maintain.record` defaults to
  `every-period`, `on-finding` stays allowed, and the build owes both arms with a fixture each.
- **DI-1:** "Source-mode receipt (Recommended)". Gov records itself as the source of its own install, so
  the receipt's readers, the wiring verdict and the currency probe run in gov as in an adopter, and
  currency reads "source, 0 behind".

**Where each landed:**
- v2 `[layers]` takes the three definitions and P28 the rule; `[policies]` takes seventeen keys,
  `[presets]` sixteen of them, with `release.environments` among the keys presets never touch; the
  selecting keys take registered names; the chain's cells take the twenty gaps.
- flow-steps declares Test's verdict backends and Deploy's version and release slots, rewrites
  `[expansions]`, and renames `deploy.release` and `life.release` to `deploy.unlease` and
  `life.unlease`, which mean the same thing: delete the build's leases and close its mailbox.
- layer-runtime declares cadence items as its tenth point, the reading and fix classes, adapter
  grants and install targets, and settles `runtime.journal` as retention.
- The register takes the twenty gaps in `[gaps-proposed]`, and widens `gap-tool-02` and
  `gap-tool-04`.

## [open] What the expansion round owes

- **The chain builds' planned units** for the eight core points and the three designs, at the chain
  re-cut v2 `[owed]` already carries.
- **The round's Tier-2 review**, owed before the round closes.
- **Too small to register:** govkit's usage text omits the `contribute` verb it dispatches
  (distribution B).
