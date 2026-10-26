# TOOL-dBoundRoles-55 — unit 49's overlay check refuses an empty expected set, and ends where unit 19 moves the house files out of the kit

**Status:** OPEN · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 6 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 |
| [2026-10-26-build-TOOL-dBoundRoles-52-round3-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-52-round3-fix-return.md) | research | TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-58 |
| [2026-10-26-prompt-TOOL-dBoundRoles-52-round3-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-52-round3-fix-brief.md) | research | TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-58 |
| [2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-54 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the seven promoted specs 45 to 51
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md`) confirmed
finding **id 40 at HIGH**, report item **H2**. Id 14 shares the item at HIGH and takes
`TOOL-dBoundRoles-54`.

Id 40 is the failure-envelope face of the item: `TOOL-dBoundRoles-49` S3 claims a roster-to-plan tie it
does not test, and the report's fix adds that it must "refuse an empty expected set rather than pass,
and state what it checks after unit 19, or retire it there". `TOOL-dBoundRoles-19` S5 moves the ten
`house/*.md` files out of the roles kit and keeps one seed path, `house/policy.toml`. From order 24 on
the roles kit seeds no overlay, so a check that compares overlays either passes over an empty
population or, on unit 54's roster side, reds on every role.

This unit gives S3 both ends: an empty expected set refuses, and unit 19's pass deletes the check with
the files it moves. It repairs `TOOL-dBoundRoles-49` and builds one step after it (order 6), after unit
54 re-derives S3's expected side.

## 2. Scope (IN)

- **S1** — The empty refusal. S3's compare fails, naming the kit path it loaded, when
  `derive_overlay_expected` returns an empty set, before it compares anything. A roster load that finds
  no slot is a broken loader or a wrong path, never a passing check. Observed by AC1.
- **S2** — The end at unit 19. `TOOL-dBoundRoles-19`'s pass, which removes the house files and their
  include from `tools/roles/kit.toml` and already re-points the OC8 checks of `tools/govkit/selftest.py`
  (its §4 Files touched), deletes S3's compare and `derive_overlay_expected` in the same pass, as its
  consumes-from edge to this unit says. From then on the moved overlays are graded where they live,
  `.governance/instructions.toml`, by 19's own criteria. Observed by AC2.
  **Readers:** by name: no product file spells the function's name at this unit's base, since unit 54
  mints it at its pass; the files that spell it are
  `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-54.md` (S1 mints it, its AC calls it),
  `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-49.md:65` (the edge naming it as
  S3's expected side) and `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-19.md:99`
  (the edge that deletes it), and from unit 54's pass to unit 19's, `tools/govkit/selftest.py`, where
  S3's compare is its one caller. by value: `tools/govkit/selftest.py`, S3's compare, the one reader of
  the expected set, deleted in the same pass; nothing else reads it.
- **S3** — What S3 checks, written beside it. The check's comment states the population it reads, the
  three breaks of unit 54 §4's table it reds, that it refuses an empty set, and that unit 19 deletes it.
  Observed by AC3.

## 3. Non-goals (OUT)

- The roster-side expected set and the compare: `TOOL-dBoundRoles-54`'s, for id 14.
- A post-19 overlay check over `.governance/instructions.toml`: unit 19's AC1 and AC2 grade the moved
  units.
- Keeping S3 alive after 19 behind a skip. A check over a population that cannot exist is deleted, not
  disabled (charter [yagni]).

### Edges

- **consumes-from** `TOOL-dBoundRoles-54` — `derive_overlay_expected` and S2's compare, to which S1 adds the empty refusal (ids 14 and 40)
- **hands-off** `TOOL-dBoundRoles-19` — the deletion of S3's compare and `derive_overlay_expected` in the pass that moves the house files out of the kit (id 40)
- **hands-off** `TOOL-dBoundRoles-60` — AC1, AC2 and §7, which unit 60 restates: a fixture empty on both sides, the after half named in unit 19's criteria and the arm's life to unit 19's pass (ids 7, 8, 28 and 36 of the round-1 audit of units 52 to 58)
- **hands-off** `TOOL-dBoundRoles-64` — §3, which unit 64 extends by the hands-off bullet for unit 63 (id 26 of the round-1 audit of units 61 to 63)

## 4. Design

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-19.md` S5 removes the ten
  `house/*.md` files and keeps `house/policy.toml` seeded; its §4 Files touched lists
  `tools/govkit/selftest.py` for the OC8 checks.
- `tools/govkit/selftest.py:6886-6891` attributes ten seed rows to the house overlays, the population S3
  reads.

### Why delete at 19 rather than re-point

After 19 the roles kit seeds no `house/*.md`, and the overlays are level-5 units in a file the plan does
not seed per role. No plan row would exist to compare a role with, so the only re-pointing is to a
different check over a different file, which 19 already owns.

### Inventory

Minted: S1's refusal line. No function.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 6. It consumes from `TOOL-dBoundRoles-54` at the same order and writes the same
file, so `--dispatch` holds it until unit 54 is CLOSED. S2's deletion lands in unit 19's pass at
order 24.

### Files touched (estimate)

- `tools/govkit/selftest.py`

### Alternatives rejected

- **Pass an empty set.** That is the empty-population-read-as-coverage class the charter's [gate] rule
  names.
- **Skip S3 when the kit seeds no overlay.** The skip is permanent from order 24 and reads as coverage
  in every later run.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — one length test before the compare.
- error / empty / loading states — S1 is the empty state, refused by name.
- observability — the refusal names the kit path the roster was loaded from.
- risks — unit 19's pass skipping S2 leaves a check that reds on every role; 19's edge to this unit
  names the deletion, and AC2 observes it.
- testing — AC1 to AC3 by probe and grep; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a `python -c` slice imports govkit's self-test module as a library, runs no suite, and
  runs S3's compare against a scratch roles kit copy whose `agents/` folder is empty, the compare fails
  naming the kit path.
  Red when: an empty roster passes the overlay check.
  fixture: the scratch kit copy is built under the run's scratch path by the probe.
- **AC2** — When `grep -n 'derive_overlay_expected' tools/govkit/selftest.py` runs on the tree unit 19's
  pass leaves, it prints nothing, and before that pass it prints the definition and its call.
  Red when: the check outlives the files it compares.
  permission: observed at unit 19's pass commit, which builds after this unit; this pass records the
  before half and unit 19's ledger the after half.
- **AC3** — When `grep -n 'unit 19 deletes' tools/govkit/selftest.py` runs before unit 19's pass, it prints
  the line of S3's comment.
  Red when: the check carries no account of its population and its end.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · the empty-roster refusal, staged by removing S1's length test, which lets an empty kit pass · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 49 carries no
  clause; veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — After unit 19, state what S3 checks, or retire it?** Options: (a) delete it in 19's pass; (b)
  re-point it at `.governance/instructions.toml`; (c) keep it with a skip. (c) reads an empty
  population as coverage. (b) duplicates 19's own criteria over the moved units. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, fewest follow-ups. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 45 to 51, id 40
  (HIGH, item H2, shared with id 14), on the report's empty-set refusal and its retire-at-19 option.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-60, the minors batch of the round-1 audit of units 52 to 58; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-64, the minors batch of the round-1 audit of units 61 to 63; nothing else moved.

## 10. Reuse audit

The seam is `TOOL-dBoundRoles-54`'s `derive_overlay_expected` and the compare it feeds in
`tools/govkit/selftest.py`, extended by one refusal, and unit 19's pass, which already edits that file.
`python tools/codebase-map/reuse_lookup.py "refuse an empty expected population in a derived check"`
ranked `check`, `checks`, `population` and `check_line`, none an empty-set refusal in govkit's selftest,
so no existing seam fits beyond the compare.

Recall terms used: `python tools/memory-recall/query.py "how is a seeded overlay count tied to the roles roster" --terms "house overlay seed rows planned_writes derive_roles_expected roster agent slot govkit selftest"`
