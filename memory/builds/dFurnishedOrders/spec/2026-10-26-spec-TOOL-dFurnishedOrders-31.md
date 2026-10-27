# TOOL-dFurnishedOrders-31 — a field table is no outcome arm: `derive_return_arms` yields only tables carrying `outcome`, so every branch of the per-order schema names an outcome from the step unit 24 builds at

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 8c395e3c · streams tooling · order 10 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-31-deviation-311.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-31-deviation-311.md) | deviation | — |
| [2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-35 TOOL-dFurnishedOrders-36 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 TOOL-dFurnishedOrders-37 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, report item **H1**. No other id shares it.

`TOOL-dFurnishedOrders-24` (order 9) gives every arm `derive_return_arms` yields one `anyOf` branch
whose `outcome` is a `const`. At order 9 that factory still yields `TOOL-dFurnishedOrders-19`'s
`[return.establishes]` table (order 8), which declares the field `establishes:list` and no outcome
(spec-19 S1; spec-15 S1 returns one triple "per table"). The only filter is
`TOOL-dFurnishedOrders-29` S30, "`derive_return_arms` reads only tables carrying `outcome`", at
order 22. Between the two steps a faithful build emits a branch with no outcome `const`, which a
return carrying only `establishes` passes while missing every template field.

This unit lands S30's rule, both of its halves, at the step after unit 24, so the branch set is right
from order 10 rather than from order 22. It repairs `TOOL-dFurnishedOrders-24` and builds one step
after it (order 10).

## 2. Scope (IN)

- **S1** — The filter. `derive_return_arms(schema)` (`tools/roles/roles_lib.py`,
  `TOOL-dFurnishedOrders-15` S1) returns a triple only for a `[return.<name>]` table that declares
  `outcome`. A table that declares fields and no `outcome` is a field table: it yields no arm, so
  `render_return_schema` (`TOOL-dFurnishedOrders-24` S1) gives it no branch. Observed by AC1.
- **S2** — The field table's render. `render_role` appends each field of a field table to the role's
  own template line, so `establishes:list` is a field of every outcome and no `- or outcome:` line
  names it; `render_agents.py --write` re-renders `.claude/agents/`. Observed by AC2.
- **S3** — The branch invariant observed on the real schema. With `[return.establishes]` present in
  `tools/roles/role-schema.toml`, every member of `anyOf` carries an `outcome` that is a `const` or
  an `enum` of non-empty strings, and a return carrying only `establishes` fails the rendered
  schema. Observed by AC1.

## 3. Non-goals (OUT)

- The branch shape, the shared `allOf` member and the `anyOf` keyword: `TOOL-dFurnishedOrders-24`'s,
  unchanged.
- The establishes rows, their pattern and their check: `TOOL-dFurnishedOrders-19` S1 and S2,
  unchanged.
- `TOOL-dFurnishedOrders-29` S30's text. That unit's pass finds S30 landed here and records it so,
  as its §4 "How an item closes" states.
- The report's left-shift gate, a spec-lint over the README's order column: no clause of this build
  names it.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-24` — `render_return_schema`'s one branch per arm, which S1 stops a field table from entering (id 1)
- **hands-off** `TOOL-dFurnishedOrders-29` — S30, landed here whole at order 10, which unit 29's pass finds present and records as closed (id 1)
- **hands-off** `TOOL-dFurnishedOrders-42` — S2's template-line render and AC1's arm assertions, which unit 42 S12 grounds and S13 completes (ids 11, 35 of the third audit)

## 4. Design

### Arms and field tables

```
[return.refused]      outcome = "refused", fields ...   -> arm   -> one anyOf branch, outcome const
[return.probe]        outcome = "probe",   fields ...   -> arm   -> one anyOf branch, outcome const
[return.establishes]  fields = ["establishes:list"]     -> field table -> no branch;
                                                           establishes:list on the template line,
                                                           and in the shared allOf member (unit 24 S2)
```

The test is the table's own declaration, never its name, so a later field table needs no edit here
and a later arm table takes its branch by unit 24 S1.

### Why this lands at order 10 and not inside unit 24

Unit 24 is specced and audited; its text is not rewritten by another unit. Its pass at order 9 meets
the field table and builds against what `derive_return_arms` yields then; its ledger answers AC1 in
the form its pass observed, naming this unit. This unit closes the defect at the next step, so no
later unit builds on a branch without an outcome.

### Inventory

Minted: none. S1 adds one condition to `derive_return_arms`; S2 one branch to `render_role`.

### Migration

None: the schema is rendered per order and no return is stored against it.

### Rollout

Live at landing. `KIT_ROLES_VERSION` moves for the kit epoch leg.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/adopt-roles.test.sh`
- `.claude/agents/` (renders, by `render_agents.py --write`)

### Alternatives rejected

- **Refuse a table with no outcome in `render_return_schema`.** It would refuse the one field table
  this build ships, so every order's render would fail.
- **Skip the table by its name `establishes`.** A typed name beside the schema that declares it; a
  second field table would become an arm again.

## 5. Production-readiness checklist

- security — no new write path; the schema stays derived from the role schema and the work order.
- perf / scale — one dictionary lookup per table.
- error / empty / loading states — a schema with no arm table renders the template branch alone, as
  unit 24 renders it.
- observability — the rendered schema and the role file show the field once, on the template line.
- risks — a field table a later unit adds without an `outcome` renders as fields, which is the
  intended reading; an arm table that forgets `outcome` would render as fields, and AC1's arm count
  shows it.
- testing — AC1 and AC2 by probes; the arm of §7 at the close.
- migration — none.
- user docs — none: no user-facing step changes, and `tools/roles/README.md`'s per-order paragraph is
  unit 24's.

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `roles_lib.derive_return_arms` over the roles kit's `role-schema.toml`
  holding `[return.establishes]`, no triple names `establishes`; and when it calls
  `roles_lib.render_return_schema("gov-builder", [])`, every member of `anyOf` carries an `outcome`
  property that is a `const` or an `enum` of non-empty strings, and `roles_lib.check_return_schema`
  on `{"establishes": []}` yields at least one failure.
  Red when: the field table takes a branch with no outcome, so an establishes-only return passes.
- **AC2** — When `python tools/roles/render_agents.py --write` runs, `.claude/agents/gov-builder.md`'s
  template line holds `establishes:list`, and `grep -c "or outcome: establishes"` over it prints 0.
  Red when: a field renders as an outcome arm, or vanishes from the role file.

## 7. Gates

`roles catalogue` · `roles render selftest` · `roles render wiring` · `roles adopter self-test` · `check-wiring self-test` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 · the shipped role schema with its field table, staged by dropping S1's `outcome` condition so the field table takes a branch · none

## 8. Open questions

- **F1 — Where does the field-table rule land?** Options: (a) a unit at order 10, the step after unit
  24; (b) a rewrite of unit 24 S1; (c) leave it in unit 29 S30 at order 22. (b) rewrites an audited
  spec from outside it; (c) is the defect. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  disposal rule's placement one step after the repaired unit. widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-26,
  delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent `TOOL-dBoundRoles-39`
  §8 F1 records. widens: none · relaxes: none
- **F3 — The units this one extends are unbuilt.** `TOOL-dFurnishedOrders-15`, `-19` and `-24` are
  specced and unbuilt at `8c395e3c`. RESOLVED (agent, 2026-10-26, delegated): the build run
  re-grounds on each at the pass and stops this unit if a named section is still absent then, rung 1,
  the brief's rule for unbuilt parents. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the spec audit of the round-1 promotions, id 1
  (HIGH, item H1).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet(s) mirroring TOOL-dFurnishedOrders-42, promoted from the spec audit of the round-2 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: `derive_return_arms` (`TOOL-dFurnishedOrders-15` S1), the one source of the arms,
and `render_role`'s template line (`tools/roles/roles_lib.py:604`), where every role field already
renders. `python tools/codebase-map/reuse_lookup.py "evaluate a JSON schema with alternative branches
per return outcome"` ranked `branches` (`tools/memory-tree/check-arms.py`), `render_json` and
`classify_outcome`, none an arm factory, so no existing seam fits beyond the two named. The recall
probe returned unit 29's S30 row and the audit's H1 text, neither disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "how are alternative outcome arms of a role
return validated" --terms "return arms refused probe outcome anyOf schema field table establishes
derive_return_arms render_role"`
