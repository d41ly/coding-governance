# KICK-dKeptSession-26 — the card showing the build's remaining rework budget beside its pointers

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 10 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0163@709e57f9 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md) | research | KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-17 KICK-dKeptSession-18 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 |

<!-- /gen:spec-records -->

## 1. Goal

Every way a build repeats draws on one rework budget per build (P39, v2:1068-1073), and
TOOL-dDeclaredLoop-30 keeps that budget on the build's transition record and answers its state with
`budget_state`, but a session never sees it: its §3 hands the card line to this build in so many
words, "the remaining budget on the card is dKeptSession's render of this record". This unit puts a
`budget —` line in the card's `## pointers` section, beside the pointers KICK-dKeptSession-13 writes,
and makes a card that omits it fail the card check, seen red on a planted card that omits it.

## 2. Scope (IN)

- **S1** — The line. `render_pointers` (KICK-dKeptSession-13 S2) prints `budget — <answer>` after its
  `item —` line, `<answer>` the one line `python <loop kit>/budget.py state --build <slug>` prints,
  which is `budget_state`'s answer as TOOL-dDeclaredLoop-30 §4 spells it: `open <spent>/<total>`,
  `spent`, or `unfrozen <spent>/<base>`. The loop kit is resolved as an optional sibling of the
  kickoff engine, as `read_card_policy` resolves the policy kit (TOOL-dPlacedRequest-2 S11). With no
  loop kit it prints `budget — skipped: no loop kit`, and a call that fails or does not answer within
  `CARD_BUDGET_BOUND = 10` seconds prints `budget — skipped: <why>`. Observed by AC1, AC3.
- **S2** — The check. `budget` is appended to KICK-dKeptSession-13's `POINTER_LINES`, so
  `check_card_pointers` fails `--card --check` on a stored card whose `## pointers` section carries no
  `budget —` line, naming it. A `skipped` line is a line, so a node with no loop kit still passes.
  Observed by AC2.
- **S3** — The refresh. The line is re-derived wherever the section is: at each item boundary
  `card.pointers` admits and at each transition, so a draw shows at the next boundary or transition
  after it lands. Observed by AC4.
- **S4** — The plants `budget-open`, `budget-spent`, `budget-unfrozen`, `budget-omitted` and
  `budget-no-kit` in `skills/session-kickoff/card-store.fixture.sh`, the loop kit a stub answering
  the planted line. Observed by AC1 to AC4.
- **S5** — `help/orientation-card.md`'s pointers section (KICK-dKeptSession-13 S10) gains the
  `budget —` line, its three answers, and that only the owner raises the budget. Observed by AC5.

## 3. Non-goals (OUT)

- The budget, its freeze, its draws, its homes and `budget_state` itself: TOOL-dDeclaredLoop-30, -48
  and -49's.
- What a build does once its budget is spent: TOOL-dDeclaredLoop-31's `flow.on-exhausted`.
- The `## pointers` section, its write and its check: KICK-dKeptSession-13's; this unit adds one line
  and one word.
- The `state` subcommand of `budget.py`: dDeclaredLoop's module; §8 F2 files the ask.

### Edges

- **consumes-from** `KICK-dKeptSession-13` — `## pointers`, the section this line joins below `item —`, with `POINTER_LINES` and `check_card_pointers`, which grade it; without them the line has no home and no check
- **consumes-from** external — dDeclaredLoop's `budget_state` in `tools/loop/budget.py` (TOOL-dDeclaredLoop-30 §4, read across every home by TOOL-dDeclaredLoop-48 S4), reached through a `state` subcommand its spec does not yet name (§8 F2)

## 4. Design

### The line

```
## pointers
records — journal memory/builds/dX/build/2026-10-27-build-KICK-dX-1-agent-ledger.md
forks — none
item — item.build.pass@1#3f9c2a71 · at 8c1e0b42
budget — open 3/10
```

| `budget_state` | Line |
|---|---|
| `open 3/10` | `budget — open 3/10` |
| `spent` | `budget — spent` |
| `unfrozen 1/4` | `budget — unfrozen 1/4` |
| no loop kit | `budget — skipped: no loop kit` |
| a failed or slow call | `budget — skipped: budget.py state exited <rc>` or `… did not answer within 10s` |

The answer is printed as the module prints it, never re-derived here: the card shows the record's own
reading, so it can never disagree with the reader the draw sites use.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `render_budget_line` | shell function, `manifest-check.sh` | `sh.function`, asked at the pass |
| `CARD_BUDGET_BOUND` | constant | none declared |
| `budget —` | card line | none |
| the five plants of S4 | fixture cases | none |

### Migration

A `## pointers` section stored before this unit lands has no `budget —` line, so `--card --check`
names it until the section is next rendered, at the next item boundary or transition; the check's
line names the remedy, `--card --pointers --build <slug>`, which renders it at once.

### Rollout

Live at landing. Until dDeclaredLoop builds the `state` subcommand the line reads
`budget — skipped: budget.py state exited 2`, and the check still passes.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`: `render_budget_line`, the `POINTER_LINES` word
- `skills/session-kickoff/manifest-check.test.sh`: the arm the §7 line declares
- `skills/session-kickoff/card-store.fixture.sh`: S4's plants
- `help/orientation-card.md`: S5's line

### Alternatives rejected

- **The budget computed in the card writer** from the transition records. A second reader of the
  draw rows would be a second answer to `budget_state`'s question, and TOOL-dDeclaredLoop-48 already
  moves those rows across four homes.
- **A card check over the whole card.** Only the pointers section carries the line, so the check is
  the section's.

## 5. Production-readiness checklist

- security — the line carries the module's one-line answer, held to `budget — ` plus at most one
  line of printable text before it is written.
- perf / scale — one bounded call per pointers render.
- error / empty / loading states — every failure is a `skipped` line naming why; the card is still
  written.
- observability — the line itself.
- risks — a stub or absent loop kit hides the budget behind `skipped`; the help page says so.
- testing — S4's plants, red and green.
- migration — none.
- user docs — `help/orientation-card.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `bash card-store.fixture.sh --plant budget-open` writes the pointers with a stub
  loop kit answering `open 3/10`, the published card's `## pointers` section carries `budget — open
  3/10` directly after its `item —` line; the plants `budget-spent` and `budget-unfrozen` print
  `budget — spent` and `budget — unfrozen 1/4`.
  Red when: the line is absent, re-worded, or placed outside the section.
- **AC2** — When the plant `budget-omitted` deletes the `budget —` line from a stored card,
  `bash skills/session-kickoff/manifest-check.sh --card --check --session <sid>` exits 1 naming
  `budget —`; on the card as written it exits 0.
  Red when: a planted card that omits the budget passes the check.
- **AC3** — When the plant `budget-no-kit` writes the pointers with no loop kit resolvable, the line
  reads `budget — skipped: no loop kit` and `--card --check` exits 0.
  Red when: a missing kit refuses the card, or prints no line.
- **AC4** — When the plant `budget-open` records a draw through the stub between two item boundaries,
  the second boundary's card reads `budget — open 4/10`.
  Red when: a boundary re-renders the section with the earlier figure.
- **AC5** — When `grep -n "budget —" orientation-card.md` runs over the help page, it finds S5's line
  naming `open`, `spent` and `unfrozen`.
  Red when: the page does not name the line.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC2 · the budget line over a stub loop kit, the failing case a stored card whose `## pointers` lacks `budget —` passing `--card --check` · none

## 8. Open questions

- **F1 — Which check reds a card that omits the budget?** Options: (a) KICK-dKeptSession-13's
  `check_card_pointers` under `--card --check`, by one word in `POINTER_LINES`; (b) a check of this
  unit's own over the whole card. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, by the
  tie-break: reuse of the section's one check, where (b) would be a second reader of the same
  section. widens: none · relaxes: none
- **F2 — `budget_state` is a function of `tools/loop/budget.py`, and TOOL-dDeclaredLoop-30 names
  only the `draw` and `--fixture` entry points; how does a shell card writer read it?** The parent
  spec is never edited here. RESOLVED (agent, 2026-10-26, delegated): this unit calls `budget.py
  state --build <slug>` and an ask goes to dDeclaredLoop, which TOOL-dDeclaredLoop-31 S3's shell verb
  `--exhausted` needs too. Ask for dDeclaredLoop, target build dDeclaredLoop: accept
  `tools/loop/budget.py` carries a `state --build <slug>` subcommand printing `budget_state`'s one
  line, exit 0, with a fixture case per answer. Until it lands, S1's `skipped` line stands in.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 26, P39 (v2:1068-1073),
  TOOL-dDeclaredLoop-30 §3 and §4, and scout C's row for this unit.

## 10. Reuse audit

The seam extended is KICK-dKeptSession-13's `## pointers` section and its `check_card_pointers`,
read through `POINTER_LINES`; the line's value is TOOL-dDeclaredLoop-30's `budget_state`, its §4
answer table read at `origin/main`'s re-grounded bytes, and its homes TOOL-dDeclaredLoop-48 S4's.
`python tools/codebase-map/reuse_lookup.py "render the remaining rework budget on the orientation card"`
ranked name stems (`render`, `render_cards_md` in `tools/codebase-map/map_lib.py`, `render_line` in
`tools/runlog/runlog_lib.py`); none renders a budget, and the loop kit is not on this tree's map at
base, so no existing seam fits the line and it joins the section KICK-dKeptSession-13 adds. Scout C's
row agrees with the parent spec: `budget_state` is specced, the card line is not. The recall query
returned scout C's row and TOOL-dPlacedRequest-14's scout row, which concerns the intake's budget and
not this one.

Recall terms used: `python tools/memory-recall/query.py "where is the remaining rework budget shown to a session" --terms "rework budget budget_state flow.rework-budget card pointers remaining budget P39 orientation card"`
