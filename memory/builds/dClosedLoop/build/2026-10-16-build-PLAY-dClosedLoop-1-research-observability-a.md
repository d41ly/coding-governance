# Research: the observability expansion, run A

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 51's return, verbatim. Its question is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-19-researcher.md`, which dispatch 52 ran
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`.

---

## 1. Verdict

Observability should be one kit-backed layer built on a **detector register** that Maintain's cadence items read. The kit carries the register, the drift-audit engine, runlog's run record and the Loop Review. Each reading is committed once per period inside a maintenance record. Each breach is turned into a keyed ask, or a patch build at Design, sent to the layer the register names as its owner.

The line with the core is simple. A witness decides a position and is core. A reading only files work and belongs to observability. The core already publishes the one signal that blocks work, default-branch red, as `refs/gov/bar-red`.

`runtime.journal` should select which registered journal readers run, and nothing else. Without observability the core loses nothing it needs: every slot renders "not installed", and the loop closes through requests (P6).

## 2. Today

| Part | What it does | Measured use | Where |
|---|---|---|---|
| drift-audit | 27 signals over records against the tree | 15 nonzero, 7 gateable, 22 with a pin, 2 dead, 0 with an owner field | `drift_report.py:3518-3535`; pins `drift_signals.py:243`; table below |
| `drift-audit records` leg | `drift_report.py --check` reds the gateable 7 and ratchets | on the bar | `gate-legs.json` (argv shown below) |
| drift history | `--check` appends readings to a node-local TSV | 838 rows, 32 readings since 2026-10-08, one node | `drift_report.py:3754,4444-4451` |
| runlog journal | 3 producers, one grammar, untracked | driver 1,964, gates 79, pushes 262 lines | runlog `README.md:15-52`; writers `run-gates.sh:2525`, `unattended.sh:13930` |
| runlog run record | a committed, structural account of one run | 20 tracked; read only by the runlog kit and Skill | `README.md:355-503`; leg `runlog record schema` |
| gate yield | `journal --by-leg` | 140 legs: 54 ever red, 86 never (39 always-run never red), from 78 bars on one node | output below |
| process-monitor | census, fence, classify, reap | 340 in census, 35 scoped, 0 flagged; the hook only dry-runs | `procmon-hook.js:119` |
| health log | self-heal events | 7 lines: 3 beacon-reaped, 2 retry-passed, 1 tree-killed, 1 scratch-swept | `lib/health_log.py:10-20` |
| branch-reconcile | verdicts for refs and worktrees | 51 MERGED, 6 IN-PROGRESS, 5 UNMERGED-LIVE | `branch_reconcile.py:1198-1203` |
| orientation card | `drift —` and `health —` cells | reads the last drift-history group | `manifest-check.sh:441-472,231` |
| post-merge bar | full bar on the landed tip, publishes `refs/gov/bar-red` | started by the lander; the ref is read by pre-push | `post-merge.sh:1-19`, `push-main.sh:420-434`, `.githooks/pre-push:1909-1933` |
| CI cron | read-only held job, nightly | `cron: '23 4 * * *'`, artifact upload | `remote-ci.yml:33-34,116-125` |
| ceiling evidence | per-leg cost, tracked | 119 rows | `tools/run-gates/ceiling-evidence.txt` |
| govkit census | adopter files classed IN-SYNC, DRIFT or FORK | gov-internal, never on the bar | `govkit/census.py:1-25` |
| outbox orders | adopter-side orders graded by `govkit check` | runs in the adopter only | `govkit.py:5398-5412` |
| LIVE.md dormancy | builds labelled active or dormant | 21 of 25 dormant | `gen_build_index.py:1797` |
| maintenance or Loop Review record | none exists | 0 tracked | `git ls-files \| grep -ci 'maintenance\|loop-review'` gives 0 |

```text
$ python tools/drift-audit/drift_report.py --json | (tabulate)
signals 27 nonzero 15 gateable 7 pinned 22
$ python tools/runlog/runlog.py journal --producer gates --by-leg --legs tools/gate-legs.json
runlog: by-leg window 2026-09-14T05:59:59Z .. 2026-10-16T11:59:06Z bars=78 red_bars=45
legs 140 ever red 54 never red 86 always_run never red 39
```

**Where the records and the code disagree:**
- **`remote_ci_red_streak`.** The research calls it a signal that "cannot move" and the one meant to watch remote CI's reds (`research-maintain.md:69-73`). In the code it shells to `gh`, which is not on this node's PATH (`drift_report.py:3333-3341`; `command -v gh` gives "no gh on PATH"). It is also skipped by construction under `--check` (`:3387-3389`). The core already watches default-branch red through `refs/gov/bar-red`.
- **Dossiers.** The research measured 28 over pin 26. Today it is 25, `ok (pin 26, drain it)`.

## 3. Attach points

| Attach point | Declared in | What observability does there | What the core does without it |
|---|---|---|---|
| journal readers | runtime `[extend]` (`layer-runtime.md:746`) | registers `runlog` (the run record) and the reading store | journal still written (`policy-and-journal`, `:767`); no run record |
| command adapters | `[extend]` `:739` | each detector and fix is a command with a witness contract and an idempotence probe | none registered |
| hook packs | `[extend]` `:742` | the card's `drift —` cell, and session-start breach detection | the cell renders not installed |
| host adapters (via `maintain.host`) | `[schedule]` `:690-701` | session-start, os-scheduler; cloud-routine through integrations | scheduler runs only core cadence items (lease and claim sweeps, held bar, `:690-692`) |
| period lease | `[schedule]` `:702-705` | `maintain/<period>` and `loop/<week>` instances | none taken |
| Plan's triage intake (asks through `record`) | flow `[maintain]` entry table (`flow.md:620-628`) | keyed asks | asks come from requests only (P6) |
| patch build at Design | `flow.md:626` | opened by `maintain.patch` | patch builds come from requests only |
| owner-gate breakpoint | flow `[review]` (`flow.md:681`) | ratifies Loop Review proposals | none |
| stage review item 7, "cost written to the value ledger" | `flow.md:675` | an optional slot; the ledger is derived from review records | the review record keeps its cost, and the slot renders not installed |
| `refs/gov/bar-red` | Flow's post-merge verdict (`post-merge.sh:12-14`) | read as the `default-branch-red` event | pre-push still refuses on it (`pre-push:1909-1933`) |

**Attach points the layer needs that no core layer declares:**
- **A cadence-step point.** `[schedule]` runs "the cadence items that their layers declare" (`:690`), but none of the nine `[extend]` points (`:736-746`) is where a cadence step with a period key registers. Flow may declare one in its step model; that record was outside what I was allowed to read.
- **A home for period-keyed records.** HYGIENE's structure has none (`HYGIENE.md:17-35`; `project/` holds waiver registries "and nothing else", `:29`).

## 4. Candidates

**A. Detectors bind on the bar.** Every detector becomes a gate leg, so its pin reds `--check`. This extends the research's candidate B.
- *Losing test:* count the detectors whose value is not a function of the committed tree. A bar that reads them gives a verdict that depends on which node ran it, which breaks P2.
- *Result:* **loses** for 9 detectors.
  - 4 drift signals read node or network state. `dangling_pointers` is "node-scoped ON PURPOSE … never gates" (`drift_report.py:964-970`). `legs_retried_after_timeout` reads run records in the git dirs (`:3123-3133`). `fleet_over_budget` does the same (`:3240-3251`). `remote_ci_red_streak` calls `gh` (`:3381-3389`).
  - Process census, branch-reconcile, the health log, adopter currency and outbox orders are node-local or another repo's.
- *What survives:* the 7 gateable signals, which are already Test gates.

**B. A detector register, read by Maintain's cadence items, with readings committed in the maintenance record.** (Pick.)
- *Losing test 1:* run an owner rule over the real detector list. Any detector left with zero or two owners loses.
- *Result 1:* 44 detectors (§7 of the request lists them; 27 drift signals plus 17 others). Under "the owner is the layer whose rows must change for the reading to fall", 5 are ambiguous: `handkept_inventories`, `open_asks_cited_by_product_source`, `legs_retried_after_timeout`, `remote_ci_red_streak` and check-wiring. Two more fields resolve all 5, leaving 0:
  - *writer tie-break:* the owner is the layer that declares the kind holding the offending row;
  - *source:* a dead probe files to the layer that feeds the detector its input.
- *Losing test 2:* do node-scoped detectors under a single period lease see every node?
- *Result 2:* the first form **lost**. 6 detectors are node-scoped (the 3 above plus process census, branch-reconcile and the health log), and `fleet.toml` declares 4 nodes:
  ```text
  $ grep -c '^\[\[node\]\]' tools/playbook/fleet.toml
  4
  ```
  The pick therefore carries a `scope` field (`repo`, `node` or `outside`), and node-scoped detectors run under a `(period, node)` lease.

**C. A node-local store as a journal reader.** The Loop Review reads time series kept under `<common-dir>`.
- *Losing test:* does one node's store see the loop?
- *Result:* **loses.**
  ```text
  first-parent landings on origin/main since 2026-09-14: 361
  gates.log bars on this node: 78 · pushes.log end lines: 131 · drift-history readings: 32
  ```
  This is the same reason the research's value-ledger candidate lost (`research-maintain.md:125-127`).

**D. Observability hosted on CI.** A scheduled workflow runs the detectors and publishes artifacts.
- *Losing test:* can it perform Maintain's direct actions?
- *Result:* **loses** as the mechanism. Both direct actions are node-local: reap acts on this node's processes, and prune on 51 MERGED local refs and worktrees. The CI job is read-only and only uploads (`remote-ci.yml:116-125`). It survives as the host value `maintain.host=cloud-routine` for repo-scoped detectors.

## 5. The contract, filled

| Field | Observability's entry |
|---|---|
| tag and definition | `layer.observability`: signals about the loop and the runtime, read as keyed readings against a register, and the cadence steps that act on them, Maintain and the Loop Review |
| instruction units | the Maintain step program; the Loop Review program; one level-scoped rule: "a reading files work, it never decides a position" |
| engine kits | drift-audit (the register's engine; `drift-history.tsv` becomes a cache); runlog's reader half (run record, `--by-leg`; its grammar moves to Runtime); the Loop Review (in dCalibratedLens); adapters wrapping process-monitor `reap.py`, branch-reconcile, codebase-map's regenerate and govkit census |
| record kinds | `maintenance` (per period or event); `loop-review` (per period, carrying the derived value ledger); `run-record` (runlog's, moved from runlog into this layer); `reading` (a section of the maintenance record, never its own file) |
| extension points declared | `detectors`: one register entry per detector, which any layer or expansion may add (distribution adds currency and outbox; integrations adds remote CI) |
| extension points used | journal readers, command adapters, hook packs, host adapters (Runtime); period lease (`[schedule]`); triage intake and the patch build at Design, breakpoints (Flow); `record` (Memory) |
| policies | `maintain.*`, `review.loop.*`, the new keys in §6, and a value for `runtime.journal` |
| gates | the `drift-audit records` leg keeps only repo-scope gateable signals; a register leg reds an entry without owner, pin, scope or liveness; the `runlog record schema` leg |

**Register entry:** `id`, `layer` (the owner), `stage`, `source` (the layer feeding its input), `scope` (repo, node or outside), `pin` and `kind` (pin, baseline or ratchet), `gateable`, `liveness` (its assertion), `events` (which events carry it), `fix` (a name in `maintain.fixes`, or none), `offender-key` (the spelling from `drift_report.py:3733`).

**Owner rule:**
1. The owner is the layer that declares the record kind whose rows the reading counts.
2. On a tie, the owner is the layer that wrote the offending row.
3. A dead probe goes to `source`.

## 6. Items and policies

**Maintain**

| Tag | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `maintain.lease` | executor | takes `maintain/<ISO date>`, or `maintain/<event>/<key>`, plus `(period, node)` for node-scope | lease record via `record`, absent a closed one for the key | held → read; already run → done; held elsewhere → skip |
| `maintain.read` | command (each register entry) | runs the period's entries, or the event's subset | readings section: id, value, pin, liveness, base sha | breach / ok / dead |
| `maintain.reap` | command `reap.py --sweep` | kills flagged trees (no tracked change) | reap's read-back, recorded | done |
| `maintain.prune` | command branch-reconcile on MERGED only | prunes landed refs and worktrees | a re-run shows 0 MERGED | done |
| `maintain.patch` | command | a breach whose `fix` changes tracked content opens a patch build at Design, intake rendered from the reading | intake keyed `hash(detector, offender keys)` | Design (`patch.ratify`) |
| `maintain.file` | command | any other breach, or a dead probe, becomes an ask for the owner (or the source), with a severity and the acceptance "reading under pin" | ask with the same key; a recurrence never files twice | Plan triage, per `maintain.on-breach` |
| `maintain.held` | command | runs the test levels and held legs policy assigns here | verdict record | red → `maintain.file` |
| `maintain.release` | command (distribution's adapter) | cuts the tag and notes when `release.cadence` is due | tag on main | verify fails → event |
| `maintain.record` | command `record` | writes the maintenance record (checked, fixed, filed) | the record at the period key | lease release |

**Event runs**

| Event | Source (a core witness) | Detectors carried | Fixes |
|---|---|---|---|
| default-branch-red | `refs/gov/bar-red` | gate verdict, hygiene on main | none; ask or patch build |
| release-verify-failed | Deploy's verify record | currency, outbox | none; ask to Plan triage |
| session-start-breach | the card's cells | the breached entry only | its declared fix |

**Loop Review**

| Tag | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `loop.lease` | executor | takes `loop/<ISO week>` | lease | gather |
| `loop.gather` | command | reads metrics from committed sources: cycle times (transitions), review yield (`reviews/`, 530 files), catches (verdict records), cost (`ceiling-evidence.txt`, 119 rows), flakes and bypasses (maintenance records), plan revisions, records overhead and surface size (git) | metrics section, every value sourced | price |
| `loop.price` | command | renders the value ledger: `kind`, `id`, `layer`, `born`, `cost`, `catches`, `last-catch`, `window`, `state` | derived table plus a JSON twin | propose |
| `loop.propose` | role | drafts retirements, merges, cap re-derivations and contract changes from the ledger | proposals list | file |
| `loop.file` | command, then the owner breakpoint | asks into Plan, ratified as `review.loop.retire` says | an ask per proposal | Plan |
| `loop.record` | `record` | writes the Loop Review record | the record | done |

**Policy keys**

| Key | Allowed values | Default | Why |
|---|---|---|---|
| `runtime.journal` | registered journal-reader names | `runlog` when installed, else none | a selector over registered names, as `[extend]` requires (`:748`) |
| `maintain.node-detectors` | every-node, lease-holder | every-node | 6 node-scoped detectors, 4 nodes |
| `maintain.record` | every-period, on-finding | on-finding | `gap-maint-04`: a zero-finding period leaves only its lease witness |
| `review.loop.catch-source` | verdict-records, journal-digest | verdict-records | the journal is node-local (78 of 361) |

## 7. Gaps

**Closed by the pick:**
- `gap-maint-01`: cadence items, with Runtime's host and lease.
- `gap-maint-02`: register entries carry an owner and a pin, and dead probes route to their source.
- `gap-maint-05`: the close-run-record and defer-dormant fixes become patch builds.
- `gap-maint-06`: the regenerate-stale fix.
- `gap-maint-07`: reap runs directly, and ratchets and retries file asks.
- `gap-maint-08`: both readings get owners and pins.
- `gap-maint-03`: designed here, but it stays dCalibratedLens's and is blocked on `gap-obs-01`.
- `gap-maint-04`: not closed; `maintain.record=on-finding` keeps it from growing.

**Exposed:**

| New gap | Evidence |
|---|---|
| `gap-obs-01`: no committed catch history | gate reds exist only in node-local `gates.log` (78 bars against 361 landings); 0 of 129 gotchas carry a catch field (`grep` gives 2 body mentions, no front matter) |
| `gap-obs-02`: no home for period-keyed records | `HYGIENE.md:17-35,29` |
| `gap-obs-03`: no cadence-step extension point | `layer-runtime.md:690` against `:736-746` |
| `gap-obs-04`: the remote-CI signal is an integration that is absent here, and is skipped under `--check` | `drift_report.py:3333-3341,3387-3389`; the core watcher is `refs/gov/bar-red` (`pre-push:1909-1933`) |
| `gap-obs-05`: register fields are missing | no owner, scope or source field (`drift_signals.py:243` PINS only); 51 MERGED refs waiting on a manual prune |

## 8. Forks

1. **Where period records live.**
   - (a) a new `memory/observe/{maintain,loop}/` tree;
   - (b) a standing `builds/maintain/` folder, which breaks "a build closes at landing";
   - (c) refs only.

   *Recommend (a).*
2. **Where catches come from.**
   - (a) Flow's verdict records name the failed legs, a core change in Test;
   - (b) each node publishes a journal digest.

   *Recommend (a).*
3. **Who runs node-scoped detectors.** Every node under its own lease, or the lease holder only. *Recommend every node.*
4. **The gateable drift signals.** Move the 7 to Test as core gate legs, leaving observability only readings, or keep them in the kit. *Recommend moving them.*
5. **A zero-finding period.** Write a maintenance record, or leave the lease witness only. *Recommend the lease witness only.*

**Files read or measured:**
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-research-maintain.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/drift-audit/drift_report.py`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/runlog/README.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/run-gates/post-merge.sh`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/.githooks/pre-push`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/HYGIENE.md`
