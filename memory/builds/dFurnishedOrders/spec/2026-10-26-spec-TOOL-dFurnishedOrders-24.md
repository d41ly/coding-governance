# TOOL-dFurnishedOrders-24 — each work order's return schema rendered as one branch per outcome, the template's and each arm's, so a valid refused or probe return passes and a malformed one fails on its own fields

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 5ff43572 · streams tooling · order 9 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-23 TOOL-dFurnishedOrders-26 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 20 unit specs
(`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`)
confirmed finding **id 4 at HIGH**, report item **H2**. No other id shares it.

`TOOL-dFurnishedOrders-19` S4 renders a work order's return schema from "the role's composed
template", and that template carries alternative outcome arms: `TOOL-dFurnishedOrders-15` §4
"Rendered return" adds `- or outcome: refused — rule, remedy, actor …` and `- or outcome: probe —
subject, question, kind …` to every role, and `TOOL-dFurnishedOrders-7` adds `contradicted`. Unit 19's
type map has no row for an arm, and its closed `SCHEMA_KEYWORDS` holds no keyword that expresses
alternatives. If the template's non-optional fields are `required`, a valid refused or probe return
lacking `evidence` fails the schema and is retried until `roles.retries` is spent; if the arm fields
are left out, the arms go unvalidated. The builder would have to invent one of the two.

This unit renders the schema as one branch per outcome and admits `anyOf` to the closed set. It
repairs `TOOL-dFurnishedOrders-19` and builds one step after it (order 9).

## 2. Scope (IN)

- **S1** — The branches. `render_return_schema(role, rows)` (`tools/roles/roles_lib.py`,
  `TOOL-dFurnishedOrders-19` S4) returns `{"allOf": [<shared>], "anyOf": [<template branch>, <arm
  branch>…]}`, per §4 "The shape". The template branch requires the template's non-optional fields,
  typed by unit 19's type map, with `outcome` an `enum` of the template's own outcomes. Each arm
  `derive_return_arms` (`TOOL-dFurnishedOrders-15` S1) yields takes one branch: `outcome` a `const` of
  the arm's outcome, each of the arm's fields required as a non-empty string. Observed by AC1.
- **S2** — The shared part. `establishes`, and `upstream` when `rows` is not empty, sit in the one
  `allOf` member every branch shares, with unit 19's row pattern, `enum`, `maxItems` and `contains`
  unchanged, so a refused or probe return answers its handed rows as a template return does. Observed
  by AC1 and AC3.
- **S3** — The keyword. `SCHEMA_KEYWORDS` gains `anyOf`, and `check_return_schema` evaluates it: the
  object passes when at least one branch passes. When none passes, the failures reported are those of
  the branch whose `outcome` the object's `outcome` matches, so a refused return missing `remedy` is
  named by `remedy`; an `outcome` no branch admits is one failure naming the outcome and the admitted
  list. `oneOf`, `if` and every other keyword still raise `RolesError`. Observed by AC2 and AC4.
- **S4** — The arms' value sets stay where they are checked today: the refusal's `actor` set
  (TOOL-dBoundRoles-26 S2) and the probe's `kinds` (`TOOL-dFurnishedOrders-15` S2) are refused by
  `validate_return`'s arm checks, never by the schema, so one rule keeps one checker. Observed by AC3.
- **S5** — The docs: `tools/roles/README.md`'s paragraph on the per-order schema says each outcome is
  one branch and an arm's fields are required on its own outcome only. NOT OBSERVED by a criterion:
  prose, graded by the memory hygiene leg's link checks at the close.

## 3. Non-goals (OUT)

- The arm factory and the arm tables: `TOOL-dFurnishedOrders-15` S1 and S2, TOOL-dBoundRoles-26 and
  `TOOL-dFurnishedOrders-7` S2. A table added later takes a branch by S1 with no edit here.
- Where `establishes` is composed and how it renders in the role file: the minors batch
  `TOOL-dFurnishedOrders-29`, for id 5.
- Which properties the Python evaluator checks beside the parent's type checks: the minors batch
  `TOOL-dFurnishedOrders-29`, for id 32. This unit decides only how the alternatives are expressed.
- The harness route's `--part rows` line: `establishes` and `upstream` only, which every branch shares,
  so `addUpstreamSchema` (`TOOL-dFurnishedOrders-19` S8) is unchanged.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-15` — `derive_return_arms`, whose `(arm, outcome, fields)` triples S1 renders as one branch each (id 4)
- **consumes-from** `TOOL-dFurnishedOrders-19` — `render_return_schema`, `check_return_schema` and `SCHEMA_KEYWORDS`, which S1 to S3 extend with the outcome branches (id 4)
- **hands-off** `TOOL-dFurnishedOrders-29` — the outcome branches, which unit 29 S12 keeps out of `validate_return`'s own evaluation, rendering them for the order's block and the harness route only (id 32)
- **hands-off** `TOOL-dFurnishedOrders-31` — `[return.establishes]` and any field table, which unit 31 keeps out of the branches S1 builds one per arm, at the step after this one (id 1 of the second audit)
- **hands-off** `TOOL-dFurnishedOrders-37` — the `anyOf` evaluator, the shared `allOf` member's readers and S4's checkers, which unit 37 S11, S18 and S33 narrow, re-point and re-ground (ids 23, 27, 16 of the second audit)

## 4. Design

### The shape

```json
{"allOf": [{"type": "object", "required": ["establishes"],
            "properties": {"establishes": {"type": "array", "items": {"type": "string", "pattern": "<ROW_PATTERN>"}}}}],
 "anyOf": [{"type": "object", "required": ["outcome", "evidence"],
            "properties": {"outcome": {"enum": ["committed", "returned"]}, "evidence": {"type": "string"}}},
           {"type": "object", "required": ["outcome", "rule", "remedy", "actor"],
            "properties": {"outcome": {"const": "refused"}, "rule": {"type": "string", "minLength": 1},
                           "remedy": {"type": "string", "minLength": 1}, "actor": {"type": "string", "minLength": 1}}},
           {"type": "object", "required": ["outcome", "subject", "question", "kind"],
            "properties": {"outcome": {"const": "probe"}, "subject": {"type": "string", "minLength": 1},
                           "question": {"type": "string", "minLength": 1}, "kind": {"type": "string", "minLength": 1}}}]}
```

The template branch's fields are illustrative; each role's are its own. With `rows` given, the shared
member also requires `upstream`, carrying unit 19's property as it renders it today.

No branch sets `additionalProperties`, because a template's optional fields and an arm's fields share
one object's keys across branches; the parent's unknown-field check (TOOL-dBoundRoles-5 S1) keeps that
rule in one place.

### Why the matching branch names the failure

`anyOf` alone answers yes or no. A retry's reason needs the field: the branch picked by the object's
own `outcome` is the one its author meant, so its failures are the useful ones, and an outcome no
branch names is reported as such rather than as every branch's misses.

### Inventory

Minted: none. `anyOf` joins an existing closed set; S1 and S3 change two existing functions.

### Migration

None: no return is stored against a schema; the schema is rendered per order and evaluated once.

### Rollout

Live at landing. `KIT_ROLES_VERSION` moves for the kit epoch leg.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/README.md`

### Alternatives rejected

- **`oneOf`.** Exactly-one needs every branch evaluated and a tie rule; the `outcome` const already
  makes the branches disjoint, so `anyOf` is enough and the evaluator stays smaller.
- **`if` and `then` per arm.** Two keywords and a nesting the evaluator must also bound, for the same
  selection the `outcome` const gives.
- **Requiring only `outcome` and leaving every other field to the parent's check.** The arms would
  then be unvalidated by the schema the harness route hands the runtime, which is the second half of
  the defect.

## 5. Production-readiness checklist

- security — no new write path; the schema stays derived from the role file and the work order.
- perf / scale — one branch per outcome arm, three at base; evaluation stops at the first passing
  branch.
- error / empty / loading states — a failing return names its own branch's field, or its unknown
  outcome.
- observability — the retry reason names the field, as unit 19 S6's retry already carries it.
- risks — a role whose template outcome repeats an arm's outcome would make two branches admit it;
  `check_roles` already refuses that redeclaration (`TOOL-dFurnishedOrders-15` S1).
- testing — AC1 to AC4 by direct probes; the arm of §7 at the close.
- migration — none.
- user docs — `tools/roles/README.md` only; no user-facing step changes.

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `roles_lib.render_return_schema("gov-builder", [])`, the result's
  `anyOf` holds one branch whose `outcome` is an `enum` of `gov-builder`'s template outcomes and one
  branch per arm `roles_lib.derive_return_arms` returns, each with `outcome` as a `const`; its `allOf`
  requires `establishes`; with `["d#s1"]` the `allOf` member also requires `upstream`; and every
  keyword in it is in `roles_lib.SCHEMA_KEYWORDS`.
  Red when: the arms have no branch, so a refusal is checked against the template's fields.
- **AC2** — When `python -c` calls `roles_lib.check_return_schema` with the AC1 schema on a refused
  return carrying `rule`, `remedy`, `actor` and `establishes` `[]`, and on a probe return carrying
  `subject`, `question`, `kind` and `establishes` `[]`, each yields no failure; a refused return
  without `remedy` yields a failure naming `remedy`; and a return whose `outcome` is `shrugged` yields
  one failure naming that outcome.
  Red when: a valid refused or probe return fails, or a malformed one passes.
- **AC3** — When `python -c` calls `roles_lib.validate_return` for `gov-builder` on the AC2 refused
  return against a work order handing `d#s1`, the defects name `upstream · dropped · d#s1` and nothing
  about the template's fields; with `actor` set to `nobody`, a defect names the actor, raised by the
  arm check and not by the schema.
  Red when: a refusal is retried for lacking the template's `evidence`.
- **AC4** — When `python -c` calls `roles_lib.check_return_schema` on `{"anyOf": [{"type": "object"}]}`
  and `{}` it yields no failure, and on `{"oneOf": []}` it raises `RolesError` naming `oneOf`.
  Red when: the evaluator admits a keyword it does not implement, or rejects the one this unit adds.

## 7. Gates

`roles catalogue` · `roles render selftest` · `roles adopter self-test` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 AC3 AC4 · a planted refused, probe and template return against one order's schema, staged by rendering the template's required fields at the top level with no branches · none

## 8. Open questions

- **F1 — Which keyword expresses the alternatives?** Options: (a) `anyOf`, the `outcome` const making
  branches disjoint; (b) `oneOf`; (c) `if`/`then` per arm. (b) and (c) cost the evaluator more for the
  same verdicts on disjoint branches. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the skeptic's
  corrected fix in the report and the fewest keywords added to a closed set. widens: none · relaxes:
  none
- **F2 — Does the schema check an arm's value sets?** Options: (a) presence and non-empty string only,
  the sets left to `validate_return`'s arm checks; (b) the sets as `enum`s in each branch. The refusal's
  `actor` admits `build:<slug>`, a pattern no closed set holds, and two checkers of one set disagree
  when one moves. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, one rule one checker.
  widens: none · relaxes: none
- **F3 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-26,
  delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent `TOOL-dBoundRoles-39`
  §8 F1 records. widens: none · relaxes: none
- **F4 — The units this one extends are unbuilt.** `TOOL-dFurnishedOrders-15` and `-19` are specced
  and unbuilt at `5ff43572`. RESOLVED (agent, 2026-10-26, delegated): the build run re-grounds on each
  at the pass and stops this unit if a named section is still absent then, rung 1, the brief's rule for
  unbuilt parents. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 20 unit specs, id 4
  (HIGH, item H2).
- rev-2 · 2026-10-26 · §3 · hands-off edges to units 31 and 37, the second spec audit's promotions
  for ids 1, 23, 27 and 16.

## 10. Reuse audit

The seams extended: `render_return_schema` and `check_return_schema` with their closed
`SCHEMA_KEYWORDS` (`TOOL-dFurnishedOrders-19` S4 and S5), and `derive_return_arms`
(`TOOL-dFurnishedOrders-15` S1), the one source of the arms. `python tools/codebase-map/reuse_lookup.py
"evaluate a JSON schema with alternative branches per return outcome"` ranked `branches`
(`tools/memory-tree/check-arms.py`), `render_json` (`tools/policy/policy.py`) and `classify_outcome`
(`tools/govkit/govkit.py`), none a schema evaluator, so no existing seam fits beyond the two named;
no JSON Schema package is added (unit 19's veto-2 ruling). The recall probe returned
`TOOL-dFurnishedOrders-15`, the audit's H2 text and scout C's row on the refusal arm, none disagreeing
with source.

Recall terms used: `python tools/memory-recall/query.py "how are alternative outcome arms of a role
return validated" --terms "return arms refused probe contradicted outcome anyOf schema validate_return
derive_return_arms template"`
