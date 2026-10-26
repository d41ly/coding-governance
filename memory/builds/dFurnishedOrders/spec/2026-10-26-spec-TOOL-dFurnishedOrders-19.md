# TOOL-dFurnishedOrders-19 — every role return declaring the rows it establishes, and each work order's return schema rendered from its own rows, so a dropped, invented or doubled row fails the return and is retried

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 2193e25d · streams tooling · order 8 · advances TOOL-dFurnishedOrders-21

**Carries:** cl-dClosedLoop-0210@c44de500 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-b.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-20 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-20 |
| [2026-10-26-build-TOOL-dFurnishedOrders-19-deviation-191.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-19-deviation-191.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-20 |
| [2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-16 |

<!-- /gen:spec-records -->

## 1. Goal

Returns declare nothing they establish for the next step, and a static return schema passes a
dropped, an invented and a doubled row (gap-roles-29,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:181`). The prior
art's probe measured it: a static schema passed all three, while a schema rendered per work order,
the order's row ids its only allowed values and each one required, refused all three
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-research-handoffs-prior-art.md:237-245`).
The owner's NT-10 made it the contract: each role return declares what it establishes, the next
work orders hand those on as upstream rows, and each order's return schema is rendered from its own
rows, so a bad row fails the return and is retried
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:313-317`).
TOOL-dDeclaredLoop-29 ships the row grammar, the hand-on and a join that refuses only on a
`measured` edge; TOOL-dBoundRoles-5 ships the per-role check and its retry. Each leaves the
per-order schema to the other (TOOL-dDeclaredLoop-29 §3, TOOL-dBoundRoles-5 §3); this unit builds it.

## 2. Scope (IN)

- **S1** — The establishes arm (shared interface J18). `tools/roles/role-schema.toml` gains the table
  `[return.establishes]`, declaring the field `establishes:list`, composed into every role's
  `return` template by `derive_return_arms` (J3, TOOL-dFurnishedOrders-15 S1, the brief's
  `compose_return_arms` respelled for the lexicon). Each member is one row line,
  `<row id> · <kind> · <text>`, TOOL-dDeclaredLoop-29 S3's row without its `- ` marker, the kind
  one of `seam`, `criterion`, `interface`, `fork`, `finding`, `repair`. Every agent file shows the
  arm once `render_agents.py --write` re-renders `.claude/agents/`. Observed by AC6.
- **S2** — The rows read. `read_establishes(text)` in `tools/roles/roles_lib.py` returns a return's
  rows: its JSON object's `establishes` list, else the lines of its `## Establishes` section.
  `validate_return` (TOOL-dBoundRoles-5 S1) calls it and adds one defect per row off the grammar,
  per kind outside the six, and per row id repeated within the return. Observed by AC6.
- **S3** — The handed rows read. `read_upstream_rows(work_order)` in `roles_lib.py` returns the ids
  of the `### upstream:rows` block TOOL-dDeclaredLoop-29 S5 renders, each `<item>#<row id>`, in
  order; a work order with no such block hands none. Observed by AC1.
- **S4** — The per-order schema. `render_return_schema(role, rows)` in `roles_lib.py` returns a JSON
  Schema (draft-07, the Agent SDK's draft) for one work order: the role's composed template, each
  type mapped by §4's table, `establishes` an array of strings held to the row pattern, and, when
  `rows` is not empty, a required `upstream` array whose items are `{id, answer, reason}` objects,
  `id` an `enum` of exactly `rows`, `answer` one of `used`, `bypassed`, `not-applicable`, `reason` a
  non-empty string, `maxItems` the count of `rows`, and one `contains`/`const` per row id. It emits
  only the keywords of `SCHEMA_KEYWORDS`. Observed by AC1.
- **S5** — The schema checked. `check_return_schema(schema, obj)` in `roles_lib.py` evaluates
  `SCHEMA_KEYWORDS` and refuses any other keyword with a `RolesError` naming it, so the renderer and
  the evaluator cannot drift. `validate_return(role, text, root, work_order)` renders the order's
  schema from `read_upstream_rows(work_order)` and evaluates the return against it, naming each
  upstream failure by its class word, `upstream · <class> · <id>`, in TOOL-dDeclaredLoop-29 S6's
  five classes (§4 "Naming the class"). A defect fails the return on every
  edge, `record` and `measured` alike (§8 F1). Observed by AC2,
  AC3, AC4 and AC5.
- **S6** — Retried as `roles.retries` says. The defects of S2 and S5 are `validate_return`'s, so
  TOOL-dBoundRoles-5 S3's `check-return` blocks the stop and re-asks while the attempts are fewer
  than `roles.retries`, naming each defect; this unit adds no retry path. Observed by AC7.
- **S7** — The order carries its schema. `render_handoff` (`tools/roles/handoff.py:312`) writes a
  `### return-schema` block, the S4 schema as one fenced `json`, inside `## Task` after the row
  contract, so the task-sha covers it. `python handoff.py return-schema --role <slot> [--upstream
  <rows file>] [--part rows]` prints the schema as one JSON line, or with `--part rows` only its
  `establishes` and `upstream` properties, for a caller that cannot read files. Observed by AC8.
- **S8** — The unit harness. `tools/workflows/unattended-unit.js` takes the optional argument
  `returnRows`, the `--part rows` line; `addUpstreamSchema(schema, returnRows)` adds its properties
  to `UNIT_SCHEMA` (`unattended-unit.js:206-216`) and to its `required` list, and a `returnRows`
  that is not an object holding an `establishes` array schema throws before any agent. Absent, the
  schema is `UNIT_SCHEMA` as at base and one log line says so, as an absent `efforts` key is logged.
  A return the runtime refuses comes back null and is re-run by TOOL-dBoundRoles-5 S6's
  `spawnWithRetries` under `retries`. The build harness's dispatch row
  (`tools/workflows/unattended-build.template.js:2460-2490`) names the `return-schema` command the
  main loop runs before each unit's call. Observed by AC9.
- **S9** — The docs: `tools/roles/README.md`'s handoff section, `tools/workflows/README.md`'s unit
  harness arguments and `help/roles.md`'s "How a task reaches an agent" name the rows and the
  per-order schema. NOT OBSERVED by a criterion: prose, graded by the memory hygiene leg's link
  checks at the close.

## 3. Non-goals (OUT)

- The `upstream` field, the row grammar's section form, `derive_upstream_rows`, the `### upstream:rows`
  block and `join_upstream`: TOOL-dDeclaredLoop-29 S1 to S8. Its join still classes and records
  every answer, and a `bypassed` answer stays a finding that gates only on a `measured` edge.
- Which items hand which rows: each owning build's population (TOOL-dDeclaredLoop-29 §3).
- The build and review harnesses' other stages. None is cut from a work order carrying upstream
  rows at base, so each keeps its static schema until TOOL-dBoundRoles-3's work order cuts it (§8
  F2).
- Writing a JSON return's rows into the trail as a `## Establishes` section: the return's writer is
  dWellOiledMachine's (TOOL-dDeclaredLoop-29 §3).
- The repair arm and the problem rows: TOOL-dFurnishedOrders-7 and TOOL-dFurnishedOrders-20 declare
  and hand them through this unit's schema.
- A JSON Schema library: the evaluator is the closed keyword set, so no external dependency lands.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-15` — `derive_return_arms`, the brief's `compose_return_arms` respelled for the lexicon, which composes the `[return.establishes]` arm into every role's template; without it the arm is a table no template carries
- **hands-off** `TOOL-dFurnishedOrders-7` — `render_return_schema`, through which a return's `repair` rows are declared and an order's handed repairs are each required once
- **hands-off** `TOOL-dFurnishedOrders-20` — `render_return_schema`, through which the problems handed as `problem#<problem id>` rows are allowed values each required once
- **consumes-from** external — TOOL-dDeclaredLoop-29 S3 to S6 (the row grammar, the `### upstream:rows` block, `join_upstream`) and TOOL-dBoundRoles-5 S1, S3 and S6 (`validate_return`, the retry, `spawnWithRetries`), specced and DEFERRED at base `2193e25d`
- **hands-off** `TOOL-dFurnishedOrders-24` — `render_return_schema`, `check_return_schema` and `SCHEMA_KEYWORDS`, which unit 24 extends with one branch per outcome (id 4)
- **hands-off** `TOOL-dFurnishedOrders-29` — `validate_return`'s schema evaluation and the establishes arm, which unit 29 S12, S13 and S30 settle (ids 32, 33, 5)
- **hands-off** `TOOL-dFurnishedOrders-30` — `returnRows` and `addUpstreamSchema`, whose rows unit 30 S9 checks in-script (id 28)

## 4. Design

### The type map

| Template type (TOOL-dBoundRoles-2 S4) | Schema |
|---|---|
| `text`, `path` | `{"type": "string"}` |
| `sha` | `{"type": "string", "pattern": "^[0-9a-f]{7,40}$"}` |
| `list` | `{"type": "array"}` |
| `int` | `{"type": "integer"}` |
| a closed set | `{"enum": [...]}` |
| `establishes:list` | `{"type": "array", "items": {"type": "string", "pattern": ROW_PATTERN}}` |

`ROW_PATTERN = ^[a-z0-9][a-z0-9-]* · (seam|criterion|interface|fork|finding|repair) · \S.*$`, one
segment of the tag grammar for the id, as TOOL-dDeclaredLoop-29 S3 states. An optional entry (`?`)
is left out of `required`.

`SCHEMA_KEYWORDS = type enum const pattern minLength required properties additionalProperties items
maxItems contains allOf`, every keyword S4 emits and S5 evaluates.

### One order's `upstream` property

```json
{"type": "array", "maxItems": 2,
 "items": {"type": "object", "required": ["id", "answer", "reason"], "additionalProperties": false,
           "properties": {"id": {"enum": ["design.seams#s1", "design.seams#s2"]},
                          "answer": {"enum": ["used", "bypassed", "not-applicable"]},
                          "reason": {"type": "string", "minLength": 1}}},
 "allOf": [{"contains": {"properties": {"id": {"const": "design.seams#s1"}}}},
           {"contains": {"properties": {"id": {"const": "design.seams#s2"}}}}]}
```

With `maxItems` equal to the row count and each row contained, every row is answered exactly once: a
doubled row with every other row present exceeds `maxItems`, and one standing in for a missing row
fails that row's `contains`. This is the probe's shape (`research-handoffs-prior-art.md:239`).

### Naming the class

The evaluator's raw failures name a keyword; `validate_return` names the class a reader acts on, from
the answered ids against `rows`: an id of `rows` answered zero times is `dropped`, an answered id not
in `rows` is `invented`, an id answered twice is `doubled`, an answer outside the three words is `bad-answer`, and an empty
reason is `no-reason`. These are TOOL-dDeclaredLoop-29 S6's words,
so the retry's reason and the join's record speak one vocabulary.

### A markdown return

A return without a JSON block answers in TOOL-dDeclaredLoop-29 S5's `## Upstream` section; its lines,
`- <row id> · <answer> · <reason>`, are read into the same objects before the evaluator runs, so both
forms meet one schema.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_establishes`, `read_upstream_rows`, `render_return_schema`, `check_return_schema` | functions, `roles_lib.py` | `py.function`, OK |
| `SCHEMA_KEYWORDS`, `ROW_PATTERN` | constants, `roles_lib.py` | no constant cell is declared |
| `[return.establishes]` | arm table, `role-schema.toml` | none |
| `return-schema`, `--part rows` | verb and flag, `handoff.py` | none |
| `### return-schema` | work-order block head | none |
| `addUpstreamSchema` | function, `unattended-unit.js` | `js.function`, OK |
| `returnRows` | harness argument | none |

### Migration

A role's return written before this unit carries no `establishes` field; from landing every
template requires it, so a stale agent file is re-rendered by `render_agents.py --write` in the same
commit. An order with no handed rows renders no `upstream` property, and its schema differs from the
static one by the `establishes` field alone.

### Rollout

Live at landing on the direct route, through `check-return`. On the harness route it is live where the
caller passes `returnRows`. `KIT_ROLES_VERSION` and the workflows kit's `version:` in
`tools/workflows/tier2-review.template.js` move for the kit epoch leg.

### Files touched (estimate)

- `tools/roles/role-schema.toml`
- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/README.md`
- `.claude/agents/` and `.claude/roles.json`, re-rendered by `tools/roles/render_agents.py --write`
- `tools/workflows/unattended-unit.js`
- `tools/workflows/unattended-build.template.js`, rendered to `tools/workflows/unattended-build.js`
- `tools/workflows/tier2-review.template.js`, rendered to `tools/workflows/tier2-review.js` (the
  kit's version line only)
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/README.md`
- `help/roles.md`

### Alternatives rejected

- **Validating with a JSON Schema package.** It is a new external dependency (veto 2); the keyword
  set S4 emits is twelve words.
- **One schema object with the row ids as property names.** A JSON parser keeps the last of two equal
  keys, so a doubled row would vanish before any check saw it.

## 5. Production-readiness checklist

- security — no new write path; the schema is derived from the work order the renderer already
  writes, and the row text is never executed.
- perf / scale — one schema render per order and one evaluation per return, linear in the rows.
- error / empty / loading states — an order with no rows renders no `upstream`; a schema keyword
  outside the set raises naming it.
- observability — each defect names its class and row id, in the retry's reason and the return-check
  record.
- risks — a role's return now fails where it passed before, on every edge; the retry bounds the
  cost, and the last attempt's return still reaches `join_upstream`'s record.
- testing — AC1 to AC10 by direct probes and scratch fixtures; the arms of §7 at the close.
- migration — the agent files re-rendered in the landing commit.
- user docs — `help/roles.md` (S9).

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `roles_lib.render_return_schema("gov-builder", ["d#s1", "d#s2"])`,
  the result's `upstream` property carries `maxItems` 2, an `id` enum of exactly `d#s1` and `d#s2`
  and two `contains` entries, `required` names `upstream` and `establishes`, and every keyword in
  it is a member of `roles_lib.SCHEMA_KEYWORDS`; with `[]`, the result carries no `upstream`.
  Red when: the schema is the static one, which passes every planted return below.
- **AC2** — When `python -c` calls `roles_lib.validate_return` for `gov-builder` on a return that
  answers only `d#s1`, against a scratch work order whose `### upstream:rows` block hands `d#s1` and
  `d#s2`, the defects include `upstream · dropped · d#s2`.
  Red when: a planted dropped row passes the return.
- **AC3** — When the AC2 return answers `d#s1`, `d#s2` and `d#s9`, the defects include
  `upstream · invented · d#s9`.
  Red when: a planted invented row passes the return.
- **AC4** — When the AC2 return answers `d#s1` twice and not `d#s2`, the defects include
  `upstream · doubled · d#s1` and `upstream · dropped · d#s2`.
  Red when: a planted doubled row passes the return.
- **AC5** — When the AC2 return answers each row once, with a reason, it carries no `upstream` defect;
  and when its work order is cut for a `record` edge, AC2 to AC4 read the same.
  Red when: a well-formed return is refused, or a `record` edge lets a bad row through.
- **AC6** — When `validate_return` reads a return whose `establishes` holds `a · widget · t`, the
  defects name the kind; with `a · seam · t` twice, they name the doubled id `a`; with no
  `establishes` field, they name the required field; and `grep -c 'establishes' gov-builder.md` in
  `.claude/agents/` prints at least 1.
  Red when: a role return declares nothing it establishes and passes.
- **AC7** — When `python handoff.py check-return` reads a `SubagentStop` payload whose return is the
  AC2 return and whose transcript's first user record is the AC2 work order, with attempts below
  `roles.retries`, it prints a `block` decision whose reason names `upstream · dropped · d#s2`.
  Red when: the failed return is accepted instead of retried.
  fixture: TOOL-dBoundRoles-5's `check-return`, built before this unit by the chain's order.
- **AC8** — When `python handoff.py render --role gov-builder --build tFix --unit TOOL-tFix-1
  --upstream <a scratch rows file> --stdout` runs, its task carries a `### return-schema` block whose
  JSON equals `render_return_schema`'s output for those rows; and `python handoff.py return-schema
  --role gov-builder --part rows --upstream <the same file>` prints one JSON line holding exactly
  `establishes` and `upstream`.
  Red when: the order and the harness route render two different schemas for one set of rows.
- **AC9** — When `node` runs `unattended-unit.js` in a `vm` context with the AC8 `--part rows` line as
  `returnRows`, the schema passed to the stub `agent` requires `establishes` and `upstream` and carries
  the enum; with `returnRows` set to `{"x": 1}`, it throws naming `returnRows`; with none, the schema
  equals `UNIT_SCHEMA` and the log names the absence.
  Red when: the harness route keeps a static schema though the caller handed rows.
- **AC10** — When `python -c` calls `roles_lib.check_return_schema` on the schema `{"oneOf": []}`, it
  raises `RolesError` naming `oneOf`.
  Red when: the evaluator silently passes a keyword it does not implement.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `policy fixtures` · `check-wiring self-test` · `lexicon naming predicates` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `workflow script syntax` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC8 AC10 · a scratch work order handing two rows, and a planted return of each kind against it · none
New arm: tools/workflows/unattended-build.test.sh · covers AC9 · the unit harness evaluated with a rows line, a malformed one and none · none

## 8. Open questions

- **F1 — Does a bad row fail the return on a `record` edge?** TOOL-dDeclaredLoop-29 S6 records a
  dropped, invented or doubled row as a finding on a `record` edge and refuses only on a `measured`
  one; the clause fails the return and retries it. Options: (a) the schema failure on every edge,
  `bypassed` still gating by measurement; (b) the parent's split. The night pass two states both
  halves, "a dropped, invented or doubled row fails the return and is retried" and "rows gate only
  where a measurement passed", the second of a `bypassed` row (`night-pass-two.md:316-317`). (b) fails
  AC5's `record` half, the clause's own case (veto 1). RESOLVED (agent, 2026-10-26, delegated): (a),
  rung 1, the clause and v2's chain row; stricter than the parent, so deviation 191 records it.
  widens: none · relaxes: none
- **F2 — Which harness stages carry the per-order schema?** Options: (a) every schema-bearing stage
  of the three harnesses; (b) the unit harness's builder, the one stage a caller hands a work
  order's rows, with the direct route covering every role. No build or review stage is cut from a
  work order carrying rows at base, so (a) adds no criterion (b) misses and nine schemas a Workflow
  script cannot derive from a template it cannot read. RESOLVED (agent, 2026-10-26, delegated): (b),
  rung 3, tie-broken by reuse of the seam M5 found, `validate_return`'s retry. widens: none ·
  relaxes: none
- **F3 — The parents this unit calls.** S2, S5, S6 and S8 extend TOOL-dBoundRoles-5 S1, S3 and S6,
  S3 and the markdown form read TOOL-dDeclaredLoop-29 S3 and S5, and S1 rides
  TOOL-dFurnishedOrders-15's `derive_return_arms`; all are unbuilt at base. RESOLVED (agent,
  2026-10-26, delegated): the build run re-grounds on each named section and stops this unit if one
  is still absent then, rung 3, the brief's parent rule. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 19, the brief's J3 and J18 and D5,
  scout B's row for cl-0210, night-pass-two.md's point 4, the prior art's probe 1, and the source at
  `2193e25d`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullets mirroring TOOL-dFurnishedOrders-24, TOOL-dFurnishedOrders-29, TOOL-dFurnishedOrders-30, promoted from the round-1 spec audit (`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended are TOOL-dBoundRoles-5's `validate_return` and its retry, the one check of a
role's return and the one retry route, which this unit feeds rather than duplicates; TOOL-dBoundRoles-2
S4's template and `parse_return_template`, which the type map reads; TOOL-dFurnishedOrders-15's
`derive_return_arms`, which carries the new arm; `render_handoff` (`tools/roles/handoff.py:312`);
and the unit harness's `UNIT_SCHEMA` (`tools/workflows/unattended-unit.js:206`). `python
tools/codebase-map/reuse_lookup.py "validate a role return against a schema rendered per work order
from its upstream rows"` ranked `rows`, `row` and `extract_row` (test helpers and the backlog's row
reader), `load_roles` and `render_role` (`roles_lib.py`) and `validate` (`tools/policy/policy.py`,
the policy file's value check, not a JSON Schema); no per-order schema or JSON Schema evaluator
exists, so S4 and S5 are new and sit beside the check they feed. The recall probe returned scout
B's row, TOOL-dBoundRoles-5 and TOOL-dBoundRoles-17; scout B's `UNIT_SCHEMA :206` and
`FINDING_SCHEMA :630` agree with source, and TOOL-dBoundRoles-5 §3's hand of the per-order schema to
TOOL-dDeclaredLoop-29 disagrees with that unit's §3, which hands it back, the gap §1 names.

Recall terms used: `python tools/memory-recall/query.py "how is a role return validated against the
rows its work order handed" --terms "establishes upstream rows return schema per work order dropped
invented doubled validate_return roles.retries join_upstream"`
