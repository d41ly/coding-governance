# TOOL-dFurnishedOrders-7 — a false handed fact repaired in the return and filed as an ask against its producer's record, routed by `roles.on-contradiction` through the refusal outcome table

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 2193e25d · streams tooling · order 9 · advances TOOL-dFurnishedOrders-21

**Carries:** cl-dClosedLoop-0198@9197dfef whole
**Carries:** node:policy-key.roles.on-contradiction

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-a.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-fix-return.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-fix-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 |
| [2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-16 |

<!-- /gen:spec-records -->

## 1. Goal

A role that finds a handed fact false has no record and no route today: only the builder's `diverged`
routes back, no return can record a repair, and nothing files one against the producer's record
(`gap-roles-17`, gap register line 169). P29's item 7 (`layer-roles.md:290-313`, settled as F3-4,
`:620-636`) asks for three things this unit builds: the repair recorded in the return as the fact as
handed, the fact as found and the key of what was read; the repair filed by the driver as an ask
against the producer's record; and `roles.on-contradiction` choosing between that default
(`repair-and-record`), stopping with `contradicted` (`return`) and parking for the owner (`ask`). The
route rides TOOL-dBoundRoles-26's refusal outcome table, never a second one.

## 2. Scope (IN)

- **S1** — The repair grammar (shared interface J10): `REPAIR_RE` and `parse_repair_line(text)` in
  `tools/roles/roles_lib.py`, the one reader of `handed=<key> · found=<one line> · read=<key>`, each
  key one of TOOL-dBoundRoles-13 S1's three forms (`blob:`, `record:`, `cmd:`), `found` non-empty,
  one line and free of the ` · ` separator. It returns `{handed, found, read}` or raises naming the
  field. Observed by AC1.
- **S2** — The arm `[return.repair]`, one table in `tools/roles/role-schema.toml` composed into every
  role's `return` template by TOOL-dFurnishedOrders-15's `derive_return_arms` (J3): the outcome
  `contradicted` with the fields `handed`, `found` and `read`, and the row kind `repair` whose text is
  S1's grammar. A return's repairs are `repair` rows of its `## Establishes` block in
  TOOL-dFurnishedOrders-19's grammar (J18), so the schema `render_return_schema` renders admits them.
  `validate_return` (TOOL-dBoundRoles-5 S1) refuses a `contradicted` return missing a field and a
  `repair` row whose text S1 refuses, naming the field or the row id. Observed by AC2 and AC3.
- **S3** — The bounds rendered with the arm: one line under the composed template stating that a
  repair whose correction would change what the role was asked to produce is a divergence, returned
  as `diverged`, and that a repair changes no record but the role's own return (item 7's "Mandate" and
  "Records"). Observed by AC3.
- **S4** — The route, `derive_repair_route(repair, value, producer)` in `roles_lib.py`: it maps the
  policy value to an actor of TOOL-dBoundRoles-26 S3's `REFUSAL_ROUTES` and answers through that
  unit's `route_refusal`, per §4 "The route". `roles.on-contradiction` is read through `resolve`
  (`tools/policy/policy.py:752`) located by `roles_lib.resolve_kit_dir`, never with `tomllib` (J1).
  Observed by AC4.
- **S5** — The producer, `derive_repair_producer(key, memory_root, build)`: a `blob:` or `record:` key
  whose path lies under `<MEMORY_ROOT>/builds/<slug>/` names that build; any other key names the work
  order's own build, the marker's `build=`. Observed by AC4.
- **S6** — The verb `python tools/roles/handoff.py route-repair --return <file> --build <slug>`, which
  prints one JSON line per repair, `{n, actor, route, producer, family, handed, read}`; with
  `--row <n> --id <ask id> --filed <date>` it prints instead the three rows S7 files for repair `n`,
  rendered by `render_ask_row`, `render_sev_row` and `render_status_row` (`tools/memory-tree/backlog.py:1516-1540`),
  reached through `resolve_kit_dir`. Observed by AC4.
- **S7** — The driver door, `bash tools/unattended/unattended.sh --repaired <slug> --return <file>`:
  for each `ask` route it mints the id in the producer's family (§8 F2), re-uses an open repair ask
  for the same `handed` key and the same `found` (§4 "Two repairs of one fact"), and files the rows
  through `write_ask_rows` (`tools/unattended/unattended.sh:9984`), the one backup, write, read-back
  and rollback every auto-filer uses, into the producer's `BACKLOG.md`. With `ASKS_CMD` blank it is
  dark, as that function's other callers are, and prints the rows it would file. A `route-back` or
  `owner` route prints its route line and files nothing: recording it is TOOL-dDeclaredLoop-14's
  `--refused`, which TOOL-dBoundRoles-26 S4 extends. Observed by AC5 and AC6.
- **S8** — A fact handed with TOOL-dFurnishedOrders-1's stale mark (J6, ` stale=<source path>@<blob12>`)
  is filed with that mark in its ask's `data` clause, so the producer reads which source moved.
  Observed by AC5.
- **S9** — The docs: `tools/roles/README.md` (the arm and the verb), `help/roles.md` (a section "When a
  handed fact is wrong"), and the `--repaired` line of `tools/unattended/VERBS.template.md`, rendered
  to `memory/guides/UNATTENDED-VERBS.md`. Observed by AC7.

## 3. Non-goals (OUT)

- Handing the repaired fact onward while its ask is open, and its stale mark when the read sources
  move: TOOL-dFurnishedOrders-14's carry, which reads the ask this unit files.
- The row grammar, the upstream rows and `render_return_schema`: TOOL-dFurnishedOrders-19's. This unit
  adds the `repair` kind's text grammar and validates it, nothing of the row mechanism.
- The arm factory `derive_return_arms`: TOOL-dFurnishedOrders-15's, extracted at `[return.probe]`.
- `REFUSAL_ROUTES`, `route_refusal`, the `refusal` row and `--refused`: TOOL-dBoundRoles-26's and
  TOOL-dDeclaredLoop-14's, read here and never re-specced.
- Fixing the producer's record. The ask asks for it; a frozen built spec is fixed by a new unit (P19).
- Closing PLAY-dClosedLoop-32. §8 F2 mints so that no outside filer and no landed id collides; an id
  a producer's run has minted on an unpushed branch stays that ask's residual.
- The problem register's reading of repair asks (`research-handoffs-design.md:90`): TOOL-dPlacedRequest-12's.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-15` — `derive_return_arms`, which composes `[return.repair]` into every role's template; without it the arm has no single home
- **consumes-from** `TOOL-dFurnishedOrders-19` — `render_return_schema` and the `repair` row kind, the rows a return declares its repairs in; without it a repair row is an invented row the schema refuses
- **consumes-from** `TOOL-dFurnishedOrders-1` — `stale=`, the mark a handed fact carries when its source moved, copied into the ask's `data` clause
- **hands-off** `TOOL-dFurnishedOrders-14` — `repair:`, the repair line S1 parses and the ask S7 files, which the carry reads to hand the repaired fact while the ask is open
- **consumes-from** external — TOOL-dBoundRoles-26 S1 to S4, TOOL-dBoundRoles-5 S1, TOOL-dBoundRoles-2 S1, TOOL-dBoundRoles-11 S5, TOOL-dBoundRoles-13 S1, TOOL-dDeclaredLoop-14's `--refused` and TOOL-dTotalRecall-3 S1 and S3, each specced and unbuilt at base `2193e25d`
- **hands-off** `TOOL-dFurnishedOrders-29` — the `roles.on-contradiction` read and `derive_repair_producer`, which unit 29 S9 re-points and S28 validates (ids 29, 61)

## 4. Design

### The arm

```toml
# tools/roles/role-schema.toml, beside TOOL-dBoundRoles-26's [return.refusal]
[return.repair]
outcome = "contradicted"
fields = ["handed", "found", "read"]
row-kind = "repair"
row-text = "handed=<key> · found=<one line> · read=<key>"
note = "A repair whose correction would change what you were asked to produce is a divergence: return diverged. A repair changes no record but your own return."
```

Under `repair-and-record` a role finishes its item and declares each repair as a row:

```
## Establishes

- r3 · repair · handed=record:memory/builds/tProd/spec/2026-10-25-spec-TOOL-tProd-2.md@3b18e512cc0f · found=the cap is 8192 bytes, not 4096 · read=blob:tools/x.py@9f0c1d2e3a4b:40-44
```

Under `return` it stops with `outcome: contradicted` and the same three fields; under `ask` it stops
the same way and the route parks it.

### The route

| `roles.on-contradiction` | What the role returns | Actor in `REFUSAL_ROUTES` | Route | Item |
|---|---|---|---|---|
| `repair-and-record` | its outcome, plus `repair` rows | `build:<producer>` | `ask`, filed by S7 | finished |
| `return` | `contradicted` | `producer` | `route-back` | never re-offered |
| `ask` | `contradicted` | `owner` | `owner`, `resolve_owner_question(kind="refusal")` | never re-offered |

One table, TOOL-dBoundRoles-26's, answers every row: `derive_repair_route` only names the actor, so a
change to how an actor routes is made once. The owner row asks with the kind `refusal`, which
TOOL-dBoundRoles-11's reader already answers; unattended it follows `run.on-owner-question`.

### The ask

Rendered by `render_ask_row` with the producer's family from `read_roster_family`
(`tools/unattended/unattended.sh:9966`):

```
- TOOL-tProd-7 · filed 2026-10-26 · A HANDED FACT WAS FOUND FALSE. the cap is 8192 bytes, not 4096 · seen `memory/builds/tFix/prompts/<return>.md`@1a2b3c4 · data handed=record:…@3b18e512cc0f read=blob:tools/x.py@9f0c1d2e3a4b:40-44 · accept the record behind the handed key states what was found, or a unit supersedes it
- SEV · TOOL-tProd-7 · LOW · a handed fact in this build's record is repaired in work orders until the record is fixed
- KEEP · TOOL-tProd-7 · filed by a repairing return of tFix; outside that build's goal
```

The `data` clause is free text in the backlog grammar (`tools/memory-tree/backlog.py:1198`), so the
repair's keys ride it without a new label; `found` is the ask's text, which S1 keeps free of the
separator. A fact handed stale adds ` stale=<path>@<blob12>` to `data` (S8).

### Two repairs of one fact

Before minting, the door reads the producer's open asks for a `data` clause carrying the same
`handed=` key. The same `found` re-uses that ask and prints `reused <id>`: the first filed holds.
A different `found` is a contradiction between roles: the door files one ask whose text carries both
found lines and whose `data` carries both `read=` keys, and prints `route route-back · re-offer never`
naming the producer, as item 7's last bound says. The carry keeps handing the first repair.

### The door

`--repaired` resolves the roles kit with `resolve_kit_dir` (`tools/unattended/lib-unattended.sh:132`),
runs `handoff.py route-repair` once for the routes, then once per `ask` route with `--row`, `--id` and
`--filed` for the rows, and hands them to `write_ask_rows`. That function's message prefix, today the
literal `gates-green:`, becomes its caller's verb name, so its lines name the verb that filed.

### Inventory

Minted: `REPAIR_RE`, `parse_repair_line`, `derive_repair_route`, `derive_repair_producer`, the
`[return.repair]` table, the outcome `contradicted`, the row kind text grammar, the `route-repair` verb
of `handoff.py`, the driver verb `--repaired`, and the ask text `A HANDED FACT WAS FOUND FALSE.`. Each
function name was asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function` and
answered OK.

### Migration

Additive. No return at base carries a repair, and no `BACKLOG.md` an ask in this shape. The arm
reaches each agent file at its next render.

### Rollout

Live at landing on the direct route; dark on the driver until the project declares `ASKS_CMD`, as
every auto-filer of `write_ask_rows` is.

### Files touched (estimate)

- `tools/roles/role-schema.toml`
- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/README.md`
- `tools/roles/adopt-roles.test.sh`
- `.claude/agents/` (every agent type, rendered by `tools/roles/render_agents.py --write`)
- `tools/unattended/unattended.sh`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`
- `help/roles.md`

### Alternatives rejected

- **A second route table, `REPAIR_ROUTES`.** Every row it would hold is a row of `REFUSAL_ROUTES` with
  a different key; two tables for one routing drift apart.
- **`handoff.py` writing the producer's `BACKLOG.md` itself.** `write_ask_rows` is the one backup,
  write, read-back and rollback the driver keeps for every auto-filer; a second writer is a copy.
- **New backlog labels `handed`, `found`, `read`.** The label set is closed and graded by V13; the free
  `data` clause carries the keys and the text carries the found line.
- **Keying the repair by the repairing return.** Item 7 as folded keys it by the sources the role
  read, so it goes stale when they move; a return is immutable and would never go stale (§8 F5).

## 5. Production-readiness checklist

- security — a new write into another build's `BACKLOG.md`, the one sanctioned foreign write, through
  `write_ask_rows`'s backup and read-back; every value reaching the row is parsed by S1 first, and a
  `found` carrying the separator, a newline or a key outside the three forms is refused before any
  write.
- perf / scale — one policy read and one `handoff.py` call per return, two more per filed repair.
- error / empty / loading states — a return with no repair prints nothing and files nothing; an
  unreadable return, an unknown policy value or a producer with no roster family is refused by name.
- observability — one route line per repair, one `filed`, `reused` or dark line per ask.
- risks — PLAY-dClosedLoop-32's residual: an id the producer's run minted on an unpushed branch
  (§8 F2); the backlog fold's V9 surfaces it at reconcile.
- testing — AC1 to AC7 by probes and fixtures a pass runs; the arm of §7 at the close.
- migration — none, per §4.
- user docs — `help/roles.md`, per S9.

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `roles_lib.parse_repair_line` on
  `handed=blob:a.py@0123456789ab:3-9 · found=the limit is 8 · read=blob:a.py@0123456789ab:3-9`, it
  returns the three fields; on a line whose `found` is empty, one whose `handed` is `path:a.py`, and
  one whose `found` carries ` · `, each raises naming that field.
  Red when: a malformed repair parses, so an ask carries a key no cut can resolve.
- **AC2** — When `validate_return` runs in a scratch copy of the roles kit over a planted
  `contradicted` return lacking `read`, it returns a line naming `read`; over a return whose `repair`
  row text lacks `found=`, a line naming the row id; over a well-formed one, no line.
  Red when: the arm is not composed, so a `contradicted` return carrying no evidence validates.
- **AC3** — When `python render_agents.py --write` runs in `tools/roles/` and
  `grep -c "outcome: contradicted"` runs over each file of `.claude/agents/`, every file counts 1, and
  `grep -c "return diverged"` over the same files counts 1 each.
  Red when: an agent file lacks the arm or its bound, so a role meets a false fact with no route.
- **AC4** — When `python handoff.py route-repair --return <plant> --build tFix` runs in a scratch
  adopter with `roles.on-contradiction` set in turn to each of its values: `repair-and-record` prints
  `actor build:tProd` and `route ask` for a `handed` key under the fixture producer's build folder and
  `actor build:tFix` for a `blob:` key of a product file; `return`, over a `contradicted` plant,
  prints `route route-back` and `re-offer never`; `ask` prints `route owner`.
  Red when: the policy value is ignored, so `return` still files an ask and finishes the item.
- **AC5** — When `bash unattended.sh --repaired tFix --return <plant>` runs in a fixture repository
  declaring `ASKS_CMD`, the fixture producer's `BACKLOG.md` gains one ask whose id is
  `TOOL-tProd-<n>`, `<n>` one past the highest the trees hold, whose `data` clause carries the
  plant's `handed=` and `read=` keys and the plant's `stale=` mark, and which `gen_build_index.py --asks`
  reads back OPEN; with `ASKS_CMD` blank the file is unchanged and the rows are printed.
  Red when: the ask lands in the filer's `BACKLOG.md` or under the filer's family, which backlog V1 refuses.
  fixture: a scratch repository with two build folders, built by the pass under `%TEMP%`.
- **AC6** — When the AC5 command runs a second time with the same plant, it prints `reused` and the
  ask count is unchanged; with a plant whose `found` differs for the same `handed` key, it prints
  `route route-back` and files one ask whose `data` carries both `read=` keys.
  Red when: a second repair files a second repair ask, so two repaired facts compete for one key.
- **AC7** — When `grep -n -- '--repaired' VERBS.template.md` runs in `tools/unattended/` and
  `grep -n 'contradicted' roles.md` runs in `help/`, each prints at least one line.
  Red when: the verb ships with no line in the guide a driver reads.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `unattended kit gate` · `unattended skill wiring` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `policy fixtures` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 AC4 · the three malformed repair lines, the evidence-less `contradicted` return and the three policy values over one plant, staged by making `derive_repair_route` answer `ask` for every value · none

AC5 and AC6 are observed by the pass's own fixture run of the verb. No arm is added to the unattended
kit's suites: they are waived for this build's landing (the README's build-level rule, owner,
2026-10-20), and their clean reading is owed with PLAY-dClosedLoop-18.

## 8. Open questions

- **F1 — Does the repair route through TOOL-dBoundRoles-26's `REFUSAL_ROUTES` or a table of its own?**
  Options: (a) the policy value names an actor of `REFUSAL_ROUTES` and `route_refusal` answers; (b) a
  `REPAIR_ROUTES` table beside it. (b) is the second route table the brief's unit row rules out, and
  two tables routing one actor drift. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most
  feature-rich survivor, tie-broken by reuse of the parent's table. widens: none · relaxes: none
- **F2 — How is the repair ask's id minted in the producer's family so it cannot collide (brief D10)?**
  Options: (a) TOOL-dTotalRecall-3's counter, `gov-claim.sh ask <FAMILY> <slug> --claimant <key>`,
  refusing to file until it lands; (b) the driver's `derive_ask_seq` (`tools/unattended/unattended.sh:9780`)
  alone; (c) the counter where it is installed, found by `resolve_kit_dir`, else `derive_ask_seq`, the
  claimant in both the repair's content key (the first 12 hex digits of the SHA-256 of its three
  fields) so a replay re-uses its ask. (a) files nothing until a later build lands; (b) keeps the
  collision PLAY-dClosedLoop-32 records with every other outside filer. A filer-owned id is refused
  by backlog V1 (`tools/memory-tree/backlog.py:1039-1045`), and a reserved range by the ids rule in
  `memory/HYGIENE.md`. RESOLVED (agent, 2026-10-26, delegated): (c), rung 3, the most feature-rich
  survivor: it files now and serialises against every outside filer once the counter lands. Neither
  arm sees an id the producer's run minted on an unpushed branch, so this unit carries no `closes`
  for PLAY-dClosedLoop-32 and names the residual in its return. widens: none · relaxes: none
- **F3 — Where is the filing door?** Options: (a) a driver verb `--repaired` filing through
  `write_ask_rows`; (b) `handoff.py route-repair --write`, writing the file from the roles kit. (b) is
  a second writer beside the driver's one copy. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3,
  tie-broken by reuse of `write_ask_rows`. grants: PLAY-dClosedLoop-3 the driver verb `--repaired` and
  its line in the unattended verbs guide, the filing the clause names · widens: none · relaxes: none
- **F4 — Which build produces a fact whose key names no build folder?** Options: (a) the work order's
  own build, whose executor cut and handed it; (b) no producer, so the repair is recorded and not
  filed; (c) the owner. (b) drops the clause's filing for every product-code fact; (c) routes a
  record question to a person. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most
  feature-rich survivor. widens: none · relaxes: none
- **F5 — Is the repair keyed by the repairing return or by the sources it read?** `layer-roles.md:295`
  and F3-4's settled text (`:640-641`) say the repaired fact is handed "keyed to the repairing
  return"; the same item's bound (`:303-304`) says the repair lives "in its repair ask, keyed by the
  sources the repairing role read, never by its immutable return", the roles round's review L2
  (`2026-10-15-review-PLAY-dClosedLoop-1-roles-b.md:222`) folded. RESOLVED (agent, 2026-10-26,
  delegated): the sources, `read=`, so the repair goes stale when they move, rung 1, the bound that
  names the key; the repairing return is the ask's `seen` locator, so the fact stays traceable to it.
  widens: none · relaxes: none
- **F6 — The `ask` value parks for the owner: with which question kind?** Options: (a) TOOL-dBoundRoles-11's
  existing kind `refusal`, as TOOL-dBoundRoles-26 asks it; (b) a new kind `contradiction`. (b) widens a
  sibling build's closed set. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none ·
  relaxes: none
- **F7 — The severity of a repair ask.** Options: (a) `LOW`, the gap register's rating of
  `gap-roles-17`; (b) `MED`; (c) `HIGH`, as the driver's other auto-filers write. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 1, the gap register's line 169 rates a missing repair route LOW,
  and the carry keeps the false fact out of every work order meanwhile. widens: none · relaxes: none
- **F8 — The parents and siblings this unit calls are unbuilt.** TOOL-dBoundRoles-26, -5, -2, -11 and
  -13, TOOL-dDeclaredLoop-14 and TOOL-dTotalRecall-3 are specced and DEFERRED at `2193e25d`;
  TOOL-dFurnishedOrders-1, -15 and -19 precede this unit in the build order. RESOLVED (agent,
  2026-10-26, delegated): this spec calls them as their specs name them; the build run re-grounds on
  each section it cites and stops the unit if one is still absent then, rung 1 (the brief's chain
  rule). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 7, the brief's J10 and D10, scout A's row
  for cl-0198, `layer-roles.md` `[trust]` item 7 and F3-4, and the source at `2193e25d`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-29, promoted from the round-1 spec audit (`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: the driver's ask auto-file, `write_ask_rows` (`tools/unattended/unattended.sh:9984`),
with `derive_ask_seq` (`:9780`), `read_roster_family` (`:9966`) and `read_ask_back` (`:9945`), which
today file only inherited reds and held suites; `render_ask_row`, `render_sev_row` and
`render_status_row` (`tools/memory-tree/backlog.py:1516-1540`), the one row renderers; the free `data`
clause (`backlog.py:95`, `:1198`); TOOL-dBoundRoles-26's `REFUSAL_ROUTES` and `route_refusal` for the
route. `python tools/codebase-map/reuse_lookup.py "file a repair of a handed fact as an ask row in the
producer build backlog"` ranked name stems (`rows`, `build_*`) and surfaced `render_ask_row` and the
driver's `ask_filed_in`, `asks_filed_in` and `id_rows` (`tools/unattended/lib-unattended.sh:692`,
`:2198`, `:2207`); reading the driver around them found `write_ask_rows`. Scout A's row said "there
is no CLI that files an ask": true of a CLI, and the driver's internal auto-file is the seam it
missed. The recall probe returned the brief's row, scout A's row, v2:847 and the roles round's review
L2, whose keying fix §8 F5 follows.

Recall terms used: `python tools/memory-recall/query.py "how is a false handed fact repaired and filed against its producer's record" --terms "repair handed fact producer record ask backlog contradiction on-contradiction refusal route mint"`
