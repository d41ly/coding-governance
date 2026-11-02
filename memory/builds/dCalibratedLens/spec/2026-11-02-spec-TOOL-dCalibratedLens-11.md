# TOOL-dCalibratedLens-11 — the Loop Review's delivery metrics and the owner queue's depth, read with no bound

**Status:** OPEN · rev-1 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 13 · advances TOOL-dCalibratedLens-18

**Carries:** cl-dClosedLoop-0468@8f541e2a whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-11-deviation-111.md](../build/2026-11-02-build-TOOL-dCalibratedLens-11-deviation-111.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |

<!-- /gen:spec-records -->

## 1. Goal

Give the Loop Review the delivery metrics the night pass named (`2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`
`[p6-sdlc]` S4): lead time, landing frequency, change failure rate, time to restore, first-pass verdict
rate, route-backs per build and scope drift, and the owner queue's depth, read with no bound (NP-18,
"Measure first"). Today the Loop Review names no delivery metric (gap-review-15) and no reading
measures the owner queue's depth, so parallel work cannot be weighed against the owner's capacity to
review it (gap-review-16). Each metric becomes one field of the `loop-review` record, derived at each
review from records every node can read.

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `8bec4cef`: TOOL-dCalibratedLens-3 (the module
`tools/loop/loop_review.py`, its `METRICS` table read by `measure_loop_metrics` in `gather`, the
`record` verb, the `loop-review` record and the window `derive_loop_window` returns under
`review.loop.window-days`), DEPL-dShippedRelease-1 (the landing record and `read_landing`),
DEPL-dShippedRelease-13 (its `core` field), DEPL-dShippedRelease-15 (the release exit record),
TOOL-dWellOiledMachine-48 (`tools/runtime/owner_items.py`), TOOL-dRankedPlan-13 and -16 (the plan record
and `tools/memory-tree/plan_fields.py`). The build run re-grounds on each and stops the unit when one is
absent.

- **S1** — The eight fields, appended to TOOL-dCalibratedLens-3 S5's `METRICS` as eight `(name, reader)`
  entries in this order, the names held in `DELIVERY_FIELDS`: `lead-time`, `landing-frequency`,
  `change-failure-rate`, `time-to-restore`, `first-pass-verdict-rate`, `route-backs-per-build`,
  `scope-drift` and `owner-queue-depth`. Each reader answers `(value, source)` over the window
  `derive_loop_window` returns: the eight share one `read_delivery_inputs(root, window)` call per walk,
  held for the walk, and each takes its value from `derive_delivery_metrics(inputs, window)`, a pure
  function returning the eight values of §4 "The values". The `record` verb writes each as the record's
  Metrics line `<name>: <value> · <source>` (TOOL-dCalibratedLens-3 §4). Observed by AC1 to AC8.
- **S2** — The landings. `read_delivery_inputs` lists the landing records with one bounded `git ls-remote
  origin 'refs/gov/landing/*'` and reads each through `read_landing(sha, root)` (DEPL-dShippedRelease-1
  S4, the same kit), keeping the landings whose landing commit's committer time falls inside the
  window. From them it derives `lead-time`, `landing-frequency`, `change-failure-rate` and
  `time-to-restore` (§4). Observed by AC1 to AC4 and AC9.
- **S3** — The release exits, for `change-failure-rate`: one bounded `git ls-remote origin
  'refs/gov/release-exit/*'`, and for each windowed landing it lists, the exit record's `outcome` read
  through the integrations kit's exit reader as a subprocess (§8 F3). Observed by AC3.
- **S4** — The review rounds. A verb `python tools/runlog/runlog.py rounds [--since <utc>]` prints one
  JSON line per committed run record under `<MEMORY_ROOT>/builds/*/build/` whose window closes at or
  after `<utc>`: its slug, its runkey, its `merged` and `terminal` facts and its `rounds` rows, each read
  through `parse_record` (`tools/runlog/record.py:1242`) and never re-parsed. From those lines the
  Loop Review derives `first-pass-verdict-rate` and `route-backs-per-build` (§4). Observed by AC5, AC6
  and AC10.
- **S5** — Scope drift. A verb `python tools/memory-tree/plan_fields.py drift <slug> --paths <file>` reads
  the build's plan record through `find_plan_record` and `read_plan_fields` (TOOL-dRankedPlan-16 S4),
  maps each listed path to its system through `derive_affected_systems` (TOOL-dRankedPlan-13 S3, its
  degraded floor included), and prints one `drift — <system>` line per system the paths reach that the
  plan's `Affected systems` lacks, or `drift — none`; no plan record prints `drift — unplanned` and exits
  1. The Loop Review hands it each windowed landing's landed paths (§4). Observed by AC7.
- **S6** — The owner queue's depth. A verb `python tools/runtime/owner_items.py depth` prints `owner queue
  — <n> open`, `<n>` the count of open owner items, read through `read_open_owner_items(repo)`, the one
  reader that `decide_owner_items` (TOOL-dWellOiledMachine-48 S4) and this verb share, extracted from
  `decide`'s walk. No policy key is read and no threshold is compared: the depth is reported, never
  bounded (NP-18). Observed by AC8.
- **S7** — An empty population and a dead source are never a zero (§4 "The states"). Observed by AC9.
- **S8** — The docs: `help/loop-review.md` (TOOL-dCalibratedLens-3 S11's page) gains a "Delivery
  metrics" section naming each field, its source and its value grammar, and why the queue depth has no
  bound; `tools/runlog/README.md` names `rounds`; `tools/loop/README.md` names the fields. NOT OBSERVED
  by a criterion: prose, read by the closing review.

## 3. Non-goals (OUT)

- A bound on parallel work by the owner queue's depth. NP-18 chose "Measure first", and v2 names a new
  key, `runtime.owner-queue`, only on a bound (`2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:538`).
  No key, no warning and no refusal is added.
- The Loop Review's module, its verbs, its record kind, its lease and its window: TOOL-dCalibratedLens-3.
  This unit adds fields and one gather step to them.
- Trending a metric across reviews, or proposing anything from one. Each record keeps its snapshot;
  no unit of this build's clauses proposes from a delivery metric.
- Pricing anything in the value ledger: units 2, 7, 9, 12 and 15.
- Writing a landing, a release exit, a run record, a plan record or an owner item: each is its own
  kit's, read here only.
- Lead time measured from the intake record (§8 F1).

### Edges

- **consumes-from** `TOOL-dCalibratedLens-3` — `METRICS`, which these eight entries join, `derive_loop_window`, the `record` verb and the `loop-review` record; without them the fields have no reader, no window and no record
- **consumes-from** external — DEPL-dShippedRelease-1 S4 (`read_landing`), -13 (`core`), -15 (the release exit record), TOOL-dWellOiledMachine-48 S4 (`decide_owner_items`), TOOL-dRankedPlan-13 S3 and -16 S4 (`plan_fields.py`, the plan record), each specced and unbuilt at base `8bec4cef` and of an ancestor build

## 4. Design

### The values

Every value is DERIVED at the review from records committed or advertised on the remote. Nothing is
pinned and nothing is typed. A duration is whole hours, `<n>h`; a share is a whole percent, `<p>%`; a
rate is one decimal.

| Field | Value | Population | How |
|---|---|---|---|
| `lead-time` | `median <n>h · of <k>` | each (landing, build) pair, a build named in the landing's `builds` field | the landing commit's committer time less the committer time of the first commit adding `<MEMORY_ROOT>/builds/<slug>/README.md` |
| `landing-frequency` | `<x.y>/week · of <k>` | the windowed landings | `k` divided by the window's length in weeks |
| `change-failure-rate` | `<p>% · of <k>` | the windowed landings whose `core` is `green` or `red` | a failure is `core: red` (DEPL-dShippedRelease-13), or a release exit whose `outcome` is `rolled-back`, `rolled-forward`, `halted` or `unverified` (DEPL-dShippedRelease-15's outcome set; `verified` and `held` are not failures) |
| `time-to-restore` | `median <n>h · open <j> · of <k>` | the windowed failures | the next landing whose `core` is `green`, its committer time less the failure's; `open` counts a failure no later green follows |
| `first-pass-verdict-rate` | `<p>% · of <k>` | the review loops of the windowed merged runs | a loop's first round's verdict is `CLEAN` |
| `route-backs-per-build` | `<x.y> · of <k>` | the distinct builds of the windowed merged runs | the rounds beyond the first in each loop, summed, divided by `k` |
| `scope-drift` | `<p>% · of <k> · unplanned <u>` | the windowed (landing, build) pairs whose build has a plan record | a pair drifts when `plan_fields.py drift` prints a system; `unplanned` counts pairs with no plan record |
| `owner-queue-depth` | `<n>` | the open owner items at the review | `owner_items.py depth` |

The median is the upper median, `sorted(v)[len(v) // 2]`, so a value is always an observed one.
Each value and its source make one Metrics line: `lead-time: median 30h · of 3 · refs/gov/landing/*`.

**A review loop**, read from a run record's `rounds` rows in their order: a loop ends at a row whose
`exit` is one of `REVIEW_EXITS` (`tools/runlog/model.py:110`), and a trailing run of rows with no exit is
one open loop. A record whose rounds were aggregated (`rounds-by-verdict`, `tools/runlog/record.py:295`)
keeps no order: its rounds count toward `route-backs-per-build` as its total less the rows that carry
an exit, and it is left out of `first-pass-verdict-rate`'s population.

**The landed paths** of a landing are `git diff --name-only <sha>^1 <sha>`, its first-parent diff, less
every path under `<MEMORY_ROOT>/`: a records path is no system, and every build's records would read as
drift otherwise.

### The states

| State | When | Value |
|---|---|---|
| empty | the population is empty | `searched-none`, its source the ref pattern or glob searched (TOOL-dCalibratedLens-3 S5) |
| unread | a source could not be read: a failed `ls-remote` or fetch, a reader's exit 2, an absent kit | `unread · <reason>` |

An `ls-remote` answering no ref is empty; one that fails is unread. `read_landing`'s exit 2 is a dead
probe and unreads every landing field, never one landing dropped. An absent integrations kit unreads no
field: `change-failure-rate` then counts `core` alone and its value carries ` · release-exit not
installed`.

### The reads

```
gather
  read_delivery_inputs(root, window)
    git ls-remote origin 'refs/gov/landing/*'      -> read_landing(sha, root) per sha   (S2)
    git ls-remote origin 'refs/gov/release-exit/*' -> the exit reader per listed sha    (S3)
    git log --no-walk --format='%H %ct' <shas>     # one call for every committer time
    python <runlog kit>/runlog.py rounds --since <window start>                         (S4)
    python <memory-tree kit>/plan_fields.py drift <slug> --paths <file> per pair        (S5)
    python <runtime kit>/owner_items.py depth                                           (S6)
  derive_delivery_metrics(inputs, window)  -> the eight values                           (S1)
record -> the loop-review record
```

A kit imports no sibling kit (TOOL-dGroundRules-1 §4), so each foreign verb runs as a bounded subprocess
(30 s) found through the inline `resolve_kit_dir` block (`tools/lib/resolve_kit_dir.py`'s canonical
copy), as TOOL-dTendedCadence-6 S1 reads its key. `read_landing` is the loop kit's own and is imported.

### Inventory

Minted: the constant `DELIVERY_FIELDS` and the functions `read_delivery_inputs` and
`derive_delivery_metrics` (`tools/loop/loop_review.py`); the verb `rounds` and its function
`read_run_rounds` (`tools/runlog/runlog.py`, `tools/runlog/record.py`); the verb `drift`
(`tools/memory-tree/plan_fields.py`); the verb `depth` and the function `read_open_owner_items`
(`tools/runtime/owner_items.py`); the eight field names. Each function was answered OK by
`python tools/lexicon/lexicon.py --suggest <name> --as py.function` at this base.

### Migration

None. A `loop-review` record written before this unit carries none of the eight fields, and nothing
reads one back.

### Files touched (estimate)

- `tools/loop/loop_review.py` (S1, S2, S3, S7)
- `tools/runlog/runlog.py` (S4, the `rounds` verb)
- `tools/runlog/record.py` (S4, `read_run_rounds`)
- `tools/runlog/selftest.py` (the arm in §7)
- `tools/runlog/README.md` (S8)
- `tools/memory-tree/plan_fields.py` (S5)
- `tools/runtime/owner_items.py` (S6)
- `tools/loop/README.md` (S8)
- `help/loop-review.md` (S8)

## 5. Production-readiness checklist

- security — no write path is added: every new verb reads, and the `loop-review` record's writer is
  unit 3's. The `--paths` file of `drift` is read as data, one repository-relative path per line,
  each refused when absolute or carrying a `..` segment, as TOOL-dRankedPlan-13 S2 refuses a scope path.
- perf / scale — two `ls-remote` calls, one `git log` and one `rounds` call per review, plus one
  `read_landing` fetch and one `drift` subprocess per windowed landing; a 60-day window held about
  fifty landings at this base's rate, measured nowhere yet (PINNED estimate, 2026-11-02, from the
  landing records' absence: re-derive at the first review).
- error / empty / loading states — §4 "The states": an empty population and a dead source each have
  their own line, and neither reads as a zero.
- observability — each field is one line of a committed record, so a reader on any node sees the same
  values.
- risks — `route-backs-per-build` counts review rounds only; a fix-pass loop's rounds reach it only where
  they are recorded as review rows (TOOL-dDeclaredLoop-32's bound counts both). `lead-time` starts at the
  build's opening commit, not at the request (§8 F1).
- testing — each criterion is a probe or a fixture of this unit's code; the arms in §7 are observed RED
  then GREEN by the main loop at the close.
- migration — §4 "Migration".
- user docs — `help/loop-review.md`, S8.

## 6. Acceptance criteria

The fixture is TOOL-dCalibratedLens-3's (its S12), `python tools/loop/loop_review.py --fixture --plant <case>`: a
scratch repository and a bare remote under `%TEMP%` with short names, holding planted landing refs
written with `render_landing_body` (DEPL-dShippedRelease-1 S1), release exits, run records, plan records
and owner items. This unit adds the cases each criterion names; "the record carries" means the record holds the Metrics
line opening with the quoted text.

- **AC1** — When `loop_review.py --fixture --plant delivery-lead` plants three builds, each opened at
  hour 0 and landed at hours 10, 30 and 50, the record carries `lead-time: median 30h · of 3`.
  Red when: the lead is measured from another commit, or a pair is dropped.
  figure: DERIVED from the planted committer times.
- **AC2** — When `--plant delivery-frequency` plants three landings inside a 14-day window and one outside
  it, the record carries `landing-frequency: 1.5/week · of 3`.
  Red when: the window from `review.loop.window-days` is not applied, so four landings count.
- **AC3** — When `--plant delivery-failure` plants four landings whose `core` is `green`, `red`, `green`
  and `pending`, and a release exit `rolled-back` on the second `green`, the record carries
  `change-failure-rate: 67% · of 3`; with the integrations kit removed from the fixture, it carries
  `change-failure-rate: 33% · of 3 · release-exit not installed`.
  Red when: a `pending` landing counts, or a failed release exit is not a failure.
- **AC4** — When `--plant delivery-restore` plants a `red` landing at hour 0, a `green` at hour 6 and a
  second `red` at hour 9 with no later landing, the record carries `time-to-restore: median 6h · open 1 ·
  of 2`.
  Red when: an unrestored failure is dropped or counted as a zero.
- **AC5** — When `--plant delivery-first-pass` plants two merged run records whose `rounds` rows are
  `CLEAN · CONVERGED` and `BLOCKED`, `CLEAN · CONVERGED`, the record carries `first-pass-verdict-rate:
  50% · of 2`.
  Red when: the rate is read over rounds instead of loops.
- **AC6** — When the same plant runs, the record carries `route-backs-per-build: 0.5 · of 2`; with a third
  record whose rounds are aggregated as `rounds-by-verdict` with three rounds and one exit, it carries
  `route-backs-per-build: 1.0 · of 3` and `first-pass-verdict-rate` keeps `of 2`.
  Red when: an aggregated record is dropped from route-backs, or read for first pass.
- **AC7** — When `--plant delivery-drift` plants a plan record whose `Affected systems` is `runlog` and a
  landing whose first-parent diff touches `tools/runlog/model.py`, `tools/loop/loop_review.py` and
  `memory/builds/x/README.md`, `python plan_fields.py drift x --paths <file>` prints `drift — loop` alone,
  and the record carries `scope-drift: 100% · of 1 · unplanned 0`; with a second landing of a build with
  no plan record, `unplanned 1`.
  Red when: a records path reads as drift, or an unplanned build counts as drifted.
- **AC8** — When `--plant delivery-depth` posts three owner items and answers one, `python owner_items.py
  depth` prints `owner queue — 2 open` and the record carries `owner-queue-depth: 2`; with 500 open items
  planted, it prints `owner queue — 500 open`, exits 0 and prints no other line.
  Red when: any bound, key or warning is read or printed for the depth.
- **AC9** — When `--plant delivery-dead` points the fixture's remote at a missing path, the record carries
  `landing-frequency: unread · ls-remote failed` and the three other landing fields unread; with the
  remote holding no landing ref, it carries `landing-frequency: searched-none`.
  Red when: a dead source reads as an empty one, or either reads as a zero.
- **AC10** — When `python tools/runlog/runlog.py rounds` runs over this tree, it exits 0 and prints one
  JSON line per tracked file matching `memory/builds/*/build/*-runlog-*.md`, each carrying `slug`,
  `runkey`, `merged`, `terminal` and `rounds`; with one such record's Data block truncated in a scratch
  copy, it exits 2 naming that record.
  Red when: a record is skipped silently, or a malformed one reads as having no rounds.
  figure: DERIVED, the count of tracked run records at the run (26 at `22a8efac3`).

## 7. Gates

`runlog selftest` · `runlog record schema` · `pre-push run-log line` · `run-gates run-log line` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop kit's leg, `loop-review selftest` (TOOL-dCalibratedLens-2's), and the runtime kit's legs are not
in the manifest at base; their arms are declared below and graded once those kits land.

New arm: tools/loop/loop_review.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 · the fixture's `delivery-*` cases, each planting one source, and the dead-remote case · none
New arm: tools/runlog/selftest.py · covers AC10 · a scratch copy of a committed run record with its Data block truncated · none

## 8. Open questions

- **F1 — Where does lead time start?** The night pass says "from intake to landing" (S4). Options: (a) the
  intake record (TOOL-dWellOiledMachine-4), homed at `<git-common-dir>/requests/*`, node-local; (b) the
  build's opening commit, the first commit adding its README, in git on every node; (c) the run's start
  commit (`derive_run_starts`, `tools/runlog/model.py:320`). (a) reads nothing on any node but the one
  that took the request, the reason v2:1345 gives `review.loop.catch-source` its default; (c) misses the
  spec run and every hand-over before the build run. RESOLVED (agent, 2026-11-02, delegated): (b), rung
  3, the most feature-rich survivor every node can read; the departure is
  `2026-11-02-build-TOOL-dCalibratedLens-11-deviation-111.md`. widens: none · relaxes: none
- **F2 — The brief names `build_run_model` and the run record as the source; which is read?** Options:
  (a) `runlog.py model` per run, which joins the node-local journals and transcripts; (b) the committed
  run record's Data block through `parse_record`, which every node holds. (a) answers differently on
  each node and costs a full model per run. RESOLVED (agent, 2026-11-02, delegated): (b), rung 3, the
  record being the model's committed rendering (`tools/runlog/record.py:3-6`). widens: none · relaxes:
  none
- **F3 — What reads a release exit's `outcome`?** DEPL-dShippedRelease-15 names `release.py read` for
  the release record and no reader verb for the exit record. Options: (a) the integrations kit's exit
  reader as a subprocess, the build run grounding on the verb that unit lands, and where none exists
  the build files the ask "dShippedRelease: a reader verb for `refs/gov/release-exit/<sha>`, printing
  its four keys" in `memory/builds/dShippedRelease/BACKLOG.md` while the field reads `core` alone and
  says `release-exit unread`; (b) a parser of the exit record's body in the loop kit. (b) is a second
  parser of a record its kit owns. RESOLVED (agent, 2026-11-02, delegated): (a), rung 3. widens: none ·
  relaxes: none
- **F4 — The brief's PRIMITIVE GAP: change failure rate and time to restore name no source record.**
  Options: (a) the landing record's `core` field (DEPL-dShippedRelease-13) and the release exit record,
  which are the night pass's "a default-branch red or a failed release verify"; (b) the bar's verdict
  lines in the node-local gates journal. RESOLVED (agent, 2026-11-02, delegated): (a), rung 1: the night
  pass's own definition, and both records are on the remote. widens: none · relaxes: none
- **F5 — The brief's PRIMITIVE GAP: no reading of the owner queue's depth.** Options: (a) a `depth` verb
  on `owner_items.py` sharing one reader with `decide_owner_items`; (b) the Loop Review reading the
  mailbox itself through `unattended.sh --mail read project`; (c) an ask to dWellOiledMachine. (b) is a
  second spelling of which mailbox row is an owner item; (c) leaves the field unread until another build
  acts. RESOLVED (agent, 2026-11-02, delegated): (a), rung 3, the one-fact reading. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, from the packet's Items 11 (`cl-dClosedLoop-0468@8f541e2a`), the
  night pass's `[p6-sdlc]` S4 and NP-18 (`night-pass.md:340-411`, `:538`, `:668`), the brief's S3 and S4,
  and runlog, the landing record (DEPL-dShippedRelease-1, -13, -15), the owner items
  (TOOL-dWellOiledMachine-48) and the plan record (TOOL-dRankedPlan-13, -16) read at base `8bec4cef`.

## 10. Reuse audit

The seams extended are the run record's reader `parse_record` (`tools/runlog/record.py:1242`) and the
runlog CLI beside `check-records` (`tools/runlog/runlog.py:475`, `:543`); the landing reader
`read_landing` (DEPL-dShippedRelease-1 S4); the owner items' walk in `decide_owner_items`
(TOOL-dWellOiledMachine-48 S4), whose reader this unit extracts; and `derive_affected_systems`
(TOOL-dRankedPlan-13 S3), so the drift's kit rule is the plan field's own. `python
tools/codebase-map/reuse_lookup.py "measure delivery metrics lead time landing frequency change failure
rate from landing records"` ranked name stems (`records`, `changed`, `leading_verb`) and runlog's
`render_record` and `write_record`; it named no delivery metric and no reader of landings, and none
exists at base. Where the brief and source disagree: the brief says change failure rate and time to
restore name no source record, and DEPL-dShippedRelease-13's `core` field and DEPL-dShippedRelease-15's
release exit are those sources (§8 F4); the brief names `build_run_model`, whose journals are node-local,
where the committed record serves every node (§8 F2). The scout's `tools/runlog/model.py` pointer agrees
with source (`build_run_model` at `:1558`).

Recall terms used: `python tools/memory-recall/query.py "how does the Loop Review read delivery metrics such as lead time, change failure rate and the owner queue depth" --terms "loop review delivery metrics lead time landing frequency change failure rate time to restore owner queue depth landing record"`

### Alternatives rejected

- **Lead time from the intake record** (F1 a). Rejected by reading TOOL-dWellOiledMachine-4's home,
  `<git-common-dir>/requests/*`: no other node holds it.
- **Re-joining each run's model** (F2 a). Rejected by reading `build_run_model`'s docstring
  (`tools/runlog/model.py:12-16`): a missing journal is a coverage state, so a second node's model of the
  same run differs.
- **First-pass read from review records' `## Verdict:` line.** Rejected by reading the review records'
  binding lines: a diff-review record carries its round only in prose or its file name, while the run
  record's `rounds` rows carry each round's verdict and exit in order.
