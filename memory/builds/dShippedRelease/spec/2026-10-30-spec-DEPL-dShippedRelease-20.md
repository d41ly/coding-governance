# DEPL-dShippedRelease-20 — an offered update runs neither `adopt` nor `test.seed`, its order names the adopter's own run of each, and outbox orders are graded

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 21 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0430@25fe9858 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md](../build/2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md) | research | DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-25 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-31 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |

<!-- /gen:spec-records -->

## 1. Goal

`kits.offer` runs nothing from the adopter's tree, so the two hooks an update owes, `test.seed` for each
new check and the `adopt` program, stay undone unless something tells the adopter to run them. This unit
gives every attended order one writer, makes the offer's order name the adopter's own run of each hook,
and closes `gap-deploy-05`, outbox orders graded by nothing, with a grader over the receipt's `orders`.
It owns no node; it reads `item.kits.offer`, `item.kits.update`, `item.test.seed` and the `adopt`
program's items.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build: `write_attended_order`
(TOOL-dSafePassage-2 S5, -4 S4), `legacy_ledger.py seed` (TOOL-dWitnessedBar-15 S1, -13 S8),
`core.py adopt` (TOOL-dLinkedLibrary-8 S3), each specced and unbuilt at base `f4597719`.

- **S1** — One order writer, I18. `render_attended_order(kind, argv, why)` in
  `tools/govkit/govkit.py`, beside `render_order_slug` (`:5735`), returns one order's text in one shape,
  §4 "The order". `write_attended_order`, TOOL-dSafePassage-2's writer, renders through it, so a step's
  order and a hook's order cannot differ in shape. Observed by AC3.
- **S2** — The hooks, declared once. `KIT_HOOKS` in `tools/govkit/govkit.py` holds one row per hook, §4
  "The hooks", and `read_kit_hooks(verb, receipt, deploy)` returns the rows that apply to `install` or
  `update`, each argv resolved through the target's `prefix`, leaving out a hook whose kit the receipt
  does not claim, with one note naming it. DEPL-dShippedRelease-17 walks these rows. Observed by AC2.
- **S3** — The offer's order. `write_offer_order` (DEPL-dShippedRelease-16 S7) gains one
  `render_attended_order("hook", argv, why)` section per `read_kit_hooks("update", …)` row. The offer
  runs neither: nothing in `update` spawns a hook, so the eighth kind has no site, and §4 "The hooks"
  says why that needs no `OFFER_MODE` row. `adopt` and `test.seed`
  are named in the order by their exact command, `<slug>` and `<id>` left for the owner, since
  `core.py adopt` needs the adoption's build and unit. Observed by AC1 and AC2.
- **S4** — The grader, `check_orders(tree, receipt)` in `tools/run-gates/check-receipt.py`, run by
  `main` after the engine rows on every tree holding a receipt, so an adopter's own bar reads it with
  no gov checkout. Each row of the receipt's `orders` takes one state, and each `.md` under
  `.governance/outbox/` no row claims is `unrecorded`, §4 "The states". It prints one line of counts
  and one line per `open` or `unrecorded` order. It never moves the exit status, §8 F1; only a row with
  no `path` is a `MALFORMED` finding, which reds as an engine row's does. Observed by AC4, AC5 and AC6.
- **S5** — The count reaches gov. `read_adopter_reading` (DEPL-dShippedRelease-7 S7) gains
  `orders_open`, the `open` rows of the committed receipt, so gov's `adopters` record shows what an
  adopter owes without a checkout. Observed by AC7.
- **S6** — `help/offers.md` gains a section "What the offer leaves to you", naming both hooks, and
  `WIRE-INTO-PROJECT.md`'s section on the orders `update` leaves (`:1401`) names the grader's line.
  Observed by AC8.

## 3. Non-goals (OUT)

- Running either hook: DEPL-dShippedRelease-17's `kits.update-attended`. This unit only names them.
- The `adopt declarations` verb: DEPL-dShippedRelease-28 adds it; S2's row names it.
- Recording `update`'s own order files on the receipt: §8 F2.
- A red on an open order: §8 F1.

### Edges

- **consumes-from** `DEPL-dShippedRelease-16` — `OFFER_MODE`, the census the eighth kind is read against, and `write_offer_order`, whose order S3 extends
- **hands-off** `DEPL-dShippedRelease-17` — `render_attended_order`, the one order writer its walk calls, and `KIT_HOOKS`, the rows it walks
- **consumes-from** external — TOOL-dSafePassage-2 and -4, TOOL-dWitnessedBar-13 and -15, TOOL-dLinkedLibrary-8, each specced and unbuilt at base `f4597719`, and DEPL-dShippedRelease-7's `read_adopter_reading`, reached through DEPL-dShippedRelease-16

## 4. Design

### Evidence

Read at `5d1c82ac0`; no product file differs from base `f4597719`.

- The receipt's `orders` holds `apply`'s rows alone: `hole`, `machine`, `gate-legs`
  (`tools/govkit/govkit.py:8012`, `:8043`, `:4620`), and `write_gate_legs` says `update` maintains no
  list (`:4290`). `update`'s own orders are files with no row: `update-conflict-` (`:10667`),
  `update-withdrawn-` (`:10760`), `update-preexisting-red-` (`:11616`), `update-declined-red-`
  (`:11658`), `update-rollback-` (`:11937`).
- `cmd_check` asserts each row's file exists and reds a stale hole order (`:5653-5668`), and it needs a
  gov checkout, so it never runs in an adopter's bar. That is why one adopter's 16 orders, five of them
  rollbacks, were graded by nothing.
- `.governance/outbox/` is ordinarily untracked (`:10269-10274`), so a clone holds receipt rows with no
  files. A red on an absent file would red every CI clone.
- `tools/run-gates/check-receipt.py` is `main(argv)` at `:401`, taking an optional tree, with its
  fixture arms in `check_fixtures` at `:202`.
- `check-receipt.py` reads the receipt with no policy and no gov checkout; so does S4.

### The order

```markdown
# Run this in your own session: <kind>

<why, one sentence>

    <argv, one line, shell-quoted>

The next `update --write` reads the witness and records this done.
```

`kind` is `step` or `hook`; the file is `.governance/outbox/update-attended-<kind>-<slug>.md`, slug from
`render_order_slug`.

### The hooks

```python
KIT_HOOKS = (
    ("test.seed", ("install", "update"), "memory-tree",
     ["python", "{prefix}/memory-tree/legacy_ledger.py", "seed", "--all"]),
    ("adopt", ("install",), "playbook-render",
     ["python", "{prefix}/playbook/core.py", "adopt", "census", "--build", "<slug>", "--unit", "<id>"]),
    ("adopt", ("update",), "playbook-render",
     ["python", "{prefix}/playbook/core.py", "adopt", "declarations", "--build", "<slug>", "--unit", "<id>"]),
)
```

An update's `adopt` run is `adopt declarations`, the one verb of the program that runs at update
(layer-expansions:461 keeps `adopt.census` for an install; `flow-steps.md:719` gives declarations both).
`<slug>` and `<id>` stay literal in an order, never resolved, and `{prefix}` is the only token.

Why no `OFFER_MODE` row: a row is keyed by a spawn site, and at this unit nothing spawns a hook.
`update` writes an order. DEPL-dShippedRelease-17's attended verb spawns one through `run_target_argv`,
already `refuse`, and refuses under the mode, so the eighth kind needs no row of its own.

### The states

| State | Meaning |
|---|---|
| `open` | a row whose file is on disk, with no `state = "applied"` |
| `discharged` | a row with `state = "applied"`, the mark `kits.update-attended` writes (DEPL-dShippedRelease-17) |
| `absent` | a row whose file is not on this tree: untracked in a clone, or deleted by the operator |
| `unrecorded` | a `.md` under the outbox no row names: `update`'s own orders and anything else there |

The line: `orders: <o> open · <d> discharged · <a> absent · <u> unrecorded`, zeros included. An
empty list prints `orders: none`, distinct from a tree with no outbox, `orders: no outbox`.

### Inventory

Minted: `render_attended_order`, `read_kit_hooks`, `check_orders`; `KIT_HOOKS`; the state words `open`,
`discharged`, `absent`, `unrecorded`; the row key `state` on an `orders` row; the field `orders_open` on
an `adopters` record; the order file prefix `update-attended-hook-`. Naming cell `py.function`: each OK
by `python tools/lexicon/lexicon.py --suggest <name> --as py.function` at `5d1c82ac` (`grade_orders`
was asked first and refused).

### Migration

Additive: a row with no `state` reads `open` or `absent`, so every existing receipt grades as it stands.

### Rollout

The grader prints from the first bar after an adopter's update carries it, moving no exit status.

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1, S2
- `tools/govkit/upgrade_steps.py`: `write_attended_order` renders through S1
- `tools/govkit/offer.py`: S3
- `tools/govkit/adopter_reading.py`: S5
- `tools/govkit/selftest.py`: the shape and hook arms
- `tools/run-gates/check-receipt.py`: S4
- `help/offers.md`, `WIRE-INTO-PROJECT.md`: S6

### Alternatives rejected

- **A hook row in `OFFER_MODE` now.** The arm joins spawn sites, and a row naming no spawn reds its
  "declared but no longer spawning" half, the failure §4 of DEPL-dShippedRelease-16 measured.
- **Grading in `cmd_check`.** It needs a gov checkout (`tools/run-gates/check-receipt.py`'s docstring
  says so), which is the population that left the orders ungraded.
- **Running the witness of each order in the bar.** A leg would then run a program an order names; the
  join on `state` runs nothing.

## 5. Production-readiness checklist

- security — the grader reads JSON and a directory listing and spawns nothing. An order's argv is gov's
  template with one `{prefix}`, validated by `target_context`'s `demand_safe_token`, and it is written
  as text an owner reads, never run here.
- perf / scale — one listing per bar.
- error / empty / loading states — `orders: none` and `orders: no outbox` are distinct lines; a
  malformed row is named; no receipt keeps today's `SKIP`.
- observability — the counts line prints on every receipt-holding tree; `adopters` records carry
  `orders_open`.
- risks — open orders never red, so an owner who ignores the line loses nothing but the visibility;
  §8 F1 prices that.
- testing — the arms of §7, each a scratch tree.
- migration — §4 "Migration".
- user docs — `help/offers.md`, `WIRE-INTO-PROJECT.md`.

## 6. Acceptance criteria

- **AC1** — When `python offer.py --fixture --plant hooks-unrun` runs over a scratch adopter whose
  `core.py` and `legacy_ledger.py` each write a canary when run, the offer of an update lands its branch
  and neither canary exists after it, in the clone or anywhere else.
  Red when: `kits.offer` runs `adopt` or `test.seed` in the adopter's tree.
  fixture: `--stub run-hooks` runs the two argvs from inside the fixture, so each canary is seen to fire.
- **AC2** — When the same run's order `update-offer-<release>.md` is read off the pushed branch by `git
  -C <remote> show`, it holds the exact line for `legacy_ledger.py seed --all` and for
  `core.py adopt declarations`, each at the target's prefix; and under `--plant no-memory-tree` the
  `test.seed` line is gone and one note names the unclaimed kit.
  Red when: an order omits a hook, or names a path the adopter's prefix does not hold.
- **AC3** — When `python offer.py --fixture --plant order-shape` renders a step's order and a hook's
  order through `write_attended_order` and `render_attended_order`, both open with the same heading
  and differ only in `kind`, `argv` and `why`.
  Red when: a second writer spells its own shape.
- **AC4** — When `python tools/run-gates/check-receipt.py <tree>` runs over a fixture tree holding one
  `hole` row with its file, one row with its file gone, one row with `state` `applied` and two
  `update-rollback-*.md` no row names, it prints `orders: 1 open · 1 discharged · 1 absent · 2 unrecorded`
  and one line per open or unrecorded order, and its exit status is unchanged by them.
  Red when: a state is miscounted, or the line is absent on a green tree.
  fixture: built by `python offer.py --fixture --plant orders-graded`.
- **AC5** — When the same command runs over a tree with no outbox it prints `orders: no outbox`; over one
  whose `orders` is empty, `orders: none`.
  Red when: the two read alike, which is an empty population read as coverage.
- **AC6** — When `--plant orders-malformed` plants a row with no `path`, the same command exits 1 naming
  it.
  Red when: a row the grader cannot read counts as `open`.
- **AC7** — When `python adopter_reading.py --fixture --plant orders-open` reads a remote whose committed
  receipt holds two open rows, the `adopters` record's `orders_open` is `2`.
  Red when: the field is absent, or counts a `state` `applied` row.
- **AC8** — When `grep -c test.seed offers.md` runs from the `help` directory it prints at least `1`.
  Red when: the page does not state what the offer leaves undone.

## 7. Gates

`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `policy fixtures` · `receipt sync (installed files match the receipt)` · `memory hygiene`

New arm: tools/run-gates/check-receipt.py · covers AC4 AC5 AC6 · `check_fixtures` gains the orders trees, its failing case a tree with no outbox read as `orders: none` · none
New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the hook canaries and the shape compare through `offer.py --fixture`, its failing case `--stub run-hooks` · none

## 8. Open questions

- **F1 — Does an open order red?** `gap-deploy-05` says "graded by nothing", and an adopter holds 16.
  Options: (a) report only, in the adopter's bar and on gov's `adopters` record; (b) red on any open
  order; (c) red past an age. (b) reds every adopter's landing on the day the kit lands, the failure
  `tools/run-gates/check-receipt.py`'s docstring declines for the `evidence` state, and it blocks a
  landing on an order the operator may have read and declined. (c) sets a bound no record gives. Each
  value of a new policy key would be a new public surface for a rule no clause asks. RESOLVED (agent,
  2026-10-30, delegated): (a), rung 3. A grade is a state per order, visible on both sides. widens: none · relaxes: none
- **F2 — Do `update`'s own orders join the receipt?** Options: (a) the grader joins the listing, marking
  them `unrecorded`; (b) `update` writes a row for each. (b) makes `cmd_check`'s existing arm
  (`tools/govkit/govkit.py:5656`) red on any such file an operator deleted after handling it, and on
  every clone of an untracked outbox. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, smallest
  change that names every order. widens: none · relaxes: none
- **F3 — Which `adopt` verb does an update's order name?** The clause says `adopt`; `adopt.census` runs
  "once in a repository" (`flow-steps.md:712`). RESOLVED (agent, 2026-10-30, delegated): `adopt
  declarations` at update and `adopt census` at install, rung 1, flow-steps' `[adopt]` rows and
  layer-expansions:461. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, from the packet's Items 20, layer-expansions:460, `gap-deploy-05`,
  scout D's unit 20 row and the brief's I17 and I18.

## 10. Reuse audit

The seams extended are `render_order_slug` (`tools/govkit/govkit.py:5735`) for the file name, the
receipt's `orders` list (written at `:7984`, `:8396`, read at `:5653`), `write_attended_order`
(TOOL-dSafePassage-2 S5), and `tools/run-gates/check-receipt.py`, the one receipt reader an adopter
holds. `python tools/codebase-map/reuse_lookup.py "outbox order written for the adopter to run itself"`
ranked name-stem helpers (`run`, `adopt`, `run_git`) and no order writer, because the order writers are
inline `write_text` calls in `_cmd_update`; the seam comes from reading source, which agrees with scout
D. The scout's "orders, but none naming a hook run" holds. Recall surfaced `gap-deploy-05`'s register
row and the debt-fold review's finding 11, which counted `adopt` and `test.seed` as a kind the offer's
list missed.

Recall terms used: `python tools/memory-recall/query.py "what target-side code does govkit update run and how is an unattended offer isolated" --terms "govkit update target-side code seven kinds GOVKIT_RERENDER outbox order hooksPath throwaway clone credential"`
