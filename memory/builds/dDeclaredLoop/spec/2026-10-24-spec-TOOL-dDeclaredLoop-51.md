# TOOL-dDeclaredLoop-51 — the eight recommendation rows amended in place, their actors in the declaration grammar

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 33 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-51-deviation-511.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-51-deviation-511.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, its item **H1**, alone in that item. `TOOL-dDeclaredLoop-22` S6 adds
eight item rows, `item.plan.recommend`, `item.plan.reason`, `item.design.recommend`, `item.design.reason`,
`item.build.recommend`, `item.test.recommend`, `item.test.reason` and `item.deploy.recommend`, with the
bare actors `command`, `planner`, `architect` and `tester`. `TOOL-dDeclaredLoop-12` S2 (order 6) already
seeds all 61 flow-steps items, these eight included, and `TOOL-dDeclaredLoop-9` S1 (order 7) accepts only
`<kind>:<name>` or a bare `executor` or `owner`. S6 also makes `architect` the actor of
`item.design.reason` while S5 has `gov-spec-writer` produce it. At order 32 the unit either duplicates
eight rows or rewrites rows `TOOL-dDeclaredLoop-12` owns, and its AC8 asserts spellings the declaration
check refuses. This unit takes the report's fix. It repairs `TOOL-dDeclaredLoop-22`.

## 2. Scope (IN)

- **S1** — The eight rows `TOOL-dDeclaredLoop-12` seeds are amended in place, never re-added: each
  `recommend` row's witness becomes `{ class = "history", by = "the recommendation record" }` and its
  `returns` `record-kind.recommendation`; each `reason` row's witness becomes `{ class = "history", by =
  "the reason record joined to the recommendation record" }`. This supersedes `TOOL-dDeclaredLoop-22` S6's
  "eight item rows" as an addition. Observed by AC1.
- **S2** — The actors, in `TOOL-dDeclaredLoop-9`'s grammar: the five `recommend` rows carry
  `command:tools/unattended/unattended.sh`, the driver whose `--recommend` verb writes the score;
  `item.design.reason` carries `role:gov-spec-writer`, the role `TOOL-dDeclaredLoop-22` S5's reason stage
  spawns; `item.plan.reason` and `item.test.reason` carry `role:gov-planner` and `role:gov-tester`, which
  `TOOL-dDeclaredLoop-9` S3 prints `pending` until dBoundRoles lands them. Observed by AC1, AC2.
- **S3** — `TOOL-dDeclaredLoop-22` AC8 is restated to these spellings, and `python
  tools/loop/loop_lib.py --check` exits 0 after the amendment. Observed by AC1, AC3.

## 3. Non-goals (OUT)

- The `--recommend` verb, the record kind and the reason stage: `TOOL-dDeclaredLoop-22`'s, unchanged.
- The architect, planner and tester roles: dBoundRoles'; `role:gov-planner` and `role:gov-tester` read
  `pending` until then.
- A spec-set lint over duplicate `[[item]]` tags and actor spellings, the finding's left-shift: AC3 is the
  definition check over the amended rows, and the lint is not named by any clause of this build.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-22` — `item.plan.recommend` and its seven siblings as that unit's S6 scopes them, and `record-kind.recommendation`, their witness and return
- **consumes-from** `TOOL-dDeclaredLoop-12` — the 61 `[[item]]` rows of `tools/loop/loop.toml`, eight of which this unit amends in place
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 39 and 44: this pass keeps the loop definition leg green and writes command actors in the verb form, scope items of that unit

## 4. Design

### Evidence

- `TOOL-dDeclaredLoop-12` §4 "Data model" seeds `item.plan.recommend` with actor `command:plan.recommend`
  and `returns = "record-kind.recommendation"`, and S2 seeds one row per flow-steps item, 61 in all,
  among them `plan.recommend` and `plan.reason` (flow-steps.md:188-189), `design.recommend` and
  `design.reason` (:244-245), and `test.recommend` and `test.reason` (:363-364).
- `TOOL-dDeclaredLoop-9` S3 prints an actor `role:<slot>` with no agent file `pending`, and its AC
  plants `role:gov-planner` as that case.

### The amended rows

| Tag | Actor | Witness | Returns |
|---|---|---|---|
| `item.plan.recommend` | `command:tools/unattended/unattended.sh` | the recommendation record | `record-kind.recommendation` |
| `item.design.recommend` | same | same | same |
| `item.build.recommend` | same | same | same |
| `item.test.recommend` | same | same | same |
| `item.deploy.recommend` | same | same | same |
| `item.plan.reason` | `role:gov-planner` (pending) | the reason record joined to the score | the role's |
| `item.design.reason` | `role:gov-spec-writer` | same | the role's |
| `item.test.reason` | `role:gov-tester` (pending) | same | the role's |

### Files touched (estimate)

- `tools/loop/loop.toml`

### Alternatives rejected

- **`role:gov-architect` for Design's reason.** No agent file exists, so it reads `pending`, while the
  reason stage that actually answers spawns `gov-spec-writer`; naming the stand-in keeps the row true.
- **Adding the rows again under this build.** Two declarations of one tag, which `TOOL-dDeclaredLoop-12`'s
  reader refuses.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — none.
- error / empty / loading states — the two pending roles are counted on every check, never green.
- observability — `loop_lib.py --check` prints each pending role.
- risks — when dBoundRoles lands an architect, Design's reason row moves to it in that build.
- testing — AC1 to AC3 as probes; the arm under §7, observed at the close.
- migration — none.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When a scratch probe loads the loop definition through `read_items`, it finds each of the eight
  tags exactly once, the five `recommend` rows whose actor is the `command:` kind naming
  `tools/unattended/unattended.sh` and whose returns is `record-kind.recommendation`, and the three `reason` rows with `role:gov-planner`,
  `role:gov-spec-writer` and `role:gov-tester`.
  Red when: a tag appears twice, or a row keeps a bare `planner`, `architect` or `tester`.
- **AC2** — When `python loop_lib.py --check` runs, it prints `role:gov-planner` and
  `role:gov-tester` as `pending` and `role:gov-spec-writer` resolved.
  Red when: Design's reason names a role with no agent file while the stage spawns another.
- **AC3** — When the same check runs on the built tree, it exits 0.
  Red when: an amended row loses a field `TOOL-dDeclaredLoop-9` requires of its actor kind.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_lib.py · covers AC1 · the eight rows' tags and actors over the tree, staged by re-adding one row with a bare actor · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Which role is Design's reason's actor?** Options: (a) `role:gov-spec-writer`, the role that
  answers it today; (b) `role:gov-architect`, printed pending, with the spec writer named as its stand-in.
  (b) declares an actor that never runs. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, matching
  `TOOL-dDeclaredLoop-22` S5 and §8 F1. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 1 (HIGH, item H1).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams are `TOOL-dDeclaredLoop-12`'s seeded rows, amended in place, and `TOOL-dDeclaredLoop-9`'s actor
grammar and pending-role rule; no new row and no new reader. `python tools/codebase-map/reuse_lookup.py
"stage exit recommendation item rows actors"` ranked generic row helpers (`rows`, `row`, `extract_row`,
`id_rows`, `render_ask_row`), none an item declaration, the loop kit not existing at base.

Recall terms used: recommend reason item rows actor role gov-spec-writer gov-planner gov-tester pending recommendation record
