# DEPL-dShippedRelease-126 — `mint` classifies a regenerate exit in the context that resolved its argv

**Status:** DEFERRED · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 31 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md) | research | DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-11-01-build-DEPL-dShippedRelease-133-token-fix-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-133-token-fix-return.md) | research | DEPL-dShippedRelease-133 DEPL-dShippedRelease-128 DEPL-dShippedRelease-127 DEPL-dShippedRelease-138 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-126-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-126-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-134 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-131 DEPL-dShippedRelease-138 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 1 of `reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md`, BLOCKER, which shares item B1 with
ids 21 and 54 (DEPL-dShippedRelease-127, -128). Unit 122 S2 builds `ctx` with `target_context` over gov's
own `.governance/deploy.toml`. That function's `[answers]` loop refuses the em dash on line 39 of that
file, so every kit in gov's root raises, and the route that exists to accept the integrations kit's exit 3
ends in the reset it was written to prevent. This unit takes `ctx` from the one resolution `mint` already
runs its argvs by.

## 2. Scope (IN)

- **S1** — The one context. `derive_regenerate_ctx(root, eid, desc)` in `tools/govkit/govkit.py` returns
  `{**canonical_ctx(eid), "kit": (desc.get("home") or "").rstrip("/") or derive_tool_root(root)}`, the
  expression `derive_regenerate_argvs` holds at `:13354`, and `derive_regenerate_argvs` calls it. Observed
  by AC1.
- **S2** — `mint` reads it. Unit 122 S2's `ctx` is S1's return, the `deploy` read leaves that item, and
  `cmd_mint` calls neither `load_deploy` nor `target_context`. Observed by AC2, AC3.
- **S3** — What `{kit}` reads. In `mint`, the integrations row's `{kit}/ci/ci_emit.py` resolves to
  `tools/integrations/ci/ci_emit.py` through the descriptor's `home`, which `resolve_descriptor_paths`
  (`:13256`) joined to the tool root at load. Observed by AC1.

## 3. Non-goals (OUT)

- The proof on a clone of gov's own root: DEPL-dShippedRelease-127.
- The regenerate population and its token set: DEPL-dShippedRelease-128.
- Respelling gov's answer or widening `ANSWER_VALUE_RE`: §8 F1.
- A checklist item that a spec reusing a function on a new root cites a run of it there: the audit's
  left-shift item, a gate of its own.

### Edges

- **consumes-from** `DEPL-dShippedRelease-122` — S1's route and S2's `ctx`, which this unit supersedes
- **hands-off** `DEPL-dShippedRelease-127` — `derive_regenerate_ctx`, which that unit's proof runs
- **hands-off** `DEPL-dShippedRelease-128` — `derive_regenerate_ctx`, whose tokens that unit grades
- **hands-off** `DEPL-dShippedRelease-138` — S2's dropped `deploy` read, on which ids 45 and 46 rest
- **hands-off** `DEPL-dShippedRelease-140` — AC3's `mint-answer-dash` and §7's arm, which that unit moves (round-5 id 23)
- **hands-off** `DEPL-dShippedRelease-145` — `derive_regenerate_ctx`, which that unit places ahead of the loop (round-5 id 3)
- **hands-off** `DEPL-dShippedRelease-144` — the fixture and §1, which the batch reads (round-5 ids 15, 24, 32)

## 4. Design

### Evidence

- `tools/govkit/govkit.py:1487-1489` is the `[answers]` loop, calling `demand_safe_token(..., prose=True)`.
- `.governance/deploy.toml:39` is `stream_ownership`, holding an em dash, and that file is tracked.
- A read-only probe at this spec's writing called `target_context` for the 11 entries with a `[[regenerate]]` row: 0 ok, 11 refused. PINNED at `e8ced8ac`.
- `tools/govkit/govkit.py:14133` turns a `Refusal` into exit 2, `tools/push-main.sh:813-820` turns any non-zero into a refused minter, and `:902-906` resets the merge.
- `derive_regenerate_argvs`' docstring promises one resolution, so a probe and the argv it classifies read one `{kit}`.

### Supersedes

- Unit 122 S2's first sentence, and its `deploy` read.
- Unit 122 §4's Evidence stands. `.governance/deploy.toml` still decides that `render` exits 3 there.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `derive_regenerate_ctx` | function, `tools/govkit/govkit.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1, S2
- `tools/integrations/ci/ci_emit.py`: the fixture of §6

### Alternatives rejected

- **`target_context` with `answers` dropped.** It still reads a `.governance/deploy.toml` the `check_mint_verb` fixture does not hold, and reads `{kit}` as `<prefix>/<entry id>`, which is `tools/playbook-render` for a kit homed at `tools/playbook`.
- **A seeded-tokens split of `target_context`.** The same `{kit}`, in a second function, for one caller.

## 5. Production-readiness checklist

- security — N/A — the context carries gov's own derived tokens, and no target's answer reaches `mint`.
- perf / scale — N/A — one dict per regenerate argv.
- error / empty / loading states — a probe token this context cannot resolve fails its term, so the block does not match, and DEPL-dShippedRelease-128 grades that population.
- observability — unit 122 S2's line prints on an accepted stop, and the `FAILED` line on a refusal.
- risks — `canonical_ctx` carries `opt_in_all`, which no probe string reads, as DEPL-dShippedRelease-128's token walk shows.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python -c` imports `tools/govkit/govkit.py` and calls `derive_regenerate_ctx` for
  `integrations` and for `playbook-render`, `kit` reads `tools/integrations` and `tools/playbook`, and
  `derive_regenerate_argvs` resolves its argvs from that value.
  Red when: a probe and the argv it classifies resolve `{kit}` from two contexts.
- **AC2** — When `python -c` walks `cmd_mint` by `ast`, it finds no call of `load_deploy` or `target_context`.
  Red when: a target's answers reach the lander again.
- **AC3** — When `python ci_emit.py --fixture --case mint-answer-dash` runs `mint` over
  a fixture whose `.governance/deploy.toml` holds `stream_ownership = "a — b"`, and whose moved kit's
  regenerate stub exits 3 on a satisfied `ok = true` row, it exits 0 printing `regenerate stopped`.
  Red when: `target_context` restored, the case exits 2 on `answers.stream_ownership`.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/integrations/ci/ci_emit.py · covers AC3 · `mint-answer-dash`, its failing case `target_context` restored in `cmd_mint` · none

## 8. Open questions

- **F1 — Which context closes the refusal?** Options: (a) the regenerate context, `{**canonical_ctx(eid), "kit": home}`;
  (b) `target_context` with `answers` dropped; (c) a seeded-tokens split of `target_context`; (d) widening
  `ANSWER_VALUE_RE`. (d) widens a guard on values interpolated into argv, veto 3. (b) and (c) read `{kit}` by
  entry id, and (b) reads a file the mint fixture lacks. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3,
  reuse of a seam, the report's first fix. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 1 (BLOCKER, item B1) of the round-4 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-5 spec audit's promoted units declare toward this unit (units 140, 145, 144); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `derive_regenerate_argvs` at `tools/govkit/govkit.py:13347`, whose context this unit lifts into one function.
`python tools/codebase-map/reuse_lookup.py "resolve a descriptor's tokens without a target descriptor"`
ranked the name-stem helpers `resolve` and `resolve_kit_dir` and missed that function, which the report's
citation found, so the probe and the source disagree and the source stands. The recall probe surfaced
this round's report and unit 122, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "which context resolves a regenerate argv at gov's own root" --terms "regenerate canonical_ctx target_context derive_regenerate_argvs home kit token mint answers demand_safe_token"`
