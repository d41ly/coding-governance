# TOOL-dTendedCadence-3 — the safe-fix set: `maintain.fixes` read as a literal set, each fix routed direct, patch or owner-gated, and `maintain.direct` reaping and pruning

**Status:** DEFERRED · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 9 · advances TOOL-dTendedCadence-19 · closes TOOL-dTendedCadence-20

**Carries:** cl-dClosedLoop-0444@f4079d73 whole
**Carries:** node:policy-key.maintain.fixes
**Carries:** node:item.maintain.direct

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-build-TOOL-dTendedCadence-1-reuse-scout-a.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-reuse-scout-a.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-6 TOOL-dTendedCadence-8 TOOL-dTendedCadence-10 |
| [2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-build-TOOL-dTendedCadence-3-deviation-31.md](../build/2026-11-01-build-TOOL-dTendedCadence-3-deviation-31.md) | deviation | — |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-1 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-2 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 |

<!-- /gen:spec-records -->

## 1. Goal

Reaping is manual and the cleanup's write mode is run by hand (gap-maint-07), run records for merged work stay open
and dormant builds are never deferred (gap-maint-05), and `maintain.fixes`, the key that names the safe fixes,
cannot be read at all: `policy.py get maintain.fixes` refuses its `{ derived = … }` default. This unit makes the key a
literal set, gives each of its six fixes its route, `direct` for the two that change no tracked content, `patch` for
the three that do, and the owner-gated proposal and disposal for `defer dormant`, and builds `maintain.direct`, the
item that applies a direct fix and files what survives it.

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `f4597719`: TOOL-dTendedCadence-1 (`maintain.py` and its
rows), TOOL-dTendedCadence-8 (the `[[reading]]` row and its `fix` field, and the I6 patch filer),
TOOL-dTendedCadence-15 (`run_breach_route`), TOOL-dTendedCadence-4 (`read_policy_value`); TOOL-dRankedPlan-4 S2 and S3
(`gen_build_index.py --dormant`, `loop_transition.py dispose`), on which ask TOOL-dTendedCadence-20 binds this unit.

- **S1** — The key. The catalogue row `maintain.fixes` (`tools/policy/catalogue.toml:1126-1130`) becomes
  `allowed = { type = "set", of = ["reap", "prune landed", "regenerate stale", "defer dormant", "records-only fixes",
  "close finished run records"], registry = "named safe fixes" }` with `empty = "allowed"`, its default the same six
  as a literal list, and gains `summary` and `usage = 'maintain.fixes = ["reap", "prune landed"]'`;
  `policy.py lists --write` takes the key out of `tools/policy/unsummarised-keys.txt`. `get` then prints the six,
  one per line, where it refuses today (`policy.py:696`). An empty set is the clause's "none": no fix applies. A
  member outside the six is refused by the reader (`check_value`, `policy.py:143-172`), so a fix the routes do not
  know never reaches a run. Observed by AC1 and AC2.
- **S2** — The routes, `FIX_ROUTES` in the new module `tools/drift-audit/maintain_fixes.py`, I11's table:

  | Fix | Route | Applied by |
  |---|---|---|
  | `reap` | `direct` | `python <process-monitor>/reap.py --sweep`, the mode `.process-monitor.conf` declares
  (`reap.py:427-443`) |
  | `prune landed` | `direct` | `python <branch-reconcile>/branch_reconcile.py --write`, never `--remote`
  (`branch_reconcile.py:1201-1205`) |
  | `regenerate stale` | `patch` | the patch intake, I6 |
  | `records-only fixes` | `patch` | the patch intake, I6 |
  | `close finished run records` | `patch` | the patch intake, I6 |
  | `defer dormant` | `owner-gated` | S6 |

  `read_fix_set(root)` reads the key through `read_policy_value("maintain.fixes", root)` (TOOL-dTendedCadence-4 S6),
  the key a literal; on `PolicyRefused` it takes the empty set and prints one `NOTE: maintain.fixes refused · <why> ·
  no fix applies` line, deny by default, never the catalogue's six. `derive_fix_route(reading,
  fix_set)` answers a reading's route: its `fix` (I3) when that fix is in
  the set, else `file`. Each sibling kit is found through the inline `resolve_kit_dir` block and run as a bounded
  subprocess, since a kit imports no sibling kit. Observed by AC2 and AC7.
- **S3** — The re-route in `tools/drift-audit/maintain.py`: `item.maintain.read`'s `act` outcome becomes four,
  `act-direct`, `act-patch`, `act-owner-gated` and `act-file`, by `derive_fix_route`, routed to
  `item.maintain.direct`, `item.maintain.patch`, `item.maintain.direct` and `item.maintain.file`; `diagnose` and
  `dead` still route to `item.maintain.file`. `tools/drift-audit/kit.toml` gains the seventh row,
  `item.maintain.direct`, actor `command:maintain.direct`, needs `item.maintain.read`, outcomes `fixed`, `survived`
  and `held`, `fixed` routed to `item.maintain.record` and `survived` and `held` to `item.maintain.file`, its witness
  "the next reading shows the set gone"; `item.maintain.file`'s needs gain `item.maintain.direct`. Observed by AC3,
  AC5 and AC7.
- **S4** — `maintain.direct`, `run_direct_fixes(root, key, readings, dry_run)`: for each reading routed to it, run its
  fix by S2's table, then take the reading again; an empty offender set is `fixed`, and each offender still standing
  is `survived` and handed to `run_breach_route` as a breach raised by `item.maintain.direct`. A fix exiting 2 or
  refused is `survived` with its first stderr line. `--dry-run` runs `reap.py --sweep --dry-run`, runs no
  `--write`, and prints what it would apply. Observed by AC3 and AC4.
- **S5** — The two readings the direct fixes act on, each a function returning drift-audit's reading dict (I4) and
  registered by a `[[reading]]` row in `tools/drift-audit/kit.toml` (TOOL-dTendedCadence-8 §4 "The row"),
  `scope = "node"`, its pin 0 and its band edges `0, 0` where TOOL-dTendedCadence-8 and -14 place them, so any
  offender reaches the act band: `measure_idle_processes(ctx)`, signal `idle_processes_past_ceiling`, its value the
  `targets` count of `reap.py --sweep --dry-run`'s summary line (`reap.py:413-416`), `fix = "reap"`; and
  `measure_landed_branches(ctx)`, signal `landed_branches_unpruned`, one offender per report row
  `branch_reconcile.py` prints with a verdict in the `--write` set of
  `branch_reconcile.py:49`, keyed by its kind and name,
  `fix = "prune landed"`. Neither row carries a `kind`, so TOOL-dTendedCadence-4 derives the owner `layer.runtime`
  for a node-scoped row, node state being Runtime's (layer-expansions:200-201). Both join `SIGNALS`
  (`tools/drift-audit/drift_report.py:3521`) by import from the same kit, report-only (`gateable` false), so
  `--readings` emits them and TOOL-dTendedCadence-8 S2's both-ways join of rows and emitted names holds. Being
  node-scoped, both are read by the node pass on every node
  (TOOL-dTendedCadence-16 S6), which this unit's §3 hands the `act-direct` route to. Observed by AC3 and AC4.
- **S6** — `defer dormant`, `run_dormant_fix(root, key, dry_run)`, ask TOOL-dTendedCadence-20's two halves. It runs
  `gen_build_index.py --dormant` (TOOL-dRankedPlan-4 S2), which writes nothing, and for each `dormant — <slug>` line
  runs `loop_transition.py dispose --build <slug>` (S3): exit 0 applies the owner's recorded move, or names it applied
  already, and is `fixed`; exit 1, `held: no owner disposition names a move`, writes nothing and is `held`, the build
  proposed to the owner by `run_breach_route` with the dormancy reading's offender key for that build; exit 2, a move
  the build's table refuses, is `survived` with the refusal. `dormant — none` and `unmeasured` apply nothing. The
  reading `live_builds_without_activity` (`drift_report.py:3479`) gains `fix = "defer dormant"` on its `[[reading]]`
  row, and its pin is 0, so each dormant build reaches the act band; the reading is pinless at this base
  (`drift_report.py:3474-3476`), and a pin of 0 files a proposal, never a red, since the reading gates nothing.
  Observed by AC6.
- **S7** — The patch fixes: `run_records_nonterminal_but_merged` (`drift_report.py:2512`) gains
  `fix = "close finished run records"` on its row, so each run record live although its witness is on the base ref
  is filed as a patch intake through I6, and the patch build closes it. `regenerate stale` is named by
  TOOL-dTendedCadence-5's map reading and `records-only fixes` by any reading whose fix changes only records; each
  reaches `item.maintain.patch` by S3. Observed by AC5.
- **S8** — The arms of §7's `New arm:` line in `tools/drift-audit/selftest.py`, one per fix and one for the empty
  set. Observed by AC2 to AC7.
- **S9** — The docs: `help/maintain.md` gains a section "The safe fixes" naming the six, their routes, the empty set
  and the deny-by-default refusal; `tools/drift-audit/README.md` names `maintain_fixes.py`. Observed by AC9.

## 3. Non-goals (OUT)

- The patch intake, its key and its `seen` recurrence: TOOL-dTendedCadence-8. This unit routes to it.
- The map reading and its regeneration: TOOL-dTendedCadence-5, which names `regenerate stale`.
- The dormancy proposal and the disposal mover themselves: TOOL-dRankedPlan-4, called and never copied; no second
  dormancy mover is built (ask TOOL-dTendedCadence-20's SEV row).
- Writing an owner's disposition record: the owner's (TOOL-dRankedPlan-4 §3).
- Closing a run record in place: `verb_landed` refuses a run not at `LANDING` (`tools/unattended/unattended.sh:6316`),
  so the close is a patch build's, never Maintain's.
- Remote branch deletion: `--remote` is never passed.
- Reaping's own fence, scope and mode: process-monitor's, unchanged.

### Edges

- **consumes-from** `TOOL-dTendedCadence-1` — `maintain.py`, whose `act` outcome S3 re-routes and whose rows gain `item.maintain.direct`
- **consumes-from** `TOOL-dTendedCadence-8` — `item.maintain.patch` and `[[reading]]`, the I6 filer the patch fixes reach and the rows whose `fix` field S5 to S7 set
- **consumes-from** `TOOL-dTendedCadence-4` — `read_policy_value`, drift-audit's one policy adapter and its `PolicyRefused`, S2's read
- **consumes-from** `TOOL-dTendedCadence-15` — `item.maintain.file`, where a survivor and a held dormant build go
- **hands-off** `TOOL-dTendedCadence-5` — `regenerate stale`, the fix name and its `act-patch` route that unit's map reading declares on its row
- **hands-off** `TOOL-dTendedCadence-9` — `derive_fix_route` and the `act` re-route in `maintain.py`, which that unit makes answer `patch` for its sweep row
- **hands-off** `TOOL-dTendedCadence-16` — `act-direct`, the route the node pass gives a node-scoped reading whose fix is direct, so `idle_processes_past_ceiling` and `landed_branches_unpruned` reach `item.maintain.direct` on every node
- **consumes-from** external — dRankedPlan's `gen_build_index.py --dormant` and `loop_transition.py dispose`, specced and unbuilt at base; process-monitor's `reap.py` and branch-reconcile's `branch_reconcile.py`, landed
- **hands-off** `TOOL-dTendedCadence-46` — `run_dormant_fix`, whose disposal that unit probes in a scratch tree and lands through a patch intake (review id 43)
- **hands-off** `TOOL-dTendedCadence-48` — the node-pass criteria, the two README rows, the dormancy pin and the reap targets' detail rows, which the minors batch repairs (review ids 7, 12, 13, 50)

## 4. Design

### Evidence

`policy.py get maintain.fixes` exits 2 at this base, "the row maintain.fixes carries a derived default no reader
computes yet" (probed; `policy.py:132-136`, `:696-698`). The reap is a dry run at every session start
(`tools/process-monitor/procmon-hook.js:119`), and `reap.py` with no `--kill` runs the sweep at the conf's mode,
exiting 1 on a survivor (`reap.py:427-488`). The cleanup's write mode removes the deletable worktrees and local
branches and touches a remote only under `--remote` (`branch_reconcile.py:1201-1206`). The run-record reading names
each live record whose witness is merged (`drift_report.py:2512-2516`), and the dormancy reading counts the
generator's `dormant` cells and is pinless (`drift_report.py:3470-3519`). `--dormant` is not in `gen_build_index.py`
at this base; only `LIVE_DORMANT_DAYS` labelling exists (`.memory-tree.conf:1034`).

The design rule decides each route: `maintain.direct` applies "the reading's fix, where it changes no tracked
content (reap, prune landed)", and `maintain.patch` files a patch intake "for a fix that changes tracked content"
(layer-expansions:224-225). `defer dormant` is TOOL-dRankedPlan-4's proposal plus its owner-gated mover, handed to
this build at its S5, and `dispose` writes nothing without the owner's disposition record (its S4).

### Data flow

```
item.maintain.read ── act ── derive_fix_route(fix, maintain.fixes)
   direct       ─▶ item.maintain.direct ─ reap.py --sweep | branch_reconcile.py --write ─ read again
                                          └ set gone ─▶ fixed ─▶ record │ standing ─▶ survived ─▶ file
   owner-gated  ─▶ item.maintain.direct ─ --dormant ─ dispose per slug ─ 0 fixed │ 1 held ─▶ file │ 2 survived ─▶ file
   patch        ─▶ item.maintain.patch (I6)
   file         ─▶ item.maintain.file
```

### Inventory

Names this unit mints, each asked of `lexicon.py --suggest <name> --as py.function` at this base and answered OK:
`read_fix_set`, `derive_fix_route`, `run_direct_fixes`, `run_dormant_fix`, `measure_idle_processes`,
`measure_landed_branches`. The module `maintain_fixes.py`, the table `FIX_ROUTES`, the route words `direct`, `patch`,
`owner-gated` and `file`, the outcomes `fixed`, `survived` and `held`, and the signals `idle_processes_past_ceiling`
and `landed_branches_unpruned`.

### Files touched (estimate)

- `tools/drift-audit/maintain_fixes.py` (new)
- `tools/drift-audit/maintain.py`
- `tools/drift-audit/drift_report.py` (the two readings joined to `SIGNALS`)
- `tools/drift-audit/kit.toml`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt` (rendered by `policy.py lists --write`)
- `help/maintain.md`

### Alternatives rejected

- **Setting `maintain.fixes` in `.governance/policy.toml` and leaving the derived default.** Rejected: every adopter
  without the file would still read a refusal, so the catalogue's documented default would never apply.
- **Keeping `item = ".+"` and refusing an unknown name in the dispatcher.** Rejected by the charter's [security]
  rule: the reader is the write boundary, so the closed set is validated there once.
- **Applying `close finished run records` in place through `verb_landed`.** Rejected: it refuses a run not at
  `LANDING` (`unattended.sh:6316`), and closing writes tracked content, which the design gives to `maintain.patch`.
- **Running every direct fix each period whatever the readings say.** Rejected: the design's witness is "the next
  reading shows the set gone", so a fix needs the reading it clears.

## 5. Production-readiness checklist

- security — the closed set is checked at the reader; a refused read applies no fix; prune never touches a remote;
  the one tracked write is `dispose`'s, and only for a build carrying the owner's disposition record.
- perf / scale — one dry sweep and one cleanup inventory per report run, each the cost of running it by hand today;
  every `drift_report.py` run now pays both, read-only.
- error / empty / loading states — an empty set: every `act` reading filed; `dormant — none`: nothing applied; a
  sibling kit absent: the fix is `survived` naming the kit, and the reading is filed.
- observability — one `maintain — <key> · item.maintain.direct · <reading> · <outcome>` line per fix.
- risks — a reap kills inside process-monitor's own fence and mode only; a survivor is filed, never retried in the
  same run.
- testing — §7's `New arm:` line.
- migration — the catalogue row's default moves from a derived prose to the same six as a list; no reader read the
  derived form, since every read refused it.
- user docs — `help/maintain.md` (S9).

## 6. Acceptance criteria

The fix fixture is a scratch git repository under `%TEMP%` with a short name holding copies of `tools/drift-audit/`,
`tools/policy/`, `tools/memory-tree/`, `tools/process-monitor/`, `tools/branch-reconcile/` and `tools/lib/`, a local
branch merged into `main` with its worktree, an unmerged branch, and stub bodies for the patch, file and record
rows that
print their tag and each breach. Each command runs with the fixture as its working directory.

- **AC1** — When `python tools/policy/policy.py get maintain.fixes` runs, it prints the six fix names one per line
  and exits 0.
  Red when: the read refuses, or a name differs from the six.
- **AC2** — When the fixture commits `.governance/policy.toml` with `[maintain]` `fixes = []`,
  `GOV_CADENCE_KEY=2026-11-01 python maintain.py --dry-run` routes every `act` reading `act-file`; with
  `fixes = ["rm"]` committed it prints `NOTE: maintain.fixes refused` and routes the same.
  Red when: an empty or refused set applies a fix, or a refusal takes the six.
- **AC3** — When `.process-monitor.conf` declares `PROCMON_REAP_MODE="reap-orphans"`, a one-second ceiling and one
  planted orphan `sleep` in scope, `GOV_CADENCE_KEY=2026-11-01 python maintain.py` routes
  `idle_processes_past_ceiling` `act-direct` and prints `fixed` once the reading shows 0 targets; under `report` mode
  it prints `survived` and the file stub receives the breach.
  Red when: a survivor reaches the record unfiled, or a cleared set is filed.
  cost: spawns one process and waits past the ceiling.
- **AC4** — When the same run reaches `landed_branches_unpruned`, the merged branch and its worktree are gone, the
  unmerged branch stands, the outcome is `fixed`, and no push runs; under `--dry-run` both branches stand.
  Red when: an unmerged branch is removed, a remote is touched, or a dry run writes.
- **AC5** — When three planted readings over their pins carry `fix = "regenerate stale"`, `"records-only fixes"` and
  `"close finished run records"`, `maintain.py --dry-run` routes each `act-patch` to the patch stub.
  Red when: a patch fix is applied in place or filed as an ask.
- **AC6** — When the fixture holds two builds dormant past `LIVE_DORMANT_DAYS`, one carrying the owner's disposition
  record naming `pause`, `GOV_CADENCE_KEY=2026-11-01 python maintain.py` runs `gen_build_index.py --dormant`, applies
  `dispose` to that build, which prints its `transition —` line and is `fixed`, and hands the other to the file stub
  as `held`, its transition log unchanged.
  Red when: a build with no disposition record moves, or a held build is not proposed.
  fixture: needs TOOL-dRankedPlan-4 S2 to S4 landed.
- **AC7** — When a reading with `fix = "reap"` stands over its pin and `fixes = ["prune landed"]` is committed, it
  routes `act-file`, and `python maintain.py --check` counts 7 items once this unit's row is in.
  Red when: a fix outside the set runs, or the direct row is missing.
- **AC8** — When `python tools/policy/policy.py lists --check` runs it exits 0, `grep -c "^maintain.fixes$"
  tools/policy/unsummarised-keys.txt` prints 0, and `grep -n 'read_policy_value("maintain.fixes"' maintain_fixes.py`
  finds the literal read.
  Red when: the row lacks a summary or usage, or no literal call reads the key.
- **AC9** — When `grep -n "The safe fixes\|defer dormant" maintain.md` runs in `help/`, each matches.
  Red when: the page omits one.

## 7. Gates

`drift-audit selftest` · `drift-audit wiring` · `policy fixtures` · `policy check` · `memory hygiene`

New arm: tools/drift-audit/selftest.py · covers AC2 AC3 AC4 AC5 AC6 AC7 · the fix fixture's six fixes, an empty and a refused set, a planted orphan, a merged and an unmerged branch and two dormant builds, staged against a `maintain_fixes.py` absent at this base · none

## 8. Open questions

- **F1 — How is `maintain.fixes` made readable?** (a) The catalogue row's default a literal list of the six, its
  `allowed` a closed `of` set; (b) the literal default, `allowed` kept `item = ".+"`; (c) the set written into
  `.governance/policy.toml` only. (c) leaves every other tree refusing; (b) admits a name no route knows, refused only
  later in the run, against validating once at the write boundary. Rung 3. RESOLVED (agent, 2026-11-01, delegated): (a). widens: none · relaxes: none
- **F2 — What does a refused `maintain.fixes` read apply?** (a) No fix, deny by default; (b) the catalogue's six, as
  a caller taking the catalogue default on `PolicyRefused` would. (b) applies fixes the file did not choose,
  against the
  charter's [security] rule. Rung 3. RESOLVED (agent, 2026-11-01, delegated): (a). widens: none · relaxes: none
- **F3 — Where does `defer dormant` run, and what of its write?** (a) In `item.maintain.direct`, calling `dispose`
  for each dormant build, its one tracked write the owner's recorded move; (b) a patch intake per dormant build whose
  patch build runs `dispose`. (b) cannot tell a proposed build from a disposable one at Maintain's time, since no
  parent offers a read-only disposition check, so ask TOOL-dTendedCadence-20's "one proposed and one disposed" would
  be observed only in the patch build; (a) is the hand-off TOOL-dRankedPlan-4 S5 makes, its S4 holding without the
  owner. v2 answers it (v2:1321, TOOL-dRankedPlan-4 S5), rung 1. RESOLVED (agent, 2026-11-01, delegated): (a). widens: none · relaxes: none
- **F4 — What do the direct fixes read?** (a) Two node-scoped readings this unit registers, the dry sweep's targets
  and the cleanup's deletable rows; (b) none, each direct fix run every period. (b) has no witness, and the design's
  is "the next reading shows the set gone". Rung 3. RESOLVED (agent, 2026-11-01, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (units 46, 48); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended: the two actuators, `run_sweep` behind `reap.py` (`tools/process-monitor/reap.py:345`) and
`write_deletions` behind `branch_reconcile.py --write` (`tools/branch-reconcile/branch_reconcile.py:1215-1216`), each
run as its kit's CLI; the existing readings `build_nonterminal_merged_runs` and `build_live_builds_without_activity`
(`tools/drift-audit/drift_report.py:2512`, `:3479`), given their fix; the policy reader's closed-set check
(`tools/policy/policy.py:143`); and dRankedPlan's proposal and mover, called by name. The probe `python
tools/codebase-map/reuse_lookup.py "apply a named safe fix: sweep idle processes, prune merged worktrees and
branches"` ranked `scan_processes` (`tools/process-monitor/census.py`), `add_scratch_worktree` and
`build_nonterminal_merged_runs` among name-stem hits, the census and the run-record reading confirming the seams above
and nothing routing a fix; so no existing seam fits the route table, and it is new over them. Where scout A's record
disagrees with source at this base: its `reap.py:345`, `:443`, `branch_reconcile.py:1201` and `drift_report.py:2512`
hold; its "removal at :988-1007" is `remove_worktree` at `:985-1008`; its `gen_build_index.py:2081-2111` dormancy
labelling is read here through `LIVE_DORMANT_DAYS` at `.memory-tree.conf:1034`.

Recall terms used: `python tools/memory-recall/query.py "which safe fixes may Maintain apply itself and which become
patch builds" --terms "maintain.fixes reap prune landed regenerate stale defer dormant records-only close finished run
records direct patch dispose"`
