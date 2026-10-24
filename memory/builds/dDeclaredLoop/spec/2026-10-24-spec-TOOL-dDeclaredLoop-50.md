# TOOL-dDeclaredLoop-50 — the review program's item rows pass the program and declaration checks

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 32 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-50-deviation-501.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-50-deviation-501.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md`)
confirmed finding **id 2 at HIGH**, its item **H2**, alone in that item. `TOOL-dDeclaredLoop-20` S1 and §4
"The item rows" give `item.review.trigger`, `item.review.dispose`, `item.review.fold` and
`item.review.cost` the bare actors `command` and `spec writer`, which `TOOL-dDeclaredLoop-9` S1 refuses
(an actor is `<kind>:<name>` or a bare `executor` or `owner`). The rows need and route to
`item.review.pin` and `item.review.report`, which `TOOL-dDeclaredLoop-20` §3 calls dFairHearing's and
which no spec declares, and `TOOL-dDeclaredLoop-12` S3 refuses an undeclared need or route target. The
rows name no `step`, which `TOOL-dDeclaredLoop-12` makes required. Landing them reds the `loop
definition` leg, while `TOOL-dDeclaredLoop-20` AC1 checks only presence, witness and routes. This unit
takes the report's fix. It repairs `TOOL-dDeclaredLoop-20`.

## 2. Scope (IN)

- **S1** — The actors, in `TOOL-dDeclaredLoop-9`'s grammar: `item.review.trigger`, `item.review.dispose`
  and `item.review.cost` carry `command:tools/unattended/unattended.sh`, the driver whose `--trigger` and
  `--review` verbs run them, with `inputs`, `allowance` and `returns` a non-role actor requires;
  `item.review.fold` carries `role:gov-spec-writer`, its defaults its role's. Observed by AC1.
- **S2** — The two upstream items declared as `[[item]]` rows owned by dFairHearing, the way
  `TOOL-dDeclaredLoop-12` S2 seeds rows other builds own: `item.review.pin`, actor
  `command:tools/workflows/review_pin.py`, needs `item.review.trigger`, routing its one outcome to
  `item.review.report`; and `item.review.report`, actor `command:tools/workflows/tier2-review.js`, needs
  `item.review.pin`, its one outcome routed to `item.review.dispose`. The harness's one call stands for
  the flow record's lens, refute and report items, which it runs inside itself. Observed by AC1.
- **S3** — The breakpoint program's step: an `[[item]]` row may carry `step = "none"` when its tag's
  middle segment is `review`, the program a breakpoint runs at whichever item boundary it is placed
  (`TOOL-dDeclaredLoop-19` S1). `check_program` in `tools/loop/loop_lib.py` admits `none` for those rows
  alone, still grades their needs, outcomes and routes, and leaves them out of every step's order and
  exit check. Observed by AC2.
- **S4** — `TOOL-dDeclaredLoop-20` AC1 gains the assertion that `python tools/loop/loop_lib.py --check`
  exits 0 with the six rows present. Observed by AC1.

## 3. Non-goals (OUT)

- The review program's verbs, record fields and counts: `TOOL-dDeclaredLoop-20`'s, unchanged.
- The flow record's lens, refute and other review items as rows of their own: dFairHearing's, run inside
  `tools/workflows/tier2-review.js`; declaring them adds rows no reader grades separately.
- A template checklist line that every definition-writing criterion asserts `loop_lib.py --check`, the
  finding's left-shift: S4 is this unit's instance; the template is a governance carrier this build's
  clauses do not name.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-20` — `item.review.trigger`, `item.review.dispose`, `item.review.fold` and `item.review.cost`, the rows this unit makes conform
- **consumes-from** `TOOL-dDeclaredLoop-12` — `check_program` and the `step` key of each `[[item]]` row, which S3 opens to `none` for the breakpoint program alone
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 39, 44 and 45: this pass keeps the loop definition leg green and writes command actors in the verb form, scope items of that unit

## 4. Design

### Evidence

- `TOOL-dDeclaredLoop-9` S1: `actor` one string `<kind>:<name>` or the bare `executor` or `owner`, kinds
  `role`, `command`, `executor`, `hook`, `owner`; its §4 table spells a command `command:<tool path or
  verb>`.
- `TOOL-dDeclaredLoop-12` S3: every need names a declared item and every route a declared item,
  `transition` or `stand-in:<path>`; S2 seeds rows owned by later builds, such as `item.plan.lease`
  owned by dRankedPlan, so a row may name an owner other than this build.
- The flow record's `review.pin` reads `review.trigger` and routes to `review.lens`
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:570`).

### The rows

| Tag | Step | Actor | Needs | Routes |
|---|---|---|---|---|
| `item.review.trigger` | `none` | `command:tools/unattended/unattended.sh` | none | fired to `item.review.pin` |
| `item.review.pin` | `none` | `command:tools/workflows/review_pin.py` | `item.review.trigger` | `item.review.report` |
| `item.review.report` | `none` | `command:tools/workflows/tier2-review.js` | `item.review.pin` | `item.review.dispose` |
| `item.review.dispose` | `none` | `command:tools/unattended/unattended.sh` | `item.review.report` | as `TOOL-dDeclaredLoop-20` §4 |
| `item.review.fold` | `none` | `role:gov-spec-writer` | `item.review.dispose` | as `TOOL-dDeclaredLoop-20` §4 |
| `item.review.cost` | `none` | `command:tools/unattended/unattended.sh` | `item.review.report` | done |

### Files touched (estimate)

- `tools/loop/loop.toml`
- `tools/loop/loop_lib.py`

### Alternatives rejected

- **Routing to `stand-in:<path>` instead of declaring the two rows.** `item.review.dispose` and
  `item.review.cost` need `item.review.report`, and a need must name a declared item, so a stand-in route
  leaves the needs dangling.
- **Placing the review rows on `step.design`.** The breakpoint program runs at any placed boundary, the
  Build step's closing review and the Test step's gate review among them, so a fixed step misplaces it.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — two more rows.
- error / empty / loading states — a `none` step on a row outside the review program is refused by name.
- observability — `loop_lib.py --check` prints the breakpoint program's rows under their own heading.
- risks — a later build declaring the lens and refute rows inserts them between `item.review.pin` and
  `item.review.report`, re-pointing two routes.
- testing — AC1 and AC2 as probes and plants; the arm under §7, observed at the close.
- migration — none.
- user docs — none beyond `help/loop.md`.

## 6. Acceptance criteria

- **AC1** — When `python loop_lib.py --check` runs on the built tree, it exits 0 with the six
  `item.review.*` rows present, and a probe reading them finds each actor in `TOOL-dDeclaredLoop-9`'s
  grammar.
  Red when: a row keeps the bare actor `command`, which the declaration check refuses.
- **AC2** — When `python loop_lib.py --fixture --plant step-none-outside-review` runs, an
  `item.plan.*` row with `step = "none"` exits 1 naming it; and `--plant review-program` with the six rows
  exits 0.
  Red when: `none` is admitted for any row, so a step's item escapes its step's checks.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_lib.py · covers AC1 AC2 · the `review-program` and `step-none-outside-review` plants, staged against `TOOL-dDeclaredLoop-20`'s rows · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Which step does a breakpoint-program item carry?** Options: (a) `none`, admitted for the review
  program alone; (b) a fixed step. (b) misplaces every review the build places outside that step.
  RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 2 (HIGH, item H2).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams are `TOOL-dDeclaredLoop-12`'s `check_program` and row schema and `TOOL-dDeclaredLoop-9`'s
actor grammar, both minted in this build; the unit adds two rows and one admitted value. `python
tools/codebase-map/reuse_lookup.py "an item row whose step is any breakpoint boundary"` ranked generic
row helpers (`rows`, `row`, `extract_row`, `id_rows`) and govkit's `step`, none a program or item check;
the loop kit does not exist at base, so its checks are not indexed.

Recall terms used: review trigger dispose fold cost pin report item rows actor step none check_program breakpoint
