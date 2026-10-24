# TOOL-dDeclaredLoop-36 — the loop kit in govkit's default selection, so a default apply installs what roles requires

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 3 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-36-deviation-361.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-deviation-361.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md`)
confirmed finding **id 35 at HIGH**, its item **H12**, alone in that item. `TOOL-dDeclaredLoop-1` S4
gives the roles kit `requires` `loop` and S1 adds a `loop` registry entry, but nothing puts `loop` in
`[selection] default` of `tools/govkit/registry.toml`, which already holds `roles` (:38-54). `apply`
refuses a selection whose `requires` is unmet and never widens it (`tools/govkit/govkit.py:7551-7565`),
so every default `govkit apply` refuses with `'roles' requires 'loop'`; and `update` checks `requires`
only for a default-gained kit (:9240-9256), so an existing adopter updates to a roles kit that reads a
loop kit it does not have. This unit takes the report's fix. It repairs `TOOL-dDeclaredLoop-1`.

## 2. Scope (IN)

- **S1** — `"loop"` joins `[selection] default` in `tools/govkit/registry.toml`, on its own line above
  `"roles"`, with a comment naming this unit and the `requires` edge it satisfies. Observed by AC1, AC2.
- **S2** — The migration `TOOL-dDeclaredLoop-1` §4 states is corrected: `update` installs the loop kit
  through its default-gained path (`derive_default_gained`, `tools/govkit/govkit.py:976`), because the
  entry joined the default after the receipt's vintage; a `--kits`-scoped update gains nothing, as
  that path's comment says. `tools/loop/README.md`'s install section says so. This amends
  `TOOL-dDeclaredLoop-1` §4 Migration's "govkit installs loop first through `requires`", a sentence of
  a spec that no code reads. Observed by AC2.
- **S3** — The class, left-shifted: selfcheck 7b (`tools/govkit/govkit.py:2506-2516`) gains one arm,
  `derive_unsatisfied_requires(default_kits(reg), descs, None)` non-empty fails, naming each
  `(kit, dependency)` pair, so a default-selected kit whose `requires` leaves the default set reds
  `govkit selfcheck` before any adopter sees it. It reuses the predicate `apply` refuses by, so the
  check and the refusal are one answer. Observed by AC3.

## 3. Non-goals (OUT)

- A refusal in `update` for a claimed kit whose `requires` the receipt cannot satisfy on a
  `--kits`-scoped run: that path's scope is the operator's narrower statement, and its own comment
  says it gains nothing. Not named by the finding.
- The loop kit's runbook anchor for `govkit runbook parity`: the audit's id 38, batched into
  `TOOL-dDeclaredLoop-56`.
- The `unattended` kit's `requires` `loop` (`TOOL-dDeclaredLoop-5` S5): unattended is not in the
  default selection, so its own `--kits` request names loop or is refused, which is the intended
  behaviour.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-1` — the `loop` registry entry and the roles kit's `requires` `loop`; without them the default set would name no entry

## 4. Design

### Evidence

- `derive_unsatisfied_requires` is the one predicate `apply` refuses by and `plan` prints by
  (`tools/govkit/govkit.py:950-975`); passing the default set with no receipt asks exactly "does the
  default install refuse".
- Selfcheck 7b already walks `default_kits(reg)` to assert each member is a real entry
  (`tools/govkit/govkit.py:2509-2511`); the new arm sits beside it.
- `derive_default_gained` installs an entry that joined the default after the receipt's vintage and
  drops a gained entry whose `requires` it cannot satisfy (`tools/govkit/govkit.py:9240-9256`); with
  `loop` gained together with nothing it needs, it installs.

### Files touched (estimate)

- `tools/govkit/registry.toml`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/loop/README.md`

### Alternatives rejected

- **Dropping `requires` `loop` from the roles kit.** The roles adopter reads the order integers from
  the loop definition (`TOOL-dDeclaredLoop-1` S4), so the dependency is real and hiding it would
  install a roles kit that cannot bind its stages.
- **Letting `apply` widen a selection by `requires`.** The owner ruled a selection is the operator's
  statement of intent (`tools/govkit/govkit.py:7553-7555`).

## 5. Production-readiness checklist

- security — no new surface; one more kit in the default install, the same kit `roles` already needs.
- perf / scale — one more kit copied on a default apply.
- error / empty / loading states — the selfcheck arm names each unmet pair; an empty default set is
  already a refusal (`tools/govkit/govkit.py:1126`).
- observability — `update` prints its `default-gained loop` line, as for any gained entry.
- risks — an adopter that removed roles by hand still gains loop on update; loop requires nothing from
  roles, so it installs standalone.
- testing — AC1 to AC3 as probes on scratch targets; the arm under §7, observed at the close.
- migration — S2.
- user docs — `tools/loop/README.md`'s install section; `help/loop.md` is `TOOL-dDeclaredLoop-1`'s.

## 6. Acceptance criteria

- **AC1** — When a probe runs `python tools/govkit/govkit.py apply` with the default selection into a
  scratch target under `%TEMP%`, it exits 0 and the target's install receipt, `install.json`, claims both
  `loop` and `roles`.
  Red when: `loop` is absent from the default set, so apply refuses with `'roles' requires 'loop'`.
  fixture: a scratch git repository under a short `%TEMP%` path; the tree holds none.
- **AC2** — When the probe takes a scratch target applied at base `ed497191` and runs
  `python tools/govkit/govkit.py update` against the working tree, it prints `default-gained loop` and
  the receipt then claims `loop`.
  Red when: the update leaves roles at a version that reads a loop kit the target lacks.
  cost: two installs into scratch targets, seconds each.
- **AC3** — When `python tools/govkit/govkit.py selfcheck` runs over a scratch copy of the registry
  whose default set holds `roles` and not `loop`, it fails naming `'roles' requires 'loop'`; over the
  working tree it passes that arm.
  Red when: the arm reads the default set without the requires predicate, so the copy passes.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC3 · a default apply into a scratch target, and a registry copy whose default set omits `loop`, each staged against the base registry · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dDeclaredLoop-1`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, the
  precedent `TOOL-dTrueNorth-19` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 35 (HIGH, item H12).

## 10. Reuse audit

The seam is govkit's own requires predicate, `derive_unsatisfied_requires`
(`tools/govkit/govkit.py:950`), and selfcheck 7b's default-set walk (:2506); the fix is one registry line
and one arm calling the existing predicate, never a second requires reader.
`python tools/codebase-map/reuse_lookup.py "default selection requires a kit outside the default"`
listed `default_kits`, `derive_default_gained` and `derive_unsatisfied_requires` in
`tools/govkit/govkit.py` among its candidates, below the directory resolvers `kit_rel` and
`resolve_kit_dir`, which read no `requires`; the three were read above and agree with source.

Recall terms used: govkit default selection requires roles loop registry update default-gained selfcheck 7b
