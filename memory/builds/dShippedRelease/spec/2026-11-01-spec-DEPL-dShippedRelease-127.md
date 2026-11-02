# DEPL-dShippedRelease-127 — the proof of `mint`'s route runs on a clone carrying gov's tracked `.governance/deploy.toml`

**Status:** DEFERRED · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 31 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md) | research | DEPL-dShippedRelease-126 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-11-01-build-DEPL-dShippedRelease-133-token-fix-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-133-token-fix-return.md) | research | DEPL-dShippedRelease-133 DEPL-dShippedRelease-128 DEPL-dShippedRelease-126 DEPL-dShippedRelease-138 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-126-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-126-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-134 DEPL-dShippedRelease-126 DEPL-dShippedRelease-128 DEPL-dShippedRelease-131 DEPL-dShippedRelease-138 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 21 of `reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md`, BLOCKER, which shares item B1 with
ids 1 and 54 (DEPL-dShippedRelease-126, -128). Unit 122 AC1 and AC3 could not pass in a gov clone, because
the refused value is tracked, and §5 priced a permanent refusal as "a loud exit 1". A fixture with a
minimal `.governance/deploy.toml` would have gone green over that outage, so this unit binds the proof to
gov's real file and proves the plant is armed.

## 2. Scope (IN)

- **S1** — The clone. `--case mint-moved-kit` (unit 122 AC1) and the `push-main.sh --prepare` run of unit
  122 AC3 each run on a `git clone` of this repo, its `.governance/deploy.toml` the tracked one and no
  fixture written over it. Observed by AC1, AC3.
- **S2** — The liveness term. Ahead of `mint`, the case calls `target_context` for `integrations` on the
  clone and fails, exit 1, printing `not armed · deploy.toml refuses nothing` unless it raises `Refusal`
  naming `answers.stream_ownership`. So a green run passed the state that refuses, and a later respelling of
  that answer reds the case instead of emptying it. Observed by AC2.
- **S3** — The record. Unit 122 §5's risks line reads: a `Refusal` is exit 2 from `main`, `run_minter`
  returns 1, and the lander resets the merge, so any refusal in `mint`'s context is a refused landing and
  not an edge. With DEPL-dShippedRelease-126 no answer reaches that context. NOT OBSERVED: the correction of
  a record.

## 3. Non-goals (OUT)

- The context itself: DEPL-dShippedRelease-126.
- The regenerate population: DEPL-dShippedRelease-128.
- Changing gov's answer: `.governance/deploy.toml` keeps its prose, and S2 reads it as the plant.

### Edges

- **consumes-from** `DEPL-dShippedRelease-122` — AC1, AC3 and §5, which this unit restates
- **consumes-from** `DEPL-dShippedRelease-126` — `derive_regenerate_ctx`, the context the clone runs
- **hands-off** `DEPL-dShippedRelease-140` — S2's term, AC1, AC2 and §7, which that unit moves (round-5 id 23)
- **hands-off** `DEPL-dShippedRelease-144` — S1, S2, AC2, AC3 and §10, which the batch restates (round-5 ids 15, 16, 17, 20, 24, 32, 48, 49)

## 4. Design

### Evidence

- `git ls-files .governance/deploy.toml` lists the file, so a scratch clone inherits line 39.
- Report id 21 ran `target_context` over the registry and printed REFUSED on `answers.stream_ownership` for each of the 11 kits with a `[[regenerate]]` row. PINNED at the audit.
- `tools/push-main.sh:813-820` is `run_minter`, and `:902-906` resets the merge on its failure.

### Supersedes

- Unit 122 AC1's and AC3's setup: "a scratch clone with no `[gate_runner.ci]`" reads as S1's clone.
- Unit 122 §5's risks line.

### Files touched (estimate)

- `tools/integrations/ci/ci_emit.py`: S1, S2

## 5. Production-readiness checklist

- security — N/A — fixture code only.
- perf / scale — a clone per case, under `%TEMP%`, as unit 122 AC3 states.
- error / empty / loading states — S2 is the state where the plant holds nothing, and AC2 stages it.
- observability — S2's line names the missing plant.
- risks — an owner respelling that answer reds the case by S2; the remedy is a new plant, and the case names it.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — fixture code.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python ci_emit.py --fixture --case mint-moved-kit` runs on a clone
  holding the tracked `.governance/deploy.toml`, `mint --base <rev>` exits 0 printing `ci-not-declared`, and the
  kit's version moved.
  Red when: the case writes its own `.governance/deploy.toml`, so an outage on gov's real file stays green.
  cost: a scratch clone under `%TEMP%`, a minute.
- **AC2** — When the case runs with `stream_ownership` respelled in the clone to hold no em dash, it exits 1
  printing `not armed`.
  Red when: the plant is gone and the case passes on an empty population.
- **AC3** — When `bash tools/push-main.sh --prepare --slug fx` runs on that clone after the kit edit, it exits 0
  and its branch holds the prepared merge.
  Red when: a refusal in `mint`'s context resets the landing.
  cost: a scratch clone under `%TEMP%`, a minute.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/integrations/ci/ci_emit.py · covers AC1 AC2 AC3 · `mint-moved-kit` on a clone, its failing case a minimal `.governance/deploy.toml` written over the tracked one · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 21 (BLOCKER, item B1) of the round-4 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-5 spec audit's promoted units declare toward this unit (units 140, 144); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is unit 122's `mint-moved-kit` case in `tools/integrations/ci/ci_emit.py`.
`python tools/codebase-map/reuse_lookup.py "run a verb over a real tracked config file in a scratch clone"`
ranked the name-stem helpers `run`, `tracked` and `scratch` and no clone fixture, because the case is
specced and unbuilt, so no existing seam fits outside that case. The recall probe surfaced this round's
report and unit 122's AC3, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how is a route proved on gov's own root rather than a minimal fixture" --terms "scratch clone gov root deploy.toml tracked fixture minimal mint lander prepare proof real file"`
