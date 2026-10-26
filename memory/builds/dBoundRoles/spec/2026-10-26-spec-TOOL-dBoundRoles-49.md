# TOOL-dBoundRoles-49 — govkit's default plan derives the seed rows it expects to preview from the plan model and the roles roster, so the third typed roles count cannot red late

**Status:** DEFERRED · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 5 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-45-round2-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-45-round2-fix-return.md) | research | TOOL-dBoundRoles-43 TOOL-dBoundRoles-45 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 |
| [2026-10-26-build-TOOL-dBoundRoles-49-deviation-491.md](../build/2026-10-26-build-TOOL-dBoundRoles-49-deviation-491.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-49-deviation-492.md](../build/2026-10-26-build-TOOL-dBoundRoles-49-deviation-492.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-9 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-37 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-50 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-66 TOOL-dBoundRoles-69 |
| [2026-10-26-prompt-TOOL-dBoundRoles-45-round2-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-45-round2-fix-brief.md) | research | TOOL-dBoundRoles-45 TOOL-dBoundRoles-43 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 |
| [2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-48 TOOL-dBoundRoles-47 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the eight promoted specs 37 to 44
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md`) confirmed
finding **id 23 at HIGH**, report item **H2**. No other id shares the item.

`TOOL-dBoundRoles-37` promises that no roster change leaves a typed count to red, and derives the two
literals of `check_roles_install`. A third stays. `tools/govkit/selftest.py:6896-6898` checks
`marks.get("write|seed", 0) + marks.get("KEEP|seed", 0) == 14` on the default plan, and its comments at
`:6886-6891` attribute ten of the fourteen to the roles kit's house overlays and one to `policy.toml`.
`TOOL-dBoundRoles-1` S2 seeds four new overlays and S3 merges two, so the count moves, and
`TOOL-dBoundRoles-19` moves it again. The `govkit selftest` leg's guard covers nothing under
`tools/roles/`, so a guarded run skips the leg and the red surfaces on a later, unrelated govkit change:
the delayed red 37 exists to close, with 37 AC3's grep green over it.

This unit replaces the literal with a count derived from the plan model, and ties the roles kit's share
of it to the overlay set 37 derives. It repairs `TOOL-dBoundRoles-37` and builds one step after it
(order 5).

## 2. Scope (IN)

- **S1** — The derivation, `derive_seed_expected(target, descs, selection)` in
  `tools/govkit/selftest.py`: the rows `gk.planned_writes` (`tools/govkit/govkit.py:3988`) returns for the
  target whose `kind` is `write`, whose `role` is `seed` and which are not `missing`. That is the one
  predicate `cmd_plan` prints both seed marks from (`govkit.py:5048-5053`), so the preview and its
  expectation cannot classify a row two ways. Observed by AC1.
- **S2** — The seed check compares counts. The check at `:6896-6898` compares the printed
  `write|seed` and `KEEP|seed` sum with `len(derive_seed_expected(t2, descs, selection))`, the default
  target `t2` and the selection the default plan used. On failure it prints both figures and the derived
  rows per kit. The `ORDER|project-owned` half of the same check is not this unit's. Observed by AC1 and
  AC3.
- **S3** — The roles share is the roster's. A second check asserts that every entry of the `overlays` set
  `derive_roles_expected` returns (`TOOL-dBoundRoles-37` S1) is the source of one derived row whose kit
  is `roles`, so an overlay the roster seeds and the plan does not preview reds by name. Observed by AC2.

## 3. Non-goals (OUT)

- `derive_roles_expected` and the two checks of `check_roles_install`: `TOOL-dBoundRoles-37`'s, read here.
- The `ORDER|project-owned == 34` literal beside the seed sum, and the `SIDE|rendered == 6` check above
  it. Neither counts a roles file; the comments at `:6856-6895` record each as a measurement of the tree.
- Widening the `govkit selftest` leg's guard to `tools/roles/`: `TOOL-dBoundRoles-37` §4 measured that it
  reds `spec tokens` on nine specs this build does not own.
- The comment block at `:6880-6895`, a dated changelog of past measurements, which stays true as history.

### Edges

- **consumes-from** `TOOL-dBoundRoles-37` — `derive_roles_expected` and the descriptors it reads through `gk.read_descriptors`, whose `overlays` set S3 ties the plan's roles share to (id 23)
- **hands-off** `TOOL-dBoundRoles-54` — S3's check, whose expected side unit 54 reads from the roster through `derive_overlay_expected`, and AC2, which unit 54's pass restates (id 14 of the round-1 audit of units 45 to 51)
- **hands-off** `TOOL-dBoundRoles-58` — the filter of `derive_seed_expected`, which unit 58 lifts into one predicate shared with `cmd_plan` (id 27 of the round-1 audit of units 45 to 51)
- **hands-off** `TOOL-dBoundRoles-64` — AC1's import form, which unit 63's observation keeps, and §3, which unit 64 extends by the hands-off bullet for unit 63 (id 26 of the round-1 audit of units 61 to 63)

## 4. Design

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `tools/govkit/selftest.py:6810-6814` builds the default target `t2` and runs `plan` on it, `:6855`
  measures its marks, and `:6896-6898` holds the typed sum.
- `tools/govkit/govkit.py:5022-5053`: `cmd_plan` reads the descriptors, resolves the selection, calls
  `planned_writes`, and prints `KEEP` for a `write` seed row whose destination exists, `write` otherwise.
- `memory/DECISIONS.md:81`, `TOOL-dClosedLexicon-13`: a preview and the verb it previews classify with
  one predicate, and the role alone is not it. Counting seed rules by role in the descriptors would be a
  second predicate; S1 reads the plan model's.

### Why two checks

S2 alone proves the preview prints every seed row the model holds, which a change to the plan's printing
breaks and a roster change does not. S3 is what ties the figure to the roster: a roles overlay that the
roster seeds and the plan drops reds by name. Together they replace what the literal did, a measured
expectation, with one that moves when the roster does.

### Inventory

Minted: `derive_seed_expected` (`py.function`) and S3's check label, asked of
`python tools/lexicon/lexicon.py --suggest derive_seed_expected --as py.function` at the pass.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 5. `TOOL-dBoundRoles-22` holds order 5 and writes no file this unit writes.

### Files touched (estimate)

- `tools/govkit/selftest.py`

### Alternatives rejected

- **Re-type the literal.** It moves at `TOOL-dBoundRoles-1`, again at `TOOL-dBoundRoles-19`, and at
  every later seed, which is the defect.
- **Count `role = "seed"` rules in the descriptors.** A second classification of the same rows, which
  `TOOL-dClosedLexicon-13` rules out (§8 F2).

## 5. Production-readiness checklist

- security — no new write path; the selftest reads a scratch target it built.
- perf / scale — one more `planned_writes` call over the default selection, already computed once by the
  plan the case runs.
- error / empty / loading states — a selection with no seed rows derives an empty set and compares equal
  to a plan that prints none.
- observability — each failing check prints both figures and the per-kit rows or the missing overlay.
- risks — `planned_writes` changes its signature; the derivation fails loudly at import of the case.
- testing — AC1 to AC3 by probe and grep; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a `python -c` slice puts `tools/govkit` on `sys.path`, imports govkit's self-test module
  as a library and runs no suite, the form units 40 and 43 use, builds a default target with its
  `make_target(..., DEPLOY_REGISTRY_DEFAULT)`, runs `govkit.py plan` on it and prints
  `measure_plan_marks`'s `write|seed` plus `KEEP|seed` beside `len(derive_seed_expected(...))`, the two
  figures are equal; with one more `house/*.md` overlay seeded in a scratch copy of the roles kit, both
  rise by one.
  Red when: the expectation is typed, so it stays put while the plan moves.
  figure: both figures are DERIVED at observation time.
  fixture: the target and the scratch kit copy are built under the run's scratch path by the probe.
- **AC2** — When the same probe drops one overlay's seed row from the scratch roles descriptor while the
  file stays under `house/`, S3's check reports that overlay by name.
  Red when: the roles share is not tied to the roster, so a dropped overlay passes.
- **AC3** — When `grep -nE 'seed", 0\) == [0-9]+' tools/govkit/selftest.py` runs on the built tree, it
  prints nothing.
  Red when: a typed seed total is left beside the plan it counts.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the default plan's seed checks of S2 and S3, staged by restoring the literal `== 14` while a scratch roles copy seeds unit 1's four extra overlays, which reds the seed check · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 37 carries no
  clause; veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Derive the total from the plan model or from the descriptors' seed rules?** Options: (a) the
  plan model's rows through `planned_writes`, with S3 tying the roles share to the roster; (b) seed rules
  counted in the descriptors, the report's first suggestion. (b) is a second classifier of one row set,
  against `TOOL-dClosedLexicon-13`, a decision record of this repository. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the report's second suggestion, the roles share from
  `derive_roles_expected`, carried by S3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 37 to 44, id 23
  (HIGH, item H2), on the report's fix.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dBoundRoles-54 and -58, promotions of the round-1 audit of units 45 to 51; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-64, the minors batch of the round-1 audit of units 61 to 63; nothing else moved.

## 10. Reuse audit

The seams are `gk.planned_writes` (`tools/govkit/govkit.py:3988`), the plan model `cmd_plan` prints from,
and `TOOL-dBoundRoles-37`'s `derive_roles_expected`. `python tools/codebase-map/reuse_lookup.py "derive an expected seed row count from the kit descriptors instead of a literal"`
ranked `rows`, `row`, `counts` and `seed`, none a plan-model count; the recall probe returned
`TOOL-dClosedLexicon-13`, which rules the descriptor count out, and `TOOL-dBoundRoles-37`, whose
derivation S3 reuses.

Recall terms used: `python tools/memory-recall/query.py "how is a govkit plan preview seed count kept from drifting" --terms "govkit selftest plan preview write seed KEEP seed count literal derived descriptors default selection"`
