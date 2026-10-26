# TOOL-dBoundRoles-54 — unit 49's overlay check reads its expected side from the roster, one `house/<slot>.md` per role slot, never from the seed rule it is compared with

**Status:** DEFERRED · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 6 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-54-deviation-541.md](../build/2026-10-26-build-TOOL-dBoundRoles-54-deviation-541.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-54-deviation-542.md](../build/2026-10-26-build-TOOL-dBoundRoles-54-deviation-542.md) | deviation | — |
| [2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-55 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the seven promoted specs 45 to 51
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md`) confirmed
finding **id 14 at HIGH**, report item **H2**. Id 40 shares the item at HIGH and takes
`TOOL-dBoundRoles-55`.

Id 14 is the grounding face of the item. `TOOL-dBoundRoles-49` S3 checks that every entry of the
`overlays` set `derive_roles_expected` returns is the source of one roles seed row of the default plan.
`TOOL-dBoundRoles-37` S1 defines `overlays` as the `house/*.md` includes of the descriptor's seed rows,
and `planned_writes` builds those rows from the same includes (`tools/govkit/govkit.py:321-338`,
`rule_sources`). Both sides come from one `[[files]]` seed rule in `tools/roles/kit.toml:35-39`, so 49
AC2, which drops an overlay's seed row, removes it from both sides and is red against a correct build,
and 49 §4's claim that S3 ties the figure to the roster is false: a role added with no seeded overlay,
or an include removed while its file stays, passes.

This unit derives S3's expected side from the roster, independent of the seed rule, and restates 49's
criterion for it. It repairs `TOOL-dBoundRoles-49` and builds one step after it (order 6).

## 2. Scope (IN)

- **S1** — The expected side, `derive_overlay_expected(kit)` in `tools/govkit/selftest.py`: the set
  `house/<slot>.md` for every slot of the installed kit's roster, read through the same
  `roles_lib.load_roles` load `TOOL-dBoundRoles-37` S1 makes. Every slot counts, `agent: false`
  included. Where unit 37 left that load inline, this pass lifts it into one function both call, so the
  selftest holds one loader. Observed by AC1.
- **S2** — The compare, both ways. S3 of unit 49 compares S1's set with the `src` of every roles-kit row
  `derive_seed_expected` returns whose source matches `house/*.md`. A slot whose overlay is not seeded
  reds naming the slot; a seeded overlay no slot owns reds naming the file. Each failure prints both
  sets. Observed by AC1 and AC2.
- **S3** — Unit 49's spec follows the check. The pass bumps `TOOL-dBoundRoles-49`'s spec with S3, §4 "Why
  two checks" and AC2 restated for S1's set, and a §9 line naming this unit, before it edits the check
  (BUILD-METHOD M2, READY). Unit 49's ledger answers AC2 `amended rev-<n>`, naming that revision.
  Observed by AC3.

## 3. Non-goals (OUT)

- The empty-set refusal and S3's end at unit 19, where the house files leave the kit:
  `TOOL-dBoundRoles-55`'s, for id 40.
- `derive_roles_expected` and its `agents` set: `TOOL-dBoundRoles-37`'s, read here.
- A tracked-file side, house files present with no role and no include. A stray file seeds nothing and
  previews nothing, and S2 reds every overlay that is seeded without a role.
- The seed-count check of 49 S2.

### Edges

- **consumes-from** `TOOL-dBoundRoles-49` — S3's check and `derive_seed_expected`, whose expected side S1 replaces (id 14)
- **consumes-from** `TOOL-dBoundRoles-37` — the installed kit's `roles_lib.load_roles` load inside `derive_roles_expected`, which S1 reads every slot through (id 14)
- **hands-off** `TOOL-dBoundRoles-55` — `derive_overlay_expected` and S2's compare, which unit 55 makes refuse an empty expected set and ends at unit 19 (ids 14 and 40)
- **hands-off** `TOOL-dBoundRoles-60` — S1, S2, AC1 to AC3, §4 and §7, which unit 60 restates: one path form, a criterion red before the bump, no typed count, the arm's life to unit 19's pass and the write set (ids 5, 13, 26, 28, 32 and 35 of the round-1 audit of units 52 to 58)
- **hands-off** `TOOL-dBoundRoles-64` — §3, which unit 64 extends by the hands-off bullet for unit 63 (id 26 of the round-1 audit of units 61 to 63)

## 4. Design

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `tools/roles/kit.toml:35-39` lists the ten house overlays and `house/policy.toml` in one seed rule;
  `tools/govkit/govkit.py:321-338` returns a list include's paths unchecked, one plan row each.
- `tools/roles/agents/` holds ten role files and `tools/roles/house/` ten `.md` overlays, one per slot;
  `gov-session.agent.md` sets `agent: false` and still has `house/gov-session.md`, so the agent-true set
  is not the overlay set.
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md` S2 seeds an empty overlay for
  each of its four new roles, and `TOOL-dWitnessedBar-23` S4 seeds `tools/roles/house/gov-tester.md`:
  one overlay per role is the convention every role-adding spec follows.

### What the check ties

| Break | Seed rule's own includes (49 rev-1) | Roster slots (S1) |
|---|---|---|
| include removed, file kept | passes | reds naming the slot |
| role added, no overlay seeded | passes | reds naming the slot |
| overlay seeded for no role | passes | reds naming the file |

### Inventory

Minted: `derive_overlay_expected` (`py.function`), asked of
`python tools/lexicon/lexicon.py --suggest derive_overlay_expected --as py.function` at the pass.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 6, after unit 49 at order 5. `TOOL-dBoundRoles-16` holds order 6 and writes no
file this unit writes; `TOOL-dBoundRoles-55` shares the order, consumes from this unit and writes the same
file, so `--dispatch` holds it until this unit is CLOSED.

### Files touched (estimate)

- `tools/govkit/selftest.py`
- the spec of TOOL-dBoundRoles-49, a rev bump (S3), named here for the dispatch write set

### Alternatives rejected

- **One overlay per agent-true slot, the report's first option.** It reds at base on `gov-session`,
  which is not an agent and has an overlay (§8 F2).
- **The kit's tracked `house/*.md` files.** Independent of the seed rule, but a role added with no
  overlay file passes, the case the report's consequence names (§8 F2).

## 5. Production-readiness checklist

- security — no new write path; the selftest reads a scratch target it built.
- perf / scale — one roster load, already made by unit 37's derivation.
- error / empty / loading states — an empty set is unit 55's refusal; each S2 failure names its slot or
  file.
- observability — failures print both sets and the difference.
- risks — a future role that deliberately has no overlay reds S2; its spec then states why, and S1 is
  where the exception lives.
- testing — AC1 to AC3 by probe and grep; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a `python -c` slice puts `tools/govkit` on `sys.path`, imports govkit's self-test module
  as a library and runs no suite, the form unit 49 AC1 uses, and calls `derive_overlay_expected` on the
  installed roles kit of a default target, it returns one house overlay path per role file, ten at
  base; with a scratch kit copy carrying one more role file and no overlay, S2's compare names that
  slot.
  Red when: the expected side is read from the seed rule, so a role with no overlay passes.
  figure: the set is DERIVED from the roster at observation time.
  fixture: the target and the scratch kit copy are built under the run's scratch path by the probe.
- **AC2** — When the same probe removes the entry for `tools/roles/house/gov-builder.md` from the seed
  include of a scratch `kit.toml` while the file stays present and tracked and the role exists, S2's
  compare names `gov-builder`.
  Red when: dropping an include removes the overlay from both sides at once.
- **AC3** — When `grep -n 'TOOL-dBoundRoles-54' memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-49.md`
  runs, it prints a §9 line, and that spec's AC2 names the roster.
  Red when: unit 49's criterion still describes a check that compares the descriptor with itself.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the roster-side overlay compare, staged by restoring the expected side to the seed rule's includes, which turns AC2's dropped include green · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 49 carries no
  clause; veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Where does S3's expected side come from?** Options: (a) one overlay per role slot; (b) one per
  agent-true slot; (c) the kit's tracked `house/*.md` files. (b) reds at base on `gov-session`, so it
  fails a correct tree. (c) passes a role added with no overlay. (a) catches all three breaks of §4's
  table. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich survivor.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 45 to 51, id 14
  (HIGH, item H2, shared with id 40), on the report's fix with the expected side read from every role
  slot.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-60, the minors batch of the round-1 audit of units 52 to 58; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-64, the minors batch of the round-1 audit of units 61 to 63; nothing else moved.

## 10. Reuse audit

The seams are `TOOL-dBoundRoles-37`'s installed-kit roster load and `TOOL-dBoundRoles-49`'s
`derive_seed_expected`, both in `tools/govkit/selftest.py`; S1 reads the first and S2 compares with the
second. `python tools/codebase-map/reuse_lookup.py "expected house overlay set derived from the roster agent slots"`
ranked `roster`, `derive_baseline_additions`, `derive_clause_hash` and `derive_scope`, none an overlay
derivation, so no existing seam fits beyond the two named.

Recall terms used: `python tools/memory-recall/query.py "how is a seeded overlay count tied to the roles roster" --terms "house overlay seed rows planned_writes derive_roles_expected roster agent slot govkit selftest"`
