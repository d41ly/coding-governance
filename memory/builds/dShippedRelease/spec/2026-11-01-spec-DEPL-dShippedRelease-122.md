# DEPL-dShippedRelease-122 — `mint` reads a regenerate exit through the accepted-outcome rule, so a declared stop lands

**Status:** DEFERRED · rev-3 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 30 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md) | research | DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |
| [2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-123 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-124 DEPL-dShippedRelease-119 DEPL-dShippedRelease-121 DEPL-dShippedRelease-120 DEPL-dShippedRelease-125 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 47 of `reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md`, HIGH, item H8. Unit 87 prices
`render`'s exit 3 for `apply` and `update` only. `cmd_mint` also runs each `[[regenerate]]` argv and fails on
any non-zero exit (`tools/govkit/govkit.py:13590-13594`), unit 8 S6 makes `render` the kit's regenerate row,
and gov declares no `[gate_runner.ci]`. Once an integrations file moves, `push-main.sh --prepare` prints
`FAILED · regenerate exited 3` and resets, so gov can land no change to that kit. This unit teaches the
third caller what `update` already knows.

## 2. Scope (IN)

- **S1** — The route. `cmd_mint` classifies each regenerate exit by `classify_outcome(root, desc, ctx, rc)`
  and `outcome_accepted(rc, oc, declares_outcome_for(desc, rc))`, as `update` does at
  `tools/govkit/govkit.py:11374-11376`. A refused exit prints the `FAILED` line and returns 1, as today.
  Observed by AC1, AC2, AC3.
- **S2** — The context. `ctx` is `target_context(root, deploy, eid, desc)`, `deploy` read once from
  `root`'s `.governance/deploy.toml`. An accepted non-zero exit prints
  `mint: <eid> · <means> · regenerate stopped` and goes on. Observed by AC1.
- **S3** — Every caller, named. `update` already classifies, `selfcheck --fix` prints the argvs and runs
  none, and `tools/run-gates/regen.py` reads a `[[regenerate]]` row only when it carries `stage`, which
  unit 8 S6's row does not. NOT OBSERVED: a statement of what stands, each cited in §4.

## 3. Non-goals (OUT)

- A mode of `render` that exits 0 on no table: §8 F1.
- A checklist item that a new exit lists every caller of its argv: the audit's left-shift item, and S3 is
  its one instance.

### Edges

- **consumes-from** `DEPL-dShippedRelease-87` — `EXIT_NOT_DECLARED`, the exit this unit routes
- **consumes-from** `DEPL-dShippedRelease-8` — S6's `[[regenerate]]` row
- **consumes-from** `DEPL-dShippedRelease-120` — the `code = 3` row, which accepts the exit in gov's own root
- **hands-off** `DEPL-dShippedRelease-126` — S1's route and S2's `ctx`, which that unit supersedes (round-4 id 1)
- **hands-off** `DEPL-dShippedRelease-127` — AC1, AC3 and §5, which that unit restates (round-4 id 21)
- **hands-off** `DEPL-dShippedRelease-128` — S1's route, whose population that unit runs (round-4 id 54)
- **hands-off** `DEPL-dShippedRelease-138` — the text and code the batch repairs (round-4 ids 45, 46)
- **hands-off** `DEPL-dShippedRelease-140` — AC1's `mint-moved-kit` and §7's arm, which that unit moves (round-5 id 23)
- **hands-off** `DEPL-dShippedRelease-145` — S1's route, which that unit's population runs (round-5 id 3)
- **hands-off** `DEPL-dShippedRelease-144` — AC1 and AC3 grade at order 31, after unit 126 S1 and S2 land, and the batch restates them (round-5 ids 4, 20, 24, 48)

## 4. Design

### Evidence

- `tools/govkit/govkit.py:13497` is `cmd_mint`, and its loop at `:13582-13594` returns 1 on any `rc != 0`.
- `tools/push-main.sh:902-906`: a failed `run_minter` resets the merge and exits 1, and `:1084` is the second call.
- `tools/govkit/govkit.py:13347` is `derive_regenerate_argvs`, whose docstring names `selfcheck --fix` and `mint` as its readers.
- `tools/run-gates/regen.py:167-168`: a `[[regenerate]]` row carrying no `stage` is not an item.
- `.governance/deploy.toml` exists at gov's root and holds no `gate_runner` key, and `.github/workflows/` holds only `remote-ci.yml`, so `render` exits 3 there and the row's `must_not_exist` holds.

### Supersedes

- Unit 87 §5's risks line: it names `update`'s row, and `mint` joins it.
- `cmd_mint`'s docstring line "a regenerate exiting non-zero", which reads "a regenerate exit `outcome_accepted` refuses".

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1, S2
- `tools/govkit/selftest.py`: the regenerate arm of §7
- `tools/integrations/ci/ci_emit.py`: the fixture of §6

### Alternatives rejected

- **A `render --no-table-ok` mode for the `[[regenerate]]` row.** Two exits for one state, and `update` already reads the row by its outcome block.

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — one probe per minted kit's regenerate argv.
- error / empty / loading states — a descriptor declaring no `[[outcome]]` keeps today's reading, since `outcome_accepted` refuses every non-zero exit with no block.
- observability — S2's line prints on the stop, and the `FAILED` line on a refusal.
- risks — `read_descriptors` now feeds a target context in `mint`; a `target_context` refusal in gov's own root is a loud exit 1 the lander already routes.
- testing — the criteria of §6 and the arms of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python ci_emit.py --fixture --case mint-moved-kit` edits a file under the kit in a scratch
  clone with no `[gate_runner.ci]` and runs `python tools/govkit/govkit.py mint --base <rev>`, it exits 0
  printing `ci-not-declared`, and the kit's version moved.
  Red when: a declared stop reads as a failed regenerate.
- **AC2** — When the case stubs a regenerate argv to exit 1 on a kit with no matching row, `mint` exits 1
  printing `FAILED`.
  Red when: the route accepts a real failure.
- **AC3** — When `bash tools/push-main.sh --prepare --slug fx` runs after that edit on a scratch clone, it
  exits 0 and its branch holds the prepared merge.
  Red when: every gov landing that moves the kit is refused and reset.
  cost: a scratch clone under `%TEMP%`, a minute.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC2 · a stub regenerate argv, its failing case every exit accepted · none

New arm: tools/integrations/ci/ci_emit.py · covers AC1 AC3 · `mint-moved-kit`, its failing case `rc != 0` restored · none

## 8. Open questions

- **F1 — Where does the exit become acceptable?** Options: (a) `cmd_mint` routes through the rule `update`
  uses; (b) the row reads a mode exiting 0 on no table. (b) gives one state two exits and undoes unit 87's
  reserved code. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, a third caller of one helper.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 47 (HIGH, item H8) of the round-3 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-4 spec audit's promoted units declare toward this unit (units 126, 127, 128, 138); no scope, design or criterion moved.
- rev-3 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-5 spec audit's promoted units declare toward this unit (units 140, 145, 144); the bullet to unit 144 carries the sentence this unit's own pass needs, because that batch builds last, and no other section moved.

## 10. Reuse audit

The seam extended is `classify_outcome` and `outcome_accepted` (`tools/govkit/govkit.py:6519`, `:6557`), called as `update` calls them at `:11374-11376`.
`python tools/codebase-map/reuse_lookup.py "route a regenerate exit through the accepted outcome rule"`
ranked `classify_outcome`, the seam this unit calls. The recall probe surfaced unit 3 and
TOOL-dRedressedBar-9, whose helper this is, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what reads a regenerate exit code" --terms "regenerate exit mint classify_outcome outcome_accepted run_minter lander cmd_mint declared stop update"`
